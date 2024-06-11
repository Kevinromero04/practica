import json
ruta = "registrados.json"

def carga ():
    try:
        with open(ruta, "r") as file:
            gato = json.load(file)
            print("datos guardados")
            return gato
    except Exception:
        print("Hubo un error")
        return {"registrados" : {}}

def guardar(data):
        with open(ruta, "w") as filo:
            json.dump(data, filo, indent=4)
        print("datos guardados")