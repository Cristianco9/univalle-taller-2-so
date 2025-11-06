# 🛰️ Simulador de Control de Satélite con Hilos y Planificador Round Robin

## 📘 Descripción

Este proyecto implementa un simulador de control de satélite utilizando **hilos en Python**.  
Simula procesos concurrentes y un **planificador Round Robin** con estructuras de **PCB** 
(Process Control Block) y **Stack** por proceso.  
El sistema muestra en consola el estado de ejecución de cada proceso de forma estructurada.

## ⚙️ Características

- 3 hilos principales:
  - SensorThread: simula lecturas de sensores.
  - ControlThread: procesa lecturas.
  - CommunicationThread: transmite telemetría.
- Planificador Round Robin básico.
- PCB y Stack independientes por hilo.
- Sincronización con Locks.
- Salida estructurada en consola.
- Solo usa la biblioteca estándar de Python.


## 🚀 Ejecución del Proyecto

Requisitos:
- Python 3.8 o superior

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Cristianco9/univalle-taller-2-so.git
   ```

2. Ejecuta el programa:
   ```
   python3 src/satellite_sim.py
   ```

## 🧩 Planificador Round Robin

El planificador Round Robin asigna un **quantum de tiempo** fijo a cada proceso.  
Cuando un proceso agota su quantum, pasa al final de la cola y el siguiente obtiene el control.

Ventajas:
- Distribución equitativa del CPU.
- Evita bloqueos por procesos largos.
- Fácil de implementar.

## 📊 Ejemplo de salida

```
==============================
[Proceso: SensorThread]

PID: 1

Estado: RUNNING

Quantum restante: 2

Contador de programa: 10

Stack:

Read sensor data

Update PCB

[Proceso: ControlThread]

PID: 2

Estado: READY

Quantum restante: 3

Contador de programa: 8

Stack:

Waiting sensor data

Calculate control output
==============================
```

## 🧠 Conceptos prácticos

- Programación concurrente con hilos.
- Estructura PCB y Stack.
- Planificación Round Robin.
- Sincronización de procesos.

## 👨‍💻 Autor

**Cristian Camilo Cortes Ortiz**

Desarrollador de Software

202478542
