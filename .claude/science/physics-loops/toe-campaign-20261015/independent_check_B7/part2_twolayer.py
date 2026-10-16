"""Part 2: two-layer (block / shifted-block) covariant walks W(k) = G(k) uBt G(k)^dag uA,
uA, uBt in commutant of D (uBt = INV uB INV, uB in commutant of shifted action INV D INV).
Check covariance + unitarity exactly-in-floating-point; scan spectrum dependence on k."""
import numpy as np, sys
from scipy.linalg import expm
from walks import *

rng = np.random.default_rng(1)
def rand_comm_unitary(C, scale=1.0):
    # random Hermitian in commutant (commutant is a *-algebra), exponentiate
    H = sum((rng.normal() + 1j * rng.normal()) * X for X in C)
    H = (H + H.conj().T) / 2
    return expm(1j * scale * H)

for ci in [0, 1, 2, 3]:
    D = class_D(ci)
    C = commutant_basis(list(D.values()))
    uA = rand_comm_unitary(C); uBt = rand_comm_unitary(C)
    A = two_layer(uA, uBt)
    print(f"class {ci}: cov defect {covariance_defect(A, D):.1e} unit defect {unitarity_defect(A):.1e}"
          f" max site displacement {site_disp_max(A)}")
    # spectrum variation
    ks = rng.uniform(-np.pi, np.pi, (200, 3))
    spec = [np.sort(np.angle(np.linalg.eigvals(symbol(A, k)))) for k in ks]
    spec = np.array(spec)
    print("   spread of quasienergies across k (per sorted band):", np.round(spec.max(0) - spec.min(0), 3))
    print("   W(0) eigen-phases:", np.round(np.sort(np.angle(np.linalg.eigvals(symbol(A, np.zeros(3))))), 4))
