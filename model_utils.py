from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "floods.save"

FEATURE_FIELDS = [
    {
        "name": "annual_rainfall",
        "label": "Annual Rainfall",
        "unit": "mm",
        "placeholder": "Example: 1850",
        "min": 0,
        "step": 0.01,
    },
    {
        "name": "monsoon_rainfall",
        "label": "Monsoon Rainfall",
        "unit": "mm",
        "placeholder": "Example: 920",
        "min": 0,
        "step": 0.01,
    },
    {
        "name": "cloud_visibility",
        "label": "Cloud Visibility",
        "unit": "%",
        "placeholder": "Example: 76",
        "min": 0,
        "max": 100,
        "step": 0.01,
    },
    {
        "name": "temperature",
        "label": "Average Temperature",
        "unit": "C",
        "placeholder": "Example: 29",
        "min": -20,
        "max": 60,
        "step": 0.01,
    },
]


def _load_model():
    if not MODEL_PATH.exists():
        return None
    try:
        import joblib
    except ImportError:
        return None
    return joblib.load(MODEL_PATH)


def _fallback_prediction(values):
    annual = values["annual_rainfall"]
    monsoon = values["monsoon_rainfall"]
    visibility = values["cloud_visibility"]
    temperature = values["temperature"]

    rainfall_score = min(annual / 2600, 1) * 45
    monsoon_score = min(monsoon / 1300, 1) * 35
    visibility_score = max((visibility - 45) / 55, 0) * 12
    temperature_score = max((temperature - 24) / 16, 0) * 8
    probability = round(min(rainfall_score + monsoon_score + visibility_score + temperature_score, 99), 2)

    if probability >= 65:
        label = "High Flood Chance"
        status = "danger"
        advice = "Issue alerts, prepare evacuation routes, and prioritize response resources."
    elif probability >= 40:
        label = "Moderate Flood Chance"
        status = "warning"
        advice = "Monitor rainfall trends closely and keep field teams ready."
    else:
        label = "Low Flood Chance"
        status = "safe"
        advice = "Continue routine monitoring and update readings when weather conditions change."

    return {
        "label": label,
        "status": status,
        "probability": probability,
        "advice": advice,
        "source": "Built-in demo risk scoring. Replace models/floods.save with your trained model for production predictions.",
    }


def predict_flood(values):
    model = _load_model()
    if model is None:
        return _fallback_prediction(values)

    feature_vector = [[values[field["name"]] for field in FEATURE_FIELDS]]
    prediction = model.predict(feature_vector)[0]

    probability = None
    if hasattr(model, "predict_proba"):
        probability = round(float(max(model.predict_proba(feature_vector)[0])) * 100, 2)

    is_flood = int(prediction) == 1
    return {
        "label": "High Flood Chance" if is_flood else "No Flood Chance",
        "status": "danger" if is_flood else "safe",
        "probability": probability,
        "advice": (
            "Issue alerts, prepare evacuation routes, and prioritize response resources."
            if is_flood
            else "Continue routine monitoring and update readings when weather conditions change."
        ),
        "source": "Prediction generated using models/floods.save.",
    }
