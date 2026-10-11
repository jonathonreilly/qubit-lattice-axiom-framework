# G1 check 2: the umklapp set on the on-shell 2<->2 manifold M is open and of
# order-one fraction for several lifts (fundamental-domain choices), d = 2, 3,
# TB and KG, plus the reduced-zone (period pi) lift relevant to staggered tastes.
# Also: near-forward umklapp at the zone edge (small transfer).
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(11)
TP = 2*np.pi
def eps_tb(k): return -np.sum(np.cos(k), axis=-1)
def eps_kg(m): return lambda k: np.sqrt(m*m + 2*np.sum(1-np.cos(k), axis=-1))
def lift_std(k, P=TP):      # (-P/2, P/2]
    return k - P*np.round(k/P)
def lift_shift(a):
    return lambda k: (k - a) - TP*np.round((k - a)/TP) + a
def lift_wiggly(k):
    # jump surface for component 0 at k0 = pi + 0.6 sin(k1) (+0.4 sin(k2) in 3D);
    # other components standard
    k = np.asarray(k, float)
    s = lift_std(k)
    b = 0.6*np.sin(k[..., 1]) + (0.4*np.sin(k[..., 2]) if k.shape[-1] > 2 else 0)
    c = np.pi + b   # domain for component 0: (c - 2pi, c]
    x = k[..., 0]
    s0 = x - TP*np.ceil((x - c)/TP)
    s = s.copy(); s[..., 0] = s0
    return s
def lift_red(k):            # period-pi reduced zone, (-pi/2, pi/2]
    return lift_std(k, np.pi)
def sample_M(eps, d, n):
    out = []
    while len(out) < n:
        k1 = rng.uniform(-np.pi, np.pi, d); k2 = rng.uniform(-np.pi, np.pi, d)
        K = k1 + k2; E = eps(k1) + eps(k2)
        b = rng.uniform(-np.pi, np.pi, d); u = rng.normal(size=d); u /= np.linalg.norm(u)
        f = lambda t: eps(b + t*u) + eps(K - b - t*u) - E
        ts = np.linspace(0, 3*TP, 721); fv = np.array([f(t) for t in ts])
        for i in np.nonzero(np.sign(fv[:-1]) != np.sign(fv[1:]))[0]:
            t = brentq(f, ts[i], ts[i+1], xtol=1e-14)
            k3 = b + t*u; k4 = K - k3
            out.append((k1, k2, k3, k4))
    return out
def dist_to_jump(k, lift, h=1e-7):
    # crude: distance (in steps) at which the lift jumps along coordinate axes
    best = np.inf
    for j in range(len(k)):
        for sgn in (1, -1):
            for r in (1e-3, 3e-3, 1e-2, 3e-2):
                kk = k.copy(); kk[j] += sgn*r
                if np.max(np.abs(lift(kk) - lift(k) - (kk - k))) > 1:
                    best = min(best, r); break
    return best
def study(name, eps, d, n=3000):
    S = sample_M(eps, d, n)
    resid = max(abs(eps(a)+eps(b)-eps(c)-eps(e)) for a, b, c, e in S)
    lifts = {"std cube": lift_std, "shifted cube": lift_shift(np.array([0.7, -0.4, 0.25][:d])),
             "wiggly domain": lift_wiggly, "reduced zone (period pi)": lift_red}
    print(f"{name}: {len(S)} on-shell samples, max energy residual {resid:.1e}")
    for ln, L in lifts.items():
        P = 2*np.pi if ln != "reduced zone (period pi)" else np.pi
        nU = 0; nUfar = 0
        for a, b, c, e in S:
            D = L(a) + L(b) - L(c) - L(e)
            # congruence check
            assert np.max(np.abs(D/P - np.round(D/P))) < 1e-9
            if np.max(np.abs(D)) > 1:
                nU += 1
                if min(dist_to_jump(x, L) for x in (a, b, c, e)) > 3e-2: nUfar += 1
        print(f"   lift {ln:26s}: umklapp fraction {nU/len(S):.3f}; "
              f"umklapp samples with every leg >0.03 from the jump set: {nUfar}")
study("TB d=2", eps_tb, 2); study("KG m=1 d=2", eps_kg(1.0), 2)
study("KG m=0 d=2", eps_kg(0.0), 2)
study("TB d=3", eps_tb, 3, 2000); study("KG m=0.5 d=3", eps_kg(0.5), 3, 2000)
# near-forward umklapp at the zone edge: k1 just below +pi in x, transfer q small
print("near-forward umklapp (std lift), TB d=2:")
eps = eps_tb
for q in (0.2, 0.05, 0.01):
    k1 = np.array([np.pi - q/3, 0.9]); k2 = np.array([0.3, -1.1])
    K = k1 + k2; E = eps(k1) + eps(k2)
    # k3 = k1 + (q, y): solve energy for y near 0
    f = lambda y: eps(k1 + np.array([q, y])) + eps(K - k1 - np.array([q, y])) - E
    ys = np.linspace(-1, 1, 2001); fv = np.array([f(y) for y in ys])
    idx = np.nonzero(np.sign(fv[:-1]) != np.sign(fv[1:]))[0]
    if len(idx) == 0: print("   no root", q); continue
    y = min((brentq(f, ys[i], ys[i+1], xtol=1e-15) for i in idx), key=abs)
    k3 = k1 + np.array([q, y]); k4 = K - k3
    D = lift_std(k1) + lift_std(k2) - lift_std(k3) - lift_std(k4)
    print(f"   |k3-k1|={np.hypot(q,y):.4f}  residual {f(y):.1e}  D/2pi = {np.round(D/TP,6)}")
