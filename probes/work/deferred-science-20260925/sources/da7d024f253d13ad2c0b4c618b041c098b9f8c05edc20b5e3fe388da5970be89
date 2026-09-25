#!/usr/bin/env python3
"""Read-only identity check for the blind conditional PRE38 packet.

This script executes no scientific program or author sealing writer, writes no
file, and reads only explicitly pinned origins and this packet's own evidence.
It does not verify the unread members listed in the supplied author37 seal.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parent
PINS = ROOT / "SOURCE_PINS.json"
EXPECTED_SCIENCE = {
    "sources/docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md":
        "2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516",
    "sources/provisional_author37/FULL_MICROSCOPIC_ENERGY_AND_FORMATION_ROOT.md":
        "7e03d6e1b644dd841cf5d7cc35863a884db8f40cf092d276cd0b90cfa7a0deeb",
    "sources/provisional_author37/AUTHOR_SEAL.json":
        "b2ed6d091f07232dec83eadc338e6385f1e20f5efddfff29288e871b0c792dd3",
}


def identity(data):
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def checked_identity(data, expected):
    actual = identity(data)
    assert actual == {"sha256": expected["sha256"], "bytes": expected["bytes"]}, (
        actual, expected
    )
    return actual


def main():
    pins = json.loads(PINS.read_bytes())
    entries = pins["sources"]
    assert len(entries) == 12
    assert len({x["frozen"] for x in entries}) == len(entries)
    frozen_payloads = {}
    rows = []
    for entry in entries:
        frozen = ROOT / entry["frozen"]
        assert frozen.resolve().is_relative_to(ROOT)
        data = frozen.read_bytes()
        checked_identity(data, entry)
        frozen_payloads[entry["frozen"]] = data
        row = {
            "frozen": entry["frozen"],
            "role": entry["role"],
            **identity(data),
            "frozen_matches": True,
        }
        if entry["type"] == "git":
            proc = subprocess.run(
                ["git", "-C", entry["repository"], "show",
                 entry["revision"] + ":" + entry["path"]],
                capture_output=True, check=True,
            )
            assert not proc.stderr
            assert proc.stdout == data
            row["exact_git_origin_matches"] = True
            row["revision"] = entry["revision"]
            row["git_path"] = entry["path"]
        else:
            assert entry["type"] == "filesystem"
        if "origin" in entry:
            assert Path(entry["origin"]).read_bytes() == data
            row["live_origin_matches"] = True
            row["origin"] = entry["origin"]
        rows.append(row)

    for path, sha in EXPECTED_SCIENCE.items():
        assert identity(frozen_payloads[path])["sha256"] == sha
    for installed, repository in [
        ("sources/INSTALLED_PHYSICS_CLAIM_REVIEWER_SKILL.md",
         "sources/docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md"),
        ("sources/INSTALLED_NO_GO_DISCIPLINE_SKILL.md",
         "sources/docs/ai_methodology/skills/no-go-discipline/SKILL.md"),
    ]:
        assert frozen_payloads[installed] == frozen_payloads[repository]

    author_seal = json.loads(frozen_payloads["sources/provisional_author37/AUTHOR_SEAL.json"])
    author_note_name = "FULL_MICROSCOPIC_ENERGY_AND_FORMATION_ROOT.md"
    note_members = [m for m in author_seal["members"] if m["path"] == author_note_name]
    assert len(note_members) == 1
    checked_identity(frozen_payloads["sources/provisional_author37/" + author_note_name], note_members[0])
    local_files = ["PRE.md", "SOURCE_PINS.json", "INDEPENDENCE_AND_FAILURE_RECORD.json",
                   "verify_pre_sources.py"]
    print(json.dumps({
        "at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Read-only source and own-evidence binding; no imported-physics verdict.",
        "source_count": len(rows),
        "exact_git_origins": sum("exact_git_origin_matches" in r for r in rows),
        "live_filesystem_origins": sum("live_origin_matches" in r for r in rows),
        "source_rows": rows,
        "installed_skills_equal_pinned_repository_skills": True,
        "author37_seal_scope": {
            "listed_members": len(author_seal["members"]),
            "members_read_and_verified": [author_note_name],
            "other_member_files_read_or_verified": False,
            "note_and_seal_match_dispatched_sha256": True,
        },
        "local_evidence": [{"path": f, **identity((ROOT / f).read_bytes())} for f in local_files],
        "scientific_programs_executed": [],
        "original_sealing_writers_executed": [],
        "all_requested_identity_checks": True,
    }, indent=2) + "\n", end="")


if __name__ == "__main__":
    main()
