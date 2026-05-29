# Handoff

This branch repairs one audited conditional instanton row by narrowing the
claim to a supplied-normalization certificate:

```text
S_inst = 8 pi^2 / g^2
```

The branch intentionally does not claim retained Atiyah-Singer integrality,
BPST existence, Luescher lattice topology, framework substrate identification,
hierarchy closure, or observation contact. Those remain separate science
targets.

Verification run:

```text
python3 -m py_compile scripts/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.py
python3 scripts/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.py --force --push-mode none --allow-non-main --concurrency 1
bash docs/audit/scripts/run_pipeline.sh
```

Result: the target row is in the audit queue as `ready: true` with no open
dependency paths.
