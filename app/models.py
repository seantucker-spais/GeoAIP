from sqlalchemy import Column, Integer, String, Float
from .database import Base

class GeoData(Base):
    __tablename__ = "geodata"

    id = Column(Integer, primary_key=True, index=True)
    record_id = Column(String, unique=True, index=True)
    timestamp = Column(String)
    source = Column(String)
    lat = Column(Float)
    long = Column(Float)
    alt = Column(Float)
    spatial_ref = Column(String)
    vector = Column(String)  # Store as JSON or similar
    geom_type = Column(String)
    bbox = Column(String)  # Store as JSON or similar
    area = Column(Float)
    length = Column(Float)
    elevation = Column(Float)
    slope = Column(Float)
    aspect = Column(Float)
    land_cover = Column(String)
    population_density = Column(Float)
    start_time = Column(String)
    end_time = Column(String)
    temporal_resolution = Column(String)
    model_name = Column(String)
    confidence_score = Column(Float)
    classification = Column(String)
    tags = Column(String)  # Store as JSON or similar
