"""R2 / L5: is the CKM inversion special to Gaussians?  Kink (tanh wall) zero modes are
sech^p profiles.  Kernel K_s(a, b) = int sech^pQ(t-a) sech^ps(t-b) dt (flat Higgs),
Q cluster shared by up and down (SU(2)_L), different p and offsets for u_R, d_R.
Clustered limit; report |Vcb|/|Vus| vs G(xi_Q), and kappa."""
import numpy as np
rng = np.random.default_rng(3)
t = np.linspace(-40, 40, 16001); dt = t[1] - t[0]
def prof(p, c):
    return np.cosh(t - c) ** (-p)
def G(p):
    p = np.asarray(p, float); pp = p - p.mean()
    V = (p[1] - p[0]) * (p[2] - p[0]) * (p[2] - p[1])
    return np.linalg.norm(pp) ** 3 / abs(V)
rows = []
for trial in range(60):
    xq, xu, xd = [np.sort(rng.normal(size=3)) for _ in range(3)]
    pQ, pu, pd = rng.uniform(0.5, 3.0, size=3)
    cu, cd = rng.uniform(-1.5, 1.5, size=2)
    dQ, du, dd = 0.01, 0.01 * rng.uniform(0.5, 2), 0.01 * rng.uniform(0.5, 2)
    PQ = np.array([prof(pQ, dQ * x) for x in xq])
    Pu = np.array([prof(pu, du * x + cu) for x in xu]); Pd = np.array([prof(pd, dd * x + cd) for x in xd])
    Mu = PQ @ Pu.T * dt; Md = PQ @ Pd.T * dt
    Uu, su, _ = np.linalg.svd(Mu); Ud, sd, _ = np.linalg.svd(Md)
    V = np.abs(Uu.T @ Ud)
    rows.append((G(xq), V[0, 1] / V[1, 2], su[1] ** 2 / (su[0] * su[2]), sd[2] / sd[0]))
rows = np.array(rows)
print("first rows: G(xi_Q), |Vcb|/|Vus|, kappa_u, m_d/m_b")
print(np.round(rows[:6], 4))
print("min |Vcb|/|Vus| over 60 kink configs:", rows[:, 1].min().round(3), "; max |ratio/G - 1|:", np.abs(rows[:, 1] / rows[:, 0] - 1).max().round(3))
print("kappa_u range:", rows[:, 2].min().round(2), rows[:, 2].max().round(2))
