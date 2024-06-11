import carga_guarda as gg
def registros():
    brr = gg.carga()
    documento = int(input("documento: "))
    if str(documento) in brr["registrados"]:
        print("Ya hay un ususario registrado")
    else:
        dic= {}
        dic["Nombre"] = str(input("Nombre: "))
        dic["Apellido"] = str(input("Apellido: "))
        dic["Numero"] = str(input("Numero: "))
        dic["Estado"] = ""
        brr["registrados"][documento]=dic
        gg.guardar(brr)
        print("usuario registrado")

registros()