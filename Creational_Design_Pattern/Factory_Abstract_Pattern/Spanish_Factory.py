from FAB_Capital_City import CapitalCity
from FAB_International_Factory import InternationalFactory
from FAB_language import Language
from FAB_Spanish import Spanish
from FAB_Madrid import Madrid

#concerate Factory 1

class SpanishFactory(InternationalFactory):
    def create_language(self) -> Language:
        return Spanish()
    
    def create_captial_city(self) -> CapitalCity:
        return Madrid()