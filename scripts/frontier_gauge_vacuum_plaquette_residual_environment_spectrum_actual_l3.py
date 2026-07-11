#!/usr/bin/env python3
"""Two-slice literal-factor-deletion discriminator on the L_s=3 Wilson kernel.

The sampled positive two-slice weight is the temporal-gauge Wilson one-step
kernel after deleting, configuration by configuration,

* the marked spatial half-plaquette weight on both slices, and
* the four marked-link mixed-plaquette factors.

The resulting character matrix is a literal-factor-deletion discriminator,
not the algebraic quotient obtained by first compressing to the marked class
sector and then stripping `M` and `D_loc`.  A significant off-diagonal element
would falsify the naive route that identifies literal deletion with a central
convolution.  A diagonal result cannot by itself establish the algebraically
stripped residual equality.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np

from frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_actual_l3 import (
    BETA,
    FACES,
    IRREPS,
    L,
    LINK_TO_FACES,
    dim_su3,
    face_matrix,
    random_haar_su3,
    random_su2_subgroup_step,
    su3_character_from_trace,
)


AUDIT_TIMEOUT_SEC = 180
TRACKED = IRREPS[:4]
SEEDS = (73009, 73013, 73019, 73037)


def marked_links(face_id: int) -> set[int]:
    return {link_id for link_id, _ in FACES[face_id]}


def spatial_real_trace(slice_links: np.ndarray, face_id: int) -> float:
    return float(np.trace(face_matrix(slice_links, FACES[face_id])).real)


def residual_log_weight(two_slice_links: np.ndarray, marked_face: int) -> float:
    total = 0.0
    for tau in range(2):
        total += (BETA / 6.0) * sum(
            spatial_real_trace(two_slice_links[tau], face_id)
            for face_id in range(len(FACES))
            if face_id != marked_face
        )
    boundary = marked_links(marked_face)
    total += (BETA / 3.0) * sum(
        np.trace(two_slice_links[1, link_id] @ two_slice_links[0, link_id].conj().T).real
        for link_id in range(3 * L**3)
        if link_id not in boundary
    )
    return float(total)


def residual_sweep(
    links: np.ndarray,
    rng: np.random.Generator,
    epsilon: float,
    marked_face: int,
) -> float:
    boundary = marked_links(marked_face)
    accepted = 0
    order = rng.permutation(2 * 3 * L**3)
    for flat in order:
        tau, link_id = divmod(int(flat), 3 * L**3)
        old = links[tau, link_id].copy()
        active_spatial = [f for f in LINK_TO_FACES[link_id] if f != marked_face]
        old_sum = (BETA / 6.0) * sum(
            spatial_real_trace(links[tau], f) for f in active_spatial
        )
        if link_id not in boundary:
            old_sum += (BETA / 3.0) * np.trace(
                links[1, link_id] @ links[0, link_id].conj().T
            ).real

        links[tau, link_id] = random_su2_subgroup_step(rng, epsilon) @ old
        new_sum = (BETA / 6.0) * sum(
            spatial_real_trace(links[tau], f) for f in active_spatial
        )
        if link_id not in boundary:
            new_sum += (BETA / 3.0) * np.trace(
                links[1, link_id] @ links[0, link_id].conj().T
            ).real
        delta = float(new_sum - old_sum)
        if delta >= 0.0 or rng.random() < math.exp(delta):
            accepted += 1
        else:
            links[tau, link_id] = old
    return accepted / (2 * 3 * L**3)


def character_vector(slice_links: np.ndarray, marked_face: int) -> np.ndarray:
    trace_w = np.trace(face_matrix(slice_links, FACES[marked_face]))
    return np.array(
        [su3_character_from_trace(trace_w, p, q) for p, q in TRACKED],
        dtype=complex,
    )


@dataclass
class Chain:
    seed: int
    marked_face: int
    initial: str
    acceptance: float
    matrices: np.ndarray


def run_chain(
    seed: int,
    marked_face: int,
    initial: str,
    therm: int,
    measure: int,
    sample_every: int,
) -> Chain:
    rng = np.random.default_rng(seed)
    if initial == "cold":
        links = np.tile(np.eye(3, dtype=complex), (2, 3 * L**3, 1, 1))
    else:
        links = np.array(
            [[random_haar_su3(rng) for _ in range(3 * L**3)] for _ in range(2)]
        )
    epsilon = 0.32
    for sweep in range(therm):
        acc = residual_sweep(links, rng, epsilon, marked_face)
        if (sweep + 1) % 25 == 0:
            if acc > 0.62:
                epsilon *= 1.05
            elif acc < 0.42:
                epsilon *= 0.95
            epsilon = float(np.clip(epsilon, 0.06, 1.2))

    samples: list[np.ndarray] = []
    acceptances: list[float] = []
    for sweep in range(measure):
        acceptances.append(residual_sweep(links, rng, epsilon, marked_face))
        if (sweep + 1) % sample_every == 0:
            incoming = character_vector(links[0], marked_face)
            outgoing = character_vector(links[1], marked_face)
            samples.append(np.outer(np.conjugate(outgoing), incoming))
    return Chain(
        seed=seed,
        marked_face=marked_face,
        initial=initial,
        acceptance=float(np.mean(acceptances)),
        matrices=np.array(samples),
    )


def block_matrices(chains: list[Chain], blocks_per_chain: int) -> np.ndarray:
    blocks: list[np.ndarray] = []
    for chain in chains:
        size = len(chain.matrices) // blocks_per_chain
        if size < 2:
            raise ValueError("insufficient samples per block")
        for block in range(blocks_per_chain):
            lo = block * size
            hi = len(chain.matrices) if block == blocks_per_chain - 1 else (block + 1) * size
            blocks.append(np.mean(chain.matrices[lo:hi], axis=0))
    return np.array(blocks)


def normalized_matrix(mean_matrix: np.ndarray) -> np.ndarray:
    return mean_matrix / mean_matrix[0, 0]


def jackknife_matrix(blocks: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = len(blocks)
    total = np.sum(blocks, axis=0)
    leave = np.array([normalized_matrix((total - blocks[i]) / (n - 1)) for i in range(n)])
    center = normalized_matrix(np.mean(blocks, axis=0))
    err = np.sqrt(
        (n - 1) / n
        * np.sum(np.abs(leave - np.mean(leave, axis=0)) ** 2, axis=0)
    )
    return center, err.real


def implementation_checks() -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []
    rng = np.random.default_rng(8803)
    links = np.array(
        [[random_haar_su3(rng) for _ in range(3 * L**3)] for _ in range(2)]
    )
    marked_face = 0
    before = residual_log_weight(links, marked_face)
    tau, link_id = 1, 17
    old = links[tau, link_id].copy()
    active_spatial = [f for f in LINK_TO_FACES[link_id] if f != marked_face]
    old_local = (BETA / 6.0) * sum(spatial_real_trace(links[tau], f) for f in active_spatial)
    if link_id not in marked_links(marked_face):
        old_local += (BETA / 3.0) * np.trace(
            links[1, link_id] @ links[0, link_id].conj().T
        ).real
    links[tau, link_id] = random_su2_subgroup_step(rng, 0.25) @ old
    new_local = (BETA / 6.0) * sum(spatial_real_trace(links[tau], f) for f in active_spatial)
    if link_id not in marked_links(marked_face):
        new_local += (BETA / 3.0) * np.trace(
            links[1, link_id] @ links[0, link_id].conj().T
        ).real
    after = residual_log_weight(links, marked_face)
    residual = abs((after - before) - (new_local - old_local))
    checks.append(("local update delta equals full literal-deletion weight delta", residual < 1e-11, f"residual={residual:.3e}"))

    boundary = marked_links(marked_face)
    checks.append(("literal-deletion census is 80+80 spatial half-factors and 77 mixed factors", len(FACES)-1 == 80 and 3*L**3-len(boundary) == 77, f"spatial=80+80 mixed={3*L**3-len(boundary)}"))
    return checks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--therm", type=int, default=900)
    parser.add_argument("--measure", type=int, default=3200)
    parser.add_argument("--sample-every", type=int, default=4)
    parser.add_argument("--blocks-per-chain", type=int, default=12)
    parser.add_argument("--chains", type=int, default=4, choices=(2, 4))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("=" * 79)
    print("L_s=3 TWO-SLICE LITERAL-FACTOR-DELETION MATRIX DISCRIMINATOR")
    print("=" * 79)
    print(
        f"beta={BETA}, chains={args.chains}, therm={args.therm}, "
        f"measure={args.measure}, sample_every={args.sample_every}"
    )
    passed = failed = 0
    print("\nImplementation checks")
    for name, ok, detail in implementation_checks():
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        passed += int(ok)
        failed += int(not ok)

    marked_faces = (0, 1, 27, 54)
    chains: list[Chain] = []
    print("\nIndependent literal-factor-deletion chains")
    for i, seed in enumerate(SEEDS[: args.chains]):
        chain = run_chain(
            seed,
            marked_faces[i],
            "cold" if i % 2 == 0 else "hot",
            args.therm,
            args.measure,
            args.sample_every,
        )
        chains.append(chain)
        diag = np.diag(normalized_matrix(np.mean(chain.matrices, axis=0)))
        print(
            f"  seed={seed} marked={marked_faces[i]:2d} init={chain.initial:4s} "
            f"acc={chain.acceptance:.3f} n={len(chain.matrices)} "
            f"diag10={diag[1].real:+.5f} diag01={diag[2].real:+.5f} "
            f"diag11={diag[3].real:+.5f}"
        )

    blocks = block_matrices(chains, args.blocks_per_chain)
    matrix, error = jackknife_matrix(blocks)
    print("\nNormalized literal-factor-deletion character matrix")
    for row, label in enumerate(TRACKED):
        cells = "  ".join(
            f"{matrix[row,col].real:+.5f}{matrix[row,col].imag:+.5f}i"
            for col in range(len(TRACKED))
        )
        print(f"  row {label}: {cells}")
    print("\nDiagonal with block-jackknife errors")
    for i, label in enumerate(TRACKED):
        print(
            f"  {label}: {matrix[i,i].real:+.7f} {matrix[i,i].imag:+.2e}i "
            f"+/- {error[i,i]:.3e}"
        )

    offdiag_mask = ~np.eye(len(TRACKED), dtype=bool)
    offdiag_z = np.abs(matrix[offdiag_mask]) / np.maximum(error[offdiag_mask], 1e-14)
    conjugate_diag_residual = abs(matrix[1, 1] - matrix[2, 2])
    conjugate_diag_error = math.sqrt(error[1, 1] ** 2 + error[2, 2] ** 2)
    checks = [
        ("trivial literal-deletion matrix element normalizes to one", abs(matrix[0,0]-1) < 1e-12, f"residual={abs(matrix[0,0]-1):.3e}"),
        ("all off-diagonal character elements are consistent with zero", float(np.max(offdiag_z)) < 4.0, f"max={float(np.max(offdiag_z)):.2f} SE"),
        ("fundamental and antifundamental diagonal elements agree", conjugate_diag_residual < 4.0 * conjugate_diag_error, f"residual={conjugate_diag_residual:.3e}, error={conjugate_diag_error:.3e}"),
        ("chain acceptance is nondegenerate", all(0.25 < c.acceptance < 0.80 for c in chains), f"range={min(c.acceptance for c in chains):.3f}..{max(c.acceptance for c in chains):.3f}"),
    ]
    print("\nDiscriminating checks")
    for name, ok, detail in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        passed += int(ok)
        failed += int(not ok)

    print("\nThis runner is not the algebraically stripped post-compression operator.")
    print("A nonzero off-diagonal element falsifies only the naive literal-deletion-as-convolution route.")
    print("A diagonal result cannot establish the desired residual equality by itself.")
    print(f"\nSUMMARY: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
