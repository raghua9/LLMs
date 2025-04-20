# GuideCreator Flow

This is GuideCreator Flow project, powered by [crewAI](https://crewai.com). In this project, we’ll walk create CrewAI Flow that generates a comprehensive learning guide on any topic. This project uses Crew Flows that provide structured, event-driven control over AI workflows by combining regular code, direct LLM calls, and crew-based processing. 

This guide creator flow demonstrates fundamental patterns, such as:

- Interactive AI assistants that combine multiple specialized subsystems
- Complex data processing pipelines with AI-enhanced transformations
- Autonomous agents that integrate with external services and APIs
- Multi-stage decision-making systems with human-in-the-loop processes

## Installation (Pre-Requisite)

- CrewAI requires Python >=3.10 and <3.13

- Create Virtual Environment – This helps keep the project’s dependencies isolated, so it doesn’t interfere with other Python projects or system packages. 
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
- CrewAI uses the [UV](https://docs.astral.sh/uv/) as its dependency management and package handling tool. It simplifies project setup and execution, offering a seamless experience. Since we are creating the project in virtual environment. 

    ```bash
    pip install uv
    ```
- Run the following command to install crewai CLI

    ```bash
    uv tool install crewai
    ```
## Create CrewAI Flow Project
- Create a new CrewAI Flow project using the CLI. This will generate a project with the basic structure needed for your flow.

    ```bash
    crewai create flow guide_creator_flow
    cd guide_creator_flow
    ```
The generated project has the following structure:

- The main flow logic in the main.py file
- Specialized crews in the crews directory
- Custom tools in the tools directory
``` bash
guide_creator_flow/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
├── main.py
├── crews/
│   └── poem_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── poem_crew.py
└── tools/
    └── custom_tool.py
```
### Add Content Writer Crew
This flow will need a specialized crew to handle the content creation process. The following command automatically creates the necessary directories and template files for the crew. The content writer crew will be responsible for writing and reviewing sections of our guide, working within the overall flow orchestrated by our main application.
```bash
crewai flow add-crew content-crew
```
## Configure the Content Writer Crew
We’ll set up two specialized agents - a writer and a reviewer - that will collaborate to create high-quality content for our guide.
1. First, update the agents configuration file to define the content creation team.
src/guide_creator_flow/crews/content_crew/config/agents.yaml
2. Next, update the tasks configuration file to define the specific writing and reviewing tasks. 
src/guide_creator_flow/crews/content_crew/config/tasks.yaml

The task definitions provide detailed instructions to agents, ensuring they produce content that meets quality standards.

3. Now, update the crew implementation file to define how  agents and tasks work together:
src/guide_creator_flow/crews/content_crew/content_crew.py

This crew definition establishes the relationship between agents and tasks, setting up a sequential process where the content writer creates a draft and then the reviewer improves it.

### Create the Flow
This is where we’ll combine regular Python code, direct LLM calls, and content creation crew into a cohesive system.

The flow will:
- Get user input for a topic and audience level
- Make a direct LLM call to create a structured guide outline
- Process each section sequentially using the content writer crew
- Combine everything into a final comprehensive document

The flow is created in the main.py file. 

Main will have the following:

- Pydantic models for structured data, ensuring type safety and clear data representation
- state class to maintain data across different steps of the flow
- Implement three main flow steps:
    - Getting user input with the @start() decorator
    - Creating a guide outline with a direct LLM call
    - Processing sections with the content crew
- Use the @listen() decorator to establish event-driven relationships between steps

This is the power of flows - combining different types of processing (user interaction, direct LLM calls, crew-based tasks) into a coherent, event-driven system.

## Setup Env Variables
```bash
OPENAI_API_KEY=your_openai_api_key
```

Note: We can OPEN_API_KEY from platform.api.com. 

## Install Dependencies
Navigate to your project directory and install the dependencies using the CrewAI CLI:

```bash
crewai install
```

## Run the Flow Project

To kickstart the Flow, run this from the root folder of project:

```bash
$ crewai flow kickoff
```

When we run this command, we’ll see the flow does the following:

1. It will prompt for a topic and audience level
2. It will create a structured outline for the guide
3. It will process each section, with the content writer and reviewer collaborating on each
4. Finally, it will compile everything into a comprehensive guide

This demonstrates the power of flows to orchestrate complex processes involving multiple components, both AI and non-AI.

Open output/complete_guide.md to view the output. 

## Visualize the Flow
This will create an HTML file that shows the structure of your flow, including the relationships between different steps and the data that flows between them. 
```bash
crewai flow plot
```

## Review the Output
Once the flow completes, you’ll find two files in the output directory:

1. guide_outline.json: Contains the structured outline of the guide
2. complete_guide.md: The comprehensive guide with all sections

And plot will create guide_creator_flow.html which gives visualization. 