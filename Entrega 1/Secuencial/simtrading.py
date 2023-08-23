import sys
import os
import gc
from Scanner import Scanner
    


def main():
    # sys.argv[0] es el nombre del script en sí mismo, los argumentos comienzan desde sys.argv[1]
    parsed_args = {"-p": None, "-f": None, "-m": None}    

    if len(sys.argv) > 3:
        for arg in sys.argv:
            if arg.startswith("-p="):
                parsed_args["-p"] = arg.split("=")[1]

            elif arg.startswith("-f="):
                parsed_args["-f"] = arg.split("=")[1]
            elif arg.startswith("-m="):
                parsed_args["-m"] = arg.split("=")[1]

        
        print("Período:", parsed_args["-p"])
        print("Formato:", parsed_args["-f"])
        print("Moneda:", parsed_args["-m"])

    else:
        print("Se necesitan al menos 3 argumentos.")
        return(1)

    scanner = Scanner()
    nombre_archivo = ruta = f"{parsed_args['-m']}_{parsed_args['-p']}.{parsed_args['-f'].lower()}"

    if parsed_args["-f"] == "CSV":
        
        #ruta = f".\MonedasCSV\{parsed_args['-m']}_{parsed_args['-p']}.{parsed_args['-f'].lower()}"
        ruta = os.path.join('.\MonedasCSV', nombre_archivo)
        print("Ruta: ",ruta)
        scanner.leer_csv(ruta)
        
        

    elif parsed_args["-f"] == "JSON":
        
        ruta = os.path.join('.\MonedasJSON', nombre_archivo)
        print("Ruta: ",ruta)
        scanner.leer_json(ruta)

    else:
        print("Formato de archivo NO valido.")
        return(1)

    del scanner    # Liberar manualmente el objeto lector
    gc.collect()  # Invocar al recolector de basura
    print("Se ha eliminado el scanner csv de la memoria")



    
if __name__ == "__main__":
    main()

