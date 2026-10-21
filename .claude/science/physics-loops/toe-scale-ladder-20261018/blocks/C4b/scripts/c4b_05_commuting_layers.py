"""C4b-05: in-premise (Z^3-TI, one qubit per site) non-Clifford O-covariant QCAs from commuting
covariant Pauli layers, and the Clifford composite of the two range-2 C4 circuits.

Layer family: alpha_P(theta) = Ad( prod_r exp(i theta P_r) ), P a Pauli string with
  (i)  beta_R(P_0) = + P_{0} (same sign!) for all R in O  [needed for generic theta]
  (ii) all translates P_r, P_s commute (so the product is well defined and TI).
Strings: C = Chamon  X(+-x) Y(+-y) Z(+-z);  K = cuboctahedral X(0,+-1,+-1) Y(+-1,0,+-1) Z(+-1,+-1,0).
Checks: (i),(ii) for axis and full; whether C and K translates commute (if all commute, the
two-layer circuit is a commuting circuit, frozen); then the Clifford point theta = pi/4 of the
composite alpha_C alpha_K: F2 symplectic image of X_0, Z_0; trace polynomial tau; exact
iteration of supports (independent of C4's Theorem 2).
"""
import itertools
import numpy as np
from c4b_common import check, total, O, menu_Q

LET = {'X': (1, 0), 'Z': (0, 1), 'Y': (1, 1)}
INVLET = {v: k for k, v in LET.items()}
AX = {'X': 0, 'Y': 1, 'Z': 2}
AXL = 'XYZ'


def string_C():
    P = {}
    for a, L in zip(range(3), 'XYZ'):
        for s in (1, -1):
            v = [0, 0, 0]; v[a] = s
            P[tuple(v)] = L
    return P


def string_K():
    P = {}
    for a, L in zip(range(3), 'XYZ'):
        others = [b for b in range(3) if b != a]
        for s1 in (1, -1):
            for s2 in (1, -1):
                v = [0, 0, 0]; v[others[0]] = s1; v[others[1]] = s2
                P[tuple(v)] = L
    return P


def beta(R, act, P):
    """signed image of a Pauli string (dict site->letter) under beta_R; returns (sign, dict)."""
    Q = menu_Q(R, act)
    sign = 1
    out = {}
    for r, L in P.items():
        a = AX[L]
        col = Q[:, a]
        b = int(np.nonzero(col)[0][0])
        sign *= int(col[b])
        out[tuple(int(x) for x in R @ np.array(r))] = AXL[b]
    return sign, out


def anticommute(P, Q):
    c = 0
    for r, L in P.items():
        M = Q.get(r)
        if M is not None and M != L:
            c += 1
    return c % 2


def translate(P, t):
    return {tuple(a + b for a, b in zip(r, t)): L for r, L in P.items()}


STR = {'C': string_C(), 'K': string_K()}
SHIFTS = list(itertools.product(range(-4, 5), repeat=3))
for name, P in STR.items():
    for act in ['axis', 'full']:
        ok = True
        for R in O:
            s, im = beta(R, act, P)
            ok &= (s == 1 and im == P)
        check(f"string {name}: beta_R(P_0) = +P_0 for all 24 R ({act} action)", ok)
    comm = all(anticommute(P, translate(P, t)) == 0 for t in SHIFTS)
    check(f"string {name}: all translates commute", comm)

cross = [t for t in SHIFTS if anticommute(STR['C'], translate(STR['K'], t))]
print(f"C_0 anticommutes with K_t for {len(cross)} translates t; e.g. {cross[:6]}")
check("C and K families do NOT commute (so alpha_C(th1) alpha_K(th2) is not a commuting circuit)", len(cross) > 0)

# ---------------------------------------------------------------- Clifford composite at theta = pi/4
# F2 vectors: dict site -> (x,z) bits (nonzero only)


def vec_of(P):
    return {r: LET[L] for r, L in P.items()}


def vadd(u, v):
    w = dict(u)
    for r, b in v.items():
        c = w.get(r, (0, 0))
        n = (c[0] ^ b[0], c[1] ^ b[1])
        if n == (0, 0):
            w.pop(r, None)
        else:
            w[r] = n
    return w


def omega(u, v):
    s = 0
    small, big = (u, v) if len(u) < len(v) else (v, u)
    for r, a in small.items():
        b = big.get(r)
        if b is not None:
            s ^= (a[0] & b[1]) ^ (a[1] & b[0])
    return s


PV = {k: vec_of(P) for k, P in STR.items()}
OFFS = {k: list(P.keys()) for k, P in STR.items()}


def apply_layer(name, v):
    """unsigned action of prod_r exp(i pi/4 P_r): v -> v + sum_{r: omega(P_r, v)=1} P_r."""
    cand = set()
    for site in v:
        for o in OFFS[name]:
            cand.add(tuple(a - b for a, b in zip(site, o)))
    out = dict(v)
    for r in cand:
        Pr = {tuple(a + b for a, b in zip(s, r)): bit for s, bit in PV[name].items()}
        if omega(Pr, v):
            out = vadd(out, Pr)
    return out


def alpha(v):          # composite alpha_C o alpha_K  (apply K first, then C)
    return apply_layer('C', apply_layer('K', v))


X0 = {(0, 0, 0): (1, 0)}
Z0 = {(0, 0, 0): (0, 1)}
aX, aZ = alpha(X0), alpha(Z0)
# symplecticity spot-check: images of X_0 and Z_0 anticommute; images of X_0 and translated X_t commute
symp = omega(aX, aZ) == 1
for t in itertools.product(range(-6, 7), repeat=3):
    if t == (0, 0, 0):
        continue
    tX = {tuple(a + b for a, b in zip(r, t)): v for r, v in aX.items()}
    tZ = {tuple(a + b for a, b in zip(r, t)): v for r, v in aZ.items()}
    if omega(aX, tX) or omega(aZ, tZ) or omega(aX, tZ):
        symp = False
        break
check("composite alpha_C alpha_K preserves commutation (images of X_0, Z_0 and translates)", symp)
rng_ = max(max(abs(c) for c in r) for r in list(aX) + list(aZ))
print(f"composite: |supp alpha(X_0)| = {len(aX)}, |supp alpha(Z_0)| = {len(aZ)}, Chebyshev range = {rng_}")
# trace polynomial tau = [X-part of alpha(X_0)] + [Z-part of alpha(Z_0)]
tau = {}
for r, b in aX.items():
    if b[0]:
        tau[r] = tau.get(r, 0) ^ 1
for r, b in aZ.items():
    if b[1]:
        tau[r] = tau.get(r, 0) ^ 1
tau = {r for r, c in tau.items() if c}
print(f"tau = tr M has {len(tau)} monomials; nonconstant = {tau != {(0, 0, 0)} and tau != set()}")
print(f"tau monomials (sorted): {sorted(tau)}")
check("composite: tau is nonconstant => ballistic spreading by C4 Theorem 2(c) (any range)",
      len(tau - {(0, 0, 0)}) > 0)

# independent of Theorem 2: iterate exactly
v = dict(X0)
sizes, radii = [], []
for n in range(1, 9):
    v = alpha(v)
    sizes.append(len(v))
    radii.append(max(max(abs(c) for c in r) for r in v))
print("iterate alpha^n(X_0): |supp| =", sizes, " Chebyshev radius =", radii)
check("alpha^n(X_0) Chebyshev radius grows linearly (radius(8) >= 2*radius(1)*... i.e. >= 8)",
      radii[-1] >= 8 and radii[-1] > radii[0])
total()
