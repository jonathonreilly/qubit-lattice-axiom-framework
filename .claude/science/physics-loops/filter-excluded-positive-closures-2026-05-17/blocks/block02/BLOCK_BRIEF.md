# Block 02 Brief: substep 4 species-label residual classification

**Lane:** staggered_dirac_realization_gate closure (continuation from block 01)
**Block 01 result:** PR #1401 — bounded_theorem synthesis of substeps 1-3; substep 4 species-label residual AC_phi_lambda explicitly carried as admitted-context.

**This block's goal:** Formally classify the substep-4 species-label closure paths and produce one of:
- (positive) a no-go theorem proving AC_phi_lambda cannot close from A_min without one of the named external premises
- (positive) a bounded_theorem proving AC_phi_lambda DOES close under named minimal premises
- (positive) a sharper enumeration than substep4_ac currently has of the three closure paths (labeling premise / C_3-breaking dynamics / empirical input)

**Target row:** `staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07_substep4ac` (currently unaudited; eff=unaudited)
**Goal-row leverage:** substep 4 carries `s3_anomaly_spacetime_lift_note` and `s3_time_theta_to_slice_coupling_note` (each 688-689 desc downstream)

## Existing context
- The bounded substep4_ac note on disk says AC_phi_lambda is bounded-narrow under specific conditions
- The new block-01 synthesis names it as carried admitted-context
- No retained_no_go currently exists for the labeling-premise route specifically

## V1-V5 must answer (in writing) before any PR
- V1: Specific obstruction (quote substep4_ac note's verdict or open-frontier text)
- V2: NEW content (no-go enumeration with proofs / bounded theorem with proof / sharper classification)
- V3: Audit lane cannot do this (yes — requires structural insight)
- V4: Non-trivial marginal content
- V5: Not a one-step variant of block 01

## Deliverable
1. Source theorem or no-go note `docs/STAGGERED_DIRAC_SUBSTEP4_LABELING_<TYPE>_NOTE_2026-05-17.md` where TYPE ∈ {NO_GO, BOUNDED_THEOREM, CLASSIFICATION}
2. Paired runner with SCORECARD
3. Cached runner output
4. Block artifacts at `.claude/science/physics-loops/filter-excluded-positive-closures-2026-05-17/blocks/block02/`
5. PR titled `[physics-loop] staggered-dirac-substep4-classification-block02: <honest status>`

## Hard rules (same as block 01)
- A_min only (A1, A2)
- No bare `retained`/`promoted`; `proposed_retained` only if certificate justifies
- No fitted values, observational comparators, literature inputs as proof
- Push only this branch
- Do NOT touch audit data, AUDIT_LEDGER, publication, README, lane registry
- One review PR; do not merge

**Time budget:** ~75 min
