## Introduction
This project analyzes LA crime data in 2024 through a structured data science workflow. The dataset source, format, and update frequency are documented in the data section of the repo. Data retrieval was performed via API/Web scraping, followed by data cleaning and transformation into tidy tabular format using scripts located in data_cleaning.ipynb.

To ensure data quality, we applied validation checks including row count verification and missing value tests (e.g., pytest assertions). We also enriched the raw dataset with additional variables to enhance analysis. Key summary statistics are presented in the exploratory analysis notebook, and 4–6 informative visualizations illustrate patterns and trends in the data.

The project includes one interactive widget to enhance user experience, embedded using Quarto Jupyter cell embedding.

Finally, a clean Git commit history with meaningful messages is included, showing individual contributions and project evolution. You can find the Git graph and author metadata in the git_history directory or rendered below.

## Project summary

This project summary can be found:

- as a website:

https://moran-teaching.github.io/project-group/

## Accessing data

Our raw data can be downloaded here:  
https://catalog.data.gov/dataset/crime-data-from-2020-to-present

Our processed data can be downloaded here:  
Our processed dataset is available in three formats—CSV, Excel, and Parquet.  
https://drive.google.com/drive/folders/1om-bKXm8b6cKOUIy6SSwtixhuxgh9OIi?usp=sharing

## Python scripts / notebooks

The following scripts/notebooks were used produce the summary: 

All key files are located in the root directory of the repository:
- `data_cleaning.ipynb`: Handles missing values, filters and standardizes raw crime data.
- `data_enrichment.ipynb`: Merges external data sources for richer feature context.
- `data_analysis.ipynb`: Performs exploratory data analysis.
- `data_analysis_modeling.ipynb`: Builds and evaluates classification models to predict crime severity.
- `index.ipynb`: Quarto homepage notebook. Contains the final narrative, conclusions, and embedded visuals for the published website.
- `test_data_cleaning.py`: Unit test script to validate cleaning functions and data consistency.

## Reproducibility

- `environment.yml`: Defines the project’s Python environment and dependencies.


