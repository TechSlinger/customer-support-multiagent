from agents import (
    support_agent,
    triage_agent,
    knowledge_agent,
)
from agno.utils.log import log_info
from agno.workflow.v2 import Workflow

def cache_solution(workflow: Workflow, query: str, solution: str):
    if "solutions" not in workflow.workflow_session_state:
        workflow.workflow_session_state["solutions"] = {}
    workflow.workflow_session_state["solutions"][query] = solution

def customer_support_execution(workflow: Workflow, query: str) -> str:
    # Check cache first
    cached_solution = workflow.workflow_session_state.get("solutions", {}).get(query)
    if cached_solution:
        log_info(f"Cache hit! Returning cached solution for query: {query}")
        return cached_solution
    
    log_info(f"No cached solution found for query: {query}")
    
    # Step 1: Classify the ticket
    log_info("Step 1: Classifying customer query...")
    classification_response = triage_agent.run(query)
    classification = classification_response.content
    
    # Step 2: Research knowledge base
    log_info("Step 2: Researching knowledge base...")
    research_context = f"""
    Customer Query: {query}
    
    Classification: {classification}
    
    Please search for relevant information, documentation, and similar cases 
    that could help resolve this customer issue.
    """
    research_response = knowledge_agent.run(research_context)
    research_info = research_response.content
    
    # Step 3: Develop solution
    log_info("Step 3: Developing solution...")
    solution_context = f"""
    Customer Query: {query}
    
    Classification: {classification}
    
    Research Information: {research_info}
    
    Please provide a clear, step-by-step solution for this customer issue.
    Make sure to format it in a customer-friendly way with clear instructions.
    Use the research information to provide the most accurate and helpful solution.
    """
    solution_response = support_agent.run(solution_context)
    solution = solution_response.content
    
    # Cache the solution
    cache_solution(workflow, query, solution)
    
    return solution

# Create the customer support workflow
customer_support_workflow = Workflow(
    name="Customer Support Resolution Pipeline",
    description="AI-powered customer support with intelligent caching and knowledge base research",
    steps=customer_support_execution,
    workflow_session_state={},  # Initialize empty session state
)

if __name__ == "__main__":
    test_queries = [
        "I can't log into my account, forgot my password",
        "How do I reset my password?",
        #"My billing seems wrong, I was charged twice",
        "The app keeps crashing when I upload files",
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{'='*50}")
        print(f"Processing Query {i}: {query}")
        print('='*50)
        
        response = customer_support_workflow.run(query=query)
        print(f"Response: {response.content}")