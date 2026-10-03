#!/usr/bin/env python3
"""Coordinator's independent check of A38 (own code).
H8 texture: m(r) = ((-1)^rx, (-1)^ry, (-1)^rz)/sqrt3 on the 2x2x2 cell.
(a) every signed permutation maps H8 to a translate of itself;
(b) pair law J s.s + K s^a s^a + D (s_i x s_j)_a on a-bonds: H8 product state stationary (no double or single flips) iff K=J, D=0;
(c) single-flip (magnon) hopping around a face: Wilson-loop phase = +-2pi/3 (pair law, and random covariant pair laws)."""
import itertools
import numpy as np
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]], complex); Z = np.diag([1.0 + 0j, -1.0]); S = [X, Y, Z]
def m_of(r):
    return np.array([(-1) ** (r[0] % 2), (-1) ** (r[1] % 2), (-1) ** (r[2] % 2)]) / np.sqrt(3)
def kets(m):
    th = np.arccos(np.clip(m[2], -1, 1)); ph = np.arctan2(m[1], m[0])
    up = np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
    dn = np.array([-np.exp(-1j * ph) * np.sin(th / 2), np.cos(th / 2)])
    return up, dn
# (a)
ok = True
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3)); 
        for i in range(3): R[perm[i], i] = sg[i]
        found = False
        for t in itertools.product((0, 1), repeat=3):
            if all(np.allclose(R @ m_of(r), m_of((np.array(R @ np.array(r)) + np.array(t)).astype(int))) for r in itertools.product((0, 1), repeat=3)):
                found = True; break
        ok &= found
print("(a) all 48 signed permutations map H8 to a translate:", ok)
def bond_h(a, J, K, D):
    h = J * sum(np.kron(s, s) for s in S) + K * np.kron(S[a], S[a])
    b, c = [(1, 2), (2, 0), (0, 1)][a]
    h = h + D * (np.kron(S[b], S[c]) - np.kron(S[c], S[b]))
    return h
def flips(J, K, D):
    dbl = 0.0; single = np.zeros(8, complex)
    sites = list(itertools.product((0, 1), repeat=3))
    for r in sites:
        for a in range(3):
            r2 = list(r); r2[a] = (r2[a] + 1) % 2
            u1, d1 = kets(m_of(r)); u2, d2 = kets(m_of(tuple(r2)))
            h = bond_h(a, J, K, D)
            psi = np.kron(u1, u2)
            dbl = max(dbl, abs(np.kron(d1, d2).conj() @ h @ psi))
            single[sites.index(r)] += np.kron(d1, u2).conj() @ h @ psi
            single[sites.index(tuple(r2))] += np.kron(u1, d2).conj() @ h @ psi
    return dbl, np.abs(single).max()
print("(b) pair law K=J, D=0: max double-flip %.2e, max single-flip %.2e" % flips(1, 1, 0))
for (J, K, D) in ((1, 0, 0), (1, 0.5, 0), (1, 1, 0.3), (1, -2, 0)):
    print("    J=%g K=%g D=%g: max double-flip %.3f, single %.3f" % ((J, K, D) + flips(J, K, D)))
def wilson(J, K, D, r0=(0, 0, 0), plane=(0, 1)):
    a, b = plane
    e = np.eye(3, dtype=int)
    corners = [np.array(r0), np.array(r0) + e[a], np.array(r0) + e[a] + e[b], np.array(r0) + e[b]]
    W = 1.0 + 0j
    for k in range(4):
        ri, rj = corners[k], corners[(k + 1) % 4]
        d = rj - ri; ax = int(np.argmax(np.abs(d)))
        lo, hi = (ri, rj) if d[ax] > 0 else (rj, ri)
        u_lo, d_lo = kets(m_of(tuple(lo % 2))); u_hi, d_hi = kets(m_of(tuple(hi % 2)))
        h = bond_h(ax, J, K, D)
        if d[ax] > 0:   # magnon hops lo -> hi
            t = np.kron(u_lo, d_hi).conj() @ h @ np.kron(d_lo, u_hi)
        else:           # magnon hops hi -> lo
            t = np.kron(d_lo, u_hi).conj() @ h @ np.kron(u_lo, d_hi)
        W *= t
    return W
for (J, K, D) in ((1, 1, 0), (1, 0.3, 0.2), (0.7, -0.4, 0.9)):
    for r0 in ((0, 0, 0), (1, 0, 0), (0, 0, 1)):
        for plane in ((0, 1), (0, 2), (1, 2)):
            W = wilson(J, K, D, r0, plane)
            if abs(W) > 1e-9:
                print("(c) J=%.1f K=%.1f D=%.1f face at %s plane %s: |W| = %.3f, phase/pi = %+.4f" % (J, K, D, r0, plane, abs(W), np.angle(W) / np.pi))
            else:
                print("(c) J=%.1f K=%.1f D=%.1f face at %s plane %s: W = 0" % (J, K, D, r0, plane))
