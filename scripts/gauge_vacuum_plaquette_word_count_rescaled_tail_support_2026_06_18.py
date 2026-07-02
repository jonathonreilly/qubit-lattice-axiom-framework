#!/usr/bin/env python3
"""Rescaled high-precision tail support for the plaquette word-count packet.

This runner stays inside the finite packet used by the existing all-k
remainder certificate. It does not set an audit status and does not close the
all-k theorem. Its job is narrower: remove the double-precision underflow /
cancellation ambiguity in the post-window residual and isolate the remaining
analytic tail proof obligation.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_word_count_all_k_remainder_certificate_narrow_2026_06_12 as allk
import gauge_vacuum_plaquette_word_count_power_block_birkhoff_certificate_narrow_2026_06_12 as w28
import gauge_vacuum_plaquette_word_count_theta_identification_two_term_asymptotic_2026_06_12 as theta_note


AUDIT_TIMEOUT_SEC = 120

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)

HIGH_PRECISION_DPS = 170
TAIL_ROWS = (19, 20, 24, 30, 36, 40)
FINITE_SCAN_MAX = 18
TAIL_RATIO_CEILING = 4.05

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_RESCALED_TAIL_SUPPORT_NOTE_2026-06-18.md"
)
PARENT_NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_ALL_K_REMAINDER_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


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


def mp_from_float(value: float) -> mp.mpf:
    return mp.mpf(repr(float(value)))


def high_precision_scaled_x(
    packet: w28.Packet,
    td: theta_note.ThetaData,
    k: int,
    dps: int = HIGH_PRECISION_DPS,
) -> list[mp.mpf]:
    """Return rho/rho_f with a dominant-channel rescaling.

    The eigenvector is computed from the symmetric reduced matrix divided by
    t00^k. The readout is accumulated in high precision before normalizing by
    the fundamental entry. This preserves the small post-leading correction
    that double precision loses around k=20.
    """

    mp.mp.dps = dps
    n = len(packet.weights)
    f = packet.index[FUND]

    dim = [mp_from_float(value) for value in packet.dim]
    d_coeff = [mp_from_float(value) for value in packet.d_coeff]
    ell_eta = [mp_from_float(value) for value in packet.ell_eta]
    t00 = mp_from_float(td.t00)
    t_rel = [
        [mp_from_float(float(td.t_matrix[i, j])) / t00 for j in range(n)]
        for i in range(n)
    ]
    fusion = [
        [mp_from_float(float(packet.fusion[i, j])) for j in range(n)]
        for i in range(n)
    ]

    matrix = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            matrix[i, j] = mp.sqrt(dim[i] * dim[j]) * (t_rel[i][j] ** k)

    vals, vecs = mp.eigsy(matrix)
    top = max(range(n), key=lambda idx: vals[idx])
    vec = [vecs[i, top] for i in range(n)]
    if sum(vec) < 0:
        vec = [-value for value in vec]

    terms = []
    for i in range(n):
        sqrt_c = mp.sqrt((d_coeff[i] ** k) / (dim[i] ** (k - 1)))
        terms.append(sqrt_c * vec[i] * (ell_eta[i] ** (k - 1)))

    raw = []
    for w in range(n):
        total = mp.mpf("0")
        for i in range(n):
            total += fusion[w][i] * terms[i]
        raw.append(d_coeff[w] * total)

    if raw[packet.index[ZERO]] < 0:
        raw = [-value for value in raw]
    return [value / raw[f] for value in raw]


def double_scaled_x(
    packet: w28.Packet,
    k: int,
) -> np.ndarray:
    rho = w28.reduced_eta_rho(packet, k)
    return rho / float(rho[packet.index[FUND]])


def q_l1_ratio(
    x_values: list[mp.mpf],
    packet: w28.Packet,
    td: theta_note.ThetaData,
    sigma: np.ndarray,
    k: int,
) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    theta = mp_from_float(td.theta)
    alpha = mp_from_float(td.alpha)
    q_total = mp.mpf("0")
    delta_total = mp.mpf("0")
    for i, x_value in enumerate(x_values):
        limiting = mp.mpf("1") if i in {f, fb} else mp.mpf("0")
        delta = x_value - limiting
        delta_total += abs(delta)
        q_total += abs(delta / (theta ** (k - 1)) - mp_from_float(float(sigma[i])))
    return q_total, q_total / (alpha**k), delta_total / (theta ** (k - 1))


def finite_scan_constant(
    packet: w28.Packet,
    td: theta_note.ThetaData,
    sigma: np.ndarray,
) -> tuple[float, int]:
    best = -1.0
    best_k = -1
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    x_inf = np.zeros(len(packet.weights), dtype=float)
    x_inf[f] = 1.0
    x_inf[fb] = 1.0
    for k in range(2, FINITE_SCAN_MAX + 1):
        x = double_scaled_x(packet, k)
        q = (x - x_inf) / (td.theta ** (k - 1)) - sigma
        ratio = float(np.linalg.norm(q, 1)) / (td.alpha**k)
        if ratio > best:
            best = ratio
            best_k = k
    return best, best_k


def note_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette word-count rescaled tail support")
    print("Source-side bounded support only; no audit status is set here.")
    print("No new import: the runner reuses the finite packet already on main.")

    packet = w28.build_packet()
    td = theta_note.theta_data(packet)
    sigma = allk.sigma_slice_packet(packet)

    print(f"packet weights={len(packet.weights)}")
    print(f"theta={td.theta:.15f}")
    print(f"alpha={td.alpha:.15f}")
    print(f"theta*alpha={td.theta_alpha:.15f}")
    print(f"theta*gamma={td.theta_gamma:.15f}")
    print(f"theta^2={td.theta**2:.15f}")
    check(
        "tail scale separation is visible on the finite packet",
        td.theta_alpha > td.theta_gamma and td.theta_alpha > td.theta**2,
        f"theta*alpha={td.theta_alpha:.15f}",
    )

    finite_const, finite_k = finite_scan_constant(packet, td, sigma)
    print(f"finite_scan_q_l1_alpha_constant={finite_const:.15e} at k={finite_k}")
    check(
        "old finite scan maximum is reproduced and occurs at k=2",
        finite_k == 2 and abs(finite_const - 56.64730598492354) < 1.0e-9,
        f"best={finite_const:.15e}, k={finite_k}",
    )

    print("high_precision_tail_rows")
    tail_rows: list[tuple[int, mp.mpf, mp.mpf, mp.mpf]] = []
    for k in TAIL_ROWS:
        x_hp = high_precision_scaled_x(packet, td, k)
        q_l1, q_over_alpha, delta_over_theta = q_l1_ratio(
            x_hp, packet, td, sigma, k
        )
        tail_rows.append((k, q_l1, q_over_alpha, delta_over_theta))
        print(
            f"  k={k:2d} q_l1={mp.nstr(q_l1, 18)} "
            f"q_l1/alpha^k={mp.nstr(q_over_alpha, 18)} "
            f"delta_l1/theta^(k-1)={mp.nstr(delta_over_theta, 18)}"
        )

    check(
        "rescaled high-precision rows stay below 4.05 alpha^k on the sampled tail",
        all(row[2] < TAIL_RATIO_CEILING for row in tail_rows),
        f"ceiling={TAIL_RATIO_CEILING}",
    )
    check(
        "sampled high-precision tail ratio is monotone decreasing",
        all(tail_rows[i + 1][2] < tail_rows[i][2] for i in range(len(tail_rows) - 1)),
    )
    check(
        "sampled high-precision tail is far below the k=2 finite-scan envelope",
        float(max(row[2] for row in tail_rows)) < finite_const / 10.0,
        f"tail_max={mp.nstr(max(row[2] for row in tail_rows), 18)}",
    )

    for k in (2, 10, 18):
        x_hp = high_precision_scaled_x(packet, td, k)
        x_double = double_scaled_x(packet, k)
        max_diff = max(
            abs(float(x_hp[i]) - float(x_double[i])) for i in range(len(packet.weights))
        )
        print(f"double_vs_high_precision k={k:2d} max_diff={max_diff:.3e}")
        check(
            f"high precision agrees with the existing double path at k={k}",
            max_diff < 1.0e-9,
        )

    x20_hp = high_precision_scaled_x(packet, td, 20)
    x20_double = double_scaled_x(packet, 20)
    q20_hp, _ratio20_hp, _delta20_hp = q_l1_ratio(x20_hp, packet, td, sigma, 20)
    x20_double_mp = [mp_from_float(float(value)) for value in x20_double]
    q20_double, _ratio20_double, _delta20_double = q_l1_ratio(
        x20_double_mp, packet, td, sigma, 20
    )
    print(
        "k20_cancellation_probe "
        f"high_precision_q={mp.nstr(q20_hp, 18)} "
        f"double_path_q={mp.nstr(q20_double, 18)}"
    )
    check(
        "high precision exposes the k=20 post-leading tail lost by the double path",
        q20_hp > mp.mpf("1.0e-7") and q20_double < q20_hp / 1000,
    )

    source_text = note_text(NOTE_PATH)
    parent_text = note_text(PARENT_NOTE_PATH)
    check("support note exists", bool(source_text), str(NOTE_PATH))
    if source_text:
        check(
            "support note keeps the closure boundary explicit",
            "does not close the all-k bridge" in source_text
            and "analytic monotone/Neumann tail proof remains open" in source_text,
        )
        check(
            "support note records the sampled tail rows",
            "k = 40" in source_text and "q_l1 / alpha^k" in source_text,
        )
    check("parent note exists", bool(parent_text), str(PARENT_NOTE_PATH))
    if parent_text:
        check(
            "parent note links the rescaled tail support without claiming closure",
            "GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_RESCALED_TAIL_SUPPORT_NOTE_2026-06-18.md"
            in parent_text
            and "does not close the all-k bridge" in parent_text,
        )

    print("remaining blocker: analytic monotone/Neumann tail proof for every k beyond the sampled high-precision window.")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
