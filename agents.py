import google.generativeai as genai

class Agent:
    def __init__(self, api_key: str, role_description: str):
        genai.configure(api_key=api_key)
        self.role_description = role_description
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def _invoke_llm(self, prompt: str) -> str:
        """Helper to invoke the LLM with the given prompt."""
        response = self.model.generate_content(
            f"Role: {self.role_description}\n\nTask: {prompt}"
        )
        return response.text

class ResearchAgent(Agent):
    def run(self, company_name: str) -> str:
        prompt = f"Find and summarize key offerings and strategic focus areas for {company_name}. Also identify its main competitors and what they're doing with AI."
        print(f"🕵️‍♂️ Research Agent is working on: {company_name}...")
        research_summary = self._invoke_llm(prompt)
        return research_summary

class UseCaseAgent(Agent):
    def run(self, research_summary: str) -> str:
        prompt = f"""
        Based on this research summary:\n\n{research_summary}\n\nPropose 3-5 relevant and creative AI and GenAI use cases where the company can improve operations or customer experience. Explain the benefit of each case.
        """
        print("💡 Use Case Agent is generating proposals...")
        use_cases = self._invoke_llm(prompt)
        return use_cases

class ResourceAgent(Agent):
    def run(self, use_cases: str) -> str:
        prompt = f"""
        For each of the following use cases:\n\n{use_cases}\n\nSearch for relevant and publicly available datasets or code repositories on platforms like Kaggle, HuggingFace, and GitHub that could support the implementation. Provide a list of clickable links for each use case.
        """
        print("📦 Resource Agent is collecting assets...")
        resources = self._invoke_llm(prompt)
        return resources

class FinalProposalAgent(Agent):
    def run(self, research_summary: str, use_case_proposals: str, resource_assets: str) -> str:
        prompt = f"""
        You are a professional proposal writer. Your goal is to combine the provided information into a single, cohesive, and professional report in markdown format.

        The report must include the following sections:
        1. An executive summary.
        2. A summary of the market research and competitor analysis.
        3. A detailed list of the proposed AI/GenAI use cases.
        4. The resource assets (datasets, code links) to support the feasibility of each use case. Ensure all links are clickable.
        
        Use the following information:
        - Research Summary: {research_summary}
        - AI Use Cases: {use_case_proposals}
        - Resource Assets: {resource_assets}
        """
        print("📝 Proposal Writer Agent is drafting the final report...")
        final_proposal = self._invoke_llm(prompt)
        return final_proposal