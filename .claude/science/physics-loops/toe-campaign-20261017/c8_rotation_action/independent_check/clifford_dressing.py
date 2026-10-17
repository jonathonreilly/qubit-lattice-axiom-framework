"""Realization dependence. W = prod_v exp(-i pi B_v / 4) is a product of
commuting local Clifford gates (non-Pauli); W A_e W^dag = -A_e B_t B_h,
W B_v W^dag = B_v. U' = P_R W satisfies U'^2 = W^2 = prod(-i B_v) = const
(prod_v B_v = 1), commutes with every stabilizer generator's group, and is
thus another legitimate Z2 realization of C2. Pair test for U' (expect
lambda' = -lambda, i.e. eta' = +1, the scalar rotation), on the same
(code, edge C2) cases as pair_test_all_reps.py. L = 6."""
import itertools
from collections import Counter
from pauli_bksf import *
from pair_test import path_ops, dagger, signed_sign
import pair_test
L = 6; lat = Lattice(L); pair_test.L = L
lat4 = Lattice(4)
classes = {}
for order in itertools.permutations(range(6)):
    code = Code(lat4, order)
    key = Span([g for _, g in code.generators()], lat4.n).canonical_basis()
    classes.setdefault(key, []).append(order)

def W_conj_string(code, x, y):
    """W S W^dag for S = path_ops(code,x,y): conjugate each factor."""
    P = (0, 0, 0); cur = list(x)
    for a in range(3):
        d = (y[a] - cur[a]) % L
        if d > L // 2: d -= L
        st = 1 if d > 0 else -1
        for _ in range(abs(d)):
            if st == 1: v = tuple(cur)
            else:
                v = list(cur); v[a] -= 1; v = tuple(v)
            A = code.A(v, a)
            Wa = pmul(pmul(A, code.B(v)), code.B(lat.add(v, a)))
            Wa = (Wa[0], Wa[1], (Wa[2] + 2) % 4)
            P = pmul(P, Wa); cur[a] += st
    return P

# sanity: W A W^dag = -A B_t B_h  checked with exp formula on Pauli algebra:
# exp(-i pi B/4) A exp(i pi B/4) = A exp(i pi B/2) = A (i B) when {A,B}=0.
res = Counter()
for orders in classes.values():
    for M in rotations():
        if order_of(M) != 2: continue
        perm = edge_perm(lat, M)
        for o in orders:
            code = Code(lat, o)
            G = code.generators((0, 0, 0)); labels = [l for l, _ in G]; gens = [g for _, g in G]
            supp = set((g[0], g[1]) for g in gens)
            b0 = [0, lat.nv, lat.nv + 1, lat.nv + 2]
            if not all((lambda im: (im[0], im[1]) in supp)(permute_pauli(gens[i], perm)) for i in b0):
                continue
            sp = Span(gens, lat.n); plaq_c = [l[2] if l[0] == 'P' else -1 for l in labels]
            hs = code.hop_signs(); h = tuple(next(iter(hs[c])) for c in range(3))
            s0 = tuple(0 if h[c] == 1 else 1 for c in range(3))
            for sname, s in (('flux0', s0), ('fluxpi', tuple(1 - t for t in s0))):
                lb, lw = set(), set()
                for x in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 1, 0), (1, 1, 1), (2, 0, 1), (1, 2, -1)]:
                    Rx = matvec(M, x)
                    if all((Rx[i] - x[i]) % L == 0 for i in range(3)): continue
                    S = path_ops(code, x, Rx)
                    for tgt, SR in ((lb, permute_pauli(S, perm)), (lw, permute_pauli(W_conj_string(code, x, Rx), perm))):
                        O = pmul(dagger(S), SR); cb = sp.decompose(O)
                        if cb is None: tgt.add('not-in-group'); continue
                        sg, _ = signed_sign(sp, cb, plaq_c, s); tgt.add(sign_vs_canonical(O) / sg)
                res[(sname, 'bare P_R lambda', str(sorted(lb, key=str)), 'P_R W lambda', str(sorted(lw, key=str)))] += 1
            break
for k, v in sorted(res.items()):
    print(v, k)
