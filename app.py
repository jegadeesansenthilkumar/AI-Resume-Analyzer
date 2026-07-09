import os
from flask import Flask, render_template, request
from resume_parser import extract_text, extract_email, extract_phone, extract_education
from skill_extractor import extract_skills

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

ALLOWED_EXTENSIONS = {"pdf", "docx"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "resume" not in request.files:
            return "No file uploaded"

        file = request.files["resume"]

        if file.filename == "":
            return "No file selected"

        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            text = extract_text(filepath)
            email = extract_email(text)
            phone = extract_phone(text)
            skills = extract_skills(text)
            education = extract_education(text)
            word_count = len(text.split())

            return render_template(
                "result.html",
                email=email,
                phone=phone,
                skills=skills,
                education=education,
                word_count=word_count,
                text=text
            )

    return render_template("index.html")

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
