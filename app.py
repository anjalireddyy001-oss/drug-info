from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_drugs():
    drugs = {}
    with open("drugs.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            drug_name = row["drug"].strip().lower()
            drugs[drug_name] = {
                "use": row.get("use", ""),
                "category": row.get("category", ""),
                "side_effects": row.get("side_effects", "").split(";")
            }
    return drugs

drug_data = load_drugs()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    drug = None

    if request.method == "POST":
        drug = request.form.get("drug", "").lower().strip()
        if drug in drug_data:
            result = drug_data[drug]
        else:
            result = "Drug not found"

    return render_template("index.html", result=result, drug=drug)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
