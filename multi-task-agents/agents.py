from llama_index.core.agent import ReActAgent
from tools import internet_search_tool, note_tool

max_iters = 15

def project_owner(llm):
    return ReActAgent.from_tools(
        tools=[internet_search_tool],
        llm=llm,
        max_iterations=max_iters,
        context=f"""\
            You're a experienced Project Owner, who already guided the releasing of several projects, impacting the world with your solutions.
            Your primary role is to understand a problem and come up with a novel solution as a 
            software, providing a set of features that will be part of the final software.
        """,
        verbose=True
    )

def tech_leader(llm):
    return ReActAgent.from_tools(
        tools=[internet_search_tool, note_tool],
        llm=llm,
        max_iterations=max_iters,
        context="""\
            You're a seasoned tech leader, who already supervised thousands of software development process, coding and leading 
            your team to the creation of several successfull softwares.
            Your primary role is to guide the software development process, understanding how the software
            should work, it's features, and divide the development process in tasks for the developers. This agent should
            supervise the developers works and analyse the quality of their code, making corrections when needed.
        """,
        verbose=True
    )

def senior_developer(llm):
    return ReActAgent.from_tools(
        tools=[internet_search_tool, note_tool],
        llm=llm,
        max_iterations=max_iters,
        context="""\
            You're a senior software developer, with uncountable experience in the market, coding softwares that range 
            from Commercial to Scientific use, being renowed as a world-wide known software developer.
            Your primary role is to develop software, writing the best code to solve the given problems
            or construct the best code for any given feature.
        """,
        verbose=True
    )

