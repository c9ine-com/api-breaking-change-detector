from google.adk.agents import SequentialAgent

from .sub_agents.github import github_agent
from .sub_agents.spring_boot import spring_boot_agent

root_agent = SequentialAgent(
    name="OrchestratorAgent",
    description=(
        "Agent to breaking API changes with user input of github repo url, first branch name and second branch name"
    ),
   # sub_agents=[github_agent, spring_boot, openapi_contract, api_change_report]
   #sub_agents=[github_agent,spring_boot_agent]
   sub_agents=[github_agent]
)

