from Creational_Design_Pattern.Factory_Abstract_Pattern.FAB_Capital_City import CapitalCity

# Create Product B1
class Madrid(CapitalCity):
    def get_population(self):
        return 7854125
    
    def list_top_attraction(self):
        return ["Royal Place", "Prado Museum", "Retrio Park"]
    
    