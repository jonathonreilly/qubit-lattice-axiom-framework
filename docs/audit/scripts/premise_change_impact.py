#!/usr/bin/env python3
"""Preview which live audits a pending edit would re-open, and what it costs.

Run this in a working tree that holds a proposed edit (for example a reworded
axiom section) before landing it. For every live judgment it rebuilds the
current science fingerprint with the same producer/comparator the
invalidation sweep uses (``audit_science_fingerprint``), so the preview can
never disagree with what ``invalidate_stale_audits.py`` will do to a judgment's
scientific basis. Rows re-opened only through a dependency (a downstream row
whose dependency's status drops) are reported separately as the cascade.

Read-only: it writes nothing and invokes no auditor. The cost estimate uses
the mean recorded cost of Claude seats in the run logs when there is one, and
otherwise the --usd-per-audit / --usd-per-critical-audit defaults, which are
rough list-price guesses. Critical rows count two seats.

  python3 docs/audit/scripts/premise_change_impact.py
  python3 docs/audit/scripts/premise_change_impact.py --json
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import audit_science_fingerprint  # noqa: E402
import ledger_io  # noqa: E402


LIVE_EXCLUDED_STATUSES = {None, "unaudited"}
RUN_LOG_GLOB = "logs/codex-audit-runs/*.jsonl"
# Rough per-seat guesses for a synchronous Claude Opus 5.5 request: dry-run
# prompts measured 225k-239k characters (~60-75k input tokens) on 2026-10-18.
# Replaced by recorded run-log means once real seats have run.
DEFAULT_USD_PER_AUDIT = 0.55
DEFAULT_USD_PER_CRITICAL_AUDIT = 1.10
DEFAULT_MONTHLY_CREDIT_USD = 400.0


def recorded_seat_costs(repo_root: Path) -> dict[str, float]:
    """Mean recorded estimated cost per Claude seat, keyed by effort."""
    costs: dict[str, list[float]] = {}
    for path in glob.glob(str(repo_root / RUN_LOG_GLOB)):
        try:
            lines = Path(path).read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        for line in lines:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("phase") != "claude_request":
                continue
            cost = event.get("estimated_cost_usd")
            effort = event.get("reasoning_effort")
            if isinstance(cost, (int, float)) and isinstance(effort, str):
                costs.setdefault(effort, []).append(float(cost))
    return {effort: sum(values) / len(values) for effort, values in costs.items()}


def seat_cost(criticality: str, recorded: dict[str, float], *,
              usd_per_audit: float, usd_per_critical_audit: float) -> float:
    effort_by_tier = {
        "leaf": "medium", "medium": "medium", "high": "high", "critical": "xhigh",
    }
    effort = effort_by_tier.get(criticality, "high")
    if effort in recorded:
        per_seat = recorded[effort]
    elif criticality == "critical":
        per_seat = usd_per_critical_audit
    else:
        per_seat = usd_per_audit
    return per_seat * (2 if criticality == "critical" else 1)


def direct_reopenings(rows: dict[str, dict], repo_root: Path) -> dict[str, str]:
    """Live judgments whose stored science baseline no longer matches."""
    epoch_cache: dict[str, str] = {}
    reopened: dict[str, str] = {}
    for cid, row in sorted(rows.items()):
        if row.get("audit_status") in LIVE_EXCLUDED_STATUSES:
            continue
        snapshot = row.get("audit_state_snapshot")
        baseline = (
            snapshot.get("science_fingerprint") if isinstance(snapshot, dict) else None
        )
        if baseline is None:
            reason = audit_science_fingerprint.legacy_science_epoch_change(
                repo_root, epoch_cache=epoch_cache
            )
        else:
            try:
                current = audit_science_fingerprint.build_matching_science_fingerprint(
                    baseline, row, rows, repo_root, epoch_cache=epoch_cache
                )
            except audit_science_fingerprint.ScienceFingerprintError as exc:
                reopened[cid] = f"science_fingerprint_unbuildable:{exc}"
                continue
            reason = audit_science_fingerprint.science_fingerprint_change(
                baseline, current
            )
        if reason is not None:
            reopened[cid] = reason
    return reopened


def reason_bucket(reason: str) -> str:
    """Group reasons: per premise unit, otherwise by the first two segments."""
    if reason.startswith("science_changed:premise_unit:"):
        return reason
    return ":".join(reason.split(":")[:2])


def cascade(rows: dict[str, dict], direct: set[str]) -> set[str]:
    """Live rows downstream of a directly re-opened row."""
    dependents: dict[str, set[str]] = {}
    for cid, row in rows.items():
        for dep in row.get("deps") or []:
            dependents.setdefault(dep, set()).add(cid)
    seen: set[str] = set()
    frontier = list(direct)
    while frontier:
        current = frontier.pop()
        for child in dependents.get(current, ()):
            if child in seen or child in direct:
                continue
            seen.add(child)
            frontier.append(child)
    return {
        cid for cid in seen
        if rows.get(cid, {}).get("audit_status") not in LIVE_EXCLUDED_STATUSES
    }


def impact_report(rows: dict[str, dict], repo_root: Path, *,
                  usd_per_audit: float = DEFAULT_USD_PER_AUDIT,
                  usd_per_critical_audit: float = DEFAULT_USD_PER_CRITICAL_AUDIT,
                  monthly_credit_usd: float = DEFAULT_MONTHLY_CREDIT_USD) -> dict:
    direct = direct_reopenings(rows, repo_root)
    downstream = cascade(rows, set(direct))
    recorded = recorded_seat_costs(repo_root)
    affected = sorted(set(direct) | downstream)
    by_tier = Counter(rows[cid].get("criticality") or "leaf" for cid in affected)
    cost = sum(
        seat_cost(
            rows[cid].get("criticality") or "leaf",
            recorded,
            usd_per_audit=usd_per_audit,
            usd_per_critical_audit=usd_per_critical_audit,
        )
        for cid in affected
    )
    live = sum(
        1 for row in rows.values()
        if row.get("audit_status") not in LIVE_EXCLUDED_STATUSES
    )
    return {
        "live_judgments": live,
        "direct": direct,
        "direct_reasons": dict(Counter(
            reason_bucket(reason) for reason in direct.values()
        )),
        "cascade": sorted(downstream),
        "affected_by_criticality": dict(by_tier),
        "estimated_reaudit_usd": round(cost, 2),
        "cost_basis": "recorded run-log means" if recorded else "defaults",
        "estimated_months_of_credit": (
            round(cost / monthly_credit_usd, 2) if monthly_credit_usd else None
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument("--json", action="store_true", help="Print the full report as JSON.")
    parser.add_argument("--usd-per-audit", type=float, default=DEFAULT_USD_PER_AUDIT)
    parser.add_argument(
        "--usd-per-critical-audit", type=float, default=DEFAULT_USD_PER_CRITICAL_AUDIT
    )
    parser.add_argument(
        "--monthly-credit-usd", type=float, default=DEFAULT_MONTHLY_CREDIT_USD
    )
    args = parser.parse_args(argv)
    rows = ledger_io.load_ledger().get("rows", {})
    report = impact_report(
        rows,
        REPO_ROOT,
        usd_per_audit=args.usd_per_audit,
        usd_per_critical_audit=args.usd_per_critical_audit,
        monthly_credit_usd=args.monthly_credit_usd,
    )
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    print(f"Live judgments: {report['live_judgments']}")
    print(f"Re-opened directly by this working tree: {len(report['direct'])}")
    for reason, count in sorted(report["direct_reasons"].items()):
        print(f"  {count:5d}  {reason}")
    print(f"Re-opened downstream (cascade): {len(report['cascade'])}")
    print(f"Affected by criticality: {report['affected_by_criticality']}")
    print(
        f"Estimated re-audit cost: ${report['estimated_reaudit_usd']:.2f} "
        f"({report['cost_basis']}; critical rows count two seats), about "
        f"{report['estimated_months_of_credit']} months at "
        f"${args.monthly_credit_usd:.0f}/month"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
