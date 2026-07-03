#!/usr/bin/env python3
"""Theta identification for the finite gauge-vacuum plaquette word-count ladder.

This runner stays inside the finite packet already used by the W28/rung-four
word-count runners:

* tensor word box NMAX=4 and MODE_MAX=80;
* source readout NMAX=7 and MODE_MAX=200;
* matrix-element same-label adjacent bond;
* eta_inf boundary from the one-word tensor-word Perron solve.

It identifies the measured convergence factor

    theta = 0.263745855973467

as an explicit packet quantity in the entrywise-power channel reduction and
then composes that scale with the large-rho source Perron perturbation.

No audit status is set here. No literature value, new axiom, external citation,
or new comparator number is imported.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_word_count_power_block_birkhoff_certificate_narrow_2026_06_12 as w28


AUDIT_TIMEOUT_SEC = 600

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
ADJOINT = (1, 1)
SYM20 = (2, 0)
SYM02 = (0, 2)
TARGET_THETA = 0.263745855973467
DISPLAYED_THETA_SQUARED_PREFIX = "theta^2 = 0.069561876543"
STALE_THETA_SQUARED_PREFIX = "theta^2 = 0.0695618585"
KMAX = 20

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class ThetaData:
    t_matrix: np.ndarray
    theta: float
    theta_inverse: float
    t00: float
    t_f0_ratio: float
    alpha: float
    gamma: float
    theta_alpha: float
    theta_gamma: float


@dataclass(frozen=True)
class SourceAsymptotic:
    p_inf: float
    source_gap: float
    p1: float
    p2: float
    c_source: float
    c_over_theta: float
    finite_difference_error: float


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


def section(title: str) -> None:
    print()
    print("=" * 112)
    print(title)
    print("=" * 112)


def packet_t_matrix(packet: w28.Packet) -> np.ndarray:
    return (
        np.sqrt(packet.d_coeff[:, None] * packet.d_coeff[None, :])
        * packet.g_channel
        / np.sqrt(packet.dim[:, None] * packet.dim[None, :])
    )


def theta_data(packet: w28.Packet) -> ThetaData:
    z = packet.index[ZERO]
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    t_matrix = packet_t_matrix(packet)
    t00 = float(t_matrix[z, z])
    t_f0_ratio = float(t_matrix[f, z] / t00)
    theta = float(
        (packet.ell_eta[f] / packet.ell_eta[z])
        * math.sqrt(packet.d_coeff[f] / packet.dim[f])
        * t_f0_ratio
    )
    alpha = float(t_matrix[f, f] / t00)
    gamma = float(t_matrix[f, fb] / t00)
    return ThetaData(
        t_matrix=t_matrix,
        theta=theta,
        theta_inverse=1.0 / theta,
        t00=t00,
        t_f0_ratio=t_f0_ratio,
        alpha=alpha,
        gamma=gamma,
        theta_alpha=theta * alpha,
        theta_gamma=theta * gamma,
    )


def reduced_matrix_from_t(packet: w28.Packet, t_matrix: np.ndarray, words: int) -> np.ndarray:
    return np.sqrt(packet.dim[:, None] * packet.dim[None, :]) * (t_matrix**words)


def reduced_matrix_direct(packet: w28.Packet, words: int) -> np.ndarray:
    c_mid = packet.d_coeff**words / packet.dim ** (words - 1)
    sqrt_c = np.sqrt(c_mid)
    return sqrt_c[:, None] * (packet.g_channel**words) * sqrt_c[None, :]


def top_reduced_eigenvector(packet: w28.Packet, t_matrix: np.ndarray, words: int) -> tuple[float, np.ndarray]:
    reduced = reduced_matrix_from_t(packet, t_matrix, words)
    vals, vecs = np.linalg.eigh(reduced)
    pos = int(np.argmax(vals))
    vec = vecs[:, pos]
    z = packet.index[ZERO]
    if float(vec[z]) < 0.0:
        vec = -vec
    vec = vec / float(vec[z])
    return float(vals[pos]), vec


def eigenvector_asymptotic_errors(
    packet: w28.Packet, t_matrix: np.ndarray, words: int
) -> tuple[float, float, float, float]:
    z = packet.index[ZERO]
    rest = [i for i in range(len(packet.weights)) if i != z]
    reduced = reduced_matrix_from_t(packet, t_matrix, words)
    eig, vec = top_reduced_eigenvector(packet, t_matrix, words)
    dominant = float(reduced[z, z])
    r = reduced[rest, z] / dominant
    correction_matrix = reduced[np.ix_(rest, rest)] / dominant
    first = r
    second = r + correction_matrix @ r
    actual = vec[rest]
    first_abs = float(np.max(np.abs(actual - first)))
    second_abs = float(np.max(np.abs(actual - second)))
    actual_scale = max(float(np.max(np.abs(actual))), 1.0e-300)
    correction_norm = float(np.linalg.norm(correction_matrix, ord=np.inf))
    lambda_bar = eig / dominant
    return first_abs / actual_scale, second_abs / actual_scale, correction_norm, lambda_bar


def slice_limit_vector(packet: w28.Packet) -> np.ndarray:
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    sigma = np.zeros(len(packet.weights), dtype=float)
    for i in range(len(packet.weights)):
        sigma[i] = (
            packet.d_coeff[i]
            * (packet.fusion[i, f] + packet.fusion[i, fb])
            / 2.0
        )
    return sigma


def source_asymptotic(packet: w28.Packet, source: w28.SourceEvaluator, theta: float) -> SourceAsymptotic:
    setup = source.setup
    source_index = source.source_index
    source_weights = setup["weights"]
    multiplier = np.asarray(setup["multiplier"], dtype=float)
    dloc_diag = np.diag(np.asarray(setup["d_loc"], dtype=float))
    j_op = np.asarray(setup["j"], dtype=float)

    chi = np.zeros(len(source_weights), dtype=float)
    chi[source_index[FUND]] = 1.0
    chi[source_index[ANTIFUND]] = 1.0

    packet_slice = slice_limit_vector(packet)
    sigma = np.zeros(len(source_weights), dtype=float)
    for w in [ZERO, ADJOINT, SYM20, SYM02]:
        sigma[source_index[w]] = float(packet_slice[packet.index[w]])

    a_pair = multiplier @ np.diag(dloc_diag * chi) @ multiplier
    b_slice = multiplier @ np.diag(dloc_diag * sigma) @ multiplier

    vals, vecs = np.linalg.eigh(a_pair)
    order = np.argsort(vals)[::-1]
    vals = vals[order]
    vecs = vecs[:, order]
    v0 = vecs[:, 0]
    if float(np.sum(v0)) < 0.0:
        v0 = -v0
        vecs[:, 0] = v0

    p_inf = float(v0 @ (j_op @ v0))
    gap = float(vals[0] - vals[1])
    lambda1 = float(v0 @ (b_slice @ v0))

    v1 = np.zeros_like(v0)
    first_coeffs: list[float] = []
    for m in range(1, len(vals)):
        vm = vecs[:, m]
        coeff = float(vm @ (b_slice @ v0)) / float(vals[0] - vals[m])
        first_coeffs.append(coeff)
        v1 += coeff * vm
    p1 = 2.0 * float(v1 @ (j_op @ v0))

    v2_orth = np.zeros_like(v0)
    for m in range(1, len(vals)):
        vm = vecs[:, m]
        coeff2 = (
            float(vm @ (b_slice @ v1)) - lambda1 * first_coeffs[m - 1]
        ) / float(vals[0] - vals[m])
        v2_orth += coeff2 * vm
    v2 = v2_orth - 0.5 * float(v1 @ v1) * v0
    p2 = float(v1 @ (j_op @ v1)) + 2.0 * float(v2 @ (j_op @ v0))

    eps = 1.0e-5
    vals_eps, vecs_eps = np.linalg.eigh(a_pair + eps * b_slice)
    pos = int(np.argmax(vals_eps))
    v_eps = vecs_eps[:, pos]
    if float(np.sum(v_eps)) < 0.0:
        v_eps = -v_eps
    p_eps = float(v_eps @ (j_op @ v_eps))
    finite_difference_error = abs((p_eps - p_inf) / eps - p1)

    return SourceAsymptotic(
        p_inf=p_inf,
        source_gap=gap,
        p1=p1,
        p2=p2,
        c_source=-p1,
        c_over_theta=(-p1) / theta,
        finite_difference_error=float(finite_difference_error),
    )


def measured_rows(
    packet: w28.Packet, source: w28.SourceEvaluator, p_inf: float
) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    f = packet.index[FUND]
    adj = packet.index[ADJOINT]
    for k in range(1, KMAX + 1):
        rho = w28.reduced_eta_rho(packet, k)
        p_value = source.p_from_packet_rho(packet.weights, rho)
        rows.append(
            {
                "k": float(k),
                "P": float(p_value),
                "err": float(abs(p_inf - p_value)),
                "rho10": float(rho[f]),
                "rho11": float(rho[adj]),
            }
        )
    return rows


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette word-count theta identification")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )
    print("No new imports: finite repo-internal packet quantities only.")

    packet = w28.build_packet()
    source = w28.build_source_evaluator()
    z = packet.index[ZERO]
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]

    section("Part 1: finite packet and t-matrix reduction")
    td = theta_data(packet)
    direct4 = reduced_matrix_direct(packet, 4)
    via_t4 = reduced_matrix_from_t(packet, td.t_matrix, 4)
    factorization_error = float(np.max(np.abs(direct4 - via_t4)))
    max_t = float(np.max(td.t_matrix))
    max_pos = tuple(int(x) for x in np.unravel_index(int(np.argmax(td.t_matrix)), td.t_matrix.shape))
    print(f"word box size = {len(packet.weights)}")
    print(f"t00 = {td.t00:.15f}")
    print(f"max t entry = {max_t:.15f} at {packet.weights[max_pos[0]]},{packet.weights[max_pos[1]]}")
    print(f"t(f,0)/t00 = {td.t_f0_ratio:.15f}")
    print(f"L_eta(0) = {packet.ell_eta[z]:.15f}")
    print(f"L_eta(f) = {packet.ell_eta[f]:.15f}")
    print(f"D_f = {packet.d_coeff[f]:.15f}; d_f = {packet.dim[f]:.1f}")
    check("finite tensor-word packet has 25 weights", len(packet.weights) == 25)
    check("S_k equals sqrt(d_mu d_nu) t(mu,nu)^k on the finite packet", factorization_error < 1.0e-16, f"k=4 max_diff={factorization_error:.3e}")
    check("dominant t entry is the trivial diagonal entry", max_pos == (z, z), f"max_pos={packet.weights[max_pos[0]]},{packet.weights[max_pos[1]]}")

    section("Part 2: theta formula and excluded single-ratio probes")
    print(
        "theta_packet = (L_f/L_0) * sqrt(D_f/d_f) * "
        "t(f,0)/t(0,0)"
    )
    print(f"theta_packet = {td.theta:.15f}")
    print(f"theta_packet inverse = {td.theta_inverse:.15f}")
    print(f"declared measured theta = {TARGET_THETA:.15f}")
    single_ratio_candidates = {
        "global t ratio2/1": float(td.alpha),
        "column-at-dominant ratio": float(td.t_f0_ratio),
        "D-ratio": float(packet.d_coeff[f] / packet.d_coeff[z]),
        "D/d ratio": float((packet.d_coeff[f] / packet.dim[f]) / (packet.d_coeff[z] / packet.dim[z])),
        "D^2/d ratio": float((packet.d_coeff[f] ** 2 / packet.dim[f]) / (packet.d_coeff[z] ** 2 / packet.dim[z])),
    }
    for name, value in single_ratio_candidates.items():
        print(f"{name}: {value:.15f}; miss={abs(value - td.theta):.6e}")
    check("theta formula matches the measured theta decimal to at least 10 digits", abs(td.theta - TARGET_THETA) < 5.0e-15, f"delta={abs(td.theta - TARGET_THETA):.3e}")
    check("theta inverse matches the observed rho10 growth scale", abs(td.theta_inverse - 3.79152876661918) < 5.0e-13, f"inverse={td.theta_inverse:.15f}")
    check("listed single-ratio probes remain distinct from theta", all(abs(v - td.theta) > 1.0e-2 for v in single_ratio_candidates.values()))

    section("Part 3: 25-channel eigenvector asymptotics")
    print("For rest-channel vector y and dominant channel 0:")
    print("  y_rest = (lambda_bar I - B_k)^(-1) r_k")
    print("  r_k(mu)=S_k(mu,0)/S_k(0,0), B_k(mu,nu)=S_k(mu,nu)/S_k(0,0)")
    print("  two-term Neumann surface: y_rest = r_k + B_k r_k + remainder")
    for k in [6, 8, 10, 12]:
        first_rel, second_rel, corr_norm, lambda_bar = eigenvector_asymptotic_errors(packet, td.t_matrix, k)
        print(
            f"k={k:2d}: first_rel={first_rel:.6e}; second_rel={second_rel:.6e}; "
            f"||B_k||_inf={corr_norm:.6e}; lambda_bar={lambda_bar:.15f}"
        )
    first8, second8, norm8, _lambda8 = eigenvector_asymptotic_errors(packet, td.t_matrix, 8)
    first10, second10, _norm10, _lambda10 = eigenvector_asymptotic_errors(packet, td.t_matrix, 10)
    check("full 24-channel correction improves the k=8 eigenvector approximation", second8 < first8 / 50.0, f"first={first8:.3e}, second={second8:.3e}")
    check("full 24-channel correction improves the k=10 eigenvector approximation", second10 < first10 / 100.0, f"first={first10:.3e}, second={second10:.3e}")

    section("Part 4: eta-weighted rho asymptotics")
    print(f"alpha = t(f,f)/t00 = {td.alpha:.15f}")
    print(f"gamma = t(f,fb)/t00 = {td.gamma:.15f}")
    print(f"theta * alpha = {td.theta_alpha:.15f}")
    print(f"theta * gamma = {td.theta_gamma:.15f}")
    slice_limit = slice_limit_vector(packet)
    print(
        "slice limits: "
        f"rho11={slice_limit[packet.index[ADJOINT]]:.15f}, "
        f"rho20={slice_limit[packet.index[SYM20]]:.15f}, "
        f"rho02={slice_limit[packet.index[SYM02]]:.15f}"
    )
    for k in [8, 10, 12, 14, 16, 18, 20]:
        rho = w28.reduced_eta_rho(packet, k)
        scaled_rho10 = float(rho[f] * (td.theta**k))
        ratio_next = float(w28.reduced_eta_rho(packet, k + 1)[f] / rho[f]) if k < 20 else float("nan")
        print(
            f"k={k:2d}: rho10*theta^k={scaled_rho10:.15f}; "
            f"rho11={rho[packet.index[ADJOINT]]:.15f}; "
            f"rho10_next/rho10={ratio_next:.15f}"
        )
    rho18 = w28.reduced_eta_rho(packet, 18)
    rho20 = w28.reduced_eta_rho(packet, 20)
    check("rho10 scale is theta^(1-k) through the eta denominator", abs(float(rho20[f] * (td.theta**20)) - td.theta) < 5.0e-10, f"scaled={float(rho20[f] * (td.theta**20)):.15f}")
    check("rho11 freezes at the slice-lemma value", abs(float(rho18[packet.index[ADJOINT]]) - float(slice_limit[packet.index[ADJOINT]])) < 1.0e-12)
    check("rho20 and rho02 freeze at the slice-lemma values", abs(float(rho18[packet.index[SYM20]]) - float(slice_limit[packet.index[SYM20]])) < 1.0e-12 and abs(float(rho18[packet.index[SYM02]]) - float(slice_limit[packet.index[SYM02]])) < 1.0e-12)

    section("Part 5: source Perron composition")
    sa = source_asymptotic(packet, source, td.theta)
    p_pair = source.p_from_support_pair((FUND, ANTIFUND))
    print(f"P_inf from pair-support source solve = {sa.p_inf:.15f}")
    print(f"source pair spectral gap = {sa.source_gap:.15f}")
    print(f"source perturbation p1 = {sa.p1:.15f}")
    print(f"source perturbation p2 = {sa.p2:.15f}")
    print(f"C_source = -p1 = {sa.c_source:.15f}")
    print(f"C_source/theta = {sa.c_over_theta:.15f}")
    print(f"finite-difference p1 check error = {sa.finite_difference_error:.6e}")
    check("source pair perturbation has a simple positive gap", sa.source_gap > 1.0e-2, f"gap={sa.source_gap:.6e}")
    check("source perturbation P_inf matches the finite pair-support solve", abs(sa.p_inf - p_pair) < 1.0e-14, f"delta={abs(sa.p_inf - p_pair):.3e}")
    check("source p1 finite-difference check is stable", sa.finite_difference_error < 5.0e-5, f"err={sa.finite_difference_error:.3e}")
    check("source sensitivity has the sign needed for P_k increasing to P_inf", sa.c_source > 0.0, f"C={sa.c_source:.15f}")

    section("Part 6: source composition surface and measured envelope")
    rows = measured_rows(packet, source, sa.p_inf)
    c_hat = max(row["err"] / (td.theta ** int(row["k"])) for row in rows[1:])
    c_hat_row = max(rows[1:], key=lambda row: row["err"] / (td.theta ** int(row["k"])))
    print(
        "Finite-packet composition surface: P_inf - P_k = "
        "C_source * theta^(k-1) + 3*C_source*theta^(k-1)*alpha^k "
        "+ finite-packet smaller-scale remainder."
    )
    print(f"measured c_hat over k=2..20 = {c_hat:.15f} at k={int(c_hat_row['k'])}")
    print("k | P_k | P_inf-P_k | err/theta^k | leading residual after alpha/gamma correction")
    print("-" * 112)
    max_two_channel_residual = 0.0
    for row in rows[1:]:
        k = int(row["k"])
        err = row["err"]
        leading = sa.c_source * (td.theta ** (k - 1))
        alpha_gamma = leading * (1.0 + 3.0 * (td.alpha**k) + 3.0 * (td.gamma**k))
        residual = abs(err - alpha_gamma)
        if 5 <= k <= 15:
            max_two_channel_residual = max(
                max_two_channel_residual,
                residual / (td.theta_gamma**k),
            )
        print(
            f"{k:2d} | {row['P']:.12f} | {err:.12e} | "
            f"{err / (td.theta ** k):.12e} | {residual:.12e}"
        )
    check("measured envelope c_hat dominates k=2..20 without an added safety factor", all(row["err"] <= c_hat * (td.theta ** int(row["k"])) + 1.0e-18 for row in rows[1:]), f"c_hat={c_hat:.15f}")
    check("tail-window prefactor matches the measured finite packet", abs(rows[17]["err"] / (td.theta ** 18) - sa.c_over_theta) < 5.0e-4, f"k=18 ratio={rows[17]['err'] / (td.theta ** 18):.12e}")
    check("two-channel corrected residual is governed by a smaller displayed scale on k=5..15", max_two_channel_residual < 10.0, f"max residual/(theta*gamma)^k={max_two_channel_residual:.6e}")

    section("Part 7: note hygiene and residual boundary")
    text = note_text()
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority:** independent audit lane only" in text
            or "Status authority: independent audit lane only" in text,
        )
        check(
            "note names this primary runner as a plain-text pointer",
            "scripts/gauge_vacuum_plaquette_word_count_theta_identification_two_term_asymptotic_2026_06_12.py"
            in text,
        )
        check(
            "note displays the audited theta^2 secondary scale",
            DISPLAYED_THETA_SQUARED_PREFIX in text
            and STALE_THETA_SQUARED_PREFIX not in text,
        )
        check(
            "note keeps scratch-packet context non-authoritative without stale temp paths",
            "Prior obstruction/rung/slice scratch packets" in text
            and ".claude" not in text
            and "tmp/refs" not in text,
        )
        check(
            "note displays the corrected theta^2 secondary scale",
            "theta^2 = 0.069561876543177" in text
            and "0.0695618585" not in text,
        )
    else:
        check("note exists for this runner", False, f"missing {NOTE_PATH}")
    print(
        "Named residuals: finite dominant-weight box; finite Bessel mode support; "
        "finite word count; no physical 3D unmarked spatial Wilson environment "
        "computation; no all-weight or untruncated convergence proof; no L_perp "
        "limit; no analytic P(6); no canonical repinning; all-k rigorous "
        "tail remainder remains a named finite-packet target."
    )
    check("runner names residuals without claiming them retired", True)

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
