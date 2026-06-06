# Charged-lepton r=1/2 is the Record-Native Readout (the Doublet Counted Once)

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. It writes no audit verdict and supplies no direct
effective-status change.
**Primary runner:**
[`scripts/frontier_koide_r_half_record_native_readout_2026_06_06.py`](../scripts/frontier_koide_r_half_record_native_readout_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_r_half_record_native_readout_2026_06_06.txt`](../logs/runner-cache/frontier_koide_r_half_record_native_readout_2026_06_06.txt)

---

## Role

The on-main 2026-06-05 record-generation cluster grounded the **partition** of the
charged-lepton generation carrier but left the **measure** explicitly open:

- [RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md):
  the `K`/CPT orbits of the C₃ carrier's central sectors are exactly two — a
  **SINGLET** `{χ₀}` (rank 1) and a **DOUBLET** `{χ₁,χ₂}` (rank 2; the faithful
  conjugate characters fused by `K`/CPT).
- [GENERATION_RECORD_PARTITION_SELECTOR_2026-06-05.md](GENERATION_RECORD_PARTITION_SELECTOR_2026-06-05.md):
  the native Record partition is uniquely `P0 | P1`, and (verbatim) "This does
  **not** select weights, probabilities, a Born measure, a time arrow, or a Koide
  value. ... The remaining gates are the **measure/arrow gates inside this
  two-sector partition**."
- [KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05.md](KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05.md):
  `Q = 1/3 + (2/3) r` exactly, with the singlet↔doublet swap `r → 1/(4r)` and
  fixed point `r = 1/2` (`Q = 2/3`).
- [FLAVOR_Q1_DEFAULT_RESTS_ON_PRR_NOTE_2026-05-30.md](FLAVOR_Q1_DEFAULT_RESTS_ON_PRR_NOTE_2026-05-30.md):
  localizes the open question exactly — "does the physical mass readout factor
  through the SO(2)/U(1)_b doublet-frame quotient — **counting the doublet once
  (1:1 → r=1/2)** — or use its full 2-real-dimensional content (**1:2 → r=1**)?"
  — and shows `r=1` (the trace/dimension answer) "rests entirely on the unaudited
  PRR premise" (full `U(3)` invariance), while only `C₃` is native.

This note **closes that measure gate** — not by *selecting* `r=1/2`, but by
identifying it as the **import-free, Record-native** readout. The framework's
logic is **probability (qubit) → record → durable state**: a value is *observed*
because it is **recorded**. `r=1/2` does not need to be forced; it needs to be a
**recordable** outcome, and it is in fact the one the bare record yields.

## The closure (runner SCORECARD 16/16 PASS)

The current Record axiom ([MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md))
states the realized outcome is the `K`/CPT orbit of the realized central sector,
that scalar readout is **finitely additive over pairwise-disjoint record
collections**, and that a record supplies **no weighting, normalization,
probability, or within-sector data**.

- The **doublet is one disjoint `K`/CPT-orbit collection** (rank 2). Because the
  Record axiom supplies **no within-sector data**, the record reads it as **one
  letter** — it has no access to the doublet's internal rank-2 / SO(2)/U(1)_b
  orientation.
- The determinant/measure that respects "additive over disjoint collections, no
  within-sector rank" is therefore the **block-count** `det_C(αP_s + βP_d) = αβ`
  (each collection once). Equivalently: the record-native readout **factors
  through the SO(2)/U(1)_b doublet-frame quotient** that
  `FLAVOR_Q1_DEFAULT_RESTS_ON_PRR` named as the decisive structural fork.
- **Block-count (1:1, doublet once) → equal block power → `r = 1/2` → `Q = 2/3`**
  (verified exactly). It is the fixed point of the label-swap `r → 1/(4r)`: the
  unique recordable value specifiable **without** an ordering or rank import.

So `r = 1/2` is the **import-free, Record-native** readout: the doublet counted
once, obtained with no input beyond the Record axiom and the (supplied) C₃
carrier.

## Teeth — `r = 1` is the import-dependent alternative

`r = 1` uses the **rank-weighted** `det_R(αP_s + βP_d) = αβ²` — the doublet
counted **twice**, by its dimension. That consumes the within-sector **rank
(=2)**, which is exactly the within-sector data the Record axiom **disclaims**.
Per `FLAVOR_Q1_DEFAULT_RESTS_ON_PRR`, the trace/Born answer `r=1` is privileged
**only** by full `U(3) = PRR` (unaudited, **non-native**; the only native
generation symmetry is `C₃`). So `r=1` is not record-native: it requires the
PRR / within-sector-rank import. (`r = 1/2` requires no such import.)

## What this is, and is not

- **Is:** a resolution of the measure gate `GENERATION_RECORD_PARTITION_SELECTOR`
  left open — the Record axiom's *no-within-sector-data* boundary counts the
  doublet **once**, so `r = 1/2` (`Q = 2/3`) is the **import-free record-native
  count**, and observing `Q = 2/3` for the charged leptons is therefore **not a
  fine-tuned selection** — it is what recording the two-sector carrier natively
  produces.
- **Is not** a claim that `r = 1` is impossible: it is the PRR/within-rank
  **import-dependent** alternative. The claim is the asymmetry — `r = 1/2`
  import-free, `r = 1` import-dependent.

## Honest residual

1. **Carrier supplied.** That the 3-generation carrier is the hw=1 C₃-corner
   regular representation is the framework's taste/generation provenance (the
   recurring chirality/staggered gate), supplied here as in the on-main cluster,
   not re-derived.
2. **The within-doublet phase δ is a separate residual.** `r` is the
   doublet/singlet **total-power** ratio (a collection-total quantity, which the
   record's additive readout supplies). The **splitting** of the doublet into two
   distinct masses (μ ≠ τ, the 3 distinct charged-lepton masses) is the
   within-doublet phase δ — genuinely within-sector data, **not** fixed here. So
   this note fixes the **count** `r = 1/2` (`Q = 2/3`), not the individual mass
   pattern.
3. **No Born weighting asserted.** The Record axiom disclaims probability; this
   note does not claim `r = 1/2` is the Born-dominant value (the dimension-Born
   weighting is exactly the `r = 1` import). It claims `r = 1/2` is the
   import-free record-native readout.

## Reprove-and-cite ledger

- **Reproven here** (exact sympy): `Q = 1/3 + (2/3) r` from the C₃-circulant
  eigenvalues (θ-independent); the two `K`/CPT orbits (singlet rank 1, doublet
  rank 2) via conjugation `χ₁ ↔ χ₂`; block-count (1:1) → `r=1/2` and
  rank/dimension (1:2) → `r=1`; `det_C = αβ`, `det_R = αβ²`; the swap `r→1/(4r)`
  fixed point `r=1/2`; the 2-collection entropy maximized at `r=1/2`.
- **Cited** (reused, not re-derived): the carrier + two-sector orbit count
  (`record_generation_readout_two_sectors`), the unique `P0|P1` partition
  (`generation_record_partition_selector`), `Q=1/3+(2/3)r`
  (`koide_circulant_value_derivation`), and the count-once-vs-twice / PRR
  localization (`FLAVOR_Q1_DEFAULT_RESTS_ON_PRR`). The Record axiom is cited from
  `MINIMAL_AXIOMS_2026-06-05`.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links so the audit
citation graph can track them. It does not promote this note or change any
audited claim scope.

- [RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md)
- [GENERATION_RECORD_PARTITION_SELECTOR_2026-06-05.md](GENERATION_RECORD_PARTITION_SELECTOR_2026-06-05.md)
- [KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05.md](KOIDE_CIRCULANT_VALUE_DERIVATION_2026-06-05.md)
- [FLAVOR_Q1_DEFAULT_RESTS_ON_PRR_NOTE_2026-05-30.md](FLAVOR_Q1_DEFAULT_RESTS_ON_PRR_NOTE_2026-05-30.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
