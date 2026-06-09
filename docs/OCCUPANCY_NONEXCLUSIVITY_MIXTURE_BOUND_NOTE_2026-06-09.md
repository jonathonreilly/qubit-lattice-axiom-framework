# Occupancy Non-Exclusivity: the Mixture Bound, Per-Context Realization, and the Availability-Preference Formulation

**Date:** 2026-06-09
**Claim type:** bounded support (a computed mixture bound + a reformulation of the existing admission)
**Type:** open_gate / support
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_occupancy_nonexclusivity_mixture_bound_2026_06_09.py`](../scripts/frontier_occupancy_nonexclusivity_mixture_bound_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_occupancy_nonexclusivity_mixture_bound_2026_06_09.txt`](../logs/runner-cache/frontier_occupancy_nonexclusivity_mixture_bound_2026_06_09.txt)
(SCORECARD: PASS=16, FAIL=0)

---

## The question

Could `r = 1/2` be a valid — even preferred — outcome that is recorded
frequently **without being exclusive** of `r = 1`? Three precise answers.

## 1. Within one readout context: non-exclusivity is a measurable number, and the data crushes it

If a fraction `(1-p)` of the record statistics in the charged-lepton context
carried sector-counting, the effective ratio mixes (variance-linear mixing —
assumption flagged; the *sign* of the conclusion is aggregation-independent):

```text
    Q(p) = 2/3 + (1-p)/3        — any sector admixture pushes Q UP.
```

The data answers with a sign: `Q_PDG = 0.6666605` sits **below** `2/3`
(`Q - 2/3 = -6.2×10⁻⁶`), and the `m_τ` uncertainty gives `σ(Q) = 6.8×10⁻⁶`.
Since an admixture can only push up, the best-fit admixture is **exactly zero**
(at the boundary), with the one-sided 2σ bound

```text
    (1 - p)  <  2.2×10⁻⁵        — sector admixture below 0.002%.
```

So within the charged-lepton context, "recorded frequently alongside" is
excluded — exclusivity there is an **empirical fact at the 10⁻⁵ level**, not an
axiom and not an assumption of the program.

## 2. Across contexts: the instinct is exactly right — both cells ARE realized

The independence result (PR #3400) means the axioms fix no *global* occupancy
rule, so the rule is **per-readout-context** — global exclusivity was never the
claim. And both cells are physically realized in the existing program:

- the **sector cell** (`r=1`) is *forced* for K-fixed (Majorana) multiplets —
  the orbit cell is structurally **unavailable** there (no K-invariant complex
  structure on the K-fixed locus; rung 0 of the neutrino program);
- the **orbit cell** (`r=1/2`) is empirically realized in the charged-lepton
  (Dirac) context, to `10⁻⁵`.

Non-exclusive across contexts; empirically exclusive within each.

## 3. "Preferred outcome," made precise: the availability-preference formulation

> **The orbit (coarser) cell is realized wherever it is available; the sector
> cell is realized where the orbit cell is structurally unavailable (K-fixed).**

One principle, no per-context freedom (availability is a structural fact decided
by K-fixedness), reproducing every realized case — and therefore exactly as
predictive as the rung-0 dichotomy, with a cleaner ontology: both cells are
legitimate outcomes of the same framework; *availability plus preference*
decides which is realized, with nothing excluded by fiat.

This is a **rewording of the same single admission** (the panel's Tier-A
verdict stands) — but arguably the better abstract wording for the Tier-A
entry, and it sharpens the retirement route: derive the **preference for the
coarser cell from record dynamics** (coarser outcome ↔ more durable
registration) at the measurement/record-production gates. Flagged as open, not
derived.

## What this note does NOT claim

- **Not** a derivation of the preference (named open target); **not** a change
  to the panel's Tier-A classification; **not** a mass prediction.
- The mixture-linearity assumption is flagged; only the sign conclusion is
  aggregation-independent.
- Within-context exclusivity is empirical, not axiomatically forbidden: a
  future context exhibiting a genuine mixture would be a discovery about its
  record statistics, not a contradiction.
- **No** comparator (PDG masses/uncertainties) is a derivation input. It does
  **not** set or change any audit status.

## Dependencies

- [KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  — the landed cells.
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the K/CPT-orbit
  Record wording.
- `KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`,
  `ORBIT_OCCUPANCY_NEUTRINO_OUT_OF_SAMPLE_PROGRAM_NOTE_2026-06-09.md`
  (plain-text context references; in review as PRs #3400/#3404).

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
