---
claim_id: record_does_not_type_newton_source_versus_test_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Record content-only readout and additivity are swap-symmetric on a disjoint pair of collections, so they do not assign which collection is the Newton source mass M in the source-linear Green pairing; the unequal-mass Green split at r=1 is exact, and a declared typing remains a second object."
upstream_dependencies:
  - minimal_axioms
  - newton_law_derived_note
runner: scripts/record_does_not_type_newton_source_versus_test_2026_08_13.py
---

# Record Does Not Type Newton Source Versus Test

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact source-versus-test typing of two disjoint Record collections
against the already-recorded source-linear Green pairing; a declared typing
remains a second object.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/record_does_not_type_newton_source_versus_test_2026_08_13.py`](../scripts/record_does_not_type_newton_source_versus_test_2026_08_13.py)

## Result Up Front

The Newton potential-kernel packet
[`NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md) supplies the
source-linear Green pairing

`G(r)=1/(4 pi r)`, `phi = M G`, `|grad phi| = M/(4 pi r^2)`

and lists among its non-claims both

`F = -M_test grad(phi)`

and

the physical product law `M_source M_test`.

If two disjoint Record collections `S` and `T` are given, that Green
assignment still needs a **typing**: which collection is the source mass `M`
that enters `phi`. Record additivity and content-only readout are
swap-symmetric. This note proves that the axioms do not assign the typing.

The current Record sentences in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) are quoted
only as premises and are not edited:

> A readout value is determined by record content alone.

> For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

Five exact statements locate the split.

1. **Two Green assignments.** For disjoint `S,T` and `r>0`,
   `|grad phi_S|(r)=I(S)/(4 pi r^2)` and
   `|grad phi_T|(r)=I(T)/(4 pi r^2)`. These are equal if and only if
   `I(S)=I(T)`.
2. **Swap symmetry of Record data.** The unordered pair of contents
   `{content(S), content(T)}`, the union collection `S∪T` when disjoint,
   and the scalar `I(S∪T)=I(S)+I(T)` are invariant under exchanging the
   labels `S↔T`. Content-only readout therefore supplies no ordered typing.
3. **Unequal-mass rejector.** Unit-atom collections with `I(S)=2` and
   `I(T)=1`, evaluated at `r=1`, give
   `|grad phi_S|(1)=1/(2 pi)` and `|grad phi_T|(1)=1/(4 pi)`. These are
   unequal. The Record union readout is `I(S∪T)=3` either way. The two
   possible Green assignments are not a function of the unlabeled Record
   data.
4. **Scoped negative.** There is no function of the unlabeled pair `{S,T}`
   — equivalently of `I(S∪T)` together with the unordered pair
   `{I(S),I(T)}` without an order — that equals the Newton source-linear
   gradient for a uniquely selected source. A declared typing
   `τ(source)=S` is a second object. Record does not type source versus
   test.
5. **Typed pairing remains an escape.** If a typing `τ` is supplied, the
   maps `B_τ=I(source)I(test)` and `F_τ=-I(test) grad(phi_source)` are
   well-defined formal maps. This note does not install `τ`, does not
   claim those maps are physical, and does not claim gravity is impossible.

A neighboring residual, not claimed here, is that the single scalar
`I(S∪T)` cannot equal a two-argument product. The object of this note is
source-versus-test typing.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The two source-linear Green assignments disagree on the unequal-mass witness, while Record additivity and content-only readout are swap-symmetric. Unlabeled Record data therefore do not select which collection is the Newton source. A declared typing remains a second object."
trace_class: negative_route_pruning
target_claim_id: newton_source_test_typing
target_blocker_text: "two-argument source–test pairing (Newton product residual)"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "A declared source/test typing, or another two-argument instrument, remains open; do not adopt axiom text."
conditional_surface_status: "exact for the unequal-mass Green split and Record swap symmetry; physical typing remains open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Work with finite record collections in the sense of the Record axiom. A
**collection** is a finite family of pairwise-disjoint records, each carrying
a formal rational strength. Scalar readout `I` is the sum of those
strengths. The empty collection has `I(empty)=0`. If `A` and `B` are
disjoint, additivity is

`I(A∪B)=I(A)+I(B)`.

The **content** of a collection is the unordered family of its record
payloads. Content-only readout means that any readout value is a function of
that content alone.

Fix two pairwise-disjoint collections `S` and `T`. The **unlabeled Record
data** of the pair are the unordered pair of contents `{content(S), content(T)}`,
equivalently the pair consisting of the union collection `S∪T` together with
the unordered pair of scalars `{I(S), I(T)}`. In particular the single
union readout `I(S∪T)=I(S)+I(T)` is part of that data and carries no order.

Newton objects are restated from the packet. The radial Green kernel and the
source-linear potential attached to a typed collection `X` are

```text
G(r) = 1/(4 pi r),
phi_X(r) = I(X) G(r) = I(X)/(4 pi r),
|grad phi_X|(r) = I(X)/(4 pi r^2).
```

The derivative is recomputed below; it is not imported as a bare number.
These formulae use one typed mass. They do not mention a second collection.

A **typing** `τ` is a declared ordered pair `(source, test)` of the two
collections. Writing `τ(source)=S` means that the Green assignment uses
`M=I(S)` and treats `T` as the complementary test collection. The opposite
typing is `τ(source)=T`. The axioms name neither ordered pair.

The unequal-mass witness used below is realized by unit-strength atoms
`S={s0,s1}` and `T={t0}`, so `I(S)=2`, `I(T)=1`, and `I(S∪T)=3`. The same
totals are obtained from lumped rational strengths with those sums. An
equal-mass control is the pair of unit atoms `S'={s0}`, `T'={t0}`.

The source-side mass-linearity lemma
[`G_NEWTON_MASS_LINEAR_POISSON_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-05-10.md`](G_NEWTON_MASS_LINEAR_POISSON_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-05-10.md)
is source-linearity of a Poisson potential in an already-typed source mass.
It does not assign which of two Record collections is that mass.

## Exact Target And Obligation Graph

**Exact target.** Decide whether unlabeled Record data of a disjoint pair
select which collection is the Newton source in the already-recorded
source-linear Green pairing, and record that a declared typing is a second
object.

| Obligation | Role | Disposition |
|---|---|---|
| pin content-only readout and disjoint additivity | premise | quoted from the axiom memo |
| pin Newton non-claim of `F = -M_test grad(phi)` and `M_source M_test` | premise | quoted from the Newton packet |
| recompute the two Green assignments from `G` | Theorem 1 | derivative of `phi_X=I(X)G` |
| show Record data are swap-symmetric | Theorem 2 | content, union, and `I` |
| exhibit the unequal-mass Green split | Theorem 3 | `1/(2 pi)` versus `1/(4 pi)` at `r=1` |
| rule out a function of unlabeled data as a unique source gradient | Theorem 4 | scoped negative |
| exhibit typed `B_τ` and `F_τ` as formal escapes | Theorem 5 | declared typing; not physical |
| derive a physical source/test typing or force law | autonomous closure | open |
| claim gravity is impossible, or that no pairing exists | non-claim | not attempted |

## Theorem 1 — Two Green Assignments

**Claim.** Let `S` and `T` be pairwise disjoint, and let `r>0`. The two
source-linear Green assignments are

`|grad phi_S|(r) = I(S)/(4 pi r^2)`,
`|grad phi_T|(r) = I(T)/(4 pi r^2)`.

These magnitudes are equal if and only if `I(S)=I(T)`.

**Proof.** The packet kernel is `G(r)=1/(4 pi r)`. Attaching the Record
readout of `S` as the source coefficient gives

`phi_S(r)=I(S) G(r)=I(S)/(4 pi r)`.

Differentiating in `r>0` yields

`d phi_S/dr = -I(S)/(4 pi r^2)`,

so `|grad phi_S|(r)=I(S)/(4 pi r^2)`. The same computation with `T` in
place of `S` yields `|grad phi_T|(r)=I(T)/(4 pi r^2)`. The two right-hand
sides are equal if and only if `I(S)=I(T)`, because `4 pi r^2>0`.

Both formulae use a single typed mass. Neither formula selects which of
`S,T` is that mass.

## Theorem 2 — Swap Symmetry Of Record Data

**Claim.** The unordered pair of contents `{content(S), content(T)}`, the
union collection `S∪T` when `S` and `T` are disjoint, and the scalar
`I(S∪T)=I(S)+I(T)` are invariant under exchanging the labels `S↔T`.
Content-only readout therefore supplies no ordered typing.

**Proof.** Content is an unordered family of record payloads, so

`{content(S), content(T)}={content(T), content(S)}`

as an unordered pair. Disjoint union of finite collections is commutative
as a set of records: the family of atoms of `S∪T` equals the family of
atoms of `T∪S`. Additivity and commutativity of rational addition give

`I(S∪T)=I(S)+I(T)=I(T)+I(S)=I(T∪S)`.

The content-only sentence says that a readout value is determined by
record content alone. Any readout of the unlabeled pair is therefore a
function of `{content(S), content(T)}`, or of the union content, or of
the commutative sum `I(S)+I(T)`. None of those objects is an ordered pair
`(source, test)`. An order `S` before `T` is extra data, not a Record
readout.

## Theorem 3 — Unequal-Mass Rejector

**Claim.** Take unit-atom collections with `I(S)=2` and `I(T)=1`, and
evaluate at `r=1`. Then

`|grad phi_S|(1) = 2/(4 pi) = 1/(2 pi)`,
`|grad phi_T|(1) = 1/(4 pi)`.

These are unequal. The Record union readout is `I(S∪T)=3` either way.
Therefore the two possible Green assignments are not a function of the
unlabeled Record data.

**Proof.** Realize `S` by two unit atoms and `T` by one unit atom, pairwise
disjoint. Additivity gives `I(S)=2`, `I(T)=1`, and

`I(S∪T)=I(S)+I(T)=3=I(T∪S)`.

Theorem 1 at `r=1` gives

`|grad phi_S|(1)=2/(4 pi)=1/(2 pi)`,
`|grad phi_T|(1)=1/(4 pi)`.

The identity `2/(4 pi)=1/(2 pi)` is cancellation in `Q(pi)`. The two
values are unequal because `2≠1`. Theorem 2 says the unlabeled Record data
of `{S,T}` equal those of `{T,S}`: same contents as an unordered pair, same
union, same scalar `3`. A function of those data therefore returns one
value on the pair. It cannot return both `1/(2 pi)` and `1/(4 pi)`. Hence
the two Green assignments are not a function of the unlabeled Record data.

The same split is obtained from lumped strengths with totals `2` and `1`.
The equal-mass control `I(S')=I(T')=1` makes the two Green magnitudes
equal, which is the “if and only if” direction of Theorem 1; it still
supplies no order if a later map needs a distinguished test factor.

## Theorem 4 — Unlabeled Record Data Do Not Select The Newton Source

**Claim.** There is no function of the unlabeled pair `{S,T}` —
equivalently of `I(S∪T)` together with the unordered pair `{I(S),I(T)}`
without an order — that equals the Newton source-linear gradient for a
uniquely selected source. A declared typing `τ(source)=S` is a second
object. Record does not assign source versus test.

**Proof.** Write `U({S,T})` for the unlabeled data of Theorem 2. Any
function `f` of `U({S,T})` is swap-invariant:

`f(U({S,T}))=f(U({T,S}))`.

The Newton source-linear gradient for a uniquely selected source would be
one of `|grad phi_S|` or `|grad phi_T|`, not both, and not an unordered
pair of those numbers. On the Theorem 3 witness those two numbers are
`1/(2 pi)` and `1/(4 pi)`, which are unequal. A swap-invariant `f` cannot
equal a uniquely selected one of them: selecting which collection is the
source is exactly the missing order.

The same obstruction is visible on the scalar data
`(I(S∪T), {I(S),I(T)})=(3,{2,1})`. Using the union scalar as the source
mass produces

`|grad phi_{S∪T}|(1)=3/(4 pi)`,

which equals neither `1/(2 pi)` nor `1/(4 pi)`. Using `min` or `max` of
`{2,1}` as a selector is an extra rule, not a Record readout. Declaring
that the first Python label is the source is a typing, not a theorem of
content-only additivity. Reading each collection separately still returns
an unordered pair of scalars and still needs an order to name one of them
the source. A geometric distinguished site — which collection sits at the
origin — is an extra lattice typing, not a Record sentence.

Therefore no function of the unlabeled pair equals the Newton
source-linear gradient for a uniquely selected source. The object that
would make the assignment is a declared typing `τ`. That typing is not
`I`, not content, and not the union.

## Theorem 5 — A Declared Typing Supplies Formal Maps, And Is A Second Object

**Claim.** If a typing `τ` is supplied, the maps

`B_τ = I(source) I(test)`,
`F_τ = -I(test) grad(phi_source)`

are well-defined formal maps. This note does not install `τ`, does not
claim those maps are physical, and does not claim gravity is impossible.

**Proof.** Given an ordered pair `(source, test)`, the scalars `I(source)`
and `I(test)` are ordinary Record readouts of the two collections
separately. Their product is then a number, and the source-linear field
`grad(phi_source)` of Theorem 1 is defined, so the displayed formulae are
ordinary algebra. On the Theorem 3 witness the two typings give two
different source fields,

`|grad phi_S|(1)=1/(2 pi)` versus `|grad phi_T|(1)=1/(4 pi)`,

and two well-defined formal forces built from those fields. The four
axioms do not name `τ`. The Newton packet already lists both
`F = -M_test grad(phi)` and the physical product law `M_source M_test` as
non-claims. This note does not reverse those non-claims, does not identify
`B_τ` or `F_τ` with a physical Record law, and does not close a force law.

The discriminating gate is only this: a declared typing makes those maps
writable; unlabeled Record data do not select the typing. Both sides are
exhibited. Gravity is not claimed impossible.

## Boundary And Non-Claims

The note does not:

- edit an axiom sentence, or argue that an axiom update is necessary;
- claim that gravity is impossible, or that no two-argument pairing can exist;
- install a physical source/test typing `τ`;
- identify `B_τ` or `F_τ` with a physical Record law;
- restore `F = -M_test grad(phi)` as a derived response rule;
- derive the physical product law `M_source M_test`;
- restate as a new claim the neighboring residual that a function of the
  single scalar `I(S∪T)` cannot equal a two-argument product;
- close gravitational coupling normalization, `G_N`, or a continuum
  Einstein equation;
- treat a geometric distinguished site, or a min/max selector, as a Record
  theorem.

The scope is the exact gap: Record does not type Newton source versus test.

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current Record content-only sentence | premise | quoted; no edit |
| current Record additivity sentence and `I(empty)=0` | premise | quoted; no edit |
| Newton kernel `G(r)=1/(4 pi r)` and source-linear `phi` | common objects | restated from the Newton packet; derivative recomputed |
| Newton non-claim of `F = -M_test grad(phi)` and `M_source M_test` | scope pin | quoted; not reversed |
| source-side mass-linearity lemma | neighboring landed linearity | source-linearity only; not a typing |
| unequal-mass Green split and swap symmetry | declared algebra | computed here |
| physical source/test typing | escape route | live, not derived |

The exact advance is a finite typing obstruction. Independent audit remains
required before any effective status may change. This note authors no audit verdict.

## Value Gate (V1–V5)

| # | Question | Answer |
|---|---|---|
| V1 | Named obstruction addressed? | The Newton packet lists `F = -M_test grad(phi)` and the physical product law `M_source M_test` as non-claims. This note isolates the missing typing that would even let those maps be written as functions of Record data. It does not call the upstream packet unratified. |
| V2 | New content? | Searched `origin/main` at `c45dd5ab30` by `git grep` for source-versus-test, source-test typing, and which collection is the source. Hits: the Newton packet is source-linear and lists the product/force as non-claims; the mass-linear Poisson composition lemma is source-linearity only. No landed swap-symmetry / unequal-mass typing obstruction appears on that commit. |
| V3 | Independently checkable? | No: textbook Green functions do not mention Record content-only swap symmetry or the axiom `I`. The runner recomputes the Green derivative, the two assignments, the union readout `3`, and the split `1/(2 pi)` versus `1/(4 pi)` in exact `sympy` arithmetic. |
| V4 | More than a restatement? | Yes. The exact `1/(2 pi)` versus `1/(4 pi)` split at `r=1` with union readout `3` is not a restatement of the Newton non-claim sentence. |
| V5 | One-step relabel? | No. The claim is not a corollary of source-linearity alone — that uses an already-typed `M` — and is not a restatement of the Newton non-claim sentence. The closest landed wording is the non-claim list; this note supplies the rejector. |

## No-Go Discipline Gate (Theorem 4 only)

The negative claim is restricted to: unlabeled Record data do not select
which collection is the Newton source. The gate does not ship a global
non-existence theorem against pairings, and it does not ship a claim that
gravity is impossible.

### N1 — materially distinct routes

| Route | Exact attack | Result | Marker |
|---|---|---|---|
| use `I(S∪T)` as the source mass `M` | set `|grad phi|=3/(4 pi)` at `r=1` | fails the unequal-mass split: `3/(4 pi)` equals neither `1/(2 pi)` nor `1/(4 pi)` | **ATTEMPTED** |
| use `min` or `max` of `{I(S),I(T)}` | declare the heavier (or lighter) collection to be the source | extra selector, not a Record readout; see N7 | **ATTEMPTED** |
| declared label order | take the first Python tuple slot as source | a typing, not a Record theorem; swap changes `grad_magnitude` when the masses differ | **ATTEMPTED** |
| separate content-only readouts | read `I(S)` and `I(T)` each by content | still an unordered pair; an order is needed to assign source versus test | **ATTEMPTED** |
| geometric distinguished site | take whichever collection sits at the origin as source | extra lattice typing, not a Record sentence | **ATTEMPTED** |
| restore `F=-M_test ∇φ` by fiat | write the force/source response rule as if derived | Newton non-claim, not derived | **ATTEMPTED** |
| add a typing sentence to the axiom memo | put `τ` into Record | not attempted; N6; no axiom sentence is edited | **NOT ATTEMPTED** |

### N2 — wall independence

Theorem 4 closes only unique selection of a Newton source from unlabeled
Record data. It does not close a later declared typing, a two-argument
instrument, a physical product law, or a force-response bridge. Those walls
remain independent.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| finite disjoint collections `S,T` with rational strengths | declared Record objects |
| scalar `I` and content-only readout | quoted axiom sentences |
| Green kernel `G(r)=1/(4 pi r)` | restated Newton object |
| source-linear `phi_X=I(X)G` | restated Newton object; `X` already typed |
| unlabeled pair `{S,T}` and `{I(S),I(T)}` | explicit hypothesis of Theorem 4 |
| declared typing `τ` | live escape; not derived |
| min/max selector or geometric origin | extra selectors; not Record |
| physical product or force law | Newton non-claims; not reversed |

### N4 — source residual matching

| Source | Exact residual used | Match and limit |
|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | content-only sentence; additivity and `I(empty)=0` | quoted as premises only; no edit |
| [`docs/NEWTON_LAW_DERIVED_NOTE.md`](NEWTON_LAW_DERIVED_NOTE.md) | source-linear kernel algebra; non-claims `F = -M_test grad(phi)` and the physical product law `M_source M_test` | quoted; derivative recomputed; non-claims not reversed |
| mass-linear Poisson composition lemma | source-linearity in an already-typed `M` | neighboring landed linearity; not a typing |

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | named collections with totals `2` and `1`, and the two Green numbers `1/(2 pi)` and `1/(4 pi)` | no classification of every two-collection map |
| per site | collection-level readout and a radial kernel; no composite carrier | no bonded-pair or lattice-site theorem |
| per mode | source-linear radial Green assignments, not spectral modes | no harmonic-mode exhaustion |
| per block | typing obstruction and the displayed formal escape only | no dynamics, `G_N`, or Einstein equation |
| lattice-wide | checked and not executed | no lattice-wide no-go against pairings or gravity |

The obstruction is per-pair / declared unequal-mass witness; it is not
lattice-wide.

### N6 — live partial-closure paths

1. A later derivation that supplies a declared typing `τ` from some
   already-landed instrument other than unlabeled Record data.
2. A later two-argument instrument that is not a function of `{S,T}`
   without order.
3. A content-only bridge that is nonetheless ordered by some extra
   landed structure, if and when that structure is derived.
4. Leaving the Newton force and product sentences as non-claims.

The quoted Record and Newton sentences already name content-only readout,
additivity, the source-linear kernel, and the non-claim of the force and
product maps. A declared typing remains a second object. No axiom sentence
is edited here. This note does not argue that an axiom update is necessary.

### N7 — hostile steelman

> Call the heavier collection the source. Then `I(S)=2` is selected by
> `max{I(S),I(T)}`, the Green assignment is uniquely `1/(2 pi)`, and
> Theorem 4 is empty.

**Answer.** That is a declared selector (max-`I` typing). Record does not
supply it: content-only additivity returns the unordered pair `{2,1}` and
the sum `3`, not a “heavier-is-source” rule. The same selector still fails
when `I(S)=I(T)` if one still needs an ordered test factor: `max` and `min`
then coincide, and the order `(source, test)` remains extra data. Theorem 4
is the absence of a unique source from unlabeled data, not the absence of
every conceivable extra selector.

### N8 — cross-cycle echo

The Newton packet’s non-claim list already withholds
`F = -M_test grad(phi)` and the physical product law `M_source M_test`.
The mass-linear Poisson lemma is source-linearity in an already-typed
mass. The present negative is a different residual: unlabeled Record data
do not select which of two collections is that mass. The unequal-mass
split is not a restatement of those parent sentences. The positive escape
(Theorem 5) does not cancel the packet non-claims; it records that a
declared typing would make the maps writable as formal algebra.

**Gate disposition.** PASS for the scoped typing obstruction. FAIL / DO NOT SHIP for "gravity is impossible" or "no two-argument pairing can exist."

## Primary Runner

[`scripts/record_does_not_type_newton_source_versus_test_2026_08_13.py`](../scripts/record_does_not_type_newton_source_versus_test_2026_08_13.py)
recomputes the two Green assignments from `G`, the Record swap symmetries,
the unequal-mass split `1/(2 pi)` versus `1/(4 pi)`, the unlabeled-data
obstruction, and the typed formal escape, all in exact `Fraction`/`sympy`
arithmetic. Identity gates call `grad_magnitude(mass, radius)` defined as
`mass / (4 pi radius**2)`. Replacing `grad_magnitude` by a swap-invariant
rule that always uses `I(S)+I(T)` must fail the unequal-mass split.
Replacing `grad_magnitude` by the product law `I(S)I(T)/(4 pi r^2)` must
fail source-linearity of the Newton packet. A declared “always `S` is
source by label order in the Python tuple” is a typing, not a Record
theorem: the swap of the two collections must change `grad_magnitude`
exactly when the masses differ.
