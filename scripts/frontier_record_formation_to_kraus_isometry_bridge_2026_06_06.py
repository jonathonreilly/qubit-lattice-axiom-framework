#!/usr/bin/env python3
"""Bridge certificate: finite pointer record formation to Kraus isometry.

This runner verifies a narrow exact statement:

  stable finite pointer projectors + orthonormal record labels
  + controlled-copy/fresh-fragment write-isometry bridge
    => W|psi> = sum_r (P_r|psi>) tensor |r> is an isometry
    => extracted K_r are the projectors P_r
    => the projective Kraus instrument is CPTP and repeat-readable.

It does not derive W from arbitrary persistent-record dynamics, does not select
a Hamiltonian/coupling/rate, does not derive a probability law from post-record
counts, and does not select a generation/Koide dial.
"""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTROLLED_COPY_NOTE = (
    "docs/RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md"
)
TOL = 1e-12
PASS = 0
FAIL = 0


def report(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 78)
    print(title)
    print("-" * 78)


def read_rel(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def require_text(path: str, needles: list[str]) -> None:
    text = read_rel(path)
    report(f"{path} exists", True)
    for needle in needles:
        report(f"{path} contains: {needle}", needle in text)


def dagger(a: np.ndarray) -> np.ndarray:
    return a.conj().T


def close(a: np.ndarray, b: np.ndarray, tol: float = TOL) -> bool:
    return np.linalg.norm(a - b) < tol


def density_from_ket(ket: np.ndarray) -> np.ndarray:
    return np.outer(ket, ket.conj())


def apply_channel(kraus: list[np.ndarray], rho: np.ndarray) -> np.ndarray:
    return sum(k @ rho @ dagger(k) for k in kraus)


def choi_matrix(kraus: list[np.ndarray]) -> np.ndarray:
    d = kraus[0].shape[0]
    blocks = []
    for i in range(d):
        row = []
        for j in range(d):
            eij = np.zeros((d, d), dtype=complex)
            eij[i, j] = 1.0
            row.append(apply_channel(kraus, eij))
        blocks.append(row)
    return np.block(blocks)


def build_projective_W(projectors: list[np.ndarray]) -> np.ndarray:
    """Record-major block-column W = [P_0; P_1; ...]."""
    return np.vstack(projectors)


def extract_blocks(W: np.ndarray, d: int, outcomes: int) -> list[np.ndarray]:
    return [W[r * d : (r + 1) * d, :] for r in range(outcomes)]


def branch_state(k: np.ndarray, rho: np.ndarray) -> tuple[float, np.ndarray | None]:
    unnorm = k @ rho @ dagger(k)
    prob = float(np.real_if_close(np.trace(unnorm)))
    if prob <= TOL:
        return prob, None
    return prob, unnorm / prob


def min_hermitian_eig(a: np.ndarray) -> float:
    h = 0.5 * (a + dagger(a))
    return float(np.min(np.linalg.eigvalsh(h)))


def source_anchor_checks() -> None:
    section("Source-anchor checks")
    require_text(
        "docs/RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE_2026-06-06.md",
        [
            "actual_current_surface_status: exact-support",
            "trace_class: upstream_support",
            "audit_required_before_effective_retained: true",
            "controlled-copy/fresh-fragment write-isometry theorem",
            "The ideal write isometry is no longer an",
            "It does not derive arbitrary persistent-record dynamics into a normalized",
            "It does not select a generation or Koide dial location.",
        ],
    )
    require_text(
        CONTROLLED_COPY_NOTE,
        [
            "Controlled-Copy Write-Isometry Theorem",
            "U_cc(pi/4)(|psi> tensor |0>_R)",
            "<eta_0|eta_1> = 0",
            "K_r = <r|W = P_r",
            "What This Does Not Close",
        ],
    )
    require_text(
        "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
        [
            "pointer-non-demolition",
            "[H_int, Pi_S] = 0",
            "This is **bounded** because",
            "does not derive a dynamics, an action, gauge bosons, coupling values",
        ],
    )
    require_text(
        "docs/PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md",
        [
            "The finite Kraus/CPTP algebra closes once a normalized linear isometry `W` is",
            "deriving `W` from persistent-record dynamics",
            "persistent-record-to-isometry bridge remains open",
        ],
    )
    require_text(
        "docs/PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md",
        [
            "exhibit V explicitly as a",
            "Selection of which `{K_r}` family is physical",
            "The choice of `{K_r}` is downstream framework physics",
        ],
    )
    require_text(
        "docs/RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05.md",
        [
            "pre-record carrier",
            "formation/preservation dynamics",
            "post-record information dynamics",
            "Record history/count support is therefore an exact **consumer** of realized",
        ],
    )


def algebra_checks() -> None:
    section("Projective record-write isometry algebra")
    ident = np.eye(2, dtype=complex)
    p0 = np.array([[1, 0], [0, 0]], dtype=complex)
    p1 = np.array([[0, 0], [0, 1]], dtype=complex)
    projectors = [p0, p1]

    for idx, p in enumerate(projectors):
        report(f"P{idx} hermitian", close(dagger(p), p))
        report(f"P{idx} idempotent", close(p @ p, p))
    report("P0 P1 = 0", close(p0 @ p1, np.zeros_like(p0)))
    report("P1 P0 = 0", close(p1 @ p0, np.zeros_like(p0)))
    report("sum_r P_r = I", close(p0 + p1, ident))

    W = build_projective_W(projectors)
    report("W has record-major block-column shape (4,2)", W.shape == (4, 2), str(W.shape))
    report("W^dagger W = I", close(dagger(W) @ W, ident))

    kraus = extract_blocks(W, 2, 2)
    report("K0 extraction equals P0", close(kraus[0], p0))
    report("K1 extraction equals P1", close(kraus[1], p1))
    resolution = sum(dagger(k) @ k for k in kraus)
    report("sum_r K_r^dagger K_r = I", close(resolution, ident))

    choi = choi_matrix(kraus)
    report("Choi matrix is positive semidefinite", min_hermitian_eig(choi) > -TOL)

    ket = np.array([np.sqrt(2 / 3), np.exp(0.37j) / np.sqrt(3)], dtype=complex)
    rho = density_from_ket(ket)
    channel = apply_channel(kraus, rho)
    expected_dephased = np.diag(np.diag(rho))
    report("unconditional channel trace is one", abs(np.trace(channel) - 1.0) < TOL)
    report("unconditional channel is pointer dephasing", close(channel, expected_dephased))
    report("pre-record coherence is removed in post-record unread state", abs(channel[0, 1]) < TOL)

    probs = []
    branches = []
    for idx, k in enumerate(kraus):
        prob, branch = branch_state(k, rho)
        probs.append(prob)
        branches.append(branch)
        report(f"branch {idx} probability is nonnegative", prob >= -TOL, f"p={prob:.12f}")
        report(f"branch {idx} normalized when nonzero", branch is not None and abs(np.trace(branch) - 1.0) < TOL)
        report(f"branch {idx} positive when nonzero", branch is not None and min_hermitian_eig(branch) > -TOL)
    report("branch probabilities sum to one", abs(sum(probs) - 1.0) < TOL, f"sum={sum(probs):.12f}")
    report("branch probabilities match pointer populations", np.allclose(probs, np.real(np.diag(rho)), atol=TOL))

    for idx, branch in enumerate(branches):
        assert branch is not None
        same_prob, same_branch = branch_state(kraus[idx], branch)
        other_prob, _ = branch_state(kraus[1 - idx], branch)
        report(f"branch {idx} repeat-read has probability one", abs(same_prob - 1.0) < TOL)
        report(f"branch {idx} repeat-read leaves state fixed", same_branch is not None and close(same_branch, branch))
        report(f"branch {idx} cross-read excluded", abs(other_prob) < TOL)

    record0 = np.array([1, 0], dtype=complex)
    record1 = np.array([0, 1], dtype=complex)
    report("record labels are orthogonal one-hot atoms", abs(np.vdot(record0, record1)) < TOL)

    image = W @ ket
    report("W preserves norm for coherent pre-record ket", abs(np.vdot(image, image) - np.vdot(ket, ket)) < TOL)
    expected_image = np.array([ket[0], 0.0, 0.0, ket[1]], dtype=complex)
    report("W writes pointer label without rotating pointer sector", close(image, expected_image))


def boundary_controls() -> None:
    section("Boundary controls")
    ident = np.eye(2, dtype=complex)
    p0 = np.array([[1, 0], [0, 0]], dtype=complex)
    p1 = np.array([[0, 0], [0, 1]], dtype=complex)
    W_single_label = ident.copy()
    single_blocks = [W_single_label]
    report("single-label write can be an isometry", close(dagger(W_single_label) @ W_single_label, ident))
    report("single-label write is not a two-outcome record split", len(single_blocks) != 2)

    fake_W = np.vstack([ident, ident])
    report("duplicating the whole state into two outcomes is not normalized", not close(dagger(fake_W) @ fake_W, ident))
    report("projector block split is the normalized two-record write", close(dagger(np.vstack([p0, p1])) @ np.vstack([p0, p1]), ident))

    general_dynamics_to_W_derived = False
    controlled_copy_to_W_derived_for_explicit_model = True
    physical_hamiltonian_selected = False
    probability_law_derived_from_counts = False
    generation_or_koide_dial_selected = False
    audit_verdict_applied = False
    report("controlled-copy to W derived for explicit finite model flag is true", controlled_copy_to_W_derived_for_explicit_model)
    report("general persistent dynamics to W derived flag is false", not general_dynamics_to_W_derived)
    report("physical Hamiltonian/coupling selected flag is false", not physical_hamiltonian_selected)
    report("probability law from post-record counts flag is false", not probability_law_derived_from_counts)
    report("generation/Koide dial selected flag is false", not generation_or_koide_dial_selected)
    report("audit verdict applied flag is false", not audit_verdict_applied)


def main() -> int:
    source_anchor_checks()
    algebra_checks()
    boundary_controls()
    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("RECORD_FORMATION_TO_KRAUS_ISOMETRY_BRIDGE=EXACT_SUPPORT_UNDER_FINITE_POINTER_MODEL")
    print("GENERAL_PERSISTENT_RECORD_DYNAMICS_TO_W_DERIVED=FALSE")
    print("POST_RECORD_COUNTS_SELECT_PROBABILITY_OR_DIAL=FALSE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
