from flask import Flask, render_template, request

app = Flask(__name__)

drug_data = {
    "paracetamol": {
        "use": "Pain relief and reduction of fever",
        "side_effects": [
            "Nausea",
            "Skin rash (rare)",
            "Liver damage at high doses"
        ]
    },
    "ibuprofen": {
        "use": "Pain, inflammation, and fever",
        "side_effects": [
            "Stomach irritation",
            "Ulcer risk",
            "Kidney problems (long-term use)"
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
            result = "Drug not found 😢"

    return render_template("index.html", result=result, drug=drug_name)

if __name__ == "__main__": 
app.run(host="0.0.0.0", port=5000)
