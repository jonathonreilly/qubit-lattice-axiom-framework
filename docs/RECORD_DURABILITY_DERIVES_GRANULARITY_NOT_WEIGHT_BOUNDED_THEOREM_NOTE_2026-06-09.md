# Record Durability Derives the Orbit Granularity — and Provably Not the Weight

**Date:** 2026-06-09
**Claim type:** bounded_theorem (a conditional derivation + a sharp negative boundary) + a companion relocation
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_record_durability_coarse_preference_2026_06_09.py`](../scripts/frontier_record_durability_coarse_preference_2026_06_09.py)
(SCORECARD: PASS=11, FAIL=0; cached:
[`logs/runner-cache/frontier_record_durability_coarse_preference_2026_06_09.txt`](../logs/runner-cache/frontier_record_durability_coarse_preference_2026_06_09.txt))
**Companion runner (the relocation half):**
[`scripts/frontier_orbit_occupancy_maxent_relocation_2026_06_09.py`](../scripts/frontier_orbit_occupancy_maxent_relocation_2026_06_09.py)
(SCORECARD: PASS=16, FAIL=0; cached:
[`logs/runner-cache/frontier_orbit_occupancy_maxent_relocation_2026_06_09.txt`](../logs/runner-cache/frontier_orbit_occupancy_maxent_relocation_2026_06_09.txt))

> **The question answered:** can the occupancy admission be skipped by deriving
> the coarse-cell preference from record **durability**? Answer: **half yes,
> half provably no.** Durability (+ retained exact CPT) **derives the
> granularity half** — durable registrable content is exactly the orbit
> functions, so the Record axiom's 2026-06-05 orbit clause is *forced by its own
> durability clause* rather than stipulated. But durability **provably cannot
> fix the weight half**: an explicit family of perfectly durable registration
> processes realizes every occupancy between the two cells. The weight admission
> survives (as the independence theorem requires) and relocates, at best, into
> one universal principle (MAXENT-R, companion runner).

---

## D1 (positive): durability + CPT-covariance ⟹ orbit granularity

On the doublet sector pair, the commutant of the K-swap is `span{1, K}` — the
algebra of **orbit functions** (computed). Every K-covariant registration
channel responds to `e₁` and `e₂` with mirror-identical statistics: **sector
distinguishability is exactly zero** (200 random channels, residual `0.0`). A
sector-resolved register is K-frame-**variant** (its content flips under the
conjugation), while an orbit register is exactly K-invariant — only orbit
content is *"fixed once registered"* in the frame-independent sense the
axiom's durability clause requires. Since the framework retains **CPT as exact
on the lattice** ([`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md)), K-covariance of
registration is a retained-grade hypothesis, not a new import.

**Theorem (conditional):** given CPT-covariant registration, durable
registrable content = orbit functions. The "coarse-cell preference" at the
**content** level — and with it the 2026-06-05 orbit refinement of the Record
axiom — is **derived**, not admitted.

## D2 (negative, sharp): durability does not constrain the weight

An explicit one-parameter family of registration processes — within-orbit
mixing (K-covariant), absorbing orbit-labeled registers, i.e. **perfectly
durable records throughout** — has standing record-weight ratio
`O_d/O_s = 1.000 → 1.400 → 2.000` as the pre-registration **source measure**
sweeps from outcome-fed to fiber-fed (computed). Both cells, and everything
between, are realized by fully durable registration. Durability constrains
*what is written*, not *how often each outcome's basin is fed*. This is the
independence theorem (PR #3400) exhibited dynamically — as it must be: no
durability argument can beat a proven independence.

## D3: the net boundary, and the relocation

- **Derived (new):** the granularity half of "preferred outcome" (D1).
- **Not derivable (proven):** the weight half; its residual is exactly the
  **source-measure class**.
- **The minimal true core of the admission** (companion runner): **MAXENT-R** —
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

**Answer to "can we just skip the admission?": no — proven; but it shrinks to
its minimal universal core.** After this note the admission is no longer
"pick the Koide cell"; it is "statistics lives on registrable alternatives"
(MAXENT-R), with the granularity half upgraded to a conditional theorem and
the Jaynes-vs-Liouville residual named and flagged.

## What this note does NOT claim

- **Not** an unconditional derivation of the occupancy weight (impossible from
  the current surface; D2 + the independence theorem).
- **Not** adoption of MAXENT-R (candidate for re-panel; the Jaynes-vs-Liouville
  choice is *supported* by the retained-status asymmetry — outcome algebra at
  axiom grade, no retained Liouville measure on generation space — but
  supported is not derived).
- D1 is conditional on **CPT-covariant registration**; the CPT note supplies
  exact lattice CPT, and registration dynamics as such remains the open gate.
- **No** comparator consumed; **no** new axiom, primitive, admission,
  vocabulary, or class tag. It does **not** set or change any audit status.

## Dependencies

- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the durability
  clause and the orbit wording (D1 derives the latter from the former + CPT).
- [CPT_EXACT_NOTE.md](CPT_EXACT_NOTE.md) — exact lattice CPT (the
  retained-grade covariance hypothesis of D1).
- [KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  — the landed cells (the targets of the relocation map).
- `KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`,
  `OCCUPANCY_NONEXCLUSIVITY_MIXTURE_BOUND_NOTE_2026-06-09.md`
  (plain-text context references; in review as PRs #3400/#3408).

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
