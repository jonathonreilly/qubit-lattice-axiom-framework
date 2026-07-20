#!/usr/bin/env bash
# Fast pre-commit hook for the audit lane.
#
# Runs ONLY the mechanical seeding + lint stages (graph + seed + lint).
# Does NOT run runner classification, load-bearing recompute, or
# invalidation — those belong to the full pipeline run on CI / cron.
#
# Goal: catch obvious problems (new note added without seeding, hash
# drift on an audited claim, hard-rule violation) before commit, in a
# few seconds.
#
# Install:
#   ln -sf ../../docs/audit/scripts/pre_commit_audit_check.sh .git/hooks/pre-commit
#
# Bypass with --no-verify only when you understand the cost.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "${REPO_ROOT}"

STAGED="$(git diff --cached --name-only)"

# Runner cache staleness: the selector reverse-maps every staged path to known
# runners whose AUDIT_INPUT_PATHS include it, in addition to staged runners.
# Run it unconditionally so a declared-input-only edit cannot evade the gate.
if ! python3 scripts/precompute_audit_runners.py --staged-only --check-only; then
    echo "[pre-commit] runner cache STALE for a staged runner or declared input."
    echo "  Refresh with:"
    echo "    python3 scripts/precompute_audit_runners.py --staged-only"
    echo "  then 'git add logs/runner-cache/' and commit again."
    echo "  (Pass --no-verify only if you understand the audit-evidence cost.)"
    exit 1
fi

# Quick path: skip ledger checks if no docs/ files are staged.
if ! echo "$STAGED" | grep -qE '^docs/.*\.md$'; then
    exit 0
fi

echo "[pre-commit] audit-lane check"

python3 docs/audit/scripts/ledger_io.py --materialize >/dev/null
python3 docs/audit/scripts/build_citation_graph.py >/dev/null
python3 docs/audit/scripts/seed_audit_ledger.py >/dev/null

if ! python3 docs/audit/scripts/audit_lint.py; then
    echo "[pre-commit] audit_lint FAILED"
    echo "  Fix the errors above, or run the full pipeline with"
    echo "    bash docs/audit/scripts/run_pipeline.sh"
    echo "  to refresh the ledger."
    exit 1
fi

# Claim-typing ratchet: a staged docs/**.md whose reseeded ledger row still
# shows the silent positive_theorem default (no Type: header, no
# meta/excluded pattern) blocks the commit. Legacy untyped rows surface as
# audit_lint `claim_type_defaulted` warnings; this gate only refuses to
# grow (or re-commit into) that class.
if ! echo "$STAGED" | python3 docs/audit/scripts/check_staged_claim_typing.py; then
    echo "[pre-commit] staged claim note(s) lack an explicit claim type (see above)."
    exit 1
fi

# If seeding changed the tracked source-of-truth shards or metadata but those
# changes are not staged, ask the developer to stage them. The monolith and
# citation graph are ignored materialized caches.
UNTRACKED_LEDGER="$(git ls-files --others --exclude-standard -- \
  docs/audit/data/ledger docs/audit/data/ledger_meta.json)"
if ! git diff --quiet docs/audit/data/ledger docs/audit/data/ledger_meta.json 2>/dev/null \
  || [[ -n "${UNTRACKED_LEDGER}" ]]; then
    echo "[pre-commit] tracked audit-ledger shards updated by seeding."
    echo "  Stage docs/audit/data/ledger and"
    echo "  docs/audit/data/ledger_meta.json, then commit again."
    exit 1
fi

echo "[pre-commit] audit-lane check OK"
