#!/usr/bin/env python3
"""Independent check of one interband single-quantum amplitude.

Does not import the author's script. The form factor and the symmetric
vanishing are exact. The non-symmetric root is isolated by a Sturm interval,
then evaluated with outward interval arithmetic.
"""
import sympy as sp
from mpmath import iv

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


I = sp.I
SIG = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
Zs = sp.symbols("Z1:4", nonzero=True)
Ws = sp.symbols("W1:4", nonzero=True)
ub = sp.Matrix(sp.symbols("b1:3"))
up = sp.Matrix(sp.symbols("v1:3"))


def phase(zv, n):
    return sp.Mul(*[zv[a] ** (2 * n[a]) for a in range(3)])


def shift(a, step):
    n = [0, 0, 0]
    n[a] = step
    return n


def psym(zv, j):
    return (zv[j] ** 4 - zv[j] ** (-4)) / (4 * I)


form_ok = True
for a in range(3):
    for j in range(3):
        bra = lambda n: phase([1 / z for z in Zs], n)
        ket = lambda n: phase(Ws, n)
        spin = (ub.T * SIG[a] * up)[0]
        elem = (
            bra(shift(a, 1)) * ket([0, 0, 0]) * psym(Ws, j)
            + bra(shift(a, 1)) * psym(Zs, j) * ket([0, 0, 0])
            + bra([0, 0, 0]) * psym(Zs, j) * ket(shift(a, 1))
            + bra([0, 0, 0]) * ket(shift(a, 1)) * psym(Ws, j)
        ) * spin / 4
        cos_bar = (Zs[a] * Ws[a] + 1 / (Zs[a] * Ws[a])) / 2
        formula = sp.Rational(1, 2) * (Ws[a] / Zs[a]) * cos_bar * (psym(Zs, j) + psym(Ws, j)) * spin
        form_ok = form_ok and sp.cancel(sp.expand(elem - formula)) == 0
check(
    "S1 form factor",
    form_ok,
    "the stress kernel is (1/2) e^{-i q_a/2} cos(Kbar_a) (P_j(k)+P_j(k')) u^dag sigma_a u'",
)

q = sp.symbols("q1:4", real=True)
sym_ok = True
for nu in ((a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)):
    kk = [q[i] / 2 + sp.pi * nu[i] for i in range(3)]
    kp = [kk[i] - q[i] for i in range(3)]
    sym_ok = sym_ok and all(sp.simplify(sp.sin(2 * kk[j]) + sp.sin(2 * kp[j])) == 0 for j in range(3))
    sym_ok = sym_ok and all(sp.simplify(sp.sin(kk[j]) + sp.sin(kp[j])) == 0 for j in range(3))
check(
    "S2 symmetric resonances",
    sym_ok,
    "at k = q/2 + pi nu both P_j(k)+P_j(k') and the sine sum vanish",
)

sh = [sp.Rational(3, 5), sp.Rational(5, 13), sp.Rational(8, 17)]
ch = [sp.Rational(4, 5), sp.Rational(12, 13), sp.Rational(15, 17)]
check(
    "S3 triples",
    all(sh[i] ** 2 + ch[i] ** 2 == 1 for i in range(3)),
    "sin(q/2) and cos(q/2) are the triples 3-4-5, 5-12-13 and 8-15-17",
)
sq = [2 * sh[i] * ch[i] for i in range(3)]
cq = [ch[i] ** 2 - sh[i] ** 2 for i in range(3)]
A = sh[1] ** 2 + sh[2] ** 2
Z = sh[0] ** 2
t = sp.symbols("t", real=True)
c = (1 - t**2) / (1 + t**2)
s = 2 * t / (1 + t**2)
X = s**2
Y = (s * cq[0] - c * sq[0]) ** 2
R = 4 * Z + 2 * A - X - Y
expr = sp.together(4 * (X + A) * (Y + A) - R**2)
poly = sp.Poly(sp.numer(expr), t)
sym = sh[0] / (1 + ch[0])
quot, rem = sp.div(poly, sp.Poly((t - sym) ** 2, t))
boxes = sp.Poly(quot, t).intervals(eps=sp.Rational(1, 10**30))
target = min(boxes, key=lambda item: abs((item[0][0] + item[0][1]) / 2 - sp.Rational(151, 1000)))
lo, hi = target[0]
check(
    "S3 root",
    rem == 0 and poly.degree() == 8 and sym == sp.Rational(1, 3)
    and not (lo <= sym <= hi) and hi - lo < sp.Rational(1, 10**20),
    f"degree 8, double root at t=1/3, and another real root in ({lo}, {hi})",
)

iv.dps = 60


def ivq(r):
    r = sp.Rational(r)
    return iv.mpf(int(r.p)) / iv.mpf(int(r.q))


T = iv.mpf([ivq(lo).a, ivq(hi).b])
cT = (1 - T**2) / (1 + T**2)
sT = 2 * T / (1 + T**2)
shI = [ivq(v) for v in sh]
chI = [ivq(v) for v in ch]
sqI = [ivq(v) for v in sq]
cqI = [ivq(v) for v in cq]
X_ = sT**2
sk = sT * cqI[0] - cT * sqI[0]
R_ = 4 * ivq(Z) + 2 * ivq(A) - X_ - sk**2
left = iv.sqrt(X_ + ivq(A)) + iv.sqrt(sk**2 + ivq(A))
right = 2 * iv.sqrt(ivq(Z) + ivq(A))
gap = left - right
check(
    "S3 genuine",
    R_.a > 0 and gap.a <= 0 <= gap.b and float(gap.delta) < 1e-20,
    "R > 0 and |s(k)|+|s(k')|-|p| encloses 0, so the squared root is a real resonance",
)

p = [2 * v for v in sh]
e1 = sp.Matrix([0, p[2], -p[1]])
pv = sp.Matrix(p)
e2 = pv.cross(e1)
eps_plus = e2.dot(e2) * (e1 * e1.T) - e1.dot(e1) * (e2 * e2.T)
eps_cross = e1 * e2.T + e2 * e1.T
tt_ok = all(pv.T * E == sp.zeros(1, 3) and sp.simplify(E.trace()) == 0 and E == E.T for E in (eps_plus, eps_cross))
c_bar = cT * chI[0] + sT * shI[0]
s_half = sT * chI[0] - cT * shI[0]
stress_alt = 2 * s_half * c_bar * cqI[0]


class C:
    def __init__(self, re, im=None):
        self.re = re
        self.im = iv.mpf(0) if im is None else im

    def __add__(self, other):
        return C(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return C(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return C(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def conj(self):
        return C(self.re, -self.im)


def dot_pauli(coeffs):
    c1, c2, c3 = coeffs
    ii = C(iv.mpf(0), iv.mpf(1))
    return [[c3, c1 - ii * c2], [c1 + ii * c2, C(-c3.re, -c3.im)]]


def mul(a, b):
    return [[a[i][0] * b[0][j] + a[i][1] * b[1][j] for j in range(2)] for i in range(2)]


def projector(h, sign):
    norm = iv.sqrt(h[0] ** 2 + h[1] ** 2 + h[2] ** 2)
    direction = dot_pauli([C(sign * h[a] / norm) for a in range(3)])
    return [[C((iv.mpf(1 if i == j else 0) + direction[i][j].re) / 2,
               direction[i][j].im / 2) for j in range(2)] for i in range(2)]


def trace_square(eps, phase):
    coeffs = []
    for i in range(3):
        cosine = c_bar if i == 0 else iv.mpf(1)
        base = C(ivq(eps[i, 0]) * cosine)
        if phase:
            base = base * C(chI[i], -shI[i])
        coeffs.append(base)
    op = dot_pauli(coeffs)
    upper = projector([sT, shI[1], shI[2]], 1)
    lower = projector([sk, -shI[1], -shI[2]], -1)
    prod = mul(mul(mul(upper, op), lower), [[op[j][i].conj() for j in range(2)] for i in range(2)])
    return prod[0][0] + prod[1][1]


traces = {name: trace_square(mat, phase)
          for name, mat in (("plus", eps_plus), ("cross", eps_cross))
          for phase in (False, True)}
away = all(tr.re.a > 0 for tr in traces.values())
check(
    "S4 amplitude",
    tt_ok and (stress_alt.a > 0 or stress_alt.b < 0) and (c_bar.a > 0 or c_bar.b < 0) and away,
    "both TT tensors are transverse and traceless, and all four spinor factors exclude 0",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL an interband witness. The stress vertex vanishes at every symmetric resonance "
        "k=q/2+pi nu. At sin(q/2)=(3/5,5/13,8/17) the line k=(kappa,q2/2,q3/2) has another exact resonance, "
        "tan(kappa/2) isolated away from 1/3, where a transverse-traceless single quantum has nonzero "
        "pair-creation amplitude. The rate was not computed.",
        flush=True,
    )
    print(
        "HIT: confirmed - with one TT quantum of energy |p(q)|, the pair-creation vertex vanishes at the "
        "symmetric resonances and is nonzero at an exact non-symmetric resonance on this rational line.",
        flush=True,
    )
