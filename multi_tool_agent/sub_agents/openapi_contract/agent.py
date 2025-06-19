from google.adk.agents import LlmAgent
from google.genai.types import GenerateContentConfig

openapi_contract_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="openapi_contract_agent",
    description="Compares two OpenAPI specification documents to perform breaking change detection and returns a structured metadata report of the findings.",
    instruction="""
    You are an APIContractAgent that compares two OpenAPI specification documents.
    Your job is to detect any breaking changes between them and output a structured
    metadata dictionary listing for every breaking change."
    """,
    generate_content_config=GenerateContentConfig(
        temperature=0.0,  # greedy decoding
        top_k=1,  # only the single most probable token
        top_p=1.0,  # include full probability mass
        seed=42  # fixed random seed for repeatability
    )
)

