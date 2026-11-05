import itertools, collections, numpy as np
src = __import__('pathlib').Path(__file__).with_name('asymmetry_misalignment_part_octonion_table_2026_10_26.py').read_text().split("# ---- Frobenius")[0]
exec(src)
# Jordan identity with a genuine quaternion subalgebra {1, e_0, e_1, e_3} (Fano line (0,1,3))
rng2 = np.random.default_rng(11)
def rand_herm_idx(n, idx):
    A = np.zeros((n, n, 8))
    for i in range(n):
        A[i, i, 0] = rng2.normal()
        for j in range(i + 1, n):
            v = np.zeros(8); v[idx] = rng2.normal(size=len(idx)); A[i, j] = v; A[j, i] = conj(v)
    return A
def mm(A, B):
    n = A.shape[0]; C = np.zeros_like(A)
    for i in range(n):
        for k in range(n): C[i, k] = sum(omul(A[i, j], B[j, k]) for j in range(n))
    return C
def jp(A, B): return (mm(A, B) + mm(B, A)) / 2
Hidx = [0, 1, 2, 4]          # 1, e_0, e_1, e_3
assert all(M[a, b, c] == 0 or c in Hidx for a in Hidx for b in Hidx for c in range(8))
for n in (3, 4, 5):
    w = 0
    for t in range(3):
        A, B = rand_herm_idx(n, Hidx), rand_herm_idx(n, Hidx); A2 = jp(A, A)
        w = max(w, np.abs(jp(jp(A, B), A2) - jp(A, jp(B, A2))).max())
    print(f"Jordan identity defect on H_{n}(H) (true quaternion subalgebra): {w:.1e}")
# complement search in the 1344 group: lifts of generators of GL(3,2)
def cmp_(A, B):
    (p, s), (q, t) = A, B
    return tuple(p[q[i]] for i in range(7)), tuple(t[i] * s[q[i]] for i in range(7))
def closure(gens):
    e = (tuple(range(7)), (1,) * 7); H = {e}; fr = [e]
    while fr:
        nf = []
        for a in fr:
            for b in gens:
                c = cmp_(a, b)
                if c not in H: H.add(c); nf.append(c)
        fr = nf
        if len(H) > 1344: break
    return H
byperm = collections.defaultdict(list)
for A in auts: byperm[A[0]].append(A)
perms = list(byperm)
def pcomp(p, q): return tuple(p[q[i]] for i in range(7))
def pclos(gs):
    e = tuple(range(7)); H = {e}; fr = [e]
    while fr:
        nf = []
        for a in fr:
            for b in gs:
                c = pcomp(a, b)
                if c not in H: H.add(c); nf.append(c)
        fr = nf
    return H
gen = None
for p, q in itertools.combinations(perms, 2):
    if len(pclos([p, q])) == 168: gen = (p, q); break
comp_found = 0
for A in byperm[gen[0]]:
    for B in byperm[gen[1]]:
        if len(closure([A, B])) == 168: comp_found += 1
print("complements to 2^3 in the 1344 signed-automorphism group (lift pairs generating order 168):", comp_found, "of", len(byperm[gen[0]]) * len(byperm[gen[1]]))
# preimage of F21 (pure perms i -> a i + b) in the 1344 group: order statistics vs AGammaL(1,8)
F21 = {tuple((a * i + b) % 7 for i in range(7)) for a in (1, 2, 4) for b in range(7)}
pre = [A for A in auts if A[0] in F21]
def order_sp(A):
    e = (tuple(range(7)), (1,) * 7); X = A; k = 1
    while X != e: X = cmp_(A, X); k += 1
    return k
print("preimage of F21: order", len(pre), "; element orders", dict(sorted(collections.Counter(order_sp(A) for A in pre).items())),
      "; AGammaL(1,8) has {1:1,2:7,3:56,6:56,7:48}")
# orbit of the real unit: automorphisms fix 1; orbits on the 8 basis lines
print("automorphisms fix the real unit: True by construction; orbit sizes on the 7 imaginary lines under the preimage of F21:",
      sorted(collections.Counter(min(A[0][i] for A in pre if True) for i in range(7)).values()))
