#!/usr/bin/env python3
"""Exact controls for operational reconstruction from record histories.

The runner separates:

1. record-state sufficiency from procedure labels;
2. continuation support from normalized probability;
3. a probability table from a tomographically complete quantum state;
4. effects from instruments and channels from their unravelings; and
5. positive one-site maps from completely positive composite maps.

It proves only finite-dimensional representation and non-entailment claims.
No probability law, operational ontology, or physical dynamics is adopted.
"""

from __future__ import annotations

from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AXIOM = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "OPERATIONAL_RECORD_RECONSTRUCTION_DEEP_PROBE_NOTE_2026-07-13.md"
FIREWALL = ROOT / "docs" / "POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md"
PRODUCTION = ROOT / "docs" / "RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md"
BUSCH = ROOT / "docs" / "BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
KRAUS = ROOT / "docs" / "KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md"
TENSOR_NOGO = ROOT / "docs" / "TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
PAULIS = (I2, X, Y, Z)
PXP = (I2 + X) / 2
PXM = (I2 - X) / 2
PYP = (I2 + Y) / 2
PYM = (I2 - Y) / 2
PZP = (I2 + Z) / 2
PZM = (I2 - Z) / 2
SIX_EFFECTS = (PXP, PXM, PYP, PYM, PZP, PZM)


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    suffix = f" :: {detail}" if detail else ""
    if condition:
        PASS += 1
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        print(f"FAIL {label}{suffix}")


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in left - right)


def probability(rho: sp.Matrix, effect: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(rho * effect))


def fingerprint(rho: sp.Matrix, effects: tuple[sp.Matrix, ...]) -> tuple[sp.Expr, ...]:
    return tuple(probability(rho, effect) for effect in effects)


def hermitian_span_rank(matrices: tuple[sp.Matrix, ...]) -> int:
    columns = [matrix.reshape(4, 1) for matrix in matrices]
    return sp.Matrix.hstack(*columns).rank()


def partial_transpose_first(matrix: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(4)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for ell in range(2):
                    out[2 * k + j, 2 * i + ell] = matrix[2 * i + j, 2 * k + ell]
    return out


def source_contract() -> None:
    section("A - Live-source and premise boundary")
    axiom = AXIOM.read_text()
    axiom_flat = " ".join(axiom.split())
    note = NOTE.read_text()
    firewall = " ".join(FIREWALL.read_text().lower().split())
    production = " ".join(PRODUCTION.read_text().lower().split())
    busch = " ".join(BUSCH.read_text().lower().split())
    kraus = " ".join(KRAUS.read_text().lower().split())
    tensor_nogo = " ".join(TENSOR_NOGO.read_text().lower().split())
    registry = json.loads(REGISTRY.read_text())

    for needle in (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
        "Only records are readable.",
        "A readout value is determined by record content alone.",
        "A state is a configuration of records.",
        "Probability, dynamics, readout contexts",
    ):
        check(f"A live axiom needle: {needle[:48]}", " ".join(needle.split()) in axiom_flat)
    check("A counts do not supply predictive probability", "does not supply a predictive probability law" in firewall)
    check("A append grammar has no predictive-weight slot", "append grammar has no slot" in production)
    check("A Busch bridge supplies an effect functional", "normalized effect-functional" in busch)
    check("A Kraus theorem does not type physical record dynamics", "any specific record-formation dynamics is cptp" in kraus)
    check("A tensor no-go retains no-extra-sector gap", "does not force generation/local tomography" in tensor_nogo)
    check("A only four approved premise nodes exist", len(registry["canonical_ids"]) == 4)
    check("A deep-probe note is authority-free", "**Authority:** none" in note)
    check("A deep-probe note contains N1-N8", all(f"### N{i}" in note for i in range(1, 9)))


def state_sufficiency_and_support() -> None:
    section("B - Record-state sufficiency and support/probability separation")

    procedure_to_record_state = {"plus": "c", "minus": "c"}
    state_fingerprint = {"c": (sp.Rational(1, 2), sp.Rational(1, 2))}
    collapsed = {
        procedure: state_fingerprint[state]
        for procedure, state in procedure_to_record_state.items()
    }
    check("B equal terminal record states force equal future fingerprints", collapsed["plus"] == collapsed["minus"])

    procedure_to_record_state = {"plus": "c_plus", "minus": "c_minus"}
    state_fingerprint = {
        "c_plus": (sp.Integer(1), sp.Integer(0)),
        "c_minus": (sp.Integer(0), sp.Integer(1)),
    }
    separated = {
        procedure: state_fingerprint[state]
        for procedure, state in procedure_to_record_state.items()
    }
    check("B a persistent preparation-reference record permits distinct fingerprints", separated["plus"] != separated["minus"])

    support = frozenset({"record_0", "record_1"})
    measure_a = {"record_0": sp.Rational(1, 2), "record_1": sp.Rational(1, 2)}
    measure_b = {"record_0": sp.Rational(1, 4), "record_1": sp.Rational(3, 4)}
    check("B both measures are normalized", sum(measure_a.values()) == sum(measure_b.values()) == 1)
    check("B both measures have the same full support", frozenset(measure_a) == frozenset(measure_b) == support)
    check("B identical support admits different predictions", measure_a != measure_b)


def state_tomography() -> None:
    section("C - Exact qubit operational tomography")
    rho_plus = PXP
    rho_minus = PXM
    rho_mixed = I2 / 2

    z_effects = (PZP, PZM)
    check("C plus, minus, and mixed states share one Z fingerprint", fingerprint(rho_plus, z_effects) == fingerprint(rho_minus, z_effects) == fingerprint(rho_mixed, z_effects))
    check("C X records distinguish all three", len({fingerprint(rho, (PXP, PXM)) for rho in (rho_plus, rho_minus, rho_mixed)}) == 3)
    check("C one binary context spans only two Hermitian dimensions", hermitian_span_rank(z_effects) == 2)
    check("C three Pauli contexts span all four Hermitian dimensions", hermitian_span_rank(SIX_EFFECTS) == 4)

    test_states = (
        PZP,
        PZM,
        PXP,
        PYP,
        I2 / 2,
        sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 5) - sp.I / 7], [sp.Rational(1, 5) + sp.I / 7, sp.Rational(1, 3)]]),
    )
    reconstructed = []
    for rho in test_states:
        rx = 2 * probability(rho, PXP) - 1
        ry = 2 * probability(rho, PYP) - 1
        rz = 2 * probability(rho, PZP) - 1
        rho_reconstructed = sp.simplify((I2 + rx * X + ry * Y + rz * Z) / 2)
        reconstructed.append(matrix_equal(rho_reconstructed, rho))
    check("C Pauli probabilities reconstruct every test density matrix", all(reconstructed))

    p_bad = sp.Rational(99, 100)
    r_bad = 2 * p_bad - 1
    rho_bad = (I2 + r_bad * (X + Y + Z)) / 2
    check("C arbitrary context-wise probabilities can violate positivity", sp.simplify(rho_bad.det()) < 0)

    lam = sp.Rational(2, 5)
    rho_mix = lam * rho_plus + (1 - lam) * rho_minus
    affine_rhs = tuple(
        sp.simplify(lam * a + (1 - lam) * b)
        for a, b in zip(fingerprint(rho_plus, SIX_EFFECTS), fingerprint(rho_minus, SIX_EFFECTS))
    )
    check("C supplied probabilistic mixtures have affine fingerprints", fingerprint(rho_mix, SIX_EFFECTS) == affine_rhs)


def effects_instruments_and_unravellings() -> None:
    section("D - Effects, instruments, channels, and actual event ambiguity")
    P0 = PZP
    P1 = PZM
    K_keep = P0
    K_flip = X * P0
    dagger = lambda matrix: matrix.conjugate().T

    effect_keep = sp.simplify(dagger(K_keep) * K_keep)
    effect_flip = sp.simplify(dagger(K_flip) * K_flip)
    check("D inequivalent operations have the same immediate effect", matrix_equal(effect_keep, P0) and matrix_equal(effect_flip, P0))

    rho = PXP
    p_keep = probability(rho, effect_keep)
    p_flip = probability(rho, effect_flip)
    post_keep = sp.simplify(K_keep * rho * dagger(K_keep) / p_keep)
    post_flip = sp.simplify(K_flip * rho * dagger(K_flip) / p_flip)
    check("D equal effects give equal immediate outcome probability", p_keep == p_flip == sp.Rational(1, 2))
    check("D their conditional post-record states differ", not matrix_equal(post_keep, post_flip))
    check("D a later Z record separates the instruments", probability(post_keep, P0) == 1 and probability(post_flip, P0) == 0)

    generic_rho = sp.Matrix(
        [
            [sp.Rational(1, 3), sp.Rational(1, 5) + sp.I / 7],
            [sp.Rational(1, 5) - sp.I / 7, sp.Rational(2, 3)],
        ]
    )
    projective_dephase = sp.simplify(P0 * generic_rho * P0 + P1 * generic_rho * P1)
    random_unitary_dephase = sp.simplify((generic_rho + Z * generic_rho * Z) / 2)
    check("D projective and random-unitary unravellings give one channel", matrix_equal(projective_dephase, random_unitary_dephase))
    projective_first_weight = probability(generic_rho, P0)
    random_unitary_first_weight = sp.Rational(1, 2) * sp.trace(generic_rho)
    check("D the same channel admits different event weights", projective_first_weight != random_unitary_first_weight)


def composition_and_complete_positivity() -> None:
    section("E - Composition is load-bearing for channels and tomography")
    rho_single = sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 5) + sp.I / 7], [sp.Rational(1, 5) - sp.I / 7, sp.Rational(1, 3)]])
    transposed = rho_single.T
    check("E transposition preserves trace on a one-site state", sp.trace(transposed) == sp.trace(rho_single) == 1)
    check("E transposition preserves one-site spectrum", transposed.charpoly().as_expr() == rho_single.charpoly().as_expr())

    bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
    bell_rho = bell * bell.conjugate().T
    partial = partial_transpose_first(bell_rho)
    check("E Bell partial transpose has the exact nonpositive spectrum", partial.eigenvals() == {sp.Rational(-1, 2): 1, sp.Rational(1, 2): 3})

    tau = sp.eye(4) / 4
    zero4 = sp.zeros(4)
    rho_left = sp.diag(tau, zero4)
    rho_right = sp.diag(zero4, tau)
    local_products = tuple(
        sp.diag(sp.kronecker_product(a, b), sp.kronecker_product(a, b))
        for a in PAULIS
        for b in PAULIS
    )
    check(
        "E different central sectors have identical local-product statistics",
        all(sp.simplify(sp.trace(rho_left * observable) - sp.trace(rho_right * observable)) == 0 for observable in local_products),
    )
    central = sp.diag(sp.eye(4), -sp.eye(4))
    check("E one global observable separates those locally identical states", sp.trace(rho_left * central) == 1 and sp.trace(rho_right * central) == -1)


def classification() -> None:
    section("F - Reconstruction classification")
    note = " ".join(NOTE.read_text().lower().replace("**", "").split())
    markers = (
        "record-state sufficiency",
        "support is not probability",
        "one readable context is not a quantum state",
        "an effect is not an instrument",
        "complete positivity already asks for composition",
        "prep-frame",
        "fiorentino and weigert",
        "does not support adding `preparation`",
    )
    for marker in markers:
        check(f"F note carries boundary marker: {marker}", marker in note)
    check("F note keeps operational objects downstream", "downstream operational definitions and representation theorems" in note)


def main() -> None:
    source_contract()
    state_sufficiency_and_support()
    state_tomography()
    effects_instruments_and_unravellings()
    composition_and_complete_positivity()
    classification()
    print("\n" + "=" * 79)
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("RESULT: FAIL")
        print("BOUNDARY: exact operational reconstruction controls; no physical probability law is supplied")
        raise SystemExit(1)
    print("RESULT: PASS")
    print("BOUNDARY: operational definitions are reconstructible only after record statistics and composition are supplied")


if __name__ == "__main__":
    main()
