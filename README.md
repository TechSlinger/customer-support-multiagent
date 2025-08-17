# Customer Support Multi-Agent System

A smart customer support automation system using multiple AI agents to classify, research, and resolve customer queries efficiently.

## Overview

This system uses three specialized AI agents:

- **🎯 Triage Agent**: Classifies customer tickets by category, priority, and tags
- **📚 Knowledge Agent**: Researches relevant information and documentation
- **🛠️ Support Agent**: Develops comprehensive step-by-step solutions

## Features

- ✅ Intelligent ticket classification
- ✅ Knowledge base research
- ✅ Automated solution generation  
- ✅ Response caching for efficiency
- ✅ Multi-step workflow processing

## Setup

### 1. Install Dependencies

```bash
# Create conda environment
conda create -n agents python=3.9
conda activate agents

# Install required packages
pip install agno mistralai python-dotenv
```

### 2. Get Mistral API Key

1. Visit [Mistral Console](https://console.mistral.ai/)
2. Sign up and create an API key
3. Copy your API key

### 3. Configure Environment

Create a `.env` file in the project directory:

```env
MISTRAL_API_KEY=your-mistral-api-key-here
```

## Usage

### Run the Workflow

```bash
python run_workflow.py
```

### Test with Custom Query

```python
from run_workflow import customer_support_workflow

response = customer_support_workflow.run(query="I can't access my account")
print(response)
```

## Project Structure

```
customer_support/
├── .env                 # Environment variables
├── agents.py           # Agent definitions
├── run_workflow.py     # Main workflow execution
└── README.md          # This file
```

## Example Queries

The system can handle various customer support scenarios:

- Account access issues: *"I can't log into my account, forgot my password"*
- Billing problems: *"My billing seems wrong, I was charged twice"*  
- Technical issues: *"The app keeps crashing when I upload files"*
- General inquiries: *"How do I reset my password?"*

## How It Works

1. **Classification**: Query is analyzed and categorized
2. **Research**: Relevant information is gathered from knowledge base
3. **Solution**: Step-by-step resolution is generated
4. **Caching**: Solutions are cached for faster future responses

## Configuration

### Agent Models

All agents use `open-mistral-nemo` model. You can modify the model in `agents.py`:

```python
model=MistralChat(id="open-mistral-nemo", api_key=MISTRAL_API_KEY)
```

### Environment Variables

Set via conda environment or `.env` file:

```bash
# Using conda
conda env config vars set MISTRAL_API_KEY=your-key
conda deactivate && conda activate agents

# Using .env file
echo "MISTRAL_API_KEY=your-key" > .env
```

## Troubleshooting

**401 Unauthorized Error:**
- Check your Mistral API key is correct
- Ensure `.env` file is in the project directory
- Verify the API key is properly loaded

**Module Import Errors:**
- Ensure all dependencies are installed: `pip install agno mistralai python-dotenv`
- Activate the correct conda environment: `conda activate agents`

## 🎬 Demo Screenshots
<img width="985" height="615" alt="image" src="https://github.com/user-attachments/assets/6b9eee30-8046-4098-a789-bf03f85e2f9d" />
<img width="1049" height="577" alt="image" src="https://github.com/user-attachments/assets/5def3cd6-f5d5-41ee-9de9-1b7bab048c25" />
<img width="1006" height="614" alt="image" src="https://github.com/user-attachments/assets/9e3bb065-6972-43ff-90cd-0077909e7112" />
<img width="1046" height="618" alt="image" src="https://github.com/user-attachments/assets/08fd5edb-d59d-4ced-9c31-eba63ad4f08e" />
<img width="1042" height="592" alt="image" src="https://github.com/user-attachments/assets/1ed64f78-7bbb-44fd-9f21-c24bd8892a4f" />
<img width="1049" height="608" alt="image" src="https://github.com/user-attachments/assets/95ee1c38-aac2-4f7a-993d-6c5b9f501819" />


