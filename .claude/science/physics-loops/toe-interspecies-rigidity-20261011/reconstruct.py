"""Reconstruct declared note/primary bytes without executing their source.

With no arguments, verify reconstruction and current external candidate files.
--output-dir DIRECTORY writes reconstructed copies only to that directory.
"""
from pathlib import Path
import argparse
import gzip
import hashlib
import json

D = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output-dir", type=Path)
args = parser.parse_args()
manifest = json.loads((D / "SOURCE_COMPOSITION.json").read_text())


def sha(b):
    return hashlib.sha256(b).hexdigest()


def read_source(rel):
    p = D / rel
    if not p.exists():
        p = D / (rel + ".gz")
    assert p.resolve().is_relative_to(D)
    raw = p.read_bytes()
    return gzip.decompress(raw) if p.suffix == ".gz" else raw


for source in manifest["historical_files"]:
    stored = (D / source["preserved_path"]).read_bytes()
    assert sha(stored) == source["stored_sha256"], source["preserved_path"]
    assert sha(read_source(source["preserved_path"])) == source["original"]["sha256"]
for output in manifest["outputs"]:
    complete = b""
    for part in output["parts"]:
        raw = read_source(part["source"])
        assert sha(raw) == part["source_sha256"], part["source"]
        if part["kind"] == "historical_lines":
            first, last = part["lines_inclusive"]
            raw = b"".join(raw.splitlines(keepends=True)[first-1:last])
            assert sha(raw) == part["raw_fragment_sha256"]
            for edit in part["edits"]:
                old, new = edit["old"].encode(), edit["new"].encode()
                assert raw.count(old) == edit["count"]
                raw = raw.replace(old, new)
        assert sha(raw) == part["output_fragment_sha256"]
        lo, hi = part["output_byte_range_half_open"]
        assert lo == len(complete) and hi == lo + len(raw)
        complete += raw
    assert sha(complete) == output["sha256"], output["name"]
    assert len(complete) == output["bytes"]
    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        dst = args.output_dir / output["name"]
        if dst.exists():
            assert dst.read_bytes() == complete, "Refuse to overwrite different bytes"
        else:
            dst.write_bytes(complete)
    else:
        candidate = D.parent / output["name"]
        if candidate.exists():
            assert candidate.read_bytes() == complete
    print(output["name"], sha(complete), "exact reconstruction")
print("PASS: source composition only; no mathematical or audit verdict")
