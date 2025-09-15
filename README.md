# AI Use Case Generation System

## Project Overview

This project is a multi-agent system designed to act as an AI consultant. It automates market research and proposes relevant AI and Generative AI (GenAI) use cases for a given company or industry. The system is built from scratch using a **raw approach** without a dedicated agent framework, providing full control over the workflow. The final output is a professional report that can be viewed and downloaded by the user.

## Core Features

  * **Sequential Multi-Agent Pipeline**: The system uses four specialized agents—a Researcher, a Use Case Generator, a Resource Collector, and a Proposal Writer—that work together in a predefined, sequential workflow.
  * **LLM Integration**: The system directly leverages the official `google-generativeai` library to interact with the Gemini API, ensuring a lightweight and stable connection.
  * **Intuitive User Interface**: A Streamlit front-end provides a simple web interface for users to input a company name.
  * **Live Progress Tracking**: The UI offers real-time status updates, showing what each agent is doing as it progresses through the pipeline.
  * **Report Generation**: The final output is a well-formatted markdown report that can be viewed in the app and downloaded as a file.

## Getting Started

### Prerequisites

  * Python 3.10 or later
  * A Google API key for the Gemini API

### Local Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/007abhishek/ai_consulting_agent.git
    cd ai_consulting_agent
    ```
2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment**:
      * On Windows: `.\venv\Scripts\activate`
      * On macOS/Linux: `source venv/bin/activate`
4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  Create a file named `.env` in the project's root directory.
2.  Add your Gemini API key to the file in the following format:
    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```

### Running the Application

1.  Ensure your virtual environment is active.
2.  Run the Streamlit application from your terminal:
    ```bash
    streamlit run streamlit_app.py
    ```
3.  The application will open automatically in your web browser.

## Project Structure

The project is organized to be clean and modular.

```
.
├── .env                  # Environment variables for API keys
├── streamlit_app.py      # The main Streamlit UI and entry point
├── agents.py             # Defines the specialized agent classes
├── orchestrator.py       # Manages the agent workflow and data flow
├── reports/              # Directory to save generated reports
├── requirements.txt      # Project dependencies
└── README.md             # This file
```

## How It Works

The `Orchestrator` class is the central control system. It initializes each agent and then calls their respective `run()` methods in a specific order. The output from one agent is passed as a string to the next agent as input, creating a simple yet powerful sequential pipeline. This raw approach provides transparency and full control over the entire process.

## Demo & Hosted App

  * **Demo Video (Loom):** [https://www.loom.com/share/b5d7d9e4a3c14d59a2f7c0a9e7f8e8b0](https://www.google.com/search?q=https://www.loom.com/share/b5d7d9e4a3c14d59a2f7c0a9e7f8e8b0)
  * **Hosted App:** [[https://ai-consultant-agent.streamlit.app/](https://www.google.com/search?q=https://ai-consultant-agent.streamlit.app/)]

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://www.google.com/search?q=https://github.com/007abhishek/ai_consulting_agent/issues) if you want to contribute.

## License

This project is licensed under the [MIT License](https://www.google.com/search?q=https://github.com/007abhishek/ai_consulting_agent/blob/main/LICENSE).
