#!/usr/bin/env python3
"""Assess whether the atomic lane should move to larger continuum solves."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scoreboard-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_best_known_lane_scoreboard.json",
    )
    parser.add_argument(
        "--one-body-continuum-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_multi_family_continuum.json",
    )
    parser.add_argument(
        "--shell-continuum-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_projector_continuum_readout.json",
    )
    parser.add_argument(
        "--basis-robustness-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_basis_robustness.json",
    )
    parser.add_argument(
        "--softening-refit-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_softening_refit.json",
    )
    parser.add_argument(
        "--retuned-contact-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_contact_retune_round.json",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_next_phase_assessment.json",
    )
    args = parser.parse_args()

    scoreboard = read_json(args.scoreboard_json)
    continuum = read_json(args.one_body_continuum_json)
    basis = read_json(args.basis_robustness_json)
    softening = read_json(args.softening_refit_json)
    retuned = read_json(args.retuned_contact_json) if args.retuned_contact_json.exists() else {}
    shell_continuum = (
        read_json(args.shell_continuum_readout_json)
        if args.shell_continuum_readout_json.exists()
        else None
    )
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()

    best_full_lane = scoreboard["best_full_lane_entry"]
    if shell_continuum is not None:
        hydrogen_limit_error = float(
            shell_continuum["continuum_limit_accuracy_metrics"]["relative_errors"][
                "hydrogen_ground"
            ]
        )
        continuum_full_rms = float(
            shell_continuum["continuum_limit_accuracy_metrics"]["scores"][
                "full_rms_relative_error"
            ]
        )
    elif "best_surviving_candidate" in continuum and continuum["best_surviving_candidate"] is not None:
        continuum_row = continuum["best_surviving_candidate"]
        hydrogen_limit_error = continuum_row["observables"]["hydrogen_ground_magnitude"]["limit_relative_error"]
        continuum_full_rms = None
    elif "best_hydrogen_limit_candidate" in continuum:
        continuum_row = continuum["best_hydrogen_limit_candidate"]
        hydrogen_limit_error = continuum_row["observables"]["hydrogen_ground_magnitude"]["limit_relative_error"]
        continuum_full_rms = None
    else:
        hydrogen_limit_error = 1.0
        continuum_full_rms = None
    retuned_best = retuned.get("best_strong_candidate") or retuned.get("best_accepted_candidate")
    basis_accept_count = (
        int(retuned_best["accepted_basis_count"])
        if retuned_best is not None
        else len(basis["accepted_rows"])
    )
    softening_has_accept = softening["accepted_candidate"] is not None
    best_hydrogen_current_error = float(
        best_full_lane["relative_errors"].get("hydrogen_ground", 1.0)
    )
    best_full_current_rms = float(
        best_full_lane["scores"].get("full_rms_relative_error", 1.0)
    )
    hydrogen_target_error = min(float(hydrogen_limit_error), float(best_hydrogen_current_error))
    shell_continuum_helpful = bool(
        shell_continuum is not None
        and float(hydrogen_limit_error) < best_hydrogen_current_error
        and (
            continuum_full_rms is None
            or float(continuum_full_rms) < best_full_current_rms
        )
    )
    continuum_live_ready = bool(
        best_full_lane["label"] == "shell_projector_continuum_live"
        and basis_accept_count >= 2
        and shell_continuum_helpful
    )
    ready_for_large_continuum = bool(
        best_full_lane["label"] in ("retuned_contact_candidate", "shell_projector_candidate")
        and basis_accept_count >= 2
        and float(hydrogen_target_error) < 0.10
    )
    recommendation = (
        "retune_on_continuum_family"
        if continuum_live_ready
        else (
            "stay_on_model_improvement"
            if shell_continuum is not None and not shell_continuum_helpful
            else (
                "proceed_to_larger_continuum_solve"
                if ready_for_large_continuum
                else "stay_on_model_improvement"
            )
        )
    )
    reason = (
        f"The {best_full_lane['label']} lane now has a live continuum winner and the "
        "continuum limit projects additional hydrogen improvement, so the next move is "
        "to retune on the continuum family rather than widen the local model surface."
        if continuum_live_ready
        else (
            "The shell-projector continuum phase improved aggregate RMS but did not improve "
            "the hydrogen error, so the current "
            f"{best_full_lane['label']} point remains the live leader and the next move is "
            "model improvement, not a wider raw continuum sweep."
            if shell_continuum is not None and not shell_continuum_helpful
            else (
                f"The {best_full_lane['label']} lane is basis-stable enough and the remaining "
                "hydrogen target error is below the current larger-continuum trigger."
                if ready_for_large_continuum
                else "Hydrogen remains the dominant residual or the correlated model "
                "is not yet robust enough across basis/refit checks."
            )
        )
    )

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "best_full_lane_entry": best_full_lane,
        "hydrogen_continuum_limit_relative_error": hydrogen_limit_error,
        "hydrogen_target_relative_error": hydrogen_target_error,
        "continuum_limit_full_rms_relative_error": continuum_full_rms,
        "shell_continuum_helpful": shell_continuum_helpful,
        "basis_accept_count": basis_accept_count,
        "softening_has_accepted_refit": bool(softening_has_accept),
        "retuned_contact_present": bool(retuned_best is not None),
        "recommendation": recommendation,
        "reason": reason,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Next-Phase Assessment")
    print("============================")
    print(f"- Recommendation: {recommendation}.")
    print(f"- Reason: {reason}")
    print(f"- Wrote assessment to {args.write_json}.")


if __name__ == "__main__":
    main()
