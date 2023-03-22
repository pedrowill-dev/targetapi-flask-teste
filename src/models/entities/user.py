from dataclasses import dataclass

@dataclass
class User:

    username: str
    password: str

    def __repr__(self):
        return str(self.__dict__)   






