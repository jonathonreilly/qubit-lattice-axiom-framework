"""Monomial (induced) representations of the binary octahedral group 2O on O-orbits of points
(face centres 6, corners 8, edge midpoints 12, and the 24-point generic orbit), decomposed into irreps.
For spinorial ones, F = m(E1/2) A1 + m(E5/2) A2 + m(H) E is the 'taste' representation of S3."""
import numpy as np, itertools
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
def su2(axis, ang):
    a = np.array(axis, float); a /= np.linalg.norm(a)
    return np.cos(ang / 2) * np.eye(2) - 1j * np.sin(ang / 2) * (a[0] * sx + a[1] * sy + a[2] * sz)
def rot(U):
    return np.array([[0.5 * np.trace(s @ U @ t @ U.conj().T).real for t in (sx, sy, sz)] for s in (sx, sy, sz)])
gZ, gX = su2([0, 0, 1], np.pi / 2), su2([1, 0, 0], np.pi / 2)
G = [np.eye(2, dtype=complex)]
key = lambda U: tuple(np.round(np.concatenate([U.real.ravel(), U.imag.ravel()]) + 0.0, 6))
seen = {key(G[0])}; fr = [G[0]]
while fr:
    nx = []
    for A in fr:
        for g in (gZ, gX):
            B = A @ g
            if key(B) not in seen: seen.add(key(B)); G.append(B); nx.append(B)
    fr = nx
assert len(G) == 48
Rs = [np.round(rot(U)).astype(int) for U in G]
idx = {key(U): i for i, U in enumerate(G)}
mul = lambda i, j: idx[key(G[i] @ G[j])]
inv = lambda i: idx[key(G[i].conj().T)]
# irreducible characters
from scipy.linalg import expm
def spinj(j):
    m = np.arange(j, -j - 1, -1); d = len(m); Jp = np.zeros((d, d), complex)
    for i in range(1, d): Jp[i - 1, i] = np.sqrt(j * (j + 1) - m[i] * (m[i] + 1))
    Jx = (Jp + Jp.conj().T) / 2; Jy = (Jp - Jp.conj().T) / 2j; Jz = np.diag(m).astype(complex)
    return Jx, Jy, Jz
def char_spin(j):
    Jx, Jy, Jz = spinj(j); out = []
    for U in G:
        # U = exp(-i theta n.sigma/2): recover theta, n
        c = np.clip(np.trace(U).real / 2, -1, 1); th = 2 * np.arccos(c)
        if abs(np.sin(th / 2)) < 1e-12:
            out.append(len(Jz) * (1 if c > 0 else (-1) ** int(round(2 * j)))); continue
        n = np.array([np.trace(1j * U @ s).real / (2 * np.sin(th / 2)) for s in (sx, sy, sz)])
        out.append(np.trace(expm(-1j * th * (n[0] * Jx + n[1] * Jy + n[2] * Jz))))
    return np.array(out)
perm_sign = lambda R: int(round(np.linalg.det(np.abs(R))))
A1 = np.ones(48); A2 = np.array([perm_sign(R) for R in Rs])
Bs = np.array([[1, 1], [-1, 1], [0, -2]]) @ np.diag([1 / np.sqrt(2), 1 / np.sqrt(6)])
E = np.array([np.trace(Bs.T @ np.abs(R) @ Bs) for R in Rs])
T1 = char_spin(1.0); T2 = T1 * A2; E12 = char_spin(0.5); E52 = E12 * A2; H = char_spin(1.5)
irr = {'A1': A1, 'A2': A2, 'E': E, 'T1': T1, 'T2': T2, 'E1/2': E12, 'E5/2': E52, 'H': H}
for k, v in irr.items(): assert abs(np.vdot(v, v).real / 48 - 1) < 1e-9, k
def decompose(ch): return {k: round((np.vdot(v, ch) / 48).real, 6) for k, v in irr.items() if abs(np.vdot(v, ch) / 48) > 1e-6}
# orbits
orbits = {'faces(6)': [s * np.eye(3, dtype=int)[a] for a in range(3) for s in (1, -1)],
          'corners(8)': [np.array(v) for v in itertools.product((1, -1), repeat=3)],
          'edges(12)': [np.array(v) for v in set(itertools.permutations((1, 1, 0))) | set(itertools.permutations((1, -1, 0))) | set(itertools.permutations((-1, -1, 0)))]}
orbits['edges(12)'] = [np.array(v) for v in {tuple(v) for v in orbits['edges(12)']}]
for name, pts in orbits.items():
    p0 = pts[0]
    Hs = [i for i in range(48) if np.array_equal(Rs[i] @ p0, p0)]          # stabiliser preimage in 2O
    # characters of the cyclic-ish stabiliser: find a generator
    order = lambda i: next(k for k in range(1, 49) if np.allclose(np.linalg.matrix_power(G[i], k), np.eye(2)))
    gen = max(Hs, key=order); n = order(gen)
    powers = {idx[key(np.linalg.matrix_power(G[gen], k))]: k for k in range(n)}
    assert set(powers) == set(Hs), 'stabiliser not cyclic'
    # coset representatives
    reps = []
    for p in pts:
        reps.append(next(i for i in range(48) if np.array_equal(Rs[i] @ p0, p)))
    print(f'== {name}: stabiliser preimage cyclic of order {n}')
    for q in range(n):
        chi = lambda h: np.exp(2j * np.pi * q * powers[h] / n)
        # induced character: chi_ind(g) = sum_i [g_i^-1 g g_i in H] chi(g_i^-1 g g_i)
        ch = np.zeros(48, complex)
        for g in range(48):
            for gi in reps:
                c = mul(mul(inv(gi), g), gi)
                if c in powers: ch[g] += chi(c)
        dec = decompose(ch)
        spinorial = abs(chi(idx[key(-np.eye(2))]) + 1) < 1e-9
        phases = sorted({round(np.angle(chi(h)) / np.pi, 3) for h in Hs})
        F = {('A1' if k == 'E1/2' else 'A2' if k == 'E5/2' else 'E'): v for k, v in dec.items() if k in ('E1/2', 'E5/2', 'H')}
        signed = all(abs(chi(h).imag) < 1e-9 for h in Hs)
        print(f'   q={q} {"spinorial" if spinorial else "integer  "} {"signed " if signed else "phased "} decomposition {dec}' + (f'  -> taste F = {F}' if spinorial else ''))
