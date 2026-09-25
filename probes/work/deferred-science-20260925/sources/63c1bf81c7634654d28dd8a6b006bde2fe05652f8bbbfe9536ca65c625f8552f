#!/usr/bin/env python3
"""Exact local/Git identity verification, no scientific runner imports."""
import hashlib
import json
from pathlib import Path
import subprocess

here = Path(__file__).resolve().parent
manifest = json.loads((here / "SOURCE_PINS.json").read_text())
rows = []
for source in manifest["sources"]:
    frozen = (here / source["frozen_path"]).read_bytes()
    if "repository" in source:
        proc = subprocess.run(["git", "show", source["commit"] + ":" + source["path"]],
                              cwd=source["repository"], capture_output=True, check=True)
        live = proc.stdout
        locator = source["commit"] + ":" + source["path"]
    else:
        live = Path(source["path"]).read_bytes()
        locator = source["path"]
    actual = hashlib.sha256(frozen).hexdigest()
    assert frozen == live, source["id"]
    assert actual == source["sha256"], source["id"]
    assert len(frozen) == source["bytes"], source["id"]
    if source.get("expected_sha256"):
        assert actual == source["expected_sha256"], source["id"]
    row = {"id": source["id"], "locator": locator, "bytes": len(frozen),
           "sha256": actual, "exact_frozen_source_match": True}
    rows.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)
out = {"all_exact": True, "source_count": len(rows), "sources": rows}
(here / "SOURCE_VERIFICATION.json").write_text(json.dumps(out, indent=2) + "\n")
