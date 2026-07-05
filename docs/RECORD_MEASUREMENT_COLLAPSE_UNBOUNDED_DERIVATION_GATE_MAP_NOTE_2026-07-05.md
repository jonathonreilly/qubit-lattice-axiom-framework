---
claim_id: record_measurement_collapse_unbounded_derivation_gate_map_note_2026-07-05
claim_type: open_gate
claim_scope: "Source-side gate map for what a retained unbounded measurement/collapse derivation would need; records why the current four-axiom surface does not yet supply it."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - record_formation_append_certification_bounded_note_2026-07-04
  - record_prerecord_instrument_kernel_gate_2026-06-06
  - record_context_generator_nonidentifiability_no_go_2026-06-17
  - post_record_finite_to_unbounded_family_lift_no_go_2026-06-06
  - record_production_kernel_boundary_2026-06-06
  - born_rule_from_gleason_busch_derivation_note_2026-05-20
runner: scripts/frontier_record_measurement_collapse_unbounded_gate_map_2026_07_05.py
---

# Record/Measurement Collapse Retained-Unbounded Gate Map

**Date:** 2026-07-05
**Type:** open_gate
**Role:** open main gate / source-side gate map
**Claim type:** open_gate
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit generated audit data, or assert retained status.
**Primary runner:**
[`scripts/frontier_record_measurement_collapse_unbounded_gate_map_2026_07_05.py`](../scripts/frontier_record_measurement_collapse_unbounded_gate_map_2026_07_05.py)

## Result

The current framework explains the post-selection part of wavefunction collapse:
once a readout context, an instrument, and a realized outcome token are
supplied, Record turns the outcome into a permanent readable atom, and the
finite supplied-context gate types the conditional state update separately from
the written post-record atom.

It does not yet derive a retained unbounded physical collapse law. In current
framework terms, that stronger claim would require a native measurement
production family. The missing family must select or derive the readout context,
instrument, site, outcome weights, realized write process, clock/rate if
dynamics are claimed, and a finite-to-unbounded compatibility principle.

Thus the honest answer is:

```text
collapse as record-conditioned update: supported under supplied finite
measurement context and realized outcome

objective physical collapse law / Born-weighted native record production:
open, not retained-unbounded derived
```

## Load-Bearing Authorities

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  the current Lattice, Qubit, Admissibility, and Record axiom surface.
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  supplies pointwise realized-state evaluation and explicitly no selector,
  probability, weighting, or typicality rule.
- [`RECORD_FORMATION_APPEND_CERTIFICATION_BOUNDED_NOTE_2026-07-04.md`](RECORD_FORMATION_APPEND_CERTIFICATION_BOUNDED_NOTE_2026-07-04.md)
  supplies occurrence-strength formation only and leaves rule/rate/clock
  content downstream.
- [`RECORD_PRERECORD_INSTRUMENT_KERNEL_GATE_2026-06-06.md`](RECORD_PRERECORD_INSTRUMENT_KERNEL_GATE_2026-06-06.md)
  supplies the finite measurement interface under cited projective/Lueders
  authority and a supplied readout context.
- [`RECORD_CONTEXT_GENERATOR_NONIDENTIFIABILITY_NO_GO_2026-06-17.md`](RECORD_CONTEXT_GENERATOR_NONIDENTIFIABILITY_NO_GO_2026-06-17.md)
  blocks dropping the supplied-context, generator, and rate inputs.
- [`RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md`](RECORD_PRODUCTION_KERNEL_BOUNDARY_2026-06-06.md)
  blocks deriving a production kernel from post-record append/count alone.
- [`POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md`](POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md)
  blocks finite-record-certificate-alone promotion to an unbounded law.
- [`BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`](BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md)
  supplies bounded finite ideal-record Born support under its own conditional
  bridge assumptions.

## Current Closed Pieces

The current four-axiom surface supplies:

- local sites and local qubit possibility algebra;
- a covariant nearest-neighbor admissibility rule for available local
  possibilities;
- record occurrence at occurrence strength: records form in the realized
  history;
- when present, each record locks exactly one admissible local possibility, with
  one record per site, permanence, readability, and finite scalar additivity.

The landed Record-formation append closes the empty-forever reading only. It
does not supply which admissible possibility is locked, which site receives the
record, the weight of competing outcomes, the rate of formation, a clock, or a
stochastic process.

The finite measurement stack also has useful conditional support:

- a supplied one-qubit state plus cited projective/Lueders authority plus a
  supplied readout context gives a probability vector over possible future
  record atoms;
- after a realized outcome is selected, the post-record layer writes a one-hot
  atom/count update;
- finite ideal-record Born bridges can type trace probabilities under their
  own effect/probability assumptions.

Those pieces are interfaces. They are not a native selector for apparatus,
context, generator, rate, or actual branch.

## First-Principles Attempt Ledger

### Route A: Record formation as collapse

Attempt: read "Records form" as the physical collapse event.

Failure: occurrence is not a formation rule. The append certification fixes
that the realized history is not empty forever and that actual formation
successions monotonically extend records, but it leaves the site, possibility,
weight, rate, clock, and process unsupplied. This is too weak to derive a
Born-weighted collapse law.

### Route B: No privileged possibility as Born/context selection

Attempt: use "No possibility is privileged" and "A law privileges no states" to
force a canonical measurement basis or probability law.

Failure: no-privilege can support at most a no-information reference such as a
tracial state when an invariant finite algebraic frame is already supplied. It
does not select a physical readout context, apparatus, or arbitrary prepared
state. On the same one-qubit state, distinct complete projective contexts give
different probability vectors while satisfying the same local projective
algebra.

### Route C: Realized-state primitive as branch selection

Attempt: cite the realized-state primitive for the selected branch.

Failure: the primitive permits pointwise evaluation at the realized state. It
explicitly supplies no state-selection rule, measure, weighting, probability,
typicality, default state, or normalization. It can register the actual record
history after the world realizes it; it cannot be used to derive which outcome
is realized.

### Route D: Supplied finite instrument as collapse derivation

Attempt: use the finite pre-record instrument gate as collapse.

Partial success: under a supplied readout context and cited projective/Lueders
authority, the gate gives finite probabilities and a selective branch update.
That is the correct interface for a finite lab model.

Failure: the readout context and physical production generator remain supplied.
The context/generator nonidentifiability no-go shows that the same state and
finite projective algebra admit multiple contexts, and that a one-step
probability vector does not identify a Markov kernel, generator, or clock/rate.

### Route E: finite records as unbounded collapse law

Attempt: promote finite record certificates or finite frequencies to an
unbounded collapse law.

Failure: finite post-record certificates do not determine unbounded laws. Two
unbounded completions can agree on the entire finite record window and disagree
on the tail or limiting statistic. A projective-consistency, direct-limit,
monotone-exhaustion, tightness, or equivalent family-lift principle must be
supplied or derived.

## Gate Table

| Gate | Current status | Needed for retained-unbounded collapse |
|---|---|---|
| occurrence | supplied by Record at occurrence strength | already present, but too weak by itself |
| admissible write target | locally typed by Qubit/Admissibility/Record | derive which site and which admissible possibility is written |
| readout context / pointer frame | supplied in finite gates | derive or register a retained context-selection theorem |
| instrument / branch update | bounded under cited projective/Lueders authority | derive a physical instrument family, not only a supplied finite lab context |
| Born weights | finite ideal-record bridges exist under assumptions | derive the probability rule for the selected physical instrument family and prepared states |
| production kernel / generator | retained no-go against post-record derivation alone | derive a kernel or generator that produces record atoms, not merely consumes them |
| clock/rate | supplied-or-separate input in existing gates | derive rate/clock normalization if physical dynamics are claimed |
| unbounded family lift | open | prove projective consistency, direct-limit compatibility, monotone exhaustion, tightness, or equivalent preservation |
| empirical frequencies/objectivity | bounded under supplied IID/reset or broadcast/dephasing models | derive/reset the repeated-trial law and durable redundant records if empirical collapse is claimed |

## Minimal Fix Target

A retained unbounded derivation would need a theorem or approved primitive
registry update with at least the following load-bearing content:

1. **Context selection:** from the supplied framework structure, select a finite
   readout context or pointer frame for each relevant measurement condition, or
   state explicitly which context data are admitted.
2. **Instrument family:** construct a family of finite local instruments whose
   outcomes write admissible Record atoms, with covariance under the lattice
   symmetries and compatibility with the admissibility rule.
3. **Probability law:** prove normalized branch weights for the selected
   instruments on the intended prepared states. If the route uses Born weights,
   expose the effect-probability assumptions and the physical reference/prepared
   state bridge.
4. **Realized write process:** distinguish the probability law from the
   realized token. Either keep the realized outcome as supplied history under
   the realized-state primitive, or add a new explicitly approved selector
   primitive.
5. **Production kernel and rate:** derive or admit the generator, stochastic
   kernel, Hamiltonian, transfer operator, or event process that produces record
   atoms; include clock/rate normalization when a physical time claim is made.
6. **Unbounded lift:** prove compatibility across finite regions/truncations or
   trials by projective consistency, monotone exhaustion, direct-limit
   compatibility, tightness, or an equivalent theorem.
7. **Objectivity/frequency bridge:** if the target is empirical collapse, prove
   the reset/IID/ergodic or broadcast/decoherence bridge that turns single-event
   probabilities and durable records into observed frequencies and shared
   classical records.

Without this package, "wavefunction collapse" should be described in the repo
as a conditional finite measurement interface plus post-record realization, not
as a retained unbounded physical collapse law.

## Status Certificate

```yaml
actual_current_surface_status: open
trace_class: direct_blocker_closure
reachability_to_target: blocks_until_measurement_production_family_exists
conditional_surface_status: "finite supplied-context collapse/update interface is available"
hypothetical_axiom_status: "a measurement-production primitive could reopen the route but would still need audit"
admitted_observation_status: "realized record histories are registrable; they are not probability laws"
proposal_allowed: false
proposal_allowed_reason: "This note maps missing gates and negative witnesses; it does not derive context selection, production kernel, Born frequencies, branch realization, or unbounded lift."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## No-Go Discipline Gate

- **N1 alternative routes checked:** Record occurrence, no-privilege symmetry,
  realized-state primitive, supplied finite instrument, and finite-record
  unbounded promotion. Each fails to close at least one necessary collapse gate.
- **N2 wall independence:** context selection, production kernel, branch
  realization, rate/clock, Born weights, and unbounded lift are separate
  residuals. Closing one does not silently close the others.
- **N3 hidden-wall scan:** this note imports no measurement primitive, no
  context selector, no stochastic kernel, no branch selector, no rate, no IID
  reset law, and no direct-limit principle.
- **N4 residual matching:** the residual is not generic "collapse mystery"; it
  is the concrete measurement-production family listed above.
- **N5 rhetoric audit:** "collapse as update" means conditional finite
  state-update/readout typing after supplied outcome data. It is not an
  objective physical collapse law.
- **N6 partial-closure scan:** the 2026-07-04 formation append closes
  empty-forever only; it does not close selector, weight, rate, or unbounded
  gates.
- **N7 steelman:** a future theorem could derive a context-selecting,
  Born-weighted, projectively consistent production family. This note leaves
  that route open and identifies what it must prove.
- **N8 cross-cycle echo:** this note does not edit audit ledgers, generated
  front-door surfaces, axiom registries, or retained status data.

## Runner Certificate

The companion runner checks:

- source anchors for the four-axiom surface, realized-state primitive,
  formation append, supplied-context finite instrument gate, context/generator
  no-go, production-kernel boundary, and finite-to-unbounded no-go;
- finite witnesses for distinct readout contexts on the same one-qubit state;
- finite producer underdetermination for the same realized word;
- finite-prefix agreement with divergent unbounded tails;
- why a tracial no-information state would not by itself derive arbitrary
  prepared-state collapse;
- that this note keeps retained/unbounded promotion disabled.

Run:

```text
python3 scripts/frontier_record_measurement_collapse_unbounded_gate_map_2026_07_05.py
```
