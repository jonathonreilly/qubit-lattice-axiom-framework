#!/usr/bin/env python3
"""Finite Hermitian endpoint checks on three supplied decimal basin triples.
No basin completeness, physical selection, or upstream closure is certified.
Historical integration source is recoverable at f24d17d97d372df977476e4a69674577f31af575.
"""
from __future__ import annotations
import math
import numpy as np

AUDIT_TIMEOUT_SEC = 120

E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0
GAMMA = 0.5

T_M = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex)
T_D = np.array([[0.0, -1.0, 1.0], [-1.0, 1.0, 0.0], [1.0, 0.0, -1.0]], dtype=complex)
T_Q = np.array([[0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0]], dtype=complex)
H_BASE = np.array(
    [
        [0.0, E1, -E1 - 1j * GAMMA],
        [E1, 0.0, -E2],
        [-E1 + 1j * GAMMA, -E2, 0.0],
    ],
    dtype=complex,
)

BASIN_1 = (0.657061342210, 0.933806343759, 0.715042329587)
BASIN_2 = (28.005676879468, 20.721919153777, 5.011726669406)
BASIN_X = (21.128264303040, 12.680028385305, 2.089234625632)


def h_of(point):
    m, d, q = point
    return H_BASE + m*T_M + d*T_D + q*T_Q

def main():
    results = []
    def check(label, condition, detail=""):
        ok = bool(condition)
        results.append(ok)
        print(f"{'PASS' if ok else 'FAIL'} {label} {detail}")
    base_eig = np.linalg.eigvalsh(H_BASE)
    base_inertia = (int(np.sum(base_eig > 0)), int(np.sum(base_eig < 0)))
    check("supplied baseline is Hermitian", np.array_equal(H_BASE,H_BASE.conj().T))
    check("supplied baseline inertia is (1,2)", base_inertia == (1,2), str(base_eig))
    for name, point, expected_inertia in [
        ("Basin 1", BASIN_1, (1,2)),
        ("Basin 2", BASIN_2, (2,1)),
        ("Basin X", BASIN_X, (2,1)),
    ]:
        H = h_of(point)
        eig = np.linalg.eigvalsh(H)
        det = np.linalg.det(H)
        inertia = (int(np.sum(eig > 0)), int(np.sum(eig < 0)))
        check(name+" supplied endpoint Hermitian", np.array_equal(H,H.conj().T))
        check(name+" finite eigenvalues separated from zero", np.all(np.isfinite(eig)) and min(abs(eig)) > 1e-6, str(eig))
        check(name+" determinant agrees with spectral product", abs(det-np.prod(eig)) < 1e-9*max(1,abs(det)), str(det))
        check(name+" supplied endpoint inertia", inertia == expected_inertia, str(inertia))
        if name == "Basin 1":
            check("Basin 1 supplied chamber inequality", point[1]+point[2] > E1)
    print("Finite decimal endpoint checks only. Equal inertia does not select a physical source or certify the specified affine path.")
    print(f"TOTAL: PASS={sum(results)} FAIL={len(results)-sum(results)}")
    return 0 if all(results) else 1
if __name__ == '__main__':
    raise SystemExit(main())
