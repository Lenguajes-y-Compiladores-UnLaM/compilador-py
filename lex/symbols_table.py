class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Symbol():
    def __init__(self, dict):
        self.value = dict['value']
        self.name = dict['name']
        self.typeOf = dict['typeOf']
        self.length = dict['length']
        
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return f'Symbol(value: {self.value}; name: {self.name}; type: {self.typeOf}; len: {self.length})'

class SymbolsTable(metaclass=SingletonMeta):
    table = []
    nextIndex = 0
    
    def append(self, symbol):
        # Verifica si ya existe, sino esta lo agrega
        toAppend = Symbol(symbol)
        if not any(el.name == toAppend.name for el in self.table):
            self.table.append(toAppend)
            self.nextIndex += 1
            return self.getLastIndex()
        else:
            return self.getIndexByName(toAppend.name)
        
    def getLastIndex(self):
        return self.nextIndex - 1
        
    def get(self):
        return self.table
        
    def getByIndex(self, idx):
        return self.table[idx]
       
    def getIndexByName(self, name):
        # Buscar el simbolo con ese nombre y lo retorna(o su indice)
        index = [idx for idx, el in enumerate(self.table) if el.name == name]
        return index[0]
    
    def setValue(self, idx, value):
        # Agrega valor y longitud al simbolo
        self.table[idx].value = value
        self.table[idx].length = len(value)

    def __str__(self):
        str = ''
        for el in self.table:
            str = str + f'{el.__repr__()}\n'
        return str