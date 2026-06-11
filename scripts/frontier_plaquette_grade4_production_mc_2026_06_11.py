#!/usr/bin/env python3
"""Grade-4 SU(3) beta=6 plaquette production runner.

This is the production harness for the pre-registered Stage-1 protocol in
docs/PLAQUETTE_MC_CERTIFICATION_PROTOCOL_NOTE_2026-06-11.md.  It reuses the
compiled Cabibbo-Marinari heatbath + subgroup overrelaxation kernels from
scripts/alpha_s_numba_wilson_loop_mc.py, but records the full Wilson
plaquette observable directly instead of Wilson-loop spectroscopy.

The runner is designed for long unattended use:

* deterministic seeds, recorded in every stream artifact;
* cold/hot starts per volume;
* checkpoint/resume for the active stream;
* per-stream autocorrelation/error estimates;
* a combined finite-volume fit P_L = P_inf + c L^-4;
* a frozen decision-band readout against the protocol's Grade-4 bands.

It does not set audit status.  The output is a reviewable MC asset for the
independent audit lane.
"""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path
from typing import Any

import numpy as np

import alpha_s_numba_wilson_loop_mc as mc


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "outputs" / "plaquette_mc_grade4_2026_06_11"
P_LICENSED = 0.5934
P_NEEDED_F4 = 0.5934379
GRADE4_BUDGET = 5.0e-5
GRADE5_BUDGET = 5.0e-6
Z_SCORE = 2.0


def log(msg: str) -> None:
    print(f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {msg}", flush=True)


def json_sanitize(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {str(k): json_sanitize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [json_sanitize(v) for v in obj]
    if isinstance(obj, np.ndarray):
        return json_sanitize(obj.tolist())
    if isinstance(obj, np.generic):
        return json_sanitize(obj.item())
    if isinstance(obj, Path):
        return str(obj)
    if isinstance(obj, float):
        return obj if math.isfinite(obj) else None
    return obj


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(json_sanitize(obj), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_csv_ints(text: str) -> list[int]:
    vals = [int(part.strip()) for part in text.split(",") if part.strip()]
    if not vals:
        raise argparse.ArgumentTypeError("expected at least one integer")
    if any(v < 2 for v in vals):
        raise argparse.ArgumentTypeError("all lattice sizes must be >= 2")
    return vals


def parse_starts(text: str) -> list[str]:
    vals = [part.strip().lower() for part in text.split(",") if part.strip()]
    allowed = {"cold", "hot"}
    if not vals or any(v not in allowed for v in vals):
        raise argparse.ArgumentTypeError("starts must be comma-separated from {cold,hot}")
    return vals


def batched_project_su3(z: np.ndarray) -> np.ndarray:
    q, r = np.linalg.qr(z)
    diag = np.diagonal(r, axis1=-2, axis2=-1)
    phase = diag / np.where(np.abs(diag) == 0.0, 1.0, np.abs(diag))
    q = q * np.conj(phase)[..., None, :]
    detq = np.linalg.det(q)
    return q * np.exp(-1j * np.angle(detq) / 3.0)[..., None, None]


def hot_links(dims: tuple[int, int, int, int], seed: int, chunk: int) -> np.ndarray:
    vol = math.prod(dims)
    out = np.empty((vol, mc.NDIM, mc.NC, mc.NC), dtype=np.complex128)
    flat = out.reshape((vol * mc.NDIM, mc.NC, mc.NC))
    rng = np.random.default_rng(seed)
    for start in range(0, flat.shape[0], chunk):
        stop = min(start + chunk, flat.shape[0])
        z = rng.normal(size=(stop - start, 3, 3)) + 1j * rng.normal(size=(stop - start, 3, 3))
        flat[start:stop] = batched_project_su3(z)
    return out


def autocorrelation(values: np.ndarray, max_lag: int) -> list[float]:
    x = np.asarray(values, dtype=np.float64)
    x = x[np.isfinite(x)]
    n = len(x)
    if n < 3:
        return []
    x = x - float(np.mean(x))
    var = float(np.dot(x, x) / n)
    if var <= 0.0:
        return [1.0] + [0.0] * min(max_lag, n - 1)
    out: list[float] = []
    for lag in range(min(max_lag, n - 1) + 1):
        out.append(float(np.dot(x[: n - lag], x[lag:]) / ((n - lag) * var)))
    return out


def tau_int_windowed(values: np.ndarray, max_lag: int, window_factor: float) -> dict[str, Any]:
    rho = autocorrelation(values, max_lag)
    if not rho:
        return {"tau_int": None, "window": None, "rho_first_10": []}
    tau = 0.5
    window = 0
    for lag in range(1, len(rho)):
        if rho[lag] <= 0.0:
            window = lag - 1
            break
        tau += rho[lag]
        window = lag
        if lag >= window_factor * tau:
            break
    return {
        "tau_int": float(max(tau, 0.5)),
        "window": int(window),
        "rho_first_10": [float(x) for x in rho[:10]],
    }


def stream_stats(values: list[float], max_lag: int, window_factor: float) -> dict[str, Any]:
    arr = np.asarray(values, dtype=np.float64)
    mean = float(arr.mean()) if len(arr) else float("nan")
    std = float(arr.std(ddof=1)) if len(arr) > 1 else float("nan")
    tau = tau_int_windowed(arr, max_lag=max_lag, window_factor=window_factor)
    tau_val = tau.get("tau_int")
    if isinstance(tau_val, float) and len(arr) > 1 and math.isfinite(std):
        stderr_tau = std * math.sqrt(2.0 * tau_val / len(arr))
        stderr_naive = std / math.sqrt(len(arr))
    else:
        stderr_tau = float("nan")
        stderr_naive = float("nan")
    return {
        "n": int(len(arr)),
        "mean": mean,
        "std_per_measurement": std,
        "stderr_naive": stderr_naive,
        "stderr_tau": stderr_tau,
        "z2_stat_error": Z_SCORE * stderr_tau if math.isfinite(stderr_tau) else None,
        "autocorrelation": tau,
    }


def checkpoint_write(path: Path, dims: tuple[int, int, int, int], u: np.ndarray, plaquettes: list[float], therm_done: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp.npz")
    np.savez(
        tmp,
        dims=np.asarray(dims, dtype=np.int64),
        u=u,
        plaquettes=np.asarray(plaquettes, dtype=np.float64),
        therm_done=np.asarray(therm_done),
        saved_at_utc=np.asarray(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())),
    )
    tmp.replace(path)


def checkpoint_load(path: Path, dims: tuple[int, int, int, int]) -> tuple[np.ndarray, list[float], bool]:
    chk = np.load(path, allow_pickle=False)
    saved_dims = tuple(int(x) for x in chk["dims"].tolist())
    if saved_dims != dims:
        raise ValueError(f"checkpoint dims {saved_dims} do not match requested dims {dims}")
    return chk["u"], [float(x) for x in chk["plaquettes"].tolist()], bool(chk["therm_done"])


def make_initial_links(args: argparse.Namespace, dims: tuple[int, int, int, int], start_kind: str, seed: int) -> np.ndarray:
    if start_kind == "cold":
        return mc.cold_links(dims)
    log(f"hot start init dims={dims} seed={seed}")
    return hot_links(dims, seed=seed, chunk=args.hot_chunk)


def run_stream(args: argparse.Namespace, L: int, start_kind: str, replica: int, stream_index: int) -> dict[str, Any]:
    dims = (L, L, L, L)
    stream_id = f"L{L}_{start_kind}_r{replica:02d}"
    output_path = args.output_dir / "streams" / f"{stream_id}.json"
    checkpoint_path = args.checkpoint_dir / f"{stream_id}.npz"
    if args.resume and output_path.exists():
        log(f"skip completed stream {stream_id}")
        return json.loads(output_path.read_text())

    fwd, bwd, parity = mc.build_neighbors(dims)
    seed = args.seed_base + stream_index * 1009 + (0 if start_kind == "cold" else 503)
    init_seed = seed + 17
    if args.resume and checkpoint_path.exists():
        u, plaquettes, therm_done = checkpoint_load(checkpoint_path, dims)
        log(f"resume stream {stream_id}: measurements={len(plaquettes)} therm_done={therm_done}")
    else:
        u = make_initial_links(args, dims, start_kind, init_seed)
        plaquettes = []
        therm_done = False

    mc.seed_numba_rng(seed)
    links_per_sweep = math.prod(dims) * mc.NDIM
    log(
        f"start stream={stream_id} dims={dims} beta={mc.BETA} links/sweep={links_per_sweep} "
        f"therm={args.therm} measurements={args.measurements} separation={args.separation} "
        f"overrelax={args.overrelax} seed={seed} threads={args.numba_threads}"
    )
    t0 = time.perf_counter()
    if not therm_done:
        for sweep in range(args.therm):
            mc.sweep_heatbath_overrelax_parallel(u, fwd, bwd, parity, mc.BETA, args.overrelax)
            if (sweep + 1) % args.progress_interval == 0:
                log(f"stream={stream_id} therm {sweep + 1}/{args.therm} P={mc.plaquette(u, fwd):.8f}")
        therm_done = True
        checkpoint_write(checkpoint_path, dims, u, plaquettes, therm_done)

    completed = len(plaquettes)
    for cfg in range(completed, args.measurements):
        for _ in range(args.separation):
            mc.sweep_heatbath_overrelax_parallel(u, fwd, bwd, parity, mc.BETA, args.overrelax)
        p = float(mc.plaquette(u, fwd))
        plaquettes.append(p)
        if (cfg + 1) % args.progress_interval == 0:
            stats = stream_stats(plaquettes, args.max_lag, args.window_factor)
            log(
                f"stream={stream_id} meas {cfg + 1}/{args.measurements} P={p:.8f} "
                f"mean={stats['mean']:.8f} stderr_tau={stats['stderr_tau']}"
            )
        if (cfg + 1) % args.checkpoint_every == 0:
            checkpoint_write(checkpoint_path, dims, u, plaquettes, therm_done)

    elapsed = time.perf_counter() - t0
    stats = stream_stats(plaquettes, args.max_lag, args.window_factor)
    result = {
        "kind": "plaquette_grade4_stream",
        "stream_id": stream_id,
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "dims": list(dims),
        "L": L,
        "beta": mc.BETA,
        "start": start_kind,
        "replica": replica,
        "seed": seed,
        "hot_init_seed": init_seed if start_kind == "hot" else None,
        "numba_threads": args.numba_threads,
        "therm_sweeps": args.therm,
        "measurement_count_target": args.measurements,
        "measurement_count_completed": len(plaquettes),
        "separation_sweeps": args.separation,
        "overrelax_sweeps_per_heatbath": args.overrelax,
        "plaquettes": plaquettes,
        "stats": stats,
        "elapsed_seconds": elapsed,
        "checkpoint_path": str(checkpoint_path),
        "update_algorithm": "numba_compiled_cabibbo_marinari_heatbath_plus_su2_subgroup_overrelaxation",
        "observable": "full Wilson plaquette average over all 6 orientations, Re Tr U_P / 3",
    }
    write_json(output_path, result)
    checkpoint_write(checkpoint_path, dims, u, plaquettes, therm_done)
    if not args.keep_checkpoints:
        checkpoint_path.unlink(missing_ok=True)
    log(f"wrote stream artifact {output_path}")
    return result


def combine_volume(streams: list[dict[str, Any]]) -> dict[str, Any]:
    L = int(streams[0]["L"])
    values = []
    stream_rows = []
    for row in streams:
        arr = np.asarray(row["plaquettes"], dtype=np.float64)
        values.append(arr)
        stream_rows.append(
            {
                "stream_id": row["stream_id"],
                "start": row["start"],
                "n": int(len(arr)),
                "mean": row["stats"]["mean"],
                "stderr_tau": row["stats"]["stderr_tau"],
                "tau_int": row["stats"]["autocorrelation"]["tau_int"],
            }
        )
    cat = np.concatenate(values) if values else np.asarray([], dtype=np.float64)
    stats = stream_stats(cat.tolist(), max_lag=min(200, max(1, len(cat) // 2)), window_factor=5.0)
    starts = {row["start"]: row for row in stream_rows}
    gate = None
    if "cold" in starts and "hot" in starts:
        c = starts["cold"]
        h = starts["hot"]
        ec = float(c["stderr_tau"]) if c["stderr_tau"] is not None else float("nan")
        eh = float(h["stderr_tau"]) if h["stderr_tau"] is not None else float("nan")
        combined = math.sqrt(ec * ec + eh * eh)
        diff = abs(float(c["mean"]) - float(h["mean"]))
        gate = {
            "cold_hot_mean_diff": diff,
            "combined_2sigma": 2.0 * combined if math.isfinite(combined) else None,
            "pass": bool(math.isfinite(combined) and diff <= 2.0 * combined),
        }
    return {
        "L": L,
        "dims": [L, L, L, L],
        "streams": stream_rows,
        "combined": stats,
        "start_state_gate": gate,
    }


def weighted_fit(volumes: list[dict[str, Any]]) -> dict[str, Any]:
    usable = []
    for row in volumes:
        mean = float(row["combined"]["mean"])
        err = row["combined"]["stderr_tau"]
        err = float(err) if err is not None else float("nan")
        if math.isfinite(mean) and math.isfinite(err) and err > 0:
            usable.append((int(row["L"]), mean, err))
    if len(usable) < 3:
        return {"status": "insufficient_volumes", "usable_points": len(usable)}
    x = np.asarray([L ** -4 for L, _, _ in usable], dtype=np.float64)
    y = np.asarray([m for _, m, _ in usable], dtype=np.float64)
    sigma = np.asarray([e for _, _, e in usable], dtype=np.float64)
    X = np.column_stack([np.ones_like(x), x])
    W = np.diag(1.0 / (sigma * sigma))
    cov = np.linalg.inv(X.T @ W @ X)
    beta = cov @ (X.T @ W @ y)
    resid = y - X @ beta
    chi2 = float(resid.T @ W @ resid)
    dof = max(0, len(usable) - 2)
    p_inf = float(beta[0])
    p_inf_stderr = float(math.sqrt(max(cov[0, 0], 0.0)))
    values_by_L = {L: m for L, m, _ in usable}
    l24_l32_shift = None
    if 24 in values_by_L and 32 in values_by_L:
        l24_l32_shift = abs(values_by_L[32] - values_by_L[24])
    z2_fit_error = Z_SCORE * p_inf_stderr
    fv_full_add = l24_l32_shift if l24_l32_shift is not None else float("inf")
    total_budget = z2_fit_error + fv_full_add
    return {
        "status": "fit",
        "usable_points": len(usable),
        "points": [{"L": L, "P_L": m, "stderr_tau": e, "x_L_minus4": L ** -4} for L, m, e in usable],
        "model": "P_L = P_inf + c L^-4",
        "P_inf": p_inf,
        "c": float(beta[1]),
        "P_inf_stderr_fit": p_inf_stderr,
        "z2_fit_error": z2_fit_error,
        "L24_L32_shift_full_systematic": l24_l32_shift,
        "total_grade_budget_z2_plus_full_shift": total_budget,
        "chi2": chi2,
        "dof": dof,
        "chi2_dof": chi2 / dof if dof > 0 else None,
        "grade4_pass": bool(
            total_budget < GRADE4_BUDGET
            and l24_l32_shift is not None
            and l24_l32_shift < GRADE4_BUDGET
            and (dof == 0 or chi2 / dof < 2.0)
        ),
        "grade5_pass": bool(total_budget < GRADE5_BUDGET),
    }


def band_readout(p_inf: float | None) -> dict[str, Any]:
    if p_inf is None or not math.isfinite(p_inf):
        return {"status": "unavailable"}
    d = p_inf - P_LICENSED
    if abs(d) <= GRADE4_BUDGET:
        band = "A_license_confirmed"
    elif abs(d) <= 1.0e-4:
        band = "C_license_broken_moderate"
    else:
        band = "D_license_broken_decisive"
    sub = None
    if band == "A_license_confirmed":
        if abs(p_inf - P_NEEDED_F4) <= 1.0e-5:
            sub = "B-i_if_grade5_lands_on_0.59344"
        elif abs(p_inf - P_LICENSED) <= 1.0e-5:
            sub = "B-ii_if_grade5_stays_on_0.59340"
        else:
            sub = "B-iii_if_grade5_elsewhere_inside_A"
    return {
        "P_license": P_LICENSED,
        "P_needed_F4": P_NEEDED_F4,
        "delta_from_license": d,
        "grade4_band": band,
        "grade5_subband_candidate": sub,
    }


def write_markdown_summary(path: Path, summary: dict[str, Any]) -> None:
    fit = summary["finite_volume_fit"]
    lines = [
        "# Plaquette Grade-4 Production MC Summary",
        "",
        f"Generated: `{summary['timestamp_utc']}`",
        "",
        "This is a production-output artifact for the pre-registered Stage-1 protocol.",
        "It does not set audit status.",
        "",
        "## Run",
        "",
        f"- Volumes requested: `{summary['run_parameters']['volumes']}`",
        f"- Starts requested: `{summary['run_parameters']['starts']}`",
        f"- Streams completed: `{summary['streams_completed']}` / `{summary['streams_requested']}`",
        f"- Update: `{summary['run_parameters']['update_algorithm']}`",
        "",
        "## Volumes",
        "",
        "| L | n | mean P_L | stderr_tau | cold/hot gate |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for row in summary["volumes"]:
        gate = row.get("start_state_gate")
        gate_text = "n/a" if gate is None else ("pass" if gate.get("pass") else "fail")
        lines.append(
            f"| {row['L']} | {row['combined']['n']} | {row['combined']['mean']:.9f} | "
            f"{row['combined']['stderr_tau']:.3e} | {gate_text} |"
        )
    lines += ["", "## Fit", ""]
    if fit.get("status") == "fit":
        lines += [
            f"- `P_inf = {fit['P_inf']:.9f}`",
            f"- `z2_fit_error = {fit['z2_fit_error']:.3e}`",
            f"- `L24_L32_shift_full_systematic = {fit['L24_L32_shift_full_systematic']}`",
            f"- `total_grade_budget_z2_plus_full_shift = {fit['total_grade_budget_z2_plus_full_shift']}`",
            f"- `chi2/dof = {fit['chi2_dof']}`",
            f"- Grade-4 pass by registered gates: `{fit['grade4_pass']}`",
            f"- Band readout: `{summary['band_readout']['grade4_band']}`",
        ]
    else:
        lines.append(f"- Fit unavailable: `{fit.get('status')}`")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_summary(args: argparse.Namespace, stream_results: list[dict[str, Any]]) -> dict[str, Any]:
    by_L: dict[int, list[dict[str, Any]]] = {}
    for row in stream_results:
        by_L.setdefault(int(row["L"]), []).append(row)
    volumes = [combine_volume(by_L[L]) for L in sorted(by_L)]
    fit = weighted_fit(volumes)
    p_inf = fit.get("P_inf") if fit.get("status") == "fit" else None
    all_gates = [
        row["start_state_gate"]["pass"]
        for row in volumes
        if isinstance(row.get("start_state_gate"), dict)
    ]
    summary = {
        "kind": "plaquette_grade4_production_summary",
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "status": "complete" if len(stream_results) == len(args.volumes) * len(args.starts) * args.replicas else "partial",
        "streams_completed": len(stream_results),
        "streams_requested": len(args.volumes) * len(args.starts) * args.replicas,
        "run_parameters": {
            "volumes": args.volumes,
            "starts": args.starts,
            "replicas": args.replicas,
            "therm_sweeps": args.therm,
            "measurements": args.measurements,
            "separation_sweeps": args.separation,
            "overrelax_sweeps_per_heatbath": args.overrelax,
            "numba_threads": args.numba_threads,
            "seed_base": args.seed_base,
            "time_budget_hours": args.time_budget_hours,
            "update_algorithm": "numba_compiled_cabibbo_marinari_heatbath_plus_su2_subgroup_overrelaxation",
            "observable": "full Wilson plaquette average over all 6 orientations, Re Tr U_P / 3",
        },
        "volumes": volumes,
        "finite_volume_fit": fit,
        "band_readout": band_readout(float(p_inf) if isinstance(p_inf, float) else None),
        "all_start_state_gates_pass": bool(all_gates and all(all_gates)),
        "status_authority": "independent audit lane only; this runner proposes no audit status",
    }
    return summary


def run(args: argparse.Namespace) -> int:
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.checkpoint_dir.mkdir(parents=True, exist_ok=True)
    mc.configure_numba_threads(args.numba_threads)
    log("compiling numba kernels")
    mc.warm_up_numba()

    manifest = {
        "kind": "plaquette_grade4_production_manifest",
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "argv": vars(args),
        "protocol_note": "docs/PLAQUETTE_MC_CERTIFICATION_PROTOCOL_NOTE_2026-06-11.md",
        "backend": "scripts/alpha_s_numba_wilson_loop_mc.py",
    }
    write_json(args.output_dir / "RUN_MANIFEST.json", manifest)

    deadline = time.monotonic() + args.time_budget_hours * 3600.0 if args.time_budget_hours else None
    stream_results: list[dict[str, Any]] = []
    stream_index = 0
    for L in args.volumes:
        for replica in range(args.replicas):
            for start_kind in args.starts:
                if deadline is not None and time.monotonic() >= deadline and stream_results:
                    log("time budget reached before starting next stream; writing partial summary")
                    summary = build_summary(args, stream_results)
                    write_json(args.output_dir / "GRADE4_SUMMARY.json", summary)
                    write_markdown_summary(args.output_dir / "GRADE4_SUMMARY.md", summary)
                    return 0
                row = run_stream(args, L, start_kind, replica, stream_index)
                stream_results.append(row)
                summary = build_summary(args, stream_results)
                write_json(args.output_dir / "GRADE4_SUMMARY.json", summary)
                write_markdown_summary(args.output_dir / "GRADE4_SUMMARY.md", summary)
                stream_index += 1

    summary = build_summary(args, stream_results)
    write_json(args.output_dir / "GRADE4_SUMMARY.json", summary)
    write_markdown_summary(args.output_dir / "GRADE4_SUMMARY.md", summary)
    log(f"completed {summary['streams_completed']} streams; summary={args.output_dir / 'GRADE4_SUMMARY.json'}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--volumes", type=parse_csv_ints, default=[8, 12, 16, 24, 32])
    parser.add_argument("--starts", type=parse_starts, default=["cold", "hot"])
    parser.add_argument("--replicas", type=int, default=1)
    parser.add_argument("--therm", type=int, default=1000)
    parser.add_argument("--measurements", type=int, default=500)
    parser.add_argument("--separation", type=int, default=6)
    parser.add_argument("--overrelax", type=int, default=3)
    parser.add_argument("--numba-threads", type=int, default=6)
    parser.add_argument("--seed-base", type=int, default=2026061104)
    parser.add_argument("--progress-interval", type=int, default=50)
    parser.add_argument("--checkpoint-every", type=int, default=25)
    parser.add_argument("--max-lag", type=int, default=200)
    parser.add_argument("--window-factor", type=float, default=5.0)
    parser.add_argument("--time-budget-hours", type=float, default=20.0)
    parser.add_argument("--hot-chunk", type=int, default=32768)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--checkpoint-dir", type=Path, default=DEFAULT_OUTPUT_DIR / "checkpoints")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--keep-checkpoints", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(run(parse_args()))
