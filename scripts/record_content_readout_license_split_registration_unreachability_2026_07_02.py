#!/usr/bin/env python3
"""Record-content readout license split and registration unreachability.

Source-side disclaimer: this runner checks the source note's finite-grid
machinery, exact identities, numeric anchors, and source-boundary guard. It
does not set, predict, or apply any audit verdict.

L1. The identity-channel readout floor writes no record, so under the readout
    clause it is readout-construction content; the record-determined component
    is exactly T_V - T_id = -Re chi_3.
L2. For the named family (1-p) delta + p T_V, the
    record-determined per-step m^2 is bounded by Delta m^2 = 0.605570 < 1,
    so the unit point is unreachable as record-determined content.
L3. At the total-variance unit point, the record-determined share is 0.248120
    and the reconstruction share is 0.751880; the shares sum to one.
"""

from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "RECORD_CONTENT_READOUT_LICENSE_SPLIT_REGISTRATION_UNREACHABILITY_THEOREM_NOTE_2026-07-02.md"
DEPS = {
    "axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
    "graph-first": ROOT / "docs" / "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md",
    "rigidity": ROOT / "docs" / "G_BARE_RIGIDITY_THEOREM_NOTE.md",
    "semigroup": ROOT / "docs" / "RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md",
}

TWOPI = 2.0 * np.pi
PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} {name}{suffix}")
    return ok


def wrap_pi(x):
    return (x + np.pi) % TWOPI - np.pi


def flatten(text):
    return " ".join(text.split())


def require_contains(label, text, needle):
    check(label, needle in text, f"needle={needle!r}")


def require_absent(label, text, needle):
    check(label, needle not in text, f"needle={needle!r}")


def rel_path(path):
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def weyl_grid_integrals(m):
    xs = (np.arange(m, dtype=float) + 0.5) * (TWOPI / m) - np.pi
    totals = {
        "haar": 0.0,
        "tv": 0.0,
        "tid": 0.0,
        "w3_tv": 0.0 + 0.0j,
        "w3_tid": 0.0 + 0.0j,
        "w8_tv": 0.0,
        "w8_tid": 0.0,
        "re_s2_naive": 0.0,
        "re_s2_min": 0.0,
        "s2_min": 0.0,
        "tv_s2_min": 0.0,
        "tid_s2_min": 0.0,
    }
    max_diff = 0.0
    chunk = 256
    for start in range(0, m, chunk):
        a = xs[start : start + chunk][:, None]
        b = xs[None, :]
        c = wrap_pi(-a - b)

        re_chi3 = np.cos(a) + np.cos(b) + np.cos(c)
        im_chi3 = np.sin(a) + np.sin(b) + np.sin(c)
        abs_chi3_sq = re_chi3 * re_chi3 + im_chi3 * im_chi3
        chi8 = abs_chi3_sq - 1.0

        cab = np.cos(a - b)
        cac = np.cos(a - c)
        cbc = np.cos(b - c)
        haar = ((2.0 - 2.0 * cab) * (2.0 - 2.0 * cac) * (2.0 - 2.0 * cbc)) / 6.0

        tv = (abs_chi3_sq + 1.0) / 2.0
        tid = ((re_chi3 + 1.0) * (re_chi3 + 1.0) + im_chi3 * im_chi3) / 2.0
        max_diff = max(max_diff, float(np.max(np.abs((tv - tid) - (-re_chi3)))))

        s2_naive = a * a + b * b + c * c
        phase_sum = a + b + c
        q = np.rint(phase_sum / TWOPI).astype(int)
        max_phase = np.maximum(np.maximum(a, b), c)
        min_phase = np.minimum(np.minimum(a, b), c)
        s2_min = s2_naive.copy()
        s2_min = np.where(q == 1, s2_naive + TWOPI * TWOPI - 2.0 * TWOPI * max_phase, s2_min)
        s2_min = np.where(q == -1, s2_naive + TWOPI * TWOPI + 2.0 * TWOPI * min_phase, s2_min)

        conj_chi3 = re_chi3 - 1j * im_chi3
        totals["haar"] += float(np.sum(haar))
        totals["tv"] += float(np.sum(haar * tv))
        totals["tid"] += float(np.sum(haar * tid))
        totals["w3_tv"] += np.sum(haar * tv * conj_chi3)
        totals["w3_tid"] += np.sum(haar * tid * conj_chi3)
        totals["w8_tv"] += float(np.sum(haar * tv * chi8))
        totals["w8_tid"] += float(np.sum(haar * tid * chi8))
        totals["re_s2_naive"] += float(np.sum(haar * re_chi3 * s2_naive))
        totals["re_s2_min"] += float(np.sum(haar * re_chi3 * s2_min))
        totals["s2_min"] += float(np.sum(haar * s2_min))
        totals["tv_s2_min"] += float(np.sum(haar * tv * s2_min))
        totals["tid_s2_min"] += float(np.sum(haar * tid * s2_min))

    norm = float(m * m)
    out = {key: value / norm for key, value in totals.items()}
    out["w3_tv"] = out["w3_tv"] / 3.0
    out["w3_tid"] = out["w3_tid"] / 3.0
    out["w8_tv"] = out["w8_tv"] / 8.0
    out["w8_tid"] = out["w8_tid"] / 8.0
    out["max_diff"] = max_diff
    return out


def section_a(g1600, g3200):
    print("\nSECTION A -- kernels re-derived on the Weyl grid")
    check("A0-haar-density-mean-M1600", abs(g1600["haar"] - 1.0) < 1e-9, f"value={g1600['haar']:.12f}")
    check(
        "A1-exact-difference-TV-minus-Tid-M1600",
        g1600["max_diff"] < 1e-12,
        f"max={g1600['max_diff']:.3e}",
    )
    check(
        "A1-exact-difference-TV-minus-Tid-M3200",
        g3200["max_diff"] < 1e-12,
        f"max={g3200['max_diff']:.3e}",
    )
    check("A2-TV-normalization", abs(g1600["tv"] - 1.0) < 1e-9, f"value={g1600['tv']:.12f}")
    check("A2-Tid-normalization", abs(g1600["tid"] - 1.0) < 1e-9, f"value={g1600['tid']:.12f}")
    check("A3-w3-Tid", abs(g1600["w3_tid"] - Fraction(1, 6)) < 1e-9, f"value={g1600['w3_tid'].real:.12f}")
    check("A3-w3-TV", abs(g1600["w3_tv"]) < 1e-9, f"value={g1600['w3_tv'].real:.12e}")
    check("A3-w8-TV", abs(g1600["w8_tv"] - Fraction(1, 16)) < 1e-9, f"value={g1600['w8_tv']:.12f}")
    check("A3-w8-Tid", abs(g1600["w8_tid"] - Fraction(1, 16)) < 1e-9, f"value={g1600['w8_tid']:.12f}")


def section_b(g1600, g3200):
    print("\nSECTION B -- branch moments and exact identities")
    target_naive = float(Fraction(-19, 8))
    e1600 = abs(g1600["re_s2_naive"] - target_naive)
    e3200 = abs(g3200["re_s2_naive"] - target_naive)
    print(f"  <Re chi_3 * s2_naive> M1600={g1600['re_s2_naive']:.12f}")
    print(f"  <Re chi_3 * s2_naive> M3200={g3200['re_s2_naive']:.12f}")
    check("B1-naive-branch-exact-identity", e3200 < 5e-9, f"error={e3200:.3e}")
    check("B1-naive-branch-double-grid-convergence", e3200 < e1600, f"errors {e1600:.3e} -> {e3200:.3e}")

    check(
        "B2-zero-sum-Rechi3-s2-min-anchor",
        abs(g3200["re_s2_min"] - (-2.422278270)) < 1e-8,
        f"value={g3200['re_s2_min']:.12f}",
    )
    check(
        "B2-zero-sum-s2-min-Haar-anchor",
        abs(g3200["s2_min"] - 9.466227112) < 1e-8,
        f"value={g3200['s2_min']:.12f}",
    )
    check(
        "B2-zero-sum-s2-TV-anchor",
        abs(g3200["tv_s2_min"] - 9.762523409) < 1e-8,
        f"value={g3200['tv_s2_min']:.12f}",
    )

    increment = -g3200["re_s2_min"]
    floor = g3200["tid_s2_min"]
    total = g3200["tv_s2_min"]
    delta_m2 = increment / 4.0
    print(f"  increment={increment:.12f} floor={floor:.12f} total={total:.12f}")
    print(f"  Delta m^2={delta_m2:.12f}")
    check("B3-increment-anchor", abs(increment - 2.422278270) < 1e-8, f"value={increment:.12f}")
    check("B3-floor-anchor", abs(floor - 7.340245139) < 1e-8, f"value={floor:.12f}")
    check(
        "B3-definitional-consistency-increment-plus-floor",
        abs(increment + floor - total) < 1e-10,
        f"residual={increment + floor - total:.3e}",
    )
    check("B3-Delta-m2-anchor", abs(delta_m2 - 0.605569567) < 2e-6, f"value={delta_m2:.12f}")
    return increment, floor, total, delta_m2


def section_c(delta_m2):
    print("\nSECTION C -- unreachability")
    margin = 1.0 - delta_m2
    required_fraction = 1.0 / delta_m2
    print(f"  margin=1-Delta m^2={margin:.12f}")
    print(f"  required informative fraction={required_fraction:.12f}")
    check("C1-Delta-m2-less-than-one", delta_m2 < 1.0, f"Delta m^2={delta_m2:.12f}")
    check("C1-unit-exclusion-margin", margin > 0.35, f"margin={margin:.12f}")
    check("C2-required-fraction-unreachable", required_fraction > 1.0, f"value={required_fraction:.12f}")
    check("C2-required-fraction-margin", required_fraction > 1.5, f"value={required_fraction:.12f}")
    for p in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1, 1)):
        value = float(p) * delta_m2
        check(
            f"C3-monotone-family-bound-p={p} (definitional)",
            value <= delta_m2 and delta_m2 < 1.0,
            f"p*Delta m^2={value:.12f}",
        )


def section_d(g3200, increment, floor):
    print("\nSECTION D -- shares at the unit point")
    s2_tv_formula = g3200["s2_min"] + float(Fraction(8, 27))
    p_star = 4.0 / s2_tv_formula
    record_share = p_star * increment / 4.0
    reconstruction_share = p_star * floor / 4.0
    print(f"  p*={p_star:.9f}")
    print(f"  record share={record_share:.9f}")
    print(f"  reconstruction share={reconstruction_share:.9f}")
    check("D1-p-star-anchor", abs(p_star - 0.409731) < 5e-6, f"value={p_star:.9f}")
    check("D2-record-share-anchor", abs(record_share - 0.248120) < 1e-5, f"value={record_share:.9f}")
    check(
        "D2-reconstruction-share-anchor",
        abs(reconstruction_share - 0.751880) < 1e-5,
        f"value={reconstruction_share:.9f}",
    )
    check(
        "D3-shares-sum-definitional",
        abs(record_share + reconstruction_share - 1.0) < 1e-12,
        f"sum={record_share + reconstruction_share:.12f}",
    )
    check("D3-record-share-interior", 0.05 < record_share < 0.95, f"value={record_share:.9f}")
    check("D3-reconstruction-share-interior", 0.05 < reconstruction_share < 0.95, f"value={reconstruction_share:.9f}")


def section_e():
    print("\nSECTION E -- source-boundary guards")
    check("E0-note-exists", NOTE.exists(), rel_path(NOTE))
    for name, path in DEPS.items():
        check(f"E0-dep-exists-{name}", path.exists(), rel_path(path))

    dep_text = {name: flatten(path.read_text(encoding="utf-8")) for name, path in DEPS.items()}
    require_contains(
        "E1-axioms-readout-marker-1",
        dep_text["axioms"],
        "Only records are readable. A readout value is determined by record content alone.",
    )
    require_contains(
        "E1-axioms-readout-marker-2",
        dep_text["axioms"],
        "For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.",
    )
    require_contains("E1-graph-first-marker", dep_text["graph-first"], "the joint commutant has dimension `10`")
    require_contains("E1-rigidity-marker", dep_text["rigidity"], "no independent scalar-normalization freedom")
    require_contains(
        "E1-semigroup-marker",
        dep_text["semigroup"],
        "continuous Markov semigroups live on the probability/ensemble",
    )

    note_raw = NOTE.read_text(encoding="utf-8")
    note_flat = flatten(note_raw)
    preserve = [
        "set only by the independent audit lane",
        "license split",
        "record-determined",
        "readout-construction",
        "T_V - T_id = -Re chi_3",
        "-19/8",
        "0.605570",
        "not attainable as record-determined content",
        "0.248120",
        "0.751880",
        "located, never forced",
        "not a citation-graph dependency",
        "does not claim:",
        "an audit verdict or any effective-status promotion",
        "does not adjudicate which component",
    ]
    for marker in preserve:
        require_contains(f"E2-note-preserve-marker: {marker[:48]}", note_flat, marker)

    runner_raw = Path(__file__).read_text(encoding="utf-8")
    combined = (note_raw + "\n" + runner_raw).lower()
    forbidden = [
        "audit" + "_" + "status:",
        "effective" + "_" + "status:",
        "only" + " " + "route",
        "exh" + "austed",
        "closes" + " " + "the" + " " + "route",
        "the" + " " + "total" + " " + "is" + " " + "unlicensed",
    ]
    for needle in forbidden:
        require_absent(f"E3-forbidden-absent: {needle}", combined, needle)


def main():
    print("Record-content readout license split runner")
    print("Computing Weyl grids M=1600 and M=3200")
    g1600 = weyl_grid_integrals(1600)
    g3200 = weyl_grid_integrals(3200)
    section_a(g1600, g3200)
    increment, floor, total, delta_m2 = section_b(g1600, g3200)
    section_c(delta_m2)
    section_d(g3200, increment, floor)
    section_e()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
