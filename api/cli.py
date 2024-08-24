import click
from geo_aip import GeoAIP

@click.group()
def cli():
    pass

@cli.command()
@click.option('--file', required=True, type=str, help='Path to data file')
def ingest(file):
    api = GeoAIP()
    api.ingest_data(file)

@cli.command()
@click.option('--lat', required=True, type=float, help='Latitude')
@click.option('--long', required=True, type=float, help='Longitude')
def query(lat, long):
    api = GeoAIP()
    result = api.query_data(lat, long)
    print(result)

if __name__ == '__main__':
    cli()
