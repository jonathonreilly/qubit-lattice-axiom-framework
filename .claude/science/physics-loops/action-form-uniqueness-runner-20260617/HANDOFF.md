# Handoff

This PR unlocks the action-form uniqueness no-go row by adding a direct primary
verifier for the source note's scoped no-go. Before this branch, the queue
selector saw:

- `claim_id`: `bridge_gap_action_form_uniqueness_no_go_note_2026-05-06`
- `criticality`: `critical`
- `runner_path`: `null`
- `ready`: `false`
- `transitive_descendants`: `266`

The new runner verifies the source candidate set, canonical parameter
coexistence, finite-beta Wilson/HK split, and the later HK-diffusion theorem's
open residual boundary.

While adding the verifier, the source note's Manton normalization was corrected:
its displayed matching equation implies `beta_M = 1` at `g_bare = 1`, not
`beta_M = 1/3`.

No audit result, audit ledger row, publication table, active review queue, or
front-door status file is edited. Independent audit remains required.

Verification to rerun:

```bash
python3 scripts/frontier_bridge_gap_action_form_uniqueness_no_go.py
python3 scripts/cached_runner_output.py scripts/frontier_bridge_gap_action_form_uniqueness_no_go.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_bridge_gap_action_form_uniqueness_no_go.py --check-only
python3 - <<'PY'
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location(
    "bcg", Path("docs/audit/scripts/build_citation_graph.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
body = Path("docs/BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md").read_text(
    encoding="utf-8"
)
print(mod.extract_runner(body, "BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md"))
PY
```
