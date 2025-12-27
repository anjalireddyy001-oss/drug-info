
from flask import Flask, render_template, request

app = Flask(__name__)

# Simple drug database
drug_data = {
    "paracetamol": {
        "use": "Pain relief and fever reduction",
        "side_effects": [
            "Nausea",
            "Allergic reactions",
            "Liver damage (overdose)"
        ]
    },
    "ibuprofen": {
        "use": "Pain relief and inflammation reduction",
        "side_effects": [
            "Stomach upset",
            "Dizziness",
            "Increased blood pressure"
        ]
    },
    "amoxicillin": {
        "use": "Treatment of bacterial infections",
        "side_effects": [
            "Diarrhea",
            "Allergic reactions",
            "Skin rash"
        ]
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    drug_name = None

    if request.method == "POST":
        drug_name = request.form["drug"].lower()

        if drug_name in drug_data:
            result = drug_data[drug_name]
        else:
            result = "Drug not found 😕"

    return render_template("index.html", result=result, drug=drug_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
