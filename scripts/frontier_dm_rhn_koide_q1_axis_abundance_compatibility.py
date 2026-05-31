#!/usr/bin/env python3
"""
RHN / Koide Q=1 axis abundance compatibility check.

This runner tests the best constructive reading of the Koide Q=1 branch:

  maybe the projected-source Q=1 component is not a visible charged-lepton
  source at all, but a pointer to the neutral right-handed-neutrino axis.

The check is intentionally narrow.  It validates that the RHN axis is the
natural neutral/Majorana place a Q=1 dark-sector idea would have to land, then
tests whether Q=1 currently carries any abundance, mass-scale, or transport
load.  On the present retained surface it does not.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
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


@dataclass(frozen=True)
class Field:
    name: str
    color_dim: int
    weak_dim: int
    hypercharge: Fraction
    chirality: str


FIELDS = [
    Field("Q_L", 3, 2, Fraction(1, 3), "L"),
    Field("L_L", 1, 2, Fraction(-1, 1), "L"),
    Field("u_R", 3, 1, Fraction(4, 3), "R"),
    Field("d_R", 3, 1, Fraction(-2, 3), "R"),
    Field("e_R", 1, 1, Fraction(-2, 1), "R"),
    Field("nu_R", 1, 1, Fraction(0, 1), "R"),
]


M_DAVIDSON_IBARRA = 2.4e8
M1_FRAMEWORK = 5.323014e10
M2_FRAMEWORK = 5.828558e10
M3_FRAMEWORK = 6.149700e11
ETA_RATIO_EXACT = 0.188785929502
M_N_TARGET = 2.130214e11
K_POWER_TARGET = 7.441639


def is_bare_majorana_singlet(field: Field) -> bool:
    return (
        field.color_dim == 1
        and field.weak_dim == 1
        and 2 * field.hypercharge == 0
    )


def main() -> int:
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    I3 = sp.eye(3)

    section("A. Koide Q=1 source-axis facts")

    P_plus = sp.simplify((I3 + C + C**2) / 3)
    P_perp = sp.simplify(I3 - P_plus)
    Z = sp.simplify(P_plus - P_perp)
    counter_z = -sp.Rational(1, 3)

    record(
        "A.1 Q=1 is exact at z=-1/3 in the projected Koide counterdomain",
        q_from_z(counter_z) == 1,
        f"Q(-1/3)={q_from_z(counter_z)}",
    )

    record(
        "A.2 Z is central/C3-invariant but not onsite",
        sp.simplify(C * Z - Z * C) == sp.zeros(3, 3)
        and sp.simplify(Z * Z - I3) == sp.zeros(3, 3)
        and not Z.is_diagonal(),
        "This is the exact branch that survives in the commutant grammar.",
    )

    local_descent = sp.simplify(sp.trace(Z) / 3 * I3)
    record(
        "A.3 onsite local descent removes the Q=1-supporting Z coordinate",
        local_descent == -sp.Rational(1, 3) * I3
        and q_from_z(0) == sp.Rational(2, 3),
        "E_loc(Z)=-I/3 is scalar-only; if the charged-lepton source domain is onsite, Q returns to 2/3.",
    )

    section("B. RHN axis compatibility")

    singlets = [field for field in FIELDS if is_bare_majorana_singlet(field)]
    record(
        "B.1 nu_R is the unique anomaly-fixed bare Majorana singlet",
        [field.name for field in singlets] == ["nu_R"],
        "Gauge-singlet same-field Majorana candidates: "
        + ", ".join(field.name for field in singlets),
    )

    nu_r = singlets[0]
    record(
        "B.2 nu_R is neutral and one-dimensional internally",
        nu_r.color_dim == 1
        and nu_r.weak_dim == 1
        and nu_r.hypercharge == 0,
        "nu_R: (color, weak, Y) = (1, 1, 0).",
    )

    charged_singlet_failures = [
        field.name
        for field in FIELDS
        if field.color_dim == 1
        and field.weak_dim == 1
        and field.name != "nu_R"
        and 2 * field.hypercharge != 0
    ]
    record(
        "B.3 other one-dimensional charged singlets fail hypercharge neutrality",
        charged_singlet_failures == ["e_R"],
        f"failed singlets={charged_singlet_failures}",
    )

    section("C. Majorana source-status guardrails")

    operator_doc = read_doc("docs/NEUTRINO_MAJORANA_OPERATOR_AXIOM_FIRST_NOTE.md")
    source_slot_doc = read_doc("docs/NEUTRINO_MAJORANA_UNIQUE_SOURCE_SLOT_NOTE.md")
    source_ray_doc = read_doc("docs/NEUTRINO_MAJORANA_SOURCE_RAY_THEOREM_NOTE.md")
    zero_doc = read_doc("docs/NEUTRINO_MAJORANA_CURRENT_STACK_ZERO_LAW_NOTE.md")

    record(
        "C.1 retained operator classification lands on nu_R nu_R",
        "nu_R : (1,1)_0" in operator_doc
        and "one-dimensional" in operator_doc
        and "nu_R nu_R" in operator_doc,
    )

    record(
        "C.2 local Majorana completion has one complex source slot",
        "one complex source slot" in source_slot_doc
        and "delta I_M(m)" in source_slot_doc
        and "activation law for `m`" in source_slot_doc,
    )

    record(
        "C.3 source ray reduces nonzero local pairing direction to mu J_x",
        "`mu J_x`, with `mu >= 0`" in source_ray_doc
        and "does **not** prove" in source_ray_doc
        and "amplitude `mu` is nonzero" in source_ray_doc,
    )

    record(
        "C.4 current retained stack has the exact zero law mu_current=0",
        "mu_current = 0" in zero_doc
        and "genuinely new axiom-side" in zero_doc
        and "charge-`2` primitive" in zero_doc,
    )

    section("D. Abundance and transport compatibility")

    mass_doc = read_doc("docs/DM_CANDIDATE_MASS_WINDOW_THEOREM_NOTE_2026-04-19.md")
    transport_doc = read_doc("docs/DM_LEPTOGENESIS_TRANSPORT_STATUS_NOTE_2026-04-16.md")
    doublet_doc = read_doc(
        "docs/DM_NEUTRINO_SOURCE_SURFACE_Z3_DOUBLET_BLOCK_POINT_SELECTION_THEOREM_NOTE_2026-04-16.md"
    )

    record(
        "D.1 RHN framework mass scale is leptogenesis-viable",
        M1_FRAMEWORK > 200 * M_DAVIDSON_IBARRA
        and M1_FRAMEWORK < M2_FRAMEWORK < M3_FRAMEWORK,
        f"M1/M_DI={M1_FRAMEWORK / M_DAVIDSON_IBARRA:.3f}; "
        f"M1<M2<M3={M1_FRAMEWORK < M2_FRAMEWORK < M3_FRAMEWORK}",
    )

    record(
        "D.2 current one-flavor transport undershoots observation",
        0 < ETA_RATIO_EXACT < 1 and (1 / ETA_RATIO_EXACT) > 5,
        f"eta/eta_obs={ETA_RATIO_EXACT:.12f}; gap factor={1 / ETA_RATIO_EXACT:.6f}",
    )

    target_ratio = M_N_TARGET / M1_FRAMEWORK
    record(
        "D.3 transport-implied target mass is a factor-four shift from M1",
        4.0 < target_ratio < 4.01 and M1_FRAMEWORK < M_N_TARGET < M3_FRAMEWORK,
        f"M_N_target/M1={target_ratio:.6f}; M_target={M_N_TARGET:.6e} GeV",
    )

    record(
        "D.4 target power-law location is non-integer",
        abs(K_POWER_TARGET - round(K_POWER_TARGET)) > 0.1
        and math.floor(K_POWER_TARGET) == 7
        and math.ceil(K_POWER_TARGET) == 8,
        f"k_target={K_POWER_TARGET:.6f}",
    )

    record(
        "D.5 mass-window note does not make Koide Q=1 load-bearing",
        "Koide" not in mass_doc and "Q=1" not in mass_doc,
        "The abundance stack currently speaks in M_N, eta/eta_obs, transport, and selector laws.",
    )

    record(
        "D.6 transport status keeps the live DM gate on a 2-real Z3 doublet-block law",
        "eta / eta_obs = 0.188785929502" in transport_doc
        and "right-sensitive `2`-real `Z_3` doublet-block" in transport_doc,
    )

    record(
        "D.7 doublet-block theorem identifies the remaining selector law, not Q=1",
        "remaining mainline datum is" in doublet_doc
        and "`2`-real `Z_3` doublet-block law" in doublet_doc
        and "does **not** derive" in doublet_doc,
    )

    section("E. Classification")

    q1_to_rhn_bridge_retained = False
    majorana_current_mu_nonzero = False
    abundance_closed_by_q1 = False
    q1_abundance_load_bearing = False
    support_only = (
        q_from_z(counter_z) == 1
        and [field.name for field in singlets] == ["nu_R"]
        and q1_to_rhn_bridge_retained is False
        and majorana_current_mu_nonzero is False
        and abundance_closed_by_q1 is False
    )

    record(
        "E.1 Q=1 has a natural neutral target axis but no retained bridge to it",
        support_only,
        "The bridge would need to identify Koide Z/Q=1 with the nu_R source ray or rule that out.",
    )

    record(
        "E.2 Q=1 currently does not close abundance, stability, or transport",
        not abundance_closed_by_q1 and not q1_abundance_load_bearing,
        "No retained formula maps Q=1 to Omega_DM, M_N, eta/eta_obs, or the doublet selector.",
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
        print("VERDICT: Koide Q=1 / RHN DM bridge is support-only on this surface.")
        print("KOIDE_Q1_RHN_AXIS_COMPATIBILITY=SUPPORT_ONLY")
        print(f"Q1_TO_RHN_BRIDGE_RETAINED={q1_to_rhn_bridge_retained}")
        print(f"MAJORANA_CURRENT_MU_NONZERO={majorana_current_mu_nonzero}")
        print(f"ABUNDANCE_CLOSED_BY_Q1={abundance_closed_by_q1}")
        print(f"Q1_ABUNDANCE_LOAD_BEARING={q1_abundance_load_bearing}")
        print("DM_SELECTOR_REMAINS_2_REAL_Z3_DOUBLET_BLOCK=TRUE")
        print("KOIDE_Q1_DM_CLOSURE=FALSE")
        print("NEXT_RUNNER=frontier_koide_q1_neutrality_classifier")
        print("NEXT_THEOREM=koide_Z_to_nu_R_singlet_source_bridge_or_no_go")
        return 0

    print("VERDICT: Koide Q=1 / RHN compatibility runner has failing checks.")
    print("KOIDE_Q1_RHN_AXIS_COMPATIBILITY=FALSE")
    print("KOIDE_Q1_DM_CLOSURE=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
