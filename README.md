# PythonAgentAI using Llama Index and GPT-3.5-turbo
Overview
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

# Setup
Add Credits to Your OpenAI Account:
Ensure you have sufficient credits in your OpenAI account. You can add credits by visiting the OpenAI billing page.

Generate an API Key and  Configure the .env File:
Create a .env file in the project root directory and add your OpenAI API key:
OPENAI_API_KEY=your-api-key
