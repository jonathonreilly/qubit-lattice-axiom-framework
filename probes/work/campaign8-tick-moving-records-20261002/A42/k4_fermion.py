"""A42 check k4: one fermion mode per site, graded (CAR) product.
(a) Even automorphisms of one mode = O(2) on the Majorana pair (phases = SO(2),
    particle-hole types = reflections).  Enumerate homomorphisms of the proper
    cubic group O = <a,b | a^4 = b^3 = (ab)^2 = 1> into the finite subgroups D_n
    of O(2) (n <= 12) and record whether the coordinate half-turn a^2 ever acts
    nontrivially.
(b) Graded one-mode subalgebras: which graded-commute with themselves.
(c) Quasi-free (Bogoliubov) nearest-neighbour ticks: with M_{-e} = M_e the
    Fourier coefficient at 2e of M(k)^dag M(k) is M_e^T M_e, so M_e = 0.
(d) 1D comparator: the two-way Majorana shift (gamma1 right, gamma2 left) is a
    valid automorphism and is reflection covariant only with the onsite swap
    gamma1 <-> gamma2 on the reflection, an action the 3D half-turns cannot carry.
"""
import itertools, numpy as np

# ---------- (a) ----------
ROTS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3), int)
        for i, p in enumerate(perm): R[p, i] = signs[i]
        if round(np.linalg.det(R)) == 1: ROTS.append(R)
def order(M):
    P = np.eye(len(M), dtype=M.dtype); k = 0
    while True:
        P = P @ M; k += 1
        if np.allclose(P, np.eye(len(M))): return k
a = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])          # quarter turn about z
b = next(R for R in ROTS if order(R) == 3 and order(a @ R) == 2)
# generate the group from a, b to confirm the presentation
G = {tuple(np.eye(3, dtype=int).ravel())}; frontier = [np.eye(3, dtype=int)]
while frontier:
    nxt = []
    for M in frontier:
        for g in (a, b):
            P = M @ g; key = tuple(P.ravel())
            if key not in G: G.add(key); nxt.append(P)
    frontier = nxt
print('(a) <a,b> has order', len(G), '; a^2 = half-turn about z:', (a @ a).tolist())
def Dn(n):
    els = []
    for k in range(n):
        t = 2 * np.pi * k / n
        els.append(np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]]))
        els.append(np.array([[np.cos(t), np.sin(t)], [np.sin(t), -np.cos(t)]]))
    return els
I = np.eye(2); homs = 0; nontriv_half = 0; images = set()
for n in range(1, 13):
    E = Dn(n)
    for A in E:
        if not np.allclose(np.linalg.matrix_power(A, 4), I): continue
        for B in E:
            if not np.allclose(np.linalg.matrix_power(B, 3), I): continue
            if not np.allclose(np.linalg.matrix_power(A @ B, 2), I): continue
            homs += 1
            if not np.allclose(A @ A, I): nontriv_half += 1
            # image size
            S = {tuple(np.round(I, 8).ravel())}; fr = [I]
            while fr:
                nx = []
                for M in fr:
                    for g in (A, B):
                        P = M @ g; k = tuple(np.round(P, 8).ravel())
                        if k not in S: S.add(k); nx.append(P)
                fr = nx
            refl = any(np.linalg.det(np.array(k).reshape(2, 2)) < 0 for k in S)
            images.add((len(S), 'with reflections' if refl else 'rotations only',
                        'a acts as reflection' if np.linalg.det(A) < 0 else 'a acts as rotation'))
print(f'    homomorphisms found: {homs}; with a^2 != 1: {nontriv_half}; image types: {sorted(images)}')

# ---------- (b) ----------
c = np.array([[0, 1], [0, 0]], complex)            # one-mode annihilator in the {|0>,|1>} basis
g1 = c + c.conj().T; g2 = -1j * (c - c.conj().T); n = c.conj().T @ c
def graded_self_commuting(gens):
    # gens: list of (operator, parity); check x y = (-1)^{|x||y|} y x for all pairs
    for X, px in gens:
        for Y, py in gens:
            if not np.allclose(X @ Y, (-1) ** (px * py) * Y @ X): return False
    return True
print('(b) graded self-commuting:  C1:', graded_self_commuting([(np.eye(2), 0)]),
      ' D=span{1,n}:', graded_self_commuting([(np.eye(2), 0), (n, 0)]),
      ' span{1,gamma}:', graded_self_commuting([(np.eye(2), 0), (g1, 1)]),
      ' M2:', graded_self_commuting([(np.eye(2), 0), (n, 0), (g1, 1), (g2, 1)]))
th = np.linspace(0, np.pi, 7)
print('    two Majoranas gamma_t = cos t g1 + sin t g2 anticommute iff t1-t2 = pi/2 mod pi:',
      [bool(np.allclose((np.cos(t)*g1+np.sin(t)*g2) @ g1, -g1 @ (np.cos(t)*g1+np.sin(t)*g2))) for t in th])

# ---------- (c) ----------
rng = np.random.default_rng(3)
Me = rng.normal(size=(2, 2))
print('(c) coefficient at 2e of M^dag M with M_{-e}=M_e is M_e^T M_e; Frobenius norm for a random M_e:',
      round(float(np.linalg.norm(Me.T @ Me)), 4), '(zero only for M_e = 0, since tr M_e^T M_e = |M_e|^2)')

# ---------- (d) ----------
L = 6  # Majoranas on a ring via Jordan-Wigner, 2L Majoranas, ordering g1_0,g2_0,g1_1,g2_1,...
def majoranas(L):
    X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]], complex)
    Z = np.diag([1, -1]).astype(complex); I2 = np.eye(2)
    out = []
    for j in range(L):
        for P in (X, Y):
            ops = [Z] * j + [P] + [I2] * (L - j - 1)
            M = np.array([[1]], complex)
            for o in ops: M = np.kron(M, o)
            out.append(M)
    return out
G1 = majoranas(L)
def idx(kind, x): return 2 * (x % L) + kind
# two-way shift as a permutation of Majoranas: g1_x -> g1_{x+1}, g2_x -> g2_{x-1}
perm = {idx(0, x): idx(0, x + 1) for x in range(L)} | {idx(1, x): idx(1, x - 1) for x in range(L)}
imgs = {k: G1[v] for k, v in perm.items()}
ok_car = all(np.allclose(imgs[i] @ imgs[j] + imgs[j] @ imgs[i], 2 * (i == j) * np.eye(2 ** L)) for i in imgs for j in imgs)
# reflection x -> -x with onsite swap g1 <-> g2 : r(g1_x) = g2_{-x}, r(g2_x) = g1_{-x}
refl = {idx(0, x): idx(1, -x) for x in range(L)} | {idx(1, x): idx(0, -x) for x in range(L)}
# covariance: alpha(r(g)) == r(alpha(g)) on generators (all maps are Majorana permutations)
cov_swap = all(perm[refl[i]] == refl[perm[i]] for i in perm)
refl_plain = {idx(0, x): idx(0, -x) for x in range(L)} | {idx(1, x): idx(1, -x) for x in range(L)}
cov_plain = all(perm[refl_plain[i]] == refl_plain[perm[i]] for i in perm)
print(f'(d) 1D two-way Majorana shift: CAR preserved={ok_car}; reflection-covariant with onsite swap={cov_swap}; '
      f'with trivial onsite action={cov_plain}')
