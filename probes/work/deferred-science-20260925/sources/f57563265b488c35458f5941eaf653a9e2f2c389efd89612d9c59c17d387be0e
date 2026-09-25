"""Seal the completed blind PRE and all evidence without replacing an old seal."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    target = HERE / "PRE_SEAL.json"
    if target.exists():
        raise FileExistsError("A PRE seal already exists; refuse to overwrite it")
    evidence = json.loads((HERE / "EVIDENCE_VERIFICATION.json").read_text())
    assert evidence["PRE_sha256"] == sha(HERE / "PRE.md")
    assert evidence["SOURCE_PINS_sha256"] == sha(HERE / "SOURCE_PINS.json")
    assert evidence["control_source_sha256"] == sha(HERE / "number_offset_control.py")
    assert evidence["control_result_sha256"] == sha(HERE / "CONTROL_ATTEMPT_01_STDOUT.json")
    assert evidence["verifier_sha256"] == sha(HERE / "verify_evidence.py")
    assert (HERE / "EVIDENCE_VERIFICATION_STDERR.txt").stat().st_size == 0
    excluded = {"PRE_SEAL.json", "PRE_SEAL_EXECUTION.json", "PRE_SEAL_STDERR.txt"}
    paths = sorted((path for path in HERE.rglob("*") if path.is_file()
                    and path.name not in excluded and "__pycache__" not in path.parts),
                   key=lambda path: path.relative_to(HERE).as_posix())
    members = [{"path": path.relative_to(HERE).as_posix(), "bytes": path.stat().st_size,
                "sha256": sha(path)} for path in paths]
    payload = {
        "sealed_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Blind independent PRE on arbitrary finite-graph occupied-number offsets; proof, controls, domains and failures retained.",
        "note": "PRE.md",
        "scientific_source_revision": "b47a67e3a08febd2aaf3545eae9a278b4901a72d",
        "source_origins": 11,
        "git_source_origins": 10,
        "scientific_parent_notes": 3,
        "new_author_sources_read": [],
        "author_programs_executed_or_imported": [],
        "member_count": len(members),
        "members": members,
        "next_step": "Stop before author disclosure. Any later authorized comparison must preserve PRE and use a separate POST."
    }
    target.write_text(json.dumps(payload, indent=2) + "\n")
    for path in paths + [target]:
        path.chmod(0o444)
    for member in json.loads(target.read_text())["members"]:
        path = HERE / member["path"]
        assert sha(path) == member["sha256"]
        assert path.stat().st_size == member["bytes"]
    print(json.dumps({
        "status": "sealed and verified",
        "member_count": len(members),
        "PRE_sha256": sha(HERE / "PRE.md"),
        "PRE_SEAL_sha256": sha(target),
        "SOURCE_PINS_sha256": sha(HERE / "SOURCE_PINS.json"),
        "control_source_sha256": sha(HERE / "number_offset_control.py"),
        "control_result_sha256": sha(HERE / "CONTROL_ATTEMPT_01_STDOUT.json")
    }, indent=2))


if __name__ == "__main__":
    main()
