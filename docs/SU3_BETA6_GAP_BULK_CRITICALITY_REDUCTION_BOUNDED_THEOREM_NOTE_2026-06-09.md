# The SU(3) Lattice-Units Gap at β=6: Reduction to a Single Bulk-Criticality Premise

**Date:** 2026-06-09
**Claim type:** bounded_theorem (a conditional gap reduction + rigorous failure-mode classification) + a named open piece
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.py`](../scripts/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.txt`](../logs/runner-cache/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.txt)
(SCORECARD: PASS=17, FAIL=0)

> **Not claimed:** an unconditional `β=6` gap, a physical (continuum-units) SU(3)
> mass-gap theorem, any Clay-problem result, any `Λ_QCD` or observed-spectrum
> statement, or any physical Planck import. **Claimed:** a conditional reduction,
> in **lattice units**, for the pure-gauge `SU(3)` fundamental-Wilson system at
> fixed spacing, with every non-premise ingredient runner-verified.

---

## Role

The landed scope note
([`FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md`](FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md))
establishes fixed-lattice compact-gauge well-definedness and strong-coupling
area-law diagnostics for representative `SU(2)`/`U(1)` one-plaquette factors, and
explicitly does **not** prove a physical `SU(3)` gap at `β=6`. This note attacks
exactly that residual, in the only honest way short of a constructive-QFT
breakthrough: a **reduction theorem**. It also upgrades the group-theory content
from the representative `SU(2)`/`U(1)` factors to **actual `SU(3)`**, via exact
Weyl-measure quadrature.

Throughout, `β=6` is the framework's bare-coupling **convention**
(`g² = 2N/β = 1`), used only to locate the target coupling on the Wilson axis;
all gap statements are in lattice units at fixed spacing.

## (R1) The anchor — exact SU(3) strong-coupling confinement

By the Weyl integration formula, single-plaquette `SU(3)` class-function
integrals reduce to **exact 2D quadratures** over the eigenvalue angles with the
`|Δ|²` Haar class density — no Monte Carlo enters any computation in this note.
The runner verifies:

- the `SU(3)` character-norm convention `u(β) → β/18` as `β → 0`, matched to
  0.4% (a fails-if-false check of the measure and normalization);
- the leading string tension `σ_sc(β) = -\ln u(β) > 0` throughout the
  strong-coupling regime (`β ≤ 2`) — the Wilson-loop **area-law** diagnostic in
  the regime where the character/cluster expansion converges (the literature
  strong-coupling gap; Osterwalder–Seiler, Münster);
- `u(β)` increases monotonically toward weak coupling (a weakening-confinement
  diagnostic, not an all-coupling confinement claim).

## (R2) Finite-volume rigor at every coupling

The reflection-positive transfer matrix of the compact-group system is
**positivity-improving for every `β ∈ (0,∞)`** (strictly positive kernel), so
Perron–Frobenius gives a unique vacuum and `gap_L(β) > 0` pointwise; continuity
of `gap_L` in `β` on the **compact** interval `[0, 6]` then gives a strictly
positive minimum at every fixed volume (extreme-value theorem; demonstrated on
an explicit `β`-family of positivity-improving kernels). Consequence: the `β=6`
gap question lives **entirely in the infinite-volume limit**.

## (R3) Failure-mode classification — the heart of the reduction

In the infinite-volume limit the `0⁺⁺` lattice-units gap is `m(β) = 1/ξ(β)`. So:

- `m(6) = 0` **requires** `ξ(β*) → ∞` at some `β* ∈ (0, 6]` — by definition a
  **second-order bulk critical point** on the Wilson axis;
- a **first-order** bulk transition does **not** close the gap: `ξ` stays finite
  on both sides (latent-heat discontinuity, no divergence); the gap can jump but
  remains positive. (The known `SU(4)`, `SU(5)` bulk transitions are of this
  harmless first-order kind.)

**Conditional theorem.** *If no second-order bulk critical point lies on the 4D
`SU(3)` fundamental-Wilson axis in `(0, 6]`, then the strong-coupling gap (R1)
persists to `β = 6`: the lattice-units gap `m(β=6) > 0`.*

By (R2)+(R3) the hypothesis is the **complete** list of what could go wrong —
not one failure mode among several.

## (R4) The premise: status and falsifiability (comparators only)

For 4D `SU(3)` with the fundamental Wilson action, Monte Carlo studies across
decades and groups find **no bulk transition** on the axis — a finite crossover
(specific-heat bump near `β ≈ 5.5`, no volume-scaling divergence). The premise is
**falsifiable with a concrete signature**: a second-order bulk point would show a
divergent, volume-scaling specific-heat/correlation-length peak, never observed.
Direct comparator evidence for the gap itself: `a\sqrt{σ} ≈ 0.22`
(`σa² ≈ 0.048`) and `m_{0^{++}} a ≈ 0.8` at `β = 6.0`. All MC values are
comparators, not derivation inputs; the premise remains a premise.

## (R5) Why the window is genuinely hard (computed, not asserted)

- **Weak side:** the non-perturbative lattice scale
  `aΛ ∼ (b_0 g²)^{-b_1/2b_0²} e^{-1/(2 b_0 g²)}` (`≈ 2.3×10⁻³` at `g² = 1`,
  two-loop, pure-gauge `SU(3)` coefficients) **vanishes faster than every power
  of `g²`** as `g² → 0`: the gap is invisible to *all orders* of weak-coupling
  perturbation theory (verified numerically for `n = 1…7`).
- **Strong side:** the leading strong-coupling tension extrapolated to `β = 6`
  gives `σ_sc ≈ 0.86` versus the MC comparator `σa² ≈ 0.048` — an **18×**
  over-prediction. The expansion has genuinely broken down well below `β = 6`.

Neither expansion reaches `β = 6`. Closing the window **unconditionally** needs
RG-constructive (Balaban-class) control — the named open piece.

## Net

```text
m_lat(β=6) > 0  ⟸  [no 2nd-order bulk point on the SU(3) Wilson axis in (0,6]]
                    (the ONE premise; comparator-supported; falsifiable)
                AND [strong-coupling gap]          (R1 — exact SU(3) quadrature)
                AND [finite-volume gap ∀β]         (R2 — PF + compactness)
                AND [failure-mode classification]  (R3 — exhaustive)
```

The fixed-lattice `SU(3)` gap question at `β=6` is reduced to one sharp,
decades-tested, concretely-falsifiable bulk-criticality premise, with every other
ingredient rigorous and runner-verified. That is the maximal honest state short
of a constructive-QFT (Balaban-class) breakthrough, which remains open.

## What this note does NOT claim

- **Not** an unconditional `β=6` gap; **not** a physical-units mass-gap theorem;
  **not** a Clay result (no continuum limit is taken or needed at fixed spacing).
- **Not** an all-coupling confinement bridge; the premise is comparator-supported,
  not proven.
- **Not** a `Λ_QCD` derivation or observed-spectrum claim; the scale-reference
  primitive is a unit reference only and is not consumed here.
- **No** new axiom, primitive, vocabulary, or class tag; **no** PDG/fitted input
  consumed as a derivation input (`β=6 → g²=1` is the framework's bare-coupling
  convention, used to locate the target coupling).
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner; exact quadrature / linear algebra): the `SU(3)`
  Weyl-measure class integrals; `u(β)/β → 1/18`; `σ_sc(β) > 0` in strong
  coupling; monotone `u(β)`; the positivity-improving/Perron–Frobenius
  finite-volume gap family and its compact-interval positive minimum; the
  all-orders invisibility of `e^{-1/(2b_0g²)}`; the two-loop `aΛ` at `g²=1`; the
  18× strong-coupling breakdown factor at `β=6`.
- **Cited** (comparator/scope only): Osterwalder–Seiler *Ann. Phys.* 110 (1978)
  440; Münster (strong-coupling expansions); `SU(3)` MC crossover and
  `a\sqrt{σ}(β=6.0) ≈ 0.2189` (Necco–Sommer-class scaling studies); glueball
  `m_{0^{++}} a` at `β=6`; Balaban (UV-stability program — the named
  constructive route); Craig–Weinstein-style classification language is not
  needed: the second-order/first-order dichotomy is standard statistical
  mechanics.

## Dependencies

- [FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md](FIXED_LATTICE_GAUGE_EXISTENCE_STRONG_COUPLING_SCOPE_NOTE_2026-06-09.md)
  — the landed parent scope note whose named residual (no physical `SU(3)` gap at
  `β=6`) this note reduces; its fixed-lattice/non-continuum scope choice is used
  unchanged.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the structural `c_t = c_s` kinetic form of the regulator block (context for
  the hypercubic transfer construction; supplies no RP, confinement, or action).
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — axiom boundary
  only (the gauge action and `β=6` convention are the repo's existing imported
  gauge-sector context, not axiom content).

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
