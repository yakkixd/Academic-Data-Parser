from flask import Flask, render_template, request
import json, os

app = Flask(__name__, 
            template_folder=os.path.join(os.getcwd(), "templates"),
            static_folder=os.path.join(os.getcwd(), "static"))

with open("D:\\A_Codespace\\Result Spoof\\result_spoof_\\results.json", "r") as f:
    results = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        roll_number = request.form.get("regno")
        result = results.get(roll_number)
        if result:
            return render_template("result.html", data=result, roll=roll_number)
        else:
            return "Our servers are facing a temporary technical problem. We regret the inconvenience caused. Please try again after some time."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
