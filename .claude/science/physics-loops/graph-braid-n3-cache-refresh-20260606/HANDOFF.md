# Handoff

This branch repairs the direct audit packaging blocker for
`docs/GRAPH_BRAID_N3_FERMION_SIGN_STAYS_NONFIBERED_NARROW_THEOREM_NOTE.md`.

The source theorem note already names the runner and cache. On `origin/main`
the cache file was present but failed the repo verifier as corrupt. This branch
refreshes the cache through `scripts/cached_runner_output.py`, preserving the
actual runner output and adding the expected cache metadata:

```text
runner: scripts/frontier_graph_braid_n3_fermion_sign_nonfibered.py
exit_code: 0
status: ok
SCORECARD: PASS=26 FAIL=0
```

Replay:

```bash
python3 -m py_compile scripts/frontier_graph_braid_n3_fermion_sign_nonfibered.py
python3 scripts/frontier_graph_braid_n3_fermion_sign_nonfibered.py
python3 scripts/cached_runner_output.py scripts/frontier_graph_braid_n3_fermion_sign_nonfibered.py --check-only
```

No `docs/audit/**` files were edited. Independent re-audit is still required
before any ledger status changes.
