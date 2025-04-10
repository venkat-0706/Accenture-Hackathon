import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy.orm import Session
from database import SessionLocal, UserInteraction, Product

def recommend_products(user_id: int):
    db: Session = SessionLocal()
    interactions = db.query(UserInteraction).all()
    products = db.query(Product).all()
    db.close()

    # Create user-product interaction matrix
    interaction_df = pd.DataFrame([{
        'user_id': i.user_id,
        'product_id': i.product_id,
        'interaction_type': i.interaction_type
    } for i in interactions])

    product_df = pd.DataFrame([{
        'product_id': p.id,
        'category': p.category,
        'price': p.price,
        'brand': p.brand
    } for p in products])

    # Pivot table to create user-item matrix
    user_item_matrix = interaction_df.pivot_table(index='user_id', columns='product_id', aggfunc='size', fill_value=0)

    # Compute similarity between products
    product_similarity = cosine_similarity(user_item_matrix.T)
    product_similarity_df = pd.DataFrame(product_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

    # Get products the user has interacted with
    user_interactions = user_item_matrix.loc[user_id]
    interacted_products = user_interactions[user_interactions > 0].index.tolist()

    # Recommend products based on similarity
    recommendations = pd.Series(dtype=float)
    for product in interacted_products:
        similar_products = product_similarity_df[product].sort_values(ascending=False)
        recommendations = recommendations.append(similar_products)

    recommendations = recommendations.groupby(recommendations.index).mean().sort_values(ascending=False)
    recommended_product_ids = recommendations.index.tolist()

    # Filter out already interacted products
    recommended_product_ids = [pid for pid in recommended_product_ids if pid not in interacted_products]

    # Get product details
    recommended_products = product_df[product_df['product_id'].isin(recommended_product_ids)].to_dict(orient='records')

    return recommended_products
