from com.teradata.openai.prompt.PromptGenerator import PromptGenerator
from com.teradata.openai.util.Logging import Logging


class Environment:
    def __init__(self, key, endpoint, model_name):
        self.key = key
        self.endpoint = endpoint
        self.model_name = model_name


class APIHandler(Logging):
    def __init__(self,
                 env: Environment,
                 li_table: list,
                 user_query: str) -> None:
        self.env = env
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
        self.log.debug(message)
        return message

    def get_query(self):
        return ""
