"""L3 check 1: lattice identities on the 09-14 integer stencils (exact integer arithmetic).
 (a) G S^T = 0
 (b) S K = -D G  (K = DeWitt c=1/2 kinetic map in canonical slots; D = backward divergence)
     => d/dt S(q) = -J D G(p) for H_N, for any lapse and shift.
 (c) polynomial kernels: S^T kills exactly affine functions (scalar charge: charge + dipole conserved => fracton);
     G^T kills exactly rigid motions a + w x r (vector charge: charge + angular moment => lineon).
 (d) S K with c != 1/2 is NOT in the row space of G (weak invariance fixes c = 1/2).
"""
import numpy as np, itertools, sys
from fractions import Fraction
import scipy.sparse as sp

L = int(sys.argv[1]) if len(sys.argv) > 1 else 5
V = L**3
def idx(x): return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
e = [np.array(v) for v in ((1,0,0),(0,1,0),(0,0,1))]
# slots: 0 xx,1 yy,2 zz,3 xy,4 yz,5 xz
off = {(0,1):3,(1,0):3,(1,2):4,(2,1):4,(0,2):5,(2,0):5}
def slot(x, a): return 6*idx(x) + a
sites = [np.array(x) for x in itertools.product(range(L), repeat=3)]

def build_G():
    rows, cols, vals = [], [], []
    for x in sites:
        for j in range(3):
            r = 3*idx(x) + j
            rows += [r, r]; cols += [slot(x+e[j], j), slot(x, j)]; vals += [1, -1]
            for i in range(3):
                if i == j: continue
                a = off[(i,j)]
                rows += [r, r]; cols += [slot(x, a), slot(x-e[i], a)]; vals += [1, -1]
    return sp.csr_matrix((vals,(rows,cols)), shape=(3*V, 6*V)).astype(np.int64)

def build_S():
    rows, cols, vals = [], [], []
    for x in sites:
        r = idx(x)
        for j in range(3):
            for i in range(3):
                if i == j: continue
                rows += [r]*3; cols += [slot(x+e[i], j), slot(x-e[i], j), slot(x, j)]; vals += [1,1,-2]
        for (i,j) in ((0,1),(1,2),(0,2)):
            a = off[(i,j)]
            rows += [r]*4
            cols += [slot(x,a), slot(x-e[i],a), slot(x-e[j],a), slot(x-e[i]-e[j],a)]
            vals += [-1, 1, 1, -1]
    return sp.csr_matrix((vals,(rows,cols)), shape=(V, 6*V)).astype(np.int64)

def build_D():  # backward divergence edges -> sites
    rows, cols, vals = [], [], []
    for x in sites:
        for j in range(3):
            rows += [idx(x), idx(x)]; cols += [3*idx(x)+j, 3*idx(x-e[j])+j]; vals += [1, -1]
    return sp.csr_matrix((vals,(rows,cols)), shape=(V, 3*V)).astype(np.int64)

def build_K2(c2num, c2den):
    """2*K for kinetic J/2[E:E - c (trE)^2], c = c2num/c2den/2 ... we pass 2c as fraction; integer scaled by c2den."""
    # dH/dp_ii = J(p_ii - c trp); dH/dp_ij = 2J p_ij.  Return c2den*K as integers (c = c2num/(2*c2den)*... )
    rows, cols, vals = [], [], []
    for x in sites:
        b = 6*idx(x)
        for i in range(3):
            for k in range(3):
                v = (c2den if i == k else 0)*2 - c2num   # 2*c2den*(delta - c) with c = c2num/(2 c2den)
                rows.append(b+i); cols.append(b+k); vals.append(v)
        for a in (3,4,5):
            rows.append(b+a); cols.append(b+a); vals.append(4*c2den)  # 2*c2den*2
    return sp.csr_matrix((vals,(rows,cols)), shape=(6*V, 6*V)).astype(np.int64)

G, S, D = build_G(), build_S(), build_D()
print(f"L={L}: G {G.shape}, S {S.shape}")
GS = (G @ S.T); print("(a) max|G S^T| =", abs(GS).max() if GS.nnz else 0)
# c = 1/2: c2num/(2 c2den) = 1/2 -> c2num = c2den = 1 ; K2 = 2K
K2 = build_K2(1, 1)
lhs = S @ K2            # = 2 S K
rhs = -2 * (D @ G)      # = -2 D G
diff = (lhs - rhs); print("(b) max|S K + D G| (c=1/2, exact integers) =", abs(diff).max() if diff.nnz else 0)

# (d) c != 1/2 : test whether rows of S K lie in row space of G (rank test, dense, small L)
if L <= 4:
    Gd = G.toarray().astype(float)
    rG = np.linalg.matrix_rank(Gd)
    for (num, den, lab) in ((1,1,"1/2"), (2,3,"1/3"), (2,1,"1"), (0,1,"0")):
        SK = (S @ build_K2(num, den)).toarray().astype(float)
        r = np.linalg.matrix_rank(np.vstack([Gd, SK]))
        print(f"(d) c={lab}: rank[G;SK]-rank G = {r - rG}  (0 => S K = L G, weakly invariant)")

# (c) polynomial kernels on infinite lattice: evaluate transposes on monomials, degree <= 3
def monos(deg):
    return [m for m in itertools.product(range(deg+1), repeat=3) if sum(m) <= deg]
def poly_kernel_scalar(deg):
    ms = monos(deg)
    # f(x) = sum c_m x^m on sites; (S^T f)(slot) = sum_x S[x,slot] f(x); evaluate at interior slots of a big box (no wrap)
    R = 6; pts = [np.array(x) for x in itertools.product(range(-R, R+1), repeat=3)]
    # build S^T f directly from stencil: (S^T f)_slot = sum over sites x of coefficient
    A = []
    for y in [np.array(v) for v in itertools.product(range(-2,3), repeat=3)]:
        for a in range(6):
            row = np.zeros(len(ms))
            # contributions: diag a=j: q_jj(y) appears in (Sq)(x) for x = y-e_i, y+e_i (coef 1) and x=y (coef -2), for each i != j
            if a < 3:
                j = a
                for i in range(3):
                    if i == j: continue
                    for (x, cf) in ((y-e[i],1),(y+e[i],1),(y,-2)):
                        row += cf*np.array([np.prod(np.array(x, float)**np.array(m)) for m in ms])
            else:
                (i,j) = {3:(0,1),4:(1,2),5:(0,2)}[a]
                # q_a(y) appears in (Sq)(x) with x=y (-1), x=y+e_i (+1), x=y+e_j (+1), x=y+e_i+e_j (-1)
                for (x, cf) in ((y,-1),(y+e[i],1),(y+e[j],1),(y+e[i]+e[j],-1)):
                    row += cf*np.array([np.prod(np.array(x, float)**np.array(m)) for m in ms])
            A.append(row)
    A = np.array(A); s = np.linalg.svd(A, compute_uv=False)
    null = len(ms) - np.sum(s > 1e-9*s[0])
    return len(ms), null
def poly_kernel_vector(deg):
    ms = monos(deg); n = len(ms)
    A = []
    for y in [np.array(v) for v in itertools.product(range(-2,3), repeat=3)]:
        for a in range(6):
            row = np.zeros(3*n)
            def add(j, x, cf):
                row[j*n:(j+1)*n] += cf*np.array([np.prod(np.array(x, float)**np.array(m)) for m in ms])
            if a < 3:
                j = a  # p_jj(y) enters (Gp)_j(x) at x = y-e_j (+1) and x = y (-1)
                add(j, y-e[j], 1); add(j, y, -1)
            else:
                (i,j) = {3:(0,1),4:(1,2),5:(0,2)}[a]
                # p_ij(y) enters (Gp)_j(x) at x=y (+1), x=y+e_i (-1); and (Gp)_i(x) at x=y (+1), x=y+e_j (-1)
                add(j, y, 1); add(j, y+e[i], -1); add(i, y, 1); add(i, y+e[j], -1)
            A.append(row)
    A = np.array(A); s = np.linalg.svd(A, compute_uv=False)
    null = 3*n - np.sum(s > 1e-9*s[0])
    return 3*n, null
for deg in (1,2,3):
    print(f"(c) deg<={deg}: scalar S^T poly kernel dim = {poly_kernel_scalar(deg)[1]} (affine = 4); "
          f"vector G^T poly kernel dim = {poly_kernel_vector(deg)[1]} (rigid motions = 6)")
