from FAB_Capital_City import CapitalCity
from FAB_International_Factory import InternationalFactory
from FAB_language import Language
from FAB_English import English
from FAB_London import London

#concerate Factory 1

class EnglandFactory(InternationalFactory):
    def create_language(self) -> Language:
        return English()
    
    def create_captial_city(self) -> CapitalCity:
        return London()