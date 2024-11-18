from abc import ABC, abstractmethod

#Abstract_Product_A
class Language(ABC):
    @abstractmethod
    def greet(self) -> str:
        pass

    