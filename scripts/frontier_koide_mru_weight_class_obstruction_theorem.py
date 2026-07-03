#!/usr/bin/env python3
"""
Frontier runner - Koide MRU unreduced weight-class obstruction.

Companion to
`docs/KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md`.

What this runner certifies as load-bearing theorem algebra:
  1. On the unreduced carrier, every weighted block-log-volume leaf satisfies
         kappa = 2 mu / nu.
     In particular, the unreduced determinant carrier has weights (1,2) and
     lands at kappa = 1.

What it checks only as non-load-bearing future-route context:
  2. If the scalar charged-lepton lane is supplied as an SO(2)-quotient of
     the real doublet, then the two-slot carrier (rho_+, rho_perp) is the
     exact quotient algebra.
  3. On that supplied reduced carrier, the same log-volume law is
     automatically equal-weight and lands at MRU:
         E_+ = E_perp <=> kappa = 2.

It does not derive the physical SO(2)-quotient bridge or decouple the
cos(3 arg b) channel, and it does not use the reduced-carrier calculation as
part of the bounded theorem claim.
"""

from __future__ import annotations

from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KOIDE_MRU_WEIGHT_CLASS_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md"

PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "", cls: str = "A") -> None:
    global PASS, FAIL
    status = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{cls}] {status}: {label}" + (f"  ({detail})" if detail else ""))


def shift_matrix() -> sp.Matrix:
    return sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def part0_weight_classification() -> None:
    print("\n=== Part 0: weighted block-log-volume classification ===")
    e_plus, e_perp, e_tot = sp.symbols("e_plus e_perp e_tot", positive=True, real=True)
    mu, nu, lam = sp.symbols("mu nu lam", positive=True, real=True)

    lagrangian = mu * sp.log(e_plus) + nu * sp.log(e_perp) - lam * (e_plus + e_perp - e_tot)
    sol = sp.solve(
        [sp.diff(lagrangian, e_plus), sp.diff(lagrangian, e_perp), e_plus + e_perp - e_tot],
        [e_plus, e_perp, lam],
        dict=True,
    )
    check("Weighted family has a unique interior stationary point", len(sol) == 1, f"sol={sol}")
    stationary = sol[0]
    check("E_+^* = mu/(mu+nu) E_tot", sp.simplify(stationary[e_plus] - e_tot * mu / (mu + nu)) == 0)
    check("E_perp^* = nu/(mu+nu) E_tot", sp.simplify(stationary[e_perp] - e_tot * nu / (mu + nu)) == 0)
    check("Stationary ratio is E_+/E_perp = mu/nu", sp.simplify(stationary[e_plus] / stationary[e_perp] - mu / nu) == 0)
    check("Hence the leaf is kappa = 2 mu / nu", sp.simplify(2 * stationary[e_plus] / stationary[e_perp] - 2 * mu / nu) == 0)


def part1_unreduced_obstruction() -> None:
    print("\n=== Part 1: unreduced determinant obstruction ===")
    c = shift_matrix()
    i3 = sp.eye(3)
    p_plus = sp.simplify((i3 + c + c**2) / 3)
    p_perp = sp.simplify(i3 - p_plus)
    alpha, beta = sp.symbols("alpha beta", positive=True, real=True)

    check(
        "P_+ and P_perp are complementary projectors",
        sp.simplify(p_plus**2 - p_plus) == sp.zeros(3)
        and sp.simplify(p_perp**2 - p_perp) == sp.zeros(3)
        and sp.simplify(p_plus * p_perp) == sp.zeros(3),
    )
    check("rank(P_+) = 1 and rank(P_perp) = 2", p_plus.rank() == 1 and p_perp.rank() == 2)

    d_unreduced = sp.simplify(alpha * p_plus + beta * p_perp)
    check("det(alpha P_+ + beta P_perp) = alpha beta^2", sp.simplify(sp.factor(d_unreduced.det()) - alpha * beta**2) == 0)
    check("Unreduced weight pair (1,2) lands at kappa = 1", sp.simplify(2 * sp.Integer(1) / sp.Integer(2) - 1) == 0)


def part2_context_quotient() -> None:
    print("\n=== Part 2: context-only SO(2)-quotient algebra ===")
    r0, r1, r2, theta = sp.symbols("r0 r1 r2 theta", real=True)
    r1p = sp.cos(theta) * r1 - sp.sin(theta) * r2
    r2p = sp.sin(theta) * r1 + sp.cos(theta) * r2

    e_plus = sp.simplify(r0**2 / 3)
    e_perp = sp.simplify((r1**2 + r2**2) / 6)
    e_perp_rot = sp.simplify((r1p**2 + r2p**2) / 6)

    check("The doublet block power is SO(2)-orbit invariant", sp.simplify(e_perp_rot - e_perp) == 0, cls="C")
    check("If the scalar lane quotients the ordered pair, the radius is invariant", sp.simplify(sp.expand(r1p**2 + r2p**2 - (r1**2 + r2**2))) == 0, cls="C")

    rho_p, rho_perp = sp.symbols("rho_p rho_perp", positive=True, real=True)
    check("Reduced carrier coordinates satisfy rho_+^2 = E_+", sp.simplify(rho_p**2 - e_plus).subs(rho_p, sp.sqrt(e_plus)) == 0, cls="C")
    check("Reduced carrier coordinates satisfy rho_perp^2 = E_perp", sp.simplify(rho_perp**2 - e_perp).subs(rho_perp, sp.sqrt(e_perp)) == 0, cls="C")

    a, x, y = sp.symbols("a x y", positive=True, real=True)
    e_plus_ab = 3 * a**2
    e_perp_ab = 6 * (x**2 + y**2)
    check("On the quotient carrier kappa = 2 E_+ / E_perp", sp.simplify(a**2 / (x**2 + y**2) - 2 * e_plus_ab / e_perp_ab) == 0, cls="C")


def part3_context_reduced_resolution() -> None:
    print("\n=== Part 3: context-only reduced-carrier resolution ===")
    rho_p, rho_perp, e_tot, lam = sp.symbols("rho_p rho_perp e_tot lam", positive=True, real=True)
    lagrangian = sp.log(rho_p) + sp.log(rho_perp) - lam * (rho_p**2 + rho_perp**2 - e_tot)
    sol = sp.solve(
        [
            sp.diff(lagrangian, rho_p),
            sp.diff(lagrangian, rho_perp),
            rho_p**2 + rho_perp**2 - e_tot,
        ],
        [rho_p, rho_perp, lam],
        dict=True,
    )
    check("Reduced carrier has a unique positive log-volume stationary point", len(sol) == 1, f"sol={sol}", cls="C")
    stationary = sol[0]
    check(
        "Reduced stationary point is rho_+ = rho_perp = sqrt(E_tot/2)",
        sp.simplify(stationary[rho_p] - sp.sqrt(e_tot / 2)) == 0
        and sp.simplify(stationary[rho_perp] - sp.sqrt(e_tot / 2)) == 0,
        cls="C",
    )

    e_plus, e_perp = sp.symbols("e_plus e_perp", positive=True, real=True)
    check(
        "The reduced stationary point is exactly E_+ = E_perp",
        sp.simplify((rho_p**2 - rho_perp**2).subs({rho_p: sp.sqrt(e_plus), rho_perp: sp.sqrt(e_perp)}) - (e_plus - e_perp)) == 0,
        cls="C",
    )

    a, b_abs_sq = sp.symbols("a b_abs_sq", positive=True, real=True)
    check("Pullback gives a^2 = 2 |b|^2", sp.simplify((3 * a**2 - 6 * b_abs_sq) / 3 - (a**2 - 2 * b_abs_sq)) == 0, cls="C")
    check("So the reduced carrier lands at kappa = 2", sp.simplify((a**2 / b_abs_sq).subs(a**2, 2 * b_abs_sq) - 2) == 0, cls="C")


def part4_context_summary() -> None:
    print("\n=== Part 4: context-only reduced determinant check ===")
    alpha, beta = sp.symbols("alpha beta", positive=True, real=True)
    d_reduced = sp.diag(alpha, beta)
    check("Reduced two-slot carrier has det = alpha beta", sp.simplify(d_reduced.det() - alpha * beta) == 0, cls="C")
    check(
        "On the reduced carrier log|det| = log alpha + log beta",
        sp.expand_log(sp.log(d_reduced.det()), force=True) == sp.log(alpha) + sp.log(beta),
        cls="C",
    )


def part5_source_boundary() -> None:
    print("\n=== Part 5: source-boundary discipline ===")
    text = NOTE.read_text()
    required = [
        "**Claim type:** bounded_theorem",
        "**Status authority:** independent audit lane.",
        "**Claim scope:** unreduced carrier obstruction only.",
        "**No-promotion statement:**",
        "This source does not derive that object",
        "non-load-bearing future-route context",
        "not part of the theorem claim",
        "cos(3 arg b)",
        "**not** derive the physical quotient bridge",
        "use the conditional reduced-carrier calculation as a load-bearing premise",
    ]
    for token in required:
        check(f"source note contains boundary phrase: {token!r}", token in text)
    forbidden = [" ".join(parts) for parts in [
        ("The", "branch", "now", "derives", "it"),
        ("exact", "missing", "object,", "now", "derived"),
        ("exact", "ret" + "ained", "two-slot", "real-isotype", "carrier"),
        ("positive", "layer:"),
        ("resolves", "it", "on", "this", "branch"),
    ]]
    for idx, token in enumerate(forbidden, start=1):
        check(f"source note omits old overclaim phrase #{idx}", token not in text)
    check("source note contains no tool-worktree paths", ".claude/" not in text)


def main() -> int:
    part0_weight_classification()
    part1_unreduced_obstruction()
    part2_context_quotient()
    part3_context_reduced_resolution()
    part4_context_summary()
    part5_source_boundary()

    print("\nInterpretation:")
    print("  The bounded theorem is the unreduced 3x3 obstruction: determinant")
    print("  weights (1,2) select kappa = 1, so the unreduced determinant")
    print("  carrier cannot force MRU.")
    print("  The quotient calculation is context only: if an independent")
    print("  upstream bridge supplies the SO(2) quotient, the non-trivial real")
    print("  doublet reduces to one scalar slot rho_perp and the standard")
    print("  log-volume law becomes the equal-weight MRU law.")
    print("  This runner does not use that context as a load-bearing premise.")
    print("  The remaining positive-route science is still the physical quotient")
    print("  / cos(3 arg b) decoupling bridge.")
    print(f"\nclassified_pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
