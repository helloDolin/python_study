class Singleton(object):
    __instance = None

    def __new__(cls):
        if Singleton.__instance == None:
            Singleton.__instance = object.__new__(cls)
        return Singleton.__instance


obj1 = Singleton()
obj2 = Singleton()

print(obj1)
print(obj2)
