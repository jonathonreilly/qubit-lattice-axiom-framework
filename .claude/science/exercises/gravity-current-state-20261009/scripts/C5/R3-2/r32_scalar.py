"""C5 R3-2: beyond TT. With only the 2+4 Lorentz(O(4))-invariant forms, which
directions does a conserved source see at long range?

Euclidean O(4) stand-in (same projector algebra as SO(1,3)).
Forms: F1 = q^2 h.h, F2 = (q.h)^2, F3 = (q.h.q) tr h, F4 = q^2 (tr h)^2,
       M1 = h.h, M2 = (tr h)^2.   EH = (F1 - 2F2 + 2F3 - F4)/4 (K1 combination).
Long-range amplitude between conserved sources: q^2 * T K^{-1} T -> c1 T.T + c2 (tr T)^2.
GR value: c2/c1 = -1/2 (in d=4).  A massive spin-2 (vDVZ) gives -1/3.
"""
import numpy as np

rng = np.random.default_rng(11)
SB = [(a, b) for a in range(4) for b in range(a, 4)]


def vec_to_h(v):
    h = np.zeros((4, 4))
    for x, (a, b) in zip(v, SB):
        h[a, b] = h[b, a] = x
    return h


def form_matrix(f, q):
    """10x10 symmetric matrix of the quadratic form f(h) in coordinates v (h = vec_to_h(v))."""
    E = np.eye(10)
    M = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            hi, hj = vec_to_h(E[i]), vec_to_h(E[j])
            M[i, j] = 0.5 * (f(hi + hj, q) - f(hi, q) - f(hj, q))
    return M


F = {
    "F1": lambda h, q: q.dot(q) * np.sum(h * h),
    "F2": lambda h, q: np.sum(q.dot(h) ** 2),
    "F3": lambda h, q: q.dot(h).dot(q) * np.trace(h),
    "F4": lambda h, q: q.dot(q) * np.trace(h) ** 2,
    "M1": lambda h, q: np.sum(h * h),
    "M2": lambda h, q: np.trace(h) ** 2,
}


def source_pairing(T):
    """h.T in coordinates: returns vector s with h.T = s.v."""
    E = np.eye(10)
    return np.array([np.sum(vec_to_h(E[i]) * T) for i in range(10)])


def conserved_T(q):
    P = np.eye(4) - np.outer(q, q) / q.dot(q)
    A = rng.normal(size=(4, 4)); A = A + A.T
    return P.dot(A).dot(P)


def amplitude_ratio(coef, q_scale=1e-3, gauge_fix=0.0, trials=6):
    """Fit q^2 T K^{-1} T = c1 T.T + c2 (trT)^2 at small q."""
    rows, rhs = [], []
    for _ in range(trials):
        qd = rng.normal(size=4); qd /= np.linalg.norm(qd)
        q = q_scale * qd
        K = sum(c * form_matrix(F[k], q) for k, c in coef.items())
        if gauge_fix:
            K = K + gauge_fix * form_matrix(lambda h, qq: np.sum((qq.dot(h) - 0.5 * qq * np.trace(h)) ** 2), q)
        T = conserved_T(q)
        s = source_pairing(T)
        amp = s.dot(np.linalg.solve(K, s)) * q.dot(q)
        rows.append([np.sum(T * T), np.trace(T) ** 2])
        rhs.append(amp)
    c, *_ = np.linalg.lstsq(np.array(rows), np.array(rhs), rcond=None)
    resid = np.abs(np.array(rows).dot(c) - rhs).max() / np.abs(rhs).max()
    return c, resid


EH = {"F1": 0.25, "F2": -0.5, "F3": 0.5, "F4": -0.25}
c, r = amplitude_ratio(EH, gauge_fix=1.0)
print(f"EH + de Donder gauge fixing: c2/c1 = {c[1]/c[0]:+.6f} (GR -1/2), fit resid {r:.1e}")
c, r = amplitude_ratio(EH, gauge_fix=3.7)
print(f"EH + other gauge-fix weight: c2/c1 = {c[1]/c[0]:+.6f}, fit resid {r:.1e}")

# Fierz-Pauli massive at q -> 0 with fixed small mass ratio q^2/m^2 -> 0 is contact; use m << q:
FP = dict(EH); FP["M1"] = -1e-9; FP["M2"] = +1e-9
c, r = amplitude_ratio(FP, q_scale=1e-2)
print(f"EH + tiny Fierz-Pauli mass (m^2 << q^2): c2/c1 = {c[1]/c[0]:+.6f} (vDVZ -1/3), fit resid {r:.1e}")

print("\nGeneric Lorentz-invariant non-gauge kinetic terms, TT mass m1^2 = 0 tuned, natural trace mass m2^2:")
for trial in range(4):
    eps = 0.3 * rng.normal(size=4)
    coef = {k: EH[k] + e for k, e in zip(["F1", "F2", "F3", "F4"], eps)}
    coef["M2"] = 1.0          # natural (cutoff-size) trace mass; M1 (TT mass) tuned to 0
    c, r = amplitude_ratio(coef)
    print(f"  eps={np.round(eps,3)}: c1 = {c[0]:+.4f} (GR 1 in these units x norm), c2/c1 = {c[1]/c[0]:+.6f}, resid {r:.1e}")

print("\nSame kinetic terms, no trace mass (m1 = m2 = 0):")
for trial in range(3):
    eps = 0.3 * rng.normal(size=4)
    coef = {k: EH[k] + e for k, e in zip(["F1", "F2", "F3", "F4"], eps)}
    c, r = amplitude_ratio(coef)
    print(f"  eps={np.round(eps,3)}: c2/c1 = {c[1]/c[0]:+.6f}, resid {r:.1e}")

# Which single kinetic condition restores -1/2 with M2 = 1?  scan one coefficient
print("\nOne-parameter restoration (M2 = 1, kinetic = EH + eps0, then shift F4 by t):")
eps0 = np.array([0.2, -0.1, 0.15, 0.05])
from scipy.optimize import brentq
def g(t):
    coef = {k: EH[k] + e for k, e in zip(["F1", "F2", "F3", "F4"], eps0)}
    coef["F4"] += t
    coef["M2"] = 1.0
    c, _ = amplitude_ratio(coef, trials=6)
    return c[1] / c[0] + 0.5
ts = np.linspace(-1.0, 1.0, 21)
vals = [g(t) for t in ts]
roots = []
for a, b, va, vb in zip(ts[:-1], ts[1:], vals[:-1], vals[1:]):
    if np.sign(va) != np.sign(vb) and abs(va) < 5 and abs(vb) < 5:
        try:
            roots.append(brentq(g, a, b, xtol=1e-10))
        except Exception:
            pass
print("  roots t* where c2/c1 = -1/2:", [round(x, 8) for x in roots])

print("  scan values c2/c1 + 1/2 (M2=1):", np.round(vals, 4))
print("\nSame scan with M2 = 0 (TT and trace masses both tuned):")
def g0(t, m2=0.0, which="F4"):
    coef = {k: EH[k] + e for k, e in zip(["F1", "F2", "F3", "F4"], eps0)}
    coef[which] += t
    if m2:
        coef["M2"] = m2
    c, _ = amplitude_ratio(coef, trials=6)
    return c[1] / c[0] + 0.5
for which in ["F4", "F3", "F2"]:
    vals0 = [g0(t, 0.0, which) for t in ts]
    rts = []
    for a, b, va, vb in zip(ts[:-1], ts[1:], vals0[:-1], vals0[1:]):
        if np.sign(va) != np.sign(vb) and abs(va) < 5 and abs(vb) < 5:
            try:
                rts.append(brentq(lambda t: g0(t, 0.0, which), a, b, xtol=1e-10))
            except Exception:
                pass
    print(f"  shift {which}: roots where c2/c1 = -1/2: {[round(x, 8) for x in rts]}")
# with M2 = 1, scan a 2D family F3,F4 for the reachable range of c2/c1
rng2 = np.random.default_rng(5)
rs = []
for _ in range(300):
    e = rng2.normal(size=4) * 0.8
    coef = {k: EH[k] + x for k, x in zip(["F1", "F2", "F3", "F4"], e)}
    coef["M2"] = 1.0
    c, _ = amplitude_ratio(coef, trials=5)
    rs.append(c[1] / c[0])
rs = np.array(rs)
print(f"\nM2=1, 300 random kinetic sets: c2/c1 range [{rs.min():.4f}, {rs.max():.4f}]; fraction within 1e-3 of -1/2: {(np.abs(rs+0.5)<1e-3).mean():.3f}; within 1e-3 of -1/3: {(np.abs(rs+1/3)<1e-3).mean():.3f}")
