from typing import List, Optional
from pydantic import BaseModel
import uuid


class Users:

    def __init__(self, name: str, mail: str, password: str, img_url: str):
        self.id = uuid.uuid4()
        self.name = name
        self.mail = mail
        self.pwd = password
        self.bio_url = None
        self.bio_pic = img_url
