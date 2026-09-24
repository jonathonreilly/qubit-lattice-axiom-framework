#!/usr/bin/env python3
"""Record readout locality, read as local tomography, admits the ordinary composite and excludes the graded one.

Setting (all supplied readings, none adopted). The Record axiom says only records are readable and a readout
value is determined by record content alone; records lock one admissible local possibility. Read as a statement
about reconstructions (D-tomo): the joint pre-record state of several sites is determined by the odds it gives
to local record menus and their joint frequencies. This runner certifies, in finite dimensions, what that reading
admits and what it excludes, on the one-site algebra M_2(C) named by the Qubit axiom.

1. Ordinary composite M_2(C) (x) M_2(C) = M_4(C): a random two-site state is reconstructed exactly from the 16
   joint frequencies of local record menus along four tetrahedral axes, and from the 16 local Pauli products;
   dimension count 15 = 3 + 3 + 9. Three sites: 63 = 9 + 27 + 27.
2. Generated algebra: the words in the commuting local copies span all of M_4(C) (16 complex dimensions), and for
   three sites M_8(C) (64). This is the landed generated-composition theorem, rechecked.
3. Graded composite (two fermionic modes with parity superselection): the local readable algebras are
   span{1, n_i}; the four local products fix 3 of the 7 real parameters of a parity-block-diagonal state; the
   states (|01> + |10>)/sqrt2 and (|01> - |10>)/sqrt2 have identical local-product statistics but trace distance 1.
   Read as two qubits (ungraded), sigma^x (x) sigma^x separates them; the mode-1 raising operator anticommutes with
   the mode-2 one, and sigma^x_1 anticommutes with the mode-1 parity, so it is not a local observable of the graded
   composite. So the graded composite fails the reading.
4. The reading alone leaves the state set open: W = (1 + X X + Y Y + Z Z)/4 has 16 local-product coordinates,
   valid marginals, is positive on every product effect (minimum 0, at antiparallel axes), equals half the swap
   operator, and has smallest eigenvalue -1/2, so it is not a state of M_4(C). Positivity on the generated
   algebra (the second reading, D-alg) excludes it.

Prints one line per check and TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys

import numpy as np

AUDIT_TIMEOUT_SEC = 300

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1.0 + 0j, -1.0])
PAULI = [I2, X, Y, Z]
rng = np.random.default_rng(2026)


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def random_state(d):
    A = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    rho = A @ A.conj().T
    return rho / np.trace(rho).real


def real_rank(mats, tol=1e-9):
    """Real dimension of the span of Hermitian matrices."""
    V = np.array([np.concatenate([m.real.ravel(), m.imag.ravel()]) for m in mats])
    return int(np.linalg.matrix_rank(V, tol=tol))


def complex_rank(mats, tol=1e-9):
    return int(np.linalg.matrix_rank(np.array([m.ravel() for m in mats]), tol=tol))


# ------------------------------------------------ 1. the ordinary composite passes the reading
tet = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / np.sqrt(3.0)   # four record-menu axes
proj = [0.5 * (I2 + n[0] * X + n[1] * Y + n[2] * Z) for n in tet]                    # the locked possibility along n
menu_products = [kron(p, q) for p in proj for q in proj]                             # joint record frequencies
pauli_products = [kron(a, b) for a in PAULI for b in PAULI]
worst_menu, worst_pauli = 0.0, 0.0
for _ in range(20):
    rho = random_state(4)
    freqs = np.array([np.trace(rho @ m).real for m in menu_products])               # 16 joint frequencies
    M = np.array([m.ravel() for m in menu_products]).T                                # rho = sum_k c_k m_k
    coef = np.linalg.solve(np.array([[np.trace(a.conj().T @ b) for b in menu_products] for a in menu_products]).real,
                           freqs)
    rho_menu = sum(c * m for c, m in zip(coef, menu_products))
    rho_pauli = 0.25 * sum(np.trace(rho @ p).real * p for p in pauli_products)
    worst_menu = max(worst_menu, np.abs(rho_menu - rho).max())
    worst_pauli = max(worst_pauli, np.abs(rho_pauli - rho).max())
one_site = real_rank([X, Y, Z])
two_site_traceless = real_rank([kron(a, b) for a in PAULI[1:] for b in PAULI[1:]])
total_traceless = real_rank(pauli_products[1:])
three = [kron(a, b, c) for a in PAULI for b in PAULI for c in PAULI]
r3 = real_rank(three[1:])
parts3 = (3 * real_rank([X, Y, Z]), 3 * two_site_traceless, real_rank([kron(a, b, c) for a in PAULI[1:] for b in PAULI[1:] for c in PAULI[1:]]))
check("the ordinary composite passes the reading: local record menus along four axes reconstruct every two-site state",
      worst_menu < 1e-12 and worst_pauli < 1e-12 and total_traceless == 15 and one_site == 3 and two_site_traceless == 9
      and r3 == 63 and sum(parts3) == 63,
      f"20 random states rebuilt from 16 joint menu frequencies to {worst_menu:.0e} and from 16 Pauli products to "
      f"{worst_pauli:.0e}; traceless dimensions 15 = {one_site} + {one_site} + {two_site_traceless}; three sites 63 = "
      f"{parts3[0]} + {parts3[1]} + {parts3[2]}")

# ------------------------------------------------ 2. the generated algebra is M_4(C); three sites M_8(C)
loc2 = [kron(a, I2) for a in PAULI] + [kron(I2, b) for b in PAULI]
words2 = [a @ b for a in loc2 for b in loc2]
loc3 = [kron(a, I2, I2) for a in PAULI] + [kron(I2, a, I2) for a in PAULI] + [kron(I2, I2, a) for a in PAULI]
words3 = [a @ b @ c for a in loc3 for b in loc3 for c in loc3]
comm = max(np.abs(kron(a, I2) @ kron(I2, b) - kron(I2, b) @ kron(a, I2)).max() for a in PAULI for b in PAULI)
check("the words in the commuting local copies span the whole composite algebra: 16 for two sites, 64 for three",
      complex_rank(words2) == 16 and complex_rank(words3) == 64 and comm == 0.0,
      f"local copies commute exactly ({comm:.0e}); span of two-letter words {complex_rank(words2)}, of three-letter words {complex_rank(words3)}")

# ------------------------------------------------ 3. the graded composite fails the reading
# two fermionic modes, Fock basis |n1 n2> ordered 00, 01, 10, 11 (Jordan-Wigner on two qubits)
sm = np.array([[0, 1], [0, 0]], dtype=complex)          # lowers |1> -> |0>
c1 = kron(sm, I2)
c2 = kron(Z, sm)
n1, n2 = c1.conj().T @ c1, c2.conj().T @ c2
I4 = np.eye(4, dtype=complex)
local_products = [I4, n1, n2, n1 @ n2]
psi_p = np.zeros(4, dtype=complex)
psi_m = np.zeros(4, dtype=complex)
psi_p[1] = psi_p[2] = 1 / np.sqrt(2)
psi_m[1], psi_m[2] = 1 / np.sqrt(2), -1 / np.sqrt(2)
rho_p, rho_m = np.outer(psi_p, psi_p.conj()), np.outer(psi_m, psi_m.conj())
same = max(abs(np.trace(rho_p @ m) - np.trace(rho_m @ m)) for m in local_products)
tdist = 0.5 * np.abs(np.linalg.eigvalsh(rho_p - rho_m)).sum()
P1 = I4 - 2 * n1                                       # mode-1 parity
Ptot = P1 @ (I4 - 2 * n2)
# parity-block-diagonal states: real parameters
even_block, odd_block = [0, 3], [1, 2]
n_params = 2 * (2 * 2) - 1                             # two Hermitian 2x2 blocks minus the trace
n_local = real_rank(local_products) - 1
acomm = np.abs(c1 @ c2 + c2 @ c1).max()                # local odd elements anticommute
x1 = kron(X, I2)
x1_odd = np.abs(x1 @ P1 + P1 @ x1).max() == 0.0 and np.abs(x1 @ P1 - P1 @ x1).max() > 0
xx_sep = np.trace(rho_p @ kron(X, X)).real - np.trace(rho_m @ kron(X, X)).real
sector_ok = all(abs(np.trace(r @ Ptot) + 1) < 1e-12 for r in (rho_p, rho_m))     # both in the odd total-parity sector
check("the graded composite fails the reading: two odd-sector states share every local-product statistic",
      same < 1e-12 and abs(tdist - 1) < 1e-12 and n_params == 7 and n_local == 3 and acomm == 0.0 and x1_odd
      and abs(xx_sep - 2) < 1e-12 and sector_ok,
      f"local readable products {{1, n1, n2, n1 n2}} fix {n_local} of {n_params} real parameters; (|01>+|10>)/sqrt2 and "
      f"(|01>-|10>)/sqrt2 agree on them to {same:.0e} with trace distance {tdist:.0f}; the mode operators anticommute "
      f"({acomm:.0e}); sigma^x_1 anticommutes with the mode-1 parity so it is not local there; read as two qubits, "
      f"sigma^x sigma^x separates them by {xx_sep:.0f}")

# ------------------------------------------------ 4. the reading alone leaves the state set open
S = kron(X, X) + kron(Y, Y) + kron(Z, Z)
W = 0.25 * (I4 + S)
swap = np.zeros((4, 4), dtype=complex)                 # |ab> -> |ba>
for a_, b_ in itertools.product(range(2), repeat=2):
    swap[2 * b_ + a_, 2 * a_ + b_] = 1.0
ev_min = np.linalg.eigvalsh(W).min()
marg = max(np.abs(np.trace(W.reshape(2, 2, 2, 2), axis1=1, axis2=3) - 0.5 * I2).max(),
           np.abs(np.trace(W.reshape(2, 2, 2, 2), axis1=0, axis2=2) - 0.5 * I2).max())
mins = []
for _ in range(4000):
    a, b = rng.normal(size=3), rng.normal(size=3)
    a, b = a / np.linalg.norm(a), b / np.linalg.norm(b)
    pa, pb = 0.5 * (I2 + a[0] * X + a[1] * Y + a[2] * Z), 0.5 * (I2 + b[0] * X + b[1] * Y + b[2] * Z)
    mins.append(np.trace(W @ kron(pa, pb)).real - 0.25 * (1 + a @ b))
formula_dev = max(abs(m) for m in mins)
anti = np.trace(W @ kron(0.5 * (I2 + Z), 0.5 * (I2 - Z))).real
coords = np.array([np.trace(W @ p).real for p in pauli_products])
check("the reading alone leaves the state set open: W = (1 + XX + YY + ZZ)/4 is positive on every product effect yet not a state",
      abs(ev_min + 0.5) < 1e-12 and marg < 1e-12 and formula_dev < 1e-12 and abs(anti) < 1e-12
      and np.abs(W - 0.5 * swap).max() < 1e-12 and np.count_nonzero(np.abs(coords) > 1e-12) == 4,
      f"smallest eigenvalue {ev_min:+.2f}; marginals I/2 to {marg:.0e}; <ab|W|ab> = (1 + a.b)/4 on 4000 random product states "
      f"to {formula_dev:.0e}, zero at antiparallel axes ({anti:.0e}); W is half the swap operator; "
      f"{np.count_nonzero(np.abs(coords) > 1e-12)} nonzero local-product coordinates")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
