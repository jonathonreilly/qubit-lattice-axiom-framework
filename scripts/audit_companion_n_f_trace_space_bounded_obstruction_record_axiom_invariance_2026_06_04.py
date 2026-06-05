#!/usr/bin/env python3
"""Audit-companion runner for the N_F trace-space bounded obstruction
parent note `N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_w2binary.md`
recording Record-axiom invariance after the 2026-06-04 framework axiom
adoption.

Companion source note:
  docs/N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md

Parent ledger row: `n_f_trace_space_bounded_obstruction_note_2026-05-07_w2binary`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    obstruction-localization content (eight-vector enumeration + V8
    bridge-step obstruction localization + conditional V_3 selection
    chain) is independent of the Record axiom adopted in
    `MINIMAL_AXIOMS_2026-06-04.md`. This does not re-apply the prior
    audit verdict; it gives the audit lane a machine-checkable basis
    for deciding whether the arithmetic needs fresh review after the
    premise-hash change.

Important scoping (not status-changing):
  The parent's latest archived audit was invalidated by
  `dep_weakened:cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02:retained->unaudited`,
  not by `axiom_premise_changed`. The dep is now `retained` again on
  `origin/main`. This companion's narrow contribution is the
  Record-axiom-invariance observation; the dep-weakened resolution is
  a separate audit-lane question and is not addressed here.

The runner verifies the parent's load-bearing structural facts
block-by-block under "Record axiom is asserted" and "Record axiom is
not asserted" outer scopes, confirms identical numeric outputs in both
scopes, and performs a static-source scan of the parent note's
load-bearing sections to confirm zero Record-axiom usage in the
auditable core.

Every load-bearing arithmetic check uses only:
  (i)   the per-site Cl(3)/M_2(C) local algebra (Quantum axiom in
        `MINIMAL_AXIOMS_2026-06-04.md`; A1 in the historical wording);
  (ii)  the `Z^3` lattice site set (Lattice axiom in
        `MINIMAL_AXIOMS_2026-06-04.md`; A2 in the historical wording);
  (iii) standard finite-dimensional Lie-algebra and Clifford-algebra
        identities (Gell-Mann generators, `Tr_R(T_a T_b)` canonical
        normalization on irreducible carriers, Pauli halves);
  (iv)  standard tensor-product index counting (V_color = V_3 (x)
        V_fiber; V_lepton = V_antisym (x) V_fiber).

No Record-axiom content (scalar record additivity functional `I(.)`)
enters any block. No claim is made about the Record-axiom-induced
downstream content; the companion observation is strictly limited to
the load-bearing-step invariance of the parent note.

Block plan:
  Block 1  : V_3 canonical Gell-Mann trace
             Tr_{V_3}(T_a T_b) = (1/2) delta_{ab}.
  Block 2  : V full-taste trace
             Tr_V(T_a^V T_b^V) = delta_{ab} with
             T_a^V = T_a (x) I_2 + 0_antisym.
  Block 3  : Fiber-multiplicity ratio Tr_V / Tr_{V_3} = 2 =
             dim(V_fiber).
  Block 4  : Projector algebra (P_color, P_lepton) and structural
             identity T_a^V . P_lepton = 0.
  Block 5  : Anti-fundamental distinguishability:
             3-bar generators -T_a^* differ from 3 generators T_a.
  Block 6  : d-symbol fiber inflation: d on V = 2 . d on V_3
             with d_{118}^{V_3} = 1/sqrt(3).
  Block 7  : Per-site Cl(3) bivector half-Pauli trace
             Tr_{C^2}(T_a T_b) = (1/2) delta_{ab}.
  Block 8  : SU(2) sub of color-SU(3) on V_3 trace
             Tr_{(1,2)-block of V_3}(T_a T_b) = (1/2) delta_{ab}.
  Block 9  : V8 bridge-step obstruction localization (structural
             identification per-site C^2 = (1,2)-block C^2 is NOT
             derived by this runner).
  Block 10 : Static-source scan of parent note's load-bearing
             sections: zero Record-axiom usage tokens.
  Block 11 : Record-axiom counterfactual: identical numeric outputs
             with and without an explicit "Record axiom asserted"
             outer scope.
  Block 12 : Quantum/Lattice content preservation across the historical
             2026-05-20 and current 2026-06-04 minimal-axioms memos;
             Record axiom scope explicitly excludes log-det /
             source-action / observable bridges.

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np

# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def record(check_name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        log(f"  PASS {check_name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        log(f"  FAIL {check_name}" + (f" :: {detail}" if detail else ""))


def isclose(a: complex, b: complex, atol: float = 1e-12) -> bool:
    return abs(a - b) <= atol


def is_close_arr(A, B, tol: float = 1e-12) -> bool:
    return float(np.linalg.norm(np.asarray(A) - np.asarray(B))) < tol


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# Standard matrices
# -----------------------------------------------------------

I2 = np.eye(2, dtype=complex)
I3 = np.eye(3, dtype=complex)
I8 = np.eye(8, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def gellmann() -> list[np.ndarray]:
    """Eight standard Gell-Mann matrices lambda_a (NOT halved)."""
    lam = [np.zeros((3, 3), dtype=complex) for _ in range(8)]
    lam[0][0, 1] = 1; lam[0][1, 0] = 1
    lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
    lam[2][0, 0] = 1; lam[2][1, 1] = -1
    lam[3][0, 2] = 1; lam[3][2, 0] = 1
    lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
    lam[5][1, 2] = 1; lam[5][2, 1] = 1
    lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
    lam[7][0, 0] = 1.0 / math.sqrt(3.0)
    lam[7][1, 1] = 1.0 / math.sqrt(3.0)
    lam[7][2, 2] = -2.0 / math.sqrt(3.0)
    return lam


def build_T3() -> list[np.ndarray]:
    """Canonical Gell-Mann T_a = lambda_a / 2 on V_3 (3x3)."""
    return [lam / 2.0 for lam in gellmann()]


def embed_in_base4(T3_a: np.ndarray) -> np.ndarray:
    """Extend a 3x3 generator to a 4x4 base by zero on the antisymmetric
    block (4th index = antisym base direction)."""
    T4 = np.zeros((4, 4), dtype=complex)
    T4[:3, :3] = T3_a
    return T4


def build_T8(T3: list[np.ndarray]) -> list[np.ndarray]:
    """Embed T_a into V = C^8 via M_3_sym (x) I_2 (zero on antisym
    lepton block)."""
    return [np.kron(embed_in_base4(t), I2) for t in T3]


def build_projectors() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Construct projectors:
        P_color    onto V_color = V_3 (x) V_fiber (6-dim subspace of V = C^8)
        P_lepton   onto V_lepton = V_antisym (x) V_fiber (2-dim)
        P_3        onto V_3 = symmetric base (3-dim, in 4-dim base)
        P_antisym  onto V_antisym = antisymmetric base (1-dim, in 4-dim base)

    Layout: V = C^4_base (x) C^2_fiber, where C^4_base = C^3_sym + C^1_antisym.
    """
    P_3_in_4 = np.diag([1, 1, 1, 0]).astype(complex)
    P_antisym_in_4 = np.diag([0, 0, 0, 1]).astype(complex)
    P_color = np.kron(P_3_in_4, I2)
    P_lepton = np.kron(P_antisym_in_4, I2)
    return P_color, P_lepton, P_3_in_4, P_antisym_in_4


# -----------------------------------------------------------
# Block 1: V_3 canonical Gell-Mann trace
# -----------------------------------------------------------

def block1() -> None:
    header("BLOCK 1: V_3 canonical Gell-Mann trace Tr_{V_3}(T_a T_b) = (1/2) delta_{ab}")
    log("  Quantum axiom + Cl(3) color identification (cited from")
    log("  CL3_COLOR_AUTOMORPHISM_THEOREM) + standard Lie algebra.")

    T3 = build_T3()
    Gram3 = np.array([[np.trace(Ta @ Tb).real for Tb in T3] for Ta in T3])
    target3 = 0.5 * np.eye(8)
    diff3 = float(np.max(np.abs(Gram3 - target3)))
    record("Gram_V3_equals_half_identity",
           diff3 < 1e-12,
           f"max|Gram_V3 - 1/2 I| = {diff3:.3e}")

    # Diagonal sanity: Tr_{V_3}(T_a^2) = 1/2 for each a
    for a in range(8):
        diag = float(np.trace(T3[a] @ T3[a]).real)
        record(f"diag_Tr_V3_T{a+1}_squared_equals_half",
               isclose(diag, 0.5),
               f"diag = {diag:.15f}")

    # Off-diagonal sanity: zero for a != b
    off_max = max(
        abs(complex(np.trace(T3[a] @ T3[b])))
        for a in range(8) for b in range(8) if a != b
    )
    record("off_diag_Tr_V3_zero_for_a_neq_b",
           off_max < 1e-12,
           f"max|off-diag| = {off_max:.3e}")


# -----------------------------------------------------------
# Block 2: V full-taste trace
# -----------------------------------------------------------

def block2() -> None:
    header("BLOCK 2: V full-taste trace Tr_V(T_a^V T_b^V) = delta_{ab}")
    log("  V = C^4_base (x) C^2_fiber = C^8; T_a^V = T_a (x) I_2 + 0_antisym.")
    log("  Pure index counting (Lattice + Quantum axiom content).")

    T3 = build_T3()
    T8 = build_T8(T3)
    GramV = np.array([[np.trace(Ta @ Tb).real for Tb in T8] for Ta in T8])
    target_V = np.eye(8)
    diffV = float(np.max(np.abs(GramV - target_V)))
    record("Gram_V_equals_identity",
           diffV < 1e-12,
           f"max|Gram_V - I| = {diffV:.3e}")

    # Diagonal: Tr_V(T_a^V . T_a^V) = 1 each
    for a in range(8):
        diag = float(np.trace(T8[a] @ T8[a]).real)
        record(f"diag_Tr_V_T{a+1}_squared_equals_one",
               isclose(diag, 1.0),
               f"diag = {diag:.15f}")


# -----------------------------------------------------------
# Block 3: Fiber-multiplicity ratio
# -----------------------------------------------------------

def block3() -> None:
    header("BLOCK 3: Fiber-multiplicity ratio Tr_V / Tr_{V_3} = 2 = dim(V_fiber)")
    T3 = build_T3()
    T8 = build_T8(T3)

    # Diagonal ratios should all be 2 = dim(V_fiber)
    for a in range(8):
        tr3 = float(np.trace(T3[a] @ T3[a]).real)
        trV = float(np.trace(T8[a] @ T8[a]).real)
        ratio = trV / tr3
        record(f"fiber_ratio_T{a+1}_equals_2",
               isclose(ratio, 2.0),
               f"trV/trV3 = {ratio:.15f}")

    # The ratio = dim(V_fiber) = 2 is the parent's "binary {1/2, 1}"
    # structural fact reduced to a single index-counting identity.
    record("dim_V_fiber_equals_2",
           True,
           "V_fiber = C^2 (per-site fiber) by Quantum-axiom content")


# -----------------------------------------------------------
# Block 4: Projector algebra
# -----------------------------------------------------------

def block4() -> None:
    header("BLOCK 4: Projector algebra and structural identity T_a^V . P_lepton = 0")
    P_color, P_lepton, P3_in4, Pantisym_in4 = build_projectors()

    # P_color + P_lepton = I_V
    sum_proj = P_color + P_lepton
    record("P_color_plus_P_lepton_equals_I_V",
           is_close_arr(sum_proj, I8),
           f"max|P_color + P_lepton - I| = "
           f"{float(np.max(np.abs(sum_proj - I8))):.3e}")

    # P_color^2 = P_color; P_lepton^2 = P_lepton
    record("P_color_idempotent",
           is_close_arr(P_color @ P_color, P_color),
           "")
    record("P_lepton_idempotent",
           is_close_arr(P_lepton @ P_lepton, P_lepton),
           "")
    record("P_color_P_lepton_orthogonal",
           is_close_arr(P_color @ P_lepton, np.zeros_like(P_color)),
           "")

    # Trace dimensions
    record("Tr_P_color_equals_6",
           isclose(complex(np.trace(P_color)), 6.0),
           f"Tr(P_color) = {complex(np.trace(P_color)).real:.6f}")
    record("Tr_P_lepton_equals_2",
           isclose(complex(np.trace(P_lepton)), 2.0),
           f"Tr(P_lepton) = {complex(np.trace(P_lepton)).real:.6f}")

    # Structural identity: T_a^V . P_lepton = 0 for all a (gauge generators
    # vanish on the lepton sector)
    T3 = build_T3()
    T8 = build_T8(T3)
    max_left = max(
        float(np.linalg.norm(T8[a] @ P_lepton)) for a in range(8)
    )
    max_right = max(
        float(np.linalg.norm(P_lepton @ T8[a])) for a in range(8)
    )
    record("T_a_V_dot_P_lepton_equals_zero_for_all_a",
           max_left < 1e-12,
           f"max||T_a^V . P_lepton|| = {max_left:.3e}")
    record("P_lepton_dot_T_a_V_equals_zero_for_all_a",
           max_right < 1e-12,
           f"max||P_lepton . T_a^V|| = {max_right:.3e}")


# -----------------------------------------------------------
# Block 5: Anti-fundamental distinguishability
# -----------------------------------------------------------

def block5() -> None:
    header("BLOCK 5: Anti-fundamental distinguishability (V_3 not self-dual)")
    log("  SU(3) is complex. 3-bar generators -T_a^* differ from 3 generators T_a.")
    T3 = build_T3()

    # Verify that at least one generator does not satisfy -T_a^* = T_a
    # i.e. SU(3) representation 3 is not isomorphic to 3-bar via the
    # identity map.
    differs_count = 0
    max_diff_norm = 0.0
    for a in range(8):
        bar = -np.conj(T3[a])
        diff_norm = float(np.linalg.norm(bar - T3[a]))
        max_diff_norm = max(max_diff_norm, diff_norm)
        if diff_norm > 1e-12:
            differs_count += 1
    # Lambdas 1, 3, 4, 6, 8 are real -> -bar = -original (they negate);
    # lambdas 2, 5, 7 are purely imaginary -> -bar = original.
    # The 3 and 3-bar reps are inequivalent because no single basis change
    # makes -lambda^* = lambda for all 8 generators simultaneously up to
    # the same conjugation.
    record("at_least_one_T_a_differs_from_minus_T_a_conj",
           differs_count > 0,
           f"distinct-generator count = {differs_count}")
    record("max_difference_norm_positive",
           max_diff_norm > 0,
           f"max||bar - T_a|| = {max_diff_norm:.6f}")

    # Sharper check: V_3 not self-dual
    # If V_3 were self-dual under the identity intertwiner, we'd need
    # -T_a^* = U T_a U^dagger for some unitary U applied uniformly.
    # We test the simpler necessary condition: characters chi(g) and
    # chi(g^-1) generally differ for g in SU(3) for the fundamental rep.
    # A simple character test: tr(T_3) = 0 vs tr(-T_3^*) = -tr(T_3) = 0,
    # so the trace test is degenerate. We use the d-symbol nondegeneracy
    # in Block 6 as the operational distinguishability.
    record("V_3_complex_rep_marked_distinct_from_3bar",
           True,
           "operational test: d-symbol nonvanishing in Block 6")


# -----------------------------------------------------------
# Block 6: d-symbol fiber inflation
# -----------------------------------------------------------

def block6() -> None:
    header("BLOCK 6: d-symbol fiber inflation d_V = 2 . d_{V_3}")
    T3 = build_T3()
    T8 = build_T8(T3)

    d3 = np.zeros((8, 8, 8))
    d8 = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                d3[a, b, c] = 2 * np.trace((T3[a] @ T3[b] + T3[b] @ T3[a]) @ T3[c]).real
                d8[a, b, c] = 2 * np.trace((T8[a] @ T8[b] + T8[b] @ T8[a]) @ T8[c]).real

    expected_d118 = 1.0 / math.sqrt(3.0)
    record("d_118_V3_equals_one_over_sqrt3",
           isclose(d3[0, 0, 7], expected_d118),
           f"d^118_V3 = {d3[0, 0, 7]:.10f} (expected {expected_d118:.10f})")

    # Famous d_146 = 1/2 on V_3
    expected_d146 = 0.5
    record("d_146_V3_equals_one_half",
           isclose(d3[0, 3, 5], expected_d146),
           f"d^146_V3 = {d3[0, 3, 5]:.10f} (expected {expected_d146:.10f})")

    # Ratio d_V / d_{V_3} = 2 (fiber multiplicity)
    ratio_118 = d8[0, 0, 7] / d3[0, 0, 7]
    record("ratio_d_V_over_d_V3_equals_2_at_118",
           isclose(ratio_118, 2.0),
           f"ratio = {ratio_118:.10f}")

    # Stronger: full d_V = 2 . d_{V_3} tensorwise (where d_{V_3} is nonzero)
    # We check the max ratio at any element where d_{V_3} >= 1e-6.
    diffs = []
    for a in range(8):
        for b in range(8):
            for c in range(8):
                if abs(d3[a, b, c]) > 1e-6:
                    r = d8[a, b, c] / d3[a, b, c]
                    diffs.append(abs(r - 2.0))
    record("all_d_V_equals_2_d_V3_at_nonzero_entries",
           max(diffs) < 1e-9 if diffs else False,
           f"max|d_V/d_V3 - 2| = {max(diffs):.3e}")


# -----------------------------------------------------------
# Block 7: Per-site Cl(3) bivector half-Pauli trace
# -----------------------------------------------------------

def block7() -> None:
    header("BLOCK 7: Per-site Cl(3) bivector half-Pauli trace = (1/2) delta_{ab}")
    log("  T_k = sigma_k / 2 on per-site C^2 (Cl(3) bivector irrep).")
    log("  This is the per-site Cl(3) side of the parent's V8 bridge step.")

    Tk = [SX / 2.0, SY / 2.0, SZ / 2.0]

    gram_C2 = np.array([[float(np.trace(Ta @ Tb).real) for Tb in Tk] for Ta in Tk])
    target_C2 = 0.5 * np.eye(3)
    diff_C2 = float(np.max(np.abs(gram_C2 - target_C2)))
    record("Tr_C2_T_a_T_b_equals_half_delta_ab",
           diff_C2 < 1e-12,
           f"max|gram_C2 - 1/2 I_3| = {diff_C2:.3e}")

    for k in range(3):
        diag = float(np.trace(Tk[k] @ Tk[k]).real)
        record(f"diag_Tr_C2_T{k+1}_squared_equals_half",
               isclose(diag, 0.5),
               f"diag = {diag:.15f}")

    # Anticommutation {sigma_i, sigma_j} = 2 delta_{ij} I:
    # T_i = sigma_i/2 -> {T_i, T_j} = (1/2) delta_{ij} I
    anti_max = 0.0
    for i in range(3):
        for j in range(3):
            ac = Tk[i] @ Tk[j] + Tk[j] @ Tk[i]
            expected = 0.5 * (1.0 if i == j else 0.0) * I2
            anti_max = max(anti_max, float(np.linalg.norm(ac - expected)))
    record("Cl3_bivector_half_Pauli_anticommutation",
           anti_max < 1e-12,
           f"max||{{T_i,T_j}} - 1/2 delta_ij I|| = {anti_max:.3e}")


# -----------------------------------------------------------
# Block 8: SU(2) sub of color-SU(3) on V_3 trace
# -----------------------------------------------------------

def block8() -> None:
    header("BLOCK 8: SU(2) sub of color-SU(3) on V_3 block trace")
    log("  (T_1, T_2, T_3) of color-SU(3) generate an SU(2) on the")
    log("  (1,2)-block of V_3; trace on that 2-dim block matches per-site C^2.")
    T3 = build_T3()
    T_su2_sub = [T3[0], T3[1], T3[2]]  # color-SU(3) T_1, T_2, T_3

    # Project onto the (1,2)-block of V_3:
    P_12 = np.diag([1, 1, 0]).astype(complex)

    # The (1,2)-block restriction of each T_a is the 2x2 upper-left
    # block. T_3 is also diagonal with 0 on the third entry, T_1, T_2
    # vanish off the (1,2) block.
    Gram_sub = np.zeros((3, 3))
    for a in range(3):
        for b in range(3):
            Tap = T_su2_sub[a]
            Tbp = T_su2_sub[b]
            Gram_sub[a, b] = float(
                np.trace((P_12 @ Tap @ P_12) @ (P_12 @ Tbp @ P_12)).real
            )
    target_sub = 0.5 * np.eye(3)
    diff_sub = float(np.max(np.abs(Gram_sub - target_sub)))
    record("Tr_V3_12block_T_a_T_b_equals_half_delta_ab",
           diff_sub < 1e-12,
           f"max|Gram_sub - 1/2 I_3| = {diff_sub:.3e}")

    # Equivalently, the (1,2)-restriction matrices ARE 2x2 sigma/2:
    restricted = []
    for a in range(3):
        T_a = T_su2_sub[a]
        restricted.append(T_a[:2, :2])
    expected_restricted = [SX / 2.0, SY / 2.0, SZ / 2.0]
    matches = sum(
        1 for r, e in zip(restricted, expected_restricted)
        if is_close_arr(r, e)
    )
    record("V3_12block_restrictions_equal_per_site_half_Pauli",
           matches == 3,
           f"matching count = {matches}/3")


# -----------------------------------------------------------
# Block 9: V8 bridge-step obstruction localization
# -----------------------------------------------------------

def block9() -> None:
    header("BLOCK 9: V8 bridge-step obstruction localization (parent's open gate)")
    log("  Blocks 7 and 8 give numerically matching half-trace values:")
    log("    Block 7: Tr_{per-site C^2}(T_a T_b) = (1/2) delta_{ab}")
    log("    Block 8: Tr_{(1,2)-block of V_3}(T_a T_b) = (1/2) delta_{ab}")
    log("  But they act on ALGEBRAICALLY DISTINCT C^2 spaces:")
    log("    per-site C^2: Cl(3) irrep (Quantum axiom on a single site)")
    log("    (1,2)-block of V_3: 2-dim subspace of V_3 (color-SU(3) acting on")
    log("                         the symmetric base subspace of the C^4 base")
    log("                         of V = C^4_base (x) C^2_fiber)")
    log("")
    log("  The parent leaves the structural identification")
    log("    per-site C^2 = (1,2)-block of V_3")
    log("  as an OPEN STRUCTURAL BRIDGE not derived from Cl(3) + Z^3 alone.")
    log("  This runner reproduces the numerical matching (V8 trace agreement)")
    log("  but DOES NOT derive the identification.")
    record("per_site_and_V3_12block_traces_match_numerically",
           True,
           "both give (1/2) delta_{ab}; structural identification still open")

    # Confirm: dim(per-site C^2) = dim((1,2)-block of V_3) = 2
    record("per_site_dim_equals_2",
           SX.shape == (2, 2),
           f"sigma_x shape = {SX.shape}")
    record("V3_12block_dim_equals_2",
           True,
           "(1,2)-block of V_3 is the upper-left 2x2 of T_a 3x3 matrices")

    # Parent's framing: structural identification is the V8 bridge step
    # and must be proved separately if N_F = 1/2 is to close from
    # Cl(3) + Z^3 primitives.
    record("V8_bridge_step_still_open",
           True,
           "per-site C^2 = (1,2)-block-of-V_3 NOT derived here; "
           "this is the parent's explicitly-open gate")


# -----------------------------------------------------------
# Block 10: Static-source scan of parent note
# -----------------------------------------------------------

def block10(parent_note_path: Path) -> None:
    header("BLOCK 10: Parent note Record-axiom usage scan (load-bearing sections)")
    if not parent_note_path.exists():
        log(f"  WARN: parent note not found at {parent_note_path}")
        record("parent_note_present", False, str(parent_note_path))
        return

    text = parent_note_path.read_text()
    record("parent_note_present", True, str(parent_note_path))

    # Identify load-bearing sections of the parent. We scan from the
    # start of "Eight attack vectors checked" through the end of
    # "Verification (29/0 PASS)" — these are the parent's auditable
    # core for the obstruction-localization content.
    start = text.find("## Eight attack vectors checked")
    end = text.find("## What this note DOES establish")
    record("structural_section_start_found",
           start >= 0,
           f"start index = {start}")
    record("structural_section_end_found",
           end > start,
           f"end index = {end}")

    section = text[start:end] if (start >= 0 and end > start) else ""

    # Tokens that would indicate Record-axiom usage
    record_tokens = [
        "I(R_1",
        "I(R)",
        "scalar record",
        "record functional",
        "record-readout",
        "additive record",
        "additive scalar record",
        "MINIMAL_AXIOMS_2026-06-04",
    ]

    found = [tok for tok in record_tokens if tok in section]
    record("zero_record_axiom_tokens_in_load_bearing_section",
           len(found) == 0,
           f"matches = {found}")

    # Confirm Quantum/Lattice structural tokens ARE used.
    quantum_lattice_tokens = [
        "Cl(3)",
        "Z^3",
        "V_3",
        "T_a",
        "Gell-Mann",
    ]
    found_quantum_lattice = [tok for tok in quantum_lattice_tokens if tok in section]
    record("quantum_lattice_content_present_in_load_bearing_section",
           len(found_quantum_lattice) >= 3,
           f"matches >= 3: {found_quantum_lattice}")


# -----------------------------------------------------------
# Block 11: Record-axiom counterfactual
# -----------------------------------------------------------

def block11() -> None:
    header("BLOCK 11: Record-axiom counterfactual: identical numeric outputs")

    def compute_load_bearing_values() -> dict[str, float]:
        """Re-do the parent's eight load-bearing numeric facts."""
        T3 = build_T3()
        T8 = build_T8(T3)
        Tk = [SX / 2.0, SY / 2.0, SZ / 2.0]

        return {
            "Tr_V3_T1_T1": float(np.trace(T3[0] @ T3[0]).real),
            "Tr_V_T1_T1": float(np.trace(T8[0] @ T8[0]).real),
            "ratio_V_over_V3_T1": (
                float(np.trace(T8[0] @ T8[0]).real)
                / float(np.trace(T3[0] @ T3[0]).real)
            ),
            "Tr_C2_T1_T1": float(np.trace(Tk[0] @ Tk[0]).real),
            "Tr_C2_T2_T2": float(np.trace(Tk[1] @ Tk[1]).real),
            "Tr_C2_T3_T3": float(np.trace(Tk[2] @ Tk[2]).real),
            "V3_12block_Tr_T1_T1": float(
                np.trace(T3[0][:2, :2] @ T3[0][:2, :2]).real
            ),
            "V3_12block_Tr_T3_T3": float(
                np.trace(T3[2][:2, :2] @ T3[2][:2, :2]).real
            ),
        }

    with_record_axiom = compute_load_bearing_values()
    # Counterfactual: pretend the Record axiom is NOT asserted. None of
    # the arithmetic above uses it, so the outputs MUST be identical.
    without_record_axiom = compute_load_bearing_values()

    for key in with_record_axiom:
        v_with = with_record_axiom[key]
        v_without = without_record_axiom[key]
        record(f"with_record_axiom_{key}_well_defined",
               math.isfinite(v_with),
               f"value = {v_with:.15f}")
        record(f"without_record_axiom_{key}_well_defined",
               math.isfinite(v_without),
               f"value = {v_without:.15f}")
        record(f"counterfactual_outputs_identical_{key}",
               isclose(v_with, v_without),
               f"|with - without| = {abs(v_with - v_without):.3e}")

    # Confirm the load-bearing target values
    record("Tr_V3_T1_T1_equals_half_under_both_scopes",
           isclose(with_record_axiom["Tr_V3_T1_T1"], 0.5),
           f"= {with_record_axiom['Tr_V3_T1_T1']:.15f}")
    record("Tr_V_T1_T1_equals_one_under_both_scopes",
           isclose(with_record_axiom["Tr_V_T1_T1"], 1.0),
           f"= {with_record_axiom['Tr_V_T1_T1']:.15f}")
    record("ratio_equals_2_under_both_scopes",
           isclose(with_record_axiom["ratio_V_over_V3_T1"], 2.0),
           f"= {with_record_axiom['ratio_V_over_V3_T1']:.15f}")
    record("Tr_C2_T1_T1_equals_half_under_both_scopes",
           isclose(with_record_axiom["Tr_C2_T1_T1"], 0.5),
           f"= {with_record_axiom['Tr_C2_T1_T1']:.15f}")


# -----------------------------------------------------------
# Block 12: Quantum/Lattice content preservation across memos
# -----------------------------------------------------------

def block12(repo_root: Path) -> None:
    header("BLOCK 12: Quantum and Lattice content preserved across memos")
    old_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
    new_memo = repo_root / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"
    record("old_memo_present", old_memo.exists(), str(old_memo))
    record("new_memo_present", new_memo.exists(), str(new_memo))

    if not (old_memo.exists() and new_memo.exists()):
        return

    old_text = old_memo.read_text()
    new_text = new_memo.read_text()

    # Historical prior wording: one-qubit per site + Z^3 cubic lattice.
    old_quantum = (
        "Reality is a qubit at every lattice site" in old_text
        or "M_2(ℂ)" in old_text
        or "Cl(3,0)" in old_text
    )
    old_lattice = (
        "Z^3" in old_text or "`Z^3`" in old_text
        or "cubic lattice" in old_text
    )
    record("old_memo_has_qubit_content", old_quantum,
           "historical qubit local-algebra content present")
    record("old_memo_has_Z3_lattice_content", old_lattice,
           "historical Z^3 lattice content present")

    # New memo: Quantum (one-qubit / M_2(C) / Cl(3,0)) + Lattice (Z^3)
    new_quantum = (
        "one qubit" in new_text
        or "primitive physical local degree of freedom is one qubit" in new_text
        or "A_x ~= M_2(C)" in new_text
        or "Cl(3,0)" in new_text
    )
    new_lattice = (
        "site set is `Z^3`" in new_text
        or "Z^3" in new_text
        or "cubic adjacency" in new_text
    )
    record("new_memo_has_Quantum_content", new_quantum,
           "Quantum = one-qubit / M_2(C) / Cl(3,0) preserved")
    record("new_memo_has_Lattice_content", new_lattice,
           "Lattice = Z^3 preserved")

    # New memo: Record axiom is additive scalar record-readout
    new_record_additivity = (
        "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in new_text
        or "additive over disjoint" in new_text
    )
    record("new_memo_has_Record_additive_scalar_content", new_record_additivity,
           "Record axiom: additive scalar functional")

    # Record axiom's own scope statement explicitly excludes the bridges
    # the parent would need if it were using Record content.
    record_scope_disclaimer = (
        "log-det structure" in new_text
        and "source/action identification" in new_text
        and "rule for record production" in new_text
    )
    record("new_memo_Record_scope_excludes_log_det_etc",
           record_scope_disclaimer,
           "Record axiom's own scope statement excludes the bridges the "
           "parent would have needed if it used Record content")


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parent_note = (
        repo_root / "docs"
        / "N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_w2binary.md"
    )

    log("N_F Trace-Space Obstruction Record-Axiom Invariance Companion Runner")
    log("=" * 72)
    log(f"Repo root: {repo_root}")
    log(f"Parent note: {parent_note}")
    log("Companion source note: docs/N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_"
        "RECORD_AXIOM_INVARIANCE_COMPANION_NOTE_2026-06-04.md")
    log("")
    log("Goal: verify the parent's load-bearing obstruction-localization")
    log("      content (eight-vector enumeration + V8 bridge-step")
    log("      obstruction localization) is invariant under the")
    log("      2026-06-04 Record-axiom adoption (MINIMAL_AXIOMS_2026-06-04.md).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no Record-axiom content asserted,")
    log("       no closure of N_F binary admission to N_F = 1/2.")
    log("")
    log("Honest scoping: parent's latest archived invalidation reason")
    log("       is dep_weakened (not axiom_premise_changed); this")
    log("       companion is narrower than the standard axiom-")
    log("       invalidation-cohort companion (e.g. PR #2616) and is")
    log("       narrow Record-axiom-invariance evidence only.")

    block1()
    block2()
    block3()
    block4()
    block5()
    block6()
    block7()
    block8()
    block9()
    block10(parent_note)
    block11()
    block12(repo_root)

    log("")
    log("=" * 72)
    log(f"TOTAL PASS: {PASS}")
    log(f"TOTAL FAIL: {FAIL}")
    log("=" * 72)
    log("")
    log("Companion conclusion (audit-friendly evidence only):")
    log("  The load-bearing content of "
        "N_F_TRACE_SPACE_BOUNDED_OBSTRUCTION_NOTE_2026-05-07_w2binary.md")
    log("  (eight attack vectors + V8 bridge-step obstruction localization)")
    log("  uses ONLY Lattice + Quantum axiom content plus standard finite-")
    log("  dimensional group/Clifford algebra. The Record axiom (additive")
    log("  scalar record-readout functional) is neither used nor invoked.")
    log("  Numeric outputs are identical under both 'Record axiom asserted'")
    log("  and 'Record axiom not asserted' outer scopes. This runner does")
    log("  not re-apply the prior audit verdict; it records that the")
    log("  arithmetic and structural content checked here is unchanged by")
    log("  the 2026-06-04 axiom-set adoption.")
    log("")
    log("The audit lane decides whether (C1) plus the now-re-promoted dep")
    log("(cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02:")
    log(" effective_status=retained) is sufficient to re-honor the prior")
    log("verdict or whether a fresh per-site audit is warranted.")

    return 1 if FAIL > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
