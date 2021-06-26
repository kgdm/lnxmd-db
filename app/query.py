from typing import List, Optional
from pydantic import BaseModel
import uuid


class query:

    def insert(self, table: str, **kwargs):
        query_build = f"INSERT INTO {table}("
        columns = ""
        data = ""
        for k, v in kwargs.items():
            columns += f"{k},"
            data += f"{v},"
        if columns.endswith(","):
            columns = columns[:-1]
        if data.endswith(","):
            data = data[:-1]
        query_build += f"{columns}) VALUES ({data})"
        return query_build

    def update(self):
        pass

    def select(self, table: str, ):
        query_build = f"select from {table}"
