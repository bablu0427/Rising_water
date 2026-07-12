# Rising Waters: Machine Learning Flood Prediction

This project is a Flask web application for predicting flood risk from rainfall and weather inputs. It is designed for a machine learning workflow that trains models such as Decision Tree, Random Forest, KNN, and XGBoost, then deploys the best model through a web interface.

## Features

- Enhanced responsive website interface
- Flood risk input form
- Result page with risk level, probability, and operational advice
- Built-in demo scoring if no trained model is present
- Support for a saved model file at `models/floods.save`
- IBM Cloud-ready project structure

## Requirements

- Python 3.8 or above
- Anaconda Navigator or Jupyter Notebook
- Flask
- Scikit-learn
- XGBoost
- Joblib

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Add Your Trained Model

Save your trained best-performing model as:

```text
models/floods.save
```

The app will automatically use this file when it exists. If the file is not present, the app uses a built-in demo scoring method so the website still works for presentation and testing.

## Suggested Dataset Features

- Annual rainfall
- Monsoon or seasonal rainfall
- Cloud visibility
- Temperature
- Other meteorological parameters

## Project Outcome

Learners can use this application to understand data preprocessing, classification model evaluation, Flask integration, and cloud deployment for disaster preparedness.
