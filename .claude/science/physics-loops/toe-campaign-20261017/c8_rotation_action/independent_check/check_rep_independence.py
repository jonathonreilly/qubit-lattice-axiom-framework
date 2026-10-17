"""Structural cross-check of claim 3. P_R maps A^sigma_e to A^{R sigma}_{Re}
exactly (no phase), so P_R maps the flux-0 (flux-pi) signed group built from
ordering sigma to the one built from R sigma. Claim 3 is therefore equivalent
to: within each of the 60 classes, the flux-0 and flux-pi signed groups do not
depend on which of the 12 orderings is used to build them. Test that directly,
and test the exact identity P_R A^sigma P_R^-1 = A^{R sigma}. L = 4."""
import itertools
from collections import Counter

from pauli_bksf import (Code, Lattice, Span, DIRS, edge_perm, matvec,
                        permute_pauli, rotations, sign_vs_canonical)

L = 4
lat = Lattice(L)
classes = {}
for order in itertools.permutations(range(6)):
    code = Code(lat, order)
    key = Span([g for _, g in code.generators()], lat.n).canonical_basis()
    classes.setdefault(key, []).append(order)


def sector(code, flux):  # flux 0 or 1 (pi) on all plaquettes
    hs = code.hop_signs()
    h = [next(iter(hs[c])) for c in range(3)]
    return tuple((0 if h[c] == 1 else 1) ^ flux for c in range(3))


def same_signed_group(codeA, sA, codeB, sB):
    gA = codeA.generators(sA)
    gB = codeB.generators(sB)
    pa = [g for _, g in gA]
    plaq_c = [lab[2] if lab[0] == "P" else -1 for lab, _ in gA]
    sp = Span([g for _, g in codeA.generators((0, 0, 0))], lat.n)
    for _, g in gB:
        cb = sp.decompose(g)
        if cb is None:
            return False
        prod = sp.product(cb)
        nc = [0, 0, 0]
        j, r = 0, cb
        while r:
            if r & 1 and plaq_c[j] >= 0:
                nc[plaq_c[j]] += 1
            r >>= 1
            j += 1
        sg = sign_vs_canonical(prod) * (-1) ** sum(sA[c] * nc[c] for c in range(3))
        if sg != sign_vs_canonical(g):
            return False
    return True


res = Counter()
for key, orders in classes.items():
    rep = Code(lat, orders[0])
    for o in orders[1:]:
        c = Code(lat, o)
        for flux in (0, 1):
            res[(flux, same_signed_group(rep, sector(rep, flux), c, sector(c, flux)))] += 1
print("(flux 0/pi, same signed group as class rep): count over 60*11 orderings:", dict(res))

# exact covariance of edge operators
ROTS = rotations()
bad = 0
for order in list(itertools.permutations(range(6)))[::37]:
    code = Code(lat, order)
    for M in ROTS:
        perm = edge_perm(lat, M)
        # rotated ordering: direction d has rank of R^{-1} d
        Minv = tuple(tuple(M[j][i] for j in range(3)) for i in range(3))
        rk = {}
        for d in DIRS:
            e = [0, 0, 0]
            e[d[0]] = d[1]
            pre = matvec(Minv, tuple(e))
            a = [i for i in range(3) if pre[i] != 0][0]
            rk[d] = code.rank[(a, pre[a])]
        new_order = tuple(DIRS.index(d) for d in sorted(DIRS, key=lambda d: rk[d]))
        rc = Code(lat, new_order)
        for v in lat.verts()[:8]:
            for a in range(3):
                img = permute_pauli(code.A(v, a), perm)
                # target edge
                e = [0, 0, 0]; e[a] = 1
                Re = matvec(M, tuple(e)); b = [i for i in range(3) if Re[i]][0]
                w = matvec(M, v)
                tgt = rc.A(w, b) if Re[b] == 1 else rc.A(lat.add(w, b, -1), b)
                if img != tgt:
                    bad += 1
print("P_R A^sigma_e P_R^-1 == A^{R sigma}_{Re} exactly: mismatches =", bad)
