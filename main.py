import sys
from parser import sintactico

def main(path):
    with open(path) as source:
        data = source.read()  
        polaca = sintactico.parse(data)
        for (i, item) in enumerate(polaca):
            print(i, item)
    source.close()
    

if __name__ == "__main__":
    # with open('out/out.txt', 'w') as f:
    #   sys.stdout = f # Comentar para ver los logs
        main(sys.argv[1])
