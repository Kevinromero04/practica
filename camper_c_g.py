import json
ruta = "campers.json"

def carga_camp ():
    try:
        with open(ruta, "r") as file:
            gato = json.load(file)
            print("datos guardados")
            return gato
    except Exception:
        print("Hubo un error")
        return {"campers" : {}}

def guardar_camp(data):
        with open(ruta, "w") as filo:
            json.dump(data, filo, indent=4)
        print("datos guardados")