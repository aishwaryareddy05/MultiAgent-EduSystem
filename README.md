# 🧠 Multi-Agent StudyCrew AI 📚🤖

A smart multi-agent system that understands learners, scrapes online platforms, and recommends personalized courses using CrewAI, LangChain, and Google Gemini.

![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![CrewAI](https://img.shields.io/badge/crewai-0.22.0-orange.svg)
![LangChain](https://img.shields.io/badge/langchain-active-lightgrey.svg)
![Last Updated](https://img.shields.io/badge/last%20updated-2025--04--15-green.svg)

---

## 🧠 Core Architecture

```mermaid
graph TB
    USER[User Input]
    ANALYST[Learning Needs Analyst]
    EXPLORER[Web Content Explorer]
    SCRAPER[Scraper Tool]
    ADVISOR[Course Advisor]
    OUTPUT[Final Recommendation]

    USER --> ANALYST
    ANALYST --> EXPLORER
    EXPLORER --> SCRAPER
    SCRAPER --> ADVISOR
    ADVISOR --> OUTPUT
🔁 Agent Flow (Sequence)

sequenceDiagram
    participant U as User
    participant A as Analyst
    participant E as Explorer
    participant S as Scraper
    participant C as Advisor

    U->>A: Submit profile
    A->>E: Request relevant course search
    E->>S: Scrape course metadata
    S->>C: Forward results
    C-->>U: Return ranked recommendations
🧠 Modular Agent Roles
Agent Role Learning Analyst Parses user intent, skill level, and preferences Web Explorer Uses search tools to explore course offerings Scraper Tool Scrapes titles, links, summaries from platforms Course Advisor Filters, scores, and recommends courses
🛠️ Tech Stack
* CrewAI – Multi-agent orchestration
* LangChain – Agent execution logic
* Gemini API – LLM for context-aware decision-making
* Serper API – Google search interface
* BeautifulSoup4 – HTML parsing & scraping
* Python – Glue that connects it all
* Streamlit – Optional UI (if implemented)
* Dotenv – Environment variable management
📂 Folder Structure

studycrew/
├── agents.py         # Agent definitions
├── tasks.py          # Tasks per agent
├── tools.py          # Custom toolset: search, scrape, cache
├── crew.py           # Crew assembly & orchestration
├── main.py           # Entry point
├── utils/            # Reusable logic (optional)
└── .env              # API keys
🚀 Getting Started

git clone https://github.com/yourusername/studycrew-ai
cd studycrew-ai
pip install -r requirements.txt
Create a .env file with:

GOOGLE_API_KEY=your_google_key
SERPER_API_KEY=your_serper_key
Run it:

python main.py
🎯 Sample Output

🎯 Goal: AI Engineer | 📘 Level: Beginner | ⏱️ Time: 3hrs/day

🎓 Learning Paths:
• Hands-On Practitioner
• Theory Builder
• Balanced Combo

🔥 Recommended Courses:
• Machine Learning Specialization – Coursera
• AI for Everyone – Andrew Ng
• TensorFlow for AI – DeepLearning.AI
...
🔍 Highlights
* 🔁 Autonomous multi-agent interaction
* 🔗 Tool-to-agent chaining with context handoff
* 📡 Real-time scraping + caching
* 📚 Personalized recommendations
* 🔄 Easily extendable agent framework
🧑‍💻 Built By
Aishwarya — turning LLMs into personalized educators 💡 Let’s connect: LinkedIn