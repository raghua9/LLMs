# ResearchCrew Crew

This is ResearchCrew Crew project, powered by [crewAI](https://crewai.com). Goal is to create research crew that will help us research and analyze a topic, then create a comprehensive report, leveraging the powerful and flexible framework provided by crewAI to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

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
## Create CrewAI Project
- Create a new CrewAI project using the CLI. This command will set up a complete project structure with all the necessary files, allowing you to focus on defining your agents and their tasks rather than setting up boilerplate code.

    ```bash
    crewai create crew research_crew
    cd research_crew
    ```
This will generate a project with the basic structure needed for your crew. The CLI automatically creates:

- A project directory with the necessary files
- Configuration files for agents and tasks
- A basic crew implementation
- A main script to run the crew
``` bash
research_crew/
├── .gitignore               # Specifies intentionally untracked files to ignore
├── pyproject.toml           # Project metadata and dependencies
├── README.md                # Project overview and setup instructions
├── .env                     # Environment variables (e.g., API keys)
└── src/
    └── research_crew/
        ├── __init__.py
        ├── main.py          # Entry point for running the crew
        ├── crew.py          # Crew and task execution logic
        ├── tools/
        │   ├── custom_tool.py   # Example tool used by agents
        │   └── __init__.py
        └── config/
            ├── agents.yaml      # Agent definitions
            └── tasks.yaml       # Task definitions
```
### Configure Agents
In CrewAI, agents are specialized entities with specific roles, goals, and backstories that shape their behavior.
For research crew, two agents are created:
- A researcher who excels at finding and organizing information
- An analyst who can interpret research findings and create insightful reports.

Modified agents.yaml file to define these specialized agents. 

### Configure Tasks
With agents defined, we now need to give them specific tasks to perform. Tasks in CrewAI represent the concrete work that agents will perform, with detailed instructions and expected outputs.

For research crew, we’ll define two main tasks:
- A research task for gathering comprehensive information
- An analysis task for creating an insightful report

Modified the tasks.yaml file. 

### Configure Crew
The crew is the container that orchestrates how agents work together to complete tasks.

For this project, crew.py is modified to do the following:

1. Creating the researcher agent and equipping it with the SerperDevTool to search the web
2. Creating the analyst agent
3. Setting up the research and analysis tasks
4. Configuring the crew to run tasks sequentially (the analyst will wait for the researcher to finish)

### Setup main script
Main script that will run the crew. This is where we provide the specific topic we want the crew to research. This script prepares the environment, specifies our research topic, and kicks off the crew’s work. 

## Setup Env Variables
```bash
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

Note: We can get SERPER_API_KEY from Serper.dev and OPEN_API_KEY from platform.api.com. 

## Install Dependencies
Navigate to your project directory and install the dependencies using the CrewAI CLI:

```bash
crewai install
```

## Run the Crew Project

To kickstart the crew of AI agents and begin task execution, run this from the root folder of project:

```bash
$ crewai run
```

This command initializes the research_crew Crew, assembling the agents and assigning them tasks as defined in the configuration.

This example will create a `report.md` file with the output of a research on LLMs in the root folder.

## Error
MacOs 12 might create error with onnxruntime
This can be corrected by adding "onnxruntime==1.19.0" in the pyproject.toml