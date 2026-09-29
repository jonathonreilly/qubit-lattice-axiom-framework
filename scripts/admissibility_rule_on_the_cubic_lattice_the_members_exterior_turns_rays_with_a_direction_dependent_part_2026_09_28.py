#!/usr/bin/env python3
"""Exact checks: the curvature member's exterior on the cubic lattice and the first-order turn of long-wave rays (harvest of probe HIT
#9364, a Claude Opus worker, refereed by Claude Sonnet). At first order in the charges the exterior is chi - 1 = Q G and 1 - N = P G with
G the cubic lattice's unit-source potential, so the index is n = 1 + (3a + p) 4 pi G (block 110 T1 with a = Q/4 pi, p = P/4 pi).
(T1) From the lattice symbol sigma = 2 sum(1 - cos k_i) and the transforms of |k|^-2m, G = G0 + G1 + G2 + G3 + O(r^-9) with
G1 = (5 sum x^4 - 3 r^4)/(32 pi r^7) (landed 2026-06-07) and G2, G3 explicit; each satisfies the lattice Laplace equation at its order,
none has an l = 0 part, and G1 is the only degree -3 correction the local equation allows. (T2) The fields' relative anisotropy is
(5 sum x^4/r^4 - 3)/(8 r^2): +1/(4r^2) on an axis, -1/(16r^2) on a face diagonal, -1/(6r^2) on a body diagonal. (T3) The line
integral of 4 pi G1 along a ray of direction t at impact b beta is f1/b^2 with f1 = (1/4) sum t^4 + sum t^2 beta^2 + (2/3) sum beta^4 - 3/4;
the ray-turn table for f1 and f2 (G2's line integral times b^4) along the axis, the face diagonal and the body diagonal; f1 vanishes
identically on the body diagonal and averages to zero over the azimuth for every direction checked. (T4) With a = p = M/2, the axis
lattice term at phi = 0 against the continuum second-order term (15 pi/4)(M/b)^2 has ratio 8/(45 pi M b).

A (premises): the axioms; landed block 110's exterior and index; the landed 2026-06-07 note's G1.
B (T1): the symbol expansion, the transforms, G1..G3, the local equations, uniqueness of G1, no l = 0 parts.
C (T2): the fields' anisotropy.
D (T3): the line integrals, the table, the body diagonal, the azimuthal averages.
E (T4): the size against the continuum second order.
Exact (sympy). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_ON_THE_CUBIC_LATTICE_THE_MEMBERS_EXTERIOR_TURNS_RAYS_WITH_A_DIRECTION_DEPENDENT_PART_FIRST_AT_THE_INVERSE_CUBE_OF_THE_IMPACT_PARAMETER_BOUNDED_THEOREM_NOTE_2026-09-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_AROUND_A_BODY_THE_WALKS_RAYS_MATCH_THE_COMPARATORS_AT_EVERY_ORDER_EXACTLY_WHEN_ITS_TWO_CHARGES_AGREE_AND_THEY_AGREE_ONLY_WHEN_HOP_ENERGY_BALANCES_THE_SLOWED_CLOCKS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_on_the_cubic_lattice_the_members_exterior_turns_rays_with_a_direction_dependent_part_first_at_the_inverse_cube_of_the_impact_parameter_bounded_theorem_note_2026-09-28"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED110 = (
    "the curvature member's two fields are `χ = 1 + a/r` and `N = wχ = 1 − p/r`",
    "`n = χ³/N = (r + a)³/(r²(r − p))`",
)
LANDED0607 = ("`G(r) = 1/(4π r) + [5/(32π)]·K₄(n̂)/r³ + O(1/r⁵)`",)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "symbol_forged": "B",
    "anisotropy_forged": "C",
    "table_forged": "D",
    "ratio_forged": "E",
    "claim_transition_injected": "G",
    "claim_classical_name_in_theorem": "G",
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
X = sp.symbols("x y z", real=True)
Q2 = sp.Poly(X[0] ** 2 + X[1] ** 2 + X[2] ** 2, *X, domain=sp.QQ)
KV = sp.symbols("k1:4", real=True)


class RP:
    """sum_k P_k(x) r^k, P_k polynomials over QQ; canonical: one term per parity of k, at the lowest k"""
    def __init__(self, d=None):
        self.d = {}
        for k, P in (d or {}).items():
            self._add(k, P)

    def _add(self, k, P):
        P = P if isinstance(P, sp.Poly) else sp.Poly(P, *X, domain=sp.QQ)
        if P.is_zero:
            return
        self.d[k] = self.d[k] + P if k in self.d else P
        if self.d[k].is_zero:
            del self.d[k]

    @staticmethod
    def rpow(k, c=1):
        return RP({k: sp.Poly(c, *X, domain=sp.QQ)})

    def __add__(a, b):
        r = RP(dict(a.d))
        for k, P in b.d.items():
            r._add(k, P)
        return r

    def scale(a, c):
        return RP({k: P * c for k, P in a.d.items()})

    def __sub__(a, b):
        return a + b.scale(-1)

    def diff(a, i):
        r = RP()
        for k, P in a.d.items():
            r._add(k, P.diff(X[i]))
            if k != 0:
                r._add(k - 2, P * sp.Poly(k * X[i], *X, domain=sp.QQ))
        return r

    def canon(a):
        out = {}
        for par in (0, 1):
            ks = [k for k in a.d if k % 2 == par]
            if not ks:
                continue
            kmin = min(ks)
            P = sp.Poly(0, *X, domain=sp.QQ)
            for k in ks:
                P = P + a.d[k] * Q2 ** ((k - kmin) // 2)
            if not P.is_zero:
                out[kmin] = P
        return out

    def is_zero(a):
        return a.canon() == {}


def Dn(f, n):
    out = RP()
    for i in range(3):
        g = f
        for _ in range(n):
            g = g.diff(i)
        out = out + g
    return out


def lap(f):
    return Dn(f, 2)


# pi times the transforms of |k|^(-2m) in three dimensions (named import): 1/(4 r), -r/8, r^3/96, -r^5/2880
TRANSFORM = {1: RP.rpow(-1, sp.Rational(1, 4)), 2: RP.rpow(1, -sp.Rational(1, 8)), 3: RP.rpow(3, sp.Rational(1, 96)), 4: RP.rpow(5, -sp.Rational(1, 2880))}


def apply_monomial(f, mon):
    """k^mon -> (-i d)^mon: d_x^a d_y^b d_z^c with sign (-1)^((a + b + c)/2) (all exponents even)"""
    g = f
    for i, e in enumerate(mon):
        assert e % 2 == 0
        for _ in range(e):
            g = g.diff(i)
    return g.scale((-1) ** (sum(mon) // 2))


def lattice_green_terms(nmax=3, allow_forge=False):
    """1/sigma = sum_j B^j / |k|^(2 + 2j), sigma = |k|^2 - B, B = S4/12 - S6/360 + S8/20160; collect by order; returns pi G_n as RP"""
    Sk = lambda m: sum(k ** m for k in KV)
    Bpoly = Sk(4) / 12 - Sk(6) / 360 + Sk(8) / 20160
    if allow_forge and mut("symbol_forged"):
        Bpoly = Sk(4) / 6 - Sk(6) / 360 + Sk(8) / 20160
    G = {0: TRANSFORM[1]}
    for n in range(1, nmax + 1):
        G[n] = RP()
    for j in range(1, nmax + 1):
        P = sp.Poly(sp.expand(Bpoly ** j), *KV)
        for mon, coef in P.terms():
            n = (sum(mon) - 2 * j) // 2
            if 1 <= n <= nmax:
                G[n] = G[n] + apply_monomial(TRANSFORM[j + 1], mon).scale(coef)
    return G, Bpoly


def only_numerator(g, k):
    """g = P r^k exactly (canonical form with a single odd term): return P"""
    c = g.canon()
    assert list(c) == [k], c
    return c[k]


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t110, t0607 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(normalize_text(n) in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility or site privileged; Admissibility is not a dynamics axiom (the member and the ray model are supplied)")
    q = list(LANDED110)
    if mut("landed_quote_forged"):
        q[1] = q[1].replace("χ³/N", "χ²/N")
    checks.check("A3", all(x in t110 for x in q), "landed block 110: the exterior chi = 1 + a/r, N = 1 - p/r and the index n = chi^3/N")
    checks.check("A4", all(x in t0607 for x in LANDED0607), "landed 2026-06-07 note: G = 1/(4 pi r) + [5/(32 pi)] K4/r^3 + O(1/r^5) (prior art for G1)")


# ============================================================================================ family B (T1)
def family_b(checks: Checks, G) -> None:
    G, _ = lattice_green_terms(3, allow_forge=True)
    kap_ok = all((lap(TRANSFORM[m + 1]).scale(-1) - TRANSFORM[m]).is_zero() for m in (1, 2, 3)) and lap(TRANSFORM[1]).is_zero()
    k = sp.Symbol("k")
    sym_ok = sp.expand(sp.series(2 * (1 - sp.cos(k)), k, 0, 10).removeO() - (k ** 2 - k ** 4 / 12 + k ** 6 / 360 - k ** 8 / 20160)) == 0
    S4 = sum(v ** 4 for v in X)
    r4 = (X[0] ** 2 + X[1] ** 2 + X[2] ** 2) ** 2
    P1 = only_numerator(G[1], -7)
    g1_ok = sp.expand(P1.as_expr() - (5 * S4 - 3 * r4) / 32) == 0
    # the landed form [5/(32 pi)] (sum n^4 - 3/5)/r^3 equals (5 S4 - 3 r^4)/(32 pi r^7)
    g1_landed = sp.expand(sp.Rational(5, 32) * (S4 - sp.Rational(3, 5) * r4) - (5 * S4 - 3 * r4) / 32) == 0
    e5 = (lap(G[1]) + Dn(G[0], 4).scale(sp.Rational(1, 12))).is_zero()
    e7 = (lap(G[2]) + Dn(G[1], 4).scale(sp.Rational(1, 12)) + Dn(G[0], 6).scale(sp.Rational(1, 360))).is_zero()
    e9 = (lap(G[3]) + Dn(G[2], 4).scale(sp.Rational(1, 12)) + Dn(G[1], 6).scale(sp.Rational(1, 360)) + Dn(G[0], 8).scale(sp.Rational(1, 20160))).is_zero()
    checks.check("B1", kap_ok and sym_ok, "the lattice symbol is k^2 - k^4/12 + k^6/360 - k^8/20160 per axis, and the transforms of |k|^-2, -4, -6, -8 obey -Lap T[m+1] = T[m]")
    checks.check("B2", g1_ok and g1_landed, "G1 = (5 sum x^4 - 3 r^4)/(32 pi r^7), equal to the landed 2026-06-07 form [5/(32 pi)] K4/r^3")
    checks.check("B3", e5 and e7 and e9, "G1, G2 and G3 (from the symbol) satisfy the lattice equation -Delta_lat G = 0 away from the source at orders r^-5, r^-7 and r^-9, exactly")
    # uniqueness of G1: a cubic-invariant degree -3 correction is c r^2/r^5 = c r^-3, and Lap r^-3 = 6 r^-5 != 0
    uniq = (lap(RP.rpow(-3)) - RP.rpow(-5, 6)).is_zero() and not lap(RP.rpow(-3)).is_zero()

    def sphere_avg(P):
        tot = sp.Integer(0)
        for mon, coef in P.terms():
            if any(e % 2 for e in mon):
                continue
            n = sum(mon) // 2
            tot += coef * sp.prod([sp.factorial2(e - 1) for e in mon]) / sp.factorial2(2 * n + 1)
        return sp.simplify(tot)
    P2 = only_numerator(G[2], -13)
    no_l0 = sphere_avg(P1) == 0 and sphere_avg(P2) == 0
    checks.check("B4", uniq and no_l0, "G1 is the only degree -3 cubic-invariant correction the local equation allows, and G1, G2 have no l = 0 part (exact sphere averages zero)")


# ============================================================================================ family C (T2)
def family_c(checks: Checks, G) -> None:
    P1 = only_numerator(G[1], -7)
    # G1/G0 = 4 P1(x)/r^6 = 4 P1(n)/r^2 for a unit direction n
    vals = []
    for d in ((1, 0, 0), (1, 1, 0), (1, 1, 1)):
        nrm2 = sum(c * c for c in d)
        v = 4 * P1.as_expr().subs({X[i]: d[i] for i in range(3)}) / nrm2 ** 2
        vals.append(sp.nsimplify(v))
    want = [sp.Rational(1, 4), -sp.Rational(1, 16), -sp.Rational(1, 6)]
    if mut("anisotropy_forged"):
        want[1] = sp.Rational(1, 16)
    checks.check("C1", vals == want, f"the fields' relative anisotropy G1/G0 = (5 sum x^4/r^4 - 3)/(8 r^2): {vals[0]}/r^2 on an axis, {vals[1]}/r^2 on a face diagonal, {vals[2]}/r^2 on a body diagonal")


# ============================================================================================ family D (T3)
b, s, phi = sp.symbols("b s phi", positive=True)


def line_integral(P, m, tvec, beta):
    """integral over s of P/r^(2m + 1) at x = b beta + s t, beta a unit vector orthogonal to the unit vector t (so r^2 = b^2 + s^2)"""
    num = sp.expand(P.subs({X[i]: b * beta[i] + s * tvec[i] for i in range(3)}, simultaneous=True))
    tot = sp.Integer(0)
    for (j,), coef in sp.Poly(num, s).terms():
        if j % 2:
            continue
        jj = j // 2
        tot += coef * b ** (2 * jj - 2 * m) * sp.gamma(jj + sp.Rational(1, 2)) * sp.gamma(m - jj) / sp.gamma(m + sp.Rational(1, 2))
    return sp.simplify(tot)


def family_d(checks: Checks, G) -> None:
    P1 = only_numerator(G[1], -7).as_expr() * 4
    P2 = only_numerator(G[2], -13).as_expr() * 4
    S4 = lambda v: sum(x ** 4 for x in v)
    S22 = lambda t_, u_: sum(t_[i] ** 2 * u_[i] ** 2 for i in range(3))
    dirs = {
        "axis": ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
        "face diagonal": ((1 / sp.sqrt(2), 1 / sp.sqrt(2), 0), (0, 0, 1), (1 / sp.sqrt(2), -1 / sp.sqrt(2), 0)),
        "body diagonal": ((1 / sp.sqrt(3), 1 / sp.sqrt(3), 1 / sp.sqrt(3)), (1 / sp.sqrt(2), -1 / sp.sqrt(2), 0), (1 / sp.sqrt(6), 1 / sp.sqrt(6), -2 / sp.sqrt(6))),
    }
    want1 = {"axis": sp.cos(4 * phi) / 6, "face diagonal": -sp.cos(2 * phi) / 12 + sp.cos(4 * phi) / 8, "body diagonal": sp.Integer(0)}
    want2 = {"axis": sp.Rational(3, 20) * sp.cos(4 * phi) + sp.Rational(5, 24) * sp.cos(8 * phi),
             "face diagonal": sp.Rational(19, 192) * sp.cos(4 * phi) - sp.Rational(1, 10) * sp.cos(6 * phi) + sp.Rational(15, 128) * sp.cos(8 * phi),
             "body diagonal": -sp.Rational(4, 135) * sp.cos(6 * phi)}
    if mut("table_forged"):
        want1["axis"] = sp.cos(4 * phi) / 3
    ok = True
    got = {}
    for name, (tv, u, v) in dirs.items():
        beta = [sp.cos(phi) * u[i] + sp.sin(phi) * v[i] for i in range(3)]
        f1 = sp.simplify(line_integral(P1, 3, tv, beta) * b ** 2)
        f2 = sp.simplify(line_integral(P2, 6, tv, beta) * b ** 4)
        formula = S4(tv) / 4 + S22(tv, beta) + sp.Rational(2, 3) * S4(beta) - sp.Rational(3, 4)
        ok = ok and sp.simplify(sp.expand_trig(f1 - want1[name])) == 0 and sp.simplify(sp.expand_trig(f2 - want2[name])) == 0
        ok = ok and sp.simplify(sp.expand_trig(f1 - formula)) == 0
        got[name] = (sp.simplify(f1), sp.simplify(f2))
    for name, (f1, f2) in got.items():
        print(f"   {name}: f1 = {f1}, f2 = {f2}")
    checks.check("D1", ok, "along the axis, the face diagonal and the body diagonal, the line integrals of 4 pi G1 and 4 pi G2 give the table's f1 and f2, and f1 = (1/4) sum t^4 + sum t^2 beta^2 + (2/3) sum beta^4 - 3/4; on the body diagonal f1 = 0 identically")
    # azimuthal average of f1 for a generic (Pythagorean) direction, and the general formula there
    tv = (sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7))
    u = (sp.Rational(3, 7), -sp.Rational(6, 7), sp.Rational(2, 7))
    v = tuple(sp.Matrix(tv).cross(sp.Matrix(u)))
    beta = [sp.cos(phi) * u[i] + sp.sin(phi) * v[i] for i in range(3)]
    f1 = sp.simplify(line_integral(P1, 3, tv, beta) * b ** 2)
    formula = S4(tv) / 4 + S22(tv, beta) + sp.Rational(2, 3) * S4(beta) - sp.Rational(3, 4)
    avg = sp.simplify(sp.integrate(sp.expand(sp.expand_trig(f1)), (phi, 0, 2 * sp.pi)) / (2 * sp.pi))
    checks.check("D2", sp.simplify(sp.expand_trig(f1 - formula)) == 0 and avg == 0, "for the direction (2,3,6)/7 the line integral matches the f1 formula and averages to zero over the azimuth; the table's f2 terms are pure cosines, so they average to zero too")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    M = sp.Symbol("M", positive=True)
    a = p = M / 2
    lattice = (3 * a + p) * 2 * (sp.Rational(1, 6)) / b ** 3  # axis, phi = 0: the b^-3 part toward the body, 2 f1/b^3 with f1 = 1/6
    cont2 = sp.Rational(15, 4) * sp.pi * (M / b) ** 2
    ratio = sp.simplify(lattice / cont2)
    want = sp.Rational(8, 45) / (sp.pi * M * b)
    if mut("ratio_forged"):
        want = want * 2
    checks.check("E1", sp.simplify(ratio - want) == 0, f"at a = p = M/2, the axis lattice term at phi = 0 against the continuum second-order (15 pi/4)(M/b)^2: ratio {ratio}")


# ============================================================================================ family G
FENCES = (
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
    "nothing is adopted and no gravitational claim is made.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the body diagonal."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Watson", "Duffin",
                   "Maradudin", "Martinsson", "Rodin", "Hankel", "Bouguer", "Schwarzschild")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Duffin) —", 1)
    norm = normalize_text(text)
    checks.check("G1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("G2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("G3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
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
    checks.check("G4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family H
N5_LINES = (
    "per_element: executed - the lattice symbol's expansion and the transforms of |k|^-2m",
    "per_site: executed - G1, G2, G3 from the symbol; the lattice equation away from the source at orders r^-5, r^-7, r^-9; G1 against the landed 2026-06-07 form",
    "per_mode: executed - the line integrals of 4 pi G1 and 4 pi G2 along the axis, face and body diagonals, and for the direction (2,3,6)/7",
    "per_block: executed - uniqueness of G1; no l = 0 parts; the azimuthal averages; the size against the continuum second order",
    "lattice_wide: checked and not executed - the remainder bound of the expansion (imported; the referee compared with the exact lattice potential out to r about 40 in floating point); rays integrated directly (floating point in the probe and the referee); second order in the charges; finite wave number",
)


def family_h(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("H1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


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
    G, _ = lattice_green_terms(3)
    family_a(checks, texts)
    family_b(checks, G)
    family_c(checks, G)
    family_d(checks, G)
    family_e(checks)
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: at first order in the charges the member's lattice exterior is Q G and P G; G's corrections G1 (landed), G2, G3 from the symbol; the first direction-dependent turn is at b^-3 with f1, zero on the body diagonal and averaging to zero; a harvest of probe #9364, refereed by Claude Sonnet (same family); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
