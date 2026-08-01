#!/usr/bin/env python3
"""Cycle 865: are the record-age offsets lawful? (the demotion decider)

Cycle 864 found scheduler-cohorts nearly synchronized in record-age with
offsets 1..5. If a declared key-structure predictor EXACTLY determines the
offsets, the record-time dictionary refines and the scheduler demotes to
gauge fully; if none does, the offsets are the gauge clock's physical
residue. Supervisor-authored. bounded_theorem, authority none, audit
unset. Independent audit still required.
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


def compact(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def git_blob(b: bytes) -> str:
    return sha1(f"blob {len(b)}\0".encode() + b).hexdigest()


def source_controls():
    payloads = {p: (ROOT / p).read_bytes() for p in AUDIT_INPUT_PATHS}
    for p, b in payloads.items():
        ast.parse(b, filename=p)
    sha_rows = {p: sha256(b).hexdigest() for p, b in payloads.items()}
    blob_rows = {p: git_blob(b) for p, b in payloads.items()}
    tree = ast.parse(Path(__file__).read_text(), filename="self")
    literal = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS":
                    literal = ast.literal_eval(node.value)
    return {
        "sha256": sha_rows,
        "pass": literal == AUDIT_INPUT_PATHS
        and sha_rows == EXPECTED_SHA256 and blob_rows == EXPECTED_GIT_BLOBS,
    }


def ring_separations(positions):
    n = 11
    seps = sorted(
        min((b - a) % n, (a - b) % n)
        for i, a in enumerate(positions) for b in positions[i + 1:]
    )
    return tuple(seps)


def main() -> int:
    started = monotonic()
    controls = source_controls()
    program, event_seeds, census = C863.derive_census()
    rep = C863.replay(program, event_seeds, census)
    stations = rep["stations"]
    e2 = rep["e2_moment"]

    stamp_rung = {}
    e1_rung = {}
    for lane, key in enumerate(census):
        if key not in e2:
            continue
        events = rep["stores"]["global"][lane]
        boundary = e2[key] * stations
        if boundary in events:
            stamp_rung[key] = events.index(boundary) + 1
        elif e2[key] == 0 and events and events[0] == 0:
            stamp_rung[key] = 1
        e1_rung[key] = 1  # first event is rung 1 by construction

    cohorts = defaultdict(list)
    for key, rung in stamp_rung.items():
        cohorts[e2[key]].append((key, rung))
    rows = []
    for moment, members in sorted(cohorts.items()):
        if len(members) < 2:
            continue
        base = min(r for _k, r in members)
        for key, rung in members:
            k, event, positions = key
            lane = census.index(key)
            events = rep["stores"]["global"][lane]
            rows.append({
                "moment": moment,
                "key": key,
                "offset": rung - base,
                "predictors": {
                    "event": event,
                    "k": k,
                    "min_sep": ring_separations(positions)[0],
                    "sep_profile": ring_separations(positions),
                    "pos_sum_mod11": sum(positions) % 11,
                    "min_pos": min(positions),
                    "e1_moment": rep["e1_moment"][key],
                    "pre_stamp_events": rung - 1,
                },
            })
    cert_a = {
        "certificate": "A_OFFSET_CENSUS",
        "multi_member_cohorts": len({r["moment"] for r in rows}),
        "member_rows": len(rows),
        "offset_histogram": dict(sorted(Counter(
            r["offset"] for r in rows
        ).items())),
        "rows_compact": [
            {"moment": r["moment"], "key": r["key"], "offset": r["offset"]}
            for r in rows
        ],
    }
    cert_a["pass"] = len(rows) > 0

    predictor_names = sorted(rows[0]["predictors"]) if rows else []
    tournament = {}
    lawful = []
    for name in predictor_names:
        mapping = {}
        witness = None
        for r in rows:
            value = compact(r["predictors"][name])
            if value in mapping and mapping[value] != r["offset"]:
                witness = {"predictor_value": value,
                           "offsets": [mapping[value], r["offset"]],
                           "key": r["key"]}
                break
            mapping[value] = r["offset"]
        tournament[name] = {
            "functional": witness is None,
            "distinct_values": len(mapping),
            "witness": witness,
        }
        if witness is None:
            lawful.append(name)
    pair_lawful = []
    if not lawful:
        for i, a in enumerate(predictor_names):
            for b in predictor_names[i + 1:]:
                mapping = {}
                ok = True
                for r in rows:
                    value = compact(
                        [r["predictors"][a], r["predictors"][b]]
                    )
                    if value in mapping and mapping[value] != r["offset"]:
                        ok = False
                        break
                    mapping[value] = r["offset"]
                if ok:
                    pair_lawful.append((a, b))
    cert_b = {
        "certificate": "B_PREDICTOR_TOURNAMENT",
        "declared_predictors": predictor_names,
        "tournament": tournament,
        "single_lawful": lawful,
        "pair_lawful": pair_lawful[:6],
    }
    cert_b["pass"] = bool(predictor_names)

    if lawful:
        verdict = f"OFFSETS_LAWFUL_SINGLE:{','.join(lawful)}"
    elif pair_lawful:
        verdict = "OFFSETS_LAWFUL_PAIR:" + compact(pair_lawful[:3])
    else:
        verdict = "OFFSETS_UNEXPLAINED_AT_DECLARED_FAMILY"
    cert_c = {
        "certificate": "C_DEMOTION_VERDICT",
        "verdict": verdict,
        "meaning": (
            "lawful offsets => the record-time dictionary refines"
            " (record-age + predictor correction) and the scheduler demotes"
            " to gauge at this scope; unexplained => the offsets are the"
            " gauge clock's physical residue and demotion stays partial"
        ),
    }
    cert_c["pass"] = True

    runtime = round(monotonic() - started, 3)
    checks = {
        "A_OFFSET_CENSUS": cert_a["pass"],
        "B_PREDICTOR_TOURNAMENT": cert_b["pass"],
        "C_DEMOTION_VERDICT": cert_c["pass"],
        "D_CONTROLS": bool(
            controls["pass"] and rep["mismatches"] == 0
            and len(rep["e1_moment"]) == C863.LANDED_E1
            and len(rep["e2_moment"]) == C863.LANDED_E2
            and runtime < AUDIT_TIMEOUT_SEC
        ),
    }
    lines = ["CYCLE865_OFFSET_LAW",
             "OWNER_DIRECTED_DEMOTION_DECIDER_NO_AXIOM_SURFACE_TOUCHED"]
    for name, payload in (("A_OFFSET_CENSUS", cert_a),
                          ("B_PREDICTOR_TOURNAMENT", cert_b),
                          ("C_DEMOTION_VERDICT", cert_c)):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    summary = {"checks": checks, "cycle": 865, "runtime_seconds": runtime,
               "verdict": verdict, "pass": all(checks.values())}
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE865_OFFSET_LAW_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
