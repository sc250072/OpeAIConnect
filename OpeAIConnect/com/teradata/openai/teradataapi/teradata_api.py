import os

import teradatasql


class TeradataApi:
    def __init__(self):
        self.host = os.getenv("TERADATA_HOST", "localhost")
        self.username = os.getenv("TERADATA_USER", "dbc")
        self.password = os.getenv("TERADATA_PASSWORD", "dbc")

    def get_con(self):
        if self.host is None or self.username is None or self.password is None:
            raise Exception("Please enter hostname, username and password")
        return teradatasql.connect(host=self.host, user=self.username, password=self.password)
