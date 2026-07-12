# No-Go Discipline Checklist

Status: **PASS** for the narrow input-interface/history-label no-go after
review iteration 1. This is source-side stress testing, not an audit verdict.

## N1 — Alternative Route Enumeration

| Attack on the exact theorem | Marker | Evidence and result |
|---|---|---|
| Hidden history/mechanism label reaches the kernel | ATTEMPTED | Source inspection of `_propagate` shows that it receives positions, adjacency, one field array, and sources; it receives no history or mechanism label. Attack fails on the supplied interface. |
| Cone index `q` leaks directly into the readout | ATTEMPTED | `_propagate` and `_phase_lag_against_baseline` receive the already-built field array, not `q`. Attack fails for the exact theorem. |
| Stateful or nondeterministic propagation distinguishes two equal arrays | ATTEMPTED | With the configured instance fixed, `_propagate` contains no random draw, time state, mutable history, or mechanism-conditioned branch. Equal inputs follow the same deterministic operations. |
| Snapshot and witness use unequal fixed instances or baselines | ATTEMPTED | The theorem fixes `X` and `F_0`; the runner computes one phase and reuses it only after exact node-array equality. The no-go does not compare different graphs, sources, constants, or baselines. |
| Zero detector norm makes the phase undefined | ATTEMPTED | The theorem explicitly restricts to cases where normalized phase is defined. The implementation's zero-norm convention is also identical for equal inputs. This is a domain boundary, not a counterexample. |
| Comparator restricted to physically admissible static solutions | ATTEMPTED | No static field equation, source law, boundary data, or physical admissibility class exists in the runner. This restriction changes the comparator class and remains a live physical question outside the theorem. |
| One equal-array witness must be fixed for all `q` | ATTEMPTED | The theorem quantifier is pointwise in `q`. Requiring one field across all indices changes the quantifier and remains an open stricter hypothesis test. |
| Readout carries independent temporal/path history | ATTEMPTED | That information is absent from the current interface and would evade the theorem by changing its domain. More same-time detector components do not evade equal-input determinism unless they carry independent history. |

These are eight distinct attacks on the narrow theorem. None is counted as a
physical retarded-field calculation or as an exclusion of future temporal
models.

## N2 — Wall-Independence Audit

The exact theorem has no conditional walls. Its explicit scope premises are:
one fixed configured instance, an unconstrained node-array input class, equal
arrays, a deterministic map, and a defined normalized phase. Temporal dynamics
and physical static-solution admissibility are different future surfaces, not
missing walls whose count is inflated here.

## N3 — Hidden-Wall Scan

The source note, runner, and checklist were scanned for `we assume`, `by
construction`, `as is standard`, `the framework provides`, `bridge context`,
`background`, `naturally`, `obviously`, `standard QFT`, `registered`, and
`canonical`.

- The fixed configured instance `X` now exposes positions, adjacency, source
  and detector nodes, baseline, kernel constants, and all non-field inputs.
- The comparator class is explicitly the unconstrained array space `R^V`.
- The equal-array witness is not called a solution of a physical static field
  equation.
- Determinism is exposed by source inspection.
- Time, source history, physical units, static-solution admissibility, and a
  propagation-speed meaning for `c` are explicitly excluded.
- Numeric constants and thresholds are load-bearing only for the finite
  fixed-layer control, not for the exact theorem.

No hidden wall remains in the narrowed claim.

## N4 — Residual Matching

| Witness | Residual attacked | Residual closed here | Match? |
|---|---|---|---|
| `scripts/shapiro_static_discriminator.py` field-array interface | whether history/mechanism information reaches the detector kernel | history-label identifiability at the supplied input interface | yes |
| old equal cone builders, preserved in the git history and quoted audit blocker | whether the purported causal comparator was independently evolved | the old comparator was only a position-only snapshot | yes |
| completed fixed-layer rows | whether delays 0–3 at cone index 1 are near-flat on the configured grid | only the finite span sentence | yes |
| earlier physical Shapiro/causal-field claims | physical propagation or field-speed interpretation | not used as witnesses | dropped |

No observed value, archived causal table, physical static solution, or
different Shapiro residual is counted toward the exact no-go.

## N5 — Rhetoric Audit

| Resolution | Tested? | Allowed statement |
|---|---|---|
| unconstrained node-array input | yes, exact equality | equal arrays are the same interface input |
| detector amplitude vector | yes, deterministic image | vectors are equal |
| single normalized detector-overlap phase | yes where defined | phases are equal |
| same-snapshot multi-detector vector | yes by the same deterministic argument | extra components do not restore an absent history label |
| configured family/seed/cone rows | yes, expected count derived from configuration | finite implementation witness is complete |
| physically admissible static solution | no | explicitly not claimed |
| one field fixed across all indices | no | explicitly not claimed |
| edge-time, multi-time, or path-history data | no | explicitly not claimed; live escape surface |
| all schedules or all observables | no | explicitly not claimed |

The source text uses the narrowest resolution: one fixed configured instance,
the unconstrained field-array interface, and its deterministic detector phase.

## N6 — Partial-Closure Path Scan

The live path around the no-go is constructive:

1. introduce an explicit temporal state and source history;
2. supply initial/boundary data and an evolution law;
3. define a physically admissible static comparator class rather than all of
   `R^V`; and
4. use a readout that receives independent temporal/path information.

A naming change from `c` to “speed” cannot supply these objects. The approved
premise registry
[`axiom_premise_nodes.json`](../../../../docs/audit/data/axiom_premise_nodes.json)
contains no primitive that supplies retarded dynamics, a physical static field
equation, or a history-sensitive readout. The constructive path remains in the
opportunity queue and is not foreclosed.

## N7 — Steelman

A hostile reviewer should object that an equal-array duplicate in `R^V` need
not satisfy any physically admissible static field equation; that one
physically fixed static field may not reproduce an indexed curve; and that a
retarded field sampled along a moving probe may carry edge-time history which
cannot be compressed into one node array. Those objections are decisive
against a physical or global causal-vs-static claim. The source note now makes
none. They do not break the stated input-interface theorem: the supplied
runner admits unconstrained arrays, receives no history label, holds the
configured instance fixed, and applies a deterministic readout. On exactly
that surface, the equal-array witness is unavoidable.

The steelman caused the comparator class, fixed inputs, quantifier, and
physical-static-solution firewall to be made explicit.

## N8 — Cross-Cycle Echo

- [`SHAPIRO_DELAY_NOTE.md`](../../../../docs/SHAPIRO_DELAY_NOTE.md) replays a
  position-only cone mimic and excludes a physical field-speed measurement.
- [`CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md`](../../../../docs/CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md)
  excludes a self-consistent retarded-potential equation and physical wave
  speed.
- No later edit introduced temporal evolution into the target runner.

The similar historical wall has not been retired by convention or metadata.
The available retirement mechanism is the explicit temporal/static-solution
extension already considered under N1, N6, and N7.

## Final Gate

All N1–N8 checks pass for the narrow theorem. They would fail for any of these
broader claims, which are forbidden: an equal-array witness is a physical
static solution; no static mechanism can mimic a causal process; one fixed
field matches the whole curve; all schedules are near-flat; or every causal
observable is snapshot-duplicable.
