# The Orbit-Occupancy Out-of-Sample Program: the Neutrino Sector as the Second Multiplet

**Date:** 2026-06-09
**Claim type:** bounded prediction-program note (a structural rung-0 dichotomy + a flagged rung-1 band) with registered kill conditions
**Type:** open_gate / prediction program
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_orbit_occupancy_neutrino_out_of_sample_2026_06_09.py`](../scripts/frontier_orbit_occupancy_neutrino_out_of_sample_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_orbit_occupancy_neutrino_out_of_sample_2026_06_09.txt`](../logs/runner-cache/frontier_orbit_occupancy_neutrino_out_of_sample_2026_06_09.txt)
(SCORECARD: PASS=17, FAIL=0)

> **Why this note exists.** A six-lens adversarial panel unanimously classified
> the orbit-occupancy premise as **Tier-A admission territory, not primitive**,
> with a named upgrade trigger: *use-novel corroboration — a second, independent
> multiplet readout constrained by the same counting rule, confirmed
> out-of-sample.* This note builds that program on the neutrino sector, where the
> rule has unavoidable structural content, and registers the **kill conditions as
> prominently as the predictions**. The upgrade trigger is **not met today**;
> this note creates the falsifiable stakes that future data will decide.

---

## The anchor (comparators, labeled)

The charged-lepton anchor is re-fit from PDG masses by exact circulant
inversion: `Q_l = 0.666661` (6×10⁻⁶ from 2/3), `r_l = 0.499991`,
`δ_l = 0.22223 ≈ 2/9`, with reconstruction residual `7×10⁻¹⁵`. The landed fork
cells (Majorana/real → `Q=1`; Dirac/holomorphic → `Q=2/3`) are encoded verbatim
(the #3138 guard).

## Rung 0 — the structural dichotomy (no knobs)

Conjugation maps `J → −J`, so the K-fixed locus of the generation doublet
carries **no invariant complex structure**: a **Majorana** (K-fixed) multiplet
*cannot* occupy the complex slot and is **forced onto the sector cell**
(`r=1, Q=1`) — this is the landed Majorana–Berezin cell, cross-checked, not
re-derived loosely. A plain-Dirac multiplet with the standard circulant readout
sits on the orbit cell (`Q=2/3`). **No free parameters.**

## The empirical exclusion band (oscillation comparators only)

For **any** absolute mass scale and either ordering, the neutrino Koide ratio is
bounded by the measured splittings:

```text
    Q_ν ≤ 0.586 (normal ordering),   Q_ν ≤ 0.500 (inverted)
```

— so **both** direct-readout cells (`Q=1` and `Q=2/3`) are **excluded** for
neutrinos.

## Rung-0 prediction (out-of-sample, no model imports)

**Orbit-occupancy + oscillation data ⟹ the neutrino mass readout is *not* the
direct charged-lepton-type context: the neutrino mass operator is structurally
different — composite (seesaw-class) and/or Majorana.**

- **Kill condition K1 (registered):** a conclusive plain-Dirac *elementary*
  neutrino mass with a standard generation readout falsifies the rule outright.
  The Majorana horn is what `0νββ`-class experiments (LEGEND-1000, nEXO) decide.

## Rung 1 — minimal seesaw (two imports, flagged) → a sharp `Σm_ν` band

**Imports (flagged, not framework theorems):** minimal seesaw `m_ν = m_D²/M_R`
with **degenerate** `M_R`; the orbit rule applied to the Dirac block. Then
`√m_ν ∝ λ²` with `λ` the `r=1/2` circulant eigenvalues, giving the **derived
closed form** (symbolic + 12-point numeric certification):

```text
    Q_ν(δ_ν) = (25.5 + 6√2 cos 3δ_ν)/36  ∈  [0.4726, 0.9440]
```

Consequences, intersected with the data band:

1. **`δ_ν ≠ δ_l` is forced:** `δ_ν = 2/9` gives `Q_ν = 0.894`, excluded — the
   rule requires the neutrino Koide phase to differ from the charged-lepton one.
2. **Normal ordering strongly preferred** (the inverted-ordering window is a
   sliver at its edge), with `m₁ ≤ 1.6 meV` and

```text
    Σm_ν = 0.059 – 0.061 eV
```

   — the minimal-NO value, sitting exactly at the resolution frontier of
   DESI/CMB-S4-class cosmology. This is a **use-novel number**: it is not yet
   measured, and upcoming data will decide it.

- **Kill conditions K2/K3 (registered):** inverted ordering confirmed, or
  `Σm_ν > ~0.065 eV`, kills rung 1; any `Q_ν` determination outside
  `[0.473, 0.586]` kills rung 1.

## Quark survey (honesty appendix)

Computed for all six charge-sector triples (MS-bar comparators): `(c,b,t)` sits
`0.28%` from `2/3`; every other triple is far (`≥ 6%`). Recorded **with the
post-hoc flag**: selecting the matching triple after the fact on
scheme-dependent masses is precisely the failure mode the panel punished —
supportive-at-best, **not** corroboration, and no framework mechanism currently
singles out that triple.

## Program status

- **Upgrade path to primitive (the panel's trigger):** (i) cosmology resolving
  `Σm_ν ≈ 0.059 eV` with normal ordering (rung 1 confirmed), and/or (ii) `0νββ`
  establishing Majorana nature (the rung-0 horn) — use-novel corroborations of
  the same counting rule on a second multiplet.
- **Bust lines:** K1 (rule dies), K2/K3 (rung 1 dies; rule retreats to rung 0).
- **Meanwhile:** the unanimous panel classification stands — Tier-A admission
  territory, worded abstractly, with this note as part of its attached
  out-of-sample portfolio. Nothing here changes any audit status.

## What this note does NOT claim

- **Not** a measurement or confirmation: the trigger is unmet; the program is
  registered, the stakes are live.
- **Not** framework theorems at rung 1: minimal seesaw and degenerate `M_R` are
  flagged model imports; rung 0 alone is import-free.
- **Not** quark corroboration (post-hoc flag above).
- **No** PDG/oscillation value used as a derivation input (all comparators
  labeled); **no** new axiom, primitive, admission, vocabulary, or class tag.
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner): the exact circulant inversion of the
  charged-lepton anchor (`Q_l`, `r_l`, `δ_l`, residual `7×10⁻¹⁵`); the
  `J → −J` / K-fixed-locus structural step; the `Q_ν` exclusion band over the
  full absolute-scale range, both orderings; the closed form
  `Q_ν(δ) = (25.5+6√2\cos3δ)/36` (symbolic + 12-point certification); the
  `δ_ν ≠ δ_l` exclusion; the `m₁`/`Σm_ν` viability band; the IO sliver; the
  six-triple quark survey.
- **Cited:** the landed fork note
  ([`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md))
  for the cells; `KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`
  and `KOIDE_R_POLARIZATION_ORBIT_QUOTIENT_GATE_SHARPENING_NOTE_2026-06-09.md`
  (plain-text context references; in review as PRs #3400/#3397); PDG masses and
  NuFIT-class oscillation splittings as labeled comparators; seesaw (Minkowski;
  Gell-Mann–Ramond–Slansky) as the flagged rung-1 import.

## Dependencies

- [KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  — the landed cells (rung 0's ground truth).
- [KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
  — the `Q`-lever.
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the K/CPT-orbit
  Record wording (rung 0's K-fixedness step).

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
