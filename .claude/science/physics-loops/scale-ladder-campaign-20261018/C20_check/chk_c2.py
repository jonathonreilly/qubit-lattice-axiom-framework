"""Independent check of the C2x/C2y anticommuting-lift argument (C20 claim C) on L = 4.
Own code: lattice matrices of the dressed lifts, momentum images of all 64 torus momenta, random Hamiltonians
symmetrized over (a) only {translations, C2x, C2y} and (b) the full dressed O_h, level degeneracies at the
eight points and controls elsewhere."""
import itertools
import numpy as np
from chk_common import load

Mdl, X, Mm, seeds = load()
nV = Mdl['nV']; L = Mdl['L']; VERTS = Mdl['VERTS']; CI = Mdl['CI']; ROTS = Mdl['ROTS']

def mat(g):
    P, s = g; U = np.zeros((nV, nV))
    U[P, np.arange(nV)] = (-1.0) ** s          # c_q -> (-1)^s(q) c_P(q)
    return U
rid = lambda d: [k for k, R in enumerate(ROTS) if np.allclose(R, np.diag(d))][0]
Ux = mat(Mdl['rots'][rid((1, -1, -1))]); Uy = mat(Mdl['rots'][rid((-1, 1, -1))])
print('Ux Uy + Uy Ux = 0 :', np.allclose(Ux @ Uy, -Uy @ Ux), '| Ux^2 = ', 'I' if np.allclose(Ux @ Ux, np.eye(nV)) else ('-I' if np.allclose(Ux @ Ux, -np.eye(nV)) else 'other'))
Ts = [mat(g) for g in Mdl['trans']]
print('translations are pure permutations (trivial signs):', all(np.all(g[1] == 0) for g in Mdl['trans']))

pos = np.array([v for v, c in VERTS]); cid = np.array([CI[c] for v, c in VERTS])
moms = [np.array(m) * 2 * np.pi / L for m in itertools.product(range(L), repeat=3)]
def pw(k):
    B = np.zeros((nV, 12), complex); B[np.arange(nV), cid] = np.exp(1j * pos @ k) / L ** 1.5; return B
PW = [pw(k) for k in moms]
def img(U, i):
    Y = U @ PW[i]
    w = [np.linalg.norm(PW[j].conj().T @ Y) for j in range(len(moms))]
    j = int(np.argmax(w)); assert abs(w[j] - np.sqrt(12)) < 1e-8; return j
fx = {i for i in range(64) if img(Ux, i) == i}; fy = {i for i in range(64) if img(Uy, i) == i}
lab = lambda i: tuple(int(x) for x in np.round(((moms[i] + np.pi) % (2 * np.pi) - np.pi) / (np.pi / 2)))
both = sorted(lab(i) for i in fx & fy)
print('C2x fixes', len(fx), 'momenta; C2y fixes', len(fy), '; both fix', len(both), ':', both)

rng = np.random.default_rng(2026)
def rand_H(rangemax=1.5):
    A = rng.normal(size=(nV, nV)) + 1j * rng.normal(size=(nV, nV))
    # keep only a finite range (min-image distance between sites)
    d = pos[:, None, :] - pos[None, :, :]; d = (d + L // 2) % L - L // 2
    A *= (np.linalg.norm(d, axis=2) <= rangemax)
    return (A + A.conj().T) / 2
def symmetrize(H, gens):
    T = sum(t @ H @ t.T for t in Ts) / len(Ts)
    grp = [np.eye(nV)]
    changed = True
    while changed:
        changed = False
        for g in list(grp):
            for h in gens:
                p = h @ g
                if not any(np.allclose(np.abs(p), np.abs(q)) and (np.allclose(p, q) or np.allclose(p, -q)) for q in grp):
                    grp.append(p); changed = True
    return sum(g @ T @ g.T for g in grp) / len(grp), len(grp)

def levels(H, i):
    return np.linalg.eigvalsh(PW[i].conj().T @ H @ PW[i])
eight = [i for i in range(64) if lab(i) in set(both)]
others = [i for i in range(64) if i not in eight]
Ofull = [mat(g) for g in Mdl['rots'] + Mdl['invs']]
for case, gens in (('C2x,C2y only', [Ux, Uy]), ('full O_h', Ofull)):
    worst_split8 = 0; min_gap_other = []; deg_other = 0
    for trial in range(4):
        H, ng = symmetrize(rand_H(), gens)
        assert np.allclose(H, H.conj().T)
        for i in eight:
            e = levels(H, i)
            worst_split8 = max(worst_split8, np.max(np.abs(e[0::2] - e[1::2])))
            # bands 0,1 touch: nu = 1 corollary
        for i in others:
            e = levels(H, i); min_gap_other.append(np.min(np.diff(e)))
            # count momenta where the lowest pair is degenerate
            deg_other += abs(e[1] - e[0]) < 1e-9
    print(f'{case} (group order {ng}): max pair splitting at the eight points = {worst_split8:.1e}; '
          f'other momenta: lowest-pair degenerate at {deg_other}/{4*len(others)}, median smallest gap {np.median(min_gap_other):.3f}')
