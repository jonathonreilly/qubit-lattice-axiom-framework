"""Node census of the supplied composite-network comparator at ten NEW rational couplings across the regimes Jz > Jx + Jy, |Jx - Jy| < Jz < Jx + Jy and
Jz < |Jx - Jy| (Jx != Jy throughout): off-plane orbits identified by PSLQ, exact ring verification, charges, interval boxes, interval clearing of the torus.

Supplied model: four-site Bloch matrix H(f) = i M(f), couplings (Jx, Jy, Jz, kappa); M(z) = sum over terms (a, b, n, t): M[a,b] += t z^n, M[b,a] -= t z^(-n),
z_j = exp(2 pi i f_j).  A middle-band touching is a zero of D = det M: the characteristic polynomial of the anti-Hermitian M has no mu^3, mu^1 term for symbolic
couplings, so spec H = {+-l1, +-l2} and D = (l1 l2)^2.  Couplings (Jx, Jy, Jz; kappa), kappa_c and kappa_f the line-node flip couplings, u_* = kappa_*^2 the birth coupling:
  H1 (6/5, 4/5, 1; 1/5)   triangle regime, kappa < kappa_c        H2 (6/5, 4/5, 1; 1/4)    triangle regime, kappa > kappa_c
  K1 (3/2, 1/2, 11/5; 1)  Jz > Jx+Jy, Jz < J0, kappa > kappa_f    K2 (3/2, 1/2, 11/5; 73/100)  Jz < J0, kappa_* < kappa < kappa_f
  K3 (3/2, 1/2, 14/5; 2)  J0 < Jz < phi s, kappa > kappa_f        K4 (6/5, 4/5, 3; 8/5)   J0 < Jz < phi s, kappa_* < kappa < kappa_f
  K5 (6/5, 4/5, 7/2; 2)   Jz > phi s (no flip)                    L1 (2, 1/2, 1; 2), L2 (2, 1/2, 1; 9/10): Jz < |Jx - Jy|, off-plane orbit;  L3 (2, 1/2, 1; 4/5): no touching.
For each coupling:
  (1) EXACT (rational ring Q[alpha, t, d, i]/(...) for the off-plane orbit, Q[alpha, t, i]/(...) for each irreducible factor of the line quadratic q(c)):
      M has rank 2 (sixteen 3x3 minors, det, tr vanish; adj M = 0, grad D = 0), a2 != 0, Qp = a2 1 + M^2 satisfies Qp^2 = a2 Qp, M Qp = 0, tr Qp = 2 a2, so Qp/a2
      is the kernel projector, and T = Im Tr(P d1H P d2H P d3H) = -8 pi^3 Im Tr(Qp N1 Qp N2 Qp N3)/a2^3 is a ring element c(alpha) t d (off-plane) or c(alpha) t (line);
      the minimal polynomial Q of alpha = cos 2 pi f3 (PSLQ, 800 digits) is verified irreducible; the relation identities of the orbit are verified exactly;
  (2) INTERVAL (mpmath.iv, 300 bits, outward rounding; the real roots of Q and of the line factors enclosed by exact rational isolating intervals of width <= 1e-50):
      every real root of Q in [-1,1] is classified (t^2 > 0 and d^2 > 0 gives a real orbit that must be listed), sign T at every node, line charges against the closed form
      -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/Jz^3;
  (3) INTERVAL: Hessian of D in theta = 2 pi f positive definite on a box around each node (Frobenius bound for its change over the box, exact rational LDL), exact node in the
      box, a2 > 0 on the box: D strictly convex on the box with an exact critical point where D = 0, so one zero per box; boxes disjoint;
  (4) INTERVAL: clearing of the torus by adaptive dyadic cubes with the outward-rounded second-order Taylor lower bound of D; the run ends when every uncleared cube lies
      inside a node box (L3: when no cube is uncleared).  Hence D > 0 outside the boxes and the zero set of D is the node list.
Controls: a removed box, a perturbed quintic or line factor, a flipped sign and a moved box centre fail; phase table and Taylor bound compared with 50-digit values and
double samples (FLOAT).  Float diagnostic: T from numpy with the kernel projector at each node.
Prints [PASS]/[FAIL] lines and TOTAL: PASS=N FAIL=M.   Run: nice -n 15 python3 census2_runner.py   (single process; -v long form; -n K1,H2 subset)."""
AUDIT_TIMEOUT_SEC = 300
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import time
import math
import itertools
import functools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
import mpmath as mp
from mpmath import iv
from mpmath.libmp import to_rational

T0 = time.time()
VERBOSE = "-v" in sys.argv
PASS = 0
FAIL = 0
OUT_BYTES = 0

def emit(s):
    global OUT_BYTES
    OUT_BYTES += len(s) + 1
    print(s, flush=True)

def vemit(s):
    if VERBOSE: emit(s)

def check(ok, label, detail):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    emit("[%s] %s: %s" % ("PASS" if ok else "FAIL", label, detail))

# ---------------------------------------------------------------- embedded data
TERMS = [(0, 1, (-1, 0, 0), "y"), (0, 1, (0, 0, 0), "x"), (0, 3, (0, 0, -1), "z"), (1, 1, (-1, 0, 0), "odd"), (1, 3, (1, 0, -1), "odd"),
         (3, 1, (0, 0, 1), "odd"), (0, 0, (1, 0, 0), "odd"), (0, 2, (-1, 0, 0), "odd"), (2, 0, (0, 0, 0), "odd"), (2, 3, (0, -1, 0), "y"),
         (2, 3, (0, 0, 0), "x"), (2, 1, (0, 0, 0), "z"), (3, 3, (0, -1, 0), "odd"), (3, 1, (0, 1, 0), "odd"), (1, 3, (0, 0, 0), "odd"),
         (2, 2, (0, 1, 0), "odd"), (2, 0, (0, -1, 1), "odd"), (0, 2, (0, 0, -1), "odd")]
COUPLINGS = {  # (Jx, Jy, Jz, kappa) exact rationals
    "H1": (Fr(6, 5), Fr(4, 5), Fr(1, 1), Fr(1, 5)),
    "H2": (Fr(6, 5), Fr(4, 5), Fr(1, 1), Fr(1, 4)),
    "K1": (Fr(3, 2), Fr(1, 2), Fr(11, 5), Fr(1, 1)),
    "K2": (Fr(3, 2), Fr(1, 2), Fr(11, 5), Fr(73, 100)),
    "K3": (Fr(3, 2), Fr(1, 2), Fr(14, 5), Fr(2, 1)),
    "K4": (Fr(6, 5), Fr(4, 5), Fr(3, 1), Fr(8, 5)),
    "K5": (Fr(6, 5), Fr(4, 5), Fr(7, 2), Fr(2, 1)),
    "L1": (Fr(2, 1), Fr(1, 2), Fr(1, 1), Fr(2, 1)),
    "L2": (Fr(2, 1), Fr(1, 2), Fr(1, 1), Fr(9, 10)),
    "L3": (Fr(2, 1), Fr(1, 2), Fr(1, 1), Fr(4, 5)),
}
# off-plane orbits found by PSLQ (800 digits): integer polynomial Q of alpha = cos 2 pi f3 (descending), relation lists (ascending powers, (num, den)) for
# sigma = c1 + c2, pi = c1 c2, r12 = s1 s2, w = s3 (s1 + s2), and one image (ts, ds, 8-digit centre of (f1, f2, f3) over 1e8), ts = sign s3, ds = sign (c1 - c2)
OFF = {
    "H2": [
        dict(Q=[900000, -2406000, -319020500, 2617502755, 483224492, -2739002788],
             image=(1, 1, (28883068, 59800163, 2099537)),
             rel={
                 "sigma": [(-12668248115396159098, 4820656408341163335), (2852293005887829136, 1606885469447054445), (-178970345581018672, 964131281668232667), (-2625185677904960, 321377093889410889), (84487926428000, 107125697963136963)],
                 "pi": [(132995319571316776037, 53027220491752796685), (-43931818484652172304, 17675740163917598895), (1507998068563994108, 10605444098350559337), (49914496118304940, 3535148032783519779), (-620332457572000, 1178382677594506593)],
                 "r12": [(-20609575504624100672, 10605444098350559337), (6113364579586233752, 3535148032783519779), (-3668098581016127920, 10605444098350559337), (26582955475999900, 3535148032783519779), (1344508761500000, 1178382677594506593)],
                 "w": [(-17577252955128257452, 8034427347235272225), (2422117495836050746, 2678142449078424075), (2401818586133263643, 1606885469447054445), (-14060111988277492, 107125697963136963), (69483578515600, 35708565987712321)],
             }),
    ],
    "K1": [
        dict(Q=[855360000000, -745861950000, -3730085353000, 11391440876000, 9557412362740, -7283318733611],
             image=(1, 1, (14626329, 80124727, 16521116)),
             rel={
                 "sigma": [(4513449905501265001261311937, 5968982757519671539200437250), (10831574240439167991975006, 66322030639107461546671525), (58337676869077134406119208, 119379655150393430784008745), (-1062771278652153835615640, 2652881225564298461866861), (414831115326872293632000, 2652881225564298461866861)],
                 "pi": [(1743250961624530442652789177967, 1104261810141139234752080891250), (-31940745681246384080613716034, 12269575668234880386134232125), (-13921859383107255849071302232, 22085236202822784695041617825), (88223261239928749498125512, 98156605345879043089073857), (-28983018096773641546905600, 98156605345879043089073857)],
                 "r12": [(-53186075041809714575689263802, 78875843581509945339434349375), (-29368022809827481753849192, 1752796524033554340876318875), (-1130212306453174182336222416, 3155033743260397813577373975), (2770948924818139273077056, 14022372192268434727010551), (-1013130943534503666892800, 14022372192268434727010551)],
                 "w": [(-1097982193354468810742895743, 710593185419008516571480625), (208158771298379351534393487, 94745758055867802209530750), (47693232667783667978313866, 28423727416760340662859225), (-470659143766249522477248, 378983032223471208838123), (152872023706308849254400, 378983032223471208838123)],
             }),
    ],
    "K3": [
        dict(Q=[453530000000, 818197050000, -1069132360500, 2764676854900, 4413375691105, -4129652167639],
             image=(1, 1, (9088061, 90032784, 13243194)),
             rel={
                 "sigma": [(3030138144201171085405147, 2142015546784171840215300), (-784258040932191607909042, 10388775401903233425044205), (1157898773342924665072597, 2077755080380646685008841), (-16984338395020628450500, 2077755080380646685008841), (380334126145820405020000, 2077755080380646685008841)],
                 "pi": [(49457131336425272084052263, 23026667127929847282314475), (-4299664941656300017701334829, 1786869369127356149107603260), (20261179644027371309056064, 89343468456367807455380163), (36088016647428453411742225, 89343468456367807455380163), (-31319688888010495865777500, 89343468456367807455380163)],
                 "r12": [(-109600953645503136494661643, 644746679582035723904805300), (-194007298127820483851926615, 2501617116778298608750644564), (-149135281885143607150556749, 625404279194574652187661141), (56386682245200383915491675, 625404279194574652187661141), (-6082133098751006826677500, 89343468456367807455380163)],
                 "w": [(-594584796655990945130287, 367502667340421639252625), (12332681282860720502624689, 7129551746404179801500925), (316141730454580368592396, 285182069856167192060037), (-181932377607932849798428, 285182069856167192060037), (22120844231629456535200, 40740295693738170294291)],
             }),
    ],
    "L1": [
        dict(Q=[319488000, 1158133760, -1514087872, 1988269936, 4215691603, -144841699],
             image=(1, 1, (94262051, 63413353, 24461453)),
             rel={
                 "sigma": [(531944086562840446506421, 1697459922183586449724360), (-54649072649832508834743, 42436498054589661243109), (96511532654349925809852, 212182490272948306215545), (-4126002059317642979712, 42436498054589661243109), (-2091363029351415705600, 42436498054589661243109)],
                 "pi": [(-9348200516542648806884837, 13579679377468691597794880), (669834494623808588642739, 339491984436717289944872), (-181322812417868128352103, 212182490272948306215545), (15268560349393714678368, 42436498054589661243109), (5693386894371572198400, 42436498054589661243109)],
                 "r12": [(3099015942190216878864187, 13579679377468691597794880), (361236350699707457844459, 339491984436717289944872), (-162782013539275537356567, 212182490272948306215545), (10734308025451260486752, 42436498054589661243109), (4066728810155570457600, 42436498054589661243109)],
                 "w": [(-523406888239287793310067, 484988549195310414206960), (-57971848898317257540313, 96997709839062082841392), (21234834527309343566688, 30311784324706900887935), (-599627831892298985728, 6062356864941380177587), (-337804003877828966400, 6062356864941380177587)],
             }),
    ],
    "L2": [
        dict(Q=[-41452398000, 28836119880, 394538093136, -871197085152, -535211112435, 777737486723],
             image=(1, 1, (467857, 55782849, 10412473)),
             rel={
                 "sigma": [(2444344349818012862444757604, 2356176714167436353769907359), (-17844986392474264270635842, 12466543461203366951163531), (6386980442191001297255376, 29088601409474522886048239), (308922548481588333797640, 4155514487067788983721177), (-888046989633334009908000, 29088601409474522886048239)],
                 "pi": [(-3190594175288994881496061285, 1346386693809963630725661348), (27814683323514705698540672, 12466543461203366951163531), (-1944873554914065464280108, 4155514487067788983721177), (-584045233575271418646090, 4155514487067788983721177), (313517240672110408089000, 4155514487067788983721177)],
                 "r12": [(-3033283522284445598536981565, 3141568952223248471693209812), (6675056431367895065129704, 4155514487067788983721177), (-12955151566372868167679928, 29088601409474522886048239), (-479453727830922647129970, 4155514487067788983721177), (1359855992542937397534000, 29088601409474522886048239)],
                 "w": [(10444235853704006711835460, 37399630383610100853490593), (-47758274673418843420892326, 48085239064641558240202191), (1577707825555699410290778, 4155514487067788983721177), (94602679235081410376520, 593644926723969854817311), (-86191205857993706769000, 4155514487067788983721177)],
             }),
    ],
}
NAMES = tuple(COUPLINGS.keys())
# node-box half-width in f units, as an integer over 10^8 (theta radius rho = 2 pi * value); default 5000
BOXRF = {"H1": 150, "H2": 1000, "K1": 1000, "K2": 500, "K3": 1000, "K4": 300, "K5": 1000, "L1": 1000, "L2": 1000, "L3": 1000}
CONTROL_AT = "K1"
E8 = 10 ** 8
KMAX = 25

# ---------------------------------------------------------------- exact tower arithmetic
class Field:
    """K = Q[alpha]/(q), q given by integer coefficients in ascending order (degree n >= 1); elements are tuples of Fractions."""
    def __init__(self, q_asc):
        self.n = len(q_asc) - 1
        lead = Fr(q_asc[-1])
        self.mon = [Fr(c) / lead for c in q_asc]
    def zero(self): return tuple(Fr(0) for _ in range(self.n))
    def one(self): return tuple([Fr(1)] + [Fr(0)] * (self.n - 1))
    def const(self, c): return tuple([Fr(c)] + [Fr(0)] * (self.n - 1))
    def alpha(self):
        if self.n == 1: return (-self.mon[0],)
        return tuple([Fr(0), Fr(1)] + [Fr(0)] * (self.n - 2))
    def add(self, a, b): return tuple(x + y for x, y in zip(a, b))
    def sub(self, a, b): return tuple(x - y for x, y in zip(a, b))
    def neg(self, a): return tuple(-x for x in a)
    def smul(self, c, a): return tuple(Fr(c) * x for x in a)
    def mul(self, a, b):
        n = self.n
        prod = [Fr(0)] * (2 * n - 1)
        for i, x in enumerate(a):
            if x == 0: continue
            for j, y in enumerate(b):
                if y != 0: prod[i + j] += x * y
        for k in range(2 * n - 2, n - 1, -1):
            c = prod[k]
            if c != 0:
                for j in range(n + 1):
                    prod[k - n + j] -= c * self.mon[j]
        return tuple(prod[:n])
    def is_zero(self, a): return all(x == 0 for x in a)
    def poly(self, coeffs_asc):
        r = self.zero(); p = self.one()
        for c in coeffs_asc:
            r = self.add(r, self.smul(c, p)); p = self.mul(p, self.alpha())
        return r
    def inv(self, a):
        x = sp.symbols("x")
        qa = sp.Poly(sum(sp.Rational(c.numerator, c.denominator) * x**j for j, c in enumerate(self.mon)), x)
        pa = sp.Poly(sum(sp.Rational(c.numerator, c.denominator) * x**j for j, c in enumerate(a)), x)
        s, t, g = sp.gcdex(pa, qa)
        assert g.degree() == 0, "element not invertible"
        res = (s * (1 / g.as_expr())).rem(qa)
        co = res.all_coeffs()[::-1]
        co = [Fr(int(sp.Rational(c).p), int(sp.Rational(c).q)) for c in co] + [Fr(0)] * (self.n - len(co))
        return tuple(co[:self.n])

class Ring:
    """R = K[t, d, i]/(t^2 - T, d^2 - Dc, i^2 + 1); elements are dicts {(et, ed, ei): K-element}."""
    def __init__(self, K, T, Dc):
        self.K, self.T, self.Dc = K, T, Dc
    def zero(self): return {}
    def lift(self, k): return {(0, 0, 0): k}
    def gen(self, which):
        return {{"t": (1, 0, 0), "d": (0, 1, 0), "i": (0, 0, 1)}[which]: self.K.one()}
    def clean(self, a): return {k: v for k, v in a.items() if not self.K.is_zero(v)}
    def add(self, a, b):
        r = dict(a)
        for k, v in b.items():
            r[k] = self.K.add(r[k], v) if k in r else v
        return self.clean(r)
    def sub(self, a, b): return self.add(a, self.smul(-1, b))
    def smul(self, c, a): return {k: self.K.smul(c, v) for k, v in a.items()}
    def kmul(self, kel, a): return self.clean({k: self.K.mul(kel, v) for k, v in a.items()})
    def mul(self, a, b):
        r = {}
        K = self.K
        for k1, v1 in a.items():
            for k2, v2 in b.items():
                v = K.mul(v1, v2)
                et, ed, ei = k1[0] + k2[0], k1[1] + k2[1], k1[2] + k2[2]
                if et == 2: v = K.mul(v, self.T); et = 0
                if ed == 2: v = K.mul(v, self.Dc); ed = 0
                if ei == 2: v = K.neg(v); ei = 0
                key = (et, ed, ei)
                r[key] = K.add(r[key], v) if key in r else v
        return self.clean(r)
    def is_zero(self, a): return len(self.clean(a)) == 0

# ---------------------------------------------------------------- symbolic Bloch matrix (couplings symbolic) and exact Fourier data
Jx, Jy, Jz, kap = sp.symbols("Jx Jy Jz kappa", positive=True)
z1, z2, z3 = sp.symbols("z1 z2 z3")

def srat(q):
    q = Fr(q); return sp.Rational(q.numerator, q.denominator)

def build_M_sym():
    amp = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz, "odd": 2 * kap}
    M = sp.zeros(4, 4)
    for (a, b, n, kind) in TERMS:
        mon = z1 ** n[0] * z2 ** n[1] * z3 ** n[2]
        M[a, b] += amp[kind] * mon
        M[b, a] -= amp[kind] / mon
    return M

def build_M(J):
    """M at exact rational couplings J = (Jx, Jy, Jz, kappa)"""
    return build_M_sym().subs({Jx: srat(J[0]), Jy: srat(J[1]), Jz: srat(J[2]), kap: srat(J[3])}).applyfunc(sp.expand)

def fourier_sym(expr):
    """Fourier coefficients {k: a_k(couplings)} of a Laurent polynomial with exponents in [-3, 3]"""
    P = sp.Poly(sp.expand(sp.expand(expr) * z1**3 * z2**3 * z3**3), z1, z2, z3)
    return {(a - 3, b - 3, c - 3): v for (a, b, c), v in P.terms()}

def tcoeffs(expr):
    """exact Fourier coefficients {k: a_k} (Fractions) of a Laurent polynomial with rational coefficients"""
    return {k: Fr(int(sp.Rational(v).p), int(sp.Rational(v).q)) for k, v in fourier_sym(expr).items()}

def sym_setup():
    """symbolic checks (a): M anti-Hermitian on the torus, char poly mu^4 + a2 mu^2 + D (no mu^3, mu^1 term); returns (ok, Fourier dicts of D and a2 in the couplings)"""
    Ms = build_M_sym()
    mu = sp.symbols("mu")
    Minv = Ms.subs({z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}, simultaneous=True)
    ah = (Ms + Minv.T).applyfunc(sp.expand) == sp.zeros(4, 4)
    cp = sp.Poly(sp.expand((mu * sp.eye(4) - Ms).det(method="berkowitz")), mu)
    co = {e[0]: sp.expand(c) for e, c in cp.terms()}
    ok = ah and co.get(3, 0) == 0 and co.get(1, 0) == 0 and co[4] == 1
    return ok, fourier_sym(co[0]), fourier_sym(co[2])

def coeffs_at(J, dd):
    sub = {Jx: srat(J[0]), Jy: srat(J[1]), Jz: srat(J[2]), kap: srat(J[3])}
    out = {}
    for k, v in dd.items():
        r = sp.Rational(sp.expand(v.subs(sub)))
        if r != 0: out[k] = Fr(int(r.p), int(r.q))
    return out

# ---------------------------------------------------------------- the off-plane orbit and line points in their rings
def offplane_point(orb, q5=None, flip_s2=False):
    """Ring R and point (z, zi) of the off-plane orbit `orb` (dict Q, rel); relation identities returned as a flag."""
    q5 = orb["Q"] if q5 is None else q5
    rel = {kq: [Fr(n, d) for (n, d) in orb["rel"][kq]] for kq in orb["rel"]}
    K = Field(list(reversed(q5)))
    sigma = K.poly(rel["sigma"]); pi_ = K.poly(rel["pi"]); r12 = K.poly(rel["r12"]); w = K.poly(rel["w"])
    alpha = K.alpha()
    T = K.sub(K.one(), K.mul(alpha, alpha))
    Dc = K.sub(K.mul(sigma, sigma), K.smul(4, pi_))
    R = Ring(K, T, Dc)
    t, d, I = R.gen("t"), R.gen("d"), R.gen("i")
    half = Fr(1, 2)
    c3 = R.lift(alpha); s3 = t
    c1 = R.smul(half, R.add(R.lift(sigma), d)); c2 = R.smul(half, R.sub(R.lift(sigma), d))
    winv = K.inv(w); Tinv = K.inv(T)
    sp_ = R.kmul(K.mul(w, Tinv), t)
    sm_ = R.kmul(K.neg(K.mul(sigma, winv)), R.mul(d, t))
    s1 = R.smul(half, R.add(sp_, sm_)); s2 = R.smul(half, R.sub(sp_, sm_))
    if flip_s2: s2 = R.smul(-1, s2)
    one = R.lift(K.one())
    rel_ok = (R.is_zero(R.sub(R.mul(c1, c2), R.lift(pi_))) and R.is_zero(R.sub(R.mul(s1, s2), R.lift(r12)))
              and R.is_zero(R.sub(R.mul(s3, R.add(s1, s2)), R.lift(w)))
              and R.is_zero(R.sub(R.add(R.mul(c1, c1), R.mul(s1, s1)), one)) and R.is_zero(R.sub(R.add(R.mul(c2, c2), R.mul(s2, s2)), one))
              and R.is_zero(R.sub(R.add(R.mul(c3, c3), R.mul(s3, s3)), one)))
    z = [R.add(c1, R.mul(I, s1)), R.add(c2, R.mul(I, s2)), R.add(c3, R.mul(I, s3))]
    zi = [R.sub(c1, R.mul(I, s1)), R.sub(c2, R.mul(I, s2)), R.sub(c3, R.mul(I, s3))]
    return R, z, zi, rel_ok, rel, q5

def line_point(qfac_asc):
    """Ring R over K = Q[alpha]/(qfac) and the line point z = (alpha + i t, alpha - i t, 1), t^2 = 1 - alpha^2."""
    K = Field(qfac_asc)
    alpha = K.alpha()
    T = K.sub(K.one(), K.mul(alpha, alpha))
    R = Ring(K, T, K.one())
    t, I = R.gen("t"), R.gen("i")
    c = R.lift(alpha); one = R.lift(K.one())
    z = [R.add(c, R.mul(I, t)), R.sub(c, R.mul(I, t)), one]
    zi = [R.sub(c, R.mul(I, t)), R.add(c, R.mul(I, t)), one]
    return R, z, zi

# ---------------------------------------------------------------- exact root isolation
def roots_in_unit(coeffs_desc):
    """Enclosures (iv, from exact rational isolating intervals of width <= 1e-50) of ALL real roots of the integer polynomial in [-1, 1];
    asserts that no isolating interval straddles +-1."""
    x = sp.symbols("x")
    deg = len(coeffs_desc) - 1
    P = sp.Poly(sum(c * x ** (deg - j) for j, c in enumerate(coeffs_desc)), x)
    out = []
    for (a_, b_), _m in P.intervals(eps=sp.Rational(1, 10**50)):
        a_ = sp.Rational(a_); b_ = sp.Rational(b_)
        assert not (a_ < -1 < b_ or a_ < 1 < b_ or a_ == b_ and abs(a_) == 1), "root at the boundary"
        if a_ >= -1 and b_ <= 1:
            lo, hi = Fr(int(a_.p), int(a_.q)), Fr(int(b_.p), int(b_.q))
            Xlo = fr_iv(lo); Xhi = fr_iv(hi)
            X = iv.make_mpf((Xlo._mpi_[0], Xhi._mpi_[1]))
            assert lo_fr(X) <= lo and hi_fr(X) >= hi
            out.append(X)
    return out

def line_quadratic(J):
    """q(c) = 4k^2 c^2 - 2 Jx Jy c + Jz^2 - Jx^2 - Jy^2 - 4k^2 over Z, number of distinct roots in [-1, 1], and the integer coefficient lists (descending) of its
    irreducible factors over Q that have a root in [-1, 1]."""
    jx, jy, jz, kk = J
    cf = [4 * kk * kk, -2 * jx * jy, jz * jz - jx * jx - jy * jy - 4 * kk * kk]
    den = functools.reduce(lambda a, b: a * b // math.gcd(a, b), (c.denominator for c in cf), 1)
    ci = [int(c * den) for c in cf]
    c_ = sp.symbols("c")
    P = sp.Poly(ci[0] * c_**2 + ci[1] * c_ + ci[2], c_)
    nroots = P.count_roots(-1, 1)
    facs = []
    for fpoly, mult in sp.factor_list(P.as_expr())[1]:
        fp = sp.Poly(fpoly, c_)
        if fp.count_roots(-1, 1) >= 1:
            assert mult == 1
            cs = [int(v) for v in fp.all_coeffs()]
            g = functools.reduce(math.gcd, cs)
            facs.append([v // g for v in cs])
    return ci, nroots, facs

# ---------------------------------------------------------------- exact analysis of a point of the torus given by (cos, sin) ring elements
def make_eval(R, z, zi):
    one = R.lift(R.K.one())
    pw = {}
    def pw_get(j, e):
        if e == 0: return one
        if (j, e) not in pw:
            base = z[j] if e > 0 else zi[j]
            r = one
            for _ in range(abs(e)): r = R.mul(r, base)
            pw[(j, e)] = r
        return pw[(j, e)]
    def eval_laurent(expr):
        P = sp.Poly(sp.expand(sp.expand(expr) * z1**3 * z2**3 * z3**3), z1, z2, z3)
        out = R.zero()
        for (a_, b_, c_), co in P.terms():
            term = R.mul(R.mul(pw_get(0, a_ - 3), pw_get(1, b_ - 3)), pw_get(2, c_ - 3))
            out = R.add(out, R.smul(Fr(int(co.p), int(co.q)), term))
        return out
    return eval_laurent

def node_exact(Mr, R, z, zi):
    """Exact ring analysis at the point z = (cos + i sin).  Returns (flags, data)."""
    K = R.K
    ev = make_eval(R, z, zi)
    Mv = [[ev(Mr[a_, b_]) for b_ in range(4)] for a_ in range(4)]
    Nv = []
    for zj in (z1, z2, z3):
        Nj = Mr.applyfunc(lambda e: sp.expand(zj * sp.diff(e, zj)))
        Nv.append([[ev(Nj[a_, b_]) for b_ in range(4)] for a_ in range(4)])
    mm = R.mul
    def det3(rows, cols):
        m = [[Mv[r][c] for c in cols] for r in rows]
        t1 = mm(m[0][0], R.sub(mm(m[1][1], m[2][2]), mm(m[1][2], m[2][1])))
        t2 = mm(m[0][1], R.sub(mm(m[1][0], m[2][2]), mm(m[1][2], m[2][0])))
        t3 = mm(m[0][2], R.sub(mm(m[1][0], m[2][1]), mm(m[1][1], m[2][0])))
        return R.add(R.sub(t1, t2), t3)
    nz = sum(0 if R.is_zero(det3(rr, cc)) else 1 for rr in itertools.combinations(range(4), 3) for cc in itertools.combinations(range(4), 3))
    det = R.zero()
    for c in range(4):
        cols = [x_ for x_ in range(4) if x_ != c]
        det = R.add(det, R.smul(1 if c % 2 == 0 else -1, R.mul(Mv[0][c], det3((1, 2, 3), cols))))
    tr = R.zero()
    for a_ in range(4): tr = R.add(tr, Mv[a_][a_])
    a2 = R.zero()
    for a_, b_ in itertools.combinations(range(4), 2):
        a2 = R.add(a2, R.sub(R.mul(Mv[a_][a_], Mv[b_][b_]), R.mul(Mv[a_][b_], Mv[b_][a_])))
    def mmul(A, B):
        return [[functools.reduce(R.add, [R.mul(A[i][k], B[k][j]) for k in range(4)], R.zero()) for j in range(4)] for i in range(4)]
    M2 = mmul(Mv, Mv)
    Qp = [[R.add(M2[i][j], a2 if i == j else R.zero()) for j in range(4)] for i in range(4)]
    Q2 = mmul(Qp, Qp); MQ = mmul(Mv, Qp)
    trQ = R.zero()
    for i in range(4): trQ = R.add(trQ, Qp[i][i])
    A1, A2_, A3 = (mmul(Qp, Nv[j]) for j in range(3))
    A12 = mmul(A1, A2_)
    trace = R.zero()
    for i in range(4):
        for k in range(4):
            trace = R.add(trace, R.mul(A12[i][k], A3[k][i]))
    flags = dict(minors=(nz == 0), det=R.is_zero(det), tr=R.is_zero(tr), a2K=(set(a2.keys()) <= {(0, 0, 0)} and not R.is_zero(a2)),
                 Q2=all(R.is_zero(R.sub(Q2[i][j], R.mul(a2, Qp[i][j]))) for i in range(4) for j in range(4)),
                 MQ=all(R.is_zero(MQ[i][j]) for i in range(4) for j in range(4)),
                 trQ=R.is_zero(R.sub(trQ, R.smul(2, a2))))
    return flags, dict(a2=a2.get((0, 0, 0), K.zero()), trace=trace, nz=nz)

# ---------------------------------------------------------------- interval helpers (mpmath.iv, outward rounding)
def lo_fr(xv):
    p, q = to_rational(xv._mpi_[0]); return Fr(p, q)
def hi_fr(xv):
    p, q = to_rational(xv._mpi_[1]); return Fr(p, q)
def fr_iv(q):
    q = Fr(q); return iv.mpf(q.numerator) / iv.mpf(q.denominator)
def up_abs(xv): return max(abs(lo_fr(xv)), abs(hi_fr(xv)))

def kval(el, X):
    s_ = iv.mpf(0)
    for cf in reversed(el): s_ = s_ * X + fr_iv(cf)
    return s_

def ring_iv(elem, X, tval, dval):
    re = iv.mpf(0); im = iv.mpf(0)
    for (et, ed, ei), el in elem.items():
        val = kval(el, X) * (tval ** et) * (dval ** ed)
        if ei == 0: re += val
        else: im += val
    return re, im

def charge_iv(trace, a2el, X, tval, dval):
    """T = Im Tr(P d1H P d2H P d3H) = -8 pi^3 Im Tr(Qp N Qp N Qp N)/a2^3 as an iv enclosure."""
    re, im = ring_iv(trace, X, tval, dval)
    a2v = kval(a2el, X)
    return -8 * iv.pi ** 3 * im / a2v ** 3, a2v, re

def offplane_iv(X, rel, tsign, dsign):
    """iv enclosures of ((c1, s1), (c2, s2), (c3, s3)) at the root X for the image (tsign, dsign) and the positivity flags of t^2, d^2."""
    sigma, pi_, w = (kval(rel[k], X) for k in ("sigma", "pi", "w"))
    T = 1 - X * X; Dc = sigma * sigma - 4 * pi_
    if not (lo_fr(T) > 0 and lo_fr(Dc) > 0): return None
    t = tsign * iv.sqrt(T); d = dsign * iv.sqrt(Dc)
    c1 = (sigma + d) / 2; c2 = (sigma - d) / 2
    sp_ = w * t / T; sm_ = -sigma * d * t / w
    return [(c1, (sp_ + sm_) / 2), (c2, (sp_ - sm_) / 2), (X, t)]

def dev_arc(zst, f0):
    """Upper bound (Fraction) of max_j |theta*_j - theta0_j| (arc), theta0 = 2 pi f0/10^8, from the enclosures of cos, sin of theta*_j:
    arc <= (pi/2) chord."""
    PI = iv.pi
    out = Fr(0)
    for (cj, sj), n in zip(zst, f0):
        th = 2 * PI * fr_iv(Fr(n, E8))
        dc = cj - iv.cos(th); ds = sj - iv.sin(th)
        out = max(out, up_abs(PI / 2 * iv.sqrt(dc * dc + ds * ds)))
    return out

def hess_box(aD, aA, f0, rf, zst):
    """Hessian-PD certificate of D on the theta-box of half-width rho = 2 pi rf around f0 (rf: Fraction in f units).
    Returns dict(pivmin, eta, dev, rho, a2low)."""
    PI = iv.pi
    rho_iv = 2 * PI * fr_iv(rf)
    rho = hi_fr(rho_iv)
    th0 = [2 * PI * fr_iv(Fr(n, E8)) for n in f0]
    S = [[Fr(0)] * 3 for _ in range(3)]
    Hiv = [[iv.mpf(0)] * 3 for _ in range(3)]
    for kk in aD:
        arg = sum((kk[j] * th0[j] for j in range(3)), iv.mpf(0))
        cs = iv.cos(arg); a = fr_iv(aD[kk]); l1k = sum(abs(q) for q in kk)
        for i in range(3):
            for j in range(i, 3):
                Hiv[i][j] = Hiv[i][j] - a * (kk[i] * kk[j]) * cs
                S[i][j] += abs(aD[kk]) * abs(kk[i] * kk[j]) * l1k
    Hmid = [[Fr(0)] * 3 for _ in range(3)]
    ss = Fr(0)
    for i in range(3):
        for j in range(i, 3):
            mid = (lo_fr(Hiv[i][j]) + hi_fr(Hiv[i][j])) / 2
            rad = (hi_fr(Hiv[i][j]) - lo_fr(Hiv[i][j])) / 2
            Hmid[i][j] = Hmid[j][i] = mid
            ss += (1 if i == j else 2) * (rad + rho * S[i][j]) ** 2
    N_ = (ss.numerator * 10 ** 40) // ss.denominator
    eta = Fr(math.isqrt(N_) + 1, 10 ** 20)            # >= sqrt(ss)  (Frobenius bound of the change of the Hessian over the box)
    Lm = [[Hmid[i][j] - (eta if i == j else 0) for j in range(3)] for i in range(3)]
    piv = []
    for i in range(3):
        p = Lm[i][i]; piv.append(p)
        if p <= 0: break
        for r in range(i + 1, 3):
            fct = Lm[r][i] / p
            for cc in range(i, 3): Lm[r][cc] -= fct * Lm[i][cc]
    pd = len(piv) == 3 and all(p > 0 for p in piv)
    dev = dev_arc(zst, f0)
    a2c = iv.mpf(0); lip = Fr(0)
    for kk in aA:
        arg = sum((kk[j] * th0[j] for j in range(3)), iv.mpf(0))
        a2c += fr_iv(aA[kk]) * iv.cos(arg)
        lip += abs(aA[kk]) * sum(abs(q) for q in kk) * rho
    a2low = lo_fr(a2c) - lip
    return dict(pd=pd, pivmin=min(piv), eta=eta, dev=dev, rho=rho, a2low=a2low)

# ---------------------------------------------------------------- torus clearing with outward-rounded double intervals
DN, UP = -np.inf, np.inf
def rd(x): return np.nextafter(x, DN)
def ru(x): return np.nextafter(x, UP)
def f_dn(x): return float(np.nextafter(float(x), DN))      # float(Fraction) is the nearest double; one ulp down is below it
def f_up(x): return float(np.nextafter(float(x), UP))
def cint(fr):
    return (0.0, 0.0) if fr == 0 else (f_dn(fr), f_up(fr))

class Taylor:
    """Second-order Taylor lower bound of D(theta) = sum a_k cos(k.theta) over dyadic cubes (f-cubes of half-width 2^-(level+1))."""
    def __init__(self, aD):
        assert all(aD.get(tuple(-q for q in k)) == v for k, v in aD.items()), "D not inversion symmetric"
        self.KS = np.array(list(aD.keys()), dtype=np.int64)
        KSl = self.KS.tolist(); A_ = [aD[tuple(k)] for k in KSl]
        self.NT = len(KSl)
        self.QC = [("c", [cint(a) for a in A_])]
        for j in range(3):
            self.QC.append(("s", [cint(-a * k[j]) for a, k in zip(A_, KSl)]))
        for j in range(3):
            for l in range(j, 3):
                self.QC.append(("c", [cint(-a * k[j] * k[l]) for a, k in zip(A_, KSl)]))
        self.R3 = f_up(sum(abs(a) * sum(abs(q) for q in k) ** 3 for a, k in zip(A_, KSl)) / 6)
        iv.prec = 120
        self.TWOPI_UP = float(ru(float((2 * iv.pi).b)))
        iv.prec = 300
    @staticmethod
    def table(ms, N):
        iv.prec = 120
        cl = np.empty(len(ms)); ch = np.empty(len(ms)); sl = np.empty(len(ms)); sh = np.empty(len(ms))
        two_pi = 2 * iv.pi
        for i, m in enumerate(ms.tolist()):
            a = two_pi * iv.mpf(m) / iv.mpf(N)
            c, s = iv.cos(a), iv.sin(a)
            cl[i] = float(rd(float(c.a))); ch[i] = float(ru(float(c.b))); sl[i] = float(rd(float(s.a))); sh[i] = float(ru(float(s.b)))
        iv.prec = 300
        return cl, ch, sl, sh
    def lower_bound(self, idx, k):
        N = 2 ** (k + 1)
        m = ((2 * idx + 1) @ self.KS.T) % N
        ums = np.unique(m)
        cl, ch, sl, sh = self.table(ums, N)
        pos = np.searchsorted(ums, m)
        Cc = (cl[pos], ch[pos]); Ss = (sl[pos], sh[pos])
        n = len(idx)
        res = []
        for kind, co in self.QC:
            accl = np.zeros(n); acch = np.zeros(n)
            src = Cc if kind == "c" else Ss
            for t in range(self.NT):
                tl, th = co[t]
                if tl == 0 and th == 0: continue
                xl, xh = src[0][:, t], src[1][:, t]
                p = np.stack([tl * xl, tl * xh, th * xl, th * xh])
                accl = rd(accl + rd(p.min(axis=0))); acch = ru(acch + ru(p.max(axis=0)))
            res.append((accl, acch))
        rho = ru(self.TWOPI_UP * 2.0 ** (-(k + 1)))
        absmax = lambda pr: np.maximum(np.abs(pr[0]), np.abs(pr[1]))
        g1 = ru(ru(absmax(res[1]) + absmax(res[2])) + absmax(res[3]))
        hs = [absmax(r) for r in res[4:10]]                       # H00 H01 H02 H11 H12 H22
        hsum = ru(ru(ru(hs[0] + hs[3]) + hs[5]) + ru(2 * ru(ru(hs[1] + hs[2]) + hs[4])))
        quad = ru(ru(0.5 * ru(rho * rho)) * hsum)
        lin = ru(rho * g1)
        rem = ru(self.R3 * ru(rho * ru(rho * rho)))
        return rd(rd(rd(res[0][0] - lin) - quad) - rem)

def clear_torus(tay, boxes, k0=3, kmax=21, chunk=10000):
    """boxes: list of (f0 ints over 1e8, rf int over 1e8).  Returns dict(level, uncleared, outside, cubes)."""
    cur = np.array(list(itertools.product(range(2 ** k0), repeat=3)), dtype=np.int64)
    k = k0; total = 0
    off = np.array(list(itertools.product((0, 1), repeat=3)), dtype=np.int64)
    while True:
        keep = []
        for s0 in range(0, len(cur), chunk):
            c = cur[s0:s0 + chunk]
            Lb = tay.lower_bound(c, k)
            keep.append(c[~(Lb > 0)])
        unc = np.concatenate(keep) if keep else np.zeros((0, 3), dtype=np.int64)
        total += len(cur)
        L = (2 ** (k + 1)) * E8
        inside = np.zeros(len(unc), dtype=bool)
        for (nj, rj) in boxes:
            ok = np.ones(len(unc), dtype=bool)
            for a in range(3):
                diff = ((2 * unc[:, a] + 1) * E8 - nj[a] * 2 ** (k + 1)) % L
                diff = np.where(diff > L // 2, diff - L, diff)
                ok &= (np.abs(diff) + E8 <= rj * 2 ** (k + 1))
            inside |= ok
        outside = int((~inside).sum())
        vemit("   level %2d: cubes %7d uncleared %6d outside the boxes %6d (%.1f s)" % (k, len(cur), len(unc), outside, time.time() - T0))
        if len(unc) == 0 or outside == 0 or k == kmax:
            return dict(level=k, uncleared=len(unc), outside=outside, cubes=total)
        cur = (2 * unc[:, None, :] + off[None, :, :]).reshape(-1, 3)
        k += 1

# ---------------------------------------------------------------- float diagnostic: T from numpy at the node
def float_T(J, f):
    """FLOAT diagnostic: T = Im Tr(P d1H P d2H P d3H), P the projector on the eigenvalues |E| < 1e-6 of H(f) (numpy); returns (T, kernel dim)."""
    jx, jy, jz, kk = (float(v) for v in J)
    amp = {"x": 2 * jx, "y": 2 * jy, "z": 2 * jz, "odd": 2 * kk}
    f = np.asarray(f, dtype=float)
    def Hd(dj=None):
        M = np.zeros((4, 4), dtype=complex)
        for (a, b, n, kind) in TERMS:
            ph = np.exp(2j * np.pi * float(np.dot(f, n)))
            if dj is None:
                M[a, b] += amp[kind] * ph; M[b, a] -= amp[kind] * np.conj(ph)
            else:
                w = amp[kind] * 2j * np.pi * n[dj]
                M[a, b] += w * ph; M[b, a] += w * np.conj(ph)
        return 1j * M
    ev, V = np.linalg.eigh(Hd())
    W = V[:, np.abs(ev) < 1e-6]
    P = W @ W.conj().T
    D = [Hd(j) for j in range(3)]
    return float(np.trace(P @ D[0] @ P @ D[1] @ P @ D[2]).imag), W.shape[1]

def f_from_iv(zst):
    out = []
    for (cj, sj) in zst:
        ang = math.atan2(float(sj.mid), float(cj.mid)) / (2 * math.pi)
        out.append(ang % 1.0)
    return out

def sgn_iv(v):
    return 1 if lo_fr(v) > 0 else (-1 if hi_fr(v) < 0 else 0)

def image_centre(base, base_signs, ts, ds):
    """8-digit centre of the image (ts, ds) of the orbit point whose centre `base` has signs base_signs: t -> -t is f -> -f, d -> -d is f1 <-> f2."""
    n = list(base)
    if ds != base_signs[1]: n[0], n[1] = n[1], n[0]
    if ts != base_signs[0]: n = [(-v) % E8 for v in n]
    return tuple(n)


def sgn_str(vals):
    return "".join("+" if v > 0 else ("-" if v < 0 else "0") for v in vals)

def flip_u(J):
    """iv enclosure of u_f = (N0 + N1 sqrt(DF))/Den, the larger root of R2 (kappa_c^2 in the triangle regime, the flip coupling above J_x + J_y), valid when s^2 + Jz s - Jz^2 > 0."""
    jx, jy, jz, kk = J
    s = jx + jy; P = jx * jy
    e1 = s * s + jz * s - jz * jz
    S = jx*jx + jy*jy - jz*jz
    N0 = S * (2*jz**3*P - 4*jz*P*s*s + jz*s**4 - 4*P*s**3 + s**5)
    N1 = 2*jz*jz*P - jz*jz*s*s - 4*P*s*s + s**4
    DF = 4*jz**4*P + 4*jz**3*P*s + 4*jz*jz*P*P - 4*jz*jz*P*s*s + jz*jz*s**4 - 8*jz*P*s**3 + 2*jz*s**5 - 4*P*s**4 + s**6
    Den = -8 * e1 * (jz**3 - 4*P*s + s**3)
    return (fr_iv(N0) + fr_iv(N1) * iv.sqrt(fr_iv(DF))) / fr_iv(Den)

def line_pred(J):
    """Predicted charges of the line nodes (x, 1-x, 0) with x < 1/2, ordered by c = cos 2 pi x, from the exact line-family flip classifications (None if undecided).
    Triangle regime: (+) for kappa < kappa_c, (-) above (if Jz^2 > |Jx^2 - Jy^2|, else (-) throughout).  Jz > Jx + Jy and kappa^2 > u_*: Jz >= phi s: (-,+); J0 < Jz < phi s:
    (-,+) below the flip u_f, (-,-) above; s < Jz < J0 (G < 0): (+,-) below, (-,-) above.  phi s: s^2 + Jz s - Jz^2 <= 0; J0: root of G."""
    jx, jy, jz, kk = J
    s = jx + jy; P = jx * jy; u = kk * kk
    if jz > s:
        e1 = s * s + jz * s - jz * jz
        if e1 <= 0: return (-1, 1)
        G = jz**5 + (4*P - 2*s*s) * jz**3 - 2*P*s*jz**2 + (4*P*P - 5*P*s*s + s**4) * jz + P*s**3 - 4*P*P*s
        if G == 0: return None
        uf = flip_u(J)
        if lo_fr(uf) > u: return (1, -1) if G < 0 else (-1, 1)
        if hi_fr(uf) < u: return (-1, -1)
        return None
    if jz > abs(jx - jy):
        if abs(jx * jx - jy * jy) >= jz * jz: return (-1,)
        uf = flip_u(J)
        if lo_fr(uf) > u: return (1,)
        if hi_fr(uf) < u: return (-1,)
    return None

def classify_roots(R, q5, cen):
    """All real roots X of Q in [-1,1]: a root with t^2 = 1 - X^2 > 0 and d^2 = sigma^2 - 4 pi > 0 (iv, strict) is a real orbit and must match the listed centre
    `cen` (|X - cos 2 pi f3| < 1e-6); roots with a definitely negative t^2 or d^2 are not real points; roots of undecided sign or real unlisted orbits count as unlisted.
    Returns (matched [(X, t^2, d^2)], unlisted, number of real roots)."""
    a_c = math.cos(2 * math.pi * cen[2] / E8)
    Xs = roots_in_unit(q5)
    matched = []; unl = 0
    for X in Xs:
        Tt = kval(R.T, X); Dd = kval(R.Dc, X)
        real = lo_fr(Tt) > 0 and lo_fr(Dd) > 0
        nonreal = hi_fr(Tt) < 0 or hi_fr(Dd) < 0
        if nonreal: continue
        if not real or abs(float(X.mid) - a_c) > 1e-6:
            unl += 1; continue
        matched.append((X, Tt, Dd))
    return matched, unl, len(Xs)

def census(name, ctx):
    """Exact/interval census at coupling `name`; returns dict(nodes, ...)."""
    J = COUPLINGS[name]
    jx, jy, jz, kp = J
    iv.prec = 300; mp.mp.prec = 300
    Mr = build_M(J)
    aD = coeffs_at(J, ctx["D"]); aA = coeffs_at(J, ctx["A"])
    rf = Fr(BOXRF.get(name, 5000), E8)
    nodes = []                                  # dict(kind, label, f0, sign, T, zst)
    x_ = sp.symbols("x")
    # ---------------- off-plane orbits: exact ring step, root classification, charges
    ex_off = True; off_txt = []; unlisted = 0; pat_ok = True; off_ctx = []
    for oi, orb in enumerate(OFF.get(name, [])):
        R, z, zi, rel_ok, rel, q5 = offplane_point(orb)
        Qx = sum(c * x_**(len(q5) - 1 - j) for j, c in enumerate(q5))
        fl = sp.factor_list(Qx)
        irr = len(fl[1]) == 1 and fl[1][0][1] == 1
        flags, dat = node_exact(Mr, R, z, zi)
        struct = set(dat["trace"].keys()) == {(1, 1, 1)}
        ex_off = ex_off and irr and rel_ok and all(flags.values()) and struct
        ts0, ds0, cen = orb["image"]
        matched, unl, nroots_off = classify_roots(R, q5, cen)
        unlisted += unl
        nmatch = len(matched)
        for (X, Tt, Dd) in matched:
            first = len(nodes)
            for ts in (1, -1):
                for ds in (1, -1):
                    Tv, a2v, re = charge_iv(dat["trace"], dat["a2"], X, ts * iv.sqrt(Tt), ds * iv.sqrt(Dd))
                    zst = offplane_iv(X, rel, ts, ds)
                    f0 = image_centre(cen, (ts0, ds0), ts, ds)
                    nodes.append(dict(kind="off", label="o%d(t,d)=(%+d,%+d)" % (oi, ts, ds), f0=f0, sign=sgn_iv(Tv), T=Tv, zst=zst, a2=a2v))
            sg = [n["sign"] for n in nodes[first:]]
            pat_ok = pat_ok and (sg[0] == sg[3] != 0 and sg[1] == sg[2] == -sg[0])
        ex_off = ex_off and nmatch == 1
        off_txt.append("Q deg %d irr %s, %d real root, %d orbit" % (len(q5) - 1, irr, nroots_off, nmatch))
    # ---------------- line nodes: exact ring step per irreducible factor, charges, closed form
    ci, nline, facs = line_quadratic(J)
    nroot_fac = 0; ex_line = True; cf_ok = True; lpat_ok = True; line_txt = []
    for fi, cs in enumerate(facs):
        qasc = list(reversed(cs))
        RL, zL, ziL = line_point(qasc)
        flagsL, datL = node_exact(Mr, RL, zL, ziL)
        structL = set(datL["trace"].keys()) == {(1, 0, 1)}
        ex_line = ex_line and all(flagsL.values()) and structL
        TtL_el = RL.T
        for XL in roots_in_unit(cs):
            nroot_fac += 1
            TtL = kval(TtL_el, XL)
            x0 = int(round(math.acos(float(XL.mid)) / (2 * math.pi) * E8))
            first = len(nodes)
            for ts in (1, -1):
                TvL, a2L, reL = charge_iv(datL["trace"], datL["a2"], XL, ts * iv.sqrt(TtL), iv.mpf(1))
                s_ = ts * iv.sqrt(TtL)
                zst = [(XL, s_), (XL, -s_), (iv.mpf(1), iv.mpf(0))]
                f0 = (x0, E8 - x0, 0) if ts == 1 else (E8 - x0, x0, 0)
                nodes.append(dict(kind="line", label="line%d(%+d)" % (fi, ts), f0=f0, sign=sgn_iv(TvL), T=TvL, zst=zst, a2=a2L, cval=float(XL.mid), ts=ts))
            c_ = XL
            qp = 8 * fr_iv(kp * kp) * c_ - 2 * fr_iv(jx * jy)
            Fc = (fr_iv(jx * jy * (jx + jy + jz)) * c_ * c_ + fr_iv((jx + jy) * (jx * jx + jy * jy + jz * (jx + jy))) * c_
                  + fr_iv((jx + jz) * (jy + jz) * (jx + jy - jz)))
            Tcl = -32 * iv.pi ** 3 * fr_iv(kp) * qp * Fc * iv.sqrt(1 - c_ * c_) / fr_iv(jz ** 3)
            diff = nodes[first]["T"] - Tcl
            cf_ok = cf_ok and up_abs(diff) < Fr(1, 10 ** 30) * abs(lo_fr(nodes[first]["T"]))
            lpat_ok = lpat_ok and nodes[first]["sign"] == -nodes[first + 1]["sign"] != 0
        line_txt.append("deg %d, %d roots" % (len(cs) - 1, len(roots_in_unit(cs))))
    ex_line = ex_line and nline == nroot_fac
    nlin = sum(1 for n in nodes if n["kind"] == "line"); noff = len(nodes) - nlin
    cf_txt = ("ok" if cf_ok else "WRONG") if nlin else "n/a"
    if OFF.get(name) or facs:
        check(ctx["ok"] and ex_off and ex_line and unlisted == 0, name + " exact",
              "ring ok: off [%s]; line q %d root(s) [%s]; unlisted %d" % (
                  "; ".join(off_txt) if off_txt else "none", nline, "; ".join(line_txt) if line_txt else "none", unlisted))
    else:
        check(ctx["ok"] and nline == 0 and unlisted == 0, name + " exact", "line q has 0 roots in [-1,1]; no algebraic node listed")
    # ---------------- interval: boxes
    box_ok = True; pivs = []; devs = []; a2s = []
    for nd in nodes:
        hb = hess_box(aD, aA, nd["f0"], rf, nd["zst"])
        nd["hb"] = hb
        okb = hb["pd"] and hb["dev"] <= hb["rho"] and hb["a2low"] > 0
        box_ok = box_ok and okb
        pivs.append(float(hb["pivmin"])); devs.append(float(hb["dev"])); a2s.append(float(hb["a2low"]))
        vemit("   box %s %s f0=%s pivmin %.4g eta %.4g dev %.3g rho %.3g a2low %.4g sign %+d |T| %s" % (
            nd["kind"], nd["label"], nd["f0"], float(hb["pivmin"]), float(hb["eta"]), float(hb["dev"]), float(hb["rho"]), float(hb["a2low"]), nd["sign"],
            mp.nstr(abs(mp.mpf(nd["T"].mid)), 9)))
    disj = True
    for a_, b_ in itertools.combinations(nodes, 2):
        dist = max(min((p - q) % E8, (q - p) % E8) for p, q in zip(a_["f0"], b_["f0"]))
        disj = disj and Fr(dist, E8) > 2 * rf
    nz = all(n["sign"] != 0 for n in nodes)
    total = sum(n["sign"] for n in nodes)
    lx = sorted([n for n in nodes if n["kind"] == "line" and n["ts"] == 1], key=lambda n: n["cval"])
    pred = line_pred(J)
    otri_txt = ""; otri_ok = True
    if pred is not None:
        otri_ok = tuple(n["sign"] for n in lx) == pred
        otri_txt = ", classification %s" % ("ok" if otri_ok else "WRONG")
    offs = [n["sign"] for n in nodes if n["kind"] == "off"]; lins = [n["sign"] for n in nodes if n["kind"] == "line"]
    if nodes:
        check(nz and pat_ok and lpat_ok and cf_ok and box_ok and disj and otri_ok, name + " charges",
              "off %s line %s (closed form %s%s); %d boxes hw %g, pivmin %.3g, arc %.1e, a2 >= %.3g, disjoint %s" % (
                  sgn_str(offs) or "-", sgn_str(lins) or "-", cf_txt, otri_txt, len(nodes), float(rf), min(pivs), max(devs), min(a2s), disj))
    else:
        check(True, name + " charges", "no node, no box")
    # ---------------- interval: clearing
    tay = Taylor(aD)
    boxes = [(nd["f0"], BOXRF.get(name, 5000)) for nd in nodes]
    t1 = time.time()
    clr = clear_torus(tay, boxes, kmax=KMAX)
    clr_ok = clr["outside"] == 0 and (clr["uncleared"] > 0 if nodes else clr["uncleared"] == 0)
    # ---------------- float cross-check
    errs = []
    for nd in nodes:
        fnode = f_from_iv(nd["zst"])
        Tf, kd = float_T(J, fnode)
        Te = float(nd["T"].mid)
        errs.append(abs(Tf - Te) / abs(Te) if kd == 2 else 1.0)
    ferr = max(errs) if errs else 0.0
    check(clr_ok and box_ok and total == 0 and nz and ferr < 1e-8, name + " census",
          "D > 0 outside boxes: level %d, %d cubes, %d uncleared (%d outside), %.0f s; %d nodes = %d off + %d line, sum %+d, float T %.0e" % (
              clr["level"], clr["cubes"], clr["uncleared"], clr["outside"], time.time() - t1, len(nodes), noff, nlin, total, ferr))
    return dict(nodes=nodes, tay=tay, boxes=boxes, aD=aD, aA=aA, clr=clr, Mr=Mr, name=name, facs=facs, ctx=ctx)

def controls(res):
    """negative controls and enclosure sanity checks at the coupling of `res`"""
    name = res["name"]
    nodes, tay, boxes = res["nodes"], res["tay"], res["boxes"]
    lvl = res["clr"]["level"]
    r1 = clear_torus(tay, boxes[1:], kmax=lvl)
    check(r1["outside"] > 0, "control removal", "%s: one box removed: %d uncleared cubes outside the others, level %d (fails as it should)" % (name, r1["outside"], r1["level"]))
    Mr = res["Mr"]
    orb = OFF[name][0]
    q5w = list(orb["Q"]); q5w[-1] += 1
    Rw, zw, ziw, relw, _, _ = offplane_point(orb, q5=q5w)
    fw, _ = node_exact(Mr, Rw, zw, ziw)
    Rf, zf, zif, relf, _, _ = offplane_point(orb, flip_s2=True)
    ff, _ = node_exact(Mr, Rf, zf, zif)
    cs = list(res["facs"][0]); cs[-1] += 1
    RL, zL, ziL = line_point(list(reversed(cs)))
    fL, _ = node_exact(Mr, RL, zL, ziL)
    check(not fw["det"] and not fw["minors"] and not ff["det"] and not ff["minors"] and not fL["minors"], "control exact",
          "%s: Q const + 1, s2 flipped, line factor const + 1: det M, minors nonzero (fail as they should)" % name)
    R0, _, _, _, _, q50 = offplane_point(orb)
    cen_bad = (orb["image"][2][0], orb["image"][2][1], (orb["image"][2][2] + 30000000) % E8)
    mt, ul, _n = classify_roots(R0, q50, cen_bad)
    check(len(mt) == 0 and ul == 1, "control unlisted", "%s: wrong listed centre: matched %d, unlisted %d (detected)" % (name, len(mt), ul))
    nd = nodes[0]
    f0 = (nd["f0"][0] + 40000, nd["f0"][1], nd["f0"][2])
    hb = hess_box(res["aD"], res["aA"], f0, Fr(BOXRF.get(name, 5000), E8), nd["zst"])
    hbc = hess_box(res["aD"], res["aA"], nd["f0"], Fr(100000, E8), nd["zst"])
    check(hb["dev"] > hb["rho"] and not hbc["pd"], "control box geometry",
          "%s: centre moved 4e-4: node outside (arc %.3g > rho %.3g); half-width 1e-3: Hessian test fails (pivmin %.3g)" % (name, float(hb["dev"]), float(hb["rho"]), float(hbc["pivmin"])))
    mp.mp.dps = 50
    ms = np.arange(0, 256, 7)
    cl, ch, sl, sh = Taylor.table(ms, 256)
    miss = 0
    for i, m in enumerate(ms.tolist()):
        cc = mp.cos(2 * mp.pi * m / 256); ss = mp.sin(2 * mp.pi * m / 256)
        miss += not (cl[i] <= cc <= ch[i] and sl[i] <= ss <= sh[i])
    rng = np.random.default_rng(1)
    viol = 0; ncub = 0
    KS = tay.KS; aDf = np.array([float(res["aD"][tuple(k)]) for k in KS.tolist()])
    for k in (3, 5, 8):
        idx = rng.integers(0, 2 ** k, size=(150, 3))
        Lb = tay.lower_bound(idx, k)
        for j in range(len(idx)):
            fc = (2 * idx[j] + 1) / 2.0 ** (k + 1)
            pts = fc + (rng.random((12, 3)) - 0.5) * 2.0 ** (-k)
            Dv = (aDf[None, :] * np.cos(2 * np.pi * pts @ KS.T)).sum(axis=1)
            viol += int((Dv < Lb[j] - 1e-9).sum()); ncub += 1
    check(miss == 0 and viol == 0, "control enclosures", "iv table holds 50-digit cos, sin at %d phases; Taylor bound <= sampled D on %d cubes, %d violations (FLOAT)" % (len(ms), ncub, viol))
    a3 = Fr(6, 25)
    tsyn = Taylor({(1, 0, 0): Fr(1, 2), (-1, 0, 0): Fr(1, 2), (3, 0, 0): a3 / 2, (-3, 0, 0): a3 / 2})
    ks = 4; rho_s = float(tsyn.TWOPI_UP * 2.0 ** (-(ks + 1)))
    wv = -9.0; wn = -9.0
    for i1 in range(2 ** ks):
        Lb = float(tsyn.lower_bound(np.array([[i1, 0, 0]]), ks)[0])
        thv = 2 * np.pi * ((2 * i1 + 1) / 2.0 ** (ks + 1) + np.linspace(-1, 1, 4001) / 2.0 ** (ks + 1))
        tm = float((np.cos(thv) + float(a3) * np.cos(3 * thv)).min())
        wv = max(wv, Lb - tm); wn = max(wn, Lb + tsyn.R3 * rho_s ** 3 - tm)
    check(wv <= 0 and wn > 1e-3, "control remainder", "adversarial D = cos t + 0.24 cos 3t: bound <= sampled min (excess %.2g); without the remainder it exceeds it by %.2g (FLOAT)" % (wv, wn))

def main():
    names = NAMES
    if "-n" in sys.argv: names = tuple(sys.argv[sys.argv.index("-n") + 1].split(","))
    ok, Dsym, Asym = sym_setup()
    ctx = dict(ok=ok, D=Dsym, A=Asym)
    check(ok, "symbolic", "M + M(1/z)^T = 0, char poly mu^4 + a2 mu^2 + D (symbolic couplings): spec H = {+-l1, +-l2}")
    ctrl = None; allres = {}
    for name in names:
        r = census(name, ctx)
        allres[name] = r
        if name == CONTROL_AT: ctrl = r
        vemit("   [%s] t = %.1f s" % (name, time.time() - T0))
    if ctrl is not None: controls(ctrl)
    check(VERBOSE or OUT_BYTES + 260 < 5000, "stdout budget", "%d bytes so far, limit 5000" % OUT_BYTES)
    emit("[INFO] runtime %.1f s (AUDIT_TIMEOUT_SEC = %d), stdout %d bytes" % (time.time() - T0, AUDIT_TIMEOUT_SEC, OUT_BYTES + 60))
    emit("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))

if __name__ == "__main__":
    main()
