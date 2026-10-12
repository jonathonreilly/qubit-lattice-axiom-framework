"""Verify preserved own evidence and reconstruct all five complete notes/primaries.

No science execution, file writes, Git operations, external downloads or audit
application occur. Raw external paper content is inventoried, not reread here.
"""
import gzip
import hashlib
import json
from pathlib import Path

P = Path(__file__).resolve().parent
W = P.parents[3]


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def packet_path(relative):
    require(not Path(relative).is_absolute() and ".." not in Path(relative).parts, "Unsafe preserved path")
    path = P / relative
    require(path.is_file() and not path.is_symlink(), "Absent/nonregular evidence: " + relative)
    require(path.resolve().is_relative_to(P.resolve()), "Evidence path escaped packet")
    return path


evidence = json.loads((P / "EVIDENCE_MAP.json").read_text())
seen = set()
for row in evidence["files"]:
    require(row["preserved"] not in seen, "Duplicate evidence target")
    seen.add(row["preserved"])
    packed = packet_path(row["preserved"]).read_bytes()
    require(sha(packed) == row["compressed_sha256"], row["preserved"])
    raw = gzip.decompress(packed)
    require(len(raw) == row["bytes"] and sha(raw) == row["sha256"], row["original"])
actual = {str(path.relative_to(P)) for path in (P / "evidence").rglob("*") if path.is_file()}
require(actual == seen, "Preserved evidence membership changed")
mapping = json.loads((P / "PUBLICATION_EDITS.json").read_text())
require(mapping["mathematical_changes"] == [], "Unexpected mathematical edit declaration")
require(len(mapping["outputs"]) == 10, "Expected five complete notes and five entire primaries")
publications = set()
for row in mapping["outputs"]:
    require(row["publication_path"] not in publications, "Duplicate publication target")
    publications.add(row["publication_path"])
    raw = gzip.decompress(packet_path(row["preserved_source"]).read_bytes())
    require(sha(raw) == row["source_sha256"], row["source_path"])
    text = raw.decode()
    for edit in row["edits"]:
        require(edit.get("occurrences", 1) == 1 and text.count(edit["before"]) == 1, "Ambiguous edit: " + edit["reason"])
        text = text.replace(edit["before"], edit["after"], 1)
    text += row["appended_text"]
    relative = Path(row["publication_path"])
    require(not relative.is_absolute() and ".." not in relative.parts, "Unsafe publication path")
    final_path = W / relative
    require(final_path.is_file() and not final_path.is_symlink() and final_path.resolve().is_relative_to(W.resolve()), "Absent/nonregular publication")
    final = final_path.read_bytes()
    require(final == text.encode() and sha(final) == row["publication_sha256"] and len(final) == row["publication_bytes"], row["publication_path"])
print("All preserved own/repository evidence, five complete notes and five entire finite primaries reconstruct exactly. External paper bytes are inventoried, not bundled or reread. No science executed.")
