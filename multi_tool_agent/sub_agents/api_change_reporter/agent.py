from google.adk.agents import LlmAgent

reporter_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="reporter_agent",
    description="Takes a JSON object of structured API change metadata and generates a final, human-readable report formatted in Markdown.",
    instruction="""
    You are the ReporterAgent. Your one job is to convert a JSON object detailing API changes into a clean, 
    human-readable Markdown report.
    The report must have a summary, a section for '🚨 Breaking Changes', 
    and a section for '✅ Non-Breaking & Additive Changes'. 
    Present all changes in Markdown tables.
    """
)

