from Dataclass.front.frontCompilable import FrontCompilable
from Dataclass.front.page import Page


class Front(FrontCompilable):
    """
    Représente un composant front contenant une liste de pages.
    """

    def __init__(self):
        self.pages = []

    def add_page(self, page):
        if not isinstance(page, Page):
            raise TypeError("La page doit être une instance de Page.")
        self.pages.append(page)

    def compile_to_flutter(self):
        """
        Méthode abstraite pour compiler en Prisma.
        """
        pass

    def compile_to_angular(self):
        """
        Méthode abstraite pour compiler en GraphQL.
        """
        pass