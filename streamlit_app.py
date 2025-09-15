import streamlit as st
from orchestrator import Orchestrator
import os

st.set_page_config(page_title="Multi-Agent AI Consultant", layout="centered")

st.title("💡 Multi-Agent AI Consultant")
st.markdown("### Generate AI/GenAI Use Cases for Any Company")
st.markdown("This app leverages a team of specialized agents to conduct market research and propose innovative AI solutions.")

# Create the reports directory if it doesn't exist
if not os.path.exists("reports"):
    os.makedirs("reports")

# User input for the company name
company_name = st.text_input("Enter the company or industry name:", "Apple")

if st.button("Start Analysis", type="primary"):
    if not company_name:
        st.warning("Please enter a company or industry name to begin.")
    else:
        # A main status container to track overall progress
        main_status = st.status(f"Starting analysis for **{company_name}**...", expanded=True)

        try:
            orchestrator = Orchestrator()

            # --- Live Status Updates for Each Agent ---
            # 1. Research Agent
            with main_status.container():
                st.write("🕵️‍♂️ **Research Agent** is working on it...")
                research_output = orchestrator.researcher.run(company_name)
                st.success("✅ Research complete!")

            # 2. Use Case Agent
            with main_status.container():
                st.write("💡 **Use Case Agent** is generating proposals...")
                use_case_output = orchestrator.use_case_agent.run(research_output)
                st.success("✅ Use cases generated!")

            # 3. Resource Agent
            with main_status.container():
                st.write("📦 **Resource Agent** is collecting assets...")
                resource_output = orchestrator.resource_agent.run(use_case_output)
                st.success("✅ Resources collected!")
            
            # 4. Final Proposal Agent
            with main_status.container():
                st.write("📝 **Proposal Writer** is drafting the final report...")
                final_proposal = orchestrator.proposal_writer.run(research_output, use_case_output, resource_output)
                st.success("✅ Final proposal drafted!")

            main_status.update(label=f"Analysis complete for **{company_name}**!", state="complete", expanded=False)
            
            st.markdown("---")
            st.subheader("Final Proposal")
            st.markdown(final_proposal)

            # Save the report to a file in the reports directory
            file_path = f"reports/{company_name.replace(' ', '_')}_proposal.md"
            with open(file_path, "w") as f:
                f.write(final_proposal)
            st.download_button(
                label="Download Proposal",
                data=final_proposal,
                file_name=file_path,
                mime="text/markdown"
            )

        except Exception as e:
            main_status.update(label="❌ Analysis failed.", state="error")
            st.error(f"An error occurred: {e}")
            st.info("Please check your API key and internet connection.")