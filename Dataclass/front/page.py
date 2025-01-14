from Dataclass.front.frontCompilable import FrontCompilable


class Page(FrontCompilable):
    """
    Représente une page dans le composant front.
    """

    def __init__(self, name, components=None):
        self.name = name
        self.components = components if components else []

    def add_component(self, component):
        self.components.append(component)

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