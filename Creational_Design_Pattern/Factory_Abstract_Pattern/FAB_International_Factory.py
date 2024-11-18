from abc import ABC, abstractmethod
from Creational_Design_Pattern.Factory_Abstract_Pattern.FAB_language import Language
from Creational_Design_Pattern.Factory_Abstract_Pattern.FAB_Capital_City import CapitalCity


#Abstract_Factory

class InternationalFactory(ABC):
    @abstractmethod
    def create_language(self) -> Language:
        pass

    @abstractmethod
    def create_captial_city(self) -> CapitalCity:
        pass