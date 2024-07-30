from llama_index.core import PromptTemplate


instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a correct solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression.
    6. Here are some examples. 
    Input: "How many employers are located in Philadelphia?" Output: df[df['EMPLOYER_CITY'] == 'PHILADELPHIA'].shape[0]
    Input: How many certified cases are there for full-time positions?  Output: df[(df[`CASE_STATUS`] == `Certified`) & (df[`FULL_TIME_POSITION`] == `Y`)].shape[0]"""

new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}


    Expression: """
)

context = """Purpose: The primary role of this agent is to assist users by providing accurate 
            information about H1b visa filing statistics by different employers. """
