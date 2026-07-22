#!/usr/bin/env python3
"""Cycle578: intrinsic contact-bound moving-transition tournament.

Route A tests exact compact flat-band content in the unmodified Cycle219 walk.
Route B constructs the actual Cycle230 antisymmetric two-CAR contact fibers and
tracks a localized dispersive dimer band.  Route C is conditional: a bounded
carried orientation/tag QCA compiles a recyclable G^2=T_f transport macro.
Candidate phases are wrapped phases, update ordinals are schedules, and none
of the tested weights are physical energy, rates, Records, or probabilities.
"""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

import numpy as np
import scipy.sparse as sparse
import scipy.sparse.linalg as sparse_linalg
import sympy as sym


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22 as c573
import physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22 as c575


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_INTRINSIC_CONTACT_BOUND_MOVING_TRANSITION_TOURNAMENT_"
    "CYCLE578_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
ACCEPTED_CYCLE575_COMMIT = "030138866d6b620ec35639fe6c74b566db5afb28"
CONTACT = 0.37
TOL = 5e-9
EIG_TOL = 3e-10
SIGNAL = 1e-6
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

DEPENDENCY_SHA256 = {
    "common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "physical_held_sparse_order_retirement_cycle563_2026_07_21.py":
        "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
    "physical_enlarged_link_contact_work_tournament_cycle569_2026_07_22.py":
        "c0f06a9cc9ffc4dcfe1d80b94da10bbef81ca1c74fddddac48712b0a7c332ced",
    "physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py":
        "a85daf8fa9b8f3f1b7ef9aed6bfb84fe908ecbe33b2524f8ffebd66471dec20d",
    "physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py":
        "87c751860966e285ca568b545763fa1076a7c9078cb085fed277354c0052810f",
}
RECEIPT_SHA256 = {
    "physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json":
        "350e2c1922379bb42091e1cb5685c9e1f698ed23b81acf7c14803ba5043fcfc1",
    "physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json":
        "c80aae229d3721b273d12188960e2a4b16402d10a982856bec76c465dad52baa",
    "physical_matter_transition_clock_equivalence_tournament_cycle573_receipt_2026_07_22.json":
        "4863e0e32c8298c1539b0d10e274cd14661ed3d8aa895bbe6af697dc9b9d5553",
    "physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_receipt_2026_07_22.json":
        "085c13c96c9b49a47a4a3c910898df806aded075e0d463c768d06424f2911498",
}
CYCLE575_NOTE_SHA256 = "99fd56cb1c6478a50d9ac23661d8a76c7e3fd507c708c2c10024c568d81163bf"


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def current_commit() -> str:
    return subprocess.check_output(
        ("git", "rev-parse", "HEAD"), cwd=ROOT, text=True
    ).strip()


def dependency_controls() -> dict[str, float]:
    observed = {name: file_sha(ROOT / "scripts" / name) for name in DEPENDENCY_SHA256}
    receipt_observed = {name: file_sha(ROOT / "outputs" / name) for name in RECEIPT_SHA256}
    receipts = {
        name: json.loads((ROOT / "outputs" / name).read_text(encoding="utf-8"))
        for name in RECEIPT_SHA256
    }
    ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", ACCEPTED_CYCLE575_COMMIT, "HEAD"),
        cwd=ROOT, check=False,
    ).returncode == 0
    retained = {
        "mass_residual": receipts[
            "physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json"
        ]["physical_M2_scope"]["one_particle_mass_residual"],
        "contact_residual": receipts[
            "physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json"
        ]["physical_M2_scope"]["Cycle230_contact_factorization_residual"],
        "seam_residual": receipts[
            "physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json"
        ]["physical_M2_scope"]["Cycle230_seam_braid_residual"],
    }
    note_hash = file_sha(ROOT / (
        "docs/work_history/repo/review_feedback/"
        "PHYSICAL_AUTONOMOUS_LOCALIZED_REFOCUSED_MATTER_TRANSITION_TOURNAMENT_"
        "CYCLE575_NOTE_2026-07-22.md"
    ))
    check(
        "accepted Cycle575 is an ancestor and every consumed physical shore artifact is byte-exact",
        ancestor and observed == DEPENDENCY_SHA256
        and receipt_observed == RECEIPT_SHA256
        and note_hash == CYCLE575_NOTE_SHA256
        and all(row.get("pass") is True for row in receipts.values())
        and max(retained.values()) < TOL,
        {
            "HEAD": current_commit(), "accepted_Cycle575_commit": ACCEPTED_CYCLE575_COMMIT,
            "ancestor": ancestor, "runners": observed, "receipts": receipt_observed,
            "Cycle575_note_sha256": note_hash, "retained": retained,
        },
    )
    return retained


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset", "cycle 578", "route a",
        "route b", "route c", "actual cycle-230 antisymmetric two-car sector",
        "intrinsic contact-bound dispersive composite band", "g squared equals t sub f",
        "all 24 proper-cubic frames", "all 576 paired frames", "wrapped phase is not energy",
        "update schedule is not time", "no second stable bound band is certified",
        "n1 — normalized alternatives", "n8 — cross-cycle echo",
        "broad localized-matter no-go: fail / do not ship", "there is no axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in body)
    check("the Cycle578 note freezes target, routes, scope, and rhetoric ceiling", not missing, missing)


# ---------------------------------------------------------------------------
# Route A: exact compact-flat-band test of the normalized six-mode walk only.


def normalized_coin_symbolic(b: sym.Symbol) -> sym.Matrix:
    identity = sym.eye(6)
    reverse = sym.zeros(6)
    for first, second in enumerate((1, 0, 3, 2, 5, 4)):
        reverse[first, second] = 1
    scalar = sym.ones(6) / 6
    return 2 * scalar + (b - 1) * identity / 2 - (1 + b) * reverse / 2


def route_a_controls() -> dict[str, object]:
    print("\nROUTE A — UNMODIFIED MASSIVE FLAT-BAND/EIGENPHASE-PAIR TEST")
    x, y, z, b = sym.symbols("x y z b", nonzero=True)
    coin = normalized_coin_symbolic(b)
    stream = sym.diag(x, 1 / x, y, 1 / y, z, 1 / z)
    identity = sym.eye(6)
    plus = (
        3*x**2*y**2*z**2 + 2*x**2*y**2*z + 3*x**2*y**2
        + 2*x**2*y*z**2 - 4*x**2*y*z + 2*x**2*y + 3*x**2*z**2
        + 2*x**2*z + 3*x**2 + 2*x*y**2*z**2 - 4*x*y**2*z
        + 2*x*y**2 - 4*x*y*z**2 - 24*x*y*z - 4*x*y + 2*x*z**2
        - 4*x*z + 2*x + 3*y**2*z**2 + 2*y**2*z + 3*y**2
        + 2*y*z**2 - 4*y*z + 2*y + 3*z**2 + 2*z + 3
    )
    minus = (
        3*x**2*y**2*z**2 - 2*x**2*y**2*z + 3*x**2*y**2
        - 2*x**2*y*z**2 - 4*x**2*y*z - 2*x**2*y + 3*x**2*z**2
        - 2*x**2*z + 3*x**2 - 2*x*y**2*z**2 - 4*x*y**2*z
        - 2*x*y**2 - 4*x*y*z**2 + 24*x*y*z - 4*x*y - 2*x*z**2
        - 4*x*z - 2*x + 3*y**2*z**2 - 2*y**2*z + 3*y**2
        - 2*y*z**2 - 4*y*z - 2*y + 3*z**2 - 2*z + 3
    )
    expected = {
        "1": -(b - 1)**2 * (b + 1) * plus / (24*x*y*z),
        "-1": (b - 1)**2 * (b + 1) * minus / (24*x*y*z),
        "b": -b**3 * (b - 1)**2 * (b + 1)
             * (x - 1)**2 * (y - 1)**2 * (z - 1)**2 / (8*x*y*z),
    }
    actual = {
        "1": sym.factor((stream @ coin - identity).det()),
        "-1": sym.factor((stream @ coin + identity).det()),
        "b": sym.factor((stream @ coin - b * identity).det()),
    }
    exact_factor_residuals = {
        key: sym.simplify(actual[key] - expected[key]) for key in expected
    }
    witness = {x: sym.Integer(2), y: sym.Integer(3), z: sym.Integer(5), b: sym.Integer(7)}
    nonzero_witnesses = {key: sym.factor(value.subs(witness)) for key, value in actual.items()}
    k0_spectrum = coin.subs(b, sym.Integer(7)).eigenvals()

    box_rows = []
    for length, beta, held in (
        (5, -0.2, False), (7, -0.3, False),
        (9, -0.35, True), (11, -0.41, True),
    ):
        normalized_coin = np.asarray(
            c219.common_species(beta).coin
            / np.exp(-1j * np.tan(beta / 2)), dtype=complex
        )
        candidate = (1 + 0j, -1 + 0j, np.exp(1j * beta))
        witness_k = 2 * np.pi * np.asarray((1, 2, 3), dtype=float) / length
        diagonal = np.diag(np.exp(-1j * (c210.DIRECTIONS @ witness_k)))
        walk = diagonal @ normalized_coin
        singular = tuple(
            float(np.linalg.svd(walk - value * np.eye(6), compute_uv=False)[-1])
            for value in candidate
        )
        values = np.linalg.eigvals(walk)
        antipodal_mismatch = min(
            abs(first + second) for first in values for second in values
        )
        box_rows.append({
            "length": length, "beta": beta, "held": held,
            "generic_3D_momentum": witness_k.tolist(),
            "candidate_minimum_singular_values": singular,
            "minimum_antipodal_eigenvalue_mismatch": float(antipodal_mismatch),
        })

    exact = all(value == 0 for value in exact_factor_residuals.values())
    nonzero = all(value != 0 for value in nonzero_witnesses.values())
    finite_signal = min(
        min(row["candidate_minimum_singular_values"]) for row in box_rows
    )
    antipodal_signal = min(row["minimum_antipodal_eigenvalue_mismatch"] for row in box_rows)
    check(
        "the normalized massive Cycle219 walk has exact nonzero generic-momentum determinant factors at its three k=0 candidates; Route A constructs no compact pair and withholds an absence/no-go conclusion at N1",
        exact and nonzero and k0_spectrum == {sym.Integer(1): 1, sym.Integer(-1): 2, sym.Integer(7): 3}
        and finite_signal > SIGNAL and antipodal_signal > SIGNAL,
        {
            "candidate_k0_spectrum_multiplicity": {str(key): value for key, value in k0_spectrum.items()},
            "exact_symbolic_factor_residuals": {key: str(value) for key, value in exact_factor_residuals.items()},
            "nonzero_polynomial_witnesses": {key: str(value) for key, value in nonzero_witnesses.items()},
            "finite_box_rows": box_rows,
            "narrow_scope": "algebraic partial for the normalized unmodified massive six-mode one-particle walk; an absence/no-go inference is not shipped",
        },
    )
    return {
        "exact_factorization": exact, "nonzero_witnesses": nonzero,
        "finite_box_rows": box_rows, "minimum_flat_candidate_signal": finite_signal,
        "minimum_antipodal_signal": antipodal_signal,
        "compact_flat_pair_constructed": False,
        "absence_or_no_go_claim_shipped": False,
    }


# ---------------------------------------------------------------------------
# Route B: actual Cycle230 two-CAR contact sector in total-momentum fibers.


def signed_coordinate(value: int, length: int) -> int:
    return value if value <= length // 2 else value - length


def site_tuple(site: int, length: int) -> tuple[int, int, int]:
    return site // (length * length), (site // length) % length, site % length


def site_flat(site: tuple[int, int, int], length: int) -> int:
    return (site[0] * length + site[1]) * length + site[2]


@lru_cache(maxsize=None)
def antisymmetric_quotient(length: int) -> tuple[sparse.csr_matrix, np.ndarray, np.ndarray, np.ndarray]:
    if length < 3 or length % 2 == 0:
        raise ValueError("relative CAR boxes must be odd with L>=3")
    sites = length**3
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    seen: set[int] = set()
    representatives = 0
    radius2 = np.zeros(36 * sites)
    contact = np.zeros(36 * sites)
    boundary = np.zeros(36 * sites)
    for site in range(sites):
        coordinate = site_tuple(site, length)
        signed = tuple(signed_coordinate(value, length) for value in coordinate)
        radius2[site*36:(site+1)*36] = sum(value*value for value in signed)
        contact[site*36:(site+1)*36] = float(site == 0)
        boundary[site*36:(site+1)*36] = float(any(abs(value) == length // 2 for value in signed))
        negative = site_flat(tuple((-value) % length for value in coordinate), length)
        for first in range(6):
            for second in range(6):
                left = (site * 6 + first) * 6 + second
                right = (negative * 6 + second) * 6 + first
                if left in seen:
                    continue
                seen.add(left)
                seen.add(right)
                if left == right:
                    continue
                rows.extend((left, right))
                cols.extend((representatives, representatives))
                data.extend((2**-0.5, -2**-0.5))
                representatives += 1
    quotient = sparse.coo_matrix(
        (data, (rows, cols)), shape=(36 * sites, representatives)
    ).tocsr()
    return quotient, radius2, contact, boundary


def relative_car_full_walk(length: int, beta: float, coupling: float,
                           momentum: tuple[float, float, float]) -> sparse.csr_matrix:
    sites = length**3
    coin = c219.common_species(beta).coin
    onsite = sparse.kron(
        sparse.eye(sites, format="csr"), sparse.csr_matrix(np.kron(coin, coin)),
        format="csr",
    )
    rows = np.arange(36 * sites, dtype=int)
    cols = np.empty(36 * sites, dtype=int)
    data = np.empty(36 * sites, dtype=complex)
    vector_k = np.asarray(momentum, dtype=float)
    for site in range(sites):
        coordinate = site_tuple(site, length)
        for first, velocity_first in enumerate(c210.DIRECTIONS):
            for second, velocity_second in enumerate(c210.DIRECTIONS):
                source = (site * 6 + first) * 6 + second
                displacement = velocity_first - velocity_second
                target_coordinate = tuple(
                    int((coordinate[axis] + displacement[axis]) % length)
                    for axis in range(3)
                )
                target_site = site_flat(target_coordinate, length)
                target = (target_site * 6 + first) * 6 + second
                cols[target] = source
                data[target] = np.exp(
                    -0.5j * np.dot(vector_k, velocity_first + velocity_second)
                )
    stream = sparse.csr_matrix(
        (data, (rows, cols)), shape=(36 * sites, 36 * sites)
    )
    phases = np.ones(36 * sites, dtype=complex)
    phases[:36] = np.exp(1j * coupling)
    return (sparse.diags(phases) @ stream @ onsite).tocsr()


def relative_car_walk(length: int, beta: float, coupling: float,
                      momentum: tuple[float, float, float]) -> sparse.csr_matrix:
    quotient, _radius2, _contact, _boundary = antisymmetric_quotient(length)
    full = relative_car_full_walk(length, beta, coupling, momentum)
    return (quotient.conj().T @ full @ quotient).tocsr()


def relative_observables(length: int, vector: np.ndarray) -> dict[str, float]:
    quotient, radius2, contact, boundary = antisymmetric_quotient(length)
    full = quotient @ vector
    probability = np.abs(full)**2
    return {
        "contact_weight": float(probability @ contact),
        "relative_radius_squared": float(probability @ radius2),
        "seam_boundary_weight": float(probability @ boundary),
    }


def isolated_eigenpair(length: int, beta: float, coupling: float,
                       momentum: tuple[float, float, float], target_phase: float,
                       prior: np.ndarray | None = None,
                       eigen_count: int = 8) -> tuple[complex, np.ndarray, dict[str, float]]:
    walk = relative_car_walk(length, beta, coupling, momentum)
    seed = np.exp(0.173j * np.arange(walk.shape[0], dtype=float))
    seed /= np.linalg.norm(seed)
    values, vectors = sparse_linalg.eigs(
        walk, k=eigen_count, sigma=0.999 * np.exp(1j * target_phase),
        v0=seed, tol=2e-11, maxiter=5000,
    )
    candidates = []
    for index, value in enumerate(values):
        vector = vectors[:, index] / np.linalg.norm(vectors[:, index])
        observables = relative_observables(length, vector)
        observables["prior_overlap"] = (
            0.0 if prior is None else float(abs(np.vdot(prior, vector)))
        )
        observables["eigen_residual"] = float(np.linalg.norm(walk @ vector - value * vector))
        observables["unit_circle_residual"] = float(abs(abs(value) - 1))
        candidates.append((value, vector, observables))
    if prior is None:
        selected = max(candidates, key=lambda row: row[2]["contact_weight"])
        value, vector, observables = selected
        pivot = int(np.argmax(np.abs(vector)))
        vector = vector * np.exp(-1j * np.angle(vector[pivot]))
        observables["parallel_transport_gauge_residual"] = 0.0
        return value, vector, observables
    value, vector, observables = max(
        candidates, key=lambda row: row[2]["prior_overlap"]
    )
    overlap = np.vdot(prior, vector)
    vector = vector * np.exp(-1j * np.angle(overlap))
    aligned_overlap = np.vdot(prior, vector)
    observables["prior_overlap"] = float(abs(aligned_overlap))
    observables["parallel_transport_gauge_residual"] = float(
        abs(aligned_overlap.imag) + max(0.0, -aligned_overlap.real)
    )
    return value, vector, observables


def exchange_residual(full: np.ndarray, length: int) -> float:
    tensor = full.reshape(length, length, length, 6, 6)
    exchanged = np.zeros_like(tensor)
    for site in range(length**3):
        coordinate = site_tuple(site, length)
        negative = tuple((-value) % length for value in coordinate)
        exchanged[coordinate] = tensor[negative].T
    return float(np.linalg.norm(exchanged.reshape(-1) + full))


def full_frame_representation(length: int, frame: np.ndarray) -> sparse.csr_matrix:
    sites = length**3
    direction_rep = c210.direction_permutation(frame)
    direction_target = np.argmax(direction_rep, axis=0)
    rows = np.empty(36 * sites, dtype=int)
    cols = np.arange(36 * sites, dtype=int)
    for site in range(sites):
        coordinate = np.asarray(site_tuple(site, length), dtype=int)
        target_coordinate = tuple(int(value % length) for value in frame @ coordinate)
        target_site = site_flat(target_coordinate, length)
        for first in range(6):
            for second in range(6):
                source = (site * 6 + first) * 6 + second
                rows[source] = (target_site * 6 + int(direction_target[first])) * 6 + int(direction_target[second])
    return sparse.csr_matrix(
        (np.ones(36 * sites), (rows, cols)), shape=(36 * sites, 36 * sites)
    )


def circular_center(probability: np.ndarray) -> complex:
    positions = np.arange(probability.size)
    return complex(np.sum(probability * np.exp(2j * np.pi * positions / probability.size)))


def route_b_controls() -> dict[str, object]:
    print("\nROUTE B — ACTUAL CYCLE230 CONTACT-BOUND DISPERSIVE DIMER")
    size_rows = []
    primary_pairs: dict[int, tuple[complex, np.ndarray]] = {}
    for length, held in ((5, False), (7, False), (9, False), (11, True)):
        value, vector, obs = isolated_eigenpair(
            length, -0.3, CONTACT, (0.0, 0.0, 0.0), -2.975575
        )
        primary_pairs[length] = (value, vector)
        row = {
            "length": length, "held": held, "beta": -0.3, "coupling": CONTACT,
            "phase": float(np.angle(value)), **obs,
        }
        size_rows.append(row)

    source_rows = []
    for coupling, target, held in ((0.31, -2.991, False), (0.43, -2.960, True)):
        value, vector, obs = isolated_eigenpair(
            7, -0.3, coupling, (0.0, 0.0, 0.0), target
        )
        source_rows.append({
            "length": 7, "held": held, "beta": -0.3, "coupling": coupling,
            "phase": float(np.angle(value)), **obs,
        })

    # Frozen K-grid on held L11.  Tracking is by adjacent-vector overlap.
    cm_length = 128
    momentum_indices = tuple(range(5))
    band_rows = []
    band_vectors = []
    prior = None
    target = -2.975575
    for momentum_index in momentum_indices:
        momentum_x = 2 * np.pi * momentum_index / cm_length
        value, vector, obs = isolated_eigenpair(
            11, -0.3, CONTACT, (momentum_x, 0.0, 0.0), target, prior
        )
        target = float(np.angle(value))
        prior = vector
        band_vectors.append(vector)
        band_rows.append({
            "momentum_index": momentum_index, "momentum_x": momentum_x,
            "phase": target, **obs,
        })

    phases = np.unwrap(np.asarray([row["phase"] for row in band_rows]))
    momenta = np.asarray([row["momentum_x"] for row in band_rows])
    maximum_band_seam_weight = max(
        row["seam_boundary_weight"] for row in band_rows
    )
    frozen_band_seam_tail_threshold = 1e-2
    finite_difference_velocity = -float((phases[3] - phases[1]) / (momenta[3] - momenta[1]))
    coefficients = np.exp(-((np.asarray(momentum_indices) - 2.0) / 1.05)**2 / 2).astype(complex)
    coefficients /= np.linalg.norm(coefficients)
    fourier = np.exp(2j * np.pi * np.outer(np.arange(cm_length), momentum_indices) / cm_length)
    vector_stack = np.asarray(band_vectors)
    packet = np.einsum("n,rn,nq->rq", coefficients, fourier, vector_stack, optimize=True) / np.sqrt(cm_length)
    eigenvalues = np.exp(1j * phases)
    packet_after = np.einsum(
        "n,rn,nq->rq", coefficients * eigenvalues, fourier, vector_stack, optimize=True
    ) / np.sqrt(cm_length)
    packet_flat = np.einsum(
        "n,rn,nq->rq", coefficients * np.exp(1j * phases[2]), fourier, vector_stack,
        optimize=True,
    ) / np.sqrt(cm_length)
    probability = np.sum(np.abs(packet)**2, axis=1)
    probability_after = np.sum(np.abs(packet_after)**2, axis=1)
    probability_flat = np.sum(np.abs(packet_flat)**2, axis=1)
    center = circular_center(probability)
    center_after = circular_center(probability_after)
    center_flat = circular_center(probability_flat)
    center_resultant = abs(center)
    center_after_resultant = abs(center_after)
    center_flat_resultant = abs(center_flat)
    packet_displacement = float(np.angle(center_after / center) * cm_length / (2 * np.pi))
    flat_displacement = float(np.angle(center_flat / center) * cm_length / (2 * np.pi))
    spectral_packet_displacement_residual = abs(
        finite_difference_velocity - packet_displacement
    )
    spectral_packet_tolerance = 5e-4
    packet_norm_residual = max(
        abs(float(np.linalg.norm(packet)) - 1),
        abs(float(np.linalg.norm(packet_after)) - 1),
    )

    # Exact CAR-fiber eigen/inverse, contact deletion, antisymmetric leakage,
    # and domain controls.  This is not a new physical-M2 embedding square.
    held_value, held_vector = primary_pairs[11]
    held_walk = relative_car_walk(11, -0.3, CONTACT, (0.0, 0.0, 0.0))
    held_deleted = relative_car_walk(11, -0.3, 0.0, (0.0, 0.0, 0.0))
    held_full_walk = relative_car_full_walk(11, -0.3, CONTACT, (0.0, 0.0, 0.0))
    eg_residual = float(np.linalg.norm(held_walk @ held_vector - held_value * held_vector))
    inverse_residual = float(np.linalg.norm(held_walk.conj().T @ (held_walk @ held_vector) - held_vector))
    contact_deletion_signal = float(np.linalg.norm((held_walk - held_deleted) @ held_vector))
    quotient, _r2, _contact, _boundary = antisymmetric_quotient(11)
    full_held = quotient @ held_vector
    full_updated = held_full_walk @ full_held
    antisymmetric_projection_leakage = float(
        np.linalg.norm(full_updated - quotient @ (quotient.conj().T @ full_updated))
    )
    antisymmetric_exchange_residual = exchange_residual(full_updated, 11)
    rng_car = np.random.default_rng(5781)
    lawful_random = rng_car.normal(size=quotient.shape[1]) + 1j * rng_car.normal(
        size=quotient.shape[1]
    )
    lawful_random /= np.linalg.norm(lawful_random)
    random_updated = held_full_walk @ (quotient @ lawful_random)
    random_projection_leakage = float(
        np.linalg.norm(random_updated - quotient @ (quotient.conj().T @ random_updated))
    )
    random_exchange_residual = exchange_residual(random_updated, 11)
    antisymmetric_leakage = max(
        antisymmetric_projection_leakage, antisymmetric_exchange_residual,
        random_projection_leakage, random_exchange_residual,
    )
    deleted_full = full_held.copy()
    deletion_index = int(np.argmax(np.abs(deleted_full)))
    deleted_full[deletion_index] = 0
    exchange_partner_deletion_leakage = float(
        np.linalg.norm(deleted_full - quotient @ (quotient.conj().T @ deleted_full))
    )
    malformed_rejected = False
    try:
        antisymmetric_quotient(4)
    except ValueError:
        malformed_rejected = True

    # All24 covariance on a manageable exact L5 fiber and all576 invariant pairs.
    frames = c210.proper_cubic_frames()
    base_value, base_vector = primary_pairs[5]
    quotient5, radius5, contact5, _boundary5 = antisymmetric_quotient(5)
    base_k = np.asarray((2 * np.pi / 31, 0.0, 0.0))
    base_value_k, base_vector_k, _base_obs_k = isolated_eigenpair(
        5, -0.3, CONTACT, tuple(base_k), -2.974
    )
    covariance_rows = []
    for frame in frames:
        full_rep = full_frame_representation(5, frame)
        quotient_rep = quotient5.conj().T @ full_rep @ quotient5
        rotated = quotient_rep @ base_vector_k
        rotated_k = tuple(float(value) for value in frame @ base_k)
        rotated_walk = relative_car_walk(5, -0.3, CONTACT, rotated_k)
        full_rotated = quotient5 @ rotated
        probability_rotated = np.abs(full_rotated)**2
        covariance_rows.append({
            "eigen_residual": float(np.linalg.norm(rotated_walk @ rotated - base_value_k * rotated)),
            "norm_residual": abs(float(np.linalg.norm(rotated)) - 1),
            "contact_weight": float(probability_rotated @ contact5),
            "relative_radius_squared": float(probability_rotated @ radius5),
        })
    paired_failures = 0
    paired_maximum = 0.0
    for left in covariance_rows:
        for right in covariance_rows:
            residual = max(
                abs(left["contact_weight"] - right["contact_weight"]),
                abs(left["relative_radius_squared"] - right["relative_radius_squared"]),
            )
            paired_maximum = max(paired_maximum, residual)
            paired_failures += int(residual >= TOL)

    # A deliberately frozen second spectral window: non-certification, not a no-go.
    second_rows = []
    for length in (5, 7, 11):
        value, _vector, obs = isolated_eigenpair(
            length, -0.3, CONTACT, (0.0, 0.0, 0.0), -3.03, eigen_count=10
        )
        second_rows.append({
            "length": length, "phase": float(np.angle(value)), **obs,
        })
    second_band_certified = (
        min(row["contact_weight"] for row in second_rows) > 0.15
        and max(row["relative_radius_squared"] for row in second_rows) < 8
    )

    maximum_eigen_residual = max(
        row["eigen_residual"] for row in size_rows + source_rows + band_rows + second_rows
    )
    minimum_contact = min(row["contact_weight"] for row in size_rows)
    maximum_radius = max(row["relative_radius_squared"] for row in size_rows)
    minimum_overlap = min(row["prior_overlap"] for row in band_rows[1:])
    maximum_gauge_residual = max(
        row["parallel_transport_gauge_residual"] for row in band_rows
    )
    maximum_covariance = max(
        max(row["eigen_residual"], row["norm_residual"]) for row in covariance_rows
    )
    check(
        "the actual Cycle230 antisymmetric contact sector gives strong finite-box evidence for a localized dispersive dimer with a gauge-fixed nonzero-K packet, CAR-fiber inverse/leakage controls, and a separately pinned physical-M2 shore",
        maximum_eigen_residual < EIG_TOL and minimum_contact > 0.25
        and maximum_radius < 2.1 and size_rows[-1]["seam_boundary_weight"] < 3e-3
        and minimum_overlap > 0.99 and maximum_gauge_residual < TOL
        and maximum_band_seam_weight <= frozen_band_seam_tail_threshold
        and abs(finite_difference_velocity) > SIGNAL
        and abs(packet_displacement) > SIGNAL and abs(flat_displacement) < TOL
        and spectral_packet_displacement_residual < spectral_packet_tolerance
        and min(center_resultant, center_after_resultant, center_flat_resultant) > 0.5
        and packet_norm_residual < TOL and eg_residual < EIG_TOL
        and inverse_residual < TOL and contact_deletion_signal > SIGNAL
        and antisymmetric_leakage < TOL
        and exchange_partner_deletion_leakage > SIGNAL and malformed_rejected
        and len(frames) == 24 and len(frames)**2 == 576
        and maximum_covariance < EIG_TOL and paired_failures == 0
        and not second_band_certified,
        {
            "size_rows": size_rows, "coupling_source_rows": source_rows,
            "held_L11_band_rows": band_rows,
            "maximum_held_L11_K_grid_seam_weight": maximum_band_seam_weight,
            "frozen_held_L11_K_grid_seam_tail_threshold": frozen_band_seam_tail_threshold,
            "K_fibers_are_periodic_relative_coordinate_truncations_not_full_finite_torus_decompositions": True,
            "finite_difference_group_displacement_per_update": finite_difference_velocity,
            "band_packet_one_update_displacement": packet_displacement,
            "spectral_packet_displacement_residual": spectral_packet_displacement_residual,
            "frozen_five_mode_discretization_tolerance": spectral_packet_tolerance,
            "flat_phase_packet_displacement_control": flat_displacement,
            "packet_circular_resultant_before": center_resultant,
            "packet_circular_resultant_after": center_after_resultant,
            "flat_control_circular_resultant": center_flat_resultant,
            "band_packet_norm_residual": packet_norm_residual,
            "maximum_parallel_transport_gauge_residual": maximum_gauge_residual,
            "EG_residual": eg_residual, "inverse_residual": inverse_residual,
            "CAR_fiber_not_new_physical_M2_compiler": True,
            "physical_M2_update_fixtures_inherited_and_pinned": True,
            "contact_gate_deletion_signal": contact_deletion_signal,
            "antisymmetric_projection_leakage": antisymmetric_projection_leakage,
            "antisymmetric_exchange_residual": antisymmetric_exchange_residual,
            "random_lawful_projection_leakage": random_projection_leakage,
            "random_lawful_exchange_residual": random_exchange_residual,
            "exchange_partner_deletion_leakage": exchange_partner_deletion_leakage,
            "all24_maximum_covariance_residual": maximum_covariance,
            "all576_maximum_invariant_residual": paired_maximum,
            "all576_failures": paired_failures,
            "second_window_rows": second_rows,
            "second_stable_bound_band_certified": second_band_certified,
            "internal_beat_transition_closed": False,
        },
    )
    return {
        "size_rows": size_rows, "coupling_source_rows": source_rows,
        "band_rows": band_rows,
        "maximum_held_L11_K_grid_seam_weight": maximum_band_seam_weight,
        "frozen_held_L11_K_grid_seam_tail_threshold": frozen_band_seam_tail_threshold,
        "K_fibers_are_periodic_relative_coordinate_truncations_not_full_finite_torus_decompositions": True,
        "finite_difference_group_displacement_per_update": finite_difference_velocity,
        "band_packet_one_update_displacement": packet_displacement,
        "spectral_packet_displacement_residual": spectral_packet_displacement_residual,
        "frozen_five_mode_discretization_tolerance": spectral_packet_tolerance,
        "packet_circular_resultant_before": center_resultant,
        "packet_circular_resultant_after": center_after_resultant,
        "maximum_parallel_transport_gauge_residual": maximum_gauge_residual,
        "maximum_eigen_residual": maximum_eigen_residual,
        "contact_gate_deletion_signal": contact_deletion_signal,
        "exchange_partner_deletion_leakage": exchange_partner_deletion_leakage,
        "all24_maximum_covariance_residual": maximum_covariance,
        "all576_maximum_invariant_residual": paired_maximum,
        "all576_failures": paired_failures,
        "second_window_rows": second_rows,
        "second_stable_bound_band_certified": second_band_certified,
        "internal_beat_transition_closed": False,
        "finite_contact_bound_band_evidence_passed": True,
        "infinite_volume_bound_band_theorem_closed": False,
        "physical_M2_bound_state_embedding_closed": False,
    }


# ---------------------------------------------------------------------------
# Route C: conditional supplied recyclable local transport controller.


def spatial_stream(state: np.ndarray, *, inverse: bool = False) -> np.ndarray:
    if state.ndim < 4 or state.shape[3] != 6:
        raise ValueError("matter direction must be the fourth axis")
    output = np.zeros_like(state)
    for direction, displacement in enumerate(c210.DIRECTIONS):
        shift = tuple(int((-1 if inverse else 1) * value) for value in displacement)
        output[..., direction, *([slice(None)] * (state.ndim - 4))] = np.roll(
            state[..., direction, *([slice(None)] * (state.ndim - 4))],
            shift, axis=(0, 1, 2),
        )
    return output


def matter_collision(state: np.ndarray, beta: float, contact: float,
                     *, inverse: bool = False) -> np.ndarray:
    matrix = np.exp(1j * contact) * c219.common_species(beta).coin
    if inverse:
        matrix = matrix.conj().T
    return np.einsum("ab,xyzb...->xyza...", matrix, state, optimize=True)


def accepted_forward_step(state: np.ndarray, beta: float, contact: float) -> np.ndarray:
    return spatial_stream(matter_collision(state, beta, contact))


def locally_compiled_inverse_step(state: np.ndarray, beta: float, contact: float,
                                  *, delete_second_reversal: bool = False) -> np.ndarray:
    reversed_input = np.einsum("ab,xyzb...->xyza...", c210.REVERSE, state, optimize=True)
    forward_streamed = spatial_stream(reversed_input)
    unstreamed = forward_streamed if delete_second_reversal else np.einsum(
        "ab,xyzb...->xyza...", c210.REVERSE, forward_streamed, optimize=True
    )
    return matter_collision(unstreamed, beta, contact, inverse=True)


def carriage_stream(state: np.ndarray, *, inverse: bool = False) -> np.ndarray:
    if state.ndim != 5 or state.shape[3:] != (6, 6):
        raise ValueError("carriage state must have six matter and six orientation rails")
    output = np.zeros_like(state)
    for orientation, displacement in enumerate(c210.DIRECTIONS):
        shift = tuple(int((-1 if inverse else 1) * value) for value in displacement)
        output[..., orientation] = np.roll(
            state[..., orientation], shift, axis=(0, 1, 2)
        )
    return output


def controller_initial(matter: np.ndarray, orientation: int) -> np.ndarray:
    if matter.ndim != 4 or matter.shape[3] != 6 or orientation not in range(6):
        raise ValueError("lawful controller input needs six matter rails and one of six orientations")
    output = np.zeros(matter.shape + (6, 2), dtype=complex)
    output[..., orientation, 0] = matter
    return output


def controller_layer(state: np.ndarray, beta: float, contact: float,
                     *, delete_carriage: bool = False,
                     delete_inverse_branch: bool = False,
                     delete_second_reversal: bool = False) -> np.ndarray:
    if state.ndim != 6 or state.shape[3:] != (6, 6, 2):
        raise ValueError("controller state leaves the 6x6x2 local rail code")
    output = np.zeros_like(state)
    output[..., 1] = accepted_forward_step(state[..., 0], beta, contact)
    if delete_inverse_branch:
        reverse_branch = accepted_forward_step(state[..., 1], beta, contact)
    else:
        reverse_branch = locally_compiled_inverse_step(
            state[..., 1], beta, contact,
            delete_second_reversal=delete_second_reversal,
        )
    output[..., 0] = reverse_branch if delete_carriage else carriage_stream(reverse_branch)
    return output


def controller_inverse_layer(state: np.ndarray, beta: float, contact: float) -> np.ndarray:
    if state.ndim != 6 or state.shape[3:] != (6, 6, 2):
        raise ValueError("controller state leaves the 6x6x2 local rail code")
    output = np.zeros_like(state)
    output[..., 0] = locally_compiled_inverse_step(state[..., 1], beta, contact)
    output[..., 1] = accepted_forward_step(
        carriage_stream(state[..., 0], inverse=True), beta, contact
    )
    return output


def controller_macro(state: np.ndarray, beta: float, contact: float, **kwargs: object) -> np.ndarray:
    return controller_layer(controller_layer(state, beta, contact, **kwargs), beta, contact, **kwargs)


def route_c_controls() -> dict[str, object]:
    print("\nROUTE C — CONDITIONAL RECYCLABLE G^2=T_f TRANSPORT CONTROLLER")
    frames = c210.proper_cubic_frames()
    fixtures = (
        (5, 1.2, -0.2, 0.0, frames[0], 0, False),
        (7, 1.7, -0.3, CONTACT, frames[8], 2, False),
        (9, 2.0, -0.35, -0.23, frames[17], 4, True),
        (9, 2.2, -0.41, 0.51, frames[22], 1, True),
    )
    rows = []
    for length, width, beta, contact, frame, orientation, held in fixtures:
        matter = c575.gaussian_state(length, width, frame)
        initial = controller_initial(matter, orientation)
        after_one = controller_layer(initial, beta, contact)
        after_macro = controller_layer(after_one, beta, contact)
        expected = np.zeros_like(initial)
        expected[..., 0] = carriage_stream(initial[..., 0])
        restored = controller_inverse_layer(
            controller_inverse_layer(after_macro, beta, contact), beta, contact
        )
        retained_forward = c573.bound_pair_step(matter, beta, contact)
        rows.append({
            "length": length, "width": width, "beta": beta,
            "contact_source": contact, "held": held,
            "EG_macro_residual": float(np.linalg.norm(after_macro - expected)),
            "inverse_residual": float(np.linalg.norm(restored - initial)),
            "forward_fixture_residual": float(
                np.linalg.norm(after_one[..., orientation, 1] - retained_forward)
            ),
            "norm_residual": max(
                abs(float(np.linalg.norm(after_one)) - 1),
                abs(float(np.linalg.norm(after_macro)) - 1),
            ),
            "tag_boundary_leakage": float(np.linalg.norm(after_macro[..., 1])),
        })

    covariance_maximum = 0.0
    paired_failures = 0
    for matter_frame in frames:
        matter = c575.gaussian_state(5, 1.25, matter_frame)
        transition_weight = c575.tagged_transition_weight(
            c575.tagged_initial(matter), -0.3, CONTACT, matter_frame
        )
        for carriage_frame in frames:
            direction_rep = c210.direction_permutation(carriage_frame)
            orientation = int(np.argmax(direction_rep[:, 0]))
            initial = controller_initial(matter, orientation)
            actual = controller_macro(initial, -0.3, CONTACT)
            expected = np.zeros_like(initial)
            expected[..., 0] = carriage_stream(initial[..., 0])
            residual = max(
                float(np.linalg.norm(actual - expected)), abs(transition_weight - 1)
            )
            covariance_maximum = max(covariance_maximum, residual)
            paired_failures += int(residual >= TOL)

    rng = np.random.default_rng(578)
    arbitrary = rng.normal(size=(5, 5, 5, 6, 6, 2)) + 1j * rng.normal(
        size=(5, 5, 5, 6, 6, 2)
    )
    arbitrary /= np.linalg.norm(arbitrary)
    arbitrary_once = controller_layer(arbitrary, -0.3, CONTACT)
    arbitrary_restored = controller_inverse_layer(arbitrary_once, -0.3, CONTACT)
    full_domain_inverse = float(np.linalg.norm(arbitrary_restored - arbitrary))
    full_domain_norm = abs(float(np.linalg.norm(arbitrary_once)) - 1)

    held_matter = c575.gaussian_state(9, 2.0, frames[17])
    held_initial = controller_initial(held_matter, 4)
    baseline = controller_macro(held_initial, -0.35, -0.23)
    no_carriage = controller_macro(
        held_initial, -0.35, -0.23, delete_carriage=True
    )
    no_inverse = controller_macro(
        held_initial, -0.35, -0.23, delete_inverse_branch=True
    )
    carriage_deletion_signal = float(np.linalg.norm(baseline - no_carriage))
    inverse_deletion_signal = float(np.linalg.norm(baseline - no_inverse))
    generic_envelope = np.linalg.norm(held_matter, axis=-1).astype(complex)
    generic_matter = generic_envelope[..., None] * np.eye(6, dtype=complex)[0]
    generic_initial = controller_initial(generic_matter, 4)
    generic_baseline = controller_macro(generic_initial, -0.35, -0.23)
    generic_no_reversal = controller_macro(
        generic_initial, -0.35, -0.23, delete_second_reversal=True
    )
    reversal_deletion_signal = float(
        np.linalg.norm(generic_baseline - generic_no_reversal)
    )
    orientation_superposition = (
        controller_initial(held_matter, 0) + controller_initial(held_matter, 2)
    ) / np.sqrt(2)
    orientation_deleted = orientation_superposition.copy()
    orientation_deleted[..., 2, :] = 0
    orientation_rail_deletion_leakage = abs(
        float(np.linalg.norm(orientation_deleted)) - 1
    )
    malformed_rejected = False
    try:
        controller_layer(np.zeros((5, 5, 5, 6, 5, 2)), -0.3, CONTACT)
    except ValueError:
        malformed_rejected = True

    maximum = max(
        row[key] for row in rows for key in (
            "EG_macro_residual", "inverse_residual", "forward_fixture_residual",
            "norm_residual", "tag_boundary_leakage",
        )
    )
    check(
        "a supplied 72-M2 carried orientation/tag law locally compiles a recyclable G-squared-equals-T-f macro with net transport, all24 covariance, all576 paired macro receipts, inverse, deletion, and lawful-domain controls",
        maximum < TOL and covariance_maximum < TOL and paired_failures == 0
        and full_domain_inverse < TOL and full_domain_norm < TOL
        and carriage_deletion_signal > SIGNAL and inverse_deletion_signal > SIGNAL
        and reversal_deletion_signal > SIGNAL and orientation_rail_deletion_leakage > SIGNAL
        and malformed_rejected,
        {
            "rows": rows, "proper_cubic_frames": len(frames),
            "paired_matter_carriage_frames": len(frames)**2,
            "paired_failures": paired_failures,
            "maximum_residual": maximum,
            "maximum_covariance_residual": covariance_maximum,
            "arbitrary_full_domain_inverse_residual": full_domain_inverse,
            "arbitrary_full_domain_norm_residual": full_domain_norm,
            "carriage_deletion_signal": carriage_deletion_signal,
            "inverse_branch_deletion_signal": inverse_deletion_signal,
            "second_reversal_deletion_signal": reversal_deletion_signal,
            "orientation_rail_deletion_leakage": orientation_rail_deletion_leakage,
            "M2_rail_identities_per_cell": 72,
            "global_single_particle_sector_input": True,
            "local_occupancy_constraint": "zero or one occupied rail per site within the declared one-particle sector",
            "constraint_genesis": "E_C input map selects one of 72 local rail identities",
            "constraint_enforcement": "every onsite factor and stream is number-preserving",
            "matter_modes": 6, "orientation_modes": 6,
            "recyclable_tag_modes": 2, "bounded_update_factor_depth": 5,
            "one_or_two_M2_gate_layout_depth_claimed": False,
            "host_schedule": False, "global_inverse_service": False,
            "controller_law_supplied": True,
        },
    )
    return {
        "rows": rows, "proper_cubic_frames": len(frames),
        "paired_frames": len(frames)**2, "paired_failures": paired_failures,
        "maximum_residual": maximum, "maximum_covariance_residual": covariance_maximum,
        "full_domain_inverse_residual": full_domain_inverse,
        "carriage_deletion_signal": carriage_deletion_signal,
        "inverse_branch_deletion_signal": inverse_deletion_signal,
        "second_reversal_deletion_signal": reversal_deletion_signal,
        "orientation_rail_deletion_leakage": orientation_rail_deletion_leakage,
        "M2_rail_identities_per_cell": 72, "net_transport_after_macro": True,
        "paired_576_are_macro_and_invariant_receipts_not_group_product_proof": True,
        "controller_law_supplied": True,
    }


def interpretation_firewall() -> dict[str, object]:
    body = normalized(NOTE)
    required = (
        "wrapped phase is not energy", "update schedule is not time",
        "group displacement is not a transition rate", "contact weight is not probability",
        "candidate occurrence is not a record", "formation is not record actuality",
        "source variation is not gravity", "no second stable bound band is certified",
    )
    missing = tuple(item for item in required if item not in body)
    check("interpretation firewall keeps phase, schedule, weights, occurrence, source, and non-certification typed", not missing, missing)
    return {"clean": not missing, "missing": missing}


def no_go_gate(retained: dict[str, float]) -> dict[str, object]:
    alternatives = (
        ("A flat pair", "normalized six-mode one-particle Bloch walk", "momentum-flat eigenphase pair", "exact compact carrier", "algebraic partial; negative not shipped"),
        ("B contact dimer", "Cycle230 antisymmetric two-CAR sector", "onsite even contact binding", "localized dispersive composite", "positive"),
        ("C recyclable transport", "72 local M2 rails", "carried U/T_f-U-dagger tag law", "net translated refocused packet", "positive supplied-law"),
        ("defect carrier", "Cycle575 seven-M2 star", "relational reflection defect", "compact stationary transition", "prior positive"),
        ("tensor composite", "Cycle575 direction-by-clock rails", "kinematic common carriage", "moving spectator transition", "prior positive"),
        ("larger contact orbit", "three-plus CAR particles or multi-band packet", "nonlinear/self-bound internal orbit", "intrinsic moving internal transition", "open"),
    )
    walls = (
        "second stable bound band or internal transition",
        "derive controller/orientation content",
        "unbounded noisy renewal",
        "empirical dimensionful calibration",
        "source/gravity response",
        "FORMATION Record actuality and Born law",
    )
    wall_mechanisms = {
        walls[0]: "spectral multiplicity and a local observable cross term",
        walls[1]: "genesis of auxiliary rail identities and branch dynamics",
        walls[2]: "error correction, renewal resources, and stability under iteration",
        walls[3]: "an independent measured scale and calibration map",
        walls[4]: "a dynamical source field and backreaction law",
        walls[5]: "admission, actuality, and measure-selection laws",
    }
    pairwise = tuple(
        (
            left, right,
            f"{left} uses {wall_mechanisms[left]}, which does not entail {wall_mechanisms[right]}",
            f"{right} uses {wall_mechanisms[right]}, which does not entail {wall_mechanisms[left]}",
            False,
        )
        for left, right in combinations(walls, 2)
    )
    n3 = (
        "Cycle219 beta-selected coin and mass map",
        "Cycle230 six intrinsic CAR modes, antisymmetric quotient, onsite coupling g=0.37, and periodic seam",
        "finite odd relative boxes and shift-invert spectral window",
        "band-packet momentum grid and initial envelope coefficients",
        "Route-C six orientation rails, two tag rails, branch law, and local circuit ordering",
        "noiseless periodic boxes and exact reusable rail identities",
    )
    n4 = (
        ("Cycle219", "massive proper-cubic free walk", "used byte-exact in all routes", True),
        ("Cycle230", "intrinsic CAR free-plus-contact update and seam", "literal antisymmetric two-particle lift used in Route B", True),
        ("Cycle563/569", "physical-M2 mass/contact/seam compiler fixtures", "retained residuals pinned", True),
        ("Cycle573", "scalar/even transition and free-stream leakage", "Route C forward branch uses it unchanged", True),
        ("Cycle575", "controller/composite imports exposed", "Route C changes return echo to net translation but does not derive control", True),
    )
    n5 = (
        ("Route A", "symbolic Bloch polynomial plus L5/L7/L9/L11", "algebraic determinant partial only; absence inference withheld"),
        ("Route B binding", "relative site and total-momentum fiber", "finite odd boxes through held L11; continuum and infinite-volume proof open"),
        ("Route B motion", "five K fibers and one finite Fourier packet", "finite-difference group displacement; no physical rate or continuum velocity theorem"),
        ("Route B transition", "one frozen secondary spectral window", "not certified; no absence theorem"),
        ("Route C", "site-local 72-rail code on finite periodic boxes", "exact macro and full finite domain; controller derivation open"),
    )
    n6 = (
        "continue the contact-band resolvent calculation to an infinite-volume pole and exponential-tail bound",
        "search cubic irreps and three-particle contact sectors for a second stable bound band",
        "couple the bound dimer to the accepted scalar/even transition rather than attach a spectator tag",
        "derive the orientation/tag carrier from an admitted recyclable local phase field",
        "replace Route-C supplied translation with interaction-generated dimer transport",
        "run independent source coupling and empirical-scale probes without calling wrapped phase energy",
    )
    n7 = (
        "Mechanism: the literal onsite even contact in the antisymmetric Cycle230 sector produces the tracked finite localized branch, while K-dependent eigenphase produces the packet displacement. "
        "Terminal obligation: an intrinsic internal clock still needs a second stable co-moving mode and a local cross observable. A hostile reviewer should accept L5/L7/L9/L11 plus held nonzero-K data only as finite evidence, "
        "reject an internal-clock or infinite-volume theorem, and identify Route C's 66 auxiliary rails and branch law as supplied. This steelman leaves constructive reopen paths and no shared impossibility."
    )
    n8 = (
        "Cycle219 supplied the massive one-particle coin and left localized transition content open",
        "Cycle230 supplied intrinsic CAR and the local even contact but explicitly lacked a physical-site compiler at that stage",
        "Cycles563/569 retained physical-M2 mass/contact/seam and source-carrier controls",
        "Cycle573 exposed free leakage of the scalar/even transition",
        "Cycle575 localized or refocused it only with explicit defect/controller/composite content",
        "Cycle578 finds finite intrinsic contact-bound moving-composite evidence, records Route-A algebraic factors without shipping an absence result, and keeps the separate controller import visible",
    )
    supplied = (
        "accepted byte-pinned Cycle219/230/563/569/573/575 physical shore",
        "beta=-0.3 species, Cycle230 coupling g=0.37, adjacent g=0.31/0.43 sensitivity values",
        "finite odd relative boxes, periodic seam, shift-invert targets, K grid, and Fourier coefficients",
        "Route-C 6x6x2 rail identity, carried orientation preparation, tag branch law, and T_f stream",
        "noiseless gates, exact one-excitation local rail constraint, and finite periodic boxes",
    )
    derived = (
        "exact symbolic non-flat determinants at all three k=0 candidate eigenvalues of the normalized massive one-particle walk",
        "finite-size-stable localized Cycle230 CAR dimer evidence with contact, radius, seam, eigen, inverse, and deletion receipts",
        "nonflat held L11 dimer band and nonzero finite-difference/Fourier-packet group displacement",
        "proper-cubic covariance under all24 frames and all576 invariant comparisons",
        "exact conditional G_C squared equals T_f macro with reset tag and net transported packet",
    )
    open_rows = (
        "infinite-volume/exponential localization theorem and continuum dispersion",
        "a second stable bound band or intrinsic internal beat/transition",
        "derivation of Route-C orientation/tag/controller law from the accepted CAR contact substrate",
        "dynamical binding of the scalar/even transition to the intrinsic contact dimer",
        "unbounded noisy operation and independent dimensionful calibration",
        "physical source/gravity/backreaction, FORMATION Record actuality, and Born probability",
    )
    ledger = {
        "C_ref": "one intrinsic contact-bound moving composite reference constructed; a second internal reference and controller derivation remain open",
        "C_num": "exact finite CAR-fiber/inverse and symbolic Route-A identities plus a dimensionless finite-difference group displacement; no empirical duration scale",
        "C_wrap": "Route-C tag resets after every transport macro and packet translates rather than returns; noisy/unbounded renewal is open",
        "C_int": "actual Cycle230 free-plus-contact interaction binds one dimer band; no second stable internal transition is certified",
        "C_local": "Route-B uses the accepted local antisymmetric CAR update; Route-C is bounded depth with 72 M2 per cell, all24/all576, but imports 66 rails beyond six-mode matter",
        "C_source": "contact coupling sensitivity g=0.31/0.37/0.43 is visible only as dimensionless source variation; no stress, gravity, redshift, or backreaction law",
    }
    qualifying_negative_families = (
        alternatives[0],
    )
    n1_required = 5
    n1_pass = len(qualifying_negative_families) >= n1_required
    negative_claim_shipped = False
    condition = (
        not n1_pass and not negative_claim_shipped and len(pairwise) == 15
        and all(row[-1] is False for row in pairwise)
        and all(row[-1] is True for row in n4)
        and max(retained.values()) < TOL
    )
    check(
        "fresh N1-N8 testing records N1 failure for the negative claims and therefore withholds flat-band absence, second-band absence, no-go, minimum-content, shared-obstruction, and axiom-pressure conclusions",
        condition,
        {
            "N1_normalized_alternatives": alternatives,
            "N1_qualifying_negative_families": qualifying_negative_families,
            "N1_required": n1_required, "N1_pass": n1_pass,
            "N2_pairwise_wall_audit": pairwise,
            "N3_hidden_condition_scan": n3,
            "N4_residual_matching": n4,
            "N5_resolution_audit": n5,
            "N6_partial_closure_paths": n6,
            "N7_hostile_steelman": n7,
            "N8_cross_cycle_echo": n8,
            "supplied": supplied, "derived": derived, "open": open_rows,
            "broad_localized_matter_no_go": "FAIL / DO NOT SHIP",
            "flat_band_absence_claim": "WITHHELD / N1 FAIL",
            "negative_claim_shipped": negative_claim_shipped,
            "second_band_absence_theorem": False,
            "minimum_content_claim": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "authority": AUTHORITY, "audit": AUDIT,
            "six_wall_ledger": ledger,
        },
    )
    return {
        "alternatives": alternatives, "pairwise": pairwise,
        "n3": n3, "n4": n4, "n5": n5, "n6": n6, "n7": n7, "n8": n8,
        "supplied": supplied, "derived": derived, "open": open_rows,
        "six_wall_ledger": ledger,
        "N1_pass": n1_pass, "negative_claim_shipped": negative_claim_shipped,
        "shared_substrate_obstruction": False, "axiom_pressure": False,
    }


def main() -> int:
    global PASS, FAIL
    PASS = 0
    FAIL = 0
    signal.alarm(int(WALL_CAP_SECONDS))
    started = time.perf_counter()
    print("Cycle578 intrinsic contact-bound moving-transition tournament")
    print("authority", AUTHORITY, "audit", AUDIT)
    retained = dependency_controls()
    note_contract()
    route_a = route_a_controls()
    route_b = route_b_controls()
    route_c = route_c_controls()
    firewall = interpretation_firewall()
    gate = no_go_gate(retained)
    elapsed = time.perf_counter() - started
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes = int(peak if sys.platform == "darwin" else peak * 1024)
    check(
        "the frozen Cycle578 tournament stays below the 360-second and 3-GiB cold caps",
        elapsed < WALL_CAP_SECONDS and peak_bytes < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "peak_RSS_bytes": peak_bytes},
    )
    summary = {
        "status": "cycle578-intrinsic-contact-bound-moving-transition-tournament",
        "authority": AUTHORITY, "audit": AUDIT,
        "tests_passed": PASS, "tests_failed": FAIL,
        "route_A_exact_nonflat_factorization": route_a.get("exact_factorization"),
        "route_B_maximum_eigen_residual": route_b.get("maximum_eigen_residual"),
        "route_B_group_displacement": route_b.get("finite_difference_group_displacement_per_update"),
        "route_B_packet_displacement": route_b.get("band_packet_one_update_displacement"),
        "route_B_all576_failures": route_b.get("all576_failures"),
        "route_C_maximum_residual": route_c.get("maximum_residual"),
        "route_C_all576_failures": route_c.get("paired_failures"),
        "firewall_clean": firewall.get("clean"),
        "shared_substrate_obstruction": gate.get("shared_substrate_obstruction"),
        "axiom_pressure": gate.get("axiom_pressure"),
        "elapsed_seconds_internal": elapsed,
        "maximum_RSS_bytes_internal": peak_bytes,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
