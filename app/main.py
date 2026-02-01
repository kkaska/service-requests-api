from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

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
def get_service_request(request_id: int):
    db: Session = SessionLocal()
    try:
        service_request = (
            db.query(ServiceRequest)
            .filter(ServiceRequest.id == request_id)
            .first()
        )

        if not service_request:
            raise HTTPException(status_code=404, detail="Service request not found")

        return {
            "id": service_request.id,
            "description": service_request.description,
            "customer_id": service_request.customer_id,
        }
    finally:
        db.close()