from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq




#creating a senior blog content reasearcher
blog_researcher = Agent(
    role='Blog reasearcher form youtube videos',
    goal='get the relevant content for the topic {topic} from youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and GEN AI and providing suggestions."

    ),
    tools=[yt_tool],

    allow_delegation=True,
)

## Creating a senior blog writer agent with YT Tool

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from youtube channel',
    verbose=True,
    memory=True,
    backstory=(
        'With a flair for simplifying complex topics,'
        'you craft engaging narratives that capivate and educate, '
        'bringing new discoveries to light in an accessible manner'
    ),
    tools=[yt_tool],
    allow_delegation=False,
)

