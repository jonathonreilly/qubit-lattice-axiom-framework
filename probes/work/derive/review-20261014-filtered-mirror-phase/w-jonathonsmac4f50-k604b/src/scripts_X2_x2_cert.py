"""X2 certificate: T1-T5 of ../PREREG.md (written before this script was run).
Walker H_W = sum_a sigma_a sin p_a on Z^3, corners {0,pi}^3 labelled by v in Z2^3 (v_a = 1 <=> k_a = pi).
Node chirality chi = prod cos k_a = (-1)^hw (F1 convention: chi=+1 right-handed, -1 left-handed).
"""
import numpy as np, itertools, sys, time
np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(20261014)
t0 = time.time()
def P(*a): print(*a); sys.stdout.flush()

C = list(itertools.product((0, 1), repeat=3))
hw = lambda c: sum(c)
add = lambda *cs: tuple(sum(x) % 2 for x in zip(*cs))
ZERO = (0, 0, 0)

# ------------------------------------------------------------------ T1
P("=== T1: corner-label (Z2^3) selection rules, exact single translations ===")
def classes(Lt, M):
    Lt, M = list(Lt), list(M)
    lm3 = [(l, m) for l in Lt for m in itertools.combinations_with_replacement(M, 3) if add(l, *m) == ZERO]
    l3m = [(l, m) for l in itertools.combinations_with_replacement(Lt, 3) for m in M if add(*l, m) == ZERO]
    acbb = [(a, b) for a in Lt for b in itertools.combinations_with_replacement(M, 2) if add(a, *b) in M]
    aabb = [(a, b) for a in itertools.combinations_with_replacement(Lt, 2)
            for b in itertools.combinations_with_replacement(M, 2) if add(*a, *b) == ZERO]
    return lm3, l3m, acbb, aabb
hw1 = [c for c in C if hw(c) == 1]
splits = {"A (light hw1; mirror hw0+hw2+hw3)": (hw1, [c for c in C if hw(c) != 1]),
          "G (T_d grading: light hw1+hw3; mirror hw0+hw2)": ([c for c in C if hw(c) % 2 == 1], [c for c in C if hw(c) % 2 == 0])}
for name, (Lt, M) in splits.items():
    lm3, l3m, acbb, aabb = classes(Lt, M)
    P(f"{name}: #light corners={len(Lt)}")
    P(f"   light*mirror^3 allowed: {len(lm3)}  e.g. {lm3[:2]}")
    P(f"   light^3*mirror allowed: {len(l3m)}  e.g. {l3m[:2]}")
    P(f"   A^c B B on a mirror label: {len(acbb)}  e.g. {acbb[:2]}")
    P(f"   A A B B allowed: {len(aabb)}  e.g. {aabb[:2]}")
P("Exhaustive scan: every light set Lt (any size 1..7, any corners), M = complement:")
rows = []
for r in range(1, 8):
    for Lt in itertools.combinations(C, r):
        M = [c for c in C if c not in Lt]
        lm3, l3m, _, aabb = classes(Lt, M)
        net = sum(-(-1) ** hw(c) for c in Lt)  # light index in units of L nodes (+1 per L node)
        rows.append((r, Lt, len(lm3) == 0 and len(l3m) == 0, len(aabb) > 0, net))
for r in range(1, 8):
    sub = [x for x in rows if x[0] == r]
    P(f"  |Lt|={r}: assignments={len(sub)}, odd-leg-free={sum(x[2] for x in sub)}, AABB-free={sum(not x[3] for x in sub)}"
      + (f"; odd-leg-free light sets: {[x[1] for x in sub if x[2]]}" if 0 < sum(x[2] for x in sub) <= 8 else ""))
three = [x for x in rows if x[0] == 3]
P(f"  T1(c) any 3-corner light set (3 generations) with both odd-leg classes forbidden? {any(x[2] for x in three)}")
P(f"  T1(d) any split with |Lt|,|M|>=1 where A A B B is forbidden? {any(not x[3] for x in rows)}")

# ------------------------------------------------------------------ T2
P("\n=== T2: filter covariance (L=4) and exact corner decoupling (Fock, L=2) ===")
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
SIG = [sx, sy, sz]
def f_nn(k): return (1 - np.cos(k).sum()) / 2
def f_F1(k):
    k = np.asarray(k, float); tot = 0.0
    for mu in range(3):
        term = np.sin(k[mu] / 2) ** 2
        for nu in range(3):
            if nu != mu: term *= np.cos(k[nu] / 2) ** 2
        tot += term
    return 1 - tot
Ks = lambda L: [np.array(k) * 2 * np.pi / L for k in itertools.product(range(L), repeat=3)]
def rotations():
    Rs = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3), int)
            for i in range(3): R[perm[i], i] = sg[i]
            if round(np.linalg.det(R)) == 1: Rs.append(R)
    return Rs
ROT = rotations(); assert len(ROT) == 24
def spin_lift(R):
    A = []
    for a in range(3):
        sp = sum(R[b, a] * SIG[b] for b in range(3))
        A.append(np.kron(SIG[a].T, s0) - np.kron(s0, sp))
    A = np.vstack(A); _, sv, vh = np.linalg.svd(A)
    U = vh[-1].conj().reshape(2, 2, order="F"); U /= np.sqrt(np.linalg.det(U))
    assert sv[-1] < 1e-10 and sv[-2] > 1e-6
    for a in range(3): assert np.allclose(U @ SIG[a] @ U.conj().T, sum(R[b, a] * SIG[b] for b in range(3)))
    return U
L = 4; sites = list(itertools.product(range(L), repeat=3)); idx = {x: i for i, x in enumerate(sites)}; N = len(sites)
def kernel_op(fun):
    ks = Ks(L); fx = {}
    for x in sites:
        fx[x] = sum(fun(k) * np.exp(1j * np.dot(k, x)) for k in ks) / N
    F = np.zeros((N, N), complex)
    for x in sites:
        for y in sites:
            F[idx[x], idx[y]] = fx[tuple((np.array(x) - np.array(y)) % L)]
    return F
def shift(a):
    S = np.zeros((N, N))
    for x in sites:
        y = list(x); y[a] = (y[a] + 1) % L; S[idx[tuple(y)], idx[x]] = 1
    return S
Sh = [shift(a) for a in range(3)]
HW = sum(np.kron((Sh[a].T - Sh[a]) / (2j), SIG[a]) for a in range(3))  # symbol sigma_a sin k_a (sign convention irrelevant)
FNN = np.kron(kernel_op(f_nn), s0); FF1 = np.kron(kernel_op(f_F1), s0)
for _nm, _fun in (("f_NN", f_nn), ("f_F1", f_F1)):
    _K = kernel_op(_fun)
    P(f"{_nm} real-space support (L=4): offsets with |F|>1e-12 have max |d|_inf = "
      f"{max(max(min(abs(d), L-abs(d)) for d in np.array(x)-np.array(y)) for x in sites for y in sites if abs(_K[idx[x], idx[y]])>1e-12)}, "
      f"number of nonzero offsets = {sum(abs(_K[idx[x], 0])>1e-12 for x in sites)}")
worst = {"HW": 0, "FNN": 0, "FF1": 0}
for R in ROT:
    U = spin_lift(R); Rop = np.zeros((N, N))
    for x in sites:
        Rop[idx[tuple((R @ np.array(x)) % L)], idx[x]] = 1
    O = np.kron(Rop, U)
    for nm, Mx in (("HW", HW), ("FNN", FNN), ("FF1", FF1)):
        worst[nm] = max(worst[nm], np.abs(O @ Mx - Mx @ O).max())
P("max over 24 proper rotations (spin-lifted) of |[R, X]|:", {k: f"{v:.1e}" for k, v in worst.items()})
P("max over 3 translations of |[T, X]|:", {nm: f"{max(np.abs(np.kron(Sh[a], s0) @ Mx - Mx @ np.kron(Sh[a], s0)).max() for a in range(3)):.1e}"
                                           for nm, Mx in (("HW", HW), ("FNN", FNN), ("FF1", FF1))})
for nm, fun in (("f_NN", f_nn), ("f_F1", f_F1)):
    P(f"{nm} at corners:", {''.join(map(str, c)): round(fun(np.pi * np.array(c)), 6) for c in C})
h = 1e-3; ex = np.array([np.pi, 0, 0])
Hs = np.array([[(f_F1(ex + h * (np.eye(3)[i] + np.eye(3)[j])) - f_F1(ex + h * (np.eye(3)[i] - np.eye(3)[j]))
                 - f_F1(ex - h * (np.eye(3)[i] - np.eye(3)[j])) + f_F1(ex - h * (np.eye(3)[i] + np.eye(3)[j]))) / (4 * h * h)
                for j in range(3)] for i in range(3)])
P("Hessian of f_F1 at (pi,0,0):", np.round(Hs, 4).tolist(), " (isotropic positive => leakage ~ |q|^2/4)")
Hn = np.array([[(f_nn(ex + h * (np.eye(3)[i] + np.eye(3)[j])) - f_nn(ex + h * (np.eye(3)[i] - np.eye(3)[j]))
                 - f_nn(ex - h * (np.eye(3)[i] - np.eye(3)[j])) + f_nn(ex - h * (np.eye(3)[i] + np.eye(3)[j]))) / (4 * h * h)
                for j in range(3)] for i in range(3)])
P("Hessian of f_NN at (pi,0,0):", np.round(Hn, 4).tolist(), " (indefinite => f_NN vanishes on a cone through hw1)")
ks = np.array(list(itertools.product(np.linspace(-np.pi, np.pi, 41), repeat=3)))
fF = np.array([f_F1(k) for k in ks]); near = np.array([min(np.linalg.norm((k - np.pi * np.array(c) + np.pi) % (2 * np.pi) - np.pi) for c in hw1) for k in ks])
P(f"f_F1 on 41^3 grid: min = {fF.min():.3e}; min |f_F1| at distance > 0.3 from every hw1 corner = {np.abs(fF[near > 0.3]).min():.3e}")
del HW, FNN, FF1

# Fock check, L = 2 torus: 8 sites x 2 spins = 16 modes; momentum modes are the 8 corners.
Lf = 2; fsites = list(itertools.product(range(Lf), repeat=3)); nm = 16
def mode(c, s): return C.index(c) * 2 + s
def Fmat(fun):  # psi_S(x, s) = sum_k f(k) e^{ikx} psi(k, s) / sqrt(8)
    F = np.zeros((nm, nm), complex)
    for xi, x in enumerate(fsites):
        for c in C:
            k = np.pi * np.array(c)
            for s in range(2): F[xi * 2 + s, mode(c, s)] = fun(k) * np.exp(1j * np.dot(k, x)) / np.sqrt(8)
    return F
def sector(Np): return [b for b in range(1 << nm) if bin(b).count("1") == Np]
def ann_matrix(m, src, dst):
    di = {b: i for i, b in enumerate(dst)}; A = np.zeros((len(dst), len(src)))
    for j, b in enumerate(src):
        if b >> m & 1:
            sgn = (-1) ** bin(b & ((1 << m) - 1)).count("1"); A[di[b ^ (1 << m)], j] = sgn
    return A
def randV(F, nterms, rng):
    V = np.zeros((nm,) * 4, complex)
    for _ in range(nterms):
        x = rng.integers(8); a = rng.integers(3); y = list(fsites[x]); y[a] = (y[a] + 1) % Lf; y = fsites.index(tuple(y))
        pool = [x * 2, x * 2 + 1, y * 2, y * 2 + 1]
        i, j, k, l = rng.choice(pool, 4); cf = rng.normal() + 1j * rng.normal()
        t = cf * np.einsum("a,b,c,d->abcd", F[i].conj(), F[j].conj(), F[k], F[l])
        V += t + t.transpose(3, 2, 1, 0).conj()
    return V
SEC = {Np: sector(Np) for Np in range(5)}
CM = {Np: [ann_matrix(m, SEC[Np], SEC[Np - 1]) for m in range(nm)] for Np in range(1, 5)}
def Hsector(V, Np):
    A = np.array([[CM[Np - 1][k] @ CM[Np][l] for l in range(nm)] for k in range(nm)])  # (k,l,dimN-2,dimN)
    D = np.einsum("ijkl,klab->ijab", V, A)
    return np.einsum("jiac,ijab->cb", A.conj(), D)
for lab, fun in (("filtered (f_F1)", f_F1), ("control: unfiltered (f=1)", lambda k: 1.0)):
    F = Fmat(fun); V = randV(F, 12, np.random.default_rng(7))
    H3 = Hsector(V, 3); H2 = Hsector(V, 2)
    assert np.allclose(H3, H3.conj().T) and np.allclose(H2, H2.conj().T)
    s3, s2 = sector(3), sector(2); worst_l = 0; worst_m = 0
    for c in C:
        for s in range(2):
            A = ann_matrix(mode(c, s), s3, s2); comm = np.abs(H2 @ A - A @ H3).max()
            if hw(c) == 1: worst_l = max(worst_l, comm)
            else: worst_m = max(worst_m, comm)
    P(f"Fock L=2, {lab}: ||H_N=3||={np.abs(H3).max():.2f}; max|[H, psi(hw1 corner)]| = {worst_l:.2e}; "
      f"max|[H, psi(mirror corner)]| = {worst_m:.2e}")

# ------------------------------------------------------------------ T3
P("\n=== T3: F6's bilinear reduction i*eps*F with f = s(s^2-1); add delta * i*eps*F1, f1 = s ===")
def H4(k, delta):
    sk = np.cos(k).sum(); f = sk * (sk ** 2 - 1) + delta * sk
    h = sum(np.sin(k[a]) * SIG[a] for a in range(3))
    return np.block([[h, -1j * f * s0], [1j * f * s0, -h]])  # basis (psi_k, psi_{k+Pi}); f(k+Pi) = -f(k)
grid = np.array(list(itertools.product(np.linspace(0, np.pi, 33), repeat=3)))  # half-zone suffices: (k,k+Pi) blocks
for delta in (0.0, 1e-3, 1e-2, 0.1):
    gaps = np.array([np.abs(np.linalg.eigvalsh(H4(k, delta))).min() for k in grid])
    at_hw1 = np.abs(np.linalg.eigvalsh(H4(np.array([np.pi, 0, 0]), delta))).min()
    P(f"delta={delta:g}: min|E| over grid = {gaps.min():.3e}; min|E| at (pi,0,0) = {at_hw1:.3e}")
P("FCC check: corner labels of hw1 and hw2 partners under translations by v with v_x+v_y+v_z even:",
  all((np.dot(np.array(c), v) % 2) == (np.dot(np.array(add(c, (1, 1, 1))), v) % 2)
      for c in C for v in itertools.product((0, 1), repeat=3) if sum(v) % 2 == 0))

# ------------------------------------------------------------------ T4
P("\n=== T4: generation splitting, CKM, strain; all subgroups of O x Z2^3 acting on the hw1 triplet ===")
def gen_action(R, a):
    G = np.zeros((3, 3))
    for i in range(3):
        j = int(np.argmax(np.abs(R[:, i])))   # R e_i = +-e_j ; corner e_i -> e_j (sign irrelevant mod 2 pi)
        G[j, i] = (-1) ** a[j]
    return G
elems = []; key = {}
for R in ROT:
    for a in itertools.product((0, 1), repeat=3):
        G = gen_action(R, a); kk = (R.tobytes(), G.tobytes())
        if kk not in key: key[kk] = len(elems); elems.append((R, G))
n = len(elems); P("group order (rotation part, generation action) pairs:", n)
mul = np.zeros((n, n), int)
for i, (R1, G1) in enumerate(elems):
    for j, (R2, G2) in enumerate(elems):
        mul[i, j] = key[((R1 @ R2).tobytes(), (G1 @ G2).tobytes())]
IDX = key[(np.eye(3, dtype=int).tobytes(), np.eye(3).tobytes())]
def closure(gens):
    S = {IDX}; frontier = [IDX]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = mul[x, g]
                if y not in S: S.add(y); new.append(y)
        frontier = new
    return frozenset(S)
GENS = {}
for i in range(n):
    K = closure([i]); GENS.setdefault(K, [i])
subs = set(GENS); grow = set(subs)
while grow:
    nxt = set()
    for H in grow:
        done = set(H)
        for g in range(n):
            if g in done: continue
            K = closure(GENS[H] + [g])
            if K not in subs: subs.add(K); GENS[K] = GENS[H] + [g]; nxt.add(K)
            if len(K) == 2 * len(H): done |= K
    grow = nxt
P(f"number of subgroups: {len(subs)}  ({time.time()-t0:.0f}s)")
TS = []  # traceless symmetric basis
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    E = np.zeros((3, 3)); E[i, j] = E[j, i] = 1; TS.append(E)
TS.append(np.diag([1., -1, 0])); TS.append(np.diag([1., 1, -2]) / np.sqrt(3))
def inv_strain_dim(H):
    rows = []
    for e in H:
        R = elems[e][0]; Mx = np.array([[np.sum(TS[p] * (R @ TS[q] @ R.T)) for q in range(5)] for p in range(5)]) / 2.0  # basis has norm^2 = 2 (normalisation bug in run 1, fixed 14:26Z)
        rows.append(Mx - np.eye(5))
    return 5 - np.linalg.matrix_rank(np.vstack(rows), tol=1e-9)
def commutant(H):
    rows = [np.kron(np.eye(3), elems[e][1]) - np.kron(elems[e][1].T, np.eye(3)) for e in H]
    _, sv, vh = np.linalg.svd(np.vstack(rows)); null = vh[np.sum(sv > 1e-9):]
    return [v.reshape(3, 3, order="F") for v in null]
def has_order3(H): return any(np.allclose(np.linalg.matrix_power(elems[e][0], 3), np.eye(3)) and not np.allclose(elems[e][0], np.eye(3)) for e in H)
viol = []; summary = {}
for H in subs:
    B = commutant(H); r3 = np.random.default_rng(len(H))
    def rnd():
        M = sum((r3.normal() + 1j * r3.normal()) * b for b in B); return (M + M.conj().T) / 2
    Mu, Md = rnd(), rnd()
    eu = np.linalg.eigvalsh(Mu); distinct = np.min(np.diff(np.sort(eu))) > 1e-6
    commut = all(np.abs(b1 @ b2 - b2 @ b1).max() < 1e-9 for b1 in B for b2 in B)
    _, Vu = np.linalg.eigh(Mu); _, Vd = np.linalg.eigh(Md); V = np.abs(Vu.conj().T @ Vd)
    ed = np.linalg.eigvalsh(Md); ckm_nontriv = distinct and np.min(np.diff(np.sort(ed))) > 1e-6 and V.max(axis=1).min() < 1 - 1e-6
    sd = inv_strain_dim(H); o3 = has_order3(H)
    k = (o3, distinct, ckm_nontriv, sd > 0); summary[k] = summary.get(k, 0) + 1
    if ckm_nontriv and sd == 0: viol.append(len(H))
    if ckm_nontriv and o3: viol.append(("order3-with-CKM", len(H)))
P("counts by (rotation part has order-3 element, 3 distinct masses, nontrivial CKM, >=1 invariant traceless strain):")
for k in sorted(summary): P("   ", k, summary[k])
P("T4 violations of prediction (nontrivial CKM with 0 invariant strain, or with an order-3 element):", viol)
Tet = closure([key[(R.tobytes(), gen_action(R, (0, 0, 0)).tobytes())] for R in ROT if np.allclose(np.linalg.matrix_power(R, 3), np.eye(3)) or np.allclose(R @ R, np.eye(3))])
Tet = closure([key[(R.tobytes(), gen_action(R, (0, 0, 0)).tobytes())] for R in ROT if np.allclose(np.linalg.matrix_power(R, 3), np.eye(3))])
B = commutant(Tet)
P(f"H = T (rotations of order 1,2,3; order {len(Tet)}): commutant dim {len(B)}, commutative "
  f"{all(np.abs(b1@b2-b2@b1).max()<1e-9 for b1 in B for b2 in B)}, invariant traceless strain dim {inv_strain_dim(Tet)}")
Mt = sum((rng.normal() + 1j * rng.normal()) * b for b in B); Mt = (Mt + Mt.conj().T) / 2
P("   generic T-invariant mass matrix (circulant):\n", np.round(Mt, 3), "\n   eigenvalues", np.round(np.linalg.eigvalsh(Mt), 4))

# ------------------------------------------------------------------ T5
P("\n=== T5 (locator, NN-forced): psi (walker) + chi coupled by Delta*f_F1(k) ===")
for lab, c_chi in (("chi flat", 0.0), ("chi = mirror-chirality walker (-sigma.sin k)", 1.0)):
    out = []
    for c in C:
        k = np.pi * np.array(c) + 1e-9; h = sum(np.sin(k[a]) * SIG[a] for a in range(3))
        Hk = np.block([[h, 0.7 * f_F1(k) * s0], [0.7 * f_F1(k) * s0, -c_chi * h]])
        out.append((''.join(map(str, c)), int(np.sum(np.abs(np.linalg.eigvalsh(Hk)) < 1e-6))))
    gl = np.array(list(itertools.product(np.linspace(-np.pi, np.pi, 25), repeat=3)))
    mins = [np.abs(np.linalg.eigvalsh(np.block([[sum(np.sin(k[a]) * SIG[a] for a in range(3)), 0.7 * f_F1(k) * s0],
                                                 [0.7 * f_F1(k) * s0, -c_chi * sum(np.sin(k[a]) * SIG[a] for a in range(3))]]))).min()
            for k in gl]
    gl_far = [m for k, m in zip(gl, mins) if min(np.linalg.norm((k - np.pi * np.array(cc) + np.pi) % (2 * np.pi) - np.pi) for cc in hw1) > 0.3]
    P(f"{lab}: zero modes per corner {out}; min|E| on 25^3 grid away from hw1 (>0.3) = {min(gl_far):.3e}")
P(f"\ndone in {time.time()-t0:.0f}s")
