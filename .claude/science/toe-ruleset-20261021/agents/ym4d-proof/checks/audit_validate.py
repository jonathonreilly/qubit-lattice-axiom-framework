"""Validate mapping provenance and file scope; no mathematical verification."""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

BASE = Path(__file__).resolve().parents[1]
ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
manifest = json.loads((BASE / "checks/audit_source_manifest.json").read_text())
graph = json.loads((BASE / "checks/audit_graph.json").read_text())
report = (BASE / "AUDIT.md").read_text()
checks = []


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(name, passed, detail):
    checks.append(dict(name=name, passed=bool(passed), detail=detail))


baseline = {x["path"]: x for x in manifest["files"]}
missing = [p for p in baseline if not (BASE / p).is_file()]
changed = [p for p in baseline if (BASE / p).is_file() and sha(BASE / p) != baseline[p]["sha256"]]
check("preexisting_lane_source_bytes_unchanged", not missing and not changed,
      dict(files=len(baseline), missing=missing, changed=changed))
current = {str(p.relative_to(BASE)) for p in BASE.rglob("*") if p.is_file()}
new = sorted(current - baseline.keys())
def allowed(p):
    return p in {"AUDIT.md", "AUDIT_LOG.md"} or p.startswith("checks/audit_")
unexpected = [p for p in new if not allowed(p)]
check("new_files_within_authorized_scope", not unexpected, dict(new=new, unexpected=unexpected))

head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
check("head_unchanged_no_commit", head == manifest["head"], dict(head=head))
diff = subprocess.run(["git", "diff", "--quiet", "HEAD", "--"], capture_output=True, text=True)
check("tracked_worktree_and_index_unchanged", diff.returncode == 0,
      dict(returncode=diff.returncode, stderr=diff.stderr))
status = subprocess.check_output(["git", "status", "--porcelain=v1", "--untracked-files=all"], text=True)
check("untracked_files_scope", all(
    ln.startswith("?? ") and (
        ln[3:] in {str((BASE / p).relative_to(ROOT)) for p in baseline}
        or ln[3:] in {str((BASE / p).relative_to(ROOT)) for p in new if allowed(p)}
    ) for ln in status.splitlines()), dict(status=status.splitlines()))

errors = []
for i, ev in enumerate(graph["evidence"]):
    path = BASE / ev["file"]
    lines = path.read_text().splitlines()
    if not 1 <= ev["line"] <= ev["end"] <= len(lines):
        errors.append([i, "invalid line span", ev["file"]])
        continue
    full = " ".join(lines[ev["line"]-1:ev["end"]]).strip()
    excerpt = " ".join(x for x in lines[ev["line"]-1:ev["end"]] if not x.lstrip().startswith("#"))
    clean = re.sub(r"\s+", " ", excerpt.replace("**", "").replace("`", "")).strip()
    clean = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", clean)
    if full != ev["full"] or ev["quote"] not in clean or sha(path) != ev["sha256"]:
        errors.append([i, "passage, quote or source hash mismatch", ev["file"]])
    if ev["quote"].replace("|", "\\|") not in report and ev["quote"] not in report:
        errors.append([i, "quotation absent from report", ev["file"]])
check("all_quote_locators_and_source_hashes_match", not errors,
      dict(quotations=len(graph["evidence"]), distinct_sources=len({e["file"] for e in graph["evidence"]}), errors=errors))

statuses = {"LANDED", "CONDITIONAL", "OPEN", "AT-RISK"}
all_rows = graph["nodes"] + graph["inventory"]
ids = [r["id"] for r in all_rows]
check("one_valid_status_and_quoted_evidence_per_row",
      len(ids) == len(set(ids)) and all(r["status"] in statuses and r["evidence"].replace("|", "\\|") in report for r in all_rows),
      dict(rows=len(ids), statuses=dict(Counter(r["status"] for r in all_rows))))
expected_original = {"N0", "N1F", "N1S"} | {f"N{i}" for i in range(2,25)}
check("original_26_nodes_present", expected_original <= set(ids) and len(expected_original) == 26,
      dict(original_nodes=sorted(expected_original)))
expected_inventory = {f"L{i:02}" for i in range(1,45)} | {f"A{i:02}" for i in range(1,9)} | {f"Q{i:02}" for i in range(1,9)} | {f"C{i:02}" for i in range(1,29)}
check("claimed_result_inventory_complete", {r["id"] for r in graph["inventory"]} == expected_inventory,
      dict(legacy=44, later_support=8, queue=8, coordinator_reviewed=27, coordinator_pending=1))
by_id = {n["id"]: n for n in graph["nodes"]}
route_errors = []
route_risks = {}
for route in graph["routes"]:
    leaves = route["leaves"]
    if len(leaves) != len(set(leaves)):
        route_errors.append([route["id"], "duplicate interface"])
    if any(x not in by_id or by_id[x]["status"] not in {"OPEN", "AT-RISK"} for x in leaves):
        route_errors.append([route["id"], "unknown or non-open leaf"])
    expected = graph["common_leaves"] + graph["geometry"][route["geometry"]] + graph["witnesses"][route["witness"]]
    if leaves != expected:
        route_errors.append([route["id"], "route factorization mismatch"])
    route_risks[route["id"]] = [x for x in leaves if by_id[x]["status"] == "AT-RISK"]
check("all_ten_candidate_route_sets_consistent", not route_errors and len(graph["routes"]) == 10 and all(route_risks.values()),
      dict(errors=route_errors, at_risk_by_route=route_risks,
           warning="Contract-relative sets, not logical necessity or independent-wall certification; SS has W OR V suppliers, SW is conditional on strict target."))

rd_hash = sha(BASE / "RD.md")
check("rd_source_still_matches_reviewed_snapshot", rd_hash == "06ad2b5b52bfa66f7784a1fb97936337c59f5164318f89af9a2a065226671e5f",
      dict(sha256=rd_hash, lines=len((BASE / "RD.md").read_text().splitlines())))
review_path = BASE / "checks/audit_review.md"
review = review_path.read_text() if review_path.exists() else ""
check("independent_mapping_review_binds_current_report",
      review.rstrip().endswith("VERDICT: LAND") and sha(BASE / "AUDIT.md") in review,
      dict(review_sha256=sha(review_path) if review_path.exists() else None,
           scope="Same-family mapping readiness only; substantive review read separately by supervising agent."))
artifact_paths = [p for p in new if allowed(p) and p != "checks/audit_validation.json"]
result = dict(
    verified_utc=datetime.now(timezone.utc).isoformat(),
    scope="Document/provenance/route bookkeeping only; no theorem, independent proof or retained status certification.",
    passed=all(c["passed"] for c in checks), checks=checks,
    artifacts={p: sha(BASE / p) for p in artifact_paths},
    remote_freshness="Not verified; fetch denied by shared FETCH_HEAD permissions.",
    scientific_numerics="None; mandatory nice priority unavailable, resource diagnostics failed; no weakened numerical run.",
)
(BASE / "checks/audit_validation.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(dict(passed=result["passed"], checks=len(checks), failures=[c for c in checks if not c["passed"]],
                      source_files=len(baseline), quote_count=len(graph["evidence"]), report_sha256=sha(BASE / "AUDIT.md"))))
raise SystemExit(0 if result["passed"] else 1)
