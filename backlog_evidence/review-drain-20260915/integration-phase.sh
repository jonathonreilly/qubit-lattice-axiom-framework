#!/bin/bash
# This phase leaves the exclusively owned checkout for exact landing/cleanup.
set -eu
phase_root=/private/tmp/review-drain-20260915
phase_label=$1
cd "$phase_root/integration-one"
export PYTHONDONTWRITEBYTECODE=1
python3 - "$phase_root" "$phase_label" <<'PY'
from pathlib import Path
import json,re,sys
root=Path(sys.argv[1]);label=sys.argv[2]
assert re.fullmatch(r'train[0-9]+[a-z]?',label)
s=json.loads((root/'integration-one.json').read_text())
assert s['owner']==label and s['path']==str(root/'integration-one')
PY
phase_verified_head=$(git rev-parse HEAD)
phase_exit() {
  phase_status=$?
  trap - EXIT INT TERM
  if [ "$phase_status" -ne 0 ]; then
    # Strict release fails closed if HEAD or tracked/untracked/ignored state moved.
    python3 /Users/jonBridger/.codex/skills/review-loop/scripts/review_workspace.py release \
      --repo "$phase_root/integration-one" --pool "$phase_root" --slot integration-one \
      --owner "$phase_label" --expected-head "$phase_verified_head" \
      > "$phase_root/$phase_label-phase-failure-release.json" \
      2> "$phase_root/$phase_label-phase-failure-release.stderr" || true
  fi
  exit "$phase_status"
}
trap phase_exit EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
python3 "$phase_root/prepare_candidate_normalized.py" "$phase_label" > "$phase_root/$phase_label-prepare.log" 2>&1
phase_verified_head=$(git rev-parse HEAD)
bash docs/audit/scripts/run_pipeline.sh --stage-citation-manifest > "$phase_root/$phase_label-pipeline.log" 2>&1
python3 docs/audit/scripts/audit_lint.py --strict > "$phase_root/$phase_label-strict.log" 2>&1
python3 docs/audit/scripts/check_changed_audit_evidence.py --base origin/main > "$phase_root/$phase_label-evidence.txt" 2>&1
