# Record Pre-Record Instrument Kernel Gate

Date: 2026-06-06

Status: bounded-support

actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact finite algebra under cited retained-bounded projective readout authorities and a supplied readout context"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: true_for_bounded_support_only
proposal_allowed_reason: "The projective instrument and trace-normalized branch are supplied by cited bounded projective/Lueders authorities; the readout context remains supplied and no bare retained status is claimed."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## 2026-06-12 audit firewall: no retained production-kernel promotion

No further repair is needed for the stated supplied-context finite algebra:
with cited bounded projective/Lueders authorities and a supplied readout
context, the runner verifies the one-qubit probability-to-record typing.

This does not promote the packet to bare retained status. The readout context,
probability/Born-rule authority, physical production generator, and clock/rate
normalization remain outside the Record axiom and outside this finite gate.
No new axiom, Tier-A admission, arbitrary measurement primitive, or audit
status is introduced here.

## Summary

This block makes the pre-record side of dynamics explicit:

```text
qubit state
  + cited projective instrument / trace-normalized branch authority
  + supplied readout context
  -> probabilities over possible future record atoms
realized outcome
  -> one-hot post-record atom/count update
```

The runner proves the finite one-qubit algebra under the cited bounded
projective-measurement authorities. `MINIMAL_AXIOMS_2026-06-05.md` supplies the
one-qubit carrier and Record's realized-outcome registration, but explicitly
does not supply a measurement instrument, Born rule, probability, or readout
context. The projective instrument step is therefore not imported from the
Record axiom: it is cited to retained-bounded projective/Lueders support, while
the concrete `Z`/`X` readout context remains a supplied input.

With that authority chain, a pre-record density matrix plus a chosen
projective readout context gives a probability vector over possible record
atoms. Once an outcome is written, the post-record object is a realized atom or
count increment, not the probability vector.

## Runner

Runner:

```text
scripts/frontier_record_prerecord_instrument_kernel_gate_2026_06_06.py
```

Cache:

```text
logs/runner-cache/frontier_record_prerecord_instrument_kernel_gate_2026_06_06.txt
```

Scorecard:

```text
PASS=36 FAIL=0
```

## Authority Repair

This repair closes the prior source-packet gap called out by audit:

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  qubit local algebra and the Record realized-outcome typing, while explicitly
  firewalling measurement/Born/probability/readout-context content out of the
  axiom itself.
- [`LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md`](LSP_PROJECTIVE_CANONICAL_KP_EQUALS_P_NARROW_THEOREM_NOTE_2026-06-05.md)
  supplies the retained-bounded canonical projective-instrument identity
  `K_r = P_r` in the restricted Naimark/Lueders frame.
- [`LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md`](LUDERS_SEQUENTIAL_PRODUCT_CONDITIONAL_BRIDGE_NARROW_THEOREM_NOTE_2026-05-22.md)
  supplies the trace-normalized branch form
  `P sigma P / Tr(P sigma P)` once the Lueders projective selection is in
  force.

These citations do not make Record probabilistic and do not select a physical
readout. They only remove the hidden import of the projective instrument and
trace pairing from this finite gate.

## Exact Bounded Content

The runner uses the pure one-qubit state

```text
rho = [[2/3, sqrt(2)/3],
       [sqrt(2)/3, 1/3]]
```

and two supplied projective instruments.

For the `Z` readout context, the cited projective trace pairing gives:

```text
p_Z = (Tr(P_0 rho), Tr(P_1 rho)) = (2/3, 1/3).
```

For the `X` instrument on the same state, the probabilities differ:

```text
p_X = (1/2 + sqrt(2)/3, 1/2 - sqrt(2)/3).
```

Therefore the instrument/readout context is load-bearing for the production
kernel. The qubit state alone is not the record-production kernel, and the
minimal Record axiom alone does not select the readout context.

## Post-Record Split

If outcome `0` is realized, the written post-record atom is:

```text
e_0 = (1, 0).
```

If outcome `1` is realized, the written atom is:

```text
e_1 = (0, 1).
```

For a current count `(4,2)`, the realized updates are integral:

```text
(4,2) -> (5,2)
(4,2) -> (4,3)
```

The ensemble expectation is instead:

```text
E[c'] = (4,2) + (2/3,1/3) = (14/3, 7/3).
```

That expectation is useful, but it is not either realized post-record update.

## What This Unlocks

This gives the dynamics stack a typed input port:

```text
pre-record carrier state
  + cited bounded projective instrument / trace bridge
  + supplied readout context
  -> production probabilities over possible record atoms
  -> realized atom after registration
  -> post-record information dynamics
```

It connects the user's implication directly: the qubit is the pre-record
probability carrier only after the bounded projective readout authority and a
readout context are supplied. The post-record site carries realized
information.

This also composes with the clock/rate gate from PR #2809. A supplied
instrument can produce one-step probabilities; a supplied generator can then
stabilize a dial location; physical rates still need clock/rate normalization.

## Boundaries

This block does not:

- derive the readout context;
- derive arbitrary physical measurement dynamics;
- derive a Born rule as a new axiom;
- derive IID frequencies or typicality from one-shot probabilities;
- derive a physical Markov generator;
- derive a physical clock or rate unit;
- select a generation/Koide dial value;
- update repo-wide authority surfaces.

The current source-side status is bounded-support because the projective
instrument/trace step is now cited to bounded projective/Lueders authorities,
while the physical readout context remains supplied and independent audit still
owns the effective status.
