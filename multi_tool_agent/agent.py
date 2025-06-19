from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool


from .prompt import ORCHESTRATOR_PROMPT
from .sub_agents.github import github_agent
from .sub_agents.spring_boot import spring_boot_agent
from .sub_agents.openapi_contract import openapi_contract_agent
from .sub_agents.api_change_reporter import reporter_agent


repository_agent = agent_tool.AgentTool(agent=github_agent)
framework_agent = agent_tool.AgentTool(agent=spring_boot_agent)
api_contract_agent = agent_tool.AgentTool(agent=openapi_contract_agent)
reporter_agent = agent_tool.AgentTool(agent=reporter_agent)

root_agent = LlmAgent(
    name="OrchestratorAgent",
    model="gemini-2.5-flash",
    instruction=ORCHESTRATOR_PROMPT,
    tools=[repository_agent, framework_agent, api_contract_agent, reporter_agent],
)

