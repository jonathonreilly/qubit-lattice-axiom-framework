"""Explicit fermionic (Majorana) form of the bare permutation P_R on the
encoded BKSF fermions, flux-0 sector, for (code, C2) pairs where P_R maps
plaquette generators onto plaquette generators (so P_R preserves the encoded
Fock space).  Encoding: A_(v,a) = -i g_v g_{v+a} * u_e (u_e = +1 in flux 0,
consistent with hop product +1), B_v = -i g_v h_v (h_v the second Majorana).
For each edge e we compute P_R(A_e) = d_e * A_{Re}^{(+orient)} * prod(B) * (plaquettes)
and print which vertices carry the B factors, relative to the endpoints of Re.
Then we solve for a Majorana map alpha: g_v -> s_v g_{Rv} or s_v h_{Rv},
h_v -> ..., consistent with all images, and evaluate alpha^2 on g_x."""
import itertools, json
from collections import Counter
from pauli_bksf import *
from pair_test import signed_sign
L = 6; lat = Lattice(L)
lat4 = Lattice(4)
classes = {}
for order in itertools.permutations(range(6)):
    code = Code(lat4, order)
    key = Span([g for _, g in code.generators()], lat4.n).canonical_basis()
    classes.setdefault(key, []).append(order)
out = Counter()
examples = 0
for orders in classes.values():
    for M in rotations():
        if order_of(M) != 2: continue
        perm = edge_perm(lat, M)
        for o in orders:
            code = Code(lat, o)
            G = code.generators((0, 0, 0)); labels = [l for l, _ in G]; gens = [g for _, g in G]
            supp = set((g[0], g[1]) for g in gens)
            base0 = [0, lat.nv, lat.nv + 1, lat.nv + 2]
            sp = None
            if not all((lambda im: (im[0], im[1]) in supp)(permute_pauli(gens[i], perm)) for i in base0):
                continue
            sp = Span(gens, lat.n)
            plaq_c = [l[2] if l[0] == 'P' else -1 for l in labels]
            hs = code.hop_signs(); h = tuple(next(iter(hs[c])) for c in range(3))
            s0 = tuple(0 if h[c] == 1 else 1 for c in range(3))
            # flux-0 signed generators
            Gs = [g for _, g in code.generators(s0)]
            spS = Span(Gs, lat.n)
            pattern = []
            v = (0, 0, 0)
            for a in range(3):
                e = [0, 0, 0]; e[a] = 1
                Re = matvec(M, tuple(e)); b = [i for i in range(3) if Re[i]][0]
                w = matvec(M, v)
                if Re[b] == 1:
                    tail, A2 = w, code.A(w, b); orient = +1
                else:
                    tail = lat.add(w, b, -1); A2 = code.A(tail, b); orient = -1
                head = lat.add(tail, b)
                img = permute_pauli(code.A(v, a), perm)
                D = pmul(img, A2)  # img * A2
                cb = spS.decompose(D)
                Bs = [labels[j][1] for j in range(len(Gs)) if cb >> j & 1 and labels[j][0] == 'B']
                if len(Bs) > lat.nv // 2:
                    Bs = [u for u in lat.verts() if u not in Bs]
                Bs = [tuple(c % L for c in u) for u in Bs]
                rel = []
                for u in Bs:
                    if u == tuple(c % L for c in tail): rel.append('tail')
                    elif u == tuple(c % L for c in head): rel.append('head')
                    else: rel.append('other')
                pattern.append((a, orient, tuple(sorted(rel))))
            out[tuple(pattern)] += 1
            break
for k, v in out.most_common():
    print(v, k)
