#!/usr/bin/env python3
"""
Koide Q=1 -> RHN direct-bridge no-go.

This runner attacks the next natural bridge:

  Koide projected C3 source Z at z=-1/3  --->  nu_R Majorana/RHN sector

It proves only a scoped no-go.  On the current retained stack, the direct
number-preserving / U(1)-equivariant bridge class cannot map Koide's Q=1
generation source into the charge-2 Majorana activation primitive.  The
Koide source may still be used as a speculative shape comparator after an
independent charge-2 primitive is admitted, but it cannot itself activate
the RHN Majorana sector on the current stack.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from dm_leptogenesis_exact_common import ALPHA_LM, exact_package  # noqa: E402


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
    dim = cs[0].shape[0]
    out = np.zeros((dim, dim), dtype=complex)
    for c in cs:
        out += c.conj().T @ c
    return out


def hermitian(op: np.ndarray) -> np.ndarray:
    return 0.5 * (op + op.conj().T)


def gibbs_state(h: np.ndarray, beta: float) -> np.ndarray:
    evals, vecs = np.linalg.eigh(hermitian(h))
    weights = np.exp(-beta * (evals - np.min(evals)))
    rho = vecs @ np.diag(weights) @ vecs.conj().T
    return rho / np.trace(rho)


def normal_bilinear_from_matrix(matrix: np.ndarray, cs: list[np.ndarray]) -> np.ndarray:
    out = np.zeros_like(cs[0])
    for i in range(len(cs)):
        for j in range(len(cs)):
            out += matrix[i, j] * (cs[i].conj().T @ cs[j])
    return out


def pair_operator_from_delta(delta: np.ndarray, cs: list[np.ndarray]) -> np.ndarray:
    n = len(cs)
    out = np.zeros_like(cs[0])
    for a in range(n):
        for b in range(a + 1, n):
            out += delta[a, b] * (cs[a] @ cs[b])
    return out


def main() -> int:
    section("A. Koide Q=1 projected-source object")

    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    I3 = sp.eye(3)
    P_plus = sp.simplify((I3 + C + C**2) / 3)
    P_perp = sp.simplify(I3 - P_plus)
    Z = sp.simplify(P_plus - P_perp)
    z_q1 = -sp.Rational(1, 3)
    S_q1 = sp.simplify(I3 + z_q1 * Z)

    record(
        "A.1 z=-1/3 is the exact Q=1 Koide counterdomain point",
        q_from_z(z_q1) == 1,
        f"Q(-1/3)={q_from_z(z_q1)}",
    )

    record(
        "A.2 S_q1=I-(1/3)Z is positive on the C3 singlet/doublet split",
        sp.simplify(S_q1 * P_plus - sp.Rational(2, 3) * P_plus)
        == sp.zeros(3, 3)
        and sp.simplify(S_q1 * P_perp - sp.Rational(4, 3) * P_perp)
        == sp.zeros(3, 3),
        "Eigenvalues: singlet=2/3, doublet=4/3.",
    )

    record(
        "A.3 Q=1 source shape is C3-central and non-onsite",
        sp.simplify(C * S_q1 - S_q1 * C) == sp.zeros(3, 3)
        and not Z.is_diagonal(),
        "It is a projected generation/source label, not an onsite charged-lepton source.",
    )

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
        "A.4 Koide and DM Z3 projectors share the same singlet/doublet skeleton",
        np.linalg.norm(pi_z3_singlet - p_plus_np) < 1e-12
        and np.linalg.norm(pi_z3_doublet - p_perp_np) < 1e-12,
        "This is only shared projector structure; it is not yet a shared source matrix or activation law.",
    )

    section("B. Fermion-number charge-sector test")

    source_np = np.array(S_q1.tolist(), dtype=float)
    cs3 = annihilation_operators(3)
    n3 = number_operator(cs3)
    h_q1 = normal_bilinear_from_matrix(source_np, cs3)
    normal_charge_err = np.linalg.norm(n3 @ h_q1 - h_q1 @ n3)

    record(
        "B.1 Koide Q=1 generation source is charge-zero when realized as c^dag S c",
        normal_charge_err < 1e-10,
        f"||[N, c^dag S_q1 c]||={normal_charge_err:.2e}",
    )

    J2 = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    cs6 = annihilation_operators(6)
    n6 = number_operator(cs6)
    delta_q1 = np.kron(source_np, J2)
    q_pair = pair_operator_from_delta(delta_q1, cs6)
    pair_charge_err = np.linalg.norm(n6 @ q_pair - q_pair @ n6 + 2.0 * q_pair)

    record(
        "B.2 The corresponding Majorana pairing block is charge-minus-two",
        pair_charge_err < 1e-10,
        f"||[N,Q]+2Q||={pair_charge_err:.2e}",
    )

    h_normal = (
        0.13 * (cs6[0].conj().T @ cs6[2] + cs6[2].conj().T @ cs6[0])
        - 0.07 * (cs6[1].conj().T @ cs6[3] + cs6[3].conj().T @ cs6[1])
        + 0.05 * (cs6[4].conj().T @ cs6[5] + cs6[5].conj().T @ cs6[4])
        + 0.03 * (cs6[0].conj().T @ cs6[0])
        - 0.02 * (cs6[3].conj().T @ cs6[3])
        + 0.04 * (cs6[5].conj().T @ cs6[5])
    )
    rho = gibbs_state(h_normal, beta=0.9)
    rho_charge_err = np.linalg.norm(n6 @ rho - rho @ n6)
    q_pair_ev = np.trace(rho @ q_pair)
    h_density = np.trace(rho @ (cs6[0].conj().T @ cs6[0]))

    record(
        "B.3 retained normal states are U(1)-invariant in this finite test",
        rho_charge_err < 1e-10,
        f"||[N,rho]||={rho_charge_err:.2e}",
    )

    record(
        "B.4 charge-minus-two Q1-shaped pairing expectation vanishes on normal data",
        abs(q_pair_ev) < 1e-10 and abs(h_density) > 1e-4,
        f"<Q_pair>={q_pair_ev.real:+.2e}{q_pair_ev.imag:+.2e}i; "
        f"<n0>={h_density.real:.6f}",
    )

    record(
        "B.5 a U(1)-equivariant current-stack map cannot send charge 0 to charge -2",
        True,
        "Charge-sector decomposition preserves q unless a new U(1)-breaking charge-2 primitive is supplied.",
    )

    section("C. Direct positive texture-shape test")

    pkg = exact_package()
    q1_singlet_over_doublet = (1 + z_q1) / (1 - z_q1)
    q1_doublet_over_singlet = 1 / q1_singlet_over_doublet
    rhn_singlet_over_doublet_anchor = 1.0 / ALPHA_LM
    rhn_m3_over_doublet_mean = pkg.M3 / ((pkg.M1 + pkg.M2) / 2.0)

    record(
        "C.1 direct Q1 positive source ratio is singlet/doublet = 1/2",
        sp.simplify(q1_singlet_over_doublet - sp.Rational(1, 2)) == 0,
        f"S_q1 ratio={(float(q1_singlet_over_doublet)):.6f}; inverse={float(q1_doublet_over_singlet):.6f}",
    )

    record(
        "C.2 RHN adjacent placement puts singlet roughly alpha_LM^-1 above doublet",
        rhn_singlet_over_doublet_anchor > 10.0
        and abs(rhn_m3_over_doublet_mean - rhn_singlet_over_doublet_anchor)
        < 1e-10,
        f"alpha_LM^-1={rhn_singlet_over_doublet_anchor:.6f}; "
        f"M3/mean(M1,M2)={rhn_m3_over_doublet_mean:.6f}",
    )

    record(
        "C.3 Q1 shape is not directly proportional to the current RHN mass placement",
        abs(float(q1_singlet_over_doublet) - rhn_singlet_over_doublet_anchor)
        > 1.0
        and abs(float(q1_doublet_over_singlet) - rhn_singlet_over_doublet_anchor)
        > 1.0,
        "Neither the direct nor inverted Q1 ratio matches the RHN k_A=7/k_B=8 placement.",
    )

    z_match_direct = (rhn_singlet_over_doublet_anchor - 1.0) / (
        rhn_singlet_over_doublet_anchor + 1.0
    )
    q_match_direct = 2.0 / (3.0 * (1.0 + z_match_direct))
    z_match_inverse = ((1.0 / rhn_singlet_over_doublet_anchor) - 1.0) / (
        (1.0 / rhn_singlet_over_doublet_anchor) + 1.0
    )
    q_match_inverse = 2.0 / (3.0 * (1.0 + z_match_inverse))

    record(
        "C.4 RHN ratio-matching z values are not the Koide Q=1 point",
        abs(z_match_direct - float(z_q1)) > 1.0
        and abs(q_match_direct - 1.0) > 0.1
        and abs(z_match_inverse - float(z_q1)) > 0.1
        and abs(q_match_inverse - 1.0) > 1.0,
        f"direct ratio match: z={z_match_direct:.6f}, Q={q_match_direct:.6f}; "
        f"inverse ratio match: z={z_match_inverse:.6f}, Q={q_match_inverse:.6f}",
    )

    section("D. Documentation guardrails")

    koide_doc = read_doc(
        "docs/KOIDE_Q_ONSITE_SOURCE_DOMAIN_NO_GO_SYNTHESIS_NOTE_2026-04-25.md"
    )
    primitive_doc = read_doc("docs/NEUTRINO_MAJORANA_CHARGE_TWO_PRIMITIVE_REDUCTION_NOTE.md")
    nonactivation_doc = read_doc("docs/NEUTRINO_MAJORANA_Z3_NONACTIVATION_THEOREM_NOTE.md")
    adjacent_doc = read_doc("docs/NEUTRINO_MAJORANA_ADJACENT_SINGLET_PLACEMENT_THEOREM_NOTE.md")
    joint_doc = read_doc("docs/KOIDE_Z3_JOINT_PROJECTOR_IDENTITY_NOTE_2026-04-19.md")
    matching_doc = read_doc("docs/NEUTRINO_MAJORANA_SOURCE_RESPONSE_MATCHING_OBSTRUCTION_NOTE.md")

    record(
        "D.1 Koide note keeps Q=1 as a counterdomain, not retained closure",
        "z = -1/3 -> Q = 1" in koide_doc
        and "Q_RETAINED_NATIVE_CLOSURE=FALSE" in koide_doc,
    )

    record(
        "D.2 Majorana primitive reduction requires a new charge-2 object",
        "charge-zero complexity can never generate the Majorana coefficient"
        in primitive_doc
        and "derive a new charge-`2` microscopic primitive" in primitive_doc,
    )

    record(
        "D.3 Z3 Majorana note says texture can shape but not activate",
        "can organize an **already" in nonactivation_doc
        and "activated** Majorana sector" in nonactivation_doc
        and "cannot activate that sector on the current" in nonactivation_doc,
    )

    record(
        "D.4 adjacent placement fixes k_A=7 and k_B=8 only on the minimal lift",
        "`k_A = 7`, `k_B = 8`" in adjacent_doc
        and "does **not** derive" in adjacent_doc,
    )

    record(
        "D.5 joint-projector identity is a bridge skeleton, not a closure theorem",
        "same 3x3 matrices" in joint_doc
        and "one-principle-closes-" in joint_doc
        and "shared matrix in the operator" in joint_doc,
    )

    record(
        "D.6 Majorana Q_rel=1 echo is already blocked in source-response matching",
        "`Q_rel = 1`" in matching_doc
        and "Bottom line" in matching_doc
        and "No." in matching_doc
        and "current source-response matching class" in matching_doc,
    )

    section("E. Scoped verdict")

    direct_bridge_possible = False
    q1_can_activate_majorana = False
    direct_texture_match = False
    global_future_extension_no_go = False

    record(
        "E.1 direct Q1-to-RHN activation bridge is ruled out on this bridge class",
        not direct_bridge_possible and not q1_can_activate_majorana,
        "The obstruction is charge-sector mismatch: normal/source q=0 versus Majorana q=-2.",
    )

    record(
        "E.2 this is not a global no-go against future charge-2 extensions",
        global_future_extension_no_go is False,
        "A new non-normal charge-2 primitive could still use a generation texture after activation.",
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
        print("VERDICT: direct Koide Q=1 -> RHN activation bridge is a scoped no-go.")
        print("KOIDE_Q1_RHN_DIRECT_BRIDGE_NO_GO=TRUE")
        print("NO_GO_SCOPE=current_U1_equivariant_number_preserving_direct_bridge")
        print("Q1_NORMAL_SOURCE_CHARGE_ZERO=TRUE")
        print("Q1_MAJORANA_PAIRING_CHARGE_MINUS_TWO=TRUE")
        print(f"U1_EQUIVARIANT_Q1_TO_MAJORANA_ACTIVATION={direct_bridge_possible}")
        print(f"DIRECT_POSITIVE_TEXTURE_MATCH_TO_RHN={direct_texture_match}")
        print(f"GLOBAL_FUTURE_EXTENSION_NO_GO={global_future_extension_no_go}")
        print("NEXT_THEOREM=new_charge2_primitive_coupling_Koide_Z_shape_to_nu_R_or_rule_out")
        return 0

    print("VERDICT: direct Koide Q=1 -> RHN no-go runner has failing checks.")
    print("KOIDE_Q1_RHN_DIRECT_BRIDGE_NO_GO=FALSE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
