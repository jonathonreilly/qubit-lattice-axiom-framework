#!/usr/bin/env python3
"""Cycle-913 finite non-functionality lemma and recorded selection-table
arithmetic (self-contained).

REVISED (review loop iteration 1, Sol reviewer, 2026-08-08).  The original
runner consumed the unlanded Cycle-863/878/911 substrate stack, and its
strongest conclusions -- "the actual-selection question (historical
shorthand O2) is SUPPLIED, not derivable, on this substrate", "the
occurrence-weight question (historical shorthand O3) is TERMINAL / has no
non-forbidden realization", and a cross-setup weight being an operation the
realized-state primitive "forbids verbatim" -- were review-refuted: the
realized-state primitive supplies pointwise evaluation and supplies no
measure, but it does not FORBID a separately derived or explicitly imported
ensemble/setup measure; and a finite fingerprint collision table shows
non-membership in one declared rule class, not global underivability.  The
original certificate carrying that ledger was also forced green
(`cert_c6["pass"] = True`).  All of those claims are WITHDRAWN.

This revised runner is SELF-CONTAINED and certifies only:

L1  CONSISTENCY ARITHMETIC on the stipulated recorded selection table
    (84 + 80 = 164; 328 = 164 x 2; the record-free subpopulation split
    51 + 16 = 67 <= 164; the collision class 15 + 15 = 30).

L2  FINITE NON-FUNCTIONALITY LEMMA (exact, with planted controls): a
    finite observation table containing two rows with identical
    fingerprint and different outcome is not a function of that
    fingerprint.  Applied to the stipulated abstract witness rows of the
    recorded collision class; a planted functional table is confirmed
    functional (tooth).  Scope: the recorded fingerprint classes only --
    NOT a statement that any selection rule is underivable.

L3  RECORDED-VALUE ECHO: the recorded compile-level fact "endpoint wires
    are gate inputs and never gate targets (0 of 34,166 gates)" and the
    recorded quadruple-readout agreement are STIPULATED history from the
    unlanded substrate; only their internal arithmetic is checked here.

Fail-closed: every certificate binds `pass` to the predicate it names.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000

from hashlib import sha256
import json
from pathlib import Path
import random
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# STIPULATED recorded values (provenance context, non-load-bearing: recorded
# by the unlanded full-checkout computation; stipulated here as a table, not
# asserted as certified facts about any landed substrate).
# ---------------------------------------------------------------------------
RECORDED = {
    "lock_points": 164,
    "realized_left_right": [84, 80],
    "menu_size": 2,
    "site_possibility_pairs": 328,
    "record_free_lock_points": 67,
    "record_free_split": [51, 16],
    "largest_neighbour_collision_class": 30,
    "collision_class_split": [15, 15],
    "compiled_gates": 34166,
    "gates_targeting_endpoint_wires": 0,
}

# abstract witness rows for the recorded collision class: identical
# fingerprint, differing outcome (the recorded worlds 95 / 51 witness pair,
# abstracted to its logical content)
WITNESS_ROWS = [
    {"fingerprint": "shared-neighbour-context", "outcome": "left"},
    {"fingerprint": "shared-neighbour-context", "outcome": "right"},
]
PLANTED_FUNCTIONAL_ROWS = [
    {"fingerprint": "ctx-a", "outcome": "left"},
    {"fingerprint": "ctx-a", "outcome": "left"},
    {"fingerprint": "ctx-b", "outcome": "right"},
]

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def is_function_of(rows: list[dict]) -> bool:
    seen: dict[str, str] = {}
    for r in rows:
        if r["fingerprint"] in seen and seen[r["fingerprint"]] != r["outcome"]:
            return False
        seen[r["fingerprint"]] = r["outcome"]
    return True


def l1_consistency() -> dict:
    r = RECORDED
    ok = (sum(r["realized_left_right"]) == r["lock_points"]
          and r["site_possibility_pairs"]
          == r["lock_points"] * r["menu_size"]
          and sum(r["record_free_split"]) == r["record_free_lock_points"]
          and r["record_free_lock_points"] <= r["lock_points"]
          and sum(r["collision_class_split"])
          == r["largest_neighbour_collision_class"]
          and 0 <= r["gates_targeting_endpoint_wires"]
          <= r["compiled_gates"])
    check("L1_CONSISTENCY_ARITHMETIC", ok,
          f"84+80={sum(r['realized_left_right'])} "
          f"164*2={r['lock_points'] * r['menu_size']} "
          f"51+16={sum(r['record_free_split'])} "
          f"15+15={sum(r['collision_class_split'])}")
    return {"all_sums_consistent": ok}


def l2_nonfunctionality(rng: random.Random) -> dict:
    witness_not_function = not is_function_of(WITNESS_ROWS)
    planted_is_function = is_function_of(PLANTED_FUNCTIONAL_ROWS)
    # randomized soundness sweep of the decision procedure itself: build
    # random tables from random maps (always functional) and random tables
    # with one planted collision (never functional)
    trials, wrong = 600, 0
    for _ in range(trials):
        n = rng.randint(1, 12)
        mapping = {f"f{i}": rng.choice(["left", "right"]) for i in range(n)}
        rows = [{"fingerprint": k, "outcome": v}
                for k, v in mapping.items() for _ in range(rng.randint(1, 3))]
        if not is_function_of(rows):
            wrong += 1
        key = rng.choice(sorted(mapping))
        broken = rows + [{"fingerprint": key,
                          "outcome": ("right" if mapping[key] == "left"
                                      else "left")}]
        if is_function_of(broken):
            wrong += 1
    ok = witness_not_function and planted_is_function and wrong == 0
    check("L2_NONFUNCTIONALITY_LEMMA", ok,
          f"witness_rows_not_a_function={witness_not_function} "
          f"planted_functional_detected={planted_is_function} "
          f"soundness_trials={trials} errors={wrong}")
    return {"witness_not_function": witness_not_function,
            "soundness_trials": trials, "errors": wrong,
            "scope": "the recorded fingerprint classes only; NOT a "
                     "derivability claim"}


def l3_recorded_echo() -> dict:
    r = RECORDED
    frac_ok = (r["gates_targeting_endpoint_wires"] == 0
               and r["compiled_gates"] == 34166)
    check("L3_RECORDED_VALUE_ECHO", frac_ok,
          f"recorded reads-never-writes ratio "
          f"{r['gates_targeting_endpoint_wires']}/{r['compiled_gates']} "
          f"(STIPULATED history; certifies nothing about a landed substrate)")
    return {"recorded_ratio": [r["gates_targeting_endpoint_wires"],
                               r["compiled_gates"]]}


def run_all(seed: int) -> dict:
    rng = random.Random(seed)
    a = l1_consistency()
    b = l2_nonfunctionality(rng)
    c = l3_recorded_echo()
    return {"l1": a, "l2": b, "l3": c,
            "science_digest": digest([a, b, c, RECORDED, WITNESS_ROWS])}


def main() -> int:
    t0 = monotonic()
    first = run_all(913)
    saved = list(CERTS)
    CERTS.clear()
    second = run_all(913)
    CERTS.clear()
    CERTS.extend(saved)
    det = first["science_digest"] == second["science_digest"]
    check("L4_DETERMINISM", det, f"double_run_digest_equal={det}")
    elapsed = monotonic() - t0
    check("L5_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 913 -- FINITE NON-FUNCTIONALITY LEMMA AND RECORDED-TABLE "
      "ARITHMETIC")
    w("=" * 78)
    w("")
    w("SCOPE: self-contained.  The unlanded substrate closure is removed.")
    w("No terminality claim, no derivability denial, and no prohibition")
    w("claim is made; the realized-state primitive supplies no measure but")
    w("does not forbid a separately derived or explicitly imported one.")
    w("")
    w("-- stipulated recorded table --------------------------------------------")
    for k, v in RECORDED.items():
        w(f"  {k}: {v}")
    w("")
    w("CLAIMS_JSON: " + compact({
        "lock_points": RECORDED["lock_points"],
        "realized_split": RECORDED["realized_left_right"],
        "site_possibility_pairs": RECORDED["site_possibility_pairs"],
        "witness_not_function": first["l2"]["witness_not_function"],
        "soundness_errors": first["l2"]["errors"],
        "recorded_ratio": first["l3"]["recorded_ratio"],
        "science_digest": first["science_digest"],
    }))
    w("")
    w("-- CERTIFICATES --------------------------------------------------------")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<32} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    w(f"VERDICT: {'PASS' if nfail == 0 else 'FAIL'}")
    text = "\n".join(out)
    sys.stdout.write(text + "\n")

    receipt = {
        "cycle": 913,
        "claim_type": "bounded_theorem",
        "headline": ("finite non-functionality lemma with planted controls, "
                     "plus consistency arithmetic on the stipulated recorded "
                     "selection table.  Non-membership in the recorded "
                     "fingerprint rule class only; no underivability, "
                     "terminality, or prohibition claim"),
        "stipulated_scope_inputs": {"recorded_table": RECORDED,
                                    "witness_rows": WITNESS_ROWS},
        "provenance_context_non_load_bearing": (
            "the recorded table comes from the unlanded Cycle-863/878/911 "
            "substrate computation; it is stipulated history and certifies "
            "nothing about any landed substrate"),
        "open_bridges": [
            "whether any lawful dynamics derives the recorded selection "
            "(history-dependent, time-dependent, site-internal, composite "
            "and separately-supplied rules are all unexcluded)",
            "any ensemble/setup measure (underived here; not forbidden by "
            "the realized-state primitive, which merely does not supply "
            "one)",
        ],
        "results": first,
        "certificates": {n: {"pass": ok, "detail": d} for n, ok, d in CERTS},
        "all_certificates_pass": nfail == 0,
        "review_loop": {
            "iteration": 1,
            "disposition": "FIX_THEN_PROCEED",
            "reviewer": "Sol",
            "date": "2026-08-08",
            "fix": ("self-contained rewrite: unlanded closure removed; "
                    "terminality/prohibition claims withdrawn; the forced-"
                    "green verdict certificate replaced by fail-closed "
                    "predicates"),
        },
        "science_digest": first["science_digest"],
    }
    (ROOT / "outputs" /
     "selection_function_cycle913_receipt_2026_07_28.json").write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
