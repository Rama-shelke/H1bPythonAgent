from dotenv import load_dotenv
load_dotenv()
import os
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
h1b_data_path = os.path.join("data", "filtered_h1b_data.csv")
h1b_df = pd.read_csv(h1b_data_path)

#PandasQueryEngine: convert natural language to Pandas python code using LLMs.
#The input to the PandasQueryEngine is a Pandas dataframe, and the output is a response.
h1b_query_engine = PandasQueryEngine(
    df=h1b_df, verbose=True, instruction_str=instruction_str
)

# Updates the prompt templates used by the query engine to guide how it processes and responds to queries.
h1b_query_engine.update_prompts({"pandas_prompt": new_prompt})


tools = [
    note_engine,
    QueryEngineTool(
        query_engine=h1b_query_engine,
        metadata=ToolMetadata(
            name="h1b_data",
            description="this csv file has details of h1b filings made by the employers",
       ),
  
  )
]



llm = OpenAI(model="gpt-3.5-turbo")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
