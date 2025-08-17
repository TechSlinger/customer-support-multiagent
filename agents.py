from agno.agent import Agent
from agno.models.mistral import MistralChat
import os
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

triage_agent = Agent(
    name="Ticket Classifier",
    model=MistralChat(id="open-mistral-nemo", api_key=MISTRAL_API_KEY),
    instructions="""
    You are a customer support ticket classifier. Your job is to analyze customer queries and extract key information.
    
    For each customer query, provide:
    1. Category (billing, technical, account_access, product_info, bug_report, feature_request)
    2. Priority (low, medium, high, urgent)
    3. Key tags/keywords (extract 3-5 relevant terms)
    4. Brief summary of the issue
    
    Format your response as:
    Category: [category]
    Priority: [priority] 
    Tags: [tag1, tag2, tag3]
    Summary: [brief summary]
    """,
    show_tool_calls=True,
    markdown=True

)

knowledge_agent = Agent(
    name="Knowledge Base Researcher",
    model=MistralChat(id="open-mistral-nemo", api_key=MISTRAL_API_KEY),
    instructions="""
    You are a knowledge base researcher for customer support. Your job is to find and compile 
    relevant information from available resources to help solve customer issues.
    
    Based on the classified ticket information, provide:
    1. Relevant knowledge base articles or documentation
    2. Common solutions for similar issues
    3. Known troubleshooting steps
    4. Related FAQ items
    5. Any warnings or special considerations
    
    If you cannot find specific information, suggest general approaches or indicate 
    what additional information might be needed.
    
    Format your response clearly with sections for easy reference by the solution developer.
    """,
    show_tool_calls=True,
    markdown=True
)

support_agent = Agent(
    name="Solution Developer",
    model=MistralChat(id="open-mistral-nemo", api_key=MISTRAL_API_KEY),
    instructions="""
    You are a solution developer for customer support. Your job is to create clear, 
    step-by-step solutions for customer issues.
    
    Based on research and knowledge base information, create:
    1. Clear problem diagnosis
    2. Step-by-step solution instructions
    3. Alternative approaches if the main solution fails
    4. Prevention tips for the future
    
    Make solutions customer-friendly with numbered steps and clear language.
    Include any relevant screenshots, links, or additional resources.
    """,
    show_tool_calls=True,
    markdown=True
)