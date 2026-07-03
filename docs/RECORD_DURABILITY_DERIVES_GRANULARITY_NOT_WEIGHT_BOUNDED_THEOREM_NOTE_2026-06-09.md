# Record Durability Derives the Orbit Granularity — and Does Not Fix the Weight

**Date:** 2026-06-09
**Claim type:** bounded_theorem (a conditional derivation + a sharp negative boundary);
the companion MAXENT-R runner is support-only and does not adopt a premise.
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_record_durability_coarse_preference_2026_06_09.py`](../scripts/frontier_record_durability_coarse_preference_2026_06_09.py)
(SCORECARD: PASS=11, FAIL=0; cached:
[`logs/runner-cache/frontier_record_durability_coarse_preference_2026_06_09.txt`](../logs/runner-cache/frontier_record_durability_coarse_preference_2026_06_09.txt))
**Companion runner (candidate-relocation support):**
[`scripts/frontier_orbit_occupancy_maxent_relocation_2026_06_09.py`](../scripts/frontier_orbit_occupancy_maxent_relocation_2026_06_09.py)
(SCORECARD: PASS=16, FAIL=0; cached:
[`logs/runner-cache/frontier_orbit_occupancy_maxent_relocation_2026_06_09.txt`](../logs/runner-cache/frontier_orbit_occupancy_maxent_relocation_2026_06_09.txt))

> **The question answered:** can the occupancy admission be skipped by deriving
> the coarse-cell preference from record **durability**? Answer: **half yes,
> half no.** In a supplied K/CPT-covariant readout context, durability
> **derives the granularity half**: durable central record labels are orbit
> labels. This supports the existing Record orbit wording; it does not rewrite
> the axiom or supply registration dynamics. But durability **does not fix the
> weight half**: an explicit family of perfectly durable registration processes
> realizes both endpoint cells and intermediate weights. MAXENT-R remains only
> a candidate support principle in the companion runner, not an adopted
> admission here.

---

## D1 (positive): durability + CPT-covariance ⟹ orbit granularity

On the doublet sector pair, the **central classical sector-label algebra**
has a one-dimensional K-invariant subalgebra: labels satisfying `x₁=x₂`,
i.e. functions of the orbit label. Every sampled K-covariant registration
channel gives identical K-invariant orbit readout on `e₁` and `e₂` (200
random channels, residual `0.0`). A sector-resolved register is K-frame-**variant**
(its content flips under the conjugation), while an orbit register is exactly
K-invariant — only orbit content is *"fixed once registered"* in the
frame-independent sense. Exact lattice CPT
([`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md)) supplies the K/CPT conjugation;
K/CPT-covariance of the registration channel is an explicit readout-context
condition, not a mechanism derived here.

**Theorem (conditional):** given CPT-covariant registration, durable
central record content = orbit content. The "coarse-cell preference" at the
**content** level is conditionally derived. This is a support theorem for the
Record axiom's orbit wording, not a replacement for the axiom and not a
registration-dynamics theorem.

## D2 (negative, sharp): durability does not constrain the weight

An explicit one-parameter family of registration processes — within-orbit
mixing (K-covariant), absorbing orbit-labeled registers, i.e. **perfectly
durable records throughout** — has standing record-weight ratio
`O_d/O_s = 1.000 → 1.400 → 2.000` as the pre-registration **source measure**
sweeps from outcome-fed to fiber-fed (computed). Both cells, and everything
between, are realized by fully durable registration. Durability constrains
*what is written*, not *how often each outcome's basin is fed*. This is the
source-measure residual exhibited dynamically; it does not depend on the
unlanded independence PR.

## D3: the net boundary, and the candidate relocation

- **Derived (new, conditional):** the granularity half of "preferred outcome" (D1).
- **Not derived from durability:** the weight half; its residual is exactly the
  **source-measure class**.
- **Candidate support only** (companion runner): **MAXENT-R** —
  *record statistics is the maximum-entropy ensemble over the registrable
  (outcome) alternatives at common stiffness.* One universal, prior
  (Jaynes-class), context-blind principle. The companion runner shows: (i) the
  entire inter-cell factor 2 is the fiber count of the 2:1 sector→orbit map
  (two independent bookkeepings, exact); (ii) MAXENT-R in a Dirac context
  yields the landed holomorphic cell (`r=1/2, Q=2/3`); (iii) in a K-fixed
  (Majorana) context the coefficient is forced real and the **same** principle
  yields the landed sector cell (`r=1, Q=1`) — it reproduces **both** realized
  cells with zero per-context choices and **voluntarily outputs `Q=1` where
  structure dictates**, which a post-hoc rule tuned to lepton data would never
  do; (iv) the sector-side alternative requires counting provably unregistrable
  distinctions as alternatives, equipped with a Liouville-class measure that is
  **not retained** on generation space.

**Answer to "can we just skip the admission?": no.** This note lands the
conditional granularity theorem and the durability-does-not-fix-weight
boundary. If MAXENT-R is later adopted after owner review, the residual would
shrink to "statistics lives on registrable alternatives"; that adoption is not
made here.

## No-Go Discipline Boundary

**Status:** PASS for the local negative claim only: durability by itself does
not select the occupancy weight.

- **N1 — Alternative routes.** Five routes were separated: central
  K-invariant labels (closes granularity only); outcome-fed durable source
  measure (weight ratio 1); fiber-fed durable source measure (weight ratio 2);
  intermediate durable source measures (intermediate ratios); and additional
  source-measure principles such as MAXENT-R or Liouville (outside durability
  alone).
- **N2 — Wall independence.** Durability/orbit labeling and source-measure
  choice are independent: the D2 family changes source measure while preserving
  durable orbit-labeled records.
- **N3 — Hidden-wall scan.** K/CPT covariance of registration and the
  pre-registration source measure are explicit premises; no measurement
  dynamics, probability rule, or weighting rule is supplied by Record.
- **N4 — Residual matching.** The residual is only "durability-alone weight
  selection." This note does not claim to settle future source-measure
  principles.
- **N5 — Rhetoric audit.** "Does not fix" means "does not fix by durability
  alone in a K/CPT-covariant record context," not "no weighting principle can
  ever be adopted or derived."
- **N6 — Partial-closure path scan.** MAXENT-R is explicitly left as a
  candidate closure path; no new axiom, primitive, or admission is adopted here.
- **N7 — Steelman.** A stronger dynamical theory of registration might select a
  source measure. This note leaves that route open and only blocks the claim
  that durability itself already does the selection.
- **N8 — Cross-cycle echo.** The result is consistent with the nonexclusive
  occupancy-cell context, but does not rely on unlanded independence-branch
  authority.

## What this note does NOT claim

- **Not** an unconditional derivation of the occupancy weight; the D2 family
  shows durability by itself does not select the source measure.
- **Not** adoption of MAXENT-R (candidate for re-panel; the Jaynes-vs-Liouville
  choice is *supported* by the retained-status asymmetry — outcome algebra at
  axiom grade, no retained Liouville measure on generation space — but
  supported is not derived).
- D1 is conditional on **CPT-covariant registration**; the CPT note supplies
  exact lattice CPT, and registration dynamics as such remains the open gate.
- **No** comparator consumed; **no adopted** new axiom, primitive, admission,
  vocabulary, or class tag. It does **not** set or change any audit status.

## Dependencies

- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the durability
  clause and the orbit wording (D1 is a conditional support theorem relating
  durability, K/CPT covariance, and orbit labels).
- [CPT_EXACT_NOTE.md](CPT_EXACT_NOTE.md) — exact lattice CPT (the
  source of the K/CPT conjugation used in D1; registration covariance remains
  an explicit readout-context condition).
- [KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  — the landed cells (the targets of the relocation map).
- [OCCUPANCY_NONEXCLUSIVITY_MIXTURE_BOUND_NOTE_2026-06-09.md](OCCUPANCY_NONEXCLUSIVITY_MIXTURE_BOUND_NOTE_2026-06-09.md)
  — landed context for nonexclusive realized cells. The orbit-occupancy
  independence branch is in-flight context only and is not a dependency here.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
