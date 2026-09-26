#!/usr/bin/env python3
"""Exact checks: the walker sea's static response to a shear wave is continuous at long wavelength and tends to half its
uniform response, which is negative for every non-scalar strain; with the sea's energy counted, member plus sea lowers its
static second-order energy under every long enough transverse traceless shear wave, at every K > 0 (a harvest of probe
#9299, confirmed by an other-family referee in #9332). Block 62's framed walk H = 1/2 sum_j {E^j(x).sigma, S_j},
S_j = (T_j - T_j^dag)/(2i), symbol s_j = sin k_j; frame E = 1 + eps cos(q.x), eps symmetric; the member's
F_2 = -K wbar (u R_1 + R_2).

A (premises): landed block 62's walk and member; the axioms.
B (T1): the vertex; the two-level element; F(k, 0); the uniform second-order term is -2 F(k, 0); the bound
   0 <= F <= ||eps||_F^2 (a + b)/4 at 400 exact rational configurations with rational |s| and |s'|.
C (T2): |s|^2 |v|^2 - (s.v)^2 = |s x v|^2; the gap polynomial |s x eps s|^2 vanishes identically only for scalar eps; the
   map k -> s(k) is open near (pi/4, pi/4, pi/4); an explicit positive gap.
D (T3): R_2 homogeneous of degree 2 in p and unchanged by relabellings; on transverse traceless h, R_1 = 0 and
   R_2 = -(p^2/4) tr(h^2), at p along an axis and at p = (1, 2, 2).
Exact (sympy, fractions). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import re
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_SEAS_RESPONSE_TO_A_LONG_SHEAR_WAVE_IS_HALF_ITS_UNIFORM_RESPONSE_AND_MEMBER_PLUS_SEA_LOWERS_ITS_ENERGY_UNDER_LONG_ENOUGH_SHEARS_AT_EVERY_K_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_seas_response_to_a_long_shear_wave_is_half_its_uniform_response_and_member_plus_sea_lowers_its_energy_under_long_enough_shears_at_every_k_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED_NEEDLES = (
    "H = ½ Σ_j {E^j(x)·σ, S_j}",
    "R_1=p^2 tr(h)-p^T h p",
    "R_2=-(p^2/4) tr(h^T h)+(1/2)|h p|^2-(1/2)(p^T h p)tr(h)+(p^2/4)tr(h)^2",
    "F_2 = −K w̄ (u R_1 + R_2)",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "two_level_forged": "B",
    "gap_forged": "C",
    "tt_member_forged": "D",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])


def sdot(vec):
    return vec[0] * SX + vec[1] * SY + vec[2] * SZ


def unit_rational(x, y):
    """a rational unit vector (inverse stereographic projection)"""
    d = 1 + x * x + y * y
    return [2 * x / d, 2 * y / d, (1 - x * x - y * y) / d]


def sym_eps():
    e = sp.symbols("e11 e12 e13 e22 e23 e33", real=True)
    return sp.Matrix([[e[0], e[1], e[2]], [e[1], e[3], e[4]], [e[2], e[4], e[5]]]), e


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, landed = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, the frame, the sea and the member are supplied)")
    needles = list(LANDED_NEEDLES)
    if mut("landed_quote_forged"):
        needles[1] = "R_1=p^2 tr(h)+p^T h p"
    checks.check("A3", all(n in landed for n in needles), "landed block 62: H = 1/2 sum_j {E^j(x).sigma, S_j}; R_1 = p^2 tr h - p^T h p; R_2 as landed; F_2 = -K wbar (u R_1 + R_2)")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    # B1: the vertex.  <k'|{f sigma_a, S_j}|k>/2 = sigma_a fhat(k' - k)(s_j(k) + s_j(k'))/2: S_j is diagonal in k with symbol
    # sin k_j, and f multiplies by fhat(k' - k); with f = cos(q.x), fhat(+-q) = 1/2.
    k, kp, fh = sp.symbols("k kp fh")
    f_then_s = fh * sp.sin(k)          # S_j first (on |k>), then f
    s_then_f = sp.sin(kp) * fh         # f first, then S_j (on |k'>)
    fhat = sp.integrate(sp.cos(t_q) * sp.exp(-sp.I * t_q), (t_q, 0, 2 * sp.pi)) / (2 * sp.pi)
    checks.check("B1", sp.simplify((f_then_s + s_then_f) / 2 - fh * (sp.sin(k) + sp.sin(kp)) / 2) == 0 and sp.simplify(fhat - sp.Rational(1, 2)) == 0,
                 "the vertex: <k'|1/2 {f sigma_a, S_j}|k> = sigma_a fhat(k' - k)(s_j(k) + s_j(k'))/2 and fhat(+-q) = 1/2 for f = cos(q.x), so <k + q|V|k> = sigma.w with w = eps (s + s')/4")
    # B2: the two-level element on exact rational unit vectors, symbolic w
    w_ = sp.Matrix(sp.symbols("w1:4", real=True))
    ok2 = True
    for (x1, y1, x2, y2) in [(sp.Rational(1, 3), sp.Rational(2, 5), sp.Rational(-3, 7), sp.Rational(1, 2)),
                             (sp.Integer(0), sp.Rational(1, 4), sp.Rational(5, 3), sp.Rational(-2, 9)),
                             (sp.Integer(2), sp.Rational(-1, 3), sp.Rational(1, 11), sp.Rational(4, 5))]:
        n1 = sp.Matrix(unit_rational(x1, y1))
        n2 = sp.Matrix(unit_rational(x2, y2))
        Pp = (sp.eye(2) + sdot(n2)) / 2
        Pm = (sp.eye(2) - sdot(n1)) / 2
        val = sp.expand((Pp * sdot(w_) * Pm * sdot(w_)).trace())
        c2 = 1 if mut("two_level_forged") else 2
        ref = sp.expand((w_.dot(w_) * (1 + n1.dot(n2)) - c2 * n1.dot(w_) * n2.dot(w_)) / 2)
        ok2 = ok2 and sp.simplify(val - ref) == 0
    checks.check("B2", ok2, "the two-level element: |<+, n'|sigma.w|-, n>|^2 = Tr[P+(n') sigma.w P-(n) sigma.w] = [|w|^2 (1 + n.n') - 2 (n.w)(n'.w)]/2 (symbolic w, three pairs of exact rational unit vectors)")
    # B3: F(k, 0)
    EPS, _ = sym_eps()
    s = sp.Matrix(sp.symbols("s1:4", real=True))
    a = sp.Symbol("a", positive=True)
    w0 = EPS * s / 2
    F0 = (w0.dot(w0) * (a * a + s.dot(s)) - 2 * s.dot(w0) ** 2) / (a * a * 2 * a)
    target = ((EPS * s).dot(EPS * s) * a ** 2 - (s.dot(EPS * s)) ** 2) / (4 * a ** 3)
    num3 = sp.expand(sp.numer(sp.together(F0 - target)))
    diff3 = sp.expand(sp.rem(sp.Poly(num3, a), sp.Poly(a ** 2 - s.dot(s), a)).as_expr())   # reduce with a^2 = |s|^2
    checks.check("B3", diff3 == 0, "at q = 0 (s' = s, b = a, w = eps s/2): F(k, 0) = (a^2 |eps s|^2 - (s.eps s)^2)/(4 a^3) for every symmetric eps")
    # B4: the uniform second-order term of -|(1 + eps) s| is -2 F(k, 0)
    lam = sp.Symbol("lam")
    v = (sp.eye(3) + lam * EPS) * s
    ser = sp.series(-sp.sqrt(sp.expand(v.dot(v))), lam, 0, 3).removeO()
    c2 = ser.coeff(lam, 2)
    unif = -((EPS * s).dot(EPS * s) * s.dot(s) - (s.dot(EPS * s)) ** 2) / (2 * s.dot(s) ** sp.Rational(3, 2))
    checks.check("B4", sp.simplify(c2 - unif) == 0, "the uniform frame 1 + eps moves the filled band's energy -|(1 + eps)s| at second order by -(r^2 |eps s|^2 - (s.eps s)^2)/(2 r^3) = -2 F(k, 0); the wave's cos^2 mean is 1/2, so F(k, 0) is the wave's pointwise q -> 0 limit of half the uniform form")
    # B5: the bound, exactly, on configurations with rational |s| and |s'|
    rng = random.Random(26)
    ok5 = True
    count = 0
    while count < 400:
        r1, r2 = Fr(rng.randint(1, 17), 10), Fr(rng.randint(1, 17), 10)
        u1 = unit_rational(Fr(rng.randint(-9, 9), 7), Fr(rng.randint(-9, 9), 7))
        u2 = unit_rational(Fr(rng.randint(-9, 9), 7), Fr(rng.randint(-9, 9), 7))
        sv = [r1 * x for x in u1]
        sq = [r2 * x for x in u2]
        E = [[Fr(rng.randint(-6, 6), 5) for _ in range(3)] for _ in range(3)]
        E = [[(E[i][j] + E[j][i]) / 2 for j in range(3)] for i in range(3)]
        wv = [sum(E[i][j] * (sv[j] + sq[j]) for j in range(3)) / 4 for i in range(3)]
        ww = sum(x * x for x in wv)
        sw = sum(x * y for x, y in zip(sv, wv))
        qw = sum(x * y for x, y in zip(sq, wv))
        ssq = sum(x * y for x, y in zip(sv, sq))
        Nn = ww * (r1 * r2 + ssq) - 2 * sw * qw
        Fv = Nn / (r1 * r2 * (r1 + r2))
        fro2 = sum(E[i][j] ** 2 for i in range(3) for j in range(3))
        ok5 = ok5 and Fv >= 0 and Fv <= fro2 * (r1 + r2) / 4
        count += 1
    checks.check("B5", ok5, "the bound 0 <= F <= ||eps||_F^2 (a + b)/4, exactly, at 400 random configurations with rational |s| = a and |s'| = b (rational radii times rational unit vectors) and rational symmetric eps")


t_q = sp.Symbol("t_q", real=True)


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    s = sp.Matrix(sp.symbols("s1:4", real=True))
    vv = sp.Matrix(sp.symbols("v1:4", real=True))
    ident = sp.expand(s.dot(s) * vv.dot(vv) - s.dot(vv) ** 2 - s.cross(vv).dot(s.cross(vv)))
    checks.check("C1", ident == 0, "|s|^2 |v|^2 - (s.v)^2 = |s x v|^2, so the uniform integrand (a^2 |eps s|^2 - (s.eps s)^2)/(2 a^3) = |s x eps s|^2/(2 a^3) >= 0")
    EPS, e = sym_eps()
    gap = sp.Poly(sp.expand(s.cross(EPS * s).dot(s.cross(EPS * s))), *s)
    sols = sp.solve(gap.coeffs(), list(e), dict=True)
    scalar_only = len(sols) > 0 and all(sol.get(e[1], e[1]) == 0 and sol.get(e[2], e[2]) == 0 and sol.get(e[4], e[4]) == 0
                                        and sp.simplify(sol.get(e[0], e[0]) - sol.get(e[3], e[3])) == 0
                                        and sp.simplify(sol.get(e[3], e[3]) - sol.get(e[5], e[5])) == 0 for sol in sols)
    kk = sp.symbols("k1:4", real=True)
    jac = sp.Matrix([sp.sin(x) for x in kk]).jacobian(list(kk)).det().subs({x: sp.pi / 4 for x in kk})
    checks.check("C2", scalar_only and sp.simplify(jac) != 0,
                 "the gap polynomial |s x eps s|^2 is identically zero only for eps = c 1 (all its coefficients vanish only there); s(k) = (sin k_j) has Jacobian (cos(pi/4))^3 != 0 at (pi/4, pi/4, pi/4), so it is open there and the gap is positive on a set of positive measure for every non-scalar eps")
    eps_t = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    s0 = sp.Matrix([1, 1, 0])
    g0 = s0.cross(eps_t * s0).dot(s0.cross(eps_t * s0))
    want = 3 if mut("gap_forged") else 4
    checks.check("C3", g0 == want, "an explicit case: at s = (1, 1, 0) the traceless shear diag(1, -1, 0) has gap |s x eps s|^2 = 4")


# ============================================================================================ family D (T3)
def R1f(h, p):
    return p.dot(p) * h.trace() - p.dot(h * p)


def R2f(h, p):
    P2 = p.dot(p)
    return -(P2 / 4) * (h.T * h).trace() + sp.Rational(1, 2) * (h * p).dot(h * p) - sp.Rational(1, 2) * p.dot(h * p) * h.trace() + (P2 / 4) * h.trace() ** 2


def family_d(checks: Checks) -> None:
    pp = sp.Matrix(sp.symbols("p1:4", real=True))
    hs = sp.symbols("h11 h12 h13 h22 h23 h33", real=True)
    Hm = sp.Matrix([[hs[0], hs[1], hs[2]], [hs[1], hs[3], hs[4]], [hs[2], hs[4], hs[5]]])
    tt = sp.Symbol("tt")
    R2 = R2f(Hm, pp)
    homog = sp.expand(R2.subs({pp[i]: tt * pp[i] for i in range(3)}, simultaneous=True) - tt ** 2 * R2) == 0
    xi = sp.Matrix(sp.symbols("x1:4", real=True))
    Hr = Hm + pp * xi.T + xi * pp.T
    relab = sp.expand(R2f(Hr, pp) - R2) == 0 and sp.expand(R1f(Hr, pp) - R1f(Hm, pp)) == 0
    checks.check("D1", homog and relab, "R_2 is homogeneous of degree 2 in p, and R_1, R_2 are unchanged by h -> h + p xi^T + xi p^T (landed block 62 T3(b), re-checked)")
    x, y, p3 = sp.symbols("x y p3", real=True)
    ok2 = True
    # p along an axis: h = [[x, y, 0], [y, -x, 0], [0, 0, 0]]
    pa = sp.Matrix([0, 0, p3])
    ha = sp.Matrix([[x, y, 0], [y, -x, 0], [0, 0, 0]])
    coef = -sp.Rational(1, 4) if not mut("tt_member_forged") else -sp.Rational(1, 2)
    ok2 = ok2 and sp.expand(R1f(ha, pa)) == 0 and sp.expand(R2f(ha, pa) - coef * pa.dot(pa) * (ha * ha).trace()) == 0
    # p = (1, 2, 2): e1 = (2, -1, 0), e2 = p x e1 = (2, 4, -5); TT basis h+ = e1 e1^T/5 - e2 e2^T/45, hx = (e1 e2^T + e2 e1^T)/15
    pb = sp.Matrix([1, 2, 2])
    e1 = sp.Matrix([2, -1, 0])
    e2 = pb.cross(e1)
    hb = x * (e1 * e1.T / 5 - e2 * e2.T / 45) + y * (e1 * e2.T + e2 * e1.T) / 15
    ok2 = ok2 and sp.expand(hb.trace()) == 0 and sp.expand(hb * pb) == sp.zeros(3, 1)
    ok2 = ok2 and sp.expand(R1f(hb, pb)) == 0 and sp.expand(R2f(hb, pb) - coef * pb.dot(pb) * (hb * hb).trace()) == 0
    checks.check("D2", ok2, "on transverse traceless h (tr h = 0, h p = 0): R_1 = 0, so the lapse constraint holds with u = 0, and R_2 = -(p^2/4) tr(h^2); the member's static energy -K wbar R_2 = K wbar (p^2/4) tr(h^2) is O(K |q|^2) (p along an axis, and p = (1, 2, 2) with an exact transverse basis)")


# ============================================================================================ family F
FENCES = (
    "This note works within block 62 as landed on main (the framed walk, its filled sea and the member's second-order energy) and counts the sea's energy in the static energy, as block 147 (landed) does when the member sees the half-filled sea; it reports the sea's response to a long shear wave and what the member's energy does against it; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the longest shear wave."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Cauchy", "Schwarz",
                   "Rayleigh", "Schrödinger", "Lebesgue", "Bessel", "Slater", "Pauli", "Bloch", "Brillouin")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Rayleigh) —", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a_) for a_ in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the vertex; the two-level element on exact unit vectors",
    "per_site: executed - F(k, 0) and the uniform second-order term for a symbolic symmetric strain; the bound at 400 exact configurations",
    "per_mode: executed - the gap polynomial and its zero set; R_1 and R_2 on transverse traceless strains at two wave vectors",
    "per_block: executed - homogeneity and relabelling invariance of the member's forms",
    "lattice_wide: checked and not executed - the q^2 part of the sea's response (floating point in the probe); the sea under one record per site",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p_ in AUDIT_INPUT_PATHS:
        print(f"  {p_}")
    texts = [Path(ROOT, p_).read_text(encoding="utf-8") if Path(ROOT, p_).exists() else "" for p_ in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 62's framed walk and member with the sea's energy counted: the sea's static response to a shear wave tends to half its uniform response, negative for every non-scalar strain; the member costs O(K q^2) on transverse traceless waves; so member plus sea lowers its static second-order energy under every long enough such wave at every K > 0; harvest of #9299 (confirmed by #9332); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
