# import just the datetime class from the datetime module
from datetime import datetime
from google.adk.agents import Agent

def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time
    """,
    tools=[get_current_time],
    # Built in tool with custom tool won't work at present
    # tools=[google_search, get_current_time], # <--- Doesn't work
)
