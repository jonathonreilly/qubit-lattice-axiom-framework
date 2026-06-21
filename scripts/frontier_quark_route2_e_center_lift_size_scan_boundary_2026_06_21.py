#!/usr/bin/env python3
"""Route-2 E-center lift finite-box replay boundary.

This runner parameterizes the previously SIZE=15-pinned E-center lift replay
just far enough to test the June 10 finite-box follow-up.  It does not derive
rho_E = 21/4 and it does not refute a future size-stable infinite-volume
theorem.  It records a narrower fact:

  * the size-inferred replay reproduces the landed 15^3 calibration; but
  * the smaller/larger executable boxes checked here do not form evidence for
    a smooth convergence story toward q_E = 15/8.

The Schur action in the tensor path is patched locally to infer its grid size
from phi_grid.  No upstream module is edited by this runner.
"""

from __future__ import annotations

# Heavy finite-box replay runner.  The live run normally completes in under a
# minute on this machine, but the audit/cache lane may be under contention.
AUDIT_TIMEOUT_SEC = 900

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import math
import re
import time

import numpy as np

from _frontier_loader import load_frontier


ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "logs" / "runner-cache" / "frontier_tensor_support_center_excess_law.txt"
NOTE = ROOT / "docs" / "QUARK_ROUTE2_E_CENTER_LIFT_SIZE_SCAN_BOUNDARY_NOTE_2026-06-21.md"

TARGET_QT = Fraction(5, 6)
TARGET_QE = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)
TARGET_SHELL_TE = Fraction(-2, 1)
TARGET_CENTER_TE = Fraction(-8, 9)
SIZES = [9, 11, 13, 15, 17]
EPS = 0.005

same = load_frontier("same_source_metric", "frontier_same_source_metric_ansatz_scan.py")
two = load_frontier("tensor_two_channel", "frontier_tensor_boundary_drive_two_channel.py")
shell = load_frontier("one_parameter_shell", "frontier_one_parameter_reduced_shell_law.py")
schur = load_frontier("oh_schur_boundary_action", "frontier_oh_schur_boundary_action.py")


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


@dataclass
class SizeRow:
    size: int
    ok: bool
    reason: str
    elapsed_s: float
    gamma_e_center: float | None = None
    gamma_e_shell: float | None = None
    gamma_t_center: float | None = None
    gamma_t_shell: float | None = None

    @property
    def q_t(self) -> float | None:
        if self.gamma_t_center is None or self.gamma_t_shell is None:
            return None
        return self.gamma_t_center / self.gamma_t_shell

    @property
    def q_e(self) -> float | None:
        if self.gamma_e_center is None or self.gamma_e_shell is None:
            return None
        return self.gamma_e_center / self.gamma_e_shell

    @property
    def rho_e(self) -> float | None:
        if self.q_e is None:
            return None
        return 6.0 * (self.q_e - 1.0)

    @property
    def shell_te(self) -> float | None:
        if self.gamma_t_shell is None or self.gamma_e_shell is None:
            return None
        return self.gamma_t_shell / self.gamma_e_shell

    @property
    def center_te(self) -> float | None:
        if self.gamma_t_center is None or self.gamma_e_center is None:
            return None
        return self.gamma_t_center / self.gamma_e_center


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "BOUNDED") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


def relative_gap(value: float, target: Fraction) -> float:
    return abs(value / float(target) - 1.0)


def patch_tensor_schur_size_inference() -> None:
    """Replace the size-15 Schur pin with a phi_grid-size inferred replay."""

    def scalar_bridge_action_size(phi_grid: np.ndarray) -> float:
        size = int(phi_grid.shape[0])
        lam, trace_idx, bulk_idx, interior = schur.schur_dtn_matrix(size, 4.0)
        action = schur.analyze_family(phi_grid, lam, trace_idx, bulk_idx, interior)
        f = action["f"]
        j = action["j_trace"]
        return float(0.5 * f @ (lam @ f) - j @ f)

    two.utk.tcomp.scalar_bridge_action = scalar_bridge_action_size


def build_phi_factory(size: int):
    h0, interior = same.build_neg_laplacian_sparse(size)
    center = interior // 2
    support = [
        same.flat_idx(center + v[0], center + v[1], center + v[2], interior)
        for v in same.SUPPORT_COORDS
    ]
    g0p = same.solve_columns(h0, support)

    def phi_from_q(q: np.ndarray) -> np.ndarray:
        phi = np.zeros((size, size, size), dtype=float)
        phi[1:-1, 1:-1, 1:-1] = (g0p @ q).reshape((interior, interior, interior))
        return phi

    return phi_from_q


def gamma_pair(q: np.ndarray, ex: np.ndarray, t1x: np.ndarray, phi_from_q) -> tuple[float, float]:
    beta_e = float(
        (two.tensor_metrics(phi_from_q(q + EPS * ex))[0] - two.tensor_metrics(phi_from_q(q - EPS * ex))[0])
        / (2.0 * EPS)
    )
    beta_t = float(
        (two.tensor_metrics(phi_from_q(q + EPS * t1x))[0] - two.tensor_metrics(phi_from_q(q - EPS * t1x))[0])
        / (2.0 * EPS)
    )
    reduced = shell.reduced_data(phi_from_q(q))
    a_aniso = float(reduced["anchor_per_Q"]) * float(np.sum(q))
    return beta_e / a_aniso, beta_t / a_aniso


def compute_size_row(size: int) -> SizeRow:
    t0 = time.time()
    try:
        phi_from_q = build_phi_factory(size)
        basis = same.build_adapted_basis()
        e0 = basis[:, 0]
        s_unit = basis[:, 1] / math.sqrt(6.0)
        e1 = basis[:, 2]
        e2 = basis[:, 3]
        t1x = basis[:, 4]
        ex = (math.sqrt(3.0) * e1 + e2) / 2.0

        # The reduced-shell normalization is itself part of the replay surface.
        # Too-small boxes can lack the active anchor needed by this current
        # shell module; record that as a parameterization boundary, not a test
        # failure.
        shell.reduced_data(phi_from_q(e0))

        gamma_e_center, gamma_t_center = gamma_pair(e0, ex, t1x, phi_from_q)
        gamma_e_shell, gamma_t_shell = gamma_pair(s_unit, ex, t1x, phi_from_q)
        return SizeRow(
            size=size,
            ok=True,
            reason="computed",
            elapsed_s=time.time() - t0,
            gamma_e_center=gamma_e_center,
            gamma_e_shell=gamma_e_shell,
            gamma_t_center=gamma_t_center,
            gamma_t_shell=gamma_t_shell,
        )
    except KeyError as exc:
        return SizeRow(size=size, ok=False, reason=f"reduced-shell anchor unavailable: {exc!r}", elapsed_s=time.time() - t0)
    except Exception as exc:  # pragma: no cover - printed as a live boundary if upstream changes.
        return SizeRow(size=size, ok=False, reason=f"{type(exc).__name__}: {exc}", elapsed_s=time.time() - t0)


def parse_landed_cache() -> dict[str, float]:
    text = CACHE.read_text()
    vals: dict[str, float] = {}
    patterns = {
        "gamma_e_center": r"gamma_E\(center\)\s*=\s*([-+0-9.eE]+)",
        "gamma_e_shell": r"gamma_E\(shell\)\s*=\s*([-+0-9.eE]+)",
        "gamma_t_center": r"gamma_T\(center\)\s*=\s*([-+0-9.eE]+)",
        "gamma_t_shell": r"gamma_T\(shell\)\s*=\s*([-+0-9.eE]+)",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match is None:
            raise RuntimeError(f"missing {key} in {CACHE}")
        vals[key] = float(match.group(1))
    return vals


def print_row_table(rows: list[SizeRow]) -> None:
    print("\nFinite-box replay table")
    print("size  status      q_T             q_E             rho_E           shell T/E       center T/E      elapsed")
    print("-" * 112)
    for row in rows:
        if not row.ok:
            print(f"{row.size:>4}  boundary    {row.reason:<76} {row.elapsed_s:>7.2f}s")
            continue
        print(
            f"{row.size:>4}  computed  "
            f"{row.q_t:+.12f}  {row.q_e:+.12f}  {row.rho_e:+.12f}  "
            f"{row.shell_te:+.12f}  {row.center_te:+.12f}  {row.elapsed_s:>7.2f}s"
        )


def exact_target_chain_check() -> tuple[bool, str]:
    rho_t = Fraction(-1, 1)
    q_t = 1 + rho_t / 6
    q_e = 1 + TARGET_RHO_E / 6
    c_te = TARGET_SHELL_TE * q_t / q_e
    ok = (
        q_t == TARGET_QT
        and q_e == TARGET_QE
        and TARGET_QE == Fraction(9, 4) * TARGET_QT
        and c_te == TARGET_CENTER_TE
        and 6 * (Fraction(9, 4) * TARGET_QT - 1) == TARGET_RHO_E
    )
    return ok, f"q_T={q_t}, q_E={q_e}, q_E/q_T=9/4, center T/E={c_te}, rho_E={TARGET_RHO_E}"


def main() -> int:
    print("Route-2 E-center lift finite-box replay boundary")
    print("=" * 86)
    print("Patch: tensor Schur action is inferred from phi_grid.shape[0] for this runner only.")
    patch_tensor_schur_size_inference()

    rows = [compute_size_row(size) for size in SIZES]
    print_row_table(rows)

    computed = {row.size: row for row in rows if row.ok}
    unavailable = [row for row in rows if not row.ok]
    cache_vals = parse_landed_cache()
    row15 = computed.get(15)

    record(
        "the parameterized replay records the too-small reduced-shell boundary instead of counting it as a failure",
        bool(unavailable) and any(row.size == 9 and "anchor" in row.reason for row in unavailable),
        "; ".join(f"N={row.size}: {row.reason}" for row in unavailable) or "no unavailable rows",
        status="BOUNDARY",
    )

    if row15 is None:
        record("the SIZE=15 replay reproduces the landed calibration cache", False, "N=15 did not compute")
    else:
        diffs = {
            "gamma_E(center)": abs(row15.gamma_e_center - cache_vals["gamma_e_center"]),
            "gamma_E(shell)": abs(row15.gamma_e_shell - cache_vals["gamma_e_shell"]),
            "gamma_T(center)": abs(row15.gamma_t_center - cache_vals["gamma_t_center"]),
            "gamma_T(shell)": abs(row15.gamma_t_shell - cache_vals["gamma_t_shell"]),
        }
        record(
            "the size-inferred replay reproduces the landed 15^3 calibration cache",
            max(diffs.values()) < 1.0e-12,
            "; ".join(f"{key} abs diff={val:.3e}" for key, val in diffs.items()),
            status="REPRO",
        )

    wrong_orientation = []
    broad_fail = []
    for size in (11, 13, 17):
        row = computed.get(size)
        if row is None:
            continue
        if row.q_e is not None and row.shell_te is not None:
            q_e_gap = relative_gap(row.q_e, TARGET_QE)
            shell_gap = relative_gap(row.shell_te, TARGET_SHELL_TE)
            if q_e_gap > 0.25 or shell_gap > 0.25:
                broad_fail.append(f"N={size}: q_E gap={q_e_gap:.3g}, shell gap={shell_gap:.3g}")
            if row.q_e * float(TARGET_QE) <= 0 or row.shell_te * float(TARGET_SHELL_TE) <= 0:
                wrong_orientation.append(f"N={size}: q_E={row.q_e:+.6f}, shell T/E={row.shell_te:+.6f}")

    record(
        "the neighboring executable boxes do not sit in the target envelope",
        len(broad_fail) >= 3,
        "; ".join(broad_fail),
        status="NO-GO",
    )
    record(
        "the neighboring executable boxes include sign/orientation conflicts with the target chain",
        len(wrong_orientation) >= 2,
        "; ".join(wrong_orientation),
        status="NO-GO",
    )

    q_e_sequence = [(size, computed[size].q_e) for size in (11, 13, 15, 17) if size in computed]
    q_e_gaps = [(size, abs(q_e - float(TARGET_QE))) for size, q_e in q_e_sequence]
    signs = [math.copysign(1.0, q_e) for _, q_e in q_e_sequence]
    monotone_gap_down = all(q_e_gaps[i + 1][1] <= q_e_gaps[i][1] for i in range(len(q_e_gaps) - 1))
    constant_sign = all(sign == signs[0] for sign in signs)
    record(
        "the checked finite-box sequence is not monotone convergence evidence for q_E -> 15/8",
        (not monotone_gap_down) and (not constant_sign),
        "q_E sequence = "
        + ", ".join(f"N={size}: {q_e:+.6f}, abs gap={gap:.6f}" for (size, q_e), (_, gap) in zip(q_e_sequence, q_e_gaps)),
        status="BOUNDARY",
    )

    ok_chain, chain_detail = exact_target_chain_check()
    record(
        "the exact endpoint algebra remains coherent if a future theorem supplies q_E=15/8",
        ok_chain,
        chain_detail,
        status="EXACT",
    )

    if NOTE.exists():
        note_text = NOTE.read_text()
        boundary_ok = (
            "does not refute a future size-stable/infinite-volume theorem" in note_text
            and "cannot be cited as finite-size convergence evidence" in note_text
            and "No observed masses, fitted targets, or PDG values" in note_text
        )
        record(
            "the paired note carries the branch-local claim-status firewall",
            boundary_ok,
            "required boundary phrases present" if boundary_ok else "required boundary phrases missing",
            status="FIREWALL",
        )

    n_pass = sum(check.ok for check in CHECKS)
    n_fail = sum(not check.ok for check in CHECKS)
    print("\nVerdict:")
    print(
        "The current executable size-parameterized replay reproduces the landed 15^3 E-center "
        "calibration, but the checked neighboring boxes do not support the naive finite-size "
        "extrapolation route.  This is a boundary/no-go for citing the 15^3 match as convergence "
        "evidence, not a refutation of a future size-stable infinite-volume theorem."
    )
    print(f"\nTOTAL: PASS={n_pass} FAIL={n_fail}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
