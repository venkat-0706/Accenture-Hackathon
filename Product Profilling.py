from sqlalchemy.orm import Session
from database import SessionLocal, Product

def get_product_profile(product_id: int):
    db: Session = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    db.close()
    return {
        'name': product.name,
        'category': product.category,
        'price': product.price,
        'brand': product.brand,
        'description': product.description
    }
