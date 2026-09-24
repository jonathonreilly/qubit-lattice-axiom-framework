#!/usr/bin/env python3
"""One-time read-only PRE freeze; refuse to replace an existing seal."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

here = Path(__file__).resolve().parent
seal_path = here / "PRE_SEAL.json"
if seal_path.exists():
    raise RuntimeError("PRE already sealed; preserve the original packet")
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = json.loads((here / "SOURCE_PINS.json").read_text())
for source in manifest["sources"]:
    assert sha(here / source["frozen_path"]) == source["sha256"]
execution = json.loads((here / "EXECUTION.json").read_text())
assert sha(here / "run_controls.py") == execution["runner_sha256"]
assert sha(here / "SOURCE_PINS.json") == execution["source_manifest_sha256"]
for run in execution["runs"]:
    assert run["exit_code"] == 0
    assert sha(here / run["script"]) == run["script_sha256"]
    for key in ("stdout", "stderr"):
        assert sha(here / run[key]) == run[key + "_sha256"]
evidence = json.loads((here / "EVIDENCE_VERIFICATION.json").read_text())
assert sha(here / "verify_evidence.py") == evidence["script_sha256"]
for name, digest in evidence["evidence_sha256"].items():
    assert sha(here / name) == digest
assert json.loads((here / "evidence_verification.stdout.txt").read_text()) == evidence
assert (here / "evidence_verification.stderr.txt").read_bytes() == b""
members = []
for path in sorted(here.rglob("*")):
    if path.is_file():
        if path.is_symlink():
            raise RuntimeError("Do not seal a symlink: " + str(path))
        members.append({"path": str(path.relative_to(here)),
                        "bytes": path.stat().st_size, "sha256": sha(path)})
seal = {"phase": "blind independent PRE",
        "sealed_at_utc": datetime.now(timezone.utc).isoformat(),
        "main_source_commit": "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8",
        "scope": "Original formation-record readout of normalized prepared vacuum and one-particle packets.",
        "provenance": "No released author candidate, author helper, active checker packet or parent runner read/run; no delegation.",
        "status": "Conditional independent reconstruction; no audit or retained-grade verdict.",
        "preservation": "One-time content-hash ledger; member files and this seal are set read-only. Preserve originals for any later POST.",
        "member_count": len(members), "members": members}
seal_path.write_text(json.dumps(seal, indent=2) + "\n")
for member in members:
    path = here / member["path"]
    assert sha(path) == member["sha256"]
    path.chmod(0o444)
seal_path.chmod(0o444)
print(json.dumps({"seal": str(seal_path), "seal_sha256": sha(seal_path),
                  "PRE_sha256": sha(here / "PRE.md"),
                  "member_count": len(members), "all_members_reverified": True}, sort_keys=True))
