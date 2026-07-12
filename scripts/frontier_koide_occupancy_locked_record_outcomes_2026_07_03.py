#!/usr/bin/env python3
"""Exact checks for the conditional locked-record statistical-slot bridge.

The runner separates three claims:

* conjugate mixed curvature is localized to the K-real restriction on four
  explicitly enumerated reciprocal real channels;
* the Record sentences permit two component readouts determined by one record
  content, while a one-slot result follows only under a supplied statistical
  rule;
* the honest Gaussian moment gives r=1, and r=1/2 follows only under a supplied
  aggregate per-outcome-cell energy condition, not from a partition ratio.

All PASS/FAIL checks are deterministic symbolic or exact finite checks. No
empirical value, fit, random draw, or floating tolerance is consumed.
"""

from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(num: int, ok: bool, desc: str, detail: str = "") -> None:
    """Record and print one non-literal check."""
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"; {detail}" if detail else ""
    print(f"CHECK {num:02d}: {tag} -- {desc}{suffix}")


def laplacian_in_b(expr: sp.Expr, b: sp.Symbol, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    """Return the Cartesian Laplacian after b=x+i y, with other symbols fixed."""
    substituted = sp.expand(expr.subs(b, x + sp.I * y))
    return sp.simplify(sp.diff(substituted, x, 2) + sp.diff(substituted, y, 2))


def formal_adjoint_on_line(matrix: sp.Matrix, b: sp.Symbol, bbar: sp.Symbol) -> sp.Matrix:
    """Formal transpose-conjugate on the b/bbar polynomial ring."""
    return matrix.T.xreplace({b: bbar, bbar: b})


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    axiom_path = root / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
    axiom_text = axiom_path.read_text(encoding="utf-8")

    quote_lock = "When present, a record locks exactly one admissible local possibility."
    quote_content = "A readout value is determined by record content\nalone."
    check(
        1,
        quote_lock in axiom_text,
        "live Record quote: a present record locks exactly one admissible local possibility",
    )
    check(
        2,
        quote_content in axiom_text,
        "live Record quote: a readout value is determined by record content alone",
    )

    a, b, c, bbar = sp.symbols("a b c bbar")
    x, y = sp.symbols("x y", real=True)
    eye3 = sp.eye(3)

    cycle = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    two_step_path = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    single_edge = sp.Matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
    two_edge_star = sp.Matrix([[0, 1, 1], [0, 0, 0], [0, 0, 0]])

    channels = {
        "cycle": (cycle, a**3 + b**3 + c**3 - 3 * a * b * c, -3 * a),
        "two_step_path": (two_step_path, a**3 - 2 * a * b * c, -2 * a),
        "single_edge": (single_edge, a**3 - a * b * c, -a),
        "two_edge_star": (two_edge_star, a**3 - 2 * a * b * c, -2 * a),
    }

    determinant_differences = {}
    off_line_laplacians = {}
    on_line_mixed_differences = {}
    hermitian_differences = {}
    for name, (channel, expected_det, expected_mixed) in channels.items():
        det_expr = sp.expand((a * eye3 + b * channel + c * channel.T).det())
        determinant_differences[name] = sp.simplify(det_expr - expected_det)
        off_line_laplacians[name] = laplacian_in_b(det_expr, b, x, y)
        on_line_mixed = sp.diff(det_expr.subs(c, bbar), b, bbar)
        on_line_mixed_differences[name] = sp.simplify(on_line_mixed - expected_mixed)
        line_matrix = a * eye3 + b * channel + bbar * channel.T
        hermitian_differences[name] = line_matrix - formal_adjoint_on_line(
            line_matrix, b, bbar
        )

    check(
        3,
        all(value == 0 for value in determinant_differences.values()),
        "four enumerated channel determinants match their exact formulas",
        detail=str(determinant_differences),
    )
    check(
        4,
        all(
            bbar not in sp.expand((a * eye3 + b * channel + c * channel.T).det()).free_symbols
            for channel, _, _ in channels.values()
        ),
        "before restriction, no enumerated determinant contains bbar",
    )
    check(
        5,
        all(value == 0 for value in off_line_laplacians.values()),
        "before restriction, every enumerated determinant is harmonic in (Re b, Im b)",
        detail=str(off_line_laplacians),
    )
    check(
        6,
        all(value == 0 for value in on_line_mixed_differences.values()),
        "on c=bbar, the four mixed derivatives equal -3a, -2a, -a, -2a",
        detail=str(on_line_mixed_differences),
    )
    check(
        7,
        all(value == sp.zeros(3) for value in hermitian_differences.values()),
        "c=bbar is the formal Hermitian/K-real restriction on all four real channels",
    )

    contaminated_det = sp.expand((a * eye3 + b * single_edge + bbar * single_edge.T).det())
    contaminated_mixed = sp.simplify(sp.diff(contaminated_det, b, bbar))
    check(
        8,
        contaminated_mixed == -a,
        "negative control: pre-restriction conjugate contamination has nonzero mixed curvature",
        detail=f"mixed={contaminated_mixed}",
    )

    # Record countermodel. One symbolic record content determines two distinct
    # coordinate readout functions. This satisfies content-determination while
    # refuting any inference from that sentence alone to one readout/slot.
    record_content = (x, y)
    component_readouts = {
        "Re": lambda content: content[0],
        "Im": lambda content: content[1],
    }
    evaluated_readouts = {
        name: readout(record_content) for name, readout in component_readouts.items()
    }
    one_locked_possibility = (record_content,)
    check(
        9,
        len(one_locked_possibility) == 1
        and len(evaluated_readouts) == 2
        and evaluated_readouts == {"Re": x, "Im": y}
        and x != y,
        "Record countermodel: one locked content determines two distinct component readouts",
        detail=f"readouts={evaluated_readouts}",
    )

    # Conditional slot rule, not an axiom consequence.
    required_slots_under_supplied_rule = len(one_locked_possibility)
    outcome_slot_labels = ("outcome:b",)
    component_slot_labels = ("component:Re(b)", "component:Im(b)")
    check(
        10,
        len(outcome_slot_labels) == required_slots_under_supplied_rule,
        "under the supplied one-possibility/one-slot rule, outcome slotting has the required count",
        detail=f"required={required_slots_under_supplied_rule}; outcome={len(outcome_slot_labels)}",
    )
    check(
        11,
        len(component_slot_labels) != required_slots_under_supplied_rule
        and len(component_slot_labels) == len(evaluated_readouts),
        "under that supplied rule, component slotting has a two-versus-one count mismatch",
        detail=f"required={required_slots_under_supplied_rule}; components={len(component_slot_labels)}",
    )

    beta, g = sp.symbols("beta g", positive=True)
    a_s = sp.symbols("a_s", real=True)
    x_s, y_s = sp.symbols("x_s y_s", real=True)
    radial = sp.symbols("radial", positive=True)

    singlet_weight = sp.exp(-3 * beta * a_s**2)
    singlet_partition = sp.integrate(singlet_weight, (a_s, -sp.oo, sp.oo))
    mean_a2 = sp.simplify(
        sp.integrate(a_s**2 * singlet_weight, (a_s, -sp.oo, sp.oo))
        / singlet_partition
    )

    cartesian_weight = sp.exp(-6 * beta * (x_s**2 + y_s**2))
    cartesian_partition = sp.integrate(
        sp.integrate(cartesian_weight, (x_s, -sp.oo, sp.oo)),
        (y_s, -sp.oo, sp.oo),
    )
    mean_b2_cartesian = sp.simplify(
        sp.integrate(
            sp.integrate(
                (x_s**2 + y_s**2) * cartesian_weight,
                (x_s, -sp.oo, sp.oo),
            ),
            (y_s, -sp.oo, sp.oo),
        )
        / cartesian_partition
    )

    polar_weight = sp.exp(-6 * beta * radial**2)
    polar_partition = sp.integrate(
        2 * sp.pi * radial * polar_weight, (radial, 0, sp.oo)
    )
    mean_b2_polar = sp.simplify(
        sp.integrate(
            2 * sp.pi * radial**3 * polar_weight, (radial, 0, sp.oo)
        )
        / polar_partition
    )
    check(
        12,
        sp.simplify(cartesian_partition - polar_partition) == 0
        and sp.simplify(cartesian_partition - sp.pi / (6 * beta)) == 0
        and mean_a2 == mean_b2_cartesian == mean_b2_polar == 1 / (6 * beta)
        and sp.simplify(mean_b2_polar / mean_a2) == 1,
        "same-density Cartesian and polar integrals agree and give the honest moment r=1",
        detail=(
            f"Z_cart={cartesian_partition}; Z_polar={polar_partition}; "
            f"<a^2>={mean_a2}; <|b|^2>={mean_b2_polar}"
        ),
    )

    # Different kernels, reproduced only as support arithmetic.
    real_kernel_partition = sp.integrate(
        sp.integrate(
            sp.exp(-g * (x_s**2 + y_s**2) / 2),
            (x_s, -sp.oo, sp.oo),
        ),
        (y_s, -sp.oo, sp.oo),
    )
    complex_kernel_partition = sp.integrate(
        2 * sp.pi * radial * sp.exp(-g * radial**2),
        (radial, 0, sp.oo),
    )
    check(
        13,
        sp.simplify(real_kernel_partition - 2 * sp.pi / g) == 0
        and sp.simplify(complex_kernel_partition - sp.pi / g) == 0
        and sp.simplify(real_kernel_partition / complex_kernel_partition) == 2,
        "different-kernel support cells give 2pi/g and pi/g; no r map is applied",
        detail=f"Z_real={real_kernel_partition}; Z_complex={complex_kernel_partition}",
    )

    a_v = sp.symbols("a_v", positive=True)
    bmag2, epsilon = sp.symbols("bmag2 epsilon", positive=True)
    energy_singlet = 3 * a_v**2
    energy_doublet = 6 * bmag2

    def endpoint(doublet_count: int) -> tuple[sp.Expr, sp.Expr]:
        solution = sp.solve(
            [
                sp.Eq(energy_singlet, epsilon),
                sp.Eq(energy_doublet, doublet_count * epsilon),
            ],
            [epsilon, bmag2],
            dict=True,
        )[0]
        r_value = sp.simplify(solution[bmag2] / a_v**2)
        q_value = sp.simplify((1 + 2 * r_value) / 3)
        return r_value, q_value

    real_dimension_endpoint = endpoint(2)
    outcome_cell_endpoint = endpoint(1)
    check(
        14,
        real_dimension_endpoint == (sp.Integer(1), sp.Integer(1))
        and outcome_cell_endpoint == (sp.Rational(1, 2), sp.Rational(2, 3)),
        "conditional aggregate laws give n_d=2 -> (r,Q)=(1,1) and n_d=1 -> (1/2,2/3)",
        detail=f"n_d=2:{real_dimension_endpoint}; n_d=1:{outcome_cell_endpoint}",
    )
    wrong_count_endpoint = endpoint(3)
    check(
        15,
        wrong_count_endpoint == (sp.Rational(3, 2), sp.Rational(4, 3))
        and wrong_count_endpoint not in {real_dimension_endpoint, outcome_cell_endpoint},
        "wrong-count discriminator: n_d=3 gives (r,Q)=(3/2,4/3)",
        detail=f"n_d=3:{wrong_count_endpoint}",
    )

    print(
        "SUMMARY files: "
        "docs/KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md; "
        "scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py"
    )
    print(
        "SUMMARY conditional residual: a Record-compatible physical rule mapping "
        "locked possibilities to statistical slots."
    )
    print(
        "SUMMARY repair: the rho-map is withdrawn; same-density moments give r=1; "
        "r=1/2 occurs only under the supplied aggregate outcome-cell condition."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
