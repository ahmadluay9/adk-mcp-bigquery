from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient
import os
from dotenv import load_dotenv

load_dotenv()
toolbox = ToolboxSyncClient(os.getenv("CLOUD_RUN_SERVICE_URL"))

# Load all the tools
tools = toolbox.load_toolset('my_bq_toolset')

root_agent = Agent(
    name="gcp_releasenotes_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about Google Cloud Release notes."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the Google Cloud Release notes. Use the tools to answer the question"
    ),
    tools=tools,
)