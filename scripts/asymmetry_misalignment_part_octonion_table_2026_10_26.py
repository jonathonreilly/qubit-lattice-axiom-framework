#!/usr/bin/env python3
"""Octonion checks: cyclic table, signed automorphisms (expect 1344, pure-perm 21 = F21), Frobenius as a colour
rotation, u -> -u inside G2, left multiplications as 3-qubit Paulis, Cayley-form support = RM(1,3) weight-4 words,
Jordan identity on H_n(O) for n = 2,3,4, and the Furey 1+3+3+1 split."""
import itertools, collections, numpy as np
rng = np.random.default_rng(7)
# basis index 0 = real unit '1'; imaginary units e_{i}, i in Z7, stored at index i+1
# cyclic table: e_i e_{i+1} = e_{i+3}  (and cyclic permutations of each triple), e_i^2 = -1
TRI = [(i % 7, (i + 1) % 7, (i + 3) % 7) for i in range(7)]
M = np.zeros((8, 8, 8))          # e_a e_b = sum_c M[a,b,c] e_c
for a in range(8): M[0, a, a] = 1; M[a, 0, a] = 1
for i in range(7): M[i + 1, i + 1, 0] = -1
for (a, b, c) in TRI:
    for (x, y, z) in ((a, b, c), (b, c, a), (c, a, b)):
        M[x + 1, y + 1, z + 1] = 1; M[y + 1, x + 1, z + 1] = -1
def omul(x, y): return np.einsum('a,b,abc->c', x, y, M)
def conj(x): return np.concatenate([[x[0]], -x[1:]])
x, y, z = rng.normal(size=(3, 8))
alt = max(np.abs(omul(omul(x, x), y) - omul(x, omul(x, y))).max(), np.abs(omul(omul(y, x), x) - omul(y, omul(x, x))).max())
assoc = np.abs(omul(omul(x, y), z) - omul(x, omul(y, z))).max()
norm = abs(np.linalg.norm(omul(x, y)) - np.linalg.norm(x) * np.linalg.norm(y))
print(f"cyclic table: alternativity defect {alt:.1e}, associator {assoc:.2f} (nonzero), |xy|-|x||y| {norm:.1e}")
# ---- signed permutation automorphisms of the imaginary units
auts = []
for p in itertools.permutations(range(7)):
    for s in itertools.product((1, -1), repeat=7):
        ok = True
        for (a, b, c) in TRI:   # e_a e_b = e_c must map to s_a s_b e_pa e_pb = s_c e_pc
            pa, pb, pc = p[a], p[b], p[c]
            val = M[pa + 1, pb + 1, pc + 1]
            if val == 0 or s[a] * s[b] * val != s[c]: ok = False; break
        if ok: auts.append((p, s))
pure = [p for p, s in auts if all(v == 1 for v in s)]
print("signed-permutation automorphisms of O:", len(auts), "; pure permutation automorphisms:", len(pure),
      "; distinct underlying perms:", len({p for p, _ in auts}))
print("   pure perms are i -> a i + b with a in {1,2,4}:", sorted(pure) == sorted({tuple((a * i + b) % 7 for i in range(7)) for a in (1, 2, 4) for b in range(7)}))
# non-split check: does some involution of the 168 perm image have no involutive lift?
def oord(ps):
    p, s = ps; q, t = p, s; k = 1
    while not (q == tuple(range(7)) and all(v == 1 for v in t)):
        q, t = tuple(p[q[i]] for i in range(7)), tuple(t[i] * s[q[i]] if False else s[q[i]] * t[i] for i in range(7)); k += 1
        if k > 50: return -1
    return k
# composition of signed perms: (p,s) acts e_i -> s_i e_{p(i)}; (p,s)o(q,t): e_i -> t_i s_{q(i)} e_{p(q(i))}
def cmp_(A, B):
    (p, s), (q, t) = A, B
    return tuple(p[q[i]] for i in range(7)), tuple(t[i] * s[q[i]] for i in range(7))
def order_sp(A):
    e = (tuple(range(7)), (1,) * 7); X = A; k = 1
    while X != e: X = cmp_(A, X); k += 1
    return k
byperm = collections.defaultdict(list)
for A in auts: byperm[A[0]].append(A)
def porder(p):
    q = p; k = 1
    while q != tuple(range(7)): q = tuple(p[q[i]] for i in range(7)); k += 1
    return k
inv_noinv = sum(1 for p, L in byperm.items() if porder(p) == 2 and not any(order_sp(A) == 2 for A in L))
print("   involutions of the perm image GL(3,2) with no involutive lift:", inv_noinv, "of", sum(porder(p) == 2 for p in byperm), "(>0 => extension 2^3.L3(2) is non-split)")
# ---- Frobenius i -> 2i: fixed unit, action on C^3 = u^perp with complex structure L_u
frob = tuple((2 * i) % 7 for i in range(7))
assert (frob, (1,) * 7) in auts
fixed = [i for i in range(7) if frob[i] == i]
u = fixed[0]
print("Frobenius i->2i is an automorphism; fixed imaginary unit(s):", fixed)
Lu = np.array([[M[u + 1, b, c] for b in range(8)] for c in range(8)])   # L_u as matrix: (L_u)_{cb}
others = [i for i in range(7) if i != u]
# complex lines {e_a, u e_a}
lines = []; used = set()
for a in others:
    if a in used: continue
    img = Lu @ np.eye(8)[a + 1]; b = int(np.argmax(np.abs(img))) - 1
    lines.append((a, b, img[b + 1])); used |= {a, b}
# complex coordinates: z_j = coefficient of e_{a_j} + i * coefficient of (u e_{a_j})
P8 = np.zeros((8, 8))
for i in range(7): P8[frob[i] + 1, i + 1] = 1
P8[0, 0] = 1
def to_c3(v): return np.array([v[a + 1] + 1j * v[b + 1] * sgn for (a, b, sgn) in lines])
F3 = np.zeros((3, 3), complex)
for j, (a, b, sgn) in enumerate(lines):
    F3[:, j] = to_c3(P8 @ np.eye(8)[a + 1])
# check complex-linearity: P8 commutes with L_u
print("   Frobenius commutes with L_u (complex-linear on u-perp):", np.allclose(P8 @ Lu, Lu @ P8),
      "; 3x3 matrix on C^3:\n", np.round(F3, 3), "\n   det", np.round(np.linalg.det(F3), 6), " eigenvalues", np.round(np.linalg.eigvals(F3), 3),
      " unitary", np.allclose(F3 @ F3.conj().T, np.eye(3)), " scalar (central in SU(3))?", np.allclose(F3, F3[0, 0] * np.eye(3)))
# ---- u -> -u via a sign character (grading by F_8): find a signed automorphism with p = id and s_u = -1
flip = [A for A in auts if A[0] == tuple(range(7)) and A[1][u] == -1]
print("diagonal sign automorphisms (characters of Z2^3) with e_u -> -e_u:", len(flip), "(these lie in G2, which is connected: u and -u are G2-equivalent)")
# ---- left / right multiplications as 3-qubit Paulis: label basis by F_8 = F_2[x]/(x^3+x+1): index 0 -> 0, e_i -> alpha^i
pw = [1]
for k in range(6):
    v = pw[-1] << 1
    if v & 8: v ^= 0b1011
    pw.append(v)
lab = [0] + pw   # basis index -> F_2^3 vector
assert sorted(lab) == list(range(8))
# grading check: e_a e_b = +- e_{a xor b}
grad = all(M[a, b, c] == 0 or lab[c] == lab[a] ^ lab[b] for a in range(8) for b in range(8) for c in range(8))
print("table is F_2^3-graded under the F_8 labelling (alpha^3 = alpha + 1):", grad)
X = np.array([[0, 1], [1, 0.]]); Z = np.diag([1., -1]); I2 = np.eye(2)
def pstring(xv, zv):
    m = np.ones((1, 1))
    for q in range(3):
        f = I2
        if (xv >> q) & 1 and (zv >> q) & 1: f = X @ Z
        elif (xv >> q) & 1: f = X
        elif (zv >> q) & 1: f = Z
        m = np.kron(f, m)   # qubit q = bit q
    return m
Pidx = np.zeros((8, 8))
for i in range(8): Pidx[lab[i], i] = 1    # basis index -> computational state |lab>
def as_pauli(Mat):
    A = Pidx @ Mat @ Pidx.T
    for xv in range(8):
        for zv in range(8):
            Pm = pstring(xv, zv)
            for sg in (1, -1):
                if np.allclose(A, sg * Pm): return (xv, zv, sg)
    return None
Lmats = [np.array([[M[a, b, c] for b in range(8)] for c in range(8)]) for a in range(8)]
Rmats = [np.array([[M[b, a, c] for b in range(8)] for c in range(8)]) for a in range(8)]
Lp = [as_pauli(Lmats[a]) for a in range(1, 8)]; Rp = [as_pauli(Rmats[a]) for a in range(1, 8)]
anti = all(np.allclose(Lmats[a] @ Lmats[b] + Lmats[b] @ Lmats[a], -2 * (a == b) * np.eye(8)) for a in range(1, 8) for b in range(1, 8))
print("left multiplications L_{e_i} are 3-qubit Pauli strings:", all(p is not None for p in Lp), "; pairwise anticommuting, square -1:", anti,
      "; right multiplications Pauli:", sum(p is not None for p in Rp), "of 7")
# ---- Cayley 4-form support
def ip(a, b): return float(a @ b)
E = np.eye(8)
supp = []
for quad in itertools.combinations(range(8), 4):
    val = 0
    for perm in itertools.permutations(quad):
        sgn = np.linalg.det(np.eye(4)[[quad.index(q) for q in perm]])
        a, b, c, d = (E[q] for q in perm)
        val += sgn * ip(a, omul(b, omul(conj(c), d)))
    if abs(val) > 1e-9: supp.append(quad)
quads = {frozenset(lab[q] for q in quad) for quad in supp}
affine_planes = set()
for a, b, c in itertools.combinations(range(8), 3):
    d = a ^ b ^ c
    if d not in (a, b, c): affine_planes.add(frozenset({a, b, c, d}))
print("Cayley 4-form: nonzero components on", len(supp), "4-subsets; equal to the 14 affine planes of F_2^3 (weight-4 words of RM(1,3)):", quads == affine_planes, len(affine_planes))
# ---- Jordan identity on H_n(K), K = O (and C, H sanity via subalgebras)
def rand_herm(n, dim=8):
    A = np.zeros((n, n, 8))
    for i in range(n):
        A[i, i, 0] = rng.normal()
        for j in range(i + 1, n):
            v = np.zeros(8); v[:dim] = rng.normal(size=dim); A[i, j] = v; A[j, i] = conj(v)
    return A
def mm(A, B):
    n = A.shape[0]; C = np.zeros_like(A)
    for i in range(n):
        for k in range(n):
            C[i, k] = sum(omul(A[i, j], B[j, k]) for j in range(n))
    return C
def jp(A, B): return (mm(A, B) + mm(B, A)) / 2
for dim, nm in ((2, "C"), (4, "H"), (8, "O")):
    for n in (2, 3, 4):
        worst = 0
        for t in range(3):
            A, B = rand_herm(n, dim), rand_herm(n, dim)
            A2 = jp(A, A); worst = max(worst, np.abs(jp(jp(A, B), A2) - jp(A, jp(B, A2))).max())
        print(f"Jordan identity defect on H_{n}({nm}): {worst:.1e}")
# ---- Furey: gamma_a = i L_a, a != u -> Cl(6) on C^8; modes c_j = (gamma_a + i gamma_{u a})/2; number operator spectrum
gam = {a: 1j * Lmats[a + 1] for a in range(7)}
cs = [(gam[a] + 1j * sgn * gam[b]) / 2 for (a, b, sgn) in lines]
car = max(np.abs(cs[j] @ cs[k].conj().T + cs[k].conj().T @ cs[j] - (j == k) * np.eye(8)).max() for j in range(3) for k in range(3))
car0 = max(np.abs(cs[j] @ cs[k] + cs[k] @ cs[j]).max() for j in range(3) for k in range(3))
if car > 1e-9:
    cs = [(gam[a] - 1j * sgn * gam[b]) / 2 for (a, b, sgn) in lines]
    car = max(np.abs(cs[j] @ cs[k].conj().T + cs[k].conj().T @ cs[j] - (j == k) * np.eye(8)).max() for j in range(3) for k in range(3))
Nop = sum(c.conj().T @ c for c in cs)
ev = np.round(np.linalg.eigvalsh((Nop + Nop.conj().T) / 2), 6)
print("Furey modes from gamma = i L: CAR defect", f"{car:.1e}/{car0:.1e}", "; number-operator multiplicities", dict(collections.Counter(ev)))
perm_modes = [[k for k in range(3) if np.allclose(P8 @ cs[j] @ P8.T, cs[k]) or np.allclose(P8 @ cs[j] @ P8.T, -cs[k]) or
               np.allclose(P8 @ cs[j] @ P8.T, 1j * cs[k]) or np.allclose(P8 @ cs[j] @ P8.T, -1j * cs[k])] for j in range(3)]
print("Frobenius maps mode c_j to c_k (up to phase):", perm_modes)
