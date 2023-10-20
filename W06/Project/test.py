from screeninfo import get_monitors

def obtener_resolucion_monitor_actual():
    # Obtiene una lista de todos los monitores conectados
    monitores = get_monitors()

    if monitores:
        # El primer monitor en la lista es el monitor principal
        monitor_principal = monitores[0]
        ancho = monitor_principal.width
        alto = monitor_principal.height
        return [ancho,alto]
    else:
        return "No se encontraron monitores."

if __name__ == "__main__":
    resolucion = obtener_resolucion_monitor_actual()
    print(resolucion)
