#!/usr/bin/env python3
"""Plot the frozen conditional detector calculation; no fitting or new inputs."""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

EXPECTED = "b2962638e5699da67393682f96cfd53b60fb2ff102a80782a1658d97621c76b4"

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()
    raw = args.input.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED, "different frozen input"
    data = json.loads(raw)
    args.outdir.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "font.family": "DejaVu Sans"})
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 4.9))
    configs = [("ideal", "Ideal directions", "#146b8c"),
               ("angle_and_candidate_error", "Angle + candidate error allowance", "#be5816")]
    for key, label, color in configs:
        rows = sorted([r for r in data["rows"] if r["budget"] == key and
                       r["assignment"] == "independent_fair_bits"],
                      key=lambda r: Fraction(r["eta_per_side"]))
        x = [100 * float(Fraction(r["eta_per_side"])) for r in rows]
        y = [float(r["gap_lower"]["decimal"]) for r in rows]
        axes[0].plot(x, y, "o-", label=label, color=color, lw=1.8, ms=5)
        threshold = next(t for t in data["thresholds"] if t["budget"] == key)
        xc = 100 * float(threshold["random_assignment_eta_threshold"][1]["decimal"])
        axes[0].axvline(xc, color=color, ls=":", lw=1.1, alpha=.85)
        axes[0].text(xc + .035, -.014, f"{xc:.3f}%", color=color, rotation=90, va="bottom")
        positive = [r for r in rows if r["N_for_each_error_at_most_1_percent"] is not None]
        axes[1].plot([100 * float(Fraction(r["eta_per_side"])) for r in positive],
                     [r["N_for_each_error_at_most_1_percent"] for r in positive],
                     "o-", color=color, lw=1.8, ms=5)
    axes[0].axhline(0, color="#3f4852", lw=1)
    axes[0].set_ylim(-.032, .057)
    axes[0].axhspan(-.032, 0, color="#e5e8ec", alpha=.8)
    axes[0].text(97.05, -.030, "No positive-gap certificate", fontsize=9, color="#46515c")
    axes[0].set_ylabel("Certified candidate margin above quantum bound 1")
    axes[0].set_title("Missed detections reduce the separation", loc="left", weight="bold", fontsize=11)
    axes[0].legend(loc="upper left", frameon=False, fontsize=9)
    axes[1].set_yscale("log")
    axes[1].set_ylabel("Sufficient included trials (each error ≤ 1%)")
    axes[1].set_title("Conservative fixed-horizon sample bound", loc="left", weight="bold", fontsize=11)
    for ax in axes:
        ax.set_xlabel("Equal per-arm detection efficiency (%)")
        ax.set_xlim(96.95, 100.08)
        ax.grid(axis="y", alpha=.15)
    fig.suptitle("Proposed reflection test: conditional detector tradeoff", x=.075, ha="left", fontsize=16, weight="bold")
    fig.text(.075, .10, "V = 0.95; independent loss; fresh fair bits for missed events; every heralded trial included.", fontsize=9)
    fig.text(.075, .065, "Orange allowance: 0.001 rad per arm plus 0.001 candidate correlation error; quantum null remains 1.", fontsize=9)
    fig.text(.075, .025, "Hypothetical design calculation. Not observed detector performance, an optimized test, or an empirical exclusion.", fontsize=9, color="#4a535d")
    fig.subplots_adjust(left=.075, right=.98, bottom=.23, top=.83, wspace=.29)
    outputs = []
    for ext in ["png", "pdf"]:
        q = args.outdir / ("DIRECT_DETECTION_TRADEOFF." + ext)
        if q.exists():
            raise FileExistsError(q)
        fig.savefig(q, dpi=170, facecolor="white")
        outputs.append({"path": str(q.resolve()), "sha256": hashlib.sha256(q.read_bytes()).hexdigest()})
    receipt = {"input_sha256": EXPECTED, "plot_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "outputs": outputs, "meaning": "Representation of frozen rows only; adjacent markers are joined as a visual guide."}
    (args.outdir / "FIGURE_RECEIPT_v1.json").open("x").write(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))

if __name__ == "__main__":
    main()
