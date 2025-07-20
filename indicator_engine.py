
from indicators.cpt_density import CPTDensityIndicator
from indicators.masw_zone import MASWZoneIndicator

def run_indicators(gdf, dataset_type):
    if dataset_type == "CPT":
        return CPTDensityIndicator().extract(gdf)
    elif dataset_type == "MASW":
        return MASWZoneIndicator().extract(gdf)
    else:
        return gdf
