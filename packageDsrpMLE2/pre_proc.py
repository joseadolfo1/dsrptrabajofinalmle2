import pandas as pd
import uuid
from loguru import logger

class PreProcessor:
    def __init__(self, path_raw_data: str) -> None:
        self.path_raw_data = path_raw_data
        self.feature_table = None

    def read_dataset(self) -> None:
        self.feature_table = pd.read_csv(self.path_raw_data, parse_dates=[0])
        print("---------------INFO----------------")
        print(self.feature_table.info())
        print("\n---------------DESCRIBE----------------")
        print(self.feature_table.describe())
        
        
    def order_dataset(self) -> None:
        time_col = self.feature_table.columns[0]
        self.feature_table = self.feature_table.sort_values(time_col)
    
    def remove_duplicates(self) -> None:
        if self.feature_table.index.duplicated().any():
            self.feature_table = self.feature_table.groupby(level=0).mean().sort_index()

    def interpolate(self) -> None:
        self.feature_table = self.feature_table.asfreq("h")
        value_column = self.feature_table.columns[1]
        self.feature_table[value_column] = self.feature_table[value_column].interpolate()

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

        print("---------------INFO----------------")
        print(self.feature_table.info())
        print("\n---------------DESCRIBE----------------")
        print(self.feature_table.describe())

        logger.info(f"Agregando columna ernergy_id al dateset")
        
        self.feature_table["energy_id"] = [str(uuid.uuid4()) for _ in range(self.feature_table.shape[0])]        
       
        return self.feature_table

    def write_feature_table(self, filepath: str) -> None:      
        if self.feature_table is not None:
            self.feature_table.to_parquet(filepath, index=False)
        else:
            raise Exception("La feature table no ha sido creada. Ejecutar el comando .run()")
       