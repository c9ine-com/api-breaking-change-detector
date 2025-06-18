from google.adk.agents import LlmAgent, ParallelAgent
from gitingest import ingest, ingest_async
from google.adk.tools import ToolContext



async def fetch_first_branch(git_url: str, first_branch_name: str, tool_context: ToolContext ) -> dict:
    """Retrieves content from a specified Git branch.

    This function fetches the content of a branch from a Git repository
    and stores it within the tool's execution context for further use.

    Args:
        git_url (str): The URL of the Git repository.
        first_branch_name (str): The name of the first branch.
        tool_context (dict): The tool's execution context.

    Returns:
        dict: A dictionary with 'status' (success) and 'content' (the branch's string data).
    """
    _, _, content = await ingest_async(
        source=git_url,
        branch=first_branch_name
    )

    tool_context.state["git:first_branch_content"] = content
    return {
          "status": "success",
          "content": content,
    }

async def fetch_second_branch(git_url: str, second_branch_name: str, tool_context: ToolContext ) -> dict:
    """Retrieves content from a specified Git branch.

    This function fetches the content of a branch from a Git repository
    and stores it within the tool's execution context for further use.

    Args:
        git_url (str): The URL of the Git repository.
        second_branch_name (str): The name of the second branch.
        tool_context (dict): The tool's execution context.

    Returns:
        dict: A dictionary with 'status' (success) and 'content' (the branch's string data).
    """
    _, _, content = await ingest_async(
      source=git_url,
      branch=second_branch_name
    )

    tool_context.state["git:second_branch_content"] = content

    return {
      "status": "success",
      "content": content,
    }

# Add the tool to the agent
github_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="github_agent_multi_branch_fetch",
    description="Fetches repo content from the given repo URL and 2 selected branches by user inputs",
    instruction="""
    You are an helpful agent that can fetch source code from a git repository url.
    You will request two branch names from user.
    Then you will get the source code of the first branch.
    After that you will get the source code of the second branch. 
    Show the content of both branches with files ending with ".java" postfix.
     """,
    tools=[fetch_first_branch, fetch_second_branch],
    output_key= "two_branches_content"# Provide the function directly
)

