from England_Factory import EnglandFactory
from Spanish_Factory import SpanishFactory


#client

def main():
    factory = EnglandFactory()
    language = factory.create_language()
    capital_city = factory.create_captial_city()

    print(f"Language: {language.__class__.__name__}")

    print(f"Greet: {language.greet()}")

    print(f"Captial City: {capital_city.__class__.__name__}")

    print(f"Total Population: {capital_city.get_population()}")

    print(f"Top Attreaction: {capital_city.list_top_attraction()}")

if __name__ == '__main__':
    main()