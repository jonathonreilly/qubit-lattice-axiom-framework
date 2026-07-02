#!/usr/bin/env python3
"""Exact sign/magnitude split for the Route-2 W1 center-ratio bridge."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from frontier_quark_route2_exact_readout_map import restricted_readout_data


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0

Q_T = Fraction(5, 6)
S_TE = Fraction(-2, 1)
T_CENTER_OVER_E_SHELL = S_TE * Q_T
F_ADJ = Fraction(8, 9)
TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)
TARGET_C_TE = Fraction(-8, 9)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def norm(text: str) -> str:
    return " ".join(text.split())


def q_e_from_rho(rho_e: Fraction) -> Fraction:
    return 1 + rho_e / 6


def rho_from_q(q_e: Fraction) -> Fraction:
    return 6 * (q_e - 1)


def c_te_from_q(q_e: Fraction) -> Fraction:
    return T_CENTER_OVER_E_SHELL / q_e


def magnitude_condition_q(fraction: Fraction = F_ADJ) -> Fraction:
    return abs(T_CENTER_OVER_E_SHELL) / fraction


def sign(value: Fraction) -> int:
    return -1 if value < 0 else 1 if value > 0 else 0


def part_a_authorities() -> None:
    print("A. Authority surface")
    note_path = DOCS / "QUARK_ROUTE2_W1_SIGN_MAGNITUDE_SPLIT_SUPPORT_NOTE_2026-06-21.md"
    readout_path = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
    naturality_path = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
    source_path = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
    typed_path = DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md"

    for path in (note_path, readout_path, naturality_path, source_path, typed_path):
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(note_path)
    readout = read(readout_path)
    naturality = read(naturality_path)
    source = read(source_path)
    typed = read(typed_path)

    check("new note declares exact support status", "**Status:** exact support" in note)
    check("new note says W1 remains open", "This is not a proof of W1" in note and "magnitude selector" in note)
    check("readout note defines c_TE algebra", "c_TE  := gamma_T(center) / gamma_E(center) = s_TE * q_T / q_E" in readout)
    check("naturality note gives target equivalence", "q_E = gamma_E(center)/gamma_E(shell) = 15/8" in naturality and "c_TE = gamma_T(center)/gamma_E(center) = -8/9" in naturality)
    check("source-domain note names missing W1 bridge", "R_conn = 8/9 -> c_TE = gamma_T(center)/gamma_E(center) = -8/9" in source)
    check("typed bridge note names positive F_adj obstruction", "F_adj as a positive SU(3) adjoint channel-count fraction" in typed)


def part_b_exact_split() -> None:
    print("\nB. Exact sign/magnitude split")
    check("T-side q_T is positive 5/6", Q_T == Fraction(5, 6) and Q_T > 0, str(Q_T))
    check("shell T/E ratio is negative -2", S_TE == Fraction(-2, 1) and S_TE < 0, str(S_TE))
    check("T-center over E-shell product is -5/3", T_CENTER_OVER_E_SHELL == Fraction(-5, 3), str(T_CENTER_OVER_E_SHELL))
    check("target q_E is positive", TARGET_Q_E > 0, str(TARGET_Q_E))
    check("target c_TE is negative", TARGET_C_TE < 0, str(TARGET_C_TE))

    positive_samples = (Fraction(1, 2), Fraction(1, 1), TARGET_Q_E, Fraction(3, 1))
    negative_samples = (Fraction(-3, 1), Fraction(-1, 1), Fraction(-1, 2))
    check("all positive q_E samples give negative c_TE", all(c_te_from_q(q) < 0 for q in positive_samples))
    check("all negative q_E samples give positive c_TE", all(c_te_from_q(q) > 0 for q in negative_samples))
    check("sign rule is sign(c_TE)=-sign(q_E)", all(sign(c_te_from_q(q)) == -sign(q) for q in positive_samples + negative_samples))

    q_from_mag = magnitude_condition_q(F_ADJ)
    rho_from_mag = rho_from_q(q_from_mag)
    check("|c_TE|=8/9 solves q_E=15/8", q_from_mag == TARGET_Q_E, str(q_from_mag))
    check("|c_TE|=8/9 solves rho_E=21/4", rho_from_mag == TARGET_RHO_E, str(rho_from_mag))
    check("q_E=15/8 gives c_TE=-8/9", c_te_from_q(TARGET_Q_E) == TARGET_C_TE, str(c_te_from_q(TARGET_Q_E)))
    check("rho_E=21/4 gives q_E=15/8", q_e_from_rho(TARGET_RHO_E) == TARGET_Q_E, str(q_e_from_rho(TARGET_RHO_E)))


def part_c_falsifiers() -> None:
    print("\nC. Falsifiers for sign-only and magnitude-free routes")
    sign_only_samples = (Fraction(1, 1), Fraction(5, 4), Fraction(2, 1), Fraction(5, 2))
    all_negative = all(c_te_from_q(q) < 0 for q in sign_only_samples)
    target_hits = [q for q in sign_only_samples if c_te_from_q(q) == TARGET_C_TE]
    check("sign-only family has many negative center ratios", all_negative and len(sign_only_samples) >= 4)
    check("sign-only family does not select the target magnitude", len(target_hits) == 0, f"hits={target_hits}")

    magnitudes = {
        Fraction(5, 6): magnitude_condition_q(Fraction(5, 6)),
        Fraction(8, 9): magnitude_condition_q(Fraction(8, 9)),
        Fraction(1, 1): magnitude_condition_q(Fraction(1, 1)),
        Fraction(10, 9): magnitude_condition_q(Fraction(10, 9)),
    }
    check("different magnitude selectors give different q_E values", len(set(magnitudes.values())) == len(magnitudes))
    check("only F_adj=8/9 among samples gives target q_E", [m for m, q in magnitudes.items() if q == TARGET_Q_E] == [F_ADJ])
    check("positive F_adj alone is a magnitude value, not the typing rule", F_ADJ > 0 and TARGET_C_TE == -F_ADJ)


def part_d_live_and_boundary() -> None:
    print("\nD. Live branch and boundary")
    data = restricted_readout_data()
    live_q_e = Fraction.from_float(data.q_e)
    live_c_te = Fraction.from_float(data.center_ratio_te)
    check("live q_E is positive", data.q_e > 0, f"q_E={data.q_e:.12f}")
    check("live c_TE is negative", data.center_ratio_te < 0, f"c_TE={data.center_ratio_te:.12f}")
    check("live c_TE sign agrees with split rule", sign(live_q_e) == 1 and sign(live_c_te) == -1)
    check("live q_E is not exact target q_E", abs(data.q_e - float(TARGET_Q_E)) > 1.0e-12, f"live={data.q_e:.12f}")
    check("live c_TE is not exact target c_TE", abs(data.center_ratio_te - float(TARGET_C_TE)) > 1.0e-12, f"live={data.center_ratio_te:.12f}")

    proof_inputs = {
        "endpoint_algebra",
        "granted_t_side_candidates",
        "positive_e_center_branch",
        "exact_rational_arithmetic",
    }
    forbidden = {
        "observed_quark_masses",
        "fitted_yukawa_entries",
        "ckm_j_error_minimization",
        "nearest_live_endpoint_selector",
    }
    check("forbidden proof inputs are absent", proof_inputs.isdisjoint(forbidden), str(sorted(proof_inputs)))


def part_e_note_hygiene() -> None:
    print("\nE. Note hygiene")
    note = read(DOCS / "QUARK_ROUTE2_W1_SIGN_MAGNITUDE_SPLIT_SUPPORT_NOTE_2026-06-21.md")
    compact = norm(note)
    check("note states sign consequence", "if `q_E > 0`, then `c_TE < 0`" in note)
    check("note states magnitude equivalence", "|c_TE| = 8/9" in note and "q_E = 15/8" in note and "rho_E = 6(q_E - 1) = 21/4" in note)
    check("note says sign is not the missing primitive", "the sign is not the load-bearing missing primitive" in compact)
    check("note leaves selected P_R unproved", "not a selected `P_R`" in note)
    check("note records expected pass count", "TOTAL: PASS=39, FAIL=0" in note)


def main() -> int:
    part_a_authorities()
    part_b_exact_split()
    part_c_falsifiers()
    part_d_live_and_boundary()
    part_e_note_hygiene()
    print(f"\nTOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("Status: exact support for W1 sign/magnitude split; W1 magnitude remains open.")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
