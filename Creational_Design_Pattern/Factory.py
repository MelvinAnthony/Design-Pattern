class A():
    def __init__(self):
        pass

    def methodA(self):
        return "This is Method A"

class B():
    def __init__(self):
        pass

    def methodB(self):
        return "This is Method B"

def get(obj=''):
    objs = dict(
        a = A(),
        b = B()
    )
    return objs[obj]


a = get('a')
b = get('b')

print(a.methodA())

print(b.methodB())