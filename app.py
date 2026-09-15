from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from utils.pdf_parser import extract_text_from_pdf
from utils.analyzer import analyze_resume


app = Flask(__name__)

# Folder where uploaded resumes will be stored
UPLOAD_FOLDER = "uploads"

# Allowed file types
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB maximum


# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    """Check whether uploaded file is a PDF."""
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():
    """Display home page."""
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """Analyze uploaded resume."""

    # Check whether a resume was uploaded
    if "resume" not in request.files:
        return render_template(
            "index.html",
            error="Please upload a resume PDF."
        )

    resume_file = request.files["resume"]

    # Check filename
    if resume_file.filename == "":
        return render_template(
            "index.html",
            error="Please select a resume file."
        )

    # Check file type
    if not allowed_file(resume_file.filename):
        return render_template(
            "index.html",
            error="Only PDF files are allowed."
        )

    # Get job description
    job_description = request.form.get("job_description", "").strip()

    if not job_description:
        return render_template(
            "index.html",
            error="Please enter a job description."
        )

    # Secure filename
    filename = secure_filename(resume_file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    # Save uploaded file
    resume_file.save(filepath)

    try:
        # Extract text from PDF
        resume_text = extract_text_from_pdf(filepath)

        if not resume_text.strip():
            return render_template(
                "index.html",
                error="Could not extract text from this PDF. Please upload a text-based PDF."
            )

        # Analyze resume
        result = analyze_resume(
            resume_text,
            job_description
        )

        return render_template(
            "result.html",
            result=result,
            filename=filename
        )

    except Exception as e:
        print("ERROR:", e)

        return render_template(
            "index.html",
            error="Something went wrong while analyzing the resume."
        )


@app.errorhandler(413)
def file_too_large(error):
    """Handle files larger than 5 MB."""
    return render_template(
        "index.html",
        error="File is too large. Maximum allowed size is 5 MB."
    ), 413


if __name__ == "__main__":
    app.run(debug=True)