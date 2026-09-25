"""Freeze this bounded POST without rewriting any PRE member or author source."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
PRE_EXPECTED = "6dfea4b57bd88c1f127e385fa2c11294df50956079f748b48952fbf0b7965c43"
ROOT_SEAL_EXPECTED = "4dd7d35946c80fda3c70322c5ee61b475ea9f5fba4fde7a0e7cbae3521ed23cd"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def main():
    seal_path = HERE / "POST_SEAL.json"
    if seal_path.exists():
        raise FileExistsError("POST_SEAL.json already exists; no overwrite allowed")
    assert digest(HERE / "PRE_SEAL.json") == PRE_EXPECTED
    pre = load(HERE / "PRE_SEAL.json")
    assert pre["member_count"] == len(pre["members"]) == 45
    for member in pre["members"]:
        source = HERE / member["path"]
        assert source.stat().st_size == member["bytes"]
        assert digest(source) == member["sha256"], member["path"]
    verified = load(HERE / "POST_EVIDENCE_VERIFICATION.json")
    assert verified["PRE_members_unchanged"] == 45
    assert verified["POST_sha256"] == digest(HERE / "POST.md")
    assert verified["POST_SOURCE_PINS_sha256"] == digest(HERE / "POST_SOURCE_PINS.json")
    assert verified["verifier_sha256"] == digest(HERE / "post_verify_evidence.py")
    pins = load(HERE / "POST_SOURCE_PINS.json")
    assert len(pins["author_inputs"]) == 21
    for source in pins["author_inputs"]:
        for key in ("path", "frozen_path"):
            path = Path(source[key])
            assert path.stat().st_size == source["bytes"]
            assert digest(path) == source["sha256"], str(path)
    assert digest(HERE / "post_frozen_author/AUTHOR_SEAL.json") == ROOT_SEAL_EXPECTED

    excluded = {"POST_SEAL.json", "POST_SEAL_EXECUTION.json", "POST_SEAL_STDERR.txt"}
    paths = [path for path in HERE.iterdir()
             if path.is_file() and path.name not in excluded
             and (path.name.startswith("POST") or path.name.startswith("post_")
                  or path.name in {"seal_post.py", "PRE.md", "PRE_SEAL.json"})]
    for dirname in ("post_frozen_author", "post_history"):
        paths.extend(path for path in (HERE / dirname).rglob("*")
                     if path.is_file() and "__pycache__" not in path.parts)
    paths = sorted(set(paths), key=lambda path: path.relative_to(HERE).as_posix())
    members = [{"path": path.relative_to(HERE).as_posix(),
                "bytes": path.stat().st_size, "sha256": digest(path)} for path in paths]
    payload = {
        "sealed_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Bounded released-source POST for photon-added input energy; no audit verdict or publication mutation.",
        "note": "POST.md",
        "PRE_members_verified_unchanged": 45,
        "PRE_seal_sha256": PRE_EXPECTED,
        "author_seal_sha256": ROOT_SEAL_EXPECTED,
        "author_files_and_origins_verified": 21,
        "PRE_reference_members": ["PRE.md", "PRE_SEAL.json"],
        "member_count": len(members),
        "members": members,
    }
    seal_path.write_text(json.dumps(payload, indent=2) + "\n")
    for path in paths:
        if path.name not in {"PRE.md", "PRE_SEAL.json"} or path.parent != HERE:
            path.chmod(0o444)
    seal_path.chmod(0o444)
    for member in load(seal_path)["members"]:
        path = HERE / member["path"]
        assert digest(path) == member["sha256"]
        assert path.stat().st_size == member["bytes"]
    print(json.dumps({
        "status": "sealed and verified",
        "member_count": len(members),
        "PRE_members_unchanged": 45,
        "POST_sha256": digest(HERE / "POST.md"),
        "POST_SOURCE_PINS_sha256": digest(HERE / "POST_SOURCE_PINS.json"),
        "POST_SEAL_sha256": digest(seal_path),
        "seal_script_sha256": digest(Path(__file__).resolve()),
    }, indent=2))


if __name__ == "__main__":
    main()
