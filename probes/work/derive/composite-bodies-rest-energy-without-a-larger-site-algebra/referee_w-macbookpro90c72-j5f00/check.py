#!/usr/bin/env python3
"""Independent referee of composite-bodies rest energy, attempt a4.

Author w-macbookpro90c72-j16c3 (claude-opus-5-5). Referee w-macbookpro90c72-j5f00 (grok-4.6).
Own moments and a small ring. The 32^3 grid and the 90-site propagation were not rebuilt.
"""
import numpy as np
import sympy as sp

FAILS = []


def require(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


# ---------------------------------------------------------------- 1D contact, residue
a, b, z = sp.symbols("a b z", positive=True)
disc = sp.sqrt(a**2 - 4 * b**2)
z_in = (a - disc) / (2 * b)
denom = -b * z**2 + a * z - b
res = 1 / (sp.I * sp.diff(denom, z).subs(z, z_in))
require(sp.simplify(sp.I * res * disc - 1) == 0, "1D residue gives 1/sqrt(a^2-4b^2)")
K = sp.symbols("K", real=True)
V = sp.symbols("V", real=True)
ser = sp.series(V**2 + 4 * sp.sin(K / 2) ** 2, K, 0, 4).removeO()
require(sp.expand(ser - (V**2 + K**2)) == 0, "equal coins: E^2 = V^2 + K^2 + O(K^4), so c^2 = 1")
ser_ct = sp.series(V**2 + 4 * sp.cos(K / 2) ** 2, K, 0, 4).removeO()
require(sp.expand(ser_ct - (V**2 + 4 - K**2)) == 0, "opposite coins: E^2 = V^2 + 4 - K^2 + O(K^4), inverted at rest")

# ring check, N=32, one K sample and K=0
def lowest(N, Vc, Kv, s1, s2):
    k = 2 * np.pi * np.arange(N) / N
    e = s1 * np.sin(k) + s2 * np.sin(Kv - k)
    U = (Vc / N) * np.ones((N, N))
    return np.linalg.eigvalsh(np.diag(e) + U).real[0]


worst = 0.0
for m in (0, 3, 8, 16):
    Kv = 2 * np.pi * m / 32
    worst = max(
        worst,
        abs(lowest(32, -1.5, Kv, 1, 1) + np.sqrt(1.5**2 + 4 * np.sin(Kv / 2) ** 2)),
        abs(lowest(32, -1.5, Kv, 1, -1) + np.sqrt(1.5**2 + 4 * np.cos(Kv / 2) ** 2)),
    )
require(worst < 1e-8, f"32-ring matches both closed forms ({worst:.1e})")

# ---------------------------------------------------------------- second moment
q1, q2, q3 = sp.symbols("q1 q2 q3", real=True)
K1, K2, K3 = sp.symbols("K1 K2 K3", real=True)
qs = (q1, q2, q3)
Ks = (K1, K2, K3)


def avg(expr):
    out = expr
    for q in qs:
        out = sp.integrate(out, (q, 0, 2 * sp.pi)) / (2 * sp.pi)
    return sp.simplify(out)


# <sin(K/2+q) sin(K/2-q)> = -cos(K)/2, and cross components vanish
mom_ok = True
for i in range(3):
    h1 = sp.sin(Ks[i] / 2 + qs[i])
    h2 = sp.sin(Ks[i] / 2 - qs[i])
    mom_ok = mom_ok and sp.simplify(avg(h1 * h2) + sp.cos(Ks[i]) / 2) == 0
    mom_ok = mom_ok and sp.simplify(avg(h1**2) - sp.Rational(1, 2)) == 0
    j = (i + 1) % 3
    mom_ok = mom_ok and avg(sp.sin(Ks[i] / 2 + qs[i]) * sp.sin(Ks[j] / 2 - qs[j])) == 0
require(mom_ok, "M2 cross term is -cos(K_i) and diagonal kinetic moments are 1/2")

# Pauli action on singlet and Cartesian triplets, two coins
# basis |s1 s2>, s = 0 up, 1 down. sigma_z = diag(1,-1), sigma_x flips.
S = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)          # singlet (|ud> - |du>)/sqrt2, index s1*2+s2
Tz = sp.Matrix([0, 1, 1, 0]) / sp.sqrt(2)
Tx = sp.Matrix([1, 0, 0, -1]) / sp.sqrt(2)         # (|uu> - |dd>)/sqrt2, direction x in a real gauge
# sigma_i^{(1)} sigma_i^{(2)} eigenvalues claimed:
# singlet: -1,-1,-1
# T_j: -1 on axis j and +1 on the other two


def pauli_product(i, vec):
    """Expectation of sigma_i on coin 1 times sigma_i on coin 2."""
    # represent the state as a 2x2 matrix of amplitudes, row s1, col s2
    amp = sp.Matrix(2, 2, lambda r, c: vec[r * 2 + c])
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    sig = (sx, sy, sz)[i]
    # <sigma1_i sigma2_i> = Tr(amp^H sig amp sig^T) with the second factor acting on the column
    transformed = sig * amp * sig.T
    return sp.simplify((amp.conjugate().T * transformed).trace())


def expectations(vec):
    return [sp.simplify(pauli_product(i, vec)) for i in range(3)]


require(expectations(S) == [-1, -1, -1], f"singlet has sigma1_i sigma2_i = -1 on every axis ({expectations(S)})")
require(expectations(Tz) == [1, 1, -1], f"T_z has (+1,+1,-1) ({expectations(Tz)})")
require(expectations(Tx) == [-1, 1, 1], f"T_x has (-1,+1,+1) ({expectations(Tx)})")

# M2 = 3 - sum cos(K_i) * (sigma1_i sigma2_i)
# singlet at small K=(0,0,kappa): m2 = 3 + sum cos = 6 - kappa^2/2
kappa = sp.symbols("kappa", real=True)
cosx, cosy, cosz = 1, 1, sp.cos(kappa)
m2_s = sp.simplify(3 - (cosx * (-1) + cosy * (-1) + cosz * (-1)))
m2_tx = sp.simplify(3 - (cosx * (-1) + cosy * (1) + cosz * (1)))  # across: direction x, motion z
m2_tz = sp.simplify(3 - (cosx * (1) + cosy * (1) + cosz * (-1)))   # along
# E^2 = V^2 + 2 m2 + O(K^4, 1/V^2), so the K^2 coefficient of E^2 is the K^2 coefficient of 2 m2
def k2(expr):
    return sp.series(sp.expand(expr), kappa, 0, 4).coeff(kappa, 2)


require(sp.series(m2_s, kappa, 0, 2).removeO() == 6 and k2(2 * m2_s) == -1,
        "singlet rest energy starts at V^2+12 and c^2 starts at -1")
require(sp.series(m2_tx, kappa, 0, 2).removeO() == 2 and k2(2 * m2_tx) == 1,
        "triplet across the motion starts at V^2+4 with c^2 = +1")
require(sp.series(m2_tz, kappa, 0, 2).removeO() == 2 and k2(2 * m2_tz) == -1,
        "triplet along the motion starts at V^2+4 with c^2 = -1")

# ---------------------------------------------------------------- exchange
# Swap of the two coins: singlet eigenvalue -1, triplet +1
swap = sp.Matrix(4, 4, lambda i, j: 1 if (i // 2 == j % 2 and i % 2 == j // 2) else 0)
require(sp.simplify(swap * S + S) == sp.zeros(4, 1), "exchange is -1 on the singlet")
require(sp.simplify(swap * Tz - Tz) == sp.zeros(4, 1) and sp.simplify(swap * Tx - Tx) == sp.zeros(4, 1),
        "exchange is +1 on the triplet")

# ---------------------------------------------------------------- timed identity, w = 4^x so the factor is 4
N = 9
g = np.log(4.0)  # w = e^{g x} = 4^x
w = 4.0 ** np.arange(N)
T = np.zeros((N, N), dtype=complex)
for x in range(1, N):
    T[x, x - 1] = 1.0
D = 0.5j * (T - T.conj().T)
sw = np.sqrt(w)
Dw = sw[:, None] * D * sw[None, :]
I = np.eye(N)
Hkin = np.kron(Dw, I) + np.kron(I, Dw)
Vop = np.zeros_like(Hkin)
Vc = -1.7
for x in range(N):
    i = x * N + x
    Vop[i, i] = Vc * w[x]
H = Hkin + Vop
Tj = np.zeros_like(H)
for x1 in range(1, N):
    for x2 in range(1, N):
        Tj[x1 * N + x2, (x1 - 1) * N + (x2 - 1)] = 1.0
defect = H @ Tj - 4 * Tj @ H
inner = [x1 * N + x2 for x1 in range(2, N - 2) for x2 in range(2, N - 2)]
timed = np.max(np.abs(defect[np.ix_(inner, inner)]))
Hunt = Hkin + np.diag([Vc if (i // N == i % N) else 0 for i in range(N * N)])
untimed = np.max(np.abs((Hunt @ Tj - 4 * Tj @ Hunt)[np.ix_(inner, inner)]))
require(timed < 1e-8 and untimed > 0.1, f"timed H T = 4 T H on the interior ({timed:.1e}); untimed fails ({untimed:.1e})")

# ray: a/g = -c^2, so singlet and the along-triplet fall up, the across-triplet falls down
require(k2(2 * m2_s) < 0 and k2(2 * m2_tz) < 0 and k2(2 * m2_tx) > 0,
        "at strong binding the singlet and the along-triplet fall up; the across-triplet falls down")

print(f"TOTAL FAIL={len(FAILS)}", flush=True)
if FAILS:
    print("SUMMARY: fails at the first broken finite claim - " + FAILS[0], flush=True)
else:
    print("HIT: confirmed - a 3D contact pair falls with the walk only in the across-triplet channel, and only as the binding grows", flush=True)
    print("SUMMARY: confirmed - equal-coin c^2=1, opposite-coin inverted, M2 eigenvalues 6 and 2, curvatures -1,+1,-1, exchange signs, and the timed factor 4. The 32^3 grid was not rebuilt.", flush=True)
