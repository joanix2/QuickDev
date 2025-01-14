from abc import ABC, abstractmethod

class FrontCompilable(ABC):
    """
    Interface de base pour des objets compilables en Prisma et GraphQL.
    """

    @abstractmethod
    def compile_to_flutter(self):
        """
        Méthode abstraite pour compiler en Prisma.
        """
        pass

    @abstractmethod
    def compile_to_angular(self):
        """
        Méthode abstraite pour compiler en GraphQL.
        """
        pass