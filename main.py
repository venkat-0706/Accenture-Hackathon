from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from agents.behavior_analysis_agent import analyze_behavior
from agents.recommendation_engine_agent import recommend_products
from agents.feedback_loop_agent import log_feedback
from agents.promotion_agent import apply_promotions

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/recommendations
::contentReference[oaicite:0]{index=0}
 
