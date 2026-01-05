from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_drugs():
    drugs = []
    with open("drugs.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["side_effects"] = row["side_effects"].split(";")
            drugs.append(row)
    return drugs

@app.route("/", methods=["GET", "POST"])
def index():
    drugs = load_drugs()
    categories = sorted(set(d["category"] for d in drugs))

    results = []
    selected_category = ""
    drug_name = ""

    if request.method == "POST":
        drug_name = request.form.get("drug", "").lower().strip()
        selected_category = request.form.get("category", "")

        for drug in drugs:
            if drug_name and drug_name != drug["drug"].lower():
                continue
            if selected_category and selected_category != drug["category"]:
                continue
            results.append(drug)

    return render_template(
        "index.html",
        results=results,
        categories=categories,
        selected_category=selected_category,
        drug_name=drug_name
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
