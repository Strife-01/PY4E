class Test :
    name = ''
    def __init__(self, name) :
        self.name = name
    def dick(self) :
        print(f"{self.name} is a dick")
    def __del__(self) :
        print('Andrei rules')

obj = Test('Teo')

print(obj.name)
obj.dick()
