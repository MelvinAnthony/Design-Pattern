from abc import ABC, abstractmethod

#Abstract_Product_B
class CapitalCity(ABC):
    @abstractmethod
    def get_population(self) -> int:
        pass

    @abstractmethod
    def list_top_attraction(self):
        pass

    