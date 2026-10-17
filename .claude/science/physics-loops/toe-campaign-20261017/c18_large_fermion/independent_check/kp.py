"""Items 2, 3, 5: Kramers degeneracy, Hessian isotropy, quartic anisotropy, non-abelian Berry
curvature of the lowest doublet at k*, and O x T invariant perturbations that break I*K."""
import itertools
import numpy as np
from model import *

FD = dict(square=1, triangle=0, plaquette=1, tube=1)
u = solve_gauge(FD)
PS = [(R, *psg(u, R)) for R in ROTS]
PS = [(R, eta, s, (R @ s) % 2) for R, eta, s in PS]
Iv = -np.eye(3, dtype=int); etaI, sI = psg(u, Iv); WI = Wmat(Iv, etaI); SI = (Iv @ sI) % 2
KP = np.array([1, -1, 1]) * np.pi / 2
rng = np.random.default_rng(2)
SETS = [(-1.0, 0.1, -0.5), (-1.0, -0.1, -0.5), (-1.0, 0.3, -0.5), (-1.0, 0.1, 0.5), (-1.0, 0.2, -0.3)]

def kstar_of(t1, t2, lam, extra=None):
    a = np.linalg.eigvalsh(bloch(u, KP, t1, t2, lam, extra))[0]; b = np.linalg.eigvalsh(bloch(u, -KP, t1, t2, lam, extra))[0]
    return KP if a < b else -KP

print("== Kramers: max |E_{2i}-E_{2i+1}| over 2000 random k, every band")
for p in SETS:
    ks = rng.uniform(-np.pi, np.pi, (2000, 3))
    ev = np.linalg.eigvalsh(bloch_batch(u, ks, *p))
    print(f"   {p}: max pair splitting {np.abs(ev[:, 0::2] - ev[:, 1::2]).max():.1e}; min gap between pairs {np.min(ev[:, 2::2] - ev[:, 1:-1:2]):.3e}")

print("\n== Hessian at k*, quartic anisotropy")
def e0(k, p, extra=None): return np.linalg.eigvalsh(bloch(u, k, *p, extra))[0]
for p in SETS:
    ks = kstar_of(*p); E0 = e0(ks, p)
    # fit E along 13 directions with polynomial in q (q^2, q^4, q^6) -> second- and fourth-order coefficients
    dirs = [np.array(d, float) / np.linalg.norm(d) for d in ((1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,-1,0),
                                                              (1,1,1),(1,-1,1),(-1,1,1),(1,2,3),(3,-1,2),(0.3,-0.7,0.2))]
    qs = np.linspace(0.01, 0.12, 12)
    c2, c4 = [], []
    for d in dirs:
        y = np.array([(e0(ks + q * d, p) + e0(ks - q * d, p)) / 2 - E0 for q in qs])
        A = np.vstack([qs**2, qs**4, qs**6]).T
        co = np.linalg.lstsq(A, y, rcond=None)[0]; c2.append(co[0]); c4.append(co[1])
    c2 = np.array(c2); c4 = np.array(c4)
    # finite-difference Hessian
    h = 2e-3; Hs = np.zeros((3, 3)); I3 = np.eye(3)
    for i in range(3):
        for j in range(3):
            Hs[i, j] = (e0(ks + h*(I3[i]+I3[j]), p) - e0(ks + h*(I3[i]-I3[j]), p) - e0(ks - h*(I3[i]-I3[j]), p) + e0(ks - h*(I3[i]+I3[j]), p)) / (4*h*h)
    hev = np.linalg.eigvalsh(Hs)
    an = []
    for dk in (0.2, 0.1, 0.05, 0.025):
        a100 = e0(ks + dk * np.array([1, 0, 0]), p) - E0
        a111 = e0(ks + dk * np.ones(3) / np.sqrt(3), p) - E0
        an.append((dk, (a111 - a100) / a100))
    print(f"   {p}: k*={np.round(ks/(np.pi/2)).astype(int)}  E0={E0:.6f}  FD-Hessian eig {np.round(hev,6)} (1/m* = {hev.mean():.5f}, spread {np.ptp(hev):.1e});"
          f" fitted q^2 coeff over 13 dirs: spread {np.ptp(c2):.1e} (2*c2={2*c2.mean():.5f})")
    print("      quartic coeff c4 by dir:", np.round(c4, 5), " (c4 differs [100] vs [111]: anisotropic)")
    print("      rel. [111]-[100] at dk: " + ", ".join(f"{dk}: {a:.2e}" for dk, a in an),
          f"  ratio a(0.1)/a(0.05) = {an[1][1]/an[2][1]:.2f} (4 = dk^2 scaling)")

print("\n== non-abelian Berry curvature of the lowest doublet at k* (Wilson loops)")
def doublet(k, p, extra=None):
    w, V = np.linalg.eigh(bloch(u, k, *p, extra)); return V[:, :2]
def wilson(k0, i, j, eps, p, n=16):
    e1, e2 = np.eye(3)[i], np.eye(3)[j]
    pts = []
    for t in np.linspace(0, 4, 4 * n, endpoint=False):
        side, f = int(t), t - int(t)
        corners = [(-1,-1), (1,-1), (1,1), (-1,1), (-1,-1)]
        a, b = np.array(corners[side]), np.array(corners[side + 1])
        x, y = (a + f * (b - a)) * eps / 2
        pts.append(k0 + x * e1 + y * e2)
    Vs = [doublet(q, p) for q in pts]
    W = np.eye(2, dtype=complex)
    for A, B in zip(Vs, Vs[1:] + Vs[:1]):
        M = B.conj().T @ A; uu, _, vv = np.linalg.svd(M); W = (uu @ vv) @ W
    return W
for p in SETS[:1] + SETS[3:4]:
    ks = kstar_of(*p); out = []
    for (i, j) in ((0, 1), (1, 2), (2, 0)):
        for eps in (0.04, 0.02):
            W = wilson(ks, i, j, eps, p)
            ph = np.angle(np.linalg.eigvals(W))
            out.append(((i, j), eps, np.sort(ph) / eps**2, np.angle(np.linalg.det(W)) / eps**2))
    for o in out:
        print(f"   {p} plane {o[0]} eps={o[1]}: Wilson-loop phases/area = {np.round(o[2], 4)}  (U(1) part det: {o[3]:.1e})")

# ---------------- perturbations that keep O and T but break I*K
print("\n== O x T invariant second-neighbour hops; which break I*K, and what they do at k*")
def paths2(c0):
    out = []
    for c1, sh1, k1 in neighbours(c0):
        for c2, sh2, k2 in neighbours(c1):
            sh = tuple(a + b for a, b in zip(sh1, sh2))
            if c2 == c0 and sh == (0, 0, 0): continue
            g = (-1.0) ** (u[EKEY[(c0, c1, sh1)]] + u[EKEY[(c1, c2, sh2)]])
            out.append((c2, sh, g, (k1, k2)))
    return out
def Xbloch(hops, k):
    X = np.zeros((12, 12), complex)
    for c1, c2, sh, z in hops:
        X[c2, c1] += z * np.exp(-1j * np.asarray(k) @ np.array(sh))
    return X
def Xsym(hops, k):
    k = np.asarray(k, float); X = np.zeros((12, 12), complex)
    for R, eta, s, S in PS:
        W = Wmat(R, eta); kk = R.T @ (k - np.pi * S)
        X += W @ Xbloch(hops, kk) @ W.T
    return X + X.conj().T
# group the 2-paths from corner 0 by endpoint class
cands = {}
for c2, sh, g, kinds in paths2(0):
    cands.setdefault((kinds, c2, sh), []).append(g)
res = []
for (kinds, c2, sh), gs in sorted(cands.items(), key=lambda t: str(t[0])):
    for z, zn in ((1.0, '1'), (1j, 'i')):
        hops = [(0, c2, sh, z * gg) for gg in gs]
        ks = rng.uniform(-np.pi, np.pi, (4, 3))
        nrm = max(np.abs(Xsym(hops, k)).max() for k in ks)
        if nrm < 1e-9: continue
        ikb = max(np.abs(Xsym(hops, k + np.pi * SI) - WI @ Xsym(hops, k).conj() @ WI.T).max() for k in ks)
        res.append((kinds, c2, sh, zn, nrm, ikb, hops))
nbreak = 0
for kinds, c2, sh, zn, nrm, ikb, hops in res:
    tag = 'BREAKS I*K' if ikb > 1e-9 else 'I*K-even'
    nbreak += ikb > 1e-9
    print(f"   path {kinds} 0->{CORN[c2]}@{sh} amp {zn}: |X|={nrm:.2f}  {tag}")
print(f"   {nbreak} of {len(res)} nonzero symmetrized second-neighbour terms break I*K")

# pick the first I*K-breaking term, add it, and look near k*
p = SETS[0]
for kinds, c2, sh, zn, nrm, ikb, hops in res:
    if ikb < 1e-9: continue
    print(f"\n   perturb with {kinds} 0->{CORN[c2]}@{sh} amp {zn}, strength delta:")
    for delta in (0.02, 0.05):
        extra_k = lambda k: Xsym(hops, k) * delta
        def H(k): return bloch(u, k, *p) + extra_k(k)
        ks = kstar_of(*p)
        evk = np.linalg.eigvalsh(H(ks))
        # 2O protection at k*: doublet still degenerate
        rand = rng.uniform(-np.pi, np.pi, (200, 3))
        spl = max(np.linalg.eigvalsh(H(k))[1] - np.linalg.eigvalsh(H(k))[0] for k in rand)
        lin = []
        for d in (np.array([1, 0, 0]), np.ones(3) / np.sqrt(3), np.array([1, 2, -1]) / np.sqrt(6)):
            for q in (1e-3, 1e-2):
                e = np.linalg.eigvalsh(H(ks + q * d)); lin.append((e[1] - e[0]) / q)
        print(f"     delta={delta}: split at k* {evk[1]-evk[0]:.1e} (2O-protected), max split at random k {spl:.3f},"
              f" (E2-E1)/|dk| near k* for 3 dirs x q=1e-3,1e-2: {np.round(lin, 4)} -> Weyl term 2*alpha")
        # lower-band minimum: shell?
        alpha = lin[0] / 2; inv_m = None
    break
