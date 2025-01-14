from abc import ABC, abstractmethod

class ApiCompilable(ABC):
    """
    Interface de base pour des objets compilables en Prisma et GraphQL.
    """

    @abstractmethod
    def compile_to_prisma(self):
        """
        Méthode abstraite pour compiler en Prisma.
        """
        pass

    @abstractmethod
    def compile_to_graphql(self):
        """
        Méthode abstraite pour compiler en GraphQL.
        """
        pass