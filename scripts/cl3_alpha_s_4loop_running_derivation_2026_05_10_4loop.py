#!/usr/bin/env python3
"""Exact consumer-boundary certificate for the four-order running account.

This runner consumes the formal coefficient/vector-field certificate and
checks that physical QFT inputs remain explicit.  It proves no physical beta
function, scheme theorem, threshold rule, running value, or no-go.
"""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs/ALPHA_S_4LOOP_RUNNING_DERIVATION_PARTIAL_NOTE_2026-05-10_4loop.md"
TARGET_NOTE = ROOT / "docs/ALPHA_S_UNIVERSAL_TWO_LOOP_BETA_KERNEL_THEOREM_NOTE_2026-06-18.md"
TARGET_RUNNER = ROOT / "scripts/frontier_alpha_s_universal_beta_kernel_2026_06_18.py"

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class OrderAccount:
    label: str
    status: str
    formal_outputs: frozenset[str]
    physical_requirements: frozenset[str]


FORMAL_SUPPLIER_OUTPUTS = frozenset(
    {
        "defined_b0_polynomial",
        "defined_b1_polynomial",
        "exact_rational_evaluations",
        "exact_slopes_roots_signs",
        "defined_coordinate_change_identities",
    }
)

COMMON_PHYSICAL_REQUIREMENTS = frozenset(
    {
        "qft_coefficient_origin",
        "physical_colour_carrier",
        "physical_coupling_identification",
        "physical_nf_interpretation",
        "scale_dependent_nf_selector",
        "physical_scale_variable",
    }
)

ACCOUNTS = (
    OrderAccount(
        "L1_b0",
        "formal_defined_template_only",
        frozenset({"defined_b0_polynomial", "defined_coordinate_change_identities"}),
        COMMON_PHYSICAL_REQUIREMENTS | {"one_loop_qft_calculation"},
    ),
    OrderAccount(
        "L2_b1",
        "formal_defined_template_only",
        frozenset({"defined_b1_polynomial", "defined_coordinate_change_identities"}),
        COMMON_PHYSICAL_REQUIREMENTS
        | {"two_loop_qft_calculation", "scheme_independence_theorem"},
    ),
    OrderAccount(
        "L3_b2",
        "physical_coefficient_import_open",
        frozenset(),
        COMMON_PHYSICAL_REQUIREMENTS
        | {"three_loop_qft_calculation", "renormalization_scheme"},
    ),
    OrderAccount(
        "L4_b3",
        "physical_coefficient_import_open",
        frozenset(),
        COMMON_PHYSICAL_REQUIREMENTS
        | {"four_loop_qft_calculation", "renormalization_scheme"},
    ),
)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def load_target_module():
    """Load the exact formal supplier as executable evidence."""
    module_name = "formal_beta_kernel_supplier"
    spec = importlib.util.spec_from_file_location(module_name, TARGET_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load formal supplier at {TARGET_RUNNER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def source_boundary_checks() -> None:
    """Guard the direct link and reject the historical promotion language."""
    note_text = NOTE.read_text(encoding="utf-8")
    target_text = TARGET_NOTE.read_text(encoding="utf-8")
    target_link = "ALPHA_S_UNIVERSAL_TWO_LOOP_BETA_KERNEL_THEOREM_NOTE_2026-06-18.md"
    check("consumer keeps the one-hop formal supplier link", target_link in note_text)
    check("formal supplier is proposed as positive_theorem", "**Claim type:** positive_theorem" in target_text)

    historical_promotions = (
        "L1 (β_0) is retained inline",
        "L2 (β_1) is algebraically retained",
        "beta_0 derivable from {C_F, C_A, T_F, N_f} alone",
        "beta_1 derivable from {C_F, C_A, T_F, N_f} alone",
        "Lane 1 import count: 4 → 3.5",
        "admitted_context_inputs:",
    )
    present = tuple(phrase for phrase in historical_promotions if phrase in note_text)
    check("historical formal-to-physical promotions are absent", len(present) == 0, str(present))

    required_boundaries = (
        "formal_defined_template_only",
        "physical_coefficient_import_open",
        "No global no-go is asserted",
        "no fractional \"import count reduction\"",
    )
    missing = tuple(phrase for phrase in required_boundaries if phrase not in note_text)
    check("repaired source states the exact accounting boundary", len(missing) == 0, str(missing))


def exact_supplier_checks(module) -> None:
    """Consume and independently query the supplier's exact certificate."""
    certificate = module.validate_canonical(module.build_certificate())
    n = sp.symbols("n", real=True)
    print("\n== Exact formal supplier ==")
    check("supplier b0 is the defined affine polynomial", sp.cancel(certificate.b0 - (11 - sp.Rational(2, 3) * n)) == 0)
    check("supplier b1 is the defined affine polynomial", sp.cancel(certificate.b1 - (102 - sp.Rational(38, 3) * n)) == 0)
    check("supplier g-to-alpha identity has zero residual", sp.cancel(certificate.induced_alpha - certificate.expected_alpha) == 0)
    check("supplier alpha-to-a identity has zero residual", sp.cancel(certificate.induced_a - certificate.expected_a) == 0)

    expected_values = {
        ("b0", 6): sp.Rational(7),
        ("b0", 5): sp.Rational(23, 3),
        ("b1", 6): sp.Rational(26),
        ("b1", 5): sp.Rational(116, 3),
    }
    for (name, argument), expected in expected_values.items():
        expression = certificate.b0 if name == "b0" else certificate.b1
        actual = sp.cancel(expression.subs(n, argument))
        check(f"formal {name}({argument}) exact evaluation", actual == expected, str(actual))


def accounting_checks() -> None:
    """Compute which physical inputs remain after consuming the formal row."""
    print("\n== Per-order physical-input accounting ==")
    supplied_physical_fields = FORMAL_SUPPLIER_OUTPUTS & set().union(
        *(account.physical_requirements for account in ACCOUNTS)
    )
    check("formal supplier exports no physical requirement field", len(supplied_physical_fields) == 0, str(sorted(supplied_physical_fields)))

    by_label = {account.label: account for account in ACCOUNTS}
    check("L1 status is formal-defined-template only", by_label["L1_b0"].status == "formal_defined_template_only")
    check("L2 status is formal-defined-template only", by_label["L2_b1"].status == "formal_defined_template_only")
    check("L3 status keeps its physical coefficient import open", by_label["L3_b2"].status == "physical_coefficient_import_open")
    check("L4 status keeps its physical coefficient import open", by_label["L4_b3"].status == "physical_coefficient_import_open")

    for account in ACCOUNTS:
        missing_physical = account.physical_requirements - FORMAL_SUPPLIER_OUTPUTS
        check(
            f"{account.label} retains every named physical requirement",
            missing_physical == account.physical_requirements,
            ",".join(sorted(missing_physical)),
        )
        check(
            f"{account.label} formal outputs do not exceed supplier",
            account.formal_outputs <= FORMAL_SUPPLIER_OUTPUTS,
            ",".join(sorted(account.formal_outputs)),
        )

    promoted_statuses = {
        "retained_inline_companion",
        "bounded_algebraic_pending_color_bridge",
        "physical_coefficient_derived",
    }
    observed_statuses = {account.status for account in ACCOUNTS}
    check("no order is assigned a promoted physical status", observed_statuses.isdisjoint(promoted_statuses), str(sorted(observed_statuses)))


def main() -> int:
    print("FOUR-ORDER FORMAL/PHYSICAL ACCOUNTING CERTIFICATE")
    source_boundary_checks()
    target = load_target_module()
    exact_supplier_checks(target)
    accounting_checks()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: formal identities verified; every physical/QFT input remains explicit.")
        return 0
    print("VERDICT: consumer-boundary certificate FAILED.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
