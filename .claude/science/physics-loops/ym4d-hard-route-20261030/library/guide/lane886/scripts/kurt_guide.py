# GUIDE only (a run can refute or guide; it proves nothing).
# Criteria written before the run:
#  C1 identities of Step 4 hold to 1e-9 on random reversible chains with an involution:
#     (MH) p in {1, 1.5, 2, 3}, t in {1, 2, 3}; (FLIP); (KE); Theorem 4.5 (a), (b), (c).
#  C2 Example 6.2 on the 2x2 spatial torus (Z_2 gauge theory in 2+1 D, 8 links):
#     as beta_s grows at fixed beta_t, kappa -> 1, S_ev -> 0, theta -> a limit in (0,1).
import itertools, numpy as np
rng = np.random.default_rng(886)

def analyse(T, flip, label, tsteps=(1, 2, 3), verbose=True):
    """T symmetric positive-definite kernel (counting measure); flip: permutation (involution) commuting with T."""
    n = T.shape[0]
    F = np.zeros((n, n)); F[np.arange(n), flip] = 1.0
    assert np.allclose(F @ T, T @ F, atol=1e-10)
    Pe = (np.eye(n) + F) / 2; Po = (np.eye(n) - F) / 2
    w, v = np.linalg.eigh(T)
    lam0 = w[-1]; Om = np.abs(v[:, -1])
    we, ve = np.linalg.eigh(Pe @ T @ Pe); wo, vo = np.linalg.eigh(Po @ T @ Po)
    lam_odd = wo[-1]; Psi = vo[:, -1]
    ev_sorted = np.sort(we)[::-1]
    rho = ev_sorted[1] / lam0; theta = lam_odd / lam0
    mu = Om**2; g = Psi / Om
    P = (T * Om[None, :]) / (lam0 * Om[:, None])          # Markov, reversible wrt mu
    assert np.allclose(P.sum(1), 1, atol=1e-9)
    M = lambda q: float(np.sum(mu * np.abs(g)**q))
    kappa = M(4); c = M(1)
    ok = True
    for p in (1, 1.5, 2, 3):
        for t in tsteps:
            lhs = theta**(p*t) * M(2*p); rhs = M(p)**2 + rho**t * (M(2*p) - M(p)**2)
            ok &= lhs <= rhs + 1e-9
    s = np.sign(g)
    q = np.array([P[i, s != s[i]].sum() for i in range(n)])
    flip_lhs = (1 - theta) * c; flip_rhs = 2 * float(np.sum(mu * q * np.abs(g)))
    ok &= abs(flip_lhs - flip_rhs) < 1e-9
    h = g**2 - 1
    lam_bar = float(np.sum(mu * h * (h - P @ h)) / np.sum(mu * h * h)) if kappa > 1 + 1e-12 else float('nan')
    V = P @ (g**2) - theta**2 * g**2
    cov = float(np.sum(mu * g**2 * V) - np.sum(mu * V))
    if kappa > 1 + 1e-12:
        ok &= abs((kappa - 1) * (lam_bar - (1 - theta**2)) + cov) < 1e-9
    ok &= kappa >= 1 / c**2 - 1e-9 and kappa - 1 >= 2 * (1 - c) - 1e-9
    sPs = float(np.sum(mu * s * (P @ s)))
    ok &= sPs <= theta + 1e-9 and sPs >= theta * (1 - (kappa - 1)) - 1e-9
    Sev = {t: float(np.sum((ev_sorted[1:] / lam0)**t)) for t in (1, 2, 4)}
    if verbose:
        print(f"{label}: theta={theta:.6f} rho={rho:.6f} kappa={kappa:.6f} c={c:.6f} lam_bar={lam_bar:.6f} "
              f"S_ev(1,2,4)={Sev[1]:.3e},{Sev[2]:.3e},{Sev[4]:.3e} identities_ok={ok}")
    return ok, theta, rho, kappa

# C1: random chains
allok = True
for trial in range(300):
    n = 2 * int(rng.integers(3, 9))
    A = rng.random((n, n)) ** rng.integers(1, 6)
    A = A @ A.T + 1e-3                                   # symmetric, positive definite, positive entries
    flip = np.arange(n).reshape(2, -1)[::-1].reshape(-1)  # swap the two halves
    F = np.zeros((n, n)); F[np.arange(n), flip] = 1.0
    T = (A + F @ A @ F) / 2
    ok, *_ = analyse(T, flip, "rand", verbose=False)
    allok &= ok
print("C1 random chains, 300 trials, all identities and inequalities hold:", allok)

# C2: Z_2 gauge theory, 2x2 spatial torus
L = 2
sites = [(x, y) for x in range(L) for y in range(L)]
links = [(s, d) for s in sites for d in (0, 1)]
lid = {l: i for i, l in enumerate(links)}
def sh(s, d): return ((s[0] + (d == 0)) % L, (s[1] + (d == 1)) % L)
plaqs = [[lid[(s, 0)], lid[(sh(s, 0), 1)], lid[(sh(s, 1), 0)], lid[(s, 1)]] for s in sites]
def gauge_links(s):
    back0 = ((s[0] - 1) % L, s[1]); back1 = (s[0], (s[1] - 1) % L)
    return [lid[(s, 0)], lid[(s, 1)], lid[(back0, 0)], lid[(back1, 1)]]
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
flipmask = np.ones(nl, dtype=int)
for s in sites:
    if s[0] == 0: flipmask[lid[(s, 0)]] = -1              # links in direction 0 leaving the layer x = 0
flip = np.array([idx(c * flipmask) for c in conf])
def run(bs, bt):
    Vv = np.array([bs * sum(1 - np.prod(c[p]) for p in plaqs) for c in conf])
    K0 = np.exp(bt * (conf @ conf.T))                      # prod_l exp(bt s_l s'_l)
    Kt = np.zeros((N, N))
    for m in gmasks:
        perm = np.array([idx(c * m) for c in conf])
        Kt += K0[:, perm]
    Kt /= len(gmasks)
    T = np.exp(-Vv / 2)[:, None] * Kt * np.exp(-Vv / 2)[None, :]
    return analyse(T, flip, f"Z2 2x2 torus beta_s={bs} beta_t={bt}")
for bt in (0.2, 0.4):
    for bs in (0.25, 0.5, 1.0, 2.0, 4.0, 8.0):
        run(bs, bt)
