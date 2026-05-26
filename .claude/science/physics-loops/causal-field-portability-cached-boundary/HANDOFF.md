# Handoff

## Summary

This block repairs `causal_field_portability_note` by splitting the finite
cache diagnostic from the unresolved carrier and portability-criterion
derivations.

The preserved bounded result:

- exact-null detector delta: `0.000e+00`;
- exact-null field: `0.000e+00`;
- forward-only ratio spread: `0.423`;
- dynamic `c=0.5` ratio spread: `0.352`.

The note now says this is a diagnosed family boundary, not a cross-family
portability theorem, physical field-theory derivation, new axiom, or audit
verdict.

## Pipeline Result

`causal_field_portability_note` after `bash docs/audit/scripts/run_pipeline.sh`:

```yaml
claim_type: bounded_theorem
audit_status: unaudited
effective_status: unaudited
ready: true
criticality: high
transitive_descendants: 84
load_bearing_score: 9.909
deps: []
helper_runner_paths: []
open_dependency_paths: []
```

## Runner Output

```bash
PYTHONPATH=scripts python3 scripts/causal_field_portability_probe.py
```

Result:

```text
Causal field portability cached boundary certificate: PASS
PASS=59 FAIL=0
```

## Remaining Science

The growth/propagation/centroid carrier and a principled portability metric
remain open theorem targets.
