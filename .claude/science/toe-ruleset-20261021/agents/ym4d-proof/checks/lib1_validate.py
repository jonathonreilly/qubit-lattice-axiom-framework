#!/usr/bin/env python3
"""Documentation/provenance validation; not a mathematical or audit verdict."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent
CHECKS = ROOT / "checks"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def norm(s):
    return " ".join(s.split())


def main():
    note_bytes = (ROOT/"LIB1.md").read_bytes()
    note = note_bytes.decode()
    log = (ROOT/"LIB1_LOG.md").read_text()
    receipt = json.loads(re.search(r"```json\n(.*?)\n```", log, re.S).group(1))
    prefix = note_bytes[:receipt["bytes"]]
    assert len(prefix) == receipt["bytes"] == receipt["stat"]["st_size"]
    assert sha(prefix) == receipt["sha256"]
    assert prefix.endswith(b"<!-- END PRE-STATED LIB1: immutable original prefix -->\n")

    sources = json.loads((CHECKS/"lib1_source_manifest.json").read_text())["sources"]
    for row in sources:
        b = Path(row["path"]).read_bytes()
        assert len(b) == row["bytes"] and sha(b) == row["sha256"], row["path"]

    quotes = [
        ("SOFTHARD.md", 349, 349, "Enlarging the inactive region regroups boundary activities while preserving their sum and controlling a decay loss."),
        ("HANDOFF.md", 420, 421, "Include holes, reference comparison and failed-return bookkeeping before claiming the history-uniform large-field step."),
        ("HANDOFF.md", 426, 428, "Construct N1's complete normalised, strictly source-local density representation, uniformly over all coarse fields, and N2."),
        ("CODEX_REVIEW_ASSEMBLY.md", 229, 229, "Close the coupled flow/large-field construction."),
        ("CODEX_REVIEW_ASSEMBLY.md", 231, 231, "Match the coefficient norm and the actual source radii."),
        ("STEP55.md", 583, 583, "boundary polymers READ cone variables, so COL's exact integration must be redone with those polymers expanded"),
        ("SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md", 576, 579, "Every original coefficient and every actual sea/coarse field read occurs in X, before and after summing histories at FIXED F."),
        ("SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md", 455, 459, "only the bare Wilson coefficient changes, and the prescribed RG kernel K remains fixed."),
        ("SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md", 592, 593, "sup_x sum_(X contains x) exp(mu|X|) sup_(real U,V; D_(rho,lambda)(u)) |V_X^F| <= d_q."),
        ("SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md", 437, 441, "D_(rho,lambda)(u)={epsilon: |epsilon_p|<=rho+lambda/u},"),
    ]
    quote_rows = []
    for file, start, end, quote in quotes:
        lines = (ROOT/file).read_text().splitlines()
        excerpt = "\n".join(lines[start-1:end])
        assert norm(quote) in norm(excerpt), (file, start, end, quote, excerpt)
        assert norm(quote) in norm(note), ("note", quote)
        quote_rows.append({"file": file, "lines": [start, end], "quote": quote,
                           "matched_with_whitespace_normalization_only": True})

    result = json.loads((CHECKS/"lib1_check_result.json").read_text())
    assert result == json.loads((CHECKS/"lib1_check_stdout.txt").read_text())
    assert (CHECKS/"lib1_check_stderr.txt").read_bytes() == b""
    assert result["result"] == "completed; all enumerated predicates satisfied"
    assert result["script_sha256"] == sha((CHECKS/"lib1_check.py").read_bytes())
    assert result["criteria_sha256"] == sha((CHECKS/"lib1_criteria.md").read_bytes())
    for sample in result["resources"]:
        assert sample["max_rss_bytes"] < 2_000_000_000
        assert sample["memory_free_percent"] >= 50
        assert max(sample["load_averages"]) < 20
        assert sample["nice"] >= 10
        assert all(x == "1" for x in sample["thread_environment"].values())
    assert result["elapsed_seconds"] < 60
    assert len(result["mutations"]) == 4

    repo = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=ROOT,
                          text=True, capture_output=True, check=True).stdout.strip()
    diff = subprocess.run(["git", "diff", "--name-only", "HEAD", "--"], cwd=repo,
                          text=True, capture_output=True, check=True).stdout.splitlines()
    assert not diff, ("tracked paths changed", diff)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, text=True,
                          capture_output=True, check=True).stdout.strip()
    assert head == "4f04b662f4d72d7ef269f6d9693ae9ff6424acf9"

    artifacts = []
    for p in [ROOT/"LIB1.md"] + sorted(CHECKS.glob("lib1_*")):
        if p.name == "lib1_validation.json":
            continue
        b = p.read_bytes()
        artifacts.append({"path": str(p.relative_to(ROOT)), "bytes": len(b), "sha256": sha(b)})
    out = {"kind": "documentation/provenance checks only", "result": "completed",
           "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "prefix_bytes": len(prefix), "prefix_sha256": sha(prefix),
           "unchanged_source_count": len(sources), "quotes": quote_rows,
           "candidate_head_unchanged": head, "tracked_diff_paths": diff,
           "artifacts": artifacts}
    (CHECKS/"lib1_validation.json").write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps({key: out[key] for key in ("result", "prefix_bytes", "unchanged_source_count", "candidate_head_unchanged")}, indent=2))
    print("Literal quote matches:", len(quote_rows))


if __name__ == "__main__":
    main()
