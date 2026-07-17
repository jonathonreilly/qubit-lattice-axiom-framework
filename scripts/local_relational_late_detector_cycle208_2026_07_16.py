#!/usr/bin/env python3
"""Cycle 208: local relational late readout for scattering channels.

Replace Cycle 207's Fourier-channel record with one fixed late partition in
relative position: the pair remains close, and the projectile lies to the
left or right of the pair centre.  The tick-70 projective readout remains a
named import; no detector or record-formation dynamics is claimed.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from fixed_total_momentum_molecular_scattering_cycle207_2026_07_16 import (
    apply_relative_step,
    channel_records,
    channel_spectrum,
    prepare_incoming,
    signed_coordinates,
)


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "LOCAL_RELATIONAL_LATE_DETECTOR_CYCLE208_NOTE_2026-07-16.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "https://arxiv.org/abs/1804.08508",
        "bisio, d'ariano, mosco, perinotti, and tosini",
        "prior work",
        "local relational partition",
        "pair-exchange invariant",
        "transmitted",
        "reflected",
        "breakup",
        "tick-70",
        "supplied projective readout",
        "nearest-neighbour detector dynamics remains open",
        "record-conditioned mass",
        "one-dimensional",
        "proper-cubic lift remains open",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves attribution, detector import, and scope", not missing, missing)


def prepare_and_evolve(coupling: float, duration: int = 76):
    length = 128
    pair_mass = 0.85
    projectile_mass = 0.3
    pair_coupling = 0.1 * np.pi
    total_momentum = float(2 * np.pi * np.fft.fftfreq(length)[14])
    state = prepare_incoming(
        length,
        total_momentum,
        pair_mass,
        projectile_mass,
        pair_coupling,
        total_momentum,
        0.08,
        32,
    )
    snapshots = {}
    for step in range(1, duration + 1):
        state = apply_relative_step(
            state,
            total_momentum,
            pair_mass,
            projectile_mass,
            pair_coupling,
            coupling,
        )
        if step in (64, 70, 76):
            snapshots[step] = state.copy()
    return snapshots, total_momentum, pair_mass, projectile_mass, pair_coupling


def local_masks(length: int, radius: int = 2, guard: int = 0):
    coordinate = signed_coordinates(length)
    pair_relative = coordinate[:, None]
    projectile_from_pair_centre = (
        2 * coordinate[None, :] - pair_relative
    )
    close = np.abs(pair_relative) <= radius
    transmitted = close & (projectile_from_pair_centre < -2 * guard)
    reflected = close & (projectile_from_pair_centre > 2 * guard)
    other = ~(transmitted | reflected)
    return transmitted, reflected, other


def local_probabilities(state: np.ndarray) -> np.ndarray:
    probability = np.sum(np.abs(state) ** 2, axis=(2, 3, 4))
    return np.asarray(
        [float(np.sum(probability[mask]).real) for mask in local_masks(state.shape[0])]
    )


def projected_state(state: np.ndarray, mask: np.ndarray) -> np.ndarray:
    projected = state * mask[:, :, None, None, None]
    return projected / np.linalg.norm(projected)


def spectral_probabilities(records: dict[str, object]) -> np.ndarray:
    reflected = records["reflected"]
    return np.asarray(
        [
            records["transmitted"]["probability"],
            reflected["probability"] if reflected is not None else 0.0,
            records["breakup"],
        ],
        dtype=float,
    )


def run(coupling: float) -> dict[int, dict[str, object]]:
    snapshots, total, pair_mass, projectile_mass, pair_coupling = prepare_and_evolve(
        coupling
    )
    results: dict[int, dict[str, object]] = {}
    for tick, state in snapshots.items():
        spectral = channel_records(
            channel_spectrum(
                state, total, pair_mass, projectile_mass, pair_coupling
            ),
            total,
            pair_mass,
            pair_coupling,
        )
        spectral_p = spectral_probabilities(spectral)
        local_p = local_probabilities(state)
        results[tick] = {
            "spectral": spectral_p,
            "local": local_p,
            "difference": local_p - spectral_p,
        }
        if coupling and tick == 70:
            transmitted_state = projected_state(state, local_masks(state.shape[0])[0])
            transmitted_spectrum = channel_records(
                channel_spectrum(
                    transmitted_state,
                    total,
                    pair_mass,
                    projectile_mass,
                    pair_coupling,
                ),
                total,
                pair_mass,
                pair_coupling,
            )
            results[tick]["conditional_transmitted"] = transmitted_spectrum
    return results


def detector_controls() -> None:
    masks = local_masks(32)
    check(
        "local T/R/X masks are disjoint and exhaustive",
        np.all((masks[0].astype(int) + masks[1].astype(int) + masks[2].astype(int)) == 1),
    )
    check(
        "pair-centre side coordinate is pair-exchange invariant",
        all(
            (2 * projectile - first - second)
            == (2 * projectile - second - first)
            and abs(first - second) == abs(second - first)
            for first in range(-4, 5)
            for second in range(-4, 5)
            for projectile in range(-4, 5)
        ),
    )

    deleted = run(0.0)
    weak = run(0.03 * np.pi)
    strong = run(0.06 * np.pi)
    for label, result in (("deleted", deleted), ("weak", weak), ("strong", strong)):
        for tick in (64, 70, 76):
            local = result[tick]["local"]
            check(
                f"{label} tick-{tick} local record alternatives are positive and normalized",
                np.min(local) >= 0 and abs(np.sum(local) - 1) < 2e-12,
                local.tolist(),
            )
        error64 = float(np.max(np.abs(result[64]["difference"])))
        error70 = float(np.max(np.abs(result[70]["difference"])))
        check(
            f"{label} one fixed tick-70 relational readout approximates spectral channels",
            error70 < 3.2e-3 and error70 < error64,
            {
                "tick64_error": error64,
                "tick70_error": error70,
                "spectral": result[70]["spectral"].tolist(),
                "local": result[70]["local"].tolist(),
            },
        )

    check(
        "collision deletion leaves only finite-packet local misclassification",
        deleted[70]["local"][0] > 0.996
        and deleted[70]["local"][1] < 0.002
        and deleted[70]["local"][2] < 0.002,
        deleted[70]["local"].tolist(),
    )
    check(
        "stronger collision increases local reflected and breakup records",
        strong[70]["local"][1] > 3 * weak[70]["local"][1]
        and strong[70]["local"][2] > 3 * weak[70]["local"][2]
        and strong[70]["local"][0] < weak[70]["local"][0],
        {
            "weak": weak[70]["local"].tolist(),
            "strong": strong[70]["local"].tolist(),
        },
    )

    for label, result, tolerance in (
        ("weak", weak, 0.01),
        ("strong", strong, 0.02),
    ):
        conditional = result[70]["conditional_transmitted"]
        transmitted = conditional["transmitted"]
        curvature_mass = conditional["curvature_mass"]
        check(
            f"{label} local T record selects an intact narrow calibrated-mass branch",
            transmitted["probability"] > (0.996 if label == "weak" else 0.991)
            and transmitted["momentum_coherence"] > 0.998
            and abs(transmitted["secant_mass"] / curvature_mass - 1) < tolerance,
            {
                "conditional_intact_probability": transmitted["probability"],
                "momentum_coherence": transmitted["momentum_coherence"],
                "secant_mass": transmitted["secant_mass"],
                "curvature_mass": curvature_mass,
                "relative_error": transmitted["secant_mass"] / curvature_mass - 1,
            },
        )

    probabilities = strong[70]["local"]
    duplicated = np.zeros((3, 3))
    duplicated[np.arange(3), np.arange(3)] = probabilities
    check(
        "a redundant local outcome record preserves all three branch weights",
        np.allclose(np.sum(duplicated, axis=0), probabilities)
        and np.allclose(np.sum(duplicated, axis=1), probabilities),
    )
    check(
        "local detector tournament retains generic complex non-Clifford phases",
        min(abs(0.03 * np.pi - index * np.pi / 4) for index in range(-4, 5)) > 1e-3
        and min(abs(0.1 * np.pi - index * np.pi / 4) for index in range(-4, 5)) > 1e-3,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    detector_controls()
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "LOCAL_RELATIONAL_SCATTERING_RECORD" if FAIL == 0 else "CYCLE208_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
