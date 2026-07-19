---
claim_id: born_form_menu_outcome_threshold_and_mixed_projective_forcing_bounded_theorem_note_2026-07-17
claim_type: bounded_theorem
claim_scope: "Conditional finite-dimensional comparison. At every finite dimension d>=2, normalization on all binary effect partitions admits a smooth non-trace grading, whereas normalization on all effect partitions of at most three outcomes forces the Born trace form; the exact maximum-arity threshold on that explicitly defined full-effect surface is therefore three. At one M_2(C) site, normalization on every finite mixed-projective partition with exact splitting and merging forces the trace form on all qubit effects. The mixed-projective and scaled-projector menu families are incomparable, so the explicitly witnessed three-family subposet has two minimal elements. Binary scaled-projector partitions remain insufficient, but no ternary sufficiency or exact threshold is claimed for that grade. Every carrier, grading, menu, and registration premise is explicit conditional input; no physical family is selected."
upstream_dependencies:
  - minimal_axioms
  - born_form_effect_menu_sitewise_forcing_and_product_menu_boundary_bounded_theorem_note_2026-07-17
  - born_form_scaled_projector_menu_family_sitewise_forcing_and_paired_menu_boundary_bounded_theorem_note_2026-07-17
runner: scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py
---

# Born Form From Ternary Effect Partitions And Finite Mixed-Projective Partitions

**Date:** 2026-07-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; every carrier, grading, and eligible-menu surface
below is an explicit mathematical input, not an adopted primitive or a
physical selection.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py`](../scripts/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.py)
**Runner cache:**
[`logs/runner-cache/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.txt`](../logs/runner-cache/born_form_menu_outcome_threshold_and_mixed_projective_forcing_2026_07_17.txt)

## Purpose And Exact Boundaries

The landed effect-partition note
[`BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`](BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md)
proves that normalization on every finite effect partition conditionally forces
the trace form at every finite dimension. The landed scaled-projector note
[`BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`](BORN_FORM_SCALED_PROJECTOR_MENU_FAMILY_SITEWISE_FORCING_AND_PAIRED_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md)
proves a one-site restricted-family forcing theorem and a paired-menu
non-forcing boundary. Both notes treat their carriers, gradings, and menu
families as conditional inputs and select no physical surface.

This note makes four narrower comparisons, with the load-bearing algebra
reproduced here.

- On the full effect algebra at every finite dimension, all binary partitions
  admit a smooth non-trace grading, while all partitions of at most three
  outcomes force the trace form. Thus the exact maximum-arity threshold on
  this defined surface is three.
- At one qubit site, finite mixtures of binary projective measurements and
  trivial measurements, closed under exact outcome splitting and merging,
  force the trace form on every qubit effect.
- The mixed-projective and scaled-projector menu families are incomparable.
  Only the finite subposet consisting of those two families and all effect
  partitions is classified: it has two minimal elements.
- Binary scaled-projector partitions are exactly projective partitions and
  coin partitions and do not force. No ternary scaled-projector sufficiency or
  exact scaled outcome-count threshold is proved here.

No statement derives a grading, a physical menu selector, record formation,
probabilities, or frequencies.

## Import And Support Inventory

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  one-site `M_2(C)` possibility domain and the Record statement that a readout
  value is determined by record content. It supplies no finite-region tensor
  carrier, effect grading, probability, eligible-menu family, or selector.
- The finite-region carrier `H_Λ = ⊗_{x∈Λ} C^2`, its effect algebra, finite
  dimensionality, and all grading and normalization conditions below are
  explicit conditional mathematical inputs.
- The two landed notes linked above delimit comparison surfaces. The full
  finite-effect extension and the paired-menu rogue used below are reproduced
  self-contained, so no audit or retention status of either parent is imported
  as proof authority. The witnessed-poset comparison remains explicitly
  dependency-bounded on the landed scaled-family forcing statement.
- Pauli/Bloch calculus, finite-dimensional spectral decomposition, positivity,
  and the nondegenerate trace pairing are zero-input finite-matrix machinery;
  the load-bearing identities are written out and runner-gated.
- Busch 2003, Caves--Fuchs--Manne--Renes 2004, Wright--Weigert 2019, and the
  Sorkin hierarchy are context-only comparators. No theorem, class identity,
  residual, or numerical value is borrowed from them.
- There are no measured, fitted, observational, phenomenological,
  cosmological, or literature-derived numerical inputs.

## Conditional Mathematical Surfaces

Let `H` be a finite-dimensional Hilbert space with `d = dim H >= 2`, let
`E(H) = {E : 0 <= E <= I}`, and let
`w : E(H) -> [0,1]` satisfy `w(0)=0` and `w(I)=1`. The value `w(E)` depends
only on the effect, not on a partition containing it. Menus are finite; zero
effects and repeated effects are allowed. Countable additivity is never used.

**Binary effect-partition normalization.** Every partition `{E,I-E}` is
eligible and `w(E)+w(I-E)=1`.

**Ternary effect-partition normalization.** Every partition
`{E_1,E_2,E_3}` with `E_1+E_2+E_3=I` is eligible and normalized. Because zero
effects are allowed and `w(0)=0`, this condition includes binary normalization
through `{E,I-E,0}`; the two conditions are alternative comparison surfaces,
not independent walls.

For the mixed-projective surface, specialize to one site, `H=C^2`, and write
`P(n)=(I+n·sigma)/2` for a unit Bloch direction `n`. A finite
mixed-projective presentation consists of component masses `lambda_r>=0`
summing to one. Each component is either the binary projective measurement
`{P(n_r),P(-n_r)}` or the trivial measurement `{I}`. After multiplication by
`lambda_r`, every component outcome is partitioned among final outcomes by
nonnegative fractions whose sum is one. Each final effect is the sum of the
pieces assigned to it. This is exact splitting and merging; it permits
repetitions, zero pieces, arbitrary finite component counts, and arbitrary
finite regrouping, but no negative pieces or cancellation.

**Finite mixed-projective partition normalization.** The grading is defined
on every effect occurring in such a presentation, is a function of the effect
alone, and normalizes every finite mixed-projective partition. Its element
domain is denoted `D_mix`.

The nonzero scaled-projector convention used later is the landed parent's:
a scaled-projector partition contains nonzero effects of the form `cP(n)` or
`cI`, with `0<c<=1`, summing to `I`.

## Binary Effect Partitions Fail At Every Finite Dimension

Fix any density matrix `rho_0` on `H` and define

`f(t)=t^3/[t^3+(1-t)^3]`, and `w_0(E)=f(Tr(rho_0 E))`.

This is a total effect-functional grading at every finite dimension:

- `0<=Tr(rho_0 E)<=1`, and the denominator of `f` is
  `3(t-1/2)^2+1/4`, so the expression is defined and lies in `[0,1]`.
- `f(0)=0`, `f(1)=1`, and `f(t)+f(1-t)=1`. Since
  `Tr[rho_0(I-E)]=1-Tr(rho_0E)`, every binary partition normalizes.
- The witness is smooth and monotone on `[0,1]` because
  `f'(t)=3t^2(1-t)^2/[t^3+(1-t)^3]^2>=0`.
- It is not a normalized trace form. Every density matrix `rho` gives
  `Tr[rho(cI)]=c`, whereas `w_0((1/4)I)=f(1/4)=1/28`, not `1/4`.

The construction is dimension-parametric: neither the complement calculation
nor the coin refutation depends on `d`. For a concrete qubit runner witness,
`rho_0=(I+(1/2)sigma_z)/2` gives
`Tr[rho_0P(n)]=(2+n_z)/4`. The three values at
`n_z in {0,1/2,1}` are `1/2,125/152,27/28`, which violate affine dependence,
and the ternary coin partition `{I/4,I/4,I/2}` has witness sum `4/7`.

Therefore binary normalization does not force the Born trace form at any
finite dimension `d>=2`, even after adding smoothness and monotonicity.

## Ternary Effect Partitions Force At Every Finite Dimension

Assume ternary effect-partition normalization on `E(H)`. The proof is
self-contained and never uses a menu of more than three outcomes.

**Partial additivity.** If `E+F<=I`, compare the ternary partition
`{E,F,I-E-F}` with the zero-padded binary partition
`{E+F,I-E-F,0}`. The common remainder and `w(0)=0` cancel, giving
`w(E+F)=w(E)+w(F)`.

**Real homogeneity.** Pairwise iteration gives `w(E)=r w(E/r)` for every
positive integer `r`, and hence rational homogeneity inside the effect
interval. If `E<=F`, partial additivity gives
`w(F)=w(E)+w(F-E)>=w(E)`, so `w` is monotone. Rational bounds converging to
any real `t in [0,1]` squeeze `w(tE)` to `t w(E)`.

**Linear extension.** For a positive matrix `A`, choose `s>0` with `A/s<=I`
and set `L(A)=s w(A/s)`. Real homogeneity makes this independent of `s`, and
partial additivity makes `L` additive on the positive cone. If a Hermitian
matrix has two positive-difference presentations `A-B=C-D`, then
`A+D=C+B`; cone additivity gives `L(A)-L(B)=L(C)-L(D)`. Thus `L` extends to a
well-defined real-linear functional on Hermitian matrices.

**Trace representation and state property.** Nondegeneracy of the
finite-dimensional trace pairing gives a unique Hermitian `rho` with
`L(X)=Tr(rho X)`. Normalization gives `Tr(rho)=1`, and
`<psi|rho|psi>=w(P_psi)>=0` for every unit vector, so `rho>=0`.

Hence `w(E)=Tr(rho E)` for all effects at every finite `d>=2`. Combining this
with the preceding dimension-parametric witness proves that, on the explicitly
defined surface “all effect partitions with at most `k` outcomes,” the exact
maximum-arity threshold is three. Proper subsets of ternary partitions are
not classified.

## Finite Mixed-Projective Partitions Force At One Site

Assume finite mixed-projective partition normalization. Set
`g(n)=w(P(n))`.

**Ray and coin homogeneity.** Splitting the positive outcome of one projective
component produces
`{aP(n),bP(n),(1-a-b)P(n),P(-n)}`. Comparing split presentations gives
additivity along each ray; nonnegativity, rational iteration, and the squeeze
argument give `w(cP(n))=c g(n)`. Projective partitions give
`g(n)+g(-n)=1`. Splitting a trivial component similarly gives `w(cI)=c`.

**Decomposition-invariance lemma.** Let

`A=sum_i a_i P(n_i)+bI`, with `a_i,b>=0` and `sum_i a_i+b<=1`.

Use projective components of masses `a_i`, a trivial component of mass `b`,
and a filler trivial component of mass `1-sum_i a_i-b`. Merge the positive
projector pieces and the `bI` piece into `A`; leave every negative projector
piece and the filler as separate outcomes. Normalization eliminates to

`w(A)=sum_i a_i g(n_i)+b`.

Because the left side depends only on `A`, the right side is invariant under
every admissible finite decomposition of the same operator.

**Bloch affinity.** For a unit direction `n`, let
`L=sum_a |n_a|` and `c_0=2/(1+L)`. The two admissible decompositions

`(c_0/2)P(n)+sum_{a:n_a!=0}(c_0|n_a|/2)P(-sign(n_a)e_a)=I/2`

and

`(1/2)P(m)+(1/2)P(-m)=I/2`

have coefficient mass one. Decomposition invariance and the complement law
give
`g(n)=(1+n·s)/2`, where `s_a=2g(e_a)-1`. Since `g(n) in [0,1]` for every
unit `n`, evaluation at `-s/|s|` shows `|s|<=1`. Thus
`rho=(I+s·sigma)/2` is a density matrix.

**The element domain is the full qubit effect algebra.** If a qubit effect
has eigenvalues `0<=lambda_-<=lambda_+<=1` and upper eigenprojector `P(n)`,
then

`E=(lambda_+-lambda_-)P(n)+lambda_- I`.

The coefficient mass is `lambda_+<=1`, so the decomposition lemma applies and
also supplies a mixed-projective presentation. It gives
`w(E)=Tr(rho E)`. Conversely every presented element is an effect because it
is a partial sum of positive pieces from a partition of `I`. Therefore
`D_mix=E(C^2)`, the representation holds throughout that domain, and the
three axis values make `rho` unique. The argument includes effects of trace
greater than one and is independent of component count, ordering, repetition,
or presentation.

This is a native finite-matrix proof. Wright--Weigert 2019 is a comparator for
a differently delimited operational mixture class; no class identity or
theorem import is asserted.

## Incomparability In The Explicitly Witnessed Family Poset

Let `S` be the landed one-site scaled-projector menu family, let `M` be the
finite mixed-projective family above, and let `F` be all finite one-site effect
partitions. Both `S` and `M` are contained in `F`. The landed bounded theorem
supplies forcing for `S`; the preceding section supplies forcing for `M`.
Neither lower family contains the other.

**A mixed-projective partition outside the scaled family.** Mix projective
components along `e_z` and `e_x` with mass `1/2` each and merge their positive
outcomes. The resulting partition contains

`A=(1/2)P(e_z)+(1/2)P(e_x)`.

Its eigenvalues are `(2-sqrt(2))/4` and `(2+sqrt(2))/4`, which are distinct
and nonzero. Thus `A` is neither a scaled rank-one effect nor an identity
multiple, so this mixed-projective partition is not in `S`.

**A scaled-projector partition outside the mixed family.** Let three coplanar
unit directions sum to zero, with every pair having dot product `-1/2`. Then
`{(2/3)P(n_k)}` is a scaled-projector partition. It has no finite
mixed-projective presentation. For positive `c,p`, direct Bloch calculation
gives

`det[cP(n)-pP(m)]=-cp(1-n·m)/2`.

If `pP(m)` is a nonzero piece assigned below `cP(n)`, positivity of the
difference forces `m=n`. A positive coin piece `pI` cannot fit below a rank-one
target because the difference has eigenvalue `-p`. Thus every nonzero piece
assigned to a trine outcome is parallel to that outcome. But every projective
component also has an antipodal piece, and none of the three trine rays is the
antipode of another. Nonnegative pieces cannot cancel. Hence every component
mass would have to vanish, contradicting that the component masses sum to one.
This covers arbitrary finite sub-splitting, repeated components, extra
directions, coins, and regrouping.

Consequently the explicitly listed subposet `{S,M,F}` has two incomparable
minimal elements, `S` and `M`. This is not a classification of all forcing
families and does not exclude an unlisted family below both.

## Binary Scaled-Projector Partitions Give Only A Lower Bound

Under the inherited nonzero-element convention, a binary scaled-projector
partition is either a projective partition or a coin partition. Indeed, if
one member is `cP(n)`, its complement has spectrum `{1-c,1}`. Matching a
scaled rank-one spectrum forces `c=1`; matching an identity spectrum forces
the excluded zero endpoint `c=0`. If one member is `cI`, the other is
`(1-c)I`.

These binary partitions do not force. Define on the scaled domain

`w(cP(n))=c(1+n_z^3)/2`, and `w(cI)=c`.

It normalizes every projective partition by the antipodal identity and every
coin partition by scalar complementation. It is smooth but not a trace form:
the three positive-axis values force the only candidate Bloch vector
`s=(0,0,1)`, while a unit direction with `n_z=1/2` has witness value `9/16`
and trace-candidate value `3/4`.

Thus binary insufficiency is shared by the full-effect and scaled-projector
grades. No ternary scaled-projector sufficiency or exact scaled outcome-count
threshold is proved here.

## No-Go Discipline Gate

The gate treats each semantic negative or open wall separately:

- **Effect-binary surface:** binary full-effect normalization does not force at
  any finite dimension.
- **Merged-effect separation:** the displayed mixed-projective partition is
  outside the scaled family.
- **Trine separation:** the displayed scaled trine has no finite
  mixed-projective presentation.
- **Witnessed-poset scope:** `{S,M,F}` has two minimal elements; no global
  family classification follows.
- **Scaled-binary surface:** binary scaled-projector normalization does not
  force; no exact scaled threshold follows.
- **Registration wall:** current framework authority supplies none of the
  grading/menu/selector surfaces; future closure remains open.

### N1 — distinct hostile routes per surface

Every route below was **ATTEMPTED**. None is recorded as an untested route or
as a borrowed audit verdict.

| Surface | Five or more distinct attacks and exact disposition |
|---|---|
| Effect-binary | (1) Domain failure: `Tr(rho_0E)` stays in `[0,1]` for every effect. (2) Arbitrary binary partitions: the symbolic complement identity handles all `E`, not samples. (3) Dimension rescue: the same construction and coin refutation work for every finite `d`. (4) Regularity rescue: the witness is smooth and monotone. (5) Alternative trace representative: every normalized density gives `1/4` on the quarter coin, while the witness gives `1/28`. (6) Presentation dependence: `w_0` is a fixed function of `E`. All six attacks fail against the narrow negative. |
| Merged-effect separation | (1) Change Bloch coordinates. (2) Swap eigenvalue ordering. (3) Match a different rank-one ray. (4) Match an identity ray. (5) Re-present the operator with different mixture components. Eigenvalues are invariant, strictly positive, and unequal, so all five attacks fail; operator membership is presentation-independent. |
| Trine separation | (1) Arbitrary sub-splitting. (2) Extra nonparallel projective directions. (3) Repeated components and multiplicities. (4) Positive coin pieces. (5) Regrouping or attempted cancellation. (6) Arbitrary finite presentation size. The determinant/support and full-rank coin arguments apply piece by piece, so all six attacks fail. |
| Witnessed-poset scope | (1) Deny forcing for `M`: closed by the self-contained proof. (2) Deny forcing for `S`: this remains exactly dependency-bounded on the landed scaled theorem. (3) Put either lower family inside the other: the two separation witnesses close both directions. (4) Remove the common upper family: both are effect partitions. (5) Insert an unlisted family below both: this succeeds against any global reading, so the conclusion is restricted to `{S,M,F}`. (6) Confuse “two minimal elements” with “no minimum”: the finite subposet statement is explicit. |
| Scaled-binary | (1) Match the complement to a rank-one spectrum. (2) Cross the spectral ordering. (3) Match an identity spectrum. (4) Swap outcomes and inspect endpoints under the nonzero convention. (5) Require regularity: the cubic directional rogue is smooth. (6) Fit a hidden density: axes fix a candidate contradicted off axis. (7) Infer ternary sufficiency: this attack succeeds against the broader inference, so only binary insufficiency is claimed. |
| Registration wall | (1) Read Qubit as supplying weights. (2) Read Record content-functionality as normalization. (3) derive a selector from Admissibility or the approved registry. (4) treat either landed mathematical parent as physical registration. (5) import comparator literature as the framework selector. (6) allow later operational equivalence, convention, or registered structure to close the gap. The first five find no present authority; the sixth remains live, so this surface is OPEN and never a structural no-go. |

### N2 — wall independence and collapse

| Pair | First closes second? | Second closes first? | Disposition |
|---|---:|---:|---|
| Ternary normalization / binary normalization | Yes, using a zero third effect and `w(0)=0` | No | Binary is logically redundant inside the ternary forcing surface; they are not counted as two walls. |
| Grading/functionality / menu eligibility-normalization | No | No | A function does not select menus; a menu class does not supply values. |
| Finite-region tensor carrier / grading-menu surface | No | No | Independent conditional inputs to the finite-dimensional theorem. |
| Physical registration / the exact conditions it would register | Yes, if it supplies them | No | Registration is an umbrella closure route, not an extra wall beside each supplied condition. |
| Merged-effect separation / trine separation | No | No | Independent inclusion directions, both required for incomparability. |
| Effect-binary / scaled-binary non-forcing | No | No | Different domains and menu classes; neither witness establishes the other. |

### N3 — hidden-condition scan

| Surface | Classification |
|---|---|
| finite `H_Λ`, `d=2^{|Λ|}`, and `E(H_Λ)` | Explicit conditional tensor carrier and effect domain; not derived from the minimal axioms. |
| effect-functionality, range, endpoint values | Explicit conditional grading conditions. |
| zero outcomes and repeated outcomes | Explicit finite-menu convention, load-bearing for the ternary-to-binary collapse. |
| all binary or all ternary effect partitions | Explicit alternative normalization surfaces. |
| finite mixed-projective splitting/merging | Explicit mathematical presentation class; no operational realizability is inferred. |
| nonzero scaled-partition elements | Explicit inherited convention, load-bearing at the complement endpoint. |
| Pauli/Bloch, spectral, PSD support, trace pairing | Zero-input finite-matrix machinery with written identities. |
| landed scaled forcing theorem | Explicit dependency-bounded input only for the finite witnessed-poset corollary; not retention authority. |
| literature and “classical mixture” language | Context only; no theorem, class identity, or physical selector imported. |

No countable extension, composite mixed-projective class, empirical value,
frequency interpretation, or physical selection is hidden.

### N4 — source residual matching

| Source surface | Exact residual used here | Match and authority |
|---|---|---|
| `MINIMAL_AXIOMS_2026-06-29.md`, Qubit and Record entries | One-site matrix possibility domain and content-functionality only | Exact factual match; no probability/menu conclusion is drawn. |
| Landed effect-partition note, “Finite-Effect Forcing Theorem” | Full finite-effect normalization conditionally forces | Comparison match; the proof needed here is copied self-contained. |
| Landed scaled-projector note, “forcing on the scaled-projector family” and “paired-menu boundary” | `S` forces; paired shapes admit rogues | Exact one-site family match; `S` forcing bounds the finite-poset corollary, while the binary rogue is copied self-contained. |
| Busch/CFMR/Wright--Weigert/Sorkin comparators | Context about effect or projective-mixture theorems and outcome hierarchy | No proof residual is used; all remain context-only. |
| `docs/repo/ACTIVE_REVIEW_QUEUE.md`, failed-N1 precedent | A bounded label cannot rescue an unscrutinized negative | Exact governance match; this section supplies the replacement per-surface gate. |

Dropping all comparator nonmatches leaves every mathematical negative
self-contained except the explicitly dependency-bounded statement that `S`
is a forcing element of the witnessed poset.

### N5 — resolution and rhetoric

| Phrase | Exact resolution | Broader resolution not claimed |
|---|---|---|
| binary effect partitions do not force | Every effect and every binary partition at every finite `d>=2` | No classification of proper ternary subsets. |
| exact effect threshold three | All arity-at-most-two partitions fail to force; all arity-at-most-three partitions force, dimension by dimension | No threshold for a different domain or menu grade. |
| mixed-projective forcing | One site, arbitrary finite presentations, all `D_mix=E(C^2)` | No composites, countable mixtures, or physical selection. |
| trine has no mixture presentation | The displayed three-outcome scaled trine under the exact finite presentation definition | No statement about other operational closure classes. |
| two minimal witnessed families | Only the explicit subposet `{S,M,F}` | No global minimum, intersection theorem, or classification of all forcing families. |
| binary scaled partitions do not force | One site, finite nonzero scaled partitions | No ternary sufficiency or exact scaled threshold. |
| registration is underived | Current minimal axioms, approved registry, and linked mathematical parents | No impossibility or “new axiom required” conclusion. |

### N6 — live partial-closure paths

| Path | Current status and possible closure |
|---|---|
| classify proper ternary subsets | Open mathematics; could sharpen the full-effect threshold below the “all ternary” surface. |
| prove ternary scaled-projector sufficiency or find a rogue | Open mathematics; required before any exact scaled threshold. |
| classify intermediate/common forcing families | Open mathematics; could enlarge the witnessed poset or find a family below both `S` and `M`. |
| match the native mixed class to an operational comparator | Open definition/theorem work; unnecessary for the native result and not assumed. |
| derive operational equivalence and a normalized grading from record dynamics | Open constructive physics; could retire functionality and grading inputs. |
| register a precise menu/selector premise through governance | No such approved primitive now; registration could supply a conditional framework surface without being misdescribed as a theorem. |
| extend finite one-site mixed presentations to composites or countable families | Open extension problem; outside the present result. |

### N7 — strongest hostile steelmen

- “The binary counterexample is only qubit-specific.” The objection would be
  decisive against the old wording, but the repaired proof now chooses an
  arbitrary finite-dimensional density matrix; the complement identity and
  quarter-coin refutation are dimension-parametric.
- “Continuity or monotonicity may rescue binary forcing.” The explicit
  derivative is nonnegative and smooth, so this does not close the witness.
- “Enough hidden components may present the trine.” The determinant/support
  argument applies to each positive piece and its compulsory antipode,
  independently of finite presentation size; coins are full rank.
- “Two incomparable forcing families do not rule out another family below
  both.” Accepted. The theorem is restricted to the three listed families,
  and global classification stays open.
- “Binary scaled insufficiency gives only a lower bound, not threshold three.”
  Accepted. No scaled ternary sufficiency or exact threshold is claimed.
- “A future operational or Record theorem could select these mathematical
  surfaces without a new axiom.” Accepted. Registration is an open
  constructive route, not a no-go.

### N8 — cross-cycle echo and retirement mechanisms

The prescribed phrase search under `docs/` and walk of all physics-loop
`NO_GO_LEDGER.md` files were rerun against current main during review. The
relevant echoes and retirement mechanisms are:

| Prior or current wall | Retirement/narrowing mechanism applicable here |
|---|---|
| bare projective qubit partitions do not force | Larger mathematical menu surfaces—scaled-projector, mixed-projective, and full effects—add linking partitions; no universal impossibility follows. |
| paired scaled partitions do not force | The full scaled family adds split and axis-cancellation partitions; this supports only the narrow binary lower bound. |
| binary effect partitions do not force | All ternary effect partitions supply common-remainder additivity; proper subsets remain live. |
| physical menu/Record registration absent | `PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md` later constructs one fixed physical ternary menu but expressly not universal ternary eligibility; constructive expansion remains live. |
| broad “no retained primitive” or “new axiom” walls | Operational quotient, convention, later construction, or approved registration can narrow them; this note says only that current authority does not supply the stated surfaces. |
| failed-N1 bounded-note precedent | `ACTIVE_REVIEW_QUEUE.md` requires a passing narrowed packet or removal; relabeling a negative as a boundary is not a cure. |

The retirement scan therefore supports the narrow mathematical statements and
keeps physical selection and broader family classification open.

## Non-Claims

- No grading, probability, frequency, record-production process, or eligible
  menu family is derived from the minimal axioms.
- No menu family is physically selected, and no grading/menu primitive is
  proposed, registered, or ratified.
- No global classification or unique-minimum theorem for all forcing families
  is claimed.
- No ternary scaled-projector sufficiency or exact scaled threshold is claimed.
- No identity with a comparator literature class and no literature theorem is
  imported.
- No audit status or verdict is authored; landing is not ratification.

## Verification

The paired runner uses exact SymPy algebra and exits nonzero on any failure. It
checks the dimension-parametric witness schema, smoothness identity, arbitrary
binary complement, quarter-coin refutation, ternary violation, common-remainder
additivity, finite-matrix forcing scaffolds, exact mixed-presentation sums,
decomposition invariance, axis affinity in symbolic and mixed-sign cases,
full-domain spectral representation including a trace-greater-than-one effect,
the merged-effect spectrum, the general PSD support determinant, the coplanar
trine, the scaled-binary classification, the smooth scaled rogue, and
current-source needles. The cache pins the runner, this source, both landed
parents, and the minimal-axiom memo by SHA-256.

Measured runner total after regeneration:
`TOTAL: PASS=48 FAIL=0`.
