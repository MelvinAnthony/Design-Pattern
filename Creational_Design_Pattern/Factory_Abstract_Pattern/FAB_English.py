from Creational_Design_Pattern.Factory_Abstract_Pattern.FAB_language import Language

# Create Product 1

class English(Language):
    def greet(self) -> str:
        return "Hello!"