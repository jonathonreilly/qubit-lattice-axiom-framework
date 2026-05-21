# `BMINUSL_ANOMALY_FREEDOM_THEOREM_NOTE_2026-04-24` — Downstream Surgical-Fix Record

**Date:** 2026-05-17
**Claim type:** meta
**Parent under repair:** [`BMINUSL_ANOMALY_FREEDOM_THEOREM_NOTE_2026-04-24.md`](BMINUSL_ANOMALY_FREEDOM_THEOREM_NOTE_2026-04-24.md)
**Wave:** downstream surgical-fix wave (direct dependent of `anomaly_forces_time_theorem`).
**Status:** branch-local hostile-audit findings; submitted as audit-prep input for the parent's pending audit review.
**Type:** fix-record meta-note (records what was patched; no new science content).
**Status authority:** independent audit lane only. This note does not set or predict the parent's audit outcome.

## 1. Source character

`BMINUSL_ANOMALY_FREEDOM_THEOREM_NOTE_2026-04-24.md` is a `positive_theorem`
that verifies the exact rational cancellation of all six `U(1)_{B-L}`
gauge anomaly traces `(G1)-(G6)` on the cited one-generation
Standard-Model matter content including `nu_R`. The arithmetic is via
`fractions.Fraction` and the runner reports `PASS=36, FAIL=0`.

The note correctly delineates **in-scope content** (the exact rational
anomaly arithmetic) from **admitted-context** (matter content,
hypercharge convention, anomaly-cancellation-as-quantum-consistency
principle, standard SM `B`/`L` bookkeeping). The hostile-audit-grade
issue fixed here is about the **tier qualifier** on the cited
upstreams; the arithmetic is unchanged.

## 2. Findings

### F-A — Tier over-claim "retained" for cited upstreams

**Symptom:** approximately 8 sites in §1-§5 described the cited
one-generation content / hypercharge convention / gauge group /
companion as "retained":

| Section | Original wording |
|---|---|
| §1 Statement (l. 26) | "On the retained one-generation matter surface including `nu_R`" |
| §1 Statement (l. 31) | "Using the doubled-hypercharge convention of the retained notes" |
| §1 Statement (l. 44) | "gauging `U(1)_{B-L}` on the retained `SU(3) x SU(2) x U(1)_Y` matter content" |
| §4 Consequences (l. 144) | "anomaly-consistent and gaugeable on the retained one-generation content" |
| §4 Consequences (l. 145) | "the extension is quantum-consistent on the retained matter spectrum" |
| §4 Consequences (l. 147) | "The retained `nu_R` slot" |
| §5 Scope Boundary (l. 158) | "gaugeability of `U(1)_{B-L}` on the retained content" |
| §5 Scope Boundary (l. 163) | "that `U(1)_{B-L}` is part of the retained gauge group" |
| §6 Falsifiability (l. 182) | "compatible with the retained companion story" |

**Reality (per 2026-05-17 ledger snapshot):**

| Upstream | `audit_status` | `effective_status` |
|---|---|---|
| `one_generation_matter_closure_note` | `unaudited` | `unaudited` |
| `standard_model_hypercharge_uniqueness_theorem_note_2026-04-24` | `unaudited` | `unaudited` |
| `anomaly_forces_time_theorem` | `unaudited` | `unaudited` |

**All three** named load-bearing upstreams are `unaudited`. Calling
them or their consequences "retained" is therefore over-stated.

**Fix:** all 8 sites now use "cited …" wording. New §10 "Upstream-tier
accounting (2026-05-17)" provides the tier table and explicitly states
the gaugeability conclusion's effective tier inherits from the weakest
upstream. The exact rational arithmetic of `(G1)-(G6)` is unaffected and
does not require any retained-tier upstream to be valid.

### Admission-inheritance note (lower-stringency)

The admission-inheritance pattern is **less stringent** for this note
than for sibling downstreams. This note imports only the
*anomaly-cancellation-as-quantum-consistency principle* from
`ANOMALY_FORCES_TIME_THEOREM` — a standard QFT input the upstream parent
itself treats as admission (i)-routed. It does **not** import:

- `d_t = 1`;
- the `(3, 1)` signature;
- admissions (i)-(iv) as direct proof steps in `(G1)-(G6)`.

So the upstream parent's recent F-B framing-fix does not propagate into
this note's arithmetic — only its overall effective tier (bounded above
by the weakest upstream tier). Recorded in §10 for downstream-audit
disambiguation.

## 3. What this fix does NOT do

- Change the (G1)-(G6) anomaly arithmetic.
- Change the matter-content table in §1.
- Change the runner expectation (`PASS=36, FAIL=0`).
- Change the §5 "claims / does not claim" or §8 "out of scope" lists.
- Change the §6 proton-decay falsifiability framing.
- Promote any upstream companion or alter any retained-tier claim.
- Modify pipeline code or any other source theorem note.
- Set or predict an audit outcome.

## 4. Suggested auditor verdict

`audited_conditional` (positive_theorem retained; effective tier
inherits from the weakest upstream, currently `unaudited` for all
three named load-bearing upstreams).

The corrected note brings the in-note tier description into line with
the ledger. The arithmetic of `(G1)-(G6)` is unaffected. Once any of
the named upstreams audits through, the note's effective tier rises
toward the weakest *audited* upstream tier automatically.

## 5. Verification

Paired runner:
`scripts/frontier_bminusl_anomaly_freedom_downstream_fix.py`

Programmatically verifies:

- **F-A:** all 8 stale "retained" sites have been retired and replaced
  with "cited" wording in live narrative blocks; new §10 "Upstream-tier
  accounting (2026-05-17)" subsection present; tier table lists the
  three upstreams at `unaudited`; effective-tier-inherits-from-weakest
  wording present.
- **Structural invariants:** §1 matter-content table preserved;
  `(G1)-(G6)` arithmetic preserved (`Tr[B-L] = 0`, `Tr[(B-L)^3] = 0`,
  …); runner expectation `PASS=36, FAIL=0` preserved; §5 / §8
  scope-boundary lists preserved; admission-inheritance note (lower
  stringency) recorded.

Cached output: `logs/runner-cache/frontier_bminusl_anomaly_freedom_downstream_fix.txt`.

## 6. Cross-references (non-load-bearing)

- [`BMINUSL_ANOMALY_FREEDOM_THEOREM_NOTE_2026-04-24.md`](BMINUSL_ANOMALY_FREEDOM_THEOREM_NOTE_2026-04-24.md) — parent under repair
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md) — upstream parent (principle import only)
- [`ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md`](ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md) — upstream F-B fix (does not directly propagate into G1-G6 arithmetic; tier inheritance only)
- [`ONE_GENERATION_MATTER_CLOSURE_NOTE.md`](ONE_GENERATION_MATTER_CLOSURE_NOTE.md) — cited matter-content companion (`unaudited`)
- [`STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md`](STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24.md) — cited hypercharge companion (`unaudited`)
- [PR #1507](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1507) — sibling downstream fix (`s3_anomaly_spacetime_lift_note`)
- [PR #1509](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1509) — sibling downstream fix (`dt1_time_dimension_proof_walk`)
- [PR #1510](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1510) — sibling downstream fix (`s3_time_spacetime_tensor_primitive`)
- [PR #1511](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1511) — sibling downstream fix (`axiom_first_sm_anomaly_cancellation_complete`)
- [PR #1512](https://github.com/jonathonreilly/cl3-lattice-framework/pull/1512) — sibling downstream fix (`chronology_protection`)
