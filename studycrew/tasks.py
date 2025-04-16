# tasks.py
from agents import profile_agent,research_agent,advisor_agent
from crewai import Task
from tools import tool


analyze_profile = Task(
        description=(
            "Carefully read and understand the user's preferences like goals :{goals}, skill level:{skill_level} and time availability :{time_availability}, "
            "and learning preferences. Generate a clear summary of the learner profile."
        ),
        expected_output="A structured learner profile with goals, current skill level, and preferences.",
        agent=profile_agent
    )

    # 🌐 Task 2: Search and Scrape Course Content

scrape_courses = Task(
        description=(
            "Based on the learner profile, use online platforms (like Coursera, Udemy, edX) to search "
            "for courses and get course names and descriptions that match the user's preferences."
        ),
        tools=[tool],
        expected_output="A list of course titles and descriptions relevant to the user profile.",
        agent=research_agent
    )

    # 🎓 Task 3: Recommend Top Courses
recommend_courses = Task(
        description=(
            "Based on the learner profile and the scraped course data, recommend the top 5 most relevant courses. "
            "Consider the user's preferences like budget, difficulty, duration, and platform trust."
        ),
        tools=[tool],
        expected_output="A ranked list of top 5 course recommendations with justification.",
        agent=advisor_agent,
        async_execution=False,
        output_file='outputfile.txt'
    )

