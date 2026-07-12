from flask import Flask, render_template, request

from model_utils import FEATURE_FIELDS, predict_flood


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("predict.html", fields=FEATURE_FIELDS)

    values = {}
    errors = []

    for field in FEATURE_FIELDS:
        raw_value = request.form.get(field["name"], "").strip()
        try:
            values[field["name"]] = float(raw_value)
        except ValueError:
            errors.append(f"{field['label']} must be a valid number.")

    if errors:
        return render_template(
            "predict.html",
            fields=FEATURE_FIELDS,
            values=request.form,
            errors=errors,
        )

    result = predict_flood(values)
    return render_template("result.html", result=result, values=values)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
