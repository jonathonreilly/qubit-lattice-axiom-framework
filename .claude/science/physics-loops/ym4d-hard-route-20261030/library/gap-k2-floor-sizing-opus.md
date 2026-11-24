lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T02:36Z

# Row 1470: sizing the weak-coupling floor for a K-II tool by step certificates

Started 2026-11-24T14:36Z (date -u), Mac mini worker 2, Claude Opus 5.5 high. Read only, no new proof.
Pinned at commit 95f65cd6f on claude/ym4d-hard-route.

Question (row 1468 Section 8 row 2, queue row 1470): at what inverse coupling X does a weak-coupling
block step with explicit constants close, for block side 2 or 3, or 2^m built by iterating a small map?
Outcome (a): X <= 100 with the clause list (order-one part <= ~400 steps, proof-design row justified);
outcome (b): X >= 1e4 or a structural reason (K-II by step certificates closed by count).

## Plan

1. Read FINISH rows 1464, 1467 (if landed), 1468; library/lean-step-side-read-opus.md Steps 3-6; row 1468 output.
2. Read the floor clauses in the Sussman-Alpoge YM4 Lean release (~/ym4d-papers/sa-ym4-lean-full, read only).
3. Read Balaban's small-field / large-field conditions (library/lit-balaban.md; CMP 109, 116, 119, 122 in ~/ym4d-papers).
4. Table: each binding clause, its floor as written, smallest x if the 1/100 exponent and constants are re-chosen,
   structural or bookkeeping, label proved / read / guessed, file:line.
5. Verdict (a) or (b).

## Step 1. Inputs read (14:40Z)

- Row 1464 (`library/lean-step-side-read-opus.md`, author only, unchecked; check 1467 has not landed: no file
  `library/lean-step-side-read-check-astra62.md` at 95f65cd6f). Its ledger of floor clauses (READ there, not re-read yet):
  `FloorConditions (C c x)` at `ParametersOfARenormalizationStep.lean:127-154` (16 inequalities), `radius_ge` (131),
  `range_ge` (138), `floorMin = max yC 2^1600` (88), `clusterRange x = ceil(x^(1/100))`
  (`EffectiveDensityOfAStep.lean:14`), `boxRadius x = clusterRange x / 2^11` (33), the C used by the flow
  C = 2^40 L + 4 n0 + 2^17 (`ExpansionReturnsAtDrawnParametersProof.lean:30`), the second floor (2^14 L)^100
  (`GradientsOfTwoSettingsProof.lean:775`), (R40) `range_ge_side` (`AdmissionAtAStepForm.lean:12`).
  Its bound: every admissible g has g^-2 > (2^51 L)^100 and >= 2^1600.
- Row 1468 (`library/gap-k2-tool-design-fable.md` 5.1, 8): map Q2 (side 2, contour mean, vMF kernel strength a x);
  one-loop drift per side-2 step 0.2575 (SKETCHED there); order-one part step count ~ 3.88 (X - 2.3);
  X = 30-100 GUESSED as the best case for a small-field expansion with computed constants (5.1).

What this row must add: re-read the 16 clauses of FloorConditions (which bind, with what C), classify each as
structural or bookkeeping, then do the same for Balaban's small-field conditions, and give the smallest x for
each clause when exponents and constants are re-chosen.

