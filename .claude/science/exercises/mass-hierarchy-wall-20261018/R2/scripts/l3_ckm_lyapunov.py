"""R2 / L3.
(i)  Clustered Gaussian class: |Vcb|/|Vus| -> G(xi_Q) = |xi_perp|^2 / (sqrt3 |xi^2_perpperp|) >= sqrt2,
     whatever the u and d cluster shapes, sizes, offsets and widths.
(ii) Exponential (sharp-wall / lattice Green function) tails: rank facts.
(iii) Anderson / random-product variant: Lyapunov gap ratios and finite-depth spread.
(iv) Observed sigma-free invariants R = ln(m1/m3)/ln(m2/m3), kappa = m2^2/(m1 m3).
"""
import numpy as np
rng = np.random.default_rng(11)

def G(p):
    p = np.asarray(p, float); pp = p - p.mean()
    V = (p[1] - p[0]) * (p[2] - p[0]) * (p[2] - p[1])
    return np.linalg.norm(pp) ** 3 / abs(V)

def gk(x, y, w=1.0):
    return np.exp(-0.5 * (x - y) ** 2 / w ** 2)

print("(i) clustered limit (delta_Q = 1e-3): ratio |Vcb|/|Vus| vs G(xi_Q)")
worst = 0
for t in range(300):
    xq, xu, xd = [np.sort(rng.normal(size=3)) for _ in range(3)]
    dQ = 1e-3; du, dd = 10 ** rng.uniform(-3, -2, size=2)
    cu, cd = rng.uniform(-1.5, 1.5, size=2); wu, wd = rng.uniform(0.5, 2.0, size=2)
    Mu = gk((dQ * xq)[:, None], (du * xu + cu)[None, :], wu)
    Md = gk((dQ * xq)[:, None], (dd * xd + cd)[None, :], wd)
    Uu = np.linalg.svd(Mu)[0]; Ud = np.linalg.svd(Md)[0]
    V = np.abs(Uu.T @ Ud)
    r = V[0, 1] / V[1, 2]
    worst = max(worst, abs(r / G(xq) - 1))
    if t < 4:
        print(f"    G = {G(xq):.4f}   |Vcb|/|Vus| = {r:.4f}   |Vub|/(|Vus||Vcb|) = {V[0,2]/(V[0,1]*V[1,2]):.4f}")
print(f"    max relative deviation from G over 300 random configs: {worst:.2e};  min_G = sqrt2 = {np.sqrt(2):.4f}")

print("\n(ii) exponential tails")
x = np.array([0.0, 0.1, 0.25]) + 1.0; y = np.array([0.0, 0.07, 0.18])
M1 = np.exp(-np.abs(x[:, None] - y[None, :]))
k = 1.0
d = np.abs(x[:, None] - y[None, :]); M2 = (1 + k * d) * np.exp(-k * d)    # overlap of two equal sharp-wall zero modes
kL, kR = 1.0, 1.7
M3 = (kL * np.exp(-kR * d) - kR * np.exp(-kL * d))                        # unequal decay constants
for name, M in [("single exponential, separated", M1), ("two equal zero modes, separated", M2), ("two unequal zero modes, separated", M3)]:
    s = np.linalg.svd(M, compute_uv=False); print(f"    {name:34s} singular values {s}")
for dl in [1e-2, 1e-3]:
    xi = dl * np.array([0.0, 2.0, 4.0]); eta = dl * np.array([1.0, 3.0, 5.0])   # interlaced
    s = np.linalg.svd(np.exp(-np.abs(xi[:, None] - eta[None, :])), compute_uv=False)
    print(f"    interlaced, delta={dl}: {s}")

print("\n(iii) random products of 3x3 steps (Anderson / theory-space chain)")
def lyap(step, n=6000):
    Q = np.eye(3, dtype=complex); acc = np.zeros(3)
    for _ in range(n):
        Q, R = np.linalg.qr(step() @ Q)
        acc += np.log(np.abs(np.diag(R)))
    return acc / n
gin = lambda: (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / np.sqrt(2)
rgin = lambda: rng.normal(size=(3, 3)) + 0j
for name, st in [("complex Ginibre", gin), ("real Ginibre", rgin),
                 ("weak complex 1+0.1X", lambda: np.eye(3) + 0.1 * gin()),
                 ("isotropic non-Gaussian (Haar*diag*Haar)", None)]:
    if st is None:
        def st():
            A = gin(); U = np.linalg.qr(A)[0]; B = gin(); W = np.linalg.qr(B)[0]
            return U @ np.diag(np.exp(rng.uniform(-1, 1, size=3))) @ W
    g = lyap(st)
    g = np.sort(g)[::-1]
    print(f"    {name:40s} gaps (g1-g2, g2-g3) = ({g[0]-g[1]:.4f}, {g[1]-g[2]:.4f})  R = {(g[0]-g[2])/(g[0]-g[1]):.3f}")
print("    digamma prediction complex Ginibre: gaps (1/4, 1/2), R = 3; weak-step (Brownian) limit: equal gaps, R = 2")

# finite depth: complex Ginibre chain with depth L chosen so the mean ln(m3/m1) ~ 8.2 (leptons)
for Lsteps in [11, 16]:
    Rs, ks = [], []
    for _ in range(3000):
        P = np.eye(3, dtype=complex)
        for _ in range(Lsteps):
            P = gin() @ P
        s = np.linalg.svd(P, compute_uv=False)
        Rs.append(np.log(s[2] / s[0]) / np.log(s[1] / s[0])); ks.append(s[1] ** 2 / (s[0] * s[2]))
    Rs, ks = np.array(Rs), np.array(ks)
    print(f"    L = {Lsteps}: R percentiles 5/50/95 = {np.percentile(Rs,[5,50,95]).round(2)};  ln kappa 5/50/95 = {np.percentile(np.log(ks),[5,50,95]).round(2)}")

print("\n(iv) observed invariants (recalled running masses, GeV; not fetched)")
sets = {
    "M_Z": dict(up=(1.27e-3, 0.619, 171.7), down=(2.90e-3, 0.055, 2.89), lep=(0.4866e-3, 0.1027, 1.746)),
    "2e16": dict(up=(0.48e-3, 0.235, 74.0), down=(1.14e-3, 0.0216, 0.99), lep=(0.4696e-3, 0.09914, 1.685)),
}
for sc, d in sets.items():
    for s, (m1, m2, m3) in d.items():
        R = np.log(m1 / m3) / np.log(m2 / m3); kap = m2 ** 2 / (m1 * m3)
        print(f"    {sc:5s} {s:5s} R = {R:.3f}  kappa = {kap:.3f}")
print("    CKM |Vcb|/|Vus| = 0.041/0.225 = %.3f ; |Vub|/(|Vus||Vcb|) = 0.0037/(0.225*0.041) = %.3f" % (0.041 / 0.225, 0.0037 / (0.225 * 0.041)))
