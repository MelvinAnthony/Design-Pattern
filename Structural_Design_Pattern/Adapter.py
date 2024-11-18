
#Two Different data Types

class Old():
    def get(self):
        return "string"
    
class New():
    def get(self):
        return 123
class Adapter():
    def __init__(self,cls):
        self.cls = cls

    def get(self):
        return str(self.cls.get())

def main(obj):
    print("This Result is: "+ obj.get())

if __name__ == '__main__':
    obj1 = Adapter(New())
    main(obj1)