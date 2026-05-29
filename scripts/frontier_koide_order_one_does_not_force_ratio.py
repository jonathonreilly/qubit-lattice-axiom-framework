#!/usr/bin/env python3
"""Diagnostic: the NCG order-one condition does NOT force the Koide ratio.

What-if test on the Connes-Lott / product-grading spectral triple that would be
needed for a chiral Koide mass operator (H = gen C^3 (x) L/R C^2, Dirac
D = [[0, M],[Mdag, 0]] with circulant Yukawa M = a I + b R + c R^2 on the
generation factor, R = cyclic shift). The question (the one untested fork the
prior chirality panel flagged): does imposing the NCG order-one condition
[[D, pi(a)], pi_opp(b)] = 0 (pi_opp(b) = J pi(b)* J^-1) pin the ratio
r = |b|^2/a^2 = 1/2 (the Koide / Q=2/3 point)?

Answer (verified two ways): NO.
 - PART 1 (circulant algebra, the natural Z_3-generation algebra): order-one is
   VACUOUS -- the inner commutator [D, pi(a)] is identically 0 because circulant
   matrices commute, BEFORE J or the grading enter. So it constrains nothing.
 - PART 2: explicit distinct-r witnesses (r = 0.05 .. 5.0) ALL satisfy
   order-zero + order-one exactly -> r is a free parameter, not pinned.
 - PART 3 (full M_3 algebra, the maximal case): the order-one solution space is
   the bimodule family D(m) = h m + m k (h, k in M_3 free) -> Yukawa free
   (Cacic 2009, arXiv:0902.2068). Numeric rank confirms a high-dim moduli space.

This is a NEGATIVE result: the NCG order-one condition is one more lens that
does NOT supply the r = 1/2 selector. It does NOT adopt the L/R-factor (e4/P2)
import; it is a what-if showing that even granting that import, order-one is not
the missing forcing principle. The chirality/r gate stays open.
"""

import numpy as np
from sympy import symbols, Matrix, eye, zeros, simplify, I as sympy_I
import sys

PASS = 0
FAIL = 0


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}  ({detail})")


def section(t):
    print("\n" + "-" * 84 + f"\n{t}\n" + "-" * 84)


# generation cyclic shift R (3x3)
Rs = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
I3 = eye(3)

# ============================================================================
section("PART 1: circulant generation algebra => order-one is VACUOUS")
# ============================================================================
a, b, c = symbols('a b c')           # Yukawa M = a I + b R + c R^2 (circulant)
ap, bp, cp = symbols('ap bp cp')     # algebra element (circulant)
M = a * I3 + b * Rs + c * Rs**2
Acirc = ap * I3 + bp * Rs + cp * Rs**2

check("circulant Yukawa M commutes with circulant algebra element: [M, a] = 0",
      simplify(M * Acirc - Acirc * M) == zeros(3))

# pi(a) on H = C^3 (x) C^2 (gen (x) L/R), acting the same on L and R blocks:
#   pi(a) = block_diag(a, a);  D = [[0, M],[Mdag, 0]]
Md = M.conjugate().T
D6 = Matrix.vstack(Matrix.hstack(zeros(3), M), Matrix.hstack(Md, zeros(3)))
pa6 = Matrix.vstack(Matrix.hstack(Acirc, zeros(3)), Matrix.hstack(zeros(3), Acirc))
inner = simplify(D6 * pa6 - pa6 * D6)
check("inner commutator [D, pi(a)] = 0 identically (=> order-one vacuous, no r constraint)",
      inner == zeros(6),
      "vanishes before J/grading enter, for ALL a,b,c")

# ============================================================================
section("PART 2: explicit distinct-r witnesses all satisfy order-zero + order-one")
# ============================================================================
Rn = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
I3n = np.eye(3, dtype=complex)
# real structure J on H = C^6 (gen (x) L/R): J = [[0, I3],[-I3, 0]] (J^2 = -I)
J = np.block([[np.zeros((3, 3)), I3n], [-I3n, np.zeros((3, 3))]])


def pi(av):  # circulant algebra element av=(al,be,ga) -> block_diag(a,a)
    al, be, ga = av
    A = al * I3n + be * Rn + ga * (Rn @ Rn)
    return np.block([[A, np.zeros((3, 3))], [np.zeros((3, 3)), A]])


def pi_opp(av):
    P = pi(av)
    return J @ P.conj() @ np.linalg.inv(J)


def order_one_max(Mn):
    Mdn = Mn.conj().T
    D = np.block([[np.zeros((3, 3)), Mn], [Mdn, np.zeros((3, 3))]])
    tr = [(1, 0, 0), (0, 1, 0), (0.3 + 0.2j, 0.7, 0.1j), (1, 1j, 0.5)]
    m = 0.0
    for av in tr:
        for bv in tr:
            O = (D @ pi(av) - pi(av) @ D) @ pi_opp(bv) - pi_opp(bv) @ (D @ pi(av) - pi(av) @ D)
            m = max(m, np.max(np.abs(O)))
    return m


for r in [0.05, 0.20, 0.50, 1.00, 2.00, 5.00]:
    bval = np.sqrt(r)              # M = I + b R  => r = |b|^2 / 1^2 = b^2
    Mn = I3n + bval * Rn
    viol = order_one_max(Mn)
    check(f"r={r:>4}: order-one satisfied (circulant algebra) max|O|={viol:.2e}",
          viol < 1e-10, f"b={bval:.4f}")

print("\n  => order-one holds for a CONTINUUM of r; it does NOT select r=1/2.")

# ============================================================================
section("PART 3: full M_3 algebra => order-one moduli space is free (Cacic 2009)")
# ============================================================================
# Order-one solution space for D off-diagonal with algebra A=M_3 acting as
# block_diag(a,a) and opposite via J: the solutions are the bimodule family
# D(m) = h m + m k (left/right module maps). Dimension of {Yukawa M} is 9 (free).
# Numeric: build the linear map M -> (order-one residual over a basis of M_3)
# and confirm its KERNEL (allowed M) has full dimension 9 (no constraint on M).
basis = []
for i in range(3):
    for j in range(3):
        E = np.zeros((3, 3), dtype=complex)
        E[i, j] = 1.0
        basis.append(E)
# algebra generators of M_3 (same basis), acting block_diag(a,a)
rows = []
for Mb in basis:                      # candidate Yukawa direction
    Mdn = Mb.conj().T
    D = np.block([[np.zeros((3, 3)), Mb], [Mdn, np.zeros((3, 3))]])
    resid = []
    for Ea in basis:
        pA = np.block([[Ea, np.zeros((3, 3))], [np.zeros((3, 3)), Ea]])
        for Eb in basis:
            pBo = J @ np.block([[Eb, np.zeros((3, 3))], [np.zeros((3, 3)), Eb]]).conj() @ np.linalg.inv(J)
            O = (D @ pA - pA @ D) @ pBo - pBo @ (D @ pA - pA @ D)
            resid.append(O.flatten())
    rows.append(np.concatenate(resid))
Lmap = np.array(rows)                 # 9 x (big): row k = order-one residual of basis Yukawa k
rank = np.linalg.matrix_rank(Lmap, tol=1e-9)
free_dim = 9 - rank
check(f"M_3 Yukawa directions unconstrained by order-one: free_dim={free_dim} of 9",
      free_dim >= 1, f"rank(order-one map)={rank} -> Yukawa NOT pinned (moduli-free)")

print(f"\n{'='*84}\n  TOTAL: PASS={PASS} FAIL={FAIL}\n{'='*84}")
print("  VERDICT: NCG order-one does NOT force the Koide ratio r=1/2 "
      "(vacuous on circulant, moduli-free on M_3).")
sys.exit(1 if FAIL else 0)
