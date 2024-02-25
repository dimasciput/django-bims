# coding=utf8
import math
import psycopg2

from django.conf import settings
from django.http import HttpResponse

from rest_framework.views import APIView


def tile2lonlat(x_tile, y_tile, zoom):
    """
    Converts tile coordinates to the corresponding
    longitude and latitude values.
    """
    n = 2.0 ** zoom
    lon_deg = x_tile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y_tile / n)))
    lat_deg = math.degrees(lat_rad)
    return lon_deg, lat_deg


def calculate_tile_bounds(x, y, z):
    """
    Calculates the bounding box for a t ile given x, y, and z (zoom level).
    """
    min_lon, max_lat = tile2lonlat(x, y, z)
    max_lon, min_lat = tile2lonlat(x + 1, y + 1, z)
    return min_lon, min_lat, max_lon, max_lat


class LocationSiteTileApiView(APIView):
    """

    """

    def get(self, request, x, y, z):
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = conn.cursor()

        minLon, minLat, maxLon, maxLat = calculate_tile_bounds(x, y, z)

        sql = """
        SELECT ST_AsMVT(q, 'default_fbis_location_site_cluster', 4096, 'geometry_point')
        FROM (
          SELECT
            site_id,
            name,
            ecosystem_type,
            ST_AsMVTGeom(
              geometry_point,
              ST_MakeEnvelope(%s, %s, %s, %s, 4326),
              4096,
              256,
              true
            ) AS geometry_point
          FROM default_fbis_location_site_cluster
          WHERE ST_Intersects(geometry_point, ST_MakeEnvelope(%s, %s, %s, %s, 4326))
        ) AS q;
        """

        cursor.execute(sql,
                       [minLon, minLat, maxLon, maxLat, minLon, minLat, maxLon, maxLat])
        tile = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return HttpResponse(tile, content_type="application/vnd.mapbox-vector-tile")
