"""check.py -- the-member-and-a-spin-polarised-walker a1 (worker w-macbookpro9927a-j2fce).

Exact (Fractions / Gaussian rationals / sympy) checks of ATTEMPT.md:
 (c) the face spin's balance law  dS~_l/dt + D(x) - D(x - e_l) = -sum_ij eps_lij (Theta_ij - Theta_ji)  (spin current delta_il D);
 (a),(b) a spin-polarised walker at rest, psi = f chi with f real: e = pi = K = 0, P'' = 0, P^B = (1/4) curl S~, and the
     member's static transverse shift is the lattice vector potential of the magnetisation wbar S~/(16 alpha).
Run from the repository root.
"""
import hashlib, os, random, subprocess, sys
from fractions import Fraction as F
from itertools import product
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, cwd=HERE).stdout.strip()
FAILS = []; NOK = 0
def ok(name, cond, detail=""):
    global NOK
    if cond: NOK += 1
    else: FAILS.append(name); print("FAIL", name, detail)

# ------------------------------------------------------------------ Q: blocks 136 and 138 on their hand-off branches
B136 = ("d7e6aacc7b8cae11c85f64497d74be97f8102afc", "physics-loop/admissibility-induced-law-block136-two-step-content-keeps-symmetric-books-bond-shift-keeps-every-constraint-20260925",
        "docs/ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md")
B138 = ("133b1d2ca7dad87ae42babc0391e1840c1b1082b", "physics-loop/admissibility-induced-law-block138-the-coins-spin-enters-the-source-link-through-its-curl-20260925",
        "docs/ADMISSIBILITY_RULE_THE_COINS_SPIN_ENTERS_THE_SOURCE_LINK_THROUGH_ITS_CURL_THE_SYMMETRIC_MOMENTUM_IS_THE_TWO_STEP_MOMENTUM_PLUS_HALF_THE_CURL_OF_THE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md")
def gshow(head, branch, path):
    r = subprocess.run(["git", "show", f"{head}:{path}"], capture_output=True, cwd=ROOT)
    if r.returncode:
        subprocess.run(["git", "fetch", "origin", branch, "--quiet"], cwd=ROOT)
        r = subprocess.run(["git", "show", f"{head}:{path}"], capture_output=True, cwd=ROOT)
    return r.stdout
t136 = gshow(*B136).decode(); t138 = gshow(*B138).decode()
ok("Q1 block 136 and 138 notes pinned by SHA256 at their branch heads", hashlib.sha256(t136.encode()).hexdigest() == "e11c9ff01559642d89c5b697e909380693b971bd539b8ea5208aeaf30b760c93" and hashlib.sha256(t138.encode()).hexdigest() == "ec6a7365dd973f1e52759daa44c4de76014421ca871f330e835e46356fcf6edd")
ok("Q2 block 138 statements", "*Statement.* For every state on `ℤ³` and `j = 1, 2, 3`: `Q_j − P″_j = ½Σ_klε_jkl∇̄_kS̃_l`." in t138
   and "*Statement.* `Σ_i∇̄_i(Θ_ij − Θ_ji) = ½ d/dt(∇̄ × S̃)_j` for every state, and both sides are nonzero." in t138
   and "next_trace_action: \"the spin's own balance law on the faces; the member's response to a spin-polarised walker; an other-family referee\"" in t138)
ok("Q3 block 136 T4 constraint", "the shift constraints, `8αpφ̇/w̄ = P_z` along the wave vector and `4αp(pN_x − ċ_x)/w̄ = P_x` across it." in t136)

# ------------------------------------------------------------------ exact lattice machinery (Gaussian rationals as pairs)
Z = (F(0), F(0))
def gm(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def ga(a, b): return (a[0] + b[0], a[1] + b[1])
def cj(a): return (a[0], -a[1])
ONE = (F(1), F(0)); MINUS = (F(-1), F(0)); MI2 = (F(0), F(-1, 2)); HALF = (F(1, 2), F(0))
SIG = [((Z, ONE), (ONE, Z)), ((Z, (F(0), F(-1))), ((F(0), F(1)), Z)), ((ONE, Z), (Z, MINUS))]
def sv(a, v): M = SIG[a]; return (ga(gm(M[0][0], v[0]), gm(M[0][1], v[1])), ga(gm(M[1][0], v[0]), gm(M[1][1], v[1])))
def vadd(u, v): return (ga(u[0], v[0]), ga(u[1], v[1]))
def vsc(u, c): return (gm(u[0], c), gm(u[1], c))
def inner(u, v): return ga(gm(cj(u[0]), v[0]), gm(cj(u[1]), v[1]))
EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
class Lat:
    def __init__(self, L, ps):
        self.L = L; self.sites = list(product(range(L), repeat=3)); self.ps = ps
        self.Hp = self.Happ(ps); self.P = [self.Sapp(self.Capp(ps, j), j) for j in range(3)]; self._K = {}
    def sh(self, x, a, s=1): y = list(x); y[a] = (y[a] + s) % self.L; return tuple(y)
    def shv(self, x, v): return tuple((x[i] + v[i]) % self.L for i in range(3))
    def Happ(self, ps):
        out = {}
        for x in self.sites:
            acc = (Z, Z)
            for a in range(3):
                acc = vadd(acc, vsc(vadd(sv(a, ps[self.sh(x, a)]), vsc(sv(a, ps[self.sh(x, a, -1)]), MINUS)), MI2))
            out[x] = acc
        return out
    def Capp(self, ps, j): return {x: vsc(vadd(ps[self.sh(x, j)], ps[self.sh(x, j, -1)]), HALF) for x in self.sites}
    def Sapp(self, ps, j): return {x: vsc(vadd(ps[self.sh(x, j)], vsc(ps[self.sh(x, j, -1)], MINUS)), MI2) for x in self.sites}
    def re(self, u, a, v): return inner(u, v if a is None else sv(a, v))[0]           # Re u^dag coin v
    def dre(self, p, a, q):   # d/dt Re psi^dag(p) coin psi(q), i dpsi/dt = H psi
        A = (lambda v: v) if a is None else (lambda v: sv(a, v))
        return -inner(self.Hp[p], A(self.ps[q]))[1] + inner(self.ps[p], A(self.Hp[q]))[1]
    def energy(self, x): return inner(self.ps[x], self.Hp[x])[0]
    def pi(self, j, x): return inner(self.ps[x], self.P[j][x])[0]
    def K(self, a, j, x):
        key = (a, j, x)
        if key not in self._K:
            xa = self.sh(x, a)
            self._K[key] = (self.re(self.ps[xa], a, self.P[j][x]) + self.re(self.P[j][xa], a, self.ps[x])) / 2
        return self._K[key]
    def Th(self, i, j, y):
        ls = [m for m in range(3) if m != j]; tot = F(0)
        for s1, s2 in product((1, -1), repeat=2):
            yy = self.sh(self.sh(y, ls[0], s1), ls[1], s2); tot += self.K(i, j, yy) + self.K(i, j, self.sh(yy, j))
        return tot / 8
    def Pdd(self, j, y):
        ls = [m for m in range(3) if m != j]; tot = F(0)
        for s1, s2 in product((1, -1), repeat=2):
            yy = self.sh(self.sh(y, ls[0], s1), ls[1], s2); tot += self.pi(j, yy) + self.pi(j, self.sh(yy, j))
        return tot / 8
    def Qb(self, j, x):
        xj = self.sh(x, j)
        return (self.re(self.ps[xj], j, self.Hp[x]) + self.re(self.Hp[xj], j, self.ps[x])) / 2
    def Q(self, j, x): return sum(self.Qb(j, self.shv(x, sg)) for sg in product((1, -1), repeat=3)) / 8
    def Sface(self, l, x, rate=False):
        j, k = [m for m in range(3) if m != l]
        f = self.dre if rate else (lambda p, a, q: self.re(self.ps[p], a, self.ps[q]))
        return (f(x, l, self.sh(self.sh(x, j), k)) + f(self.sh(x, k), l, self.sh(x, j))) / 2
    def St(self, l, x, rate=False): return sum(self.Sface(l, self.shv(x, sg), rate) for sg in product((1, -1), repeat=3)) / 8
    def curl(self, j, x):
        return sum(e * (self.St(l, x) - self.St(l, self.sh(x, k, -1))) for (jj, k, l), e in EPS.items() if jj == j)
    def D0(self, x):
        pairs = [((0, 0, 0), (1, 1, 1)), ((0, 0, 1), (1, 1, 0)), ((0, 1, 0), (1, 0, 1)), ((1, 0, 0), (0, 1, 1))]
        return sum(self.re(self.ps[self.shv(x, a)], None, self.ps[self.shv(x, b)]) for a, b in pairs) / 4
    def D(self, x): return sum(self.D0(self.shv(x, sg)) for sg in product((1, -1), repeat=3)) / 8
    def torque(self, l, x): return -sum(e * (self.Th(i, j, x) - self.Th(j, i, x)) for (ll, i, j), e in EPS.items() if ll == l)

rnd = random.Random(9200)
def rq(): return (F(rnd.randint(-5, 5), rnd.randint(1, 4)), F(rnd.randint(-5, 5), rnd.randint(1, 4)))

# ------------------------------------------------------------------ C: the spin's balance law (exact, random states)
import time as _tm
_t0 = _tm.time()
for L, nst, stride in ((5, 2, 1), (6, 1, 7)):
    for s in range(nst):
        lat = Lat(L, {x: (rq(), rq()) for x in product(range(L), repeat=3)})
        res = F(0); nzr = nzt = nzd = 0; cnt = 0
        for x in lat.sites[::stride]:
            for l in range(3):
                r = lat.St(l, x, True); dD = lat.D(x) - lat.D(lat.sh(x, l, -1)); tq = lat.torque(l, x)
                res = max(res, abs(r + dD - tq)); nzr += r != 0; nzt += tq != 0; nzd += dD != 0; cnt += 1
        ok(f"C1 L={L} state {s}: dS~_l/dt + D(x) - D(x-e_l) = -sum eps_lij (Theta_ij - Theta_ji) at {cnt} (site, l); all three terms nonzero",
           res == 0 and nzr == cnt and nzt > cnt // 2 and nzd == cnt, f"{res} {nzr} {nzt} {nzd} {cnt}")
lat5 = Lat(5, {x: (rq(), rq()) for x in product(range(5), repeat=3)})
t1 = max(abs(lat5.Q(j, x) - lat5.Pdd(j, x) - lat5.curl(j, x) / 2) for x in lat5.sites[::9] for j in range(3))
ok("C2 my densities reproduce block 138 T1: Q_j - P''_j = (1/2)(curl S~)_j (L=5, random state)", t1 == 0)
# the beat identity behind C1 (sympy): sigma(s') sigma_l - sigma_l sigma(s) = (s'_l - s_l) + i eps_mln (s_m + s'_m) sigma_n
s = sp.symbols("s1:4"); t = sp.symbols("t1:4"); Pm = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
sd = lambda v: v[0] * Pm[0] + v[1] * Pm[1] + v[2] * Pm[2]
bi = True
for l in range(3):
    lhs = sd(t) * Pm[l] - Pm[l] * sd(s)
    rhs = (t[l] - s[l]) * sp.eye(2) + sp.I * sum((EPS.get((m, l, n), 0) * (s[m] + t[m]) * Pm[n] for m in range(3) for n in range(3)), sp.zeros(2))
    bi &= sp.simplify(lhs - rhs) == sp.zeros(2)
kb, qq = sp.symbols("kb q", real=True)
trig = sp.simplify(sp.sin(kb + qq/2) - sp.sin(kb - qq/2) - 2 * sp.cos(kb) * sp.sin(qq/2)) == 0 and \
       sp.simplify((sp.sin(kb + qq/2) + sp.sin(kb - qq/2)) * sp.cos(kb) - sp.sin(2*kb) * sp.cos(qq/2)) == 0 and \
       sp.simplify(sp.cos(sp.Symbol('a')) * sp.cos(sp.Symbol('b')) * sp.cos(sp.Symbol('c')) * 4 - sum(sp.cos(sp.Symbol('a') + e1*sp.Symbol('b') + e2*sp.Symbol('c')) for e1 in (1, -1) for e2 in (1, -1))) == 0
ok("C3 beat identities: coin commutator, s_l - s'_l = 2cos(kb_l) sin(q_l/2), (s_a + s'_a) cos kb_a = sin 2kb_a cos(q_a/2), 4 prod cos = sum of 4 body-diagonal cosines", bi and trig)

# ------------------------------------------------------------------ A/B: the spin-polarised walker at rest on the 6^3 torus
L = 6; box = {(x, y, z) for x in range(3) for y in range(3) for z in range(3)}
chi = ((F(3, 5), F(0)), (F(0), F(4, 5)))                  # chi = (3/5, 4i/5): n = chi^dag sigma chi = (0, 24/25, -7/25)
n_chi = [inner(chi, sv(a, chi))[0] for a in range(3)]
psr = {x: (chi if x in box else (Z, Z)) for x in product(range(L), repeat=3)}
W = Lat(L, psr)
zero_all = all(W.energy(x) == 0 for x in W.sites) and all(W.pi(j, x) == 0 for x in W.sites for j in range(3)) and \
           all(W.K(a, j, x) == 0 for x in W.sites for a in range(3) for j in range(3))
ok("A1 at rest (psi = 1_box chi): energy density, two-step momentum and every current K vanish at every site, so Theta = 0 and P'' = 0",
   n_chi == [F(0), F(24, 25), F(-7, 25)] and zero_all)
PB = {(j, x): W.Q(j, x) / 2 for j in range(3) for x in W.sites}             # P^B = (P'' + Q)/2 with P'' = 0
curl = {(j, x): W.curl(j, x) for j in range(3) for x in W.sites}
nzPB = sum(1 for v in PB.values() if v != 0)
ok("A2 P^B = (1/4)(curl S~) at every bond; nonzero on part of the bonds only (the box's neighbourhood)",
   all(PB[(j, x)] == curl[(j, x)] / 4 for j in range(3) for x in W.sites) and 0 < nzPB < 3 * W.L ** 3, f"{nzPB}")
StT = {l: sum(W.St(l, x) for x in W.sites) for l in range(3)}
ok("A3 total face spin = b(b-1)^2 n with b = 3 (the magnetisation's dipole moment before the factor wbar/(16 alpha))",
   [StT[l] for l in range(3)] == [12 * v for v in n_chi])
# exact inverse Laplacian on zero-mean fields: G = q(-Lap), q(lam) = 1/lam on the spectrum {1..12} of -Lap on the 6^3 torus, q(0) = 0
lam = sp.symbols("lam"); pts = list(range(0, 13))
qpoly = sp.Poly(sp.interpolate([(0, 0)] + [(v, sp.Rational(1, v)) for v in range(1, 13)], lam), lam)
coef = [F(int(sp.fraction(c)[0]), int(sp.fraction(c)[1])) for c in qpoly.all_coeffs()]
def mlap(f):   # -Lap f = sum_i (2 f(x) - f(x+e_i) - f(x-e_i))
    return {x: sum(2 * f[x] - f[W.sh(x, i)] - f[W.sh(x, i, -1)] for i in range(3)) for x in W.sites}
def G(f):
    acc = {x: F(0) for x in W.sites}
    for c in coef:
        acc = mlap(acc); acc = {x: acc[x] + c * f[x] for x in W.sites}
    return acc
alpha, wbar = F(1, 4), F(1)                                                 # alpha = K/4 with K = 1
N = {j: G({x: wbar * PB[(j, x)] / (4 * alpha) for x in W.sites}) for j in range(3)}
chk = all(4 * alpha * mlap(N[j])[x] == wbar * PB[(j, x)] for j in range(3) for x in W.sites)
GS = {l: G({x: W.St(l, x) - StT[l] / W.L ** 3 for x in W.sites}) for l in range(3)}
A = {j: {x: wbar / (16 * alpha) * sum(e * (GS[l][x] - GS[l][W.sh(x, k, -1)]) for (jj, k, l), e in EPS.items() if jj == j) for x in W.sites} for j in range(3)}
ok("A4 static transverse shift: 4 alpha (-Lap) N = wbar P^B solved exactly, and N equals the lattice vector potential curl G of the magnetisation wbar S~/(16 alpha)",
   chk and all(N[j][x] == A[j][x] for j in range(3) for x in W.sites) and any(N[j][x] != 0 for j in range(3) for x in W.sites))
divN = max(abs(sum(N[j][x] - N[j][W.sh(x, j, -1)] for j in range(3))) for x in W.sites)
ok("A5 the shift is transverse (lattice divergence zero), so the longitudinal constraint is P^B_parallel = 0 and the clock is not driven", divN == 0)
# B: first-order-in-time rates at rest
PH = [W.Sapp(W.Capp(W.Hp, j), j) for j in range(3)]
dpi = max(abs(-inner(W.Hp[x], W.P[j][x])[1] + inner(W.ps[x], PH[j][x])[1]) for x in W.sites for j in range(3))
spinrate = {(l, x): W.St(l, x, True) for l in range(3) for x in W.sites}
gradD = all(spinrate[(l, x)] == -(W.D(x) - W.D(W.sh(x, l, -1))) for l in range(3) for x in W.sites)
curlrate = max(abs(sum(e * (spinrate[(l, x)] - spinrate[(l, W.sh(x, k, -1))]) for (jj, k, l), e in EPS.items() if jj == j)) for j in range(3) for x in W.sites)
ok("B1 at rest the two-step momentum does not move (d pi/dt = 0), the spin moves only by a gradient (dS~/dt = -grad D, torque 0), so the source P^B is momentarily static",
   dpi == 0 and gradD and curlrate == 0 and any(v != 0 for v in spinrate.values()))

print(f"checks passed {NOK}, failed {len(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL exact: (c) the coin's face spin keeps its own books, dS~_l/dt + dbar_l D = -sum_ij eps_lij (Theta_ij - Theta_ji), "
      "with an isotropic spin current delta_il D (D = the body-diagonal overlap averaged by C1C2C3) and block 120's two-step stress as the "
      "torque, for every state (beat proof; exact on 5^3 and 6^3); (a),(b) a spin-polarised walker at rest (psi = f chi, f real) sources "
      "neither the clock nor the lengths (e = 0, Theta = 0), only the shift through P^B = (1/4) curl S~, and the static shift is the lattice "
      "vector potential of the magnetisation wbar S~/(16 alpha) (exact on 6^3); the member's lattice static equation is read from block 136 T4")
print("HIT: the face spin's balance law is exact: for every state of the walk, dS~_l/dt + dbar_l D = -sum_ij eps_lij (Theta_ij - Theta_ji), "
      "so the spin current is isotropic, J^S_il = delta_il D with D the body-diagonal overlap averaged over the eight body diagonals, and the "
      "torque is exactly the antisymmetric part of block 120's two-step stress; its curl is block 138 T3. A spin-polarised walker at rest sources "
      "only the shift, whose static solution is the vector potential of the magnetisation wbar S~/(16 alpha)")
