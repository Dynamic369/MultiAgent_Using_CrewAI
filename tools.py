from crewai_tools import YoutubeChannelSearchTool
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key= os.getenv('GROQ_API_KEY')
huggingface_api_key = os.getenv('HF_TOKEN')

yt_tool = YoutubeChannelSearchTool(
    config={
        "llm": {
            "provider": "groq",
            "config": {
                "model": "llama-3.1-8b-instant",
                "api_key": groq_api_key
            }
        },
        "embedder": {
            "provider": "huggingface",
            "config": {
                "model": "sentence-transformers/all-MiniLM-L6-v2",
                "api_key": huggingface_api_key
            }
        }
    },
    youtube_channel_handle='@krishnaik06'
)
