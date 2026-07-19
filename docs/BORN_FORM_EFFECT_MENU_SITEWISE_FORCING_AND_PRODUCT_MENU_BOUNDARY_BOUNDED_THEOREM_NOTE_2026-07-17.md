---
claim_id: born_form_effect_menu_sitewise_forcing_and_product_menu_boundary_bounded_theorem_note_2026-07-17
claim_type: bounded_theorem
claim_scope: "Conditional finite-dimensional result: normalization on every finite effect partition forces the Born trace form, while on a two-qubit bonded pair the joint relaxation from global orthogonal additivity and full projective-menu eligibility to product-menu normalization does not force that form. The pair result is not an H4-only necessity or minimality statement. The tensor carrier, grading domain, menu family, and Pauli-conjugation premise are explicit conditional inputs; no menu grade is selected or derived."
upstream_dependencies:
  - minimal_axioms
runner: scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py
---

# Born Form From Finite Effect Partitions And A Joint Product-Menu Relaxation

**Date:** 2026-07-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; every grading and menu hypothesis below is an
explicit input, not an adopted primitive.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict.
**Primary runner:**
[`scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py`](../scripts/born_form_effect_menu_sitewise_forcing_2026_07_17.py)
**Runner cache:**
[`logs/runner-cache/born_form_effect_menu_sitewise_forcing_2026_07_17.txt`](../logs/runner-cache/born_form_effect_menu_sitewise_forcing_2026_07_17.txt)

## Purpose And Exact Boundary

This note proves two conditional finite-dimensional statements.

1. If a normalized, noncontextual grading is defined on every effect of a
   finite matrix algebra and every finite effect partition of the identity is
   eligible, then the grading has the unique Born trace form. The proof is
   reproduced from finite operator algebra and uses no literature theorem.
2. On a conditional two-qubit bonded-pair carrier, if the grading is defined
   on all projections but the only normalization requirements are those
   carried by product-projector resolutions, then a non-Born grading exists.
   This second result jointly drops global orthogonal additivity (the parent
   surface's H2) and restricts full composite-menu eligibility (the parent
   surface's H4). It therefore proves no H4-only necessity, no minimal
   entangled-menu family, and no statement about what happens when global
   additivity is retained.

The two statements compare different explicitly assumed menu surfaces. They
do not select a physical surface. The registered axioms supply no probability
grading, effect algebra, tensor-product finite-region carrier, menu family,
additivity law, or Pauli symmetry.

## Import And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) is the only
  source dependency. It supplies the `Z^3` nearest-neighbor lattice and the
  one-site `M_2(ℂ)` possibility domain, while expressly limiting the axioms to
  their named primitive content.
- The finite-region carrier
  `H_Λ = ⊗_{x∈Λ} ℂ²`, the associated matrix effects and projections, every
  grading domain, and every eligible menu family below are conditional
  mathematical inputs. They are not derived from the minimal axioms.
- Global orthogonal additivity (called parent H2 for comparison) and full
  bonded-pair projective-menu eligibility (called parent H4 for comparison)
  are not premises of the product-menu counterexample. The counterexample
  changes both conditions at once.
- Invariance under the three Pauli conjugations is an additional conditional
  premise used only in the final symmetry corollary.
- `BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md`,
  and `BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`
  are comparison surfaces only. No result from them is used in either proof.
- No measured, fitted, observational, phenomenological, cosmological, or
  literature-derived numerical value enters this note.

## Finite-Effect Assumptions

Let `Λ` be a finite region, let `H_Λ = ⊗_{x∈Λ} ℂ²` have dimension
`d = 2^{|Λ|}`, and let
`E(H_Λ) = {E : 0 ≤ E ≤ I}` be its effect algebra. Assume:

**Effect-domain noncontextual grading.** There is a function
`w : E(H_Λ) → [0,1]` with `w(0)=0` and `w(I)=1`. Its value depends only on
the effect, not on a menu containing that effect.

**Finite effect-partition normalization.** For every finite family of effects
`{E_i}` satisfying `Σ_i E_i = I`, the family is eligible and
`Σ_i w(E_i)=1`.

Only finite partitions are assumed. Countable additivity is not used.

## Finite-Effect Forcing Theorem

Under the two finite-effect assumptions, there is a unique density matrix
`σ` such that

`w(E) = Tr(σE)`

for every effect `E`, at every finite dimension `d ≥ 2`.

### Proof

**Partial additivity.** If `E+F≤I`, compare the normalized menus
`{E,F,I-E-F}` and `{E+F,I-E-F}`. Their common remainder cancels, giving
`w(E+F)=w(E)+w(F)`. The menu `{E,I-E}` also gives
`w(E)+w(I-E)=1`.

**Homogeneity.** Repeating `E/r` in the menu
`{E/r,...,E/r,I-E}` gives `w(E/r)=w(E)/r`, hence rational homogeneity on
`[0,1]`. If `E≤F`, partial additivity gives
`w(F)=w(E)+w(F-E)≥w(E)`, so `w` is monotone. For real `t∈[0,1]`, rational
bounds `q_1<t<q_2` imply
`q_1E≤tE≤q_2E`; rational homogeneity and monotonicity squeeze
`w(tE)` to `t w(E)`.

**Positive-cone and linear extension.** For a positive matrix `A`, choose
`s>0` with `A/s≤I` and set `F(A)=s w(A/s)`. Homogeneity makes this
independent of `s`, and partial additivity makes `F` additive on the positive
cone. Every Hermitian matrix is a difference of two positive matrices. If
`A-B=C-D`, then `A+D=C+B`; cone additivity gives
`F(A)-F(B)=F(C)-F(D)`. Thus `F` is a well-defined real-linear functional on
the Hermitian matrices.

**Trace representation.** The trace pairing on the finite-dimensional real
space of Hermitian matrices is nondegenerate. Therefore a unique Hermitian
matrix `σ` satisfies `F(H)=Tr(σH)` for every Hermitian `H`.

**State property.** From `w(I)=1`, `Tr(σ)=1`. For every unit vector `ψ`, the
rank-one projector `P_ψ` is an effect and
`⟨ψ|σ|ψ⟩=w(P_ψ)≥0`; hence `σ≥0`.

This proof is dimension-generic and imports no representation theorem.

## The One-Site Hemisphere Grading Cannot Extend To Effects

For a Bloch unit vector `n`, let `P(n)=(I+n·σ⃗)/2`. Define the lexicographic
hemisphere grading `g` by reading `(n_z,n_y,n_x)` and assigning `1` when the
first nonzero component is positive and `0` when it is negative; also set
`g(0)=0` and `g(I)=1`. Then `g(P(n))+g(P(-n))=1`, including on the tie sets,
so it normalizes every one-site binary projective menu.

It cannot be the restriction of a finite-effect grading. Any such extension
would have the trace form just proved. A normalized trace functional on a
qubit is affine in the Bloch direction. The values
`g(P(e_x))=g(P(e_z))=1` force the affine value `1/2` at
`u=(e_x-e_z)/√2`, while the hemisphere rule gives `g(P(u))=0`.

## Bonded-Pair Counterexample Under A Joint Relaxation

Work conditionally on `H=ℂ²⊗ℂ²`. A product-projector menu is a finite family
of nonzero projections `R_i=A_i⊗B_i` that are mutually orthogonal and sum to
`I_4`. The exact relaxed hypothesis surface is:

- a noncontextual function `W` is defined on every projection of `H`, with
  values in `[0,1]`, `W(0)=0`, and `W(I_4)=1`; and
- every product-projector menu is normalized by `Σ_i W(R_i)=1`.

Normalization also carries additivity across any eligible product
coarse-graining. No additivity is required for an arbitrary orthogonal pair
of projections. Relative to the parent projective surface, this is a joint
change: global orthogonal additivity is removed and menu eligibility is
restricted. The theorem below concerns only that joint surface.

### Product Factorization Is Well Defined

For a nonzero product projection `R=A⊗B`,

`Tr_2(R)=(Tr B)A`, and `Tr_1(R)=(Tr A)B`.

Because nonzero projections have positive integer trace, the supports of the
two partial traces recover `A` and `B` uniquely. Thus a product rule assigned
to nonzero `R` is independent of any proposed factorization. The zero
projection is handled separately.

### Exhaustive Classification Of Product-Projector Menus

Every product-projector menu is, up to swapping the sites, one of the
following tree forms:

- `{I_4}`;
- `{P(a)⊗I, P(-a)⊗I}`;
- `{P(a)⊗I, P(-a)⊗P(d), P(-a)⊗P(-d)}`; or
- `{P(a)⊗P(b), P(a)⊗P(-b),
   P(-a)⊗P(c), P(-a)⊗P(-c)}`.

Here is the complete case proof. A nonzero product projection on
`ℂ²⊗ℂ²` has rank `1`, `2`, or `4`. Orthogonality makes ranks additive, so
the only rank partitions of the identity are
`(4)`, `(2,2)`, `(2,1,1)`, and `(1,1,1,1)`.

- **Rank `(4)`.** The only element is `I_4`.
- **Rank `(2,2)`.** A rank-two product projection is either `P(a)⊗I` or
  `I⊗P(b)`. One of each type has overlap trace `1` and cannot be orthogonal.
  Two of the same type are orthogonal only when their rank-one factors are
  antipodal, giving the binary tree form.
- **Rank `(2,1,1)`.** Up to a site swap, the rank-two term is `P(a)⊗I`.
  Each rank-one remainder lies below its complement `P(-a)⊗I`, so each has
  first factor `P(-a)`. Their second factors must be orthogonal and hence
  antipodal, giving the three-element tree form.
- **Rank `(1,1,1,1)`.** Choose one leaf `P(a)⊗P(b)`. Each of the other three
  leaves is orthogonal to it through the first factor `P(-a)` or the second
  factor `P(-b)`. With three leaves and two factors, two use the same factor.
  If two use the first factor, their common first factor is `P(-a)` and
  mutual orthogonality forces antipodal second factors `P(c),P(-c)`; their
  sum is `P(-a)⊗I`. Completeness then forces the fourth leaf to be
  `P(a)⊗P(-b)`. If two use the second factor, the same argument with the
  sites swapped gives the other rooting. This exhausts the last partition.

The identities used here are elementary and exact:
`Tr(P(a)P(c))=(1+a·c)/2`, so qubit rank-one projectors are orthogonal exactly
at antipodes; product overlaps factorize; and a rank-one projector lies below
another projection exactly when their overlap trace is one. The paired runner
certifies the rank partitions, both mixed-rank cases, the pigeonhole step, and
the forced-complement identities independently of the normalization checks.

### Full-Domain Non-Born Grading

Choose hemisphere gradings `g_1,g_2` as above. Define

- `W(0)=0`;
- `W(A⊗B)=g_1(A)g_2(B)` for each nonzero product projection; and
- `W(R)=1/2` for every non-product projection `R`.

The factor-uniqueness result makes the product clause unambiguous. The last
clause is an arbitrary full-domain completion: eligible product menus contain
no non-product projection, so their normalization cannot constrain those
values.

On every classified tree menu, the product rule sums to one by the two
one-site complement laws `g_i(P(n))+g_i(P(-n))=1`. The same identities give
additivity for every eligible product coarse-graining. Hence `W` satisfies the
exact relaxed hypothesis surface on all product-projector menus.

The completion is explicitly not globally additive. Let
`R=P(e_z)⊗P(e_z)`, let `P` project onto
`(|01⟩+|10⟩)/√2`, and set `Q=R+P`. The two summands are orthogonal. Both `P`
and `Q` are non-product projections; the partial-trace spectrum of `Q` is
`{3/2,1/2}`. Therefore

`W(Q)-W(R)-W(P)=1/2-1-1/2=-1`.

This defect is part of the joint relaxation, not an omitted claim about the
parent global-additivity surface.

Finally, `W(A⊗I)=g_1(A)`. The three-direction affine contradiction above
shows that this restriction is not a one-site trace form. But the restriction
of every pair-state trace form `R↦Tr(ρR)` to `A⊗I` is affine in the Bloch
direction. Thus no density matrix on the pair represents `W`.

### Exact Consequence

Product-projector-menu normalization on a two-qubit pair, when global
orthogonal additivity is simultaneously replaced by menu-carried
coarse-graining, does not force the Born trace form. This is a bounded joint
relaxation result. It does not show that parent H4 alone can or cannot be
weakened, that entangled menus are necessary, that any intermediate menu
family is sufficient, or that a globally additive non-Born grading exists.

## Pauli-Conjugation Symmetry Corollary

Add to the finite-effect assumptions at one site the premise
`w(UEU†)=w(E)` for each Pauli matrix `U∈{X,Y,Z}`. These conjugations, together
with the identity action, form the finite Pauli conjugation group (equivalently
the Klein-four action after phases are removed). Uniqueness of the trace
representative transfers the invariance to `σ`. A `2×2` Hermitian matrix
invariant under conjugation by all three Pauli matrices is scalar; trace one
then gives `σ=I/2`. This symmetry premise is conditional and is not derived from an
absence of conditioning records.

## No-Go Discipline Gate For The Joint Relaxation

The negative statement is only that the exact joint relaxed surface above
does not force a trace form. The following N1--N8 record applies to that
bounded statement.

### N1 — Alternative Routes

Five distinct attacks were attempted in this cycle:

1. **ATTEMPTED — full projection domain.** Extend the product rule to every
   non-product projection and test consistency. The explicit constant
   completion succeeds on the stated surface; its global-additivity defect is
   separately exposed.
2. **ATTEMPTED — rank-two `(2,2)` menus.** Enumerate both site orientations
   and mixed orientations. Mixed orientations are nonorthogonal; same-site
   antipodal pairs normalize exactly.
3. **ATTEMPTED — adaptive `(2,1,1)` menus.** Put the rank-two split on either
   site and allow the other-site direction on the refined branch to vary. The
   containment proof forces the tree form, which normalizes exactly.
4. **ATTEMPTED — four-rank-one and proposed non-tree menus.** Run the
   factor-colored orthogonality graph from an arbitrary leaf in both
   rootings. Pigeonhole plus the forced complement exhausts the partition;
   every resulting tree normalizes.
5. **ATTEMPTED — countable or zero-padded product partitions.** In dimension
   four, mutually orthogonal nonzero projections have positive integer ranks
   summing to four, so there are at most four. Removing zero padding reduces
   every countable proposal to one of the four finite rank partitions above.

### N2 — Independence Audit

The two raw changes are tested directionally before they are collapsed:

| Directional pairwise test | Automatically closes the other condition? | Reason |
|---|---|---|
| Restore global orthogonal additivity → expand product-only eligibility to every finite projective menu | **No** | An additivity law constrains values but does not declare any additional menu eligible. |
| Expand eligibility to every finite projective menu → restore global orthogonal additivity | **Yes**, given the stated full projection domain and noncontextual menu values | For orthogonal `R,S`, compare `{R,S,I-R-S}` with `{R+S,I-R-S}` and cancel the common complement. |

The conditions are therefore not independent. Full projective-menu
eligibility implies the relevant global additivity on this domain, while the
reverse implication fails. The source consequently presents one collapsed
joint relaxation, not two independent walls. Restoring global additivity
excludes this particular `W` by its exact defect, but no claim is made here
that either strengthening alone classifies every possible grading.

### N3 — Hidden-Condition Scan

The load-bearing phrases classify as follows:

| Phrase | Classification |
|---|---|
| all pair projections | explicit full-domain assumption |
| nonnegative, normalized, noncontextual values | explicit grading assumptions |
| `ℂ²⊗ℂ²` bonded-pair carrier | explicit conditional structural input |
| product-projector menus only | exact eligible-family boundary |
| menu-carried coarse-graining | exact additivity boundary; global additivity excluded |
| unique product factors | proved from partial traces |
| finite dimension four | exact resolution boundary |
| comparison documents and literature | support only; no proof input |

No unlisted measured value, boundary condition, standard-theorem import, or
global additivity premise is used.

### N4 — Residual Matching

| Cited source locator | Witness or mechanism | Residual attacked there | Residual claimed here | Exact match? |
|---|---|---|---|---|
| `docs/BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md:101-114` | lexicographic hemisphere grading | non-Born values on one-site binary projective menus | the same `g_i`, defined here self-containedly and reproduced by the runner | **Yes**, at the one-site restriction |
| `docs/BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md:67-84,117-133` | full bonded-pair projective surface | positive closure under global additivity, full menus, and a named bridge | joint relaxation changes both global additivity and menu eligibility | **No** negative residual; comparator only |
| `docs/BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md:40-72,182-204` | finite-effect representation | positive trace-form result under effect-partition additivity | finite-effect forcing is reproved here | **No** projective residual; comparator only |
| `docs/STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md:16-29,53-104` | correlated joint-law counterexample | outcome factorization is not fixed by one-copy Born marginals | product-menu normalization does not fix a projection grading | **No**; different residual, so it supplies no witness support |

After non-matches are dropped, only the first row supplies a matching prior
shape. The present note redefines and rechecks that grading rather than using
the prior claim as a premise; the universal pair-menu result rests on the
classification and construction proved here.

### N5 — Resolution And Rhetoric Audit

The effect theorem is finite-region and finite-effect-menu conditional. The
negative is only a bonded-pair, dimension-four, product-projector-menu result
under the named joint relaxation. It is not promoted to a larger region,
arbitrary entangled-menu family, global-additivity surface, lattice-wide
claim, H4 necessity statement, or physical selection of a menu grade.

### N6 — Partial-Closure Paths

Three strengthening routes are separated:

- restoring global orthogonal additivity excludes this witness, without a
  claim here that all alternatives are classified;
- making every finite projective resolution eligible derives global
  orthogonal additivity and likewise excludes this witness; and
- making every finite effect partition eligible closes the form by the
  self-contained finite-effect theorem above.

Intermediate entangled-projective families and larger product regions remain
open. None of these menu or additivity conditions is supplied by the
registered primitive set.

### N7 — Strongest Steelman

**Hostile steelman of the shipped claim.** The purported universal
counterexample may cover only the tree menus the author chose to write down.
A rank-one leaf can be orthogonal to the selected leaf in both tensor slots,
so its factor color is ambiguous; a different coloring, a nonunique product
factorization, or an unlisted continuous product basis might evade the
pigeonhole argument and impose a normalization constraint involving the
arbitrary non-product completion. If any such menu exists, the construction
does not establish the claimed joint-relaxation counterexample.

The objection is closed, rather than assumed away. Partial traces recover the
two factors of every nonzero product projection uniquely. A double-colored
leaf may be assigned either available color: with three other leaves and two
colors, any assignment still yields two leaves with the same color. Their
shared qubit factor is the unique antipode of the selected factor; mutual
orthogonality then forces their other factors to be antipodal, their sum is a
complete rank-two branch, and the remaining leaf is the forced complement.
The rank partitions `(4)`, `(2,2)`, `(2,1,1)`, and `(1,1,1,1)` exhaust every
finite or zero-padded product menu, and every eligible leaf is a product, so
the non-product completion enters no normalization. The paired runner checks
factor recovery, both site orientations, the color pigeonhole, forced
complements, and normalization separately. Thus the strongest route against
the current narrowed claim is closed by the continuous proof and independent
certificates, not by the removed H4-only rhetoric.

### N8 — Cross-Cycle Echo

A repo-wide search for `product-projector`, `product menu`, `partial menu`,
`dimension-2`, `unentangled frame`, `effect menu`, `Gleason`, and
`factorization` found the following closest prior mechanisms:

- the one-site dimension-two hemisphere residual in
  `BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md`,
  which is reproduced here and is closed on the finite-effect surface;
- full composite projective and effect-menu positive routes, which use
  stronger hypothesis surfaces and therefore are not counterexamples to the
  joint relaxed statement; and
- outcome-factorization negatives such as
  `STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md`,
  whose residual concerns correlations/factorization rather than menu
  normalization and so supplies no witness for this claim.

No searched prior wall retires the exact joint relaxed counterexample. The
two positive menu-strength mechanisms are retained as explicit reopen paths.

## Non-Claims

- No grading, probability law, finite-region tensor carrier, menu family,
  additivity law, or Pauli symmetry is derived from the axioms.
- No menu grade is selected or registered.
- No H4-only weakening, entangled-menu necessity, minimal menu family,
  globally additive counterexample, or larger-region statement is proved.
- No record conditioning, rates, dynamics, update rule, orientation, scale,
  phenomenology, or observational value is derived.
- No literature theorem, comparison document, or prior negative is used as a
  proof premise.
- No audit verdict is set; landing is not ratification.

## Verification

The primary runner checks the finite-effect proof at dimensions two and four;
the hemisphere complement and three-direction contradiction; product-factor
uniqueness by partial traces; the complete rank-partition classification,
including mixed-rank exclusions, both adaptive branches, the factor-color
pigeonhole step, and forced complements; product-menu normalization; the
full-domain global-additivity defect; pair-state trace affinity; and the Pauli
commutant. It also pins the minimal-axiom boundary and the narrowed source
sentences. The paired cache records the exact runner SHA, output, and total for
this source revision.
