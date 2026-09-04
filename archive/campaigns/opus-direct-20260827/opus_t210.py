"""
T210 - RECORD CONSISTENCY: does requiring the admissibility conditionals to come
from an actual joint distribution over permanent record configurations fix the
FORM of the rule?

This is the TOE scorecard's named Root A attack ("uniqueness of the FORM
(weight/Born functional) from NN-determination + Record consistency, as native
new theorems").  The packet has never used global consistency: R104's
"convex-consistency" is a LOCAL affineness premise about the rule's input, a
different condition.

CHAIN UNDER TEST
  1. Record permanence + one-per-site  => a configuration is a random field.
  2. Admissibility: each site's distribution is determined by its neighbours
     => the field is MARKOV on the lattice graph.
  3. Z^3 nearest-neighbour adjacency is TRIANGLE-FREE => cliques are edges.
  4. Positivity + Hammersley-Clifford => mu = prod over EDGES of phi(v_x,v_y).
  5. Convex-consistency => phi affine in each argument.
  6. Cubic covariance + symmetry => phi = a + lambda (v.v').
  => rule  P(v_x | ne) ∝ prod_{y~x} (1 + lambda v_x.v_y)     [PRODUCT form]

CONTROL THAT MUST FAIL: the packet's linear rule is affine in the SUM,
  P(v_x | ne) ∝ 1 + lambda v_x.(sum_y v_y)                   [SUM form]
If the chain is right, the SUM form is NOT the conditional of any joint field.

Everything is re-proven here; nothing is imported as authority.
"""
import numpy as np, itertools

# cubic-covariant finite menu of pure states (records are null => |v| = 1)
MENU = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], dtype=float)
M = len(MENU)

def cubic_rotations():
    Rs = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product([1,-1], repeat=3):
            R = np.zeros((3,3))
            for i,p in enumerate(perm): R[i,p] = sg[i]
            if abs(np.linalg.det(R) - 1) < 1e-12: Rs.append(R)
    return Rs
ROT = cubic_rotations()
print(f"proper cubic rotations: {len(ROT)}  (expect 24)")

# ---- step 3: is Z^3 nearest-neighbour adjacency triangle-free? --------------
nb = [np.array(d) for d in
      [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
tri = 0
for a, b in itertools.combinations(nb, 2):
    if np.sum(np.abs(a - b)) == 1: tri += 1     # would-be triangle with origin
print(f"triangles through a site in Z^3 NN adjacency: {tri}  "
      f"=> cliques are {'edges only' if tri == 0 else 'LARGER'}")

# ---- step 5+6: classify symmetric, covariant, multi-affine edge potentials --
# multi-affine basis on MENU x MENU: {1, v_i} (x) {1, v'_j}  -> 16 functions
def basis_funcs():
    B = []
    for i in range(4):
        for j in range(4):
            F = np.zeros((M, M))
            for a in range(M):
                for b in range(M):
                    ca = 1.0 if i == 0 else MENU[a][i-1]
                    cb = 1.0 if j == 0 else MENU[b][j-1]
                    F[a, b] = ca*cb
            B.append(F)
    return B
B = basis_funcs()
Bm = np.array([f.ravel() for f in B])
print(f"multi-affine basis: {len(B)} functions, rank {np.linalg.matrix_rank(Bm)}")

perm_of = {}
for r, R in enumerate(ROT):
    p = []
    for a in range(M):
        w = R @ MENU[a]
        p.append(int(np.argmin(np.linalg.norm(MENU - w, axis=1))))
    perm_of[r] = np.array(p)

# constraints on coefficients c (len 16): symmetry + covariance
rows = []
for a in range(M):
    for b in range(M):
        # symmetry  phi(a,b) - phi(b,a) = 0
        rows.append([B[k][a, b] - B[k][b, a] for k in range(len(B))])
        for r in range(len(ROT)):
            pa, pb = perm_of[r][a], perm_of[r][b]
            rows.append([B[k][pa, pb] - B[k][a, b] for k in range(len(B))])
Arow = np.array(rows)
U, sv, Vt = np.linalg.svd(Arow, full_matrices=False)
tol = max(Arow.shape)*np.finfo(float).eps*sv.max()
k = int(np.sum(sv <= tol))
print(f"\ndim of symmetric + cubic-covariant + multi-affine potentials = {k}")
sol = [Vt[len(Vt)-k+i] for i in range(k)]
for i, c in enumerate(sol):
    P = sum(c[j]*B[j] for j in range(len(B)))
    dot = np.array([[MENU[a] @ MENU[b] for b in range(M)] for a in range(M)])
    fit = np.linalg.lstsq(np.vstack([np.ones(M*M), dot.ravel()]).T, P.ravel(), rcond=None)
    resid = np.max(np.abs(np.vstack([np.ones(M*M), dot.ravel()]).T @ fit[0] - P.ravel()))
    print(f"  basis {i}: fits  a*1 + lam*(v.v')  with a={fit[0][0]:+.4f} "
          f"lam={fit[0][1]:+.4f}, residual {resid:.2e}")
print("  => the potential is forced to  phi = a + lambda (v.v').")

# ============================================================================
# COMPATIBILITY: does a joint field exist with the given conditionals?
# For every site i and every configuration v:
#     mu(v) = P(v_i | ne(i)) * sum_{v_i'} mu(v_i', v_{-i})            [linear]
# A joint exists iff this linear system has a nontrivial NONNEGATIVE solution.
# ============================================================================
DOT = MENU @ MENU.T

def compat(adj, cond, nsite, label):
    cfgs = list(itertools.product(range(M), repeat=nsite))
    idx = {c: i for i, c in enumerate(cfgs)}
    rows = []
    for i in range(nsite):
        for c in cfgs:
            r = np.zeros(len(cfgs))
            r[idx[c]] += 1.0
            p = cond(i, c, adj)
            for s in range(M):
                cc = list(c); cc[i] = s
                r[idx[tuple(cc)]] -= p[c[i]]
            rows.append(r)
    A = np.array(rows)
    U, sv, Vt = np.linalg.svd(A, full_matrices=False)
    tol = max(A.shape)*np.finfo(float).eps*sv.max()
    k = int(np.sum(sv <= tol))
    out = f"  {label:34s} nullspace dim = {k}"
    if k >= 1:
        vecs = [Vt[len(Vt)-k+i] for i in range(k)]
        v = vecs[0]
        if v.max() < 0: v = -v
        pos = v.min() > -1e-10*abs(v).max()
        out += f"   min/max = {v.min()/abs(v).max():+.2e}  {'POSITIVE -> joint EXISTS' if pos else 'not positive'}"
    else:
        out += f"   smallest sv = {sv[-1]:.3e}  -> NO joint field"
    print(out)
    return k

def make_cond(kind, lam):
    def cond(i, c, adj):
        ne = adj[i]
        w = np.zeros(M)
        for s in range(M):
            if kind == "product":
                w[s] = np.prod([1 + lam*DOT[s, c[j]] for j in ne])
            elif kind == "sum":
                w[s] = 1 + lam*sum(DOT[s, c[j]] for j in ne)
            elif kind == "exp":
                w[s] = np.exp(lam*sum(DOT[s, c[j]] for j in ne))
        return w/np.sum(w)
    return cond

PATH3 = {0: [1], 1: [0, 2], 2: [1]}
STAR4 = {0: [1, 2, 3], 1: [0], 2: [0], 3: [0]}

print("\n=== does a joint field exist? (3-site path 1-2-3) ===")
for lam in (0.0, 0.1, 0.3, 0.6):
    print(f" lambda = {lam}")
    for kind in ("product", "sum", "exp"):
        compat(PATH3, make_cond(kind, lam), 3, f"{kind} form")

print("\n=== same, on a 4-site star (centre has 3 neighbours) ===")
for lam in (0.1, 0.3):
    print(f" lambda = {lam}")
    for kind in ("product", "sum"):
        compat(STAR4, make_cond(kind, lam), 4, f"{kind} form")

print("\n=== CONTROL: recover the known joint for the product form ===")
lam = 0.3
cfgs = list(itertools.product(range(M), repeat=3))
mu = np.array([(1+lam*DOT[c[0], c[1]])*(1+lam*DOT[c[1], c[2]]) for c in cfgs])
mu /= mu.sum()
cond = make_cond("product", lam)
err = 0.0
for i in range(3):
    for j, c in enumerate(cfgs):
        marg = sum(mu[cfgs.index(tuple(list(c)[:i]+[s]+list(c)[i+1:]))] for s in range(M))
        err = max(err, abs(mu[j] - cond(i, c, PATH3)[c[i]]*marg))
print(f"  explicit joint  mu ∝ (1+lam v1.v2)(1+lam v2.v3)  reproduces its own")
print(f"  conditionals to {err:.2e}  -> the solver's positive nullspace is that joint.")

print("\n=== how badly does the SUM form fail?  (Brook path-independence) ===")
print("  lambda   best relative residual of any normalised candidate joint")
for lam in (0.05, 0.1, 0.2, 0.4):
    cond = make_cond("sum", lam)
    rows = []
    for i in range(3):
        for c in cfgs:
            r = np.zeros(len(cfgs)); r[cfgs.index(c)] += 1.0
            p = cond(i, c, PATH3)
            for s in range(M):
                cc = list(c); cc[i] = s
                r[cfgs.index(tuple(cc))] -= p[s]
            rows.append(r)
    A = np.array(rows)
    sv = np.linalg.svd(A, compute_uv=False)
    print(f"   {lam:5.2f}   smallest singular value {sv[-1]:.4e}   "
          f"(ratio to largest {sv[-1]/sv[0]:.2e})")
