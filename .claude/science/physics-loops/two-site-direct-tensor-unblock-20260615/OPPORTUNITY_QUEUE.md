# Opportunity Queue

1. Re-audit `LOCAL_TOMOGRAPHY_FROM_QUBIT_COMPLEX_STRUCTURE...`; simulation
   shows it becomes a critical ready row.
2. Re-audit `TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE...`; simulation shows it
   becomes a ready row.
3. If both pass audit, downstream rows waiting on the local-tomography/tensor
   carrier chain can be reconsidered without relying on the conditional
   multisite Pauli theorem.
