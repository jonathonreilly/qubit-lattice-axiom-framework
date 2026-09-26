#!/usr/bin/env python3
"""Independent check of the sea's long-wavelength shear response.

Exact identities only. The author's floating-point q^2 coefficients are not rebuilt.
Rayleigh-Schrodinger for a Slater sea and dominated convergence are the labelled imports.
"""
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


k, kp, fh = sp.symbols("k kp fh")
vertex = sp.Rational(1, 2) * (fh * sp.sin(k) + sp.sin(kp) * fh)
check(
    "A1 vertex",
    sp.simplify(vertex - fh * (sp.sin(k) + sp.sin(kp)) / 2) == 0,
    "the anticommutator {f, S} averages the two sines; fhat of cos(q.x) at ±q is 1/2, so w = eps(s+s')/4",
)

sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])


def sdot(v):
    return v[0] * sx + v[1] * sy + v[2] * sz


n = sp.Matrix(sp.symbols("n1:4", real=True))
np_ = sp.Matrix(sp.symbols("m1:4", real=True))
w = sp.Matrix(sp.symbols("w1:4", real=True))
Pp = (sp.eye(2) + sdot(np_)) / 2
Pm = (sp.eye(2) - sdot(n)) / 2
tr = sp.expand((Pp * sdot(w) * Pm * sdot(w)).trace())
ref = sp.expand((w.dot(w) * (1 + n.dot(np_)) - 2 * n.dot(w) * np_.dot(w)) / 2)
gap = sp.expand(tr - ref)
unit = {n[0] ** 2: 1 - n[1] ** 2 - n[2] ** 2, np_[0] ** 2: 1 - np_[1] ** 2 - np_[2] ** 2}
check(
    "A2 interband square",
    sp.expand(gap.subs(unit)) == 0,
    "Tr[P+ sigma.w P- sigma.w] = [|w|^2(1+n.n') - 2(n.w)(n'.w)]/2 once n and n' are unit vectors",
)

e = sp.symbols("e11 e12 e13 e22 e23 e33", real=True)
EPS = sp.Matrix([[e[0], e[1], e[2]], [e[1], e[3], e[4]], [e[2], e[4], e[5]]])
s = sp.Matrix(sp.symbols("s1:4", real=True))
a = sp.Symbol("a", positive=True)
w0 = EPS * s / 2
F0 = (w0.dot(w0) * (a * a + s.dot(s)) - 2 * s.dot(w0) ** 2) / (a * a * 2 * a)
target = ((EPS * s).dot(EPS * s) * a**2 - (s.dot(EPS * s)) ** 2) / (4 * a**3)
check(
    "A3 pointwise limit",
    sp.simplify(sp.expand((F0 - target).subs(s.dot(s), a**2))) == 0,
    "F(k,0) = (a^2 |eps s|^2 - (s.eps s)^2)/(4 a^3)",
)
lam = sp.Symbol("lam")
series = sp.series(-sp.sqrt(sp.expand(((sp.eye(3) + lam * EPS) * s).dot((sp.eye(3) + lam * EPS) * s))), lam, 0, 3).removeO()
c2 = sp.simplify(series.coeff(lam, 2))
unif = -((EPS * s).dot(EPS * s) * s.dot(s) - (s.dot(EPS * s)) ** 2) / (2 * s.dot(s) ** sp.Rational(3, 2))
check(
    "A4 uniform second order",
    sp.simplify(c2 - unif) == 0 and sp.simplify(unif + 2 * target.subs(a, sp.sqrt(s.dot(s)))) == 0,
    "the lambda^2 term of -|(1+eps)s| equals -2 F(k,0), so half the uniform form is -F(k,0)",
)

spv = sp.Matrix(sp.symbols("t1:4", real=True))
cross2 = sp.simplify(s.dot(s) * spv.dot(spv) - s.dot(spv) ** 2 - (s.cross(spv)).dot(s.cross(spv)))
fro = sum(EPS[i, j] ** 2 for i in range(3) for j in range(3))
ev = EPS * s
row_gap = sp.expand(fro * s.dot(s) - ev.dot(ev))
sos = sp.expand(sum((EPS.row(i).cross(s)).dot(EPS.row(i).cross(s)) for i in range(3)))
check(
    "B gram identities",
    cross2 == 0 and sp.expand(row_gap - sos) == 0,
    "|s|^2|t|^2-(s.t)^2 = |s x t|^2, and ||eps||_F^2 |s|^2 - |eps s|^2 is the sum of the three row cross-squares",
)

shear = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
sv = sp.Matrix([1, 1, 0])
gap_c = (shear * sv).dot(shear * sv) * sv.dot(sv) - (sv.dot(shear * sv)) ** 2
scalar = sp.symbols("c", real=True)
eye_gap = sp.simplify(((scalar * sp.eye(3) * s).dot(scalar * sp.eye(3) * s) * s.dot(s) - (s.dot(scalar * sp.eye(3) * s)) ** 2))
check(
    "C1 uniform sign",
    gap_c == 4 and sp.expand(eye_gap) == 0,
    "the integrand |s|^2|eps s|^2-(s.eps s)^2 vanishes for a scalar and equals 4 at s=(1,1,0) for diag(1,-1,0)",
)

pp = sp.Matrix(sp.symbols("p1:4", real=True))
hs = sp.symbols("h11 h12 h13 h22 h23 h33", real=True)
Hm = sp.Matrix([[hs[0], hs[1], hs[2]], [hs[1], hs[3], hs[4]], [hs[2], hs[4], hs[5]]])
P2 = pp.dot(pp)
R1 = P2 * Hm.trace() - pp.dot(Hm * pp)
R2 = (
    -(P2 / 4) * (Hm.T * Hm).trace()
    + sp.Rational(1, 2) * (Hm * pp).dot(Hm * pp)
    - sp.Rational(1, 2) * pp.dot(Hm * pp) * Hm.trace()
    + (P2 / 4) * Hm.trace() ** 2
)
t = sp.Symbol("t")
hom = sp.expand(R2.subs({pp[i]: t * pp[i] for i in range(3)}) - t**2 * R2)
xi = sp.Matrix(sp.symbols("x1:4", real=True))
Hr = Hm + pp * xi.T + xi * pp.T
R2r = (
    -(P2 / 4) * (Hr.T * Hr).trace()
    + sp.Rational(1, 2) * (Hr * pp).dot(Hr * pp)
    - sp.Rational(1, 2) * pp.dot(Hr * pp) * Hr.trace()
    + (P2 / 4) * Hr.trace() ** 2
)
tt = sp.simplify(R1.subs({hs[0]: 1, hs[3]: -1, hs[1]: 0, hs[2]: 0, hs[4]: 0, hs[5]: 0, pp[0]: 0, pp[1]: 0, pp[2]: 1}))
check(
    "C2 member",
    hom == 0 and sp.expand(R2r - R2) == 0 and tt == 0,
    "this R2 is degree 2 in p and invariant under h -> h + p xi^T + xi p^T; a TT wave with tr h = 0 and h p = 0 has R1 = 0",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL exact for the long-wave sign. F(k,0) is half the negative of the uniform second-order form, "
        "the uniform integrand is nonnegative and not identically zero for a non-scalar symmetric strain, "
        "and the member polynomial used here is O(|p|^2) and vanishes in the R1 channel of a TT wave. "
        "So for every K>0 a long enough TT shear has negative second-order energy. "
        "Dominated convergence and Rayleigh-Schrodinger for the filled sea are imports. "
        "The floating-point q^2 relabelling coefficients were not rebuilt and are not certified.",
        flush=True,
    )
    print(
        "HIT: confirmed - the sea's static response is continuous at q=0 and equals half the uniform second-order form, "
        "and member plus sea has negative second-order energy for every K>0 once a TT shear wave is long enough. "
        "The q^2 relabelling coefficient remains uncertified.",
        flush=True,
    )
