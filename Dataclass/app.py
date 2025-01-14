from Dataclass.back.api import Api
from Dataclass.front.front import Front

class App:
    """
    Représente une application contenant une API et un composant front.
    """

    def __init__(self, api, front):
        if not isinstance(api, Api):
            raise TypeError("L'API doit être une instance de Api.")
        if not isinstance(front, Front):
            raise TypeError("Le front doit être une instance de Front.")
        self.api = api
        self.front = front