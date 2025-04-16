from crewai import Agent
from crewai import LLM
#from langchain_groq import ChatLiteLLM
from langchain_groq import ChatGroq 
#from crewai.llm import ChatLLM
from tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

# 🔑 Load Groq LLM (Gemma/LLama via Groq API)
llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
    verbose=True,
    
)


# 🧑‍🏫 Learning Needs Analyst
profile_agent=Agent(
        role="Learning Needs Analyst",
        goal="Understand the user's skill level, learning goals, and preferences to build a structured learner profile.",
        backstory=(
            "You are an educational strategist skilled in interpreting learners’ backgrounds and translating them into actionable learning paths."
        ),
        
        llm=llm,
        verbose=True,
        memory=True,
        allow_delegation=True
    )

# 🌐 Web Content Explorer
research_agent= Agent(
        role="Web Content Explorer",
        goal="Search online education platforms and get course content relevant to the learner profile.",
        backstory=(
            "You're an expert in navigating learning platforms like Coursera, Udemy, edX, etc. "
            "You specialize in identifying and extracting useful educational resources."
        ),
        tools=[tool],
        llm=llm,
        verbose=True,
        memory=True,
        allow_delegation=False
    )

# 🎯 Course Advisor
advisor_agent=Agent(
        role="Course Advisor",
        goal="Recommend the most relevant and personalized learning resources based on learner profile and data.",
        backstory=(
            "You're a trusted course mentor who knows how to match the perfect learning content with individual goals, "
            "experience level, and preferences. You prioritize quality, relevance, and value."
        ),
        tools=[tool],
        llm=llm,
        verbose=True,
        memory=True,
        allow_delegation=False
    )
