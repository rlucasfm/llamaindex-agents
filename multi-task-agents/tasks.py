def Task(description, agent, expected_output):
    return {
        "agent": agent,
        "query": f"""\
            {description}

            Your final answear must be {expected_output}
        """
    }

def problem_analysis(agent, problem_description, aditional_info):
    return Task(
        agent=agent, 
        description=f"""\
            Analyze the problem in the <prob> tag: <prob>{problem_description}</prob>
            Extra info provided about it are provided inside the <add> tag: <add>{aditional_info}</add>

            Search the internet to try to understand deply the problem and it's causes and effects.
            Understand how a software can solve this problem in the most effective way
            and be a sellable software.

            If you can't find any useful info in the internet, answear with your own knowledge.

            Your final report should be a list of 3 possible solutions, describing each solution
            as a software, with it's features and key details.

            Keep in mind, attention to detail is crucial for
			a comprehensive analysis. It's currenlty 2024.
        """,
        expected_output="""\
            A list of 3 solutions ONLY, following this example:
            1. ...
            2. ...
            3. ...
        """
    )

def define_solution(agent, problem_description, solutions):
    return Task(
        agent=agent,
        description=f"""\
            Given this solutions : {solutions}\n
            That solves this problems: {problem_description}

            Understanding the problem, select from the suggested solutions the best one, that better fit
            the described problems and have the best commercial appeal.
        """,
        expected_output="""The selected solution in the format:
            Solution: ...
            Key Features: 
                - ...
                - ...
        """
    )

def define_project_structure(agent, solution):
    return Task(
        agent=agent,
        description=f"""\
            Given the solution: {solution}

            Using popular software architectures, define the best architecture and structure to 
            apply for the software implementing the given solution. Think about scale and software quality,
            and deploying that software in the cloud.
        """,
        expected_output="""A detailed description about the project architecture and structure following this example:
        Architecture: ...
        Folder Structure: ...
        Extra info: ...
        """
    )
