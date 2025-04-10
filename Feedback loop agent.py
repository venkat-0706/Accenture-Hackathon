from sqlalchemy.orm import Session
from database import SessionLocal, UserInteraction

def log_feedback(user_id: int, product_id: int, feedback: str):
    db: Session = SessionLocal()
    interaction = UserInteraction(user_id=user_id, product_id=product_id, interaction_type=feedback, timestamp='2025-04-10')
    db.add(interaction)
    db.commit()
    db.close()
