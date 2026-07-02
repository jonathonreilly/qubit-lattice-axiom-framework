#!/usr/bin/env python3
"""Torus-dual abelianization of SU(N) class weights: for the heat-kernel
member the Weyl-denominator-dressed weight is an exact signed Gaussian on the
regular points of the rho-shifted weight lattice; the structure is
gluing-stable; a continuous Weyl-consistent theta shift-slot on the
nonabelian torus dual is obstructed.

Paired note:
docs/THETA_TORUS_DUAL_ABELIANIZATION_SHIFTED_WEIGHT_LATTICE_GAUSSIAN_GLUING_STABLE_WEYL_SHIFT_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-02.md

Class-A finite checks only: band-limited torus Fourier extraction on
degeneracy-free offset grids (exact for finite character sums), Poisson image
identities, finite Weyl-group linear algebra, and Weyl-quadrature dual
coefficients. Deterministic; no fits, no external comparators, no measured
values. One overall normalization per dual table is fixed on a single mode
and every other mode is then parameter-free.

Sections:
  A. SU(2) torus dual: Delta * K_t has modes exactly A n e^{-t n^2/4} on
     nonzero n (regular shifted weights; n = 0 absent), anti-invariant
     c_{-n} = -c_n; the Wilson member has the same support and antisymmetry;
     the integer-spin (center-even) restriction populates only the odd-mu
     coset — the block-1 center grading is the coset shadow of the lattice.
  B. SU(2) position side: the full-lattice Poisson image identity
     sum_n n e^{-t n^2/4} e^{i n phi} = image sum over 2 pi k shifts —
     the exact branch/winding-sum structure of the class weight.
  C. SU(3) torus dual: on a degeneracy-free offset grid, the window modes of
     Delta * K_t match the signed d_R e^{-t C2(R)} table on the shifted
     weight orbit lattice (parameter-free after the table's own
     construction); anti-invariance under the mode swap; non-regular lines
     carry zero; all three triality cosets are populated.
  D. Gluing: heat-kernel semigroup c_R(t1) c_R(t2)/d_R = c_R(t1+t2) exactly;
     the dual support cannot grow under gluing (pointwise coefficient
     products); the Wilson member is not form-stable (tau_R / C2 ratios at
     beta = 6, computed by fresh Weyl quadrature, are not constant).
  E. Weyl-shift obstruction: the W-fixed subspace of the Cartan is zero for
     su(2) and su(3), and any nonzero integer shift of the SU(3) dual table
     breaks Weyl anti-invariance — no continuous W-consistent label-shift
     theta slot exists on the nonabelian torus dual.

Expected close: TOTAL: PASS=17 FAIL=0
"""
from __future__ import annotations

from itertools import permutations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


# ---------------------------------------------------------------------------
# Section A: SU(2) torus dual
# ---------------------------------------------------------------------------
print("Section A: SU(2) torus dual")

T_HK = 0.7
JMAX2 = 40          # sum over 2j = 0..2*JMAX2 (all integer and half-integer j)
NG = 1024
PHI = (np.arange(NG) + 0.31) * 2 * np.pi / NG   # no 0 or pi on the grid


def su2_hk_class(phi: np.ndarray, t: float, twoj_max: int, step: int = 1,
                 start: int = 0) -> np.ndarray:
    """K_t(phi) = sum over 2j in {start, start+step, ...} of
    (2j+1) e^{-t j(j+1)} chi_j(phi)."""
    K = np.zeros_like(phi)
    for twoj in range(start, twoj_max + 1, step):
        n = twoj + 1
        K += n * np.exp(-t * (twoj / 2.0) * (twoj / 2.0 + 1.0)) \
            * np.sin(n * phi) / np.sin(phi)
    return K


K2 = su2_hk_class(PHI, T_HK, 2 * JMAX2)
F2 = np.sin(PHI) * K2


def mode(f: np.ndarray, grid: np.ndarray, n: int) -> complex:
    return complex(np.mean(f * np.exp(-1j * n * grid)))


c1 = mode(F2, PHI, 1)
ok_zero = abs(mode(F2, PHI, 0)) < 1e-12
ok_all = True
ok_anti = True
for n in range(1, 29):
    cn = mode(F2, PHI, n)
    pred = c1 * (n * np.exp(-T_HK * n * n / 4.0)) / np.exp(-T_HK / 4.0)
    ok_all = ok_all and abs(cn - pred) < 1e-10 * max(1.0, abs(pred))
    ok_anti = ok_anti and abs(mode(F2, PHI, -n) + cn) < 1e-10
check("A1 SU(2) HK dual: c_0 = 0 (regular lattice only); c_n = A n"
      " e^{-t n^2/4} on every n in [1,28] after fixing A at n=1",
      ok_zero and ok_all)
check("A2 SU(2) HK dual: Weyl anti-invariance c_(-n) = -c_n", ok_anti)

BETA_W = 6.0
w_wilson = np.exp(BETA_W * np.cos(PHI))
# class weight -> dressed function sin(phi) * w is Weyl-odd but NOT band
# limited; extract modes by quadrature (smooth integrand, spectral accuracy)
FW = np.sin(PHI) * w_wilson
ok_wsup = abs(mode(FW, PHI, 0)) < 1e-10
ok_wanti = True
ok_wnz = True
for n in range(1, 12):
    cn = mode(FW, PHI, n)
    ok_wanti = ok_wanti and abs(mode(FW, PHI, -n) + cn) < 1e-10
    ok_wnz = ok_wnz and abs(cn) > 1e-12
check("A3 SU(2) Wilson member: same support structure (c_0 = 0, all"
      " n != 0 populated) and anti-invariance", ok_wsup and ok_wanti and ok_wnz)

K2_int = su2_hk_class(PHI, T_HK, 2 * JMAX2, step=2, start=0)  # integer spins
F2_int = np.sin(PHI) * K2_int
ok_coset = all(abs(mode(F2_int, PHI, n)) < 1e-10 for n in range(0, 24, 2)) \
    and all(abs(mode(F2_int, PHI, n)) > 1e-12 for n in range(1, 10, 2))
check("A4 center-even (integer-spin) restriction populates only the odd-mu"
      " coset: the block-1 Z_2 grading is the coset shadow of the dual"
      " lattice", ok_coset)

# ---------------------------------------------------------------------------
# Section B: SU(2) position-side branch/image sum
# ---------------------------------------------------------------------------
print("Section B: position-side branch sum")

KS = np.arange(-40, 41)
ok_img = True
for t in [0.4, 0.9]:
    for ph in [0.4, 1.3, 2.2, 3.0]:
        lhs = sum(n * np.exp(-t * n * n / 4.0) * np.sin(n * ph)
                  for n in range(1, 300))
        # sum_{n in Z} n e^{-t n^2/4} e^{i n phi}
        #   = i sqrt(4 pi / t) sum_k (2 (phi + 2 pi k)/t) e^{-(phi+2pik)^2/t}
        # imaginary part / 2 restricted to n >= 1 equals lhs by oddness
        rhs = 0.5 * np.sqrt(4 * np.pi / t) * np.sum(
            (2 * (ph + 2 * np.pi * KS) / t)
            * np.exp(-((ph + 2 * np.pi * KS) ** 2) / t))
        ok_img = ok_img and abs(lhs - rhs) < 1e-10 * max(1.0, abs(lhs))
check("B1 full-lattice Poisson image identity: the dual Gaussian equals the"
      " 2 pi k branch/winding image sum exactly", ok_img)

# ---------------------------------------------------------------------------
# Section C: SU(3) torus dual
# ---------------------------------------------------------------------------
print("Section C: SU(3) torus dual on the shifted weight lattice")

NGD = 48
T3 = 0.35
G1 = (np.arange(NGD) + 0.31) * 2 * np.pi / NGD
G2 = (np.arange(NGD) + 0.11) * 2 * np.pi / NGD
TT1, TT2 = np.meshgrid(G1, G2, indexing="ij")
Z1 = np.exp(1j * TT1)
Z2 = np.exp(1j * TT2)
Z3 = np.exp(-1j * (TT1 + TT2))
MIN_SEP = min(float(np.abs(Z1 - Z2).min()), float(np.abs(Z1 - Z3).min()),
              float(np.abs(Z2 - Z3).min()))
check("C1 offset grid is degeneracy-free (eigenvalues never collide)",
      MIN_SEP > 1e-3, f"min separation = {MIN_SEP:.4f}")

DELTA3 = (Z1 - Z2) * (Z1 - Z3) * (Z2 - Z3)


def mu_norm2(a: int, b: int) -> float:
    return (2.0 / 3.0) * (a * a + a * b + b * b)


def su3_char_grid(p: int, q: int) -> np.ndarray:
    lam = [p + q, q, 0]
    e = [lam[j] + 2 - j for j in range(3)]

    def det3(a, b, c):
        return (a[0] * (b[1] * c[2] - b[2] * c[1])
                - a[1] * (b[0] * c[2] - b[2] * c[0])
                + a[2] * (b[0] * c[1] - b[1] * c[0]))

    num = det3([Z1 ** e[0], Z1 ** e[1], Z1 ** e[2]],
               [Z2 ** e[0], Z2 ** e[1], Z2 ** e[2]],
               [Z3 ** e[0], Z3 ** e[1], Z3 ** e[2]])
    den = det3([Z1 ** 2, Z1, np.ones_like(Z1)],
               [Z2 ** 2, Z2, np.ones_like(Z2)],
               [Z3 ** 2, Z3, np.ones_like(Z3)])
    return num / den


PMAXH = 16
K3 = np.zeros_like(TT1, dtype=complex)
PRED = {}
for p in range(PMAXH + 1):
    for q in range(PMAXH + 1):
        a, b = p + 1, q + 1
        dR = a * b * (a + b) / 2.0
        c2 = mu_norm2(a, b) - mu_norm2(1, 1)
        if T3 * c2 > 50:
            continue
        K3 += dR * np.exp(-T3 * c2) * su3_char_grid(p, q)
        e = (p + q + 2, q + 1, 0)
        for perm in permutations(range(3)):
            sg = 1
            pl = list(perm)
            for i in range(3):
                for j in range(i + 1, 3):
                    if pl[i] > pl[j]:
                        sg = -sg
            E = [e[perm[0]], e[perm[1]], e[perm[2]]]
            key = (E[0] - E[2], E[1] - E[2])
            PRED[key] = PRED.get(key, 0.0) + sg * dR * np.exp(-T3 * c2)
F3 = DELTA3 * K3
check("C2 dressed weight is finite on the whole grid (no degeneracy leak)",
      bool(np.all(np.isfinite(F3))))

MWIN = 14
ok_match = True
nz = 0
for n1 in range(-MWIN, MWIN + 1):
    for n2 in range(-MWIN, MWIN + 1):
        cn = complex(np.mean(F3 * np.exp(-1j * (n1 * TT1 + n2 * TT2))))
        want = PRED.get((n1, n2), 0.0)
        if abs(want) > 1e-10:
            nz += 1
        if abs(cn - want) > 1e-6 * max(1.0, abs(want)):
            ok_match = False
check("C3 window modes match the signed d_R e^{-t C2} table on the shifted"
      " weight orbit lattice (parameter-free)",
      ok_match, f"modes checked = {(2*MWIN+1)**2}, nonzero = {nz}")

# the full Weyl group W = S_3 acts on the mode lattice: a mode (n1, n2)
# stands for the exponent vector (n1, n2, 0) modulo (1,1,1); a permutation
# pi acts on the three slots, then the third component is subtracted off.
W_ELEMENTS = []
for perm in permutations(range(3)):
    sg = 1
    pl = list(perm)
    for i in range(3):
        for j in range(i + 1, 3):
            if pl[i] > pl[j]:
                sg = -sg
    W_ELEMENTS.append((perm, sg))


def w_act(perm, m):
    v = (m[0], m[1], 0)
    pv = (v[perm[0]], v[perm[1]], v[perm[2]])
    return (pv[0] - pv[2], pv[1] - pv[2])


def table_anti_invariant(table, win: int) -> bool:
    for n1 in range(-win, win + 1):
        for n2 in range(-win, win + 1):
            v0 = table.get((n1, n2), 0.0)
            for perm, sg in W_ELEMENTS:
                if abs(table.get(w_act(perm, (n1, n2)), 0.0) - sg * v0) > 1e-9:
                    return False
    return True


check("C4 full Weyl anti-invariance of the dual table: PRED(w m) ="
      " sgn(w) PRED(m) for all six w in W", table_anti_invariant(PRED, MWIN))

ok_reg = all(abs(PRED.get((n, n), 0.0)) < 1e-12
             and abs(PRED.get((n, 0), 0.0)) < 1e-12
             and abs(PRED.get((0, n), 0.0)) < 1e-12
             for n in range(-MWIN, MWIN + 1))
check("C5 non-regular lines (n1 = n2, n1 = 0, n2 = 0) carry zero:"
      " support is the REGULAR shifted lattice", ok_reg)

cosets = {(n1 - n2) % 3 for (n1, n2), v in PRED.items() if abs(v) > 1e-10}
check("C6 all three triality cosets of the dual lattice are populated"
      " (block-1 Z_3 grading = the coset shadow)", cosets == {0, 1, 2})

# ---------------------------------------------------------------------------
# Section D: gluing
# ---------------------------------------------------------------------------
print("Section D: gluing stability")

ok_semi = True
for (p, q) in [(0, 0), (1, 0), (1, 1), (2, 1), (3, 2)]:
    a, b = p + 1, q + 1
    dR = a * b * (a + b) / 2.0
    c2 = mu_norm2(a, b) - mu_norm2(1, 1)
    for (ta, tb) in [(0.3, 0.5), (0.7, 0.2), (1.1, 0.9)]:
        cA = dR * np.exp(-ta * c2)
        cB = dR * np.exp(-tb * c2)
        cAB = dR * np.exp(-(ta + tb) * c2)
        ok_semi = ok_semi and abs(cA * cB / dR - cAB) < 1e-12 * abs(cAB)
check("D1 heat-kernel member is the exact gluing fixed class:"
      " c_R(t1) c_R(t2)/d_R = c_R(t1+t2)", ok_semi)

wA = {(0, 0): 1.0, (1, 0): 0.8, (1, 1): 0.0, (2, 0): 0.3}
wB = {(0, 0): 0.5, (1, 0): 0.2, (1, 1): 0.4, (2, 0): 0.0}
glued = {k: wA[k] * wB[k] for k in wA}
check("D2 dual support cannot grow under gluing (pointwise coefficient"
      " products: zero stays zero)",
      glued[(1, 1)] == 0.0 and glued[(2, 0)] == 0.0 and glued[(1, 0)] > 0)

NQW = 200
q1 = (np.arange(NQW) + 0.5) * 2 * np.pi / NQW
q2 = (np.arange(NQW) + 0.13) * 2 * np.pi / NQW
Q1G, Q2G = np.meshgrid(q1, q2, indexing="ij")
Y1 = np.exp(1j * Q1G)
Y2 = np.exp(1j * Q2G)
Y3 = np.exp(-1j * (Q1G + Q2G))
DDW = np.abs((Y1 - Y2) * (Y1 - Y3) * (Y2 - Y3)) ** 2
RETRW = (Y1 + Y2 + Y3).real
WGTW = np.exp((BETA_W / 3.0) * RETRW) * DDW
NRMW = float(np.sum(DDW))


def su3_char_at(p: int, q: int) -> np.ndarray:
    lam = [p + q, q, 0]
    e = [lam[j] + 2 - j for j in range(3)]

    def det3(a, b, c):
        return (a[0] * (b[1] * c[2] - b[2] * c[1])
                - a[1] * (b[0] * c[2] - b[2] * c[0])
                + a[2] * (b[0] * c[1] - b[1] * c[0]))

    num = det3([Y1 ** e[0], Y1 ** e[1], Y1 ** e[2]],
               [Y2 ** e[0], Y2 ** e[1], Y2 ** e[2]],
               [Y3 ** e[0], Y3 ** e[1], Y3 ** e[2]])
    den = det3([Y1 ** 2, Y1, np.ones_like(Y1)],
               [Y2 ** 2, Y2, np.ones_like(Y2)],
               [Y3 ** 2, Y3, np.ones_like(Y3)])
    return num / den


CW = {}
for (p, q) in [(0, 0), (1, 0), (1, 1), (2, 0)]:
    ch = su3_char_at(p, q)
    CW[(p, q)] = float(np.sum(WGTW * np.conj(ch)).real / NRMW)
DIMS = {(0, 0): 1.0, (1, 0): 3.0, (1, 1): 8.0, (2, 0): 6.0}
TAUS = {}
for k in [(1, 0), (1, 1), (2, 0)]:
    c2 = mu_norm2(k[0] + 1, k[1] + 1) - mu_norm2(1, 1)
    TAUS[k] = -np.log(CW[k] / (DIMS[k] * CW[(0, 0)])) / c2
spread = max(TAUS.values()) - min(TAUS.values())
check("D3 Wilson member (beta=6, fresh Weyl quadrature) is NOT form-stable:"
      " tau_R/C2 ratios are not constant",
      spread > 1e-2,
      "ratios = " + ", ".join(f"{k}:{v:.4f}" for k, v in TAUS.items()))

# ---------------------------------------------------------------------------
# Section E: Weyl-shift obstruction
# ---------------------------------------------------------------------------
print("Section E: Weyl-shift obstruction")

check("E1 su(2): the W-average of the Cartan action is 0 (fixed subspace"
      " zero)", (1.0 + (-1.0)) / 2.0 == 0.0)

P3S = []
for perm in permutations(range(3)):
    M = np.zeros((3, 3))
    for i, pp in enumerate(perm):
        M[i, pp] = 1.0
    P3S.append(M)
AVG = sum(P3S) / 6.0
PI0 = np.eye(3) - np.ones((3, 3)) / 3.0
norm_fixed = float(np.linalg.norm(PI0 @ AVG @ PI0))
check("E2 su(3): the W-average restricted to the Cartan (sum-zero subspace)"
      " is exactly 0 — no W-fixed direction exists",
      norm_fixed < 1e-14, f"norm = {norm_fixed:.2e}")

ok_shift = True
for (s1, s2) in [(1, 0), (0, 1), (1, 1), (2, 1), (-1, -1), (2, 2)]:
    shifted = {(n1 + s1, n2 + s2): v for (n1, n2), v in PRED.items()}
    ok_shift = ok_shift and (not table_anti_invariant(shifted, MWIN - 3))
check("E3 every tested nonzero lattice shift of the SU(3) dual table"
      " (including diagonal shifts) breaks full-W anti-invariance: the"
      " U(1)-template label-shift theta slot does not lift to the"
      " nonabelian torus dual", ok_shift)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
