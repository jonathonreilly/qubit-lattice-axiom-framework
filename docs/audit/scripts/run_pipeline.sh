#!/usr/bin/env bash
# Run the full audit-lane pipeline end to end.
#
# This script is mechanical and deterministic. It does NOT perform any
# audits — those are done by the current best Codex GPT model at maximum
# reasoning (or any independent auditor)
# using AUDIT_AGENT_PROMPT_TEMPLATE.md, with results applied via
# scripts/apply_audit.py.
#
# Run order:
#   1. build_citation_graph.py       -> data/citation_graph.json
#   2. seed_audit_ledger.py          -> data/audit_ledger.json (preserves
#                                       prior audits if note hash unchanged)
#   3. sanitize_legacy_audit_artifacts.py
#                                      -> removes deprecated author-status keys
#   4. classify_runner_passes.py     -> data/runner_classification.json
#                                       (heuristic; optional, slow on cold cache)
#   5. compute_load_bearing.py       -> updates graph criticality metrics
#   6. compute_effective_status.py   -> applies claim_type-based status + summary
#   7. invalidate_stale_audits.py    -> resets stale audit verdicts
#   8. build_cycle_inventory.py      -> data/cycle_inventory.json
#   9. compute_audit_queue.py        -> data/audit_queue.json (consumes
#                                       cycle inventory for break targets)
#  10. compute_reaudit_candidates.py -> data/reaudit_candidates.json
#  11. compute_audit_dispatch_queue.py
#                                      -> data/audit_dispatch_queue.json
#  12. compute_auditor_reliability.py-> data/auditor_reliability.json
#  13. audit_lint.py                 -> validates the ledger against hard rules
#  14. render_audit_ledger.py        -> writes AUDIT_LEDGER.md
#  15. render_publication_effective_status.py
#                                      -> writes audit-derived publication views
#  16. render_front_door_status.py    -> writes docs/repo/FRONT_DOOR_STATUS.md
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../../.." && pwd)"
cd "${REPO_ROOT}"

echo "==> 0/16 check_axiom_premise_clean.py (guard: axiom/primitive premise docs stay pure)"
python3 docs/audit/scripts/check_axiom_premise_clean.py

echo "==> 1/16 build_citation_graph.py"
python3 docs/audit/scripts/build_citation_graph.py

echo "==> 2/16 seed_audit_ledger.py"
python3 docs/audit/scripts/seed_audit_ledger.py

echo "==> 3/16 sanitize_legacy_audit_artifacts.py"
python3 docs/audit/scripts/sanitize_legacy_audit_artifacts.py

echo "==> 4/16 classify_runner_passes.py"
python3 docs/audit/scripts/classify_runner_passes.py

echo "==> 5/16 compute_load_bearing.py"
python3 docs/audit/scripts/compute_load_bearing.py

echo "==> 6/16 compute_effective_status.py"
python3 docs/audit/scripts/compute_effective_status.py

echo "==> 7/16 invalidate_stale_audits.py"
for attempt in 1 2 3 4 5 6 7 8 9 10; do
  python3 docs/audit/scripts/invalidate_stale_audits.py
  invalidated="$(
    python3 - <<'PY'
import json
with open("docs/audit/data/audit_ledger.json", encoding="utf-8") as f:
    print(len(json.load(f).get("last_invalidations", [])))
PY
  )"
  if [[ "${invalidated}" == "0" ]]; then
    break
  fi
  echo "==> 7.${attempt}/16 compute_effective_status.py post-invalidation (${invalidated} invalidated)"
  python3 docs/audit/scripts/compute_effective_status.py
done

if [[ "${invalidated}" != "0" ]]; then
  echo "invalidate_stale_audits.py did not reach a fixed point after 10 passes" >&2
  exit 1
fi

echo "==> 8/16 build_cycle_inventory.py"
python3 docs/audit/scripts/build_cycle_inventory.py

echo "==> 9/16 compute_audit_queue.py"
python3 docs/audit/scripts/compute_audit_queue.py

echo "==> 10/16 compute_reaudit_candidates.py"
python3 docs/audit/scripts/compute_reaudit_candidates.py

echo "==> 11/16 compute_audit_dispatch_queue.py"
python3 docs/audit/scripts/compute_audit_dispatch_queue.py

echo "==> 12/16 compute_auditor_reliability.py"
python3 docs/audit/scripts/compute_auditor_reliability.py

echo "==> 13/16 audit_lint.py"
python3 docs/audit/scripts/audit_lint.py

echo "==> 14/16 render_audit_ledger.py"
python3 docs/audit/scripts/render_audit_ledger.py

echo "==> 15/16 render_publication_effective_status.py"
python3 docs/audit/scripts/render_publication_effective_status.py

echo "==> 16/16 render_front_door_status.py"
python3 docs/audit/scripts/render_front_door_status.py

echo
echo "Pipeline complete."
echo "  Read docs/audit/AUDIT_LEDGER.md for the rendered ledger."
echo "  Read docs/audit/AUDIT_QUEUE.md   for the next-up audit queue."
echo "  Read docs/repo/FRONT_DOOR_STATUS.md for the front-door status snapshot."
echo "  Read docs/audit/data/reaudit_candidates.json for unblocked re-audit candidates."
echo "  Read docs/audit/AUDIT_DISPATCH_QUEUE.md for dispatcher-only targeted re-audits."
echo "  Read docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md for the"
echo "    audit-vs-publication-tables gap report."
echo "  Read docs/publication/ci3_z3/<NAME>_EFFECTIVE_STATUS.md for the audit-"
echo "    derived view of each publication table."
