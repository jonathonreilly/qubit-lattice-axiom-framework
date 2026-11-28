# GUIDE only. Second version: full group Gamma = <z_0, z_1>; exact zeros of g handled; each check named.
# Criteria (unchanged, written before the first run):
#  C1 identities of Step 4 on random chains (done in kurt_guide.py: all hold).
#  C2 Example 6.2 on the 2x2 spatial torus: as beta_s grows at fixed beta_t,
#     kappa -> 1, S_ev -> 0, theta -> a limit in (0,1).
import itertools, numpy as np

def analyse(T, flips, chi, label):
    n = T.shape[0]
    Fs = []
    for f in flips:
        F = np.zeros((n, n)); F[np.arange(n), f] = 1.0
        assert np.allclose(F @ T, T @ F, atol=1e-10); Fs.append(F)
    I = np.eye(n)
    Ptriv = I.copy(); Pchi = I.copy()
    for F, e in zip(Fs, chi):
        Ptriv = Ptriv @ (I + F) / 2
        Pchi = Pchi @ (I + (1 - 2 * e) * F) / 2
    w, v = np.linalg.eigh(T); lam0 = w[-1]; Om = np.abs(v[:, -1])
    we = np.sort(np.linalg.eigvalsh(Ptriv @ T @ Ptriv))[::-1]
    wo, vo = np.linalg.eigh(Pchi @ T @ Pchi)
    theta = wo[-1] / lam0; Psi = vo[:, -1]; rho = we[1] / lam0
    gapdeg = (wo[-1] - wo[-2]) / lam0
    mu = Om**2; g = Psi / Om; g[np.abs(g) < 1e-10] = 0.0
    P = (T * Om[None, :]) / (lam0 * Om[:, None])
    M = lambda q: float(np.sum(mu * np.abs(g)**q))
    kappa = M(4); c = M(1); bad = []
    for p in (1, 1.5, 2, 3):
        for t in (1, 2, 3):
            if theta**(p*t) * M(2*p) > M(p)**2 + rho**t * (M(2*p) - M(p)**2) + 1e-9: bad.append(f"MH p={p} t={t}")
    s = np.sign(g)
    rhs = float(np.sum(mu[:, None] * P * np.abs(g)[None, :] * (1 - np.outer(s, s))))
    if abs((1 - theta) * c - rhs) > 1e-9: bad.append("FLIP(general form)")
    h = g**2 - 1; V = P @ (g**2) - theta**2 * g**2
    cov = float(np.sum(mu * g**2 * V) - np.sum(mu * V)); lam_bar = float('nan')
    if kappa > 1 + 1e-9:
        lam_bar = float(np.sum(mu * h * (h - P @ h)) / np.sum(mu * h * h))
        if abs((kappa - 1) * (lam_bar - (1 - theta**2)) + cov) > 1e-9: bad.append("KE")
    if kappa < 1 / c**2 - 1e-9 or kappa - 1 < 2 * (1 - c) - 1e-9: bad.append("4.5ab")
    sPs = float(np.sum(mu * s * (P @ s)))
    if sPs > theta + 1e-9 or sPs < theta * (1 - (kappa - 1)) - 1e-9: bad.append("4.5c")
    Sev = [float(np.sum((we[1:] / lam0)**t)) for t in (1, 2, 4)]
    print(f"{label}: theta={theta:.5f} rho={rho:.5f} kappa={kappa:.6f} c={c:.5f} lam_bar={lam_bar:.4f} "
          f"S_ev(1,2,4)={Sev[0]:.2e},{Sev[1]:.2e},{Sev[2]:.2e} mu(g=0)={float(np.sum(mu[g==0])):.3f} "
          f"sector-top gap={gapdeg:.2e} failed={bad}")

L = 2
sites = [(x, y) for x in range(L) for y in range(L)]
links = [(s, d) for s in sites for d in (0, 1)]
lid = {l: i for i, l in enumerate(links)}
def sh(s, d): return ((s[0] + (d == 0)) % L, (s[1] + (d == 1)) % L)
plaqs = [[lid[(s, 0)], lid[(sh(s, 0), 1)], lid[(sh(s, 1), 0)], lid[(s, 1)]] for s in sites]
def gauge_links(s):
    return [lid[(s, 0)], lid[(s, 1)], lid[(((s[0] - 1) % L, s[1]), 0)], lid[((s[0], (s[1] - 1) % L), 1)]]
nl = len(links); N = 2 ** nl
conf = np.array(list(itertools.product([1, -1], repeat=nl)))
def idx(c): return int(sum((1 if v == -1 else 0) << (nl - 1 - i) for i, v in enumerate(c)))
gmasks = []
for bits in itertools.product([0, 1], repeat=len(sites)):
    m = np.ones(nl, dtype=int)
    for b, s in zip(bits, sites):
        if b:
            for l in gauge_links(s): m[l] *= -1
    gmasks.append(m)
fm0 = np.ones(nl, dtype=int); fm1 = np.ones(nl, dtype=int)
for s in sites:
    if s[0] == 0: fm0[lid[(s, 0)]] = -1
    if s[1] == 0: fm1[lid[(s, 1)]] = -1
flips = [np.array([idx(c * fm0) for c in conf]), np.array([idx(c * fm1) for c in conf])]
K0cache = {}
def run(bs, bt):
    Vv = np.array([bs * sum(1 - np.prod(c[p]) for p in plaqs) for c in conf])
    K0 = np.exp(bt * (conf @ conf.T)); Kt = np.zeros((N, N))
    for m in gmasks:
        Kt += K0[:, np.array([idx(c * m) for c in conf])]
    Kt /= len(gmasks)
    T = np.exp(-Vv / 2)[:, None] * Kt * np.exp(-Vv / 2)[None, :]
    analyse(T, flips, (1, 0), f"bs={bs} bt={bt}")
for bt in (0.2, 0.4):
    for bs in (0.25, 0.5, 1.0, 2.0, 4.0, 8.0):
        run(bs, bt)
