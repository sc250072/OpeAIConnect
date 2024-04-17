import logging
import os

from dotenv import load_dotenv

from com.teradata.openai.apihandler.APIHandler import Environment
from com.teradata.openai.apihandler.AzureOpenAIHandler import AzureOpenAIHandler
from com.teradata.openai.teradataapi.teradata_api import TeradataApi
from com.teradata.openai.util.Logging import Logging


def validate():
    key = os.getenv("AZURE_OPENAI_API_KEY")
    user_query = os.getenv("USER_QUERY")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    if key is None or user_query is None or azure_endpoint is None:
        raise Exception("Please provide Azure OpenAI API key, end point and user question")


class Main(Logging):

    def __init__(self):
        pass

    def main(self):
        load_dotenv()
        key = os.getenv("AZURE_OPENAI_API_KEY")
        user_query = os.getenv("USER_QUERY")
        db_name = os.getenv("TERADATA_USER")
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        azure_model_name = os.getenv("AZURE_OPENAI_MODEL")
        validate()
        tapi = TeradataApi()
        env = Environment(key, azure_endpoint, azure_model_name)
        if db_name is not None:
            tbl_list = tapi.get_table_names(db_name)
            api = AzureOpenAIHandler(env, tbl_list, user_query)
            query = api.get_query()
            con = tapi.get_con()
            try:
                with con.cursor() as cur:
                    cur.execute(query)
                    rows = cur.fetchall()
                    if len(rows) > 0:
                        for row in rows:
                            self.log.info(row)
                            print(row)
                    else:
                        self.log.info("No data exists")
                        print("No data exists")
            except Exception as ex:
                self.log.error(str(ex))
        else:
            raise Exception("Please provider a valid username")


if __name__ == "__main__":
    main = Main()
    main.main()
