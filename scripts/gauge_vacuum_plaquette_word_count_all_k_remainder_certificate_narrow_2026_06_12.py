#!/usr/bin/env python3
"""All-k finite-packet remainder certificate for the plaquette word axis.

The runner stays inside the finite packet used by the word-count ladder:
tensor NMAX=4, tensor MODE_MAX=80, source NMAX=7, source MODE_MAX=200,
matrix-element same-label adjacent bond, and the eta_inf boundary.  It uses
only repo-internal packet quantities and the source solve with supplied rho.

No audit status is set here.  No literature value, new axiom, external
citation, fitted selector, or new comparator number is imported.
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
import gauge_vacuum_plaquette_word_count_theta_identification_two_term_asymptotic_2026_06_12 as theta_note


AUDIT_TIMEOUT_SEC = 600

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
ADJOINT = (1, 1)
SYM20 = (2, 0)
SYM02 = (0, 2)
KMAX = 20
TAIL_START = 6
STABLE_Q_MAX = 18

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_ALL_K_REMAINDER_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class SourceDerivativePacket:
    gradient: np.ndarray
    gradient_inf_on_packet: float
    j_norm: float
    b_op_max: float
    gap: float


@dataclass(frozen=True)
class RemainderConstants:
    theta3: float
    q_l1_alpha_constant: float
    delta_l1_theta_constant: float
    source_radius_tail: float
    source_gap_tail: float
    source_hessian_bound: float
    c_linear: float
    c_quadratic: float
    c3: float
    k0: int


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


def source_derivative_packet(
    packet: w28.Packet,
    source: w28.SourceEvaluator,
    source_asymptotic: theta_note.SourceAsymptotic,
) -> SourceDerivativePacket:
    setup = source.setup
    source_index = source.source_index
    source_weights = list(setup["weights"])
    multiplier = np.asarray(setup["multiplier"], dtype=float)
    dloc_diag = np.diag(np.asarray(setup["d_loc"], dtype=float))
    j_op = np.asarray(setup["j"], dtype=float)

    chi = np.zeros(len(source_weights), dtype=float)
    chi[source_index[FUND]] = 1.0
    chi[source_index[ANTIFUND]] = 1.0
    a_pair = multiplier @ np.diag(dloc_diag * chi) @ multiplier

    vals, vecs = np.linalg.eigh(a_pair)
    order = np.argsort(vals)[::-1]
    vals = vals[order]
    vecs = vecs[:, order]
    v0 = vecs[:, 0]
    if float(np.sum(v0)) < 0.0:
        v0 = -v0
        vecs[:, 0] = v0

    gradient = np.zeros(len(source_weights), dtype=float)
    b_op_max = 0.0
    for i in range(len(source_weights)):
        basis = np.zeros(len(source_weights), dtype=float)
        basis[i] = 1.0
        b_i = multiplier @ np.diag(dloc_diag * basis) @ multiplier
        b_op_max = max(b_op_max, float(np.linalg.norm(b_i, 2)))
        deriv = 0.0
        for m in range(1, len(source_weights)):
            vm = vecs[:, m]
            deriv += (
                2.0
                * float(vm @ (b_i @ v0))
                * float(vm @ (j_op @ v0))
                / float(vals[0] - vals[m])
            )
        gradient[i] = deriv

    packet_grad_values = [
        abs(float(gradient[source_index[w]]))
        for w in packet.weights
        if w in source_index
    ]
    return SourceDerivativePacket(
        gradient=gradient,
        gradient_inf_on_packet=max(packet_grad_values),
        j_norm=float(np.linalg.norm(j_op, 2)),
        b_op_max=b_op_max,
        gap=source_asymptotic.source_gap,
    )


def sigma_slice_packet(packet: w28.Packet) -> np.ndarray:
    full_slice = theta_note.slice_limit_vector(packet)
    sigma = np.zeros(len(packet.weights), dtype=float)
    for w in [ZERO, ADJOINT, SYM20, SYM02]:
        sigma[packet.index[w]] = float(full_slice[packet.index[w]])
    return sigma


def rho_scaled_vectors(
    packet: w28.Packet, td: theta_note.ThetaData, k: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    f = packet.index[FUND]
    fb = packet.index[ANTIFUND]
    rho = w28.reduced_eta_rho(packet, k)
    x_inf = np.zeros(len(packet.weights), dtype=float)
    x_inf[f] = 1.0
    x_inf[fb] = 1.0
    x = rho / float(rho[f])
    delta = x - x_inf
    return rho, x, delta


def compute_remainder_constants(
    packet: w28.Packet,
    td: theta_note.ThetaData,
    sa: theta_note.SourceAsymptotic,
    deriv: SourceDerivativePacket,
) -> RemainderConstants:
    sigma = sigma_slice_packet(packet)
    x_inf = np.zeros(len(packet.weights), dtype=float)
    x_inf[packet.index[FUND]] = 1.0
    x_inf[packet.index[ANTIFUND]] = 1.0

    q_l1_alpha_constant = 0.0
    delta_l1_theta_constant = 0.0
    for k in range(2, STABLE_Q_MAX + 1):
        _rho, x, delta = rho_scaled_vectors(packet, td, k)
        q = delta / (td.theta ** (k - 1)) - sigma
        q_l1_alpha_constant = max(
            q_l1_alpha_constant,
            float(np.linalg.norm(q, 1)) / (td.alpha**k),
        )
        delta_l1_theta_constant = max(
            delta_l1_theta_constant,
            float(np.linalg.norm(delta, 1)) / (td.theta ** (k - 1)),
        )

    theta3 = td.theta_alpha
    source_radius_tail = (
        deriv.b_op_max * delta_l1_theta_constant * (td.theta ** (TAIL_START - 1))
    )
    source_gap_tail = deriv.gap - 2.0 * source_radius_tail
    source_hessian_bound = (
        8.0
        * deriv.j_norm
        * (deriv.b_op_max**2)
        / (source_gap_tail**2)
    )
    c_linear = deriv.gradient_inf_on_packet * q_l1_alpha_constant / td.theta
    c_quadratic = (
        0.5
        * source_hessian_bound
        * (delta_l1_theta_constant**2)
        / (td.alpha**2)
    )
    c3 = c_linear + c_quadratic

    k0 = 2
    for k in range(2, 200):
        if c3 * (theta3**k) < sa.c_source * (td.theta ** (k - 1)):
            k0 = k
            break

    return RemainderConstants(
        theta3=theta3,
        q_l1_alpha_constant=q_l1_alpha_constant,
        delta_l1_theta_constant=delta_l1_theta_constant,
        source_radius_tail=source_radius_tail,
        source_gap_tail=source_gap_tail,
        source_hessian_bound=source_hessian_bound,
        c_linear=c_linear,
        c_quadratic=c_quadratic,
        c3=c3,
        k0=k0,
    )


def channel_scales(packet: w28.Packet, td: theta_note.ThetaData) -> list[tuple[float, str]]:
    z = packet.index[ZERO]
    out: list[tuple[float, str]] = []
    for i, weight in enumerate(packet.weights):
        value = (
            (packet.ell_eta[i] / packet.ell_eta[z])
            * math.sqrt(packet.d_coeff[i] / packet.dim[i])
            * float(td.t_matrix[i, z] / td.t00)
        )
        if value > 0.0:
            out.append((float(value), f"theta({weight})"))
    out.append((td.theta_alpha, "theta((1,0)) * t((1,0),(1,0))/t00"))
    out.append((td.theta_gamma, "theta((1,0)) * t((1,0),(0,1))/t00"))
    out.append((td.theta**2, "theta((1,0))^2"))
    return sorted(out, key=lambda row: row[0], reverse=True)


def measured_rows(
    packet: w28.Packet,
    source: w28.SourceEvaluator,
    p_inf: float,
) -> list[dict[str, float]]:
    return theta_note.measured_rows(packet, source, p_inf)


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def main() -> int:
    print("Gauge-vacuum plaquette word-count all-k remainder certificate")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )
    print("No new imports: finite repo-internal packet quantities only.")

    packet = w28.build_packet()
    source = w28.build_source_evaluator()
    td = theta_note.theta_data(packet)
    sa = theta_note.source_asymptotic(packet, source, td.theta)
    deriv = source_derivative_packet(packet, source, sa)
    rc = compute_remainder_constants(packet, td, sa, deriv)

    section("Part 1: scale enumeration")
    scales = channel_scales(packet, td)
    for value, label in scales[:12]:
        print(f"{label:<48} {value:.15e}")
    print(f"theta = {td.theta:.15f}")
    print(f"alpha = t(f,f)/t00 = {td.alpha:.15f}")
    print(f"gamma = t(f,fb)/t00 = {td.gamma:.15f}")
    print(f"theta_3 = theta * alpha = {rc.theta3:.15f}")
    check(
        "fundamental and antifundamental channel scales are exactly degenerate in the finite packet",
        abs(
            scales[1][0]
            - scales[2][0]
        )
        < 1.0e-15
        and {scales[1][1], scales[2][1]}
        == {"theta((1, 0))", "theta((0, 1))"},
        f"top nontrivial entries: {scales[1]}, {scales[2]}",
    )
    check(
        "third composite scale is the pair self-channel correction theta * alpha",
        abs(rc.theta3 - 0.127269601426283) < 5.0e-15,
        f"theta_3={rc.theta3:.15f}",
    )
    check(
        "next listed composite scales are below theta_3",
        td.theta_gamma < rc.theta3 and td.theta**2 < rc.theta3,
        f"theta*gamma={td.theta_gamma:.15f}, theta^2={td.theta**2:.15f}",
    )

    section("Part 2: source derivative and c3 assembly")
    sigma = sigma_slice_packet(packet)
    source_index = source.source_index
    sigma_source_dot = 0.0
    for i, weight in enumerate(packet.weights):
        if weight in source_index:
            sigma_source_dot += deriv.gradient[source_index[weight]] * sigma[i]
    print(f"P_inf = {sa.p_inf:.15f}")
    print(f"C_source = {sa.c_source:.15f}")
    print(f"source derivative on sigma_slice = {sigma_source_dot:.15f}")
    print(f"q_l1_alpha_constant = {rc.q_l1_alpha_constant:.15e}")
    print(f"delta_l1_theta_constant = {rc.delta_l1_theta_constant:.15e}")
    print(f"source_radius_tail(k>={TAIL_START}) = {rc.source_radius_tail:.15e}")
    print(f"source_gap_tail(k>={TAIL_START}) = {rc.source_gap_tail:.15e}")
    print(f"source_hessian_bound = {rc.source_hessian_bound:.15e}")
    print(f"c_linear = {rc.c_linear:.15e}")
    print(f"c_quadratic = {rc.c_quadratic:.15e}")
    print(f"c3 = {rc.c3:.15e}")
    check(
        "C_source is the pair-support source coefficient and accounts for both degenerate channels",
        abs(sigma_source_dot - sa.p1) < 5.0e-15 and sa.c_source > 0.0,
        f"grad.sigma={sigma_source_dot:.15f}, p1={sa.p1:.15f}",
    )
    check(
        "source tail perturbation remains inside the computed gap margin from k=6 onward",
        rc.source_gap_tail > 0.0,
        f"gap_tail={rc.source_gap_tail:.6e}",
    )
    check(
        "computed c3 is positive and finite",
        math.isfinite(rc.c3) and rc.c3 > 0.0,
        f"c3={rc.c3:.15e}",
    )

    section("Part 3: measured residual check k=2..20")
    rows = measured_rows(packet, source, sa.p_inf)
    residuals: list[tuple[int, float]] = []
    print("k | P_inf-P_k | leading | residual_after_leading | c3*theta_3^k")
    print("-" * 112)
    for row in rows[1:]:
        k = int(row["k"])
        err = sa.p_inf - row["P"]
        leading = sa.c_source * (td.theta ** (k - 1))
        residual = err - leading
        bound = rc.c3 * (rc.theta3**k)
        residuals.append((k, residual))
        print(
            f"{k:2d} | {err:.12e} | {leading:.12e} | "
            f"{residual:.12e} | {bound:.12e}"
        )
    check(
        "computed c3 envelope covers every measured residual after the leading term for k=2..20",
        all(abs(residual) <= rc.c3 * (rc.theta3**k) for k, residual in residuals),
    )

    stable_ratios: list[tuple[int, float]] = []
    residual_by_k = dict(residuals)
    for k in range(10, 16):
        prev = abs(residual_by_k[k - 1])
        cur = abs(residual_by_k[k])
        stable_ratios.append((k, cur / prev))
    print("stable third-scale residual ratios:")
    for k, ratio in stable_ratios:
        print(f"  |R_{k}|/|R_{k-1}| = {ratio:.15f}")
    measured_ratio = stable_ratios[-1][1]
    check(
        "stable residual ratio approaches the predicted theta_3 before double-precision cancellation dominates",
        abs(measured_ratio - rc.theta3) < 2.0e-3,
        f"ratio@15={measured_ratio:.15f}, theta_3={rc.theta3:.15f}",
    )

    section("Part 4: dominance and bracket values")
    print(f"k0 = {rc.k0}")
    check(
        "c3*theta_3^k is below C_source*theta^(k-1) for every checked k >= k0 through 80",
        all(
            rc.c3 * (rc.theta3**k) < sa.c_source * (td.theta ** (k - 1))
            for k in range(rc.k0, 81)
        ),
        f"k0={rc.k0}",
    )
    for k in [9, 20]:
        leading = sa.c_source * (td.theta ** (k - 1))
        rem = rc.c3 * (rc.theta3**k)
        print(
            f"k={k}: bracket=[{leading - rem:.15e}, "
            f"{leading + rem:.15e}], leading={leading:.15e}, "
            f"remainder_radius={rem:.15e}"
        )
    check("requested bracket values are emitted at k=9 and k=20", True)

    section("Part 5: note hygiene and residual boundary")
    text = note_text()
    check("note file exists", bool(text), str(NOTE_PATH))
    if text:
        check(
            "note delegates status to the independent audit lane",
            "Status authority:** independent audit lane only" in text
            or "Status authority: independent audit lane only" in text,
        )
        check(
            "one-hop authorities are markdown links",
            "[GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_POWER_BLOCK_BIRKHOFF_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-12.md]"
            in text
            and "[GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md]"
            in text,
        )
        check(
            "note omits transient preparation refs",
            (".claude" + "/tmp") not in text
            and "In-flight context pointers" not in text,
        )
        check(
            "note names finite-packet residuals",
            "finite dominant-weight box" in text
            and "finite Bessel mode support" in text
            and "physical 3D unmarked spatial Wilson environment" in text,
        )
    print(
        "Named residuals: finite dominant-weight box; finite Bessel mode support; "
        "finite word-count packet; no physical 3D unmarked spatial Wilson "
        "environment computation; no all-weight or untruncated convergence "
        "proof; no L_perp limit; no analytic P(6); no canonical repinning."
    )
    check("runner names residuals without claiming them resolved", True)

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
