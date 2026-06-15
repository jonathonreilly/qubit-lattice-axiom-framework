#!/usr/bin/env python3
"""End-to-end composition check for the finite derived word-chain packet.

This runner composes already-built finite packet pieces:

* tensor word NMAX=4, MODE_MAX=80;
* source readout NMAX=7, MODE_MAX=200;
* matrix-element same-label adjacent bond;
* eta_inf boundary on unmarked word slots;
* rank-25 reduced word-count family;
* pair-support source limit and the all-k remainder constants.

It is a composition check, not a re-derivation of the source-dependency notes. No
review outcome is set here. No literature value, new axiom, external citation,
new comparator number, or fitted selector is imported.
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gauge_vacuum_plaquette_tensor_word_perron_derived_rho_composed_readout_2026_06_11 as one_word
import gauge_vacuum_plaquette_word_count_all_k_remainder_certificate_narrow_2026_06_12 as remainder_note
import gauge_vacuum_plaquette_word_count_power_block_birkhoff_certificate_narrow_2026_06_12 as w28
import gauge_vacuum_plaquette_word_count_theta_identification_two_term_asymptotic_2026_06_12 as theta_note


AUDIT_TIMEOUT_SEC = 600

ZERO = (0, 0)
FUND = (1, 0)
ANTIFUND = (0, 1)
ADJOINT = (1, 1)

NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "GAUGE_VACUUM_PLAQUETTE_DERIVED_WORD_CHAIN_END_TO_END_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-12.md"
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


def section(title: str) -> None:
    print()
    print("=" * 112)
    print(title)
    print("=" * 112)


def p_for_k(packet: w28.Packet, source: w28.SourceEvaluator, words: int) -> float:
    rho = w28.reduced_eta_rho(packet, words)
    return source.p_from_packet_rho(packet.weights, rho)


def source_pair_value(source_nmax: int, source_mode_max: int) -> float:
    setup = one_word.source_setup(source_nmax, source_mode_max)
    index = dict(setup["index"])
    rho_vec = np.zeros(len(setup["weights"]), dtype=float)
    rho_vec[index[FUND]] = 1.0
    rho_vec[index[ANTIFUND]] = 1.0
    _eig, p_value, _psi, _u0 = one_word.source_perron_from_rho_vector(
        setup, rho_vec
    )
    return float(p_value)


def note_text() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def parse_checked_ledger(text: str) -> dict[str, float]:
    start = "<!-- runner-checked-ledger:start -->"
    end = "<!-- runner-checked-ledger:end -->"
    if start not in text or end not in text:
        return {}
    body = text.split(start, 1)[1].split(end, 1)[0]
    out: dict[str, float] = {}
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|") or "---" in line or "key" in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        key = cells[0].strip().strip("`")
        raw = cells[1].strip().strip("`")
        try:
            out[key] = float(raw)
        except ValueError:
            continue
    return out


def compare_float(key: str, observed: float, expected: float) -> bool:
    if key in {"tensor_NMAX", "tensor_MODE_MAX", "source_NMAX", "source_MODE_MAX", "k0"}:
        return int(round(observed)) == int(round(expected))
    atol = 5.0e-15
    rtol = 5.0e-13
    return math.isclose(observed, expected, rel_tol=rtol, abs_tol=atol)


def main() -> int:
    print("Gauge-vacuum plaquette derived word-chain end-to-end composition")
    print(
        "Status authority: independent audit lane only. This source runner "
        "does not set or predict an audit outcome."
    )
    print("No new imports: finite repo-internal packet quantities only.")

    packet = w28.build_packet()
    source = w28.build_source_evaluator()
    td = theta_note.theta_data(packet)
    sa = theta_note.source_asymptotic(packet, source, td.theta)
    deriv = remainder_note.source_derivative_packet(packet, source, sa)
    rc = remainder_note.compute_remainder_constants(packet, td, sa, deriv)

    section("Part 1: finite packet rebuild and derived reduced family")
    print(
        f"tensor NMAX={w28.TW_NMAX}, tensor MODE_MAX={w28.TW_MODE_MAX}, "
        f"source NMAX={w28.SOURCE_NMAX}, source MODE_MAX={w28.SOURCE_MODE_MAX}"
    )
    print(f"word box size = {len(packet.weights)}")
    print(f"eta_inf(0,0) = {packet.eta_inf[packet.index[ZERO]]:.15f}")
    print(f"theta = {td.theta:.15f}")
    print(f"theta_3 = {rc.theta3:.15f}")
    check("finite tensor word packet has the expected 25 weights", len(packet.weights) == 25)
    check(
        "derived theta formula reproduces the stated finite-packet value",
        abs(td.theta - 0.263745855973467) < 5.0e-15,
        f"theta={td.theta:.15f}",
    )
    check(
        "third scale is theta times the self-channel alpha",
        abs(rc.theta3 - td.theta * td.alpha) < 1.0e-16,
        f"theta_3={rc.theta3:.15f}, theta*alpha={td.theta * td.alpha:.15f}",
    )

    section("Part 2: source pair-support limit and word rungs")
    p_pair = source.p_from_support_pair((FUND, ANTIFUND))
    p_values = {k: p_for_k(packet, source, k) for k in [1, 2, 3, 4, 5, 9, 17, 20]}
    for k in [1, 2, 3, 4, 5, 9, 17, 20]:
        print(f"P_{k:<2d} = {p_values[k]:.15f}")
    print(f"P_inf(pair support) = {sa.p_inf:.15f}")
    print(f"distance to fenced comparator 0.5934 = {abs(sa.p_inf - one_word.CANONICAL_COMPARATOR):.15f}")
    check(
        "source pair-support solve matches P_inf",
        abs(p_pair - sa.p_inf) < 1.0e-14,
        f"p_pair={p_pair:.15f}, P_inf={sa.p_inf:.15f}",
    )
    check(
        "headline rungs reproduce the finite word-chain table",
        abs(p_values[1] - 0.434215413260) < 5.0e-13
        and abs(p_values[2] - 0.433061880380) < 5.0e-13
        and abs(p_values[3] - 0.543142610051) < 5.0e-13
        and abs(p_values[4] - 0.603630724651) < 5.0e-13,
    )
    check(
        "P20 is within the certified tail scale of P_inf",
        0.0 <= sa.p_inf - p_values[20] < 5.0e-12,
        f"P_inf-P20={sa.p_inf - p_values[20]:.12e}",
    )

    section("Part 3: remainder envelope on measured rungs")
    rows = theta_note.measured_rows(packet, source, sa.p_inf)
    residuals: list[tuple[int, float, float]] = []
    for row in rows[1:]:
        k = int(row["k"])
        err = sa.p_inf - row["P"]
        leading = sa.c_source * (td.theta ** (k - 1))
        residual = err - leading
        bound = rc.c3 * (rc.theta3**k)
        residuals.append((k, residual, bound))
        print(
            f"k={k:2d}: err={err:.12e}, leading={leading:.12e}, "
            f"residual={residual:.12e}, bound={bound:.12e}"
        )
    check(
        "all measured rungs k=2..20 satisfy the source-dependency remainder envelope",
        all(abs(residual) <= bound for _k, residual, bound in residuals),
    )
    check(
        "dominance gate is k0=17 and remains valid through k=80",
        rc.k0 == 17
        and all(
            rc.c3 * (rc.theta3**k) < sa.c_source * (td.theta ** (k - 1))
            for k in range(rc.k0, 81)
        ),
        f"k0={rc.k0}",
    )

    section("Part 4: source-box sensitivity is named, not hidden")
    source_box = {
        5: source_pair_value(5, one_word.SOURCE_MODE_MAX),
        7: source_pair_value(7, one_word.SOURCE_MODE_MAX),
        9: source_pair_value(9, one_word.SOURCE_MODE_MAX),
    }
    for nmax, p_value in source_box.items():
        print(f"source NMAX={nmax}: P_inf_pair = {p_value:.15f}")
    drift_57 = source_box[7] - source_box[5]
    drift_79 = source_box[9] - source_box[7]
    print(f"source NMAX 5->7 drift = {drift_57:.15e}")
    print(f"source NMAX 7->9 drift = {drift_79:.15e}")
    check(
        "the theorem surface is the source NMAX=7 pair-support value",
        abs(source_box[7] - sa.p_inf) < 1.0e-14,
    )
    check(
        "source-box drift is much smaller than the fenced comparator distance",
        max(abs(drift_57), abs(drift_79))
        < abs(sa.p_inf - one_word.CANONICAL_COMPARATOR),
        f"max_source_drift={max(abs(drift_57), abs(drift_79)):.6e}",
    )

    section("Part 5: note content and checked numeric ledger")
    text = note_text()
    check("composition note exists", bool(text), str(NOTE_PATH))
    if text:
        forbidden_phrases = [
            "only " + "route",
            "last " + "route",
            "ex" + "hausted",
            "closes " + "the program",
            "audit " + "status",
        ]
        ledger_expected = {
            "tensor_NMAX": float(w28.TW_NMAX),
            "tensor_MODE_MAX": float(w28.TW_MODE_MAX),
            "source_NMAX": float(w28.SOURCE_NMAX),
            "source_MODE_MAX": float(w28.SOURCE_MODE_MAX),
            "P_1": p_values[1],
            "P_2": p_values[2],
            "P_3": p_values[3],
            "P_4": p_values[4],
            "P_20": p_values[20],
            "P_inf": sa.p_inf,
            "theta": td.theta,
            "theta_inverse": td.theta_inverse,
            "theta_3": rc.theta3,
            "C_source": sa.c_source,
            "c3": rc.c3,
            "k0": float(rc.k0),
            "comparator_distance": abs(sa.p_inf - one_word.CANONICAL_COMPARATOR),
            "source_NMAX5_P_inf": source_box[5],
            "source_NMAX7_P_inf": source_box[7],
            "source_NMAX9_P_inf": source_box[9],
            "source_5_to_7_drift": drift_57,
            "source_7_to_9_drift": drift_79,
        }
        ledger = parse_checked_ledger(text)
        missing = sorted(set(ledger_expected) - set(ledger))
        unknown = sorted(set(ledger) - set(ledger_expected))
        mismatches = [
            key
            for key, expected in ledger_expected.items()
            if key in ledger and not compare_float(key, ledger[key], expected)
        ]
        check(
            "note delegates status to the independent audit lane",
            "Status authority:** independent audit lane only" in text
            or "Status authority: independent audit lane only" in text,
        )
        check(
            "one-hop authority inputs are markdown links",
            "[GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md]" in text
            and "[SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_TENSOR_TRANSFER_PERRON_SOLVE_NOTE.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_ALL_WEIGHT_CONVOLUTION_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-17.md]" in text,
        )
        check(
            "source dependency pointers use repo markdown links, not temp handles",
            (".claude" + "/tmp") not in text
            and "[GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_THETA_IDENTIFICATION_TWO_TERM_ASYMPTOTIC_NARROW_THEOREM_NOTE_2026-06-12.md]" in text
            and "[GAUGE_VACUUM_PLAQUETTE_WORD_COUNT_RUNG_FOUR_DEEP_RIM_BOUNDED_NOTE_2026-06-12.md]" in text,
        )
        check(
            "note avoids banned overreach phrases",
            not any(phrase in text for phrase in forbidden_phrases),
        )
        check(
            "checked numeric ledger has no missing or unknown rows",
            not missing and not unknown,
            f"missing={missing}, unknown={unknown}",
        )
        check(
            "every checked numeric ledger row matches recomputed values",
            not mismatches,
            f"mismatches={mismatches}",
        )
        check(
            "residual table names the required open targets",
            "word-geometry lift" in text
            and "L_perp on the physical surface" in text
            and "physical 3D rim" in text
            and "analytic P(6)" in text
            and "no repinning" in text,
        )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
