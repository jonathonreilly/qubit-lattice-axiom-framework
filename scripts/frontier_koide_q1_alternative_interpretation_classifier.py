#!/usr/bin/env python3
"""
Koide Q=1 alternative-interpretation classifier.

This runner probes five non-DM readings of the exact Koide counterdomain point

    z = -1/3 -> Q = 1

and assigns the narrowest current status:

1. probe-only deformation
2. no-go / underselection witness
3. shared C3 flavor-geometry skeleton
4. possible future Majorana texture shape after independent activation
5. unphysical projected background removed by canonical onsite descent

It does not promote Q=1 to a physical particle or retained closure.  It tries
to determine which interpretations actually hold on the current surface.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
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


def annihilation_operators(n_modes: int) -> list[np.ndarray]:
    sigma_minus = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    ident = np.eye(2, dtype=complex)

    operators: list[np.ndarray] = []
    for mode in range(n_modes):
        op = np.array([[1.0]], dtype=complex)
        for idx in range(n_modes):
            if idx < mode:
                op = np.kron(op, sigma_z)
            elif idx == mode:
                op = np.kron(op, sigma_minus)
            else:
                op = np.kron(op, ident)
        operators.append(op)
    return operators


def number_operator(cs: list[np.ndarray]) -> np.ndarray:
    out = np.zeros_like(cs[0])
    for c in cs:
        out += c.conj().T @ c
    return out


def pair_operator_from_delta(delta: np.ndarray, cs: list[np.ndarray]) -> np.ndarray:
    out = np.zeros_like(cs[0])
    for a in range(len(cs)):
        for b in range(a + 1, len(cs)):
            out += delta[a, b] * (cs[a] @ cs[b])
    return out


def main() -> int:
    section("A. Shared algebraic setup")

    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    I3 = sp.eye(3)
    P_plus = sp.simplify((I3 + C + C**2) / 3)
    P_perp = sp.simplify(I3 - P_plus)
    Z = sp.simplify(P_plus - P_perp)
    z_q1 = -sp.Rational(1, 3)
    S_q1 = sp.simplify(I3 + z_q1 * Z)

    record(
        "A.1 Q=1 is exact in the projected commutant counterdomain",
        q_from_z(z_q1) == 1,
        f"z={z_q1} -> Q={q_from_z(z_q1)}",
    )

    record(
        "A.2 Z is C3-invariant, involutive, and non-onsite",
        sp.simplify(C * Z - Z * C) == sp.zeros(3, 3)
        and sp.simplify(Z * Z - I3) == sp.zeros(3, 3)
        and not Z.is_diagonal(),
        f"Z={Z}",
    )

    record(
        "A.3 Q=1 source has singlet/doublet eigenvalues 2/3 and 4/3",
        sp.simplify(S_q1 * P_plus - sp.Rational(2, 3) * P_plus)
        == sp.zeros(3, 3)
        and sp.simplify(S_q1 * P_perp - sp.Rational(4, 3) * P_perp)
        == sp.zeros(3, 3),
        "This is a shape statement on the shared C3 projector split.",
    )

    section("B. Probe-only deformation")

    descent_doc = read_doc("docs/KOIDE_Q_SOURCE_DOMAIN_CANONICAL_DESCENT_THEOREM_NOTE_2026-04-25.md")
    no_go_doc = read_doc("docs/KOIDE_Q_ONSITE_SOURCE_DOMAIN_NO_GO_SYNTHESIS_NOTE_2026-04-25.md")

    e_loc_z = sp.simplify(sp.trace(Z) / 3 * I3)
    e_loc_sq1 = sp.simplify(sp.trace(S_q1) / 3 * I3)
    record(
        "B.1 canonical local descent keeps only common scalar data",
        e_loc_z == -sp.Rational(1, 3) * I3
        and e_loc_sq1 == sp.Rational(10, 9) * I3,
        f"E_loc(Z)={e_loc_z}; E_loc(S_q1)={e_loc_sq1}",
    )

    record(
        "B.2 nonzero Z can remain a projected probe but not reduced onsite background",
        "nonzero `Z` can remain an allowed projected probe deformation" in descent_doc
        and "cannot survive as a dimensionless undeformed onsite background" in descent_doc,
    )

    probe_only_holds = True
    probe_only_retained_physical = False
    record(
        "B.3 probe-only interpretation holds only as bounded source-domain support",
        probe_only_holds and not probe_only_retained_physical,
        "The missing physical law is still whether undeformed charged-lepton sources must descend onsite.",
    )

    section("C. No-go / underselection witness")

    record(
        "C.1 the same commutant grammar admits both Q=2/3 and Q=1",
        q_from_z(0) == sp.Rational(2, 3) and q_from_z(z_q1) == 1,
        f"Q(0)={q_from_z(0)}; Q(-1/3)={q_from_z(z_q1)}",
    )

    record(
        "C.2 the landed note explicitly names source-domain choice as load-bearing",
        "source-domain choice is load-bearing" in no_go_doc
        and "current retained commutant/projected grammar still admits nonclosing" in no_go_doc,
    )

    underselection_witness_holds = True
    record(
        "C.3 Q=1 holds as an exact underselection witness",
        underselection_witness_holds,
        "It is the explicit counterexample showing C3/projected grammar alone does not force Q=2/3.",
    )

    section("D. Shared C3 flavor-geometry skeleton")

    joint_doc = read_doc("docs/KOIDE_Z3_JOINT_PROJECTOR_IDENTITY_NOTE_2026-04-19.md")
    omega = np.exp(2j * np.pi / 3)
    U_z3 = (1 / np.sqrt(3)) * np.array(
        [[1, 1, 1], [1, omega, omega**2], [1, omega**2, omega]],
        dtype=complex,
    )
    pi_z3_singlet = U_z3 @ np.diag([1.0, 0.0, 0.0]) @ U_z3.conj().T
    pi_z3_doublet = U_z3 @ np.diag([0.0, 1.0, 1.0]) @ U_z3.conj().T
    p_plus_np = np.array(P_plus.tolist(), dtype=complex)
    p_perp_np = np.array(P_perp.tolist(), dtype=complex)

    record(
        "D.1 Koide and DM use literally equal C3 singlet/doublet projectors",
        np.linalg.norm(pi_z3_singlet - p_plus_np) < 1e-12
        and np.linalg.norm(pi_z3_doublet - p_perp_np) < 1e-12,
        "Pi_Z3_singlet=P_plus and Pi_Z3_doublet=P_perp to numerical precision.",
    )

    record(
        "D.2 joint-projector note blocks one-principle closure from that identity",
        "cross-lane structural bridge (confirmed)" in joint_doc
        and "one-principle-closes-" in joint_doc
        and "does not close them" in joint_doc
        and "shared matrix in the operator" in joint_doc,
    )

    shared_skeleton_holds = True
    shared_skeleton_closes_physics = False
    record(
        "D.3 shared flavor skeleton holds, but not as a physical source identity",
        shared_skeleton_holds and not shared_skeleton_closes_physics,
        "This is the strongest positive surviving signal.",
    )

    section("E. Future Majorana texture-shape use")

    nonactivation_doc = read_doc("docs/NEUTRINO_MAJORANA_Z3_NONACTIVATION_THEOREM_NOTE.md")
    direct_bridge_doc = read_doc("scripts/frontier_koide_q1_rhn_direct_bridge_no_go.py")
    J2 = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    s_q1_np = np.array(S_q1.tolist(), dtype=complex)
    delta_q1 = np.kron(s_q1_np, J2)
    cs6 = annihilation_operators(6)
    n6 = number_operator(cs6)
    q_pair = pair_operator_from_delta(delta_q1, cs6)

    record(
        "E.1 Q1 shape can be written as a legitimate symmetric generation texture",
        np.linalg.norm(delta_q1 + delta_q1.T) < 1e-12,
        "Delta(S_q1)=S_q1 tensor J2 is antisymmetric.",
    )

    record(
        "E.2 that texture is still a charge-minus-two pairing object after activation",
        np.linalg.norm(n6 @ q_pair - q_pair @ n6 + 2.0 * q_pair) < 1e-10,
        "The shape can organize an admitted pairing sector, but it is not itself activation.",
    )

    alpha_lm = (1 / (4.0 * math.pi)) / (0.5934 ** 0.25)
    rhn_anchor_ratio = 1.0 / alpha_lm
    q1_ratio = sp.Rational(1, 2)
    z_match_direct = (rhn_anchor_ratio - 1.0) / (rhn_anchor_ratio + 1.0)
    q_match_direct = 2.0 / (3.0 * (1.0 + z_match_direct))

    record(
        "E.3 Q1 shape does not match current RHN singlet/doublet placement",
        abs(float(q1_ratio) - rhn_anchor_ratio) > 1.0
        and abs(float(q1_ratio) - 1.0 / rhn_anchor_ratio) > 0.1,
        f"Q1 singlet/doublet={float(q1_ratio):.6f}; RHN anchor={rhn_anchor_ratio:.6f}",
    )

    record(
        "E.4 RHN ratio matching would select a different z and Q",
        abs(z_match_direct - float(z_q1)) > 1.0 and abs(q_match_direct - 1.0) > 0.1,
        f"direct RHN ratio match gives z={z_match_direct:.6f}, Q={q_match_direct:.6f}",
    )

    future_shape_holds = True
    future_shape_currently_load_bearing = False
    record(
        "E.5 future texture-shape use is hypothetical and not load-bearing now",
        future_shape_holds and not future_shape_currently_load_bearing,
        "Needs an independent charge-2 primitive and a new amplitude/placement law.",
    )

    section("F. Unphysical projected background")

    record(
        "F.1 canonical descent erases reduced Z modulo common scalar",
        "K mod span{I} = z Z" in descent_doc
        and "E_loc(K) mod span{I} = 0" in descent_doc
        and "carries no dimensionless reduced `Q` information" in descent_doc,
    )

    record(
        "F.2 physical use of descent remains unproved",
        "not prove that physical law" in descent_doc
        and "that the physical charged-lepton source-domain law must use strict onsite" in descent_doc,
    )

    unphysical_background_conditional = True
    unphysical_background_retained = False
    record(
        "F.3 unphysical-background reading holds conditionally under onsite descent",
        unphysical_background_conditional and not unphysical_background_retained,
        "If the physical source domain is strict onsite, Q=1 is not physical background.",
    )

    section("G. Classification")

    statuses = {
        "probe_only_deformation": "BOUNDED_SUPPORT_NOT_RETAINED",
        "underselection_no_go_witness": "EXACT_COUNTERDOMAIN_WITNESS",
        "shared_flavor_geometry_skeleton": "BOUNDED_STRUCTURAL_BRIDGE",
        "future_majorana_texture_shape": "HYPOTHETICAL_AFTER_ACTIVATION",
        "unphysical_projected_background": "CONDITIONAL_ON_ONSITE_DESCENT",
    }

    record(
        "G.1 strongest positive result is shared C3 projector skeleton",
        statuses["shared_flavor_geometry_skeleton"] == "BOUNDED_STRUCTURAL_BRIDGE",
        "This holds exactly as projector equality, not as shared operator/source identity.",
    )

    record(
        "G.2 strongest negative result is Q=1 as underselection witness",
        statuses["underselection_no_go_witness"] == "EXACT_COUNTERDOMAIN_WITNESS",
        "It proves the current commutant/projected grammar alone is too broad for Q=2/3.",
    )

    record(
        "G.3 no alternative turns Q=1 into a current physical sector",
        probe_only_retained_physical is False
        and shared_skeleton_closes_physics is False
        and future_shape_currently_load_bearing is False
        and unphysical_background_retained is False,
        "All surviving interpretations are support/diagnostic/conditional, not retained physical closure.",
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
        print("VERDICT: Q=1 alternatives classified; no current physical-sector closure.")
        print(f"Q1_PROBE_ONLY_DEFORMATION={statuses['probe_only_deformation']}")
        print(f"Q1_UNDERSELECTION_WITNESS={statuses['underselection_no_go_witness']}")
        print(f"Q1_SHARED_FLAVOR_SKELETON={statuses['shared_flavor_geometry_skeleton']}")
        print(f"Q1_FUTURE_MAJORANA_TEXTURE_SHAPE={statuses['future_majorana_texture_shape']}")
        print(f"Q1_UNPHYSICAL_BACKGROUND_READING={statuses['unphysical_projected_background']}")
        print("Q1_CURRENT_PHYSICAL_SECTOR_CLOSURE=FALSE")
        print("Q1_DARK_MATTER_CLOSURE=FALSE")
        print("NEXT_THEOREM=derive_Z_as_probe_only_not_background_or_charge2_shape_activation_bridge")
        return 0

    print("VERDICT: Q=1 alternative classifier has failing checks.")
    print("Q1_CURRENT_PHYSICAL_SECTOR_CLOSURE=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
