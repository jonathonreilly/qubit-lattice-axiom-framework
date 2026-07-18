---
claim_id: theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional structure theorem on the phase-erased (k = 0) slice of the supplied determinant-channel readout surface, three exact slices. Log equivalence: for strictly positive modulus readouts, independent-block multiplicativity is exactly equivalent to additivity of the logarithmic-coordinate readout (both directions through the exponential bridge); with the rebuilt bounded-additive linearity support theorem (repo-native, every step gated), the family is the modulus-character class. Additivity incompatibility: on this slice, where the channel value composes multiplicatively and the readout is a fixed nonnegative function of it, the parent's scalar record-additive shape admits only the identically-zero readout (exact two-step proof), and block multiplicativity does not imply scalar additivity (exact witness F(x) = x); so the parent block's two odd-side routes are genuinely distinct here, and the viable odd-side ingredient on this slice is the homomorphism form (equivalently its logarithmic-coordinate presentation). Non-reconstruction boundary: pre-erasure readouts with identical logarithmic modulus content can differ in multiplicativity (exact two-readout discriminator), so log-modulus data reconstruct neither the phase nor the block law. Bookkeeping corollary: the parent T2 tail, on this slice, sharpens to transported K/CPT orbit constancy plus the homomorphism ingredient; whether any Record/log bridge connects the registrable additive shape to logarithmic coordinates is named as the exact open link, not claimed. No physical readout, carrier, exhaustion, or orientation is derived; the obligation stays open; the gauge side and theta-bar are untouched."
upstream_dependencies:
  - minimal_axioms
  - theta_cross_sector_determinant_forcing_property_characterization_bounded_theorem_note_2026-07-17
  - theta_p2_k_cpt_determinant_character_phase_erasure_bounded_note_2026-06-10
  - registrable_readout_additive_even_phase_free_narrow_theorem_note_2026-06-10
runner: scripts/theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_2026_07_18.py
---

# Theta Post-Erasure Odd-Side Structure: Log Equivalence, Scalar-Additivity Incompatibility, And The Honest Tail

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; every property below is a supplied-class
property, assumed, not adopted; no physical identification is made.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_2026_07_18.py`](../scripts/theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_2026_07_18.txt`](../logs/runner-cache/theta_post_erasure_odd_side_log_equivalence_and_additivity_incompatibility_2026_07_18.txt)

## Purpose

The parent block
[`THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md`](THETA_CROSS_SECTOR_DETERMINANT_FORCING_PROPERTY_CHARACTERIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md)
left its T2 reduction conditional on "an independently supplied quark-side
odd-side ingredient" — the Record-registrable additive shape (P-add), or
the independent-block determinant homomorphism (P-hom) — as alternative,
separately sufficient assumptions. This note settles how those two
ingredients relate on the phase-erased slice (the `k = 0` class of the
cited erasure notes, whose "invariant members of this determinant-character
family are phase-free functions of `|det|`"): they are **not** one supply —
the additive shape is incompatible with the slice's multiplicative channel
composition except degenerately, while the homomorphism ingredient is
exactly equivalent to additivity in logarithmic coordinates. A review-lens
counterexample refuting an earlier draft's conflation of the two additivity
notions is adopted here as the distinctness witness.

## The Post-Erasure Surface

Per the cited erasure notes, the post-erasure slice carries, per sector
block, a readout `r(z) = F(|z|)` with `F : (0, ∞) → [0, ∞)`, and channel
values composing multiplicatively across independent blocks
(`|z_1 z_2| = |z_1| |z_2|`, from the determinant block law). Ingredients:

- **(P-hom, slice form)** block multiplicativity:
  `F(x·y) = F(x)·F(y)` on moduli.
- **(P-log)** additivity of the logarithmic-coordinate readout
  `G(u) = log F(e^u)`: `G(u+v) = G(u) + G(v)`. This is a coordinate
  presentation defined only for strictly positive `F`; it is **not** the
  parent's (P-add), which is additivity of the scalar readout itself over
  pairwise-disjoint records.
- **(P-add, slice form)** the parent's scalar shape on this slice: the
  composite record's readout equals the sum, `F(x·y) = F(x) + F(y)`.

**Degeneracy lemma.** A multiplicative `F` with a zero is identically zero
(`F(x) = F(x_0)·F(x/x_0)`), and `F(1) = F(1)^2` forces `F(1) ∈ {0, 1}`;
nondegenerate multiplicative `F` is strictly positive, so `G` is defined.

## Results

**T1 (log equivalence).** For strictly positive `F`, (P-hom, slice form)
holds iff (P-log) holds — both directions exact through the bijective
exponential bridge `e^u·e^v = e^{u+v}`. With the rebuilt repo-native support theorem
[`BOUNDED_ADDITIVE_ON_INTERVAL_LINEARITY_REBUILT_SUPPORT_NOTE_2026-07-18.md`](BOUNDED_ADDITIVE_ON_INTERVAL_LINEARITY_REBUILT_SUPPORT_NOTE_2026-07-18.md)
(an additive function bounded on an interval of positive length is
linear — rational homogeneity, the centered triangle decomposition, the
integer-scaling rational sandwich, and the Archimedean squeeze, each
gated exactly there; this note's runner cells remain consistency
instances of that authority, not a re-derivation),
`G(u) = s·u` and `F(x) = x^s` — the modulus-character family. The
homomorphism ingredient and its logarithmic-coordinate presentation are
one supply; the parent's scalar additive shape is not part of this
equivalence.

**T2 (scalar-additivity incompatibility, bounded negative).** On this
slice — channel values composing multiplicatively, readout a fixed
function `F ≥ 0` of the channel value — the parent's scalar additive
shape admits only the degenerate readout: `F(1·1) = F(1) + F(1)` gives
`F(1) = 0`, and then `F(x) + F(1/x) = F(1) = 0` with both terms
nonnegative gives `F(x) = 0` for every `x`. Conversely block
multiplicativity does not imply the scalar shape: `F(x) = x` is
multiplicative while `F(2·3) = 6 ≠ 5 = F(2) + F(3)`, exactly. So on the
erased determinant slice the parent's two odd-side routes are genuinely
distinct, and the viable odd-side ingredient here is the homomorphism
form (equivalently (P-log)); the additive route can operate only through
a readout that is not a fixed nonnegative function of the multiplicative
channel value — for example on logarithmic-coordinate data, which is
exactly the (P-log) presentation, or through a Record/log bridge not
supplied by anything cited here.

**T3 (non-reconstruction boundary, bounded negative).** Logarithmic
modulus content reconstructs neither the phase nor the block law:
pre-erasure, the full character `e^{i·arg z}|z|^s` registers the phase
(`1` versus `i` at `arg z = 0, π/2`, fixed modulus) while
`log|r| = s·log|z|` is phase-silent; and the two readouts `z/|z|` and
`e^{i·sin(arg z)}` have identical (zero) logarithmic modulus at unit
modulus while the first is multiplicative and the second is not
(`1 ≠ e^{2i}` at the pair `(i, i)`, exactly). So sharing log-modulus data
decides neither ingredient.

**T4 (bookkeeping corollary on the parent tail).** On the erased
determinant slice, the parent T2 conditional tail sharpens to:
transported K/CPT orbit constancy on the quark determinant channel, plus
the homomorphism ingredient (in either presentation). Whether any
Record/log bridge connects the registrable scalar-additive shape to
logarithmic-coordinate additivity is the exact open link this note names
and does not claim; the physical half (carrier, readout map, exhaustion —
the no-go's live routes), the gauge side, and
`theta_bar = theta_gauge + arg det(M_u M_d)` are untouched.

## No-Go Discipline Gate

T2 and T3 are bounded negatives, answered:

- **N1 route inventory.** Against T2: (1) drop nonnegativity — signed
  scalar readouts leave the stated surface (the erased class is
  nonnegative by its character form); named to its resolution; (2) let
  the readout depend on the record pair rather than the channel value —
  outside the fixed-function surface, named untested; (3) rescale the
  channel value before reading — reparametrization preserves the
  multiplicative composition, so the proof applies unchanged; ATTEMPTED;
  (4) log-coordinate data — exactly (P-log), where additivity is viable
  and equivalent to (P-hom) (T1); (5) a Record/log bridge theorem — the
  named open link, not foreclosed. Against T3: the same-modulus
  phase-twist attack is the discriminator witness itself; enlarging the
  data to full complex values trivially reconstructs — outside the
  log-modulus surface, named.
- **N2 wall independence:** T2 concerns the additive shape's viability;
  T3 concerns reconstruction from log-modulus data; the discriminator
  witnesses differ and neither result implies the other.
- **N3 hidden-wall scan:** strict positivity (for (P-log)'s domain), the
  nondegenerate-interval boundedness input, and the fixed-function
  surface are stated where used; the exponential bridge is bijective.
- **N4 residual matching and dependency roles:** the parent block
  supplies the ingredient inventory this note structures; the erasure
  note supplies the `k = 0` slice; the registrability note supplies the
  scalar-additive shape being tested; `minimal_axioms` supplies only the
  Record sentence lineage those notes rest on, with no direct load here
  beyond scope discipline.
- **N5 rhetoric audit:** "admits only the degenerate readout" is scoped
  to the fixed-nonnegative-function surface with multiplicative
  composition; "genuinely distinct" is scoped to this slice; the earlier
  draft's "one supply in two presentations" claim about (P-add) and
  (P-hom) is withdrawn and replaced by the T1 equivalence, which relates
  (P-hom) to (P-log) only.
- **N6 partial-closure scan:** closure paths named — the homomorphism
  ingredient with orbit-constancy transport (parent T2 shape); a future
  Record/log bridge; the no-go's live routes for the physical half.
- **N7 steelman:** "the incompatibility just says additive and
  multiplicative laws differ — textbook." Reply: the mathematics is
  elementary and stated as such; the content is the placement — the
  parent presented two alternative sufficient routes, and this note
  proves that on the erased determinant slice one of them is degenerate
  as stated, which changes what a closing theorem on the obligation's
  forcing half must supply.
- **N8 cross-cycle echo:** the parent lane's own review round already
  corrected one quantifier-level conflation; this block adopts a
  review-lens counterexample the same way, recorded in the review
  history.

## Non-Claims

- Does **not** derive the physical quark readout, its registrability, the
  orbit-constancy transport, the carrier, or any Record/log bridge; the
  obligation remains open exactly as stated.
- Does **not** modify the parent characterization at the pre-erasure
  level, where both routes remain alternative sufficient assumptions.
- Does **not** touch the gauge-side theta, theta-bar, or the action-level
  bare slot.
- Does **not** set an audit verdict; independent audit remains required.

## Verification

The primary runner checks the listed reductions and witnesses and nothing
more (sympy, exact arithmetic, single process): modulus multiplicativity;
both directions of the exponential bridge with the strict-positivity
domain stated; power-family consistency instances for the named
bounded-additive theorem (not a derivation of it); the degeneracy lemma;
the incompatibility proof steps (`F(1) = 0`; nonnegative pair summing to
zero; the exact `6 ≠ 5` witness for the converse); the non-reconstruction
discriminator pair at exact points; the pre-erasure phase-silence
contrast; and needle checks pinning the parent's odd-side ingredient
sentence, the erasure note's phase-free-family line, and this note's
claim identifier and labels. Mutation checks (one load-bearing mutation
per check family, reverted) are recorded in the review history and PR
body.

Measured runner total after final verification:
`TOTAL: PASS=18 FAIL=0`.
