#!/usr/bin/env python3
"""Read-only POST38 bindings and exact rational coefficient check.

No file writes, original writer execution, scientific program execution or
unreleased source traversal. In particular, only the author37 note/seal already
pinned in PRE are read; its unread members and its independent checker are not.
"""

from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parent
EXPECTED_PRE_SEAL = "db299c055ce8a454d3bd8a99ef33e13ba9688582214cf0250a16af278fab2025"
EXPECTED_AUTHOR_SEAL = "0be5f2ee5066c8a584f1d5db3ddad0c2fec2226ec1929033065d05611ea139e3"
EXPECTED_AUTHOR_NOTE = "8b5ae458dd48672764ed9a79d35affcb945473ac330a9afbeb23af4d7411204d"


def identity(data):
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def check(data, entry):
    assert identity(data) == {"sha256": entry["sha256"], "bytes": entry["bytes"]}


def git_bytes(repository, revision, path):
    proc = subprocess.run(["git", "-C", repository, "show", revision + ":" + path],
                          capture_output=True, check=True)
    assert not proc.stderr
    return proc.stdout


def main():
    pins = json.loads((ROOT / "POST_SOURCE_PINS.json").read_bytes())
    pre_seal_data = (ROOT / "PRE_SEAL.json").read_bytes()
    assert identity(pre_seal_data)["sha256"] == EXPECTED_PRE_SEAL
    pre_seal = json.loads(pre_seal_data)
    assert len(pre_seal["members"]) == 20
    pre_rows = []
    for member in pre_seal["members"]:
        path = ROOT / member["path"]
        check(path.read_bytes(), member)
        assert path.stat().st_mode & 0o222 == 0
        pre_rows.append({**member, "unchanged": True, "read_only": True})
    assert (ROOT / "PRE_SEAL.json").stat().st_mode & 0o222 == 0
    for name in ("report", "seal", "source_pins"):
        entry = pins["preserved_pre"][name]
        check((ROOT / entry["path"]).read_bytes(), entry)

    pre_pins = json.loads((ROOT / "SOURCE_PINS.json").read_bytes())
    assert len(pre_pins["sources"]) == 12
    reused_rows = []
    for entry in pre_pins["sources"]:
        data = (ROOT / entry["frozen"]).read_bytes()
        check(data, entry)
        row = {"frozen": entry["frozen"], **identity(data), "frozen_matches": True}
        if "origin" in entry:
            assert Path(entry["origin"]).read_bytes() == data
            row["origin"] = entry["origin"]
            row["live_origin_matches"] = True
        if entry["type"] == "git":
            assert git_bytes(entry["repository"], entry["revision"], entry["path"]) == data
            row["revision"] = entry["revision"]
            row["git_path"] = entry["path"]
            row["exact_git_origin_matches"] = True
        reused_rows.append(row)

    released = pins["released_sources"]
    assert len(released) == 5
    assert len({entry["frozen"] for entry in released}) == 5
    released_rows = []
    author_bytes = {}
    for entry in released:
        path = ROOT / entry["frozen"]
        assert path.resolve().is_relative_to(ROOT / "post_sources" / "author38")
        data = path.read_bytes()
        check(data, entry)
        assert Path(entry["origin"]).read_bytes() == data
        author_bytes[path.name] = data
        released_rows.append({**entry, "frozen_and_live_origin_match": True})
    assert identity(author_bytes["AUTHOR_SEAL.json"])["sha256"] == EXPECTED_AUTHOR_SEAL
    assert identity(author_bytes["NATIVE_GROUND_RESIDENCE_AND_ENERGY_BUDGET_ROOT.md"])["sha256"] == EXPECTED_AUTHOR_NOTE
    author_seal = json.loads(author_bytes["AUTHOR_SEAL.json"])
    assert len(author_seal["members"]) == 4
    assert {m["path"] for m in author_seal["members"]} == set(author_bytes) - {"AUTHOR_SEAL.json"}
    for member in author_seal["members"]:
        check(author_bytes[member["path"]], member)

    # Compare dependency metadata only against the three pre-authorized inputs.
    allowed_dependency_frozen = {
        "sources/provisional_author37/FULL_MICROSCOPIC_ENERGY_AND_FORMATION_ROOT.md",
        "sources/provisional_author37/AUTHOR_SEAL.json",
        "sources/docs/FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    }
    dependency_entries = [e for e in pre_pins["sources"] if e["frozen"] in allowed_dependency_frozen]
    assert len(dependency_entries) == 3
    expected_dependencies = {e["origin"]: e["sha256"] for e in dependency_entries}
    author_pins = json.loads(author_bytes["SOURCE_PINS.json"])
    assert {e["path"]: e["sha256"] for e in author_pins["source_files"]} == expected_dependencies
    assert len(author_pins["source_files"]) == 3
    formation = next(e for e in dependency_entries if e["type"] == "git")
    assert author_pins["main_revision"] == "60c5f194d940a7bbaf1cdd545296e31d74a02f1a"
    author_revision_data = git_bytes(formation["repository"], author_pins["main_revision"], formation["path"])
    check(author_revision_data, formation)

    coefficient_rows = []
    for alpha in (Fraction(1), Fraction(2), Fraction(3)):
        normalized_rate_floor = Fraction(4, 5) * (4-alpha)
        normalized_count_capacity = Fraction(1, 2)
        normalized_time_bound = normalized_count_capacity / normalized_rate_floor
        assert normalized_time_bound == Fraction(5, 8) / (4-alpha)
        coefficient_rows.append({
            "alpha": str(alpha), "rate_in_units_kappa_n": str(normalized_rate_floor),
            "capacity_in_units_n": str(normalized_count_capacity),
            "time_in_units_inverse_kappa": str(normalized_time_bound),
            "scope": "Exact rational arithmetic of the displayed conditional bound, not a native control",
        })
    assert coefficient_rows[1]["time_in_units_inverse_kappa"] == "5/16"
    author_time = datetime.fromisoformat(author_seal["at"])
    pre_time = datetime.fromisoformat(pre_seal["at_utc"])
    assert author_time < pre_time
    evidence_names = ["POST.md", "POST_SOURCE_PINS.json", "POST_REVIEW_RECORD.json", "verify_post_bindings.py"]
    result = {
        "at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Read-only binding, preservation and rational coefficient check; no imported scientific premise is established by this execution.",
        "preserved_pre_member_count": len(pre_rows),
        "preserved_pre_members": pre_rows,
        "reused_source_binding_count": len(reused_rows),
        "reused_source_rows": reused_rows,
        "released_source_binding_count": len(released_rows),
        "released_source_rows": released_rows,
        "all_four_author38_members_verified": True,
        "author38_dependency_hashes_equal_three_authorized_PRE_inputs": True,
        "formation_parent_at_author_named_revision": {
            "revision": author_pins["main_revision"], "path": formation["path"],
            **identity(author_revision_data), "exact_match": True,
        },
        "recorded_seal_order": {"author38": author_seal["at"], "PRE38": pre_seal["at_utc"],
                                "author_precedes_PRE": True, "external_trusted_timestamp_claim": False},
        "coefficient_rows": coefficient_rows,
        "local_POST_evidence": [{"path": name, **identity((ROOT / name).read_bytes())} for name in evidence_names],
        "author37_scope": "Only previously authorized note and seal; other members and independent checker remain unread.",
        "scientific_or_original_author_programs_executed": [],
        "file_writes_by_this_verifier": [],
        "all_requested_checks": True,
    }
    print(json.dumps(result, indent=2) + "\n", end="")


if __name__ == "__main__":
    main()
