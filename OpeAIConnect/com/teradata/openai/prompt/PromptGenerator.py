from com.teradata.openai.teradataapi.teradata_api import TeradataApi
from com.teradata.openai.util import Constants


class Message:
    def __init__(message, system, user):
        message.system = system
        message.user = user


class PromptGenerator:
    def __init__(self,
                 table_name: str,
                 user_query: str) -> str:
        self.table_name = table_name
        self.user_query = user_query

    def generate_prompt(self) -> Message:
        api = TeradataApi()
        con = api.get_con()
        with con.cursor() as cur:
            cur.execute("show table %s" % self.table_name)
            rows = cur.fetchall()
            table_def = "".join([str(col).replace("\r", "\n") for col in rows[0]])
        system = Constants.system_template % table_def
        user = Constants.user_template % self.user_query
        return Message(system, user)
