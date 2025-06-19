from gitingest import ingest_async
from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext


async def fetch_branch(git_url: str, branch_name: str) -> dict:
    """Retrieves content from a specified Git branch.

    This function fetches the content of a branch from a Git repository
    and stores it within the tool's execution context for further use.

    Args:
        git_url (str): The URL of the Git repository.
        branch_name (str): The name of the branch.

    Returns:
        dict: A dictionary with 'llm_friendly_code' (the branch's string data).
    """
    _, _, content = await ingest_async(
        source=git_url,
        branch=branch_name,
        max_file_size= 100_000
    )
    return {
          "llm_friendly_code": content,
    }

# Add the tool to the agent
github_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="github_agent_branch_fetch",
    description="Fetches repo content from a specific branch of given repo URL",
    tools=[fetch_branch]
)

