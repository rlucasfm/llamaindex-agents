from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.objects import ObjectIndex, SimpleToolNodeMapping
from agents import market_analyst, strategy_planner, creative_content_creator, photographer_agent, reviewer_agent

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo")

agents = {
    "Market_Analyst_agent": market_analyst(llm),
    "Strategy_Planner_agent": strategy_planner(llm),
    "Creative_Content_Creator_agent": creative_content_creator(llm),
    "Photographer_agent": photographer_agent(llm),
    "Reviewer_agent": reviewer_agent(llm),
}

query_engine_tools = []
for agent_name, agent in agents.items():
    tool = QueryEngineTool(
        query_engine=agent,
        metadata=ToolMetadata(
            name=f"tool_{agent_name}",
            description=f"This tool uses the {agent_name} agent to answear queries."
        )
    )
    query_engine_tools.append(tool)

tool_mapping = SimpleToolNodeMapping.from_objects(query_engine_tools)
obj_index = ObjectIndex.from_objects(
    query_engine_tools,
    tool_mapping
)

retriever = obj_index.as_retriever()

top_agent = OpenAIAgent.from_tools(
    tool_retriever=retriever,
    system_prompt=""" \
        You are a top-level agent designed to choose the most appropriate agent of the 5 agents provided in the object index based on the user query and use the appropriate agent to answer queries.
        Please ALWAYS choose the approprate agents among the 5 provided based on the user query to answer a question. Do NOT rely on prior knowledge.\

    """,
    verbose=True,
)

response = top_agent.query("Analise o mercado para uma nova agencia de IA, que planeja se estabelecer em Imperatriz - MA, Brasil.")