# Block01 Section R1 — Equal-Block Measure from Dephasing + Block-Exchange Invariance

**Date:** 2026-06-20
**Route:** R1 (equal-block measure — the stronger candidate)
**Target:** `docs/KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md`
(bounded_theorem; r=1/2, Q=2/3 conditional on two named inputs).
**Runner:** `scripts/koide_records_objectivity_block_exchange_dephasing_2026_06_20.py`
**Cache:** `logs/runner-cache/koide_records_objectivity_block_exchange_dephasing_2026_06_20.txt`
(TOTAL: PASS=17 FAIL=0)
**Outcome:** NAMED-PREMISE SPLIT (equal-block input is NOT derived; identified
exactly as the isotype-label-counting readout measure, not supplied by A_min).

## Goal

Try to DERIVE input (1) of the conditional note — the equal-block `(1,1)`
weighting `w_s = w_p` for the C3 singlet/doublet split — from the dephasing
channel's fixed-point measure, *forced* by a BLOCK-EXCHANGE invariance of the
Record readout, rather than assumed. If it derives, the row flips toward
unconditional. Hard guard: r and Q must be OUTPUTS; no import of the empirical
Koide value.

## What the runner does (all residuals explicit, all checks pass)

- **R1.A** Builds the dephasing channel D on 3x3 density operators (full
  decoherence in the C-eigen/Fourier basis), verifies CPTP, idempotent, and
  that its fixed set is the C-diagonal (functions of C). Residuals all 1e-16.
- **R1.B** The maximally-symmetric (C-invariant, max-entropy, full-rank)
  dephasing fixed point is `I/3`. Its singlet/doublet block probabilities are
  **the rank/dimension (Plancherel) measure (1/3, 2/3)**. The matching capacity
  branch with weights (1,2) peaks at r=1 → **Q=1**. This reproduces the note's
  central claim: the dephasing comparison points to rank-weighting, not (1,1).
- **R1.C** BLOCK-EXCHANGE TEST. The singlet block is dim 1, the doublet block
  dim 2. A `*`-automorphism / unitary preserves block dimension, so **no
  block-exchange map exists in A_min**: 200 random unitaries cannot push the
  rank-1 singlet projector onto the rank-2 doublet projector (best similarity
  0.286 < 1). The only genuine grading-preserving symmetry is C-equivariance,
  whose invariant state is `I/3` → dimension weights (1,2) again.
- **R1.D** Identifies equal-block `(1,1)` exactly as the **isotype-label-counting
  (dimension-blind) measure**: uniform over the 2 isotype LABELS, ignoring that
  the blocks have dimensions 1 and 2. Confirms `r* = w_p/(2 w_s)`, so r=1/2
  requires `w_s = w_p` exactly — a dimension-blind weight. (1,1) → r=1/2 → Q=2/3
  is recomputed as the OUTPUT of that branch.
- **R1.E** Reads recorded axiom content (`axiom_premise_nodes.json`): the Record
  axiom supplies "no readout context, sector-generation rule, weighting,
  normalization, probability, dynamics"; the realized_state_primitive supplies a
  slot, "never ... measure, typicality ..., weighting, probability rule". So the
  label-counting measure is **NOT supplied by A_min**.
- **R1.F** Non-import guard: (1,1)→Q=2/3 and (1,2)→Q=1 from the SAME machinery;
  2/3 appears only as a solved output, never as a premise.

## The load-bearing wall (why R1 does not close)

Equal-block weighting `w_s = w_p` is a **dimension-blind, isotype-label-counting
measure**. The dephasing/decoherence structure of A_min supplies only
*dimension-aware* (trace / Plancherel) measures: its maximally-symmetric fixed
point is `I/3`, giving block weights (1/3, 2/3) = (1,2), i.e. **Q=1, not Q=2/3**.

The candidate forcing symmetry — block-exchange invariance — **cannot exist** in
A_min because the singlet (dim 1) and doublet (dim 2) blocks are not isomorphic:
no `*`-automorphism or unitary swaps unequal-dimension blocks. So block-exchange
invariance is not a symmetry of the Record readout algebra and cannot force
`w_s = w_p`. This independently re-derives, from channel structure, the freedom
left open by the cited isotype-split no-go
(`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21`): PD + Ad-invariance
+ orthogonality leave the scalar/traceless (= singlet/doublet) weight free, and
the dephasing fixed-point measure picks the dimension weight, not the equal one.

## Exactly what additional structure would force equal weighting

Equal-block `(1,1)` requires a readout that **registers one scalar per isotype
LABEL with equal a-priori weight, independent of block dimension** — a counting
measure on the set {singlet, doublet}, not a state-trace on the Hilbert space.
A_min's Record axiom registers additive scalar outcomes in a *supplied* readout
context but does not supply that context, the sector-generation rule, or the
per-label weight. Therefore the equal-block input is an **additional named
readout-context premise**, not a consequence of dephasing/block-exchange in
A_min. R1 does not supply it; nothing in A_min + the four primitives does.

## Honest status

- **Does it derive the input?** No. Honest outcome = **named_premise** split.
- **Why it is still valuable:** R1 sharpens the residual from "equal-block is an
  unforced metric choice" to the precise statement "equal-block = a dimension-
  blind isotype-LABEL-COUNTING readout measure, which is exactly the structure
  A_min's Record axiom does NOT supply (it supplies only dimension-aware
  trace/Plancherel measures, whose fixed point gives Q=1)." This pins the
  missing premise to a single, auditable object: a label-counting readout
  context. It also independently confirms, from channel fixed-point structure,
  the note's claim and the isotype-split no-go, and rules out block-exchange
  invariance as a closure route (the unequal block dimensions are a hard
  obstruction).
- **No empirical import:** r=1/2 / Q=2/3 appear only as solved outputs; the
  (1,2) counterfactual yields Q=1 from identical machinery (non-circular).
- **No new axiom/primitive introduced.** Verdict authority is the independent
  audit lane; this section records a derivation attempt and its honest result.

## Recommendation for the row

The row stays **conditional**. R1 does not flip it. The closure path for input
(1) is now precisely named: derive (or admit) a dimension-blind isotype-label-
counting readout measure. The dephasing/block-exchange route is closed against
forcing it; any future positive work must supply the label-counting readout
context as an independently audited structure, since A_min's intrinsic measures
on the C3 grading are dimension-weighted and yield Q=1.
