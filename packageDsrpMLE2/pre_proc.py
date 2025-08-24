import pandas as pd
import uuid
from loguru import logger
from pathlib import Path
from loguru import logger
from packageDsrpMLE2.config import CSV_FILE, PARQUET_PATH

class PreProcessor:
    def __init__(self, path_raw_data: Path = CSV_FILE) -> None:
        self.path_raw_data = path_raw_data
        self.feature_table = None
        self.raw_data = None
        self.processed_data = None

    def read_dataset(self) -> None:
        self.raw_data = pd.read_csv(self.path_raw_data, parse_dates=[0], index_col=[0])
        
        
    def order_dataset(self) -> None:
        self.processed_data = self.raw_data.sort_index()
    
    def remove_duplicates(self) -> None:
        if self.processed_data.index.duplicated().any():
            self.processed_data = self.processed_data.groupby(level=0).mean().sort_index()

    def interpolate(self) -> None:
        self.processed_data = self.processed_data.asfreq("h")
        value_column = self.processed_data.columns[0]
        self.processed_data[value_column] = self.processed_data[value_column].interpolate()

    def run(self) -> None:

        logger.info(f"Inicializando Pre-Procesamiento de raw data")
        logger.info(f"Leendo dataset {self.path_raw_data} ")
        self.read_dataset()
        logger.info(f"Ordenando dataset por la columna tiempo")
        self.order_dataset()
        logger.info(f"Reemplazando valores duplicados por su media")
        self.remove_duplicates()
        logger.info(f"Interpolando valores faltantes")
        self.interpolate()

        logger.info(f"Preprocesamiento finalizado...")

  
        logger.info(f"Agregando columna ernergy_id al dateset / adecuando para feast")

        self.feature_table = self.processed_data.copy().reset_index()

        self.feature_table["energy_id"] = [str(uuid.uuid4()) for _ in range(self.feature_table.shape[0])]        

        #self.feature_table["event_timestamp"] = self.feature_table["Datetime"]

        self.feature_table.to_parquet(PARQUET_PATH, index=False)

        logger.info(f"parquet final guardado en {PARQUET_PATH}")


if __name__ == "__main__":
    data = PreProcessor()
    data.run()
    print(data.feature_table)