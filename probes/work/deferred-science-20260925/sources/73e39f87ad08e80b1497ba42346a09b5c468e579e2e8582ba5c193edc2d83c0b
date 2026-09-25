#!/usr/bin/env python3
"""Create the independent PRE38 manifest once; never run an author sealer.

Reads only this packet, refuses an existing seal, checks the already-recorded
verification identities, then makes the twenty members and manifest read-only.
Execution receipts are external to the content manifest to avoid self-hashing.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SEAL = ROOT / "PRE_SEAL.json"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    assert not SEAL.exists(), "PRE seal already exists; preserve it"
    files = sorted(p for p in ROOT.rglob("*") if p.is_file())
    assert len(files) == 20, [p.relative_to(ROOT).as_posix() for p in files]
    assert all(not p.is_symlink() for p in files)
    verification = json.loads((ROOT / "EVIDENCE_VERIFICATION.json").read_bytes())
    execution = json.loads((ROOT / "EVIDENCE_VERIFICATION_EXECUTION.json").read_bytes())
    assert verification["all_requested_identity_checks"] is True
    assert verification["source_count"] == 12
    assert execution["returncode"] == 0
    assert (ROOT / "EVIDENCE_VERIFICATION.stderr").read_bytes() == b""
    for name in ("stdout", "stderr"):
        entry = execution[name]
        data = (ROOT / entry["path"]).read_bytes()
        assert digest(data) == entry["sha256"] and len(data) == entry["bytes"]
    for entry in verification["local_evidence"]:
        data = (ROOT / entry["path"]).read_bytes()
        assert digest(data) == entry["sha256"] and len(data) == entry["bytes"]
    assert digest((ROOT / "verify_pre_sources.py").read_bytes()) == execution["script_sha256"]
    members = []
    for file in files:
        data = file.read_bytes()
        members.append({"path": file.relative_to(ROOT).as_posix(),
                        "sha256": digest(data), "bytes": len(data)})
    seal = {
        "at_utc": datetime.now(timezone.utc).isoformat(),
        "signed_by": "/root/rotor_upper_tail_check",
        "signature_kind": "Author identification with SHA256 content manifest; no external digital-signature assertion.",
        "phase": "blind independent PRE38, before author38 release",
        "scope": "Conditional consequences of original number balance and explicitly provisional author37 full-energy/activity and infimum imports. No independent proof or numerical confirmation of those imports.",
        "source_binding_count": 12,
        "member_count": len(members),
        "author38_read": False,
        "other_active_packets_read": False,
        "scientific_or_original_author_programs_executed": [],
        "evidence_status": "Source binding verifier exited zero with empty stderr. Analytic scope discriminators are written in PRE; no native numerical control is claimed.",
        "immutability": "All listed files and this manifest are chmod 0444; future phases must use new filenames and preserve these hashes.",
        "members": members,
    }
    SEAL.write_text(json.dumps(seal, indent=2) + "\n")
    for file in files + [SEAL]:
        file.chmod(0o444)
    for entry in members:
        file = ROOT / entry["path"]
        assert digest(file.read_bytes()) == entry["sha256"]
        assert file.stat().st_mode & 0o222 == 0
    assert SEAL.stat().st_mode & 0o222 == 0
    print(json.dumps({
        "sealed_utc": seal["at_utc"],
        "member_count": len(members),
        "source_binding_count": 12,
        "PRE_sha256": digest((ROOT / "PRE.md").read_bytes()),
        "SOURCE_PINS_sha256": digest((ROOT / "SOURCE_PINS.json").read_bytes()),
        "PRE_SEAL_sha256": digest(SEAL.read_bytes()),
        "all_member_hashes_rechecked": True,
        "all_members_and_seal_read_only": True,
        "stop_pending_author38_release": True,
    }, indent=2) + "\n", end="")


if __name__ == "__main__":
    main()
