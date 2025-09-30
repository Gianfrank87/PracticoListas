######## EJERCICIO 6 #######

from super_heroes_data import superheroes

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, data):
        nuevo = Nodo(data)
        if not self.head:
            self.head = nuevo
        else:
            aux = self.head
            while aux.next:
                aux = aux.next
            aux.next = nuevo

    def eliminar(self, nombre):
        ant, aux = None, self.head
        while aux:
            if aux.data["name"].lower() == nombre.lower():
                if ant:
                    ant.next = aux.next
                else:
                    self.head = aux.next
                return True
            ant = aux
            aux = aux.next
        return False

    def buscar(self, nombre):
        aux = self.head
        while aux:
            if aux.data["name"].lower() == nombre.lower():
                return aux.data
            aux = aux.next
        return None

    def recorrer(self):
        aux = self.head
        while aux:
            yield aux.data
            aux = aux.next


# --- Programa principal ---

lista = ListaEnlazada()
for sh in superheroes:
    # aca añado la casa marvel a todos los personajes para evitar errores que no supe como resolver
    sh["casa"] = "Marvel"
    lista.agregar(sh)

print("a) Eliminar Linterna Verde:")
# Aca me daba error de que no estaba en la lista.
if lista.eliminar("Linterna Verde"):
    print("Linterna Verde eliminado")
else:
    print("Linterna Verde no estaba en la lista")

print("\nb) Año de aparición de Wolverine:")
wolverine = lista.buscar("Wolverine")
if wolverine:
    print(wolverine["first_appearance"])
else:
    print("Wolverine no encontrado")

print("\nc) Cambiar la casa de Dr Strange a DC (para demostrar el cambio):")
dr_strange = lista.buscar("Dr Strange")
if dr_strange:
    # Cambie la casa de Dr Strange a "DC" (para probar el cambio)
    dr_strange["casa"] = "DC"  
    print(dr_strange)
else:
    print("Dr Strange no encontrado")
    
if not dr_strange:
    dr_strange = lista.buscar("Dr. Strange") 

print("\nd) Superhéroes cuya biografía menciona 'traje' o 'armadura':")
for sh in lista.recorrer():
    bio = sh["short_bio"].lower()
    if "traje" in bio or "armadura" in bio:
        print(sh["name"])

print("\ne) Nombre y casa de superhéroes anteriores a 1963:")
for sh in lista.recorrer():
    if sh["first_appearance"] < 1963:
        casa = sh.get("casa", "No definida")
        print(sh["name"], "-", casa)

print("\nf) Casa de Capitana Marvel y Mujer Maravilla:")
# Capitana Marvel y Mujer Maravilla no existen.
for nombre in ["Capitana Marvel", "Mujer Maravilla"]:
    sh = lista.buscar(nombre)
    if sh:
        print(nombre, "->", sh.get("casa", "No definida"))
    else:
        print(nombre, "no encontrado")

print("\ng) Info de Flash y Star-Lord:")
for nombre in ["Flash", "Star-Lord"]:
    sh = lista.buscar(nombre)
    if sh:
        print(sh)
    else:
        print(nombre, "no encontrado")

print("\nh) Superhéroes que comienzan con B, M o S:")
for sh in lista.recorrer():
    if sh["name"].startswith(("B", "M", "S")):
        print(sh["name"])

print("\ni) Cantidad de superhéroes por casa:")
conteo = {}
for sh in lista.recorrer():
    casa = sh.get("casa", "No definida")
    conteo[casa] = conteo.get(casa, 0) + 1
print(conteo)