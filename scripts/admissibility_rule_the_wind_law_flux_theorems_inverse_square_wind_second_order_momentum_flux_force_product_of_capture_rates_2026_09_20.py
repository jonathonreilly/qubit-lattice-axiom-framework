#!/usr/bin/env python3
"""Exact checks: the wind law of the inertial record gas (block 44's clause; supplied, not adopted).

T1: the rate of change of the occupancy of a site is minus the lattice divergence of the current observable
j(x->y) = [record at x pointing to y, y empty] - [record at y pointing to x, x empty]; so in a stationary state the mean current through any closed
surface around a capturing body equals its capture rate.  T2: the rate of change of the momentum at a site is minus the divergence of an explicit
momentum-flux observable (a moving record carries its momentum; an exchange passes e_d forward and e_d' back; scattering passes the mean change
across its bond); so the mean force on a body is the mean momentum flux through any surface enclosing it.  T3: with block 44's product-state
current, a body capturing Q per tick has the wind g = sqrt3 Q/(4 pi r^2 (1 - rho)) (sphere menu; spherical symmetry and local equilibrium
assumed), and through a cube surface of half-side R the mean current over the 6 (2R+1)^2 crossing bonds sums to Q exactly.  T4: for the sphere
menu the tilted one-site state has <s_i s_j> = delta_ij/3 + l_i l_j/15 - delta_ij l^2/45 to second order (from the uniform moments 1/3, 1/5, 1/15),
hence sqrt3 Pi_ij = (rho/3) delta_ij + A g_i g_j + B g^2 delta_ij with A = (3/5 - rho)/rho, B = -1/(5 rho); for the six-axis menu <s_i s_j> is
diagonal, while the full flux includes the exchange term -g_i g_j.  T5: from the second-order flux alone (the inviscid value) the force of a uniform wind g1 on a body drawing the inflow q is A q g1/sqrt(3) (the pressure
adjusts by the second-order momentum balance), that is (3/5 - rho)/(1 - rho) times Q2 g1/rho; it changes sign at rho = 3/5.  The executed flows are
viscous and do not follow it (see the note).
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import ast
import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_WIND_LAW_FLUX_THEOREMS_INVERSE_SQUARE_WIND_OF_A_CAPTURING_BODY_SECOND_ORDER_MOMENTUM_FLUX_FORCE_PROPORTIONAL_TO_PRODUCT_OF_CAPTURE_RATES_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_wind_law_flux_theorems_inverse_square_wind_of_a_capturing_body_second_order_momentum_flux_force_proportional_to_product_of_capture_rates_bounded_theorem_note_2026-09-20"
AXIOM_NEEDLES = ("A site never carries more than one record; records are permanent.",)

MUTATION_GATE = {
    "current_without_blocking": "B",
    "momentum_flux_without_exchange": "B",
    "cube_surface_count_wrong": "C",
    "wind_coefficient_without_blocking_factor": "C",
    "fourth_moment_wrong": "D",
    "advective_coefficient_without_exclusion": "D",
    "bernoulli_adjustment_dropped": "E",
    "sign_change_density_wrong": "E",
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


E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
M6 = range(6)
ZERO = (Fraction(0), Fraction(0), Fraction(0))


def vadd(a, b, s=1):
    return tuple(Fraction(a[i]) + s * Fraction(b[i]) for i in range(3))


def vscale(a, k):
    return tuple(Fraction(a[i]) * k for i in range(3))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentence used")


# ============================================================================================ family B (T1, T2)
def family_b(checks: Checks) -> None:
    L, n, gamma = 3, 2, Fraction(1)
    sites = list(product(range(L), repeat=3))
    add = lambda x, d: tuple((x[i] + E[d][i]) % L for i in range(3))
    ok_mass, ok_mom, count = True, True, 0
    for occ in combinations(sites, n):
        for contents in product(M6, repeat=n):
            cfg = dict(zip(occ, contents))
            count += 1
            # brute force: the generator applied to n_x and to the momentum at x
            dn = {}
            dp = {}
            for x, d in cfg.items():
                y = add(x, d)
                if y not in cfg:
                    dn[x] = dn.get(x, 0) - 1
                    dn[y] = dn.get(y, 0) + 1
                    dp[x] = vadd(dp.get(x, ZERO), E[d], -1)
                    dp[y] = vadd(dp.get(y, ZERO), E[d])
                else:
                    d2 = cfg[y]
                    diff = vadd(E[d], E[d2], -1)
                    dp[x] = vadd(dp.get(x, ZERO), diff, -1)
                    dp[y] = vadd(dp.get(y, ZERO), diff)
            for x in cfg:
                for k in (0, 2, 4):
                    y = add(x, k)
                    if y in cfg:
                        a, b = cfg[x], cfg[y]
                        loss = vscale(E[a], gamma) if b == a ^ 1 else vscale(vadd(E[a], E[b], -1), gamma / 2)
                        dp[x] = vadd(dp.get(x, ZERO), loss, -1)
                        dp[y] = vadd(dp.get(y, ZERO), loss)
            # the observables: for each site x and each neighbour y = x + e_k, the net current and the net momentum flux from x to y
            div_j = {}
            div_pi = {}
            for x in sites:
                for k in M6:
                    y = add(x, k)
                    jxy = 0
                    flux = ZERO
                    if x in cfg and cfg[x] == k:                                  # the record at x points to y
                        if y not in cfg or mut("current_without_blocking"):
                            jxy += 1
                        if y not in cfg:
                            flux = vadd(flux, E[k])
                        elif not mut("momentum_flux_without_exchange"):
                            flux = vadd(flux, vadd(E[k], E[cfg[y]], -1))
                    if y in cfg and cfg[y] == k ^ 1:                              # the record at y points to x
                        if x not in cfg or mut("current_without_blocking"):
                            jxy -= 1
                        if x not in cfg:
                            flux = vadd(flux, E[k ^ 1], -1)
                        elif not mut("momentum_flux_without_exchange"):
                            flux = vadd(flux, vadd(E[k ^ 1], E[cfg[x]], -1), -1)
                    if x in cfg and y in cfg:                                     # scattering on the bond: the mean momentum passed from x to y
                        a, b = cfg[x], cfg[y]
                        flux = vadd(flux, vscale(E[a], gamma) if b == a ^ 1 else vscale(vadd(E[a], E[b], -1), gamma / 2))
                    div_j[x] = div_j.get(x, 0) + jxy
                    div_pi[x] = vadd(div_pi.get(x, ZERO), flux)
            for x in sites:
                ok_mass = ok_mass and dn.get(x, 0) == -div_j.get(x, 0)
                ok_mom = ok_mom and dp.get(x, ZERO) == vscale(div_pi.get(x, ZERO), -1)
    checks.check("B1", ok_mass, f"T1: at every site of every one of the {count} two-record configurations of the 3^3 torus the rate of change of the occupancy is minus the divergence of the current j(x->y) = [record at x pointing to y, y empty] - [the reverse]: records are conserved locally, so a stationary flow carries the capture rate of a body through every surface around it")
    checks.check("B2", ok_mom, "T2: at every site of every configuration the rate of change of the momentum is minus the divergence of the momentum flux (a moving record carries e_d; an exchange passes e_d forward and e_d' back; scattering passes the mean change across its bond): the mean force on a body is the momentum flux through any surface enclosing it")


# ============================================================================================ family C (T3)
def family_c(checks: Checks) -> None:
    ok = True
    for big_r in (1, 2, 3, 5):
        inside = set(product(range(-big_r, big_r + 1), repeat=3))
        crossing = sum(1 for x in inside for k in M6 if tuple(x[i] + E[k][i] for i in range(3)) not in inside)
        want = 6 * (2 * big_r + 1) ** 2 + (1 if mut("cube_surface_count_wrong") else 0)
        ok = ok and crossing == want
    checks.check("C1", ok, "T3: the surface of a cube of half-side R is crossed by 6 (2R+1)^2 bonds (R = 1, 2, 3, 5); by T1 the mean current over them sums to the capture rate, an inverse-square law for the mean current")
    rho, q = Fraction(29, 100), Fraction(78, 10)
    block = 1 if mut("wind_coefficient_without_blocking_factor") else (1 - rho)
    coef_sq = 3 * q * q / (16 * block * block)                 # (sqrt3 Q/(4 (1 - rho)))^2, to be divided by pi^2 r^4
    checks.check("C2", coef_sq == 3 * q * q / (16 * (1 - rho) ** 2) and Fraction(3) * (1 - rho) ** 2 * coef_sq * 16 == 9 * q * q, "T3: with the product-state current J = (1 - rho) g/sqrt 3 of block 44 a spherically symmetric inflow of Q per tick has the momentum density g = sqrt3 Q/(4 pi r^2 (1 - rho)): the square of its coefficient is 3 Q^2/(16 (1 - rho)^2) over pi^2 r^4 (checked at Q = 78/10, rho = 29/100)")


# ============================================================================================ family D (T4)
def sphere_moment(a, b, c):
    """<s_x^a s_y^b s_z^c> over the uniform sphere: zero unless all even, else (a-1)!!(b-1)!!(c-1)!!/(a+b+c+1)!!"""
    if a % 2 or b % 2 or c % 2:
        return Fraction(0)
    df = lambda m: 1 if m <= 0 else m * df(m - 2)
    return Fraction(df(a - 1) * df(b - 1) * df(c - 1), df(a + b + c + 1))


def family_d(checks: Checks) -> None:
    m4 = Fraction(1, 4) if mut("fourth_moment_wrong") else sphere_moment(0, 0, 4)
    ok = sphere_moment(0, 0, 2) == Fraction(1, 3) and m4 == Fraction(1, 5) and sphere_moment(2, 0, 2) == Fraction(1, 15)
    rng = random.Random(4)
    for _ in range(20):
        lam = [Fraction(rng.randint(-5, 5), 7) for _ in range(3)]
        l2 = sum(v * v for v in lam)
        for i in range(3):
            for j in range(3):
                # second-order cumulant expansion: <s_i s_j>_l = <s_i s_j> + (1/2) l_k l_m (<s_i s_j s_k s_m> - <s_i s_j><s_k s_m>)
                tot = Fraction(0)
                for k in range(3):
                    for m in range(3):
                        e4 = [0, 0, 0]
                        for t in (i, j, k, m):
                            e4[t] += 1
                        four = m4 if max(e4) == 4 else sphere_moment(*e4)
                        tot += lam[k] * lam[m] * (four - (Fraction(1, 3) if i == j else 0) * (Fraction(1, 3) if k == m else 0))
                want = lam[i] * lam[j] / 15 - (l2 / 45 if i == j else 0)
                ok = ok and tot / 2 == want
    for rho in (Fraction(29, 100), Fraction(1, 2), Fraction(3, 4)):
        # sqrt3 Pi_ij = rho <s_i s_j> - rho^2 <s_i><s_j>, with g = rho l/3
        a_coef = (rho * Fraction(1, 15) - (0 if mut("advective_coefficient_without_exclusion") else rho ** 2 * Fraction(1, 9))) * 9 / rho ** 2
        b_coef = -rho * Fraction(1, 45) * 9 / rho ** 2
        ok = ok and a_coef == (Fraction(3, 5) - rho) / rho and b_coef == -1 / (5 * rho)
    checks.check("D1", ok, "T4: the uniform sphere has <s_z^2> = 1/3, <s_z^4> = 1/5, <s_x^2 s_z^2> = 1/15; the tilted state has <s_i s_j> = delta_ij/3 + l_i l_j/15 - delta_ij l^2/45 to second order (20 rational tilts); hence sqrt3 Pi_ij = (rho/3) delta_ij + A g_i g_j + B g^2 delta_ij with A = (3/5 - rho)/rho and B = -1/(5 rho)")
    # six axes: <s_1^2> = 2 cosh l1/(2 sum cosh) -> 1/3 + l1^2/9 - (l2^2 + l3^2)/18, and <s_1 s_2> = 0 identically
    ok6 = True
    for _ in range(10):
        l = [Fraction(rng.randint(-4, 4), 9) for _ in range(3)]
        second = (2 + l[0] ** 2) * Fraction(1, 6) - Fraction(1, 3) * sum(v * v for v in l) * Fraction(1, 6)     # (2 + l1^2)/(6 + l^2) to second order
        ok6 = ok6 and second == Fraction(1, 3) + l[0] ** 2 / 9 - (l[1] ** 2 + l[2] ** 2) / 18
    ok6 = ok6 and all(E[d][0] * E[d][1] == 0 for d in M6)
    # Enumerate all oriented streaming events in an anisotropic product state.
    dens=[Fraction(v,60) for v in (8,2,7,3,4,6)]
    rho=sum(dens);g=[sum(dens[d]*E[d][i] for d in M6) for i in range(3)]
    flux=[[Fraction(0) for _ in range(3)] for _ in range(3)]
    for d in M6:
        for i in range(3):
            for j in range(3):
                flux[i][j]+=dens[d]*(1-rho)*E[d][i]*E[d][j]
                flux[i][j]+=sum(dens[d]*dens[b]*(E[d][i]-E[b][i])*E[d][j] for b in M6)
    ok6=ok6 and all(flux[i][j]==sum(dens[d]*E[d][i]*E[d][j] for d in M6)-g[i]*g[j] for i in range(3) for j in range(3))
    ok6=ok6 and flux[0][1]!=0
    checks.check("D2", ok6, "T4: for the six-axis menu <s_1^2> = 1/3 + l_1^2/9 - (l_2^2 + l_3^2)/18 to second order and <s_1 s_2> vanishes identically: the full six-axis flux has the off-diagonal exchange term -g_1 g_2 and is not isotropic at second order")


# ============================================================================================ family E (T5)
def family_e(checks: Checks) -> None:
    nn = [[sphere_moment(*[(i == t) + (j == t) for t in range(3)]) for j in range(3)] for i in range(3)]
    ok = all(nn[i][j] == (Fraction(1, 3) if i == j else 0) for i in range(3) for j in range(3))
    shown = []
    for rho in (Fraction(29, 100), Fraction(1, 2), Fraction(3, 5), Fraction(3, 4)):
        a = (Fraction(3, 5) - rho) / rho
        b_eff = -1 / (5 * rho) if mut("bernoulli_adjustment_dropped") else -a / 2
        # sqrt(3) F/(q g1): the inflow -q n/(4 pi R^2) crossed with the uniform wind g1, integrated over the sphere:
        #   A g1 (g2.n) -> A q g1 ;  A g2 (g1.n) -> A q g1 <n n> = A q g1/3 ;  2 B_eff (g1.g2) n -> 2 B_eff q g1/3
        coef = a * 1 + a * nn[0][0] + 2 * b_eff * nn[0][0]
        ratio = rho * coef / (1 - rho)                           # against the simple estimate Q2 g1/rho, with q = sqrt3 Q2/(1 - rho)
        ok = ok and coef == a and ratio == (Fraction(3, 5) - rho) / (1 - rho)
        shown.append(f"rho {rho}: {ratio}")
    flip = Fraction(1, 2) if mut("sign_change_density_wrong") else Fraction(3, 5)
    ok = ok and (Fraction(3, 5) - flip) / (1 - flip) == 0
    checks.check("E1", ok, "T5: with <n_i n_j> = delta_ij/3 over the sphere and the pressure adjusting by the second-order balance (B_eff = -A/2), the inviscid value of the force of a uniform wind g1 on a body drawing the inflow q is A q g1/sqrt(3), that is (3/5 - rho)/(1 - rho) times the simple estimate Q2 g1/rho: " + "; ".join(shown) + "; it changes sign at rho = 3/5")


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied inertial clause of block 44 and derives what that clause implies for the flow around capturing bodies; neither the clause nor anything here is adopted.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Navier", "Stokes", "Bernoulli", "Bjerknes", "Pearson", "Sage", "Boltzmann", "Gibbs", "Laplace", "Poisson", "Galileo", "Galilei", "Knudsen", "Mach", "Fick", "Brown", "Planck", "Einstein", "Poincare", "Gauss", "Langevin", "Riemann", "Smoluchowski")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Gauss)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    nodes=list(ast.walk(ast.parse(src)))
    float_hits=[x for x in nodes if isinstance(x,ast.Constant) and isinstance(x.value,float)]
    float_hits += [x for x in nodes if isinstance(x,ast.Call) and
        ((isinstance(x.func,ast.Name) and x.func.id in ("float","N")) or
         (isinstance(x.func,ast.Attribute) and x.func.attr in ("evalf","N")))]
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
    "per_element: executed — the uniform sphere's moments 1/3, 1/5, 1/15; the six-axis second moments",
    "per_site: executed — the mass and momentum continuity identities at every site of all 12636 two-record configurations of the 3^3 torus",
    "per_mode: not applicable — the retained finite identities concern local rates and integrated flux, not a mode spectrum",
    "per_block: executed — the tilted second moments on 20 rational tilts; the flux coefficients at three densities; the force coefficient at four densities",
    "lattice_wide: T1 and T2 are identities of the generator on every lattice; T3 is a statement in the local-equilibrium closure with spherical symmetry; T4 is exact for product states; T5 is the inviscid value that follows from T4; the wind profile and the forces between bodies are executed, not proved",
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
    print("scope: the wind law of the inertial record gas — exact continuity of number and momentum, inverse-square mean current around a capturing body, second-order momentum flux with A = (3/5 - rho)/rho, inviscid force (3/5 - rho)/(1 - rho) of the simple estimate with a sign change at rho = 3/5; exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
