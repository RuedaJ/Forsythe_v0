
from indicators.base import BaseIndicator
import geopandas as gpd

class MASWZoneIndicator(BaseIndicator):
    def extract(self, gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        # Add a label for MASW line-based zones
        gdf["survey_type"] = "MASW"
        return gdf
