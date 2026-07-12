#!/usr/bin/env python3
"""
sigma_hier supplied-input selection replay
===========================================

STATUS: supplied-input S_3 selection table — conditional on three admitted external
inputs (the pinned chamber point, the NuFit 5.3 NO 3-sigma magnitude windows without
SK-atm, and a supplied sin(delta_CP) < 0 sign comparator motivated by T2K),
sigma_hier = (2, 1, 0) is the unique
hierarchy pairing with:
  (a) all 9 |U_PMNS| entries inside the NuFit 5.3 NO 3-sigma ranges, AND
  (b) the supplied sin(delta_CP) < 0 comparator.

Framework convention: "axiom" means only Cl(3) on Z^3.

Context
-------
The P3 closure pins the chamber point

    (m_*, delta_*, q_+*) = (0.657061, 0.933806, 0.715042)

using three PMNS observational inputs (s12^2, s13^2, s23^2), the imposed
branch-choice rule (A-BCC), and the already chosen sigma_hier=(2,1,0).
The hierarchy pairing was listed as an independent conditional — an S_3
permutation choice assigning eigenvectors of H to the charged-lepton rows
(e, mu, tau). This runner replays that supplied construction; it does not use
the pairing-conditioned pin as independent evidence for the same pairing.

This runner checks a two-step supplied-input replay:

STEP 1 (9/9 NuFit 5.3 magnitude filter, without SK-atm):
    Among all 6 elements of S_3, exactly TWO — sigma=(2,0,1) and
    sigma=(2,1,0) — place all 9 |U_PMNS|_{ij} entries inside the NuFit
    5.3 NO 3-sigma ranges. The other 4 permutations each fail >= 4 entries.

STEP 2 (supplied CP-sign discriminator):
    The two 9/9-passing permutations are related by a mu<->tau row swap,
    which preserves all |U| magnitudes but reverses the sign of the
    Jarlskog invariant J, hence reverses sin(delta_CP):
      sigma=(2,1,0): sin(delta_CP) = -0.9874  (delta_CP ~ -81 deg)
      sigma=(2,0,1): sin(delta_CP) = +0.9874  (delta_CP ~ +81 deg)
    The negative-sign comparator is supplied rather than derived, with the
    T2K 2021 negative-phase preference as motivation. It is not presented as
    a joint T2K/NOvA preference: NOvA 2021 instead disfavored the neighborhood
    of delta_CP=3*pi/2 in normal ordering at about 2 sigma.

Conclusion:
    The combination of the 9/9 NuFit 5.3 3-sigma magnitude check without
    SK-atm AND the supplied sign comparator (sin(delta_CP) < 0) uniquely
    selects sigma = (2, 1, 0) from the 6-element S_3 at the pinned point.

    This is a supplied-input selection statement, not an internal
    derivation: sigma_hier is not derivable from Cl(3)/Z^3 alone; it is
    uniquely selected, among the 6 elements of S_3 at the pinned point, by
    the joint requirement that all 9 PMNS magnitudes pass the supplied
    NuFit 5.3 3-sigma windows AND that sin(delta_CP) is negative under the
    supplied negative-sign comparator.

    The CP phase value sin(delta_CP) = -0.9874 is then a conditional geometric
    consequence of the selected pairing under the supplied comparators, not a
    separately imposed input. The supplied pin was itself obtained under
    sigma_hier=(2,1,0), so this replay is not independent selector evidence.
"""

from __future__ import annotations

import itertools
import math
import os

import numpy as np

np.set_printoptions(precision=6, suppress=True, linewidth=120)

PASS_COUNT = 0
FAIL_COUNT = 0


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

# Pinned chamber point (P3 observational closure, unique under A-BCC + sigma)
M_STAR = 0.657061
DELTA_STAR = 0.933806
Q_PLUS_STAR = 0.715042


def H_mat(m: float, delta: float, q_plus: float) -> np.ndarray:
    return H_BASE + m * T_M + delta * T_DELTA + q_plus * T_Q


# NuFit 5.3 NO 3-sigma ranges on |U_PMNS|_{ij}, without SK-atm
PDG_LO = np.array(
    [[0.801, 0.518, 0.142], [0.236, 0.458, 0.630], [0.264, 0.471, 0.610]]
)
PDG_HI = np.array(
    [[0.842, 0.580, 0.155], [0.507, 0.691, 0.779], [0.527, 0.700, 0.762]]
)


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


def count_passes(U_abs: np.ndarray) -> int:
    return int(np.sum((U_abs >= PDG_LO) & (U_abs <= PDG_HI)))


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


def part1_h_at_pin() -> np.ndarray:
    print()
    print("=" * 80)
    print("Part 1: H at pinned chamber point — eigendecomposition")
    print("=" * 80)

    Hpin = H_mat(M_STAR, DELTA_STAR, Q_PLUS_STAR)
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
# Part 2: Enumerate all 6 S_3 permutations — magnitude filter
# ---------------------------------------------------------------------------


def part2_magnitude_filter(V: np.ndarray) -> dict:
    print()
    print("=" * 80)
    print("Part 2: STEP 1 — magnitude filter: which sigmas pass 9/9 NuFit ranges")
    print("=" * 80)
    print()
    print(f"  {'sigma':14s}  {'n_pass':8s}  {'sin(dCP)':10s}  note")
    print("  " + "-" * 64)

    all_perms = list(itertools.permutations([0, 1, 2]))
    results = {}
    for perm in all_perms:
        P = pmns_for_permutation(V, perm)
        U_abs = np.abs(P)
        n = count_passes(U_abs)
        sin_dcp = jarlskog_sin_dcp(P)
        results[perm] = {"P": P, "U_abs": U_abs, "n_pass": n, "sin_dcp": sin_dcp}
        note = ""
        if n == 9:
            note = "  <-- passes all 9 magnitudes"
        print(
            f"  sigma={perm}  {n}/9 pass    sin(dCP)={sin_dcp:+.4f}{note}"
        )

    passing_9 = [p for p, r in results.items() if r["n_pass"] == 9]
    check(
        "Exactly 2 of 6 S_3 permutations pass all 9 NuFit 3-sigma magnitudes",
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
        "All other 4 permutations fail >= 4 NuFit entries",
        min_fail_others >= 4,
        f"minimum failures in excluded permutations: {min_fail_others}",
    )

    return results


# ---------------------------------------------------------------------------
# Part 3: STEP 2 — CP-phase discriminator
# ---------------------------------------------------------------------------


def part3_cp_phase_discriminator(results: dict) -> None:
    print()
    print("=" * 80)
    print("Part 3: STEP 2 — CP-phase discriminator between (2,0,1) and (2,1,0)")
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
    print("  The sin(delta_CP) < 0 comparator is a supplied input motivated by T2K 2021.")
    print("  It is not a joint T2K/NOvA preference or confidence-level combination.")
    print()
    check(
        "sigma=(2,0,1) fails the supplied sin(delta_CP)<0 comparator",
        s201 > 0.0,
        f"sin(dCP) = {s201:+.4f} > 0",
    )
    check(
        "sigma=(2,1,0) passes the supplied sin(delta_CP)<0 comparator",
        s210 < 0.0,
        f"sin(dCP) = {s210:+.4f} < 0",
    )


# ---------------------------------------------------------------------------
# Part 4: Selected permutation detail — all 9 entries
# ---------------------------------------------------------------------------


def part4_selected_sigma_detail(results: dict) -> None:
    print()
    print("=" * 80)
    print("Part 4: Selected sigma = (2, 1, 0) — full 9/9 NuFit detail")
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
            inside = PDG_LO[i, j] <= U[i, j] <= PDG_HI[i, j]
            flavor = ["e", "mu", "tau"][i]
            mass = ["1", "2", "3"][j]
            check(
                f"|U_{flavor}{mass}| in [{PDG_LO[i,j]:.3f}, {PDG_HI[i,j]:.3f}]",
                inside,
                f"val = {U[i,j]:.4f}",
            )

    print()
    sin_dcp = r["sin_dcp"]
    check(
        "sin(delta_CP) = -0.9874 ± 0.001 at the selected sigma",
        abs(sin_dcp + 0.9874) < 0.001,
        f"sin(dCP) = {sin_dcp:+.4f}",
    )
    check(
        "delta_CP ~ -81 deg (passes the supplied negative-sign comparator)",
        sin_dcp < -0.9,
        f"sin(dCP) = {sin_dcp:+.4f}",
    )


# ---------------------------------------------------------------------------
# Part 5: Non-passing permutations — exhibit failure entries
# ---------------------------------------------------------------------------


def part5_non_passing_failures(results: dict) -> None:
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
                if not (PDG_LO[i, j] <= U[i, j] <= PDG_HI[i, j]):
                    fl = ["e", "mu", "tau"][i]
                    ms = ["1", "2", "3"][j]
                    failures.append(
                        f"|U_{fl}{ms}|={U[i,j]:.3f} "
                        f"not in [{PDG_LO[i,j]:.3f},{PDG_HI[i,j]:.3f}]"
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
# Supplied-input scope gate (downstream hygiene, 2026-07-12)
# ---------------------------------------------------------------------------

_FORBIDDEN_CLOSURE_PHRASES = [
    "no observational ambiguity",
    "promoted from",
    "observationally unique at the live pin",
    "resolved under observational promotion",
]


def _has_overclaim(flat: str) -> bool:
    """True if any withdrawn observational-closure phrase is present in the
    whitespace-flattened note text."""
    return any(p in flat for p in _FORBIDDEN_CLOSURE_PHRASES)


_SUPPLIED_INPUT_HEADER = "## Supplied inputs (admitted, external)"


def _has_supplied_input_header(note: str) -> bool:
    """Detect the exact supplied-input Markdown section header."""
    return _SUPPLIED_INPUT_HEADER in note.splitlines()


def supplied_input_scope_gate() -> None:
    """Discriminating downstream-hygiene gate for the supplied-input reframe.

    Re-derives the S_3 selection from H at the pin (gates 1-3, which FAIL if
    the physics were wrong) AND pins the paired note to the supplied-input
    framing with no observational-closure language (gates 4-7). Gates 8-9
    are flip self-tests: they inject a wrong object and assert the string
    detectors fire, so a green here cannot be tautological.
    """
    # --- Re-derive the selection independently from H at the pin ---
    Hpin = H_mat(M_STAR, DELTA_STAR, Q_PLUS_STAR)
    w, V = np.linalg.eigh(Hpin)
    V = V[:, np.argsort(np.real(w))]
    sins = {}
    mag_pass = set()
    for perm in itertools.permutations([0, 1, 2]):
        P = pmns_for_permutation(V, perm)
        if count_passes(np.abs(P)) == 9:
            mag_pass.add(perm)
        sins[perm] = jarlskog_sin_dcp(P)
    s210 = sins[(2, 1, 0)]
    s201 = sins[(2, 0, 1)]
    joint = {p for p in mag_pass if sins[p] < 0}

    check(
        "gate 1: magnitude filter selects exactly {(2,0,1),(2,1,0)}",
        mag_pass == {(2, 0, 1), (2, 1, 0)},
        f"mag_pass = {sorted(mag_pass)}",
    )
    check(
        "gate 2: 9/9 AND sin(dCP)<0 selects exactly {(2,1,0)}",
        joint == {(2, 1, 0)},
        f"joint = {sorted(joint)}",
    )
    check(
        "gate 3: CP sign split — s(2,1,0)<0<s(2,0,1), exact opposites",
        abs(s210 + s201) < 1e-9 and s210 < 0.0 < s201,
        f"s210={s210:+.4f} s201={s201:+.4f}",
    )

    # --- Pin the paired note to the supplied-input framing ---
    note_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "docs",
        "SIGMA_HIER_UNIQUENESS_THEOREM_NOTE_2026-04-19.md",
    )
    with open(note_path, encoding="utf-8") as fh:
        note = fh.read()
    flat = " ".join(note.split())
    dep_edge = (
        "[neutrino_dirac_pmns_retained_lane_packet_2026-04-16]"
        "(NEUTRINO_DIRAC_PMNS_RETAINED_LANE_PACKET_2026-04-16.md)"
    )

    check(
        "gate 4: note carries no withdrawn observational-closure phrase",
        not _has_overclaim(flat),
    )
    check(
        "gate 5: note declares the supplied-input subsection",
        _has_supplied_input_header(note),
    )
    check(
        "gate 6: note carries the dated 2026-07-12 scope-narrowing record",
        "2026-07-12" in note and "narrow" in flat,
    )
    check(
        "gate 7: sole markdown dep edge (neutrino_dirac packet) present once",
        note.count(dep_edge) == 1,
        f"count = {note.count(dep_edge)}",
    )

    # --- Flip self-tests (positive controls): the detectors must fire ---
    injected = " ".join(
        (note + " Here sigma_hier is promoted from a free conditional.").split()
    )
    check(
        "gate 8: overclaim detector fires on an injected forbidden phrase",
        _has_overclaim(injected),
    )
    check(
        "gate 9: supplied-input detector distinguishes presence from absence",
        _has_supplied_input_header(note)
        and not _has_supplied_input_header(
            note.replace(_SUPPLIED_INPUT_HEADER, "## REDACTED", 1)
        ),
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    print("=" * 80)
    print("sigma_hier SUPPLIED-INPUT SELECTION REPLAY (two-step)")
    print()
    print("  Step 1 (9/9 magnitude filter): reduces S_3 from 6 to 2 permutations.")
    print("  Step 2 (CP-phase discriminator): selects sigma=(2,1,0) uniquely.")
    print("  Conclusion: sigma_hier = (2,1,0) is uniquely selected, conditional on")
    print("  the supplied inputs, by [9/9 NuFit 3-sigma magnitudes] AND [sin(delta_CP) < 0].")
    print("=" * 80)

    V = part1_h_at_pin()
    results = part2_magnitude_filter(V)
    part3_cp_phase_discriminator(results)
    part4_selected_sigma_detail(results)
    part5_non_passing_failures(results)
    supplied_input_scope_gate()

    print()
    print("=" * 80)
    print("Selection statement (supplied-input, conditional on PMNS observation):")
    print()
    print("  At the pinned chamber point (m_*, delta_*, q_+*) = (0.657061, 0.933806,")
    print("  0.715042), the hierarchy pairing sigma_hier = (2, 1, 0) is the unique")
    print("  element of S_3 satisfying both:")
    print("    (1) all 9 |U_PMNS|_{ij} inside NuFit 5.3 NO 3-sigma ranges, AND")
    print("    (2) the supplied sin(delta_CP) < 0 comparator.")
    print()
    print("  Proof structure:")
    print("    - The 9/9 magnitude check reduces 6 S_3 elements to 2: (2,0,1) and")
    print("      (2,1,0), which differ only by a mu<->tau row swap.")
    print("    - The mu<->tau swap preserves all |U| magnitudes but reverses Jarlskog:")
    print("        sigma=(2,0,1): sin(delta_CP) = +0.9874 (fails supplied sign cut)")
    print("        sigma=(2,1,0): sin(delta_CP) = -0.9874 (passes supplied sign cut)")
    print("    - Therefore sigma=(2,1,0) is the sole pairing passing the supplied filter.")
    print()
    print("  This is a supplied-input selection at the live pin: sigma_hier is")
    print("  not derived from Cl(3)/Z^3 alone, and it is not observationally")
    print("  closed; it is uniquely selected there, conditional on the three")
    print("  admitted external inputs, by the combined 4-observable PMNS")
    print("  constraint.")
    print("  This is a pinned-point selection only, not a chamber-wide or")
    print("  all-basin uniqueness claim; other admitted basins must be")
    print("  checked separately.")
    print("  The supplied pin was itself obtained under sigma=(2,1,0), so this")
    print("  replay is a consistency table, not independent selector evidence.")
    print()
    print("  The CP-phase value sin(delta_CP) = -0.9874 is then a conditional")
    print("  geometric consequence: a confirmed >3-sigma positive sin(delta_CP)")
    print("  measurement at DUNE/Hyper-K would rule out this pairing.")
    print("=" * 80)
    print()
    print(f"PASS = {PASS_COUNT}")
    print(f"FAIL = {FAIL_COUNT}")

    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
