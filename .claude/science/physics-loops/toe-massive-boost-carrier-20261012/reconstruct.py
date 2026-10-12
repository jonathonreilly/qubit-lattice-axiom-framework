"""Read-only reconstruction of the complete massive-carrier note and primary.

Check all preserved own input bytes and every administrative forward map.
Never import/execute scientific helpers, write files, query Git, download
external content, run caches/graphs/lint or apply an audit.
"""
import gzip
import hashlib
import json
from pathlib import Path

P = Path(__file__).resolve().parent
W = P.parents[3]
EXPECTED = {
    "docs/MASSIVE_BOOST_CARRIER_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "scripts/massive_boost_carrier_2026_10_12.py",
}
CATEGORIES = {"claim_metadata", "review_status", "portable_provenance", "historical_status",
              "runner_declarations", "canonical_cli", "suppress_output_side_effect"}


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def packet_path(relative):
    require(relative not in {"", "."} and not Path(relative).is_absolute() and ".." not in Path(relative).parts, "Unsafe preserved path")
    path = P / relative
    require(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(P.resolve()), "Absent/nonregular evidence: " + relative)
    return path


evidence = json.loads(packet_path("EVIDENCE_MAP.json").read_text())
originals, preserved = {}, {}
for row in evidence["files"]:
    require(row["original"] not in originals and row["preserved"] not in preserved, "Duplicate evidence original/target")
    require(row["preserved"].startswith("evidence/"), "Evidence target outside own evidence folder")
    packed = packet_path(row["preserved"]).read_bytes()
    require(sha(packed) == row["compressed_sha256"], row["preserved"])
    raw = gzip.decompress(packed)
    require(len(raw) == row["bytes"] and sha(raw) == row["sha256"], row["original"])
    originals[row["original"]] = row
    preserved[row["preserved"]] = row
actual = {str(path.relative_to(P)) for path in (P / "evidence").rglob("*") if path.is_file()}
require(actual == set(preserved), "Preserved own evidence membership changed")
mapping = json.loads(packet_path("PUBLICATION_EDITS.json").read_text())
require(mapping["mathematical_changes"] == [], "Unexpected mathematical edit declaration")
require(len(mapping["outputs"]) == 2 and {r["publication_path"] for r in mapping["outputs"]} == EXPECTED,
        "Expected one complete note and one entire primary")
for row in mapping["outputs"]:
    require(row["mathematical_changes"] == [] and row["source_path"] in originals, "Missing frozen source identity")
    frozen = originals[row["source_path"]]
    require(frozen["preserved"] == row["preserved_source"] and frozen["sha256"] == row["source_sha256"], "Source map points to another original")
    raw = gzip.decompress(packet_path(row["preserved_source"]).read_bytes())
    require(len(raw) == row["source_bytes"] and sha(raw) == row["source_sha256"], row["source_path"])
    text = raw.decode()
    for edit in row["edits"]:
        require(edit["category"] in CATEGORIES and edit["occurrences"] == 1 and text.count(edit["before"]) == 1,
                "Unapproved/ambiguous administrative edit: " + edit["reason"])
        text = text.replace(edit["before"], edit["after"], 1)
    text += row["appended_text"]
    path = W / row["publication_path"]
    require(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(W.resolve()), "Absent/nonregular publication")
    data = path.read_bytes()
    require(data == text.encode() and len(data) == row["publication_bytes"] and sha(data) == row["publication_sha256"], row["publication_path"])
print("All own evidence and the complete massive-carrier note/primary reconstruct exactly. External PDF bytes remain inventoried only. No science executed.")
