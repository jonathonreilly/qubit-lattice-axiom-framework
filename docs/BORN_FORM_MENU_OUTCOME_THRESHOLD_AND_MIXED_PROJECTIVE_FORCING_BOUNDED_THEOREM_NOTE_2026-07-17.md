---
claim_id: born_form_menu_outcome_threshold_and_mixed_projective_forcing_bounded_theorem_note_2026-07-17
claim_type: bounded_theorem
claim_scope: "Bridge-conditional execution of the lane's two remaining planned slices plus a family-map corollary. Outcome threshold: two-outcome effect menus do not force the Born trace form (an exact smooth non-Born witness satisfies every binary normalization on the full effect domain; the complement law is all the normalization the binary surface states), while adding three-outcome effect menus restores partial additivity, which iterates to the homogeneity the landed chain needs with no menu of arity above three — the outcome-count threshold for the effect-grade forcing is exactly three, at one site as witnessed and at every finite region dimension once the hypotheses are stated on that region's effect algebra. Mixture forcing: the mixed-projective menu family (finite classical mixtures of binary projective measurements and coins with exact outcome splitting and merging) forces the Born trace form on its element domain at one site, with no imported literature theorem, through a decomposition-invariance lemma. Incomparability: the mixed-projective and scaled-projector forcing families are inclusion-incomparable (a merged two-direction element lies outside the scaled family; the coplanar three-element menu admits no mixture presentation), so the witnessed forcing families form no chain and no unique inclusion-minimal forcing family exists among them. No menu family is selected; no minimality within any chain is claimed; the grading primitive is assumed here, not adopted."
upstream_dependencies:
  - minimal_axioms
  - born_form_effect_menu_sitewise_forcing_and_product_menu_boundary_bounded_theorem_note_2026-07-17
  - born_form_scaled_projector_menu_family_sitewise_forcing_and_paired_menu_boundary_bounded_theorem_note_2026-07-17
runner: scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py
---

# Born Form: The Menu Outcome-Count Threshold, Mixed-Projective Forcing, And The Incomparability Of Forcing Families

**Date:** 2026-07-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; every grading hypothesis below is assumed, not
adopted; which menu family the physical registration supplies is underived.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py`](../scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py)
**Runner cache:**
[`logs/runner-cache/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.txt`](../logs/runner-cache/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.txt)

## Purpose

The first two blocks of this lane fixed the poles and one intermediate
family: at effect grade every finite effect partition eligible forces the
Born form sitewise
([`BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`](BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md),
"(E2) finite effect menus are eligible."), and the scaled-projector family
already suffices while its paired subfamily fails
([`BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`](BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md)).
Two named slices remained: the normalization ingredient itself (what
happens when menu additivity is weakened by outcome count — the lane's
parked additivity boundary), and a native rendering of the comparator
mixture class (projective measurements plus classical randomness and
processing). This note takes both, and adds a family-map corollary; the
full classification of forcing families stays open:

- **Outcome threshold.** Two-outcome menus, on the full effect domain,
  do not force the Born trace form: an exact smooth witness satisfies
  every binary normalization and is no trace form (its value on the coin
  `(1/4)1` is `1/28`, where every normalized trace form gives `1/4`).
  Adding three-outcome menus restores partial additivity, which iterates
  to the homogeneity the parent chain needs. The threshold is exactly
  three.
- **Mixed-projective forcing.** The family of menus presentable as finite
  classical mixtures of binary projective measurements and coins, with
  exact outcome splitting and merging, forces the Born form on its element
  domain — through a decomposition-invariance lemma and the parent block's
  axis-cancellation identity, with no imported literature theorem.
- **Incomparability.** The mixed-projective and scaled-projector forcing
  families are inclusion-incomparable: merged elements leave the scaled
  family, and the coplanar three-element menu admits no mixture
  presentation. The witnessed forcing families therefore form no chain,
  and no unique inclusion-minimal forcing family exists among them.

No family is selected; nothing here derives which menus record formation
supplies.

## Authorities and Inputs

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — the
  one-site `M_2(C)` possibility domain and the Record sentences "Only
  records are readable. A readout value is determined by record content
  alone." The axioms supply no menus, weights, or probabilities.
- The two parent blocks named above — the effect-grade forcing chain
  (steps (A)-(E)), the scaled-projector family with its characterization
  and axis-cancellation identity, and the paired-subfamily boundary. Their
  runners' load-bearing identities are re-derived here where reused.
- Literature comparators (never proof inputs): Busch 2003 and
  Caves-Fuchs-Manne-Renes 2004, whose surrounding discussion also records
  the folklore insufficiency of two-outcome normalization; Wright-Weigert
  2019, whose qubit theorem from projective measurements and their
  classical mixtures is the comparator for the mixed-projective family
  (no identity between their exact class and this family is claimed);
  Sorkin's interference hierarchy, as a structural analogy for the
  two-versus-three-outcome step only (no formal correspondence claimed or
  used).

## Hypotheses

Let `H_Λ` be the Hilbert space of a finite region (`d = 2^{|Λ|} ≥ 2`) and
`E(H_Λ)` its effect algebra; the witnesses of T1 and the mixture family of
X1 live at one site (`H = C^2`), and are so labeled. Throughout, `w`
is a weight with `w(0) = 0`, `w(1) = 1`, `0 ≤ w ≤ 1`, defined on the stated
domain, and a function of the effect alone (its value does not depend on
which eligible menu embeds the effect).

**(G1) two-outcome eligibility.** `w` is defined on all of `E(H_Λ)`; every
binary effect menu `{E, 1 − E}` (and the trivial menu `{1}`) is eligible
and normalized: `w(E) + w(1 − E) = 1`.

**(G2) three-outcome eligibility.** Every ternary effect menu
`{E_1, E_2, E_3}` with `E_1 + E_2 + E_3 = 1` is eligible and normalized.

**(X1) mixed-projective menus.** A menu is mixed-projective when it admits
a presentation: finitely many components, each a binary projective
measurement `{P(n_i), P(−n_i)}` or the trivial measurement `{1}`, carrying
weights `λ_i ≥ 0` with `Σ_i λ_i = 1`; each component outcome is split
across the menu's elements by substochastic rows summing to one (exact
splitting), and each element is the sum of the pieces assigned to it
(exact merging). The element domain `D_mix` is the set of effects arising
as elements of such presentations; `w` is defined on `D_mix` and every
mixed-projective menu is eligible and normalized.

G1-G2 decompose the parent's "(E2) finite effect menus are eligible." by
outcome count. X1 is a native mixture family: projective menus, coins,
same-direction splits, and merged elements such as
`(1/2)P(e_z) + (1/2)P(e_x)` are all mixed-projective; the scaled-projector
family is not contained in it (T3 below), nor it in the scaled family.
Whether the physical registration supplies any of these surfaces is
underived and is not decided here.

## Results

**T1 (two-outcome boundary: an exact smooth non-Born grading).** Under G1
alone the Born form is not forced. Witness: with
`f(t) = t^3 / (t^3 + (1−t)^3)` and `σ_0 = (1 + (1/2)σ_z)/2`, define
`w_0(E) = f(Tr(σ_0 E))`. Then:

- `f` is exactly defined on `[0,1]` (its denominator is
  `1 − 3t + 3t^2 = 3(t − 1/2)^2 + 1/4 ≥ 1/4`), with `f(0) = 0`,
  `f(1) = 1`, and the exact complement identity `f(t) + f(1−t) = 1`; so
  `w_0` is a function of the effect alone, `w_0(0) = 0`, `w_0(1) = 1`,
  `0 ≤ w_0 ≤ 1`, and `w_0(E) + w_0(1−E) = 1` for every effect `E` — every
  binary normalization holds.
- `w_0` is no trace form, by one exact coin value: every normalized trace
  form gives `Tr(ρ (1/4)1) = 1/4`, while `w_0((1/4)1) = f(1/4) = 1/28`.
  As a secondary exhibit, `w_0(P(n)) = f((2 + n_z)/4)` depends on `n_z`
  alone, so a matching trace form would need vanishing `x, y` Bloch
  coefficients and affinity in `n_z`, while the exact values at
  `n_z ∈ {0, 1/2, 1}` are `1/2`, `125/152`, `27/28` and the affine
  midpoint prediction is `41/56 ≠ 125/152`.
- The parent chains fail on this surface at their first step: partial
  additivity is unavailable, and indeed `w_0` violates the ternary menu
  `{(1/4)1, (1/4)1, (1/2)1}` exactly:
  `1/28 + 1/28 + 1/2 = 4/7 ≠ 1`.

So two-outcome normalization on the full effect domain admits smooth
non-Born gradings; the comparator literature records the two-outcome
insufficiency as folklore, and the witness here is native and gated.

**T2 (three-outcome threshold).** Under G1 + G2, for effects with
`E_1 + E_2 ≤ 1`, the ternary menu `{E_1, E_2, 1 − E_1 − E_2}` and the
binary menu `{E_1 + E_2, 1 − E_1 − E_2}` eliminate to partial additivity
`w(E_1 + E_2) = w(E_1) + w(E_2)` — the parent block's step (A), with its
only ternary input now supplied by G2. Partial additivity then iterates
pairwise to `w(kE') = k·w(E')` for integer scalings inside the effect
interval, giving the parent step (B)'s rational homogeneity, monotonicity,
and squeeze with no menu of arity above three; the parent steps (C)-(E)
apply as written. The Born trace form is therefore forced on `E(H_Λ)` at
every finite region dimension, with G1-G2 stated on that region's effect
algebra. Combined with T1: **the outcome-count threshold for the
effect-grade forcing is exactly three** — binary normalization admits the
T1 one-site witness (so no universal forcing holds), ternary
normalization kills it (the exact violation above) and forces the form. No claim is made about
families between (binary plus some proper subset of ternary menus), and
none about minimality within the ternary surface. The two-versus-three
step is structurally reminiscent of the pairwise-versus-triple level in
the Sorkin interference hierarchy; that analogy is comparator-only.

**T3 (mixed-projective forcing).** Under X1, there is a unique density
matrix `σ` with `w(E) = Tr(σE)` for every `E ∈ D_mix`. The proof, with no
imported literature theorem:

- **(a) Splits and coins.** Same-direction splits
  `{λP(n), μP(n), (1−λ−μ)P(n), P(−n)}` are mixed-projective (one
  component, split `+` outcome), giving ray additivity and, with the
  bounded rational squeeze, `w(λP(n)) = λ g(n)` for `g(n) := w(P(n))`;
  coin refinements give `w(c1) = c`; projective menus give the complement
  law. These are the parent block's (a)-(d) steps, re-derived on
  presentations inside X1.
- **(b) Decomposition invariance (the merge lemma).** Let
  `{a_i, n_i}` be finite with `a_i ≥ 0`, `Σ_i a_i ≤ 1`. The menu with
  components along each `n_i` (weight `a_i`) and a coin component (weight
  `1 − Σ_i a_i`), whose `+` outcomes are all merged into one element
  `A = Σ_i a_i P(n_i)` while each `−` outcome and the coin stay separate,
  is mixed-projective; its normalization plus (a) eliminates to

  > `w(A) = Σ_i a_i g(n_i)`.

  The left side depends on the operator `A` alone (the weight is a
  function of the effect), so the right side is invariant across all such
  decompositions of the same operator: whenever
  `Σ_i a_i P(n_i) = Σ_j b_j P(m_j)` with both families admissible,
  `Σ_i a_i g(n_i) = Σ_j b_j g(m_j)`.
- **(c) Affinity from the parent identity.** Halving the parent block's
  axis-cancellation identity gives two admissible decompositions of one
  operator:

  > `(c_0/2) P(n) + Σ_{a : n_a ≠ 0} (c_0 |n_a|/2) P(−sign(n_a) e_a)
  >  = (1/2) 1 = (1/2) P(m) + (1/2) P(−m)`,

  with `c_0 = 2/(1+L)`, `L = Σ_a |n_a|`, and total coefficient mass `1` on
  each side. The merge lemma and the complement law then eliminate to the
  parent's affinity equation, so `g(n) = (1 + n·s)/2` with
  `s_a = 2 g(e_a) − 1`; positivity gives `|s| ≤ 1` as in the parent, and
  `σ = (1 + s·σ)/2` represents `w` on every element of `D_mix`: for any
  element `E` of a presentation, refine the presentation so that `E` stays
  merged while every piece not assigned to `E` is a separate outcome; each
  separate outcome is a single piece with value fixed by ray homogeneity
  or the coin values, so normalization gives `w(E)` as one minus their
  sum, which is the matching sum of `E`'s own piece values, i.e.
  `Tr(σE)`. This covers elements of arbitrary trace (the merge-lemma menu
  of (b) is the special case where the complement pieces are single
  outcomes and a coin); the runner gates a trace-exceeding-one instance
  exactly. Uniqueness follows from the axis values.

The comparator statement (Wright-Weigert 2019) reaches a Born-forcing
conclusion for their mixture class; T3 is the native theorem for this
family, proved independently, and no identity between the two classes is
claimed.

**T4 (incomparability of the witnessed forcing families).** Neither
forcing family contains the other:

- The merged element `(1/2)P(e_z) + (1/2)P(e_x) ∈ D_mix` has two distinct
  nonzero eigenvalues `(2 ± √2)/4`, so it lies outside the
  scaled-projector family `S`.
- The coplanar three-element menu `{(2/3)P(n_k)}` (unit `n_k` summing to
  zero) is a scaled-projector menu but admits no mixed-projective
  presentation: every element is rank 1, so every piece assigned to it is
  a nonnegative multiple of that element's projector; hence every
  component measures along some `±n_k`, and its opposite outcome — a
  multiple of `P(−n_k)` — has no element parallel to it to be assigned to
  (the three directions are pairwise at `cos` angle `−1/2`, not `−1`, and
  coin pieces, being multiples of `1`, fit inside no rank-1 element). So
  all component weights vanish, contradicting `Σλ_i = 1`.

The witnessed forcing families (scaled-projector; mixed-projective; their
common enlargement, the full effect family) therefore form no chain under
inclusion, and no unique inclusion-minimal forcing family exists among
them. Any classification of all forcing families remains open; this note
maps the witnessed ones only.

**T5 (scaled-grade two-outcome corollary).** A binary menu `{E, 1−E}`
inside the scaled-projector family forces `E ∈ {cP(n) : c = 1}` or
`E = c1` (the complement `1 − cP(n)` has eigenvalues `{1−c, 1}`, which
match a scaled rank-1 pattern only at `c = 1` and an identity pattern
only at the excluded endpoint `c = 0`), so binary
scaled menus are exactly the projective menus and coins — a subfamily of
the parent block's paired subfamily, whose non-forcing is already
witnessed there twice. The outcome-count threshold is thus consistent
across the grades treated in this lane.

## No-Go Discipline Gate

T1 and T4's non-presentability slice are bounded negatives, answered
jointly:

- **N1 route inventory (five routes):** (1) strengthen binary menus with
  monotonicity or continuity demands — outside G1 as stated, named
  untested (the T1 witness is in fact smooth, so smoothness alone cannot
  close the gap); (2) restrict the domain to projectors — the parent's
  projective-grade results already govern that surface; RULED OUT as a
  rescue by the parent R1 lineage; (3) add some but not all ternary menus
  — named untested (no claim between G1 and G1+G2); (4) present the
  coplanar menu with sub-outcome splitting — ATTEMPTED inside the T4
  argument: splitting only produces parallel pieces, and parallelism is
  what fails; (5) present it with additional coin components — ATTEMPTED:
  coin pieces are multiples of `1` and fit inside no rank-1 element.
- **N2 wall independence:** two walls are presented (binary
  insufficiency; coplanar non-presentability); they concern different
  surfaces and neither implies the other.
- **N3 hidden-wall scan:** the T1 witness is total on `E(H)` and its
  properties are gated; the T4 argument's parallelism step is stated and
  gated as the rank-1 piece condition.
- **N4 residual matching:** the cited prior negatives are the parent
  blocks' rogue-existence results, reused at the same resolutions; the T4
  obstruction cites no prior wall — its witness basis is the exact
  parallelism and coin gates of this note's own runner.
- **N5 rhetoric audit:** "forces nothing beyond the complement law" is
  scoped to G1 on the effect domain at one site; "no mixture
  presentation" is scoped to the exact X1 presentation form; "no unique
  inclusion-minimal forcing family" is scoped to the witnessed families.
- **N6 partial-closure scan:** closure paths named — G2 (ternary), X1
  (mixtures), the parent families; none is foreclosed.
- **N7 steelman (T1):** "binary menus are the physical case, so the
  boundary kills the program." Reply: T2 shows one added outcome restores
  the full forcing; which menus record formation supplies is exactly the
  underived registration question, and the note selects nothing.
- **N7 steelman (T4):** "sub-splitting pieces or adding extra components
  could evade the parallelism obstruction." Reply: every piece is
  positive semidefinite, so pieces cannot cancel; a nonzero PSD summand
  below a rank-1 element is supported on that element's ray (gated), so
  sub-splitting only multiplies parallel pieces, extra components'
  opposite outcomes still need parallel homes that the coplanar menu does
  not contain, and coin pieces are full-rank; the obstruction stands.
- **N8 cross-cycle echo:** the parent walls were crossed by enlarging the
  menu family; T2 records the same mechanism (ternary menus), and T4
  shows two enlargements that force are mutually non-substitutable.

## Non-Claims

- Does **not** claim any grading exists on any surface; G1, G2, X1 are
  conditional input only.
- Does **not** select a menu family, register a primitive, or derive menu
  eligibility from the axioms.
- Does **not** classify families between G1 and G1+G2, does **not** claim
  X1 equals the comparator class, and does **not** claim any minimal
  forcing family exists or is unique beyond the witnessed
  incomparability.
- Does **not** import Sorkin's hierarchy, Gleason's theorem, or any
  literature result as a proof input.
- Does **not** set an audit verdict; landing is not ratification, and
  independent audit remains required.

## Verification

The primary runner exactly checks the listed algebraic reductions and
representative witnesses (sympy, rational/symbolic arithmetic, single
process, one-site `M_2` objects only); the arbitrary-finite-family and
all-real-parameter steps are carried by the written proof, with the runner
gating their load-bearing identities: the `f`-identities (complement,
endpoints, denominator lower bound) symbolically; the T1 witness values
and the exact three-point non-affinity; the exact ternary violation
`4/7 ≠ 1`; the one-line coin refutation (`1/28` versus the trace-form
`1/4`, with the trace value derived on a generic normalized state); the
trace-exceeding-one merged element `(4/5)P(n) + (3/5)P(−n)` taking its
matching sum by the separate-outcomes route; the step-(A) elimination with its ternary input flagged; the
merge-lemma elimination; the halved axis-cancellation identity as two
decompositions of `(1/2)1` and the resulting affinity equation; the
presentation gates for the menus T3 uses (splits, coins, merge menus);
the merged element's eigenvalues `(2 ± √2)/4` and its exclusion from the
scaled family; the parallelism and coin steps of the T4
non-presentability argument on the exact coplanar menu (pairwise
`cos = −1/2` gates); the T5 eigenvalue characterization of binary scaled
menus; and needle checks pinning the quoted sentences of the axiom memo
and both parent notes. Mutation checks (one load-bearing mutation per
check family, reverted) are recorded in the review history and PR body.

Measured runner total after final verification:
`TOTAL: PASS=44 FAIL=0`.
