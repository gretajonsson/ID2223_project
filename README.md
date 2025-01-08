# ID2223_project
Project for the course ID2223 at KTH Autumn 2024. Project results can be shown here:
https://gretajonsson.github.io/ID2223_project/

# Real-Time Traffic Accident Predictor

This project aims to predict the likelihood of traffic accidents using real-time weather and accident data. By combining data from the Swedish Police API (Polisen), Open Meteo, and utilizing Hopsworks for feature storage and orchestration, the model provides insights several days in advance to help drivers make informed decisions about road safety. Additionally, GitHub Actions is used for automating workflows, and the results are published using GitHub Pages for easy access and visualization.

---

## Project Structure

```
ID2223_PROJECT/
│
├── .github/workflows/
│   └── main.yml                  # CI/CD workflow configuration
│   └── page_update.yml           # Builds page agian
│
├── data/
│   ├── aqi-api-key.txt           # API key for AQI data (if applicable)
│   ├── forecast_table.png        # Snapshot of forecast data
│   ├── forecast.png              # Example forecast visualization
│   ├── header.png                # Example header visualization
│   ├── hopsworks-api-key.txt     # API key for Hopsworks integration
│   ├── kommuner.json             # Geo-data for Swedish municipalities
│   └── police_api_backfill.csv   # Historical accident data
│
├── project/
│   ├── accidents_model/          # Model-related files
│   │   ├── images/               # Images for model visualizations
│   │   └── model.json            # Model configuration
│   ├── functions/                # Reusable functions
│   │   └── util.py               # Utility functions
│   └── __pycache__/              # Cached files (auto-generated)
│
├── batch_inference.ipynb         # Notebook for batch predictions
├── data_retrival.ipynb           # Notebook for retrieving data from APIs
├── feature_backfill.ipynb        # Notebook for uploading backfills
├── feature_pipeline.ipynb        # Notebook for creating feature pipelines
├── training_pipeline.ipynb       # Notebook for model training pipeline
├── update_police_api_backfill.ipynb  # Notebook to update police API backfill
│
├── .cache.sqlite                 # Local cache file
├── .gitattributes                # Git configuration
├── .gitignore                    # Git ignored files
├── index.html                    # Front-end visualization (if applicable)
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gretajonsson/ID2223_PROJECT.git
   cd ID2223_PROJECT
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate 
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run the Code

1. **Set up API keys:**
   - Place your API keys for Polisen and Open Meteo in the `data/` folder (e.g., `hopsworks-api-key.txt`, `aqi-api-key.txt`).

2. **Run the notebooks in order:**
   - Start by executing `data_retrival.ipynb` to fetch data.
   - Upload the data to hopsworks using `feature_backfill.ipynb`
   - Process the data using `feature_pipeline.ipynb`.
   - Train the model by running `training_pipeline.ipynb`.
   - Generate predictions using `batch_inference.ipynb`.

3. **Update backfill data (optional):**
   - Use `update_police_api_backfill.ipynb` if new historical data needs to be added.

4. **Visualize the results:**
   - Open the `index.html` file to view the front-end visualization (if applicable).

---

## Usage

### Data Retrieval
- Use `data_retrival.ipynb` to fetch data from the APIs (Polisen, Open Meteo).

### Feature Engineering
- Run `feature_backfill.ipynb` to upload the data to hopsworks.
- Run `feature_pipeline.ipynb` to generate engineered features from raw data.

### Model Training
- Use `training_pipeline.ipynb` to train the XGBoost regression model.

### Inference
- Perform batch predictions with `batch_inference.ipynb`.

---

## Key Features

- **Weather-Based Prediction**: Incorporates weather factors like temperature, precipitation, and wind speed.
- **APIs**: Real-time data fetched from Polisen and Open Meteo APIs.
- **Modular Code**: Organized pipelines for data retrieval, feature engineering, training, and inference.

---