from Creational_Design_Pattern.Factory_Abstract_Pattern.FAB_language import Language

# Create Product 2

class Spanish(Language):
    def greet(self) -> str:
        return "Hola!"