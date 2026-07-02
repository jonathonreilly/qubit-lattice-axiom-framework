#!/usr/bin/env python3
"""Bounded one-parameter reduced sewing-shell law on the star-supported source class.

This primary runner now consumes the self-contained replay module added on
2026-06-17, rather than importing the five older frontier helper modules. The
scientific scope is unchanged:

1. Every star-support point-Green column has unit total charge and induces the
   same normalized reduced shell law.
2. By linearity, any star-supported source on this reduced surface has sewing
   law fixed by total charge Q alone.
3. The admitted local O_h and finite-rank source-family comparators satisfy the
   same reduced one-parameter law to machine precision.

This remains bounded reduced-shell support, not full nonlinear GR closure.
"""

from __future__ import annotations

from dataclasses import dataclass

import frontier_one_parameter_reduced_shell_law_self_contained_replay_2026_06_17 as replay


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "FINITE") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


def main() -> None:
    print("Bounded one-parameter reduced sewing-shell law")
    print("=" * 72)
    print("source packet: self-contained 2026-06-17 finite-operator replay")

    columns = replay.build_point_green_columns(15)
    point_data = [replay.reduced_data(col) for col in columns]
    ref = point_data[0]

    point_charge_diff = max(abs(float(d["Q"]) - 1.0) for d in point_data)
    point_rad_diff = max(
        replay.max_profile_diff(ref["radial_profile"], d["radial_profile"])
        for d in point_data
    )
    point_mode_diff = max(
        replay.max_mode_diff(ref["norm_orbit"], d["norm_orbit"]) for d in point_data
    )
    point_shell_diff = max(
        replay.max_profile_diff(ref["mean_shell"], d["mean_shell"]) for d in point_data
    )
    point_aniso_diff = max(
        replay.max_profile_diff(ref["mean_aniso"], d["mean_aniso"]) for d in point_data
    )
    c_aniso = float(ref["anchor_per_Q"])

    family_oh = replay.reduced_data(replay.build_best_oh_phi_grid())
    family_fr = replay.reduced_data(replay.build_finite_rank_phi_grid())
    families = [family_oh, family_fr]
    family_rad_diff = max(
        replay.max_profile_diff(ref["radial_profile"], fam["radial_profile"])
        for fam in families
    )
    family_mode_diff = max(
        replay.max_mode_diff(ref["norm_orbit"], fam["norm_orbit"]) for fam in families
    )
    family_shell_diff = max(
        replay.max_profile_diff(ref["mean_shell"], fam["mean_shell"]) for fam in families
    )
    family_aniso_diff = max(
        replay.max_profile_diff(ref["mean_aniso"], fam["mean_aniso"]) for fam in families
    )
    family_c_diff = max(abs(float(fam["anchor_per_Q"]) - c_aniso) for fam in families)

    print(f"c_aniso = {c_aniso:.15f}")
    print(f"max point-column charge difference from unity = {point_charge_diff:.3e}")
    print(f"max point-column radial-profile difference = {point_rad_diff:.3e}")
    print(f"max point-column orbit-mode difference = {point_mode_diff:.3e}")
    print(f"max point-column shell-mean total-field difference = {point_shell_diff:.3e}")
    print(f"max point-column shell-mean anisotropic-field difference = {point_aniso_diff:.3e}")
    print(f"max family-vs-reference c_aniso difference = {family_c_diff:.3e}")

    record(
        "all seven point-Green columns carry unit total charge",
        point_charge_diff < 1e-12,
        f"max |Q-1| across columns = {point_charge_diff:.3e}",
    )
    record(
        "all seven point-Green columns induce the same radial shell kernel per unit charge",
        point_rad_diff < 1e-12,
        f"max radial-profile difference = {point_rad_diff:.3e}",
    )
    record(
        "all seven point-Green columns induce the same anisotropic orbit mode per unit charge",
        point_mode_diff < 1e-12,
        f"max orbit-mode difference = {point_mode_diff:.3e}",
    )
    record(
        "all seven point-Green columns induce the same shell-mean exterior response per unit charge",
        point_shell_diff < 1e-12 and point_aniso_diff < 1e-12,
        (
            f"max total-field difference = {point_shell_diff:.3e}, "
            f"max anisotropic-field difference = {point_aniso_diff:.3e}"
        ),
    )
    record(
        "the anisotropic anchor amplitude obeys A_aniso = c_aniso * Q with one computed finite-lattice constant",
        point_mode_diff < 1e-12 and point_charge_diff < 1e-12,
        f"c_aniso = {c_aniso:.15f}",
    )
    record(
        "the admitted local O_h and finite-rank source-family comparators satisfy the same one-parameter reduced shell law",
        family_rad_diff < 1e-12
        and family_mode_diff < 1e-12
        and family_shell_diff < 1e-12
        and family_aniso_diff < 1e-12
        and family_c_diff < 1e-12,
        (
            f"radial={family_rad_diff:.3e}, orbit={family_mode_diff:.3e}, "
            f"shell={family_shell_diff:.3e}, aniso={family_aniso_diff:.3e}, "
            f"c_diff={family_c_diff:.3e}"
        ),
    )
    record(
        "on the reduced surface the sewing-shell law behaves like one isotropic shell density plus one cubic shear mode tied to total charge",
        family_mode_diff < 1e-12 and family_c_diff < 1e-12,
        f"c_aniso = {c_aniso:.15f}",
        status="BOUNDED",
    )

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    n_pass = sum(c.ok for c in CHECKS)
    n_fail = sum(not c.ok for c in CHECKS)
    print(f"PASS={n_pass} FAIL={n_fail} TOTAL={len(CHECKS)}")
    if n_fail == 0:
        print("All checks passed.")
    else:
        print("Some checks failed.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
