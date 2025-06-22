# api-breaking-change-detector

Install ADK:

```
 pip install -r requirements.txt
```

Run the following command to launch the dev UI.

```
adk web
```


## About the Project

API Contract Breaking Change Validator

Our multi-agent system monitors microservice APIs, detecting and warning about breaking changes in CI pipelines for every Git commit, preventing integration failures and speeding development.

Inspiration
-----------

In the world of microservices, a simple change to an API endpoint can have a ripple effect, causing unforeseen issues and breaking consumer applications. Manually tracking these changes is error-prone and inefficient. Our inspiration came from the need to automate the detection of these "breaking changes." We envisioned a system that could proactively warn developers about the potential impact of their code changes, ensuring a more stable and reliable development lifecycle. We were particularly inspired by the principles of Consumer-Driven Contract Testing (CDC) but wanted to create a more integrated and automated solution.

What it does
------------

The API Contract Breaking Change Validator is a multi-agent system designed to automatically detect breaking changes in API endpoints within a microservices architecture. When a developer commits new code, our system is triggered within the CI/CD pipeline. It intelligently analyses the code, identifies API endpoint definitions, and compares them against the existing versions. If a breaking change is detected—such as a modified field, a removed endpoint, or a change in response structure—the system immediately flags it and can even halt the pipeline, preventing the problematic code from being deployed. This provides an essential safety net for development teams.

How we built it
---------------

Our solution is built upon a sophisticated multi-agent architecture, orchestrated using the Agent Development Kit (ADK). The system is comprised of several specialised agents working in concert:

*   **Orchestrator Agent:** This is the central coordinator that manages the workflow.
    
*   **GitHub Agent (Repository Agent):** This agent is responsible for fetching the source code from different branches of a Git repository.
    
*   **Spring Boot Agent (Framework Agent):** This agent, powered by a Large Language Model (LLM), is an expert in the Spring Boot framework. It analyses the fetched code to identify controllers and extract API endpoint definitions, ideally in the OpenAPI format.
    
*   **OpenAPI Agent (API Contract Agent):** This agent compares the two sets of API contracts (from the old and new branches) to detect any breaking changes.
    
*   **Reporter Agent:** Once changes are identified, this agent generates a human-readable report detailing the breaking changes.
    

The entire system is designed to be deployed on Google Cloud and integrated seamlessly into a GitLab CI/CD pipeline. We utilised the gitingest library to help process the source code into a format that the LLM could easily understand.

Challenges we ran into
----------------------

One of the most significant challenges was designing the "Framework Agent." Teaching an LLM to reliably and accurately parse source code to find all API controllers and extract their precise definitions is a complex task. It required careful prompt engineering and a deep understanding of how to structure the input for the LLM to get consistent results. Another challenge was the integration with the CI/CD pipeline, ensuring that our agent system could be triggered reliably and could provide feedback (success or failure) back to the pipeline in a timely manner. Finally, setting up a robust testing strategy for a multi-agent system presented its own unique set of hurdles.

Accomplishments that we're proud of
-----------------------------------

We are incredibly proud of the multi-agent architecture we designed. The modularity of having specialised agents for specific tasks (repository interaction, framework analysis, contract comparison) makes the system flexible and extensible. We successfully implemented the core agents, including the repository agent using gitingest and the orchestrator to manage the flow. A major accomplishment was successfully deploying a sample version of our ADK project on Google Cloud, making it accessible for testing and demonstration. This proved that our concept was viable and could be realised in a real-world cloud environment.

What we learned
---------------

This project was a deep dive into the practical application of multi-agent systems and the Agent Development Kit. We learned a great deal about the nuances of designing and building collaborative agents. A key takeaway was the power of LLMs in understanding and processing complex information like source code, but also the challenges in ensuring their accuracy and reliability. We also gained valuable hands-on experience in deploying and integrating such a system with CI/CD pipelines on Google Cloud, highlighting the importance of a solid infrastructure for development and testing.

What's next for API Contract Breaking Change Validator
------------------------------------------------------

The future for our validator is bright. The immediate next steps involve completing the implementation of the Framework Agent, API Contract Agent, and Reporter Agent to fully realise the end-to-end vision. We plan to enhance the system's accuracy and expand its support to other programming languages and frameworks beyond Spring Boot. We also aim to make the generated reports more insightful and actionable for developers. Ultimately, we envision this tool becoming an indispensable part of any modern CI/CD pipeline, ensuring API stability and fostering better collaboration between teams in a microservices environment. We also plan to contribute our findings and potentially some of our tools back to the open-source community.

