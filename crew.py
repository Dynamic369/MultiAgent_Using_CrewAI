from crewai import Crew,Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task 
from crewai_tools import YoutubeChannelSearchTool

# Forming the tech-focused cew with some enhanced configuration
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,  # Ensuring tasks are executed in order
    memory=True,
    cache=True,
    max_rpm=10,  # Limiting requests per minute to avoid rate limiting
    share_crew=True
)



# Start the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL vs Data Science'})
print(result)