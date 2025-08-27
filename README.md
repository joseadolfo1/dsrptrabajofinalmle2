# DsrpTrabajoFinalMLE2

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Este es el trabajo final del modulo MLE2 del programa de epecializado en Machine Learning Engineer

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         packageDsrpMLE2 and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── packageDsrpMLE2   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes packageDsrpMLE2 a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

##  Problema de ML
Se busca predecir el consumo energetico de la empresa PJM Interconnection LLC. Empresa de energis de USA.

## Diagrama de flujo del proyecto
![Diagrama de Flujo](./reports/figures/DF_MLE2.png)

## Diccionario de datos

|  cabecera      |tipo         | descripcion |
|----------------|-------------|-------------|
|**Datetime**  |timestamp      |marca de tiempo con una granularidad de 1h|
|**PJME_MW**  |float      |consumo energetico en Megawatts (MW)|

# Model Card

## Metadata

- **Library**: scikit-learn, feast, prophet, statsmodels, xgboost, ExponentialSmoothing
- **Tags**: # Serie Temporal

## Authors

- José Adolfo Cusihuallpa

## Framework

scikit-learn, JupiterLab, Feast

## Intended Uses

El trabajo pretende hacer la prediccion del consumo electrico de la empresa PJM.

## Model Description

Se entrenan los modelos Prophet, ExponentialSmoothing (ETS) y XGBRegressor

## Visualización del dataset

![dataset](./reports/figures/dataset_pre_feast.png)


## Resultados
Comparacion de la metrica RMSE de los modelos.

Resultado en Dagshub/MLFlow: https://dagshub.com/joseadolfo1/dsrptrabajofinalmle2/experiments

![RMSE](./reports/figures/RMSE.png)



## Conclusiones

De los resultados obtenidos el modelo con mejores metricas resulta ser el XGBOOST, sin embargo, cuanto menos esto nos lleva a levantar una ceja ya que es posible que se haya presentado un data leakage en el modelo por la precision de sus predicciones.
