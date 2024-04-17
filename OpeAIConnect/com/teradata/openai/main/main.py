import logging
import os

from dotenv import load_dotenv

from com.teradata.openai.apihandler.AzureOpenAIHandler import AzureOpenAIHandler
from com.teradata.openai.teradataapi.teradata_api import TeradataApi
from com.teradata.openai.util.Logging import Logging


class Main(Logging):
    def __init__(self):
        load_dotenv()
        logging.basicConfig(filename='poc.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        key = os.getenv("AZURE_OPENAI_API_KEY")
        user_query = os.getenv("USER_QUERY")
        db_name = os.getenv("TERADATA_USER")
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        tapi = TeradataApi()
        tbl_list = []
        if db_name is not None:
            tbl_list = tapi.get_table_names(db_name)
            api = AzureOpenAIHandler(key, azure_endpoint, tbl_list, user_query)
            query = api.get_query()
            con = tapi.get_con()
            try:
                with con.cursor() as cur:
                    cur.execute(query)
                    rows = cur.fetchall()
                    for row in rows:
                        self.log.info(row)
            except Exception as ex:
                self.log.error(str(ex))
        else:
            raise Exception("Please provider a valid username")


