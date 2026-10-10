"""R2 step 2: complete list (by dimension count) of cubic-invariant, gauge-invariant
quadratic A-block symbols Q(k) of homogeneous degree n, for each version.

W(n): all symbols with Q(k)V(k)=0 for every k (integrated gauge invariance:
      includes Chern-Simons-like / h:R-like terms that are invariant only up to
      a total derivative).
S(n): the 'strong' subset: Hermitian forms in local gauge-invariant linear
      functionals m(k) (m(k).V(k)=0) -- what a compact lattice model built from
      local gauge-invariant operators produces.
I(d): dimension of local invariant linear functionals of degree d (no symmetry).
Also: the lowest degree at which ANY invariant symbol is nonzero (protection).
"""
import numpy as np
from r2_common import *

rng = np.random.default_rng(7)
NS = 45
KS = rng.normal(size=(NS, 3))


def reynolds(Qfun):
    Ds = [Drep(g) for g in GROUP]
    def Qr(k):
        return sum(D.T @ Qfun(g @ k) @ D for g, D in zip(GROUP, Ds)) / len(GROUP)
    return Qr


def weak_count(Vf, n):
    basis, ms = Q_param_basis(n)
    rows = []
    Dg = [(g, Drep(g)) for g in (C4Z, C3D)]
    cols = []
    for (mi, S) in basis:
        col = []
        for k in KS:
            mv = np.array([np.prod(k ** np.array(m)) for m in ms])
            Q = mv[mi] * S
            col.append((Q @ Vf(k)).ravel())
            for g, D in Dg:
                kr = g @ k
                mvr = np.prod(kr ** np.array(ms[mi]))
                col.append((mvr * S - D @ Q @ D.T).ravel())
        c = np.concatenate(col)
        cols.append(np.concatenate([c.real, c.imag]))
    A = np.array(cols).T
    N = nullspace(A)
    return N.shape[1], N, basis, ms


def functionals(Vf, d):
    """real row-vector polynomials m(k) of degree d with m(k).V(k)=0."""
    ms = monos(d)
    nparam = 6 * len(ms)
    cols = []
    for p in range(nparam):
        a, mi = divmod(p, len(ms))
        col = []
        for k in KS:
            mv = np.prod(k ** np.array(ms[mi]))
            row = np.zeros(6); row[a] = mv
            col.append(row @ Vf(k))
        cols.append(np.concatenate(col))
    A = np.array(cols).T
    N = nullspace(A)
    funcs = []
    for j in range(N.shape[1]):
        c = N[:, j]
        def m(k, c=c):
            mv = np.array([np.prod(k ** np.array(mm)) for mm in ms])
            return np.array([np.dot(c[a * len(ms):(a + 1) * len(ms)], mv) for a in range(6)])
        funcs.append(m)
    return funcs


def strong_count(Vf, n, maxd):
    gens = []
    F = {d: functionals(Vf, d) for d in range(0, maxd + 1)}
    for da in range(0, n + 1):
        db = n - da
        if db < da or da > maxd or db > maxd:
            continue
        for ia, ma in enumerate(F[da]):
            for ib, mb in enumerate(F[db]):
                if da == db and ib < ia:
                    continue
                if (da + db) % 2 == 0:
                    sgn = (-1) ** ((db - da) // 2)
                    gens.append(lambda k, ma=ma, mb=mb, s=sgn: s * (np.outer(ma(k), mb(k)) + np.outer(mb(k), ma(k))))
                else:
                    gens.append(lambda k, ma=ma, mb=mb: 1j * (np.outer(ma(k), mb(k)) - np.outer(mb(k), ma(k))))
    if not gens:
        return 0
    Ds = [Drep(g) for g in GROUP]
    evals = []
    for Gf in gens:
        e = []
        for k in KS[:20]:
            Q = sum(D.T @ Gf(g @ k) @ D for g, D in zip(GROUP, Ds)) / 24.0
            e.append(Q.ravel())
        e = np.concatenate(e)
        evals.append(np.concatenate([e.real, e.imag]))
    A = np.array(evals)
    s = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(s > 1e-8 * s[0])) if s[0] > 1e-12 else 0


if __name__ == '__main__':
    maxdeg = {'S': 4, 'S-tl': 4, 'V': 4, 'V-tl': 6}
    print('Invariant local linear functionals I(d) (count, no symmetry imposed)')
    for name, Vf in VERSIONS.items():
        print(' ', name, [len(functionals(Vf, d)) for d in range(0, 4)])
    print()
    print('Cubic(O)-invariant gauge-invariant A-block symbols of degree n')
    print('version  n  W(all, integrated inv.)  S(strong: forms in local invariants)  weak-only')
    for name, Vf in VERSIONS.items():
        for n in range(0, maxdeg[name] + 1):
            w, *_ = weak_count(Vf, n)
            s = strong_count(Vf, n, maxd=3)
            print(f'{name:6s} {n:2d} {w:6d} {s:6d} {w - s:6d}')
        print()
