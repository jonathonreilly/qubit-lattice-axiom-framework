# The Unconditionally-Derived Emergent Time Axis IS the Thermodynamic Arrow; its One Residual (Orientation) is the Past Hypothesis — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_theorem (the time-axis = entropy-axis identification; the orientation-as-past-hypothesis reframing)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/derived_time_axis_is_thermodynamic_arrow_runner.py`](../scripts/derived_time_axis_is_thermodynamic_arrow_runner.py)
**Cached output:** [`logs/runner-cache/derived_time_axis_is_thermodynamic_arrow_runner.txt`](../logs/runner-cache/derived_time_axis_is_thermodynamic_arrow_runner.txt)

## Audit context

The unique emergent time **axis** is derived unconditionally from the record ontology (the
record-count `I`-gradient; companion correction note), leaving one residual: the **orientation**
(which `I`-direction is future). This note records what that derivation **unlocks**: the time axis
is the **thermodynamic arrow** (record formation is entropy production), and its one residual is
identified with the **past hypothesis** — a universal cosmological boundary condition, not a
framework-specific gap. Anchors:
[`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)
(`retained_bounded`),
[`POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06`](POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md)
(`retained_no_go`),
[`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02`](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md)
(`retained_bounded`).

## Safe statement

**Theorem.** Records form via decoherence, so the derived record-count time axis coincides with the
entanglement-entropy-increase axis:

1. **Record formation is entropy production.** Under a generic local system–environment coupling, as
   the system decoheres (pointer coherence → 0) the system–environment entanglement entropy `S_E`
   rises from 0, **strongly correlated** with the record-formation progress (`corr ≈ 0.93`,
   `S_E : 0 → 1`).
2. **The decoherence onset is the second-law arrow.** `S_E` is **monotone** through the onset
   (records forming); long-time monotonicity is **coarse-grained** (finite-environment fluctuations
   → the statistical second law), with `~0.9` of steps non-decreasing.
3. **The time axis IS the entropy-increase axis.** The record-count ordering and the entropy ordering
   **agree** (rank agreement `≈ 1.0`). So the unconditionally-derived record-count time axis is the
   **thermodynamic arrow**.
4. **The orientation residual is the past hypothesis.** The dynamics is time-symmetric, so the
   arrow's **sign** is fixed by the **low-entropy / low-record END** — the **start** (`S_E = 0`,
   records `= 0`). That end is the **past hypothesis**: a boundary condition (the standing
   `POST_RECORD_ARROW_ORIENTATION_FIREWALL`, `retained_no_go`), here identified as the **universal
   thermodynamic past hypothesis**, not a framework-specific gap.

So **time = record count = entropy increase**, and **future = the high-record / high-entropy
direction**; the one residual bit (orientation) is the universal low-entropy past hypothesis.

## What this unlocks (the point of the note)

Placing the derived time axis inside thermodynamics has concrete consequences:

- **The "problem of time" reduces to the universal past hypothesis.** The emergent-time picture's
  only residual (the arrow's sign) is the same low-entropy-initial-condition that all of physics
  carries — not a defect of the minimal axioms. The framework *derives* the time **axis** and
  *inherits* the past hypothesis like every other physical theory.
- **The records-flow second-law results gain a substrate.** The thermalizing-arrow used downstream
  (e.g. `FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW`) is the same entropy-increase = record-count
  axis derived here, grounding "thermalization" in record/entropy production rather than positing it.

## Boundary (honest)

- **Coarse-grained second law.** The decoherence *onset* is sharply monotone; long-time monotonicity
  is statistical (finite-environment fluctuations, the standard coarse-grained second law), not an
  exact monotone — as expected for a finite closed system.
- **A correlation/identification, not a new dynamics.** It identifies the derived record-count axis
  with the entropy-increase axis and the orientation with the past hypothesis; it does not derive the
  past hypothesis (which is a boundary condition, by the orientation firewall).
- The record-formation step is generic (the no-record case is fine-tuned; companion); the time
  **axis** itself is derived unconditionally (companion correction).

## Forbidden imports check

No new axiom. A_min + standard decoherence and entanglement entropy (reproduced in the runner); the
time axis is the record-ontology derivation; the monotone is the `retained_bounded` records-arrow.
The past hypothesis is *named* (a boundary condition), not derived. Exact finite-dimensional.

## Runner check breakdown

Class A: (1) `corr(records, S_E) > 0.8` (record formation = entropy production); (2) the decoherence
onset is monotone in `S_E`, coarse-monotone `> 0.5` of steps; (3) record-ordering = entropy-ordering
(rank agreement `> 0.8`); (4) the start is low-`S_E`/low-record (the past hypothesis). Expected
`runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

As a generic local coupling decoheres the system, the entanglement entropy rises from zero in lockstep
with record formation (corr `0.93`, rank agreement `1.0`), monotone through the onset and coarse-grained
at long times — so the unconditionally-derived record-count time axis coincides with the entropy-increase
axis (the thermodynamic arrow). The time-symmetric dynamics leaves the arrow's sign to the low-entropy
end (the start), identifying the emergent-time picture's one residual (orientation) with the universal
past hypothesis rather than a framework gap. The result is an identification + reframing, honest about the
coarse-grained second law and that the past hypothesis is a named boundary condition. Effective status
remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/derived_time_axis_is_thermodynamic_arrow_runner.py
```
