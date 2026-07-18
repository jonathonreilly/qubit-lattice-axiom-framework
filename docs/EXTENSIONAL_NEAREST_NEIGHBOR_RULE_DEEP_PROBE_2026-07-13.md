# Extensional Nearest-Neighbor Rule: Deep Derivation Probe

**Date:** 2026-07-13

**Type:** bounded_theorem

**Scope:** finite non-entailment and construction probe

**Authority:** none. This note does not select a physical rule, edit an axiom
or primitive, or set an audit status.

**Primary runner:**
[`scripts/extensional_nearest_neighbor_rule_deep_probe_2026_07_13.py`](../scripts/extensional_nearest_neighbor_rule_deep_probe_2026_07_13.py)

## Question

This probe is about the Admissibility statement in the
[`live four-axiom foundation`](MINIMAL_AXIOMS_2026-06-29.md).

Can the current statement that there is one fixed covariant nearest-neighbor
Admissibility rule be made extensional in a way that derives:

1. physical continuation and transitive reachability;
2. support for every locally available record value;
3. same-site/same-content permanence; and
4. ordinary finite-site quantum composition?

## Result

The answer splits cleanly.

An explicit **append-only cellular relation** can derive items 1-3 exactly.
The runner gives one complete witness: the local availability menu is the
majority value among recorded neighbors, with both values available on a tie;
one lawful step appends one available value at any open site and changes
nothing already recorded. On all `3^8 = 6561` record configurations of the
finite witness:

- every step adds exactly one record;
- every value in the local menu has a successor;
- all prior site/content pairs are preserved; and
- futures carrying conflicting values at the same site never reconnect.

This proves that the proposed continuation-support and permanence clauses can
be theorems of an explicit rule.

It does **not select the physical rule**. Even after imposing proper-cubic
covariance, neighbor dependence, and exact `0 <-> 1` no-privilege symmetry on
the smallest ternary neighbor-profile model, there are
**282,429,536,480** varying rule tables. The current structural clauses reduce
the search space; they do not come close to naming one law.

The append rule also **does not derive tensor composition**. Exactly the same
record successor graph can be placed over the ordinary `M_4(C)` two-site
algebra or over `M_4(C) direct-sum M_4(C)` with an extra global central sector.
The rule cannot see that sector because its state and transition predicates
refer only to record configurations.

## Exact Rule-Space Census

For a local profile whose six neighbor slots are each `open`, `0`, or `1`,
there are `3^6 = 729` profiles. The 24 proper cubic rotations partition these
into 57 orbits. Global value flip fixes 9 of those orbits and pairs the other
48 into 24 pairs.

A nonempty binary availability menu has three possible values:

```text
{0}, {1}, {0,1}.
```

On each paired profile orbit, no-privilege covariance lets one choose any of
the three menus and forces the flipped partner. On a self-flip orbit only
`{0,1}` is allowed. Hence:

```text
number of covariant label-equivariant tables = 3^24
number that actually vary with neighbors       = 3^24 - 1
                                                = 282,429,536,480.
```

This is a lower-bound witness, not an exhaustive count for the full
`M_2(C)` possibility domain.

### Basis-free maximum-support schema

The strongest rule schema found without selecting a named possibility works
on any one-site possibility set `D`. Let a record state be a partial map
`C : Z^3 -> D`. For an open site `x`, define

```text
A_C(x) = D                                      if no neighbor is recorded,
         { C(y) : y is a recorded neighbor }    otherwise.
```

An atomic successor appends `x -> p` for any `p in A_C(x)` and changes no old
entry. Continuation is the reflexive-transitive closure of that relation.

This schema is translation- and proper-cubic-covariant and equivariant under
every relabeling of `D`; it selects no coordinate, basis, or named value. It
proves continuation, menu-complete support, exact permanence, and sibling
nonreconnection by construction. Reading `D=M_2(C)` follows the literal axiom
but treats arbitrary matrices as possibilities; restricting `D` to rays or
rank-one projectors adds exactly the operational-typing content isolated by
the companion probe.

The schema is deliberately maximum-support and physically weak. It copies
already represented neighboring values and makes the whole domain available
in a blank neighborhood. It does not derive quantum interference, formation
eligibility, probabilities, or composition. Its purpose is to prove that the
candidate Admissibility/Record properties can be consequences of an exact,
basis-neutral rule rather than independent clauses.

## The Three Serious Rule Routes

### 1. Append-only cellular relation

The route takes a state to be a partial site-to-content map and defines the
law answer as the set of all one-record extensions allowed by the local menu.
Its transitive closure is continuation.

It buys:

- exact menu-to-successor support;
- a local causal dependency relation;
- monotone record extension;
- same-site/same-content permanence; and
- nonreconnection of incompatible recorded branches.

It leaves:

- which one of the hundreds of billions of local tables is physical;
- simultaneous overlapping-event composition;
- actualization and weights;
- coherent pre-record evolution; and
- the quantum state/effect/composite structure.

The rule is therefore a valid record-layer witness, not a TOE candidate.

### 2. Reversible quantum cellular automaton

A reversible QCA is promising for coherent local propagation, but it begins
with a quasi-local or finite tensor-product algebra and a reversible global
update. Composition is therefore premise-supplied in the QCA definition, not
derived from the local rule.

The exact two-qubit control is a CNOT copy. It writes a blank target, but a
second CNOT erases it and the inverse always exists. Thus global reversible
access does not yield absolute record permanence. A QCA route must additionally
derive or impose one of:

- a future invariant record algebra;
- a superselection/allowed-operation restriction;
- an ever-growing inaccessible archive; or
- an access-relative rather than absolute meaning of permanence.

The [Schumacher-Werner QCA construction](https://arxiv.org/abs/quant-ph/0405174)
likewise starts from an infinite quantum lattice system with a discrete global
time step, translation covariance, and finite propagation; it supports the
structural viability of a local quantum rule, not a derivation of the
framework's composite or Record semantics.

### 3. Local quantum instrument

An ideal record-writing isometry

```text
W|psi> = sum_i P_i|psi> tensor |i>
```

does give a CPTP nonselective channel and record-conditioned branches.
However, it already imports:

- the system-register tensor product;
- the pointer projectors/effect context;
- the trace/Born pairing for outcome weights;
- fresh register capacity; and
- an outcome token or unraveling if one branch is to be actual.

The nonselective channel dephases but does not select a realized record. The
selective instrument supplies a record label only because its Kraus outcomes
were part of the definition. This is an excellent conditional dynamics
surface, not a derivation from record configurations alone.

## What Is Actually Learned

The current foundation already postulates one fixed rule, but it does not yet
give that rule an **exact predictive specification** or prove an exact
physical-equivalence class for every claimed observable. The two draft
sentences state universal properties the rule should satisfy. They do not
supply or derive its predictive content.

There are now two legitimate constitutional paths:

1. state continuation/support and exact permanence in the axioms, then derive
   or supply a predictive specification inside that class; or
2. derive or supply the predictive specification first and prove those
   sentences as theorems.

For a TOE, path 2 is stronger if an exact predictive specification—or a proved
physical-equivalence class—can be derived or supplied. The witness here proves
only that path 2 is logically possible. It does not produce predictive content
with the needed quantum, matter, probability, time, and gravity consequences.

The composition seam remains independent. A record-only local rule cannot
distinguish ordinary tensor composition from an extra invisible global sector.
To retire a Qubit composition clause, the eventual rule must act on enough
global operational structure to prove no-extra-global generation or local
tomography.

Actualization remains independent too: the append-only relation determines a
set of successors, and the same set accepts different normalized measures and
different realized-member selectors.

## Constitutional Effect

No additional axiom is declared necessary by this probe.

- The Admissibility and Record additions remain valid **property candidates**.
- They become theorems only after the already-postulated fixed rule is given
  enough exact predictive content to prove them.
- A Qubit composition sentence remains a live candidate because none of the
  tested rule routes derives composition without first assuming an operational
  composite.
- The larger unresolved obligation is an exact predictive specification—or a
  proved physical-equivalence class—for the already-postulated fixed rule. It
  cannot be replaced by another existence sentence.

## No-Go Discipline Gate

**Gate result:** `PASS` for the exact finite census and displayed finite
constructions. No broad no-go or constitutional conclusion is claimed, so a
No-Go Discipline verdict for either is not applicable. The finite witnesses show
non-entailment and route prices; they do not show that a TOE-grade rule cannot
exist.

### N1 -- alternative routes

1. Append-only classical/possibilistic CA -- executed; closes record semantics,
   not quantum composition or dynamics.
2. Reversible QCA -- executed on the minimal reversible copy; composition is
   presupposed and global reversal defeats absolute permanence.
3. Local quantum instrument -- executed; closes a conditional write model but
   imports tensor product, effects, weights, and unraveling.
4. Stable-subalgebra QCA -- live; could derive persistence if a nontrivial
   future-invariant record algebra is forced by the physical update.
5. Topological/superselection archive -- live; could make local reversal
   impossible while retaining global unitarity.
6. Branching history law -- live; could make continuation fundamental but must
   still derive amplitudes, consistency, and probability.

### N2 -- wall independence

- Rule-table selection is independent of append semantics: hundreds of
  billions of tables share the same append schema.
- Append semantics is independent of composition: ordinary and
  duplicate-sector composites share one successor graph.
- Reversible dynamics is independent of permanence: CNOT supplies the first
  without the second.
- A nonselective channel is independent of actualization: it supplies the
  ensemble update without a realized label.

### N3 -- hidden-wall scan

The append witness is explicitly classical/possibilistic. The QCA and
instrument routes explicitly price their tensor product, pointer, trace,
fresh-register, and selection content. No mathematical construction is called
the physical rule.

### N4 -- residual matching

The rule-count residual is rule selection; the duplicate-sector residual is
composition; the CNOT residual is absolute permanence; and the nonselective
instrument residual is actualization. None is used as evidence for another.

### N5 -- resolution audit

Enumeration is exhaustive only for ternary six-neighbor profiles with binary
menus. The append theorem is exhaustive only on the stated finite witness plus
its elementary general proof. The QCA/instrument controls are minimal
counterexamples, not classifications of all possible dynamics.

### N6 -- partial closure

A future rule can close continuation, permanence, composition, and
actualization together. A derived invariant record algebra can repair the QCA
route. A generated-global-algebra theorem can retire the composition
candidate. None is excluded.

### N7 -- steelman

The strongest live route is a local quantum automaton on a generated
quasi-local algebra whose future dynamics creates an increasing invariant
commutative record algebra. If the same structure also fixes a consistent
history measure, then continuation, records, composition, and actualization
could all be theorems of one rule. The current repo has no such construction,
but this probe does not weaken it.

### N8 -- cross-cycle echo

Earlier rule-table toys repeatedly proved properties of supplied models and
were then correctly fenced from the physical rule. Earlier tensor, Kraus, and
record-write rows likewise proved conditional algebra while leaving
composition, pointer selection, and formation open. This probe preserves those
boundaries and consolidates them into one rule-first target.
