# AI Resume Analyzer

An AI-powered web application that analyzes a candidate's resume against a given job description and helps identify how well the candidate matches the job requirements.

## 🚀 Features

* 📄 Upload a resume in PDF format
* 💼 Enter a job description
* 🔍 Extract relevant information from the resume
* 🧠 Analyze resume–job compatibility
* 📊 Generate a resume match score
* ✅ Identify matching skills
* ❌ Identify missing or required skills
* 🌐 Simple and user-friendly web interface
* 🐍 Python-based backend

## 🛠️ Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Other

* PDF processing
* Natural Language Processing
* Machine Learning
* Git & GitHub

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
│
├── data/
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   └── ...
│
├── uploads/
│
└── utils/
    └── ...
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AnushkaIngole20/ai-resume-analyzer.git
```

### 2. Open the project

```bash
cd ai-resume-analyzer
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

The application will normally be available at:

```text
http://127.0.0.1:5000
```

Open this address in your web browser.

## 📌 How to Use

1. Open the AI Resume Analyzer website.
2. Upload a candidate's resume in PDF format.
3. Enter or paste the required job description.
4. Submit the information.
5. The system analyzes the resume against the job description.
6. View the generated match score and skill analysis.

## 🧪 Testing

The application can be tested using different combinations of resumes and job descriptions.

Example:

| Resume              | Job Description      | Expected Result |
| ------------------- | -------------------- | --------------- |
| AI/ML Resume        | AI/ML Engineer       | High Match      |
| Full-Stack Resume   | Full-Stack Developer | High Match      |
| Data Analyst Resume | Data Analyst         | High Match      |
| AI/ML Resume        | Data Analyst         | Lower Match     |
| Full-Stack Resume   | Data Analyst         | Lower Match     |

Testing different combinations helps verify whether the analyzer can distinguish between relevant and less-relevant candidates.

## 🎯 Objective

The main objective of this project is to simplify the initial resume screening process by automatically comparing candidate resumes with job requirements and providing useful insights about their suitability for a particular role.

## 🔮 Future Scope

* Improve AI-based semantic matching
* Add multiple resume comparison
* Add recruiter dashboard
* Provide detailed candidate ranking
* Support additional document formats
* Improve skill and experience extraction
* Add job recommendation based on candidate skills

## 👩‍💻 Author

**Anushka Ingole**

GitHub:
https://github.com/AnushkaIngole20

## 📄 License

This project is created for educational and project demonstration purposes.
