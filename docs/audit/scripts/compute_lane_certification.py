#!/usr/bin/env python3
"""Rolling lane certification (two-tier assurance, owner-approved 2026-07-12).

For each flagship lane in lane_certification_config.json, walk the configured
scientific root claim or claims and their transitive dependency closure and
report whether every row is currently chain-satisfying: retained-grade, a
decoration of a retained parent, or an accepted premise.
Certification is a state the repository re-enters continuously as audit
throughput catches up with landings — never a scheduled event. A lane's
marker rolling back (after an axiom edit or source change) is the honest
coordination signal, not an error.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import premise_nodes

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA = REPO_ROOT / "docs" / "audit" / "data"
CONFIG = DATA / "lane_certification_config.json"
LEDGER = DATA / "audit_ledger.json"
OUT = DATA / "lane_certification.json"

RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}


def is_accepted_premise(claim_id: str) -> bool:
    return premise_nodes.is_accepted_premise_dep(claim_id)


def status_satisfies_certification(claim_id: str, status: object) -> bool:
    """Match the pipeline's chain boundary without inventing premise policy."""
    if status in RETAINED_GRADE:
        return True
    if isinstance(status, str) and status.startswith("decoration_under_"):
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
        configured_roots = lane.get("roots")
        roots = (
            [str(value) for value in configured_roots if value]
            if isinstance(configured_roots, list)
            else [str(lane.get("root"))] if lane.get("root") else []
        )
        name = lane.get("lane")
        missing_roots = [root for root in roots if root not in rows]
        if not roots or missing_roots:
            missing = [
                {"claim_id": root, "effective_status": "not_in_ledger"}
                for root in missing_roots
            ]
            lanes_out.append({
                "lane": name,
                "root": roots[0] if len(roots) == 1 else None,
                "roots": roots,
                "certified": False,
                "closure_size": len(roots),
                "uncertified_count": len(missing) if roots else 1,
                "blocking": missing,
                "note": (
                    "no root claims configured"
                    if not roots
                    else f"root claims not in ledger: {missing_roots}"
                ),
            })
            continue
        seen: set[str] = set()
        frontier = list(roots)
        blocking: list[dict] = []
        invalid_roots: set[str] = set()
        for root in roots:
            root_row = rows[root]
            if not (
                root_row.get("claim_type") not in {"meta", "decoration"}
                and root_row.get("effective_status") in RETAINED_GRADE
            ):
                invalid_roots.add(root)
                blocking.append({
                    "claim_id": root,
                    "effective_status": root_row.get("effective_status"),
                    "reason": "root_not_retained_science",
                })
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
            if cid not in invalid_roots and not status_satisfies_certification(cid, status):
                blocking.append({"claim_id": cid, "effective_status": status})
            for dep in row.get("deps") or []:
                if dep not in seen:
                    frontier.append(dep)
        lanes_out.append({
            "lane": name,
            "root": roots[0] if len(roots) == 1 else None,
            "roots": roots,
            "closure_size": len(seen),
            "uncertified_count": len(blocking),
            "certified": not blocking,
            "blocking": sorted(
                blocking, key=lambda b: str(b.get("claim_id"))
            ),
        })

    OUT.write_text(json.dumps({
        "schema": "lane_certification_v2",
        "repo_head": head,
        "lanes": lanes_out,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for lane in lanes_out:
        mark = "CERTIFIED" if lane["certified"] else f"{lane.get('uncertified_count', '?')} blocking"
        print(f"lane_certification: {lane['lane']}: {mark} (closure {lane.get('closure_size')})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
