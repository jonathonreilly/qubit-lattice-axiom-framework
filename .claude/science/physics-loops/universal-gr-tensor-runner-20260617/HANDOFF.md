# Handoff

This PR unlocks the universal GR tensor variational candidate row by registering
the existing primary verifier in the source note. Before this branch, the queue
selector saw:

- `claim_id`: `universal_gr_tensor_variational_candidate_note`
- `criticality`: `critical`
- `runner_path`: `null`
- `ready`: `false`
- `transitive_descendants`: `651`

The source runner already existed and passed. This branch makes it
discoverable via a top-level `**Script:**` line and refreshes the cache after
renaming the runner banner to verifier language.

No audit result, audit ledger row, publication table, active review queue, or
front-door status file is edited. Independent audit remains required.

Verification to rerun:

```bash
python3 scripts/frontier_universal_gr_tensor_variational_candidate.py
python3 scripts/cached_runner_output.py scripts/frontier_universal_gr_tensor_variational_candidate.py --check-only
python3 - <<'PY'
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location(
    "bcg", Path("docs/audit/scripts/build_citation_graph.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
body = Path("docs/UNIVERSAL_GR_TENSOR_VARIATIONAL_CANDIDATE_NOTE.md").read_text(
    encoding="utf-8"
)
print(mod.extract_runner(body, "UNIVERSAL_GR_TENSOR_VARIATIONAL_CANDIDATE_NOTE.md"))
PY
```
