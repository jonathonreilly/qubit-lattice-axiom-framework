#!/usr/bin/env python3
"""Multi-plaquette character gluing: the emergent integer sector-record
context is exact on the finite 2D U(1) surface, branch-datum-free, with the
theta pairing derived from the action slot; nonabelian matched-label contrast.

Paired note:
docs/GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md

Class-A finite checks only: 1D/2D/3D deterministic quadratures against exact
identities, exact integer constraint enumeration on small closed tori, and
finite dual-series arithmetic. No fits, no external comparators, no measured
values, no randomness.

Sections:
  A. U(1) dual coefficients: Wilson c_n = I_n(beta) > 0 paired; heat-kernel
     member c_n = e^{-t n^2/2} verified by quadrature.
  B. Gluing mechanism: shared-link integration multiplies coefficients and
     matches labels; on closed 2x2 / 2x3 tori the link constraints force a
     single matched label (derived by enumeration, not assumed); chart-shift
     columns sum to zero; the constrained sum reproduces Z = sum_n c_n^V.
  C. Flux-form sector weights: Z_n = c_n^V / sum > 0 on every sector, paired,
     odd support, truncation-stable, finite-truncation exhaustion explicit.
  D. Winding form and branch discharge (heat-kernel member): theta enters as
     the dual-label shift; flux form == Poisson winding form; Z_Q > 0 paired
     with odd support; closed-surface plaquette-angle sum vanishes
     identically; total Q = sum_p k_p invariant under refundamentalization of
     any link; regional splits chart-covariant with compensating shifts.
  E. Pointwise selector interface arithmetic on the derived winding context.
  F. Nonabelian contrast on the same gluing: SU(2) gluing identity and
     orthogonality by quadrature; 1-cell torus matched-label decomposition
     Z = sum_j c_j / d_j; SU(3) dual coefficients positive and paired at
     beta = 6; Z-valued conjugation-odd functions on matched labels exist and
     are non-unique.

Expected close: TOTAL: PASS=30 FAIL=0
"""
from __future__ import annotations

import cmath
from pathlib import Path
import numpy as np
from scipy.special import iv

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
# Section A: U(1) dual coefficients
# ---------------------------------------------------------------------------
print("Section A: U(1) dual coefficients")

NGRID = 4096
TH = np.linspace(0.0, 2.0 * np.pi, NGRID, endpoint=False)

for beta in [1.0, 6.0]:
    w = np.exp(beta * np.cos(TH))
    ok = True
    for n in range(0, 7):
        cn = float(np.mean(w * np.exp(-1j * n * TH)).real)
        ok = ok and abs(cn - float(iv(n, beta))) < 1e-10
    check(f"A1 Wilson coefficients c_n(beta={beta:g}) = I_n(beta) (n<=6)", ok)

ok = True
for beta in [1.0, 6.0]:
    cs = np.array([float(iv(abs(n), beta)) for n in range(-30, 31)])
    ok = ok and bool(np.all(cs > 0))
check("A2 Wilson coefficients positive and paired c_n = c_-n (|n|<=30)", ok)

T_HK = 0.5
ks = np.arange(-60, 61)
w_hk = np.array([np.sum(np.exp(-T_HK * ((t + 2 * np.pi * ks) ** 2) / 2.0))
                 for t in TH[::8]])
# heat-kernel member: the wrapped Gaussian sum_k exp(-T (theta+2pi k)^2/2)
# has Fourier coefficients (1/2pi) sqrt(2pi/T) exp(-n^2/(2T)) — the Gaussian
# dual-label profile (Poisson identity).
ok = True
for n in range(0, 6):
    cn = float(np.mean(w_hk * np.exp(-1j * n * TH[::8])).real)
    ref = (np.sqrt(2.0 * np.pi / T_HK) / (2.0 * np.pi)
           * np.exp(-n * n / (2.0 * T_HK)))
    ok = ok and abs(cn - ref) < 1e-9
check("A3 heat-kernel member: quadrature coefficients are the Gaussian"
      " dual-label profile", ok)

# ---------------------------------------------------------------------------
# Section B: gluing mechanism on closed surfaces
# ---------------------------------------------------------------------------
print("Section B: gluing = label matching (derived, not assumed)")

beta = 2.0
cn_w = np.array([float(iv(abs(n), beta)) for n in range(-30, 31)])
ns_w = np.arange(-30, 31)
ok = True
for (A, B) in [(0.3, 1.1), (-0.7, 0.4), (2.0, -1.3)]:
    lhs = complex(np.mean(np.exp(beta * np.cos(A + TH)) * np.exp(beta * np.cos(B - TH))))
    rhs = complex(np.sum(cn_w ** 2 * np.exp(1j * ns_w * (A + B))))
    ok = ok and abs(lhs - rhs) < 1e-10
check("B1 shared-link gluing: int dV w(A+V) w(B-V) = sum_n c_n^2 e^{in(A+B)}",
      ok)


def torus_incidence(Lx: int, Ly: int):
    plaqs = [(x, y) for x in range(Lx) for y in range(Ly)]
    pidx = {p: i for i, p in enumerate(plaqs)}
    links = ([("x", x, y) for x in range(Lx) for y in range(Ly)]
             + [("y", x, y) for x in range(Lx) for y in range(Ly)])
    lidx = {l: i for i, l in enumerate(links)}
    inc = np.zeros((len(links), len(plaqs)), dtype=np.int64)
    for (x, y) in plaqs:
        j = pidx[(x, y)]
        inc[lidx[("x", x, y)], j] += 1
        inc[lidx[("y", (x + 1) % Lx, y)], j] += 1
        inc[lidx[("x", x, (y + 1) % Ly)], j] -= 1
        inc[lidx[("y", x, y)], j] -= 1
    return inc, plaqs, links


def matched_assignments(inc: np.ndarray, nmax: int):
    P = inc.shape[1]
    sols = []
    from itertools import product
    for v in product(range(-nmax, nmax + 1), repeat=P):
        vv = np.array(v, dtype=np.int64)
        if np.all(inc @ vv == 0):
            sols.append(v)
    return sols


INC22, PLQ22, LNK22 = torus_incidence(2, 2)
sols22 = matched_assignments(INC22, 3)
check("B2 2x2 torus: link constraints force all labels equal (enumeration)",
      len(sols22) == 7 and all(len(set(s)) == 1 for s in sols22),
      f"solutions = {len(sols22)}, all matched")

INC23, PLQ23, LNK23 = torus_incidence(2, 3)
sols23 = matched_assignments(INC23, 3)
check("B3 2x3 torus: link constraints force all labels equal (enumeration)",
      len(sols23) == 7 and all(len(set(s)) == 1 for s in sols23),
      f"solutions = {len(sols23)}, all matched")

col_pattern_ok = True
for inc in (INC22, INC23):
    col_pattern_ok = col_pattern_ok and bool(np.all(inc.sum(axis=1) == 0))
    col_pattern_ok = col_pattern_ok and bool(
        np.all(np.sort(np.abs(inc), axis=1)[:, -2:].sum(axis=1) == 2))
check("B4 every link column has exactly one +1 and one -1 (sums to zero)",
      col_pattern_ok)

NTR = 6
cs = np.array([float(iv(abs(n), beta)) for n in range(-NTR, NTR + 1)])
from itertools import product as iproduct
z_enum = 0.0
for v in iproduct(range(-NTR, NTR + 1), repeat=4):
    vv = np.array(v, dtype=np.int64)
    if np.all(INC22 @ vv == 0):
        z_enum += float(np.prod([cs[n + NTR] for n in v]))
z_dual = float(np.sum(cs ** 4))
check("B5 constrained enumeration reproduces Z = sum_n c_n^V (2x2, beta=2)",
      abs(z_enum - z_dual) < 1e-12 * abs(z_dual),
      f"Z = {z_dual:.6f}")

# ---------------------------------------------------------------------------
# Section C: flux-form sector weights on the closed torus
# ---------------------------------------------------------------------------
print("Section C: flux-form sector weights")

for beta in [1.0, 6.0]:
    ok = True
    detail = ""
    for V in [4, 16]:
        N = 12  # underflow-free window; the |n| > N tail is bounded in C3
        cs = np.array([float(iv(abs(n), beta)) for n in range(-N, N + 1)])
        Zn = cs ** V
        Zn = Zn / Zn.sum()
        idx0 = N
        ok = ok and bool(np.all(Zn > 0)) and float(np.min(Zn)) > 1e-300
        ok = ok and bool(np.allclose(Zn, Zn[::-1]))
        ok = ok and Zn[idx0 + 1] > 0  # odd support
        if V == 4:
            detail = (f"V=4: Z_0={Zn[idx0]:.6f} Z_1={Zn[idx0+1]:.6f} "
                      f"Z_2={Zn[idx0+2]:.6f}")
    check(f"C1 beta={beta:g}: Z_n > 0 all sectors, paired, odd support", ok,
          detail)

beta = 6.0
V = 4
c30 = np.array([float(iv(abs(n), beta)) for n in range(-30, 31)])
c60 = np.array([float(iv(abs(n), beta)) for n in range(-60, 61)])
z30 = c30 ** V / np.sum(c30 ** V)
z60 = c60 ** V / np.sum(c60 ** V)
drift = float(np.max(np.abs(z30 - z60[30:-30])))
check("C2 truncation stability |n|<=30 vs |n|<=60 (beta=6, V=4)",
      drift < 1e-12, f"max drift = {drift:.2e}")

tail = float(np.sum(z60[np.abs(np.arange(-60, 61)) > 10]))
check("C3 finite-truncation tail bound: mass at |n|>10 explicit and tiny",
      tail < 1e-9, f"tail = {tail:.2e}")

# ---------------------------------------------------------------------------
# Section D: winding form and branch discharge (heat-kernel member)
# ---------------------------------------------------------------------------
print("Section D: winding form and branch-datum discharge")

BT = 1.3
THETA0 = 0.9
ks = np.arange(-40, 41)


def w_theta_hk(tp: float, theta: float, bt: float) -> complex:
    vals = np.exp(-bt / 2.0 * (tp + 2 * np.pi * ks) ** 2
                  + 1j * (theta / (2 * np.pi)) * (tp + 2 * np.pi * ks))
    return complex(np.sum(vals))


ok = True
for n in range(-3, 4):
    samples = TH[::16]
    cn_num = complex(np.mean([w_theta_hk(t, THETA0, BT) * cmath.exp(-1j * n * t)
                              for t in samples]))
    cn_ref = (np.sqrt(2 * np.pi / BT) / (2 * np.pi)
              * np.exp(-((n - THETA0 / (2 * np.pi)) ** 2) / (2 * BT)))
    ok = ok and abs(cn_num - cn_ref) < 1e-9
check("D1 theta slot: theta-inserted weight has coefficients shifted by"
      " theta/2pi (pairing derived from the action slot)", ok)


def z_flux(bt: float, V: int, theta: float, N: int = 80) -> float:
    ns_ = np.arange(-N, N + 1)
    return float(np.sum(np.exp(-V * (ns_ - theta / (2 * np.pi)) ** 2 / (2 * bt))))


def z_wind(bt: float, V: int, theta: float, N: int = 80) -> float:
    Qs = np.arange(-N, N + 1)
    pref = np.sqrt(2 * np.pi * bt / V)
    return float(pref * np.sum(np.exp(-2 * np.pi ** 2 * bt * Qs ** 2 / V)
                               * np.exp(1j * Qs * theta)).real)


ok = True
for bt in [0.7, 2.0]:
    for V in [4, 16]:
        for theta in [0.0, 1.0, float(np.pi)]:
            ok = ok and abs(z_flux(bt, V, theta) - z_wind(bt, V, theta)) < 1e-12
check("D2 flux form equals Poisson winding form Z(theta) = sum_Q e^{i theta Q} Z_Q",
      ok)

ZQ = lambda bt, V, Q: np.sqrt(2 * np.pi * bt / V) * np.exp(-2 * np.pi ** 2 * bt * Q ** 2 / V)
zqs = np.array([ZQ(2.0, 16, Q) for Q in range(-6, 7)])
check("D3 winding weights Z_Q > 0, paired, odd support",
      bool(np.all(zqs > 0)) and abs(ZQ(2.0, 16, 3) - ZQ(2.0, 16, -3)) < 1e-18
      and ZQ(2.0, 16, 1) > 0,
      f"Z_0={ZQ(2.0,16,0):.6f} Z_1={ZQ(2.0,16,1):.6f} Z_2={ZQ(2.0,16,2):.6f}")

ok = True
for (inc, nl) in [(INC22, 8), (INC23, 12)]:
    th_links = 0.1 + 0.37 * np.arange(inc.shape[0])  # fixed deterministic angles
    th_p = inc.T @ th_links
    ok = ok and abs(float(np.sum(th_p))) < 1e-12
check("D4 closed surface: sum_p theta_p = 0 identically (link cancellation),"
      " so Q = sum_p k_p is an exact integer", ok)

kk = np.array([2, -1, 0, 3], dtype=np.int64)  # arbitrary dual assignment, 2x2
regionA = [0, 1]
regionB = [2, 3]
ok = True
for li in range(INC22.shape[0]):
    col = INC22[li]
    kk2 = kk + col  # refundamentalization of link li
    ok = ok and (kk2.sum() == kk.sum())  # total invariant
    dQA = int(kk2[regionA].sum() - kk[regionA].sum())
    dQB = int(kk2[regionB].sum() - kk[regionB].sum())
    ok = ok and (dQA + dQB == 0)  # regional shifts compensate exactly
check("D5 total Q invariant under refundamentalizing any link; regional"
      " splits shift compensatingly (boundary chart covariance)", ok)

# ---------------------------------------------------------------------------
# Section E: pointwise selector interface arithmetic on the derived context
# ---------------------------------------------------------------------------
print("Section E: selector interface arithmetic")

wpi = np.array([((-1) ** Q) * ZQ(2.0, 16, Q) for Q in range(-6, 7)])
w0 = np.array([ZQ(2.0, 16, Q) for Q in range(-6, 7)])
check("E1 at theta=pi odd winding sectors carry negative weight; at theta=0"
      " all sector weights nonnegative",
      bool(np.all(w0 >= 0)) and all(wpi[Q + 6] < 0 for Q in [-3, -1, 1, 3]))

# ---------------------------------------------------------------------------
# Section F: nonabelian contrast on the same gluing
# ---------------------------------------------------------------------------
print("Section F: nonabelian matched-label contrast")


def su2(t: float, x: float, y: float, z: float) -> np.ndarray:
    return np.array([[t + 1j * z, 1j * x + y], [1j * x - y, t - 1j * z]],
                    dtype=complex)


def chi_su2_mat(j: float, M: np.ndarray) -> float:
    tr = float(np.trace(M).real) / 2.0
    tr = min(1.0, max(-1.0, tr))
    thh = float(np.arccos(tr))
    if abs(np.sin(thh)) < 1e-12:
        return (2 * j + 1) * float(np.cos(2 * j * thh))
    return float(np.sin((2 * j + 1) * thh) / np.sin(thh))


NP_, NT_, NF_ = 48, 24, 48
psis = (np.arange(NP_) + 0.5) * np.pi / NP_
thetas_ = (np.arange(NT_) + 0.5) * np.pi / NT_
phis = (np.arange(NF_) + 0.5) * 2 * np.pi / NF_
A2 = su2(np.cos(0.4), np.sin(0.4) * 0.0, np.sin(0.4) * 0.6, np.sin(0.4) * 0.8)
B2 = su2(np.cos(1.1), np.sin(1.1) * 1.0, 0.0, 0.0)
acc = {(a, b): 0.0 for a in (0.5, 1.0) for b in (0.5, 1.0)}
norm = 0.0
for ps in psis:
    sp = np.sin(ps)
    for tt in thetas_:
        st = np.sin(tt)
        for ff in phis:
            wgt = sp * sp * st
            nvec = np.array([st * np.cos(ff), st * np.sin(ff), np.cos(tt)])
            V2 = su2(np.cos(ps), *(np.sin(ps) * nvec))
            norm += wgt
            for a in (0.5, 1.0):
                ca = chi_su2_mat(a, A2 @ V2)
                for b in (0.5, 1.0):
                    acc[(a, b)] += wgt * ca * chi_su2_mat(b, V2.conj().T @ B2)
ok = True
for a in (0.5, 1.0):
    for b in (0.5, 1.0):
        val = acc[(a, b)] / norm
        ref = chi_su2_mat(a, A2 @ B2) / (2 * a + 1) if a == b else 0.0
        ok = ok and abs(val - ref) < 2e-3
check("F1 SU(2) gluing identity int dV chi_a(AV) chi_b(V^dag B)"
      " = delta_ab chi_a(AB)/d_a (S^3 quadrature)", ok)

NW = 4096
tw = np.linspace(0.0, np.pi, NW, endpoint=False) + np.pi / (2 * NW)
weyl = np.sin(tw) ** 2
ok = True
for a_n in range(0, 4):
    for b_n in range(0, 4):
        val = float(np.sum(weyl * (np.sin((a_n + 1) * tw) / np.sin(tw))
                           * (np.sin((b_n + 1) * tw) / np.sin(tw))) /
                    np.sum(weyl) / 1.0)
        # normalized Weyl measure on SU(2) classes: (2/pi) sin^2 dtheta
        ok = ok and abs(val - (1.0 if a_n == b_n else 0.0)) < 1e-10
check("F2 SU(2) character orthogonality under the Weyl class measure", ok)

ok = True
detail = ""
for beta, nmax in [(1.0, 8), (6.0, 16)]:
    # nmax keeps every coefficient far above the quadrature roundoff floor
    cj = []
    for n in range(0, nmax + 1):
        wv = np.exp(beta * np.cos(tw)) * (np.sin((n + 1) * tw) / np.sin(tw))
        cj.append(float(np.sum(weyl * wv) / np.sum(weyl)))
    cj = np.array(cj)
    zt = float(np.sum(cj / (np.arange(0, nmax + 1) + 1.0)))
    ok = ok and bool(np.all(cj > 0)) and zt > 0
    if beta == 6.0:
        detail = f"beta=6: Z(1-cell torus) = sum_j c_j/d_j = {zt:.6f}"
check("F3 SU(2) matched-label decomposition on the 1-cell torus:"
      " Z = sum_j c_j/d_j with every sector weight positive", ok, detail)


def su3_char_t(p: int, q: int, t1: np.ndarray, t2: np.ndarray) -> np.ndarray:
    z1 = np.exp(1j * t1)
    z2 = np.exp(1j * t2)
    z3 = np.exp(-1j * (t1 + t2))
    lam = [p + q, q, 0]
    e = [lam[j] + 2 - j for j in range(3)]

    def det3(a, b, c):
        return (a[0] * (b[1] * c[2] - b[2] * c[1])
                - a[1] * (b[0] * c[2] - b[2] * c[0])
                + a[2] * (b[0] * c[1] - b[1] * c[0]))

    num = det3([z1 ** e[0], z1 ** e[1], z1 ** e[2]],
               [z2 ** e[0], z2 ** e[1], z2 ** e[2]],
               [z3 ** e[0], z3 ** e[1], z3 ** e[2]])
    den = det3([z1 ** 2, z1, np.ones_like(z1)],
               [z2 ** 2, z2, np.ones_like(z2)],
               [z3 ** 2, z3, np.ones_like(z3)])
    return num / den


NQ = 200
g1 = (np.arange(NQ) + 0.5) * 2 * np.pi / NQ
g2 = (np.arange(NQ) + 0.13) * 2 * np.pi / NQ
T1G, T2G = np.meshgrid(g1, g2, indexing="ij")
Z1 = np.exp(1j * T1G)
Z2 = np.exp(1j * T2G)
Z3 = np.exp(-1j * (T1G + T2G))
DD = (np.abs((Z1 - Z2) * (Z1 - Z3) * (Z2 - Z3)) ** 2)
RETR = (Z1 + Z2 + Z3).real
beta = 6.0
WGT = np.exp((beta / 3.0) * RETR) * DD
NRM = float(np.sum(DD))
coefs = {}
for (p, q) in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]:
    ch = su3_char_t(p, q, T1G, T2G)
    coefs[(p, q)] = float(np.sum(WGT * np.conj(ch)).real / NRM)
ok = (all(v > 0 for v in coefs.values())
      and abs(coefs[(1, 0)] - coefs[(0, 1)]) < 1e-8 * abs(coefs[(1, 0)])
      and abs(coefs[(2, 0)] - coefs[(0, 2)]) < 1e-8 * abs(coefs[(2, 0)]))
check("F4 SU(3) dual coefficients at beta=6: positive on every matched label,"
      " conjugation-paired", ok,
      f"c00={coefs[(0,0)]:.5f} c10={coefs[(1,0)]:.5f} c11={coefs[(1,1)]:.5f}"
      f" c20={coefs[(2,0)]:.5f}")

Q1 = lambda p, q: p - q
Q2 = lambda p, q: (p - q) ** 3
ok = (Q1(0, 1) == -Q1(1, 0) and Q2(0, 1) == -Q2(1, 0)
      and Q1(0, 2) == -Q1(2, 0) and Q2(0, 2) == -Q2(2, 0)
      and Q1(2, 0) != Q2(2, 0)
      and coefs[(1, 0)] > 0 and (Q1(1, 0) % 2 == 1))
check("F5 Z-valued conjugation-odd functions on the SU(3) matched labels"
      " exist with odd support and are NON-unique (p-q vs (p-q)^3)", ok)

print("Section G: source-boundary guards")
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md"
note = NOTE.read_text(encoding="utf-8")
check("G1 note declares canonical bounded_theorem claim type", "**Claim type:** bounded_theorem" in note)
check("G2 note separates scope from claim type", "**Scope:** exact finite witness-surface constructions plus wall-sharpening" in note)
check("G3 note does not use runner PASS as source status", "**Status:** PASS" not in note)
check("G4 note does not expose effective_status metadata", "effective_status =" not in note and "effective_status:" not in note)
check("G5 note does not lean on in-flight PR wording as authority", "in-flight" not in note)
check("G6 witness-surface is explicitly not physical", "not the physical gauge" in note and "sector" in note)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
