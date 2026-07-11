#!/usr/bin/env python3
"""Audit-facing certificate for the mirror chokepoint boundary fit note.

The certificate deliberately proves only the bounded finite-window claim in
docs/MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md:

  * the fixed dense boundary card is Born-clean, k=0-clean, gravity-positive,
    and decohering for N = 40, 60, 80, 100;
  * the same card reaches a gravity-estimator validity boundary at N = 120;
  * the quoted exponent is the post-hoc log-log fit to 1 - pur_cl on exactly
    the selected fit rows and is not used as a selection rule.

It does not certify an asymptotic law or a mirror-family theorem.
"""

from __future__ import annotations

import hashlib
import math
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from mirror_chokepoint_joint import (
    compute_field_3d,
    generate_mirror_chokepoint_dag,
    measure_joint,
    propagate_3d,
)


AUDIT_TIMEOUT_SEC = 500
REPO_ROOT = Path(__file__).resolve().parent.parent
COMPANION_PATH = REPO_ROOT / "scripts" / "mirror_chokepoint_joint.py"
EXPECTED_COMPANION_SHA256 = "afff61d204cc8a146c0b15c1c40e2105cdcb71693de7302da791b21efe07d563"

BOUNDARY_COMMAND = [
    sys.executable,
    "scripts/mirror_chokepoint_joint.py",
    "--npl-half",
    "60",
    "--connect-radius",
    "5.0",
    "--n-layers",
    "40",
    "60",
    "80",
    "100",
    "120",
    "--layer2-prob",
    "0.0",
]

RETAINED_N = (40, 60, 80, 100)
ESTIMATOR_WALL_N = 120
BORN_TOL = 1e-10
K0_TOL = 1e-12
GRAVITY_T_MIN = 2.0
DECOHERENCE_CEILING = 0.95
DISPLAY_TOL = 5e-5
DISPLAY_SE_TOL = 5e-4
PROPAGATION_NORM_TOL = 1e-30

# Values printed in the source note's finite-window table.  These are not
# fitted targets: the live replay is run first, and the parsed rows must match
# this frozen transcription before any fit arithmetic is accepted.
EXPECTED_DISPLAY_ROWS = {
    40: (0.6884, 0.8608, 0.03, 0.9850, 4.7499, 0.666),
    60: (0.4791, 0.8440, 0.03, 0.9953, 3.9733, 0.473),
    80: (0.4291, 0.8182, 0.03, 1.0029, 3.0551, 0.672),
    100: (0.2308, 0.9043, 0.02, 1.0058, 1.3089, 0.570),
}


@dataclass(frozen=True)
class Row:
    n: int
    cfg: str
    dtv: float
    pur_cl: float
    pur_se: float
    s_norm: float
    gravity: float
    gravity_se: float
    born: float
    k0: float
    ok: int


def _float(value: str) -> float:
    return float("nan") if value == "nan" else float(value)


def parse_rows(stdout: str) -> dict[tuple[int, str], Row]:
    rows: dict[tuple[int, str], Row] = {}
    for raw in stdout.splitlines():
        line = raw.replace(chr(177), " ").strip()
        if not line:
            continue
        parts = line.split()
        if not parts or not parts[0].isdigit():
            continue
        n = int(parts[0])
        if len(parts) >= 3 and parts[1] == "mirror" and parts[2] == "p2=0":
            cfg = "mirror p2=0"
            start = 3
        elif len(parts) >= 2 and parts[1] == "random":
            cfg = "random"
            start = 2
        else:
            continue
        if len(parts) <= start or parts[start] == "FAIL":
            continue
        metric = parts[start:]
        if len(metric) < 10:
            raise ValueError(f"could not parse row: {raw!r}")
        row = Row(
            n=n,
            cfg=cfg,
            dtv=float(metric[0]),
            pur_cl=float(metric[1]),
            pur_se=float(metric[2]),
            s_norm=float(metric[3]),
            gravity=float(metric[4]),
            gravity_se=float(metric[5]),
            born=_float(metric[6]),
            k0=float(metric[7]),
            ok=int(metric[8]),
        )
        rows[(n, cfg)] = row
    return rows


def fit_decoherence(rows: list[Row]) -> tuple[float, float, float, float, float]:
    xs = [math.log(row.n) for row in rows]
    ys = [math.log(1.0 - row.pur_cl) for row in rows]
    n = len(xs)
    x_bar = sum(xs) / n
    y_bar = sum(ys) / n
    sxx = sum((x - x_bar) ** 2 for x in xs)
    sxy = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys))
    alpha = sxy / sxx
    intercept = y_bar - alpha * x_bar
    coeff = math.exp(intercept)
    residual = sum((y - (intercept + alpha * x)) ** 2 for x, y in zip(xs, ys))
    total = sum((y - y_bar) ** 2 for y in ys)
    r2 = 1.0 - residual / total
    n95 = ((1.0 - 0.95) / coeff) ** (1.0 / alpha)
    n99 = ((1.0 - 0.99) / coeff) ** (1.0 / alpha)
    return coeff, alpha, r2, n95, n99


def check(name: str, ok: bool, detail: str) -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {name}: {detail}")
    return ok


def check_display_row(row: Row) -> bool:
    expected = EXPECTED_DISPLAY_ROWS[row.n]
    actual = (
        row.dtv,
        row.pur_cl,
        row.pur_se,
        row.s_norm,
        row.gravity,
        row.gravity_se,
    )
    tolerances = (
        DISPLAY_TOL,
        DISPLAY_TOL,
        DISPLAY_SE_TOL,
        DISPLAY_TOL,
        DISPLAY_TOL,
        DISPLAY_SE_TOL,
    )
    labels = ("d_TV", "pur_cl", "pur_se", "S_norm", "gravity", "gravity_se")
    matches = [
        math.isclose(got, want, rel_tol=0.0, abs_tol=tol)
        for got, want, tol in zip(actual, expected, tolerances)
    ]
    detail = ", ".join(
        f"{label}={'match' if ok else 'DRIFT'}"
        for label, ok in zip(labels, matches)
    )
    return check(f"N={row.n} displayed row transcription", all(matches), detail)


def companion_sha256() -> str:
    return hashlib.sha256(COMPANION_PATH.read_bytes()).hexdigest()


def wall_gravity_validity() -> dict[str, object]:
    """Diagnose whether N=120's printed gravity zeros are evaluated values.

    The companion's ``measure_joint`` returns a row after its d_TV/purity
    gates, but initializes gravity to zero and evaluates the centroid shift
    only when both detector norms exceed 1e-30.  Reconstruct those two norms
    for every returned mirror row so a default zero cannot be certified as a
    physical zero.
    """
    returned = 0
    valid = 0
    unresolved = 0
    unresolved_seeds: list[int] = []
    field_free_norms: list[float] = []

    for seed in (s * 7 + 3 for s in range(16)):
        positions, adj, _, _ = generate_mirror_chokepoint_dag(
            ESTIMATOR_WALL_N, 60, 12.0, 5.0, seed, 0.0
        )
        if measure_joint(positions, adj, ESTIMATOR_WALL_N, 5.0) is None:
            continue
        returned += 1

        by_layer: defaultdict[int, list[int]] = defaultdict(list)
        for idx, (x, _, _) in enumerate(positions):
            by_layer[round(x)].append(idx)
        layers = sorted(by_layer)
        src = by_layer[layers[0]]
        detector = list(by_layer[layers[-1]])
        center_y = sum(position[1] for position in positions) / len(positions)
        barrier = by_layer[layers[len(layers) // 3]]
        slit_a = [i for i in barrier if positions[i][1] > center_y + 3][:3]
        slit_b = [i for i in barrier if positions[i][1] < center_y - 3][:3]
        blocked = set(barrier) - set(slit_a + slit_b)
        mass_layer = layers[2 * len(layers) // 3]
        mass_nodes = [
            i for i in by_layer[mass_layer] if positions[i][1] > center_y + 1
        ]
        field_m = compute_field_3d(positions, mass_nodes)
        field_f = [0.0] * len(positions)
        amplitude_m = propagate_3d(positions, adj, field_m, src, 5.0, blocked)
        amplitude_f = propagate_3d(positions, adj, field_f, src, 5.0, blocked)
        norm_m = sum(abs(amplitude_m[d]) ** 2 for d in detector)
        norm_f = sum(abs(amplitude_f[d]) ** 2 for d in detector)
        if norm_m > PROPAGATION_NORM_TOL and norm_f > PROPAGATION_NORM_TOL:
            valid += 1
        else:
            unresolved += 1
            unresolved_seeds.append(seed)
            field_free_norms.append(norm_f)

    return {
        "returned": returned,
        "valid": valid,
        "unresolved": unresolved,
        "unresolved_seeds": unresolved_seeds,
        "min_field_free_norm": min(field_free_norms),
        "max_field_free_norm": max(field_free_norms),
    }


def run_replay() -> str:
    print("LIVE_REPLAY_COMMAND:")
    print("  " + " ".join(BOUNDARY_COMMAND).replace(sys.executable, "python3", 1))
    proc = subprocess.run(
        BOUNDARY_COMMAND,
        check=False,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC - 30,
    )
    print()
    print("LIVE_REPLAY_STDOUT_BEGIN")
    print(proc.stdout.rstrip())
    print("LIVE_REPLAY_STDOUT_END")
    if proc.stderr.strip():
        print("LIVE_REPLAY_STDERR_BEGIN")
        print(proc.stderr.rstrip())
        print("LIVE_REPLAY_STDERR_END")
    if proc.returncode != 0:
        raise RuntimeError(f"boundary replay exited {proc.returncode}")
    return proc.stdout


def main() -> int:
    print("=" * 78)
    print("MIRROR CHOKEPOINT BOUNDARY FIT CERTIFICATE")
    print("Source note: docs/MIRROR_CHOKEPOINT_BOUNDARY_FIT_NOTE.md")
    print("Scope: fixed finite window on the dense boundary card only")
    print("=" * 78)
    print()

    actual_companion_sha = companion_sha256()
    companion_ok = actual_companion_sha == EXPECTED_COMPANION_SHA256
    print("COMPANION_PROVENANCE:")
    print(f"  path={COMPANION_PATH.relative_to(REPO_ROOT)}")
    print(f"  expected_sha256={EXPECTED_COMPANION_SHA256}")
    print(f"  actual_sha256={actual_companion_sha}")
    print()

    stdout = run_replay()
    rows = parse_rows(stdout)
    mirror_rows = [rows[(n, "mirror p2=0")] for n in RETAINED_N]
    wall = rows[(ESTIMATOR_WALL_N, "mirror p2=0")]

    print()
    print("PRE_FIT_INCLUSION_GATES:")
    checks: list[bool] = [
        check(
            "companion source SHA pin",
            companion_ok,
            f"actual={actual_companion_sha}",
        )
    ]
    checks.append(
        check(
            "fixed card header",
            "NPL_HALF=60 (total 120), k=5.0, 16 seeds" in stdout,
            "strict layer-1, npl_half=60, connect_radius=5.0, layer2_prob=0.0, 16 seeds",
        )
    )
    for row in mirror_rows:
        grav_t = row.gravity / row.gravity_se if row.gravity_se > 0 else float("inf")
        checks.extend(
            [
                check_display_row(row),
                check(f"N={row.n} seed count", row.ok == 16, f"ok={row.ok}"),
                check(f"N={row.n} Born-clean", row.born < BORN_TOL, f"Born={row.born:.2e} < {BORN_TOL:.0e}"),
                check(f"N={row.n} k=0 control", abs(row.k0) <= K0_TOL, f"k0={row.k0:.2e}"),
                check(
                    f"N={row.n} gravity-positive",
                    row.gravity > 0.0 and grav_t > GRAVITY_T_MIN,
                    f"gravity={row.gravity:+.4f}+/-{row.gravity_se:.3f}, t={grav_t:.2f}",
                ),
                check(
                    f"N={row.n} decohering",
                    row.pur_cl < DECOHERENCE_CEILING,
                    f"pur_cl={row.pur_cl:.4f} < {DECOHERENCE_CEILING:.2f}",
                ),
            ]
        )

    checks.append(
        check(
            "N=120 legacy display sentinel",
            wall.ok == 11 and wall.gravity == 0.0 and wall.gravity_se == 0.0,
            f"ok={wall.ok}/16, gravity={wall.gravity:+.4f}+/-{wall.gravity_se:.3f}; "
            "displayed zeros require the validity diagnostic below",
        )
    )

    wall_validity = wall_gravity_validity()
    print()
    print("N120_GRAVITY_ESTIMATOR_VALIDITY:")
    print(f"  returned_rows={wall_validity['returned']}/16")
    print(f"  valid_gravity_rows={wall_validity['valid']}")
    print(f"  unresolved_gravity_rows={wall_validity['unresolved']}")
    print("  unresolved_seeds=" + ",".join(str(v) for v in wall_validity["unresolved_seeds"]))
    print(f"  field_free_detector_norm_range={wall_validity['min_field_free_norm']:.3e}..{wall_validity['max_field_free_norm']:.3e}")
    checks.append(
        check(
            "N=120 gravity estimator is unresolved, not zero",
            wall_validity["returned"] == 11
            and wall_validity["valid"] == 0
            and wall_validity["unresolved"] == 11
            and wall_validity["max_field_free_norm"] < PROPAGATION_NORM_TOL,
            "0/11 returned rows satisfy both detector-norm gates; exclude the row from gravity claims",
        )
    )

    coeff, alpha, r2, n95, n99 = fit_decoherence(mirror_rows)
    print()
    print("POST_INCLUSION_DECOHERENCE_FIT:")
    print("  fit_input_N: " + ", ".join(str(row.n) for row in mirror_rows))
    print("  fit_input_1_minus_pur_cl: " + ", ".join(f"{1.0 - row.pur_cl:.4f}" for row in mirror_rows))
    print(f"  coeff={coeff:.10f}")
    print(f"  alpha={alpha:.10f}")
    print(f"  r2={r2:.10f}")
    print(f"  illustrative_N_pur_0p95={n95:.6g}")
    print(f"  illustrative_N_pur_0p99={n99:.6g}")
    checks.extend(
        [
            check("fit coefficient rounds to 0.3901", round(coeff, 4) == 0.3901, f"round(coeff,4)={round(coeff, 4):.4f}"),
            check("fit exponent rounds to -0.245", round(alpha, 3) == -0.245, f"round(alpha,3)={round(alpha, 3):.3f}"),
            check("fit R2 rounds to 0.126", round(r2, 3) == 0.126, f"round(R2,3)={round(r2, 3):.3f}"),
            check("illustrative pur=0.95 N rounds to 4.32e3", f"{n95:.2e}" == "4.32e+03", f"N={n95:.6g}"),
            check("illustrative pur=0.99 N rounds to 3.05e6", f"{n99:.2e}" == "3.05e+06", f"N={n99:.6g}"),
        ]
    )

    print()
    print("SELECTOR_FIREWALL:")
    checks.append(
        check(
            "fit is not an inclusion selector",
            tuple(row.n for row in mirror_rows) == RETAINED_N
            and wall.n == ESTIMATOR_WALL_N,
            "inclusion gates are evaluated before alpha/R2; the estimator-invalid row is excluded before fitting",
        )
    )
    print("  safe_scope: bounded finite-window report for the named dense boundary card")
    print("  excluded_scope: no N=120 zero-gravity result, mirror-family theorem, or bounded/asymptotic law")

    n_pass = sum(1 for ok in checks if ok)
    print()
    print(f"PASS={n_pass}/{len(checks)}")
    if n_pass == len(checks):
        print("STATUS: BOUNDED FINITE-WINDOW CERTIFICATE PASS")
        return 0
    print("STATUS: BOUNDED FINITE-WINDOW CERTIFICATE FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
