"""F2 part 5b: inspect the dressed-lambda solution of the translation-sector 1-jet system."""
import numpy as np, itertools
import f2_dressed_translation as F
from f2_common import *
F.rng = np.random.default_rng(1)
m2 = 1.0
nb = len(F.basis(np.zeros(4)))
names = ([f'cos p{mu}' for mu in range(4)] + [f'cos 2p{mu}' for mu in range(4)]
         + [f'cos p{a} cos p{b}' for a, b in itertools.combinations(range(4), 2)]
         + [f'prod cos {t}' for t in itertools.combinations(range(4), 3)] + ['prod cos all'])

def build(m2, npts, im):
    rows, rhs = [], []
    for _ in range(npts):
        p = shell_point(F.rng, m2, True, im=im)
        n = 2 * np.sin(p); dn_c = np.zeros(4, complex); dn_c[0] = 2 * np.cos(p[0])
        N0 = W * np.array([n[m] * n[k] for (m, k) in COMPS]); sc = 1 / np.linalg.norm(N0)
        B = F.basis(p)
        for t in tangent_basis(n, F.rng):
            const = 0.5 * (t @ dn_c)
            coefs = np.array([(gr @ t) * n[0] + val * (t @ dn_c) for (val, gr) in B])
            for a in range(NC):
                r = np.zeros(400 + nb, complex)
                for mu in range(4):
                    r[a * 40 + 10 * mu: a * 40 + 10 * mu + 10] = t[mu] * N0
                r[400:] = -1j * coefs * N0[a]
                rows.append(r * sc); rhs.append(1j * const * N0[a] * sc)
    return np.array(rows), np.array(rhs)

G, b = build(m2, 200, 0.6)
u, _, rank, sv = np.linalg.lstsq(G, b, rcond=None)
print('residual', np.linalg.norm(G @ u - b) / np.linalg.norm(b), 'rank', rank, '/', G.shape[1])
U, S, Vh = np.linalg.svd(G, full_matrices=False)
null = Vh[S < 1e-9 * S[0]].conj()
print('nullity', len(null), '; beta-components of null space: max', np.abs(null[:, 400:]).max() if len(null) else 0)
# project u to remove null-space components in beta (min-norm already); print beta
beta = u[400:]
for nm, bv in zip(names, beta):
    if abs(bv) > 1e-8:
        print(f'  beta[{nm:22s}] = {bv.real:+.8f} {bv.imag:+.1e}j')
# lambda on shell vs closed forms
p = shell_point(F.rng, m2, True)
lam = 0.5 + sum(bv * val for bv, (val, gr) in zip(beta, F.basis(p)))
print('lambda at a shell point =', lam, ' 1/(2cos p0)=', 1/(2*np.cos(p[0])))
# check whether lambda depends on direction c (built for c_dir = 0): print M structure for comp (0,0)
M = u[:400].reshape(10, 4, 10)        # [a, mu, b]
for a in (0, 4):
    for mu in range(4):
        nz = [(COMPS[bb], np.round(M[a, mu, bb], 6)) for bb in range(10) if abs(M[a, mu, bb]) > 1e-8]
        print(f'  output comp {COMPS[a]}, mu={mu}: ', nz)
