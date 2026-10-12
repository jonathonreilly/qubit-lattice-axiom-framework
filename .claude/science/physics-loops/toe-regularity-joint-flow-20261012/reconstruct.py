"""Verify every preserved byte and reconstruct all three notes and primaries."""
from pathlib import Path
import gzip
import hashlib
import json

P = Path(__file__).resolve().parent
W = P.parents[3]

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def sha(data):
    return hashlib.sha256(data).hexdigest()

evidence = json.loads((P / "EVIDENCE_MAP.json").read_text())
for row in evidence["files"]:
    packed = (P / row["preserved"]).read_bytes()
    require(sha(packed) == row["compressed_sha256"], row["preserved"])
    raw = gzip.decompress(packed)
    require(len(raw) == row["bytes"] and sha(raw) == row["sha256"], row["original"])
for row in json.loads((P / "PUBLICATION_EDITS.json").read_text())["outputs"]:
    raw = gzip.decompress((P / row["preserved_source"]).read_bytes())
    require(sha(raw) == row["source_sha256"], row["source_path"])
    text = raw.decode()
    for edit in row["edits"]:
        require(text.count(edit["before"]) == 1, "Ambiguous transformation: " + edit["reason"])
        text = text.replace(edit["before"], edit["after"], 1)
    text += row["appended_text"]
    final = (W / row["publication_path"]).read_bytes()
    require(final == text.encode() and sha(final) == row["publication_sha256"], row["publication_path"])
print("All preserved own/repository bytes, three complete notes and three entire finite primaries reconstruct exactly. External paper bytes are inventoried, not bundled or reread here.")
