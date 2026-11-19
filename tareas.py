tareas=[]

def agregar_tareas(titulo):
    if not titulo.strip():
        raise ValueError("El titulo no puede estar vacio")
    tareas.append(titulo.strip())

def listar_tareas():
    return tareas

def eliminar_tarea(indice):
    return tareas.pop(indice)


