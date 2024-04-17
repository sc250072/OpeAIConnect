import os

import teradatasql

from com.teradata.openai.util.Logging import Logging


class TeradataApi(Logging):
    def __init__(self):
        self.host = os.getenv("TERADATA_HOST", "localhost")
        self.username = os.getenv("TERADATA_USER", "dbc")
        self.password = os.getenv("TERADATA_PASSWORD", "dbc")

    def get_con(self):
        if self.host is None or self.username is None or self.password is None:
            raise Exception("Please enter hostname, username and password")
        return teradatasql.connect(host=self.host, user=self.username, password=self.password)

    def get_table_names(self, db_name) -> list:
        con = self.get_con()
        tbl_list = []
        if db_name is not None:
            query = "SELECT TableName FROM DBC.TablesV WHERE TableKind = 'T' AND DatabaseName = '" + db_name + "'"
            with con.cursor() as cur:
                cur.execute(query)
                tables = cur.fetchall()
                for table_name in tables:
                    name = db_name + "." + table_name[0]
                    tbl_list.append(name)
        return tbl_list

