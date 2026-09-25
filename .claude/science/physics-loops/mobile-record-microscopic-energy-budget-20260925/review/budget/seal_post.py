#!/usr/bin/env python3
"""Seal only the new POST38 generation, preserving all PRE members.

This is this checker's own new metadata writer. It executes no original author
writer, reads no external source, and refuses to overwrite an existing seal.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SEAL = ROOT / "POST_SEAL.json"


def identity(data):
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def checked(path, entry):
    assert identity(path.read_bytes()) == {"sha256": entry["sha256"], "bytes": entry["bytes"]}


def main():
    assert not SEAL.exists(), "Preserve the existing POST seal"
    names = ["POST.md", "POST_SOURCE_PINS.json", "POST_REVIEW_RECORD.json",
             "verify_post_bindings.py", "POST_EVIDENCE_VERIFICATION.json",
             "POST_EVIDENCE_VERIFICATION.stderr", "POST_EVIDENCE_VERIFICATION_EXECUTION.json",
             "seal_post.py"]
    files = [ROOT / name for name in names]
    sources = sorted(p for p in (ROOT / "post_sources").rglob("*") if p.is_file())
    assert len(sources) == 5
    files = sorted(files + sources)
    assert len(files) == 13 and all(p.is_file() and not p.is_symlink() for p in files)
    evidence = json.loads((ROOT / "POST_EVIDENCE_VERIFICATION.json").read_bytes())
    execution = json.loads((ROOT / "POST_EVIDENCE_VERIFICATION_EXECUTION.json").read_bytes())
    assert evidence["all_requested_checks"] is True
    assert execution["returncode"] == 0
    assert (ROOT / "POST_EVIDENCE_VERIFICATION.stderr").read_bytes() == b""
    for key in ("stdout", "stderr"):
        entry = execution[key]
        checked(ROOT / entry["path"], entry)
    for entry in evidence["local_POST_evidence"]:
        checked(ROOT / entry["path"], entry)
    assert identity((ROOT / "verify_post_bindings.py").read_bytes())["sha256"] == execution["script_sha256"]
    pre_seal_data = (ROOT / "PRE_SEAL.json").read_bytes()
    assert identity(pre_seal_data)["sha256"] == "db299c055ce8a454d3bd8a99ef33e13ba9688582214cf0250a16af278fab2025"
    pre_seal = json.loads(pre_seal_data)
    for member in pre_seal["members"]:
        path = ROOT / member["path"]
        checked(path, member)
        assert path.stat().st_mode & 0o222 == 0
    assert (ROOT / "PRE_SEAL.json").stat().st_mode & 0o222 == 0
    members = [{"path": p.relative_to(ROOT).as_posix(), **identity(p.read_bytes())} for p in files]
    payload = {
        "at_utc": datetime.now(timezone.utc).isoformat(),
        "signed_by": "/root/rotor_upper_tail_check",
        "signature_kind": "Checker identification and SHA256 content manifest; no external cryptographic-signature assertion.",
        "phase": "Released-source POST38",
        "scope": "Conditional comparison of the complete four-member author38 argument and metadata with preserved PRE38. No independent confirmation of the author37 import or retained audit disposition.",
        "result": "No required mathematical correction; fixed-parameter, hitting-time, unbounded-reservoir and additive-energy interpretations are explicit in POST.",
        "member_count": len(members),
        "released_source_binding_count": 5,
        "reused_PRE_source_binding_count": 12,
        "preserved_PRE": {
            "report": identity((ROOT / "PRE.md").read_bytes()),
            "seal": identity(pre_seal_data),
            "member_count": len(pre_seal["members"]),
            "all_member_hashes_reverified_and_read_only": True,
        },
        "original_author_or_scientific_programs_executed": [],
        "other_active_packets_or_publications_read": False,
        "immutability": "All listed POST members and this seal are chmod 0444. PRE remains unchanged; future work requires a new generation.",
        "members": members,
    }
    SEAL.write_text(json.dumps(payload, indent=2) + "\n")
    for path in files + [SEAL]:
        path.chmod(0o444)
    for entry in members:
        path = ROOT / entry["path"]
        checked(path, entry)
        assert path.stat().st_mode & 0o222 == 0
    print(json.dumps({
        "sealed_utc": payload["at_utc"], "member_count": len(members),
        "POST_sha256": identity((ROOT / "POST.md").read_bytes())["sha256"],
        "POST_SEAL_sha256": identity(SEAL.read_bytes())["sha256"],
        "POST_SOURCE_PINS_sha256": identity((ROOT / "POST_SOURCE_PINS.json").read_bytes())["sha256"],
        "all_POST_members_reverified_and_read_only": True,
        "all_twenty_PRE_members_preserved": True,
        "stopped_after_POST": True,
    }, indent=2) + "\n", end="")


if __name__ == "__main__":
    main()
