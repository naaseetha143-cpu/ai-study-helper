from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------- SYLLABUS PLANNER ----------------
@app.route("/syllabus", methods=["GET", "POST"])
def syllabus():
    syllabus_text = None
    roadmap = None

    if request.method == "POST":
        syllabus_text = request.form.get("syllabus")

        topics = [t.strip() for t in syllabus_text.split("\n") if t.strip()]
        roadmap = []

        for i, topic in enumerate(topics, start=1):
            roadmap.append(f"Day {i}: {topic}")

    return render_template(
        "syllabus.html",
        syllabus=syllabus_text,
        roadmap=roadmap
    )


# ---------------- ASSIGNMENT TRACKER ----------------
@app.route("/assignment", methods=["GET", "POST"])
def assignment():
    guidance = None
    assignment_name = None
    due_date = None

    if request.method == "POST":
        assignment_name = request.form.get("assignment")
        aim = request.form.get("aim")
        due_date = request.form.get("due_date")

        guidance = [
            "Understand the assignment objective clearly.",
            f"Focus on the aim: {aim}",
            "Research required concepts and references.",
            "Prepare an outline or flow.",
            "Start implementation step-by-step.",
            "Review, correct errors, and finalize.",
            f"Submit before: {due_date}"
        ]

    return render_template(
        "assignment.html",
        assignment=assignment_name,
        due_date=due_date,
        guidance=guidance
    )


# ---------------- CHATBOT (RULE-BASED AI) ----------------
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    if "day" in user_message and "quiz" in user_message:
        reply = (
            "Daily Quiz:\n"
            "1) Define today’s main concept.\n"
            "2) Explain it in your own words.\n"
            "3) Give one real-life example."
        )

    elif "final quiz" in user_message or "full quiz" in user_message:
        reply = (
            "Final Quiz:\n"
            "1) Explain all core concepts.\n"
            "2) Write short notes on important topics.\n"
            "3) Solve two application-based questions.\n"
            "4) Draw diagrams if applicable.\n"
            "5) Revise weak areas."
        )

    elif "important" in user_message:
        reply = (
            "Important Questions:\n"
            "1) Explain key definitions.\n"
            "2) Compare major topics.\n"
            "3) Write short notes.\n"
            "4) Previous exam-based questions."
        )

    elif "roadmap" in user_message or "plan" in user_message:
        reply = (
            "Your roadmap is divided day-wise.\n"
            "Complete one topic per day.\n"
            "Revise daily and attempt quizzes."
        )

    else:
        reply = (
            "I can help you with:\n"
            "- Day-wise roadmap\n"
            "- Daily quizzes\n"
            "- Final revision quizzes\n"
            "- Important questions\n\n"
            "Example: 'Give Day 2 quiz'"
        )

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
