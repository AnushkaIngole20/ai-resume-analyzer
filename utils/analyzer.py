import re
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Location of skills file
SKILLS_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "skills.txt"
)


def load_skills():
    """
    Load skills from data/skills.txt.
    """

    if not os.path.exists(SKILLS_FILE):
        return []

    with open(SKILLS_FILE, "r", encoding="utf-8") as file:
        skills = [
            line.strip().lower()
            for line in file
            if line.strip()
        ]

    return list(dict.fromkeys(skills))


def clean_text(text):
    """
    Basic NLP text preprocessing.
    """

    text = text.lower()

    # Replace multiple spaces/newlines
    text = re.sub(r"\s+", " ", text)

    # Keep letters, numbers, spaces, +, # and dots
    text = re.sub(r"[^a-z0-9\s+#.\-]", " ", text)

    return text.strip()


def extract_skills(text):
    """
    Detect known skills from text.
    """

    cleaned_text = clean_text(text)

    skills = load_skills()

    found_skills = []

    for skill in skills:

        # Escape special characters in skill names
        escaped_skill = re.escape(skill)

        # Word boundary matching
        pattern = r"(?<!\w)" + escaped_skill + r"(?!\w)"

        if re.search(pattern, cleaned_text):
            found_skills.append(skill)

    return sorted(set(found_skills))


def calculate_similarity(resume_text, job_description):
    """
    Calculate similarity using TF-IDF and cosine similarity.
    """

    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_description)

    if not resume_clean or not job_clean:
        return 0.0

    documents = [
        resume_clean,
        job_clean
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def generate_suggestions(
    resume_skills,
    job_skills,
    missing_skills,
    match_score
):
    """
    Generate basic recommendations.
    """

    suggestions = []

    if match_score < 40:
        suggestions.append(
            "Your resume has a low similarity with the job description. "
            "Consider adding more relevant skills and project experience."
        )

    elif match_score < 70:
        suggestions.append(
            "Your resume has a moderate match. "
            "Add more skills mentioned in the job description."
        )

    else:
        suggestions.append(
            "Your resume has a good match with the job description. "
            "Keep your technical skills and projects clearly mentioned."
        )

    if missing_skills:
        suggestions.append(
            "Consider learning or mentioning these relevant skills: "
            + ", ".join(missing_skills[:5])
            + "."
        )

    if "github" not in resume_skills:
        suggestions.append(
            "Consider adding your GitHub profile or coding projects."
        )

    if "git" not in resume_skills:
        suggestions.append(
            "Mention Git/version-control experience if you have it."
        )

    if not resume_skills:
        suggestions.append(
            "No known technical skills were detected. "
            "Make sure your skills section is clearly written."
        )

    return suggestions


def analyze_resume(resume_text, job_description):
    """
    Complete resume analysis.
    """

    # Extract skills
    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    # Find missing skills
    missing_skills = [
        skill
        for skill in job_skills
        if skill not in resume_skills
    ]

    # Calculate AI similarity
    match_score = calculate_similarity(
        resume_text,
        job_description
    )

    # Generate suggestions
    suggestions = generate_suggestions(
        resume_skills,
        job_skills,
        missing_skills,
        match_score
    )

    return {
        "match_score": match_score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }