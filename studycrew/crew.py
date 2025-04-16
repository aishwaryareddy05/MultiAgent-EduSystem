# crew.py
from agents import profile_agent,research_agent,advisor_agent
from crewai import Crew,Process
from tasks import analyze_profile,scrape_courses,recommend_courses


crew=Crew(
    agents=[profile_agent,research_agent,advisor_agent],
    tasks=[analyze_profile,scrape_courses,recommend_courses],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback
inputs = {
    'goals': 'AI Engineer',
    'skill_level': 'beginner',
    'time_availability': '3hours per day'
}
result=crew.kickoff(inputs=inputs)
print(result)