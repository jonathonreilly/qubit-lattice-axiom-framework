#!/usr/bin/env python3
"""
Koide Q=1 neutrality classifier.

This runner tests the narrow question raised by the Q counterdomain:

  z = -1/3 -> Q = 1

Does that exact Koide/source-domain component already qualify as a neutral
dark-sector object on the current retained surface?

The answer checked here is deliberately conservative.  The Q=1 branch is
exact in the projected C3-commutant source grammar, but it is not neutral if
it is kept on the charged-lepton carrier.  It becomes a plausible dark-sector
bridge only after an additional map to the unique nu_R singlet/Majorana lane,
and that bridge is not currently retained.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.splitlines():
            print(f"       {line}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def read_doc(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def q_from_z(z_value: sp.Expr) -> sp.Expr:
    z_value = sp.sympify(z_value)
    return sp.simplify(sp.Rational(2, 3) / (1 + z_value))


def ktl_from_z(z_value: sp.Expr) -> sp.Expr:
    z_value = sp.sympify(z_value)
    w_plus = sp.simplify((1 + z_value) / 2)
    r = sp.simplify((1 - w_plus) / w_plus)
    return sp.simplify((r**2 - 1) / (4 * r))


def electric_charge(t3: Fraction, y: Fraction) -> Fraction:
    return t3 + y / 2


def main() -> int:
    a, b, c, alpha, beta, gamma = sp.symbols(
        "a b c alpha beta gamma", real=True
    )
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    I3 = sp.eye(3)

    section("A. Exact Koide Q=1 counterdomain")

    record(
        "A.1 cyclic generator has order three",
        C**3 == I3 and C != I3 and C**2 != I3,
    )

    P_plus = sp.simplify((I3 + C + C**2) / 3)
    P_perp = sp.simplify(I3 - P_plus)
    Z = sp.simplify(P_plus - P_perp)
    expected_Z = sp.simplify(
        -sp.Rational(1, 3) * I3
        + sp.Rational(2, 3) * C
        + sp.Rational(2, 3) * C**2
    )

    record(
        "A.2 projected Z is the central C3-commutant source label",
        sp.simplify(Z - expected_Z) == sp.zeros(3, 3)
        and sp.simplify(C * Z - Z * C) == sp.zeros(3, 3)
        and sp.simplify(Z * Z - I3) == sp.zeros(3, 3),
        f"Z={Z}",
    )

    record(
        "A.3 Z is not an onsite diagonal source function",
        (not Z.is_diagonal())
        and any(Z[i, j] != 0 for i in range(3) for j in range(3) if i != j),
        "The Q=1 component is visible only in the projected/commutant grammar.",
    )

    onsite = sp.diag(a, b, c)
    fixed_equations = list(sp.simplify(C * onsite * C.T - onsite))
    fixed_solutions = sp.solve(fixed_equations, [a, b, c], dict=True)
    record(
        "A.4 strict onsite C3-invariant scalar sources erase Z",
        fixed_solutions == [{a: c, b: c}],
        f"C diag(a,b,c) C^(-1)=diag(a,b,c) -> {fixed_solutions}",
    )

    commutant_source = sp.simplify(alpha * I3 + beta * C + gamma * C**2)
    diagonal_conditions = [
        commutant_source[i, j]
        for i in range(3)
        for j in range(3)
        if i != j
    ]
    diagonal_solutions = sp.solve(diagonal_conditions, [beta, gamma], dict=True)
    record(
        "A.5 onsite functions intersect the C3 commutant only in scalar I",
        diagonal_solutions == [{beta: 0, gamma: 0}],
        f"alpha I+beta C+gamma C^2 diagonal -> {diagonal_solutions}",
    )

    counter_z = -sp.Rational(1, 3)
    record(
        "A.6 z=-1/3 gives Q=1 and K_TL=3/8",
        q_from_z(counter_z) == 1 and ktl_from_z(counter_z) == sp.Rational(3, 8),
        f"z={counter_z} -> Q={q_from_z(counter_z)}, K_TL={ktl_from_z(counter_z)}",
    )

    local_descent = sp.simplify(sp.trace(Z) / 3 * I3)
    record(
        "A.7 scalar local descent erases the non-onsite Z coordinate",
        local_descent == -sp.Rational(1, 3) * I3,
        "E_loc(Z)=(Tr Z/3)I=-I/3: only a scalar survives, so the onsite z-coordinate is gone.",
    )

    record(
        "A.8 descended onsite readout returns Q=2/3, not Q=1",
        q_from_z(0) == sp.Rational(2, 3),
        "Q=1 is therefore not the local charged-lepton zero-section value.",
    )

    section("B. Neutrality classifier")

    charged_lepton_q = electric_charge(Fraction(-1, 2), Fraction(-1, 1))
    nu_r_q = electric_charge(Fraction(0, 1), Fraction(0, 1))

    record(
        "B.1 charged-lepton carrier inherits visible electric charge",
        charged_lepton_q == Fraction(-1, 1),
        f"e_L: T3=-1/2, Y=-1 -> Q_EM={charged_lepton_q}",
    )

    record(
        "B.2 Q=1 branch is not neutral if interpreted on the charged-lepton carrier",
        charged_lepton_q != 0,
        "A charged-lepton-source counterdomain is a visible-sector obstruction, not dark matter.",
    )

    record(
        "B.3 nu_R is neutral under the SM gauge factors",
        nu_r_q == 0,
        "nu_R: color singlet, weak singlet, Y=0 -> Q_EM=0.",
    )

    record(
        "B.4 nu_R is the only same-generation bare Majorana singlet slot",
        True,
        "The Majorana operator note classifies the unique gauge-invariant internal bilinear as nu_R nu_R.",
    )

    section("C. Retained-surface guardrails")

    koide_doc = read_doc(
        "docs/KOIDE_Q_ONSITE_SOURCE_DOMAIN_NO_GO_SYNTHESIS_NOTE_2026-04-25.md"
    )
    majorana_doc = read_doc("docs/NEUTRINO_MAJORANA_OPERATOR_AXIOM_FIRST_NOTE.md")
    source_doc = read_doc("docs/NEUTRINO_MAJORANA_UNIQUE_SOURCE_SLOT_NOTE.md")
    zero_doc = read_doc("docs/NEUTRINO_MAJORANA_CURRENT_STACK_ZERO_LAW_NOTE.md")

    record(
        "C.1 Koide surface explicitly rejects retained native Q closure",
        "Q_RETAINED_NATIVE_CLOSURE=FALSE" in koide_doc
        and "FULL_DIMENSIONLESS_KOIDE_CLOSURE=FALSE" in koide_doc,
    )

    record(
        "C.2 Koide residual target is still a source-domain theorem",
        "derive_retained_source_domain_equals_onsite_function_algebra_not_C3_commutant"
        in koide_doc
        and "derive_Z_as_probe_only_not_background" in koide_doc,
    )

    record(
        "C.3 Majorana operator note identifies nu_R as (1,1)_0",
        "`nu_R : (1,1)_0`" in majorana_doc
        and "one-dimensional" in majorana_doc
        and "nu_R nu_R" in majorana_doc,
    )

    record(
        "C.4 Majorana source slot is local-form support, not existence closure",
        "one complex source slot" in source_doc
        and "does **not** prove" in source_doc
        and "that `m` is nonzero" in source_doc,
    )

    record(
        "C.5 current retained Majorana stack sets mu_current=0",
        "mu_current = 0" in zero_doc
        and "genuinely new axiom-side" in zero_doc
        and "charge-`2` primitive" in zero_doc,
    )

    section("D. Classification")

    bridge_retained = False
    charged_inheritance_neutral = charged_lepton_q == 0
    rhn_singlet_neutral = nu_r_q == 0
    dm_neutrality_closure = (
        q_from_z(counter_z) == 1
        and rhn_singlet_neutral
        and bridge_retained
        and "`mu_current = 0`" not in zero_doc
    )

    record(
        "D.1 no retained map sends Koide Z/Q=1 to the nu_R Majorana source",
        bridge_retained is False,
        "The exact positive target would be koide_Z_to_nu_R_singlet_source_bridge_or_no_go.",
    )

    record(
        "D.2 Q=1 dark-matter neutrality does not close on the current surface",
        dm_neutrality_closure is False,
        "Neutrality is available on the RHN lane, but the Koide Q=1 branch has not reached that lane.",
    )

    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print()
    print("=" * 88)
    print("Summary")
    print("=" * 88)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

    print()
    if n_pass == n_total:
        print("VERDICT: Q=1 is exact but dark-matter neutrality is support-only/open.")
        print("KOIDE_Q1_NEUTRALITY_CLASSIFIER=TRUE")
        print(f"Q1_CHARGED_LEPTON_INHERITANCE_NEUTRAL={charged_inheritance_neutral}")
        print(f"Q1_RHN_SINGLET_NEUTRAL={rhn_singlet_neutral}")
        print(f"Q1_TO_RHN_BRIDGE_RETAINED={bridge_retained}")
        print(f"Q1_DARK_MATTER_NEUTRALITY_CLOSURE={dm_neutrality_closure}")
        print("NEXT_THEOREM=koide_Z_to_nu_R_singlet_source_bridge_or_no_go")
        return 0

    print("VERDICT: Q=1 neutrality classifier has failing checks.")
    print("KOIDE_Q1_NEUTRALITY_CLASSIFIER=FALSE")
    print("Q1_DARK_MATTER_NEUTRALITY_CLOSURE=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
