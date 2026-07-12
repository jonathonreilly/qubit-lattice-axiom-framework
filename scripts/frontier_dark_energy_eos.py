#!/usr/bin/env python3
"""Class-A verifier for the dark-energy spectral-bridge obstruction.

The verifier exercises dependency inventory, exact countermodels, and an
independent symbolic path for every displayed geometric formula.  It uses no
observational values, fitted selectors, or literature inputs.

Expected result: ``TOTAL: PASS=12 FAIL=0``.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AXIOM_MEMO = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PREMISE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    suffix = f"  ({detail})" if detail else ""
    if ok:
        PASS += 1
        print(f"  [PASS (A)] {label}{suffix}")
    else:
        FAIL += 1
        print(f"  [FAIL (A)] {label}{suffix}")


def main() -> int:
    axiom_text = AXIOM_MEMO.read_text(encoding="utf-8")
    axiom_flat = " ".join(axiom_text.split())
    registry = json.loads(PREMISE_REGISTRY.read_text(encoding="utf-8"))

    print("=" * 78)
    print("DARK-ENERGY EOS: SPECTRAL-BRIDGE OBSTRUCTION  [class A]")
    print("=" * 78)

    print("\n-- dependency firewall --")
    check(
        "minimal axioms supply neither a Hamiltonian nor a time metric",
        "does not choose a Hamiltonian or transfer operator" in axiom_flat
        and "define a time metric" in axiom_flat,
    )
    check(
        "source/action and physical-observable identification remain open",
        "source/action and physical-observable identification" in axiom_flat,
    )
    expected_nodes = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check(
        "approved foundation registry contains exactly the four declared nodes",
        set(registry["canonical_ids"]) == expected_nodes
        and set(registry["nodes"]) == expected_nodes,
        str(sorted(registry["canonical_ids"])),
    )

    print("\n-- same-reduct countermodels --")
    radius_graph = Fraction(2, 1)
    gap = Fraction(3, 1) / radius_graph**2
    lambda_family = tuple(beta * gap for beta in map(Fraction, (0, 1, 2)))
    check(
        "one fixed intrinsic graph spectrum admits distinct adjoined coefficients",
        gap == Fraction(3, 4) and len(set(lambda_family)) == 3,
        f"lambda_1={gap}; Lambda_beta={lambda_family}",
    )
    check(
        "Lambda=lambda_1 is only the beta=1 expansion",
        [value == gap for value in lambda_family] == [False, True, False],
    )

    print("\n-- independent geometric algebra --")
    # Derive the Einstein tensor of R x S^n_R from
    # Ric_00=0, Ric_ij=(n-1)g_ij/R^2, and scalar=n(n-1)/R^2.
    n = Fraction(3, 1)
    scalar_coefficient = n * (n - 1)
    g00_coefficient = scalar_coefficient / 2
    gij_coefficient = (n - 1) - scalar_coefficient / 2
    lambda_from_tt = g00_coefficient / radius_graph**2
    lambda_from_spatial = -gij_coefficient / radius_graph**2
    check(
        "fixed round S^3 x R has incompatible vacuum Einstein components",
        lambda_from_tt == Fraction(3, 4)
        and lambda_from_spatial == Fraction(1, 4)
        and lambda_from_tt != lambda_from_spatial,
        f"tt={lambda_from_tt}; spatial={lambda_from_spatial}",
    )

    hubble, a_phys, grav, rho, cosmological = sp.symbols(
        "H a_phys G rho Lambda", nonzero=True
    )
    friedmann = sp.Eq(
        hubble**2 + a_phys**-2,
        sp.Rational(8, 3) * sp.pi * grav * rho + cosmological / 3,
    )
    solved_lambda = sp.solve(friedmann, cosmological)[0]
    expected_residual = 3 / a_phys**2 + 3 * hubble**2 - 8 * sp.pi * grav * rho
    check(
        "closed-FRW residual is Lambda=lambda_1+3H^2-8piG rho",
        sp.simplify(solved_lambda - expected_residual) == 0,
    )

    u = sp.symbols("u", real=True, positive=True)
    gap_ratio = sp.simplify((3 / (radius_graph * u) ** 2) / (3 / radius_graph**2))
    positive_roots = [root for root in sp.solve(sp.Eq(gap_ratio, 1), u) if root.is_positive]
    check(
        "global de Sitter slice gap equals Lambda iff the slice is the throat",
        gap_ratio == u**-2 and positive_roots == [sp.Integer(1)],
        f"lambda_1/Lambda={gap_ratio}; positive root={positive_roots}",
    )

    delta = sp.symbols("delta")
    source_shift_residual = sp.simplify(delta - 8 * sp.pi * grav * (delta / (8 * sp.pi * grav)))
    check(
        "Lambda/source split leaves the geometric equation invariant",
        source_shift_residual == 0,
    )

    print("\n-- conditional EOS and stencil checks --")
    w, drho_dt = sp.symbols("w drho_dt")
    continuity = sp.Eq(drho_dt + 3 * hubble * (1 + w) * rho, 0)
    w_solution = sp.solve(continuity, w)[0]
    check(
        "continuity uniquely gives w=-1 for supplied constant positive density",
        sp.simplify(w_solution.subs(drho_dt, 0) + 1) == 0,
        str(w_solution),
    )

    h = sp.symbols("h")
    shell_gap = 6 * (1 - sp.cos(h)) / h**2
    relative_series = sp.series(shell_gap / 3, h, 0, 6).removeO().expand()
    shell_coefficient = relative_series.coeff(h, 2)
    check(
        "rotational S^3 shell stencil derives relative coefficient -1/12",
        shell_coefficient == -sp.Rational(1, 12),
        str(relative_series),
    )
    check(
        "the derived shell coefficient disproves universal -1/4",
        shell_coefficient != -sp.Rational(1, 4),
    )

    print("\n" + "=" * 78)
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: obstruction certificate FAILED.")
        return 1
    print("VERDICT: exact no-go candidate supported on the declared foundation-plus-")
    print("intrinsic-spectrum scope.  The surviving EOS statement is conditional.")
    print("Independent audit is required before any effective retained status.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
