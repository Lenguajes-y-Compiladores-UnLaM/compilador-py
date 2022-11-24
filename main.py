import sys
from parser import sintactico
from assembly import asembler
import flags

def main(path):
    with open(path) as source:
        print("Comienzo de Compilacion\n...")
        data = source.read()  
        polaca = sintactico.parse(data)
        asembler.run(polaca)
    source.close()
    print("...\nFin de Compilacion")
    

if __name__ == "__main__":
    if(flags.save_output):
        with open('out/out.txt', 'w') as f:
            sys.stdout = f # Comentar para ver los logs
            main(sys.argv[1])
    else: main(sys.argv[1])
