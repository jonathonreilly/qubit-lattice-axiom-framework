AUDIT_INPUT_PATHS = ('docs/THE_MINIMAL_TURN_NEUTRAL_FAR_WALL_TERM_FOR_THREE_FAMILIES_HAS_A_FREE_FAMILY_MATRIX_WHOSE_ONLY_RULE_BLIND_CHOICE_KEEPS_U3_SO_NO_FAMILY_LABEL_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""gap-vertex-family-tensor: family tensor of the minimal symmetric far-wall gapping term, N_f = 3, 3450 proxy.
Self-contained (numpy + stdlib). Seeded. Prints < 6000 chars, ends with TOTAL."""
AUDIT_TIMEOUT_SEC = 120
import itertools, math
from fractions import Fraction as F
import numpy as np
rng = np.random.default_rng(20261024)
NP = [0, 0]
def check(name, ok, info=""):
    NP[0 if ok else 1] += 1
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))
FL = ["3", "4", "5", "0"]; K = np.array([1, 1, -1, -1]); QA = np.array([3, 4, 5, 0]); QB = np.array([2, 1, 2, -1])
l1 = np.array([1, -2, 1, 2]); l2 = np.array([2, 1, -2, 1])
print("== A. lattice, turn charge, anomaly [T]")
neutral = all(int(QA @ l) == 0 and int(QB @ l) == 0 and int(l @ (K * l)) == 0 for l in (l1, l2)) and int(l1 @ (K * l2)) == 0
minors = [l1[i]*l2[j]-l1[j]*l2[i] for i in range(4) for j in range(i+1, 4)]
g = 0
for m in minors: g = math.gcd(g, int(m))
check("A1 l1,l2 neutral, K-null, mutually null, primitive (gcd minors=1)", neutral and g == 1, f"gcd={g}")
tc = {(a, b): int((a*l1 + b*l2).sum()) % 3 for a in range(-3, 4) for b in range(-3, 4)}
check("A2 turn charge (q=1, k=0) of n1 l1+n2 l2 is 2(n1+n2) mod 3", all(v == (2*(a+b)) % 3 for (a, b), v in tc.items()))
q = np.ones(4)
an = (int(K @ q**2), int(K @ (q*QA)), int(K @ (q*QB)))
check("A3 per-family Z3 anomaly (K q^2, K q QA, K q QB) = (0,2,2): mixed term 2N_f = 0 mod 3 iff N_f = 0 mod 3",
      an == (0, 2, 2), f"coeffs={an}; N_f=1,2,3 -> {[(2*n)%3 for n in (1,2,3)]}")
print("== B. fewest-change turn-neutral L in the lattice [T]")
cand = []
for a in range(-9, 10):
    for b in range(-9, 10):
        L = a*l1 + b*l2
        if (a or b) and L.sum() % 3 == 0: cand.append((int(np.abs(L).sum()), a, b, tuple(int(x) for x in L)))
cand.sort(); m8 = [c for c in cand if c[0] == cand[0][0]]
check("B1 minimum norm 8, only +-(l2-l1) = +-(1,3,-3,-1); it CONSERVES mode number (sum L = 0)",
      cand[0][0] == 8 and sorted(c[3] for c in m8) == [(-1, -3, 3, 1), (1, 3, -3, -1)] and sum(m8[0][3]) == 0, f"{[c[3] for c in m8]}")
br = [c for c in cand if sum(c[3]) != 0]; mb = [c for c in br if c[0] == br[0][0]]
check("B2 minimal mode-number-breaking turn-neutral L: norm 12, four vectors (two up to sign)",
      br[0][0] == 12 and len(mb) == 4, f"{sorted(c[3] for c in mb)} sumL={[sum(c[3]) for c in mb]}")
print("== C. family distributions of L=(1,3,-3,-1) over 3 families [T]")
L0 = np.array([1, 3, -3, -1])
def splits(n):
    s = 1 if n >= 0 else -1
    return [tuple(s*x for x in t) for t in itertools.product(range(abs(n)+1), repeat=3) if sum(t) == abs(n)]
dists = []
for parts in itertools.product(*[splits(int(n)) for n in L0]):
    v = np.array(parts)
    if int(sum(K[f]*int(v[f] @ v[f]) for f in range(4))) == 0: dists.append(v)
onsite = [v for v in dists if np.abs(v).max() == 1]
ok = len(onsite) == 9 and all(tuple(v[1]) == (1, 1, 1) and tuple(v[2]) == (-1, -1, -1) for v in onsite)
check("C1 null norm-8 distributions; the one-site (Pauli) ones force flavours 4,5 = (1,1,1): 9 tuples (i,j)",
      ok, f"null={len(dists)}, one-site={len(onsite)}, sites needed in rest={sorted(set(int(np.abs(v).max()) for v in dists))}")
print("== D/E. tensor and u(3) commutant (tangent space) [T]/[F]")
def lam(n):
    return [S for S in itertools.combinations(range(3), n)]
def lam_rep(X, n):
    B = lam(n); d = len(B); M = np.zeros((d, d), complex)
    for c, T in enumerate(B):
        for k, t in enumerate(T):
            for s in range(3):
                if X[s, t] == 0: continue
                new = list(T); new[k] = s
                if len(set(new)) < n: continue
                perm = sorted(range(n), key=lambda i: new[i]); sign = np.linalg.det(np.eye(n)[perm]) if n > 1 else 1
                M[B.index(tuple(sorted(new))), c] += sign * X[s, t]
    return M
gens = []
for i in range(3):
    for j in range(3):
        H = np.zeros((3, 3), complex)
        if i == j: H[i, i] = 1
        elif i < j: H[i, j] = H[j, i] = 1
        else: H[i, j] = 1j; H[j, i] = -1j
        gens.append(1j * H)
def slot(X, n, cre):  # annihilation slots carry X, creation slots carry conj(X)
    return lam_rep(np.conj(X) if cre else X, n)
def action(X, slots):
    mats = [slot(X, n, c) for n, c in slots]; dims = [m.shape[0] for m in mats]; tot = 0
    for k in range(len(mats)):
        A = np.array([[1.0+0j]])
        for j, d in enumerate(dims): A = np.kron(A, mats[k] if j == k else np.eye(d))
        tot = tot + A
    return tot
def stab_dim(T, slots, gl=gens):
    cols = [action(X, slots) @ T for X in gl]; M = np.array(cols).T; M = np.vstack([M.real, M.imag])
    s = np.linalg.svd(M, compute_uv=False); return int(np.sum(s < 1e-9 * max(1, s.max())))
def inv_dim(slots, gl):
    Ms = [action(X, slots) for X in gl]; M = np.vstack(Ms); s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s < 1e-9)) + (M.shape[1] - len(s))
slotsD = [(1, True), (3, True), (3, False), (1, False)]  # psi3^+_i, (psi4^+)^3, (psi5)^3, psi0_j
def tensorC(C): return np.einsum('ij,a,b->iabj', C, [1], [1]).reshape(-1).astype(complex)
traceless = [X for X in gens if abs(np.trace(X)) < 1e-12] + [gens[0] - gens[4], gens[4] - gens[8]]
check("D1 tensor space 3b x L3(3b) x L3(3) x 3 has dim 9 (C_ij); u(3)- and su(3)-invariant subspaces both dim 1 (C = 1)",
      inv_dim(slotsD, gens) == 1 and inv_dim(slotsD, traceless) == 1)
w = np.exp(2j*np.pi/3); Cg = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3))
def centre_phase(slots):  # group element w*1 in U(3): Lambda^n(3) -> w^n, Lambda^n(3bar) -> w^-n
    return np.exp(sum((-n if c else n) for n, c in slots)*2j*np.pi/3)
ph = centre_phase(slotsD); Ac = action((2j*np.pi/3)*np.eye(3), slotsD)
check("D2 family centre w*1 acts on the norm-8 term as w^(-sum L) = 1 (generator check: action = 0); the q=1 turn IS this centre",
      abs(ph-1) < 1e-12 and np.allclose(Ac, 0))
cases = {"C=1": np.eye(3), "generic": Cg, "rank1 E11": np.diag([1., 0, 0]), "diag(1,2,3)": np.diag([1., 2, 3]), "diag(1,1,2)": np.diag([1., 1, 2])}
sd = {k: stab_dim(tensorC(C), slotsD) for k, C in cases.items()}
check("E1 commutant dims: C=1 -> 9 (u(3), contains SU(3)); generic -> 1; E11 -> 5; diag(1,2,3) -> 3; diag(1,1,2) -> 5",
      sd == {"C=1": 9, "generic": 1, "rank1 E11": 5, "diag(1,2,3)": 3, "diag(1,1,2)": 5}, str(sd))
check("E2 every non-invariant choice lies on a U(3) orbit of dim 9-stab >= 4: minimal term NOT unique",
      all(9 - v >= 4 for k, v in sd.items() if k != "C=1"), f"orbit dims={ {k: 9-v for k, v in sd.items()} }")
P = np.zeros((9, 6))
for i in range(3):
    for j in range(3): P[3*i+j, i] = 1; P[3*i+j, 3+j] = -1
check("E3 rephasing of the 9 monomials by the 6 free mode phases has rank 5: 4 phases of a generic C are not removable",
      np.linalg.matrix_rank(P) == 5)
print("== G. control: k = -q_mirror frame (turn imposes nothing) [T]")
slotsG = [(1, True), (2, False), (1, True), (2, True)]  # l1 one-site: psi3^+, psi4 psi4, psi5^+, psi0^+ psi0^+
check("G1 minimal term l1 (norm 6) one-site tensor space dim 81 has NO su(3) singlet; centre phase w^(-2) != 1",
      inv_dim(slotsG, traceless) == 0 and abs(centre_phase(slotsG) - np.conj(w)**2) < 1e-12)
Tr = rng.normal(size=81)
check("G2 a generic real choice there has discrete commutant (dim 0), but it is a choice from an 81-dim space",
      stab_dim(Tr.astype(complex), slotsG) == 0)
print("== H. a symmetric gapping SET at N_f = 3 (bosonic lattice) [T]")
def intker(A):
    M = [r[:] for r in A]; n = len(A[0]); U = [[int(i == j) for j in range(n)] for i in range(n)]; piv = 0
    for r in range(len(M)):
        while True:
            nz = [c for c in range(piv, n) if M[r][c] != 0]
            if not nz: break
            c0 = min(nz, key=lambda c: abs(M[r][c]))
            for X in (M, U):
                for row in X: row[piv], row[c0] = row[c0], row[piv]
            for c in range(piv+1, n):
                if M[r][c]:
                    qq = M[r][c] // M[r][piv]
                    for X in (M, U):
                        for row in X: row[c] -= qq*row[piv]
            if all(M[r][c] == 0 for c in range(piv+1, n)): break
        if piv < n and M[r][piv] != 0: piv += 1
    return [[U[i][c] for i in range(n)] for c in range(piv, n)]
R = [[F(-3, 5), F(-4, 5)], [F(4, 5), F(-3, 5)]]
def graph_lattice(U):
    nf = len(U); O = [[R[i//nf][j//nf]*U[i % nf][j % nf] for j in range(2*nf)] for i in range(2*nf)]; d = 15
    A = [[int(O[i][j]*d) for j in range(2*nf)] + [(-d if k == i else 0) for k in range(2*nf)] for i in range(2*nf)]
    return np.array(intker(A)), O
def props(B, nf):
    qa = np.concatenate([np.repeat(QA[:2], nf), np.repeat(QA[2:], nf)]); qb = np.concatenate([np.repeat(QB[:2], nf), np.repeat(QB[2:], nf)])
    k = np.concatenate([np.ones(2*nf), -np.ones(2*nf)])
    G = B @ np.diag(k) @ B.T
    return (np.all(B @ qa == 0) and np.all(B @ qb == 0) and np.all(G == 0) and np.linalg.matrix_rank(B) == 2*nf), sorted(set(int(x) % 3 for x in B.sum(1)))
B1, _ = graph_lattice([[F(1)]]); p1 = props(B1, 1)
check("H1 N_f=1: the unique Lagrangian lattice (graph of R) has a turn-charged element: no symmetric gapping", p1[0] and p1[1] != [0], f"charges={p1[1]}")
U3 = [[F(2, 3) - int(i == j) for j in range(3)] for i in range(3)]
B3, O3 = graph_lattice(U3); p3 = props(B3, 3)
check("H2 N_f=3: graph of R x (2J/3 - 1) is primitive, Lagrangian, A,B-neutral and turn-NEUTRAL (all elements)",
      p3[0] and p3[1] == [0], f"rank={len(B3)}, charges={p3[1]}")
Bi, _ = graph_lattice([[F(int(i == j)) for j in range(3)] for i in range(3)]); pi_ = props(Bi, 3)
check("H3 control: the family-diagonal N_f=3 lattice (U = 1) is turn-charged (spontaneous turn breaking)", pi_[1] != [0], f"charges={pi_[1]}")
fam = np.array([[sum(b[f*3+i] for f in range(4)) for i in range(3)] for b in B3])
Lsum = np.array([[sum(b[f*3+i] for i in range(3)) for f in range(4)] for b in B3])
check("H4 family-net charges of the set have rank 3: no continuous family torus survives (discrete residue)",
      np.linalg.matrix_rank(fam) == 3)
def perm_ok(p):
    Pm = np.zeros((12, 12))
    for f in range(4):
        for i in range(3): Pm[f*3+p[i], f*3+i] = 1
    X = B3 @ Pm.T; sol, res, *_ = np.linalg.lstsq(B3.T.astype(float), X.T.astype(float), rcond=None)
    return np.allclose(B3.T @ sol, X.T) and np.allclose(sol, np.round(sol))
check("H5 all 6 family permutations map the set's lattice to itself: S3 kept, so the three families are NOT distinguished (R1 fails)",
      all(perm_ok(p) for p in itertools.permutations(range(3))))
Ur = np.array(U3, float)
cm = np.array([(X @ Ur - Ur @ X).reshape(-1) for X in gens]).T; cm = np.vstack([cm.real, cm.imag])
dimc = int(np.sum(np.linalg.svd(cm, compute_uv=False) < 1e-9))
check("H6 the family map U = 2J/3 - 1 is real (antiunitary with X = 1 kept, R2 fails); its u(3) commutant is u(1)+u(2), dim 5",
      dimc == 5 and np.isrealobj(Ur) and np.allclose(Ur @ Ur.T, np.eye(3)))
m8_in = []
for i in range(3):
    for j in range(3):
        x = [int(k == i) for k in range(3)] + [1, 1, 1]; y = [-1, -1, -1] + [-int(k == j) for k in range(3)]
        m8_in.append([sum(O3[r][c]*x[c] for c in range(6)) for r in range(6)] == [F(t) for t in y])
check("H7 none of the 9 minimal (norm-8) monomials lies in this gapping lattice: the minimal term is not part of it", not any(m8_in))
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
