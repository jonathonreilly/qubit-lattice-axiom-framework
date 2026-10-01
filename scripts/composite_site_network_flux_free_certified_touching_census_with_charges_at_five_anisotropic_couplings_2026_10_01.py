"""Node census of the supplied anisotropic composite-network comparator at five rational couplings: charges, completeness, total charge.

Supplied model: four-site Bloch matrix H(f) = i M(f), couplings (Jx, Jy, Jz, kappa); M(z) = sum over terms (a, b, n, t): M[a,b] += t z^n,
M[b,a] -= t z^(-n), z_j = exp(2 pi i f_j).  Terms, couplings, integer quintics Q5 and relation polynomials are embedded below (copied from the
quintic-identification runner).  A middle-band touching is a zero of D = det M: the characteristic polynomial of the anti-Hermitian M has no mu^3,
mu^1 term, so spec H = {+-l1, +-l2} and D = (l1 l2)^2.  Couplings: B = (6/5, 4/5, 1; 3/10), A = (1, 4/5, 1; 9/20), C = (1, 4/5, 1; 4/5),
F = (2, 1, 5/2; 9/10), G = (3/2, 1/2, 4/5; 3/2).

For each coupling the script establishes, with exact steps and outward-rounded interval steps (mpmath.iv at 300 bits for point values;
nextafter-rounded IEEE doubles with iv-enclosed phase tables for the torus clearing):
  (1) EXACT: at the algebraic off-plane point (quintic Q5; all four sign images (t, d) at once in the ring Q[alpha, t, d, i]/(...)) and at the line
      node(s) (x, 1-x, 0), cos 2 pi x a root of the line quadratic q(c): M has rank 2 (sixteen 3x3 minors, det, tr vanish; hence adj M = 0 and
      grad D = 0), a2 != 0, Qp = a2 1 + M^2 satisfies Qp^2 = a2 Qp, M Qp = 0, tr Qp = 2 a2 (so Qp/a2 is the kernel projector P), and the charge
      integrand T = Im Tr(P d1H P d2H P d3H) = -8 pi^3 Im Tr(Qp N1 Qp N2 Qp N3)/a2^3, N_j = z_j dM/dz_j, is a ring element c(alpha) t d
      (off-plane) or c(alpha) t (line);
  (2) INTERVAL: sign T at every image from the exact ring element (alpha and the square roots enclosed by iv); the signs obey the I, S, SI
      symmetry pattern and sum to zero; the line node values agree with the closed form -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/Jz^3;
  (3) INTERVAL: the Hessian of D in theta = 2 pi f is positive definite on a box around each node (midpoint Hessian from iv cosines, Frobenius
      bound eta = rho ||S||_F for its change over the box, exact rational LDL), the exact node lies in the box, a2 > 0 on the box.  D is strictly
      convex on the box with an exact critical point where D = 0, so the box contains exactly one zero of D; the boxes are disjoint;
  (4) INTERVAL: clearing of the torus.  Adaptive dyadic cubes; on each cube the second-order Taylor form of D (value, gradient, Hessian at the
      centre from iv-enclosed cosines and sines of the dyadic phases, rational third-derivative remainder) gives a lower bound of D, and a cube
      is cleared when the bound is > 0.  The run ends when every uncleared cube lies inside one node box.  Hence D > 0 on the torus outside the
      boxes and the zero set of D is the node list.
Controls: a removed box, a perturbed quintic, a flipped sign and a moved box centre must fail; the phase table and the Taylor bound are compared with
50-digit values and double samples (FLOAT).  Float diagnostic: T from numpy with the kernel projector at each node.
Prints [PASS]/[FAIL] lines and TOTAL: PASS=N FAIL=M.   Run: nice -n 15 python3 census_runner.py   (single process, about 20 s, under 300 MB; -v for
the long form, -n B,A for a subset)."""
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
COUPLINGS = {  # (Jx, Jy, Jz, kappa) as exact rationals
    "B": (Fr(6, 5), Fr(4, 5), Fr(1, 1), Fr(3, 10)),
    "A": (Fr(1, 1), Fr(4, 5), Fr(1, 1), Fr(9, 20)),
    "C": (Fr(1, 1), Fr(4, 5), Fr(1, 1), Fr(4, 5)),
    "F": (Fr(2, 1), Fr(1, 1), Fr(5, 2), Fr(9, 10)),
    "G": (Fr(3, 2), Fr(1, 2), Fr(4, 5), Fr(3, 2)),
}
Q5 = {  # integer quintic, descending coefficients
    "B": [864, 816, -166396, 837889, 205720, -829767],
    "A": [2686761091215, -52236803198601, 134862005654370, -5777693580942, -195927410075697, -295855810345],
    "C": [-323559360, 4015330704, 4437964845, -14633761482, 9591225363, 9746879930],
    "F": [7936185600, -13738636800, -148594878216, 375269121036, 231788784834, -325717384243],
    "G": [-470888437500, -1739470443750, 2234062696500, -1564217518875, -5666826883970, 44902909367],
}
# image selector of the node orbit: (sign of s3, sign of c1 - c2); 8-digit box centre of (f1, f2, f3) as integers over 10^8
IMAGE = {
    "B": (1, 1, (25505693, 58994705, 4263857)),
    "A": (1, 1, (22299904, 68643705, 25024034)),
    "C": (1, 1, (3526285, 68747588, 34048849)),
    "F": (1, 1, (21102178, 70127486, 11232242)),
    "G": (-1, 1, (5586652, 36728320, 75125841)),
}
# exact rational coefficient lists (ascending powers alpha^0..alpha^4) of sigma = c1+c2, pi = c1 c2, r12 = s1 s2, w = s3 (s1+s2), as (numerator, denominator)
REL = {
    "B": {
        "sigma": [(-8915671241644, 5829855325085), (14260388057896, 17489565975255), (-2346373866944, 17489565975255), (-61959648128, 5829855325085), (7060595616, 5829855325085)],
        "pi": [(256447731374471, 192385225727805), (-843597637422044, 577155677183415), (52872244231616, 577155677183415), (4017765826292, 192385225727805), (-42517638048, 64128408575935)],
        "r12": [(-251484535350124, 192385225727805), (691353695498476, 577155677183415), (-251551149459364, 577155677183415), (4212901116932, 192385225727805), (181869503712, 64128408575935)],
        "w": [(-2008954513477, 1165971065017), (1824219028444, 3497913195051), (5691646059169, 3497913195051), (-222899094812, 1165971065017), (1599837840, 1165971065017)],
    },
    "A": {
        "sigma": [(-399142521604852990579574711, 1806389738407601276972313600), (-35301545512760521955119429, 55752769703938311017664000), (-2027046615517650421624893, 9292128283989718502944000), (3056264451827092943733519, 18584256567979437005888000), (-78474043365715526201919, 7433702627191774802355200)],
        "pi": [(-592462987196206645599102769, 9031948692038006384861568000), (20926595791375199954320043, 557527697039383110176640000), (54413722385612825394330987, 185842565679794370058880000), (-25134694620234480472697073, 185842565679794370058880000), (80645499937367639899281, 9292128283989718502944000)],
        "r12": [(-910188866169986461424511559, 1003549854670889598317952000), (136297017191313268154101019, 185842565679794370058880000), (21342318840284852436341913, 185842565679794370058880000), (-33646257596868308912457027, 185842565679794370058880000), (50465628292347547642647, 4646064141994859251472000)],
        "w": [(734517412581177475365643, 11612505461191722494822016), (-155062630965830923732487, 215046397429476342496704), (-667910878395719978153, 1991170346569225393488), (1187036599820062026159, 2654893795425633857984), (-9217572151545909945, 5309787590851267715968)],
    },
    "C": {
        "sigma": [(3344411137325134499209, 54126631190952834848600), (-490919195779650295563141, 541266311909528348486000), (118741451702771459676843, 541266311909528348486000), (4305912022553302848483, 33829144494345521780375), (-90130456620887421204, 6765828898869104356075)],
        "pi": [(-706983843953100165484337, 2165065247638113393944000), (2686757558699177576545213, 21650652476381133939440000), (939196233618290701952301, 21650652476381133939440000), (-59120273248931142519219, 1353165779773820871215000), (399919815301432362093, 67658288988691043560750)],
        "r12": [(-220567655478087357559563, 2165065247638113393944000), (3022840411461035912204387, 21650652476381133939440000), (-2252931762322255402618101, 21650652476381133939440000), (-34048425053588037880581, 1353165779773820871215000), (219741333963055638507, 67658288988691043560750)],
        "w": [(-118602079501581242817, 154647517688436670996), (-7002074211704733782, 38661879422109167749), (55037962799164395369, 154647517688436670996), (7132629048071577804, 38661879422109167749), (795089715447317040, 38661879422109167749)],
    },
    "F": {
        "sigma": [(1252892411426830241021, 6816812032214946973332), (-3417925901510107871, 11476114532348395578), (845197695542759936, 21039543309305391893), (-215928397656064800, 1912685755391399263), (656760226963478400, 21039543309305391893)],
        "pi": [(15193256287522039702007, 27267248128859787893328), (-21607541944774965455, 22952229064696791156), (8067754989058067665, 252474519711664702716), (358227517662728000, 1912685755391399263), (-929804432003937000, 21039543309305391893)],
        "r12": [(-12903794444867533951163, 9089082709619929297776), (15408428000678392487, 22952229064696791156), (-2341742030404622793, 84158173237221567572), (22559751455259200, 1912685755391399263), (-338109830642089800, 21039543309305391893)],
        "w": [(-408618685580650529098, 464782638560110020909), (42622036995402355025, 56337289522437578292), (94154675230904439869, 103285030791135560202), (-301801503683085980, 521641569652199799), (234423885971268000, 1912685755391399263)],
    },
    "G": {
        "sigma": [(48957755006296777475720548, 175057539358066779561712425), (-56203774633254140506637234, 35011507871613355912342485), (1653578529056576166357100, 2334100524774223727489499), (-45195161095745951902300, 259344502752691525276611), (-2321155440562249785000, 28816055861410169475179)],
        "pi": [(-39101677276320531152391203669, 60394851078533038948790786625), (25172925943019346969868458286, 12078970215706607789758157325), (-920516327655355581438001484, 805264681047107185983877155), (8089226607007098129499780, 17894770689935715244086159), (112166904472935386971000, 662769284812433897929117)],
        "r12": [(14919962490475552008820814236, 60394851078533038948790786625), (11692748243529699482450020876, 12078970215706607789758157325), (-684639962132382245360746064, 805264681047107185983877155), (4939354909176277357819480, 17894770689935715244086159), (69343009956727542256000, 662769284812433897929117)],
        "w": [(-403352889483742131039278818, 375123298624428813346526625), (-87176728248568115590567786, 75024659724885762669305325), (5835619392253065943487852, 5001643981659050844620355), (-25754076529926832342684, 111147644036867796547119), (-455548162942546312600, 4116579408772881353597)],
    },
}
NAMES = ("B", "A", "C", "F", "G")
# node-box half-width in f units, as an integer over 10^8 (theta radius rho = 2 pi * value)
BOXRF = {"B": 5000, "A": 5000, "C": 5000, "F": 5000, "G": 5000}
E8 = 10 ** 8

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

# ---------------------------------------------------------------- Bloch matrix at exact couplings, Fourier data
z1, z2, z3 = sp.symbols("z1 z2 z3")

def srat(q):
    q = Fr(q); return sp.Rational(q.numerator, q.denominator)

def build_M(J):
    jx, jy, jz, kk = (srat(v) for v in J)
    amp = {"x": 2 * jx, "y": 2 * jy, "z": 2 * jz, "odd": 2 * kk}
    M = sp.zeros(4, 4)
    for (a, b, n, kind) in TERMS:
        mon = z1 ** n[0] * z2 ** n[1] * z3 ** n[2]
        M[a, b] += amp[kind] * mon
        M[b, a] -= amp[kind] / mon
    return M.applyfunc(sp.expand)

def tcoeffs(expr):
    """exact Fourier coefficients {k: a_k} of a Laurent polynomial with exponents in [-3, 3]"""
    P = sp.Poly(sp.expand(sp.expand(expr) * z1**3 * z2**3 * z3**3), z1, z2, z3)
    return {(a - 3, b - 3, c - 3): Fr(int(v.p), int(v.q)) for (a, b, c), v in P.terms()}

def char_data(Mr):
    mu = sp.symbols("mu")
    Minv = Mr.subs({z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}, simultaneous=True)
    ah = (Mr + Minv.T).applyfunc(sp.expand) == sp.zeros(4, 4)
    cp = sp.Poly(sp.expand((mu * sp.eye(4) - Mr).det(method="berkowitz")), mu)
    co = {e[0]: sp.expand(c) for e, c in cp.terms()}
    ok = ah and co.get(3, 0) == 0 and co.get(1, 0) == 0 and co[4] == 1
    return ok, co

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

def offplane_point(name, q5=None, flip_s2=False):
    """Ring R and point (z, zi) of the off-plane orbit at coupling `name`; relation identities returned as flags."""
    q5 = Q5[name] if q5 is None else q5
    rel = {kq: [Fr(n, d) for (n, d) in REL[name][kq]] for kq in REL[name]}
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

# ---------------------------------------------------------------- interval helpers (mpmath.iv, outward rounding)
def lo_fr(xv):
    p, q = to_rational(xv._mpi_[0]); return Fr(p, q)
def hi_fr(xv):
    p, q = to_rational(xv._mpi_[1]); return Fr(p, q)
def fr_iv(q):
    q = Fr(q); return iv.mpf(q.numerator) / iv.mpf(q.denominator)
def up_abs(xv): return max(abs(lo_fr(xv)), abs(hi_fr(xv)))

def root_in_unit(coeffs_desc):
    """Exact rational isolating interval (a, b) of the unique real root in [-1, 1] of the integer polynomial, and its iv enclosure."""
    x = sp.symbols("x")
    deg = len(coeffs_desc) - 1
    P = sp.Poly(sum(c * x ** (deg - j) for j, c in enumerate(coeffs_desc)), x)
    ivs = [(a_, b_) for (a_, b_), _ in P.intervals(eps=sp.Rational(1, 10**50)) if a_ >= -1 and b_ <= 1]
    assert len(ivs) == 1, "root count %d" % len(ivs)
    a_lo, a_hi = Fr(int(ivs[0][0].p), int(ivs[0][0].q)), Fr(int(ivs[0][1].p), int(ivs[0][1].q))
    Xlo = fr_iv(a_lo); Xhi = fr_iv(a_hi)
    X = iv.make_mpf((Xlo._mpi_[0], Xhi._mpi_[1]))
    assert lo_fr(X) <= a_lo and hi_fr(X) >= a_hi
    return X

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

def offplane_iv(name, X, q5, rel, tsign, dsign):
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

def clear_torus(tay, boxes, k0=3, kmax=21, chunk=20000):
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

def line_quadratic(J):
    """integer coefficients (descending) of q(c) = 4k^2 c^2 - 2 Jx Jy c + Jz^2 - Jx^2 - Jy^2 - 4k^2 and its irreducible factors with a root in [-1, 1]."""
    jx, jy, jz, kk = J
    cf = [4 * kk * kk, -2 * jx * jy, jz * jz - jx * jx - jy * jy - 4 * kk * kk]
    den = functools.reduce(lambda a, b: a * b // math.gcd(a, b), (c.denominator for c in cf), 1)
    ci = [int(c * den) for c in cf]
    c_ = sp.symbols("c")
    P = sp.Poly(ci[0] * c_**2 + ci[1] * c_ + ci[2], c_)
    nroots = P.count_roots(-1, 1)
    facs = []
    for fpoly, _m in sp.factor_list(P.as_expr())[1]:
        fp = sp.Poly(fpoly, c_)
        if fp.count_roots(-1, 1) == 1:
            cs = [int(v) for v in fp.all_coeffs()]
            g = functools.reduce(math.gcd, cs)
            facs.append([v // g for v in cs])
    return ci, nroots, facs

def census(name, detail=True):
    """Exact/interval census at coupling `name`; returns dict(nodes, ...)."""
    J = COUPLINGS[name]
    jx, jy, jz, kp = J
    iv.prec = 300; mp.mp.prec = 300
    Mr = build_M(J)
    s1ok, co = char_data(Mr)
    aD = tcoeffs(co[0]); aA = tcoeffs(co[2])
    rf = Fr(BOXRF[name], E8)
    nodes = []                                  # dict(kind, label, f0, sign, T)
    # ---------------- exact: off-plane orbit
    R, z, zi, rel_ok, rel, q5 = offplane_point(name)
    x_ = sp.symbols("x")
    Qx = sum(c * x_**(5 - j) for j, c in enumerate(q5))
    fl = sp.factor_list(Qx)
    irr = len(fl[1]) == 1 and fl[1][0][1] == 1
    nroot = sp.Poly(Qx, x_).count_roots(-1, 1)
    flags, dat = node_exact(Mr, R, z, zi)
    struct = set(dat["trace"].keys()) == {(1, 1, 1)}
    ex_off = irr and nroot == 1 and rel_ok and all(flags.values()) and struct
    # ---------------- exact: line nodes
    ci, nline, facs = line_quadratic(J)
    ex_line = (nline == len(facs))
    if facs:
        qasc = list(reversed(facs[0]))
        RL, zL, ziL = line_point(qasc)
        flagsL, datL = node_exact(Mr, RL, zL, ziL)
        structL = set(datL["trace"].keys()) == {(1, 0, 1)}
        ex_line = ex_line and all(flagsL.values()) and structL
    check(s1ok and ex_off and ex_line, name + " exact", "Q5 irreducible %s, %d root in [-1,1]; ring rank 2 (16 minors, det, tr), Qp^2=a2 Qp, M Qp=0, tr Qp=2 a2, T=c(alpha) t d; line quadratic %d root(s) in [-1,1]; spectrum even" % (irr, nroot, nline))
    # ---------------- interval: charges
    X = root_in_unit(q5)
    Tt = kval(R.T, X); Dd = kval(R.Dc, X)
    base_signs, base_signs2, cen = IMAGE[name]
    base_signs = (base_signs, base_signs2)
    offs = {}
    for ts in (1, -1):
        for ds in (1, -1):
            Tv, a2v, re = charge_iv(dat["trace"], dat["a2"], X, ts * iv.sqrt(Tt), ds * iv.sqrt(Dd))
            zst = offplane_iv(name, X, q5, rel, ts, ds)
            f0 = image_centre(cen, base_signs, ts, ds)
            nodes.append(dict(kind="off", label="(t,d)=(%+d,%+d)" % (ts, ds), f0=f0, sign=sgn_iv(Tv), T=Tv, zst=zst, a2=a2v, resT=re))
    off_signs = [n["sign"] for n in nodes]
    sym_ok = (off_signs[0] == off_signs[3] != 0 and off_signs[1] == off_signs[2] == -off_signs[0])
    Tabs = nodes[0]["T"]
    # ---------------- interval: line node charges (+ closed form cross-check)
    line_info = ""
    if facs:
        XL = root_in_unit(facs[0])
        TtL = kval(RL.T, XL)
        x0 = int(round(math.acos(float(XL.mid)) / (2 * math.pi) * E8))
        for ts in (1, -1):
            TvL, a2L, reL = charge_iv(datL["trace"], datL["a2"], XL, ts * iv.sqrt(TtL), iv.mpf(1))
            s_ = ts * iv.sqrt(TtL)
            zst = [(XL, s_), (XL, -s_), (iv.mpf(1), iv.mpf(0))]
            f0 = (x0, E8 - x0, 0) if ts == 1 else (E8 - x0, x0, 0)
            nodes.append(dict(kind="line", label="line(%+d)" % ts, f0=f0, sign=sgn_iv(TvL), T=TvL, zst=zst, a2=a2L, resT=reL))
        # closed form of the line-family triple product for the node (x, 1-x, 0), x < 1/2: T = -32 pi^3 kappa q'(c) F_c(c) sin(2 pi x)/Jz^3
        c_ = XL
        qp = 8 * fr_iv(kp * kp) * c_ - 2 * fr_iv(jx * jy)
        Fc = (fr_iv(jx * jy * (jx + jy + jz)) * c_ * c_ + fr_iv((jx + jy) * (jx * jx + jy * jy + jz * (jx + jy))) * c_
              + fr_iv((jx + jz) * (jy + jz) * (jx + jy - jz)))
        Tcl = -32 * iv.pi ** 3 * fr_iv(kp) * qp * Fc * iv.sqrt(1 - c_ * c_) / fr_iv(jz ** 3)
        diff = nodes[4]["T"] - Tcl
        cf_ok = up_abs(diff) < Fr(1, 10 ** 30) * abs(lo_fr(nodes[4]["T"]))
        line_ok_sym = nodes[4]["sign"] == -nodes[5]["sign"] != 0
        line_info = " (|T|=%s, closed form agrees %s)" % (mp.nstr(abs(mp.mpf(nodes[4]["T"].mid)), 8), cf_ok)
        sym_ok = sym_ok and line_ok_sym and cf_ok
    total = sum(n["sign"] for n in nodes)
    nz = all(n["sign"] != 0 for n in nodes)
    check(nz and sym_ok, name + " charges", "sign T (iv) %s at (t,d)=(+,+),(+,-),(-,+),(-,-), |T|=%s; line %s%s" % (
        ",".join("%+d" % v for v in off_signs), mp.nstr(abs(mp.mpf(Tabs.mid)), 9),
        ",".join("%+d" % n["sign"] for n in nodes[4:]) if facs else "none", line_info))
    # ---------------- interval: boxes
    box_ok = True; pivs = []; devs = []; a2s = []
    for nd in nodes:
        hb = hess_box(aD, aA, nd["f0"], rf, nd["zst"])
        nd["hb"] = hb
        okb = hb["pd"] and hb["dev"] <= hb["rho"] and hb["a2low"] > 0
        box_ok = box_ok and okb
        pivs.append(float(hb["pivmin"])); devs.append(float(hb["dev"])); a2s.append(float(hb["a2low"]))
        vemit("   box %s %s f0=%s pivmin %.4g eta %.4g dev %.3g rho %.3g a2low %.4g" % (nd["kind"], nd["label"], nd["f0"], float(hb["pivmin"]), float(hb["eta"]), float(hb["dev"]), float(hb["rho"]), float(hb["a2low"])))
    # boxes pairwise disjoint (periodic sup distance of centres > 2 rf)
    disj = True
    for a_, b_ in itertools.combinations(nodes, 2):
        dist = max(min((p - q) % E8, (q - p) % E8) for p, q in zip(a_["f0"], b_["f0"]))
        disj = disj and Fr(dist, E8) > 2 * rf
    check(box_ok and disj, name + " boxes", "%d, half-width %.2g: Hessian PD (min pivot %.3g), node inside (arc %.2g <= rho %.2g), a2 >= %.4g, disjoint" % (
        len(nodes), float(rf), min(pivs), max(devs), float(max(n["hb"]["rho"] for n in nodes)), min(a2s)))
    # ---------------- interval: clearing
    tay = Taylor(aD)
    boxes = [(nd["f0"], BOXRF[name]) for nd in nodes]
    t1 = time.time()
    clr = clear_torus(tay, boxes)
    clr_ok = clr["outside"] == 0 and clr["uncleared"] > 0
    check(clr_ok, name + " clearing", "D > 0 outside the boxes: level %d (half-width %.2g), %d cubes, %d uncleared of which %d outside the boxes, %.1f s" % (
        clr["level"], 2.0 ** -(clr["level"] + 1), clr["cubes"], clr["uncleared"], clr["outside"], time.time() - t1))
    # ---------------- float cross-check
    errs = []
    for nd in nodes:
        fnode = f_from_iv(nd["zst"])
        Tf, kd = float_T(J, fnode)
        Te = float(nd["T"].mid)
        errs.append(abs(Tf - Te) / abs(Te) if kd == 2 else 1.0)
    # ---------------- census statement
    nn = len(nodes)
    check(clr_ok and box_ok and total == 0 and nz and max(errs) < 1e-8, name + " census", "%d touchings = 4 off-plane + %d line; charges %s, total %+d; float T agrees %.1e" % (
        nn, nn - 4, ",".join("%+d" % n["sign"] for n in nodes), total, max(errs)))
    return dict(nodes=nodes, tay=tay, boxes=boxes, aD=aD, aA=aA, clr=clr, X=X, q5=q5, Mr=Mr)

def controls(res):
    """negative controls at B and enclosure sanity checks"""
    name = "B"
    nodes, tay, boxes = res["nodes"], res["tay"], res["boxes"]
    # c1: removing one node box must leave uncleared cubes outside the remaining boxes at the finest level reached
    lvl = res["clr"]["level"]
    r1 = clear_torus(tay, boxes[1:], kmax=lvl)
    check(r1["outside"] > 0, "control box", "one box removed: %d uncleared cubes outside the others at level %d (fails as it should)" % (r1["outside"], r1["level"]))
    # c2: perturbed quintic and flipped s2 must destroy the exact rank-2 point
    Mr = res["Mr"]
    q5w = list(Q5[name]); q5w[-1] += 1
    Rw, zw, ziw, relw, _, _ = offplane_point(name, q5=q5w)
    fw, _ = node_exact(Mr, Rw, zw, ziw)
    Rf, zf, zif, relf, _, _ = offplane_point(name, flip_s2=True)
    ff, _ = node_exact(Mr, Rf, zf, zif)
    check(not fw["det"] and not fw["minors"] and not ff["det"] and not ff["minors"], "control exact",
          "Q5 constant + 1, or s2 sign flipped: det M, minors nonzero (fail as they should)")
    # c3: moved box centre must fail containment
    nd = nodes[0]
    f0 = (nd["f0"][0] + 40000, nd["f0"][1], nd["f0"][2])
    hb = hess_box(res["aD"], res["aA"], f0, Fr(BOXRF[name], E8), nd["zst"])
    check(hb["dev"] > hb["rho"], "control box centre", "box centre moved by 4e-4 in f1: node outside (arc %.3g > rho %.3g)" % (float(hb["dev"]), float(hb["rho"])))
    # c4: enclosure sanity: iv phase table against 50-digit mpmath, Taylor lower bound against double-precision samples of D
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
    check(miss == 0 and viol == 0, "control enclosures", "iv table contains 50-digit cos, sin at %d phases; Taylor bound <= sampled D on %d random cubes (levels 3, 5, 8), violations %d (FLOAT sample)" % (len(ms), ncub, viol))

def main():
    names = NAMES
    if "-n" in sys.argv: names = tuple(sys.argv[sys.argv.index("-n") + 1].split(","))
    res = None
    for name in names:
        r = census(name)
        if name == "B": res = r
        vemit("   [%s] t = %.1f s" % (name, time.time() - T0))
    if res is not None: controls(res)
    emit("[INFO] runtime %.1f s (AUDIT_TIMEOUT_SEC = %d), stdout %d bytes" % (time.time() - T0, AUDIT_TIMEOUT_SEC, OUT_BYTES))
    emit("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))

if __name__ == "__main__":
    main()

