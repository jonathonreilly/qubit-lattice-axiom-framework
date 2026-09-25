"""Freeze the bounded released-source POST without replacing an existing seal."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def check_members(directory, name, expected):
    path = directory / name
    assert sha(path) == expected
    seal = load(path)
    for member in seal["members"]:
        p = directory / member["path"]
        assert sha(p) == member["sha256"] and p.stat().st_size == member["bytes"]
    assert len(seal["members"]) == seal["member_count"]
    return seal["member_count"]


def main():
    destination = HERE / "POST_SEAL.json"
    assert not destination.exists(), "An existing POST seal must not be replaced."
    pre_sha = "75b6df3f1a085d3f921f9480a633e726c09230d9b027b62bc3e48b3a2898cdef"
    pre_count = check_members(HERE, "PRE_SEAL.json", pre_sha)
    prior_dir = HERE.parent / "photon-added-energy-independent"
    prior_sha = "19f2c31594a7a807771dde273c81bc01af9ecaf001f70eb569f4228be99e779c"
    prior_count = check_members(prior_dir, "PUBLICATION_COMPARISON_SEAL.json", prior_sha)
    incident_sha = "e60ae5601e7625476f3e221d5ac18b5d7eb94c41b8773a1bb7f37bd3c30ae536"
    assert sha(prior_dir / "PUBLICATION_SCOPE_INCIDENT.json") == incident_sha
    pins = load(HERE / "POST_SOURCE_PINS.json")
    for source in pins["sources"]:
        origin, frozen = Path(source["origin"]), HERE / source["frozen"]
        assert sha(origin) == sha(frozen) == source["sha256"]
        assert origin.stat().st_size == frozen.stat().st_size == source["bytes"]
    first = load(HERE / "POST_BINDING_EXECUTION.json")
    second = load(HERE / "POST_BINDING_ATTEMPT_02_EXECUTION.json")
    assert first["exit_code"] == 1 and second["exit_code"] == 0
    assert sha(HERE / "post_history/post_bind_and_check_attempt_01.py") == first["source_sha256"]
    assert sha(HERE / "post_bind_and_check.py") == second["source_sha256"]
    for execution, prefix in [(first, "POST_BINDING"), (second, "POST_BINDING_ATTEMPT_02")]:
        assert sha(HERE / f"{prefix}_STDOUT.json") == execution["stdout_sha256"]
        assert sha(HERE / f"{prefix}_STDERR.txt") == execution["stderr_sha256"]
    result = load(HERE / "POST_BINDING_ATTEMPT_02_STDOUT.json")
    assert result["checker_sha256"] == second["source_sha256"]
    for parent in result["current_parent_git_bindings"]:
        assert sha(HERE.parent / "campaign-working" / parent["path"]) == parent["sha256"]
    assert sha(HERE / "POST.md") == "c743b65fe76f616baa1bb261a49a2e9df31cf6f4526530b998d01c152ac253c2"

    names = ["PRE.md", "PRE_SEAL.json", "SOURCE_PINS.json", "POST.md",
             "POST_SOURCE_PINS.json", "POST_CORRECTIONS.json", "post_bind_and_check.py",
             "POST_BINDING_EXECUTION.json", "POST_BINDING_STDOUT.json", "POST_BINDING_STDERR.txt",
             "POST_BINDING_FAILURE_HISTORY.json", "POST_BINDING_ATTEMPT_02_EXECUTION.json",
             "POST_BINDING_ATTEMPT_02_STDOUT.json", "POST_BINDING_ATTEMPT_02_STDERR.txt",
             "post_history/post_bind_and_check_attempt_01.py", "seal_post.py"]
    names += [str(p.relative_to(HERE)) for p in (HERE / "post_frozen_author").iterdir() if p.is_file()]
    assert len(names) == len(set(names)) == 26
    members = [{"path": name, "bytes": (HERE/name).stat().st_size,
                "sha256": sha(HERE/name)} for name in sorted(names)]
    seal = {
        "sealed_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Bounded released-source root32 POST; original record law, domains, energy/accounting distinctions and conditional weak-field supplement. No author-program execution or audit verdict.",
        "report": "POST.md",
        "author_seal_sha256": pins["author_seal_sha256"],
        "author_members_verified": 8,
        "released_source_origins": len(pins["sources"]),
        "current_parent_git_origins_verified": 3,
        "PRE_preserved": {"seal_sha256": pre_sha, "members_verified": pre_count},
        "prior_Part_A_scope_record_preserved": {
            "directory": str(prior_dir), "seal_sha256": prior_sha,
            "members_verified": prior_count, "incident_sha256": incident_sha,
            "scope": "Read-only hash verification; no new Part B science inspection or validation."},
        "POST_domain_argument_attribution": "Independent POST addition, not sealed root or blind PRE authorship.",
        "weak_field_rate_independently_verified": False,
        "author_programs_executed_or_imported": [],
        "other_active_scientific_packets_opened_during_POST": [],
        "failure_history_preserved": "POST_BINDING_FAILURE_HISTORY.json",
        "member_count": len(members), "members": members,
        "next_step": "Stop. Root may read this complete sealed comparison before any public incorporation."
    }
    with destination.open("x") as stream:
        json.dump(seal, stream, indent=2)
        stream.write("\n")
    for name in names:
        (HERE/name).chmod(0o444)
    destination.chmod(0o444)
    verified = load(destination)
    for member in verified["members"]:
        assert sha(HERE/member["path"]) == member["sha256"]
    print(json.dumps({"status": "sealed and all members reverified",
                      "member_count": len(members), "POST_sha256": sha(HERE/"POST.md"),
                      "POST_SEAL_sha256": sha(destination), "PRE_members_unchanged": pre_count,
                      "prior_publication_members_unchanged": prior_count,
                      "author_members_verified": 8,
                      "released_source_origins": len(pins["sources"])}, indent=2))


if __name__ == "__main__":
    main()
