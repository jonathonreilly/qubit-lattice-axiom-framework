---
claim_id: admissibility_record_continuation_refinement_conditional_bounded_theorem_note_2026-07-13
claim_type: bounded_theorem
claim_scope: "Under an explicit site-tagged immutable-extension representation, distinct same-site record successors have disjoint syntactic extension cones; finite supported chains refine monotonically under a common fixed one-record append schedule. The Admissibility distribution supplies supported lock outcomes conditional on formation, so a singleton continuation map that omits a supported outcome is rejected rather than an alternative realization of the same rule. The axioms still do not supply a physical state-successor relation or post-record operation-algebra restriction. The exact route-two sentence remains a composite named condition, not an axiom edit."
upstream_dependencies:
  - minimal_axioms
runner: scripts/frontier_admissibility_record_continuation_refinement_2026_07_13.py
---

# Admissibility and Record-Continuation Refinement: Conditional Bounded Theorem

**Date:** 2026-07-13
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note does not set or
forecast an audit verdict, edit an axiom or primitive, or change any audit
surface.
**Primary runner:**
[`scripts/frontier_admissibility_record_continuation_refinement_2026_07_13.py`](../scripts/frontier_admissibility_record_continuation_refinement_2026_07_13.py)

## Result

The decisive question has a split answer.

At the **site-tagged immutable-history level**, a useful conditional theorem
closes. If a state has two formation-successors that add different record
contents at the same previously open site, their immutable partial-map
extension cones cannot reconnect. Any common extension would have to retain
both different contents at that site. The certificate is local to one site,
and finite supported chains refine their record-content partition monotonically
under a common fixed one-record append schedule.

That result is **not yet an unconditional consequence of Record**. It uses an
explicit representation condition: a formed record remains tied to its
original site and content in every later history state. The current Record text
says records are permanent but does not separately state site immobility or a
formation-successor relation. A migrating-record semantics remains an untested
alternative. The theorem below is exact inside the site-tagged immutable model.

At the **physical-continuation level**, the desired result is not presently a
theorem. Admissibility gives a probability distribution over the local
possibility domain, and Record makes its support the possible lock outcomes
conditional on formation. It therefore does not permit a purported same-rule
formation law to discard a supported outcome. What remains absent is the
physical state-successor relation, its temporal or causal realization, and any
change to the physical operation algebra when a record forms.

At the **quantum operation-algebra level**, history nonreconnection is not yet
a physical superselection theorem. On the runner's separately supplied finite
tensor-product comparator, the full matrix algebra has scalar center. A
block-preserving algebra has record sectors only after the block-preserving
restriction is supplied. The current axiom memo explicitly says that
Admissibility is not dynamics and supplies neither a transfer operator nor
physical persistence dynamics.

The history result is order-theoretic. It proves neither branch orthogonality
nor decoherence, and a one-time block projection is not permanence.

So the strongest honest conclusion is:

- **proved conditionally:** in the explicit site-tagged immutable-extension
  model, distinct same-site record contents have disjoint syntactic extension
  cones; under a common fixed one-record append schedule, finite supported
  chains refine monotonically;
- **supplied at outcome level:** conditional on formation, the Admissibility
  distribution supports the possible contents that Record may lock; a
  same-rule continuation model may not erase one of those supported outcomes;
- **not derived now:** site-tagged physical successor semantics or dynamic
  activation of a record-preserving physical operation algebra;
- **not extensionally specified on the checked authority surface:** the axiom
  and primitive foundation plus the adjacent rule/realization notes
  checked by the runner name no physical rule table, closure operator, or
  rule-to-successor bridge.

This narrows, but does not settle, the proposed new physics. The live theorem
conditions are (1) a context-scoped bridge from an **available alternative** to
a **physical continuation**, and (2) post-record preservation of the
site/content distinction by every later physical continuation or operation.
Whether those conditions derive, remain permanent theorem imports, or require
foundation text is still open.

## Exact Named Condition

This named condition is the working route-two target under test and is not an
axiom edit:

> When a record forms at a site, the site's admissible local possibilities separate into law-admissible continuations that do not reconnect.

It is consumed verbatim here as the condition under test. Nothing in the
[`live axiom memo`](MINIMAL_AXIOMS_2026-06-29.md) is changed.

The condition contains three logically different pieces:

1. **outcome law:** Admissibility assigns the probability distribution, hence
   its support, from the nearest-neighbor conditions;
2. **state lift:** supported lock outcomes are represented as physical
   formation-successor states in the stated context;
3. **separation:** successor states carrying different same-site record contents
   have no later common continuation.

The current axioms supply item 1 and, read with Record, supported lock outcomes
conditional on formation. They do not separately define item 2 as a physical
state relation. Item 3 follows once that state lift and site-tagged
immutable-extension semantics are supplied. If "do not reconnect" is intended to exclude quantum
cross-sector operations, then a fourth piece -- persistent restriction of the
physical operation algebra -- is also unretired.

The working sentence is therefore a **composite condition**, not the minimum
atom proved necessary by this attempt. Its plural "possibilities" is read as
the support of the conditional lock-outcome distribution. The nonreconnection
theorem itself needs two distinct supported successor states, whose physical
state-level lift remains explicit. The exact sentence remains held verbatim
here for the theorem candidate; this decomposition prevents the state-lift and
preservation requirements from being hidden under the word "separate."

## Landed Premise Surface

Only the following current axiom content is load-bearing:

```text
There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Records form.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

A state is a configuration of records.
```

The same memo's boundary is also controlling:

```text
Admissibility is not a dynamics axiom.
```

It explicitly leaves transition operators, update laws, formation rules,
record-production dynamics, and physical persistence dynamics outside the
axiom content.

Context-only corpus checks agree with that boundary:

- the local finite-atom note says that the axioms name the rule but do not
  supply its content, and labels its concrete rule as a bounded toy instance;
- the covariance-classification and saturation notes classify supplied rule
  models without identifying the physical rule;
- the tick and protocol notes name rule-to-dynamics realization predicates as
  conditions rather than derivations;
- the fresh-site permanence note explicitly treats site-tagged monotone record
  identity as a representation condition and says the bare axiom does not
  separately state an immobility law;
- the bootstrap-continuation note derives nonemptiness of the first menu and
  conditional flip-closure, but labels its concrete rules as toys, leaves
  formation selection downstream, and does not prove a physical successor-state
  relation or physical preservation.

Those adjacent notes are not used as theorem premises. They are checked only
as boundary surfaces so that a toy rule or conditional representation is not
silently treated as the physical rule or as axiom content.

## Conditional Site-Tagged Immutable-Extension Theorem

The theorem uses this explicit representation condition:

> **Site-tagged immutable-extension semantics.** A formed record is
> individuated by its site and locked content. Every later history state
> preserves that same site/content pair.

This is a named condition of the theorem candidate. Record uniqueness and
permanence motivate it, but the axioms do not independently supply a successor
relation or forbid a permanent record from migrating.

Let a state `C` be a partial map from lattice sites to locked local
possibilities. Write

```text
C <= D
```

when `D` agrees with `C` at every site recorded in `C`. For an open site `x`
and possibility `p`, write

```text
C[x := p]
```

for the state that preserves all of `C` and adds the record `(x,p)`.

Define a one-record immutable formation extension to have that form. More
generally, call `L` an immutable formation extension of `C` at `(x,p)` when

```text
C <= L    and    L(x) = p.
```

Such an extension may add other fresh records simultaneously. The proof below
uses only those two displayed conditions. The runner exhausts the one-record
case and checks one collateral-record fixture. Neither occurrence nor
permanence supplies the existence, granularity, or physical law of these
extensions.

### Theorem 1 -- sibling nonreconnection

Suppose `p != q`, and let `L` and `R` be law-admissible formation-successors of
`C` satisfying

```text
C <= L,  L(x) = p,    and    C <= R,  R(x) = q.
```

Then there is no state `D` with `L <= D` and `R <= D`.

**Proof.** Under the named site-tagged semantics, the first extension requires
`D(x)=p`; the second requires `D(x)=q`. Since `p != q`, no such partial map
exists. The contradiction is witnessed at `x`; no global comparison, clock,
foliation, probability, or infinite-volume limit is used. QED.

This excludes a common **syntactic immutable extension** at every later depth.
Any physical future cone defined as a subset of that syntactic cone is also
disjoint. The theorem does not prove that either sibling exists, that the
syntactic extensions are physical, or that records are site-immobile.

### Theorem 2 -- conditional dynamic refinement

Fix a finite ordered list of distinct sites. At each stage, require every
supported chain to use the same next site and to add exactly one record there.
Under branch support and site-tagged immutable-extension semantics, group the
finite chains by their accumulated content prefix on that fixed schedule. Each
stage refines the preceding partition: histories whose prefixes first differ
at the scheduled site conflict there by Theorem 1, while every older prefix is
preserved. The number of nonempty blocks is nondecreasing. It grows strictly at
a stage exactly when at least one old block supports at least two contents at
that stage's common site. In the explicit independent binary full-support
model used by the runner, `n` recorded sites give `2^n` potential blocks. A
constraint such as global equality can leave the count at two after the first
split, so per-record doubling is not a general theorem.

"Enlarging" here means a nondecreasing refinement of finite, fixed-schedule
record-content classes and a longer invariant label on a separately supplied
realized history.
It does **not** mean that `2^n` worlds are jointly realized, or that every record
event strictly increases the number of nonempty classes. This theorem does not
supply the realized history or its selection mechanism. A
finite `N`-site region also saturates after `N` records; unbounded refinement
requires fresh support or another separately derived capacity mechanism.

### Theorem 3 -- conditional covariance and local composition

If a physical successor-state lift carries the support of the same fixed
distribution at every site and transforms with that proper-cubic-covariant
support, lattice motions map a
formation extension at `x` to a formation extension at the moved site. The
separation proof is invariant because it uses only equality of the site and
inequality of its two contents. When two fixed distinct-site records are
compatible, their partial-map union is order-independent. Competing appends at
one site are incompatible.

The conditional in the first sentence is load-bearing. Covariance of the menu
does not by itself state covariance -- or even existence -- of a successor
relation. Partial-map union does not prove physical formation commutation:
after one append, the other's nearest-neighbor menu may change. Physical
commutation needs a separate compatibility theorem. Disjoint dependency
supports are one sufficient route, but are not necessary; two laws may overlap
on read-only data and still commute. Overlapping quantum record refinements
require a compatibility or causal-order law as well.

## Rejected Historical Same-Rule Witness

The pre-revision argument tried to hold a set-valued availability table fixed
while comparing a branch-complete continuation map with a singleton map. That
is not a same-rule witness under the current axiom. The rule is
distribution-valued over Qubit's one-site possibility domain. On a finite
context whose distribution has support `{0,1}`, both values have positive
probability; read with Record, both are supported lock outcomes conditional on
formation. A singleton map that omits one value therefore realizes a different
rule or fails to realize the stated distribution.

The runner retains the finite `3^6 = 729` pattern and 24-rotation construction
only as a rejector. It verifies that the two maps are distinct for a separately
supplied historical set-valued interface and then verifies that the singleton
map is incompatible with the current probability-distribution rule. No
full-domain same-rule lift, branch-completeness independence conclusion, or
physical copying claim survives this rejection.

## Quantum Operation-Algebra Boundary

On the runner's separately supplied finite `N`-qubit tensor-product comparator,
the unrestricted algebra is `M_(2^N)(C)`, whose center is scalar. The
foundation supplies the one-site `M_2(C)` presentation, not this multi-site
tensor-product carrier; the comparator is not a framework premise. Finite
unitary conjugation preserves both that full algebra and its scalar center. For
a record projector `P`, the block algebra

```text
B_P = {X : [X,P] = 0}
```

has a nontrivial center only after that restricted observable algebra -- or
algebra containing the allowed unitary operators -- is supplied. General
physical channels are maps constrained separately below. The conditional
expectation

```text
E_P(X) = P X P + (1-P) X (1-P)
```

is a supplied exact projection onto `B_P`. It is idempotent, fixes `P`, deletes
cross-block operators, is covariant when `P` transforms with the record
content, and composes algebraically with the corresponding map on a disjoint
factor. It is not a derivation of the restricted algebra and not a
superselection theorem. One application does not prevent a later
sector-changing unitary. Imposing it before formation also deletes pre-record
interference, so a fixed restriction is not a formation mechanism.

These are exact finite algebra statements. They show what a physical lift of
history separation would look like, and why it is not free:

- Admissibility does not say that `E_P` is a physical channel;
- Record does not define the full algebra of possible quantum operations;
- physical permanence would require every future admissible operation or
  channel to preserve the record block, for example `Phi*(P)=P`;
- deriving that post-formation invariant operation class is the route-two
  target. If `E_P` itself is activated, it is a supplied exact dephasing law,
  not derived superselection;
- none of this chooses a realized block, supplies weights, or sets a rate.

Accordingly, the site-tagged history reading of the named condition is a
conditional order theorem, while its strong physical-operation reading remains
open.

### Infinite-volume entry boundary

Exact superselection sectors may occur as inequivalent representations or
tail/topological charges even when an abstract quasi-local algebra has trivial
center. This runner constructs no such sector. For formation initiated in a
bounded region, finite-range finite-time propagation changes only a finite or
quasi-local causal region and does not by itself alter data defined only by
agreement outside every finite region. Known infinite-sector routes therefore
need semi-infinite/global support, an infinite-time or thermodynamic limit, or
a separately supplied representation-changing/nonunitary mechanism.

Infinite-volume permanence remains a live route. Causal finite-time entry into
that sector is an independent theorem, not something the spatially infinite
lattice supplies for free.

Context-only primary comparators, not framework premises: the original
[Lieb--Robinson bound](https://doi.org/10.1007/BF01645779), a modern
[quasi-locality treatment](https://arxiv.org/abs/1810.02428), and
[infinite-plane toric-code sectors](https://arxiv.org/abs/1012.3857).

### No decoherence theorem

Theorem 1 is an order-theoretic incompatibility theorem, not a decoherence
theorem. It supplies no branch vectors, class operators, record projectors in a
history Hilbert space, off-diagonal density-matrix bound, or decoherence
functional. A consistent-histories lift would have to prove, on separately
supplied state and dynamics,

```text
D(alpha,beta) = Tr(C_alpha rho C_beta^dagger) = 0    for alpha != beta,
```

or state an approximation bound. The full finite algebra still contains a
coherent inverse unless a physical-operation theorem excludes it.

Context-only primary comparators: [Griffiths' consistent-histories
construction](https://link.springer.com/article/10.1007/BF01015734) and
[Hartle's strong-record formulation](https://arxiv.org/abs/1608.04145).

## Bell And Contextual-Scope Discriminator

As an ancillary control, the runner compares deterministic local assignments
to four CHSH settings with a separately supplied context-indexed no-signaling
target. Under measurement independence and local factorization, the joint
assignments satisfy `|CHSH| <= 2` and cannot reproduce the supplied
`2 sqrt(2)` target.

This does not follow from the named continuation condition, derive the target
probabilities, or rule out contextual, nonlocal, measurement-dependent, or
global-history completions. It is a discriminator only: a physical
continuation proposal must state its setting, locality, and intervention
semantics before the appropriate Bell control can be applied.

Context-only primary comparator: [Fine's joint-distribution
equivalence](https://doi.org/10.1103/PhysRevLett.48.291).

## Direct Answer To The Decisive Question

Does the current nearest-neighbor Admissibility surface generate a local,
covariant, dynamically enlarging set of nonreconnecting continuation sectors?

**Not from the current supplied surface.** Admissibility supplies the local
covariant lock-outcome distribution conditional on formation. Under separately named site-tagged
immutable-extension semantics, distinct supported same-site record contents
have no common syntactic extension. Under the additional common fixed
one-record append schedule of Theorem 2, finite supported content partitions
are non-coarsening. The axioms do not generate that physical state-successor
semantics, schedule, or a post-record physical operation algebra. Nor do they
force strict class growth at every formation event; within the fixed schedule,
strict growth requires at least two supported contents in an existing class.

The already-postulated fixed rule cannot currently be evaluated extensionally
from the checked authority surface because no exact predictive specification
or physical-equivalence theorem is supplied. The axiom and primitive foundation give only
locality, covariance, determination, and nonconstant variation constraints.
The adjacent rule/realization notes checked by the runner explicitly keep
their concrete tables or bridges toy, supplied, or conditional. This is enough
to test consequences common to all allowed rules; it is not an extensional
physical table from which to compute connected components or a fixed algebra.

That finding does not establish that route two is impossible. The unprinted
physical rule could be an extensive, monotone, confluent closure or could
induce a constrained operation algebra. Supplying or deriving its extensional
content could help close the state-lift and physical-preservation residuals. The current
axiom sentences alone do not force that outcome.

## Effect On The TOE Lanes

| lane | what this bounded theorem candidate supplies | what remains open |
|---|---|---|
| fixed reality | order-theoretic incompatibility of separately supplied site-tagged immutable successors | physical successor semantics, physical preservation, selector mechanism |
| probability | the axiom supplies the conditional lock-outcome measure; this note supplies only a fixed-schedule finite partition of conditional history chains | general event algebra, frame extension, prepared-state identification, realized draw, and formation site/rate |
| time | record-inclusion order inside the supplied extension model | physical successor dynamics, dependency relation, trigger, rate, duration |
| arrow | fixed-schedule monotonicity inside that representation, not a thermodynamic arrow | site identity, general physical event order, low-entropy boundary, entropy functional, thermodynamic law |
| causality | a set-theoretic local conflict certificate and order-independent union of fixed compatible appends | physical formation commutation, dependency support, finite causal activation, continuum cone |
| matter | no result about physical coherence | Hamiltonian/action, decoherence control, and a persistent restriction that preserves unresolved coherence |
| gauge / covariance | conditional proper-cubic spatial covariance of the finite successor witness | physical pointer/content selection, gauge covariance, Lorentz recovery, CPT |
| gravity / capacity | finite label-count bookkeeping only | conserved resource, support renewal, source identity, field/lapse law, equivalence principle |
| cosmology | no result | initial boundary, expansion dynamics, vacuum/dark-sector content |
| Wigner / friend | no result; coherent reversal remains in the full finite algebra | derivation that the inverse is physically inadmissible, or relational consistency |
| Lorentz / CPT | no result | continuum symmetry and transformation of the formation/preservation law |
| mass / counting / chirality | no new consequence | possibility individuation, conjugate counting, exchange sign, mass relations |

The theorem retires only the order-theoretic question of whether two
conflicting site-tagged immutable record maps have a common extension. It does
not retire quantum recombination, coherent erasure, decoherence, or the
physical-superselection wall.

## Axiom Need At This Stage

No axiom edit is justified by this bounded theorem candidate.

The exact target remains verbatim as the working route-two condition,
but this attempt does **not** establish that it is minimal or ready for axiom
text. It bundles an outcome-to-state successor lift with operational preservation,
and gives "do not reconnect" both a weak partial-map reading and a strong
physical reading. Only the weak reading is proved, and only under the explicit
site-tagged immutable-extension condition.

The next derivation target is now smaller and testable:

1. derive site identity and a physical successor relation, or keep the
   site-tagged immutable representation explicit;
2. give the fixed Admissibility rule extensional or retained-derived content;
3. derive a physical successor-state representation of its supported
   lock outcomes in the stated formation context;
4. derive that every later physical operation preserves formed record content
   without suppressing pre-record coherence.

If those land, the working sentence can become theorem text and no addition is
needed. If they fail after the physical rule and operation class are genuinely
specified, the surviving foundation candidate -- or permanently named
conditional input -- is the context-scoped outcome-to-state continuation and
post-record preservation bridge. Failure alone does not prove axiom necessity.
The realized draw and formation site/rate remain downstream
even if that bridge closes.

## No-Go Discipline Gate

**Status: `FAIL / DO NOT SHIP` for the scoped negative inference below.** The
positive site-tagged extension and refinement
theorems remain bounded results. The broader claim that the framework's
unprinted physical rule cannot close route two is not made; the negative
disposition is `partial-narrowing` with a named live steelman.

The candidate negative tested here was:

> The checked foundation text contains no physical state-successor rule or
> physical operation-class clause.

This is a checked source-surface fact, but the route-closure packet lacks
retained authority. The negative is therefore not shipped as a no-go. It is
not a full-model impossibility claim or proof that new axiom text is required.

### N1 -- alternative routes

| route and attempted attack | marker | outcome against the scoped negative | evidence and authority status |
|---|---|---|---|
| recover a successor law by reading the foundation and approved-premise registry as executable dynamics | ATTEMPTED | fails at the source-text level: the memo expressly separates Admissibility from dynamics and the approved primitives add no successor or operation rule | `MINIMAL_AXIOMS_2026-06-29.md#relation-to-dynamics-and-kinetic-branch-selection`, approved foundation/meta; registry check A1-A18 |
| read Record permanence as site-tagged immutable extension | ATTEMPTED | succeeds conditionally for weak syntactic nonreconnection, so the note narrows rather than rejects route two; site identity remains explicit representation data | Theorem 1 and C1-C10, paired unaudited runner evidence; `RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md#inputs-and-boundaries`, with current status left pipeline-derived |
| try to vary successor support while holding the distribution-valued rule fixed | ATTEMPTED | fails: on the finite full-support contexts, the singleton map omits a supported lock outcome and is not a realization of the same current rule | B1-B16, paired unaudited runner rejector |
| use the unrestricted finite quantum operation algebra as the physical sector supplier | ATTEMPTED | fails on the separately supplied finite tensor-product comparator because the full matrix algebra has scalar center and later coherent reversal remains available | E1, E12-E13, paired unaudited runner evidence |
| impose a block-preserving algebra or conditional expectation after formation | ATTEMPTED | succeeds conditionally, but the operation class and its activation are supplied rather than generated by Admissibility | E2-E11, paired unaudited runner evidence; three-route R2F, historical context only |
| treat one supplied conditional expectation as permanent physical superselection | ATTEMPTED | a later sector-changing unitary reopens the block, so one application is not an all-future operation restriction | E4-E6 and E12, paired unaudited runner evidence |
| identify order-theoretic record classes with decoherent histories | ATTEMPTED | fails at the typed level because no state, class operators, or decoherence functional is present | no-decoherence boundary above; external histories papers are context only |

The five-route threshold is exceeded, but only the source-text row has approved
authority and the other route outcomes rely on current or unaudited evidence.
Because N1 requires retained authority for every closed route, **N1 fails**;
none of those outcomes is promoted to retained authority.
Infinite-volume tail sectors and constrained local-code dynamics remain live
steelman routes against any broader no-go and are therefore excluded from the
scoped-negative route table rather than mislabeled as ruled out.

### N2 -- wall independence

The route-two residual collapses to two independent bridges:

- **context-scoped successor realization/support:** what the physical
  continuation relation is, its domain/context, and which available contents it
  supports;
- **post-record physical preservation:** why every later physical continuation
  or operation preserves formed record content, including the site/content
  identity needed by the partial-map theorem.

| pair | first closes second? | second closes first? | independent after collapse? |
|---|---:|---:|---:|
| outcome-to-state successor realization / preservation | no -- a branching successor graph may still admit later overwrite, migration, or coherent reversal | no -- a fixed preserving algebra may exist from the start without defining physical formation-successor states | yes |

The Record axiom already types an actual present record as locking one
possibility. The realized draw and formation site/rate,
metric time, and capacity are downstream TOE lanes; they are not extra atoms of
this route-two theorem residual.

### N3 -- hidden-wall scan

The mandated phrase scan was run over the result, proofs, boundaries,
TOE table, axiom-need section, and verification text, excluding this checklist's
quoted search vocabulary:

```text
we assume | by construction | as is standard | the framework provides |
bridge context | background | naturally | obviously | standard QFT |
registered | canonical
```

No proof-body hit remains. The verification phrase "approved-primitive
registry" names the machine-readable foundation register and is cited at A17;
it is authority bookkeeping, not a physical premise. The earlier prose word
"naturally" was removed rather than used to carry the physical state-lift.
No hidden condition was promoted, so the two-wall N2 count is unchanged.

The close-variant semantic scan also classified the following terms rather
than letting them act as free synonyms:

- `continuation` is a site-tagged syntactic state extension only in the weak
  theorem; its physical relation remains open;
- `physical continuation` requires the missing successor/operation bridge;
- weak partial-map objects are called record-content classes or syntactic
  extension cones; `sector` in the strong sense requires a named operation
  algebra or representation;
- `dynamic enlargement` means partition refinement along formation events, not
  a supplied clock or rate;
- `covariant` means lattice-motion covariance; no internal pointer action is
  smuggled in;
- the runner's one-record append is a special-case representation, not a claim
  that simultaneous multi-record formation is impossible;
- order-independent partial-map union is not physical commutation of formation
  channels;
- distribution support is outcome-level and does not itself define a temporal
  state-successor graph;
- finite `M_(2^N)(C)` is a separately supplied runner comparator, not a
  foundation-provided multi-site tensor-product carrier;
- references to the fixed rule mean the framework's existentially fixed rule,
  not a runner witness or a licensed-surface representative.

No wavefunction ontology, Hamiltonian, transition kernel, probability, Born
weight, clock, foliation, resource law, environment trace, or infinite-volume
sector is imported into Theorems 1-3.

### N4 -- residual matching

| cited witness, exact location, status | witness residual | residual used here | match? |
|---|---|---|---:|
| `MINIMAL_AXIOMS_2026-06-29.md#L105`, approved foundation/meta | the distribution is expressly separated from transition, formation-site/rate, and persistence dynamics | checked text supplies neither physical state-successor realization nor physical preservation | yes |
| `RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md#L76`, status read from the pipeline rather than asserted here | site-tagged monotone identity is explicit representation data; migration is untested | site-tagged identity is a condition here | yes |
| `RECORD_LOCAL_FINITE_ATOM_AVAILABILITY_NARROW_THEOREM_NOTE_2026-06-17.md#L125`, unaudited | the concrete local rule is a declared toy because physical rule content is unsupplied | no toy table is identified with the physical rule | yes, context only |
| `TICK_ADMISSIBILITY_REALIZATION_BRIDGE_CLAUSE_TO_PREDICATE_NARROW_THEOREM_NOTE_2026-07-10.md#L15`, unaudited | tick-to-Admissibility realization is not derived | a static menu is not treated as a physical successor process | yes, context only |
| `PROTOCOL_ADMISSIBILITY_3D_REALIZATION_BRIDGE_AND_WORD_DISPERSIVENESS_NARROW_THEOREM_NOTE_2026-07-10.md#L37`, unaudited | physical rule-to-protocol identification is not derived | no protocol is used as the successor law | yes, context only |
| `BOOTSTRAP_CONTINUATION_AVAILABILITY_NONEMPTY_FREE_ORBIT_REDUCTION_PROPAGATION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-04.md#L7`, unaudited | first-support nonemptiness and conditional flip-closure; toy rules do not determine the fixed rule | outcome support does not supply a temporal successor graph or operation preservation | yes for the boundary; not proof of this negative |
| `RECORD_FORMATION_APPEND_CERTIFICATION_BOUNDED_NOTE_2026-07-04.md#L52`, unaudited | occurrence does not supply a total formation rule, weight, or rate | only the formation-rule overlap is relevant | partial; not counted as independent support |
| `SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md#L186`, unaudited | record order supplies neither rate nor axis label | state-successor realization/preservation | no; used only to prevent a time overclaim |
| `work_history/repo/review_feedback/RECORD_FORMATION_THREE_ROUTE_ASSUMPTIONS_EXERCISE_AND_AXIOM_TARGET_NOTE_2026-07-13.md#L169`, historical source | route two needs a continuation relation, allowed-operation algebra, and activation | the same support/preservation pair | yes, context only |
| [paired runner B/C/E/F](../scripts/frontier_admissibility_record_continuation_refinement_2026_07_13.py), current unaudited source evidence | rejected historical support-map variation, syntactic separation, finite algebra, scoped Bell control | exactly the bounded computations claimed here | yes |

After dropping the two non-matches and the partial rate witness, the scoped
claim still has the approved source-text boundary plus its paired-runner exact
typed witness. The unaudited adjacent notes are corroborating context, never
promoted authority.

The finite full-center result does not exclude constrained, represented, weakly
closed, topological, or quasilocal algebras. The Bell block addresses only the
supplied target under deterministic-local joint-assignment premises; it is not
evidence for branch support itself.

### N5 -- rhetoric and resolution audit

| negative phrase | per-element / site | per-mode | per-block | lattice-wide / continuum | retained wording |
|---|---|---|---|---|---|
| a singleton map can realize the same full-support distribution | all 729 six-neighbor patterns on the common one-neighbor domain; rejected | not tested | finite typed support maps only | no physical infinite rule tested | **rejected historical witness, not a current nonuniqueness theorem** |
| conflicting immutable siblings do not reconnect | exact one-site contradiction; yes | not a mode claim | all five-site partial maps exhausted; collateral fixture checked | proof extends to any partial-map lattice only under site-tagged immutability; no physical cone claim | **no common syntactic immutable extension** |
| the unrestricted algebra has no nontrivial record center | not a site-menu statement | not tested as a field mode decomposition | exact for finite full matrix algebras | false as a universal inference: infinite/tail representations remain open | **finite full-algebra scalar center** |
| a one-time block projection is not permanence | exact later-flip rejector | not tested | two-qubit block example | no all-future infinite operation class tested | **one tested projection does not impose all-future preservation** |
| bounded local formation does not automatically enter a tail sector | no framework computation | no | no | literature-motivated boundary only; entry theorem unproved | **infinite-volume route remains open** |
| deterministic local joint completion misses the supplied CHSH target | per setting/outcome exact | no field modes | two-setting/two-outcome table | no claim about contextual, nonlocal, or global histories | **only under the stated Bell premises** |

The computations therefore cover a six-neighbor three-letter pattern space, 24
proper rotations, five-site syntactic partial maps, finite two-qubit algebras,
and a supplied two-setting/two-outcome Bell target. They do not classify
arbitrary `M_2(C)`-valued physical rules, infinite-lattice operation algebras,
continuum causal dynamics, or experimental data. "Local" in Theorem 1 means
the contradiction is witnessed at one site; it does not mean a physical
formation process has one-site causal support. The negative is consequently
only "physical successor and preservation laws are not supplied by the checked
surface," never "impossible" or "false in nature."

### N6 -- partial-closure and import-retirement paths

The approved-primitive registry check was run against
[`axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json), then each
registered primitive source was read. The scale-reference primitive supplies
units only, kinetic isotropy supplies only `c_t=c_s`, and the realized-state
primitive supplies pointwise evaluation only. None supplies a physical
state-successor graph, site identity, an operation algebra, activation,
realized draw, or formation site/rate.
They remain approved premises, not walls.

| candidate retirement path | current status | exact contribution if it lands |
|---|---|---|
| interpret Record through the `RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md#L76` site-tagged monotone-history condition | source condition, not axiom text; status read from the pipeline | retires weak syntactic preservation/site identity for consumers that state the representation; does not create a physical successor graph or superselection |
| `BOOTSTRAP_CONTINUATION_AVAILABILITY_NONEMPTY_FREE_ORBIT_REDUCTION_PROPAGATION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-04.md#L34` | unaudited bounded note | retires first-support nonemptiness and gives conditional symmetry propagation; not a temporal state lift or all-future preservation |
| extensional fixed rule plus a retained outcome-to-state theorem | absent | would retire context-scoped physical successor realization |
| retained post-record operation theorem, e.g. every future `Phi` obeys `Phi*(P)=P` | absent | would retire strong physical preservation/nonreconnection without choosing a branch or weight |
| `TICK_ADMISSIBILITY_REALIZATION_BRIDGE_CLAUSE_TO_PREDICATE_NARROW_THEOREM_NOTE_2026-07-10.md#L15` and `PROTOCOL_ADMISSIBILITY_3D_REALIZATION_BRIDGE_AND_WORD_DISPERSIVENESS_NARROW_THEOREM_NOTE_2026-07-10.md#L37` realization predicates | unaudited and conditional | give templates for a rule-to-process proof, but currently retire neither bridge |
| this exact working sentence as a theorem condition | current unaudited source note, not registered | lets bounded consumers expose what the condition buys while state lift and preservation are separately targeted for retirement |
| controlled-vocabulary, interpretation-stance, or convention reframe | none found for state-successor realization or operation preservation | a definition can clarify the weak site-tagged reading, but cannot turn a physical successor graph or all-future channel preservation into labeling only |

The branch and controlled-vocabulary scans therefore found real partial routes,
but no convention-only closure that would make "new axiom required" a valid
conclusion. A continuation construction with explicit locality, setting, and
intervention semantics can also face the Bell control without selecting or
weighting an outcome. No premise registration is performed.

### N7 -- strongest steelman

**Hostile reviewer steelman.** The framework says there is one fixed rule;
absence of its predictive specification is not evidence that its mathematics lacks an
extensive, monotone, idempotent, or confluent closure. The bootstrap note
already obtains a nonempty first menu and conditional reachability closure, and
the record-faithful branch shows that extra record-faithfulness can sharply
constrain neighbor response. The actual rule might similarly induce
distribution-compatible successor states and a commuting-projector, tail, or other preserving
operation class. Until its predictive specification and process realization
are derived or supplied, a
claim that route two fails in the framework would be premature.

This steelman defeats the broad actual-rule no-go and is why that claim is
demoted to `partial-narrowing`. It does not defeat the scoped source-text fact
or the rejected finite singleton-map witness recorded here.

### N8 -- cross-cycle echo

The required repository phrase search was run with `rg` for
`structurally undecidable`, `no retained primitive`, `requires new axiom`, and
`cannot be derived from A_min`. All `NO_GO_LEDGER.md` files under
`.claude/science/physics-loops/` were then listed and searched for
Admissibility, formation, dynamics, realization, successor, and continuation.
The directly similar hits and the earlier cycles already cited above were
walked as follows:

| prior cycle or ledger | repeated wall | current disposition / retirement mechanism | treatment here |
|---|---|---|---|
| `RECORD_FORMATION_APPEND_CERTIFICATION_BOUNDED_NOTE_2026-07-04.md` | occurrence was confused with a total formation rule | axiom append closed occurrence only; the realized draw and formation site/rate stayed open | outcome support is not called a temporal state graph |
| `RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md` | permanence was read as site immobility | site-tagged monotone identity was exposed as representation data | the same condition is explicit in Theorem 1 |
| `SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md` | record order was read as metric time | axis/order and rate/metric were separated | partition refinement supplies no clock rate or duration |
| `work_history/repo/review_feedback/RECORD_FORMATION_THREE_ROUTE_ASSUMPTIONS_EXERCISE_AND_AXIOM_TARGET_NOTE_2026-07-13.md` | a fixed algebra was read as dynamic formation | activation and allowed-operation scope stayed open | one-time `E_P`, fixed algebra, and persistent operation law are separated |
| `.claude/science/physics-loops/tier-a-elimination-block30-ac-reta-formation-nonsupply/NO_GO_LEDGER.md` | formation occurrence was read as a selector, rate, or time metric | live; future occurrence/action theorem or owner governance named | different downstream residual; selection/rate remain outside this route-two result |
| `.claude/science/physics-loops/staggered-dirac-a1a2-realization-closure-20260710/NO_GO_LEDGER.md` | Admissibility availability was read as kinetic-law selection | live narrow countermodel; reopens only with a rule-to-kinetic selector theorem | same missing type of realization bridge; warns that this cycle's typed witness is not a full-foundation countermodel |
| theta ledgers `.claude/science/physics-loops/tier-a-elimination-block09-theta-gauge/NO_GO_LEDGER.md`, `.claude/science/physics-loops/tier-a-elimination-block11-theta-g3/NO_GO_LEDGER.md`, and `.claude/science/physics-loops/tier-a-elimination-block12-theta-g1/NO_GO_LEDGER.md` | admissible alternatives were read as selected/coefficiented dynamics | live action/measure/selection residuals; no convention retirement | analogous type warning, but different residual; not counted as support for continuation nonuniqueness |
| `STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md#L194` | a missing named-set bijection looked axiom-like | external labeling convention legitimately closes naming only | inapplicable to a physical successor graph or operation preservation; only wording/labels could retire this way |
| `OBSERVABLE_PRINCIPLE_P1_BRIDGE_STRUCTURAL_REFRAMING_NARROW_NOTE_2026-05-21.md#L323` | physical identification was proposed as a convention reframe | reframe did not reduce the load-bearing physical identification | directly cautions against calling the support/preservation bridge a definition |

No similar wall was found to have been retired by a mechanism omitted here.
The reusable mechanisms are explicit decomposition, a genuine bridge theorem,
or a labeling-only convention when the residual is truly nominative. Only the
first has landed in this attempt. This note makes no constitutional or audit
change.

## Verification

The companion runner checks:

- the exact target sentence and axiom non-edit boundary;
- foundation-source and approved-primitive registry needles saying
  Admissibility is not dynamics and concrete checked rule surfaces are supplied
  models/conditions, plus the site-identity representation boundary;
- all 729 neighbor patterns and 24 proper cubic rotations for the witness rule;
- label-swap equivariance and rejection of the historical singleton-map comparison under the current distribution-valued rule;
- exhaustive syntactic immutable-extension-cone disjointness on all five-site
  partial configurations;
- independent binary full-support `2^n` refinement, a constrained non-doubling
  control, and finite saturation;
- full versus block-preserving operation algebras on the separately supplied
  finite tensor-product comparator, covariant/disjoint
  conditional expectations, finite-unitary center preservation, later-flip and
  premature-dephasing rejectors;
- the deterministic-local CHSH ceiling and a separately supplied
  context-indexed no-signaling target;
- smoke-like negative controls for overwrite, fixed-algebra-before-formation,
  and the rejected historical branch-support comparison.

No axiom, primitive, audit ledger, generated audit surface, or registry is
edited.

Measured runner output:

```text
TOTAL: PASS=76 FAIL=0
```
