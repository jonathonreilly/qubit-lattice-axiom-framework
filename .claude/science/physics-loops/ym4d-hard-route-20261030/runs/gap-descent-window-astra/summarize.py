#!/usr/bin/env python3
"""Summarize saved GUIDE data, refusing incomplete window spectra."""
import json
import math
from pathlib import Path
from collect import collect

ROOT = Path(__file__).resolve().parent
WINDOW = (2.3, 2.4, 2.5, 2.6)
MULTS = (0, 8, 4, 2, 1)


def read(name):
    return json.loads((ROOT / name).read_text())


def main():
    summary = {"grade": "GUIDE", "criterion": "absolute cutoff change <= 1e-4"}
    spectra = {}
    for cutoff in (180, 200):
        files = [ROOT / f"E{cutoff}_{s}.json" for s in ("sector0", "other")]
        records = [x for f in files for x in json.loads(f.read_text())["results"]]
        keys = [(x["beta"], x["multiplier"], x["sector"]) for x in records]
        assert len(keys) == len(set(keys)), "duplicate spectrum"
        points = collect(files)
        spectra[cutoff] = {(x["beta"], x["multiplier"]): x for x in points}
        expected = {(b, m) for b in WINDOW for m in MULTS}
        assert expected <= set(spectra[cutoff]), (cutoff, expected - set(spectra[cutoff]))
        sector0 = {(x["beta"], x["multiplier"]): x for x in records if x["sector"] == 0}
        ratios = [(x["eigenvalues"][0] / sector0[x["beta"], x["multiplier"]]["eigenvalues"][1],
                   x["beta"], x["multiplier"], x["sector"])
                  for x in records if x["sector"] != 0 and x["beta"] in WINDOW]
        largest = max(ratios)
        assert largest[0] < .98, "close competing sector requires tighter solve"
        summary[f"E{cutoff}"] = {
            "complete_points": len(points),
            "max_other_sector_over_candidate": largest,
            "max_recorded_residual": max(x["residual"] for x in records),
            "window_winning_sectors": sorted({x["winning_sector"] for x in points if x["beta"] in WINDOW}),
        }
        (ROOT / f"E{cutoff}_gaps.json").write_text(json.dumps({"grade": "GUIDE", "results": points}, indent=2) + "\n")
    summary["window"] = []
    for b in WINDOW:
        points = [spectra[200][b, m] for m in MULTS]
        gap_change = max(abs(spectra[180][b, m]["gap"] - spectra[200][b, m]["gap"]) for m in MULTS)
        delta_change = max(abs(spectra[180][b, m]["difference"] - spectra[200][b, m]["difference"]) for m in MULTS)
        assert max(gap_change, delta_change) <= 1e-4
        summary["window"].append({"beta": b, "points": points, "max_gap_change": gap_change, "max_difference_change": delta_change})
    summary["minimum_window_difference"] = min(
        (spectra[200][b, m]["difference"], b, m) for b in WINDOW for m in MULTS if m)
    leak = read("leak_sweep.json")
    summary["leakage_window"] = [x for x in leak["grid"] if x["beta"] in WINDOW]
    summary["leakage_brackets"] = leak["first_negative_brackets"]
    summary["leakage_max_window_disagreement"] = max(x["cutoff_disagreement"] for x in summary["leakage_window"])
    summary["zero_charge_controls"] = []
    for cutoff in (180, 200):
        d = read(f"E{cutoff}_zero_control.json")
        x = d["results"][0]
        assert x["beta"] == 2.6 and x["multiplier"] == -1 and x["sector"] == 0
        gap = math.log(x["eigenvalues"][0] / x["eigenvalues"][1])
        ref = next(x for x in summary["leakage_window"] if x["n"] == 2 and x["beta"] == 2.6)["values"][1]["zero_gap"]
        summary["zero_charge_controls"].append({"cutoff": cutoff, "cube_gap": gap, "reduced_gap": ref, "difference": gap - ref})
    (ROOT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({k: v for k, v in summary.items() if k not in ("window", "leakage_window")}, indent=2))


if __name__ == "__main__":
    main()
