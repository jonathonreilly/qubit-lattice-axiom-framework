#!/usr/bin/env python3
"""Certificate for the narrowed Fam1 H=0.25 fine-pair synthesis."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "WAVE_DIRECT_DM_H025_TWO_POINT_SYNTHESIS_NOTE.md"
LOGS = {
    0: ROOT / "logs" / "2026-04-08-wave-direct-dm-h025-control-fam1-seed0.txt",
    1: ROOT / "logs" / "2026-04-08-wave-direct-dm-h025-control-fam1-seed1.txt",
}


@dataclass(frozen=True)
class StrengthRow:
    strength: float
    d_early: float
    d_late: float
    delta_hist: float
    r_hist: float


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, ok: bool, detail: str = "") -> None:
        if ok:
            self.pass_count += 1
            tag = "PASS"
        else:
            self.fail_count += 1
            tag = "FAIL"
        suffix = f" ({detail})" if detail else ""
        print(f"  [{tag}] {label}{suffix}")


def parse_rows(text: str) -> dict[float, StrengthRow]:
    chunks = re.split(r"\[strength=([0-9.]+)\]", text)
    rows: dict[float, StrengthRow] = {}
    for i in range(1, len(chunks), 2):
        strength = float(chunks[i])
        body = chunks[i + 1]
        vals = {}
        for key, pattern in {
            "d_early": r"dM\(early\)\s+=\s+([+-][0-9.]+)",
            "d_late": r"dM\(late\)\s+=\s+([+-][0-9.]+)",
            "delta_hist": r"delta_hist\s+=\s+([+-][0-9.]+)",
            "r_hist": r"R_hist\s+=\s+([+-][0-9.]+)%",
        }.items():
            m = re.search(pattern, body)
            if not m:
                raise ValueError(f"missing {key} at strength {strength}")
            vals[key] = float(m.group(1))
        rows[strength] = StrengthRow(strength, vals["d_early"], vals["d_late"], vals["delta_hist"], vals["r_hist"])
    return rows


def main() -> int:
    gate = Gate()
    note = NOTE.read_text(encoding="utf-8")
    print("Wave direct-dM H=0.25 Fam1 fine-pair synthesis")

    required = [
        "Fam1 Fine-Pair Synthesis",
        "Claim type:** bounded_theorem",
        "controlled `Fam1`, `H = 0.25`, `S = 0.004`",
        "seed `1` has the larger-magnitude negative `R_hist`",
        "coarse-to-fine seed-ordering reversal",
        "removed from this row",
        "remains out of scope",
    ]
    for phrase in required:
        gate.check(f"note contains {phrase!r}", phrase in note)

    forbidden = [
        "old coarse-H seed ordering is not refinement-stable",
        "flip is driven by uneven late-gain compression",
        "old high band closes",
        "low band retains",
        "coarse-`H` `R_hist` band",
        "coarse-`H` late-gain band",
        "would become retained",
        "\nStatus: retained\n",
        "\nStatus: promoted\n",
    ]
    for phrase in forbidden:
        gate.check(f"note avoids unsupported phrase {phrase!r}", phrase not in note)

    expected = {
        0: {"d_early": 0.004989, "d_late": 0.006246, "delta_hist": -0.001256, "r_hist": -20.12, "spread": "7.77%"},
        1: {"d_early": 0.004411, "d_late": 0.006255, "delta_hist": -0.001843, "r_hist": -29.47, "spread": "5.22%"},
    }
    rows = {}
    for seed, path in LOGS.items():
        text = path.read_text(encoding="utf-8")
        gate.check(f"seed {seed} log exists", path.exists(), str(path))
        gate.check(f"seed {seed} log declares Fam1", "family=Fam1" in text)
        gate.check(f"seed {seed} log declares H=0.250", "H=0.250" in text)
        gate.check(f"seed {seed} log has exact null summary", "null max |delta_hist| = 0.000e+00" in text)
        gate.check(f"seed {seed} log has negative sign pattern", "delta_hist sign pattern = - - -" in text)
        gate.check(f"seed {seed} log has spread summary", expected[seed]["spread"] in text)
        rows[seed] = parse_rows(text)[0.004]
        exp = expected[seed]
        gate.check(f"seed {seed} dM(early) matches", abs(rows[seed].d_early - exp["d_early"]) < 5e-7, f"{rows[seed].d_early:+.6f}")
        gate.check(f"seed {seed} dM(late) matches", abs(rows[seed].d_late - exp["d_late"]) < 5e-7, f"{rows[seed].d_late:+.6f}")
        gate.check(f"seed {seed} delta_hist matches", abs(rows[seed].delta_hist - exp["delta_hist"]) < 5e-7, f"{rows[seed].delta_hist:+.6f}")
        gate.check(f"seed {seed} R_hist matches", abs(rows[seed].r_hist - exp["r_hist"]) < 5e-3, f"{rows[seed].r_hist:+.2f}%")

    gate.check("both fine-pair seeds have negative delta_hist", rows[0].delta_hist < 0 and rows[1].delta_hist < 0)
    gate.check("seed 1 has larger-magnitude negative R_hist at H=0.25", abs(rows[1].r_hist) > abs(rows[0].r_hist))
    gate.check("the runner does not inspect coarse high/low band logs", all("high-band" not in str(p) and "low-band" not in str(p) for p in LOGS.values()))

    ok = gate.fail_count == 0
    print(f"\nWave direct-dM H=0.25 Fam1 fine-pair synthesis: {'PASS' if ok else 'FAIL'}")
    print(f"PASS={gate.pass_count} FAIL={gate.fail_count}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
