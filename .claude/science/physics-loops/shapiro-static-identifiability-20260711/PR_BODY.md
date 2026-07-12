## Summary

This block closes the Shapiro static-discriminator missing derivation with the
narrowest exact result supported by the supplied harness:

- the old "causal" branch contained no time evolution; it supplied one
  position-only cone field array;
- for one fixed configured instance `X`, the detector readout is a
  deterministic map of that array, so an equal-array witness gives exactly the
  same detector vector and phase;
- this is an input-interface/history-label `no_go`, not construction of a
  physically admissible static solution and not a physical causal-vs-static
  theorem;
- the separate four-row fixed-layer control completes in 93.99 s with cone
  span `0.028991 rad`, fixed-layer span `0.000446 rad`, and pairing-free span
  gap `0.028544 rad`;
- both direct cache consumers and their paired notes/caches are aligned to the
  repaired semantics.

Independent audit is still required before the repository may treat this
source claim as effective `retained_no_go`.

## Exact audit blocker addressed

> The exact static-cone mimic is supported only because the runner's causal
> and static-cone field builders are algebraically identical; no independent
> causal propagation delay is actually computed in the causal branch. The
> note's broader boundary claim also requires the static scheduling curve to be
> near-flat, but the cached runner timed out with no results.

The repair does not invent the absent causal dynamics. It proves the exact
interface obstruction, exposes the missing temporal/static-admissibility
premises, and supplies completed assertion-gated scheduling rows.

## Trace and claim state

- [Handoff](HANDOFF.md)
- [Trace gate](TRACE_GATE.md)
- [Claim-status certificate](CLAIM_STATUS_CERTIFICATE.md)
- [Assumptions and imports](ASSUMPTIONS_AND_IMPORTS.md)
- [Route portfolio](ROUTE_PORTFOLIO.md)
- [No-Go Discipline N1-N8](NO_GO_DISCIPLINE_CHECKLIST.md)
- [Review history](REVIEW_HISTORY.md)
- [Primary theorem/no-go note](../../../../docs/SHAPIRO_STATIC_DISCRIMINATOR_NOTE.md)
- [Primary runner](../../../../scripts/shapiro_static_discriminator.py)
- [Primary cache](../../../../logs/runner-cache/shapiro_static_discriminator.txt)

Trace classification: `direct_blocker_closure` for
`shapiro_static_discriminator_note`.

Actual branch-local status: exact `no_go` proposal plus bounded finite
scheduling control. No bare retained/promoted or audit verdict is authored.

## Review disposition

Review-loop iteration 2:

- Code / Runner: PASS
- Physics Claim Boundary: NO-GO plus bounded finite control
- Imports / Support: DISCLOSED; no observed, fitted, literature, unit, or
  causal-law input is load-bearing for the exact theorem
- Nature Retention: NO-GO
- No-Go Discipline: PASS, N1-N8
- Repo Governance: PASS
- Audit Compatibility: PASS

Open physical routes are preserved: a physically admissible static comparator,
one field fixed across all cone indices, explicit retarded evolution, and an
interface carrying independent temporal/path history.

## Verification

```text
python3 -m py_compile scripts/shapiro_static_discriminator.py \
  scripts/shapiro_qa_retest_boundary.py \
  scripts/shapiro_unique_discriminator_v2.py

python3 scripts/precompute_audit_runners.py \
  --runners scripts/shapiro_static_discriminator.py,scripts/shapiro_qa_retest_boundary.py,scripts/shapiro_unique_discriminator_v2.py \
  --check-only --push-mode none --allow-non-main

python3 scripts/shapiro_qa_retest_boundary.py
python3 scripts/shapiro_unique_discriminator_v2.py
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Results: all caches fresh; all changed runners pass; primary cache
`ASSERTIONS: PASS`; strict audit lint has zero errors. Pipeline-generated audit
and effective-status outputs were validation-only and are not included in this
branch.

This PR is for review only. Do not merge it from the physics-loop worker.
