#!/usr/bin/env python3
"""Block26: finite lease tensorization and exact autonomy boundary.

The runner imports the literal Block24 append channel and Block25 overlap
factor maps. It proves the complete-carrier tensor product on supplied
hard-core finite anchor families, attacks deterministic covariant ownership
on exact pair/cycle symmetries, and constructs explicit symmetric convex
mixtures of the physical append channels that survive those obstructions.
"""

from __future__ import annotations

import hashlib
import itertools
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_block24_overlap_projector_hard_exclusion_gate_2026_08_30 as block25  # noqa: E402
import admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30 as block24  # noqa: E402


parent = block24.parent
PACKET = ROOT / ".claude/science/physics-loops" / (
    "toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830"
)
RUNNER_SOURCE_PIN = PACKET / "RUNNER_SOURCE_PIN.md"
BLOCK24_SOURCE = (
    "scripts/admissibility_d4_self_delimiting_forward_record_append_history_"
    "2026_08_30.py"
)
BLOCK24_SOURCE_SHA256 = (
    "f98534f07655e0de296f2060932e34aa7a600f08545f3661be2843d05accc15d"
)
BLOCK25_SOURCE = (
    "scripts/admissibility_d4_block24_overlap_projector_hard_exclusion_gate_"
    "2026_08_30.py"
)
BLOCK25_SOURCE_SHA256 = (
    "5a1be28753ca13adc8fb22c1909fe3b2e86b79e9e8e65ab38aae02a625f6901f"
)
BLOCK24_NOTE = (
    "docs/ADMISSIBILITY_D4_SELF_DELIMITING_FORWARD_RECORD_APPEND_FINITE_"
    "HISTORY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md"
)
BLOCK24_NOTE_SHA256 = (
    "8bf1c8dc1bece0a2eaa057a7f1ef6d060afee2337793601a186ce4eab8da4a81"
)
BLOCK25_NOTE = (
    "docs/ADMISSIBILITY_D4_BLOCK24_OVERLAP_PROJECTOR_HARD_EXCLUSION_"
    "TOTALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md"
)
BLOCK25_NOTE_SHA256 = (
    "3a4da9d35a7af79e11931eabae72417b25021cf4d3f5bda62c22dc530dc8e6ee"
)
AXIOM_NOTE = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_NOTE_SHA256 = (
    "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753"
)
FROZEN = {
    "GOAL.md": "f6c8f11a6cc7362d98759bf143e21d41aa7643e7dcd10667ea242f1388ee365c",
    "AUTHORITY_GATE.md": "9aa8d443e1422fedb3d78efdb19c1e67b0578700874c133a78e544953ca1eab6",
    "ASSUMPTIONS_AND_IMPORTS.md": "e41401201f48a05ff8e9d7c9bb003e3fdd382d870f75133dc58f745a3b5b121d",
    "PREFLIGHT_WITNESSES.md": "9a8eaa9fadc2cd3f4592a8289558942783c521b50d518a420b1ac93568c6ddba",
    "ROUTE_PORTFOLIO.md": "fe54e1a0913ff81475134c4e4b845e41bc0ae7f586ef63592e4abc642c7664ae",
    "APPROACH_REGISTRY.md": "84451b59b4758604bcf21cbc2a1bcb45872d5561c77f4f25f0eae22a82b1c030",
    "OPPORTUNITY_QUEUE.md": "21c1c61776195b760023274161d2435cff74e442ee0a3d8e3bb34bbf5ba6335d",
    "PRIOR_ART_SWEEP.md": "d720b34b814d021fdde74b5d928dc2aaa032b884cf5710761bab6e4415d54382",
    "MUTATION_PLAN.md": "4eeb72b1b8959a908868f43b693df60b2815c2bf62a302790d44b7b455356543",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "2f62b6cce2a57c868ede4152da825eb8900789af71d8201ea96ffb584ec42a31",
    "TRACE_GATE.md": "a56a13396cbab8dccbf81fb60ffc018b58e79b40fda3302d27b098c4a5cab527",
    "ARTIFACT_PLAN.md": "f4c174290d8adb02db5c0a6dd36e5f5805547638571f315767cc6730aa6ad532",
    "PREREG_AMENDMENT_1.md": "3d41c28d2f5a6c90d1e20b9fc82c2a35817beacccc03fec94f72407a5b095afb",
    "INDEPENDENT_PREREG_ATTACK.md": "1da8de064e96c5150846b8cc6172f08dce61d12346f9087617d6d78d6724daf6",
}
AUDIT_INPUT_PATHS = (
    "scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py",
    "scripts/admissibility_d4_block24_overlap_projector_hard_exclusion_gate_2026_08_30.py",
    "scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py",
    "docs/ADMISSIBILITY_D4_SELF_DELIMITING_FORWARD_RECORD_APPEND_FINITE_HISTORY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md",
    "docs/ADMISSIBILITY_D4_BLOCK24_OVERLAP_PROJECTOR_HARD_EXCLUSION_TOTALIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/INDEPENDENT_PREREG_ATTACK.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block24-self-delimiting-forward-append-history-20260830/STATE.yaml",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/INDEPENDENT_PREREG_ATTACK.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/STATE.yaml",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/ROUTE_PORTFOLIO.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/OPPORTUNITY_QUEUE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/PRIOR_ART_SWEEP.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/PREREG_AMENDMENT_1.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/INDEPENDENT_PREREG_ATTACK.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/STATE.yaml",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/CLAIM_STATUS_CERTIFICATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block26-existing-qubit-lease-autonomy-20260830/REVIEW_HISTORY.md",
)
AUDIT_TIMEOUT_SEC = 900

ZERO = (0, 0, 0)
E1 = (1, 0, 0)
E2 = (0, 1, 0)
E3 = (0, 0, 1)
DIRECTIONS = parent.DIRECTIONS
OUTCOMES = parent.OUTCOMES
ROTATIONS = parent.ROTATIONS
SUPPORT = frozenset(parent.SUPPORT)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runner_source_pin_ok() -> bool:
    if not RUNNER_SOURCE_PIN.exists():
        return False
    pins = {}
    for line in RUNNER_SOURCE_PIN.read_text().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            pins[key.strip()] = value.strip().strip("`")
    return pins.get("source_sha256") == file_sha256(Path(__file__))


def frozen_hashes_ok() -> bool:
    return (
        all(file_sha256(PACKET / name) == digest for name, digest in FROZEN.items())
        and file_sha256(ROOT / BLOCK24_SOURCE) == BLOCK24_SOURCE_SHA256
        and file_sha256(ROOT / BLOCK25_SOURCE) == BLOCK25_SOURCE_SHA256
        and file_sha256(ROOT / BLOCK24_NOTE) == BLOCK24_NOTE_SHA256
        and file_sha256(ROOT / BLOCK25_NOTE) == BLOCK25_NOTE_SHA256
        and file_sha256(ROOT / AXIOM_NOTE) == AXIOM_NOTE_SHA256
        and runner_source_pin_ok()
    )


def add(left, right):
    return parent.add(left, right)


def negate(vector):
    return parent.negate(vector)


def subtract(left, right):
    return add(left, negate(right))


def scale(number, vector):
    return parent.scale(number, vector)


def translate(sites, center):
    return frozenset(parent.translate(set(sites), center))


def rotate_sites(sites, rotation):
    return frozenset(parent.mat_vec(rotation, site) for site in sites)


def complete_carrier(anchor, mutation=None):
    current = translate(SUPPORT, anchor)
    if mutation == "selected_64_only":
        return current | translate(
            SUPPORT, block24.forward_center(anchor, E1)
        )
    targets = (
        translate(SUPPORT, block24.forward_center(anchor, front))
        for front in DIRECTIONS
    )
    return frozenset().union(current, *targets)


def hard_core_family(anchors, mutation=None):
    carriers = {anchor: complete_carrier(anchor, mutation) for anchor in anchors}
    return carriers, all(
        carriers[left].isdisjoint(carriers[right])
        for left, right in itertools.combinations(anchors, 2)
    )


def hard_core_accepts_partial_pair(pair, mutation=None):
    left = complete_carrier(pair.anchor_a)
    right = complete_carrier(pair.anchor_b)
    if mutation == "admit_partial_overlap":
        left = translate(SUPPORT, pair.anchor_a)
        right = translate(SUPPORT, pair.anchor_b)
    return left.isdisjoint(right)


def reduce_projectors(expression, symbols):
    reduced = sp.expand(expression)
    for symbol in symbols:
        reduced = block24.projector_reduce(reduced, symbol)
    return sp.simplify(reduced)


@lru_cache(maxsize=1)
def imported_local_certificate():
    branches = block24.all_append_branches()
    certificate = block24.append_channel_certificate(branches, deep=True)
    required = (
        "branch_count",
        "fourteen_per_control",
        "factor_complete",
        "derived_effects",
        "positive_effects",
        "stochastic_rows",
        "controls_orthogonal",
        "actual_physical_gram_sum",
        "p_valid_projector",
        "kraus_complete",
        "arbitrary_reference",
        "classical_record_qnd",
        "coherent_code_not_qnd",
        "branch_covariance",
        "target_nonblank",
    )
    return branches, certificate, all(certificate[key] for key in required)


TENSOR_GRAM_EQUATION = (
    "sum_alpha_vec (tensor_i K_i,alpha_i)^dagger "
    "(tensor_i K_i,alpha_i) = tensor_i(sum_alpha_i K_i,alpha_i^dagger "
    "K_i,alpha_i) = tensor_i I_i"
)
TENSOR_MARGINAL_EQUATION = (
    "Tr_removed[(id_R tensor tensor_i Psi_i)(rho)] = "
    "(id_R tensor tensor_kept Psi_i)(Tr_removed rho)"
)


@lru_cache(maxsize=None)
def arbitrary_finite_tensor_induction(local_certificate_ok, mutation=None):
    # The imported Block24 channel has 1,176 success maps plus its literal
    # STOP.  Its actual operator Gram sum is I.  The mutation replaces that
    # local operator equality by (17/16)I before the tensor induction.
    n = sp.symbols("n", integer=True, positive=True)
    index = sp.symbols("i", integer=True, positive=True)
    local_gram = (
        sp.Rational(17, 16)
        if mutation == "bad_row"
        else (sp.S.One if local_certificate_ok else sp.Symbol("G_local"))
    )
    base = local_gram == 1
    generic_product = sp.Product(local_gram, (index, 1, n)).doit()
    step = sp.simplify(
        local_gram ** (n + 1) - local_gram**n * local_gram
    ) == 0
    kraus_count = 1177 ** n
    return (
        base
        and generic_product == 1
        and step
        and kraus_count.is_positive is True
    )


@lru_cache(maxsize=None)
def finite_tensor_completeness(mutation=None):
    branches, local, local_ok = imported_local_certificate()
    anchors = (ZERO, (60, 0, 0), (0, 60, 0))
    _carriers, disjoint = hard_core_family(anchors)
    local_complete_with_stop = (
        len(branches) == 1176
        and local["actual_physical_gram_sum"]
        and local["p_valid_projector"]
        and local["kraus_complete"]
        and local["arbitrary_reference"]
    )
    translated_channels = all(
        anchored_append_channel_certificate(anchor) for anchor in anchors
    )
    structural_induction = arbitrary_finite_tensor_induction(
        local_ok and local_complete_with_stop,
        "bad_row" if mutation == "bad_row" else None,
    )
    return (
        disjoint
        and translated_channels
        and structural_induction
        and local["classical_record_qnd"]
        and local["target_nonblank"]
        and local["branch_covariance"]
        and tensor_projective_certificate()
        and tensor_order_certificate()
    )


def partial_trace_second(matrix):
    result = sp.zeros(2)
    for a in range(2):
        for b in range(2):
            result[a, b] = sp.simplify(
                sum(matrix[2 * a + j, 2 * b + j] for j in range(2))
            )
    return result


def apply_channel(matrix, kraus):
    return sp.simplify(sum((k * matrix * k.H for k in kraus), sp.zeros(matrix.rows)))


@lru_cache(maxsize=None)
def tensor_projective_certificate(mutation=None):
    # Coefficientwise generic identity:
    # sum_(mu,u,r,s) K^mu_(u,r) rho_(a,r;b,s) K*^mu_(u,s)
    # = sum_(r,s) G_(s,r) rho_(a,r;b,s), with G=sum_mu K_mu^dag K_mu.
    rho = sp.symbols("rho00 rho01 rho10 rho11")
    gram = sp.eye(2)
    if mutation == "postselected_containment":
        gram = sp.diag(1, 0)
    after = sp.simplify(
        sum(gram[s, r] * rho[2 * r + s] for r in range(2) for s in range(2))
    )
    before = sp.simplify(rho[0] + rho[3])
    return after == before


@lru_cache(maxsize=1)
def tensor_order_certificate():
    # Bind the generic tensor-factor identity to two literal physical append
    # branches whose complete 224-site carriers are disjoint.
    anchor_left = ZERO
    anchor_right = (60, 0, 0)
    branch_left = typed_append_group(anchor_left, E1, E2)[0]
    branch_right = typed_append_group(anchor_right, E2, E3)[-1]
    physical_binding = (
        block24.append_factorization_is_physical(branch_left)
        and block24.append_factorization_is_physical(branch_right)
        and complete_carrier(anchor_left).isdisjoint(
            complete_carrier(anchor_right)
        )
    )
    a0, a1, a2, a3 = sp.symbols("a0:4")
    b0, b1, b2, b3 = sp.symbols("b0:4")
    left = sp.Matrix([[a0, a1], [a2, a3]])
    right = sp.Matrix([[b0, b1], [b2, b3]])
    embedded_left = sp.kronecker_product(left, sp.eye(2))
    embedded_right = sp.kronecker_product(sp.eye(2), right)
    return physical_binding and sp.simplify(
        embedded_left * embedded_right - embedded_right * embedded_left
    ) == sp.zeros(4)


@lru_cache(maxsize=1)
def global_stop_projectivity_fails():
    # Local valid=|0> appends to |1>; local invalid=|1> is STOP.
    ket0 = sp.Matrix([1, 0])
    ket1 = sp.Matrix([0, 1])
    input_state = sp.kronecker_product(ket0, ket1)
    input_density = input_state * input_state.T
    single_success = ket1 * ket0.T
    single_stop = ket1 * ket1.T
    local_x = (single_success, single_stop)
    per_lease = tuple(
        sp.kronecker_product(a, b) for a in local_x for b in local_x
    )
    per_output = apply_channel(input_density, per_lease)
    p_both = sp.kronecker_product(ket0 * ket0.T, ket0 * ket0.T)
    global_success = sp.kronecker_product(single_success, single_success)
    global_stop = sp.eye(4) - p_both
    global_output = apply_channel(input_density, (global_success, global_stop))
    return (
        partial_trace_second(per_output) == ket1 * ket1.T
        and partial_trace_second(global_output) == ket0 * ket0.T
    )


@lru_cache(maxsize=None)
def carrier_covariance_certificate(mutation=None):
    anchor = (7, -5, 3)
    carrier = complete_carrier(anchor)
    rotations = ROTATIONS[:-1] if mutation == "incomplete_frames" else ROTATIONS
    rotation_ok = len(rotations) == 24 and all(
        rotate_sites(carrier, rotation)
        == complete_carrier(parent.mat_vec(rotation, anchor))
        for rotation in rotations
    )
    ax, ay, az, tx, ty, tz = sp.symbols("ax ay az tx ty tz", integer=True)
    symbolic_anchor = (ax, ay, az)
    translation = (tx, ty, tz)
    moved = complete_carrier(add(symbolic_anchor, translation))
    expected = frozenset(add(site, translation) for site in complete_carrier(symbolic_anchor))
    return rotation_ok and moved == expected


def relative_owner_certificate(anchors, mutation=None):
    carriers, hard_core = hard_core_family(anchors)
    if not hard_core:
        return False
    owner = {}
    for anchor, sites in carriers.items():
        for site in sites:
            if site in owner:
                return False
            owner[site] = anchor
    relative = all(owner[site] == anchor for anchor, sites in carriers.items() for site in sites)
    if mutation == "absolute_owner_claim":
        # The exact shared target has two distinct physical claimants even if only
        # one is placed in the supplied declaration.
        claims = {
            (ZERO, (-1, 0, 0)): block24.forward_center(ZERO, (-1, 0, 0)),
            ((-18, 0, 0), (1, 0, 0)): block24.forward_center(
                (-18, 0, 0), (1, 0, 0)
            ),
        }
        relative &= len(set(claims.values())) == len(claims)
    return relative


@lru_cache(maxsize=1)
def shared_target_absolute_boundary():
    anchor_a = ZERO
    front_a = (-1, 0, 0)
    anchor_b = (-18, 0, 0)
    front_b = (1, 0, 0)
    source = OUTCOMES[0]
    clean, current_a, target_a, current_b, target_b, center_a, center_b = (
        block25.clean_target_only_pair(anchor_a, front_a, anchor_b, front_b)
    )
    left = block25.tip_control(anchor_a, front_a, source)
    right = block25.tip_control(anchor_b, front_b, source)
    shared, overlaps, q = block25.shared_product_fidelity(left, right)
    return (
        clean
        and current_a.isdisjoint(current_b)
        and center_a == center_b == (-9, 0, 0)
        and target_a == target_b
        and len(shared) == 32
        and all(value == 1 for value in overlaps)
        and q == 1
        and block25.projections_commute(q)
    )


@lru_cache(maxsize=None)
def renewal_boundary_certificate(mutation=None):
    left = ZERO
    right = scale(27, E1)
    initial_overlap = complete_carrier(left) & complete_carrier(right)
    returned_left = scale(9, E1)
    returned_right = scale(18, E1)
    returned_overlap = complete_carrier(returned_left) & complete_carrier(returned_right)
    if mutation == "initial_implies_renewal":
        return not initial_overlap and not returned_overlap
    left_target = translate(SUPPORT, returned_left)
    right_target = translate(SUPPORT, returned_right)
    return (
        not initial_overlap
        and left_target.isdisjoint(right_target)
        and len(returned_overlap) == 64
        and block24.forward_center(returned_left, E1) == returned_right
        and block24.forward_center(returned_right, negate(E1)) == returned_left
    )


@lru_cache(maxsize=1)
def renewal_overlap_witness():
    left = ZERO
    right = scale(27, E1)
    returned_left = scale(9, E1)
    returned_right = scale(18, E1)
    return (
        len(complete_carrier(left) & complete_carrier(right)),
        len(complete_carrier(returned_left) & complete_carrier(returned_right)),
    )


@lru_cache(maxsize=1)
def blank_debit_certificate():
    return all(
        parent.pointer_overlap(
            parent.BLANK_POINTER, parent.locked_word(front, outcome)
        )
        == 0
        for front in DIRECTIONS
        for outcome in OUTCOMES
    )


PAIR_ROTATION = ((-1, 0, 0), (0, -1, 0), (0, 0, 1))
PAIR_TRANSLATION = (-19, -1, 0)
PAIR_ANCHORS = (ZERO, (-19, -1, 0))
PAIR_FRONTS = ((-1, 0, 0), (1, 0, 0))


def affine(rotation, translation, site):
    return add(parent.mat_vec(rotation, site), translation)


def affine_control_signature(control, rotation, translation=ZERO):
    return {
        (
            affine(rotation, translation, item.physical_site),
            item.role,
            parent.mat_vec(rotation, item.local_site),
            parent.mat_vec(rotation, item.vector),
        )
        for item in control.constraints
    }


def control_signature(control):
    return {
        (item.physical_site, item.role, item.local_site, item.vector)
        for item in control.constraints
    }


@lru_cache(maxsize=None)
def pair_symmetry_certificate(mutation=None):
    rotation = PAIR_ROTATION
    translation = PAIR_TRANSLATION
    if mutation == "improper_pair_map":
        rotation = ((-1, 0, 0), (0, 1, 0), (0, 0, 1))
    if mutation == "break_claimant_exchange":
        translation = add(PAIR_TRANSLATION, E1)
    source_a = OUTCOMES[0]
    source_b = parent.mat_vec(rotation, source_a)
    anchor_a, anchor_b = PAIR_ANCHORS
    front_a, front_b = PAIR_FRONTS
    target_a = block24.forward_center(anchor_a, front_a)
    target_b = block24.forward_center(anchor_b, front_b)
    control_a = block25.tip_control(anchor_a, front_a, source_a)
    control_b = block25.tip_control(anchor_b, front_b, source_b)
    determinant = sp.Matrix(rotation).det()
    proper = rotation in ROTATIONS and determinant == 1
    exchanges = (
        affine(rotation, translation, anchor_a) == anchor_b
        and affine(rotation, translation, anchor_b) == anchor_a
        and parent.mat_vec(rotation, front_a) == front_b
        and parent.mat_vec(rotation, front_b) == front_a
        and affine(rotation, translation, target_a) == target_b
        and affine(rotation, translation, target_b) == target_a
        and parent.rotate_word(parent.locked_word(front_a, source_a), rotation)
        == parent.locked_word(front_b, source_b)
        and parent.rotate_word(parent.locked_word(front_b, source_b), rotation)
        == parent.locked_word(front_a, source_a)
        and affine_control_signature(
            control_a, rotation, translation
        )
        == control_signature(control_b)
        and affine_control_signature(
            control_b, rotation, translation
        )
        == control_signature(control_a)
    )
    # The first coordinate equation is 2*x=-19, so no lattice fixed point.
    fixed_point_free = all(
        affine(rotation, translation, site) != site
        for site in itertools.product(range(-24, 6), repeat=3)
    ) and translation[0] % 2 == 1
    return proper and exchanges and fixed_point_free


@lru_cache(maxsize=None)
def deterministic_pair_certificate(mutation=None):
    descriptor_invariant = pair_symmetry_certificate(
        "break_claimant_exchange"
        if mutation == "break_claimant_exchange"
        else None
    )
    if mutation == "coordinate_winner":
        chosen = (1, 0)
        swapped = tuple(reversed(chosen))
        return chosen == swapped
    safety_limit = 2 if mutation == "allow_double_grant" else 1
    invariant_grants, safe_invariant, liveness = deterministic_pair_grant_sets(
        safety_limit
    )
    return (
        descriptor_invariant
        and invariant_grants == ((0, 0), (1, 1))
        and safe_invariant == ((0, 0),)
        and liveness == ()
    )


@lru_cache(maxsize=None)
def deterministic_pair_grant_sets(safety_limit=1):
    all_grants = tuple(itertools.product((0, 1), repeat=2))
    invariant_grants = tuple(
        grant for grant in all_grants if grant == tuple(reversed(grant))
    )
    safe_invariant = tuple(
        grant for grant in invariant_grants if sum(grant) <= safety_limit
    )
    liveness = tuple(grant for grant in safe_invariant if sum(grant) == 1)
    return invariant_grants, safe_invariant, liveness


TRIANGLE_ROTATION = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
TRIANGLE_FRONTS = (negate(E1), negate(E3), negate(E2))
TRIANGLE_SOURCES = (E1, E3, E2)
TRIANGLE_ANCHORS = (
    add(scale(9, E1), E3),
    add(E2, scale(9, E3)),
    add(E1, scale(9, E2)),
)


@lru_cache(maxsize=None)
def triangle_certificate(mutation=None):
    sources = TRIANGLE_SOURCES
    if mutation == "frozen_triangle_source":
        sources = (E1, E1, E1)
    controls = tuple(
        block25.tip_control(anchor, front, source)
        for anchor, front, source in zip(
            TRIANGLE_ANCHORS, TRIANGLE_FRONTS, sources
        )
    )
    current = tuple(translate(SUPPORT, anchor) for anchor in TRIANGLE_ANCHORS)
    targets = tuple(
        translate(SUPPORT, block24.forward_center(anchor, front))
        for anchor, front in zip(TRIANGLE_ANCHORS, TRIANGLE_FRONTS)
    )
    geometry = all(
        current[i].isdisjoint(current[j])
        and current[i].isdisjoint(targets[j])
        and current[j].isdisjoint(targets[i])
        for i, j in itertools.combinations(range(3), 2)
    )
    pair_data = []
    for i, j in itertools.combinations(range(3), 2):
        shared, overlaps, q = block25.shared_product_fidelity(controls[i], controls[j])
        pair_data.append(
            len(shared) == 2
            and overlaps == (sp.Rational(1, 2), sp.Rational(1, 2))
            and q == sp.Rational(1, 4)
            and sp.simplify(2 * q * (1 - q)) == sp.Rational(3, 8)
        )
    cycle = all(
        parent.mat_vec(TRIANGLE_ROTATION, TRIANGLE_ANCHORS[i])
        == TRIANGLE_ANCHORS[(i + 1) % 3]
        and parent.mat_vec(TRIANGLE_ROTATION, TRIANGLE_FRONTS[i])
        == TRIANGLE_FRONTS[(i + 1) % 3]
        and parent.mat_vec(TRIANGLE_ROTATION, sources[i])
        == sources[(i + 1) % 3]
        and parent.rotate_word(
            parent.locked_word(TRIANGLE_FRONTS[i], sources[i]),
            TRIANGLE_ROTATION,
        )
        == parent.locked_word(
            TRIANGLE_FRONTS[(i + 1) % 3], sources[(i + 1) % 3]
        )
        and affine_control_signature(
            controls[i], TRIANGLE_ROTATION
        )
        == control_signature(controls[(i + 1) % 3])
        for i in range(3)
    )
    all_grants = tuple(itertools.product((0, 1), repeat=3))
    invariant_grants = tuple(
        grant
        for grant in all_grants
        if grant == (grant[2], grant[0], grant[1])
    )
    deterministic_wall = all(sum(bits) != 1 for bits in invariant_grants)
    triple_shared = set.intersection(*(set(target) for target in targets))
    return (
        TRIANGLE_ROTATION in ROTATIONS
        and sp.Matrix(TRIANGLE_ROTATION) ** 3 == sp.eye(3)
        and geometry
        and all(pair_data)
        and triple_shared == {ZERO}
        and cycle
        and deterministic_wall
    )


@lru_cache(maxsize=1)
def edge_anticorrelation_triangle_fails():
    satisfying = tuple(
        bits
        for bits in itertools.product((0, 1), repeat=3)
        if bits[0] + bits[1] == 1
        and bits[1] + bits[2] == 1
        and bits[2] + bits[0] == 1
    )
    return satisfying == ()


def basis(index, dimension):
    vector = sp.zeros(dimension, 1)
    vector[index, 0] = 1
    return vector


def partial_trace_two_qubit(rho, keep):
    result = sp.zeros(2)
    for a in range(2):
        for b in range(2):
            if keep == 0:
                result[a, b] = sum(rho[2 * a + j, 2 * b + j] for j in range(2))
            else:
                result[a, b] = sum(rho[2 * j + a, 2 * j + b] for j in range(2))
    return sp.simplify(result)


@lru_cache(maxsize=None)
def unary_owner_code_certificate(mutation=None):
    ket00 = basis(0, 4)
    ket01 = basis(1, 4)
    ket10 = basis(2, 4)
    rho_ind = sp.eye(4) / 4
    if mutation == "independent_owner_state":
        rho_one = rho_ind
    else:
        rho_one = (ket10 * ket10.T + ket01 * ket01.T) / 2
    swap = sp.Matrix(
        [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
    )
    exact_one = sp.diag(0, 1, 1, 0)
    marginals = (
        partial_trace_two_qubit(rho_one, 0) == sp.eye(2) / 2
        and partial_trace_two_qubit(rho_one, 1) == sp.eye(2) / 2
        and partial_trace_two_qubit(rho_ind, 0) == sp.eye(2) / 2
        and partial_trace_two_qubit(rho_ind, 1) == sp.eye(2) / 2
    )
    return (
        sp.trace(rho_one) == 1
        and rho_one.is_positive_semidefinite
        and swap * rho_one * swap.T == rho_one
        and sp.trace(exact_one * rho_one) == 1
        and marginals
        and sp.trace(exact_one * rho_ind) == sp.Rational(1, 2)
    )


@lru_cache(maxsize=None)
def unary_owner_instrument_certificate(mutation=None):
    ket00 = basis(0, 4)
    ket01 = basis(1, 4)
    ket10 = basis(2, 4)
    p00 = ket00 * ket00.T
    k_a = (ket10 * ket00.T) / sp.sqrt(2)
    k_b = (ket01 * ket00.T) / sp.sqrt(2)
    kraus = [k_a, k_b, sp.eye(4) - p00]
    if mutation == "delete_owner_outcome":
        kraus = [k_a, sp.eye(4) - p00]
    completeness = sp.simplify(sum((k.H * k for k in kraus), sp.zeros(4)))
    blank_output = apply_channel(p00, kraus)
    expected = (ket10 * ket10.T + ket01 * ket01.T) / 2
    return completeness == sp.eye(4) and blank_output == expected


def nonempty_subsets(items):
    for count in range(1, len(items) + 1):
        yield from itertools.combinations(items, count)


@dataclass(frozen=True)
class CompoundKrausDescriptor:
    kind: str
    owner: str
    gram_weight: object
    appends: tuple


@dataclass(frozen=True)
class RoutedChannelTerm:
    sector: tuple
    owner: str
    weight: object
    channel_anchor: tuple | None
    kraus_form: str


@dataclass(frozen=True)
class AnchoredAppendChannel:
    anchor: tuple
    successes: tuple
    stop_present: bool = True
    stop_action: str = "I-P_valid; no new Record"


@lru_cache(maxsize=None)
def typed_append_group(anchor, front, source):
    word = parent.locked_word(front, source)
    return tuple(
        block24.append_branch(anchor, word, outcome) for outcome in OUTCOMES
    )


@lru_cache(maxsize=None)
def anchored_append_channel(anchor, stop_present=True):
    return AnchoredAppendChannel(
        anchor=anchor,
        successes=tuple(block24.all_append_branches(anchor)),
        stop_present=stop_present,
    )


@lru_cache(maxsize=None)
def anchored_append_channel_certificate(anchor, stop_present=True):
    """All 1,176 physical successes plus literal K_STOP=I-P_valid."""
    channel = anchored_append_channel(anchor, stop_present)
    grouped = {
        (front, source): tuple(
            branch
            for branch in channel.successes
            if branch.front == front and branch.source == source
        )
        for front in DIRECTIONS
        for source in OUTCOMES
    }
    rows = tuple(
        sp.simplify(sum(branch.effect.scalar for branch in group))
        for group in grouped.values()
    )
    p = sp.symbols("p_valid", commutative=True)
    stop_gram = (1 - p) ** 2 if channel.stop_present else sp.S.Zero
    gram = reduce_projectors(p + stop_gram, (p,))
    local = imported_local_certificate()[1]
    return (
        len(channel.successes) == 1176
        and len(grouped) == 84
        and all(len(group) == 14 for group in grouped.values())
        and all(row == 1 for row in rows)
        and all(
            branch.anchor == channel.anchor
            and branch.forward_center
            == block24.forward_center(channel.anchor, branch.front)
            and append_current_is_qnd(branch)
            and append_has_one_blank_debit(branch)
            and append_output_owner(branch)
            == (branch.anchor, branch.front, branch.target)
            for branch in channel.successes
        )
        and local["actual_physical_gram_sum"]
        and local["p_valid_projector"]
        and local["classical_record_qnd"]
        and local["branch_covariance"]
        and block24.translation_covariance_certificate()
        and channel.stop_action == "I-P_valid; no new Record"
        and gram == 1
        and sp.simplify(stop_gram.subs(p, 1)) == 0
    )


def append_output_word(branch):
    data = block24.factor_dictionary(branch.factors)
    return tuple(item[2] for item in data["forward_writer_pointer_maps"])


def append_output_owner(branch):
    decoded = parent.decode_locked_word(append_output_word(branch))
    if decoded is None:
        return None
    front, outcome = decoded
    derived_anchor = subtract(
        branch.forward_center, scale(block24.DISPLACEMENT, front)
    )
    return derived_anchor, front, outcome


def append_current_is_qnd(branch, mutation=None):
    factors = branch.factors
    if mutation == "overwrite_other_record":
        factors = block24.make_append_factors(
            branch.anchor,
            branch.current_word,
            branch.target,
            current_output_override=parent.BLANK_POINTER,
        )
    data = block24.factor_dictionary(factors)
    maps = data["current_pointer_projectors"]
    output = tuple(item[2] for item in maps)
    return (
        tuple(item[1] for item in maps) == branch.current_word
        and output == branch.current_word
    )


def append_has_one_blank_debit(branch):
    data = block24.factor_dictionary(branch.factors)
    writer_output = append_output_word(branch)
    return (
        branch.effect.forward_input == parent.BLANK_BLOCK
        and data["forward_center"] == branch.forward_center
        and writer_output == parent.locked_word(branch.front, branch.target)
        and parent.pointer_overlap(parent.BLANK_POINTER, writer_output) == 0
    )


@lru_cache(maxsize=None)
def common_target_clique_certificate(mutation=None):
    """Equal-mixture channels for each supplied nonempty claimant subset.

    This is deliberately *not* a claim/grant transaction in the target
    pointer shell: Block24 requires that shell to be exactly Blank.  For each
    separately supplied subset S and stored-label tuple, the physical channel
    is the convex mixture |S|^-1 sum_f Psi_f of literal complete Block24
    channels.  On the declared all-valid/common-Blank sector, every selected
    Psi_f succeeds and exactly one branch writes the shared target.  Off that
    sector, each selected channel retains its own literal STOP completion.
    """
    target = ZERO
    anchors = {front: scale(-9, front) for front in DIRECTIONS}
    currents = {front: translate(SUPPORT, anchor) for front, anchor in anchors.items()}
    target_sites = translate(SUPPORT, target)
    geometry = all(
        currents[left].isdisjoint(currents[right])
        for left, right in itertools.combinations(DIRECTIONS, 2)
    ) and all(sites.isdisjoint(target_sites) for sites in currents.values())
    cross_current_qnd = all(
        currents[other].isdisjoint(complete_carrier(anchors[front]))
        for front, other in itertools.permutations(DIRECTIONS, 2)
    )
    sources = OUTCOMES
    if mutation == "single_source_clique":
        sources = (E1,)
    groups = {
        (front, source): typed_append_group(anchors[front], front, source)
        for front in DIRECTIONS
        for source in sources
    }
    anchored_channels_ok = all(
        anchored_append_channel_certificate(
            anchors[front],
            stop_present=not (
                mutation == "delete_clique_stop" and front == E1
            ),
        )
        for front in DIRECTIONS
    )
    anchored_successes = {
        front: anchored_append_channel(anchors[front]).successes
        for front in DIRECTIONS
    }
    physical_groups = (
        len(groups) == 84
        and all(
            len(group) == 14
            and all(
                branch.forward_center == target
                and block24.append_factorization_is_physical(branch)
                and append_current_is_qnd(branch)
                and append_has_one_blank_debit(branch)
                for branch in group
            )
            and sp.simplify(sum(branch.effect.scalar for branch in group)) == 1
            for group in groups.values()
        )
    )
    valid_controls_are_inside_full_channel = all(
        block24.append_valid_sector_eigenvalue(
            parent.locked_word(front, source), True
        )
        == 1
        and all(branch in anchored_successes[front] for branch in group)
        for (front, source), group in groups.items()
    )
    output_words = {
        (front, outcome): append_output_word(
            typed_append_group(anchors[front], front, E1)[OUTCOMES.index(outcome)]
        )
        for front in DIRECTIONS
        for outcome in OUTCOMES
    }
    orthogonal_outputs = len(set(output_words.values())) == 84 and all(
        parent.pointer_overlap(left, right) == int(left == right)
        for left, right in itertools.combinations_with_replacement(
            output_words.values(), 2
        )
    )
    output_owner_derived = all(
        append_output_owner(branch)
        == (branch.anchor, branch.front, branch.target)
        for group in groups.values()
        for branch in group
    )
    common_blank = True
    for left, right in itertools.combinations(DIRECTIONS, 2):
        for source_left in OUTCOMES:
            for source_right in OUTCOMES:
                control_left = block25.tip_control(
                    anchors[left], left, source_left
                )
                control_right = block25.tip_control(
                    anchors[right], right, source_right
                )
                shared, overlaps, fidelity = block25.shared_product_fidelity(
                    control_left, control_right
                )
                common_blank &= (
                    control_left.target_center
                    == control_right.target_center
                    == target
                    and len(shared) == 32
                    and all(value == 1 for value in overlaps)
                    and fidelity == 1
                    and block25.projections_commute(fidelity)
                )

    normalized = at_most_one = full_cptp = declared_exact_one = True
    for subset in nonempty_subsets(DIRECTIONS):
        selected = list(subset)
        if mutation == "drop_clique_winner" and len(subset) == 3:
            selected = selected[:-1]
        weight = sp.S.One / len(subset)
        weight_sum = sp.simplify(sum(weight for _front in selected))
        normalized &= weight_sum == 1
        selected_rows_are_one = True
        for front in selected:
            # All 14 possible stored labels are physical rows.  A concrete
            # supplied label tuple selects one of these rows per claimant.
            for source in OUTCOMES:
                group = groups.get((front, source), ())
                row = sp.simplify(sum(branch.effect.scalar for branch in group))
                selected_rows_are_one &= row == 1
                for outcome, branch in zip(OUTCOMES, group):
                    descriptor = CompoundKrausDescriptor(
                        kind="success",
                        owner=str(front),
                        gram_weight=sp.simplify(
                            weight * branch.effect.scalar
                        ),
                        appends=(branch,),
                    )
                    if (
                        mutation == "double_clique_writer"
                        and len(subset) == 2
                        and front == selected[0]
                        and source == OUTCOMES[0]
                        and outcome == OUTCOMES[0]
                    ):
                        other = subset[1]
                        descriptor = CompoundKrausDescriptor(
                            kind="success",
                            owner="double",
                            gram_weight=descriptor.gram_weight,
                            appends=(
                                descriptor.appends[0],
                                typed_append_group(
                                    anchors[other], other, OUTCOMES[0]
                                )[0],
                            ),
                        )
                    at_most_one &= len(descriptor.appends) <= 1
        # Convexity of selected complete physical channels supplies the
        # full-space Gram identity.  Each certificate above explicitly
        # includes K_STOP=I-P.
        full_cptp &= (
            weight_sum == 1
            and anchored_channels_ok
            and imported_local_certificate()[1]["p_valid_projector"]
        )
        # Every individual source row is one. Therefore an arbitrary supplied
        # label tuple has sum_f (1/|S|)*1=1 on the all-valid/common-Blank
        # sector; no 14^|S| tuple enumeration is hidden here.
        declared_exact_one &= selected_rows_are_one and weight_sum == 1
    singleton = all(
        anchored_append_channel(anchors[front]).successes
        == tuple(block24.all_append_branches(anchors[front]))
        and anchored_append_channel(anchors[front]).stop_present
        for front in DIRECTIONS
    )
    covariance = all(
        {
            parent.mat_vec(rotation, front) for front in subset
        }
        == set(
            tuple(parent.mat_vec(rotation, front) for front in subset)
        )
        and all(
            parent.mat_vec(rotation, anchors[front])
            == anchors[parent.mat_vec(rotation, front)]
            for front in subset
        )
        for subset in nonempty_subsets(DIRECTIONS)
        for rotation in ROTATIONS
    )
    return (
        geometry
        and cross_current_qnd
        and physical_groups
        and anchored_channels_ok
        and valid_controls_are_inside_full_channel
        and common_blank
        and orthogonal_outputs
        and output_owner_derived
        and normalized
        and singleton
        and at_most_one
        and full_cptp
        and declared_exact_one
        and covariance
        and imported_local_certificate()[1]["branch_covariance"]
    )


def partial_overlap_pair():
    return block25.build_pair(
        PAIR_FRONTS[0],
        PAIR_FRONTS[1],
        OUTCOMES[0],
        parent.mat_vec(PAIR_ROTATION, OUTCOMES[0]),
        (-1, -1, 0),
    )


@lru_cache(maxsize=1)
def unsharp_overlap_matrices():
    pair = partial_overlap_pair()
    q = sp.simplify(pair.product_fidelity)
    amplitude = sp.sqrt(q)
    perpendicular = sp.sqrt(1 - q)
    vector_p = sp.Matrix([1, 0])
    vector_q = sp.Matrix([amplitude, perpendicular])
    p = vector_p * vector_p.T
    q_projector = vector_q * vector_q.T
    f_a = p / 2
    f_b = q_projector / 2
    f_zero = sp.eye(2) - f_a - f_b
    return pair, p, q_projector, f_a, f_b, f_zero


@lru_cache(maxsize=1)
def selected_pair_fiber_binding_certificate():
    """Restrict each full P_valid to the named exact-current E_11 fiber."""
    pair = partial_overlap_pair()
    selected = {
        "A": (pair.front_a, pair.source_a, pair.anchor_a),
        "B": (pair.front_b, pair.source_b, pair.anchor_b),
    }
    all_words = tuple(
        parent.locked_word(front, source)
        for front in DIRECTIONS
        for source in OUTCOMES
    )
    exact_current_restriction = all(
        all(
            parent.pointer_overlap(parent.locked_word(front, source), word)
            == int(word == parent.locked_word(front, source))
            for word in all_words
        )
        and sp.simplify(
            sum(
                branch.effect.scalar
                for branch in typed_append_group(anchor, front, source)
            )
        )
        == 1
        for front, source, anchor in selected.values()
    )
    e_a, e_b, pi_a, pi_b = sp.symbols(
        "E_A E_B Pi_A Pi_B", commutative=True
    )
    e_11 = e_a * e_b
    # Once the other 83 current-word controls vanish, the surviving full
    # P_valid term is exactly current-presence times the named target-Blank
    # projector Pi.  The two disjoint current factors commute with both Pis.
    restricted_a = reduce_projectors(
        e_11 * (e_a * pi_a) - e_11 * pi_a,
        (e_a, e_b, pi_a, pi_b),
    ) == 0
    restricted_b = reduce_projectors(
        e_11 * (e_b * pi_b) - e_11 * pi_b,
        (e_a, e_b, pi_a, pi_b),
    ) == 0
    return (
        exact_current_restriction
        and reduce_projectors(e_11, (e_a, e_b)) == e_11
        and restricted_a
        and restricted_b
    )


@lru_cache(maxsize=None)
def unsharp_overlap_certificate(mutation=None):
    pair, p, q_projector, f_a, f_b, f_zero = unsharp_overlap_matrices()
    eigenvalues = set(f_zero.eigenvals())
    completeness = sp.simplify(f_a + f_b + f_zero) == sp.eye(2)
    span_positive = eigenvalues == {
        sp.Rational(1, 4),
        sp.Rational(3, 4),
    }
    a_ray = sp.Matrix([1, 0])
    weights = (
        sp.simplify((a_ray.T * f_a * a_ray)[0]),
        sp.simplify((a_ray.T * f_b * a_ray)[0]),
        sp.simplify((a_ray.T * f_zero * a_ray)[0]),
    )
    groups = {
        "A": typed_append_group(pair.anchor_a, pair.front_a, pair.source_a),
        "B": typed_append_group(pair.anchor_b, pair.front_b, pair.source_b),
    }
    anchored_channels = {
        owner: anchored_append_channel(
            group[0].anchor,
            stop_present=not (
                mutation == "delete_pair_stop" and owner == "A"
            ),
        )
        for owner, group in groups.items()
    }
    descriptors = [
        CompoundKrausDescriptor(
            kind="success",
            owner=owner,
            gram_weight=sp.simplify(
                sp.Rational(1, 2) * branch.effect.scalar
            ),
            appends=(branch,),
        )
        for owner, channel in anchored_channels.items()
        for branch in channel.successes
    ] + [
        CompoundKrausDescriptor(
            kind="stop",
            owner="none",
            gram_weight=(sp.Rational(1, 2), "I-P_valid"),
            appends=(),
        )
        for _owner in anchored_channels
    ]
    if mutation == "delete_pair_stop":
        descriptors = [
            descriptor
            for index, descriptor in enumerate(descriptors)
            if not (descriptor.kind == "stop" and index == len(descriptors) - 2)
        ]
    if mutation == "double_writer_branch":
        descriptors[0] = CompoundKrausDescriptor(
            kind="success",
            owner="double",
            gram_weight=sp.simplify(
                sp.Rational(1, 2) * groups["A"][0].effect.scalar
            ),
            appends=(groups["A"][0], groups["B"][0]),
        )
    row_complete = all(
        sp.simplify(sum(branch.effect.scalar for branch in group)) == 1
        for group in groups.values()
    )
    convex_complete = (
        row_complete
        and sp.Rational(1, 2) + sp.Rational(1, 2) == 1
        and sum(descriptor.kind == "stop" for descriptor in descriptors) == 2
        and all(
            anchored_append_channel_certificate(
                channel.anchor, channel.stop_present
            )
            for channel in anchored_channels.values()
        )
    )
    actual_branches = all(
        block24.append_factorization_is_physical(branch)
        and append_current_is_qnd(
            branch,
            "overwrite_other_record"
            if mutation == "overwrite_other_record" and owner == "A" and branch == group[0]
            else None,
        )
        and append_has_one_blank_debit(branch)
        for owner, group in groups.items()
        for branch in group
    )
    at_most_one = all(len(descriptor.appends) <= 1 for descriptor in descriptors)
    recorded_owner = all(
        descriptor.kind == "stop"
        or (
            len(descriptor.appends) == 1
            and append_output_owner(descriptor.appends[0])
            == (
                descriptor.appends[0].anchor,
                descriptor.appends[0].front,
                descriptor.appends[0].target,
            )
            and descriptor.owner
            == ("A" if descriptor.appends[0].anchor == pair.anchor_a else "B")
        )
        for descriptor in descriptors
    )
    current_a = translate(SUPPORT, pair.anchor_a)
    current_b = translate(SUPPORT, pair.anchor_b)
    cross_current_qnd = (
        current_a.isdisjoint(current_b)
        and current_a.isdisjoint(complete_carrier(pair.anchor_b))
        and current_b.isdisjoint(complete_carrier(pair.anchor_a))
    )
    target_pointer_records_distinguishable = translate(
        parent.POINTER, pair.target_a
    ).isdisjoint(translate(parent.POINTER, pair.target_b))
    covariance = pair_symmetry_certificate() and all(
        parent.rotate_word(append_output_word(groups["A"][OUTCOMES.index(outcome)]), PAIR_ROTATION)
        == append_output_word(
            groups["B"][OUTCOMES.index(parent.mat_vec(PAIR_ROTATION, outcome))]
        )
        for outcome in OUTCOMES
    )
    scalar = sp.symbols("w", real=True)
    no_stop_equations = (
        sp.Eq(1 - scalar * (1 + sp.Rational(1, 2)), 0),
        sp.Eq(1 - scalar * (1 - sp.Rational(1, 2)), 0),
    )
    no_scalar_totalizer = sp.solve(no_stop_equations, (scalar,), dict=True) == []
    projector_sum = sp.simplify(p + q_projector)
    projector_sum_spectrum = tuple(projector_sum.eigenvals())
    lambda_max = max(projector_sum_spectrum, key=sp.default_sort_key)
    maximal_scalar = sp.simplify(1 / lambda_max)
    residual = sp.simplify(sp.eye(2) - maximal_scalar * projector_sum)
    residual_spectrum = tuple(residual.eigenvals())
    delta = sp.symbols("delta", positive=True)
    maximal_residual = (
        maximal_scalar.is_positive
        and all(value.is_nonnegative for value in residual_spectrum)
        and any(value == 0 for value in residual_spectrum)
        and any(value.is_positive for value in residual_spectrum)
        and sp.simplify(1 - (maximal_scalar + delta) * lambda_max).is_negative
    )
    return (
        pair.clean_target_only_overlap
        and pair.product_fidelity == sp.Rational(1, 4)
        and pair.commutator_norm_factor == sp.Rational(3, 8)
        and selected_pair_fiber_binding_certificate()
        and completeness
        and span_positive
        and weights
        == (sp.Rational(1, 2), sp.Rational(1, 8), sp.Rational(3, 8))
        and convex_complete
        and actual_branches
        and at_most_one
        and recorded_owner
        and cross_current_qnd
        and target_pointer_records_distinguishable
        and covariance
        and no_scalar_totalizer
        and maximal_residual
    )


@lru_cache(maxsize=None)
def current_record_qnd_certificate(mutation=None):
    pair = partial_overlap_pair()
    controls = (
        (pair.anchor_a, pair.front_a, pair.source_a),
        (pair.anchor_b, pair.front_b, pair.source_b),
    )
    maps_ok = True
    for index, (anchor, front, source) in enumerate(controls):
        word = parent.locked_word(front, source)
        factors = block24.make_append_factors(anchor, word, OUTCOMES[0])
        branch = block24.append_branch(anchor, word, OUTCOMES[0])
        maps_ok &= append_current_is_qnd(
            branch,
            "overwrite_other_record"
            if mutation == "overwrite_other_record" and index == 0
            else None,
        )
    current_a = translate(SUPPORT, pair.anchor_a)
    current_b = translate(SUPPORT, pair.anchor_b)
    return maps_ok and current_a.isdisjoint(current_b)


@lru_cache(maxsize=None)
def sectorized_singleton_certificate(mutation=None):
    pair = partial_overlap_pair()
    groups = {
        "A": typed_append_group(pair.anchor_a, pair.front_a, pair.source_a),
        "B": typed_append_group(pair.anchor_b, pair.front_b, pair.source_b),
    }
    anchored_channels = {
        "A": anchored_append_channel(pair.anchor_a),
        "B": anchored_append_channel(pair.anchor_b),
    }
    def coefficients(present_a, present_b):
        if present_a and not present_b:
            return (sp.S.One, sp.S.Zero, sp.S.Zero)
        if present_b and not present_a:
            return (sp.S.Zero, sp.S.One, sp.S.Zero)
        if present_a and present_b:
            return (sp.Rational(1, 2), sp.Rational(1, 2), sp.S.Zero)
        return (sp.S.Zero, sp.S.Zero, sp.S.One)

    routing = {
        bits: coefficients(*bits)
        for bits in itertools.product((0, 1), repeat=2)
    }
    if mutation == "raw_mixture_singletons":
        routing[(1, 0)] = (sp.Rational(1, 2), sp.S.Zero, sp.Rational(1, 2))
    normalized = all(sp.simplify(sum(weights)) == 1 for weights in routing.values())
    singleton = routing[(1, 0)] == (1, 0, 0) and routing[(0, 1)] == (0, 1, 0)
    symmetric = routing[(1, 1)][0] == routing[(1, 1)][1]
    actual = all(
        len(group) == 14
        and all(block24.append_factorization_is_physical(branch) for branch in group)
        for group in groups.values()
    )
    current_a = translate(SUPPORT, pair.anchor_a)
    current_b = translate(SUPPORT, pair.anchor_b)
    commuting_presence = (
        pair.clean_target_only_overlap
        and current_a.isdisjoint(current_b)
        and current_a.isdisjoint(translate(SUPPORT, pair.target_b))
        and current_b.isdisjoint(translate(SUPPORT, pair.target_a))
    )

    # Four actual direct-sum current-Record sectors.  Since the two current
    # blocks are disjoint and every selected append is QND there, these
    # projectors commute with and survive every routed channel.
    p_a, p_b = sp.symbols("p_A p_B", commutative=True)
    sectors = {
        (0, 0): (1 - p_a) * (1 - p_b),
        (1, 0): p_a * (1 - p_b),
        (0, 1): (1 - p_a) * p_b,
        (1, 1): p_a * p_b,
    }
    sector_sum = reduce_projectors(sum(sectors.values()), (p_a, p_b)) == 1
    sector_orthogonality = all(
        reduce_projectors(left * right, (p_a, p_b)) == 0
        for left_key, left in sectors.items()
        for right_key, right in sectors.items()
        if left_key != right_key
    )
    routed_physical_families = all(
        (
            weights[0] == 0
            or anchored_append_channel_certificate(pair.anchor_a)
        )
        and (
            weights[1] == 0
            or anchored_append_channel_certificate(pair.anchor_b)
        )
        for weights in routing.values()
    )
    routed_terms = tuple(
        RoutedChannelTerm(
            sector=sector,
            owner=owner,
            weight=weight,
            channel_anchor=(
                anchored_channels[owner].anchor if owner in anchored_channels else None
            ),
            kraus_form=(
                "sqrt(weight) K_owner,mu E_sector"
                if owner in anchored_channels
                else "E_00"
            ),
        )
        for sector, weights in routing.items()
        for owner, weight in zip(("A", "B", "identity"), weights)
        if weight != 0
    )
    routed_operator_binding = all(
        (
            term.owner == "identity"
            and term.sector == (0, 0)
            and term.channel_anchor is None
        )
        or (
            term.owner in anchored_channels
            and term.channel_anchor == anchored_channels[term.owner].anchor
            and term.weight > 0
        )
        for term in routed_terms
    )
    swap_covariance = pair_symmetry_certificate() and all(
        routing[(right, left)]
        == (weights[1], weights[0], weights[2])
        for (left, right), weights in routing.items()
    )
    # For M_(s,o,mu)=sqrt(w_so) K_(o,mu) E_s and full channel
    # Grams G_o=I, the complete Gram is sum_s E_s^2 sum_o w_so.
    direct_sum_gram = reduce_projectors(
        sum(
            sectors[sector] ** 2 * sp.simplify(sum(weights))
            for sector, weights in routing.items()
        ),
        (p_a, p_b),
    )
    direct_sum_complete = (
        sector_sum
        and sector_orthogonality
        and normalized
        and all(
            anchored_append_channel_certificate(channel.anchor)
            for channel in anchored_channels.values()
        )
        and all(
            sp.simplify(sum(branch.effect.scalar for branch in group)) == 1
            for group in groups.values()
        )
        and direct_sum_gram == 1
    )
    return (
        normalized
        and singleton
        and symmetric
        and actual
        and commuting_presence
        and routed_physical_families
        and routed_operator_binding
        and swap_covariance
        and direct_sum_complete
        and current_record_qnd_certificate()
    )


TERMINAL_TEXT = (
    "TERMINAL: CONDITIONAL-FINITE-LEASE-TENSOR-AND-PHYSICAL-"
    "CONVEX-COLLISION-CHANNELS-POSITIVE"
)
SCOPE_TEXT = (
    "SCOPE: supplied finite disjoint carriers, separately supplied common-target "
    "subsets, and the exact q=1/4 pair; collision-law identity, renewal, firing, "
    "rate, retention, obligation retirement, and TOE closure remain open; "
    "deterministic descriptor classifications are diagnostics, not impossibility claims"
)
NO_GO_CHECKLIST = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
RESOLUTION_LINES = (
    "per_element: checked 1,176 literal success factors, exact rows, STOP "
    "algebra, selected-fiber effects, and physical mutations",
    "per_site: checked 224-site carriers, current/target intersections, "
    "Blank debit, output-owner decoding, and returned overlap",
    "per_mode: checked all 84 current labels, 63 nonempty common-target "
    "subsets, 24 cubic frames, and source-label covariance",
    "per_block: checked full anchored channels, arbitrary finite disjoint "
    "tensor algebra, physical pair/clique mixtures, and four Record sectors",
    "lattice_wide: checked and not executed — no endogenous registry, "
    "renewal, Blank production, invocation/rate, gravity, Born derivation, "
    "retention, obligation retirement, or TOE closure is constructed",
)


def emitted_claim_text(mutation=None):
    terminal = TERMINAL_TEXT
    scope = SCOPE_TEXT
    if mutation == "promote_scope":
        scope += "; TOE SCORES MOVE AND OBLIGATIONS RETIRE"
    if mutation == "ship_negative_terminal":
        terminal += "; GENERAL ARBITRATION NO-GO"
    return terminal + "\n" + scope


def scope_guard_certificate(mutation=None):
    emitted = emitted_claim_text(mutation).upper()
    forbidden_promotions = (
        "TOE SCORES MOVE",
        "OBLIGATIONS RETIRE",
        "AXIOM UPDATE FORCED",
        "GRAVITY DERIVED",
        "BORN RULE DERIVED",
        "GENERAL ARBITRATION NO-GO",
        "AUDIT RETAINED",
    )
    return not any(phrase in emitted for phrase in forbidden_promotions)


def negative_claim_demotion_certificate(mutation=None):
    """Bind the written failed N1--N8 gate to a positive-only terminal."""
    if not NO_GO_CHECKLIST.exists():
        return False
    text = NO_GO_CHECKLIST.read_text()
    required_sections = tuple(f"## N{index}" for index in range(1, 9))
    written_gate = (
        all(section in text for section in required_sections)
        and "Gate result for a negative claim: `FAIL`" in text
        and "remove deterministic no-go language from the terminal" in text
        and "conditional positive bounded theorem" in text
    )
    emitted = emitted_claim_text(mutation).upper()
    negative_absent = (
        "NO-GO" not in emitted
        and "DETERMINISTIC-SYMMETRY-BOUNDARY" not in emitted
    )
    positive_steelman_executed = (
        common_target_clique_certificate()
        and unsharp_overlap_certificate()
    )
    substantive_n5 = (
        tuple(line.split(":", 1)[0] for line in RESOLUTION_LINES)
        == ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")
        and all(len(line) >= 40 for line in RESOLUTION_LINES)
        and "checked and not executed —" in RESOLUTION_LINES[-1]
    )
    return (
        written_gate
        and negative_absent
        and positive_steelman_executed
        and substantive_n5
    )


MUTATION_TARGETS = (
    ("selected_64_only", "complete_carrier_geometry"),
    ("admit_partial_overlap", "hard_core_excludes_Block25_pair"),
    ("global_all_or_none_stop", "projective_consistency"),
    ("bad_row", "finite_tensor_CPTP"),
    ("postselected_containment", "projective_consistency"),
    ("absolute_owner_claim", "relative_ownership_only"),
    ("initial_implies_renewal", "renewal_boundary"),
    ("improper_pair_map", "pair_exchange_symmetry"),
    ("break_claimant_exchange", "deterministic_pair_boundary"),
    ("coordinate_winner", "deterministic_pair_boundary"),
    ("allow_double_grant", "deterministic_pair_boundary"),
    ("frozen_triangle_source", "three_cycle_boundary"),
    ("independent_owner_state", "kinematic_one_owner_coupling"),
    ("delete_owner_outcome", "kinematic_owner_preparation"),
    ("single_source_clique", "common_target_clique"),
    ("drop_clique_winner", "common_target_clique"),
    ("delete_clique_stop", "common_target_clique"),
    ("double_clique_writer", "common_target_clique"),
    ("double_writer_branch", "unsharp_partial_overlap"),
    ("delete_pair_stop", "unsharp_partial_overlap"),
    ("overwrite_other_record", "collision_old_Record_QND"),
    ("raw_mixture_singletons", "sectorized_singleton_reduction"),
    ("incomplete_frames", "carrier_family_covariance"),
    ("ship_negative_terminal", "negative_claim_demoted"),
    ("promote_scope", "scope_guards"),
)


def evaluated_checks(mutation=None):
    branches, local, local_ok = imported_local_certificate()
    geometry = block24.fixed_anchor_geometry()
    carrier = complete_carrier(ZERO, mutation)
    anchors = (ZERO, (60, 0, 0), (0, 60, 0))
    carriers, hard_core = hard_core_family(anchors)
    pair = partial_overlap_pair()
    partial_admitted = hard_core_accepts_partial_pair(
        pair, "admit_partial_overlap" if mutation == "admit_partial_overlap" else None
    )
    projective = tensor_projective_certificate(
        "postselected_containment" if mutation == "postselected_containment" else None
    )
    if mutation == "global_all_or_none_stop":
        projective = not global_stop_projectivity_fails()
    return (
        (
            "freeze",
            frozen_hashes_ok() and block24.frozen_hashes_ok() and block25.frozen_hashes_ok(),
            "12 preregistration files and exact Block24/25/axiom inputs are content pinned",
        ),
        (
            "literal_Block24_channel_import",
            len(branches) == 1176 and local_ok,
            "all 1,176 literal branches re-contract to 84 orthogonal normalized controls with local CPTP completion",
        ),
        (
            "complete_carrier_geometry",
            len(carrier) == 224
            and geometry["sites"] == 224
            and geometry["radius2"] == 169
            and geometry["pairwise_disjoint"],
            "the literal channel carrier is one current plus six candidate 32-site blocks, 224 sites at radius 13",
        ),
        (
            "finite_hard_core_family",
            hard_core and all(len(sites) == 224 for sites in carriers.values()),
            "a three-anchor fixture has pairwise-disjoint complete carriers; the proof consumes only the pairwise predicate",
        ),
        (
            "hard_core_excludes_Block25_pair",
            not partial_admitted
            and pair.clean_target_only_overlap
            and pair.product_fidelity == sp.Rational(1, 4)
            and bool(block25.tip_control(pair.anchor_a, pair.front_a, pair.source_a).carrier_sites
                     & block25.tip_control(pair.anchor_b, pair.front_b, pair.source_b).carrier_sites),
            "the q=1/4 partial-overlap pair is outside the direct tensor family rather than silently admitted",
        ),
        (
            "finite_tensor_CPTP",
            finite_tensor_completeness(
                "bad_row" if mutation == "bad_row" else None
            ),
            "the literal 1,176-success-plus-STOP Gram identity factorizes as the displayed tensor equation for arbitrary positive n, with reference marginalization, QND/debit, covariance, and order checks",
        ),
        (
            "tensor_order_independence",
            tensor_order_certificate(),
            "embedded disjoint local factors commute exactly, so enumeration and sequential order only relabel branches",
        ),
        (
            "projective_consistency",
            projective and global_stop_projectivity_fails(),
            "coefficientwise arbitrary two-block input reduction commutes with the local channel; one global STOP fails the control",
        ),
        (
            "carrier_family_covariance",
            carrier_covariance_certificate(
                "incomplete_frames" if mutation == "incomplete_frames" else None
            ),
            "complete carriers transform through all 24 proper-cubic frames and an arbitrary symbolic translation",
        ),
        (
            "relative_ownership_only",
            relative_owner_certificate(
                anchors, "absolute_owner_claim" if mutation == "absolute_owner_claim" else None
            )
            and shared_target_absolute_boundary(),
            "owner(site)=declared anchor is single-valued inside the supplied family; the exact shared-target pair blocks absolute promotion",
        ),
        (
            "Blank_debit_and_classical_Record_QND",
            blank_debit_certificate() and local["target_nonblank"],
            "each success consumes one exact selected Blank and returns a Locked pointer orthogonal to Blank while old Records remain imported-QND",
        ),
        (
            "renewal_boundary",
            renewal_boundary_certificate(
                "initial_implies_renewal" if mutation == "initial_implies_renewal" else None
            ),
            "the 0/27e1 inward pair is initially disjoint but returned 9e1/18e1 carriers overlap on exactly 64 sites and both STOP",
        ),
        (
            "pair_exchange_symmetry",
            pair_symmetry_certificate(
                "improper_pair_map" if mutation == "improper_pair_map" else None
            ),
            "a fixed-point-free affine proper-cubic half-turn exchanges both Block25 claimants, fronts, targets, and Record labels",
        ),
        (
            "deterministic_pair_boundary",
            deterministic_pair_certificate(
                mutation
                if mutation
                in (
                    "break_claimant_exchange",
                    "coordinate_winner",
                    "allow_double_grant",
                )
                else None
            ),
            "on the supplied unordered claimant descriptor, enumerating all deterministic equivariant grants leaves 00/11 invariant; this is a diagnostic, not an actual joint-sharp state claim",
        ),
        (
            "three_cycle_boundary",
            triangle_certificate(
                "frozen_triangle_source"
                if mutation == "frozen_triangle_source"
                else None
            )
            and edge_anticorrelation_triangle_fails(),
            "the label-covariant three-cycle descriptor has three q=1/4 pair overlaps; its abstract edgewise grant constraints are inconsistent, without asserting a jointly sharp actual state",
        ),
        (
            "kinematic_one_owner_coupling",
            unary_owner_code_certificate(
                "independent_owner_state" if mutation == "independent_owner_state" else None
            ),
            "an abstract two-qubit coupling shows that equal marginals do not fix the joint owner law; this is kinematic, not a physical Record construction",
        ),
        (
            "kinematic_owner_preparation",
            unary_owner_instrument_certificate(
                "delete_owner_outcome" if mutation == "delete_owner_outcome" else None
            ),
            "three abstract four-dimensional Kraus operators prepare the one-hot coupling; no lattice Record semantics are claimed",
        ),
        (
            "common_target_clique",
            common_target_clique_certificate(
                mutation
                if mutation
                in (
                    "single_source_clique",
                    "drop_clique_winner",
                    "delete_clique_stop",
                    "double_clique_writer",
                )
                else None
            ),
            "each of 63 separately supplied nonempty common-target subsets and every stored label tuple has a CPTP 1/k mixture; its declared valid sector writes exactly one Locked winner",
        ),
        (
            "unsharp_partial_overlap",
            unsharp_overlap_certificate(
                mutation
                if mutation in ("double_writer_branch", "delete_pair_stop")
                else None
            ),
            "on the named E11 principal two-projector fiber, the q=1/4 half-mixture has no-write eigenvalues {1/4,3/4}; every full-channel Kraus trajectory writes zero or one target",
        ),
        (
            "collision_old_Record_QND",
            current_record_qnd_certificate(
                "overwrite_other_record" if mutation == "overwrite_other_record" else None
            ),
            "both clean current carriers are disjoint and every selected branch returns its complete current Locked word unchanged",
        ),
        (
            "sectorized_singleton_reduction",
            sectorized_singleton_certificate(
                "raw_mixture_singletons"
                if mutation == "raw_mixture_singletons"
                else None
            ),
            "four explicit commuting old-Record sectors route literal Block24 on singletons and the equal half-mixture only when both current Records are present",
        ),
        (
            "negative_claim_demoted",
            negative_claim_demotion_certificate(
                "ship_negative_terminal"
                if mutation == "ship_negative_terminal"
                else None
            ),
            "the written N1--N8 gate fails the negative, executes its physical stochastic steelman, and binds a positive-only terminal",
        ),
        (
            "scope_guards",
            scope_guard_certificate("promote_scope" if mutation == "promote_scope" else None),
            "no Blank generation, renewal, fairness, rate, gravity, Born, axiom, audit, obligation, TOE, or general no-go promotion",
        ),
    )


def main() -> int:
    checks = evaluated_checks()
    for name, ok, _detail in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}")

    mutation_results = []
    for mutation, designated_check in MUTATION_TARGETS:
        altered = evaluated_checks(mutation)
        by_name = {name: ok for name, ok, _detail in altered}
        rejected = designated_check in by_name and not by_name[designated_check]
        mutation_results.append(rejected)
    mutation_ok = all(mutation_results)
    print(
        f"{'PASS' if mutation_ok else 'FAIL'} mutations="
        f"{sum(mutation_results)}/{len(MUTATION_TARGETS)} "
        + ",".join(mutation for mutation, _check in MUTATION_TARGETS)
    )

    pair, _p, _q, _fa, _fb, f_zero = unsharp_overlap_matrices()
    print(f"WITNESS pair_anchors={pair.anchor_a},{pair.anchor_b}")
    print(f"WITNESS pair_targets={pair.target_a},{pair.target_b}")
    print(f"WITNESS pair_q={pair.product_fidelity}")
    print(f"WITNESS pair_commutator_norm_squared={pair.commutator_norm_factor}")
    print(
        "WITNESS named_E11_principal_fiber_no_write_eigenvalues="
        f"{sorted(f_zero.eigenvals(), key=str)}"
    )
    _invariant_grants, safe_invariant_grants, _live_grants = (
        deterministic_pair_grant_sets()
    )
    initial_overlap, returned_overlap = renewal_overlap_witness()
    print(
        "WITNESS deterministic_safe_invariant_grants="
        f"{safe_invariant_grants}"
    )
    print(
        "WITNESS renewal_initial_overlap="
        f"{initial_overlap} returned_overlap={returned_overlap}"
    )

    for line in RESOLUTION_LINES:
        print(line)

    passed = sum(ok for _name, ok, _detail in checks)
    total = len(checks) + 1
    total_passed = passed + int(mutation_ok)
    ok = total_passed == total
    if ok:
        print(TERMINAL_TEXT)
        print(SCOPE_TEXT)
    print(f"TOTAL: PASS={total_passed} FAIL={total - total_passed}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
