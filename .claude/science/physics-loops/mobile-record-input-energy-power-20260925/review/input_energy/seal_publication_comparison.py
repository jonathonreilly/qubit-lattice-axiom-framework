"""Freeze the bounded Part A publication correspondence, preserving PRE/POST."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    seal_path = HERE / "PUBLICATION_COMPARISON_SEAL.json"
    if seal_path.exists():
        raise FileExistsError("Publication comparison already sealed; no overwrite")
    verified = json.loads((HERE / "PUBLICATION_EVIDENCE_VERIFICATION.json").read_text())
    checks = {
        "report_sha256": "PUBLICATION_COMPARISON.md",
        "source_pins_sha256": "PUBLICATION_SOURCE_PINS.json",
        "binding_results_sha256": "PUBLICATION_BINDING_RESULTS.json",
        "metadata_checks_sha256": "PUBLICATION_METADATA_CHECKS.json",
        "scope_incident_sha256": "PUBLICATION_SCOPE_INCIDENT.json",
        "verifier_sha256": "publication_verify_evidence.py",
    }
    for key, name in checks.items():
        assert verified[key] == digest(HERE / name)
    assert verified["preserved_seal_member_counts"] == [45, 42, 22]
    references = {"PRE.md", "PRE_SEAL.json", "POST.md", "POST_SEAL.json"}
    excluded = {seal_path.name, "PUBLICATION_SEAL_EXECUTION.json", "PUBLICATION_SEAL_STDERR.txt"}
    paths = [path for path in HERE.iterdir() if path.is_file() and path.name not in excluded
             and (path.name.startswith("PUBLICATION_") or path.name.startswith("publication_")
                  or path.name in references or path.name == Path(__file__).name)]
    paths.extend(path for path in (HERE / "publication_frozen").rglob("*")
                 if path.is_file() and "__pycache__" not in path.parts)
    paths = sorted(set(paths), key=lambda path: path.relative_to(HERE).as_posix())
    members = [{"path": path.relative_to(HERE).as_posix(), "bytes": path.stat().st_size,
                "sha256": digest(path)} for path in paths]
    payload = {
        "sealed_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Part A-only final publication correspondence; shared front/footer and process bindings. No Part B validation, new numerical replication, audit or source mutation.",
        "report": "PUBLICATION_COMPARISON.md",
        "scope_incident_preserved": True,
        "combined_input_fingerprint_recomputed": False,
        "prior_reference_members": sorted(references),
        "other_preserved_PRE_seal": {
            "path": str(HERE.parent / "number-offset-observation-independent/PRE_SEAL.json"),
            "sha256": "75b6df3f1a085d3f921f9480a633e726c09230d9b027b62bc3e48b3a2898cdef",
            "members_verified_unchanged": 22
        },
        "member_count": len(members),
        "members": members,
    }
    seal_path.write_text(json.dumps(payload, indent=2) + "\n")
    for path in paths:
        if not (path.parent == HERE and path.name in references):
            path.chmod(0o444)
    seal_path.chmod(0o444)
    for member in json.loads(seal_path.read_text())["members"]:
        path = HERE / member["path"]
        assert digest(path) == member["sha256"]
        assert path.stat().st_size == member["bytes"]
    print(json.dumps({
        "status": "sealed and verified",
        "members": len(members),
        "report_sha256": digest(HERE / "PUBLICATION_COMPARISON.md"),
        "seal_sha256": digest(seal_path),
        "source_pins_sha256": digest(HERE / "PUBLICATION_SOURCE_PINS.json"),
        "scope_incident_sha256": digest(HERE / "PUBLICATION_SCOPE_INCIDENT.json")
    }, indent=2))


if __name__ == "__main__":
    main()
