import carga_guarda as gg
import camper_c_g as brr
def camper ():
    rhlm = gg.carga()
    docu = int(input("documento: "))
    if str(docu) in rhlm["registrados"]:
        nota = int(input("digite la nota: "))
        if nota >= 101:
            print("la nota debe ser del 1 al 100")
        elif nota <= 59:
            rhlm["registrados"][str(docu)]["Estado"] = "denegado"
            gg.guardar(rhlm)
        elif nota >= 60:
            rhlm["registrados"][str(docu)]["Estado"] = "aprobado"
            gg.guardar(rhlm)
    else: 
        print("el usuario no existe")
def mueve():
    rhlm = gg.carga()
    uaa = brr.carga_camp()
    docu = int(input("necesitamos que lo confirme: "))
    if str(docu) in rhlm["registrados"]:
        rhlm["campers"] = rhlm.pop("registrados")
        usuario =rhlm["campers"][str(docu)]
        if usuario["Estado"] == "aprobado":
            uaa["campers"] = usuario
            brr.guardar_camp(uaa)
            rhlm["registrados"] = rhlm.pop("campers")
            rhlm["registrados"].pop(str(docu))
            gg.guardar(rhlm)
        elif usuario["Estado"] == "denegado":
            rhlm["registrados"] = rhlm.pop("campers")
            rhlm["registrados"].pop(str(docu))
            gg.guardar(rhlm)
    else:
        print("documento equivocado")

mueve()