def apply_promotions(recommended_products):
    # Example: Apply a 10% discount to all recommended products
    for product in recommended_products:
        product['discounted_price'] = product['price'] * 0.9
    return recommended_products
