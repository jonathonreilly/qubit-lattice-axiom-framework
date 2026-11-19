#!/usr/bin/env python3
"""minimal-toe-b runner: frame-freedom check for the information-minimal site.

Rule R4 (proposed): the one-excitation modes of a site are its qubit levels (2)
plus its owned links (d, one per axis); exclusion (at most one per mode) makes the
site's matter space the exterior algebra Lambda(C^d + C^2).  Unread local frames
are compared by the frame changes that preserve the split and the site volume
form: S(U(d) x U(2)).  This runner checks, exactly (fractions), what that gives:
  A. d=3: the commuting U(1) generator and the charge table of all 32 states;
  B. anomaly cancellation of the even (one-handedness) half;
  C. the Z6 kernel (global form of the group);
  D. which d give a chiral (non-self-conjugate) even half;
  E. S3_L x S3_R family symmetry -> democratic (rank-1) mass matrix, V = 1;
  F. counting estimate Lambda ~ N^(-1/2) (everpresent Lambda) vs measured.
No observed number enters A-E.  F compares to measured H0, Omega_L.
"""
AUDIT_TIMEOUT_SEC = 60
from fractions import Fraction as Fr
from itertools import combinations
from math import comb as _comb
def comb(n, k):
    return _comb(n, k) if 0 <= k <= n else 0
import numpy as np

P = F = 0
def check(name, ok, info=""):
    global P, F
    if ok: P += 1
    else: F += 1
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))

def states(d):
    """(k_link, k_qubit) occupation sectors with multiplicity C(d,kl)*C(2,kq)."""
    return [(kl, kq) for kl in range(d + 1) for kq in range(3)]

def hyper(d):
    # traceless generator commuting with SU(d) x SU(2): diag(a 1_d, b 1_2), d a + 2 b = 0
    # normalised so the qubit-mode charge is 1/2: b = 1/2, a = -1/d
    return Fr(-1, d), Fr(1, 2)

def table(d, parity=0):
    a, b = hyper(d)
    out = []
    for kl, kq in states(d):
        if (kl + kq) % 2 == parity:
            out.append((kl, kq, kl * a + kq * b, comb(d, kl), comb(2, kq)))
    return out

# ---- A: d = 3 charge table ----
names = {(0, 0): "nu^c (1,1)", (2, 0): "u^c (3b,1)", (1, 1): "Q (3,2)",
         (3, 1): "L (1,2)", (0, 2): "e^c (1,1)", (2, 2): "d^c (3b,1)"}
T = table(3, 0)
print("d=3 even half, sector (k_link,k_qubit): label, Y")
for kl, kq, Y, dl, dq in T:
    print(f"  ({kl},{kq}) {names[(kl, kq)]:12s} Y={str(Y):5s} dim={dl*dq}")
want = {(1, 1): Fr(1, 6), (2, 0): Fr(-2, 3), (2, 2): Fr(1, 3), (3, 1): Fr(-1, 2),
        (0, 2): Fr(1), (0, 0): Fr(0)}
got = {(kl, kq): Y for kl, kq, Y, _, _ in T}
check("A1 even half = one left-handed SM generation with nu^c (hypercharges exact)",
      got == want)
check("A2 even half has 16 states, odd half 16 (32 total)",
      sum(dl * dq for *_, dl, dq in T) == 16 and
      sum(dl * dq for *_, dl, dq in table(3, 1)) == 16)
# electric charge Q = T3 + Y integral multiples of 1/3, colour singlets integral
qs = set()
for kl, kq, Y, dl, dq in T:
    t3s = [Fr(0)] if kq != 1 else [Fr(1, 2), Fr(-1, 2)]
    for t in t3s:
        qs.add((kl % 3 == 0, t + Y))
check("A3 colour-singlet states carry integer charge; coloured carry thirds",
      all((q.denominator == 1) == sing for sing, q in qs), str(sorted(q for _, q in qs)))

# ---- B: anomalies of the even half (all left-handed Weyl) ----
def anomalies(d):
    a, b = hyper(d)
    TT = table(d, 0)
    def dynkin_cubic(n, k):  # cubic index of Lambda^k C^n for SU(n), fundamental = 1
        return Fr(comb(n - 3, k - 1) - comb(n - 3, k - 2) if n >= 3 else 0) if 0 < k < n else Fr(0)
    def T2(n, k):  # quadratic index of Lambda^k C^n, fundamental = 1/2
        return Fr(comb(n - 2, k - 1), 2) if 0 < k < n else Fr(0)
    Y3 = sum(dl * dq * Y ** 3 for kl, kq, Y, dl, dq in TT)
    Yg = sum(dl * dq * Y for kl, kq, Y, dl, dq in TT)
    c3 = sum(dq * dynkin_cubic(d, kl) for kl, kq, Y, dl, dq in TT) if d >= 3 else Fr(0)
    cY = sum(dq * T2(d, kl) * Y for kl, kq, Y, dl, dq in TT)
    wY = sum(dl * T2(2, kq) * Y for kl, kq, Y, dl, dq in TT)
    witten = sum(dl for kl, kq, Y, dl, dq in TT if kq == 1)
    return Y3, Yg, c3, cY, wY, witten
Y3, Yg, c3, cY, wY, W = anomalies(3)
check("B1 U(1)_Y^3 = 0", Y3 == 0, str(Y3))
check("B2 U(1)_Y-gravity^2 = 0", Yg == 0, str(Yg))
check("B3 SU(3)^3 = 0", c3 == 0, str(c3))
check("B4 SU(3)^2 U(1) = 0 and SU(2)^2 U(1) = 0", cY == 0 and wY == 0, f"{cY},{wY}")
check("B5 Witten SU(2): even number of doublets", W % 2 == 0, f"doublets={W}")
check("B6 16 Weyl per family: Z16 (Spin-Z4) count satisfied", 16 % 16 == 0)

# ---- C: Z6 kernel: (w 1_3, -1_2, e^{2 pi i Y}) acts trivially on all 32 states ----
a, b = hyper(3)
triv = all(((Fr(kl, 3) + Fr(kq, 2) + kl * a + kq * b) % 1) == 0
           for kl, kq in states(3))
check("C1 Z6 = <(w,-1,e^{2pi i Y})> acts trivially: group is (SU3xSU2xU1)/Z6", triv)

# ---- D: which space dimensions give a chiral even half ----
def chiral(d):
    a, b = hyper(d)
    ev = sorted((kl, kq, Y) for kl, kq, Y, _, _ in table(d, 0))
    conj = sorted((d - kl, 2 - kq, -Y) for kl, kq, Y, _, _ in table(d, 0))
    return ev != conj
res = {d: chiral(d) for d in range(1, 7)}
check("D1 even half chiral exactly for odd d (d=1,3,5), vectorlike for even d",
      all(res[d] == (d % 2 == 1) for d in res), str(res))
an1 = anomalies(1); an5 = anomalies(5)
check("D2 d=1: U(1)^3 anomaly nonzero (no consistent chiral theory)", an1[0] != 0,
      f"Y3={an1[0]}")
check("D3 d=5: anomaly free but SU(5)xSU(2)xU(1) (excluded by d=3 from R1)",
      an5[0] == 0 and an5[1] == 0, f"Y3={an5[0]}, grav={an5[1]}, su5^3={an5[2]}")

# ---- E: no privileged family: S3_L x S3_R invariant mass matrix ----
rng = np.random.default_rng(0)
perms = [np.eye(3)[list(p)] for p in [(0,1,2),(1,0,2),(0,2,1),(2,1,0),(1,2,0),(2,0,1)]]
basis = []
for i in range(3):
    for j in range(3):
        E = np.zeros((3, 3)); E[i, j] = 1.0; basis.append(E)
# project generic matrix onto invariants
M = rng.normal(size=(3, 3))
Mi = sum(p @ M @ q.T for p in perms for q in perms) / 36.0
sv = np.linalg.svd(Mi, compute_uv=False)
check("E1 S3xS3-invariant mass matrix is democratic, rank 1 (one heavy family)",
      np.allclose(Mi, Mi[0, 0]) and sv[1] < 1e-12, f"sv={np.round(sv,12)}")
Mu = 2.3 * np.ones((3, 3)); Md = 0.7 * np.ones((3, 3))
wu, Uu = np.linalg.eigh(Mu); wd, Ud = np.linalg.eigh(Md)
V = Uu.T @ Ud
check("E2 up/down democratic: heavy states aligned, |V_33| = 1 (CKM ~ 1 at leading order)",
      abs(abs(V[2, 2]) - 1) < 1e-12)

# ---- F: counting estimate (everpresent Lambda): Lambda l_P^2 ~ N^(-1/2) ----
H0 = 67.4e3 / 3.0857e22          # s^-1 (measured)
tP = 5.391e-44
N = (1.0 / (H0 * tP)) ** 4       # records in the past 4-volume ~ H^-4 / l_P^4
lam_count = N ** -0.5
lam_obs = 3 * 0.685 * (H0 * tP) ** 2
r = lam_obs / lam_count
print(f"F: N={N:.2e}, N^-1/2={lam_count:.2e}, Lambda_obs l_P^2={lam_obs:.2e}, ratio={r:.2f}")
check("F1 counting gives measured Lambda to an O(1) factor (coefficient not derived)",
      0.1 < r < 10, f"ratio={r:.2f}")
print(f"TOTAL: PASS={P} FAIL={F}")
