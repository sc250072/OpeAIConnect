# OpeAIConnect
This project aims to create SQL queries from natural language. 
This sample proof of concept (POC) is centered around the employee table, which is already present in the provided Teradata instance. 
It employs the OpenAI gpt-3.5-turbo language model to generate SQL queries based on human input. 
The process involves using the "show table" statement to retrieve the table structure, which is then utilized to construct prompts for the language model. 
The model generates SQL query statements, which are subsequently submitted to Teradata for execution. The results are then displayed as output.
