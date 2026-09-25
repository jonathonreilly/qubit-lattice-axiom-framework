#!/usr/bin/env python3
"""One-time own seal for the bounded final correspondence generation.

No original writer is executed. Only this new external directory is mutated.
All permitted origins are read once more for identity, never modified.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SEAL = ROOT / "PUBLICATION_COMPARISON_SEAL.json"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    assert not SEAL.exists(), "Preserve an existing seal"
    files = sorted(p for p in ROOT.rglob("*") if p.is_file())
    assert len(files) == 176
    assert all(not p.is_symlink() for p in files)
    pins = json.loads((ROOT / "SOURCE_PINS.json").read_bytes())
    assert len(pins["origins"]) == 168
    for row in pins["origins"]:
        data = (ROOT / row["frozen"]).read_bytes()
        assert sha(data) == row["sha256"] and len(data) == row["bytes"]
        assert Path(row["origin"]).read_bytes() == data
    execution = json.loads((ROOT / "VERIFICATION_EXECUTION.json").read_bytes())
    verification = json.loads((ROOT / "VERIFICATION_REPORT.json").read_bytes())
    assert execution["exit_code"] == 0
    assert execution["before_after_content_size_mtime_ctime_equal"] is True
    assert verification["all_requested_checks"] is True
    for key in ("stdout", "stderr"):
        record = execution[key]
        data = (ROOT / record["path"]).read_bytes()
        assert sha(data) == record["sha256"] and len(data) == record["bytes"]
    assert (ROOT / "VERIFICATION.stderr").read_bytes() == b""
    assert sha((ROOT / "verify_publication_readonly.py").read_bytes()) == execution["source_sha256"]
    members = []
    for file in files:
        data = file.read_bytes()
        members.append({"path": file.relative_to(ROOT).as_posix(), "sha256": sha(data), "bytes": len(data)})
    payload = {
        "at_utc": datetime.now(timezone.utc).isoformat(),
        "signed_by": "/root/rotor_upper_tail_check",
        "signature_kind": "Checker identification and SHA256 content manifest, not an external digital-signature claim.",
        "phase": "Final released-source publication correspondence for combined37/38",
        "scope": "Complete proof/source/output/cache correspondence. No new blind reconstruction, scientific execution, retained audit decision or publication mutation.",
        "required_repairs": [],
        "canonical_manifest_sha256": "d8908ec842e1e8e4bf565dd4a9032a00dd19c4c691f4062c2d6be58692c855b9",
        "canonical_note_sha256": "b6529a9f54915bd6d8157401e74cc1dbdb8d3577917dc8eadf4ca0133f04680d",
        "source_snapshot_count": 168,
        "member_count": len(members),
        "prior_author_and_independent_seals": pins["seals"],
        "prior_scope_preserved": "PRE38/POST38 imported Part I; complete author37 and independent37 evidence was exposed only for this final correspondence. Independent-only additions retain attribution.",
        "scientific_programs_or_original_writers_executed": [],
        "immutability": "This manifest and all listed members are chmod 0444. Prior packets remain unchanged. Future revisions require new filenames or a new generation.",
        "members": members,
    }
    SEAL.write_text(json.dumps(payload, indent=2) + "\n")
    for path in files + [SEAL]:
        path.chmod(0o444)
    for member in members:
        path = ROOT / member["path"]
        assert sha(path.read_bytes()) == member["sha256"]
        assert path.stat().st_mode & 0o222 == 0
    print(json.dumps({
        "sealed_utc": payload["at_utc"],
        "member_count": len(members), "source_snapshot_count": 168,
        "PUBLICATION_COMPARISON_sha256": sha((ROOT / "PUBLICATION_COMPARISON.md").read_bytes()),
        "PUBLICATION_COMPARISON_SEAL_sha256": sha(SEAL.read_bytes()),
        "SOURCE_PINS_sha256": sha((ROOT / "SOURCE_PINS.json").read_bytes()),
        "all_members_rechecked_and_read_only": True,
        "stopped_after_seal": True,
    }, indent=2) + "\n", end="")


if __name__ == "__main__":
    main()
