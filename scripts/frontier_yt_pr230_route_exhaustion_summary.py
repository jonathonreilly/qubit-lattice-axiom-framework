#!/usr/bin/env python3
"""Gate for the PR230 route-exhaustion summary note."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "YT_PR230_ROUTE_EXHAUSTION_SUMMARY_NOTE_2026-05-22.md"
OUTPUT = ROOT / "outputs" / "yt_pr230_route_exhaustion_summary_2026-05-22.json"


def main() -> int:
    text = NOTE.read_text(encoding="utf-8")
    checks = {
        "status_support_only": "not retained; not proposed_retained" in text,
        "backup_branch_named": "backup/pr230-pre-clean-20260522-172104558" in text,
        "surviving_gate_named": "source-coupled site-diagonal local action" in text
        and "external compositional one-site product RN source semantics" in text,
        "direct_compute_demoted": "partial" in text
        and "chunk outputs must not be promoted" in text,
        "fh_lsz_blocker_named": "canonical `O_H`, scalar LSZ normalization" in text,
        "wz_blocker_named": "accepted electroweak action authority" in text,
        "schur_blocker_named": "non-identifiability" in text,
        "lsp_firewall_named": "measurement instrumentation" in text
        and "themselves a source selector" in text,
        "negative_scope_limited": "not universal no-go theorems" in text,
        "forbidden_import_firewall": all(
            token in text
            for token in (
                "`H_unit`",
                "`yt_ward_identity`",
                "`y_t_bare`",
                "`alpha_LM`",
                "fitted selectors",
            )
        ),
    }
    for name, ok in checks.items():
        print(f"{'PASS' if ok else 'FAIL'}: {name}")

    result = {
        "status": "route-memory support only / no retained or proposed_retained claim",
        "proposal_allowed": False,
        "checks": checks,
        "pass_count": sum(1 for ok in checks.values() if ok),
        "fail_count": sum(1 for ok in checks.values() if not ok),
        "review_surface": [
            "docs/YT_PR230_ROUTE_EXHAUSTION_SUMMARY_NOTE_2026-05-22.md",
            "scripts/frontier_yt_pr230_route_exhaustion_summary.py",
            "outputs/yt_pr230_route_exhaustion_summary_2026-05-22.json",
        ],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(f"SUMMARY: PASS={result['pass_count']} FAIL={result['fail_count']}")
    return 0 if result["fail_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
