from Creational_Design_Pattern.Factory_Abstract_Pattern.FAB_Capital_City import CapitalCity

# Create Product B1
class London(CapitalCity):
    def get_population(self):
        return 89000000
    
    def list_top_attraction(self):
        return ["Tower Bridge", "Backinghm Palace", "Big Ben"]
    
