#!/usr/bin/env python3
"""Cycle 864: do the landed temporal laws live in record-time?

Owner-directed seam-closure (supervisor-run). Coordinates: a universe's
record-time = its clean-event count (the Cycle-861 ladder). Tests:

A. THE MOMENT LAW IN RECORD-AGE: scheduler-moment cohorts (keys stamping
   at the same orbit moment) — do cohort-mates share RECORD AGE (stamp
   rung)? Exact spreads; plus the record-age cohort census (both
   directions).
B. RECORD-TIME PERIODICITY: the inter-event gap sequence per key —
   eventually periodic? The record-time period law (period in events),
   on a declared sample.
C. THE TIMELESS SECTOR: laws that cannot be record-time expressed
   (never-clean worlds; the depth-0 trios; the zero-record cycles) —
   counted and stated as gauge-layer content.
D. B-AXIS CONTACT: the exact discharge condition for the
   ANOMALY_FORCES_TIME B-AXIS premise, and what A/B imply for it.

Machinery: the Cycle-863 replay substrate imported as a sha-pinned core
(the same import pattern as the 719 core). bounded_theorem, authority
none, audit unset. Independent audit still required.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import json
from pathlib import Path
import sys
from time import monotonic

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle863_time_from_records_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]: "e5c16b86bf98187d1440a56e1ce5d91c2d655ed08b5c7c65c0585bf30608fe62",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "871b9e986ca5e684ceadce25ff3e03164ef26c98",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle863_time_from_records_2026_07_28 as C863

PERIOD_SAMPLE = 48
PERIOD_MIN_EVENTS = 64


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def source_controls():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p, b in payloads.items():
        ast.parse(b, filename=p)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    self_tree = ast.parse(Path(__file__).read_text(), filename="self")
    literal = None
    for node in self_tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS":
                    literal = ast.literal_eval(node.value)
    ok = (
        literal == AUDIT_INPUT_PATHS
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and all(
            not Path(p).is_absolute() and (ROOT / p).is_file()
            for p in AUDIT_INPUT_PATHS
        )
    )
    return {"sha256": sha_rows, "git_blobs": blob_rows, "pass": ok}


def eventual_period(seq):
    """Minimal p with seq[i]==seq[i+p] for the tail half; None if none."""

    tail = seq[len(seq) // 2:]
    for p in range(1, len(tail) // 2 + 1):
        if all(tail[i] == tail[i + p] for i in range(len(tail) - p)):
            return p
    return None


def main() -> int:
    started = monotonic()
    controls = source_controls()
    program, event_seeds, census = C863.derive_census()
    rep = C863.replay(program, event_seeds, census)
    stations = rep["stations"]

    e2 = rep["e2_moment"]
    stamp_rung: dict = {}
    censored = 0
    for lane, key in enumerate(census):
        if key not in e2:
            continue
        boundary = e2[key] * stations
        events = rep["stores"]["global"][lane]
        if boundary in events:
            stamp_rung[key] = events.index(boundary) + 1
        elif e2[key] == 0 and events and events[0] == 0:
            stamp_rung[key] = 1
        else:
            censored += 1

    cohorts = defaultdict(list)
    for key, rung in stamp_rung.items():
        cohorts[e2[key]].append(rung)
    spread_hist = Counter()
    cohort_rows = []
    for moment, rungs in sorted(cohorts.items()):
        spread = max(rungs) - min(rungs)
        spread_hist[spread] += 1
        if len(rungs) > 1:
            cohort_rows.append(
                {"moment": moment, "size": len(rungs),
                 "rungs": sorted(rungs), "spread": spread}
            )
    age_cohorts = Counter(stamp_rung.values())
    multi_age = {a: c for a, c in age_cohorts.items() if c > 1}
    zero_spread = sum(
        c for s, c in spread_hist.items() if s == 0
    )
    multi_cohorts = [r for r in cohort_rows]
    surviving = all(r["spread"] == 0 for r in multi_cohorts)
    cert_a = {
        "certificate": "A_MOMENT_LAW_IN_RECORD_AGE",
        "stamped_with_rung": len(stamp_rung),
        "rung_censored": censored,
        "scheduler_cohorts_total": len(cohorts),
        "multi_member_cohorts": len(multi_cohorts),
        "within_cohort_spread_histogram": dict(sorted(spread_hist.items())),
        "multi_member_rows": multi_cohorts[:10],
        "record_age_cohort_sizes": dict(sorted(multi_age.items())),
        "verdict": (
            "MOMENT_LAW_SURVIVES_IN_RECORD_TIME" if surviving and multi_cohorts
            else "MOMENT_LAW_TRANSFORMS" if multi_cohorts
            else "NO_MULTI_MEMBER_COHORTS_AT_SCOPE"
        ),
    }
    cert_a["pass"] = len(stamp_rung) > 0

    sampled = 0
    period_rows = Counter()
    aperiodic = 0
    rates = Counter()
    for lane, key in enumerate(census):
        events = rep["stores"]["global"][lane]
        if len(events) < PERIOD_MIN_EVENTS:
            continue
        gaps = tuple(b - a for a, b in zip(events, events[1:]))
        p = eventual_period(gaps)
        if p is None:
            aperiodic += 1
        else:
            span = sum(gaps[len(gaps) // 2:len(gaps) // 2 + p])
            period_rows[(p, span)] += 1
        window = events[:min(len(events), 1024)]
        if window[-1] > 0:
            rates[round(len(window) * stations / window[-1], 2)] += 1
        sampled += 1
        if sampled >= PERIOD_SAMPLE:
            break
    cert_b = {
        "certificate": "B_RECORD_TIME_PERIODICITY",
        "declared_sample": {"lanes": sampled,
                           "min_events": PERIOD_MIN_EVENTS,
                           "cap": C863.EVENT_STORE_CAP},
        "eventually_periodic": sum(period_rows.values()),
        "aperiodic_within_store": aperiodic,
        "period_law_rows_top": [
            {"events_per_period": p, "scheduler_span": s, "keys": c}
            for (p, s), c in period_rows.most_common(8)
        ],
        "events_per_orbit_rate_top": [
            {"rate": r, "keys": c} for r, c in rates.most_common(6)
        ],
        "verdict": (
            "RECORD_TIME_PERIOD_LAW_PRESENT"
            if period_rows and aperiodic == 0
            else "MIXED" if period_rows else "NO_PERIODICITY_AT_SAMPLE"
        ),
    }
    cert_b["pass"] = sampled > 0

    never = sum(
        1 for lane, key in enumerate(census)
        if not rep["stores"]["global"][lane]
    )
    set_only = sum(
        1 for lane, key in enumerate(census)
        if rep["stores"]["global"][lane] and census[lane] not in e2
    )
    cert_c = {
        "certificate": "C_TIMELESS_SECTOR",
        "never_clean_worlds": never,
        "set_but_unstamped_worlds": set_only,
        "statement": (
            "laws about never-clean worlds (incl. the depth-0 trios and the"
            " zero-record cycles) have NO record-time expression: in the"
            " formation-is-the-tick reading these are timeless worlds and"
            " their regularities (meets, marks, state periods) are"
            " gauge-layer content by scope, not failed reductions"
        ),
    }
    cert_c["pass"] = never > 0

    cert_d = {
        "certificate": "D_B_AXIS_CONTACT",
        "premise": (
            "ANOMALY_FORCES_TIME_THEOREM B-AXIS: one supplied blocked time"
            " step, one declared evolution axis, no admitted second clock;"
            " the theorem itself states 'No step defines time via the"
            " anomaly'"
        ),
        "discharge_condition": (
            "B-AXIS discharges (premise -> derived) iff the evolution axis"
            " is CONSTITUTED by the record order: (i) the landed temporal"
            " laws restate in record-time coordinates (certificates A/B"
            " here), and (ii) the axis admits no second record-clock (the"
            " single-clock content) — condition (ii) is untested here and"
            " remains the open leg"
        ),
        "what_this_cycle_contributes": (
            "A and B are the (i)-leg evidence; C scopes the gauge remainder;"
            " the (ii)-leg needs the scaled-bank construction"
        ),
    }
    cert_d["pass"] = True

    runtime = round(monotonic() - started, 3)
    checks = {
        "A_MOMENT_LAW_IN_RECORD_AGE": cert_a["pass"],
        "B_RECORD_TIME_PERIODICITY": cert_b["pass"],
        "C_TIMELESS_SECTOR": cert_c["pass"],
        "D_B_AXIS_CONTACT": cert_d["pass"],
        "E_CONTROLS": bool(
            controls["pass"] and rep["mismatches"] == 0
            and rep["init_failures"] == 0 and runtime < AUDIT_TIMEOUT_SEC
            and len(rep["e1_moment"]) == C863.LANDED_E1
            and len(rep["e2_moment"]) == C863.LANDED_E2
        ),
    }
    lines = ["CYCLE864_LAWS_IN_RECORD_TIME",
             "OWNER_DIRECTED_SEAM_CLOSURE_NO_AXIOM_SURFACE_TOUCHED"]
    for name, payload in (("A_MOMENT_LAW_IN_RECORD_AGE", cert_a),
                          ("B_RECORD_TIME_PERIODICITY", cert_b),
                          ("C_TIMELESS_SECTOR", cert_c),
                          ("D_B_AXIS_CONTACT", cert_d)):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    summary = {"checks": checks, "cycle": 864, "runtime_seconds": runtime,
               "verdict_A": cert_a["verdict"], "verdict_B": cert_b["verdict"],
               "pass": all(checks.values())}
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE864_LAWS_IN_RECORD_TIME_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
