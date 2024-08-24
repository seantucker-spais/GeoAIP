GeoAIP API
GeoAIP is an API designed for managing and querying geospatial data, aligning with the SpaIS1.0 schema. It supports data ingestion, querying, and management, tailored for GeoAI applications.

Features
Data Ingestion: Seamlessly ingest geospatial data into a structured format.
Data Querying: Perform spatial, temporal, and attribute-based queries.
64-Dimensional Vector Support: Optimized for complex geospatial data representation.
Technology Stack
Language: Python
Framework: FastAPI
Data Storage: Parquet files
Geospatial Tools: GeoPandas, PyArrow
Optional: SQLAlchemy for relational database integration
Installation
Prerequisites
Python 3.8+
pip
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/GeoAIP.git
cd GeoAIP
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the API:

bash
Copy code
uvicorn app.main:app --reload
Access API Documentation:

Go to http://127.0.0.1:8000/docs for interactive API documentation.
API Endpoints
Data Ingestion
POST /data/ingest
Description: Ingest new geospatial data.
Request Body: JSON conforming to the SpaIS1.0 schema.
Response: Confirmation of data ingestion.
Data Querying
GET /data/query
Description: Query geospatial data.
Query Parameters: Filter by lat, long, radius, tags, etc.
Response: JSON with matching records.
Schema Overview (SpaIS1.0)
record_id: Unique identifier for each record.
timestamp: Time of data collection.
source: Data source.
lat, long, alt: Geospatial coordinates.
vector: 32-dimensional vector representation.
geom_type, bbox: Geometry type and bounding box.
additional attributes: Include area, slope, aspect, etc.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Create a new Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or suggestions, please contact: info@spais.io
GeoAI For Parquet
