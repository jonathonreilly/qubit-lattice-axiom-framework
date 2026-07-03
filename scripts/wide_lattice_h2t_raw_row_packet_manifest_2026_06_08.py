"""Raw-row packet verifier for the wide-lattice h^2+T distance-law note.

This does not recompute the slow wide-lattice replay.  It verifies that the
restricted source note embeds the raw rows from the SHA-pinned frozen replay
log so an auditor can recompute the distance and F~M fits from the packet.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE = REPO_ROOT / "docs" / "WIDE_LATTICE_H2T_DISTANCE_LAW_NOTE.md"
FROZEN_LOG = REPO_ROOT / "logs" / "2026-04-05-wide-lattice-h2t-distance-replay.txt"
FROZEN_LOG_SHA256 = "2faf31bf9b1015df87adaadbfa8393c4a26e100abdc6ccaf6daf70308a30e024"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{tag} {name}{suffix}")


def main() -> None:
    note = NOTE.read_text(encoding="utf-8")
    log_bytes = FROZEN_LOG.read_bytes()
    log_text = log_bytes.decode("utf-8", errors="replace")
    sha = hashlib.sha256(log_bytes).hexdigest()

    print("WIDE LATTICE RAW ROW PACKET MANIFEST")
    print(f"note={NOTE.relative_to(REPO_ROOT)}")
    print(f"frozen_log={FROZEN_LOG.relative_to(REPO_ROOT)}")
    print(f"frozen_sha256={sha}")

    check("frozen log sha pinned", sha == FROZEN_LOG_SHA256)
    check("note names frozen sha", FROZEN_LOG_SHA256 in note)
    check("note names verifier cache", "logs/runner-cache/wide_lattice_h2t_distance_replay.txt" in note)
    check("note names raw-row manifest cache", "logs/runner-cache/wide_lattice_h2t_raw_row_packet_manifest_2026_06_08.txt" in note)

    distance_rows = re.findall(
        r"^\s+z=\s*(\d+)\s+delta=([+-]\d+\.\d+)\s+(TOWARD|AWAY)\s*$",
        log_text,
        re.MULTILINE,
    )
    check("distance row count", len(distance_rows) == 10, f"count={len(distance_rows)}")
    for z, delta, direction in distance_rows:
        row = f"| {int(z)} | `{delta}` | {direction} |"
        check(f"distance row z={z} exposed", row in note, row)

    fm_rows = re.findall(
        r"^\s+s=([0-9]e-[0-9]{2}):\s+delta=([+-]\d+\.\d+e[+-]\d+)\s+(TOWARD|AWAY)\s*$",
        log_text,
        re.MULTILINE,
    )
    check("F~M row count", len(fm_rows) == 6, f"count={len(fm_rows)}")
    for strength, delta, direction in fm_rows:
        row = f"| `{strength}` | `{delta}` | {direction} |"
        check(f"F~M row s={strength} exposed", row in note, row)

    check("peak-tail recompute visible", "| peak tail from `z >= 4` | `-0.9579` | `0.9801` | 8 |" in note)
    check("far-tail recompute visible", "| far tail from `z >= 5` | `-1.0578` | `0.9904` | 7 |" in note)
    check("F~M exponent visible", "alpha = 1.000003, R^2 = 1.000000, n = 6" in note)

    print(f"RAW_ROW_PACKET PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
