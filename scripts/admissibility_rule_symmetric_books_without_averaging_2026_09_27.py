#!/usr/bin/env python3
"""Exact checks: symmetric books without averaging. For block 54's walk, the plain site energy e = Re psi^dag H psi, the unaveraged
two-step momentum density P^s and the symmetric stress K^s (block 179) obey, for every state and as matrix-symbol identities,
de/dt + div P^s = 0 and dP^s/dt + div K^s = 0, with the energy current equal to the momentum density and K^s symmetric; hence
d^2 e/dt^2 = sum_aj dbar_a dbar_j K^s_aj exactly. So the plain site energy meets block 135's member identity with the stress K^s, and
the member admits the content iff alpha = K/4, without block 135's body-diagonal average or block 120's transverse average (the
supervisor's own derivation, unrefereed). Blocks 69, 135, 136 as landed; block 179 (pushed) placed.

A (premises): landed blocks 69, 135, 136; the axioms.
B (T1): energy continuity: sum_j (1 - e^{-iq_j}) P^s_j = i(e h(k) - h(k') e), e = (h(k) + h(k'))/2, the symbol of Re psi^dag H psi.
C (T2): momentum continuity with the symmetric stress K^s (block 179); P^s sums to block 69's S_j C_j.
D (T3): the double divergence: sum_aj w_a w_j K^s_aj = -(h'^2 e - 2 h' e h + e h^2), the symbol of d^2 e/dt^2; on eigen-coins -(E - E')^2 e.
E (T4): block 135 T4's demand with e_u = e and Theta = K^s holds for every state iff K/(4 alpha) = 1.
Exact (sympy). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_SYMMETRIC_BOOKS_WITHOUT_AVERAGING_THE_PLAIN_SITE_ENERGY_MEETS_THE_MEMBERS_IDENTITY_EXACTLY_WITH_A_SYMMETRIC_TWO_STEP_STRESS_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_THE_TWO_STEP_CONTENT_MEETS_THE_MEMBERS_IDENTITY_FOR_EVERY_STATE_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_symmetric_books_without_averaging_the_plain_site_energy_meets_the_members_identity_exactly_with_a_symmetric_two_step_stress_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "Set P_j=S_j C_j=(T_j^2-T_j^-2)/(4i)",
)
LANDED135 = (
    "So the site energy misses by the one factor `Π_l cos q_l`, which is the symbol of `C₁C₂C₃`, and `ë′ = −p·Θ·p` exactly.",
    "- (a) At `β = −α` the member demands `ë_u = −(Kw̄²/(4α)) p·Θ·p` of the energy `e_u` that sources its clock. This is block 134 T1, re-derived with `R₂` and the full stress.",
    "- (b) Block 120's realisation without its transverse average, `φ_j = ½(1 + T_j⁻¹)`, meets neither `e` nor `e′`.",
    "  - The site energy is `e(x) = Re ψ†(x)(Hψ)(x)` (blocks 55–56).",
)
LANDED136 = (
    "The site energy, the unaveraged and one-step momenta, and block 62's site stress also fail.",
    "  - The carried momentum is `P″_j = φ_jᵀπ_j`, with `φ_jᵀ = ½(1 + T_j)Π_{l≠j}C_l` (block 120's average). It lives on the bond `x → x + e_j`.",
    "  - `Q_j = C₁C₂C₃ Q^b_j` is the coin-energy current, where `Q^b_j = ½Re[ψ†(x+e_j)σ_j(Hψ)(x) + (Hψ)†(x+e_j)σ_jψ(x)]` on the bond.",
    "  - `Θ_ij = φ_jᵀK_i^j` is block 120's stress, read as the source block 135 uses, and `Θ^sym = (Θ + Θᵀ)/2` is its symmetric part.",
    "  - `Ṗ_z = −pΘ_zz` and `Ṗ_x = −pΘ_xz`, with the symmetric stress;",
    "  - `ė_u = (Kw̄²/(4α)) pP_z`.",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "energy_forged": "B",
    "momentum_forged": "C",
    "double_forged": "D",
    "member_forged": "E",
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
I = sp.I
R = sp.Rational
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
Z = sp.symbols("z1:4")   # e^{ik_a}
W = sp.symbols("w1:4")   # e^{ik'_a}


def sn(x):
    return (x - 1 / x) / (2 * I)


def cs(x):
    return (x + 1 / x) / 2


def hmat(zz):
    return sum((sn(zz[a]) * SIG[a] for a in range(3)), sp.zeros(2))


def symbols_of(zk, zkp, forge=False):
    A = [R(1, 4) * (zk[a] + 1 / zkp[a]) * SIG[a] for a in range(3)]
    f = [R(1, 2) * (1 + zk[a] / zkp[a]) * sn(zk[a] * zkp[a]) for a in range(3)]
    h, hp = hmat(zk), hmat(zkp)
    half = R(1, 3) if (forge and mut("momentum_forged")) else R(1, 2)
    Ks = [[R(1, 2) * (A[a] * f[j] + A[j] * f[a]) for j in range(3)] for a in range(3)]
    Ps = [R(1, 2) * (half * f[j] * sp.eye(2) + hp * A[j] + A[j] * h) for j in range(3)]
    e = R(1, 2) * (h + hp)
    return dict(A=A, f=f, h=h, hp=hp, Ks=Ks, Ps=Ps, e=e)


def zfrom(s_, c_):
    return c_ + I * s_




# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69, t135, t136 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its densities and the member are supplied)")
    needles = list(LANDED135)
    if mut("landed_quote_forged"):
        needles[1] = "- (a) At `β = −α` the member demands `ë_u = −(Kw̄²/(2α)) p·Θ·p` of the energy `e_u` that sources its clock. This is block 134 T1, re-derived with `R₂` and the full stress."
    checks.check("A3", all(n in t69 for n in LANDED69) and all(n in t135 for n in needles) and all(n in t136 for n in LANDED136), "landed blocks 69 (the two-step momentum), 135 (the site energy misses by prod cos q_l; the member's demand; the unaveraged realisation fails) and 136 (the unaveraged momenta fail with its stress; T4(b)'s conditions for keeping every constraint)")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    S = symbols_of(Z, W)
    w = [1 - W[a] / Z[a] for a in range(3)]
    e = S["e"] if not mut("energy_forged") else S["h"]
    lhs = sum((w[j] * S["Ps"][j] for j in range(3)), sp.zeros(2))
    ok = sp.simplify(sp.expand(lhs - I * (e * S["h"] - S["hp"] * e))) == sp.zeros(2)
    checks.check("B1", ok, "energy continuity as matrix symbols for every coin: sum_j (1 - e^{-iq_j}) P^s_j = i(e h(k) - h(k') e) with e = (h(k) + h(k'))/2, the pair symbol of the site energy Re psi^dag H psi: the energy current is the momentum density P^s")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    S = symbols_of(Z, W, forge=True)
    w = [1 - W[a] / Z[a] for a in range(3)]
    ok = all(sp.simplify(sp.expand(sum((w[a] * S["Ks"][a][j] for a in range(3)), sp.zeros(2)) - I * (S["Ps"][j] * S["h"] - S["hp"] * S["Ps"][j]))) == sp.zeros(2) for j in range(3))
    sym = all(sp.simplify(S["Ks"][a][j] - S["Ks"][j][a]) == sp.zeros(2) for a in range(3) for j in range(3))
    sub0 = {W[i]: Z[i] for i in range(3)}
    tot = all(sp.simplify(S["Ps"][j].subs(sub0) - sn(Z[j]) * cs(Z[j]) * sp.eye(2)) == sp.zeros(2) for j in range(3))
    # block 136's objects from their landed definitions are exactly the body-diagonal averages of these
    w_ = [1 - W[a] / Z[a] for a in range(3)]
    cq = [cs(Z[l] / W[l]) for l in range(3)]
    C123 = cq[0] * cq[1] * cq[2]
    P2 = [sn(Z[j]) * cs(Z[j]) + sn(W[j]) * cs(W[j]) for j in range(3)]
    phi = [R(1, 2) * (1 + Z[j] / W[j]) * sp.Mul(*[cq[l] for l in range(3) if l != j]) for j in range(3)]
    Ppp = [phi[j] * R(1, 2) * P2[j] * sp.eye(2) for j in range(3)]
    Qb = [R(1, 4) * (Z[j] + 1 / W[j]) * (SIG[j] * S["h"] + S["hp"] * SIG[j]) for j in range(3)]
    PB = [(Ppp[j] + C123 * Qb[j]) / 2 for j in range(3)]
    Th = [[phi[j] * S["A"][i] * P2[j] for j in range(3)] for i in range(3)]
    avg_ok = all(sp.simplify(sp.expand(PB[j] - C123 * S["Ps"][j])) == sp.zeros(2) for j in range(3))
    avg_ok = avg_ok and all(sp.simplify(sp.expand((Th[i][j] + Th[j][i]) / 2 - C123 * S["Ks"][i][j])) == sp.zeros(2) for i in range(3) for j in range(3))
    checks.check("C2", avg_ok, "from block 136's landed definitions: P^B = (P'' + Q)/2 = C1C2C3 P^s and Theta^sym = C1C2C3 K^s exactly (and e' = C1C2C3 e by definition): block 136's books are the body-diagonal average of these")
    checks.check("C1", ok and sym and tot, "momentum continuity dP^s/dt + div K^s = 0 as matrix symbols (block 179); K^s symmetric; P^s sums to block 69's two-step momentum S_j C_j")


# ============================================================================================ family D (T3)
def family_d(checks: Checks):
    S = symbols_of(Z, W)
    w = [1 - W[a] / Z[a] for a in range(3)]
    dd = sum((w[a] * w[j] * S["Ks"][a][j] for a in range(3) for j in range(3)), sp.zeros(2))
    h, hp, e = S["h"], S["hp"], S["e"]
    target = -(hp * hp * e - 2 * hp * e * h + e * h * h)
    if mut("double_forged"):
        target = -(hp * hp * e - hp * e * h + e * h * h)
    ok = sp.simplify(sp.expand(dd - target)) == sp.zeros(2)
    checks.check("D1", ok, "the double divergence sum_aj (1 - e^{-iq_a})(1 - e^{-iq_j}) K^s_aj equals -(h'^2 e - 2 h' e h + e h^2), the symbol of d^2 e/dt^2 = -[H, [H, e]]: d^2 e/dt^2 = sum_aj dbar_a dbar_j K^s_aj for every state")
    # an exact pair of unequal energies: k with sines (3/5, 4/5, 0) (E = 1), k' with sines (0, 0, 3/5) (E' = 3/5)
    zk = [zfrom(R(3, 5), R(4, 5)), zfrom(R(4, 5), R(3, 5)), sp.Integer(1)]
    zkp = [sp.Integer(1), sp.Integer(1), zfrom(R(3, 5), R(4, 5))]
    Sk = symbols_of(zk, zkp)
    s = [sn(t) for t in zk]
    s2 = [sn(t) for t in zkp]
    E = sp.sqrt(sum(x ** 2 for x in s))
    Ep = sp.sqrt(sum(x ** 2 for x in s2))
    u = sp.Matrix([E + s[2], s[0] + I * s[1]])
    up = sp.Matrix([Ep + s2[2], s2[0] + I * s2[1]])
    wk = [1 - zkp[a] / zk[a] for a in range(3)]
    ddv = sp.simplify((up.H * sum((wk[a] * wk[j] * Sk["Ks"][a][j] for a in range(3) for j in range(3)), sp.zeros(2)) * u)[0])
    ev = sp.simplify((up.H * Sk["e"] * u)[0])
    checks.check("D2", E == 1 and Ep == R(3, 5) and ddv != 0 and sp.simplify(ddv + (E - Ep) ** 2 * ev) == 0, f"on eigen-coins the identity reads dbar dbar : K^s = -(E - E')^2 e_q; at the pair with energies 1 and 3/5 both sides are {ddv}, non-zero")
    return ddv


# ============================================================================================ family E (T4)
def family_e(checks: Checks, ddv) -> None:
    K, al = sp.symbols("K alpha", positive=True)
    # block 135 T4(a): the member demands ddot e_u = -(K/(4 alpha)) p.Theta.p = (K/(4 alpha)) dbar dbar : Theta; the walk gives ddot e = dbar dbar : K^s
    factor = K / (4 * al) if not mut("member_forged") else K / (2 * al)
    sol = sp.solve(sp.Eq(factor * ddv, ddv), al)
    checks.check("E1", sol == [K / 4], "with e_u = e (the plain site energy) and Theta = K^s, block 135 T4(a)'s demand holds for every state iff alpha = K/4 (the double divergence is non-zero on the pair above, so the ratio is forced); no body-diagonal average and no transverse average")
    # block 136 T4(b): every constraint is kept iff (i) P conserved with the symmetric stress and (ii) de_u/dt = (K/(4 alpha)) p.P;
    # with e_u = e, P = P^s, Theta = K^s: (i) is T2 and (ii) reads -div P^s = (K/(4 alpha))(-div P^s), non-zero on the pair of D2
    zk = [zfrom(R(3, 5), R(4, 5)), zfrom(R(4, 5), R(3, 5)), sp.Integer(1)]
    zkp = [sp.Integer(1), sp.Integer(1), zfrom(R(3, 5), R(4, 5))]
    Sk = symbols_of(zk, zkp)
    s_ = [sn(t) for t in zk]
    s2 = [sn(t) for t in zkp]
    E = sp.sqrt(sum(x ** 2 for x in s_))
    Ep = sp.sqrt(sum(x ** 2 for x in s2))
    u = sp.Matrix([E + s_[2], s_[0] + I * s_[1]])
    up = sp.Matrix([Ep + s2[2], s2[0] + I * s2[1]])
    wk = [1 - zkp[a] / zk[a] for a in range(3)]
    divP = sp.simplify((up.H * sum((wk[j] * Sk["Ps"][j] for j in range(3)), sp.zeros(2)) * u)[0])
    sol2 = sp.solve(sp.Eq(factor * divP, divP), al)
    checks.check("E2", divP != 0 and sol2 == [K / 4], f"block 136 T4(b)'s conditions with e_u = e, P = P^s, Theta = K^s: momentum is conserved with the symmetric stress (T2), and de/dt = -div P^s equals (K/(4 alpha))(-div P^s) for every state iff alpha = K/4 (div P^s = {divP} at the pair of D2): every nonzero-mode constraint is kept without averages")


# ============================================================================================ family F
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
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at alpha = K/4."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Cartan", "Hayashi", "Shirafuji", "Wilson", "Belinfante", "Rosenfeld", "Ivanenko", "Kibble", "Sciama", "Hehl", "Laurent", "Gordon")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Belinfante) —", 1)
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
    "per_element: executed - energy and momentum continuity as matrix symbols for every coin; the symmetry of K^s",
    "per_site: executed - the double-divergence identity as a matrix symbol",
    "per_mode: executed - an exact pair of unequal energies: both sides of the identity, non-zero",
    "per_block: executed - block 135 T4's demand and block 136 T4(b)'s conditions with the plain site energy, P^s and K^s: alpha = K/4",
    "lattice_wide: checked and not executed - every state (operator identities from symbol identities); the member's full field equations beyond the longitudinal identity; rates, records",
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
    ddv = family_d(checks)
    family_e(checks, ddv)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: the plain site energy, the unaveraged two-step momentum P^s and the symmetric stress K^s are exactly conserved with energy current = momentum density; d^2 e/dt^2 = dbar dbar : K^s for every state; block 135's member identity holds with them iff alpha = K/4, without averages; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
