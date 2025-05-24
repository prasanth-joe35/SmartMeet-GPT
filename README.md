
# SmartMeet GPT – AI Meeting Insight Generator

SmartMeet GPT is an AI-powered productivity tool that transforms unstructured meeting notes into actionable insights. Built with **Streamlit** and **OpenAI GPT-3.5**, it provides structured summaries, professional email drafts, and prioritized next steps — all from raw notes.

>  Designed and developed by **Prasanth A** to demonstrate real-world prompt engineering, AI integration

---

## 🔍 Features

- 📝 Paste meeting notes (text-based)
- 🧠 Generate structured summaries instantly
- 📧 Draft stakeholder-ready emails
- 📋 Get recommended next steps
- 🎨 Modern, SaaS-style UI with session-safe behavior
- 🔁 Built using prompt engineering best practices

---

## 📸 Demo Screenshot


---

## 🛠️ Tech Stack

| Layer            | Tools / Technologies            |
|------------------|----------------------------------|
|  LLM Backend     | OpenAI GPT-3.5 Turbo             |
|  Framework       | Streamlit                        |
|  Prompt Logic    | Prompt engineering + role-based prompts |
| UI Styling       | Custom CSS for SaaS look         |
| State Mgmt       | `st.session_state` for persistence |

---

## How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/prasanth-joe35/smartmeet-gpt.git
cd smartmeet-gpt
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file and add:

```
OPENAI_API_KEY= ...................
```

### 4. Run the app

```bash
streamlit run smartmeet_app.py
```

---

##  Folder Structure

```
 smartmeet-gpt/
│
├── smartmeet_app.py      # Main Streamlit app
├── .env                        # API key (not committed to repo)
├
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

##  Prompt Strategy

Each feature is powered by a tailored prompt:

- **Summary Generator**: `"You are an expert meeting analyst assistant..."`
- **Email Generator**: `"You are a professional assistant..."`
- **Action Recommender**: `"You are a productivity coach..."`

This ensures:
- Clear roles for the AI
- Predictable, clean output
- Easy future expansion

---

##  Author

**Prasanth A**  
MBA (Analytics & Data Science)  
AI + Software Developer 
📫 [LinkedIn](https://www.linkedin.com/in/prasanthjoe35) • [GitHub](https://github.com/prasanth-joe35)

---


## 📄 License

MIT License © 2025 Prasanth A
