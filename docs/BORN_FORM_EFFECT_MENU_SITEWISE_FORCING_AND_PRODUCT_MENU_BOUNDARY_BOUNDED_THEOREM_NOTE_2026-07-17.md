---
claim_id: born_form_effect_menu_sitewise_forcing_and_product_menu_boundary_bounded_theorem_note_2026-07-17
claim_type: bounded_theorem
claim_scope: "Bridge-conditional two-sided statement on the menu grade of the graded-constraint hypothesis surface, with the projective and effect grades treated as the two poles and intermediate menu families named untested. Effect horn: if the assumed grading is defined on the effect algebra of a finite region with finite effect-partition menus eligible, the Born trace form is forced sitewise at every finite dimension >= 2, reproved from finite operator algebra with no literature bridge input; the landed one-site projective rogue extends to no such grading. Projective horn boundary: on a bonded pair, grading hypotheses whose eligible menus are the product-projector resolutions, and whose additivity is the normalization carried by those menus (global orthogonal additivity over arbitrary projection pairs is not retained: it alone rebuilds full frame-function strength, where the landed Gleason route forces the form regardless of menu restriction), do not force the Born trace form (constructive witness; exhaustive product-menu classification), so the landed composite route's menu family cannot be weakened all the way to product-projector menus at 2x2 with menu-carried additivity; no claim is made that full H4 or any particular entangled-menu family is minimal. The menu grade itself is underived; no horn is selected; the grading primitive is assumed here, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py
---

# Born Form At Effect-Menu Grade: Sitewise Forcing With No Bridge Input, And The Product-Menu Boundary On The Projective Horn

**Date:** 2026-07-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; the grading hypotheses are assumed here, not
adopted, and the menu grade they are stated at is itself underived.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here. Every grading hypothesis below is conditional input only.
**Primary runner:**
[`scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py`](../scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py)
**Runner cache:**
[`logs/runner-cache/born_form_effect_menu_sitewise_forcing_2026_07_17.txt`](../logs/runner-cache/born_form_effect_menu_sitewise_forcing_2026_07_17.txt)

## Purpose

The landed composite bridge note
[`BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md`](BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md)
fixes the form of a lawful graded constraint at projective-menu grade: its
hypotheses H1-H3 place a weight function on projections, H4 makes every
finite orthogonal resolution of a bonded-pair identity menu-eligible,
including resolutions that contain entangled projections, and the trace form
then follows through one named literature bridge input, stated there as
"Gleason's theorem is imported as named classical mathematics."

This note isolates the menu-grade dial in that hypothesis surface and proves
one exact statement on each side of it:

- **Effect horn.** If the same grading hypotheses are instead stated on the
  effect algebra of a finite region — weights defined on all effects, finite
  effect partitions of the identity menu-eligible — the Born trace form is
  forced already at a single site, at every finite dimension `>= 2`, by a
  five-step finite operator-algebra argument reproved here with no literature
  bridge input. The landed one-site projective rogue assignment extends to no
  grading of this kind, so the dimension-2 loophole is a feature of the
  projective grade, not of the site dimension.
- **Projective horn boundary.** On the bonded pair, the projective-grade
  hypotheses restricted to product-projector menus — with additivity
  carried by those menus, since retaining global orthogonal additivity by
  itself rebuilds full frame-function strength and the landed Gleason
  route then forces the form regardless of menu restriction — do not force
  the Born trace form: a constructive product-form rogue normalizes every
  product-projector menu (classified exhaustively) while restricting on
  one site to the landed non-quadratic assignment. H4's menu family
  therefore cannot be weakened all the way to product-projector menus at
  `2 x 2` with menu-carried additivity; whether full H4 or some
  intermediate entangled-menu family is minimal is not established here.

Neither horn is selected. The axioms supply no menus at all; which resolutions
of the identity are menus, and at which grade, is exactly the registration
content the landed note declares as H4's specification burden. This note
sharpens that burden into a two-sided exact statement and moves nothing else.

## Authorities and Inputs

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — source for
  the `Z^3` nearest-neighbor lattice, the one-site `M_2(C)` possibility
  domain, and the Record sentences "Only records are readable. A readout
  value is determined by record content alone." The axioms do not supply
  probabilities, weights, menus, update rules, or record-production
  processes, and the memo's Qualification states: "These axioms state only
  their named primitive content. Further physical structure requires a
  retained derivation or bridge, or explicit approved-primitive registration,
  before use as a premise."
- [`BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md`](BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md)
  — the landed projective-horn route: hypotheses H1-H4, the one-site rogue
  construction R1, the composite rescue R2/R3 through the Gleason bridge
  input, and the declared specification burden. Cited as the projective-horn
  authority; its Gleason import is not used by this note's effect-horn
  results.
- [`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  — the repo's reproven-from-primitives effect-representation argument on
  `M_2(C)` under hypotheses (M1)-(M3), with the explicit reconstruction
  `σ = ½[ 𝟙 + Σ_{a∈{x,y,z}} (2 m(P_a^+) − 1) σ_a ]`. Theorem T1 below
  restates that five-step argument dimension-generically and the runner
  re-derives its load-bearing identities independently at dimensions 2 and 4.
- Literature comparators (never proof inputs): Busch 2003 and
  Caves-Fuchs-Manne-Renes 2004 for the effect-level representation theorem;
  Wallach 2002 for the statement that unentangled frame functions determine
  density operators only when every tensor factor has dimension at least 3.
  The `2 x 2` product-menu boundary claimed here is proved by this note's own
  constructive witness and classification, not by the comparator.

## Hypotheses

Let `Λ ⊂ Z^3` be a finite region, `H_Λ = ⊗_{x∈Λ} C^2`, `d = 2^{|Λ|}`, and
`E(H_Λ) = { E : 0 ≤ E ≤ 1 }` the effect algebra of the region algebra. The
landed projective-horn hypotheses H1-H3 place `w ≥ 0` on projections with
`w(0) = 0`, `w(identity) = 1`, menu-normalization on finite orthogonal
resolutions of the identity, additivity, and embedding-independence. The
effect-grade restatement assumed by the effect horn is:

**(E1) grading exists at effect grade.** There is `w : E(H_Λ) → [0,1]` with
`w(0) = 0` and `w(1) = 1`. As at projective grade, `w` is a function of the
effect alone; the value does not depend on which eligible menu embeds it.

**(E2) finite effect menus are eligible.** For every finite family
`{E_i} ⊂ E(H_Λ)` with `Σ_i E_i = 1`, the family is an eligible menu and
`Σ_i w(E_i) = 1`.

E1-E2 keep the shape of H1-H3 together with an H4-style universal
menu-eligibility clause — in the landed note, universal eligibility is
carried by H4's "every finite orthogonal resolution ... is menu-eligible",
not by H1-H3 alone — with "projection" replaced by "effect" and orthogonal
resolutions replaced by finite effect partitions. They are neither implied
by nor implied-in the projective-grade hypotheses on the same region: the
domain and the menu family are both enlarged, and the enlarged menu family
is a strictly stronger normalization demand. Only finite menus
are used anywhere below; no countable-additivity clause is assumed. Whether
the physical registration supplies menus at projective grade, at effect
grade, at neither, or at some intermediate family is underived and is not
decided here.

## Results

**T1 (effect horn: sitewise forcing at every finite dimension, no bridge
input).** Assume E1-E2 on a finite region of dimension `d ≥ 2`. Then there is
a unique density matrix `σ` with `w(E) = Tr(σE)` for every effect `E`. The
proof is the five-step finite argument, dimension-generic:

- **(A) Partial additivity.** For effects with `E_1 + E_2 ≤ 1`, apply E2 to
  the menus `{E_1, E_2, 1 − E_1 − E_2}` and `{E_1 + E_2, 1 − E_1 − E_2}`:
  subtracting, `w(E_1 + E_2) = w(E_1) + w(E_2)`. The two-outcome menu
  `{E, 1 − E}` gives the complement law `w(E) + w(1 − E) = 1`.
- **(B) Homogeneity.** Iterating (A) on the `(r+1)`-outcome menu
  `{E/r, ..., E/r, 1 − E}` gives `w(E/r) = w(E)/r` and then `w(qE) = q w(E)`
  for rational `q ∈ [0,1]`. Monotonicity follows from (A): if `E ≤ F` then
  `F − E` is an effect and `w(F) = w(E) + w(F − E) ≥ w(E)`. For real
  `t ∈ [0,1]` and rationals `q_1 < t < q_2`, the operator inequalities
  `q_1 E ≤ tE ≤ q_2 E` then squeeze `w(tE)` between `q_1 w(E)` and
  `q_2 w(E)`, so `w(tE) = t w(E)`.
- **(C) Linear extension.** `Herm(M_d)` is a real vector space of dimension
  `d^2` spanned by effects (the normalized identity-plus-generator elements
  `(1 + B_k)/2` and `1` itself). Additivity plus homogeneity on the positive
  cone extend `w` to a well-defined real-linear functional `F` on
  `Herm(M_d)`: scale any positive `A` into the effect interval, set
  `F(A) = s·w(A/s)` for `s` dominating the top eigenvalue (well-defined by
  homogeneity), and define `F` on differences; the standard two-sided
  cancellation argument shows representation-independence.
- **(D) Trace representation.** The trace pairing `⟨X,Y⟩ = Tr(XY)` is a
  nondegenerate real inner product on `Herm(M_d)`, so `F(H) = Tr(σH)` for a
  unique Hermitian `σ`, reconstructed linearly from the `d^2` basis values of
  `w`. At `d = 2` this is exactly the landed display
  `σ = ½[ 𝟙 + Σ_{a∈{x,y,z}} (2 m(P_a^+) − 1) σ_a ]`.
- **(E) State property.** `w(1) = 1` gives `Tr σ = 1`; for every unit vector
  `ψ` the rank-1 projector is an effect, so `⟨ψ|σ|ψ⟩ = w(P_ψ) ≥ 0`, hence
  `σ ≥ 0`.

No step uses `d ≥ 3`, a composite, a projective frame-function analysis, or
any literature theorem. The runner re-derives the load-bearing identities of
every step exactly at `d = 2` and `d = 4`.

**T2 (effect horn: the landed rogue extends to no effect-grade grading).**
The landed R1 assignment `g` — the lexicographic hemisphere rule on one-site
rank-1 projections, which satisfies the projective-grade hypotheses on
one-site binary menus — extends to no `w` satisfying E1-E2 on a single site.
By T1 any such `w` is a trace form; every `2 x 2` trace form is affine in the
Bloch direction, and the landed exact three-direction contradiction
(`g(e_x) = g(e_z) = 1` with `g(1) = 1` forces the value `1/2` at
`(e_x − e_z)/√2`, where `g` assigns `0`) refutes every trace-form
restriction. The landed note's sentence "Three directions plus normalization
refute every `2x2` trace form at once" is reused unchanged; what is new is
the direction of use: at effect grade the refutation kills the rogue rather
than the forcing, at one site, with no composite and no bridge input.

**T3 (projective horn boundary: product-projector menus do not force the
Born form on the bonded pair).** Work on a bonded nearest-neighbor pair,
`d = 4`, at projective grade, but with the eligible menus restricted to
product-projector resolutions: finite families of nonzero projectors of the
form `A ⊗ B` (`A`, `B` one-site projectors) summing to the pair identity.
The hypothesis surface at this restriction is stated exactly: the weight
domain remains all pair projections and the weight is a function of the
projection alone (the landed H1/H3 shape), but additivity enters only as
the normalization carried by the eligible product-projector menus and
their within-family coarse-grainings (merging orthogonal product elements
whose sum is again a product projector). The landed H2 read as global
orthogonal additivity over arbitrary projection pairs is not retained
here, and cannot be: any globally additive normalized weight is already a
frame function on the full projection lattice (finite induction over
orthogonal sums), where the landed note's Gleason bridge input forces the
trace form at `d = 4` regardless of which menus are eligible — global
additivity by itself restores exactly the "full projection-measure
strength" of the landed refutation-seat finding, and the menu-family dial
is meaningful only with menu-carried additivity. Values on non-product
projections are then constrained by no eligible menu, and the witness
below is completed to the full domain by an explicit arbitrary extension.
Then:

- **(T3a) Classification.** Every product-projector menu is a tree menu: up
  to swapping the two sites, it is `{1}`, or `{P(a)⊗1, P(−a)⊗1}`, or
  `{P(a)⊗1, P(−a)⊗P(d), P(−a)⊗P(−d)}`, or
  `{P(a)⊗P(b), P(a)⊗P(−b), P(−a)⊗P(b'), P(−a)⊗P(−b')}` — a first-site split
  refined branchwise on the second site, or the site-swapped form. The proof
  is a finite case analysis from two exact facts: one-site rank-1 projectors
  are orthogonal exactly when their Bloch directions are antipodal, and
  `(P(a)⊗P(b)) ⊥ (P(c)⊗P(d))` exactly when `a·c = −1` or `b·d = −1`. Three
  pairwise-orthogonal rank-1 products cannot share one first-site direction
  (three mutually antipodal second-site directions are impossible), a rank-3
  complement is never a product projector (product-projector ranks on the
  pair are 1, 2, 4), and a rank-1 product below `P(−a)⊗1` must carry first
  slot `−a` (a rank-1 projector lies below a projector exactly when their
  overlap trace is 1, and `Tr(P(−a)P(c)) = (1 − a·c)/2 = 1` forces
  `c = −a`). The runner gates each fact and each case branch exactly.
- **(T3b) Constructive rogue.** Define `W` on product projectors by the
  product rule `W(A ⊗ B) = g_1(A) · g_2(B)`, with `g_1`, `g_2` lexicographic
  hemisphere rules and `g_i(1) = 1`, `g_i(0) = 0`, and extend `W` to the
  remaining (non-product) pair projections by the constant value `1/2` — an
  arbitrary choice that no product-projector menu constrains, so the
  extended `W` is defined on the full projection domain of the landed H1
  while every menu-normalization obligation of the restricted family falls
  on the product values alone. The extension satisfies within-family
  additivity — for orthogonal product pairs whose sum is again a product
  projector, which the T3a machinery classifies as same-first-slot second
  -site merges `P(a)⊗P(b) + P(a)⊗P(−b) = P(a)⊗1` and antipodal rank-2
  merges `P(a)⊗1 + P(−a)⊗1 = 1` (and site-swaps), the product rule is
  exactly additive — and it is not globally additive, witnessed exactly:
  for `R = P(e_z)⊗P(e_z)`, `P` the projector onto `(|01⟩ + |10⟩)/√2`, and
  `Q = R + P` (orthogonal, with `Q` non-product by its partial-trace
  spectrum `{3/2, 1/2}`), the extension gives
  `W(Q) − W(R) − W(P) = 1/2 − 1 − 1/2 = −1`. That failure is forced by the
  boundary itself, not a defect of the witness: a globally additive
  completion cannot exist, since global additivity would make `W` a frame
  function and the landed Gleason input would force the trace form,
  contradicting the non-Born product restriction. Using `g_i(n) + g_i(−n) = 1` (which the
  hemisphere rule satisfies exactly, including on its tie set), `W` sums to
  1 on every tree menu of either rooting, hence on every product-projector
  menu by T3a. Its one-site restriction `W(A ⊗ 1) = g_1(A)` is the landed
  rogue, which by the three-direction contradiction is no trace form; since
  `E ↦ Tr(ρ(E ⊗ 1))` is trace-affine for every pair state `ρ`, no density
  matrix on the pair represents `W`.
- **(T3c) Consequence.** At `2 x 2`, projective-grade hypotheses whose menu
  family contains only product-projector resolutions, with additivity
  carried by that family, do not force the Born form; and the restriction
  is meaningful only in that menu-carried reading, since global orthogonal
  additivity alone is frame-function strength and the landed bridge input
  then forces the form at `d = 4` whatever the menus. The landed composite route's H4 clause — menu-eligibility for
  resolutions "that contain entangled projections", with the landed
  refutation-seat finding "Without this full projection-measure strength a
  partial menu assignment is not a frame function and Gleason does not
  apply" — therefore cannot be weakened all the way to product-projector
  menus at `2 x 2`; whether full H4, or some intermediate projective-menu
  family, is minimal is untested here. This agrees with the comparator
  statement (Wallach 2002) that
  unentangled frame functions determine density operators only when every
  factor has dimension at least 3; the `2 x 2` case claimed here is proved
  natively by T3a-T3b. Entangled projections are not products (the runner
  gates a Bell-projector Schmidt-rank witness), and `W` assigns them no
  value, so T3 is consistent with, and does not touch, the landed R2/R3
  forcing under full H4 strength.

**T4 (the menu grade is the dial, and the attribution moves).** T1-T3
together relocate the landed dimension-2 loophole: it is not a fact about the
site, it is a fact about the projective grade. On the effect horn the form is
fixed sitewise and the nearest-neighbor lattice pays for nothing in the
form-fixing step — composites matter there only for values (joint states and
their conditioning), which remain underived. On the projective horn the
lattice composite plus full entangled-menu strength plus the Gleason bridge
input remain exactly what the landed note says they are, and T3 shows the
entangled-menu clause cannot be weakened to product menus at `2 x 2`. The
landed attribution sentence "adjacency alone pays for nothing here without
H4's strength" is thereby sharpened in both directions: with effect menus,
adjacency is not needed for the form; with product-projective menus,
adjacency plus the bridge input still do not suffice. Which menu family the
physical registration supplies — the two grades treated here are the poles,
and intermediate families remain untested — is an open item of the declared
specification burden; this note records two bounded horns and selects no
grade.

**T5 (zero-information limit at a finite-group premise, effect horn).**
Under the additional named premise that `w` is invariant under conjugation by
the three one-site Pauli unitaries — a finite group, strictly weaker than the
landed R4 premise of invariance under every unitary automorphism — the
reconstruction of T1 forces `σ = 1/2 · 1` (the maximally mixed `I/2`) at
one site: invariance transfers to
`σ` by uniqueness, and the only `2 x 2` Hermitian commuting with all three
Pauli conjugations is scalar. Weights are then uniform on binary menus,
consistent with the landed uniform-on-orbits results. This premise is named
here and not derived; "no conditioning records" alone does not supply it.

## Relation To The Landed Effect-Level Surface

The finite-region statement of
[`BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](BUSCH_POVM_EXTENSION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
reaches the same trace-form conclusion on `E(H_Λ)`, but its landed
derivation routes the `|Λ| ≥ 2` case through the projective companion
[`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md),
which imports Gleason's projective theorem as named standard mathematics,
and it assumes countable additivity. T1 differs on exactly those two
surfaces: the five-step argument is dimension-generic on the effect algebra,
so no projective import enters at any `|Λ|`, and only finite menus are
assumed. The legacy chain
[`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md)
carries separate inductive-limit and identification inputs that this note
does not use and does not discharge. The orientation memo
[`GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md`](GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION_2026-07-04.md)
is cited for orientation and scope discipline only and carries no premise
weight here.

## No-Go Discipline Gate

T3 is a bounded negative boundary ("product-projector menus do not force the
Born trace form at `2 x 2`"), so the negative-claim checklist is answered
for it:

- **N1 route inventory (five routes against T3):** (1) coarse rank-2 product
  menus added — ATTEMPTED, the rogue normalizes them (T3a covers ranks 1, 2,
  4); (2) non-tree product menus that might constrain further — RULED OUT by
  the T3a classification; (3) countable product-projector partitions — a
  finite-dimensional identity admits at most `d` nonzero mutually orthogonal
  projectors, so countable adds nothing at `d = 4`; (4) menus mixing
  projective structure with non-projective effects (classical mixtures of
  projective menus and other intermediate families) — OUTSIDE T3's scope by
  construction and named untested; the comparator literature suggests such
  families can force the form already at one site, which is exactly why T3
  is scoped to product-projector resolutions only; (5) larger regions
  (`2 x 2 x 2` product menus) — untested here; the comparator statement says
  qubit factors never suffice, but no native claim is made beyond the bonded
  pair.
- **N2 wall independence:** T3 names one wall (product-menu insufficiency at
  `2 x 2`); no second wall is presented.
- **N3 hidden-wall scan:** T3's hypothesis surface is stated exactly in
  its preamble: menu-carried additivity only, with the global-additivity
  reading excluded and shown to trivialize the restriction (it alone
  rebuilds frame-function strength). The witness is completed to the full
  projection domain by the explicit arbitrary extension stated in T3b,
  which satisfies within-family additivity and provably cannot be globally
  additive (the exact `W(Q) − W(R) − W(P) = −1` gate; a reviewer-supplied
  reconciliation finding adopted here). The tie-set convention inside the
  hemisphere rule is inherited verbatim from the landed R1 construction
  and gated.
- **N4 residual matching:** the only cited prior negative is the landed R1
  rogue existence, reused at the same resolution (one-site binary menus and
  their product refinements).
- **N5 rhetoric audit:** the negative is stated as "do not force the Born
  trace form", scoped to the stated menu family on the stated pair; T3c
  states the exact family and dimension, and the note nowhere claims that
  full H4 or any particular entangled-menu family is minimal.
- **N6 partial-closure scan:** the closure path is named, not denied — full
  H4 strength (landed) or effect-grade menus (T1); T3 forecloses neither.
- **N7 steelman:** "product menus are the physically natural family, so T3
  kills the projective horn." Reply: T3 proves insufficiency of that family,
  not naturalness; which family the registration supplies is exactly the
  declared open specification item, and the landed composite route under
  full H4 strength is untouched.
- **N8 cross-cycle echo:** the structurally similar prior wall — one-site
  dimension-2 rogue existence — was retired on the composite by H4 strength
  (landed R3) and is retired sitewise at effect grade by T2 here; both
  mechanisms are cited, and neither retires T3's product-menu wall.

## Non-Claims

- Does **not** claim any grading exists, at any grade; E1-E2 and the
  projective-grade hypotheses are conditional input only.
- Does **not** select a menu grade, register or modify any primitive, or
  derive menu-eligibility from the axioms; the axioms supply no menus.
- Does **not** derive weight values, record conditioning, rates, dynamics,
  update rules, orientation, or scale.
- Does **not** touch the landed composite route's conclusions under full H4
  strength, and does **not** re-prove or use Gleason's projective theorem.
- Does **not** set an audit verdict or close the probability wall; landing is
  not ratification, and independent audit remains required.

## Verification

The primary runner re-derives every load-bearing identity exactly (sympy,
rational/symbolic arithmetic, single process, dimensions 2 and 4 only):
the menu bookkeeping behind (A) and (B) as formal linear elimination; the
effect-cone witnesses (including a noncommuting pair); the monotonicity and
squeeze inequalities on exact witnesses with a non-monotone rejector; the
`d = 2` and `d = 4` effect bases with nondegenerate trace Gram matrices; the
reconstruction identity `w(E) = Tr(σE)` on symbolic effects, matching the
landed Bloch display at `d = 2`; the state property; the exact
three-direction refutation of every `2 x 2` trace form and its T2 corollary
logic; the antipodal-orthogonality and product-orthogonality lemmas; each
case branch of the T3a classification (including the three-antipodal
impossibility, the rank-3 non-product fact, and the below-`P(−a)⊗1`
forcing); the hemisphere complement law including tie-set witnesses; the
product-rogue normalization on both tree rootings and coarse menus; the
trace-affinity of pair-state restrictions; the Bell-projector Schmidt-rank
witness; the Pauli-commutant computation behind T5; and needle checks that
pin the quoted sentences of the axiom memo and the two landed notes named
above. Mutation checks (one load-bearing mutation per check family,
reverted) are recorded in the review history and PR body.

Measured runner total after final verification:
`TOTAL: PASS=56 FAIL=0`.
