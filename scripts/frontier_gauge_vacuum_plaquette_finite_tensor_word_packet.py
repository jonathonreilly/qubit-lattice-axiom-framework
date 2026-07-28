#!/usr/bin/env python3
"""Gauge-vacuum plaquette finite tensor-word packet — bounded source-note runner.

Verifies docs/GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md
on the truncated NMAX = 4 weight box at MODE_MAX = 80 Bessel modes and
stipulated parameter x = 2:

  (P1) nonnegativity of tensor_word matrix entries
  (P2) conjugation-swap symmetry of tensor_word
  (P3) nonnegativity of boundary amplitude under unit-vector readout

Plus consistency check (derived corollary, not separate load-bearing):
  S · boundary0 = boundary0 exactly (since (0,0) is fixed by S),
  and therefore S · amp = amp follows from (P2) — verified numerically
  to confirm the chain composes consistently, not as a separate property.

The construction is:

  diag_c    = diag( c_(p,q)(6) / (d_(p,q) c_(0,0)(6)) ) on NMAX=4 box
  N_f       = SU(3) fundamental fusion-multiplicity matrix on the box
  N_fbar    = SU(3) anti-fundamental fusion-multiplicity matrix on the box
  tensor_word = diag_c · (N_f + N_fbar) · diag_c · (N_f + N_fbar)^T · diag_c

where c_(p,q)(x=2) is computed via a Schur-Weyl Bessel determinant truncated
to MODE_MAX = 80 modes (matching the stipulated-integral companion
GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09).

This is a split note following prior audit feedback on the parent
GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.
The bounded scope is ONLY (P1)-(P3); the parent's matrix-element identity
between the constructed matrix and actual spatial-environment boundary
amplitudes is NOT claimed here.

Imports: numpy + scipy.special.iv (family convention; matches the
stipulated-integral companion runner
frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.py).

Output form: deliberately compact — one line per check, no rule bars, marker
text carried once — so that the complete execution certificate stays small.
Every one of the checks is printed individually with its measured value; no
check, value, or section is elided or summarized away. The numeric content and
the check set are identical to the prior verbose-format revision of this runner.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

import numpy as np
from scipy.special import iv

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md"
AUDIT_INPUT_PATHS = (
    "docs/GAUGE_VACUUM_PLAQUETTE_FINITE_TENSOR_WORD_PACKET_BOUNDED_NOTE_2026-05-10.md",
    "docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md",
    "docs/GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md",
)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {name}" + (f" | {detail}" if detail else ""))


def section(title: str) -> None:
    print(f"-- {title}")


# Stipulated finite-evaluation parameters (match the companion integral).
BETA = 6.0
ARG = BETA / 3.0
MODE_MAX = 80
NMAX = 4

NOTE_TEXT = NOTE_PATH.read_text() if NOTE_PATH.exists() else ""
NOTE_FLAT = re.sub(r"\s+", " ", NOTE_TEXT)


# ---------------------------------------------------------------------------
# Stipulated finite integral coefficient (Schur-Weyl Bessel determinant)
# Matches companion frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute
# ---------------------------------------------------------------------------
def dim_su3(p: int, q: int) -> int:
    """Standard SU(3) irrep dimension for (p, q) Dynkin label."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def highest_weight_triple(p: int, q: int) -> list[int]:
    return [p + q, q, 0]


def coefficient_matrix(mode: int, lam: list[int]) -> np.ndarray:
    return np.array(
        [[iv(mode + lam[j] + i - j, ARG) for j in range(3)] for i in range(3)],
        dtype=float,
    )


def wilson_character_coefficient(p: int, q: int) -> float:
    """c_(p,q)(x=2) via a Schur-Weyl Bessel determinant."""
    lam = highest_weight_triple(p, q)
    total = 0.0
    for mode in range(-MODE_MAX, MODE_MAX + 1):
        total += float(np.linalg.det(coefficient_matrix(mode, lam)))
    return total


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


# ---------------------------------------------------------------------------
# SU(3) fundamental + anti-fundamental fusion multiplicities on the box
# ---------------------------------------------------------------------------
def build_mult_matrices(nmax: int):
    """Build N_f and N_fbar matrices on the NMAX weight box.

    Standard SU(3) tensoring with fundamental (1,0) and anti-fundamental (0,1)
    via their respective three-neighbor Pieri recurrences, restricted to the
    (p, q) ∈ [0..nmax]² box.
    """
    weights = weights_box(nmax)
    index = {w: i for i, w in enumerate(weights)}
    nf = np.zeros((len(weights), len(weights)), dtype=int)
    nfb = np.zeros((len(weights), len(weights)), dtype=int)
    for p, q in weights:
        i = index[(p, q)]
        for a, b in [(p + 1, q), (p - 1, q + 1), (p, q - 1)]:
            if a >= 0 and b >= 0 and (a, b) in index:
                nf[index[(a, b)], i] += 1
        for a, b in [(p, q + 1), (p + 1, q - 1), (p - 1, q)]:
            if a >= 0 and b >= 0 and (a, b) in index:
                nfb[index[(a, b)], i] += 1
    return nf, nfb, weights, index


def conjugation_swap_matrix(weights, index) -> np.ndarray:
    """Permutation matrix swap[(p,q) → (q,p)] on the box."""
    swap = np.zeros((len(weights), len(weights)), dtype=int)
    for w in weights:
        swap[index[(w[1], w[0])], index[w]] = 1
    return swap


# ---------------------------------------------------------------------------
# Part 1: Note structure
# ---------------------------------------------------------------------------
def part1_note_structure():
    section("Part 1: note structure (20 markers)")
    required = [
        "Finite Tensor-Word Packet",
        "Claim type:** bounded_theorem",
        "finite truncated tensor-word packet only",
        "## Claim",
        "## Bounded inputs",
        "## Proof-Walk",
        "## Dependencies",
        "## Boundaries",
        "## Verification",
        "(P1) **Nonnegativity",
        "(P2) **Conjugation-swap",
        "(P3) **Nonnegative boundary amplitude",
        "Derived corollary of (P2)",
        "(I-1) **Stipulated finite integral coefficients.**",
        "(I-2) **`SU(3)` fundamental and anti-fundamental fusion",
        "GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md",
        "GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09",
        "claim the parent note's structural matrix-element identity",
        "close the full untruncated tensor-transfer construction",
        "split note for one finite tensor-word packet",
    ]
    for marker in required:
        ok = marker in NOTE_TEXT or marker in NOTE_FLAT
        check(f"note has {marker!r}", ok)


# ---------------------------------------------------------------------------
# Part 2: Forbidden vocabulary
# ---------------------------------------------------------------------------
def part2_forbidden_vocabulary():
    section("Part 2: rejected vocabulary absent (note + docstring)")
    forbidden = [
        "algebraic universality",
        "lattice-realization-invariant",
        "two-class framing",
        "(CKN)",
        "(LCL)",
        "(SU5-CKN)",
        "imports problem",
        "Every prediction listed",
        "two-axiom claim",
        "retires admission",
        "sub-class (i)",
        "sub-class (ii)",
        "Wilson asymptotic universality",
        "Bounded statement.",  # rejected in PR #887 review
        "post-2026-05-10 narrowing",  # rejected in PR #887 review
        "explicitly out of the bounded scope",  # rejected in PR #887 review
    ]
    runner_text = Path(__file__).read_text()
    docstring_match = re.match(r'^(?:#![^\n]*\n)?[^"]*"""(.*?)"""',
                               runner_text, re.DOTALL)
    runner_docstring = docstring_match.group(1) if docstring_match else ""
    for token in forbidden:
        check(f"note lacks {token!r}", token not in NOTE_TEXT)
        check(f"doc lacks {token!r}", token not in runner_docstring)


# ---------------------------------------------------------------------------
# Part 3: Cited upstreams
# ---------------------------------------------------------------------------
def part3_cited_upstreams():
    section("Part 3: cited upstreams")
    must_exist = [
        "docs/GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TENSOR_TRANSFER_THEOREM_NOTE.md",
        "docs/GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md",
    ]
    for rel in must_exist:
        check(f"upstream: {rel}", (ROOT / rel).exists())


# ---------------------------------------------------------------------------
# Part 4: Construct tensor_word and verify (P1), (P2), (P3.a), (P3.b)
# ---------------------------------------------------------------------------
def part4_construct_and_verify_packet():
    section("Part 4: construct tensor_word; verify (P1),(P2),(P3)")
    nf, nfb, weights, index = build_mult_matrices(NMAX)
    swap = conjugation_swap_matrix(weights, index)
    print(f"NMAX={NMAX} box [0..{NMAX}]^2 = {len(weights)} states; "
          f"MODE_MAX={MODE_MAX}; beta={BETA}; beta/3={ARG}")

    # Compute Wilson character coefficients on the box
    coeffs = np.array(
        [wilson_character_coefficient(p, q) for p, q in weights], dtype=float
    )
    dims = np.array([dim_su3(p, q) for p, q in weights], dtype=float)
    c00 = coeffs[index[(0, 0)]]
    normalized = coeffs / (dims * c00)

    # (I-2) sanity checks: N_f and N_fbar entries in {0, 1}
    nf_entries_ok = bool(np.min(nf) >= 0 and np.max(nf) <= 1)
    nfb_entries_ok = bool(np.min(nfb) >= 0 and np.max(nfb) <= 1)
    check("(I-2) N_f entries in {0,1}", nf_entries_ok)
    check("(I-2) N_fbar entries in {0,1}", nfb_entries_ok)

    # (I-2) sanity checks: S · N_f = N_fbar · S (conjugation swap)
    nf_swap_diff = int(np.max(np.abs(swap @ nf - nfb @ swap)))
    nfb_swap_diff = int(np.max(np.abs(swap @ nfb - nf @ swap)))
    check("(I-2) S·N_f = N_fbar·S", nf_swap_diff == 0, f"max|.| = {nf_swap_diff}")
    check("(I-2) S·N_fbar = N_f·S", nfb_swap_diff == 0, f"max|.| = {nfb_swap_diff}")

    # Local Wilson coefficient sanity: c_(0,0)(6) > 0, normalized[(0,0)] = 1
    c00_pos = bool(c00 > 0)
    norm_00_one = bool(abs(normalized[index[(0, 0)]] - 1.0) < 1e-12)
    check("(I-1) c_(0,0)(x=2) > 0", c00_pos, f"c_(0,0)(2) = {c00:.6f}")
    check("(I-1) normalized[(0,0)] = 1", norm_00_one,
          f"val = {normalized[index[(0, 0)]]:.15f}")

    # Local Wilson coefficient conjugation symmetry: normalized[(p,q)] = normalized[(q,p)]
    norm_swap_diff = float(
        np.max(np.abs(normalized - normalized[[index[(q, p)] for p, q in weights]]))
    )
    check("(I-1) c_(p,q)(2) = c_(q,p)(2) up to normalization",
          norm_swap_diff < 1e-12, f"max|norm - S·norm| = {norm_swap_diff:.2e}")

    # Construct tensor_word per eq. (3) of the bounded note
    diag_c = np.diag(normalized)
    tensor_word = diag_c @ (nf + nfb) @ diag_c @ (nf + nfb).T @ diag_c
    print(f"tensor_word = {tensor_word.shape[0]}x{tensor_word.shape[1]} real"
          " = diag_c·(N_f+N_fbar)·diag_c·(N_f+N_fbar)^T·diag_c")

    # (P1) nonnegativity
    word_min = float(np.min(tensor_word))
    word_max = float(np.max(tensor_word))
    check("(P1) min(tensor_word) >= 0", word_min >= 0.0, f"min = {word_min:.6e}, max = {word_max:.6e}")

    # (P2) conjugation-swap symmetry
    word_swap_diff = float(np.max(np.abs(swap @ tensor_word - tensor_word @ swap)))
    check("(P2) ||S·tw - tw·S||_inf < 1e-12", word_swap_diff < 1e-12, f"max diff = {word_swap_diff:.2e}")

    # (P3) nonneg boundary amplitude
    boundary0 = np.zeros(len(weights), dtype=float)
    boundary0[index[(0, 0)]] = 1.0
    amp = tensor_word @ boundary0
    amp_min = float(np.min(amp))
    amp_max = float(np.max(amp))
    check("(P3) min(amp) >= 0", amp_min >= 0.0, f"min = {amp_min:.6e}, max = {amp_max:.6e}")

    # (P3-corollary, derived from P2): the (0,0) state is fixed by S,
    # so S · boundary0 = boundary0 trivially. Combined with (P2):
    #   S · amp = S · tensor_word · boundary0
    #          = tensor_word · S · boundary0   [by (P2)]
    #          = tensor_word · boundary0
    #          = amp.
    # Verify the trivial S-fixed-point step explicitly, plus the
    # consistency S · amp = amp at numerical precision.
    s_b0_diff = int(np.max(np.abs(swap @ boundary0 - boundary0)))
    check("(P3-cor, EXACT) S·boundary0 = boundary0", s_b0_diff == 0, f"max|S·b0 - b0| = {s_b0_diff}")
    amp_swap_diff = float(np.max(np.abs(swap @ amp - amp)))
    check("(P3-cor, consistency) ||S·amp - amp||_inf < 1e-12",
          amp_swap_diff < 1e-12, f"max diff = {amp_swap_diff:.2e}")

    # Print sample entries for diagnostic visibility
    cols = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0)]
    print("tensor_word[w,(0,0)] " + "  ".join(
        f"{w}={tensor_word[index[w], index[(0, 0)]]:.6e}"
        for w in cols if w in index))
    rows = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 2)]
    print("amp[w] = (tensor_word·e_(0,0))[w] " + "  ".join(
        f"{w}={amp[index[w]]:.6e}" for w in rows if w in index))


# ---------------------------------------------------------------------------
# Part 5: Import boundary
# ---------------------------------------------------------------------------
def part5_import_boundary():
    section("Part 5: import boundary")
    runner_text = Path(__file__).read_text()
    # numpy + scipy.special.iv is the family convention used by the companion
    # frontier_gauge_vacuum_plaquette_rho_pq_6_wilson_environment_compute.
    bad = []
    for ln in runner_text.splitlines():
        ln = ln.strip()
        if ln.startswith("from "):
            mod = ln.split()[1].split(".")[0]
        elif ln.startswith("import "):
            mod = ln.split()[1].split(".")[0].rstrip(",")
        else:
            continue
        # Allow numpy, scipy, plus stdlib
        if mod not in {"numpy", "scipy", "pathlib", "re", "sys", "__future__"}:
            bad.append(ln)
    check("imports limited to numpy + scipy + stdlib",
          not bad, f"non-allowed = {bad}" if bad else "ok")


# ---------------------------------------------------------------------------
# Part 6: Boundary check
# ---------------------------------------------------------------------------
def part6_boundary_check():
    section("Part 6: what is NOT claimed")
    not_claimed = [
        "claim the parent note's structural matrix-element identity",
        "close the full untruncated tensor-transfer construction",
        "close `analytic P(6)`",
        "change any parent or companion source row",
    ]
    for marker in not_claimed:
        check(f"not claimed: {marker!r}", marker in NOTE_TEXT)

    check("note has 'Claim type:** bounded_theorem'",
          "Claim type:** bounded_theorem" in NOTE_TEXT)
    check("note has 'split note for one finite tensor-word packet'",
          "split note for one finite tensor-word packet" in NOTE_TEXT)
    check("note has 'No framework axiom'",
          "No framework axiom" in NOTE_TEXT)


def main() -> int:
    print("frontier_gauge_vacuum_plaquette_finite_tensor_word_packet.py")
    print("Bounded packet: tensor_word at NMAX=4, MODE_MAX=80, x=2; verifies"
          " (P1)-(P3) at double precision plus the derived (P3-corollary) check.")

    part1_note_structure()
    part2_forbidden_vocabulary()
    part3_cited_upstreams()
    part4_construct_and_verify_packet()
    part5_import_boundary()
    part6_boundary_check()

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL == 0:
        print("RESULT: one explicit nonnegative-entry matrix tensor_word constructed from")
        print("stipulated finite integral coefficients (NMAX=4, MODE_MAX=80,")
        print("x=2) and SU(3) fusion multiplicities verifies three structural")
        print("properties at double precision: (P1) nonnegativity of matrix entries,")
        print("(P2) conjugation-swap symmetry, (P3) nonnegative boundary amplitude")
        print("under (0,0)-component unit-vector readout. The boundary-amplitude")
        print("conjugation symmetry follows immediately from (P2) since (0,0) is")
        print("fixed by the conjugation swap (consistency check, not a separate")
        print("load-bearing property). The parent's broader matrix-element identity")
        print("z_(p,q)^env = <chi, T^L eta> is NOT claimed here; this is a")
        print("split-note bounded packet only.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
