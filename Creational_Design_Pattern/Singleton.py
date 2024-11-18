                                                    #1. without Singletone
# class Singletone:
#     pass

# obj = Singletone()
# obj2 = Singletone()

# print(obj)
# print(obj2)

# print(obj == obj2)

                                                                # 2. with Singletone without function inherit

# class Singletone:
#     __instance = None

#     def __new__(cls):
#         print(cls)
#         return 1

# obj = Singletone()
# obj2 = Singletone()

# print(obj)
# print(obj2)

# print(obj == obj2)


                                                    # 3. Singletone with function inherit

class Singletone:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
obj = Singletone()
obj2 = Singletone()

print(obj)
print(obj2)

print(obj == obj2)
