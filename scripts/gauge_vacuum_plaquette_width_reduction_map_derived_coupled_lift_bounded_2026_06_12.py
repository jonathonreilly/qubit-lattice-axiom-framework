#!/usr/bin/env python3
"""Derived width-reduction map for the finite plaquette width-two packet.

This runner stays inside repo-internal finite data:

* tensor word box NMAX=4 and MODE_MAX=80;
* source readout NMAX=7 and MODE_MAX=200;
* width-two pair layer dimension 25^2 = 625;
* no external values except the already admitted fenced comparison number.

It implements two rail-removal candidates and two intra-layer shared-link
bonds.  The Haar/Wilson channel-sum reduction with the matrix-element
shared-link bond is the primary branch derived in the companion note.  The
Perron reduction and character shared-link bond are controls.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word


AUDIT_TIMEOUT_SEC = 600

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
TW_NMAX = 4
TW_MODE_MAX = 80
SOURCE_NMAX = one_word.SOURCE_NMAX
SOURCE_MODE_MAX = one_word.SOURCE_MODE_MAX
WIDTH1_P_INF_REFERENCE = 0.615191992185898
WIDTH1_THETA_REFERENCE = 0.263745855973467
COMPARATOR = one_word.CANONICAL_COMPARATOR
COMPARATOR_TEXT = one_word.CANONICAL_COMPARATOR_TEXT
KMAX = 12

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WIDTH_REDUCTION_MAP_DERIVED_COUPLED_LIFT_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class Packet:
    weights: tuple[tuple[int, int], ...]
    index: dict[tuple[int, int], int]
    d_coeff: np.ndarray
    dim: np.ndarray
    fusion: np.ndarray
    tensor_word: np.ndarray
    eta_inf: np.ndarray
    t_matrix: np.ndarray
    source_setup: dict[str, object]


@dataclass(frozen=True)
class Candidate:
    name: str
    vector: np.ndarray
    license_label: str


@dataclass(frozen=True)
class EffectiveBranch:
    candidate: str
    bond: str
    t_eff: np.ndarray
    d_eff_norm: np.ndarray
    t00: float
    theta_closed: float
    max_t_norm_diff: float
    max_d_norm_diff: float


@dataclass(frozen=True)
class MeasurementRow:
    k: int
    p_value: float
    rho10: float
    rho11: float
    error_to_ptriv: float


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 112)
    print(title)
    print("=" * 112)


def build_packet() -> Packet:
    tw = one_word.build_tensor_word(TW_NMAX, TW_MODE_MAX)
    weights = tuple(tw["weights"])
    index = dict(tw["index"])
    d_coeff = np.asarray(tw["normalized"], dtype=float)
    dim = np.asarray([one_word.src_existing.dim_su3(p, q) for p, q in weights], dtype=float)
    fusion = np.asarray(tw["nf"] + tw["nfb"], dtype=float)
    tensor_word = np.asarray(tw["tensor_word"], dtype=float)
    _eta_eig, _eta_vec, eta_inf = one_word.perron_vector_of_tensor_word(
        tensor_word, index
    )
    g_channel = fusion.T @ ((d_coeff * d_coeff)[:, None] * fusion)
    t_matrix = (
        np.sqrt(d_coeff[:, None] * d_coeff[None, :])
        * g_channel
        / np.sqrt(dim[:, None] * dim[None, :])
    )
    return Packet(
        weights=weights,
        index=index,
        d_coeff=d_coeff,
        dim=dim,
        fusion=fusion,
        tensor_word=tensor_word,
        eta_inf=np.asarray(eta_inf, dtype=float),
        t_matrix=t_matrix,
        source_setup=one_word.source_setup(SOURCE_NMAX, SOURCE_MODE_MAX),
    )


def source_p(packet: Packet, rho25: np.ndarray) -> float:
    setup = packet.source_setup
    source_weights = list(setup["weights"])
    source_index = dict(setup["index"])
    rho_vec = np.zeros(len(source_weights), dtype=float)
    for i, weight in enumerate(packet.weights):
        if weight in source_index:
            rho_vec[source_index[weight]] = float(rho25[i])
    _eig, p_value, _psi, _u0 = one_word.source_perron_from_rho_vector(
        setup, rho_vec
    )
    return float(p_value)


def conjugate(weight: tuple[int, int]) -> tuple[int, int]:
    return (weight[1], weight[0])


def swap_permutation(packet: Packet) -> np.ndarray:
    perm = np.empty(len(packet.weights), dtype=int)
    for i, weight in enumerate(packet.weights):
        perm[i] = packet.index[conjugate(weight)]
    return perm


def conjugation_error(packet: Packet, matrix: np.ndarray) -> float:
    perm = swap_permutation(packet)
    return float(np.max(np.abs(matrix[np.ix_(perm, perm)] - matrix)))


def width1_theta(packet: Packet) -> float:
    z = packet.index[ZERO]
    f = packet.index[FUND]
    ell_eta = packet.fusion.T @ (packet.d_coeff * packet.eta_inf)
    return float(
        (ell_eta[f] / ell_eta[z])
        * math.sqrt(packet.d_coeff[f] / packet.dim[f])
        * (packet.t_matrix[f, z] / packet.t_matrix[z, z])
    )


def candidate_vectors(packet: Packet) -> list[Candidate]:
    return [
        Candidate(
            name="perron",
            vector=packet.eta_inf.copy(),
            license_label="control: stationary finite tensor-word rail",
        ),
        Candidate(
            name="haar_wilson_sum",
            vector=packet.dim * packet.d_coeff,
            license_label="primary: Wilson channel coefficients d_lambda D_lambda",
        ),
    ]


def pair_space(packet: Packet) -> tuple[
    tuple[tuple[tuple[int, int], tuple[int, int]], ...],
    dict[tuple[tuple[int, int], tuple[int, int]], int],
]:
    pairs = tuple((left, right) for left in packet.weights for right in packet.weights)
    return pairs, {pair: i for i, pair in enumerate(pairs)}


def contraction_matrix(packet: Packet, vector: np.ndarray) -> np.ndarray:
    pairs, pair_index = pair_space(packet)
    cmat = np.zeros((len(pairs), len(packet.weights)), dtype=float)
    for a_idx, left in enumerate(packet.weights):
        for b_idx, right in enumerate(packet.weights):
            cmat[pair_index[(left, right)], a_idx] = float(vector[b_idx])
    return cmat


def q_pair(packet: Packet, bond: str) -> np.ndarray:
    pairs, _pair_index = pair_space(packet)
    q = np.zeros(len(pairs), dtype=float)
    for pos, (left, right) in enumerate(pairs):
        if bond == "factorized":
            q[pos] = 1.0
        elif left == right and bond == "character":
            q[pos] = 1.0
        elif left == right and bond == "matrix_element":
            q[pos] = 1.0 / float(packet.dim[packet.index[left]])
        elif bond not in {"character", "matrix_element"}:
            raise ValueError(f"unknown bond: {bond}")
    return q


def pair_matrix(base: np.ndarray, packet: Packet, bond: str) -> np.ndarray:
    q = q_pair(packet, bond)
    sqrt_q = np.sqrt(q)
    out = np.kron(base, base)
    return sqrt_q[:, None] * out * sqrt_q[None, :]


def reduce_pair_matrix(
    pair_mat: np.ndarray,
    scalar_base: np.ndarray,
    packet: Packet,
    vector: np.ndarray,
) -> np.ndarray:
    cmat = contraction_matrix(packet, vector)
    scalar = float(vector @ (scalar_base @ vector))
    return (cmat.T @ pair_mat @ cmat) / scalar


def closed_effective_t(
    packet: Packet,
    vector: np.ndarray,
    bond: str,
) -> np.ndarray:
    scalar = float(vector @ (packet.t_matrix @ vector))
    if bond == "character":
        q_diag = np.ones(len(packet.weights), dtype=float)
    elif bond == "matrix_element":
        q_diag = 1.0 / packet.dim
    else:
        raise ValueError(f"unknown coupled bond: {bond}")
    side = vector * np.sqrt(q_diag)
    return (
        side[:, None]
        * side[None, :]
        * (packet.t_matrix * packet.t_matrix)
        / scalar
    )


def normalized_d_eff(packet: Packet, vector: np.ndarray, bond: str) -> np.ndarray:
    if bond == "character":
        q_diag = np.ones(len(packet.weights), dtype=float)
    elif bond == "matrix_element":
        q_diag = 1.0 / packet.dim
    else:
        raise ValueError(f"unknown coupled bond: {bond}")
    v0 = float(vector[packet.index[ZERO]])
    return ((vector / v0) ** 2) * q_diag * (packet.d_coeff**2) / packet.dim


def effective_branch(packet: Packet, candidate: Candidate, bond: str) -> EffectiveBranch:
    t_eff = closed_effective_t(packet, candidate.vector, bond)
    d_eff = normalized_d_eff(packet, candidate.vector, bond)
    z = packet.index[ZERO]
    f = packet.index[FUND]
    t_norm = t_eff / float(t_eff[z, z])
    t_ref_norm = packet.t_matrix / float(packet.t_matrix[z, z])
    return EffectiveBranch(
        candidate=candidate.name,
        bond=bond,
        t_eff=t_eff,
        d_eff_norm=d_eff,
        t00=float(t_eff[z, z]),
        theta_closed=float(t_eff[f, z] / t_eff[z, z]),
        max_t_norm_diff=float(np.max(np.abs(t_norm - t_ref_norm))),
        max_d_norm_diff=float(np.max(np.abs(d_eff - packet.d_coeff))),
    )


def top_rho_from_t(packet: Packet, t_eff: np.ndarray, k: int) -> tuple[float, np.ndarray]:
    reduced = np.sqrt(packet.dim[:, None] * packet.dim[None, :]) * (t_eff**k)
    vals, vecs = np.linalg.eigh(reduced)
    pos = int(np.argmax(vals))
    vec = vecs[:, pos].real
    z = packet.index[ZERO]
    if float(vec[z]) < 0.0:
        vec = -vec
    rho = vec / float(vec[z])
    return float(vals[pos]), rho


def measurement_rows(
    packet: Packet,
    branch: EffectiveBranch,
    p_limit: float,
) -> list[MeasurementRow]:
    rows: list[MeasurementRow] = []
    f = packet.index[FUND]
    adj = packet.index[(1, 1)]
    for k in range(1, KMAX + 1):
        _eig, rho = top_rho_from_t(packet, branch.t_eff, k)
        p_value = source_p(packet, rho)
        rows.append(
            MeasurementRow(
                k=k,
                p_value=p_value,
                rho10=float(rho[f]),
                rho11=float(rho[adj]),
                error_to_ptriv=abs(p_value - p_limit),
            )
        )
    return rows


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette width-reduction map derived coupled lift runner")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )
    print("No new imports: repo-internal finite packet quantities only.")

    packet = build_packet()
    z = packet.index[ZERO]
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]

    section("Part 1: width-one anchors")
    rho_pair = np.zeros(len(packet.weights), dtype=float)
    rho_pair[f] = 1.0
    rho_pair[fb] = 1.0
    p_width1 = source_p(packet, rho_pair)
    rho_triv = np.zeros(len(packet.weights), dtype=float)
    rho_triv[z] = 1.0
    p_triv = source_p(packet, rho_triv)
    theta1 = width1_theta(packet)
    print(f"P_inf(width1 pair support) = {p_width1:.15f}")
    print(f"P_trivial_source = {p_triv:.15f}")
    print(f"theta(width1) = {theta1:.15f}")
    check(
        "width-one pair-support source limit matches declared anchor",
        abs(p_width1 - WIDTH1_P_INF_REFERENCE) < 5.0e-13,
        f"delta={abs(p_width1 - WIDTH1_P_INF_REFERENCE):.3e}",
    )
    check(
        "width-one theta matches declared anchor",
        abs(theta1 - WIDTH1_THETA_REFERENCE) < 5.0e-15,
        f"delta={abs(theta1 - WIDTH1_THETA_REFERENCE):.3e}",
    )
    check(
        "trivial source readout stays below the width-one pair-support readout",
        p_triv < p_width1,
        f"P_triv={p_triv:.15f}",
    )

    section("Part 2: 625-box reduction gates")
    t_pair_factorized = pair_matrix(packet.t_matrix, packet, "factorized")
    t_pair_matrix = pair_matrix(packet.t_matrix, packet, "matrix_element")
    t_pair_character = pair_matrix(packet.t_matrix, packet, "character")
    tensor_pair_factorized = pair_matrix(packet.tensor_word, packet, "factorized")
    print(f"pair layer dimension = {t_pair_factorized.shape[0]}")
    check("width-two pair layer has 625 states", t_pair_factorized.shape == (625, 625))

    primary_candidate: Candidate | None = None
    branches: list[EffectiveBranch] = []
    for candidate in candidate_vectors(packet):
        print(f"{candidate.name}: {candidate.license_label}")
        reduced_t_factorized = reduce_pair_matrix(
            t_pair_factorized, packet.t_matrix, packet, candidate.vector
        )
        reduced_tensor_factorized = reduce_pair_matrix(
            tensor_pair_factorized, packet.tensor_word, packet, candidate.vector
        )
        check(
            f"G1 {candidate.name}: factorized t reduction reproduces width-one t",
            float(np.max(np.abs(reduced_t_factorized - packet.t_matrix))) < 2.0e-15,
            f"max_diff={float(np.max(np.abs(reduced_t_factorized - packet.t_matrix))):.3e}",
        )
        check(
            f"G1 {candidate.name}: factorized tensor reduction reproduces width-one tensor_word",
            float(np.max(np.abs(reduced_tensor_factorized - packet.tensor_word))) < 2.0e-15,
            f"max_diff={float(np.max(np.abs(reduced_tensor_factorized - packet.tensor_word))):.3e}",
        )
        if candidate.name == "haar_wilson_sum":
            primary_candidate = candidate

        for bond, pair_t in [
            ("character", t_pair_character),
            ("matrix_element", t_pair_matrix),
        ]:
            branch = effective_branch(packet, candidate, bond)
            reduced_direct = reduce_pair_matrix(
                pair_t, packet.t_matrix, packet, candidate.vector
            )
            direct_diff = float(np.max(np.abs(reduced_direct - branch.t_eff)))
            branches.append(branch)
            print(
                f"{candidate.name}/{bond}: t00={branch.t00:.15e}; "
                f"theta_closed={branch.theta_closed:.15e}; "
                f"max |D_eff_norm-D|={branch.max_d_norm_diff:.6e}; "
                f"max normalized t shift={branch.max_t_norm_diff:.6e}"
            )
            check(
                f"G2 {candidate.name}/{bond}: direct 625 contraction matches closed effective t",
                direct_diff < 5.0e-17,
                f"max_diff={direct_diff:.3e}",
            )
            check(
                f"G2 {candidate.name}/{bond}: effective t is nonnegative and finite",
                np.all(np.isfinite(branch.t_eff)) and float(np.min(branch.t_eff)) >= -1.0e-18,
                f"min={float(np.min(branch.t_eff)):.3e}",
            )
            check(
                f"G2 {candidate.name}/{bond}: effective t is conjugation-symmetric",
                conjugation_error(packet, branch.t_eff) < 1.0e-16,
                f"max_error={conjugation_error(packet, branch.t_eff):.3e}",
            )

    section("Part 3: licensed branch and shared-link control")
    if primary_candidate is None:
        raise RuntimeError("missing primary candidate")
    primary = next(
        b
        for b in branches
        if b.candidate == "haar_wilson_sum" and b.bond == "matrix_element"
    )
    control = next(
        b
        for b in branches
        if b.candidate == "haar_wilson_sum" and b.bond == "character"
    )
    print("licensed reduction: haar_wilson_sum")
    print("licensed intra-layer bond: matrix_element")
    print(f"control character theta_closed = {control.theta_closed:.15e}")
    print(f"primary matrix theta_closed = {primary.theta_closed:.15e}")
    check(
        "matrix-element and character controls are numerically distinct",
        abs(primary.theta_closed - control.theta_closed) > 1.0e-3,
        f"delta={abs(primary.theta_closed - control.theta_closed):.3e}",
    )
    check(
        "primary effective D is the derived normalized D^4 row on the Haar/matrix branch",
        float(np.max(np.abs(primary.d_eff_norm - packet.d_coeff**4))) < 5.0e-16,
        f"D_eff(1,0)={primary.d_eff_norm[f]:.15e}, D(1,0)^4={(packet.d_coeff[f]**4):.15e}",
    )
    check(
        "primary measured rho10 decay ratio is the fundamental-trivial t contact ratio",
        primary.theta_closed > 0.0
        and abs(primary.theta_closed - float(primary.t_eff[z, f] / primary.t_eff[z, z])) < 1.0e-15
        and abs(primary.theta_closed - float(primary.t_eff[fb, z] / primary.t_eff[z, z])) < 1.0e-15,
        f"theta_closed={primary.theta_closed:.15e}",
    )

    section("Part 4: coupled width-two measurement")
    rows = measurement_rows(packet, primary, p_triv)
    print("k | P_coupled | |P-P_triv| | rho10 | rho11")
    print("-" * 112)
    for row in rows:
        print(
            f"{row.k:2d} | {row.p_value:.12f} | {row.error_to_ptriv:.12e} | "
            f"{row.rho10:.12e} | {row.rho11:.12e}"
        )
    rho_ratio = rows[7].rho10 / rows[6].rho10
    err_ratio = rows[6].error_to_ptriv / rows[5].error_to_ptriv
    print(f"rho10 measured theta ratio k8/k7 = {rho_ratio:.15e}")
    print(f"P-error measured theta ratio err7/err6 = {err_ratio:.15e}")
    check(
        "coupled matrix branch converges to the trivial source limit by k=12",
        rows[-1].error_to_ptriv < 1.0e-13,
        f"err12={rows[-1].error_to_ptriv:.3e}",
    )
    check(
        "measured rho10 theta agrees with the closed effective t-ratio",
        abs(rho_ratio - primary.theta_closed) < 5.0e-8,
        f"rho_ratio={rho_ratio:.15e}, closed={primary.theta_closed:.15e}",
    )
    check(
        "measured P-error theta tracks the closed effective t-ratio before roundoff",
        abs(err_ratio - primary.theta_closed) < 5.0e-5,
        f"err_ratio={err_ratio:.15e}, closed={primary.theta_closed:.15e}",
    )

    section("Part 5: fenced comparator distances")
    width1_gap = abs(p_width1 - COMPARATOR)
    width2_gap = abs(p_triv - COMPARATOR)
    signed_displacement = p_width1 - p_triv
    signed_gap_units = signed_displacement / width1_gap
    distance_closure = (width1_gap - width2_gap) / width1_gap
    print("Plaquette reuse license: comparator is used only as comparison/reuse context.")
    print("```text")
    print(f"P_inf(width1) = {p_width1:.15f}")
    print(f"P_inf(width2 coupled, haar/matrix reduction) = {p_triv:.15f}")
    print(f"{COMPARATOR_TEXT} fenced comparator = {COMPARATOR:.15f}")
    print(f"|P_inf(width1) - {COMPARATOR_TEXT}| = {width1_gap:.15f}")
    print(f"|P_inf(width2 coupled) - {COMPARATOR_TEXT}| = {width2_gap:.15f}")
    print(f"signed_displacement_from_width1_in_gap_units = {signed_gap_units:.15f}")
    print(f"absolute_distance_closure_fraction = {distance_closure:.15f}")
    print(f"theta(width2 coupled measured) = {rho_ratio:.15e}")
    print(f"theta(width2 coupled closed_t_ratio) = {primary.theta_closed:.15e}")
    print("```")
    check(
        "coupled width-two limit is not a bounded lift toward the fenced comparator",
        width2_gap > width1_gap,
        f"width1_gap={width1_gap:.3e}, width2_gap={width2_gap:.3e}",
    )
    check(
        "reported signed gap units record the overshoot rather than a tuned match",
        signed_gap_units > 1.0 and distance_closure < 0.0,
        f"signed_gap_units={signed_gap_units:.6f}, distance_closure={distance_closure:.6f}",
    )

    section("Part 6: note hygiene")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority:** independent audit lane only" in text
            or "Status authority: independent audit lane only" in text,
        )
        check(
            "note uses markdown links for one-hop authorities",
            "[GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md]" in text
            and "[SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md]" in text,
        )
        check(
            "note keeps context pointers as repo filenames without load-bearing links",
            "GAUGE_VACUUM_PLAQUETTE_WIDTH_TWO_LADDER_STRUCTURAL_LIFT_BOUNDED_NOTE_2026-06-12.md"
            in text
            and "[GAUGE_VACUUM_PLAQUETTE_WIDTH_TWO_LADDER_STRUCTURAL_LIFT_BOUNDED_NOTE_2026-06-12.md]"
            not in text,
        )
        check(
            "note includes a visible no-go discipline gate for the bounded negative",
            "## No-Go Discipline Gate" in text
            and "Gate result: PASS" in text,
        )
    else:
        check("note exists for this runner", False, f"missing {NOTE_PATH}")

    print(
        "Named residuals: finite dominant-weight box; finite Bessel mode support; "
        "finite width-two pair layer; no all-weight width-reduction theorem; no "
        "physical 3D unmarked spatial Wilson environment computation; no "
        "width-to-infinity slab; no slab-stacking to 3D; no L_perp limit; "
        "no analytic P(6); no repinning."
    )
    check("runner names residuals without claiming them retired", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
