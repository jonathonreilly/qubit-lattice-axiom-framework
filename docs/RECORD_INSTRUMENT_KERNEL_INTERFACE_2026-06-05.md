---
claim_id: record_instrument_kernel_interface_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Record Instrument Kernel Interface

**Date:** 2026-06-05
**Claim type:** bounded support map and exact conditional interface.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_instrument_kernel_interface_2026_06_05.py`](../scripts/frontier_record_instrument_kernel_interface_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_instrument_kernel_interface_2026_06_05.txt`](../logs/runner-cache/frontier_record_instrument_kernel_interface_2026_06_05.txt).

**Local support inputs:**

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md`](RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md)
- [`RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md`](RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md)
- [`RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md`](RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md)
- [`PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md`](PERSISTENT_RECORD_AS_KRAUS_OPERATOR_NOTE_2026-05-20.md)
- [`KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](KRAUS_CHOI_REPRESENTATION_ON_QUBIT_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- [`PRE_RECORD_REFERENCE_STATE_MAXIMAL_SYMMETRY_OPEN_GATE_NOTE_2026-06-05.md`](PRE_RECORD_REFERENCE_STATE_MAXIMAL_SYMMETRY_OPEN_GATE_NOTE_2026-06-05.md)

## Question

Once a finite record instrument is supplied, what is the typed dynamics surface
between a pre-record quantum state and the post-record history/count layer?

The useful answer is:

```text
pre-record state rho + supplied instrument {K_r}
  -> probability kernel mu_r = Tr(K_r rho K_r^dag)
  -> selected branch state rho_r, if outcome r is realized
  -> realized record atom e_r
  -> post-record append/count update.
```

The kernel is a probability state over possible record atoms. The realized
post-record update is a one-hot atom or count/history update. These are
different object types.

## Result

Given a finite-dimensional state `rho` and a supplied finite instrument
`{K_r}` with `sum_r K_r^dag K_r = I`, the following are exact finite-matrix
facts:

1. `mu_r = Tr(K_r rho K_r^dag)` is a normalized probability vector on the
   finite record alphabet.
2. For every `mu_r > 0`, the selective state
   `rho_r = K_r rho K_r^dag / mu_r` is a normalized positive state.
3. If outcome `r` is realized, the post-record update is
   `c -> c + e_r`, where `e_r` is the one-hot atom for that realized record.
4. The predictive expectation `E[c'] = c + mu` is generally fractional and is
   an ensemble/pre-record object, not a realized post-record count.
5. Sequential instruments compose into a joint kernel
   `mu_{r,s} = Tr(L_s K_r rho K_r^dag L_s^dag)` on record-history words.
6. Coarse-graining commutes with both probability push-forward and one-hot
   atom/count push-forward.

This is the precise interface conditional audit lanes can cite when they need
"probabilities over possible records" without turning the recorded site into a
probability distribution.

## Dynamics meaning

The interface separates four layers:

| layer | object | dynamics form |
|---|---|---|
| pre-record | density state `rho` | supplied quantum/CPTP/instrument update |
| instrument kernel | probability vector `mu` on possible atoms | trace/effect or Kraus probability map |
| realized record | atom `e_r` or history word | append one realized symbol |
| post-record information | count/history/readout | integral add/count/coarse-grain update |

This lets record dynamics carry unbounded histories while the probability law
remains a law over possible next records. It also explains why a record-letter
prior can be a stable post-record setting on a dial while a Born/dimension prior
is a pre-record or ensemble setting. This note does not select between those
settings.

## Negative route pruning

| route | verdict | reason |
|---|---|---|
| atom/probability identification | pruned | atoms live in the record algebra; probabilities are states on that algebra |
| expectation/realization identification | pruned | expectation `c + mu` can be fractional |
| post-record append derives the instrument | pruned | append starts after an outcome is supplied |
| coarse-graining selects the physical readout | pruned | it only pushes supplied labels/kernels forward |
| sequential record history supplies a time metric | pruned | it gives word order, not physical time or rate normalization |

These are route-specific prunings. They do not say measurement, Born
operationalism, local observability, or record production is impossible.

## What remains open

- Deriving the physical instrument `{K_r}` or record-writing isometry.
- Deriving the trace/effect probability rule or the reference state used in a
  Born value.
- Deriving local observability / redundant broadcast from the three axioms.
- Deriving record production, decoherence, rates, time, or a physical
  measurement Hamiltonian.
- Selecting a generation/Koide dial setting.

## What this unlocks

- Conditional audit rows can cite a typed kernel interface instead of mixing
  probability states with realized records.
- Dynamics rows can state whether they supply an instrument, a kernel, a
  realized atom, or post-record count/history propagation.
- Coarse-grained audit lanes can push probabilities and records through the
  same finite label map while preserving the type distinction.
- A future record-production theorem only needs to feed an instrument or
  realized atom into this interface; it does not need a new post-record history
  axiom.

## Boundaries

- Does not derive a physical instrument, Born rule, reference state, local
  observability, decoherence, rates, time, or a measurement Hamiltonian.
- Does not identify a nonselective density matrix with a realized record atom.
- Does not force a record-letter prior, Born/dimension prior, or Koide/generation
  dial location.
- Does not apply audit verdicts.

## Runner summary

The runner verifies:

- a nontrivial qubit Kraus instrument produces a normalized probability kernel;
- nonzero selective branches are normalized positive states;
- realized count updates are one-hot and integral while predictive expectations
  are generally fractional;
- sequential instruments compose into a normalized joint kernel over record
  history words;
- coarse-graining commutes with probability and one-hot/count push-forward;
- the source note keeps the open residuals and selector boundaries explicit.

Expected result:

```text
SCORECARD PASS=48 FAIL=0
```

```yaml
claim_id: record_instrument_kernel_interface_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact-support given a supplied finite instrument and trace/effect pairing"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
