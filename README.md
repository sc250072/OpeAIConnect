# OpeAIConnect
This project aims to create SQL queries from natural language. 
This sample proof of concept (POC) is centered around the employee table, which is already present in the provided Teradata instance. 
It employs the OpenAI gpt-3.5-turbo language model to generate SQL queries based on human input. 
The process involves using the "show table" statement to retrieve the table structure, which is then utilized to construct prompts for the language model. 
The model generates SQL query statements, which are subsequently submitted to Teradata for execution. The results are then displayed as output.

Here are the steps for executing the project:

   1. Clone the project using the command "git clone".
   2. Open the project in PyCharm.
   3. Configure the Run Configurations for "main.py".
   4. Set up the Teradata instance details and OpenAI API key as environment variables with the following key names:
      1. TERADATA_HOST=whomooz;
      2. TERADATA_USER=guest;
      3. TERADATA_PASSWORD=please;
      4. OPENAI_KEY=key