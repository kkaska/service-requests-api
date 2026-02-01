from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db import SessionLocal
from app.models import ServiceRequest

app = FastAPI(title="Service Requests API")

@app.get("/")
def root():
    return {"message": "Service Requests API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/service-requests/{request_id}")
# Would need to add authentication in a production scenario
def get_service_request(request_id: int):
    db = SessionLocal()
    try:
        result = db.execute(
            # Join customer details with service request
            # Would likely be split it into seperate endpoint for customer details to comply with GDPR etc in production
            text("""
                SELECT
                    sr.id,
                    sr.description,
                    sr.status,
                    sr.created_at,
                    c.first_name,
                    c.last_name,
                    c.email,
                    c.phone,
                    c.address
                FROM service_requests sr
                JOIN customers c ON sr.customer_id = c.id
                WHERE sr.id = :request_id
            """),
            {"request_id": request_id}
        ).mappings().first()

        if not result:
            raise HTTPException(status_code=404, detail="Service request not found")

        return dict(result)
    finally:
        db.close()