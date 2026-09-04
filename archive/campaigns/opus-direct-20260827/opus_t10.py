"""T10 — THE 3D CURVATURE POTENTIAL (the induced-gravity test).
3D conformal g = lam^2 I_3, lam = 1 + eps*s(x) depending on ONE coordinate.
Linearised 3D scalar curvature: R = -4 eps Lap(s).
Extract the on-site potential of -K_hat^2 in the orthonormal frame and fit
a*prof + b*Lap(prof).  A nonzero b means a curvature potential in 3D, where
integral sqrt(g) R is NOT topological -> an induced Einstein-Hilbert term."""
import sympy as sp
from itertools import combinations
d = 3
BAS = []
for k in range(d+1): BAS += [tuple(c) for c in combinations(range(d), k)]
IDX = {b: i for i, b in enumerate(BAS)}; F = len(BAS)
eps_ = sp.Symbol("epsilon")
def lin(e): return sp.expand(sp.series(sp.expand(e), eps_, 0, 2).removeO())
def epsm(a):
    M = sp.zeros(F, F)
    for Sx in BAS:
        if a in Sx: continue
        T = tuple(sorted(Sx + (a,)))
        M[IDX[T], IDX[Sx]] = (-1) ** sum(1 for i in Sx if i < a)
    return M
def iota(a, gi):
    M = sp.zeros(F, F)
    for Sx in BAS:
        for pos, i in enumerate(Sx):
            T = tuple(x for x in Sx if x != i)
            M[IDX[T], IDX[Sx]] += (-1) ** pos * gi[a, i]
    return M
Lx, Ly, Lz = 4, 3, 3
sites = [(x, y, z) for x in range(Lx) for y in range(Ly) for z in range(Lz)]
sid = {s: i for i, s in enumerate(sites)}; N = len(sites)
def wrap(s): return (s[0] % Lx, s[1] % Ly, s[2] % Lz)
prof = {s: sp.Rational(((2*s[0]*s[0] + 1) % 5) - 2, 4) for s in sites}   # depends on x only
lam = {s: 1 + eps_*prof[s] for s in sites}
deg = [len(b) for b in BAS]
def Dh_diag(s):   # D = V * Lambda(g^-1) with V = det^(1/2) = lam^3 ; degree k: lam^(3-2k)
    return [lin(lam[s]**sp.Rational(3-2*k, 2)) for k in deg]
def Gam(s, a):
    gi = sp.eye(d) * lin(1/lam[s]**2)
    return sp.Matrix(F, F, lambda p, q: lin((epsm(a) + iota(a, gi))[p, q]))
def U(s, r):
    hs, hr = Dh_diag(s), Dh_diag(r)
    return sp.diag(*[lin(sp.sqrt(sp.together(lam[r]**sp.Rational(3-2*k,1)/lam[s]**sp.Rational(3-2*k,1)))**sp.Rational(1,1)) if False else lin((lam[r]/lam[s])**(3-2*k)/1) for k in deg])
# transport must satisfy U^T D_s U = D_r  with D diagonal: u_k^2 * D_s,k = D_r,k
def Utrans(s, r):
    return sp.diag(*[lin(sp.sqrt((lam[r]/lam[s])**(3-2*k))) for k in deg])
def Lam(s, r, a):
    Us = Utrans(s, r)
    return sp.Matrix(F, F, lambda p, q: lin((sp.Rational(1,2)*(Gam(s,a)*Us + Us*Gam(r,a)))[p, q]))
K = sp.zeros(F*N, F*N)
for s in sites:
    for a in range(d):
        e = [0,0,0]; e[a] = 1
        rp = wrap((s[0]+e[0], s[1]+e[1], s[2]+e[2])); rm = wrap((s[0]-e[0], s[1]-e[1], s[2]-e[2]))
        for sgn, r in ((+1, rp), (-1, rm)):
            blk = Lam(s, r, a); i, j = sid[s]*F, sid[r]*F
            for p in range(F):
                for q in range(F): K[i+p, j+q] += sgn*sp.Rational(1,2)*blk[p, q]
K = sp.Matrix(F*N, F*N, lambda i, j: lin(K[i, j]))
Dh = sp.zeros(F*N, F*N); Dhi = sp.zeros(F*N, F*N)
for s in sites:
    h = [lin(sp.sqrt(lam[s]**(3-2*k))) for k in deg]
    for k in range(F):
        Dh[sid[s]*F+k, sid[s]*F+k] = h[k]; Dhi[sid[s]*F+k, sid[s]*F+k] = lin(1/h[k])
Kh = sp.Matrix(F*N, F*N, lambda i, j: lin((Dh*K*Dhi)[i, j]))
print(f"3D: K_hat antisymmetric: {sp.Matrix(F*N, F*N, lambda i,j: lin((Kh+Kh.T)[i,j])).is_zero_matrix}", flush=True)
M = sp.Matrix(F*N, F*N, lambda i, j: lin(-sum(Kh[i,k]*Kh[k,j] for k in range(F*N))))
def lap(s):
    tot = -6*prof[s]
    for a in range(d):
        e = [0,0,0]; e[a] = 1
        tot += prof[wrap((s[0]+e[0],s[1]+e[1],s[2]+e[2]))] + prof[wrap((s[0]-e[0],s[1]-e[1],s[2]-e[2]))]
    return tot
degind = all(sp.expand(M[sid[s]*F+k, sid[s]*F+k] - M[sid[s]*F, sid[s]*F]) == 0 for s in sites for k in range(F))
print(f"3D: on-site term degree-independent: {degind}", flush=True)
a_, b_ = sp.symbols("a_ b_")
rows = [(s, sp.expand(sp.diff(M[sid[s]*F, sid[s]*F], eps_))) for s in sites]
(s1,c1),(s2,c2) = rows[0], rows[9]
sol = sp.solve([sp.Eq(a_*prof[s1]+b_*lap(s1), c1), sp.Eq(a_*prof[s2]+b_*lap(s2), c2)], [a_,b_], dict=True)
print(f"3D fit: {sol}", flush=True)
if sol:
    A, Bc = sol[0][a_], sol[0][b_]
    ok = all(sp.expand(c - (A*prof[s]+Bc*lap(s))) == 0 for s,c in rows)
    print(f"3D LAW = ({A})*prof + ({Bc})*Lap(prof); holds at all {len(rows)} sites: {ok}", flush=True)
    print(f"   with R_lin = -4*eps*Lap  ->  curvature coefficient = R * {sp.nsimplify(-Bc/4)}", flush=True)
