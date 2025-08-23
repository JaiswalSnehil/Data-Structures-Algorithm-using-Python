class Calculator:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_string(cls, value_str):
            return cls(int(value_str))
    
    @staticmethod 
    def add(a, b):
         return a + b

calc = Calculator.from_string("10")
print(Calculator.add(10,20))