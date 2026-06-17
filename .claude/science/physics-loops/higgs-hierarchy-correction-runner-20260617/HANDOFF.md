# Handoff

This PR unlocks the Higgs hierarchy correction row by adding a focused primary
verifier for the source note's bounded negative result. Before this branch,
the queue selector saw:

- `claim_id`: `higgs_mass_hierarchy_correction_note`
- `criticality`: `critical`
- `runner_path`: `null`
- `ready`: `false`
- `transitive_descendants`: `359`

The new runner recomputes the L_t=2 and L_t=4 APBC eigenvalue sums, the
curvature ratio `A4/A2 = 8/7`, and the resulting mass direction. It also
checks that the near-125 first-power branch is recorded as a negative control
without a framework derivation.

No audit result, audit ledger row, publication table, active review queue, or
front-door status file is edited. Independent audit remains required.

Verification to rerun:

```bash
python3 scripts/frontier_higgs_mass_hierarchy_correction.py
python3 scripts/cached_runner_output.py scripts/frontier_higgs_mass_hierarchy_correction.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_higgs_mass_hierarchy_correction.py --check-only
python3 - <<'PY'
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location(
    "bcg", Path("docs/audit/scripts/build_citation_graph.py")
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
body = Path("docs/HIGGS_MASS_HIERARCHY_CORRECTION_NOTE.md").read_text(
    encoding="utf-8"
)
print(mod.extract_runner(body, "HIGGS_MASS_HIERARCHY_CORRECTION_NOTE.md"))
PY
```
