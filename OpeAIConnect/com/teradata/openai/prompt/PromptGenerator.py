from com.teradata.openai.teradataapi.teradata_api import TeradataApi
from com.teradata.openai.util import Constants
from com.teradata.openai.util.Logging import Logging


class Message:
    def __init__(message, system, user):
        message.system = system
        message.user = user


class PromptGenerator(Logging):
    def __init__(self,
                 li_table: list,
                 user_query: str) -> str:
        self.li_table = li_table
        self.user_query = user_query

    def generate_prompt(self) -> Message:
        table_def = self._get_tables_def()
        system = Constants.system_template % table_def
        user = Constants.user_template % self.user_query
        return Message(system, user)

    def _get_tables_def(self) -> str:
        api = TeradataApi()
        con = api.get_con()
        query = ''
        try:
            for table_name in self.li_table:
                with con.cursor() as cur:
                    cur.execute("show table %s" % table_name)
                    rows = cur.fetchall()
                    table_def = "".join([str(col).replace("\r", "\n") for col in rows[0]])
                    query = query + "\n" + table_def
            print(query)
        except Exception as ex:
            self.log.error(str(ex))
            print(str(ex))
        return query
