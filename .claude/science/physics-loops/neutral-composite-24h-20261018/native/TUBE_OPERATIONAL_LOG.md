# Operational record

Initial tube variational run reached L3 with energy -10.994240777497456 and residual estimate 1.95e-6, then failed saving because optional quimb joblib dependency was absent. No scientific conclusion follows. Root replaced local generated-state persistence with standard-library pickle and tightened local eigensolver tolerance from default .001 to 1e-10 and compression from1e-11to1e-13 before rerun. Energy-convergence flag alone is not a stationarity certificate. Initial exact tube/Lanczos runs L3..7 completed; those nodes still need convergence and reconstructed-vector checks.

Finite runner dependency cleanup first failed because boundary probe imported mpo after extracting pure rung model. Replaced its two-rung MPO conversion with the identical explicit Kronecker Hamiltonian; no model change. Aggregate replay required.
