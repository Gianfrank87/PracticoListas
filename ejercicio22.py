from jedi_data import jedi_list # <-- ¡Importación de los datos!
# -----------------------------------------------------------------

def listar_jedi(jedi_list):
    """Función auxiliar para mostrar la información de un Jedi de forma legible."""
    for jedi in jedi_list:
        print(f"  - Nombre: {jedi['nombre']}")
        print(f"    Especie: {jedi['especie']}")
        print(f"    Maestros: {', '.join(jedi['maestros']) if jedi['maestros'] else 'Ninguno'}")
        print(f"    Sables: {', '.join(jedi['sables'])}\n")
    if not jedi_list:
        print("  (Ningún Jedi encontrado para este criterio)")

# a. listado ordenado por nombre y por especie;
def a_listar_ordenado(data):
    orden_nombre = sorted(data, key=lambda jedi: jedi['nombre'])
    orden_especie = sorted(data, key=lambda jedi: jedi['especie'])
    return orden_nombre, orden_especie

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
def b_buscar_por_nombre(data, nombres):
    resultados = []
    for nombre in nombres:
        jedi = next((j for j in data if j['nombre'].lower() == nombre.lower()), None)
        if jedi:
            resultados.append(jedi)
    return resultados

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
def c_padawans_de_maestros(data, maestros):
    padawans = []
    for jedi in data:
        for maestro in maestros:
            # Comprobación más robusta
            if maestro.lower() in [m.lower() for m in jedi['maestros']]:
                padawans.append(jedi)
                break
    return padawans

# d. mostrar los Jedi de especie humana y twi'lek;
def d_jedi_por_especie(data, especies):
    return [jedi for jedi in data if jedi['especie'] in especies]

# e. listar todos los Jedi que comienzan con A;
def e_jedi_que_empiezan_con(data, letra):
    return [jedi for jedi in data if jedi['nombre'].startswith(letra)]

# f. mostrar los Jedi que usaron sable de luz de más de un color;
def f_jedi_multi_sable(data):
    return [jedi for jedi in data if len(jedi['sables']) > 1]

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
def g_jedi_por_color_sable(data, colores):
    resultados = []
    for jedi in data:
        if any(color in jedi['sables'] for color in colores):
            resultados.append(jedi)
    return resultados

# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
def h_padawans_por_nombre_maestro(data, maestros):
    padawans_completos = c_padawans_de_maestros(data, maestros)
    return [jedi['nombre'] for jedi in padawans_completos]


# -----------------------------------------------------------------
# --- Programa principal ---
# -----------------------------------------------------------------

print("="*60)
print("Resolución de Actividades (Lista de Jedi importada)")
print("="*60)

# a. listado ordenado por nombre y por especie
orden_nombre, orden_especie = a_listar_ordenado(jedi_list)
print("a. Listado Ordenado por Nombre:")
listar_jedi(orden_nombre)
print("-"*25)
print("a. Listado Ordenado por Especie:")
listar_jedi(orden_especie)
print("="*60)

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto
jedi_buscados = b_buscar_por_nombre(jedi_list, ["Ahsoka Tano", "Kit Fisto"])
print("b. Información de Ahsoka Tano y Kit Fisto:")
listar_jedi(jedi_buscados)
print("="*60)

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices
padawans_maestros = c_padawans_de_maestros(jedi_list, ["Yoda", "Luke Skywalker"])
print("c. Padawans de Yoda y Luke Skywalker:")
listar_jedi(padawans_maestros)
print("="*60)

# d. mostrar los Jedi de especie humana y twi'lek
jedi_especies = d_jedi_por_especie(jedi_list, ["Humano", "Twi'lek"])
print("d. Jedi de especie Humana y Twi'lek:")
listar_jedi(jedi_especies)
print("="*60)

# e. listar todos los Jedi que comienzan con A
jedi_a = e_jedi_que_empiezan_con(jedi_list, "A")
print("e. Jedi que comienzan con 'A':")
listar_jedi(jedi_a)
print("="*60)

# f. mostrar los Jedi que usaron sable de luz de más de un color
jedi_multi = f_jedi_multi_sable(jedi_list)
print("f. Jedi con sables de más de un color:")
listar_jedi(jedi_multi)
print("="*60)

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta
jedi_colores = g_jedi_por_color_sable(jedi_list, ["amarillo", "violeta"])
print("g. Jedi con sable de luz Amarillo o Violeta:")
listar_jedi(jedi_colores)
print("="*60)

# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron
nombres_padawans = h_padawans_por_nombre_maestro(jedi_list, ["Qui-Gon Jinn", "Mace Windu"])
print("h. Nombres de Padawans de Qui-Gon Jinn y Mace Windu:")
if nombres_padawans:
    print(f"  - Padawans encontrados: {', '.join(nombres_padawans)}")
else:
    print("  (No se encontraron padawans directos para esos maestros en los datos)")
print("="*60)