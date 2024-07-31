# PythonAgentAI using Llama Index and GPT-3.5-turbo
## Overview
This project leverages the Retrieval-Augmented Generation (RAG) approach to enable natural language querying of CSV data. By utilizing LlamaIndex 🦙, we ingest CSV data and provide users with the ability to enter natural language queries. These queries are then converted into Pandas queries, and the results are transformed into natural language outputs using OpenAI's GPT-3.5-turbo.

# What is Retrieval-Augmented Generation (RAG)?
Retrieval-Augmented Generation (RAG) is a method that combines the strengths of retrieval-based and generation-based models. It retrieves relevant information from a knowledge base and uses this context to generate more accurate and relevant responses. This approach enhances the capabilities of language models by grounding their responses in external data, improving accuracy and relevance.

# LlamaIndex 🦙
LlamaIndex is a powerful data framework designed for context-augmented LLM applications. It provides data connectors to ingest various data sources and formats, including APIs, PDFs, documents, and SQL databases. LlamaIndex also offers an advanced retrieval and query interface, allowing seamless integration with language models for context-augmented outputs.

# LlamaIndex Features
CSV Data Ingestion: Efficiently ingest CSV data using LlamaIndex.
Natural Language Querying: Enter natural language queries about the ingested data.
Query Conversion: Convert natural language queries into Pandas queries.
Context-Augmented Responses: Use GPT-3.5-turbo to generate natural language responses based on query results

## Setup
Add Credits to Your OpenAI Account:
Ensure you have sufficient credits in your OpenAI account. You can add credits by visiting the OpenAI billing page.

Generate an API Key and  Configure the .env File:
Create a .env file in the project root directory and add your OpenAI API key:
OPENAI_API_KEY=your-api-key

# Example Queries and Results

User Input:  what are the top 5 companies with the largest h1b filings
Pandas Query by Llama Index: df['EMPLOYER_NAME'].value_counts().head()
Output: 
The top 5 companies with the largest H1B filings are:
1. Ernst & Young U.S. LLP - 7262 filings
2. Amazon.com Services LLC - 6090 filings
3. Google LLC - 6067 filings
4. Microsoft Corporation - 3441 filings
5. COGNIZANT TECHNOLOGY SOLUTIONS US CORP - 3418 filings
-------------
User Input: what is the average prevailing wage of new york city employees in the h1b filing data?
Pandas Query by Llama Index: df[df['EMPLOYER_CITY'] == 'NEW YORK CITY']['PREVAILING_WAGE'].mean()
Output: The average prevailing wage of New York City employees in the H1B filing data is $143,998.

-------------
User Input:  what are all the different countries that the employers belong to?
Pandas Query by Llama Index: df['EMPLOYER_COUNTRY'].unique()
Output: The employers in the H1b filings belong to countries such as the United States of America, India, Georgia, Mexico, Angola, Afghanistan, Chile, Barbados, and Belgium.

-------------
