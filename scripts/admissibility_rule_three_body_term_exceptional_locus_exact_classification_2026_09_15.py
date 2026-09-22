#!/usr/bin/env python3
"""Exact checks: the exceptional locus of the three-body term of the six-menu product rule.

Scope.  The six Bloch-axis menu with the covariant positive product rule (p, q, r); the normalizer values Z_k; the mixed
differences of log K_3 as polynomial numerators over Q (r = 1).  X1: the two mixed-difference ratios of K_2 factor so that
both equal 1 only at p = q = r.  X2: on the line p = q the witness E_1 factors as -8 (t-1)^3 (t^3 - 3t^2 - 6t - 1) and E_2
vanishes; on the line p = r the Z_3 values collapse to three polynomials and every numerator carries the factor
(q-1)^3 (q^3 - 3q^2 - 15q - 19).  X3: the lex Groebner basis of (E_1, G) gives the univariate h(q) with the factors
(q-1)^6, the rho-cubic, the sextic s and a sextic without positive roots; on s, p = psi(q) exchanges the two positive
roots; all 16 numerators vanish at the six points (reductions modulo the minimal polynomials).  X5: all 16 numerators
are nonzero at (3,1,2) and (5,2,4).  Exact arithmetic (sympy over Q; Sturm isolation; no floating point).
"""

from __future__ import annotations

import itertools
import re
import sys
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THREE_BODY_TERM_EXCEPTIONAL_LOCUS_EXACT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_MONOTONE_FORMATION_LAW_PLANE_CHAIN_COUPLING_REGION_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/ADMISSIBILITY_RULE_RECORDED_SET_GIBBS_THEOREM_FORMATION_LAWS_MARKOV_GRAPH_BOUNDED_THEOREM_NOTE_2026-09-15.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
CLAIM_ID = "admissibility_rule_three_body_term_exceptional_locus_exact_classification_bounded_theorem_note_2026-09-15"
BLOCK08_CLAIM_ID = "admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15"
BLOCK10_CLAIM_ID = "admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_bounded_theorem_note_2026-09-15"
BLOCK10_FRAGMENT = "nonzero at every nonconstant triple"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
)

MUTATION_GATE = {
    "pattern_values_wrong": "B",
    "k2_ratio_factor_wrong": "B",
    "line_pq_factor_wrong": "B",
    "line_pr_values_wrong": "B",
    "declared_triple_on_locus_claimed": "B",
    "h_factor_wrong": "C",
    "psi_not_root_claimed": "C",
    "offline_pair_denied": "C",
    "numerators_nonzero_at_point_claimed": "C",
    "claim_physical_rule": "F",
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
        self.failed_families: list[str] = []

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        if not ok:
            self.failed_families.append(label[0])
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


p, q, r, t = sp.symbols("p q r t", positive=True)
R = sp.Rational
M = 6


def orbit_type(s: int, u: int) -> str:
    if s == u:
        return "p"
    if s // 2 == u // 2:
        return "q"
    return "r"


def z3_def(a, b, c, wp, wq, wr):
    w = {"p": wp, "q": wq, "r": wr}
    return sp.expand(sum(w[orbit_type(s, a)] * w[orbit_type(s, b)] * w[orbit_type(s, c)] for s in range(M)))


def z2_def(a, b, wp, wq, wr):
    w = {"p": wp, "q": wq, "r": wr}
    return sp.expand(sum(w[orbit_type(s, a)] * w[orbit_type(s, b)] for s in range(M)))


V1 = p**3 + q**3 + 4 * r**3
V2 = p * q * (p + q) + 4 * r**3
V3 = r * (p**2 + q**2) + r**2 * (p + q) + 2 * r**3
V4 = 2 * p * q * r + r**2 * (p + q) + 2 * r**3
V5 = 3 * r**2 * (p + q)
E1 = sp.expand((V1 * V5**2 - V3**3).subs(r, 1))
E2 = sp.expand((V1 * V4**2 - V2 * V3**2).subs(r, 1))
SEXTIC = sp.Poly(q**6 - 6 * q**5 - 3 * q**4 + 4 * q**3 - 3 * q**2 - 6 * q + 31, q)
RHO_CUBIC = sp.Poly(q**3 - 3 * q**2 - 15 * q - 19, q)
T_CUBIC = sp.Poly(q**3 - 3 * q**2 - 6 * q - 1, q)
U_SEXTIC = sp.Poly(q**6 + 3 * q**5 + 6 * q**4 + 13 * q**3 + 15 * q**2 + 12 * q + 22, q)
PSI = -R(8, 85) * q**5 + R(116, 255) * q**4 + R(196, 255) * q**3 + R(82, 85) * q**2 + R(121, 255) * q + R(356, 255)


def numerators():
    """The distinct nonzero third-difference numerators num - den over all argument tuples (r = 1)."""
    cache = {}

    def z(a, b, c):
        key = tuple(sorted((a, b, c)))
        if key not in cache:
            cache[key] = z3_def(a, b, c, p, q, sp.Integer(1))
        return cache[key]
    out = set()
    for a, a2, b, b2, c, c2 in itertools.product(range(M), repeat=6):
        if a == a2 or b == b2 or c == c2:
            continue
        n = sp.expand(z(a, b, c) * z(a2, b2, c) * z(a2, b, c2) * z(a, b2, c2) - z(a2, b, c) * z(a, b2, c) * z(a, b, c2) * z(a2, b2, c2))
        if n != 0:
            out.add(n)
    return sorted(out, key=str)


def positive_intervals(P: sp.Poly, eps):
    return [P.refine_root(a, b, eps=eps) for (a, b), m in P.intervals() if b > 0]


def horner_interval(poly, a, b):
    lo, hi = sp.Integer(0), sp.Integer(0)
    for c in sp.Poly(poly, q).all_coeffs():
        cands = [lo * a, lo * b, hi * a, hi * b]
        lo, hi = min(cands) + c, max(cands) + c
    return lo, hi


# ============================================================================================ family A
def family_a(checks: Checks, note_text: str, axiom_text: str, b08: str, b10: str) -> None:
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4,
                 "the four declared inputs exist (this note, the axiom memo, block 08, block 10)")
    checks.check("A2", all(n in normalize_text(axiom_text) for n in AXIOM_NEEDLES), "the three axiom sentences used are present verbatim in the axiom memo")
    f08, f10 = normalize_text(b08).lower(), normalize_text(b10).lower()
    checks.check("A3", BLOCK08_CLAIM_ID in f08 and BLOCK10_CLAIM_ID in f10 and BLOCK10_FRAGMENT in f10,
                 "the parents' claim ids and block 10's open-lemma fragment are present")
    flat = normalize_text(note_text)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def family_b(checks: Checks, report: dict) -> None:
    x, mx, y, z = 0, 1, 2, 4
    pv = [sp.expand(z3_def(x, x, x, p, q, r) - V1), sp.expand(z3_def(x, x, mx, p, q, r) - V2), sp.expand(z3_def(x, x, y, p, q, r) - V3),
          sp.expand(z3_def(x, mx, y, p, q, r) - V4), sp.expand(z3_def(x, y, z, p, q, r) - V5)]
    vals = {z3_def(a, b, c, p, q, r) for a in range(M) for b in range(M) for c in range(M)}
    n_vals = len(vals) + (1 if mut("pattern_values_wrong") else 0)
    checks.check("B1", all(v == 0 for v in pv) and n_vals == 5, f"the five pattern values V_1..V_5 match the definition; Z_3 takes {len(vals)} distinct values over the 216 triples")
    nums = numerators()
    report["nums"] = nums
    checks.check("B2", len(nums) == 16, f"there are {len(nums)} distinct nonzero third-difference numerators over the 6^6 argument tuples (r = 1)")
    r1 = sp.factor(z2_def(mx, mx, p, q, r) * z2_def(x, x, p, q, r) / (z2_def(mx, x, p, q, r) * z2_def(x, mx, p, q, r)))
    r2 = sp.factor(z2_def(y, y, p, q, r) * z2_def(x, x, p, q, r) / (z2_def(y, x, p, q, r) * z2_def(x, y, p, q, r)))
    exp1 = ((p**2 + q**2 + 4 * r**2) / (2 * (p * q + 2 * r**2)))**2
    exp2 = ((p**2 + q**2 + 4 * r**2) / (2 * r * (p + q + r)))**2
    ok1 = sp.simplify(r1 - exp1) == 0 and sp.simplify(r2 - exp2) == 0
    cond = sp.factor(sp.expand((p**2 + q**2 + 4 * r**2) - 2 * r * (p + q + r)))
    ok2 = sp.expand(cond - ((p - r)**2 + (q - r)**2)) == 0
    if mut("k2_ratio_factor_wrong"):
        ok2 = False
    checks.check("B3", ok1 and ok2, "X1: the two K_2 ratios are [(p^2+q^2+4r^2)/(2(pq+2r^2))]^2 and [(p^2+q^2+4r^2)/(2r(p+q+r))]^2; the second is 1 iff (p-r)^2 + (q-r)^2 = 0")
    e1_line = sp.factor(E1.subs({p: t, q: t}))
    e2_line = sp.expand(E2.subs({p: t, q: t}))
    target = -8 * (t - 1)**3 * (t**3 - 3 * t**2 - 6 * t - 1)
    ok_line = sp.expand(e1_line - target) == 0 and e2_line == 0
    if mut("line_pq_factor_wrong"):
        ok_line = False
    W1, W2, W3 = 2 * t**3 + 4, 2 * (t**2 + t + 1), 6 * t
    collapse = sp.expand(W2**3 - W1 * W3**2 - 8 * (t - 1)**3 * (t**3 - 3 * t**2 - 6 * t - 1)) == 0
    tiv = positive_intervals(T_CUBIC, R(1, 10**6))
    checks.check("B4", ok_line and collapse and len(tiv) == 1 and 4 < tiv[0][0] and tiv[0][1] < 5 and len(T_CUBIC.intervals()) == 3,
                 "X2a: on p = q, E_1 = -8(t-1)^3(t^3-3t^2-6t-1), E_2 = 0, W_2^3 - W_1 W_3^2 = 8(t-1)^3(t^3-3t^2-6t-1); the cubic has three real roots and one positive root in (4,5)")
    vals_pr = {z3_def(a, b, c, sp.Integer(1), q, sp.Integer(1)) for a in range(M) for b in range(M) for c in range(M)}
    exp_pr = {sp.expand(q**3 + 5), sp.expand(q**2 + q + 4), sp.expand(3 * q + 3)}
    fac_ok = True
    for n in nums:
        nl = sp.Poly(sp.expand(n.subs(p, 1)), q)
        if nl.is_zero:
            continue
        rem1 = nl.rem(sp.Poly((q - 1)**3, q))
        rem2 = nl.rem(RHO_CUBIC)
        fac_ok = fac_ok and rem1.is_zero and rem2.is_zero
    if mut("line_pr_values_wrong"):
        vals_pr = vals_pr | {sp.Integer(7)}
    riv = positive_intervals(RHO_CUBIC, R(1, 10**6))
    checks.check("B5", vals_pr == exp_pr and fac_ok and len(riv) == 1 and 6 < riv[0][0] and riv[0][1] < 7,
                 "X2b: on p = r, Z_3 takes the three values q^3+5, q^2+q+4, 3q+3; every numerator on the line is divisible by (q-1)^3 (q^3-3q^2-15q-19); the cubic's positive root lies in (6,7)")
    sym = all(sp.expand(n.subs({p: q, q: p}, simultaneous=True) - n) == 0 for n in nums)
    checks.check("B6", sym, "X2c: every numerator is symmetric in (p, q), so the line q = r mirrors the line p = r")
    on = {}
    for tr in ((R(3, 2), R(1, 2)), (R(5, 4), R(1, 2))):
        on[tr] = sum(1 for n in nums if n.subs({p: tr[0], q: tr[1]}) != 0)
    nz_ok = all(v == 16 for v in on.values())
    if mut("declared_triple_on_locus_claimed"):
        nz_ok = all(v == 0 for v in on.values())
    checks.check("B7", nz_ok, f"X5: at (3,1,2) and (5,2,4) all 16 numerators are nonzero ({on[(R(3, 2), R(1, 2))]}, {on[(R(5, 4), R(1, 2))]})")


# ============================================================================================ family C
def family_c(checks: Checks, report: dict, exact: bool) -> None:
    nums = report["nums"]
    G = sp.expand(sp.cancel(sp.factor(E2) / (-(p - q)**2)))
    Gb = sp.groebner([E1, G], p, q, order="lex")
    h = [g for g in Gb.exprs if not g.has(p)][0]
    hp = sp.Poly(h, q)
    target_h = (q - 1)**6 * RHO_CUBIC.as_expr() * SEXTIC.as_expr() * U_SEXTIC.as_expr()**2
    lead = sp.Poly(sp.expand(target_h), q).LC()
    h_ok = sp.expand(h * lead / hp.LC() - target_h) == 0
    u_pos = positive_intervals(U_SEXTIC, R(1, 10**6))
    if mut("h_factor_wrong"):
        h_ok = False
    checks.check("C1", h_ok and len(u_pos) == 0 and len(Gb.exprs) == 3,
                 "X3 algebraic identity: the lex Groebner basis of (E_1, G) has three elements; its univariate part is (q-1)^6 (q^3-3q^2-15q-19) s(q) u(q)^2 with u without positive roots")
    lin = [g for g in Gb.exprs if sp.Poly(g, p).degree() == 1][0]
    A = sp.expand(sp.Poly(lin, p).coeff_monomial(p))
    B = sp.expand(-sp.Poly(lin, p).coeff_monomial(1))
    Ainv = sp.invert(sp.Poly(A, q), SEXTIC)
    psi = (sp.Poly(B, q) * Ainv).rem(SEXTIC)
    psi_ok = sp.expand(psi.as_expr() - PSI) == 0
    s_psi = sp.Poly(sp.expand(SEXTIC.as_expr().subs(q, PSI)), q).rem(SEXTIC).is_zero
    e1_psi = sp.Poly(sp.expand(E1.subs(p, PSI)), q).rem(SEXTIC).is_zero
    g_psi = sp.Poly(sp.expand(G.subs(p, PSI)), q).rem(SEXTIC).is_zero
    Ainv_r = sp.invert(sp.Poly(A, q), RHO_CUBIC)
    p_rho = (sp.Poly(B, q) * Ainv_r).rem(RHO_CUBIC)
    if mut("psi_not_root_claimed"):
        s_psi = False
    checks.check("C2", psi_ok and s_psi and e1_psi and g_psi and p_rho.as_expr() == 1,
                 "X3 construction: on the sextic factor p = psi(q) with s(psi) = E_1(psi, q) = G(psi, q) = 0 modulo s; on the rho-cubic p = 1")
    eps = R(1, 10**30)
    ivs = positive_intervals(SEXTIC, eps)
    coarse = [(a, b) for (a, b), m in SEXTIC.intervals() if b > 0]  # the initial isolating intervals, one per positive root
    pairing = True
    for a, b in ivs:
        lo, hi = horner_interval(PSI, a, b)
        # psi(root) is itself a root of s (s(psi) = 0 mod s); its exact enclosure must lie in the coarse interval of the OTHER root
        inside = [cv for cv in coarse if cv[0] <= lo and hi <= cv[1]]
        own = [cv for cv in coarse if cv[0] <= a and b <= cv[1]]
        pairing = pairing and len(inside) == 1 and len(own) == 1 and inside[0] != own[0]
    if mut("offline_pair_denied"):
        pairing = False
    checks.check("C3", len(ivs) == 2 and 1 < ivs[0][0] and ivs[0][1] < 2 and 6 < ivs[1][0] and ivs[1][1] < 7 and pairing,
                 "X3: s has exactly two positive roots, in (1,2) and (6,7), and the exact enclosure of psi over each refined isolating interval lies inside the other root's coarse isolating interval: psi exchanges sigma_1 and sigma_2")
    points = [("(1,1)", sp.Integer(1), sp.Poly(q - 1, q)), ("(t*,t*)", q, T_CUBIC), ("(1,rho)", sp.Integer(1), RHO_CUBIC), ("(sigma1,sigma2)", PSI, SEXTIC)]
    all_zero = True
    detail = []
    for name, subp, modulus in points:
        bad = sum(1 for n in nums if not sp.Poly(sp.expand(n.subs(p, subp)), q).rem(modulus).is_zero)
        detail.append(f"{name}: {bad}")
        all_zero = all_zero and bad == 0
    if mut("numerators_nonzero_at_point_claimed"):
        all_zero = False
    checks.check("C4", all_zero, "X3 sufficiency: all 16 numerators reduce to zero at each of the four representative points (their mirrors follow by B6): " + "; ".join(detail))
    if exact:
        print(f"exact h(q) = {sp.factor(h)}")
        print(f"exact isolating intervals of s: {[(str(a), str(b)) for a, b in ivs]}")


# ============================================================================================ family F
FENCES = (
    "This note constructs six pair-additive points and verifies exact polynomial identities for the supplied six-axis product rule; exhaustive classification is deferred. It states nothing infinite-volume beyond the hypothesis map of X4, selects no rule or order as physical, and gives no structural reason for the off-line pair.",
    "No plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "no value, constant or theorem is imported as authority.",
)
FORBIDDEN = (
    "the physical rule", "the physical order", "for every coupling", "selects the", "fires wake condition", "the Bridge weights",
    "the Bridge conjecture", "certified", "phase transition", "washes out", "toward the plane", "the trend",
)
CLAIM_INJECTIONS = {"claim_physical_rule": "The point t* is the physical rule."}
CLASSICAL_NAMES = ("Buchberger", "Sturm", "Groebner", "Gröbner", "Sylvester", "Dobrushin", "Kolmogorov")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    nroots = "nro" + "ots("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln or nroots in ln]
    checks.check("F3", not bad and len(scan) > 200, f"runner source: no floating-point literal, conversion or numeric root call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.splitlines()[0].strip()
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem X3"):
            body = body + " (by Buchberger)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art and Imports ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — all 16 distinct third-difference numerators at the four representative exceptional points (exact reductions) and at the two declared triples; the two K_2 ratios factored",
    "per_site: not applicable — no lattice sites enter; the objects are polynomials in the weights",
    "per_mode: executed — the five pattern values of Z_3 against the definition on all 216 triples; the three-letter collapse on p = q and the three values on p = r",
    "per_block: executed — the lex Groebner basis, the factorization of h, the sextic's isolating intervals refined to 10^-30, the exchange psi(sigma_1) = sigma_2 by exact enclosure",
    "lattice_wide: polynomial identities at their stated domains and six sufficiency constructions; exhaustive locus certification deferred; infinite-law remarks only under X4 hypotheses",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5 and all(len(l) >= 40 for l in N5_LINES), "the five N5 resolution lines are printed")


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
    exact = "--exact" in argv
    checks = Checks()
    texts = [(ROOT / pth).read_text(encoding="utf-8") if (ROOT / pth).is_file() else "" for pth in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for pth in AUDIT_INPUT_PATHS:
        print(f"  {pth}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: six pair-additive constructions; exhaustive classification deferred — pattern values, the 16 numerators, X1's factorizations, the three collapse lines, the Groebner elimination, the sextic pair, the reductions at the six points, the declared triples; exact")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, texts[0], texts[1], texts[2], texts[3])
    family_b(checks, report)
    family_c(checks, report, exact)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
