#!/usr/bin/env python3
"""One sequential documentation check of the B1–B4 author revision.

No numerical physics, subprocess pools, source mutations or frozen-output writes.
The criteria and original-input snapshot predate this script.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import unicodedata

BASE = Path(__file__).resolve().parent.parent
CHECKS = BASE / "checks"
OUTPUT = CHECKS / "sh_revision_v2_results.json"
LIMIT = 2_000_000_000
THREAD_KEYS = (
    "BLAS", "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS", "NUMEXPR_NUM_THREADS",
)
if OUTPUT.exists():
    raise SystemExit("Refusing a second run or overwrite of the v2 result.")
if any(os.environ.get(k) != "1" for k in THREAD_KEYS):
    raise SystemExit("All declared BLAS/thread controls must equal 1.")
if os.environ.get("PYTHONDONTWRITEBYTECODE") != "1" or not sys.dont_write_bytecode:
    raise SystemExit("Bytecode writing must be disabled.")


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def receipt(path):
    s = path.stat()
    return {
        "path": str(path.relative_to(BASE)), "bytes": s.st_size,
        "st_mode": oct(s.st_mode), "st_ino": s.st_ino,
        "st_mtime_ns": s.st_mtime_ns, "st_ctime_ns": s.st_ctime_ns,
        "sha256": digest(path),
    }


def peak_rss():
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def memory_guard():
    if peak_rss() >= LIMIT:
        raise MemoryError("Peak RSS exceeded the strict 2 GB documentation-check limit.")


def normalize(value):
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r"(?<=\w)[-‐‑]\s*\n\s*(?=\w)", "", value)
    value = re.sub(r"(?m)^\s*(?:>\s*)+", "", value)
    value = value.replace("*", "").replace("`", "")
    return " ".join(value.split())


def unquote(line):
    while line.startswith(">"):
        line = line[1:]
        if line.startswith(" "):
            line = line[1:]
    return line


def allowed_new(path):
    return bool(re.fullmatch(r"checks/sh_.*_v2[^/]*", path))


result = {
    "utc_start": datetime.now(timezone.utc).isoformat(),
    "kind": "author documentation/provenance checks; not independent science review",
    "thread_environment": {k: os.environ[k] for k in THREAD_KEYS},
    "platform": sys.platform, "python": sys.version,
    "pools": False, "rss_limit_bytes": LIMIT,
    "errors": [], "open_residue": [], "historical_hash_drift": [],
}
errors = result["errors"]
residue = result["open_residue"]
baseline = json.loads((CHECKS / "sh_revision_v2_baseline.json").read_text())
memo_path = BASE / "SOFTHARD.md"
memo = memo_path.read_text()
memo_raw = memo_path.read_bytes()
result["memo"] = receipt(memo_path)
result["criteria"] = receipt(CHECKS / "sh_revision_v2_criteria.md")
result["script"] = receipt(Path(__file__).resolve())
result["baseline"] = receipt(CHECKS / "sh_revision_v2_baseline.json")
if result["criteria"]["st_mtime_ns"] >= result["script"]["st_mtime_ns"]:
    errors.append("Criteria do not predate the script.")

result["prefix_unchanged"] = (
    memo_raw[:2035] == baseline["original_memo"].encode()[:2035]
    and hashlib.sha256(memo_raw[:2035]).hexdigest()
    == "9492d1f7d9d159d39325e9d67f944e0dc34a3a42a9314c8289bb8fc4c1bd0b0d"
)
if not result["prefix_unchanged"]:
    errors.append("The pre-stated prefix changed.")
old_lines = Counter(x for x in baseline["original_memo"].splitlines() if x)
new_lines = Counter(unquote(x) for x in memo.splitlines() if unquote(x))
missing_lines = list((old_lines - new_lines).elements())
result["missing_original_lines"] = missing_lines
if missing_lines:
    errors.append("Original memo text was not fully preserved.")
result["original_log_prefix_preserved"] = (BASE / "SOFTHARD_LOG.md").read_text().startswith(
    baseline["original_log"]
)
if not result["original_log_prefix_preserved"]:
    errors.append("Original log content changed.")

# Snapshot coverage, not a moving git branch, is the dependency stability check.
current = {}
for p in sorted(BASE.rglob("*")):
    if p.is_file():
        current[str(p.relative_to(BASE))] = receipt(p)
        memory_guard()
result["current_source_receipts"] = current
scope_changes = []
for name, old in baseline["files"].items():
    now = current.get(name)
    if now is None or now["sha256"] != old["sha256"]:
        scope_changes.append(name)
        if name not in {"SOFTHARD.md", "SOFTHARD_LOG.md"}:
            errors.append("Dependency changed after baseline: " + name)
added = sorted(set(current) - set(baseline["files"]))
for name in added:
    if not allowed_new(name):
        errors.append("Unexpected added path: " + name)
result["scope"] = {"changed_existing": scope_changes, "new_paths_before_output": added}

# Frozen manifests stay untouched. Resolve downloaded PDFs by exact identity.
by_hash = {}
for name, r in current.items():
    by_hash.setdefault(r["sha256"], []).append(name)


def resolve_input(path, expected_hash=None):
    candidate = Path(path) if Path(path).is_absolute() else BASE / path
    if candidate.is_file():
        return candidate
    if expected_hash:
        matches = by_hash.get(expected_hash, [])
        if matches:
            return BASE / matches[0]
    return None


manifest = json.loads((CHECKS / "sh_source_manifest.json").read_text())
literature = json.loads((CHECKS / "sh_literature_manifest.json").read_text())
inventory = json.loads((CHECKS / "sh_kernel_inventory.json").read_text())
frozen_validation = json.loads((CHECKS / "sh_validation.json").read_text())
expected_hash = {}
records = []
for group, entries in [
    ("required", manifest["required_sources"]),
    ("external_pdf", manifest["arxiv_read_only"]),
    ("downloaded_pdf", literature),
    ("inventory", inventory),
    ("artifact", frozen_validation["artifacts"]),
]:
    for item in entries:
        name = item.get("path", item.get("file"))
        expected_hash[name] = item["sha256"]
        source = resolve_input(name, item["sha256"])
        row = {"group": group, "historical_path": name, "expected_sha256": item["sha256"]}
        if source is None:
            row["status"] = "UNAVAILABLE"
            residue.append({"kind": "hash_input_unavailable", "path": name, "group": group})
        else:
            now_hash = digest(source)
            row.update({"resolved_path": str(source), "actual_sha256": now_hash})
            row["status"] = "MATCH" if now_hash == item["sha256"] else "PREEXISTING_DRIFT"
            if row["status"] == "PREEXISTING_DRIFT":
                rel = str(source.relative_to(BASE))
                if baseline["files"].get(rel, {}).get("sha256") != now_hash:
                    errors.append("New rather than pre-existing hash drift: " + name)
                result["historical_hash_drift"].append(row)
        records.append(row)
result["frozen_manifest_recheck"] = records
memory_guard()

from pypdf import PdfReader

pdf_cache = {}


def pdf_page(path, page):
    key = str(path)
    if key not in pdf_cache:
        pdf_cache[key] = PdfReader(path)
    return pdf_cache[key].pages[page - 1].extract_text()


quote_rows = []
for item in json.loads((CHECKS / "sh_quote_check.json").read_text())["checks"]:
    name = item["source"]
    source = resolve_input(name, expected_hash.get(name))
    row = {"historical": item, "present_in_revised_memo": normalize(item["quote"]) in normalize(memo)}
    if not row["present_in_revised_memo"]:
        errors.append("Quotation missing in revised memo: " + name + " / " + item["quote"])
    if source is None:
        row["status"] = "UNAVAILABLE"
        residue.append({"kind": "quote_source_unavailable", "path": name, "quote": item["quote"]})
    else:
        row["resolved_path"] = str(source)
        q = normalize(item["quote"])
        if "page" in item:
            found = q in normalize(pdf_page(source, item["page"]))
            row["current_page"] = item["page"]
        else:
            lines = source.read_text().splitlines()
            lo, hi = item["lines"]
            found = q in normalize("\n".join(lines[lo - 1:hi]))
            row["current_lines"] = [lo, hi] if found else None
            if not found:
                width = hi - lo + 1
                for count in range(1, max(4, width + 2) + 1):
                    matches = [
                        [start + 1, start + count]
                        for start in range(len(lines) - count + 1)
                        if q in normalize("\n".join(lines[start:start + count]))
                    ]
                    if matches:
                        row["current_lines"] = matches[0]
                        row["all_minimal_matches"] = matches
                        row["locator_shifted"] = True
                        found = True
                        break
        row["status"] = "MATCH" if found else "FAIL"
        if not found:
            errors.append("Quotation mismatch: " + name + " / " + item["quote"])
    quote_rows.append(row)
    memory_guard()
result["quotes"] = quote_rows
result["quote_counts"] = dict(Counter(x["status"] for x in quote_rows))

dimock = resolve_input("checks/sh_dimock_II.pdf", expected_hash["checks/sh_dimock_II.pdf"])
locator = {"section": "3.3", "representation_pages": [28, 31], "theorem_start": 29, "remark_3": 31}
if dimock is None:
    locator["status"] = "UNAVAILABLE"
    residue.append({"kind": "B4_locator_input_unavailable"})
else:
    p28 = normalize(pdf_page(dimock, 28))
    p29 = normalize(pdf_page(dimock, 29))
    p31 = normalize(pdf_page(dimock, 31))
    locator["predicates"] = {
        "section_heading_on_28": "3.3 the main theorem" in p28,
        "equation_201_on_28": "(201)" in p28,
        "equation_202_on_28": "(202)" in p28,
        "theorem_3_1_on_29": "Theorem 3.1." in p29,
        "remark_3_on_31": "3. With more work" in p31,
        "quoted_remark_on_31": "This difficult step is not necessary for this model." in p31,
    }
    locator["status"] = "MATCH" if all(locator["predicates"].values()) else "FAIL"
    if locator["status"] == "FAIL":
        errors.append("Corrected Dimock II locator did not match the PDF.")
result["dimock_II_locator_v2"] = locator

md_paths = sorted(set(re.findall(r"(?<![\w/])([A-Za-z0-9_./-]+\.md)\b", memo)))
missing_paths = [name for name in md_paths if not (BASE / name).is_file()]
result["local_markdown_paths"] = {"checked": md_paths, "missing": missing_paths}
if missing_paths:
    errors.append("Missing local Markdown references: " + repr(missing_paths))

registry = (BASE / "PROOF.md").read_text().splitlines()
science_lines = {
    i for i in range(308, 355)
    if registry[i - 1].startswith("> - **") and "batch —" not in registry[i - 1]
}
crosswalk = memo.split("#### I6. Explicit registry assignment", 1)[1].split("## 6.", 1)[0]
assigned = set()
for lo, hi in re.findall(r"P(\d+)(?:–P(\d+))?", crosswalk):
    assigned.update(range(int(lo), int(hi or lo) + 1))
result["B1_structural_crosswalk"] = {
    "registry_science_lines": sorted(science_lines), "assigned_lines": sorted(assigned),
    "missing_lines": sorted(science_lines - assigned),
    "note": "Finite index coverage only; no semantic or proof certification.",
}
if science_lines - assigned:
    errors.append("Missing review-scoped registry assignments.")
result["fix_markers"] = {b: memo.count("[R-fix 2026-10-29 " + b + "]") for b in ["B1", "B2", "B3", "B4"]}
if any(n == 0 for n in result["fix_markers"].values()):
    errors.append("Missing binding-fix marker.")

git = subprocess.run(["git", "status", "--porcelain", "-z"], capture_output=True, check=True)
root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
task_prefix = str(BASE.relative_to(root)) + "/"
status = []
for item in git.stdout.decode().split("\0"):
    if not item:
        continue
    code, name = item[:2], item[3:]
    status.append({"status": code, "path": name})
    rel = name[len(task_prefix):] if name.startswith(task_prefix) else None
    if code != "??" and rel not in {"SOFTHARD.md", "SOFTHARD_LOG.md"}:
        errors.append("Unexpected tracked change: " + name)
    if code == "??" and rel is None:
        errors.append("Unexpected untracked path outside task: " + name)
result["git_status"] = status
diffcheck = subprocess.run(["git", "diff", "--check"], capture_output=True, text=True)
result["diff_check"] = {"exit_code": diffcheck.returncode, "output": diffcheck.stdout + diffcheck.stderr}
if diffcheck.returncode:
    errors.append("git diff --check failed.")
memory_guard()
result["peak_rss_bytes"] = peak_rss()
result["rss_under_limit"] = result["peak_rss_bytes"] < LIMIT
result["utc_end"] = datetime.now(timezone.utc).isoformat()
result["status"] = "FAIL" if errors else "PARTIAL_UNAVAILABLE_INPUTS" if residue else "PASS_DOCUMENTATION_ONLY"
with OUTPUT.open("x") as stream:
    json.dump(result, stream, ensure_ascii=False, indent=2)
    stream.write("\n")

log = BASE / "SOFTHARD_LOG.md"
entry = "\n## [R-fix 2026-10-29 B4] Single v2 checker execution\n\n"
entry += "The new checker ran once, sequentially, with all recorded thread controls equal to 1 and no pools. "
entry += "Result: " + result["status"] + ". This is an author documentation check, not a science verdict.\n\n"
entry += "```json\n" + json.dumps({
    "results_file_post_write": receipt(OUTPUT), "memo_checked": result["memo"],
    "log_pre_append": receipt(log), "peak_rss_bytes": result["peak_rss_bytes"],
    "quote_counts": result["quote_counts"], "errors": errors,
    "open_residue": residue,
}, ensure_ascii=False, indent=2) + "\n```\n"
with log.open("a") as stream:
    stream.write(entry)
print(json.dumps({
    "status": result["status"], "quote_counts": result["quote_counts"],
    "locator": locator, "errors": errors, "open_residue_count": len(residue),
    "historical_hash_drift_count": len(result["historical_hash_drift"]),
    "scope": result["scope"], "peak_rss_bytes": result["peak_rss_bytes"],
    "result_file": str(OUTPUT), "log_after_append": receipt(log),
}, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 2 if residue else 0)
