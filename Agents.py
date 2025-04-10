import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal, UserInteraction

def analyze_behavior(user_id: int):
    db: Session = SessionLocal()
    interactions = db.query(UserInteraction).filter(UserInteraction.user_id == user_id).all()
    df = pd.DataFrame([{
        'product_id': i.product_id,
        'interaction_type': i.interaction_type,
        'timestamp': i.timestamp
    } for i in interactions])
    db.close()
    # Analyze behavior patterns here
    return df
