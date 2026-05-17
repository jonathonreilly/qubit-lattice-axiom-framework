#!/usr/bin/env python3
"""Resolve the full script-dependency chain for every audit-pending claim.

PROBLEM (systemic, observed in lattice_distance_law_note audit):
  Audit packets currently contain the source note + primary runner + cache.
  But primary runners often IMPORT from other scripts/*.py helper modules
  (e.g. lattice_no_barrier_distance.py imports from lattice_mirror_distance).
  Auditor sees opaque imports → falls back to `audited_conditional class C`
  even when the chain is sound.

THIS TOOL:
  For every claim_id in the audit queue (or audit ledger), parses the primary
  runner's Python AST to extract `from scripts.X import ...` / `import scripts.X`
  statements, walks the transitive closure, and reports the full set of
  scripts/*.py files the audit packet should contain.

OUTPUT:
  - stdout: summary report
  - logs/runner-cache/audit_packet_script_deps.txt: cached output
  - docs/audit/data/audit_packet_script_deps.json: machine-readable mapping
    {claim_id -> {primary_runner, helper_runner_paths[]}}

This output should be consumed by the audit packet builder (currently
external to the repo's audit pipeline) to assemble complete packets and
avoid spurious `class C` verdicts caused by missing helper modules.

Does not modify audit verdict/status data and performs no git operations.
When invoked, writes the diagnostic JSON map; callers may tee stdout to the
runner-cache log.
"""

from __future__ import annotations

import ast
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
AUDIT_DATA = REPO_ROOT / "docs" / "audit" / "data"


def parse_script_imports(script_path: Path) -> set[str]:
    """Return the set of helper script names this script imports.

    Looks for patterns like:
      from scripts.X import Y, Z
      import scripts.X
      from .X import Y  (relative inside scripts/)

    Returns a set of script basenames (without .py) that exist in scripts/.
    """
    if not script_path.exists():
        return set()
    try:
        tree = ast.parse(script_path.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        return set()

    helpers = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            module = node.module or ""
            # from scripts.X import ...
            if module.startswith("scripts."):
                helpers.add(module.removeprefix("scripts."))
            # from .X import ...  (relative within scripts/)
            elif node.level >= 1 and module:
                helpers.add(module)
            elif node.level >= 1 and not module:
                # `from . import X`
                for alias in node.names:
                    helpers.add(alias.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith("scripts."):
                    helpers.add(alias.name.removeprefix("scripts."))

    # Keep only those that exist as scripts/<name>.py
    return {h for h in helpers if (SCRIPTS_DIR / f"{h}.py").exists()}


def transitive_helpers(primary_script: str, seen: set[str] | None = None) -> set[str]:
    """Walk transitive imports starting from primary_script (basename).

    Returns the full set of helper script basenames (excluding primary).
    """
    if seen is None:
        seen = set()
    primary_path = SCRIPTS_DIR / f"{primary_script}.py"
    if not primary_path.exists():
        return set()
    direct = parse_script_imports(primary_path)
    new_helpers = direct - seen - {primary_script}
    seen.update(new_helpers)
    for h in list(new_helpers):
        seen.update(transitive_helpers(h, seen) - {primary_script})
    return seen - {primary_script}


def main() -> int:
    print("=" * 78)
    print("AUDIT PACKET SCRIPT-DEP RESOLVER")
    print("=" * 78)
    print()

    # Load audit ledger to get runner paths per claim_id
    ledger_path = AUDIT_DATA / "audit_ledger.json"
    queue_path = AUDIT_DATA / "audit_queue.json"

    if not ledger_path.exists():
        print(f"ERROR: missing {ledger_path}")
        return 1

    ledger = json.loads(ledger_path.read_text())
    rows = ledger.get("rows", {})

    print(f"Total claims in ledger: {len(rows)}")

    # Audit queue for pending status
    pending_ids = set()
    if queue_path.exists():
        queue = json.loads(queue_path.read_text())
        for q in queue.get("queue", []):
            pending_ids.add(q.get("claim_id", ""))
    print(f"Pending audits in queue: {len(pending_ids)}")
    print()

    # Map each claim_id -> {primary_runner, helper_runners/helper_runner_paths}
    deps_by_claim = {}
    claims_with_helpers = 0
    claims_no_runner = 0
    claims_runner_missing = 0
    total_helpers = 0
    helper_freq = defaultdict(int)

    for claim_id, row in rows.items():
        runner_path = row.get("runner_path", "")
        if not runner_path:
            claims_no_runner += 1
            continue
        # Normalize path
        rp = Path(runner_path)
        if not rp.is_absolute():
            rp = REPO_ROOT / rp
        if not rp.exists():
            claims_runner_missing += 1
            continue

        primary_basename = rp.stem
        helpers = transitive_helpers(primary_basename)

        deps_by_claim[claim_id] = {
            "primary_runner": str(rp.relative_to(REPO_ROOT)),
            "primary_basename": primary_basename,
            "helper_runners": sorted(helpers),
            "helper_runner_paths": [f"scripts/{h}.py" for h in sorted(helpers)],
            "is_pending": claim_id in pending_ids,
        }

        if helpers:
            claims_with_helpers += 1
            total_helpers += len(helpers)
            for h in helpers:
                helper_freq[h] += 1

    print(f"Claims with runner path: {len(deps_by_claim)}")
    print(f"Claims with no runner declared: {claims_no_runner}")
    print(f"Claims whose runner file is missing: {claims_runner_missing}")
    print()

    # Pending-only stats
    pending_with_helpers = sum(
        1 for d in deps_by_claim.values() if d["is_pending"] and d["helper_runners"]
    )
    pending_total = sum(1 for d in deps_by_claim.values() if d["is_pending"])
    print(f"Pending claims with helper imports (would trigger class-C bug): {pending_with_helpers} / {pending_total}")
    print()

    # Most common helpers
    print("Top 20 most-imported helper scripts:")
    for helper, count in sorted(helper_freq.items(), key=lambda kv: kv[1], reverse=True)[:20]:
        print(f"  {count:4d}x  scripts/{helper}.py")
    print()

    # Sample affected claims
    print("Sample claims that would trigger class-C from missing helpers:")
    samples = [
        (cid, d) for cid, d in deps_by_claim.items()
        if d["is_pending"] and d["helper_runners"]
    ][:10]
    for cid, d in samples:
        print(f"  - {cid}")
        print(f"      primary: {d['primary_runner']}")
        print(f"      helpers: {d['helper_runner_paths']}")
    print()

    # Save output
    output_path = AUDIT_DATA / "audit_packet_script_deps.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(deps_by_claim, indent=2, sort_keys=True))
    print(f"Wrote {output_path.relative_to(REPO_ROOT)}")
    print()

    print("=" * 78)
    print("RECOMMENDATION FOR AUDIT ORCHESTRATOR")
    print("=" * 78)
    print()
    print("When assembling the audit packet for claim_id X:")
    print("  1. Include the source note (docs/X.md)")
    print("  2. Include the primary runner (scripts/<primary>.py)")
    print("  3. Include the runner cache (logs/runner-cache/<primary>.txt)")
    print("  4. NEW: Include all transitive helper scripts named in")
    print("     audit_packet_script_deps.json[X]['helper_runner_paths']")
    print()
    print(f"This change would prevent {pending_with_helpers} pending audits from")
    print(f"hitting the class-C 'missing dependency' verdict due to packet")
    print(f"incompleteness alone.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
