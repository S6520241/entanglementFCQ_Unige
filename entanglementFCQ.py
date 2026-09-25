import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

simulator = AerSimulator()
shots_sim = 10000

print("--- Risultati Home Assignment 4 ---")

qc1 = QuantumCircuit(2, 2)
qc1.ry(2 * np.arccos(np.sqrt(0.4)), 0) # Imposta qubit 0
qc1.x(1)
qc1.h(1) # Imposta qubit 1 a |-\rangle
qc1.measure([0,1], [0,1])
qc1_transpiled = transpile(qc1, simulator)
counts1 = simulator.run(qc1_transpiled, shots=shots_sim).result().get_counts()

print(f"Risultati Punto 1 (Stato Separabile): {counts1}")
qc2 = QuantumCircuit(2, 2)
qc2.h(0)
qc2.cx(0, 1)
qc2.measure([0,1], [0,1])
qc2_transpiled = transpile(qc2, simulator)
counts2 = simulator.run(qc2_transpiled, shots=shots_sim).result().get_counts()

print(f"Risultati Punto 2a (|Phi+>): {counts2}")
qc3 = QuantumCircuit(2, 2)
qc3.x(0)
qc3.x(1)
qc3.h(0)
qc3.cx(0, 1)
qc3.measure([0,1], [0,1])
qc3_transpiled = transpile(qc3, simulator)
counts3 = simulator.run(qc3_transpiled, shots=shots_sim).result().get_counts()

print(f"Risultati Punto 2c (|Psi->): {counts3}")