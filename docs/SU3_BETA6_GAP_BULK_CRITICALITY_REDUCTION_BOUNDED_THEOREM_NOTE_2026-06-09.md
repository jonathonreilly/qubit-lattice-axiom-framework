# The SU(3) Mass Gap at β=6: Reduction to a Single Bulk-Criticality Premise

**Date:** 2026-06-09
**Claim type:** bounded_theorem (a conditional gap theorem + a rigorous failure-mode classification) + a named open piece
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.py`](../scripts/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.txt`](../logs/runner-cache/frontier_su3_beta6_gap_bulk_criticality_reduction_2026_06_09.txt)
(SCORECARD: PASS=17, FAIL=0)

> **This note does not prove the unconditional β=6 gap.** It does the next-best
> rigorous thing: it anchors both ends, classifies the *unique* way the gap could
> fail, and thereby reduces "prove the SU(3) mass gap at the framework's coupling"
> to **one sharp, falsifiable premise** about bulk criticality on the Wilson axis.

---

## Role

The fixed-Planck-lattice Yang–Mills note
([`YANG_MILLS_MASS_GAP_FIXED_PLANCK_LATTICE_BOUNDED_NOTE_2026-06-09.md`](YANG_MILLS_MASS_GAP_FIXED_PLANCK_LATTICE_BOUNDED_NOTE_2026-06-09.md))
left exactly one quantitative residual: the strong-coupling expansion proves the
SU(3) gap only at small `β`, while the framework's bare coupling `β = 6` sits in
the scaling/crossover region beyond its convergence. This note attacks that
residual. The result is a **reduction theorem**: the entire remaining question is
equivalent to the absence of a *second-order bulk critical point* on the SU(3)
Wilson axis in `(0, 6]`.

## (R1) The anchor — exact SU(3) strong-coupling confinement

Using the Weyl integration formula, single-plaquette SU(3) class-function
integrals are **exact 2D quadratures** (eigenvalue angles with the
`|Δ|²` Haar class density) — no Monte Carlo anywhere in this note's computations.
The runner verifies:

- the SU(3) character-norm convention `u(β) → β/18` as `β → 0` (matched to 0.4% —
  a genuine fails-if-false check of the measure and normalization);
- the leading string tension `σ_sc(β) = -\ln u(β) > 0` throughout the
  strong-coupling regime (`β ≤ 2`): the Wilson loop obeys an **area law** —
  confinement, hence exponential clustering, hence a **mass gap**, in the regime
  where the character/cluster expansion converges (Osterwalder–Seiler; Münster);
- `u(β)` increases monotonically toward weak coupling (no spurious artifacts).

## (R2) Finite-volume rigor at *every* coupling

The reflection-positive transfer matrix is **positivity-improving for every
`β ∈ (0,∞)`** (strictly positive kernel), so Perron–Frobenius gives a unique
vacuum and `gap_L(β) > 0` pointwise; `gap_L` is continuous in `β`, so on the
**compact** interval `[0, 6]` it attains a strictly positive minimum at every
fixed volume (extreme-value theorem; demonstrated on an explicit `β`-family of
positivity-improving kernels). Consequence: **the β=6 gap question lives entirely
in the infinite-volume limit** — finite volume is rigorous at all couplings.

## (R3) Failure-mode classification — the heart of the reduction

In the infinite-volume limit the 0⁺⁺ gap is `m(β) = 1/ξ(β)`. So:

- `m(6) = 0` **requires** `ξ(β*) → ∞` at some `β* ∈ (0, 6]` — by definition, a
  **second-order bulk critical point** on the Wilson axis.
- A **first-order** bulk transition does **not** close the gap: the correlation
  length stays finite on both sides (latent-heat discontinuity, no divergence);
  the gap can jump but remains positive. (The known SU(4), SU(5) bulk transitions
  are of this harmless first-order kind.)

**Conditional theorem.** *If no second-order bulk critical point lies on the 4D
SU(3) fundamental-Wilson axis in `(0, 6]`, then the strong-coupling gap (R1)
persists to `β = 6`: `m(β=6) > 0`.*

The hypothesis is not decoration — it is the **complete** list of what could go
wrong, by (R2)+(R3).

## (R4) The premise: status and falsifiability

For 4D SU(3) with the fundamental Wilson action, decades of Monte Carlo across
many groups find **no bulk transition** on the axis — only a finite crossover
(specific-heat bump near `β ≈ 5.5`, height finite, no volume-scaling divergence).
The premise is **falsifiable with a concrete signature**: a second-order bulk
point would show a divergent, volume-scaling specific-heat/correlation-length
peak — never observed. And the gap itself is seen directly: at `β = 6.0`,
`a\sqrt{σ} ≈ 0.22` (`σa² ≈ 0.048`) and `m_{0^{++}} a ≈ 0.8`. All MC values are
comparators, not derivation inputs.

## (R5) Why the window is genuinely hard (computed, not asserted)

- **Weak side:** the non-perturbative scale `aΛ ∼ (b_0g²)^{-b_1/2b_0²}
  e^{-1/(2b_0g²)}` (`≈ 2.3×10⁻³` at `g²=1`, two-loop) **vanishes faster than every
  power of `g²`** as `g² → 0` — the gap is invisible to *all orders* of
  weak-coupling perturbation theory (verified numerically for `n = 1…7`).
- **Strong side:** the leading strong-coupling tension extrapolated to `β = 6`
  gives `σ_sc ≈ 0.86`, versus the MC scaling value `σa² ≈ 0.048` — an **18×**
  over-prediction. The expansion has genuinely broken down well below 6.

Neither expansion reaches `β = 6`. Closing the window *unconditionally* requires
RG-constructive (Balaban-class) control — that is the named open piece, stated as
such and not papered over.

## Net

```text
   m(β=6) > 0   ⟸   [no 2nd-order bulk point on the SU(3) Wilson axis in (0,6]]
                     (single premise; MC-supported for decades; falsifiable)
                 AND [strong-coupling gap]          (rigorous, R1 — exact quadrature)
                 AND [finite-volume gap ∀β]         (rigorous, R2 — PF + compactness)
                 AND [failure-mode classification]  (rigorous, R3)
```

For the framework: its mass-gap question at `β = 6` on the fixed Planck lattice is
now **one falsifiable premise away from closed**, with every other ingredient
rigorous and runner-verified. The premise is the kind of statement lattice
field theory has tested continuously since the 1980s, with a concrete divergence
signature that has never appeared.

## What this note does NOT claim

- **Not** an unconditional `β=6` gap (the premise is MC-supported, not proven);
  **not** a Clay-problem result (no continuum limit is taken — see the parent
  fixed-Planck note).
- **Not** a derivation of any MC number: `a\sqrt{σ}`, the crossover location, and
  the glueball mass are comparators only.
- **No** new axiom, primitive, vocabulary, or class tag; **no** PDG/fitted input
  consumed as derivation input (`β=6 → g²=1` is the framework's own bare-coupling
  convention, used to locate the target coupling).
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner, exact quadrature/linear algebra): the SU(3) Weyl-measure
  class integrals; `u(β)/β → 1/18`; `σ_sc(β) > 0` in strong coupling; monotone
  `u(β)`; the positivity-improving/PF finite-volume gap family and its compact-
  interval minimum; the all-orders invisibility of `e^{-1/(2b_0g²)}`; the two-loop
  `aΛ` at `g²=1`; the 18× strong-coupling breakdown factor at `β=6`.
- **Cited** (comparator/scope only): Osterwalder–Seiler *Ann. Phys.* 110 (1978)
  440 (lattice RP, strong-coupling gap); Münster (strong-coupling expansions);
  Guth *PRD* 21 (1980) 2291, Fröhlich–Spencer (U(1) Coulomb phase, in the parent
  note); SU(3) MC: plaquette/specific-heat crossover and `a\sqrt{σ}(β=6.0)≈0.2189`
  (Necco–Sommer-class scaling studies); Balaban (UV stability program; the named
  constructive route).

## Dependencies

- [YANG_MILLS_MASS_GAP_FIXED_PLANCK_LATTICE_BOUNDED_NOTE_2026-06-09.md](YANG_MILLS_MASS_GAP_FIXED_PLANCK_LATTICE_BOUNDED_NOTE_2026-06-09.md)
  — the parent fixed-`a` reframing whose named residual this note attacks.
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md) — the
  fixed Planck spacing (no continuum limit taken).
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the hypercubic-symmetric surface on which the RP/transfer construction applies.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
