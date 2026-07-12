#!/usr/bin/env python3
"""Rolling lane certification (two-tier assurance, owner-approved 2026-07-12).

For each flagship lane in lane_certification_config.json, walk the root
claim's transitive dependency closure in the citation graph and report
whether every row is currently retained-grade (or an accepted premise).
Certification is a state the repository re-enters continuously as audit
throughput catches up with landings — never a scheduled event. A lane's
marker rolling back (after an axiom edit or source change) is the honest
coordination signal, not an error.
"""
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA = REPO_ROOT / "docs" / "audit" / "data"
CONFIG = DATA / "lane_certification_config.json"
LEDGER = DATA / "audit_ledger.json"
OUT = DATA / "lane_certification.json"

RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go", "meta"}
ACCEPTED_PREFIXES = ("minimal_axioms",)


def is_accepted_premise(claim_id: str) -> bool:
    if claim_id.startswith(ACCEPTED_PREFIXES) or claim_id.endswith("_primitive"):
        return True
    return False


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = ledger.get("rows", {})
    try:
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT,
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        head = None

    lanes_out = []
    for lane in config.get("lanes", []):
        root = lane.get("root")
        name = lane.get("lane")
        if root not in rows:
            lanes_out.append({
                "lane": name, "root": root, "certified": False,
                "closure_size": 0, "blocking": [],
                "note": "root claim not in ledger",
            })
            continue
        seen: set[str] = set()
        frontier = [root]
        blocking: list[dict] = []
        while frontier:
            cid = frontier.pop()
            if cid in seen:
                continue
            seen.add(cid)
            if is_accepted_premise(cid):
                continue
            row = rows.get(cid)
            if row is None:
                blocking.append({"claim_id": cid, "effective_status": "not_in_ledger"})
                continue
            status = row.get("effective_status")
            if status not in RETAINED_GRADE and not str(status or "").startswith(
                "decoration_under_"
            ):
                blocking.append({"claim_id": cid, "effective_status": status})
            for dep in row.get("deps") or []:
                if dep not in seen:
                    frontier.append(dep)
        lanes_out.append({
            "lane": name,
            "root": root,
            "closure_size": len(seen),
            "uncertified_count": len(blocking),
            "certified": not blocking,
            "blocking": sorted(
                blocking, key=lambda b: str(b.get("claim_id"))
            )[:15],
        })

    OUT.write_text(json.dumps({
        "schema": "lane_certification_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repo_head": head,
        "lanes": lanes_out,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for lane in lanes_out:
        mark = "CERTIFIED" if lane["certified"] else f"{lane.get('uncertified_count', '?')} blocking"
        print(f"lane_certification: {lane['lane']}: {mark} (closure {lane.get('closure_size')})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
