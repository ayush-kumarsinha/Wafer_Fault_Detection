from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load models
imputer = joblib.load("models/imputer.pkl")
selector = joblib.load("models/selector.pkl")
model = joblib.load("models/wafer_fault_detection_model.pkl")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        file = request.files["file"]

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        df = pd.read_csv(filepath)

        # Remove wafer column if present
        if "Unnamed: 0" in df.columns:
            df = df.drop(columns=["Unnamed: 0"])

        # Imputation
        df = pd.DataFrame(
            imputer.transform(df),
            columns=df.columns
        )

        print("Before Selector:", df.shape)

        # Feature Selection
        selected_data = selector.transform(df)

        print("After Selector:", selected_data.shape)

        # Prediction
        predictions = model.predict(selected_data)

        good_count = (predictions == 1).sum()
        bad_count = (predictions == -1).sum()

        return render_template(
            "index.html",
            prediction_text=f"Good Wafers: {good_count} | Bad Wafers: {bad_count}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)