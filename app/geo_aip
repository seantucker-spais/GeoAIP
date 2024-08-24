import json

class GeoAIP:
    def __init__(self):
        # Initialization code, if needed
        pass

    def ingest_data(self, filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
        # Process and store data as needed
        print(f"Data ingested from {filepath}")
        return data

    def query_data(self, lat, long):
        # Implement query logic here
        result = {"lat": lat, "long": long, "message": "Query successful"}
        print(f"Query Result: {result}")
        return result
