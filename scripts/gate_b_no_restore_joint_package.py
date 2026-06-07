#!/usr/bin/env python3
"""Gate B no-restore joint package harness.

Freeze the bounded Born / d_TV / MI / decoherence comparison on the same
grown-geometry family with restore fixed to 0. This asks how much of the
non-gravity package survives when the restoring pull toward the grid is
removed entirely.

The comparison is intentionally narrow:
- exact grid reference
- no-restore grown rows at a few drift values

This is a companion to gate_b_grown_joint_package.py, but it isolates the
no-restore lane the user asked for.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
import random
import re
import time
from dataclasses import dataclass
from pathlib import Path


BETA = 0.8
K = 5.0
H = 0.5
NL = 25
PW = 10
MAX_D_PHYS = 3
LAM = 10.0
N_YBINS = 8
SEEDS = [0]
ROWS = [
    ("exact grid", 0.0, 1.0),
    ("no restore drift=0.0", 0.0, 0.0),
    ("no restore drift=0.2", 0.2, 0.0),
    ("no restore drift=0.5", 0.5, 0.0),
]
AUDIT_TIMEOUT_SEC = 180
REPO_ROOT = Path(__file__).resolve().parents[1]
FROZEN_LOG = REPO_ROOT / "logs" / "2026-04-05-gate-b-no-restore-joint-package.txt"
RECOMPUTE_CERT = REPO_ROOT / "outputs" / "gate_b_no_restore_recompute_certificate_2026_06_07.json"
BORN_TOL = 5.0e-18
METRIC_TOL = 5.0e-4
DECOH_TOL = 5.0e-2
ROW_RE = re.compile(
    r"^(?P<label>exact grid|no restore drift=[0-9.]+)\s+"
    r"(?P<born>[0-9.]+e[+-][0-9]+)\s+"
    r"(?P<dtv>[0-9.]+)\s+"
    r"(?P<mi>[0-9.]+)\s+"
    r"(?P<decoh>[0-9.]+)%$",
    re.MULTILINE,
)


@dataclass
class JointRow:
    label: str
    born: float
    d_tv: float
    mi: float
    decoh: float

    def as_dict(self) -> dict[str, float | str]:
        return {
            "label": self.label,
            "born": self.born,
            "d_tv": self.d_tv,
            "mi": self.mi,
            "decoh": self.decoh,
        }


def grow(drift: float, restore: float, seed: int):
    rng = random.Random(seed)
    hw = int(PW / H)
    nl = NL
    md = max(1, round(MAX_D_PHYS / H))
    pos: list[tuple[float, float, float]] = []
    adj: dict[int, list[int]] = {}
    nmap: dict[tuple[int, int, int], int] = {}
    layers: list[list[int]] = []

    pos.append((0.0, 0.0, 0.0))
    nmap[(0, 0, 0)] = 0
    layers.append([0])

    for layer in range(1, nl):
        x = layer * H
        nodes: list[int] = []
        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                if layer == 1:
                    y = iy * H
                    z = iz * H
                else:
                    prev = nmap.get((layer - 1, iy, iz))
                    if prev is None:
                        continue
                    _, py, pz = pos[prev]
                    y = py + rng.gauss(0, drift * H)
                    z = pz + rng.gauss(0, drift * H)
                    y = y * (1 - restore) + (iy * H) * restore
                    z = z * (1 - restore) + (iz * H) * restore
                idx = len(pos)
                pos.append((x, y, z))
                nmap[(layer, iy, iz)] = idx
                nodes.append(idx)
        layers.append(nodes)

        for iy in range(-hw, hw + 1):
            for iz in range(-hw, hw + 1):
                si = nmap.get((layer - 1, iy, iz))
                if si is None:
                    continue
                edges: list[int] = []
                for dy in range(-md, md + 1):
                    for dz in range(-md, md + 1):
                        di = nmap.get((layer, iy + dy, iz + dz))
                        if di is not None:
                            edges.append(di)
                adj[si] = adj.get(si, []) + edges

    return pos, adj, layers


def propagate(pos, adj, blocked):
    n = len(pos)
    order = sorted(range(n), key=lambda i: pos[i][0])
    amps = [0j] * n
    amps[0] = 1.0
    hm = H * H
    for i in order:
        if abs(amps[i]) < 1e-30 or i in blocked:
            continue
        for j in adj.get(i, []):
            if j in blocked:
                continue
            dx = pos[j][0] - pos[i][0]
            dy = pos[j][1] - pos[i][1]
            dz = pos[j][2] - pos[i][2]
            L = math.sqrt(dx * dx + dy * dy + dz * dz)
            if L < 1e-10:
                continue
            act = L
            theta = math.atan2(math.sqrt(dy * dy + dz * dz), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            amps[j] += amps[i] * cmath.exp(1j * K * act) * w * hm / (L * L)
    return amps


def setup_slits(pos, layers):
    bl = NL // 3
    barrier = layers[bl]
    sa = [i for i in barrier if pos[i][1] >= 0.5]
    sb = [i for i in barrier if pos[i][1] <= -0.5]
    blocked = set(barrier) - set(sa + sb)
    return barrier, sa, sb, blocked, bl


def born_measure(pos, adj, barrier, det):
    upper = sorted([i for i in barrier if pos[i][1] > 1.0], key=lambda i: pos[i][1])
    lower = sorted([i for i in barrier if pos[i][1] < -1.0], key=lambda i: -pos[i][1])
    middle = sorted(
        [i for i in barrier if abs(pos[i][1]) <= 1.0 and abs(pos[i][2]) <= 1.0],
        key=lambda i: abs(pos[i][1]) + abs(pos[i][2]),
    )
    if not upper or not lower or not middle:
        return float("nan")
    s_a = [upper[0]]
    s_b = [lower[0]]
    s_c = [middle[0]]
    all_s = set(s_a + s_b + s_c)
    other = set(barrier) - all_s
    probs = {}
    for key, open_set in [
        ("abc", all_s),
        ("ab", set(s_a + s_b)),
        ("ac", set(s_a + s_c)),
        ("bc", set(s_b + s_c)),
        ("a", set(s_a)),
        ("b", set(s_b)),
        ("c", set(s_c)),
    ]:
        blocked = other | (all_s - open_set)
        amps = propagate(pos, adj, blocked)
        probs[key] = [abs(amps[d]) ** 2 for d in det]
    i3_sum = 0.0
    p_sum = 0.0
    for di in range(len(det)):
        i3 = (
            probs["abc"][di]
            - probs["ab"][di]
            - probs["ac"][di]
            - probs["bc"][di]
            + probs["a"][di]
            + probs["b"][di]
            + probs["c"][di]
        )
        i3_sum += abs(i3)
        p_sum += probs["abc"][di]
    return i3_sum / p_sum if p_sum > 1e-30 else float("nan")


def measure_row(label: str, drift: float, restore: float) -> JointRow:
    born_vals = []
    dtv_vals = []
    mi_vals = []
    decoh_vals = []

    for seed in SEEDS:
        pos, adj, layers = grow(drift, restore, seed)
        det = layers[-1]
        barrier, sa, sb, blocked, bl = setup_slits(pos, layers)

        born_vals.append(born_measure(pos, adj, barrier, det))

        pa = propagate(pos, adj, blocked | set(sb))
        pb = propagate(pos, adj, blocked | set(sa))

        da = [abs(pa[d]) ** 2 for d in det]
        db = [abs(pb[d]) ** 2 for d in det]
        na = sum(da)
        nb = sum(db)
        if na > 1e-30 and nb > 1e-30:
            dtv = 0.5 * sum(abs(a / na - b / nb) for a, b in zip(da, db))
            dtv_vals.append(dtv)

        bw = 2 * (PW + 1) / N_YBINS
        ed = max(1, round(NL / 6))
        st = bl + 1
        sp = min(NL - 1, st + ed)
        mid = []
        for layer in range(st, sp):
            mid.extend(layers[layer])
        ba = [0j] * N_YBINS
        bb = [0j] * N_YBINS
        for m in mid:
            b2 = max(0, min(N_YBINS - 1, int((pos[m][1] + PW + 1) / bw)))
            ba[b2] += pa[m]
            bb[b2] += pb[m]
        s_overlap = sum(abs(a - b) ** 2 for a, b in zip(ba, bb))
        na3 = sum(abs(a) ** 2 for a in ba)
        nb3 = sum(abs(b) ** 2 for b in bb)
        sn = s_overlap / (na3 + nb3) if (na3 + nb3) > 0 else 0.0
        dcl = math.exp(-LAM**2 * sn)

        rho = {}
        for d1 in det:
            for d2 in det:
                rho[(d1, d2)] = (
                    pa[d1].conjugate() * pa[d2]
                    + pb[d1].conjugate() * pb[d2]
                    + dcl * pa[d1].conjugate() * pb[d2]
                    + dcl * pb[d1].conjugate() * pa[d2]
                )
        tr = sum(rho[(d, d)] for d in det).real
        pur = 1.0
        if tr > 1e-30:
            for key in rho:
                rho[key] /= tr
            pur = float(sum(abs(v) ** 2 for v in rho.values()).real)
        decoh_vals.append(100 * (1 - pur))

        prob_a = [0.0] * N_YBINS
        prob_b = [0.0] * N_YBINS
        for d in det:
            b2 = max(0, min(N_YBINS - 1, int((pos[d][1] + PW + 1) / bw)))
            prob_a[b2] += abs(pa[d]) ** 2
            prob_b[b2] += abs(pb[d]) ** 2
        na_prob = sum(prob_a)
        nb_prob = sum(prob_b)
        mi = 0.0
        if na_prob > 1e-30 and nb_prob > 1e-30:
            pa_n = [v / na_prob for v in prob_a]
            pb_n = [v / nb_prob for v in prob_b]
            h_val = 0.0
            hc = 0.0
            for b2 in range(N_YBINS):
                pmix = 0.5 * pa_n[b2] + 0.5 * pb_n[b2]
                if pmix > 1e-30:
                    h_val -= pmix * math.log2(pmix)
                if pa_n[b2] > 1e-30:
                    hc -= 0.5 * pa_n[b2] * math.log2(pa_n[b2])
                if pb_n[b2] > 1e-30:
                    hc -= 0.5 * pb_n[b2] * math.log2(pb_n[b2])
            mi = h_val - hc
        mi_vals.append(mi)

    return JointRow(
        label=label,
        born=sum(born_vals) / len(born_vals),
        d_tv=sum(dtv_vals) / len(dtv_vals),
        mi=sum(mi_vals) / len(mi_vals),
        decoh=sum(decoh_vals) / len(decoh_vals),
    )


def _computed_rows() -> list[JointRow]:
    return [measure_row(label, drift, restore) for label, drift, restore in ROWS]


def _row_passes_ranges(row: JointRow) -> bool:
    return (
        0.0 <= row.born < 3e-15
        and 0.0 <= row.d_tv <= 1.0
        and 0.0 <= row.mi <= 1.0
        and 0.0 <= row.decoh <= 100.0
    )


def _row_spec_payload() -> list[dict[str, float | str]]:
    return [
        {"label": label, "drift": drift, "restore": restore}
        for label, drift, restore in ROWS
    ]


def _certificate_metadata() -> dict[str, object]:
    return {
        "certificate": "gate_b_no_restore_recompute_certificate_2026_06_07",
        "generated_by": "scripts/gate_b_no_restore_joint_package.py --recompute --write-certificate",
        "claim_id": "gate_b_no_restore_joint_package_note",
        "h": H,
        "k": K,
        "beta": BETA,
        "nl": NL,
        "pw": PW,
        "max_d_phys": MAX_D_PHYS,
        "lambda": LAM,
        "n_ybins": N_YBINS,
        "seeds": SEEDS,
        "rows_spec": _row_spec_payload(),
        "frozen_log_tolerances": {
            "born": BORN_TOL,
            "d_tv": METRIC_TOL,
            "mi": METRIC_TOL,
            "decoh": DECOH_TOL,
        },
    }


def _certificate_payload(rows: list[JointRow]) -> dict[str, object]:
    return {**_certificate_metadata(), "rows": [row.as_dict() for row in rows]}


def _write_recompute_certificate(rows: list[JointRow]) -> Path:
    payload = _certificate_payload(rows)
    RECOMPUTE_CERT.parent.mkdir(parents=True, exist_ok=True)
    RECOMPUTE_CERT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return RECOMPUTE_CERT


def _load_recompute_certificate(failures: list[str]) -> dict[str, JointRow]:
    if not RECOMPUTE_CERT.exists():
        failures.append(f"missing recompute certificate: {RECOMPUTE_CERT.relative_to(REPO_ROOT)}")
        return {}
    try:
        payload = json.loads(RECOMPUTE_CERT.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        failures.append(f"bad recompute certificate json: {exc}")
        return {}
    for key, expected in _certificate_metadata().items():
        actual = payload.get(key)
        if actual != expected:
            failures.append(f"recompute certificate metadata mismatch for {key}: {actual!r}")
    rows_raw = payload.get("rows")
    if not isinstance(rows_raw, list):
        failures.append("recompute certificate has no rows list")
        return {}
    if not rows_raw:
        failures.append("recompute certificate rows list is empty")
        return {}
    rows: dict[str, JointRow] = {}
    for raw in rows_raw:
        try:
            row = JointRow(
                label=str(raw["label"]),
                born=float(raw["born"]),
                d_tv=float(raw["d_tv"]),
                mi=float(raw["mi"]),
                decoh=float(raw["decoh"]),
            )
        except (KeyError, TypeError, ValueError) as exc:
            failures.append(f"bad recompute row: {exc}")
            continue
        rows[row.label] = row
    return rows


def _compare_frozen_to_recompute(
    frozen_rows: dict[str, JointRow],
    recompute_rows: dict[str, JointRow],
    expected_labels: list[str],
    failures: list[str],
) -> None:
    if list(recompute_rows.keys()) != expected_labels:
        failures.append(f"recompute row labels mismatch: {list(recompute_rows.keys())}")
        return
    exact = recompute_rows.get("exact grid")
    no_restore_zero = recompute_rows.get("no restore drift=0.0")
    if exact and no_restore_zero:
        for attr in ("born", "d_tv", "mi", "decoh"):
            if not math.isclose(getattr(exact, attr), getattr(no_restore_zero, attr), rel_tol=0.0, abs_tol=1e-12):
                failures.append(f"recompute exact grid and drift=0.0 differ on {attr}")
    for label in expected_labels:
        frozen = frozen_rows.get(label)
        recompute = recompute_rows.get(label)
        if frozen is None or recompute is None:
            continue
        if not _row_passes_ranges(recompute):
            failures.append(f"{label} recompute row outside bounded ranges")
        comparisons = (
            ("born", BORN_TOL),
            ("d_tv", METRIC_TOL),
            ("mi", METRIC_TOL),
            ("decoh", DECOH_TOL),
        )
        for attr, tol in comparisons:
            delta = abs(getattr(frozen, attr) - getattr(recompute, attr))
            if delta > tol:
                failures.append(f"{label} frozen {attr} differs from recompute by {delta:.3e}")


def run_full_replay(write_certificate: bool = False):
    t0 = time.time()
    print("=" * 76)
    print("GATE B NO-RESTORE JOINT PACKAGE HARNESS")
    print("  Born / d_TV / MI / decoherence with restore fixed to 0")
    print("=" * 76)
    print(f"h={H}, W={PW}, L={int((NL - 1) * H)}, seeds={len(SEEDS)}, LAM={LAM}")
    print("growth rule: template + drift + no restore + NN connectivity from grid labels")
    print()
    print(f"{'geometry':<20} {'Born':>10} {'d_TV':>8} {'MI':>8} {'Decoh':>8}")

    rows = _computed_rows()
    for row in rows:
        print(
            f"{row.label:<20} {row.born:>10.2e} {row.d_tv:>8.3f} "
            f"{row.mi:>8.3f} {row.decoh:>7.1f}%"
        )

    print()
    print("SAFE INTERPRETATION")
    print("  This harness isolates the no-restore lane only.")
    print("  The exact grid is the reference row; the no-restore rows show how")
    print("  much of the joint package survives without the restoring pull.")
    print("  Treat this as bounded evidence, not a full generated-geometry closure.")
    if write_certificate:
        path = _write_recompute_certificate(rows)
        print(f"RECOMPUTE_CERTIFICATE={path.relative_to(REPO_ROOT)}")
    print(f"\nTotal time: {time.time() - t0:.0f}s")


def verify_frozen_log() -> int:
    text = FROZEN_LOG.read_text(encoding="utf-8")
    rows = {
        m.group("label"): JointRow(
            label=m.group("label"),
            born=float(m.group("born")),
            d_tv=float(m.group("dtv")),
            mi=float(m.group("mi")),
            decoh=float(m.group("decoh")),
        )
        for m in ROW_RE.finditer(text)
    }

    failures: list[str] = []
    expected_labels = [label for label, _drift, _restore in ROWS]
    if "GATE B NO-RESTORE JOINT PACKAGE HARNESS" not in text:
        failures.append("missing frozen-log title")
    if list(rows.keys()) != expected_labels:
        failures.append(f"row labels mismatch: {list(rows.keys())}")
    if "Treat this as bounded evidence" not in text:
        failures.append("bounded-evidence safe interpretation missing")
    if not re.search(r"Total time:\s*\d+s", text):
        failures.append("expected frozen live replay time marker is missing")

    exact = rows.get("exact grid")
    no_restore_zero = rows.get("no restore drift=0.0")
    if exact and no_restore_zero:
        for attr in ("born", "d_tv", "mi", "decoh"):
            if not math.isclose(getattr(exact, attr), getattr(no_restore_zero, attr), rel_tol=0.0, abs_tol=1e-12):
                failures.append(f"exact grid and drift=0.0 differ on {attr}")

    for label in expected_labels:
        row = rows.get(label)
        if row is None:
            continue
        if not _row_passes_ranges(row):
            failures.append(f"{label} frozen row outside bounded replay ranges")
        if not (0.0 <= row.born < 3e-15):
            failures.append(f"{label} Born value outside bounded replay range: {row.born:.3e}")
        if not (0.0 <= row.d_tv <= 1.0):
            failures.append(f"{label} d_TV outside probability range: {row.d_tv:.3f}")
        if not (0.0 <= row.mi <= 1.0):
            failures.append(f"{label} MI outside bounded replay range: {row.mi:.3f}")
        if not (0.0 <= row.decoh <= 100.0):
            failures.append(f"{label} decoherence outside percent range: {row.decoh:.1f}")

    recompute_rows = _load_recompute_certificate(failures)
    if recompute_rows:
        _compare_frozen_to_recompute(rows, recompute_rows, expected_labels, failures)

    print("=" * 76)
    print("GATE B NO-RESTORE JOINT PACKAGE FROZEN LOG VERIFIER")
    print(f"log: {FROZEN_LOG.relative_to(REPO_ROOT)}")
    print(f"recompute certificate: {RECOMPUTE_CERT.relative_to(REPO_ROOT)}")
    print("=" * 76)
    for label in expected_labels:
        row = rows.get(label)
        if row is None:
            continue
        print(
            f"{row.label:<20} Born={row.born:.2e} d_TV={row.d_tv:.3f} "
            f"MI={row.mi:.3f} Decoh={row.decoh:.1f}% PASS"
        )
    print()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"SCORECARD PASS=0 FAIL={len(failures)}")
        return 1
    print()
    print("RECOMPUTED ROWS")
    for label in expected_labels:
        row = recompute_rows[label]
        print(
            f"{row.label:<20} Born={row.born:.4e} d_TV={row.d_tv:.6f} "
            f"MI={row.mi:.6f} Decoh={row.decoh:.6f}% PASS"
        )
    print()
    print("SAFE READ: bounded no-restore joint-package replay; drift rows remain sensitive.")
    print(f"SCORECARD PASS={len(rows) + len(recompute_rows)} FAIL=0")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--recompute",
        action="store_true",
        help="Run the original live replay instead of verifying the frozen log.",
    )
    parser.add_argument(
        "--write-certificate",
        action="store_true",
        help="With --recompute, write the completed recompute certificate used by the default verifier.",
    )
    args = parser.parse_args()
    if args.recompute:
        run_full_replay(write_certificate=args.write_certificate)
        return 0
    if args.write_certificate:
        parser.error("--write-certificate requires --recompute")
    return verify_frozen_log()


if __name__ == "__main__":
    raise SystemExit(main())
