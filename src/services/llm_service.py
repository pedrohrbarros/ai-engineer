from langchain.agents import create_agent

from src.constants.knowledge_base import KNOWLEDGE_BASE

class LLMService:

    def __init__(self):
        self.agent = create_agent(
            model="google_genai:gemini-3.5-flash-lite",
            tools=[],
            verbose=True,
            system_prompt=f"""
                You are a helpful assistant that will answer questions about BEON.tech's mission using the following knowledge base:
                {KNOWLEDGE_BASE}
                """
        )

    def genereate_response(self, 
    prompt: str,
    ) -> str:
        result = self.agent.invoke(
            {
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        return result["messages"][-1].content_blocks
