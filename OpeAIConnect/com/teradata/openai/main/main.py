import os

from com.teradata.openai.apihandler.APIHandler import APIHandler
from com.teradata.openai.teradataapi.teradata_api import TeradataApi


key = os.getenv("OPENAI_KEY")
api = APIHandler(key, "airflow.employee", "How many employees are there?")
query = api.get_query()
#query = "SELECT * FROM airflow.employee"
tapi = TeradataApi()
con = tapi.get_con()
with con.cursor() as cur:
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
