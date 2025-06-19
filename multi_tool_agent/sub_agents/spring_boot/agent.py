from google.adk.agents import LlmAgent
from google.genai.types import GenerateContentConfig

spring_boot_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="spring_boot_agent",
    description="Generates api specs in OpenAPI specifications format from Spring Boot REST based source codes",
    instruction="""
    You are an OpenAPI 3.0 specification generator. 
    Given Java 17 Spring Boot controller and model source code, output only the corresponding OpenAPI 3 YAML document. 
    Do not include explanations, reasoning, or any text outside the valid YAML.
    
    """, #Do not miss any endpoints from source code and double check OpenAPI 3 YAML document with source code.
    generate_content_config=GenerateContentConfig(
        temperature=0.0,  # greedy decoding
        top_k=1,  # only the single most probable token
        top_p=1.0,  # include full probability mass
        seed=42  # fixed random seed for repeatability
    )

)

