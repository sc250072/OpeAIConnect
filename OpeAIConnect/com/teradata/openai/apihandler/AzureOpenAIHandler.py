import os
import re
import logging

from openai.lib.azure import AzureOpenAI

from com.teradata.openai.apihandler.APIHandler import APIHandler


class AzureOpenAIHandler(APIHandler):
    def __init__(self, key: str, endpoint: str, li_table: list, user_query: str):
        super().__init__(key, li_table, user_query)
        self.endpoint = endpoint

    def get_query(self):
        message = self._get_msg()
        client = AzureOpenAI(
            api_key=self.key,
            api_version="2024-02-01",
            azure_endpoint=self.endpoint
        )
        response = client.chat.completions.create(model="gpt-35-turbo",
                                                  messages=message,
                                                  temperature=0,
                                                  max_tokens=256)
        sql = response.choices[0].message.content
        # Extracting sql from response got from Azure OpenAI using regular expression. Query is embedded between ```
        try:
            pattern = r"```(.*?)```"
            sql = re.findall(pattern, sql, re.DOTALL)[0]
        except Exception as ex:
            logging.error(str(ex))
        return sql
