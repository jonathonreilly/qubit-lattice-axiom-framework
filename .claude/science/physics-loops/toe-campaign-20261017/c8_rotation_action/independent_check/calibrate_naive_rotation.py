"""Calibration of the pair test and decomposition of P_R into
'naive scalar-fermion rotation' x 'edge signs'.

In the flux-0 sector the plaquette subspace is the BKSF encoding of spinless
fermions on vertices with A_(v,a) <-> -i g_v g_{v+a} (one Majorana g per vertex,
edges positively oriented); check: hop product = +1 for that algebra.
The naive scalar rotation alpha0: c_v -> c_{Rv} acts on hops as
A_e -> o_e A_{Re}, o_e = -1 if R reverses the edge orientation.
(1) Pair test with alpha0 in place of P_R: expect lambda = -1 (scalar fermions:
    c+_x c+_Rx -> c+_Rx c+_x = - c+_x c+_Rx).
(2) For P_R: D_e = P_R(A_e) * o_e A_{Re}  (should be +-(stabilizer)); record
    whether D_e contains vertex terms and its sign d_e; then kappa := alpha^2 on
    one fermion = prod_{e in path x->Rx} d_e when D_e has no B content, and
    lambda(P_R) = -kappa.
"""
import itertools, json
from collections import Counter
from pauli_bksf import *
from pair_test import path_ops, dagger, signed_sign
import pair_test

L = 6; lat = Lattice(L); pair_test.L = L
reps = [tuple(r) for r in json.load(open('reps_L4.json'))]
res = Counter()
for r in reps:
    code = Code(lat, r)
    hs = code.hop_signs(); h = tuple(next(iter(hs[c])) for c in range(3))
    s0 = tuple(0 if h[c] == 1 else 1 for c in range(3))
    G = code.generators((0, 0, 0)); labels = [l for l, _ in G]; gens = [g for _, g in G]
    plaq_c = [l[2] if l[0] == 'P' else -1 for l in labels]
    sp = Span(gens, lat.n)
    base = [i for i, l in enumerate(labels) if l[1] == (0, 0, 0)]
    supp = set((g[0], g[1]) for g in gens)
    for M in rotations():
        if order_of(M) != 2: continue
        perm = edge_perm(lat, M)
        if not all(sp.decompose(permute_pauli(gens[i], perm)) is not None for i in base):
            continue
        hsym = all((permute_pauli(gens[i], perm)[0], permute_pauli(gens[i], perm)[1]) in supp for i in base)
        # alpha0 on single hops
        def alpha0_A(v, a):
            e = [0, 0, 0]; e[a] = 1
            Re = matvec(M, tuple(e)); b = [i for i in range(3) if Re[i]][0]
            w = matvec(M, v)
            if Re[b] == 1:
                return code.A(w, b)
            Q = code.A(lat.add(w, b, -1), b)
            return (Q[0], Q[1], (Q[2] + 2) % 4)
        # alpha0 preserves the flux-0 signed plaquettes?
        ok0 = True
        for v in [(0, 0, 0)]:
            for c in range(3):
                a, b = Code.plane(c); add = lat.add
                img = pmul(pmul(pmul(alpha0_A(v, b), alpha0_A(add(v, b), a)), alpha0_A(add(v, a), b)), alpha0_A(v, a))
                cb = sp.decompose(img)
                sg, _ = signed_sign(sp, cb, plaq_c, s0)
                ok0 &= (sign_vs_canonical(img) == sg)
        # pair test for alpha0 and P_R (x off axis)
        lam0 = set(); lamP = set(); Bcontent = Counter(); kap = set()
        for x in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 1, 0), (1, 1, 1), (2, 0, 1)]:
            Rx = matvec(M, x)
            if all((Rx[i] - x[i]) % L == 0 for i in range(3)): continue
            # path ops as list for alpha0
            P = (0, 0, 0); Pa = (0, 0, 0); cur = list(x)
            for a in range(3):
                d = (Rx[a] - cur[a]) % L
                if d > L // 2: d -= L
                st = 1 if d > 0 else -1
                for _ in range(abs(d)):
                    if st == 1: v = tuple(cur)
                    else:
                        v = list(cur); v[a] -= 1; v = tuple(v)
                    P = pmul(P, code.A(v, a)); Pa = pmul(Pa, alpha0_A(v, a))
                    cur[a] += st
            O = pmul(dagger(P), Pa); cb = sp.decompose(O)
            sg, _ = signed_sign(sp, cb, plaq_c, s0); lam0.add(sign_vs_canonical(O) / sg)
            if hsym:
                O = pmul(dagger(P), permute_pauli(P, perm)); cb = sp.decompose(O)
                sg, _ = signed_sign(sp, cb, plaq_c, s0); lamP.add(sign_vs_canonical(O) / sg)
        # D_e content
        for a in range(3):
            v = (1, 2, 0)
            D = pmul(permute_pauli(code.A(v, a), perm), alpha0_A(v, a))
            cb = sp.decompose(D)
            if cb is None:
                Bcontent['not in group'] += 1; continue
            nB = sum(1 for j in range(len(gens)) if cb >> j & 1 and labels[j][0] == 'B')
            Bcontent[min(nB, lat.nv - nB)] += 1
        res[(('hsym', hsym), ('alpha0 ok', ok0), ('lam alpha0', tuple(sorted(lam0, key=str))), ('lam P_R', tuple(sorted(lamP, key=str))), ('#B in D_e', tuple(sorted(Bcontent.items()))))] += 1
for k, v in sorted(res.items(), key=str):
    print(v, k)
