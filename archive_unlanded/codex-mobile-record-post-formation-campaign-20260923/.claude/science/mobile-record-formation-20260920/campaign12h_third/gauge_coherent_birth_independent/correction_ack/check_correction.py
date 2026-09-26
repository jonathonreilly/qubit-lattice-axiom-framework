#!/usr/bin/env python3
"""Authenticate only the accepted coarse-instrument wording correction."""
from __future__ import annotations

import difflib
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
INDEPENDENT = OUT.parent
BASE = INDEPENDENT.parent
ARCHIVE = BASE / "gauge_coherent_birth_source_history/before_coarse_instrument_qualification"
ORIGINAL_SEAL = "GAUGE_COMPLETION_AND_COHERENT_BIRTH_AUTHOR_SEAL.json"
CORRECTED_SEAL = "GAUGE_COMPLETION_AND_COHERENT_BIRTH_CORRECTED_SEAL.json"
EXPECTED = {
    "original": "016efff81e95874edb19222e7d5b490bc0b1e1693aed003b04a58d444fa71f08",
    "corrected": "f145523828176240065fa7638bb2b3b1a20993c866d5ac216e9cb99543a40c44",
    "precomparison": "fc30598ddaf5e586a999301ba3ad4561a78a6614268399d09fa8fb435519cc3b",
    "comparison": "d6b6af6ace5311c0e0415edd26b4066017e3674981fabe8b3c203af1f425bdf4",
}
bindings: dict[str, dict] = {}


def read_bound(path: Path, expected: dict | str | None = None) -> bytes:
    path = path.resolve()
    raw = path.read_bytes()
    row = {"path": str(path), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
    if isinstance(expected, str):
        assert row["sha256"] == expected, (path, row, expected)
    elif expected is not None:
        assert row["sha256"] == expected["sha256"], (path, row, expected)
        assert row["bytes"] == expected["bytes"], (path, row, expected)
    if str(path) in bindings:
        assert bindings[str(path)] == row, ("concurrent source change", path)
    bindings[str(path)] = row
    return raw


def load(path: Path, expected: dict | str | None = None) -> dict:
    return json.loads(read_bound(path, expected))


def main() -> None:
    original = load(ARCHIVE / ORIGINAL_SEAL, EXPECTED["original"])
    corrected = load(BASE / CORRECTED_SEAL, EXPECTED["corrected"])
    mapping = load(ARCHIVE / "ARCHIVE_MAPPING.json")
    assert mapping["original_seal_sha256"] == EXPECTED["original"]
    assert corrected["original_seal_sha256"] == EXPECTED["original"]
    assert corrected["independent_comparison_seal_sha256"] == EXPECTED["comparison"]
    before = {row["path"]: row for row in original["artifacts"]}
    after = {row["path"]: row for row in corrected["artifacts"]}
    mapped = {row["original_path"]: row for row in mapping["mapping"]}
    assert len(before) == len(after) == len(mapped) == 28
    assert before.keys() == after.keys() == mapped.keys()
    relocated = {}
    for path, old in before.items():
        m = mapped[path]
        assert (m["sha256"], m["bytes"]) == (old["sha256"], old["bytes"])
        archived = Path(m["archive_path"])
        assert archived.parent == ARCHIVE and archived.name == Path(path).name
        read_bound(archived, old)
        read_bound(Path(path), after[path])
        relocated[path] = archived
    relocated[str(BASE / ORIGINAL_SEAL)] = ARCHIVE / ORIGINAL_SEAL
    read_bound(BASE / ORIGINAL_SEAL, EXPECTED["original"])

    prior_counts = {}
    for filename, key in [("PRE_COMPARISON_SEAL.json", "precomparison"),
                          ("FINAL_COMPARISON_SEAL.json", "comparison")]:
        prior = load(INDEPENDENT / filename, EXPECTED[key])
        for kind in ["sources", "artifacts"]:
            for row in prior[kind]:
                read_bound(relocated.get(row["path"], Path(row["path"])), row)
        prior_counts[filename] = {kind: len(prior[kind]) for kind in ["sources", "artifacts"]}

    replacements = {
        "COHERENT_NEUTRAL_PAIR_FORMATION_AND_GAUGE_MEMORY.md": [
            ("## 2. Complete instrument family on these two formation transitions",
             "## 2. Complete coarse birth-map family on these two transitions"),
            ("matter outputs, nonlocal field changes or initial environment correlations.\n",
             "matter outputs, nonlocal field changes or initial environment correlations.\n\n"
             "The classification by chi below concerns the birth CP map and generator\n"
             "after summing over mu. If individual mu outcomes are retained as records,\n"
             "their separate outcome maps are additional instrument data; chi alone does\n"
             "not classify that refinement. Unitary rotations of a Kraus list preserve\n"
             "the summed map while changing its individually marked outcomes.\n"),
        ],
        "FRESH_MOVING_MEMORY_DILATES_COHERENT_PAIR_BIRTH.md": [
            ("## 5. Minimal pure probe size distinguishes the instrument choices\n\n"
             "For the real-chi instrument family of the preceding note, retain the same",
             "## 5. Minimal pure probe size for the coarse channel\n\n"
             "For the real-chi coarse birth-map family of the preceding note, retain the same"),
            ("respectively. The displayed qubit collision attains the coherent case.\n",
             "respectively. The displayed qubit collision attains the coherent case.\n\n"
             "This minimum concerns the summed channel and its coarse event/no-event\n"
             "instrument. Preserving a specified finer mu-outcome record is an additional\n"
             "requirement, not classified by chi or by this channel's Choi rank alone.\n"),
        ],
    }
    changed = [path for path in before if (before[path]["sha256"], before[path]["bytes"]) !=
               (after[path]["sha256"], after[path]["bytes"])]
    assert set(Path(path).name for path in changed) == set(replacements)
    assert set(corrected["changed_artifacts"]) == set(replacements)
    generated_diff = ""
    deltas = []
    for name, changes in replacements.items():
        path = str(BASE / name)
        old = read_bound(relocated[path], before[path]).decode()
        new = read_bound(BASE / name, after[path]).decode()
        forward = old
        for removed, inserted in changes:
            assert forward.count(removed) == 1, (name, removed)
            forward = forward.replace(removed, inserted)
        assert forward == new, ("unlisted forward delta", name)
        inverse = new
        for removed, inserted in reversed(changes):
            assert inverse.count(inserted) == 1, (name, inserted)
            inverse = inverse.replace(inserted, removed)
        assert inverse == old, ("inverse recovery", name)
        generated_diff += "".join(difflib.unified_diff(
            old.splitlines(keepends=True), new.splitlines(keepends=True),
            fromfile=f"original/{name}", tofile=f"corrected/{name}"))
        deltas.append({"name": name, "before": before[path], "after": after[path],
                       "unique_replacements": len(changes), "inverse_byte_recovery": True})
    recorded_diff = read_bound(BASE / "GAUGE_COHERENT_BIRTH_F1_CORRECTION.diff").decode()
    assert generated_diff == recorded_diff, "Recorded diff is not the complete exact delta."

    result = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "PASS; accepted F1 wording correction resolved at these exact source identities.",
        "scope": "Only source-delta and provenance acknowledgment; no unchanged mathematics rerun.",
        "original_author_artifacts_authenticated": 28,
        "archived_original_seals_authenticated": 1,
        "corrected_author_artifacts_authenticated": 28,
        "unchanged_author_artifacts": 26,
        "prior_independent_bindings_authenticated": prior_counts,
        "complete_recorded_diff_verified": True,
        "changed_sources": deltas,
        "semantic_assessment": [
            "Chi now explicitly classifies the summed birth CP map and generator, not retained mu outcome maps.",
            "The Choi-rank minimum is explicitly scoped to the coarse channel/event instrument; finer records need separate data.",
            "The four exact prose replacements exhaust both full-note changes; no equation, checker, result, log or other author artifact changed.",
        ],
        "unchanged_limits": "No stronger quantum completion, instrument-classification, autonomous-memory, publication or audit conclusion is asserted.",
        "failures": [],
        "sources": sorted(bindings.values(), key=lambda row: row["path"]),
    }
    (OUT / "CORRECTION_ACK.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "sources"}, indent=2))
    print(f"Authenticated unique input files: {len(bindings)}")


if __name__ == "__main__":
    main()
