# P-REC Spin/Taste Clifford Core + Consumer-Reframe Partial Unlock of the 1105 Cone (Deps-All-Retained, Keystone-Decoupled, Bounded Theorem)

**Date:** 2026-06-20
**Type:** bounded_theorem + consumer-reframe
**Claim type:** bounded_theorem
**Status:** source-note proposal awaiting independent audit handling. Status
authority is the independent audit lane only; this note asserts no audit verdict
and claims no "retained"/"promoted" standing. **Audit-readiness purpose:** its
load-bearing dependencies are all retained-grade, so the row is deps-all-retained
("ready"), and it does **not** route through the unaudited keystone
`anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
or its parent `anomaly_forces_time_theorem` (both kept CONTEXT-ONLY).
**Primary runner:**
[`scripts/frontier_abj_prec_spin_taste_clifford_core_bank_2026_06_20.py`](../scripts/frontier_abj_prec_spin_taste_clifford_core_bank_2026_06_20.py)
(**TOTAL: PASS=40 FAIL=0**, explicit per-check residuals ~1e-15).
**Cached runner output:**
[`logs/runner-cache/frontier_abj_prec_spin_taste_clifford_core_bank_2026_06_20.txt`](../logs/runner-cache/frontier_abj_prec_spin_taste_clifford_core_bank_2026_06_20.txt)

This note follows the decoupling precedent of
[`SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08.md`](SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08.md):
the load-bearing facts are **reproven in-tree from retained anchors**, so the
result is auditable on its own without the unaudited keystone in its dependency
path.

## Why this note exists (audit-unblock)

Wall **P-REC** was the highest-value identification wall on the ABJ B-axis: the
staggered-ε carrier → spacetime `γ₅` identification was said to require a
**single-taste selector**, because the free staggered algebra carries a full
`M₄(C)` taste symmetry and picking one taste/Dirac factor is selector-dependent
(registered data unless derived; root authority
[`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`](NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md)).

This note banks two things, both recomputed in-tree:

1. the **spin/taste Clifford core** on the blocked even `2⁴` carrier — the
   taste-singlet chirality operator `Γ₅^spin`; and
2. the **consumer-reframe partial unlock** — the keystone consumer edge
   B4 → B5/EVEN → B6 (chirality + even dimension) is discharged by
   `γ₅`-**existence alone**, so no single-taste / irreducible selector is needed
   by the consumer.

## Premises

- **(Axiom)** The `{Lattice, Quantum, Record}` baseline (A_min):
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md). Three spatial
  axes `d_s = 3` are A_min content; the blocked staggered carrier is the
  `2⁴` hypercube vertex space.
- **(R1, retained)** Clifford volume-chirality even-dimension parity law:
  [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  (`positive_theorem` / **retained**). A volume-chirality operator
  anticommuting with all generators and squaring to `+I` exists iff the total
  Clifford dimension `n` is even. **Recomputed in runner Part B(i)/C2**, not cited
  blind.
- **(R2, retained_no_go, scope-noted M₂(C)-only)** No per-site chirality:
  [`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`](NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md)
  (`no_go` / **retained_no_go**). The per-site qubit space `M₂(C)` admits no
  volume-chirality of the four anticommuting generators. **Not collided** here
  (runner Part C1): `Γ₅^spin` lives in the `2⁴` doubled carrier, not per-site.
- **(R3, retained_bounded, verify)** Free staggered-Dirac 2-point SO(4)
  spin⊗taste factorisation:
  [`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  (`bounded_theorem` / **retained_bounded**). The free staggered carrier
  factorises as `spin ⊗ taste` with the taste `M₄(C)` as a spectator.
  **Verified** in runner Part C3 (carrier dim `16 = spin 4 × taste 4`); its own
  runner re-checked PASS=54.
- **(Carrier, CONTEXT-ONLY)** The Kawamoto-Smit staggered carrier
  (`audited_conditional`) is kept context-only; **no single-taste is admitted**.

## Statement and result

**Theorem (bounded).** On the blocked even `2⁴` staggered carrier with the
canonical staggered phases `η_μ(b) = (-1)^{Σ_{ν<μ} b_ν}`:

1. **Spin/taste Clifford core.** The blocked staggered generators `α_μ`
   (`μ = 0..3`) satisfy `{α_μ, α_ν} = 2 δ_{μν}` (Cl₄), and the volume element
   `Γ₅^spin = α₀ α₁ α₂ α₃` is a **taste-singlet chirality operator**:
   `(Γ₅^spin)² = +I`, `{Γ₅^spin, α_μ} = 0` for all `μ` (residuals ~1e-15), and
   `Γ₅^spin` commutes with all of the `M₄(C)` taste commutant. So `Γ₅^spin` is a
   **single chirality object valid for every taste — no taste is selected.**

2. **Consumer-reframe partial unlock (the KEY RESULT, recomputes block02 PR-A,
   PASS=35).** The keystone consumer edge **B4 → B5/EVEN → B6** (a chirality
   operator must exist; it exists iff `n = d_s + d_t` is even) is **discharged by
   `γ₅`-EXISTENCE alone**:
   - **(parity-of-`n`, irreducible-rep-INDEPENDENT)** the anticommutant-nullity
     existence verdict is nonzero iff `n` is even, and this verdict is
     **identical** on the irreducible Clifford rep and on reducible
     multiplicity-`m` carriers (`n = 2..6`, `m = 1,2,4`). The decisive-failure
     probe found **no** reducibility flip (Part B(i)); had one existed the reframe
     fails.
   - **(taste-dial-INVARIANT)** both consumed quantities — `γ₅`-existence and the
     representative chirality-graded anomaly trace — are **invariant across all
     four `M₄(C)` taste sectors** (existence residual 3.3e-15; per-sector trace
     spread 9.5e-16; each sector = ¼ the full taste-summed trace; Σ sectors =
     full).

Therefore the single-taste / irreducible-Dirac-factor selection that P-REC was
admitting is a **within-sector dial, not load-bearing** for the B4/B5/B6 edge.
**No single-taste / irreducible selector is needed for the 1105 consumer.**

## What this is — and what it is NOT

- **This IS a PARTIAL UNLOCK of the 1105 cone (the B4/B5/B6 chirality +
  even-dimension edge):** that edge is discharged from A_min + the taste-singlet
  core + the three retained deps, with **no new axiom, no new primitive, and no
  single-taste admission**.
- **This is NOT a derivation of the single-taste selector.** The single-taste /
  irreducible selection wall **stays walled as a supplier statement** — but it is
  **moot for the consumer**, because the consumer needs only `γ₅`-existence
  (parity-of-`n`), which the taste-singlet `Γ₅^spin` already supplies.
- **Scope fence (honest).** The unlock is the B4/B5/B6 edge ONLY. It does **not**
  touch P-ABJ (B2 external admission; `χ≠0` only on admitted curved geometry while
  A_min is flat-cubic), P-COMP (B3 RH-completion existence; Hamming-odd =
  vectorlike fiber-flip), or P-HY (the "is-gauged" predicate). The `d_t = 1` pin
  still needs SC/(B-AXIS). The result holds **invariantly over the entire `M₄(C)`
  law-admissible taste family**, so it is a derivation of **unnecessity**, not
  realized-state-dependent registered data.

## Honest forced / admitted / convention ledger

- **F1 (forced).** The taste-singlet `Γ₅^spin` exists on the `2⁴` carrier and
  satisfies the B4/B5 existence predicate (Part A, residuals ~1e-15).
- **F2 (forced).** `γ₅`-existence is parity-of-`n` only and irrep-independent
  (Part B(i), no reducibility flip); the consumed quantities are taste-dial-
  invariant (Part B(ii)).
- **A1 (admission left standing).** The single-taste / irreducible selector is
  **not derived**; it remains a walled supplier statement. The unlock works by
  making it **unnecessary for the consumer**, not by cracking it.
- **C1 (context-only).** The Kawamoto-Smit carrier (`audited_conditional`) and the
  keystone/parent are kept context-only; no single-taste is admitted.

## Reprove-and-cite (source discipline)

- The spin/taste core, the parity law, and the taste-dial invariance are all
  **recomputed in-tree** by the primary runner (PASS=40), not asserted by name.
- **Retained deps recomputed/verified, not cited blind:** R1 (Part B(i)/C2),
  R2 non-collision (Part C1), R3 spin⊗taste factorisation (Part C3).
- **Absorbed (cited by path + PASS, NOT rebuilt):**
  - block01 P-REC core
    [`scripts/frontier_abj_prec_r4_taste_reconstruction_2026_06_20.py`](../scripts/frontier_abj_prec_r4_taste_reconstruction_2026_06_20.py)
    (PASS=43) — the original `Γ₅^spin` residual-0 construction; **re-derived
    verbatim in Part A** so the bank holds without importing it as a load-bearing
    fact.
  - block02 consumer-reframe
    [`scripts/frontier_abj_prec_consumer_reframe_2026_06_20.py`](../scripts/frontier_abj_prec_consumer_reframe_2026_06_20.py)
    (PASS=35) — the original B4/B5/B6 reframe; **its KEY RESULT is recomputed in
    Part B.**
- **Keystone-decoupled:**
  `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
  (keystone, unaudited) and `anomaly_forces_time_theorem` (parent, unaudited) are
  **CONTEXT-ONLY** — never inputs; every load-bearing fact is recomputed (Part C4).

## Forbidden-imports check

No PDG values, fitted selectors, or literature numerical comparators are used as
derivation inputs. The Clifford/anticommutant facts are reproven in-runner; the
staggered phases and spin⊗taste structure are A_min/retained content. No new axiom
or primitive is introduced and no numerical prediction is changed.
