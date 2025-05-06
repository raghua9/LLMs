# LlmAgent. 'adk web' will give UI option to try the Agent. 'adk run' will run in CLI. 

from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

from .util import load_instruction_from_file

# --- Sub Agent 1: Scriptwriter ---
scriptwriter_agent = LlmAgent(
    name="ShortsScriptwriter",
    model="gemini-2.0-flash",
    instruction=load_instruction_from_file("scriptwriter_instruction.txt"),
    tools=[google_search],
    output_key="generated_script",  # Save result to state
)

# --- Sub Agent 2: Visualizer ---
visualizer_agent = LlmAgent(
    name="ShortsVisualizer",
    model="gemini-2.0-flash",
    instruction=load_instruction_from_file("visualizer_instruction.txt"),
    description="Generates visual concepts based on a provided script.",
    output_key="visual_concepts",  # Save result to state
)

# --- Sub Agent 3: Formatter ---
# This agent would read both state keys and combine into the final Markdown
formatter_agent = LlmAgent(
    name="ConceptFormatter",
    model="gemini-2.0-flash",
    instruction="""Combine the script from state['generated_script'] and the visual concepts from state['visual_concepts'] into the final Markdown format requested previously (Hook, Script & Visuals table, Visual Notes, CTA).""",
    description="Formats the final Short concept.",
    output_key="final_short_concept",
)


# --- Llm Agent Workflow ---
youtube_shorts_agent = LlmAgent(
    name="youtube_shorts_agent",
    model="gemini-2.0-flash",
    instruction=load_instruction_from_file("shorts_agent_instruction.txt"),
    description="You are an agent that can write scripts, visuals and format youtube short videos. You have subagents that can do this",
    
    # The follwing way of calling the sub-agents is throwing error https://github.com/google/adk-python/issues/53
    #sub_agents=[scriptwriter_agent, visualizer_agent, formatter_agent],
    # So alternate is used. 
    tools=[AgentTool(agent=scriptwriter_agent), AgentTool(agent=visualizer_agent), AgentTool(agent=formatter_agent)],
)

# --- Root Agent for the Runner ---
# The runner will now execute the workflow
root_agent = youtube_shorts_agent
