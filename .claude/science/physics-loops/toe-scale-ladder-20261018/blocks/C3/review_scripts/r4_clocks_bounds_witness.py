"""R4: Theorem D exact (own enumeration, incl. Z^2 path shapes), B1 Stirling
inequality, B2 term inequality, Theorem F arithmetic and O_h stabiliser,
09-22 kappa values, and an exact exchangeable-with-ties clock whose record
law has covariance-LRO (tests the necessity-corollary wording)."""
import itertools, math
from fractions import Fraction as F
from rv_common import Checks
C = Checks("r4")

def p_decreasing(path, K):
    # exact P(T_{y0} > ... > T_{yn}) for T_y = max_{k in K} zeta_{y+k}, zeta iid continuous
    cells = sorted({(y[0]+k[0], y[1]+k[1]) for y in path for k in K})
    ix = {c: i for i, c in enumerate(cells)}
    win = [[ix[(y[0]+k[0], y[1]+k[1])] for k in K] for y in path]
    good = tot = 0
    for perm in itertools.permutations(range(len(cells))):
        T = [max(perm[i] for i in w) for w in win]
        tot += 1
        good += all(T[i] > T[i+1] for i in range(len(T)-1))
    return F(good, tot)

K1 = [(0, 0), (1, 0)]
for n in range(1, 6):
    path = [(i, 0) for i in range(n+1)]
    p = p_decreasing(path, K1)
    C.ok(f"D, Z, T=max(z_x,z_x+1), right path n={n}: P(decr)={p} == 2/(n+2)! and <= 1/ceil((n+1)/3)!", p == F(2, math.factorial(n+2)) and p <= F(1, math.factorial(-(-(n+1)//3))))
    pathL = [(-i, 0) for i in range(n+1)]
    C.ok(f"D, Z, left path n={n}: P(decr) == 2/(n+2)!", p_decreasing(pathL, K1) == F(2, math.factorial(n+2)))
# Z^2 shapes, K = {0, e1, e2}: |K-K| = 7
K2 = [(0, 0), (1, 0), (0, 1)]
KK = {(a[0]-b[0], a[1]-b[1]) for a in K2 for b in K2}
b = len(KK)
shapes = {"L": [(0, 0), (1, 0), (1, 1)], "zig": [(0, 0), (1, 0), (1, 1), (2, 1)], "vert": [(0, 0), (0, 1), (0, 2)]}
for nm, pth in shapes.items():
    n = len(pth)-1
    p = p_decreasing(pth, K2)
    C.ok(f"D, Z^2 K={{0,e1,e2}} (b={b}) shape {nm} n={n}: P(decr)={p} <= 1/ceil((n+1)/b)! = {F(1, math.factorial(-(-(n+1)//b)))}", p <= F(1, math.factorial(-(-(n+1)//b))))

# B1 Stirling form: a(ceil(r/2)-1) <= (D/(D-1)) (2e(D-1)/r)^ceil(r/2) for r >= 2e(D-1)
def a(k, D):
    return 1.0 if k <= 0 else D*(D-1)**(k-1)/math.factorial(k+1)
okB1 = True
for D in (2, 4, 6, 8):
    for r in range(math.ceil(2*math.e*(D-1)), 160):
        q = -(-r//2)
        if a(q-1, D) > (D/(D-1))*(2*math.e*(D-1)/r)**q*(1+1e-12): okB1 = False
C.ok("B1 Stirling form holds for D in {2,4,6,8}, 2e(D-1) <= r < 160", okB1)
# B2 term: a(k1-1)a(k2-1) <= D^2 (2(D-1))^s s/s!, all k1,k2>=0, k1+k2=s
okB2 = True
for D in (2, 4, 6):
    for s in range(1, 60):
        for k1 in range(0, s+1):
            lhs = a(k1-1, D)*a(s-k1-1, D)
            if lhs > D**2*(2*(D-1))**s*s/math.factorial(s)*(1+1e-12): okB2 = False
C.ok("B2 product inequality a(k1-1)a(k2-1) <= D^2(2(D-1))^s s/s! incl. boundary cases", okB2)

# F: O_h stabiliser and covariance arithmetic
Oh = [M for perm in itertools.permutations(range(3)) for sg in itertools.product((1, -1), repeat=3)
      for M in [tuple(tuple(sg[i] if j == perm[i] else 0 for j in range(3)) for i in range(3))]]
app = lambda M, v: tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))
e1 = (1, 0, 0)
stab = [M for M in Oh if app(M, e1) == e1]
C.ok(f"|O_h| = {len(Oh)}, stabiliser of e1 has {len(stab)} elements (8/48 = 1/6)", len(Oh) == 48 and len(stab) == 8)
diag = {app(M, (1, 1, 1)) for M in Oh}
C.ok("g(1,1,1) uniform on the 8 body diagonals", len(diag) == 8)
# given w=g(1,1,1), the phase g e1 satisfies <g e1, w> = 1
C.ok("in W the phase g e1 always has <g e1, w> = +1 (phase coupled to clock direction)", all(sum(x*y for x, y in zip(app(M, e1), app(M, (1, 1, 1)))) == 1 for M in Oh))
covF = F(1, 6)*(1 - 6*F(1, 10**5)) - F(1, 36)
C.ok(f"F bound (1/6)(1-6e-5)-1/36 = {covF} = 124991/900000 > 0.1388", covF == F(124991, 900000) and covF > F(1388, 10000))
# 09-22 rate laws, k in 0..6 formed neighbours on Z^3
for nm, f in (("1+k", lambda k: F(1+k)), ("(1+k)^2", lambda k: F((1+k)**2)), ("1/(1+k)", lambda k: F(1, 1+k))):
    vals = [f(k) for k in range(7)]
    C.ok(f"kappa({nm}) on Z^3 = {max(vals)/min(vals)}", max(vals)/min(vals) in (7, 49))

# Exchangeable-with-ties clock: w.p. 1/2 all T_x = 1/2 (one atom), w.p. 1/2 iid U[0,1].
# Exchangeable (mixture of iid), O_h- and translation-covariant in law, Cov(T_x,T_y)=0.
# Rule on Z: r(.|empty)=delta_0, any strictly earlier neighbour -> 1.
# Tie phase: xi == 0.  iid phase: xi_x = 1 iff some neighbour earlier.
def iid_phase_joint(dist_):
    # exact E[xi_0 xi_x] in the iid phase by enumerating orders on the needed sites
    sites = sorted({-1, 0, 1, dist_-1, dist_, dist_+1})
    ix = {s: i for i, s in enumerate(sites)}
    good = tot = 0
    for perm in itertools.permutations(range(len(sites))):
        x0 = perm[ix[-1]] < perm[ix[0]] or perm[ix[1]] < perm[ix[0]]
        xx = perm[ix[dist_-1]] < perm[ix[dist_]] or perm[ix[dist_+1]] < perm[ix[dist_]]
        tot += 1; good += x0 and xx
    return F(good, tot)
Exi = F(1, 2)*F(2, 3)
for r in (3, 4, 5):
    cov = F(1, 2)*iid_phase_joint(r) - Exi**2
    C.ok(f"exchangeable-with-ties clock: Cov(xi_0, xi_{r}) = {cov} > 0 (covariance-LRO, constant 1/9 for r>=3)", cov == F(1, 9))
covT = F(1, 2)*F(1, 4) + F(1, 2)*F(1, 4) - (F(1, 2))**2  # E[T_xT_y] - E T E T, x != y
C.ok(f"... while its clocks are pairwise UNcorrelated: Cov(T_x,T_y) = {covT}", covT == 0)
C.done()
