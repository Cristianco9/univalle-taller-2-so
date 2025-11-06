import threading
import time
import random

# ================================================================
# ESTRUCTURAS DE DATOS PRINCIPALES
# ================================================================

class PCB:
    """
    Clase PCB (Process Control Block)
    Representa la estructura de control de un proceso (hilo).
    
    Atributos:
    ----------
    pid : int
        Identificador único del proceso.
    nombre : str
        Nombre del proceso o hilo.
    estado : str
        Estado actual del proceso: READY, RUNNING o TERMINATED.
    program_counter : int
        Contador de programa que simula el avance de instrucciones.
    stack : list
        Pila de ejecución donde se almacenan las últimas instrucciones.

    Métodos:
    --------
    push_stack(data):
        Inserta una instrucción en el stack.
    pop_stack():
        Extrae la última instrucción del stack.
    """
    
    def __init__(self, pid, nombre):
        self.pid = pid
        self.nombre = nombre
        self.estado = "READY"
        self.program_counter = 0
        self.stack = []

    def push_stack(self, data):
        """Agrega una nueva instrucción al stack del proceso."""
        self.stack.append(data)

    def pop_stack(self):
        """Elimina y retorna la última instrucción del stack, si existe."""
        if self.stack:
            return self.stack.pop()
        return None


# ================================================================
# FUNCIONES DE LOS HILOS (PROCESOS)
# ================================================================

def control_orientacion(pcb):
    """
    Simula el proceso encargado de controlar la orientación del satélite.
    Realiza tres ajustes de orientación consecutivos.
    """
    for i in range(3):
        pcb.estado = "RUNNING"                    # Estado activo
        pcb.program_counter += 1                  # Incremento del contador
        instruccion = f"Ajuste de orientación #{i+1}"
        pcb.push_stack(instruccion)               # Registrar en el stack
        mostrar_estado(pcb)                       # Mostrar estado actual
        time.sleep(random.uniform(0.4, 0.7))      # Simulación de tiempo de trabajo
    pcb.estado = "TERMINATED"                     # Proceso completado
    mostrar_estado(pcb)


def monitoreo_bateria(pcb):
    """
    Simula el monitoreo del nivel de batería del satélite.
    Genera tres lecturas aleatorias entre 50% y 100%.
    """
    for i in range(3):
        pcb.estado = "RUNNING"
        pcb.program_counter += 1
        nivel = random.randint(50, 100)
        instruccion = f"Nivel batería: {nivel}%"
        pcb.push_stack(instruccion)
        mostrar_estado(pcb)
        time.sleep(random.uniform(0.4, 0.7))
    pcb.estado = "TERMINATED"
    mostrar_estado(pcb)


def comunicacion_base(pcb):
    """
    Simula el envío de tres transmisiones hacia la estación base.
    """
    for i in range(3):
        pcb.estado = "RUNNING"
        pcb.program_counter += 1
        instruccion = f"Transmisión #{i+1} enviada"
        pcb.push_stack(instruccion)
        mostrar_estado(pcb)
        time.sleep(random.uniform(0.4, 0.7))
    pcb.estado = "TERMINATED"
    mostrar_estado(pcb)


# ================================================================
# PLANIFICADOR DE EVENTOS (SIMULADOR DE CPU)
# ================================================================

def planificador_eventos(pcbs):
    """
    Simula un planificador de tipo Round Robin básico.
    Itera sobre los procesos y les asigna CPU de forma rotativa,
    mostrando cuál se activa en cada ciclo.
    
    Parámetros:
    -----------
    pcbs : list[PCB]
        Lista con los bloques de control de proceso.
    """
    print("\n🛰️  INICIO DE SIMULACIÓN DEL CONTROL SATELITAL 🛰️")
    print("════════════════════════════════════════════════════════════\n")

    # Bucle principal: mientras exista al menos un proceso no terminado
    while any(pcb.estado != "TERMINATED" for pcb in pcbs):
        for pcb in pcbs:
            if pcb.estado != "TERMINATED":
                print(f"🕒 Planificador: Activando proceso '{pcb.nombre}' (PID={pcb.pid})")
                print("────────────────────────────────────────────────────────────\n")
                time.sleep(0.5)

    print("\n✅ Todos los procesos han finalizado.\n")


# ================================================================
# PRESENTACIÓN EN CONSOLA (INTERFAZ CLI)
# ================================================================

def mostrar_estado(pcb):
    """
    Muestra el estado actual del proceso en formato estructurado vertical,
    similar a un bloque JSON, pero más visual y claro.
    
    Parámetros:
    -----------
    pcb : PCB
        Objeto del proceso cuyo estado se desea visualizar.
    """
    print("🧩 PROCESO:", pcb.nombre)
    print("──────────────────────────────────────────")
    print(f"PID: {pcb.pid}")
    print(f"Estado: {pcb.estado}")
    print(f"Program Counter: {pcb.program_counter}")
    print("Stack (top 3):")
    
    # Mostrar solo las tres últimas instrucciones del stack
    if pcb.stack:
        for item in pcb.stack[-3:]:
            print(f"  - {item}")
    else:
        print("  (vacío)")
    
    print("──────────────────────────────────────────\n")


# ================================================================
# FUNCIÓN PRINCIPAL (MAIN)
# ================================================================

def main():
    """
    Punto de entrada principal del programa.
    Crea los procesos, lanza los hilos y ejecuta el planificador de eventos.
    """
    # Crear los bloques de control (PCB)
    pcb1 = PCB(1, "Control de Orientación")
    pcb2 = PCB(2, "Monitoreo de Batería")
    pcb3 = PCB(3, "Comunicación con la Base")

    # Crear los hilos que simulan los procesos
    t1 = threading.Thread(target=control_orientacion, args=(pcb1,))
    t2 = threading.Thread(target=monitoreo_bateria, args=(pcb2,))
    t3 = threading.Thread(target=comunicacion_base, args=(pcb3,))

    # Iniciar los hilos
    t1.start()
    t2.start()
    t3.start()

    # Ejecutar el planificador en paralelo
    planificador_eventos([pcb1, pcb2, pcb3])

    # Esperar a que todos los hilos finalicen
    t1.join()
    t2.join()
    t3.join()

    # Mostrar resumen final
    print("📊 ESTADO FINAL DE LOS PROCESOS:")
    print("════════════════════════════════════════════════════════════")
    for pcb in [pcb1, pcb2, pcb3]:
        mostrar_estado(pcb)


# ================================================================
# EJECUCIÓN DIRECTA
# ================================================================

if __name__ == "__main__":
    main()

