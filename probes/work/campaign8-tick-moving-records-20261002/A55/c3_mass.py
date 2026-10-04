"""A55 c3: covariant local functions of corner records as an on-site charge potential mu_v n_v; staggered part,
covariance check under the role-pattern space group, and pi-flux KS bands with mu (half-filling gap).
Backgrounds (coarse x, records f in {+-1}^3): uniform, alternating eps*f0, hedgehog f_i = (-1)^x_i,
cyclic f_i = (-1)^x_{i+1}, anticyclic f_i = (-1)^x_{i-1}, random."""
import signal, sys, itertools
signal.alarm(100)
import numpy as np
sys.path.insert(0, '/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A52')
from a52lib import ROT

L = 8
X = np.array(list(itertools.product(range(L), repeat=3)))
N = len(X)
idx = lambda x: ((x[..., 0] % L) * L + (x[..., 1] % L)) * L + (x[..., 2] % L)
EPS = (-1) ** X.sum(1)
NB = [np.array(d) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
NB2 = [np.array(d) for d in itertools.product([-1, 0, 1], repeat=3) if sum(abs(c) for c in d) == 2]

def background(kind, seed=0):
    f0 = np.array([1, 1, 1])
    if kind == 'uniform':
        return np.tile(f0, (N, 1))
    if kind == 'alternating':
        return EPS[:, None] * f0
    if kind == 'hedgehog':
        return (-1) ** X
    if kind == 'cyclic':
        return (-1) ** X[:, [1, 2, 0]]
    if kind == 'anticyclic':
        return (-1) ** X[:, [2, 0, 1]]
    if kind == 'random':
        return np.random.default_rng(seed).choice([-1, 1], size=(N, 3))

def funcs(F):
    """covariant local scalars at every corner (range 1 and sqrt2)."""
    out = {}
    h = {k: np.zeros(N) for k in ['f.f', '(f.d)(f\'.d)', 'd.(f x f\')', "f'.d", 'd2.(f x f\')', '(f.d)[d.(f x f\')]', '(f\'.d)[d.(f x f\')]']}
    for d in NB:
        Fn = F[idx(X + d)]
        h['f.f'] += (F * Fn).sum(1)
        h['(f.d)(f\'.d)'] += (F @ d) * (Fn @ d)
        h['d.(f x f\')'] += np.cross(F, Fn) @ d
        h["f'.d"] += Fn @ d
        h['(f.d)[d.(f x f\')]'] += (F @ d) * (np.cross(F, Fn) @ d)
        h['(f\'.d)[d.(f x f\')]'] += (Fn @ d) * (np.cross(F, Fn) @ d)
    for d in NB2:
        Fn = F[idx(X + d)]
        h['d2.(f x f\')'] += np.cross(F, Fn) @ d
    return h

def turn_bg(F, R, a):
    """image background under x -> R x + a (records turned by R)."""
    Xg = (X @ R.T + a) % L
    Fg = np.zeros_like(F)
    Fg[idx(Xg)] = F @ R.T
    return Fg, idx(Xg)

# covariance check: h[g.r](g v) == h[r](v); turns about the origin corner and about the cube centre (1/2,1/2,1/2),
# plus single coarse translations
F = background('random', 7)
h = funcs(F)
bad = 0; tot = 0
elems = [(R, np.zeros(3, int)) for R in ROT]
c = np.array([.5, .5, .5])
elems += [(R, np.round(c - R @ c).astype(int)) for R in ROT]
elems += [(np.eye(3, dtype=int), np.array(a)) for a in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]]
for R, a in elems:
    Fg, im = turn_bg(F, R, a)
    hg = funcs(Fg)
    for k in h:
        tot += 1
        if np.abs(hg[k][im] - h[k]).max() > 1e-12:
            bad += 1
print("covariance of the 5 record functions on a random background, %d space-group elements: %d/%d failures" % (len(elems), bad, tot))

# staggered components
print("staggered part m = <eps h>, uniform part <h>, number of distinct values, per background:")
for kind in ['uniform', 'alternating', 'hedgehog', 'cyclic', 'anticyclic', 'random']:
    F = background(kind, 3)
    h = funcs(F)
    row = []
    for k, v in h.items():
        row.append("%s: m=%+.3f mean=%+.3f vals=%s" % (k, (EPS * v).mean(), v.mean(), sorted(set(np.round(v, 6).tolist()))[:4]))
    print("  %-11s | " % kind + " | ".join(row[4:]))

# pi-flux KS bands with mu_v = lam * h_v
def ks_hop(L):
    H = np.zeros((N, N))
    for a_, x in enumerate(X):
        for axis, u in [(0, 1), (1, (-1) ** x[0]), (2, (-1) ** (x[0] + x[1]))]:
            e = np.zeros(3, int); e[axis] = 1
            b = idx(x + e)
            H[a_, b] += -u; H[b, a_] += -u
    return H
H0 = ks_hop(L)
def gap_half(mu):
    ev = np.linalg.eigvalsh(H0 + np.diag(mu))
    return ev[N // 2] - ev[N // 2 - 1], ev
print("pi-flux 8^3, on-site potential lam*h, half-filling gap (pure staggered prediction 2|lam m|):")
for kind in ['uniform', 'alternating', 'hedgehog', 'cyclic', 'anticyclic', 'random']:
    F = background(kind, 3)
    h = funcs(F)
    for k in ["(f.d)(f'.d)", "d.(f x f')", "(f.d)[d.(f x f')]", "(f'.d)[d.(f x f')]"]:
        for lam in [0.25]:
            mu = lam * h[k]
            gp, ev = gap_half(mu)
            m = (EPS * mu).mean(); mb = mu.mean()
            pred = None
            if len(set(np.round(mu, 9))) <= 2:
                ks = 2 * np.pi * np.arange(L) / L
                pr = []
                for kk in itertools.product(ks, repeat=3):
                    e = np.sqrt(4 * np.sum(np.cos(kk) ** 2) + m * m)
                    pr += [mb + e, mb - e]
                pr = np.sort(pr)
                pred = np.abs(np.sort(np.concatenate([ev, ev])) - pr).max()
            print("  %-11s %-12s lam=%.2f: staggered m=%+.3f, gap=%.4f, 2|m|=%.4f%s" % (
                kind, k, lam, m, gp, 2 * abs(m), "" if pred is None else ", spectrum vs mb +- sqrt(4 sum cos^2 + m^2): %.1e" % pred))
print("done")
