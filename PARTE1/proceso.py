import psutil

def proceso():
    # Obtiene una lista de los procesos en ejecución
    procesos = psutil.process_iter()

    # Inicializa la variable para almacenar el proceso con mayor uso de memoria
    proceso_memoria = None

    # Iterar sobre la lista de procesos
    for proceso in procesos:
        try:
            # Obtiene el uso de memoria del proceso
            uso_memoria = proceso.memory_info().rss / (1024 * 1024)

            # Si el uso de memoria del proceso es mayor que el actual, actualiza la variable
            if proceso_memoria is None or uso_memoria > proceso_memoria.memory_percent():
                proceso_memoria = proceso

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Imprime el nombre y el uso de memoria del proceso con mayor uso
    if proceso_memoria is not None:
        print(f"El proceso con mayor uso de memoria es: {proceso_memoria.name()} ({proceso_memoria.memory_percent():.2f}%)")

proceso()