# Asymmetry Persistence + Collapse Note

**Date:** 2026-04-02 (rescoped 2026-05-23)
**Status:** narrow qualitative observations from the completed N=80 stdout

**Audit-narrowing acknowledgment (2026-05-23):**
The 2026-05-10 audit verdict
(`asymmetry_persistence_collapse_note`, `audited_failed`,
`auditor_confidence = high`, `load_bearing_step_class = C`,
`load_bearing_score = 2.585`) states:

> "Issue: the note's bounded tables are stale relative to the supplied
> runner source/stdout, and the runner depends on unlisted imported
> infrastructure for graph generation, propagation, layernorm, and
> pruning. Why this blocks: the conclusion depends on exact finite rows,
> especially the N=100 layernorm collapse pocket, but the current packet
> neither reproduces those rows nor supplies the imported closure
> authority. Repair target: align the runner/note configuration, provide
> a completed cached log or sliced deterministic runner for the stated
> sweep, and cite/audit the imported infrastructure. Claim boundary
> until fixed: the packet only supports partial qualitative observations
> from the completed N=80 stdout, not the full bounded claim."

This source-note edit adopts the audit verdict's explicitly-named
"Claim boundary until fixed" as the new scope of the note. The
N=100 quantitative rows and the narrow N=100 layernorm-assisted
collapse-pocket claim are removed from the bounded surface. What
remains is the partial qualitative observation set from the
completed N=80 stdout. This source edit does not set audit status
or hand-author audit JSON. Generated audit outputs are regenerated
by the review pipeline.

Helper-runner one-hop dependencies have been registered on the
audit-ledger row via `helper_runner_paths` (PR #1700 fix to the
audit-packet parser), so the next audit pass receives the helper
script set alongside the primary runner.

## Cited authority chain

The primary runner registered against this row is
`scripts/asymmetry_persistence_collapse_pilot.py`
(`runner_sha256 = e39f93682f3659b7a5343d0b24e228be936c0fe492dfd68697de0939ba5887d2`,
audit-window cache: `status: timeout, exit_code: None, elapsed_sec: 120.01`
at the standard `120 s` audit budget, deposited at
[`logs/runner-cache/asymmetry_persistence_collapse_pilot.txt`](../logs/runner-cache/asymmetry_persistence_collapse_pilot.txt)).
The pilot is genuinely slow because it sweeps the full
`N in {80, 100}` grid; this note's narrowed bounded surface only
references the partial qualitative content from the completed N=80
portion of that sweep, not the unreached N=100 portion.

Helper one-hop dependencies (registered as `helper_runner_paths`):

- `scripts/asymmetry_persistence_pilot.py`
  (provides `generate_3d_asymmetry_persistence_dag`)
- `scripts/gap_topological_asymmetry.py`
  (admitted-context input)
- `scripts/gap_topological_asymmetry_layernorm_combo.py`
  (admitted-context input; provides the layernorm-regulated propagator
  and asymmetry-persistence pruning rule used by all rows of the
  asymmetry-persistence cluster).

Closure of the regulated-propagator + pruning-rule step lives on the
admitted-context bracket of those imports, not this row.

## Question

Does the generated asymmetry-persistence geometry remain useful when we add
stochastic collapse?

This pilot compares, on the same dense 3D generated graphs:

- baseline generated geometry
- asymmetry persistence only
- collapse only
- asymmetry persistence + collapse

When feasible, it also compares linear propagation against per-layer
normalization.

Script:
[scripts/asymmetry_persistence_collapse_pilot.py](../scripts/asymmetry_persistence_collapse_pilot.py)

Log:
[logs/2026-04-02-asymmetry-persistence-collapse-pilot.txt](../logs/2026-04-02-asymmetry-persistence-collapse-pilot.txt)
(historical frozen log path; the live audit-window cache deposit is
`logs/runner-cache/asymmetry_persistence_collapse_pilot.txt`, see
"Cited authority chain" above for status).

## Setup (sweep configuration; only the N=80 portion is in scope of this note)

The primary runner is configured to sweep:

- dense generated 3D graphs
- `N=80` with `npl=50` (in scope of this note)
- `N=100` with `npl=60` (OUT OF SCOPE for this note's narrowed bounded
  surface; the audit-window run did not complete the N=100 portion
  within the 120 s budget)
- thresholds `0.00, 0.10, 0.20`
- `8` matched seeds
- collapse probability `p=0.2`
- Monte Carlo realizations (runner default; the audit verdict noted a
  source/stdout configuration mismatch on the realization count, which
  the narrowed qualitative surface no longer relies on)

## Qualitative observations from the completed N=80 stdout (in scope)

The narrowed bounded surface of this note is the following partial
qualitative observation set drawn from the completed N=80 portion of
the runner's stdout at the audit window:

- in the unitary lane at N=80, the persistence-pruned geometry
  registers a lower `pur_min` than the unpruned baseline at the swept
  thresholds, with the per-layer-normalization variant registering
  lower still;
- in the linear collapse lane at N=80, the persistence-pruned
  geometry does not register a uniform lowering of detector purity
  relative to the unpruned baseline; the qualitative direction is
  consistent with "not a generic collapse rescue at N=80".

These observations are qualitative directional summaries of the
completed N=80 stdout. No specific numerical row, threshold-row, or
pocket on the N=100 portion of the sweep is asserted by this note.

## Narrow conclusion

Within the narrowed N=80 qualitative scope:

- the generated asymmetry-persistence geometry registers a unitary
  decoherence aid (lower `pur_min`) at N=80;
- the same geometry does not register a generic stochastic-collapse
  rescue at N=80.

The note does not assert any quantitative N=100 row and does not
assert the existence of a narrow N=100 layernorm-assisted
collapse-pocket pocket. Any such pocket is OUT OF SCOPE of this
note's bounded surface and would require a completed N=100 cached
artifact or a sliced deterministic runner that demonstrates it
within the audit compute budget.

## What is closed inside the audited scope (narrowed)

- The qualitative observation that asymmetry-persistence is a unitary
  decoherence aid at N=80 and is not a generic collapse rescue at
  N=80, supported by the completed N=80 portion of the registered
  runner's audit-window stdout.

## What remains open (named missing bridges, OUT OF SCOPE)

- The N=100 quantitative rows and the narrow N=100 layernorm-assisted
  collapse-pocket claim. Closing these would require either a faster
  harness that completes the N=100 portion within the audit compute
  budget, a wider compute window declared as the intentionally-slow
  reason, a completed cached stdout artifact for the N=100 portion, or
  a sliced deterministic runner for that portion of the sweep.
- Audit/citation of the helper one-hop closure authorities
  (`scripts/asymmetry_persistence_pilot.py`,
  `scripts/gap_topological_asymmetry.py`,
  `scripts/gap_topological_asymmetry_layernorm_combo.py`).
- Reconciliation of the runner/source-note configuration on the
  Monte Carlo realization count (the narrowed qualitative surface no
  longer relies on this).

## Boundary

This source note does not set audit status or hand-author audit JSON,
does not assert a generic collapse rescue, does not assert any
specific N=100 quantitative row, and does not assert any narrow N=100
layernorm-assisted collapse pocket. Its bounded surface is the
partial qualitative observations from the completed N=80 stdout of
the registered primary runner. It records the cited audit-snapshot
repair path, cites the registered primary runner and its frozen
audit-window cache, and names the admitted-context helper imports the
row depends on.
