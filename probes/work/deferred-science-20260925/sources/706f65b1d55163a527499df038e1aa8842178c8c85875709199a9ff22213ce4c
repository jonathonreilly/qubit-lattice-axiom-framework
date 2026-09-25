#!/usr/bin/env python3
"""Seal separate POST files without touching any PRE member."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    target = ROOT / "POST_SEAL.json"
    assert not target.exists()
    expected_pre = "7b3a5de5ad3c2d1d47ad259333aa7ab90297d0108ebe36868306a72f8f4b1234"
    assert sha(ROOT / "PRE_SEAL.json") == expected_pre
    pre = json.loads((ROOT / "PRE_SEAL.json").read_text())
    prior_paths = {row["path"] for row in pre["members"]} | {"PRE_SEAL.json"}
    for row in pre["members"]:
        path = ROOT / row["path"]
        assert sha(path) == row["sha256"] and path.stat().st_size == row["bytes"]
        assert path.stat().st_mode & 0o222 == 0

    pins = json.loads((ROOT / "POST_SOURCE_PINS.json").read_text())
    for row in pins["released_sources_and_reused_helper"]:
        assert sha(ROOT / row["snapshot"]) == sha(Path(row["source"])) == row["sha256"]
    execution = json.loads((ROOT / "POST_CHECK_EXECUTION.json").read_text())
    assert execution["returncode"] == 0
    for name, row in execution["files"].items():
        assert sha(ROOT / name) == row["sha256"]
        assert (ROOT / name).stat().st_size == row["bytes"]

    binding = {
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "Final mechanical source/evidence binding, not a scientific verdict",
        "pre_seal_sha256": expected_pre,
        "pre_member_count_reverified_unchanged": len(pre["members"]),
        "released_sources_and_helper_reverified_against_current_originals": len(pins["released_sources_and_reused_helper"]),
        "post_check_execution_returncode": execution["returncode"],
        "post_sha256": sha(ROOT / "POST.md"),
        "post_source_pins_sha256": sha(ROOT / "POST_SOURCE_PINS.json"),
        "post_evidence_check_sha256": sha(ROOT / "POST_EVIDENCE_CHECK.json"),
    }
    (ROOT / "POST_FINAL_BINDING.json").write_text(json.dumps(binding, indent=2) + "\n")
    members = []
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
        relative = str(path.relative_to(ROOT))
        if relative in prior_paths:
            continue
        path.chmod(0o444)
        members.append({"path": relative, "bytes": path.stat().st_size,
                        "sha256": sha(path), "mode": "0444"})
    seal = {
        "schema": "independent-post-evidence-seal-v1",
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "root": str(ROOT), "phase": "Released-source POST after immutable independent PRE",
        "dependency": {"path": "PRE_SEAL.json", "sha256": expected_pre,
                       "unchanged_member_count": len(pre["members"])},
        "member_count": len(members), "members": members,
        "authority": "Scoped conditional source comparison and evidence correspondence; not an audit verdict",
        "preservation": "Keep all PRE and POST members unchanged; later work uses separate artifacts",
    }
    target.write_text(json.dumps(seal, indent=2) + "\n")
    target.chmod(0o444)
    for row in members:
        assert sha(ROOT / row["path"]) == row["sha256"]
    for row in pre["members"]:
        assert sha(ROOT / row["path"]) == row["sha256"]
    print(json.dumps({"post": str(ROOT / "POST.md"), "post_sha256": sha(ROOT / "POST.md"),
                      "seal": str(target), "seal_sha256": sha(target),
                      "member_count": len(members), "unchanged_PRE_members": len(pre["members"])}, indent=2))


if __name__ == "__main__":
    main()
