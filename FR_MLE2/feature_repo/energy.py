import pandas as pd
import sys

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2])) 
from packageDsrpMLE2.config import PARQUET_PATH


from feast import (
    Entity,
    FeatureView,
    FileSource,
    Field,
    FeatureService,
 )

from feast.types import String, Float64, UnixTimestamp
from feast.on_demand_feature_view import on_demand_feature_view 

# 1)Entidad
energy = Entity(name="energy", join_keys=["energy_id"])

# 2) Origen de datos
energy_source = FileSource(
    name="energy_source",
    path=str(PARQUET_PATH),
    event_timestamp_column="Datetime",
)

# 3) Vista de características
energy_view = FeatureView(
    name="energy_view",
    entities=[energy],
    schema=[
        Field(name="PJME_MW", dtype=Float64, description="This is a energy consumption"),
        Field(name="Datetime", dtype=UnixTimestamp),
    ],
    source=energy_source,
)

# 5) On‑demand feature view con nombre y firma corregida
@on_demand_feature_view(
    name="energy_feature_view",
    sources=[energy_view],
    schema=[
        Field(name="y", dtype=Float64),
        Field(name="ds", dtype=UnixTimestamp),
    ],
)
def energy_feature_view(input_df: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame()
    df["y"] = input_df["PJME_MW"] / 1000.0
    df["ds"] = input_df["Datetime"]
    return df

dsrp_feature_service = FeatureService(
    name="dsrp_feature_service",
    features=[energy_view, energy_feature_view],
    )
