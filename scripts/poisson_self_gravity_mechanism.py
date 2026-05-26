#!/usr/bin/env python3
"""Finite no-go certificate for the Poisson self-gravity mechanism row."""

from __future__ import annotations

# This runner reuses the existing exact-lattice implementation sources and
# executes several audit-window checks. The end-to-end Born diagnostic is the
# slow leg, so the audit lane should use the extended timeout.
AUDIT_TIMEOUT_SEC = 1800

from dataclasses import dataclass
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import scripts.poisson_self_gravity_born_audit as born  # noqa: E402
import scripts.poisson_self_gravity_loop as loop  # noqa: E402
import scripts.poisson_self_gravity_loop_v3 as v3  # noqa: E402


@dataclass(frozen=True)
class Check:
    name: str
    ok: bool
    detail: str


class Checkbook:
    def __init__(self) -> None:
        self.checks: list[Check] = []

    def require(self, name: str, ok: bool, detail: str) -> None:
        self.checks.append(Check(name, bool(ok), detail))

    @property
    def pass_count(self) -> int:
        return sum(1 for check in self.checks if check.ok)

    @property
    def fail_count(self) -> int:
        return sum(1 for check in self.checks if not check.ok)

    def report(self) -> None:
        print("CHECK SUMMARY")
        for check in self.checks:
            status = "PASS" if check.ok else "FAIL"
            print(f"  {status:4s} {check.name}: {check.detail}")


def _zero_field(lat) -> list[list[float]]:
    return [[0.0 for _ in range(lat.npl)] for _ in range(lat.nl)]


def _set_max_d(value: float) -> None:
    # The helper modules share scripts.minimal_source_driven_field_probe.
    # Reset the lattice depth before each packet so importing V3 does not
    # leak its tractability override into the loop or Born packets.
    loop.m.MAX_D_PHYS = value
    v3.m.MAX_D_PHYS = value
    born.m.MAX_D_PHYS = value


def _run_loop_packet(checks: Checkbook) -> dict[str, float]:
    _set_max_d(3.0)
    lat = loop.m.Lattice3D.build(loop.NL_PHYS, loop.PW, loop.H)
    source_nodes = loop._source_cluster_nodes(lat)
    origin = [lat.nmap[(0, 0, 0)]]
    zero = _zero_field(lat)
    free = loop._propagate_from_sources(lat, zero, loop.m.K, origin)
    z_free = loop._centroid_z(free, lat)
    p_free = loop._detector_prob(free, lat)

    ref_raw = loop._poisson_like_field(
        lat,
        source_nodes,
        [1.0 / len(source_nodes)] * len(source_nodes),
        max(loop.SOURCE_STRENGTHS) * max(loop.EPSILONS),
    )
    gain = loop.FIELD_TARGET_MAX / loop._field_abs_max(ref_raw)

    zero_loop_field, _, zero_converged, zero_iters, zero_residual = loop._self_consistent_loop(
        lat,
        0.0,
        0.0,
        source_nodes,
        gain,
        max_iters=loop.QUICK_MAX_ITERS,
    )
    zero_amps = loop._propagate_from_sources(lat, zero_loop_field, loop.m.K, origin)
    zero_delta = loop._centroid_z(zero_amps, lat) - z_free
    zero_escape = loop._detector_prob(zero_amps, lat) / p_free

    print("LOOP QUICK PACKET")
    print(f"  source nodes: {source_nodes}")
    print(f"  zero shift/escape: {zero_delta:+.3e} / {zero_escape:.12f}")
    print(f"  zero converged: {zero_converged} in {zero_iters} iters, residual={zero_residual:.3e}")

    checks.require(
        "loop exact-zero centroid",
        math.isclose(zero_delta, 0.0, abs_tol=loop.HARDBAR_ZERO_EPS_SHIFT),
        f"|shift|={abs(zero_delta):.3e}",
    )
    checks.require(
        "loop exact-zero escape",
        math.isclose(zero_escape, 1.0, abs_tol=loop.HARDBAR_ZERO_EPS_ESCAPE_DEV),
        f"|escape-1|={abs(zero_escape - 1.0):.3e}",
    )
    checks.require(
        "loop exact-zero convergence",
        zero_converged,
        f"converged={zero_converged}, residual={zero_residual:.3e}",
    )

    nonzero_rows: list[dict[str, float | bool]] = []
    for epsilon in loop.QUICK_EPSILONS:
        inst_vals: list[float] = []
        loop_vals: list[float] = []
        born_vals: list[float] = []
        escapes: list[float] = []
        converged_count = 0
        toward_count = 0

        for source_strength in loop.QUICK_SOURCE_STRENGTHS:
            inst_field = loop._poisson_like_field(
                lat,
                source_nodes,
                [1.0 / len(source_nodes)] * len(source_nodes),
                epsilon * source_strength * gain,
            )
            loop_field, _, converged, n_iter, residual = loop._self_consistent_loop(
                lat,
                source_strength,
                epsilon,
                source_nodes,
                gain,
                max_iters=loop.QUICK_MAX_ITERS,
            )
            inst_amps = loop._propagate_from_sources(lat, inst_field, loop.m.K, origin)
            loop_amps = loop._propagate_from_sources(lat, loop_field, loop.m.K, origin)

            inst_delta = loop._centroid_z(inst_amps, lat) - z_free
            loop_delta = loop._centroid_z(loop_amps, lat) - z_free
            born_i3 = loop._born_i3(loop_field, lat, loop.m.K)
            escape = loop._detector_prob(loop_amps, lat) / p_free

            inst_vals.append(inst_delta)
            loop_vals.append(loop_delta)
            born_vals.append(born_i3)
            escapes.append(escape)
            converged_count += int(converged)
            toward_count += int(loop_delta > 0.0)
            ratio = loop_delta / inst_delta if abs(inst_delta) > 1e-30 else math.nan
            nonzero_rows.append(
                {
                    "epsilon": epsilon,
                    "source_strength": source_strength,
                    "inst_delta": inst_delta,
                    "loop_delta": loop_delta,
                    "ratio": ratio,
                    "born_i3": born_i3,
                    "escape": escape,
                    "converged": converged,
                    "iters": n_iter,
                    "residual": residual,
                }
            )

        loop_alpha = loop._fit_power(list(loop.QUICK_SOURCE_STRENGTHS), [abs(v) for v in loop_vals])
        ratios = [abs(lv / iv) for lv, iv in zip(loop_vals, inst_vals) if abs(iv) > 1e-30]
        mean_ratio = sum(ratios) / len(ratios)
        max_born = max(born_vals)
        max_escape = max(escapes)
        lo_ratio, hi_ratio = loop.HARDBAR_LOOP_INST_RATIO
        lo_alpha, hi_alpha = loop.HARDBAR_MASS_LAW_EXP

        print(
            f"  eps={epsilon:.2f}: max Born={max_born:.3e}, "
            f"toward={toward_count}/{len(loop.QUICK_SOURCE_STRENGTHS)}, "
            f"mean |loop/inst|={mean_ratio:.3f}, alpha={loop_alpha:.3f}, "
            f"max escape={max_escape:.3f}, converged={converged_count}/{len(loop.QUICK_SOURCE_STRENGTHS)}"
        )

        checks.require(
            "loop frozen-field Born floor",
            max_born <= loop.HARDBAR_BORN_FROZEN,
            f"max I3/P={max_born:.3e}",
        )
        checks.require(
            "loop weak-field TOWARD sign",
            toward_count == len(loop.QUICK_SOURCE_STRENGTHS),
            f"toward={toward_count}/{len(loop.QUICK_SOURCE_STRENGTHS)}",
        )
        checks.require(
            "loop small-control ratio",
            lo_ratio <= mean_ratio <= hi_ratio,
            f"mean |loop/inst|={mean_ratio:.3f}",
        )
        checks.require(
            "loop near-linear mass exponent",
            loop_alpha is not None and lo_alpha <= loop_alpha <= hi_alpha,
            f"alpha={loop_alpha:.3f}" if loop_alpha is not None else "alpha=n/a",
        )
        checks.require(
            "loop nonzero rows not converged",
            converged_count == 0,
            f"converged={converged_count}/{len(loop.QUICK_SOURCE_STRENGTHS)} under quick cap",
        )

    return {
        "zero_delta": zero_delta,
        "zero_escape": zero_escape,
        "max_born": max(float(row["born_i3"]) for row in nonzero_rows),
        "max_escape": max(float(row["escape"]) for row in nonzero_rows),
        "max_ratio": max(abs(float(row["ratio"])) for row in nonzero_rows),
    }


def _run_v3_packet(checks: Checkbook) -> dict[str, float]:
    _set_max_d(2.0)
    lat = v3.m.Lattice3D.build(v3.NL_PHYS, v3.PW, v3.H)
    launch_nodes = [lat.nmap[(0, 0, 0)]]
    source_patch_nodes = v3._source_cluster_nodes(lat)
    det_line = v3._detector_line(lat)
    zero = _zero_field(lat)
    free = v3._propagate_from_sources(lat, zero, launch_nodes)
    z_free = v3._centroid_z(free, lat)
    p_free = v3._detector_prob(free, lat)

    ref_raw = v3._poisson_like_field(
        lat,
        source_patch_nodes,
        [1.0 / len(source_patch_nodes)] * len(source_patch_nodes),
        max(v3.QUICK_SOURCE_STRENGTHS) * max(v3.QUICK_EPSILONS),
    )
    gain = v3.FIELD_TARGET_MAX / v3._field_abs_max(ref_raw)

    null_field, _, null_conv, null_iters, null_resid, null_amps = v3._run_loop(
        lat,
        launch_nodes,
        source_patch_nodes,
        max(v3.QUICK_SOURCE_STRENGTHS),
        0.0,
        gain,
    )
    zero_delta = v3._centroid_z(null_amps, lat) - z_free
    zero_escape = v3._detector_prob(null_amps, lat) / p_free
    phase_slope, phase_r2, phase_span = v3._phase_ramp_metrics(lat, free, null_amps, det_line)

    print()
    print("V3 MATCHED-NULL PACKET")
    print(f"  source patch nodes: {source_patch_nodes}")
    print(
        f"  zero shift/escape/phase/span: {zero_delta:+.3e} / "
        f"{zero_escape:.12f} / {phase_slope:+.3e} / {phase_span:+.3e}"
    )
    print(f"  zero converged: {null_conv} in {null_iters} iters, residual={null_resid:.3e}, R2={phase_r2:.3f}")

    checks.require(
        "v3 exact-zero centroid",
        math.isclose(zero_delta, 0.0, abs_tol=1e-12),
        f"|shift|={abs(zero_delta):.3e}",
    )
    checks.require(
        "v3 exact-zero escape",
        math.isclose(zero_escape, 1.0, abs_tol=1e-12),
        f"|escape-1|={abs(zero_escape - 1.0):.3e}",
    )
    checks.require(
        "v3 matched-null phase zero",
        math.isclose(phase_slope, 0.0, abs_tol=1e-12)
        and math.isclose(phase_span, 0.0, abs_tol=1e-12),
        f"slope={phase_slope:+.3e}, span={phase_span:+.3e}",
    )
    checks.require(
        "v3 exact-zero convergence",
        null_conv,
        f"converged={null_conv}, residual={null_resid:.3e}",
    )

    nonzero_rows: list[dict[str, float | bool]] = []
    for epsilon in v3.QUICK_EPSILONS:
        for source_strength in v3.QUICK_SOURCE_STRENGTHS:
            coupled_field, _, converged, iters, residual, coupled_amps = v3._run_loop(
                lat,
                launch_nodes,
                source_patch_nodes,
                source_strength,
                epsilon,
                gain,
            )
            centroid = v3._centroid_z(coupled_amps, lat) - z_free
            null_centroid = v3._centroid_z(null_amps, lat) - z_free
            delta = centroid - null_centroid
            slope, r2, span = v3._phase_ramp_metrics(lat, null_amps, coupled_amps, det_line)
            escape = v3._detector_prob(coupled_amps, lat) / p_free
            print(
                f"  eps={epsilon:.2f} s={source_strength:.4f}: "
                f"delta={delta:+.3e}, phase={slope:+.3e}, span={span:+.3e}, "
                f"escape={escape:.3f}, converged={converged}, residual={residual:.3e}"
            )
            if epsilon > 0.0:
                nonzero_rows.append(
                    {
                        "delta": delta,
                        "slope": slope,
                        "span": span,
                        "escape": escape,
                        "converged": converged,
                        "iters": iters,
                        "residual": residual,
                        "r2": r2,
                    }
                )

    max_delta = max(abs(float(row["delta"])) for row in nonzero_rows)
    max_span = max(abs(float(row["span"])) for row in nonzero_rows)
    max_escape = max(float(row["escape"]) for row in nonzero_rows)
    conv_count = sum(1 for row in nonzero_rows if bool(row["converged"]))

    checks.require(
        "v3 nonzero rows not converged",
        conv_count == 0,
        f"converged={conv_count}/{len(nonzero_rows)}",
    )
    checks.require(
        "v3 stronger centroid observable",
        all(float(row["delta"]) > 0.0 for row in nonzero_rows),
        f"max |delta|={max_delta:.3e}",
    )
    checks.require(
        "v3 phase-ramp observable",
        all(abs(float(row["span"])) >= 1e-3 for row in nonzero_rows),
        f"max |span|={max_span:.3e}",
    )
    checks.require(
        "v3 effect remains control-size",
        max_delta <= 5e-2 and max_escape <= 1.25,
        f"max |delta|={max_delta:.3e}, max escape={max_escape:.3f}",
    )

    return {
        "zero_delta": zero_delta,
        "zero_escape": zero_escape,
        "max_delta": max_delta,
        "max_span": max_span,
        "max_escape": max_escape,
    }


def _run_born_packet(checks: Checkbook) -> dict[str, float]:
    _set_max_d(3.0)
    lat = born.m.Lattice3D.build(born.NL_PHYS, born.PW, born.H)
    slit_nodes = born._slit_nodes(lat)
    zero = _zero_field(lat)
    free_slit_amps = born._propagate_from_sources(lat, zero, slit_nodes)
    z_free = born._centroid_z(free_slit_amps, lat)
    p_free = born._detector_prob(free_slit_amps, lat)

    ref_raw = born._poisson_like_field(
        lat,
        slit_nodes,
        [1.0 / len(slit_nodes)] * len(slit_nodes),
        max(born.SOURCE_STRENGTHS) * max(born.EPSILONS),
    )
    gain = born.FIELD_TARGET_MAX / born._field_abs_max(ref_raw)

    zero_field, zero_conv, zero_iters, zero_resid, zero_amps = born._iterate_loop(
        lat,
        slit_nodes,
        max(born.SOURCE_STRENGTHS),
        0.0,
        gain,
    )
    zero_delta = born._centroid_z(zero_amps, lat) - z_free
    zero_escape = born._detector_prob(zero_amps, lat) / p_free
    zero_born = born._born_i3(zero_field, lat, slit_nodes)

    print()
    print("END-TO-END BORN DIAGNOSTIC PACKET")
    print(f"  slit nodes: {slit_nodes}")
    print(
        f"  zero shift/escape/Born: {zero_delta:+.3e} / "
        f"{zero_escape:.12f} / {zero_born:.3e}"
    )
    print(f"  zero converged: {zero_conv} in {zero_iters} iters, residual={zero_resid:.3e}")

    checks.require(
        "born exact-zero centroid",
        math.isclose(zero_delta, 0.0, abs_tol=1e-12),
        f"|shift|={abs(zero_delta):.3e}",
    )
    checks.require(
        "born exact-zero escape",
        math.isclose(zero_escape, 1.0, abs_tol=1e-12),
        f"|escape-1|={abs(zero_escape - 1.0):.3e}",
    )
    checks.require(
        "born exact-zero convergence",
        zero_conv,
        f"converged={zero_conv}, residual={zero_resid:.3e}",
    )

    source_strength = born.SOURCE_STRENGTHS[0]
    epsilon = born.EPSILONS[0]
    abc_field, step_conv, step_iters, step_resid, _ = born._iterate_loop(
        lat,
        slit_nodes,
        source_strength,
        epsilon,
        gain,
    )
    step_born = born._born_i3(abc_field, lat, slit_nodes)

    subset_probs: dict[str, float] = {}
    subset_conv: dict[str, bool] = {}
    subset_iters: dict[str, int] = {}
    for mask in (1, 2, 4, 3, 5, 6, 7):
        open_nodes = [slit_nodes[i] for i in range(3) if mask & (1 << i)]
        field, converged, n_iter, resid, amps = born._iterate_loop(
            lat,
            open_nodes,
            source_strength,
            epsilon,
            gain,
        )
        key = "".join(ch for ch, bit in zip("abc", (1, 2, 4)) if mask & bit)
        subset_probs[key] = born._detector_prob(amps, lat)
        subset_conv[key] = converged
        subset_iters[key] = n_iter

    p_a = subset_probs["a"]
    p_b = subset_probs["b"]
    p_c = subset_probs["c"]
    p_ab = subset_probs["ab"]
    p_ac = subset_probs["ac"]
    p_bc = subset_probs["bc"]
    p_abc = subset_probs["abc"]
    end_i3 = abs(p_abc - p_ab - p_ac - p_bc + p_a + p_b + p_c) / p_abc
    end_conv = all(subset_conv.values())
    max_end_iters = max(subset_iters.values())

    print(
        f"  eps={epsilon:.2f} s={source_strength:.4f}: "
        f"step Born={step_born:.3e}, step converged={step_conv}, "
        f"end Born={end_i3:.3e}, end converged={end_conv}, "
        f"end max iters={max_end_iters}, step residual={step_resid:.3e}"
    )

    checks.require(
        "born step-local Born floor",
        step_born <= 1e-10,
        f"step I3/P={step_born:.3e}, step converged={step_conv}",
    )
    checks.require(
        "born end-to-end diagnostic nonzero",
        end_i3 >= 1e-7,
        f"end I3/P={end_i3:.3e}",
    )
    checks.require(
        "born end-to-end nonconverged",
        not end_conv,
        f"end converged={end_conv}, max subset iters={max_end_iters}",
    )

    return {
        "zero_delta": zero_delta,
        "zero_escape": zero_escape,
        "zero_born": zero_born,
        "step_born": step_born,
        "end_born": end_i3,
    }


def _note_hygiene_checks(checks: Checkbook) -> None:
    note_path = os.path.join(ROOT, "docs", "POISSON_SELF_GRAVITY_MECHANISM_NOTE.md")
    with open(note_path, "r", encoding="utf-8") as handle:
        text = handle.read()
    checks.require(
        "note declares no_go",
        "**Claim type:** no_go" in text,
        "claim type marker present",
    )
    checks.require(
        "note states no new axiom",
        "No new axiom" in text,
        "no-new-axiom sentence present",
    )
    checks.require(
        "note removes retained evidence section",
        "## Retained Evidence" not in text,
        "old retained-evidence heading absent",
    )
    checks.require(
        "note preserves audit authority boundary",
        "audit-ratified self-gravity mechanism claim" in text,
        "audit authority boundary present",
    )


def main() -> None:
    checks = Checkbook()

    print("=" * 96)
    print("POISSON SELF-GRAVITY MECHANISM FINITE CONTROL NO-GO")
    print("  recomputes the mechanism hard bars; no hard-coded MechanismVerdict")
    print("=" * 96)

    loop_packet = _run_loop_packet(checks)
    v3_packet = _run_v3_packet(checks)
    born_packet = _run_born_packet(checks)
    _note_hygiene_checks(checks)

    print()
    print("FINITE NO-GO READ")
    print(f"  loop max frozen Born I3/P:       {loop_packet['max_born']:.3e}")
    print(f"  loop max escape ratio:           {loop_packet['max_escape']:.3f}")
    print(f"  V3 max matched-null centroid:    {v3_packet['max_delta']:.3e}")
    print(f"  V3 max phase span:               {v3_packet['max_span']:.3e}")
    print(f"  end-to-end diagnostic Born I3/P: {born_packet['end_born']:.3e}")
    print("  mechanism closure: blocked on nonconverged nonzero loops and diagnostic-only end-to-end Born")
    print()

    checks.report()
    print()
    print(f"RUNNER STATUS: {'PASS' if checks.fail_count == 0 else 'FAIL'} (PASS={checks.pass_count} FAIL={checks.fail_count})")
    if checks.fail_count:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
