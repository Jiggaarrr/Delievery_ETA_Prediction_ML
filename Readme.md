# Delivery ETA Prediction API

A simple machine learning API that predicts the estimated delivery time for an order based on factors such as distance, traffic, weather, vehicle type, and order size.

The trained machine learning model is saved using Joblib and served through a **FastAPI** application. The API accepts order details and returns the predicted delivery time in minutes.

## What this project does

The API takes the following inputs:

- **Distance** — distance of the delivery in kilometers
- **Traffic** — traffic condition
- **Weather** — weather condition
- **Vehicle** — vehicle used for delivery
- **Order Size** — number/size of items in the order

It then passes these values to the trained model and returns the estimated delivery time.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- FastAPI
- Uvicorn
- Docker

## Project Structure

```text
delivery-eta-prediction/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── delivery_eta_model.pkl
├── delivery_eta_prediction.csv
└── Delivery_ETA_Code_File.ipynb
```

## API Endpoints

### `GET /`

A simple endpoint to check whether the API is running.

Example response:

```json
{
  "message": "Delivery ETA Prediction API"
}
```

### `POST /predict`

Predicts the estimated delivery time for an order.

The endpoint accepts:

| Input | Type | Description |
|---|---|---|
| `Distance_km` | float | Delivery distance in kilometers |
| `Traffic` | string | Traffic condition |
| `Weather` | string | Weather condition |
| `Vehicle` | string | Delivery vehicle |
| `Order_Size` | integer | Size of the order |

Example response:

```json
{
  "predicted_delivery_time_minutes": 42.5
}
```

The prediction is returned in minutes and rounded to two decimal places.

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/delivery-eta-prediction.git
cd delivery-eta-prediction
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the API

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger UI to test the `/predict` endpoint directly from your browser.

## Running with Docker

Build the Docker image:

```bash
docker build -t delivery-eta-api .
```

Run the container:

```bash
docker run -p 8000:8000 delivery-eta-api
```

Then open:

```text
http://localhost:8000/docs
```

## Model

The trained model is stored in:

```text
delivery_eta_model.pkl
```

The FastAPI application loads this model when the application starts and uses it to generate delivery-time predictions.

## Dataset

The project also includes:

```text
delivery_eta_prediction.csv
```

This file contains the prediction-related data used with the project.

The original machine learning work is also included in:

```text
Delivery_ETA_Code_File.ipynb
```

## How the Prediction Works

When a request is sent to `/predict`, the API creates a data row containing the five input features:

```text
Distance_km
Traffic
Weather
Vehicle
Order_Size
```

The trained model then predicts the delivery time and the API returns the result in minutes.

## Future Improvements

Some possible improvements for this project:

- Add proper input validation for categorical values
- Add model performance metrics
- Add authentication for the API
- Add logging and monitoring
- Deploy the API to a cloud platform
- Add a frontend for easier interaction
- Add automated testing

## Author

**Jigar Vishwakarma**

Computer Engineering Student | AI/ML Enthusiast