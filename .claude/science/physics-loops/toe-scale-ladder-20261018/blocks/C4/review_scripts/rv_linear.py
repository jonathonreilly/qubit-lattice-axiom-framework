"""F2 linear layer: covariant (unsigned) image space, own Gaussian elimination on int bitsets."""
import itertools
import numpy as np
from rv_common import O, Qmat, LAB

BITS = {'X': (1, 0), 'Y': (1, 1), 'Z': (0, 1)}
FROMBITS = {v: k for k, v in BITS.items()}

def cell(rad):
    return [r for r in itertools.product(range(-rad, rad + 1), repeat=3)]

def qperm(R, action):
    Qm = Qmat(R, action)
    return {a: LAB[int(np.nonzero(Qm[:, LAB.index(a)])[0][0])] for a in LAB}

def label_bitmap(q):
    """2x2 F2 matrix taking bits(c) -> bits(q(c)) ; check linearity."""
    cx = BITS[q['X']]; cz = BITS[q['Z']]
    # bits(c)=(u,w) = u*X + w*Z  ->  u*bits(qX)+w*bits(qZ)
    for c in LAB:
        u, w = BITS[c]
        img = ((u * cx[0] + w * cz[0]) % 2, (u * cx[1] + w * cz[1]) % 2)
        assert img == BITS[q[c]]
    return cx, cz

def covariant_space(rad, action, group=None):
    sites = cell(rad)
    idx = {r: i for i, r in enumerate(sites)}
    N = len(sites)
    # variable index: img in {0:X,1:Z}, site i, bit k -> 4*i + 2*img + k
    def var(img, i, k):
        return 4 * i + 2 * img + k
    nv = 4 * N
    def vec_of(label, i, k):
        """bitset (int) of variables expressing coordinate (site i, bit k) of v_label."""
        if label == 'X':
            return 1 << var(0, i, k)
        if label == 'Z':
            return 1 << var(1, i, k)
        return (1 << var(0, i, k)) ^ (1 << var(1, i, k))
    rows = []
    G = O if group is None else group
    for R in G:
        q = qperm(R, action)
        cx, cz = label_bitmap(q)
        for a in ('X', 'Z'):
            b = q[a]
            # (R.v_a) at site R r : bits = u*cx + w*cz where (u,w) bits of v_a at r
            img = {}
            for r in sites:
                Rr = tuple(int(x) for x in R @ np.array(r))
                i = idx[r]; j = idx[Rr]
                u = vec_of(a, i, 0); w = vec_of(a, i, 1)
                for k in (0, 1):
                    e = 0
                    if cx[k]: e ^= u
                    if cz[k]: e ^= w
                    img[(j, k)] = e
            for j in range(N):
                for k in (0, 1):
                    rows.append(vec_of(b, j, k) ^ img[(j, k)])
    # Gaussian elimination -> nullspace
    piv = {}
    for r in rows:
        while r:
            h = r.bit_length() - 1
            if h in piv:
                r ^= piv[h]
            else:
                piv[h] = r
                break
    # reduce fully
    keys = sorted(piv)
    for h in keys:
        for h2 in keys:
            if h2 != h and (piv[h2] >> h) & 1:
                piv[h2] ^= piv[h]
    free = [v for v in range(nv) if v not in piv]
    basis = []
    for f in free:
        vec = 1 << f
        for h, r in piv.items():
            if (r >> f) & 1:
                vec |= 1 << h
        basis.append(vec)
    # verify
    for b in basis:
        for r in rows:
            assert bin(b & r).count('1') % 2 == 0
    return sites, basis

def decode(vec, sites):
    """-> (dictX, dictZ) unsigned Pauli strings."""
    out = ({}, {})
    for i, r in enumerate(sites):
        for img in (0, 1):
            u = (vec >> (4 * i + 2 * img)) & 1
            w = (vec >> (4 * i + 2 * img + 1)) & 1
            if u or w:
                out[img][r] = FROMBITS[(u, w)]
    return out

if __name__ == '__main__':
    for rad in (1, 2):
        for a in ['trivial', 'sign', 'signf', 'axis', 'full']:
            sites, basis = covariant_space(rad, a)
            print(rad, a, 'dim', len(basis), flush=True)
