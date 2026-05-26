# Handoff

## Summary

This block repairs `gate_b_farfield_note` by splitting the auditable numerical
result from the unresolved physical Gate B bridge.

The preserved bounded result is the committed h=0.5 far-field cache:

| Row | TOWARD | F~M |
|---|---:|---:|
| `drift=0.3,rest=0.5` | `36/36` | `1.00` |
| `drift=0.2,rest=0.7` | `36/36` | `1.00` |
| `drift=0.1,rest=0.9` | `36/36` | `1.00` |
| `exact grid` | `36/36` | `1.00` |

The note now says this is not a physical Gate B bridge theorem, not a clean
Gate B closure, and not a new axiom or audit verdict.

## Pipeline Result

`gate_b_farfield_note` after `bash docs/audit/scripts/run_pipeline.sh`:

```yaml
claim_type: bounded_theorem
audit_status: unaudited
effective_status: unaudited
ready: true
criticality: critical
transitive_descendants: 122
load_bearing_score: 14.443
deps: []
open_dependency_paths: []
```

## Runner Output

```bash
PYTHONPATH=scripts python3 scripts/gate_b_farfield_harness.py
```

Result:

```text
Gate B far-field cached certificate: PASS
PASS=28 FAIL=0
```

## Remaining Science

The primitive-to-physical-gravity bridge remains open. A future theorem would
need to derive the source law, propagation/readout map, valley-linear action,
and TOWARD/F~M far-field criterion from accepted primitives.
