import pandas as pd
from feast import (
    Entity,
    FeatureView,
    FileSource,
    Field,
    RequestSource,
    FeatureService,
 )

from feast.types import String, Float64
from feast.on_demand_feature_view import on_demand_feature_view 

# 1)Entidad
energy_consumption = Entity(name="energy_consumption", join_keys=["energy_consumption_id"])


# 2) Origen de datos
energy_consumption_source = FileSource(
    name="energy_consumption_source",
    path="./data/ec_ft.parquet",
    event_timestamp_column="Datetime",
)

# 3) Vista de características
energy_consumption_view = FeatureView(
    name="energy_consumption_view",
    entities=[energy_consumption],
    schema=[
        Field(name="PJME_MW", dtype=Float64, description="This is a energy consumption"),
    ],
    source=energy_consumption_source,
)

"""
# 4) RequestSource renombrado para no colisionar
input_req = RequestSource(
    name="input_request",
    schema=[
        Field(name="y", dtype=Float64),
    ],
)
"""

# 5) On‑demand feature view con nombre y firma corregida
@on_demand_feature_view(
    name="ec_feature_view",
    sources=[energy_consumption_view],
    schema=[
        Field(name="y", dtype=Float64),
    ],
)
def ec_feature_view(input_df: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame()
    df["y"] = input_df["PJME_MW"] / 1000    
    return df

dsrp_feature_service = FeatureService(
    name="dsrp_feature_service",
    features=[energy_consumption_view, ec_feature_view],
    )
