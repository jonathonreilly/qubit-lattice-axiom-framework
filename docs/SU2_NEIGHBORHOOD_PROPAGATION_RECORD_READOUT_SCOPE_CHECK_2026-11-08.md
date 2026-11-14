---
claim_type: bounded_theorem
---

# Scope check for the neighborhood propagation and record-readout examples

**Type:** bounded_theorem

**Primary runner:** `scripts/gb1_cf_record_readout_scope_check_2026_11_14.py`
**Cached output:** `logs/runner-cache/gb1_cf_record_readout_scope_check_2026_11_14.txt`

This records the scope of the [positive constructions](SU2_NEIGHBORHOOD_PROPAGATION_RECORD_READOUT_BOUNDED_THEOREM_NOTE_2026-11-08.md)
and two explicit instrument-specific counterexamples. It is not a general no-go packet or an
audit verdict. No five-route negative-packet PASS is claimed.

## N1 — Actual routes and counterexamples

ATTEMPTED: copy permanent neighbor records down a supplied path. This succeeds.
ATTEMPTED: retain coherent data and form a fresh output record after adjacent
gates. Both the controlled-reversal and electric instruments succeed under
their stated quantum conditions.
ATTEMPTED: decode the electric vacuum using two work qubits, then uncompute.
This independent construction succeeds and returns its work.
ATTEMPTED: replace live data first by permanent computational-basis records.
The two phase states have identical outcome-labelled ensembles, and dephased
J3 has code overlap one half. These refute that particular substitution.

These are not five failed independent physical route families. Autonomous
formation, measurement-based computation with a prepared resource, different
codes, preparation records and history-dependent laws remain open. No universal
locality, permanence or framework obstruction is inferred.

## N2 — Conditions and implications

The tensor quantum state, allowed controls, preparation, driven schedule and
output instrument are one supplied experiment. No count of mutually independent
physical walls is claimed; mutual derivability is unresolved. The current-state
qualification is a distinct identification question, not a proof of impossibility.

## N3 — Hidden-condition check

The note names every gate and its geometry, its quantum state/preparation,
the Born instrument, the imposed future freezing of output, and the original
five-state gauge representation. It distinguishes the fixed-phase apparatus
from an autonomous all-origin law. The record relay separately supplies its
content support and formation order. The two models are not silently combined
into a single law.

## N4 — Residual matching

No prior no-go closes a residual here. The record-sufficiency note is a
comparison of causal-state choices, not imported exclusion of the present
candidate. Clock/thermal results and numerical counts from the routing source
are not used. No current-main audit verdict is changed.

## N5 — Resolutions tested

Per element: exact qubit gates, five code columns and electric projectors.
Per site: adjacent supports, one fresh output, and no reuse after recording.
Per block: the active link with arbitrary external entanglement; the final
electric instrument commutes with the supplied endpoint gauge actions.
Per mode: not tested; no dispersion, gap or continuum result is claimed.
Lattice-wide: the conditional copy induction works on arbitrary finite paths;
a global quantum code-preparation/record law is not constructed or excluded.

## N6 — Partial closure

The positive electric instrument uses the existing one-qubit site size.
Only the original fixed-spectator output subspace must expand for a recorded
one. A different causal-state realization may avoid changing axioms, so an
axiom change is not asserted necessary. The neighborhood wording was adopted
independently in PR #10143, as recorded in the [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md); it does not supply this instrument.

## N7 — Strongest counter-route

The successful fresh-output construction directly defeats the claim that
permanent records make coherent computation impossible. A prepared entangled
resource with local measurements and advancing output sites is another
concrete route to test. Its resource state, adaptive control, symmetry, and
relation to the framework's state sentence still need an actual construction.
Failure of data-first computational recording says nothing universal about it.

## N8 — Nearby work and preserved limits

The 2026-07-11 rank-one record-operation normal-form note distinguishes finite
same-carrier unitarity from enlarged/open instruments. The 2026-08-14
record-sufficiency note explicitly leaves preparation records, history
conditioning and live causal prestates as distinct routes. The 2026-09-24
isolated-formation note rejects the inference of independent outcomes merely
from separated dynamics. These scoped comparisons were inspected; no
retirement of a larger wall is inferred from their titles or status.

## Checks

The primary runner rebuilds this note's finite statements with dense state
vectors, apart from the theorem's exact-rational runner. It checks the
19-pair, 7-onsite electric instrument on all five code columns and with an
entangled external qubit; the commutation of `P0` and `P1` with endpoint
gauge actions; the two record-first counterexamples (equal recorded ensembles
for `J0` and `J1` against opposite certain electric values, and code overlap
`1/2` for dephased `J3`); and the record relay on a 13-step path that
approaches itself, before and after a rotation and translation. Six controls
must fail and do: two circuit mutations, a non-invariant projector, the
claim that live `J0` and `J1` already share a density matrix, live `J3` with
overlap `1/2`, and a relay with a second initial record beside the path. The
controlled-reversal experiment and the two-work-qubit decoder are checked
only by the theorem's runner,
`scripts/gb1_cf_neighborhood_record_readout_exact_2026_11_08.py`.
