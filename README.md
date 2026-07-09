# AI Resume Analyzer

AI Resume Analyzer is a Flask-based web application that analyzes resumes in PDF and DOCX formats. The application extracts important information such as contact details, skills, education, and resume content and displays the results through a simple web interface.

## Features

- Upload resumes in PDF format
- Upload resumes in DOCX format
- Extract text from resumes
- Extract email addresses
- Extract phone numbers
- Detect technical skills
- Identify education details
- Calculate resume word count
- Display extracted information on a results page
- Simple and user-friendly web interface

## Technologies Used

- Python
- Flask
- HTML
- CSS
- pdfplumber
- python-docx

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── uploads/
```
## How It Works

1. The user uploads a resume in PDF or DOCX format.
2. The Flask application receives and processes the uploaded file.
3. Resume text is extracted using `pdfplumber` or `python-docx`.
4. Contact information and education details are extracted from the resume.
5. Technical skills are detected using keyword matching.
6. The application calculates the resume word count.
7. The analysis results are displayed through the web interface.

## Installation

Clone the repository:

```bash
git clone https://github.com/jegadeesansenthilkumar/AI-Resume-Analyzer.git
```

Navigate to the project directory:

```bash
cd AI-Resume-Analyzer
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Current Version

This is Version 1 of the AI Resume Analyzer.

The current version focuses on the basic resume processing pipeline, including file upload, text extraction, contact information extraction, skill detection, education detection, and displaying the analysis results.

## Future Enhancements

- Job description comparison
- ATS compatibility scoring
- Matching and missing skill detection
- Resume improvement suggestions
- Semantic similarity using NLP and Sentence Transformers
- Interactive analysis dashboard
- Database integration
- User accounts and resume history
- AI-generated resume recommendations
- Online deployment

## Privacy

Uploaded resumes are intended for temporary local processing and should not be committed to the GitHub repository. The `uploads` directory is excluded using the `.gitignore` file.

## Author

**Jegadeesan S**

Computer Science Engineering Student interested in Python, Machine Learning, Data Analysis, Artificial Intelligence, and Software Development.

## Disclaimer

This project is currently under development and is intended for educational and portfolio purposes.
