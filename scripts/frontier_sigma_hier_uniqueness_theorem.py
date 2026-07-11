#!/usr/bin/env python3
"""
sigma_hier supplied-input S3 table uniqueness theorem
======================================================

The theorem note registers packet (P-SIG): a supplied chamber pin, nine
external magnitude comparator windows, and an external CP-sign comparator
gate. This runner parses that fenced packet and constructs every scan input
from it. It then performs exact finite enumeration of S_3.

The result is deliberately narrow: sigma=(2,1,0) is the unique table row that
passes all nine supplied windows and the supplied sign gate. The runner does
not ratify the pin, the physical-sheet choice, or the observational authority
behind the comparator context, and it does not present those inputs as
framework derivations.
"""

from __future__ import annotations

import itertools
import math
import operator
import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=120)

PASS_COUNT = 0
FAIL_COUNT = 0

NOTE_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "SIGMA_HIER_UNIQUENESS_THEOREM_NOTE_2026-04-19.md"
)
WINDOW_LABELS = (
    "U_e1",
    "U_e2",
    "U_e3",
    "U_mu1",
    "U_mu2",
    "U_mu3",
    "U_tau1",
    "U_tau2",
    "U_tau3",
)
GATE_OPERATORS = {
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
}


@dataclass(frozen=True)
class SuppliedPacket:
    pin: tuple[float, float, float]
    window_labels: tuple[str, ...]
    pdg_lo: np.ndarray
    pdg_hi: np.ndarray
    sign_variable: str
    sign_operator: str
    sign_bound: float
    sign_gate_text: str
    block_text: str
    note_text: str


def parse_supplied_packet(note_path: Path) -> SuppliedPacket:
    note_text = note_path.read_text(encoding="utf-8")
    block_match = re.search(
        r"## Supplied-Input Registration \(P-SIG\)\s+"
        r"```text\n(?P<block>.*?)\n```",
        note_text,
        flags=re.DOTALL,
    )
    if block_match is None:
        raise ValueError("missing fenced (P-SIG) supplied-input packet")
    block_text = block_match.group("block")

    number = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?"
    pin_match = re.search(
        rf"^PIN:\s*m_\*\s*=\s*({number})\s*;\s*"
        rf"delta_\*\s*=\s*({number})\s*;\s*"
        rf"q_\+\*\s*=\s*({number})\s*$",
        block_text,
        flags=re.MULTILINE,
    )
    if pin_match is None:
        raise ValueError("missing or malformed PIN line in (P-SIG)")
    pin_values = tuple(float(value) for value in pin_match.groups())

    window_rows = re.findall(
        rf"^(U_(?:e|mu|tau)[123]):\s*"
        rf"\[\s*({number})\s*,\s*({number})\s*\]\s*$",
        block_text,
        flags=re.MULTILINE,
    )
    window_labels = tuple(row[0] for row in window_rows)
    if window_labels != WINDOW_LABELS:
        raise ValueError(
            "WINDOWS must contain the nine labeled entries in PMNS row-major order"
        )
    pdg_lo = np.array([float(row[1]) for row in window_rows]).reshape(3, 3)
    pdg_hi = np.array([float(row[2]) for row in window_rows]).reshape(3, 3)

    sign_match = re.search(
        rf"^SIGN-GATE:\s*(sin_delta_cp)\s*(<=|>=|<|>)\s*({number})\s*$",
        block_text,
        flags=re.MULTILINE,
    )
    if sign_match is None:
        raise ValueError("missing or malformed SIGN-GATE line in (P-SIG)")
    sign_variable, sign_operator, sign_bound_text = sign_match.groups()

    return SuppliedPacket(
        pin=pin_values,
        window_labels=window_labels,
        pdg_lo=pdg_lo,
        pdg_hi=pdg_hi,
        sign_variable=sign_variable,
        sign_operator=sign_operator,
        sign_bound=float(sign_bound_text),
        sign_gate_text=sign_match.group(0).split(":", 1)[1].strip(),
        block_text=block_text,
        note_text=note_text,
    )


def sign_gate_accepts(value: float, packet: SuppliedPacket) -> bool:
    comparator = GATE_OPERATORS[packet.sign_operator]
    return bool(comparator(value, packet.sign_bound))


def windows_are_well_formed(pdg_lo: np.ndarray, pdg_hi: np.ndarray) -> bool:
    return bool(
        pdg_lo.shape == (3, 3)
        and pdg_hi.shape == (3, 3)
        and np.all(np.isfinite(pdg_lo))
        and np.all(np.isfinite(pdg_hi))
        and np.all(pdg_lo <= pdg_hi)
    )


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def echo_and_check_packet(packet: SuppliedPacket) -> None:
    print()
    print("=" * 80)
    print("Parsed supplied-input packet (P-SIG)")
    print("=" * 80)
    print(
        "  PIN: "
        f"m_* = {packet.pin[0]:.6f} ; "
        f"delta_* = {packet.pin[1]:.6f} ; "
        f"q_+* = {packet.pin[2]:.6f}"
    )
    print("  WINDOWS:")
    for label, lo, hi in zip(
        packet.window_labels, packet.pdg_lo.flat, packet.pdg_hi.flat
    ):
        print(f"    {label}: [{lo:.3f}, {hi:.3f}]")
    print(f"  SIGN-GATE: {packet.sign_gate_text}")
    print()

    check(
        "(P-SIG) PIN contains exactly three finite supplied values",
        len(packet.pin) == 3 and all(math.isfinite(value) for value in packet.pin),
    )
    check(
        "(P-SIG) WINDOWS contains all nine labeled row-major entries",
        packet.window_labels == WINDOW_LABELS
        and packet.pdg_lo.shape == (3, 3)
        and packet.pdg_hi.shape == (3, 3),
    )
    check(
        "(P-SIG) WINDOWS has finite ordered [lo, hi] pairs",
        windows_are_well_formed(packet.pdg_lo, packet.pdg_hi),
    )
    check(
        "(P-SIG) SIGN-GATE is a supported parsed comparator",
        packet.sign_variable == "sin_delta_cp"
        and packet.sign_operator in GATE_OPERATORS
        and math.isfinite(packet.sign_bound),
        packet.sign_gate_text,
    )

    note_surface_needles = (
        "(P-SIG-a)",
        "(P-SIG-b)",
        "(P-SIG-c)",
        "supplied-input packet entry",
        "## Repair Note (2026-07-11)",
    )
    for needle in note_surface_needles:
        check(
            f"Note surface contains {needle!r}",
            needle in packet.note_text,
        )
    forbidden = "observationally unique at the live pin"
    check(
        "Note surface omits the superseded live-pin observational phrase",
        forbidden not in packet.note_text,
    )


# ---------------------------------------------------------------------------
# Retained atlas constants (exact)
# ---------------------------------------------------------------------------

GAMMA = 0.5
E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0

T_M = np.array(
    [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex
)
T_DELTA = np.array(
    [[0.0, -1.0, 1.0], [-1.0, 1.0, 0.0], [1.0, 0.0, -1.0]], dtype=complex
)
T_Q = np.array(
    [[0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0]], dtype=complex
)
H_BASE = np.array(
    [
        [0.0, E1, -E1 - 1j * GAMMA],
        [E1, 0.0, -E2],
        [-E1 + 1j * GAMMA, -E2, 0.0],
    ],
    dtype=complex,
)

def H_mat(m: float, delta: float, q_plus: float) -> np.ndarray:
    return H_BASE + m * T_M + delta * T_DELTA + q_plus * T_Q


def pmns_for_permutation(
    V: np.ndarray, perm: tuple[int, int, int]
) -> np.ndarray:
    """
    Row-permute the eigenvector matrix to get the PMNS matrix.
    V[:,k] = k-th eigenvector (ascending eigenvalue order).
    perm = (i0, i1, i2): electron row <- row i0 of V in axis basis,
    muon <- i1, tau <- i2.
    Under Z_3 trichotomy + Higgs Z_3 gauge-redundancy, U_e = I so PMNS = U_nu.
    """
    return V[list(perm), :]


def count_passes(
    U_abs: np.ndarray, pdg_lo: np.ndarray, pdg_hi: np.ndarray
) -> int:
    return int(np.sum((U_abs >= pdg_lo) & (U_abs <= pdg_hi)))


def jarlskog_sin_dcp(P: np.ndarray) -> float:
    J = (P[0, 0] * P[0, 1].conjugate() * P[1, 0].conjugate() * P[1, 1]).imag
    s13sq = abs(P[0, 2]) ** 2
    c13sq = max(1.0 - s13sq, 1e-18)
    s12sq = abs(P[0, 1]) ** 2 / c13sq
    s23sq = abs(P[1, 2]) ** 2 / c13sq
    s12 = math.sqrt(max(s12sq, 0.0))
    c12 = math.sqrt(max(1.0 - s12sq, 0.0))
    s13 = math.sqrt(max(s13sq, 0.0))
    c13 = math.sqrt(max(c13sq, 0.0))
    s23 = math.sqrt(max(s23sq, 0.0))
    c23 = math.sqrt(max(1.0 - s23sq, 0.0))
    denom = s12 * c12 * s23 * c23 * s13 * c13 * c13
    if denom < 1e-18:
        return 0.0
    return float(max(-1.0, min(1.0, J / denom)))


# ---------------------------------------------------------------------------
# Part 1: H at the pinned point, eigendecomposition
# ---------------------------------------------------------------------------


def part1_h_at_pin(pin: tuple[float, float, float]) -> np.ndarray:
    print()
    print("=" * 80)
    print("Part 1: H at pinned chamber point — eigendecomposition")
    print("=" * 80)

    Hpin = H_mat(*pin)
    check("H_pin is Hermitian", np.allclose(Hpin, Hpin.conj().T, atol=1e-14))

    w, V = np.linalg.eigh(Hpin)
    order = np.argsort(np.real(w))
    w = np.real(w[order])
    V = V[:, order]

    print(f"  eigenvalues (ascending): {w}")
    print(f"  det(H_pin) = {np.linalg.det(Hpin).real:.6f}")

    check(
        "det(H_pin) > 0 (C_base component, consistent with P3 Sylvester theorem)",
        float(np.linalg.det(Hpin).real) > 0.0,
        f"det = {np.linalg.det(Hpin).real:.6f}",
    )
    check(
        "signature(H_pin) = (2, 0, 1): two negative, one positive eigenvalue",
        sum(w < 0) == 2 and sum(w > 0) == 1,
        f"eigenvalues = {w}",
    )

    w_base, _ = np.linalg.eigh(H_BASE)
    check(
        "signature(H_base) = (2, 0, 1) — same as H_pin (Sylvester)",
        sum(np.real(w_base) < 0) == 2 and sum(np.real(w_base) > 0) == 1,
    )

    return V


# ---------------------------------------------------------------------------
# Part 2: Enumerate all 6 S_3 permutations — supplied magnitude filter
# ---------------------------------------------------------------------------


def scan_permutations(
    V: np.ndarray, pdg_lo: np.ndarray, pdg_hi: np.ndarray
) -> dict:
    results = {}
    for perm in itertools.permutations([0, 1, 2]):
        P = pmns_for_permutation(V, perm)
        U_abs = np.abs(P)
        results[perm] = {
            "P": P,
            "U_abs": U_abs,
            "n_pass": count_passes(U_abs, pdg_lo, pdg_hi),
            "sin_dcp": jarlskog_sin_dcp(P),
        }
    return results


def selected_permutations(
    results: dict, packet: SuppliedPacket
) -> list[tuple[int, int, int]]:
    return [
        perm
        for perm, result in results.items()
        if result["n_pass"] == 9
        and sign_gate_accepts(result["sin_dcp"], packet)
    ]


def part2_magnitude_filter(
    V: np.ndarray, pdg_lo: np.ndarray, pdg_hi: np.ndarray
) -> dict:
    print()
    print("=" * 80)
    print("Part 2: STEP 1 — magnitude filter: supplied (P-SIG-b) windows")
    print("=" * 80)
    print()
    print(f"  {'sigma':14s}  {'n_pass':8s}  {'sin(dCP)':10s}  note")
    print("  " + "-" * 64)

    results = scan_permutations(V, pdg_lo, pdg_hi)
    for perm, result in results.items():
        n = result["n_pass"]
        sin_dcp = result["sin_dcp"]
        note = ""
        if n == 9:
            note = "  <-- passes all 9 magnitudes"
        print(
            f"  sigma={perm}  {n}/9 pass    sin(dCP)={sin_dcp:+.4f}{note}"
        )

    passing_9 = [p for p, r in results.items() if r["n_pass"] == 9]
    check(
        "Exactly 2 of 6 S_3 permutations pass all 9 supplied magnitude windows",
        len(passing_9) == 2,
        f"passing: {passing_9}",
    )
    check(
        "The 2 magnitude-passing permutations are (2,0,1) and (2,1,0)",
        set(passing_9) == {(2, 0, 1), (2, 1, 0)},
        f"found: {passing_9}",
    )
    min_fail_others = min(
        9 - r["n_pass"] for p, r in results.items() if p not in [(2, 0, 1), (2, 1, 0)]
    )
    check(
        "All other 4 permutations fail >= 4 supplied magnitude windows",
        min_fail_others >= 4,
        f"minimum failures in excluded permutations: {min_fail_others}",
    )

    return results


# ---------------------------------------------------------------------------
# Part 3: STEP 2 — supplied CP-sign discriminator
# ---------------------------------------------------------------------------


def part3_cp_phase_discriminator(
    results: dict, packet: SuppliedPacket
) -> None:
    print()
    print("=" * 80)
    print("Part 3: STEP 2 — supplied (P-SIG-c) CP-sign discriminator")
    print("=" * 80)

    r_201 = results[(2, 0, 1)]
    r_210 = results[(2, 1, 0)]

    print()
    print("  The two magnitude-passing permutations differ only by mu<->tau swap.")
    print("  A row swap in PMNS preserves all |U| magnitudes but reverses Jarlskog J.")
    print()

    s201 = r_201["sin_dcp"]
    s210 = r_210["sin_dcp"]
    dcp_201 = math.degrees(math.asin(s201))
    dcp_210 = math.degrees(math.asin(s210))
    print(f"  sigma=(2,0,1): sin(delta_CP) = {s201:+.4f}  "
          f"(delta_CP = {dcp_201:+.2f} deg)")
    print(f"  sigma=(2,1,0): sin(delta_CP) = {s210:+.4f}  "
          f"(delta_CP = {dcp_210:+.2f} deg)")

    check(
        "sigma=(2,0,1) and sigma=(2,1,0) give equal-magnitude |U| rows (mu<->tau swap identity)",
        np.allclose(np.sort(r_201["U_abs"], axis=0), np.sort(r_210["U_abs"], axis=0), atol=1e-12),
    )
    check(
        "sigma=(2,0,1) gives sin(delta_CP) = +0.9874 (positive, delta_CP ~ +81 deg)",
        abs(s201 - 0.9874) < 0.001,
        f"sin(dCP) = {s201:+.4f}",
    )
    check(
        "sigma=(2,1,0) gives sin(delta_CP) = -0.9874 (negative, delta_CP ~ -81 deg)",
        abs(s210 + 0.9874) < 0.001,
        f"sin(dCP) = {s210:+.4f}",
    )

    print()
    print(f"  Applying parsed SIGN-GATE: {packet.sign_gate_text}")
    print("  Its external observational authority is comparator context, not ratified here.")
    print()

    check(
        "sigma=(2,0,1) fails the supplied SIGN-GATE",
        not sign_gate_accepts(s201, packet),
        f"sin(dCP) = {s201:+.4f}; gate: {packet.sign_gate_text}",
    )
    check(
        "sigma=(2,1,0) passes the supplied SIGN-GATE",
        sign_gate_accepts(s210, packet),
        f"sin(dCP) = {s210:+.4f}; gate: {packet.sign_gate_text}",
    )
    selected = selected_permutations(results, packet)
    check(
        "The supplied packet uniquely selects sigma=(2,1,0) from S_3",
        selected == [(2, 1, 0)],
        f"selected: {selected}",
    )


# ---------------------------------------------------------------------------
# Part 4: Unique physical permutation detail — all 9 entries
# ---------------------------------------------------------------------------


def part4_physical_sigma_detail(
    results: dict, pdg_lo: np.ndarray, pdg_hi: np.ndarray
) -> None:
    print()
    print("=" * 80)
    print("Part 4: Selected sigma = (2, 1, 0) — full 9/9 supplied-window detail")
    print("=" * 80)

    r = results[(2, 1, 0)]
    U = r["U_abs"]

    print()
    print("  |U_PMNS| at pinned point, sigma=(2,1,0):")
    flavor_labels = ["e   ", "mu  ", "tau "]
    for i in range(3):
        row_str = "  [" + ", ".join(f"{U[i,j]:.4f}" for j in range(3)) + "]"
        print(f"    {flavor_labels[i]}: {row_str[2:]}")

    print()
    for i in range(3):
        for j in range(3):
            inside = pdg_lo[i, j] <= U[i, j] <= pdg_hi[i, j]
            flavor = ["e", "mu", "tau"][i]
            mass = ["1", "2", "3"][j]
            check(
                f"|U_{flavor}{mass}| in [{pdg_lo[i,j]:.3f}, {pdg_hi[i,j]:.3f}]",
                inside,
                f"val = {U[i,j]:.4f}",
            )

    print()
    sin_dcp = r["sin_dcp"]
    check(
        "sin(delta_CP) = -0.9874 ± 0.001 at the physical sigma",
        abs(sin_dcp + 0.9874) < 0.001,
        f"sin(dCP) = {sin_dcp:+.4f}",
    )
    check(
        "delta_CP ~ -81 deg at the supplied pin",
        sin_dcp < -0.9,
        f"sin(dCP) = {sin_dcp:+.4f}",
    )


# ---------------------------------------------------------------------------
# Part 5: Non-passing permutations — exhibit failure entries
# ---------------------------------------------------------------------------


def part5_non_passing_failures(
    results: dict, pdg_lo: np.ndarray, pdg_hi: np.ndarray
) -> None:
    print()
    print("=" * 80)
    print("Part 5: Non-magnitude-passing permutations — failure entries")
    print("=" * 80)

    excluded = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0)]
    all_ge4 = True
    for perm in excluded:
        r = results[perm]
        U = r["U_abs"]
        n_fail = 9 - r["n_pass"]
        failures = []
        for i in range(3):
            for j in range(3):
                if not (pdg_lo[i, j] <= U[i, j] <= pdg_hi[i, j]):
                    fl = ["e", "mu", "tau"][i]
                    ms = ["1", "2", "3"][j]
                    failures.append(
                        f"|U_{fl}{ms}|={U[i,j]:.3f} "
                        f"not in [{pdg_lo[i,j]:.3f},{pdg_hi[i,j]:.3f}]"
                    )
        if n_fail < 4:
            all_ge4 = False
        detail = "; ".join(failures[:2]) + (f"... ({n_fail} total)" if n_fail > 2 else "")
        print(f"  sigma={perm}: {n_fail} NuFit failures — {detail}")

    check(
        "All 4 magnitude-excluded permutations have >= 4 NuFit failures",
        all_ge4,
    )


# ---------------------------------------------------------------------------
# Part 6: Corrupted-parse negative control on copies
# ---------------------------------------------------------------------------


def part6_corrupted_parse_negative_control(
    V: np.ndarray, packet: SuppliedPacket, real_results: dict
) -> None:
    print()
    print("=" * 80)
    print("Part 6: corrupted-parse negative control (copy only)")
    print("=" * 80)

    real_lo_before = packet.pdg_lo.copy()
    real_hi_before = packet.pdg_hi.copy()
    corrupt_lo = packet.pdg_lo.copy()
    corrupt_hi = packet.pdg_hi.copy()

    original_lo = float(corrupt_lo[0, 0])
    original_hi = float(corrupt_hi[0, 0])
    corrupt_lo[0, 0] = original_hi
    corrupt_hi[0, 0] = original_lo

    corrupt_well_formed = windows_are_well_formed(corrupt_lo, corrupt_hi)
    corrupt_results = scan_permutations(V, corrupt_lo, corrupt_hi)
    real_selected = selected_permutations(real_results, packet)
    corrupt_selected = selected_permutations(corrupt_results, packet)
    uniqueness_flipped = corrupt_selected != real_selected

    check(
        "Swapping one copied window's lo/hi fails validation or flips uniqueness",
        (not corrupt_well_formed) or uniqueness_flipped,
        "window U_e1 copied as "
        f"[{corrupt_lo[0,0]:.3f}, {corrupt_hi[0,0]:.3f}]; "
        f"well_formed={corrupt_well_formed}; selected={corrupt_selected}",
    )
    check(
        "Corrupted-parse negative control does not mutate the real packet arrays",
        np.array_equal(packet.pdg_lo, real_lo_before)
        and np.array_equal(packet.pdg_hi, real_hi_before),
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    try:
        packet = parse_supplied_packet(NOTE_PATH)
    except (OSError, ValueError) as exc:
        print("=" * 80)
        print("sigma_hier SUPPLIED-INPUT S3 TABLE UNIQUENESS")
        print("=" * 80)
        check("Parse fenced supplied-input packet (P-SIG)", False, str(exc))
        print()
        print(f"PASS = {PASS_COUNT}")
        print(f"FAIL = {FAIL_COUNT}")
        return 1

    print("=" * 80)
    print("sigma_hier SUPPLIED-INPUT S3 TABLE UNIQUENESS (two-step)")
    print()
    print("  Inputs: parsed PIN, WINDOWS, and SIGN-GATE from note packet (P-SIG).")
    print("  Step 1: 9/9 supplied-window filter reduces S_3 from 6 to 2 rows.")
    print("  Step 2: supplied sign gate selects sigma=(2,1,0) uniquely.")
    print("  Scope: finite table arithmetic on supplied inputs; no authority ratification.")
    print("=" * 80)

    echo_and_check_packet(packet)
    V = part1_h_at_pin(packet.pin)
    results = part2_magnitude_filter(V, packet.pdg_lo, packet.pdg_hi)
    part3_cp_phase_discriminator(results, packet)
    part4_physical_sigma_detail(results, packet.pdg_lo, packet.pdg_hi)
    part5_non_passing_failures(results, packet.pdg_lo, packet.pdg_hi)
    part6_corrupted_parse_negative_control(V, packet, results)

    print()
    print("=" * 80)
    print("Theorem statement (on supplied packet (P-SIG)):")
    print()
    print(
        "  Supplied PIN: (m_*, delta_*, q_+*) = "
        f"({packet.pin[0]:.6f}, {packet.pin[1]:.6f}, {packet.pin[2]:.6f})."
    )
    print("  Given (P-SIG-a)-(P-SIG-c), sigma_hier = (2, 1, 0) is the unique")
    print("  element of S_3 satisfying both:")
    print("    (1) all 9 |U_PMNS|_{ij} inside the supplied windows, AND")
    print(f"    (2) the supplied SIGN-GATE: {packet.sign_gate_text}.")
    print()
    print("  Proof structure:")
    print("    - The 9/9 magnitude check reduces 6 S_3 elements to 2: (2,0,1) and")
    print("      (2,1,0), which differ only by a mu<->tau row swap.")
    print("    - The mu<->tau swap preserves all |U| magnitudes but reverses Jarlskog:")
    print("        sigma=(2,0,1): sin(delta_CP) = +0.9874 (fails supplied gate)")
    print("        sigma=(2,1,0): sin(delta_CP) = -0.9874 (passes supplied gate)")
    print("    - Therefore the supplied packet selects only sigma=(2,1,0).")
    print()
    print("  This is a supplied-input selection statement. It neither derives")
    print("  sigma_hier from Cl(3)/Z^3 nor ratifies the pin, windows, sign gate,")
    print("  physical sheet, or wider chamber/basin uniqueness.")
    print()
    print("  Conditional on supplied pin (P-SIG-a), sin(delta_CP) = -0.9874 is")
    print("  the falsifiable computed prediction for the selected table row.")
    print("=" * 80)
    print()
    print(f"PASS = {PASS_COUNT}")
    print(f"FAIL = {FAIL_COUNT}")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
