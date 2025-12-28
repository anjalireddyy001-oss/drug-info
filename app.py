from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_drugs():
    drugs = {}
    with open("drugs.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            drug_name = row["drug"].strip().lower()
            drugs[drug_name] = {
                "use": row["use"],
                "side_effects": row["side_effects"].split(";")
            }
    return drugs

drug_data = load_drugs()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    drug_name = None

    if request.method == "POST":
        drug_name = request.form["drug"].lower()
        if drug_name in drug_data:
            result = drug_data[drug_name]
        else:
            result = "Drug not found"

    return render_template(
        "index.html",
        result=result,
        drug=drug_name
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
