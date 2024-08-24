from pydantic import BaseModel
from typing import List, Optional

class GeoData(BaseModel):
    record_id: str
    timestamp: str
    source: str
    lat: float
    long: float
    alt: float
    spatial_ref: str
    vector: List[float]
    geom_type: Optional[str] = None
    bbox: Optional[List[float]] = None
    area: Optional[float] = None
    length: Optional[float] = None
    elevation: Optional[float] = None
    slope: Optional[float] = None
    aspect: Optional[float] = None
    land_cover: Optional[str] = None
    population_density: Optional[float] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    temporal_resolution: Optional[str] = None
    model_name: Optional[str] = None
    confidence_score: Optional[float] = None
    classification: Optional[str] = None
    tags: Optional[List[str]] = None
