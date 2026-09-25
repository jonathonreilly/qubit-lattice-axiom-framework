"""New PRE43 evidence binder and one-shot seal writer; no science execution."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import subprocess

HERE = Path(__file__).resolve().parent


def digest(data):
    return sha256(data).hexdigest()


def identity(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(HERE)), "sha256": digest(data), "bytes": len(data)}


def write_json(name, obj):
    with (HERE / name).open("x") as stream:
        json.dump(obj, stream, indent=2)
        stream.write("\n")


assert not (HERE / "PRE_SEAL.json").exists(), "Never replace a seal"
pins = json.loads((HERE / "SOURCE_PINS.json").read_text())
source_checks = []
for row in pins["sources"]:
    frozen = HERE / row["frozen_path"]
    raw = frozen.read_bytes()
    assert digest(raw) == row["sha256"] and len(raw) == row["bytes"]
    origin = row["origin"]
    if origin.startswith("git:"):
        live = subprocess.check_output([
            "git", "-C", row["repository"], "show", row["revision"] + ":AGENTS.md"
        ])
    else:
        live = Path(origin).read_bytes()
    assert live == raw, origin
    if row.get("exact_git_object"):
        repository = Path(origin).parent.parent
        git_bytes = subprocess.check_output([
            "git", "-C", str(repository), "show",
            row["revision"] + ":docs/" + Path(origin).name
        ])
        assert git_bytes == raw, origin
    source_checks.append({"origin": origin, **identity(frozen), "exact_origin_bytes": True})

execution_checks = []
for label in ("freeze", "L4", "L6", "L8", "verification"):
    receipt_path = HERE / (label + ".execution.json")
    receipt = json.loads(receipt_path.read_text())
    script = Path(receipt["command"][2])
    assert script.parent == HERE
    assert digest(script.read_bytes()) == receipt["source_sha256"]
    assert digest((HERE / "run_logged.py").read_bytes()) == receipt["recorder_sha256"]
    assert receipt["exit_code"] == 0 and receipt["elapsed_seconds"] > 0
    for suffix, log in receipt["outputs"].items():
        data = (HERE / log["path"]).read_bytes()
        assert digest(data) == log["sha256"] and len(data) == log["bytes"]
        if suffix == "stderr.txt":
            assert data == b""
    console_path = HERE / (label + ".console.txt")
    if console_path.exists():
        expected = (json.dumps(receipt, indent=2) + "\n").encode()
        expected += (HERE / receipt["outputs"]["stdout.txt"]["path"]).read_bytes()
        assert console_path.read_bytes() == expected
        assert (HERE / (label + ".console.stderr.txt")).read_bytes() == b""
    execution_checks.append({**identity(receipt_path), "script": identity(script),
                             "exit_code": receipt["exit_code"],
                             "all_log_bindings_exact": True,
                             "console_binding_checked": console_path.exists()})

assert (HERE / "freeze.stdout.txt").read_bytes() == (HERE / "SOURCE_PINS.json").read_bytes()
expected_results = {
    "L4_RESULTS.json": "2e896ec6eded7299c0b7e0102fff2805a5927101d3b704e56d8a846e7c8e7924",
    "L6_RESULTS.json": "0ba30fb5223f0148bcf86ae19058e6a9a48909997c0e1ad69c80f5d3d2f34952",
    "L8_RESULTS.json": "adf385dc98dbf8477ff6c11b33ed1e6c5d67a73120070f554031cf85d748c21f",
    "verification.stdout.txt": "d95633c06ab117b62e6a4f287335dffb4266c59fcb3c797340ff6e826a813c62",
}
for name, expected_hash in expected_results.items():
    assert digest((HERE / name).read_bytes()) == expected_hash
assert not list(HERE.rglob("*.pyc"))
report = (HERE / "PRE.md").read_text()
assert "+{\\bf e}_{au}-{\\bf e}_{dv}+{\\bf e}_{av}-{\\bf e}_{du}." in report

bindings = {
    "at_utc": datetime.now(timezone.utc).isoformat(),
    "phase": "Blind independent PRE43 final evidence binding",
    "scope": "Source, saved execution and log identities only; scientific programs not rerun",
    "report": identity(HERE / "PRE.md"),
    "source_pins": identity(HERE / "SOURCE_PINS.json"),
    "sources": source_checks,
    "executions": execution_checks,
    "scientific_results_and_verifier_output": [identity(HERE / name) for name in expected_results],
    "genuinely_read_only_scientific_verifier": identity(HERE / "verify_read_only.py"),
    "final_binder": identity(Path(__file__)),
    "preserved_failed_executions": 0,
    "author43_access": False,
    "parent_or_author_scientific_program_execution": False,
    "prior40_mutation_or_scientific_code_reuse": False,
    "new_delegation_or_model_effort_change": False,
    "publication_or_audit_mutation": False,
}
write_json("FINAL_BINDINGS.json", bindings)
members = [identity(path) for path in sorted(HERE.rglob("*")) if path.is_file()]
seal = {
    "sealed_at_utc": datetime.now(timezone.utc).isoformat(),
    "phase": "Blind independent PRE43; author43 still unreleased",
    "report": identity(HERE / "PRE.md"),
    "source_pins": identity(HERE / "SOURCE_PINS.json"),
    "member_count": len(members),
    "members": members,
    "seal_self_exclusion": "PRE_SEAL.json and the later PRE_SEAL_RECEIPT.json cannot self-hash",
    "immutability": "Original packet members and seal set to mode 0444 after hash verification",
    "stop_condition": "No author43 access or further research after PRE sealing",
}
write_json("PRE_SEAL.json", seal)
for row in members:
    assert identity(HERE / row["path"]) == row
for row in members:
    (HERE / row["path"]).chmod(0o444)
(HERE / "PRE_SEAL.json").chmod(0o444)
receipt = {
    "at_utc": datetime.now(timezone.utc).isoformat(),
    "member_count": len(members),
    "seal": identity(HERE / "PRE_SEAL.json"),
    "report": identity(HERE / "PRE.md"),
    "source_pins": identity(HERE / "SOURCE_PINS.json"),
    "all_member_hashes_verified_after_writing_seal": True,
    "all_member_permissions_0444": all((HERE / row["path"]).stat().st_mode & 0o777 == 0o444 for row in members),
    "receipt_outside_its_own_manifest": True,
    "no_science_rerun": True,
}
write_json("PRE_SEAL_RECEIPT.json", receipt)
(HERE / "PRE_SEAL_RECEIPT.json").chmod(0o444)
print(json.dumps(receipt, indent=2))
