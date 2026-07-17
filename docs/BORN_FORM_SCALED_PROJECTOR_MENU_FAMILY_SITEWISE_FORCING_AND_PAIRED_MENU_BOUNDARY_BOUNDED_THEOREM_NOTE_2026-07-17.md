---
claim_id: born_form_scaled_projector_menu_family_sitewise_forcing_and_paired_menu_boundary_bounded_theorem_note_2026-07-17
claim_type: bounded_theorem
claim_scope: "Bridge-conditional thinning of the effect-menu horn at one site: on the scaled-projector family (nonnegative multiples of one-site rank-1 projectors and of the identity), menu normalization plus effect-functionality forces the Born trace form on that domain at a single M_2(C) site, with no literature bridge input, no composite, finite menus only, and no effect with two distinct nonzero eigenvalues used anywhere; scaled rank-1 menus carry the form-forcing, and identity-multiple menus are used only to determine the identity ray of the domain. Boundary: the paired subfamily (equal-weight antipodal pairs plus identity multiples) does not force — the landed one-site rogue extends to it explicitly — so some menu outside the paired subfamily is necessary. The family sits strictly between the projective and full-effect menu families; whether it or any smaller family is minimal is not established; no menu grade is selected; the grading primitive is assumed here, not adopted."
upstream_dependencies:
  - minimal_axioms
  - born_form_effect_menu_sitewise_forcing_and_product_menu_boundary_bounded_theorem_note_2026-07-17
runner: scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py
---

# Born Form On The Scaled-Projector Menu Family: Sitewise Forcing With No Literature Bridge Input, And The Paired-Menu Boundary

**Date:** 2026-07-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; the grading hypotheses are assumed here, not
adopted; the menu family the physical registration supplies is underived.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here. Every grading hypothesis below is conditional input only.
**Primary runner:**
[`scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py`](../scripts/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.py)
**Runner cache:**
[`logs/runner-cache/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.txt`](../logs/runner-cache/born_form_scaled_projector_menu_family_sitewise_forcing_2026_07_17.txt)

## Purpose

The parent block
[`BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`](BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md)
proved sitewise Born forcing at effect grade (its E1-E2: weights on all
effects, every finite effect partition eligible) and left the space between
the poles open, naming "classical mixtures of projective menus and other
intermediate families" as untested, with the hypothesis-surface sentence:
"Whether the physical registration supplies menus at projective grade, at
effect grade, at neither, or at some intermediate family is underived and is
not decided here."

This note closes one named piece of that gap with an exactly delimited
intermediate family and a two-sided statement:

- **Forcing.** On the scaled-projector family — effects that are nonnegative
  multiples of one-site rank-1 projectors or of the identity — menu
  normalization plus effect-functionality already forces the Born trace form
  on that domain, at a single `M_2(C)` site, with no literature bridge
  input. The proof is a direct four-menu-schema argument (complement,
  same-direction split, axis cancellation, coins) and uses no effect with
  two distinct nonzero eigenvalues; the form-forcing runs on scaled rank-1
  menus, with coin menus used only to determine the identity ray.
- **Boundary.** The paired subfamily — menus that are disjoint unions of
  equal-weight antipodal pairs and identity multiples, the shape produced by
  classically mixing binary projective measurements without splitting or
  regrouping outcomes — does not force: the landed one-site rogue extends to
  it explicitly. A forcing family on this surface must therefore contain
  some menu outside the paired subfamily; the proof's nontrivial split
  instances and non-axis axis-cancellation instances are unpaired and
  supply them.

Consequence for the menu-grade dial: sitewise form-fixing does not need
any effect beyond scaled projectors and identity multiples. The registration
question gains a witnessed necessary condition — the supplied menu family
must leave the paired subfamily — with no sufficiency boundary among
unpaired families established, no family selected, and no minimality claim
made.

## Authorities and Inputs

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — source for
  the one-site `M_2(C)` possibility domain and the Record sentences "Only
  records are readable. A readout value is determined by record content
  alone." The axioms do not supply probabilities, weights, menus, update
  rules, or record-production processes.
- [`BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`](BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md)
  — the parent surface: the effect-grade pole (its T1), the landed
  lexicographic hemisphere rogue and its exact three-direction refutation of
  every `2 x 2` trace form (reused here at the same resolution), and the
  named-untested intermediate-family gap this note addresses.
- [`BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md`](BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md)
  — the projective-horn frontier note whose hypothesis surface both blocks
  condition on; not otherwise used.
- Literature comparators (never proof inputs): Wright-Weigert 2019 (a
  Gleason-type theorem for qubits from projective measurements and their
  classical mixtures — a differently delimited restricted family; a native
  translation of their exact class is a separate open increment); Busch 2003
  and Caves-Fuchs-Manne-Renes 2004 (the full effect-family pole).

## The Family

Work at one site, `A ≅ M_2(C)`, `P(n) = (1 + n·σ)/2` for unit Bloch
directions `n`. Define the scaled-projector effects

> `S = { c P(n) : c ∈ [0,1], n unit } ∪ { c 1 : c ∈ [0,1] }`,

and write `S_sharp` for the rank-1 part `{ c P(n) : c ∈ (0,1] }`. Every
element of `S` is an effect; a nonzero element determines its parameters
uniquely (`c P(n)` has eigenvalue pair `{c, 0}`, `c 1` has `{c, c}`, so `c`
and, for rank 1, `n` are recovered from the operator). A **scaled-projector
menu** is a finite family of nonzero elements of `S` summing to `1`.

**T1 (exact menu characterization).** A finite family
`{c_k P(n_k)}_k ∪ {d_j 1}_j` of nonzero scaled-projector effects is a menu
iff

> `Σ_k c_k n_k = 0` and `Σ_k c_k / 2 + Σ_j d_j = 1`.

Proof: expand in the basis `{1, σ_x, σ_y, σ_z}`; the identity component
gives the scalar condition, the Pauli components give the vector condition.
The family therefore contains, among others: every projective menu
`{P(n), P(−n)}`; every coin `{c 1, (1−c) 1}` and its refinements;
same-direction splits `{λP(n), μP(n), (1−λ−μ)P(n), P(−n)}`; the
axis-cancellation menus of T2; and three-element coplanar menus such as
`{(2/3)P(n_1), (2/3)P(n_2), (2/3)P(n_3)}` with `n_1 + n_2 + n_3 = 0`. It
does not contain any effect with two distinct nonzero eigenvalues (e.g.
`diag(1/2, 1/4)`), so it is a proper subfamily of the parent block's
effect-partition family.

## Hypotheses

**(F1) grading exists on the scaled-projector domain.** There is
`w : S → [0,1]` with `w(0) = 0` and `w(1) = 1`; `w` is a function of the
effect alone — its value does not depend on which eligible menu embeds the
effect.

**(F2) scaled-projector menus are eligible.** For every scaled-projector
menu `{A_j}`, `Σ_j w(A_j) = 1`.

F1-F2 are the parent block's E1-E2 with the effect algebra replaced by `S`
and effect partitions replaced by scaled-projector menus: the domain and the
menu family both shrink, so F1-F2 is a strictly weaker hypothesis surface
than the effect-grade pole, and strictly stronger than bare projective
menus, which it contains. Only finite menus are used; no countable clause is
assumed. Whether the physical registration supplies this family, a larger
one, a smaller one, or none is underived and is not decided here.

## Results

**T2 (forcing on the scaled-projector family, without an imported literature theorem).** Assume
F1-F2 at one site. Then there is a unique density matrix `σ` with
`w(E) = Tr(σE)` for every `E ∈ S`. The proof uses four menu schemas, all
inside `S`, and only the rank-1 schemas carry the forcing:

- **(a) Ray additivity.** Fix `n` and write `h(λ) = w(λP(n))`. For
  `λ, μ ≥ 0` with `λ + μ ≤ 1`, T1 validates the same-direction splits
  `{λP(n), μP(n), (1−λ−μ)P(n), P(−n)}` and
  `{(λ+μ)P(n), (1−λ−μ)P(n), P(−n)}` (the degenerate members with zero
  coefficient are dropped). Subtracting their normalizations gives
  `h(λ) + h(μ) = h(λ+μ)`. With `h ≥ 0` this gives monotonicity
  (`h(μ') = h(μ) + h(μ'−μ) ≥ h(μ)`), rational homogeneity by iteration, and
  the rational squeeze `q_1 h(1) ≤ h(t) ≤ q_2 h(1)` for rationals
  `q_1 < t < q_2`; hence `h(λ) = λ g(n)` for all real `λ ∈ [0,1]`, with
  `g(n) := w(P(n))`.
- **(b) Complement.** The projective menu `{P(n), P(−n)}` gives
  `g(n) + g(−n) = 1`.
- **(c) Axis cancellation.** For a unit `n` with components `n_a`
  (`a ∈ {x,y,z}`), set `L = |n_x| + |n_y| + |n_z| ∈ [1, √3]` and
  `c_0 = 2/(1+L) ∈ (0,1]`. By T1,

  > `{ c_0 P(n) } ∪ { c_0 |n_a| P(−sign(n_a) e_a) : n_a ≠ 0 }`

  is a menu: its vector part is `c_0 (n − Σ_a n_a e_a) = 0` and its scalar
  part is `c_0 (1 + L)/2 = 1`. Normalization, (a), and (b) give

  > `g(n) = (1 + L)/2 − Σ_a |n_a| g(−sign(n_a) e_a)
  >        = (1 − L)/2 + Σ_a |n_a| g(sign(n_a) e_a)
  >        = (1 + n·s)/2`,

  with `s_a := 2 g(e_a) − 1`. So `g` is affine in the Bloch direction, with
  its coefficients read off the three axis values.
- **(d) Coins.** Menus `{c 1, c' 1, (1−c−c') 1}` make `f(c) := w(c 1)`
  additive and bounded, hence `f(c) = c` by the same
  rational-homogeneity-plus-squeeze argument. Coins are not used in
  (a)-(c); they only complete the representation over the identity ray of
  `S`.
- **(e) State property and uniqueness.** `g(n) ∈ [0,1]` for all unit `n`
  forces `|s| ≤ 1` (evaluate at `n = −s/|s|` when `s ≠ 0`), so
  `σ := (1 + s·σ)/2` is a density matrix, and
  `w(cP(n)) = c g(n) = Tr(σ · cP(n))`, `w(c1) = c = Tr(σ · c1)` on all of
  `S`. Uniqueness: any representing density matrix reproduces the three
  axis values, which determine `s`.

No step uses a literature theorem, a composite, an effect outside `S`, a
projective frame-function analysis, or countable additivity. The runner
re-derives every load-bearing identity exactly, including the
axis-cancellation identity symbolically on a generic octant and on rational
witnesses in all octants and on the degenerate axis cases.

**T3 (paired-menu boundary).** Call a scaled-projector menu **paired** when
its multiset of elements is a disjoint union of equal-weight antipodal pairs
`{λP(m), λP(−m)}` and identity multiples `{d 1}` — the shape produced by
classically mixing binary projective measurements and coins without
splitting or regrouping outcomes. Then:

- **(T3a) The paired subfamily does not force.** Extend the parent block's
  landed lexicographic hemisphere rogue `g` by
  `w(λP(n)) := λ g(n)`, `w(c1) := c`. On any paired menu the normalization
  sum is `Σ_i λ_i [g(m_i) + g(−m_i)] + Σ_j d_j = Σ_i λ_i + Σ_j d_j = 1` by
  the complement law and T1's scalar condition, so the extension satisfies
  F1-F2 restricted to paired menus; and it is no trace form, by the landed
  exact three-direction contradiction, reused at the same resolution. The
  same computation is witnessed a second time, self-contained in this note,
  by the smooth assignment `g_c(n) = (1 + n_z^3)/2`: it obeys the
  complement law and stays in `[0,1]`, its axis values force the unique
  trace-form candidate `s = (0, 0, 1)`, and at `m = (√3/2, 0, 1/2)` that
  candidate gives `3/4` while `g_c(m) = 9/16` — so the paired subfamily
  admits non-Born gradings that are not tied to the parent's hemisphere
  construction (a review-panel finding adopted here; both witnesses are
  runner-gated).
- **(T3b) Some unpaired menu is necessary.** For any eligible-menu family
  `M` contained in the paired subfamily, F1 plus normalization on `M` does
  not force the Born form: the T3a witness satisfies both. Any menu family
  on this surface whose normalization forces the Born form must therefore
  contain an unpaired menu. In the T2 proof, the nontrivial same-direction
  splits and the non-axis axis-cancellation menus (the latter have no
  antipodal pair at all for generic `n`) are the unpaired menus that carry
  this role.

T3 makes no claim about which intermediate families beyond the paired
subfamily force or fail: the scaled-projector family forces (T2), the
paired subfamily does not (T3a), and the exact boundary between them across
all intermediate families is not classified here.

**T4 (dial recalibration and comparators).** Combined with the parent
block: sitewise Born form-fixing needs neither the full effect algebra nor
any effect with two distinct nonzero eigenvalues — the scaled-projector
family suffices, its rank-1 menus carrying the form-forcing with coin menus
determining only the identity ray. The landed one-site
rogue survives on bare projective and paired menus and dies on the
scaled-projector family (T2 plus the three-direction contradiction), with
the composite/entangled/Gleason route of the projective horn unchanged and
untouched. The registration question therefore sharpens to an exactly
witnessed line: whether the supplied menus ever leave the paired subfamily.
The comparator literature (Wright-Weigert 2019) reaches a Born-forcing
conclusion for a differently delimited restricted family built from
projective measurements and their classical mixtures with outcome
processing; no containment claim between that class and `S` is made here,
and a native translation of their exact class — like any minimal-family
classification — is a named open increment, not attempted in this note.

## No-Go Discipline Gate

T3a is a bounded negative ("the paired subfamily does not force"), so the
negative-claim checklist is answered for it:

- **N1 route inventory (five routes against T3a):** (1) unequal-weight
  antipodal completions — such menus are not paired by definition and lie in
  the forcing family; ATTEMPTED via T2, which covers them; (2) adding coins
  of arbitrary rational or real weight — paired menus already include
  identity multiples, and the extension normalizes them (T3a computation);
  (3) same-direction splits — exactly the unpaired schema; RULED OUT as a
  rescue of the paired subfamily by definition, and named as what activates
  forcing (T3b); (4) countable paired menus — a finite-sum menu family is
  assumed throughout (F2 is finite); named outside scope; (5) two-site
  paired menus and composite rescues — outside this note's one-site scope
  and already handled at the projective grade by the parent block's product
  boundary; named untested at scaled grade.
- **N2 wall independence:** one wall (paired subfamily insufficiency); no
  second wall presented.
- **N3 hidden-wall scan:** the T3a witness is total on `S` (both rays
  defined), satisfies F1 on all of `S`, and its menu obligations are
  evaluated on the paired subfamily only — the restriction is the claim.
  The hemisphere tie convention is inherited verbatim from the landed
  parent construction and gated.
- **N4 residual matching:** the only cited prior negative is the landed
  one-site rogue existence, reused at the same resolution.
- **N5 rhetoric audit:** "does not force" is scoped to the paired subfamily
  at one site; T3 explicitly declines to classify other intermediate
  families.
- **N6 partial-closure scan:** the closure paths are named, not denied —
  the scaled-projector family itself (T2), or the parent block's effect
  pole, or the landed projective-composite route.
- **N7 steelman:** "paired menus are what classical mixing gives you, so
  the physical case is closed against forcing." Reply: T3a proves exactly
  that insufficiency for unsplit mixing; whether record formation supplies
  only paired menus is the underived registration question, and the note
  selects nothing.
- **N8 cross-cycle echo:** the structurally similar prior walls — the
  one-site projective rogue (parent R1 lineage) and the parent's
  product-menu boundary — were crossed by enlarging the menu family
  (effect grade; entangled composite menus). T3b records the same
  mechanism here: the wall is crossed by the unpaired schemas, not by
  dimension or composites.

## Non-Claims

- Does **not** claim any grading exists, on any family; F1-F2 are
  conditional input only.
- Does **not** select a menu family or grade, register or modify any
  primitive, or derive menu eligibility from the axioms.
- Does **not** claim the scaled-projector family is minimal, and does
  **not** classify intermediate families between the paired subfamily and
  `S`; the Wright-Weigert class is a comparator, not translated here.
- Does **not** extend beyond one site: composite menus, values, and record
  conditioning are outside scope, as in the parent block.
- Does **not** set an audit verdict; landing is not ratification, and
  independent audit remains required.

## Verification

The primary runner exactly checks the listed algebraic reductions and
representative witnesses (sympy, rational/symbolic arithmetic, single
process, one-site `M_2` objects only); the arbitrary-finite-family and
all-real-parameter steps are carried by the written proof, with the runner
gating their load-bearing identities:
the parameter-recovery lemma for `S`; the T1 characterization identity
symbolically and on witnesses (projective, coin, split, axis-cancellation
in a generic octant, all-octant rationals, degenerate axis cases, a
coplanar three-element menu) with a non-menu rejector; the ray-additivity
and coin eliminations as formal linear algebra; the monotone
rational-squeeze scaffolding with the interval-nonvacuity guard and a
non-monotone rejector; the axis-cancellation affinity elimination to
`g(n) = (1 + n·s)/2`; the state bound `|s| ≤ 1` and the representation and
uniqueness identities on symbolic scaled effects; the paired-menu
normalization of the rogue extension as a formal identity under the
complement law; the unpairedness of the split and axis schemas; the reused
exact three-direction refutation with an affine control; and needle checks
pinning the quoted sentences of the axiom memo and the parent block note.
Mutation checks (one load-bearing mutation per check family, reverted) are
recorded in the review history and PR body.

Measured runner total after final verification:
`TOTAL: PASS=60 FAIL=0`.
