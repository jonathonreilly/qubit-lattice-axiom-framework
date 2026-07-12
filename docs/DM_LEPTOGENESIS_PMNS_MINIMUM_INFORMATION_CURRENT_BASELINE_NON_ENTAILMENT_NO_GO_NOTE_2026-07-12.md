# DM Leptogenesis PMNS Minimum-Information Current-Baseline Non-Entailment No-Go

**Type:** no_go
**Claim type:** no_go
**Claim boundary:** exact non-entailment of the adopted minimum-information
closure selector from the current supplied premises (four axioms plus three
approved primitives); not a no-go
against a future downstream selector theorem
**Audit status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Date:** 2026-07-12
**Primary runner:**
[`scripts/frontier_dm_leptogenesis_pmns_minimum_information_baseline_no_go.py`](../scripts/frontier_dm_leptogenesis_pmns_minimum_information_baseline_no_go.py)
**Primary cached output:**
[`logs/runner-cache/frontier_dm_leptogenesis_pmns_minimum_information_baseline_no_go.txt`](../logs/runner-cache/frontier_dm_leptogenesis_pmns_minimum_information_baseline_no_go.txt)
**Load-bearing authorities:** [Minimal Framework Axioms](MINIMAL_AXIOMS_2026-06-29.md),
[Scale-Reference Primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md),
[Kinetic-Isotropy Primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md), and
[Realized-State Primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)

## Result

The previously missing positive derivation does not exist on the stated
premise surface.  More precisely:

> **Current-baseline non-entailment theorem.** The adopted law
>
> `choose the positive off-seed source minimizing I_seed subject to
> eta_{i_*} / eta_obs = 1`
>
> is not entailed by the current supplied premises.

This is an exact negative boundary, not a positive PMNS source selector.  The
proof keeps one explicit model of Lattice, Qubit, Admissibility, and Record
fixed and
constructs conservative downstream completions that all satisfy the axiom
memo's law qualification—same supplied domain, one answer at every state, and
no state preference—but disagree on:

1. whether the physical source minimizes `I_seed`;
2. the relative weight of the `x` and `y` information blocks;
3. the observational exact-closure anchor; and
4. the transport-favored column.

Because the completions agree on every statement in the supplied-premise language
and disagree on the adopted selector law, the selector law cannot be a logical
consequence of that language.

## Minimal premise set

The proof uses only the current source of framework premises:

- Lattice: `Z^3`, nearest-neighbor adjacency, translations, and proper cubic
  rotations, with no privileged site;
- Qubit: the full one-site algebraic presentation `M_2(C)`, with no privileged
  possibility;
- Admissibility: one translation- and cubic-covariant nearest-neighbor rule;
- Record: permanent locking of one admissible possibility and finite additive
  scalar readout;
- the qualification that a state is a record configuration and a law
  privileges no states, has a supplied domain, and gives one answer wherever
  that condition holds.

Call this language and theory `A_min`.  The axiom memo explicitly leaves
weighting, normalization, source/action structure, physical-observable
identification, and state-selection rules outside the axioms.  In particular,
`A_min` contains no PMNS source chart, seed probability distribution, KL
functional, flavored transport map, `eta_obs`, or source-selection variational
principle.

The no-go first establishes derivability failure from `A_min`, then extends
the same completion pair identically across all three approved primitives. It
does not assume that
symbols absent from `A_min` are meaningless; they are legitimate downstream
objects once a separate theorem or supplied condition introduces them.

### Approved-primitive extension

Give both completions the same scale reference, the same kinetic equality
`c_t=c_s`, and the same realized state (the uniform recorded state constructed
below). These interpretations satisfy the three approved primitive notes. The
scale primitive carries no dimensionless content, kinetic isotropy supplies no
selector, and the realized-state primitive supplies a pointwise slot but no
state-selection rule, weighting, normalization, or state-contingent value.
Therefore the two completions still disagree on the selector while agreeing
on the entire current supplied-premise surface.

## Proof

### An explicit model of the base axioms

Non-entailment requires a consistent base model, so the proof does not merely
assume one. Use sites `Z^3` with the usual six nearest neighbors. Attach the
full matrix algebra `M_2(C)` at every site and take rank-one projectors as the
local pure possibilities. Define the available set from a neighbor condition
by the top spectral projector of the unordered sum of the six neighboring
rank-one projectors; an absent neighbor record contributes the zero matrix, and
when the top eigenvalue is degenerate, allow every rank-one projector in that
eigenspace. The state class is all partial rank-one-projector record
configurations that obey this pointwise rule. This is one fixed rule, is
invariant under translations and proper cubic rotations, and varies with the
neighbor condition. It also privileges no one-site possibility: under a common
`U in U(2)`, the neighbor sum transforms as `B -> U B U^dagger` and its top
spectral projector as `P_top -> U P_top U^dagger`.

The configuration with projector `P_0` recorded at every site is admissible:
the neighbor sum is `6P_0`, so the rule makes `P_0` available. Records are
permanent, and for a finite disjoint record family define scalar readout as its
cardinality; this is content-determined, additive, and zero on the empty
family. A constant total law on the supplied domain gives one answer at every
state and privileges no state. Thus this is a concrete model `M` of `A_min`.
The primary runner checks the 24-element proper cubic action on the neighbor
set, the actual matrix-unit multiplication/span of `M_2(C)`, a non-diagonal
spectral sum and common-unitary covariance, a degenerate spectral sum, and the
uniform record/readout conditions. The analytic construction above remains
load-bearing because no finite runner instantiates the infinite lattice.

### Lemma 1: the law qualification does not choose a selector law

Fix the explicit model `M` above. Add a downstream two-point source domain

`Q = {q_x, q_y}`

on which both points are positive, off-seed, on the same supplied seed surface,
and satisfy the same supplied closure predicate.  Fix one information cost

`I_seed(q_x) = 0.1`, `I_seed(q_y) = 0.2`.

Now form two conservative completions over the identical `M`:

- `C_min` returns `q_x` at every state;
- `C_alt` returns `q_y` at every state.

Both laws have the same supplied domain, are total and single-valued, and are
constant over states.  They therefore satisfy the law qualification equally:
neither privileges a state.  They disagree only on the downstream rule used
to choose a source.  `C_min` implements minimization of `I_seed`; `C_alt` does
not.  Since `A_min` cannot distinguish the two completions, it does not entail
the minimization principle.

This lemma attacks the load-bearing verb **minimize**, not merely the numerical
optimizer that executes it.

### Lemma 2: equal modality weighting is independent of the baseline

The ambiguity remains even if one grants the KL form and the target note's
native fixed totals. Let `u=(1/3,1/3,1/3)`.
For

`K(t)=D_KL((1/3+t,1/3-t,1/3)||u)`,

direct differentiation gives

`K'(t)=log((1+3t)/(1-3t))>0` for `0<t<1/3`.

Also `K(0)=0` and `lim_{t->1/3} K(t)=(2/3)log 2>0.46`. The intermediate
value theorem therefore gives unique strictly positive distributions
`p_x,p_y` with

`D_KL(p_x||u)=0.1`, `D_KL(p_y||u)=0.15`.

With the supplied target-surface values `xbar=0.5633333333333334` and
`ybar=0.30666666666666664`, use two fixed-total positive sources:

- `q_x=(x=3 xbar p_x, y=3 ybar u, delta=0)`;
- `q_y=(x=3 xbar u, y=3 ybar p_y, delta=0)`.

The adopted information cost normalizes each block by its own total, so these
native rescalings leave the KL values `0.1` and `0.15` unchanged.

For

`I^(w_x,w_y) = w_x D_KL(x/sum(x)||u) + w_y D_KL(y/sum(y)||u) + (1-cos delta)`

one obtains

| positive weights | `I(q_x)` | `I(q_y)` | unique minimizer |
|---|---:|---:|---|
| `(1,1)` | `0.1` | `0.15` | `q_x` |
| `(2,1/2)` | `0.2` | `0.075` | `q_y` |

Both objectives are nonnegative information-deformation costs and both define
total state-neutral laws.  No `A_min` symmetry exchanges the downstream `x`
and `y` modalities or fixes their relative normalization.  Thus equal weights
are additional selector content, not an axiom consequence.

### Lemma 3: exact observational closure is independent of the baseline

Keep the same `M` and the same two downstream sources.  Give them transport
values

`eta(q_x)=1`, `eta(q_y)=2`.

One completion supplies `eta_obs=1`; another supplies `eta_obs=2`.  The exact
closure locus is `{q_x}` in the first and `{q_y}` in the second.  Every
four-axiom fact is identical between the two completions because neither the
transport map nor `eta_obs` occurs in `A_min`.

Therefore the equality `eta_{i_*}/eta_obs=1` cannot be derived from the four
axioms without a separate physical-observable and normalization bridge.  In
the old optimizer it is an imposed observational constraint, exactly as the
code indicates.

### Lemma 4: the favored column is downstream transport data

Over the same fixed `M`, one transport completion may assign column values
`(2,1,1/2)` and another `(1,2,1/2)`.  Their favored columns are respectively
`0` and `1`.  Both assignments are compatible with `A_min`, which contains no
flavor-column transport map.

Hence the baseline cannot select `i_*`.  A later transport theorem may do so
on a supplied downstream surface, but that would be a new bridge rather than a
derivation from the four axioms alone.

### Theorem conclusion

The adopted law is a conjunction of the selector principle, its equal-weight
information objective, the favored-column input, and the exact observational
closure constraint. Lemmas 1–4 each give two completions of the same base
model that disagree on one of those pieces, and the approved-primitive section
extends both identically. Consequently the adopted minimum-information closure
law is not entailed by the current supplied premises.

The primary runner constructs these completion pairs, realizes Lemma 2 with
strictly positive three-component probability vectors, and verifies the
state-neutral/total/single-valued law conditions.  The proof itself is the
standard model-theoretic criterion for non-entailment: a sentence is not a
consequence of a theory when two models agreeing on the theory disagree on
the sentence.

## Exact scope firewall

This theorem is deliberately narrower than “no selector can exist.”

- It is not a no-go against downstream selector physics.
- It does not rule out a future downstream selector theorem using additional
  retained structure.
- It does not rule out explicit owner approval of a new primitive, although
  that would supply new premise content rather than derive the law from the
  current `A_min`.
- It does not prove that KL, relative action, or transport extremality is
  physically wrong.
- It does not invalidate the conditional optimizer output.
- It does not close the positive PMNS-assisted `N_e` branch.

It proves exactly one negative statement: the requested first-principles
derivation cannot be completed on the current supplied-premise set.
A positive closure must add and independently justify at least a selector
bridge and an observational closure bridge.

## Downstream authority firewall

This row supplies no positive selector authority.  A downstream runner may
continue to import the conditional optimizer as a comparator or as an explicit
post-axiom convention, but it must not cite this no-go as if it supplied the
minimum-information law.  Any descendant whose positive conclusion requires
the law remains conditional until a separate positive selector authority is
available.

## No-go discipline record

### N1 — alternative routes

| Attack | Result | Marker |
|---|---|---|
| Derive KL from Record additivity | The [minimal axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies finite additive record readout but no probability simplex, coarse graining, data processing, or source-to-record map. The completion pair survives. | ATTEMPTED |
| Derive minimization from log-det/Legendre duality | The same memo explicitly leaves log-det and source/action bridges outside the axioms. A Legendre identity defines a functional after those objects are supplied; it does not supply the physical verb minimize. | ATTEMPTED |
| Fix equal x/y weights by cubic symmetry | The x/y modalities are not primitive lattice axes. The native-total KL construction above flips its minimizer under two positive weight pairs. | ATTEMPTED |
| Derive exact closure from transport | No supplied premise contains `eta_obs` or an observational normalization rule. The two comparator completions have different exact-closure loci. | ATTEMPTED |
| Derive the favored column from realized state | The [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) supplies a pointwise slot but no contingent value. Two transport completions favor different columns. | ATTEMPTED |
| Close by convention | The original gate may adopt the law and run its optimizer, but a definition is not an entailment from the supplied premises. | ATTEMPTED |

### N2 — collapsed wall set

Equal modality weighting is part of the broader selector-objective wall. The
collapsed set is: `(W_selector)` physical source-selection objective and
modality normalization; `(W_anchor)` `eta_obs` observable/normalization bridge;
`(W_transport)` seed/transport/favored-column authority. No one of these three
logically supplies either of the others. The proof needs only one differing
completion; it does not claim that three new axioms are required.

### N3 — hidden-wall scan

“Supplied seed surface” and “supplied closure predicate” are deliberate grants
inside the countermodel, not baseline consequences. “Standard model-theoretic
criterion” is instantiated by the displayed pair of expansions. The observed
target is excluded from the proof. The construction uses no hidden “standard
QFT,” canonical-source, naturalness, fitted, or literature premise.

### N4 — residual matching

| Candidate witness | Its residual | Match? | Use |
|---|---|---|---|
| `docs/MINIMAL_AXIOMS_2026-06-29.md` and the three linked primitive notes | exact content of the current supplied-premise language | yes | load-bearing |
| `docs/DM_LEPTOGENESIS_PMNS_ISEED_SELECTOR_ROUTE_PROBES_NOTE_2026-07-02.md` | computed diagnostics on imported PMNS machinery | no | context only; dropped as proof witness |
| `docs/DM_NEUTRINO_SOURCE_SURFACE_INFO_GEOMETRIC_SELECTION_OBSTRUCTION_NOTE_2026-04-17.md` | a different reduced variational family | no | context only; dropped |
| `docs/DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md` | positive-cone identity plus sampled conditional branch | no | steelman only; dropped |

### N5 — rhetoric resolution

The theorem is not a per-site, per-mode, or per-block absence claim. It is a
theory-language statement: the two expansions agree on the complete supplied
base interpretation and disagree downstream. Untested broader statements—no
selector exists, no nonlocal law works, or no future theorem can close the
gate—are expressly excluded.

### N6 — partial-closure paths

| Path | File/status at this block | What it can close |
|---|---|---|
| Adopt the min-law convention | `docs/DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md`; source type `open_gate` | conditional optimizer only |
| Derive a source/action law | `docs/DM_LEPTOGENESIS_PMNS_RELATIVE_ACTION_STATIONARITY_THEOREM_NOTE_2026-04-16.md`; source type `bounded_theorem`, current audit ratification absent | could address `W_selector`, not automatically `W_anchor` |
| Derive target-free normalization | no current supplied-premise authority found; opportunity recorded in this loop | could address `W_anchor` |
| Approve a selector primitive | `docs/audit/data/axiom_premise_nodes.json`; no selector primitive registered | would supply, not derive, selector content |
| Existing approved primitives | the three linked primitive notes | none supplies a selector, weighting, normalization, or favored-column value |

Thus a convention, downstream theorem, or future approved primitive can move
the positive gate; none changes the theorem about the present premise set.

### N7 — steelman

The strongest objection is that relative entropy can be characterized by
additivity, coarse-graining consistency, and data processing, while a log-det
Legendre dual can furnish an effective action. If those principles were
already supplied, the counterexpansions might violate hidden semantics. They
are not supplied: the current axiom memo explicitly limits Record to finite
additive scalar readout and leaves weighting, log-det, source/action, and
physical-observable bridges outside the axioms. Adding such premises is a live
future route preserved by this theorem.

### N8 — cross-cycle echo

| Similar prior wall | Current disposition | Retirement mechanism considered here? |
|---|---|---|
| `docs/PMNS_CHART_CONSTANTS_RETENTION_NOTE_2026-05-03.md` | source `open_gate`; positive chart-constant imports remain conditional | yes; a retained downstream bridge could retire an input but does not follow from `A_min` automatically |
| `docs/STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md` | source `no_go`, current audit ratification absent; naming can be fixed by convention | yes; convention closure is preserved but is not physical selector entailment |
| `docs/OBSERVABLE_PRINCIPLE_P1_CAMPAIGN_CLOSURE_SYNTHESIS_NOTE_2026-05-18.md` | source `bounded_theorem`; adopts an explicit conditional principle after many failed derivations | yes; this is the same honest conditional-adoption route retained by the original gate |
| `.claude/science/physics-loops/hubble-c1-absolute-scale-gate-20260428/NO_GO_LEDGER.md` multipocket selector wall | not recorded as retired; requires pocket measure/sector weights | yes; a future weighting authority remains possible |
| `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` scale wall | retired operationally by explicit owner-approved primitive supply | yes; the same governance mechanism could supply a selector, but would not derive it from the current premises |

All eight checks pass for the narrow current-premise non-entailment claim.

## Relationship to the original selector gate

The adopted law under diagnosis remains defined and numerically exercised in
`docs/DM_LEPTOGENESIS_PMNS_MINIMUM_INFORMATION_SOURCE_LAW_NOTE_2026-04-16.md`.
That path is context only, not a load-bearing dependency of this proof. The
original row remains an `open_gate` so its positive consumers cannot treat
this negative theorem as selector authority.

## Reproduction

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_minimum_information_baseline_no_go.py
```

The runner has no physics helper imports and consumes no observed number as a
proof input. The analytic model construction and two-completion proof in this
note are load-bearing; the runner supplies finite local-algebra, covariance,
record/readout, KL, and completion-identity checks.
