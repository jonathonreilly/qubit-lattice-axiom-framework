# Occupancy Non-Exclusivity: the Mixture Bound, Per-Context Realization, and the Availability-Preference Formulation

**Date:** 2026-06-09
**Claim type:** open_gate
**Type:** bounded support: charged-lepton mixture bound plus a candidate
availability-preference formulation
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_occupancy_nonexclusivity_mixture_bound_2026_06_09.py`](../scripts/frontier_occupancy_nonexclusivity_mixture_bound_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_occupancy_nonexclusivity_mixture_bound_2026_06_09.txt`](../logs/runner-cache/frontier_occupancy_nonexclusivity_mixture_bound_2026_06_09.txt)
(SCORECARD: PASS=16, FAIL=0)

---

## The question

Could `r = 1/2` be a valid, even preferred, outcome that is recorded
frequently **without globally excluding** `r = 1`? Three precise answers.

## 1. Within One Readout Context: Mixture Is Measurable

If a fraction `(1-p)` of the record statistics in the charged-lepton context
carried sector-counting, the effective ratio mixes under the variance-linear
model (assumption flagged; any convex interpolation from the orbit cell toward
the sector cell has the same upward sign):

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

So within the charged-lepton context, a sector-cell admixture is constrained
below the `10^-5` level under this mixture model. That is an **empirical
charged-lepton-context bound**, not an axiom and not an assumption of the
program.

## 2. Across Contexts: No Global Exclusion Is Claimed

The framework should not be read as globally excluding the sector cell just
because the charged-lepton context is tightly orbit-cell-like. The clean
context-local statement is:

- the **sector cell** (`r=1`) is the direct cell for K-fixed (Majorana)
  multiplets, where the orbit cell is structurally **unavailable** (no
  K-invariant complex structure on the K-fixed locus; rung 0 of the neutrino
  program);
- the **orbit cell** (`r=1/2`) is empirically realized in the charged-lepton
  (Dirac) context, to `10⁻⁵`.

Thus `r=1/2` and `r=1` remain valid cells of the framework. What is empirically
exclusive is the charged-lepton context's observed mixture, not the global
space of possible readout contexts.

## 3. Candidate Preferred-Outcome Wording: Availability Preference

> **The orbit (coarser) cell is realized wherever it is available; the sector
> cell is realized where the orbit cell is structurally unavailable (K-fixed).**

This is a candidate abstract wording for the open orbit-occupancy program, not
a new axiom, primitive, or admission. It says both cells are legitimate direct
cells of the same framework, while availability is a structural fact decided by
the readout context. It matches the charged-lepton orbit-cell case and the
conditional K-fixed sector-cell case without adding per-context freedom.

The retirement target remains open: derive the **preference for the coarser
cell from record dynamics** (coarser outcome ↔ more durable registration) at
the measurement/record-production gates. This note only names that target and
does not derive it.

## What this note does NOT claim

- **Not** a derivation of the preference (named open target); **not** a Tier-A
  admission, primitive, or registry change; **not** a mass prediction.
- The mixture-linearity assumption is flagged; only the sign conclusion is
  robust for convex mixtures between the orbit and sector cells.
- Within-context exclusivity is empirical, not axiomatically forbidden: a
  future context exhibiting a genuine mixture would be a discovery about its
  record statistics, not a contradiction.
- **No** comparator (PDG masses/uncertainties) is used to derive the framework
  rule. The comparators are load-bearing only for the charged-lepton empirical
  mixture bound. This note does **not** set or change any audit status.

## Dependencies

- [KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  — the landed cells.
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the K/CPT-orbit
  Record wording.
- [ORBIT_OCCUPANCY_NEUTRINO_OUT_OF_SAMPLE_PROGRAM_NOTE_2026-06-09.md](ORBIT_OCCUPANCY_NEUTRINO_OUT_OF_SAMPLE_PROGRAM_NOTE_2026-06-09.md)
  — the landed neutrino-sector open program and K-fixed conditional sector-cell
  context.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
