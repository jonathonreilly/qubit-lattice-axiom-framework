# Block 02 V1-V5 value gate — substep-4 species-label classification

**Date:** 2026-05-17
**Target:** AC_φλ residual from `staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac`
**Chosen route:** **NO-GO theorem** classifying the species-label residual

## Honest landscape (read first)

The substep-4 AC narrowing (2026-05-07) decomposed `AC_narrow = AC_φ ∧ AC_λ ∧ AC_φλ`.
Today (2026-05-17) two block-01 bridge theorems landed:

- `STAGGERED_DIRAC_SUBSTEP4_AC_LAMBDA_SIMULTANEOUS_DIAGONALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md` — **AC_λ positive bridge** (simultaneous-diagonalization corollary)
- `STAGGERED_DIRAC_SUBSTEP4_AC_PHI_TRACE_EQUIPARTITION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md` — **AC_φ positive bridge** (trace-equipartition identity)

What's left **unhandled** for substep 4: the AC_φλ atom — the explicit identification "framework's 3-fold hw=1 structure IS the SM flavor-generation structure {e/μ/τ, u/c/t, d/s/b, ν_e/ν_μ/ν_τ}".

The substep-4 AC narrowing note already foreshadowed (Step 6) that "AC_φλ has no standard-QFT axiom equivalent" — the SM's "three generations" is empirical, not derivable from any QFT axiom. The C_3-preserved meta-note (2026-05-08) further records that the labeling-convention reframe under preserved C_3 does **not** constitute closure of AC_φλ; it is a separate parameter/readout move.

This block formalizes the impossibility as a NO-GO theorem rather than leaving it as ambient note-language.

## V1: Verdict-identified obstruction

**Yes.** The 2026-05-07 substep-4 AC narrowing note (lines 273-281) explicitly identifies AC_φλ as "specifically the point at which framework derivation must cross into PDG-empirical territory, and the framework's retained-grade rule forbids using PDG data in a positive theorem proof. This is structural, not a small bookkeeping issue."

The 2026-05-08 C_3-preserved meta note further records: "Strict derivation closure of AC_φλ still requires either (a) an explicit user-approved labeling axiom or (b) C_3-breaking dynamics in retained primitives; neither is added here. The 10-probe A3 campaign (PRs #709-#713 + #719-#723) established that no C_3-breaking mechanism is derivable within A_min."

So the obstruction is named (twice) but not formally classified as a no-go theorem. This block closes that gap.

## V2: NEW content (not in any existing note)

The no-go will establish:

1. **Invariant statement.** Under A1 (Cl(3)) + A2 (Z³) + the substep-4-narrow upstream stack, every endomorphism on H_{hw=1} commuting with the C_3[111] cyclic generator carries a permutation symmetry of the three corner labels — namely, the symmetric group action through the C_3 ⊆ S_3 orbit. This permutation-invariance is preserved by all A_min-compatible dynamics.

2. **Required-break statement.** For an *injective name-bearing* map `H_{hw=1} → {e, μ, τ}` (a specific bijection to a labeled set, not just an orbit-equivariant map) to be a theorem of A_min, the framework must distinguish a specific ordering of the C_3 orbit. This requires breaking the orbit symmetry — equivalent to producing an A_min-compatible C_3-breaking operator.

3. **No-such-operator lemma.** No C_3-breaking operator exists in A_min (cites the 10-probe A3 campaign + 2026-05-08 preserved meta + 2026-05-10 species-count regulator-dependence no-go).

4. **Three closure-path enumeration.** AC_φλ is bounded under named external premises:
   - (P1) **Labeling-convention premise**: stipulate a specific mass-ordering bijection (not a theorem of A_min; ZERO retained-grade content consumed; consistent with preserved-C_3).
   - (P2) **C_3-breaking dynamics premise**: add a C_3-breaking primitive (rejected by 10-probe A3 campaign within A_min; requires new axiom).
   - (P3) **PDG-empirical premise**: import three observed lepton masses as identification input (forbidden by retained-grade rule).
   These three are the ONLY routes; any fourth route reduces to one of these.

5. **Counter-models.** Exhibit two explicit endomorphism-equivariant alternatives that are A_min-indistinguishable: the identity-labeling and the C_3-rotated-labeling are both A_min-consistent, but they disagree on the species map. This is a counter-model that A_min cannot resolve.

The 2026-05-08 meta-note **interprets** the situation; this no-go **proves** the interpretation by (i) producing the counter-model, (ii) enumerating the exhaustive closure paths, and (iii) tying P2 to existing retained no-go content.

## V3: Audit lane could complete?

**No.** The audit lane does syntactic/dependency checks and cross-row consistency. It cannot:
- Construct the C_3-orbit indistinguishability counter-model.
- Prove the exhaustiveness of the three closure paths.
- Quantify the orbit-symmetry preservation under the A_min upstream stack.

This requires structural mathematical insight beyond what the audit pipeline does. The audit lane can REVIEW the no-go after it's written; it cannot AUTHOR it.

## V4: Non-trivial marginal content

**Yes.** The no-go does three things not present anywhere on main:

- Formalizes the AC_φλ impossibility as a **structural invariant** (orbit-equivariance under C_3) rather than just a "no equivalent QFT axiom" assertion.
- Constructs explicit indistinguishable counter-models (identity vs cyclic relabeling), which gives an explicit mathematical witness.
- Establishes the **closure path enumeration is exhaustive** — not just "here are three known paths" but "ANY other closure route reduces to one of these three" (by the invariant argument).

This unlocks downstream decisions: the s3_anomaly_spacetime_lift and s3_time_theta_to_slice rows (688-689 desc) can now treat AC_φλ as a **classified-impossible-without-named-premise** dependency rather than a vague "admitted-context" hanger.

## V5: Not a one-step variant

**Not a relabel:**

- The substep4_ac note (2026-05-07) decomposes AC_narrow and says "AC_φλ is the residual"; it does not produce a counter-model or prove exhaustiveness of closure paths.
- The C_3-preserved meta note (2026-05-08) interprets the situation but explicitly says (line 153) "does NOT claim AC_φλ is trivially closed by definition." It records the labeling-convention reframe as a SEPARATE move; the no-go would formally classify the residual itself.
- The 10-probe A3 obstruction routes (r1-r5) prove no C_3-breaking mechanism EXISTS; this no-go uses that result as a lemma in a larger statement that quantifies over ALL closure paths, not just C_3-breaking attempts.
- The hierarchy α_LM exponent species-count no-go (2026-05-10) shows regulator-dependence for SPECIES COUNT; this no-go addresses the orthogonal SPECIES IDENTIFICATION problem.
- The block-01 bridges (today) handle AC_λ and AC_φ; neither addresses AC_φλ.

## V1-V5 outcome: PASS

Route: write a **NO-GO theorem** for AC_φλ formal closure within A_min, with three named external-premise routes (labeling / C_3-breaking / PDG-empirical), with explicit indistinguishable counter-models, with exhaustiveness argument.

## Honest scope limits (in writing now)

The no-go does NOT:
- Promote labeling-convention from "convention" to "theorem".
- Discharge AC_φλ via the labeling-convention path (that's a separate downstream move).
- Modify substep 4's bounded_theorem status.
- Touch any retained theorem.
- Add a new axiom.

It DOES:
- Formally classify the residual.
- Make impossibility-within-A_min into a positive content (a theorem).
- Enumerate exhaustive closure paths.
- Unlock downstream rows blocked on this admission status.

A no-go is positive content.
