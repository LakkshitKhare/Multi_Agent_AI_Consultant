import os
from dotenv import load_dotenv
from agents import ResearchAgent, UseCaseAgent, ResourceAgent, FinalProposalAgent

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

class Orchestrator:
    def __init__(self):
        # Instantiate each agent with the API key
        self.researcher = ResearchAgent(
            api_key=API_KEY,
            role_description="You are a meticulous market researcher specializing in corporate strategy."
        )
        self.use_case_agent = UseCaseAgent(
            api_key=API_KEY,
            role_description="You are a creative AI strategist and consultant."
        )
        self.resource_agent = ResourceAgent(
            api_key=API_KEY,
            role_description="You are a diligent data engineer and asset collector."
        )
        self.proposal_writer = FinalProposalAgent(
            api_key=API_KEY,
            role_description="You are a professional proposal writer, known for clear and concise reports."
        )

    def run_workflow(self, company_name: str) -> str:
        print("\n--- Starting Agent Workflow ---")
        
        # Step 1: Research Agent
        research_output = self.researcher.run(company_name)
        
        # Step 2: Use Case Agent
        use_case_output = self.use_case_agent.run(research_output)
        
        # Step 3: Resource Agent
        resource_output = self.resource_agent.run(use_case_output)
        
        # Step 4: Final Proposal Agent
        final_proposal = self.proposal_writer.run(research_output, use_case_output, resource_output)
        
        print("\n--- Workflow Complete ---")
        
        return final_proposal