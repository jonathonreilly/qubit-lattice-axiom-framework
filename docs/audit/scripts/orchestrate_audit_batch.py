#!/usr/bin/env python3
"""Batch audit orchestrator (fitness-review F1, owner-approved direction).

Drains a flagship lane (or an explicit claim list) with parallel
restricted-packet Sol xhigh auditors under the two-tier regime:

  round:  targets = dep-ready unaudited rows in scope
          -> prep (runner cache refresh, vocab check)
          -> parallel detached codex workers (2 passes on critical rows)
          -> serialized apply -> pipeline -> lint -> commit -> push per claim
          -> recompute readiness; next round

Reliability mechanics baked in from the 2026-07-11/12 lived pattern:
stdin-closed detached launches; deliverable monitored by SIZE (placeholder
files lie); per-worker stall kill; apply/commit/push retried on main races;
one claim per commit; direct-main push for routine verdicts per the
audit-loop skill authorization.

Scope guard: claim_type=no_go rows (forensic tier) are REPORTED and skipped
in v1 — forensic packets need the heavyweight evidence transport and are run
individually per the audit-loop skill.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS.parents[2]
DATA = REPO_ROOT / "docs" / "audit" / "data"
RETAINED = {"retained", "retained_bounded", "retained_no_go", "meta"}
AUDITABLE_TYPES = {"positive_theorem", "bounded_theorem", "open_gate"}

SPEC_TEMPLATE = """# AUDIT TASK (restricted packet, fresh context): {cid} — pass {pass_no}

You are an independent hostile auditor for this physics repo's audit lane.
Judge ONLY from the restricted packet. Do NOT read the audit ledger, any
prior audit rationale, publication framing, or any file not listed below.
{second_pass_line}

## Governing instructions (read in order)
1. docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md (role, step classes, verdict
   rules, output schema; note its tier-scope preamble — this is a
   DEVELOPMENT-TIER row)
2. docs/ai_methodology/skills/audit-loop/references/nature-grade-rubric.md
3. docs/audit/FRESH_LOOK_REQUIREMENTS.md
4. docs/audit/ALGEBRAIC_DECORATION_POLICY.md
5. docs/audit/README.md (orientation; see 'Two-Tier Assurance')

## The claim
- claim_id: {cid}
- source note: {note_path}
- ledger claim_type author hint: {claim_type} (you own the final claim_type)
- one-hop dependencies (read them): {deps}
- primary runner: {runner_path}
- runner cached output: {cache_path}

## Tier
Development tier: if walls/negative boundaries are named, answer N1-N8 as
structured judgments with quoted evidence in a `no_go_discipline` object
(structural validation; no manifest-containment, live-stdout, transport, or
full-universe disposition plumbing is required of you).

## Mandatory independent math audit
Re-derive every load-bearing identity OUTSIDE the runner's implementation
path (your own fresh symbolic/manual computation). A wrong displayed formula
anywhere in the packet forbids audited_clean.

## Output
EXACTLY ONE JSON object (template §5 fields) written in ONE shot at the END
(no placeholder writes) to:
    {out_json}
with provenance fields:
    "auditor": "codex-audit-batch-{ident}",
    "auditor_family": "codex-gpt-5.6",
    "auditor_model": "gpt-5.6-sol",
    "auditor_reasoning_effort": "xhigh",
    "independence": "{independence}"
Stdout: 3-line summary. Do not edit repo files.
"""


def sh(cmd: list[str], cwd: Path | None = None, timeout: int | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd or REPO_ROOT), capture_output=True, text=True, timeout=timeout)


def load_rows() -> dict[str, dict]:
    ledger = json.loads((DATA / "audit_ledger.json").read_text(encoding="utf-8"))
    return ledger.get("rows", {})


def accepted(cid: str) -> bool:
    return cid.startswith("minimal_axioms") or cid.endswith("_primitive")


def dep_ready(row: dict, eff: dict[str, str]) -> bool:
    for dep in row.get("deps") or []:
        if accepted(dep):
            continue
        status = eff.get(dep, "MISSING")
        if status in RETAINED or str(status).startswith("decoration_under_"):
            continue
        return False
    return True


def lane_closure(root: str, rows: dict[str, dict]) -> set[str]:
    seen: set[str] = set()
    frontier = [root]
    while frontier:
        cid = frontier.pop()
        if cid in seen or accepted(cid):
            continue
        seen.add(cid)
        row = rows.get(cid)
        if not row:
            continue
        frontier.extend(d for d in (row.get("deps") or []) if d not in seen)
    return seen


def compute_targets(scope: set[str], rows: dict[str, dict]) -> tuple[list[dict], list[str]]:
    eff = {cid: r.get("effective_status", "?") for cid, r in rows.items()}
    targets, skipped = [], []
    for cid in sorted(scope):
        row = rows.get(cid)
        if not row:
            continue
        if row.get("effective_status") in RETAINED or str(
            row.get("effective_status") or ""
        ).startswith("decoration_under_"):
            continue
        if row.get("audit_status") not in {None, "unaudited"}:
            skipped.append(f"{cid}: audit_status={row.get('audit_status')}")
            continue
        ctype = row.get("claim_type") or row.get("claim_type_author_hint")
        if ctype == "no_go":
            skipped.append(f"{cid}: no_go row — forensic tier, run individually")
            continue
        if ctype not in AUDITABLE_TYPES:
            skipped.append(f"{cid}: claim_type={ctype} — not batch-auditable")
            continue
        if not dep_ready(row, eff):
            continue
        targets.append(row)
    return targets, skipped


def launch_worker(row: dict, pass_no: int, workdir: Path) -> dict:
    cid = row["claim_id"]
    ident = f"{'A' if pass_no == 1 else 'B'}-{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4().hex[:6]}"
    out_json = workdir / f"audit_{cid[:60]}_{pass_no}.json"
    spec = SPEC_TEMPLATE.format(
        cid=cid,
        pass_no=("1" if pass_no == 1 else "2 (independent confirmation)"),
        second_pass_line=(
            "You have not seen and must not seek any prior audit of this claim."
            if pass_no == 2 else ""
        ),
        note_path=row.get("note_path"),
        claim_type=row.get("claim_type") or row.get("claim_type_author_hint"),
        deps=json.dumps([d for d in (row.get("deps") or [])]),
        runner_path=row.get("runner_path") or "(none recorded)",
        cache_path=(
            f"logs/runner-cache/{Path(row['runner_path']).stem}.txt"
            if row.get("runner_path") else "(none)"
        ),
        out_json=str(out_json),
        ident=ident,
        independence=("cross_family" if pass_no == 1 else "fresh_context"),
    )
    spec_path = workdir / f"spec_{cid[:60]}_{pass_no}.md"
    spec_path.write_text(spec, encoding="utf-8")
    log = open(workdir / f"log_{cid[:60]}_{pass_no}.txt", "w")
    proc = subprocess.Popen(
        [
            "codex", "exec", "-m", "gpt-5.6-sol",
            "-c", "model_reasoning_effort=xhigh",
            "-s", "read-only", "-C", str(REPO_ROOT),
            "-o", str(workdir / f"lastmsg_{cid[:60]}_{pass_no}.txt"),
            spec,
        ],
        stdin=subprocess.DEVNULL, stdout=log, stderr=log, cwd=str(REPO_ROOT),
    )
    return {"cid": cid, "pass": pass_no, "proc": proc, "out": out_json, "log": log}


def wait_workers(jobs: list[dict], stall_minutes: int = 45) -> None:
    deadline = time.time() + stall_minutes * 60
    while time.time() < deadline:
        pending = [j for j in jobs if j["proc"].poll() is None]
        delivered = sum(1 for j in jobs if j["out"].exists() and j["out"].stat().st_size > 200)
        if not pending or delivered == len(jobs):
            break
        time.sleep(30)
    for j in jobs:
        if j["proc"].poll() is None:
            j["proc"].kill()
        j["log"].close()


def apply_serialized(jobs: list[dict], report: list[dict], retries: int = 3) -> None:
    for j in sorted(jobs, key=lambda x: (x["cid"], x["pass"])):
        if not (j["out"].exists() and j["out"].stat().st_size > 200):
            report.append({"cid": j["cid"], "pass": j["pass"], "result": "no_delivery"})
            continue
        try:
            verdict = json.loads(j["out"].read_text(encoding="utf-8")).get("verdict")
        except json.JSONDecodeError:
            report.append({"cid": j["cid"], "pass": j["pass"], "result": "malformed_json"})
            continue
        applied = False
        for attempt in range(retries):
            sh(["git", "fetch", "origin", "main", "-q"])
            sh(["git", "reset", "--hard", "origin/main", "-q"])
            sh(["git", "clean", "-qfd"])
            res = sh([sys.executable, str(SCRIPTS / "apply_audit.py"), "--file", str(j["out"])], timeout=1800)
            if "Applied 1/1" not in res.stdout:
                report.append({
                    "cid": j["cid"], "pass": j["pass"], "result": "apply_rejected",
                    "detail": (res.stdout + res.stderr).strip().splitlines()[:2],
                })
                break
            pipe = sh(["bash", str(SCRIPTS / "run_pipeline.sh")], timeout=1800)
            lint = sh([sys.executable, str(SCRIPTS / "audit_lint.py"), "--strict"], timeout=600)
            if pipe.returncode != 0 or lint.returncode != 0:
                report.append({"cid": j["cid"], "pass": j["pass"], "result": "pipeline_or_lint_failed"})
                break
            sh(["git", "add", "-A"])
            pass_word = "first" if j["pass"] == 1 else "second"
            sh(["git", "commit", "-q", "-m",
                f"audit: {j['cid']} {verdict} (codex-cli, gpt-5.6-sol, xhigh, {pass_word}/batch)"])
            push = sh(["git", "push", "-q", "origin", "HEAD:main"])
            if push.returncode == 0:
                report.append({"cid": j["cid"], "pass": j["pass"], "result": verdict})
                applied = True
                break
        if not applied and not any(
            r for r in report if r["cid"] == j["cid"] and r["pass"] == j["pass"]
        ):
            report.append({"cid": j["cid"], "pass": j["pass"], "result": "push_race_exhausted"})


def main() -> int:
    ap = argparse.ArgumentParser(description="Batch audit orchestrator (development tier)")
    scope_group = ap.add_mutually_exclusive_group(required=True)
    scope_group.add_argument("--lane", help="lane name from lane_certification_config.json")
    scope_group.add_argument("--claims", help="comma-separated claim ids")
    ap.add_argument("--max-workers", type=int, default=6)
    ap.add_argument("--rounds", type=int, default=6)
    ap.add_argument("--stall-minutes", type=int, default=45)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    dirty = sh(["git", "status", "--porcelain"]).stdout.strip()
    if dirty and not args.dry_run:
        print("refusing to run: repository checkout is not clean (the apply "
              "loop resets to origin/main). Run from a dedicated clean audit "
              "worktree.")
        return 2

    workdir = Path(os.environ.get("AUDIT_BATCH_WORKDIR") or f"/tmp/audit_batch_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}")
    workdir.mkdir(parents=True, exist_ok=True)
    report: list[dict] = []

    for round_no in range(1, args.rounds + 1):
        rows = load_rows()
        if args.lane:
            config = json.loads((DATA / "lane_certification_config.json").read_text(encoding="utf-8"))
            roots = [l["root"] for l in config.get("lanes", []) if l.get("lane") == args.lane]
            if not roots:
                print(f"unknown lane {args.lane!r}")
                return 2
            scope = lane_closure(roots[0], rows)
        else:
            scope = {c.strip() for c in args.claims.split(",") if c.strip()}
        targets, skipped = compute_targets(scope, rows)
        print(f"== round {round_no}: {len(targets)} dep-ready targets, {len(skipped)} skipped")
        for line in skipped:
            print(f"   skip: {line}")
        if not targets:
            break
        if args.dry_run:
            for row in targets:
                passes = 2 if row.get("criticality") == "critical" else 1
                print(f"   would audit: {row['claim_id']} (passes={passes})")
            break
        batch = targets[: max(1, args.max_workers // 2)]
        jobs: list[dict] = []
        for row in batch:
            runner = row.get("runner_path")
            if runner:
                sh([sys.executable, str(REPO_ROOT / "scripts" / "cached_runner_output.py"), runner], timeout=1800)
            passes = 2 if row.get("criticality") == "critical" else 1
            for p in range(1, passes + 1):
                jobs.append(launch_worker(row, p, workdir))
        print(f"   launched {len(jobs)} workers; waiting (stall {args.stall_minutes}m)")
        wait_workers(jobs, args.stall_minutes)
        apply_serialized(jobs, report)
        (workdir / "report.jsonl").write_text(
            "".join(json.dumps(r, sort_keys=True) + "\n" for r in report), encoding="utf-8"
        )

    print("== batch report ==")
    for r in report:
        print(f"   {r['cid']} p{r['pass']}: {r['result']}")
    print(f"report: {workdir / 'report.jsonl'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
