from llama_index.core.agent import ReActAgent
from tools import internet_search_tool, instagram_search_tool

def market_analyst(llm):
    return ReActAgent.from_tools(
        tools=[internet_search_tool], 
        llm=llm, 
        max_iterations=5,
        verbose=True, 
        context="""\
            The primary role of this agent is to search about a company/product and analyze it's features, 
            providing in-depth insights to marketing strategies.
            """
        )

def strategy_planner(llm):
    return ReActAgent.from_tools(
        tools=[internet_search_tool], 
        llm=llm, 
        max_iterations=5,
        verbose=True, 
        context="""\
            The primary role of this agent is to synthesize amazing insights from product analysis
				to formulate incredible marketing strategies.
            """
        )


def creative_content_creator(llm):
    return ReActAgent.from_tools(
        tools=[internet_search_tool, instagram_search_tool], 
        llm=llm, 
        max_iterations=5,
        verbose=True, 
        context="""\
            The primary role of this agent is to develop compelling and innovative content
            for social media campaigns, with a focus on creating
            high-impact Instagram ad copies.
            """
        )

def photographer_agent(llm):
    return ReActAgent.from_tools(
        tools=[internet_search_tool, instagram_search_tool], 
        llm=llm,
        max_iterations=5,
        verbose=True, 
        context="""\
            The primary role of this agent is to take the most amazing photographs for instagram ads that
            capture emotions and convey a compelling message.
            """
        )

def reviewer_agent(llm):
    return ReActAgent.from_tools(
        tools=[internet_search_tool, instagram_search_tool], 
        llm=llm,
        max_iterations=5,
        verbose=True, 
        context="""\
            The primary role of this agent is to oversee the work done by your team to make sure it's the best
            possible and aligned with the product's goals, review, approve,
            ask clarifying question or delegate follow up work if necessary to make
            decisions
            """
        )