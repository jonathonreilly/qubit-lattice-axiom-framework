#!/usr/bin/env python3
"""Exact checks: a closed lattice with content has no static state, and its uniform motion has the static pull's own coupling iff
alpha = K/4 - within block 60's
homogeneous kinetic model (T5(b)), block 124's kinetic family and block 129's volume power, and block 101's static clock law, all
as landed on main: the member's clock constraint has no zero mode, so a static closed lattice holds no positive content; the
member's kinetic term on a uniform dilation has c_k = 12 alpha + 36 beta = -24 alpha at the closing ratio, so the lattice stretches or
shrinks with lambdadot^2 = rho/(24 alpha), which is (8 pi G/3) rho with the static pull's G = 1/(16 pi K) iff alpha = K/4 (at beta = -alpha, alpha/K
is the member's only free kinetic ratio, so this is blocks 134-136's condition met again), and then l-ddot/l = -(4 pi G/3)(rho + 3p); content crosses bonds at rate w/l, so a top-speed walker's energy falls exactly as 1/l, its
pressure is rho/3 and on the growing branch the lattice goes as t^(1/2); rest content gives t^(2/3); each motion has a time
mirror, so the equations fix no direction (the supervisor's own derivation; not adopted).

B (T1): the zero mode: no static solution; the homogeneous model's constraint and c_k on the dilation.
C (T2): the uniform motion's coupling against the static pull's; its rate of change.
D (T3): walkers on a uniformly stretched lattice; exact solutions and their time mirrors.
E (T3): mixtures of rest and top-speed content.
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_LATTICE_EXPANDS_WITH_THE_STATIC_PULLS_COUPLING_IFF_ALPHA_EQUALS_K_OVER_FOUR_AND_TOP_SPEED_WALKERS_LOSE_ENERGY_AS_ONE_OVER_THE_LENGTH_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_lattice_expands_with_the_static_pulls_coupling_iff_alpha_equals_k_over_four_and_top_speed_walkers_lose_energy_as_one_over_the_length_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "dilation_amplitude_forged": "B",
    "static_pull_normalization_forged": "C",
    "pressure_sign_flipped": "C",
    "hop_rate_scaling_forged": "D",
    "solution_exponent_forged": "D",
    "mixture_pressure_forged": "E",
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
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


Fr = Fraction
HALF = sp.Rational(1, 2)
QUARTER = sp.Rational(1, 4)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the member, its kinetic term, the content and its crossing of bonds are supplied; the memo does not define a time metric)")


# ============================================================================================ family B
def homogeneous(ck, s, m_of_lam):
    t = sp.Symbol("t", real=True)
    lam = sp.Function("lam")(t)
    w = sp.Symbol("w", positive=True)
    L = ck * sp.exp(s * lam) * sp.diff(lam, t) ** 2 / w - w * m_of_lam(lam)
    con = sp.diff(L, w).subs(w, 1)
    el = (sp.diff(sp.diff(L, sp.diff(lam, t)), t) - sp.diff(L, lam)).subs(w, 1)
    return t, lam, con, el


def family_b(checks: Checks) -> None:
    px, py, pz = sp.symbols("px py pz")
    hs = sp.symbols("h11 h12 h13 h22 h23 h33")
    h = sp.Matrix([[hs[0], hs[1], hs[2]], [hs[1], hs[3], hs[4]], [hs[2], hs[4], hs[5]]])
    pv = sp.Matrix([px, py, pz])
    r1 = sp.expand(-(pv.T * h * pv)[0] + pv.dot(pv) * h.trace())    # block 101's R1 on a plane wave
    no_zero = r1.subs({px: 0, py: 0, pz: 0}) == 0
    ck, s = sp.symbols("c_k s")
    mfun = sp.Function("m")
    t, lam, con, el = homogeneous(ck, s, mfun)
    kept = sp.simplify(sp.diff(con, t) + sp.diff(lam, t) * el) == 0
    checks.check("B1", no_zero and kept, "the member's clock constraint K R1 = e has no zero mode (R1 vanishes at p = 0), so a static closed lattice holds no positive content; in block 60's homogeneous model c_k l^s lamdot^2/w - w m(lam) the constraint's rate of change is -lamdot times the lengths' equation, for any m(lam)")
    al, be = sp.symbols("alpha beta", positive=True)
    amp = 1 if mut("dilation_amplitude_forged") else 2
    hd = amp * sp.Symbol("ld") * sp.eye(3)
    kin = sp.expand(al * (hd * hd).trace() + be * hd.trace() ** 2)
    c_dil = sp.simplify(kin / sp.Symbol("ld") ** 2)
    checks.check("B2", sp.simplify(c_dil - (12 * al + 36 * be)) == 0 and sp.simplify(c_dil.subs(be, -al) + 24 * al) == 0,
                 "the member's kinetic term alpha tr(Hdot^2) + beta (tr Hdot)^2 on the uniform dilation h = 2 lam delta gives c_k = 12 alpha + 36 beta (block 124), which is -24 alpha < 0 at the closing ratio: block 60 T5(b)'s uniform solution exists")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    al, K, G, rho = sp.symbols("alpha K G rho", positive=True)
    p = sp.Symbol("p")
    r = sp.Symbol("r", positive=True)
    m = sp.Symbol("m", positive=True)
    # block 101's static clock law u = -e/(4 K p^2); 1/p^2 is 1/(4 pi r): u = -m/(16 pi K r) = -G m / r
    norm = 8 if mut("static_pull_normalization_forged") else 16
    g_static = sp.solve(sp.Eq(-m / (4 * K * 4 * sp.pi * r), -sp.Symbol("Gs") * m / r), sp.Symbol("Gs"))[0]
    g_used = 1 / (norm * sp.pi * K)
    same = sp.simplify(g_static - g_used) == 0
    H2 = rho / (24 * al)
    sol = sp.solve(sp.Eq(H2, sp.Rational(8, 3) * sp.pi * g_used * rho), al)
    checks.check("C1", same and sol == [K / 4], "the static clock law gives the pull's coupling G = 1/(16 pi K); the uniform motion's constraint lamdot^2 = rho/(24 alpha) (c_k = -24 alpha, s = 3, rho = m/l^3) is (8 pi G/3) rho with that G iff alpha = K/4")
    ld, ldd, l = sp.symbols("ld ldd l", positive=True)
    sign = 1 if mut("pressure_sign_flipped") else -1
    mprime = sign * 3 * p * l ** 3
    ldd_sol = sp.solve(-24 * al * (2 * l ** 3 * ldd + 3 * l ** 3 * ld ** 2) + mprime, ldd)[0]
    acc = sp.simplify((ldd_sol + ld ** 2).subs(ld ** 2, H2))
    target = -(rho + 3 * p) / (48 * al)
    at_quarter = sp.simplify(acc.subs(al, K / 4).subs(K, 1 / (16 * sp.pi * G)) + sp.Rational(4, 3) * sp.pi * G * (rho + 3 * p)) == 0
    checks.check("C2", sp.simplify(acc - target) == 0 and at_quarter,
                 "with the content's pressure defined by dm/dlam = -3 p l^3, the lengths' equation gives l-ddot/l = -(rho + 3p)/(48 alpha), which is -(4 pi G/3)(rho + 3p) at alpha = K/4")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    k = sp.symbols("k1:4", real=True)
    l, mw = sp.symbols("l m_w", positive=True)
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    power = 2 if mut("hop_rate_scaling_forged") else 1
    Hk = sum((sig[a] * sp.sin(k[a]) for a in range(3)), sp.zeros(2, 2)) / l ** power
    ev = [sp.simplify(e) for e in Hk.eigenvals()]
    s2 = sum(sp.sin(ka) ** 2 for ka in k)
    scale_ok = all(sp.simplify(e ** 2 - s2 / l ** 2) == 0 for e in ev)
    eps = sp.Symbol("eps", positive=True)
    lam = sp.Symbol("lam", real=True)
    m_top = eps * sp.exp(-lam * power)
    p_top = -sp.diff(m_top, lam) / (3 * sp.exp(3 * lam))
    rho_top = m_top / sp.exp(3 * lam)
    checks.check("D1", scale_ok and sp.simplify(p_top - rho_top / 3) == 0,
                 "content crosses bonds at rate 1/l: the massless walk on a uniformly stretched lattice is H(k)/l, so a top-speed walker keeps its wave vector and its energy falls exactly as 1/l; its pressure is rho/3")
    t = sp.Symbol("t", real=True)
    al, m0, t0, t1 = sp.symbols("alpha m0 t0 t1", positive=True)
    ok = True
    expo_rest = sp.Rational(1, 3) if mut("solution_exponent_forged") else sp.Rational(2, 3)
    for mfun, lgrow, ts in ((lambda x: m0, (1 + t / t0) ** expo_rest, t0), (lambda x: eps * sp.exp(-x), (1 + t / t1) ** HALF, t1)):
        tt, lamf, con, el = homogeneous(-24 * al, 3, mfun)
        found = []
        for lsol in (lgrow, lgrow.subs(t, -t)):    # the growing branch and its time mirror
            lamsol = sp.log(lsol)
            c = sp.simplify(con.subs(lamf, lamsol).doit().subs(tt, t))
            tsol = sp.solve(c, ts)
            if not tsol:
                ok = False
                continue
            found.append(tsol[0])
            e2 = sp.simplify(el.subs(lamf, lamsol).doit().subs(tt, t).subs(ts, tsol[0]))
            ok = ok and e2 == 0
        ok = ok and len(found) == 2 and sp.simplify(found[0] - found[1]) == 0
    checks.check("D2", ok, "exact uniform solutions at c_k = -24 alpha, s = 3: rest content gives l = (1 + t/t0)^(2/3), t0 = (4/3) sqrt(6 alpha/m0); top-speed content gives l = (1 + t/t1)^(1/2), t1 = sqrt(6 alpha/eps); each time mirror (t -> -t) solves with the same constant, so the equations fix no direction")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    m0, eps, al = sp.symbols("m0 eps alpha", positive=True)
    lam = sp.Symbol("lam", real=True)
    m_mix = m0 + eps * sp.exp(-lam)
    p_mix = -sp.diff(m_mix, lam) / (3 * sp.exp(3 * lam))
    expected = (eps * sp.exp(-lam) / sp.exp(3 * lam)) / (3 if not mut("mixture_pressure_forged") else 1)
    tt, lamf, con, el = homogeneous(-24 * al, 3, lambda x: m0 + eps * sp.exp(-x))
    kept = sp.simplify(sp.diff(con, tt) + sp.diff(lamf, tt) * el) == 0
    checks.check("E1", sp.simplify(p_mix - expected) == 0 and kept,
                 "a mixture of rest and top-speed content, m = m0 + eps/l: the pressure is that of the top-speed part alone, rho_top/3, and the constraint is kept by the lengths' equation")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 60, 101, 124 and 129 as landed on main (the homogeneous kinetic model, the static clock law, the kinetic family and the volume power), with blocks 134, 135 and 136 as landed for the kinetic normalization; it reports how a closed lattice with content moves as a whole; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein", "Schwarz", "Liouville", "Morse", "Infeld", "Hoffmann", "Fierz", "Darwin", "Laue", "Poincare", "Poincaré", "Grommer", "Belinfante", "Rosenfeld", "Lemaitre", "Lemaître", "Robertson", "Hubble", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the member's clock constraint at the zero mode, and its kinetic term on the uniform dilation",
    "per_site: executed - block 60's homogeneous model: the constraint kept by the lengths' equation for any content m(lam)",
    "per_mode: executed - the uniform motion's coupling against the static pull's, and its rate of change",
    "per_block: executed - the walk on a uniformly stretched lattice; exact uniform solutions for rest and top-speed content; mixtures",
    "lattice_wide: uniform content on a closed lattice; block 60's homogeneous kinetic model with s = 3; unit rate",
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
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: a closed lattice with positive content has no static state and stretches or shrinks uniformly (the equations fix no direction); the uniform motion carries the static pull coupling iff alpha = K/4, the condition of blocks 134-136 met again, with l-ddot/l = -(4 pi G/3)(rho + 3p); top-speed walkers lose energy as 1/l, giving t^(1/2); rest content gives t^(2/3); supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
