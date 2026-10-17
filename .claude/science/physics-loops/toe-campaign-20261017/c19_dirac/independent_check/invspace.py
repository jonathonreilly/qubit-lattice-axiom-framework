"""Exact invariant-operator spaces by signed-orbit counting (no floating point averaging)."""
import itertools
import numpy as np
from core import *

def shifts(kind):
    if kind == 'r1': S = [(0,0,0)] + [tuple(int(x) for x in d) for d in DV]
    elif kind == 'l1<=2': S = [s for s in itertools.product(range(-2, 3), repeat=3) if sum(map(abs, s)) <= 2]
    elif kind == 'cube': S = list(itertools.product(range(-1, 2), repeat=3))
    elif kind == 'linf<=2': S = list(itertools.product(range(-2, 3), repeat=3))
    elif kind == 'onsite': S = [(0,0,0)]
    return S

def group_elems(with_inv=True, which='O'):
    """list of (R, eta, s, w1) for the unitary point-group elements."""
    G = []
    for R, (e, s), w in zip(ROTS, PSG, W1):
        if which == 'T' and w: continue
        G.append((R, e, s, w))
    if with_inv:
        eI, sI = PSGI
        H = []
        for R, e, s, w in G:
            # inversion composed with R: (I R).  sigma composes: c -> sigma_R c_R ; then I
            # build via direct PSG solve for I R
            p = psg(INV @ R)
            H.append((INV @ R, p[0], p[1], w))
        G = G + H
    return G

def invariant_basis(S, stag=False, imag=False, chiA2=False, with_inv=True, chiI=1, which='O'):
    """Real coefficient vectors over indices (sh,c2,c1), sh in S.  Operator blocks
    m[sh] = (1j if imag else 1) * A[sh]. Hermiticity: m_{-sh}[c1,c2] = (-1)^{stag |sh|} conj(m_sh[c2,c1]).
    Invariance: under each group element with character chi(g) = (-1)^{w1 chiA2} * (chiI if inversion)."""
    Sset = set(S); idx = {}
    for sh in S:
        for c2 in range(12):
            for c1 in range(12): idx[(sh, c2, c1)] = len(idx)
    G = group_elems(with_inv, which)
    ops = []
    for R, e, s, w in G:
        isinv = round(np.linalg.det(R)) == -1
        chi = ((-1) ** (w * chiA2)) * (chiI if isinv else 1)
        ops.append(('g', R, e, s, chi))
    ops.append(('tau',))
    def apply(op, key):
        sh, c2, c1 = key
        if op[0] == 'tau':
            sgn = ((-1) ** (sum(map(abs, sh)) % 2) if stag else 1) * (-1 if imag else 1)
            return (tuple(-x for x in sh), c1, c2), sgn
        _, R, e, s, chi = op
        Rsh = tuple(int(x) for x in R @ np.array(sh))
        return (Rsh, rc(R, c2), rc(R, c1)), chi * e[c2] * e[c1] * (-1) ** int(s @ np.array(sh))
    seen = {}; basis = []
    for key in idx:
        if key in seen: continue
        orb = {key: 1}; stack = [key]; bad = False
        while stack:
            k = stack.pop()
            for op in ops:
                k2, sg = apply(op, k)
                assert k2 in Sset or k2[0] in Sset
                v = orb[k] * sg
                if k2 in orb:
                    if orb[k2] != v: bad = True
                else:
                    orb[k2] = v; stack.append(k2)
        for k in orb: seen[k] = True
        if not bad:
            vec = np.zeros(len(idx))
            for k, v in orb.items(): vec[idx[k]] = v
            basis.append(vec)
    return idx, basis

def to_blocks(idx, vec, imag=False):
    m = {}
    for (sh, c2, c1), i in idx.items():
        if vec[i] != 0:
            m.setdefault(sh, np.zeros((12, 12), complex))[c2, c1] += (1j if imag else 1) * vec[i]
    return m

if __name__ == '__main__':
    print("signed-orbit counts of invariant one-fermion terms (translation-invariant P = 0 unless stag)")
    for S in ('onsite', 'r1', 'l1<=2', 'cube'):
        for imag in (False, True):
            for inv in (False, True):
                idx, b = invariant_basis(shifts(S), imag=imag, with_inv=inv)
                print(f"  P=0  shifts {S:8s} {'imag' if imag else 'real'}  O{'xI' if inv else '  '} : dim {len(b)}")
    idx, b = invariant_basis(shifts('r1'), imag=True, with_inv=True, chiI=-1)
    print(f"  P=0  r1 imag, O-invariant but inversion-ODD: dim {len(b)}")
    print("staggered (P = Q):")
    for S in ('onsite', 'r1', 'l1<=2', 'cube'):
        for imag in (False, True):
            for a2 in (0, 1):
                idx, b = invariant_basis(shifts(S), stag=True, imag=imag, chiA2=a2, with_inv=False)
                print(f"  P=Q  shifts {S:8s} {'imag' if imag else 'real'}  {'A2' if a2 else 'A1'} under O: dim {len(b)}")
