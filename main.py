from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from api_tools import pokemon_engine

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo")

champions_path = os.path.join('data', 'champions.csv')
champions_df = pd.read_csv(champions_path)

champions_query_engine = PandasQueryEngine(df=champions_df, verbose=True, instruction_str=instruction_str, llm=llm)
champions_query_engine.update_prompts({"pandas_prompt": new_prompt})

# champions_query_engine.query("What is the champion with the lowest HP?")

tools = [
    note_engine,
    pokemon_engine,
    QueryEngineTool(
        query_engine=champions_query_engine, 
        metadata=ToolMetadata(
            name="champion_data",
            description="this gives information about League of Legends champions, including their Champion Name, Role, Base Health, Base Mana, Base Armor, Base Attack Damage and Gold Efficiency"
        ),
    ),
]

agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input('Enter a prompt (q to quit): ')) != 'q':
    result = agent.query(prompt)
    print(result)