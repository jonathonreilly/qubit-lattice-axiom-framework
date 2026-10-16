# Actual entry invocation

The scientific fixture was launched once through `functions.exec` / `exec_command`:

```text
/opt/homebrew/opt/python@3.13/bin/python3.13 /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/local_conserving_sparse_compiler_fixture/run_fixture.py
```

The outer working directory was `/Users/jonreilly/Documents/Codex`; the tool yielded session 19829 and was polled once to completion. The launcher created a fresh `runs/attempt_01`, copied its own source and the scientific source before execution, and ran the exact child argv in `EXECUTION.json`. Both child streams were redirected to the retained full stdout/stderr files. The outer launcher printed the same receipt object stored as `EXECUTION.json`; no additional outer scientific result was emitted. No earlier small checker was launched.

`seal_packet.py` is a subsequent deterministic bookkeeping step. It verifies source/stream hashes and parent identities, copies those exact parents, checks emitted-list counts and adjacency from the saved JSON, and freezes the packet. It does not rerun matrix propagation or perform another scientific experiment.
