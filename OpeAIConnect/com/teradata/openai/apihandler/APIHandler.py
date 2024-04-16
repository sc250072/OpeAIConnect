from openai import OpenAI

from com.teradata.openai.prompt.PromptGenerator import PromptGenerator
from com.teradata.openai.util import Constants


class APIHandler:
    def __init__(self,
                 key: str,
                 li_table: list,
                 user_query: str) -> str:
        self.key = key
        self.li_table = li_table
        self.user_query = user_query

    def _get_msg(self):
        gen = PromptGenerator(self.li_table, self.user_query)
        msg = gen.generate_prompt()
        message = [
            {
                "role": "system",
                "content": msg.system
            },
            {
                "role": "user",
                "content": msg.user
            }
        ]
        print(message)
        return message

    def get_query(self):
        message = self._get_msg()
        client = OpenAI(api_key=self.key)
        response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=message,
                                                  temperature=0,
                                                  max_tokens=256)
        print(response)
        sql = response.choices[0].message.content
        print(sql)
        sql = sql.replace('```sql\n', '')
        sql = sql.replace('```', '')
        print(sql)
        return sql
