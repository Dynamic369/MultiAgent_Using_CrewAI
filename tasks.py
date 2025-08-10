from crewai import Task
from tools import yt_tool 
from agents import blog_reseacrher, blog_writer

 ## Reaeasrch Task
research_task = Task(
    description=(
        "Tdentify the video {topic}."
        "Get the detailed information about the video from the YouTube channel."
    ),
    expected_output='Acomprehensive 3 paragraphs long repost based on the {topic} and create the content for the blog.',
    tools=[yt_tool],
    agent=blog_reseacrher,
)

## Writing Task
write_task = Task(
    description=(
        'Get the info from the youtube channel on the topic {topic}.'
    ),
    expected_output='Summarize the info from the youtube channel video on the topic {topic} and write a blog post.',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)