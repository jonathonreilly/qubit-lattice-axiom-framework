"""Off-plane touchings of the supplied anisotropic comparator (J_x != J_y): exact identification at five rational couplings.

Supplied model: four-site Bloch matrix H(f) = i M(f) of the composite-site comparator network, couplings (Jx, Jy, Jz, kappa);
M(z) = sum over terms (a, b, n, t):  M[a,b] += t z^n,  M[b,a] -= t z^(-n),  z_j = exp(2 pi i f_j).

This single self-contained script prints [PASS]/[FAIL] lines for
  (a) M anti-Hermitian on the torus and a characteristic polynomial without mu^3, mu^1 terms (symbolic couplings);
  (b) structure identities (symbolic couplings): H = [[h_x, iW],[-iW^dag, h_y]], W W^dag = lambda^2 1, |d_x|^2 det M = s1^2+s2^2+s3^2, |d_x|^2 >= (2Jx-2Jy)^2;
  (c) for each coupling B, A, C, F, G: Q5 irreducible with one root in [-1, 1]; exact ring verification of the algebraic node (six relation and unit-circle
      identities, sixteen 3x3 minors, det M, tr M, a2 nonzero); outward-rounded interval box certificate (S2) Hessian pivots, (S3) containment, (S4) a2 > 0;
  (d) negative controls at B (perturbed sigma coefficient, flipped s2, wrong Q5 constant must give nonzero minors);
  (e) minimal polynomial N10 of c1 at B: degree 10, irreducible, c1 and c2 are roots (exact); cross-check at A against an embedded earlier PSLQ polynomial.
The node is described by alpha = c3 (a root of the integer quintic Q5) and four rational polynomials of degree 4 in alpha:
sigma = c1 + c2, pi = c1 c2, r12 = s1 s2, w = s3 (s1 + s2).  The polynomials were found numerically (PSLQ) and are embedded below as literals;
the exact checks in this script are what establish them.
Exact steps: Fractions / sympy.  Interval steps: mpmath.iv (300 bits, outward rounding) combined with exact Fractions.
Run: python3 <this script>   (single process, a few seconds, under 100 MB)."""
AUDIT_TIMEOUT_SEC = 900
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys
import time
import itertools
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp
from mpmath.libmp import to_rational

T0 = time.time()
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
# earlier PSLQ polynomial of cos(2 pi f1) at A (degree 10, descending integer coefficients), embedded for the proportionality cross-check
N10_A_PSLQ = [853448585920008264, 94736216839347861552, 375130234123113112668, 610710543338153996592, 550754366751654130602,
              336593198079779698764, 155784673239596928515, 45252907101346784356, 3627747217837094412, -1420821403391966840, -269513067616356085]
NAMES = ("B", "A", "C", "F", "G")
RHO = Fr(1, 10**6)          # box radius in angle units
PASS = 0
FAIL = 0
OUT_BYTES = 0

def emit(s):
    global OUT_BYTES
    OUT_BYTES += len(s) + 1
    print(s, flush=True)

def check(ok, label, detail):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    emit("[%s] %s: %s" % ("PASS" if ok else "FAIL", label, detail))

# ---------------------------------------------------------------- exact tower arithmetic (inlined)
class Field:
    """K = Q[alpha]/(q), q given by integer coefficients in ascending order; elements are tuples of Fractions."""
    def __init__(self, q_asc):
        self.n = len(q_asc) - 1
        lead = Fr(q_asc[-1])
        self.mon = [Fr(c) / lead for c in q_asc]
    def zero(self): return tuple(Fr(0) for _ in range(self.n))
    def one(self): return tuple([Fr(1)] + [Fr(0)] * (self.n - 1))
    def const(self, c): return tuple([Fr(c)] + [Fr(0)] * (self.n - 1))
    def alpha(self): return tuple([Fr(0), Fr(1)] + [Fr(0)] * (self.n - 2))
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

# ---------------------------------------------------------------- symbolic Bloch matrix
Jx, Jy, Jz, kap = sp.symbols("Jx Jy Jz kappa", positive=True)
z1, z2, z3 = sp.symbols("z1 z2 z3")

def build_M():
    amp = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz, "odd": 2 * kap}
    M = sp.zeros(4, 4)
    for (a, b, n, kind) in TERMS:
        t = amp[kind]
        mon = z1 ** n[0] * z2 ** n[1] * z3 ** n[2]
        M[a, b] += t * mon
        M[b, a] -= t / mon
    return M

def tcoeffs(expr):
    """exact Fourier coefficients {k: a_k} of a Laurent polynomial with exponents in [-3, 3]"""
    P = sp.Poly(sp.expand(sp.expand(expr) * z1**3 * z2**3 * z3**3), z1, z2, z3)
    return {(a - 3, b - 3, c - 3): Fr(int(v.p), int(v.q)) for (a, b, c), v in P.terms()}

# ---------------------------------------------------------------- (a) anti-Hermiticity and characteristic polynomial (symbolic couplings)
def check_a(Msym):
    mu = sp.symbols("mu")
    Minv = Msym.subs({z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}, simultaneous=True)
    ah = (Msym + Minv.T).applyfunc(sp.expand) == sp.zeros(4, 4)
    cp = sp.Poly(sp.expand((mu * sp.eye(4) - Msym).det(method="berkowitz")), mu)
    co = {e[0]: sp.expand(c) for e, c in cp.terms()}
    ok = ah and co.get(3, 0) == 0 and co.get(1, 0) == 0 and co[4] == 1
    check(ok, "a", "M + M(1/z)^T = 0 (anti-Hermitian on the torus); char poly mu^4 + a2 mu^2 + D with mu^3, mu^1 coefficients zero (symbolic Jx,Jy,Jz,kappa) => D = l1^2 l2^2 >= 0")
    return co

# ---------------------------------------------------------------- (b) structure identities (symbolic couplings)
def check_b(Msym, co):
    a, b, c, k = sp.symbols("a b c k", positive=True)
    M = Msym.subs({Jx: a / 2, Jy: b / 2, Jz: c / 2, kap: k / 2})
    x, y, u = z1, z2, z3
    v = 1 / u
    conj = lambda e: sp.expand(e.subs({x: 1 / x, y: 1 / y, u: 1 / u}, simultaneous=True).subs(sp.I, -sp.I))
    sg = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    dag = lambda Mx: Mx.T.applyfunc(conj)
    def vec(Mx): return [sp.expand((s * Mx).trace() / 2) for s in sg]
    s1 = (x - 1 / x) / (2 * sp.I); c1 = (x + 1 / x) / 2; s2 = (y - 1 / y) / (2 * sp.I); c2 = (y + 1 / y) / 2
    dxv = sp.Matrix([b * s1, -(a + b * c1), -2 * k * s1]); dyv = sp.Matrix([b * s2, -(a + b * c2), -2 * k * s2])
    hx = M[:2, :2] * sp.I; hy = M[2:, 2:] * sp.I; Wm = M[:2, 2:]
    zero2 = sp.zeros(2, 2)
    f_hx = (hx - sum((dxv[i] * sg[i] for i in range(3)), zero2)).applyfunc(sp.expand) == zero2
    f_hy = (hy - sum((dyv[i] * sg[i] for i in range(3)), zero2)).applyfunc(sp.expand) == zero2
    w = k * (1 / x - 1) + k * (1 - y) * v
    f_W = (Wm - sp.Matrix([[w, c * v], [-c, v * conj(w)]])).applyfunc(sp.expand) == zero2
    f_ba = (M[2:, :2] + dag(Wm)).applyfunc(sp.expand) == zero2
    lam2 = sp.expand(w * conj(w) + c**2)
    f_unit = (Wm * dag(Wm) - lam2 * sp.eye(2)).applyfunc(sp.expand) == zero2
    check(f_hx and f_hy and f_W and f_ba and f_unit, "b1", "H = [[h_x, iW],[-iW^dag, h_y]], h_x = d(th1).sigma, h_y = d(th2).sigma, W = [[w, c v],[-c, v conj(w)]]; W W^dag = lambda^2 1 with lambda^2 = |w|^2 + c^2 (symbolic)")
    e = vec(dag(Wm) * hx * Wm)
    dx2 = sp.expand(dxv.dot(dxv)); dy2 = sp.expand(dyv.dot(dyv))
    D = sp.expand(M.det(method="berkowitz"))
    D_from_co = sp.expand(co[0].subs({Jx: a / 2, Jy: b / 2, Jz: c / 2, kap: k / 2}))
    f_det = sp.expand(D - (lam2**2 + dx2 * dy2 - 2 * sum(dyv[i] * e[i] for i in range(3)))) == 0
    s = [sp.expand(dx2 * dyv[i] - e[i]) for i in range(3)]
    f_sos = sp.expand(dx2 * D - sum(si**2 for si in s)) == 0
    f_norm = sp.expand(sum(ei**2 for ei in e) - lam2**2 * dx2) == 0
    check(f_det and f_sos and f_norm and sp.expand(D - D_from_co) == 0, "b2", "det M = lambda^4 + |d_x|^2|d_y|^2 - 2 d_y.e, |e|^2 = lambda^4 |d_x|^2, and |d_x|^2 det M = s1^2 + s2^2 + s3^2 with s = |d_x|^2 d_y - e (symbolic)")
    f_bound = sp.expand(dx2 - (a - b)**2 - (2 * a * b * (1 + c1) + 4 * k**2 * s1**2)) == 0
    check(f_bound, "b3", "|d_x|^2 = (2Jx-2Jy)^2 + 2ab(1 + cos th1) + 4k^2 sin^2 th1 (exact identity, every term >= 0), so |d_x|^2 >= (2Jx-2Jy)^2 > 0 for Jx != Jy")

# ---------------------------------------------------------------- exact ring verification of the algebraic node
def to_frac_list(lst): return [Fr(n, d) for (n, d) in lst]

def exact_verify(Mr, q5, rel, flips=(), sigma_shift=Fr(0)):
    """Mr: 4x4 sympy matrix with exact rational couplings.  rel: dict of coefficient lists (Fractions, ascending).
    Returns (results dict, nonzero minors, ring context)."""
    K = Field(list(reversed(q5)))
    sig_l = list(rel["sigma"]); sig_l[0] = sig_l[0] + sigma_shift
    sigma = K.poly(sig_l); pi_ = K.poly(rel["pi"]); r12 = K.poly(rel["r12"]); w = K.poly(rel["w"])
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
    if "s1" in flips: s1 = R.smul(-1, s1)
    if "s2" in flips: s2 = R.smul(-1, s2)
    if "s3" in flips: s3 = R.smul(-1, s3)
    one = R.lift(K.one())
    res = {}
    res["c1c2=pi"] = R.is_zero(R.sub(R.mul(c1, c2), R.lift(pi_)))
    res["s1s2=r12"] = R.is_zero(R.sub(R.mul(s1, s2), R.lift(r12)))
    res["s3(s1+s2)=w"] = R.is_zero(R.sub(R.mul(s3, R.add(s1, s2)), R.lift(w)))
    res["c1^2+s1^2=1"] = R.is_zero(R.sub(R.add(R.mul(c1, c1), R.mul(s1, s1)), one))
    res["c2^2+s2^2=1"] = R.is_zero(R.sub(R.add(R.mul(c2, c2), R.mul(s2, s2)), one))
    res["c3^2+s3^2=1"] = R.is_zero(R.sub(R.add(R.mul(c3, c3), R.mul(s3, s3)), one))
    z = [R.add(c1, R.mul(I, s1)), R.add(c2, R.mul(I, s2)), R.add(c3, R.mul(I, s3))]
    zi = [R.sub(c1, R.mul(I, s1)), R.sub(c2, R.mul(I, s2)), R.sub(c3, R.mul(I, s3))]
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
    Mv = [[eval_laurent(Mr[a_, b_]) for b_ in range(4)] for a_ in range(4)]
    def det3(rows, cols):
        m = [[Mv[r][c] for c in cols] for r in rows]
        mm = R.mul
        t1 = mm(m[0][0], R.sub(mm(m[1][1], m[2][2]), mm(m[1][2], m[2][1])))
        t2 = mm(m[0][1], R.sub(mm(m[1][0], m[2][2]), mm(m[1][2], m[2][0])))
        t3 = mm(m[0][2], R.sub(mm(m[1][0], m[2][1]), mm(m[1][1], m[2][0])))
        return R.add(R.sub(t1, t2), t3)
    nz = sum(0 if R.is_zero(det3(rr, cc)) else 1 for rr in itertools.combinations(range(4), 3) for cc in itertools.combinations(range(4), 3))
    res["minors"] = (nz == 0)
    det = R.zero()
    for c in range(4):
        cols = [x_ for x_ in range(4) if x_ != c]
        det = R.add(det, R.smul(1 if c % 2 == 0 else -1, R.mul(Mv[0][c], det3((1, 2, 3), cols))))
    res["det=0"] = R.is_zero(det)
    tr = R.zero()
    for a_ in range(4): tr = R.add(tr, Mv[a_][a_])
    res["tr=0"] = R.is_zero(tr)
    a2 = R.zero()
    for a_, b_ in itertools.combinations(range(4), 2):
        a2 = R.add(a2, R.sub(R.mul(Mv[a_][a_], Mv[b_][b_]), R.mul(Mv[a_][b_], Mv[b_][a_])))
    res["a2!=0"] = not R.is_zero(a2)
    return res, nz, dict(R=R, K=K, c1=c1, c2=c2, sigma=sigma, pi=pi_)

# ---------------------------------------------------------------- interval box certificate
def lo_fr(xv):
    p, q = to_rational(xv._mpi_[0]); return Fr(p, q)
def hi_fr(xv):
    p, q = to_rational(xv._mpi_[1]); return Fr(p, q)

def box_cert(name, Dn, A2n, q5, rel):
    iv = mp.iv; iv.prec = 300; mp.mp.prec = 300
    def fr_iv(q):
        q = Fr(q); return iv.mpf(q.numerator) / iv.mpf(q.denominator)
    def up(xv): return max(abs(lo_fr(xv)), abs(hi_fr(xv)))
    aD = tcoeffs(Dn); aA = tcoeffs(A2n)
    assert all(aD.get(tuple(-q for q in kk)) == vv for kk, vv in aD.items()), "D not inversion symmetric"
    tsign, dsign, cent = IMAGE[name]
    f0 = [Fr(n, 10**8) for n in cent]
    PI = iv.pi
    th0 = [2 * PI * fr_iv(q) for q in f0]
    S = [[Fr(0)] * 3 for _ in range(3)]
    Hiv = [[iv.mpf(0)] * 3 for _ in range(3)]
    for kk in aD:
        arg = sum((kk[j] * th0[j] for j in range(3)), iv.mpf(0))
        cs = iv.cos(arg); a = fr_iv(aD[kk]); l1k = sum(abs(q) for q in kk)
        for i in range(3):
            for j in range(i, 3):
                Hiv[i][j] = Hiv[i][j] - a * (kk[i] * kk[j]) * cs
                S[i][j] += abs(aD[kk]) * abs(kk[i] * kk[j]) * l1k
    eta = Fr(0)
    Hmid = [[Fr(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(i, 3):
            mid = (lo_fr(Hiv[i][j]) + hi_fr(Hiv[i][j])) / 2
            rad = (hi_fr(Hiv[i][j]) - lo_fr(Hiv[i][j])) / 2
            Hmid[i][j] = Hmid[j][i] = mid
            eta += (1 if i == j else 2) * (rad + RHO * S[i][j])
    Lm = [[Hmid[i][j] - (eta if i == j else 0) for j in range(3)] for i in range(3)]
    piv = []
    s2_ok = True
    for i in range(3):
        p = Lm[i][i]; piv.append(p)
        if p <= 0: s2_ok = False; break
        for r in range(i + 1, 3):
            fct = Lm[r][i] / p
            for cc in range(i, 3): Lm[r][cc] -= fct * Lm[i][cc]
    # root alpha0 of Q5 inside [-1, 1] (unique by the exact count), exact rational isolating interval
    x = sp.symbols("x")
    Q = sp.Poly(sum(c * x**(5 - j) for j, c in enumerate(q5)), x)
    ivs = [(a_, b_) for (a_, b_), _ in Q.intervals(eps=sp.Rational(1, 10**50)) if a_ >= -1 and b_ <= 1]
    assert len(ivs) == 1
    a_lo, a_hi = Fr(int(ivs[0][0].p), int(ivs[0][0].q)), Fr(int(ivs[0][1].p), int(ivs[0][1].q))
    Xlo = fr_iv(a_lo); Xhi = fr_iv(a_hi)
    X = iv.make_mpf((Xlo._mpi_[0], Xhi._mpi_[1]))
    assert lo_fr(X) <= a_lo and hi_fr(X) >= a_hi
    def relpoly(lst):
        s_ = iv.mpf(0)
        for j, cf in enumerate(lst): s_ += fr_iv(cf) * X**j
        return s_
    sigma, pi_, r12, w = (relpoly(rel[kq]) for kq in ("sigma", "pi", "r12", "w"))
    T = 1 - X * X
    Dc = sigma * sigma - 4 * pi_
    Tpos = lo_fr(T) > 0; Dcpos = lo_fr(Dc) > 0
    if not (Tpos and Dcpos):
        return dict(s2=s2_ok, pivmin=min(piv), eta=eta, dev=Fr(1), a2low=Fr(-1), Tpos=Tpos, Dcpos=Dcpos, alpha=None, f=None)
    t = tsign * iv.sqrt(T); d = dsign * iv.sqrt(Dc)
    c1 = (sigma + d) / 2; c2 = (sigma - d) / 2; c3 = X; s3 = t
    sp_ = w * t / T; sm_ = -sigma * d * t / w
    s1 = (sp_ + sm_) / 2; s2v = (sp_ - sm_) / 2
    devs = []
    fvals = []
    for cj, sj, thj in ((c1, s1, th0[0]), (c2, s2v, th0[1]), (c3, s3, th0[2])):
        dc = cj - iv.cos(thj); ds = sj - iv.sin(thj)
        devs.append(PI / 2 * iv.sqrt(dc * dc + ds * ds))
        ang = iv.atan2(sj, cj) / (2 * PI)
        if lo_fr(ang) < 0: ang = ang + 1
        fvals.append(ang)
    devmax = max(up(q) for q in devs)
    a2c = iv.mpf(0); lip = Fr(0)
    for kk in aA:
        arg = sum((kk[j] * th0[j] for j in range(3)), iv.mpf(0))
        a2c += fr_iv(aA[kk]) * iv.cos(arg)
        lip += abs(aA[kk]) * sum(abs(q) for q in kk) * RHO
    a2low = lo_fr(a2c) - lip
    mp.mp.dps = 40
    def dec(ivv):
        m = (lo_fr(ivv) + hi_fr(ivv)) / 2
        return mp.nstr(mp.mpf(m.numerator) / mp.mpf(m.denominator), 12)
    return dict(s2=s2_ok, pivmin=min(piv), eta=eta, dev=devmax, a2low=a2low, Tpos=Tpos, Dcpos=Dcpos, alpha=dec(X), f=[dec(q) for q in fvals])

# ---------------------------------------------------------------- main
def main():
    Msym = build_M()
    co = check_a(Msym)
    check_b(Msym, co)
    x_ = sp.symbols("x")
    stash = {}
    for name in NAMES:
        jx, jy, jz, kk = COUPLINGS[name]
        sub = {Jx: sp.Rational(jx.numerator, jx.denominator), Jy: sp.Rational(jy.numerator, jy.denominator),
               Jz: sp.Rational(jz.numerator, jz.denominator), kap: sp.Rational(kk.numerator, kk.denominator)}
        Mr = Msym.subs(sub).applyfunc(sp.expand)
        Dn = sp.expand(co[0].subs(sub)); A2n = sp.expand(co[2].subs(sub))
        rel = {kq: to_frac_list(REL[name][kq]) for kq in REL[name]}
        q5 = Q5[name]
        Qx = sum(c * x_**(5 - j) for j, c in enumerate(q5))
        fl = sp.factor_list(Qx)
        irr = len(fl[1]) == 1 and fl[1][0][1] == 1
        nroot = sp.Poly(Qx, x_).count_roots(-1, 1)
        res, nz, ctx = exact_verify(Mr, q5, rel)
        bx = box_cert(name, Dn, A2n, q5, rel)
        ring_ok = all(res.values())
        box_ok = bx["s2"] and bx["dev"] <= RHO and bx["a2low"] > 0 and bx["Tpos"] and bx["Dcpos"]
        ok = irr and nroot == 1 and ring_ok and box_ok
        check(ok, "c %s" % name, "Q5 irreducible=%s, roots in [-1,1]=%d; ring identities %d/%d exact (nonzero minors %d/16); iv-certified box: S2 pivmin %.3g, S3 dev %.2g<=1e-6, S4 a2>=%.4g, T>0 %s, Dc>0 %s"
              % (irr, nroot, sum(res.values()), len(res), nz, float(bx["pivmin"]), float(bx["dev"]), float(bx["a2low"]), bx["Tpos"], bx["Dcpos"]))
        if bx["alpha"] is not None:
            emit("[INFO] %s node: alpha0 = c3 = %s, f = (%s, %s, %s)" % (name, bx["alpha"], bx["f"][0], bx["f"][1], bx["f"][2]))
        stash[name] = (Mr, rel, q5, ctx)
    # (d) negative controls at B
    Mr, rel, q5, _ = stash["B"]
    resS, nzS, _ = exact_verify(Mr, q5, rel, sigma_shift=Fr(1, 10**9))
    check(nzS > 0 and not resS["det=0"], "d1 control", "sigma constant coefficient + 1e-9: nonzero minors %d/16, det M(z) nonzero -> control fails as it should" % nzS)
    resF, nzF, _ = exact_verify(Mr, q5, rel, flips=("s2",))
    check(nzF > 0 and not resF["det=0"], "d2 control", "sign of s2 flipped: nonzero minors %d/16, det M(z) nonzero -> control fails as it should" % nzF)
    q5w = list(q5); q5w[-1] += 1
    resQ, nzQ, _ = exact_verify(Mr, q5w, rel)
    check(nzQ > 0 and not resQ["det=0"], "d3 control", "Q5 constant term + 1: nonzero minors %d/16, det M(z) nonzero -> control fails as it should" % nzQ)
    # (e) minimal polynomial of c1 at B (exact resultant) and the A cross-check
    al, xx = sp.symbols("alpha x")
    def n10(name):
        rel_ = {kq: to_frac_list(REL[name][kq]) for kq in REL[name]}
        pol = lambda lst: sum(sp.Rational(c.numerator, c.denominator) * al**j for j, c in enumerate(lst))
        Qa = sum(c * al**(5 - j) for j, c in enumerate(Q5[name]))
        Rr = sp.resultant(sp.Poly(Qa, al), sp.Poly(xx**2 - pol(rel_["sigma"]) * xx + pol(rel_["pi"]), al), al)
        num = sp.Poly(sp.numer(sp.together(sp.Poly(sp.together(Rr), xx).as_expr())), xx)
        cont, prim = num.primitive()
        return prim
    prim = n10("B")
    fl = sp.factor_list(prim.as_expr())
    irr10 = len(fl[1]) == 1 and fl[1][0][1] == 1
    ctx = stash["B"][3]; R = ctx["R"]; K = ctx["K"]
    def eval_in_ring(poly, elem):
        acc = R.zero()
        for cf in poly.all_coeffs():
            acc = R.add(R.mul(acc, elem), R.lift(K.const(Fr(int(cf), 1))))
        return acc
    r1 = R.is_zero(eval_in_ring(prim, ctx["c1"])); r2 = R.is_zero(eval_in_ring(prim, ctx["c2"]))
    check(prim.degree() == 10 and irr10 and r1 and r2, "e B", "N10 = Res_alpha(Q5, x^2 - sigma x + pi): degree %d, irreducible over Q = %s; N10(c1) = 0 and N10(c2) = 0 exactly in the ring (%s, %s)" % (prim.degree(), irr10, r1, r2))
    primA = n10("A")
    ours = primA.all_coeffs()
    prop = len(ours) == len(N10_A_PSLQ) and all(ours[i] * N10_A_PSLQ[0] == N10_A_PSLQ[i] * ours[0] for i in range(len(ours)))
    check(prop, "e A", "exact N10 at A (degree %d) is proportional to the embedded earlier PSLQ polynomial of cos(2 pi f1) (ratio %s)" % (primA.degree(), sp.Rational(ours[0], N10_A_PSLQ[0])))
    emit("[INFO] runtime %.1f s (AUDIT_TIMEOUT_SEC = %d)" % (time.time() - T0, AUDIT_TIMEOUT_SEC))
    emit("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    raise SystemExit(0 if FAIL == 0 else 1)
