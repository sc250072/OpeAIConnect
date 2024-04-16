import os

from com.teradata.openai.apihandler.APIHandler import APIHandler
from com.teradata.openai.teradataapi.teradata_api import TeradataApi
from dotenv import load_dotenv


load_dotenv()
key = os.getenv("OPENAI_KEY")
user_query = os.getenv("USER_QUERY")
tbl_list = ["student.student_details", "student.course_details"]
api = APIHandler(key, tbl_list, user_query)
query = api.get_query()
#query = "SELECT * FROM airflow.employee"
tapi = TeradataApi()
con = tapi.get_con()
with con.cursor() as cur:
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
