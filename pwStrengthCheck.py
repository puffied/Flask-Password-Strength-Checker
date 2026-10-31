from flask import Flask, render_template, request,jsonify
import re

app = Flask(__name__)


def checkPwStrength(password):
    if not password:
        feedback.append("Start typing to check strength.")
        return {"score": 0, "status": "empty", "message": "Enter a password.", "feedback": []}

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 20
    else:
        feedback.append("At least 8 characters")
    
    if len(password) >= 12:
        score += 20

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 20
    else:
        feedback.append("Mix uppercase & lowercase")

    if re.search(r"\d", password):
        score += 20
    else:
        feedback.append("Add a number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        feedback.append("Add a special character")

    if score < 40:
        status, message = "weak", "Weak password!"
    elif score < 80:
        status, message = "medium", "Medium password."
    else:
        status, message = "strong", "Strong password!"

    return {"score": score, "status": status, "message": message, "feedback": feedback}



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/check", methods=["POST"])
def api_check():
    data = request.get_json()
    password = data.get("password", "")
    result = checkPwStrength(password)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)