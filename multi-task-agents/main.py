from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
# from llama_index.llms.lmstudio import LMStudio
from agents import project_owner, senior_developer, tech_leader
from tasks import define_project_structure, define_solution, problem_analysis
import nest_asyncio

nest_asyncio.apply()
load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo")
# llm = LMStudio(
#     model_name="TheBloke/OpenHermes-2.5-Mistral-7B-GGUF",
#     base_url="http://localhost:1234/v1",
#     temperature=0.7,
#     timeout=0
# )

# Contratar agentes
agents = {
    "Project_Owner": project_owner(llm),
    "Techleader": tech_leader(llm),
    "Senior_Developer": senior_developer(llm)
}

# Executar tarefas
def execute_task(task):
    curr_agent = task["agent"]
    return curr_agent.query(task["query"])


# # Cliente chega na agencia de IA :v
# Input do client
problem = "Can't find a way to encounter good mechanics that know how to fix my old car."
info = "I live in a little city, and is not so common to find old cars here."

# Executar primeira tarefa
print("---- Executing first task ----")
res_1 = execute_task(problem_analysis(agents["Project_Owner"], problem, info))
print(f"First task output: {res_1}")

# Executar segunda tarefa
print("---- Executing second task ----")
res_2 = execute_task(define_solution(agents["Project_Owner"], problem, res_1))
print(f"Second task output: {res_2}")

# Executar terceira tarefa
print("---- Executing third task ----")
res_3 = execute_task(define_project_structure(agents["Techleader"], res_2))
print(f"Third task output: {res_3}")