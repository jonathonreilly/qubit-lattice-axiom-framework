# Handoff

This PR unlocks the quark mass-ratio support packet row by registering the
existing primary bundle verifier in the source note. Before this branch, the
queue selector saw:

- `claim_id`: `quark_mass_ratio_note_2026-04-18`
- `criticality`: `critical`
- `runner_path`: `null`
- `ready`: `false`
- `transitive_descendants`: `629`

The source runner already existed and passed. This branch makes it
discoverable via a top-level `**Script:**` line, changes runner wording from
audit-output language to source-side subrunner-output language, and refreshes
the cache.

No audit result, audit ledger row, publication table, active review queue, or
front-door status file is edited. Independent audit remains required.

Verification to rerun:

```bash
python3 scripts/frontier_quark_mass_ratio_review.py
python3 scripts/cached_runner_output.py scripts/frontier_quark_mass_ratio_review.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_quark_mass_ratio_review.py --check-only
python3 - <<'PY'
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location(
    "bcg", Path("docs/audit/scripts/build_citation_graph.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
body = Path("docs/QUARK_MASS_RATIO_NOTE_2026-04-18.md").read_text(
    encoding="utf-8"
)
print(mod.extract_runner(body, "QUARK_MASS_RATIO_NOTE_2026-04-18.md"))
PY
```
