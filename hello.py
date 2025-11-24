import qiskit
from qiskit import QuantumCircuit
# NEW: Import Aer from the separate package
from qiskit_aer import AerSimulator 

# 1. Create a Quantum Circuit (2 qubits, 2 classical bits)
qc = QuantumCircuit(2, 2)

# 2. Add gates (Bell State)
qc.h(0)
qc.cx(0, 1)


qc.measure([0, 1], [0, 1])


simulator = AerSimulator()


job = simulator.run(qc, shots=1000)
result = job.result()


counts = result.get_counts(qc)
print("Counts:", counts)