#!/usr/bin/env python3
"""Read-only checksum verifier for this PRE packet; not a science validator."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent


def check(rows):
    failures = []
    for row in rows:
        path = ROOT / row["path"]
        if not path.resolve().is_relative_to(ROOT):
            failures.append({"path": row["path"], "reason": "outside packet"})
        elif not path.is_file():
            failures.append({"path": row["path"], "reason": "missing file"})
        elif hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            failures.append({"path": row["path"], "reason": "SHA256 mismatch"})
    return failures


def self_test():
    path = ROOT / "path_engine.py"
    genuine = {"path": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    rows = {
        "genuine_accepted": not check([genuine]),
        "altered_digest_rejected": bool(check([{**genuine, "sha256": "0" * 64}])),
        "missing_file_rejected": bool(check([{**genuine, "path": "ABSENT_TAMPER_TEST"}])),
        "outside_packet_rejected": bool(check([{**genuine, "path": "../outside_packet"}])),
    }
    print(json.dumps({"scope": "provenance checks only", "tests": rows,
                      "passed": all(rows.values())}, indent=2))
    return all(rows.values())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("seal", nargs="?", default="PRE_SEAL.json")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        sys.exit(0 if self_test() else 1)
    seal = json.loads((ROOT / args.seal).read_text())
    failures = check(seal["artifacts"])
    print(json.dumps({"seal": args.seal, "checked": len(seal["artifacts"]),
                      "failures": failures, "passed": not failures}, indent=2))
    sys.exit(1 if failures else 0)
