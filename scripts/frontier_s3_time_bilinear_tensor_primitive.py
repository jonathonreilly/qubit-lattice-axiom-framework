#!/usr/bin/env python3
"""Exact seven-star carrier algebra and homogeneous-normalization no-go.

This runner is self-contained.  It does not import the older numerical tensor
pipeline or endpoint-fitted coefficients.  Exact SymPy arithmetic checks:

1. the 24-element proper-cubic action on the seven-site star;
2. the A1^2 + E + T1 adapted decomposition;
3. the oriented-axis bright subspace span(E_x, T1x);
4. exact center-excess blindness for a symbolic general cubic-commutant map;
5. the bilinear carrier factorization; and
6. an explicit scaled carrier family whose homogeneous algebra does not select
   the normalization lambda=1.

The last item is an algebraic normalization theorem.  It assumes the carrier
ray O_lambda=lambda K_R; it does not derive a physical tensor/readout
identification for that ray.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


@dataclass
class Check:
    name: str
    ok: bool
    detail: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str) -> None:
    CHECKS.append(Check(name, bool(ok), detail))
    print(f"[EXACT] {'PASS' if ok else 'FAIL'}: {name}")
    print(f"    {detail}")


def signed_permutation_rotations() -> list[sp.Matrix]:
    rotations: list[sp.Matrix] = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for source_axis, target_axis in enumerate(perm):
                matrix[target_axis, source_axis] = signs[source_axis]
            if matrix.det() == 1:
                rotations.append(matrix)
    unique = {tuple(matrix): matrix for matrix in rotations}
    return list(unique.values())


ARMS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
ARM_INDEX = {coord: index + 1 for index, coord in enumerate(ARMS)}


def star_rep(rotation: sp.Matrix) -> sp.Matrix:
    rep = sp.zeros(7)
    rep[0, 0] = 1
    for source, coord in enumerate(ARMS, start=1):
        image = tuple(int(value) for value in rotation * sp.Matrix(coord))
        rep[ARM_INDEX[image], source] = 1
    return rep


def vector(entries: list[sp.Expr | int]) -> sp.Matrix:
    return sp.Matrix(entries)


def main() -> int:
    print("Seven-star bilinear carrier: exact support and homogeneous-normalization no-go")
    print("=" * 78)

    rotations = signed_permutation_rotations()
    reps = [star_rep(rotation) for rotation in rotations]
    rotation_keys = {tuple(rotation) for rotation in rotations}
    closed = all(tuple(left * right) in rotation_keys for left in rotations for right in rotations)
    record(
        "the signed-permutation construction gives the proper cubic group",
        len(rotations) == 24
        and len({tuple(rotation) for rotation in rotations}) == 24
        and closed
        and all(rotation.T * rotation == sp.eye(3) and rotation.det() == 1 for rotation in rotations),
        f"group_order={len(rotations)}; closure, orthogonality, and determinant +1 hold exactly",
    )

    sqrt2, sqrt3, sqrt6, sqrt12 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6), sp.sqrt(12)
    e0 = vector([1, 0, 0, 0, 0, 0, 0])
    shell = vector([0, 1, 1, 1, 1, 1, 1]) / sqrt6
    e1 = vector([0, 1, 1, -1, -1, 0, 0]) / 2
    e2 = vector([0, 1, 1, 1, 1, -2, -2]) / sqrt12
    tx = vector([0, 1, -1, 0, 0, 0, 0]) / sqrt2
    ty = vector([0, 0, 0, 1, -1, 0, 0]) / sqrt2
    tz = vector([0, 0, 0, 0, 0, 1, -1]) / sqrt2
    basis = sp.Matrix.hstack(e0, shell, e1, e2, tx, ty, tz)
    record(
        "the displayed A1^2 + E + T1 adapted basis is exactly orthonormal",
        sp.simplify(basis.T * basis) == sp.eye(7),
        "B^T B = I_7 exactly",
    )

    p_a1 = e0 * e0.T + shell * shell.T
    p_e = e1 * e1.T + e2 * e2.T
    p_t1 = tx * tx.T + ty * ty.T + tz * tz.T
    group_average = sum(reps, sp.zeros(7)) / sp.Integer(len(reps))
    invariant_projectors = all(
        rep * projector == projector * rep
        for rep in reps
        for projector in (p_a1, p_e, p_t1)
    )
    record(
        "the proper-cubic star module decomposes exactly as A1^2 + E + T1",
        invariant_projectors
        and sp.simplify(group_average - p_a1) == sp.zeros(7)
        and sp.simplify(p_a1 + p_e + p_t1) == sp.eye(7),
        "group average has rank 2 and the three orthogonal projectors sum to I_7",
    )

    ex = sp.simplify((sqrt3 * e1 + e2) / 2)
    e_perp = sp.simplify((-e1 + sqrt3 * e2) / 2)
    x_axis = sp.Matrix([1, 0, 0])
    c4_reps = [
        rep
        for rotation, rep in zip(rotations, reps)
        if rotation * x_axis == x_axis
    ]
    p_c4 = sum(c4_reps, sp.zeros(7)) / sp.Integer(len(c4_reps))
    p_bright = ex * ex.T + tx * tx.T
    p_dark = e_perp * e_perp.T + ty * ty.T + tz * tz.T
    record(
        "the oriented-axis stabilizer selects exactly the aligned bright pair E_x and T1x",
        len(c4_reps) == 4
        and sp.simplify(p_c4 - p_a1 - p_bright) == sp.zeros(7)
        and p_bright.rank() == 2,
        "|C4_x|=4 and P_C4x - P_A1 = |E_x><E_x| + |T1x><T1x|",
    )
    record(
        "the remaining E + T1 coordinates form the exact dark complement",
        sp.simplify(p_bright + p_dark - p_e - p_t1) == sp.zeros(7)
        and sp.simplify(p_bright * p_dark) == sp.zeros(7),
        "B_x direct_sum D_x = E direct_sum T1 with orthogonal projectors",
    )

    a00, a01, a10, a11, eigen_e, eigen_t = sp.symbols(
        "a00 a01 a10 a11 eigen_e eigen_t", real=True
    )
    commutant_block = sp.diag(1, 1, 1, 1, 1, 1, 1)
    commutant_block[:2, :2] = sp.Matrix([[a00, a01], [a10, a11]])
    commutant_block[2:4, 2:4] = eigen_e * sp.eye(2)
    commutant_block[4:7, 4:7] = eigen_t * sp.eye(3)
    general_g = sp.simplify(basis * commutant_block * basis.T)
    identity_7 = sp.eye(7)
    commutator_constraints = sp.Matrix.vstack(
        *[
            sp.kronecker_product(rep.T, identity_7)
            - sp.kronecker_product(identity_7, rep)
            for rep in reps
        ]
    )
    commutant_nullity = 49 - commutator_constraints.rank()
    parameter_matrices = [
        general_g.diff(parameter)
        for parameter in (a00, a01, a10, a11, eigen_e, eigen_t)
    ]
    parameter_rank = sp.Matrix.hstack(
        *[matrix.reshape(49, 1) for matrix in parameter_matrices]
    ).rank()
    record(
        "the six-parameter displayed family exhausts the proper-cubic commutant",
        commutant_nullity == 6 and parameter_rank == 6,
        f"commutant_nullity={commutant_nullity}; displayed_parameter_rank={parameter_rank}",
    )
    ell = sp.Matrix([[1, -sp.Rational(1, 6), -sp.Rational(1, 6),
                      -sp.Rational(1, 6), -sp.Rational(1, 6),
                      -sp.Rational(1, 6), -sp.Rational(1, 6)]])
    total_charge = sp.ones(1, 7)
    non_scalar = sp.Matrix.hstack(ex, tx, e_perp, ty, tz)
    commutes = all(sp.simplify(general_g * rep - rep * general_g) == sp.zeros(7) for rep in reps)
    record(
        "a symbolic general proper-cubic commutant operator gives exact center-excess decoupling",
        commutes
        and sp.simplify(ell * general_g * non_scalar) == sp.zeros(1, 5)
        and sp.simplify(total_charge * non_scalar) == sp.zeros(1, 5),
        "ell G and total charge annihilate E_x, T1x, E_perp, T1y, and T1z identically",
    )

    delta, u_e, u_t = sp.symbols("delta u_E u_T", real=True)
    carrier = sp.Matrix([[u_e, u_t], [delta * u_e, delta * u_t]])
    outer = sp.Matrix([1, delta]) * sp.Matrix([[u_e, u_t]])
    record(
        "the carrier is the exact rank-at-most-one affine-scalar/bright outer product",
        sp.simplify(carrier - outer) == sp.zeros(2)
        and sp.factor(carrier.det()) == 0,
        "K_R=[1,delta]^T[u_E,u_T] and det(K_R)=0 as polynomial identities",
    )

    delta_q = sp.symbols("delta_q", finite=True, real=True)
    q_witness = e0 + ex
    witness_coordinates = {
        u_e: sp.simplify((ex.T * q_witness)[0]),
        u_t: sp.simplify((tx.T * q_witness)[0]),
        delta: delta_q,
    }
    model_one = carrier
    model_two = 2 * carrier
    witness_one = model_one.subs(witness_coordinates)
    witness_two = model_two.subs(witness_coordinates)
    homogeneous_invariants = (
        model_one.det() == 0
        and model_two.det() == 0
        and model_one.subs({u_e: 0, u_t: 0}) == sp.zeros(2)
        and model_two.subs({u_e: 0, u_t: 0}) == sp.zeros(2)
    )
    record(
        "homogeneous carrier algebra does not select lambda=1 in O_lambda=lambda K_R",
        homogeneous_invariants
        and sp.simplify((sp.ones(1, 7) * q_witness)[0]) == 1
        and witness_coordinates[u_e] == 1
        and witness_coordinates[u_t] == 0
        and witness_one != witness_two,
        "q*=e0+E_x has Q=1,u_E=1,u_T=0; K_R(q*) and 2K_R(q*) differ for every finite delta_q",
    )

    c_e, c_t = sp.symbols("c_E c_T", nonzero=True, real=True)
    channel_scaled = carrier * sp.diag(c_e, c_t)
    full_channel_scaler = p_a1 + c_e * p_e + c_t * p_t1
    channel_covariant = all(
        sp.simplify(full_channel_scaler * rep - rep * full_channel_scaler)
        == sp.zeros(7)
        for rep in reps
    )
    record(
        "proper-cubic inequivalent bright channels retain independent normalization freedom",
        sp.factor(channel_scaled.det()) == 0
        and channel_scaled.subs({c_e: 1, c_t: 1}) == carrier
        and channel_scaled.subs({c_e: 2, c_t: 3}) != carrier
        and channel_covariant,
        "P_A1+c_E P_E+c_T P_T1 commutes with every rotation, while scaled K_R remains rank one",
    )

    registry = json.loads((DOCS / "audit/data/axiom_premise_nodes.json").read_text())
    owner_registry = json.loads(
        (DOCS / "audit/data/owner_governed_premise_nodes.json").read_text()
    )
    tier_a_registry = json.loads(
        (DOCS / "audit/data/tier_a_admissions.json").read_text()
    )
    required_nodes = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    node_paths = {
        node: DOCS.parent / registry["nodes"][node]["current_path"]
        for node in required_nodes
    }
    node_text = {node: path.read_text() for node, path in node_paths.items()}
    normalized_node_text = {
        node: " ".join(text.split()) for node, text in node_text.items()
    }
    canonical_ids = set(registry["canonical_ids"])
    expected_owner_ids = {"staggered_dirac_realization_gate_note_2026-05-03"}
    owner_ids = set(owner_registry["canonical_ids"])
    owner_boundary = " ".join(
        owner_registry["nodes"][
            "staggered_dirac_realization_gate_note_2026-05-03"
        ]["boundary"].split()
    )
    registry_notes = {
        node: " ".join(registry["nodes"][node]["note"].split())
        for node in required_nodes
    }
    boundary_ok = (
        canonical_ids == required_nodes
        and "scalar readout" in normalized_node_text["minimal_axioms"]
        and "source/action and physical-observable identification"
        in normalized_node_text["minimal_axioms"]
        and "no mass ratio, coupling, mixing angle, phase, selector, readout bridge"
        in normalized_node_text["scale_reference_primitive"]
        and "no mass ratio, coupling, mixing angle, phase, selector, readout bridge"
        in registry_notes["kinetic_isotropy_primitive"]
        and "no state, state-selection rule, measure, typicality/genericity assumption, weighting, probability rule, preferred/default state, or state-contingent value"
        in registry_notes["realized_state_primitive"]
        and owner_ids == expected_owner_ids
        and "Retires only the current minimum AC_phi_lambda Tier-A atoms"
        in owner_boundary
        and "tensor" not in owner_boundary.lower()
        and tier_a_registry["genuine_admitted_input_count"] == 0
        and tier_a_registry["canonical_ids"] == []
        and tier_a_registry["derivation_targets"] == {}
    )
    record(
        "the strict dependency guard covers every approved premise node and confirms its narrow scope",
        boundary_ok,
        f"axiom/primitive ids={sorted(canonical_ids)}; owner ids={sorted(owner_ids)}; live Tier-A targets=0",
    )

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    passed = sum(check.ok for check in CHECKS)
    failed = sum(not check.ok for check in CHECKS)
    print(f"PASS={passed} FAIL={failed} TOTAL={len(CHECKS)}")
    if failed == 0:
        print("FINAL_TAG: S3_TIME_BILINEAR_CARRIER_HOMOGENEOUS_NORMALIZATION_NO_GO_EXACT")
        return 0
    print("FINAL_TAG: S3_TIME_BILINEAR_CARRIER_CHECK_FAILED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
