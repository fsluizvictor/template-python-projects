from datetime import datetime 

class MyClass:

    __slots__=['uid', 'createdAt', 'modifiedAt']

    def __init__(self, uid: str, createdAt: datetime, modifiedAt: datetime):
        self.uid = uid
        self.createdAt = createdAt
        self.modifiedAt = modifiedAt
