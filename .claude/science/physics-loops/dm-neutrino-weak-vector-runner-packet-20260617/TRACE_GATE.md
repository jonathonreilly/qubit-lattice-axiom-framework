# Trace Gate

Trace classification: `runner_artifact_repair`.

The gate passes when:

- build-citation-graph extraction resolves `scripts/frontier_dm_neutrino_weak_vector_theorem.py` as the parent row primary runner;
- the runner cache is fresh;
- the runner reports `18 PASS, 0 FAIL`.

Passing this trace gate does not apply an audit verdict.
