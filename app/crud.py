from sqlalchemy.orm import Session
from . import models, schemas

def create_record(db: Session, geo_data: schemas.GeoData):
    db_record = models.GeoData(**geo_data.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
