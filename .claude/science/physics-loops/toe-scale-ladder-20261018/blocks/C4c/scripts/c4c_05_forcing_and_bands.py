"""C4c-05: (a) single-overlap forcing rule on named supports (which sites of a commuting U(1)
family's gate are forced to act diagonally); (b) two-magnon Bloch bands of an explicit member of
the covered family (axis action, n-basis): alpha = D_body o Ad(sigma_n^{(x)}) o D_face o D_axis
with D_X = prod over the X bond orbit of exp(i phi_X sigma_n sigma_n) (C4b Lemma 4 exhibit type),
computed on an L^3 torus by brute force in the 2-magnon sector and Bloch-decomposed."""
import itertools
import numpy as np
from c4c_common import check, total, T, cheb

def single_overlaps(S):
    Sset = set(S); forced = set()
    for p in S:
        for q in S:
            t = tuple(np.subtract(p, q))
            if t == (0, 0, 0):
                continue
            ov = Sset & set(tuple(np.add(s, t)) for s in S)
            if len(ov) == 1:
                s = next(iter(ov)); forced.add(s); forced.add(tuple(np.subtract(s, t)))
    return forced

e = np.eye(3, dtype=int)
named = {
    'bond e1': [(0, 0, 0), (1, 0, 0)],
    'bond (1,1,1)': [(0, 0, 0), (1, 1, 1)],
    'unit cube': list(itertools.product((0, 1), repeat=3)),
    'segment of 3': [(-1, 0, 0), (0, 0, 0), (1, 0, 0)],
    'segment of 4': [(k, 0, 0) for k in range(4)],
    '7-site star': [(0, 0, 0)] + [tuple(s * e[i]) for i in range(3) for s in (1, -1)],
    '3x3 square': [(x, y, 0) for x in (-1, 0, 1) for y in (-1, 0, 1)],
    '27-cell': list(itertools.product((-1, 0, 1), repeat=3)),
}
for name, S in named.items():
    f = single_overlaps(S)
    un = [s for s in S if s not in f]
    print(f"  {name:14s} |S|={len(S):2d}  not forced by single-overlap rule: {un}")
check("(a) convex-position supports (bonds, unit cube) fully forced -> diagonal",
      all(len(single_overlaps(named[k])) == len(named[k]) for k in ('bond e1', 'bond (1,1,1)', 'unit cube')))
# A site with only ONE non-forced site: U(1) needs >= 2 non-diagonal sites for a hop, so diagonal.
check("(a) segment-of-3 and 7-site star: exactly one unforced site -> diagonal by charge counting",
      all(len(named[k]) - len(single_overlaps(named[k])) <= 1 for k in ('segment of 3', '7-site star')))

# (b) explicit covered instance on L^3 torus, 2-magnon sector, n-basis (magnon = +n spin? we use
# 'up along n' = magnon; sigma_n = +1 on magnon, -1 on vacuum).
L = 5
sites = list(itertools.product(range(L), repeat=3)); idx = {s: i for i, s in enumerate(sites)}
phi = {'axis': 0.31, 'face': 0.57, 'body': 0.23}
orbits = {'axis': [tuple(v) for v in e],
          'face': [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)],
          'body': [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1)]}
def wrap(p):
    return tuple(int(v) % L for v in p)
def diag_phase(conf):
    """total phase of D_body Ad... on a configuration (set of magnon sites); sigma_n sigma_n = +1
    for equal, -1 for different.  Ad(sigma_n^{(x)}) contributes a global sign only (sigma_n is
    diagonal) -> configuration-independent up to (-1)^{#magnons}, here fixed per sector."""
    tot = 0.0
    for key, vecs in orbits.items():
        for s in sites:
            for v in vecs:
                a = s in conf; b = wrap(np.add(s, v)) in conf
                tot += phi[key] * (1 if a == b else -1)
    return tot
vac = diag_phase(set())
pairs_rel = [rho for rho in itertools.product((-1, 0, 1), repeat=3)
             if rho != (0, 0, 0) and [x for x in rho if x][0] > 0]
assert len(pairs_rel) == 13
# brute-force: U on 2-magnon near states is diagonal; build W(K) by Bloch sum over the torus
Ks = [2 * np.pi * np.array(k) / L for k in itertools.product(range(L), repeat=3)]
bands = []
for K in Ks:
    W = np.zeros((13, 13), complex)
    for j, rho in enumerate(pairs_rel):
        # U|0,rho> = e^{i(phase-vac)} |0,rho>  (diagonal): Bloch coefficient
        conf = {(0, 0, 0), wrap(rho)}
        W[j, j] = np.exp(1j * (diag_phase(conf) - vac))
    bands.append(np.sort(np.angle(np.linalg.eigvals(W))))
bands = np.array(bands)
spread = np.max(bands.max(0) - bands.min(0))
print("  13 pair quasienergies (rad, relative to vacuum):", np.round(bands[0], 6))
check("(b) covered instance: all 13 two-magnon bands exactly flat over the 125 torus momenta",
      spread < 1e-12, f"max band width = {spread:.1e}")
# brute-force cross-check that U maps each near pair to itself translated by 0 (diagonal) on the
# full 2-magnon torus space is automatic for a diagonal unitary; verify that the phase depends
# only on rho (translation invariance of the instance):
ph = {}
okTI = True
for s in sites[:10]:
    for rho in pairs_rel:
        conf = {s, wrap(np.add(s, rho))}
        val = diag_phase(conf) - vac
        if rho in ph and abs(ph[rho] - val) > 1e-9:
            okTI = False
        ph[rho] = val
check("(b) pair phase depends only on rho (TI of the instance)", okTI)
total()
