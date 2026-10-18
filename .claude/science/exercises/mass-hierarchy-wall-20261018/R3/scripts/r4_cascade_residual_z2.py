#!/usr/bin/env python3
"""R3 test 4: the historic EWSB cascade's residual Z2 (swap of axes 2,3 after the VEV picks axis 1).

Setting: 8 corner states n in {0,1}^3. A charge-e1 spurion (the VEV direction) breaks translation by e1
but keeps translations by e2, e3 (characters (-1)^{n_y}, (-1)^{n_z}) and the C2 that swaps y <-> z.
The C2 is allowed an arbitrary corner-dependent sign dressing (any PSG-type gauge dressing).
Claim tested: every operator commuting with this residual group (any order in the spurion, any loop
order) has equal spectra on the (010, 110) and (001, 101) blocks, so the two 'colour-direction'
generations stay degenerate; a JW-ordering split would have to break the residual C2.
Also checked: chirality-odd blocks (Hom from even-hw to odd-hw corners) have equal singular values
on the two swapped blocks.
"""
import itertools as it
import numpy as np

rng = np.random.default_rng(11)
N = [np.array(v) for v in it.product((0, 1), repeat=3)]
idx = {tuple(v): i for i, v in enumerate(N)}

def Ty():
    return np.diag([(-1.0) ** v[1] for v in N])

def Tz():
    return np.diag([(-1.0) ** v[2] for v in N])

def C2yz(signs):
    P = np.zeros((8, 8))
    for v in N:
        w = (v[0], v[2], v[1])
        P[idx[w], idx[tuple(v)]] = signs[idx[tuple(v)]]
    return P

def closure(gens):
    G = [np.eye(8)]
    frontier = [np.eye(8)]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                x = h @ g
                if not any(np.allclose(x, y) for y in G):
                    G.append(x); new.append(x)
        frontier = new
    return G

for trial in range(4):
    signs = np.ones(8) if trial == 0 else rng.choice([-1.0, 1.0], size=8)
    G = closure([Ty(), Tz(), C2yz(signs)])
    X = rng.standard_normal((8, 8)) + 1j * rng.standard_normal((8, 8)); X = X + X.conj().T
    Y = sum(g @ X @ g.T for g in G) / len(G)
    blocks = {"A{000,100}": [(0, 0, 0), (1, 0, 0)], "B{010,110}": [(0, 1, 0), (1, 1, 0)],
              "C{001,101}": [(0, 0, 1), (1, 0, 1)], "D{011,111}": [(0, 1, 1), (1, 1, 1)]}
    # check block structure (charge e1 only mixes n with n+e1)
    off = max(abs(Y[idx[a], idx[b]]) for k1, B1 in blocks.items() for k2, B2 in blocks.items() if k1 != k2 for a in B1 for b in B2)
    ev = {k: np.round(np.linalg.eigvalsh(Y[np.ix_([idx[a] for a in B], [idx[a] for a in B])]), 6) for k, B in blocks.items()}
    # chirality-odd block: rows odd-hw corners, cols even-hw corners
    oddc = [v for v in N if v.sum() % 2]; evc = [v for v in N if v.sum() % 2 == 0]
    M = Y[np.ix_([idx[tuple(v)] for v in oddc], [idx[tuple(v)] for v in evc])]
    # odd hw: 100 (block A), 010 (B), 001 (C), 111 (D); even: 000 (A), 110 (B), 101 (C), 011 (D)
    sv = {f"{tuple(o)}<-{tuple(e)}": round(abs(M[i, j]), 6) for i, o in enumerate(oddc) for j, e in enumerate(evc) if abs(M[i, j]) > 1e-12}
    print(f"trial {trial}: |G|={len(G)}, signs={signs.astype(int).tolist()}, max inter-block |Y| = {off:.1e}")
    print(f"   block spectra: {ev}")
    print(f"   B == C: {np.allclose(ev['B{010,110}'], ev['C{001,101}'])};   nonzero chirality-odd entries |M|: {sv}")
