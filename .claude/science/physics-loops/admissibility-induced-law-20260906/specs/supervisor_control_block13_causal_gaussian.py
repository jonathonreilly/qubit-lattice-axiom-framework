"""Control, block 13 (supervisor): the causal Gaussian formation law in level time.
(1) exact return probabilities P_n of the difference of two lazy directed walks (steps (0,0),(1,0),(0,1)), n <= 200, vs bounds 1/(36n), 2/n;
(2) half-space variance series at g = 1 (log growth vs harmonic numbers) and g = 1/2 (bounded);
(3) 2D: C(2n,n)/4^n bounds; (4) transverse-torus check of the path-count kernel against the level recursion;
(5) symbol expansion at g = 1 (level direction quadratic, transverse quartic) and the block-09 graph terms;
(6) grid sums of 1/|1-a|^2 (formation) vs 1/(2 sum(1-cos)) (static) on N^3 grids; (7) Taylor expansion of log f(s.a) at the aligned point."""
from fractions import Fraction as F
from math import comb, log
import sympy as sp
import time

# (1) P_n exact via integer walk counts on the transverse plane
t0 = time.time()
N = 200
counts = {(0, 0): 1}
P = [F(1)]
for n in range(1, N + 1):
    new = {}
    for (a, b), c in counts.items():
        for da, db in ((0, 0), (1, 0), (0, 1)):
            new[(a + da, b + db)] = new.get((a + da, b + db), 0) + c
    counts = new
    R = sum(c * c for c in counts.values())
    P.append(F(R, 9 ** n))
print(f"P_n computed to n={N} in {time.time()-t0:.1f}s")
ok_lo = all(P[n] >= F(1, 36 * n) for n in range(1, N + 1))
ok_hi = all(P[n] <= F(2, n) for n in range(1, N + 1))
print("bounds 1/(36n) <= P_n <= 2/n for 1<=n<=200:", ok_lo, ok_hi)
print("n*P_n at n=10,50,100,200:", [float(n * P[n]) for n in (10, 50, 100, 200)], " (3*sqrt(3)/(2*pi) =", 3 * 3 ** 0.5 / (2 * 3.141592653589793), ")")
# (2) variance series
for g in (F(1), F(1, 2)):
    V = [F(0)]
    for t in range(1, N + 1):
        V.append(V[-1] + g ** (2 * (t - 1)) * P[t - 1])
    H = [F(0)]
    for t in range(1, N + 1):
        H.append(H[-1] + F(1, t))
    if g == 1:
        print("g=1: Var_t/sigma^2 at t=10,50,100,200:", [float(V[t]) for t in (10, 50, 100, 200)], "; Var_t/H_t:", [float(V[t] / H[t]) for t in (10, 50, 100, 200)])
        print("   c1*H_t <= Var_t with c1=1/36:", all(V[t] >= H[t] / 36 for t in range(1, N + 1)), "; Var_t <= 1 + 2*H_{t-1}:", all(V[t] <= 1 + 2 * H[t - 1] for t in range(1, N + 1)))
    else:
        print("g=1/2: Var_t/sigma^2 at t=10,50,200:", [float(V[t]) for t in (10, 50, 200)], "; bound 1/(1-g^2)=4/3; monotone bounded:", all(V[t] <= F(4, 3) for t in range(N + 1)))
# (3) 2D
ok2 = all(F(comb(2 * n, n), 4 ** n) >= F(1, 2) / sp.sqrt(n) for n in range(1, 5))  # placeholder float-free? use squares
ok2lo = all(F(comb(2 * n, n), 4 ** n) ** 2 >= F(1, 4 * n) for n in range(1, 401))
ok2hi = all(F(comb(2 * n, n), 4 ** n) ** 2 <= F(3, 4 * (2 * n + 1)) for n in range(1, 401))
print("2D: 1/(4n) <= (C(2n,n)/4^n)^2 <= 3/(4(2n+1)) for n<=400:", ok2lo, ok2hi)
# (4) transverse torus check: W x W torus, T levels, g=1 (w=1/3), sigma^2 = 1; covariance recursion vs path-count kernel with images
W, T = 5, 6
w = F(1, 3)
import itertools
sites = [(a, b) for a in range(W) for b in range(W)]
idx = {s: i for i, s in enumerate(sites)}
def A_matrix():
    A = [[F(0)] * (W * W) for _ in range(W * W)]
    for (a, b) in sites:
        for (da, db) in ((0, 0), (1, 0), (0, 1)):
            A[idx[(a, b)]][idx[((a - da) % W, (b - db) % W)]] += w
    return A
A = A_matrix()
# covariance recursion: C_t = A C_{t-1} A^T + I, C_0 = 0 (boundary level supplied, no fluctuation)
n = W * W
C = [[F(0)] * n for _ in range(n)]
def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
AT = [[A[j][i] for j in range(n)] for i in range(n)]
Cs = [C]
for t in range(1, T + 1):
    C = matmul(matmul(A, C), AT)
    for i in range(n):
        C[i][i] += 1
    Cs.append(C)
# path-count kernel: G_m(y, z) = w^m * #monotone paths of length m from z to y on the torus (with images) = (A^m)[y][z]
def var_from_paths(t, y):
    # Var(v_t(y)) = sum_{m=0}^{t-1} sum_z G_m(y,z)^2
    Am = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    tot = F(0)
    for m in range(t):
        tot += sum(Am[idx[y]][j] ** 2 for j in range(n))
        Am = matmul(Am, A)
    return tot
print("torus 5x5, 6 levels: Var from recursion vs path kernel at level 6, site (2,3):", Cs[6][idx[(2, 3)]][idx[(2, 3)]], var_from_paths(6, (2, 3)), Cs[6][idx[(2, 3)]][idx[(2, 3)]] == var_from_paths(6, (2, 3)))
# (5) symbol
k1, k2, k3, K, q1, q2, eps = sp.symbols("k1 k2 k3 K q1 q2 epsilon", real=True)
a = sp.Rational(1, 3) * (sp.exp(-sp.I * k1) + sp.exp(-sp.I * k2) + sp.exp(-sp.I * k3))
symb = sp.expand(sp.simplify((1 - a) * (1 - sp.conjugate(a))))
symb_real = sp.simplify(sp.expand_complex(symb).rewrite(sp.cos))
print("symbol |1-a|^2 =", sp.simplify(sp.trigsimp(symb_real)))
# transverse plane: k = (u, v, -u-v) => K=0 ; expand in eps
sub = {k1: eps * q1, k2: eps * q2, k3: -eps * (q1 + q2)}
ser = sp.series(symb_real.subs(sub), eps, 0, 6).removeO()
print("transverse expansion (K=0):", sp.simplify(sp.expand(ser)))
# level direction k = (u,u,u)
ser2 = sp.series(symb_real.subs({k1: eps, k2: eps, k3: eps}), eps, 0, 4).removeO()
print("level-direction expansion k=(e,e,e):", sp.simplify(ser2), " (K^2/9 with K=3e gives e^2)")
# (6) grid sums (exact rationals impossible with cos; use high-precision floats here in the control only)
import math
for Ngrid in (8, 16, 32):
    sf = ss = 0.0
    for i in range(Ngrid):
        for j in range(Ngrid):
            for l in range(Ngrid):
                if i == j == l == 0:
                    continue
                kk = (2 * math.pi * i / Ngrid, 2 * math.pi * j / Ngrid, 2 * math.pi * l / Ngrid)
                re = 1 - sum(math.cos(x) for x in kk) / 3
                im = sum(math.sin(x) for x in kk) / 3
                sf += 1 / (re * re + im * im)
                ss += 1 / (2 * sum(1 - math.cos(x) for x in kk))
    print(f"grid N={Ngrid}: mean 1/|1-a|^2 = {sf / Ngrid**3:.4f} ; mean 1/(2 sum(1-cos)) = {ss / Ngrid**3:.4f}")
# (7) Taylor expansion of log f(s.a) at the aligned point (exponential coordinates on S^2 near the north pole)
th1, th2, ph1, ph2 = sp.symbols("theta1 theta2 phi1 phi2", real=True)
def unit(u1, u2):
    r = sp.sqrt(u1 ** 2 + u2 ** 2)
    return sp.Matrix([sp.sin(r) * u1 / r, sp.sin(r) * u2 / r, sp.cos(r)])
s_vec = unit(eps * th1, eps * th2)
a_vec = unit(eps * ph1, eps * ph2)
dot = sp.simplify((s_vec.T * a_vec)[0])
for name, f in (("Born (1+t)/2", lambda t: (1 + t) / 2), ("exponential e^{beta t}", lambda t: sp.exp(sp.Symbol("beta") * t))):
    expr = sp.log(f(dot))
    ser = sp.series(expr, eps, 0, 3).removeO()
    print(f"log f(s.a) for f = {name}:", sp.simplify(sp.expand(ser)))
