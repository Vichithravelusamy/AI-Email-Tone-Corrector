# 📧 AI Email Tone Corrector

> An AI-powered email writing assistant that analyzes, rewrites, and improves professional emails using **Groq Llama 3.3** and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red)
![Groq](https://img.shields.io/badge/Groq-LLM-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

AI Email Tone Corrector is an intelligent web application that helps users write better professional emails.

Using the power of **Groq's Llama 3.3-70B Versatile** model, the application analyzes an email draft, rewrites it in a professional tone, identifies missing information, provides improvement suggestions, and rates the overall quality of the email.

Whether you're writing to HR, a recruiter, manager, client, professor, or colleague, this application helps ensure your communication is clear, concise, and professional.

---

# ✨ Features

### 📩 Professional Email Rewriting

- Rewrites poorly written emails
- Improves grammar
- Enhances professionalism
- Makes emails concise and impactful

---

### 🎯 Tone Analysis

Analyzes the email tone such as:

- Professional
- Friendly
- Formal
- Informal
- Polite
- Assertive

---

### 🔍 Missing Details Detection

Detects whether the email is missing:

- Subject clarity
- Attachments
- Important dates
- Deadlines
- Contact information
- Job title
- Resume mention
- Cover letter mention

---

### 💡 Improvement Suggestions

Provides actionable recommendations to improve:

- Structure
- Grammar
- Readability
- Tone
- Professionalism
- Clarity

---

### ⭐ Overall Rating

Rates the email on a scale of **1–10** based on:

- Professionalism
- Completeness
- Tone
- Clarity
- Readability

---

### ⚡ Lightning Fast AI

Powered by **Groq's ultra-fast inference engine** for quick responses.

---

# 🏗️ System Architecture

```
               User
                 │
                 ▼
          Streamlit Frontend
                 │
                 ▼
        Prompt Engineering Layer
                 │
                 ▼
         Groq Llama 3.3 API
                 │
                 ▼
        AI Generated Response
                 │
                 ▼
      Rewritten Professional Email
```

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | User Interface |
| Groq API | AI Inference |
| Llama 3.3 70B | Language Model |
| python-dotenv | Environment Variables |

---

# 📂 Project Structure

```
AI-Email-Tone-Corrector/
│
├── app.py
├── .env
├── requirements.txt
├── .gitignore
├── README.md
│
└── screenshots/
      home.png
      output.png
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Vichithravelusamy/AI-Email-Tone-Corrector.git
```

---

## 2. Navigate into the Project

```bash
cd AI-Email-Tone-Corrector
```

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a file named **`.env`** in the project root.

```
GROQ_API_KEY=your_groq_api_key
```

You can generate your API key here:

https://console.groq.com/keys

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser at:

```
http://localhost:8501
```

---

# 🖥️ Application Workflow

1. Open the application.
2. Select the recipient.
3. Select the purpose of the email.
4. Paste your email draft.
5. Click **Analyze & Improve**.
6. Wait for the AI analysis.
7. View:
   - Rewritten Email
   - Tone Analysis
   - Missing Details
   - Improvement Suggestions
   - Overall Rating

---




# 📊 Example

## Input

```
Hi HR,

I need job.

Please check my resume.

Thanks
```

---

## Output

### Rewritten Email

Dear Hiring Manager,

I hope you are doing well.

I am writing to express my interest in available opportunities at your organization. Please find my resume attached for your review.

I would appreciate the opportunity to discuss how my skills and experience align with your team's requirements.

Thank you for your time and consideration.

Kind regards,

Your Name

---

### Tone Analysis

Professional but incomplete.

---

### Missing Details

- Subject line
- Job title
- Contact information
- Resume mention
- Relevant skills

---

### Overall Rating

8.5/10

---

# 📦 Requirements

```
streamlit
groq
python-dotenv
```

---

# 🔒 Security

- API keys are stored securely using `.env`.
- Sensitive credentials are excluded from Git using `.gitignore`.
- No user emails are permanently stored.

---

# ⚙️ Configuration

You can change the AI model in `app.py`.

Example:

```python
model="llama-3.3-70b-versatile"
```

Other supported Groq models can also be used.

---

# 📈 Future Improvements

- Export to PDF
- Export to DOCX
- Email templates
- AI-generated subject lines
- Grammar scoring
- Resume-aware email generation
- Gmail integration
- Outlook integration
- Dark mode optimization
- Multi-language support
- Copy to clipboard
- Download results
- Email history
- Prompt customization
- AI confidence score

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.

```bash
git checkout -b feature/new-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to GitHub.

```bash
git push origin feature/new-feature
```

5. Open a Pull Request.

---

# 🐛 Reporting Issues

Found a bug?

Please open an issue with:

- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots (if applicable)

GitHub Issues:

https://github.com/Vichithravelusamy/AI-Email-Tone-Corrector/issues

---

# 📄 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute it for personal and commercial purposes.

---

# 👨‍💻 Author

**Vichithra Velusamy**

GitHub: https://github.com/Vichithravelusamy

LinkedIn: *(Add your LinkedIn profile URL here)*

---

# 🌟 Support

If you found this project helpful:

⭐ Star this repository

🍴 Fork it

🛠️ Contribute

📢 Share it with others

---

## Made with ❤️ using Python, Streamlit, and Groq AI.
