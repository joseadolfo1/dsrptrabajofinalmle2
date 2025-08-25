import pandas as pd
import uuid
from loguru import logger
from pathlib import Path
from loguru import logger
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from packageDsrpMLE2.config import CSV_FILE, PARQUET_PATH, FIGURES_DIR

def save_figure(figura, name:str, directorio=FIGURES_DIR) -> None:
        ruta = Path(directorio / name)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        logger.info(f"Guardando imagen {name} en ruta : {ruta}")
        figura.savefig(ruta, dpi=150, bbox_inches="tight")


class PreProcessor:
    def __init__(self, path_raw_data: Path = CSV_FILE) -> None:
        self.path_raw_data = path_raw_data
        self.feature_table = None
        self.raw_data = None
        self.processed_data = None

    def read_dataset(self) -> None:
        logger.info(f"Leendo dataset {self.path_raw_data} ")
        self.raw_data = pd.read_csv(self.path_raw_data, parse_dates=[0], index_col=[0])
        
        
    def order_dataset(self) -> None:
        logger.info(f"Ordenando dataset por la columna tiempo")
        self.processed_data = self.raw_data.sort_index()
    
    def remove_duplicates(self) -> None:
        logger.info(f"Reemplazando valores duplicados por su media")
        if self.processed_data.index.duplicated().any():
            self.processed_data = self.processed_data.groupby(level=0).mean().sort_index()

    def interpolate(self) -> None:
        logger.info(f"Interpolando valores faltantes")
        self.processed_data = self.processed_data.asfreq("h")
        value_column = self.processed_data.columns[0]
        self.processed_data[value_column] = self.processed_data[value_column].interpolate()    
    

    def run(self) -> None:

        logger.info(f"Inicializando Pre-Procesamiento de raw data")        
        self.read_dataset()
        
        self.order_dataset()
        
        self.remove_duplicates()
        
        self.interpolate()

        fig, ax = plt.subplots(figsize=(20, 5))
        sns.set_style("whitegrid")
        sns.set_palette("deep")
        value_column = self.processed_data.columns[0]
        sns.lineplot(data=self.processed_data, x=self.processed_data.index, y=value_column, ax=ax, linewidth=0.1, alpha=0.90)
        plt.tight_layout()
        save_figure(fig, name="dataset_pre_feast.png")

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