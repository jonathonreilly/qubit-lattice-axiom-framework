"""POST byte/provenance checks and recorded-arithmetic checks, not a science rerun.

No author module is imported or executed. No unlisted research packet is read.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from decimal import Decimal, localcontext
import json
import math

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
AUTHOR = BASE / "unrestricted-record-count-personal"
PRE_SEAL_SHA = "b6e0c33fe1286a876f1230759cb62769d57475d76c2ea1a6aae633064e2ba9d0"
AUTHOR_SEAL_SHA = "fd268c0ec9d37f68136e81e153d71c7775ac652118f8e2adcf40f8c5776b60d8"
AUTHOR_NOTE_SHA = "5ad270f81ab37e1ffb14130937228c6c67b0bdd0858362d76ea6bf5057a8d1cd"
MICRO_POST_SEAL_SHA = "73dc48a63907c5cbe3f3973723151a84af4b7d55e10959eb62f7c6b042da3545"
MICRO_NOTE = "MICROSCOPIC_FINITE_BIN_RECORD_BRIDGE_ROOT.md"


def identity(path):
    data = path.read_bytes()
    return {"sha256": sha256(data).hexdigest(), "bytes": len(data)}


def require_identity(path, expected):
    actual = identity(path)
    assert actual["sha256"] == expected["sha256"], (str(path), actual, expected)
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], (str(path), actual, expected)
    return actual


def snapshot(origin, relative, expected):
    actual = require_identity(origin, expected)
    destination = HERE / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    data = origin.read_bytes()
    assert sha256(data).hexdigest() == actual["sha256"]
    if destination.exists():
        require_identity(destination, actual)
    else:
        with destination.open("xb") as handle:
            handle.write(data)
        destination.chmod(0o444)
    return {"origin": str(origin), "snapshot": relative, **actual}


def check_seal(directory, filename, expected_hash):
    require_identity(directory / filename, {"sha256": expected_hash})
    manifest = json.loads((directory / filename).read_text())
    for member in manifest["members"]:
        require_identity(directory / member["path"], member)
    assert len(manifest["members"]) == manifest["frozen_member_count"]
    return manifest


pre = check_seal(HERE, "PRE_SEAL.json", PRE_SEAL_SHA)
require_identity(HERE / "PRE.md", {
    "sha256": "1fd58a66171c23568841d2527a2091f3992e584cbad970bdb8979a38e4c68e7e"
})
author_seal_id = require_identity(AUTHOR / "AUTHOR_SEAL.json", {"sha256": AUTHOR_SEAL_SHA})
author_seal = json.loads((AUTHOR / "AUTHOR_SEAL.json").read_text())
assert len(author_seal["files"]) == 7
assert author_seal["files"]["UNRESTRICTED_FINITE_BIN_RECORD_CONTRAST_ROOT.md"]["sha256"] == AUTHOR_NOTE_SHA
released = [snapshot(AUTHOR / "AUTHOR_SEAL.json", "post-released/AUTHOR_SEAL.json", author_seal_id)]
for name, pin in author_seal["files"].items():
    assert Path(name).name == name
    released.append(snapshot(AUTHOR / name, "post-released/" + name, pin))

pre_sources = json.loads((HERE / "SOURCE_PINS.json").read_text())["sources"]
root_sources = json.loads((AUTHOR / "SOURCE_PINS.json").read_text())
assert root_sources["main_commit"] == "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8"
micro_dir = BASE / "microscopic-record-readout-independent"
micro_post = check_seal(micro_dir, "POST_SEAL.json", MICRO_POST_SEAL_SHA)
micro_pre = check_seal(micro_dir, "PRE_SEAL.json", "34cbabad0237942680176e23a39bfdd6e9f4f34bbf56f1ff4f50b15178838f41")
micro_member = next(x for x in micro_post["members"] if x["path"] == "post-released/" + MICRO_NOTE)
prior_snapshot = snapshot(micro_dir / micro_member["path"], "post-prior-source/" + MICRO_NOTE, micro_member)
parents = []
for pin in root_sources["sources"]:
    origin = Path(pin["path"])
    require_identity(origin, pin)
    matching = [x for x in pre_sources if x["sha256"] == pin["sha256"] and x["bytes"] == pin["bytes"]]
    if matching:
        assert len(matching) == 1
        prior = matching[0]
        require_identity(HERE / prior["snapshot"], pin)
        evidence = {"snapshot": prior["snapshot"], "prior_provenance": prior}
    else:
        assert origin.name == MICRO_NOTE
        require_identity(HERE / prior_snapshot["snapshot"], pin)
        evidence = {"snapshot": prior_snapshot["snapshot"],
                    "prior_POST_seal_sha256": MICRO_POST_SEAL_SHA,
                    "prior_review": "Earlier independent microscopic-record POST, reused; not new review."}
    parents.append({"origin": str(origin), "sha256": pin["sha256"], "bytes": pin["bytes"], **evidence})
assert len(parents) == 7

execution = json.loads((AUTHOR / "EXECUTION.json").read_text())
result = json.loads((AUTHOR / "COUNT_WINDOW_RESULTS.json").read_text())
assert execution["code_sha256"] == author_seal["files"]["count_window_controls.py"]["sha256"]
assert execution["output_sha256"] == author_seal["files"]["COUNT_WINDOW_RESULTS.json"]["sha256"]
assert execution["exit_code"] == 0
assert execution["stderr_bytes"] == (AUTHOR / "COUNT_WINDOW.stderr").stat().st_size == 0
assert 0 < result["elapsed_seconds"] < execution["elapsed_seconds"]

# Check the recorded formula values independently with Decimal arithmetic.
# This reads result rows only; it is not quadrature, history re-enumeration,
# execution of the author code, or a replication of its run.
arithmetic = []
with localcontext() as context:
    context.prec = 60
    for index, row in enumerate(result["poisson_proposal_rows"]):
        h, b, j, l = (Decimal(str(row[k])) for k in ("h", "b", "r_j", "r_l"))
        lo, hi = min(h, b), max(h, b)
        overlap = lo * lo * hi - lo ** 3 / 3
        mean = j * l * h * b
        second = mean ** 2 + mean + j * l ** 2 * h * b ** 2 + j ** 2 * l * overlap
        upper = mean ** 2 + mean * (1 + (j + l) * b)
        expected = {"mean": mean, "overlap_square_exact": overlap,
                    "overlap_square_quadrature": overlap, "second_moment": second,
                    "proposed_second_bound": upper, "variance": second - mean ** 2,
                    "bernoulli_variance_formula": mean * (1 - mean)}
        discrepancies = {}
        for key, value in expected.items():
            relative = abs(Decimal(str(row[key])) - value) / max(abs(value), Decimal(1))
            assert relative < Decimal("2e-14"), (index, key, relative)
            discrepancies[key] = float(relative)
        assert second <= upper
        arithmetic.append({"row": index, "h": float(h), "b": float(b),
                           "r_j": float(j), "r_l": float(l),
                           "max_scaled_recorded_formula_discrepancy": max(discrepancies.values()),
                           "second_bound_holds_in_decimal_arithmetic": True})
assert len(arithmetic) == 12
assert sum(r["bernoulli_variance_formula"] < 0 for r in result["poisson_proposal_rows"]) == 5

register = result["finite_history_register"]
assert register["event_cap"] == 6 and register["universal_pair_cap"] == 15
assert register["nested_partition_histories"] == sum(math.comb(10, n) for n in range(7)) == 848
assert [r["bins"] for r in register["rows"]] == [4, 8, 16, 32]
assert [r["aggregate_bracket_gap"] for r in register["rows"]] == [856, 445, 251, 218]
assert [r["aggregate_square_bracket_gap"] for r in register["rows"]] == [1446, 553, 299, 266]
assert [r["exact_brackets"] for r in register["rows"]] == [227, 448, 617, 644]
for row in register["rows"]:
    assert row["histories_checked"] == 848 and row["maximum_actual_count"] == 2
    example = row["multiple_count_example"]
    assert example["actual"] == 2 and example["lower"] <= 2 <= example["upper"]
assert len(result["checks_passed"]) == 6

# Recheck mutable origins after taking the snapshots and interpreting records.
for pin in released + parents:
    require_identity(Path(pin["origin"]), pin)
check_seal(HERE, "PRE_SEAL.json", PRE_SEAL_SHA)

pins = {
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "phase": "Bounded released-source unrestricted-count POST",
    "unchanged_PRE_seal_sha256": PRE_SEAL_SHA,
    "unchanged_PRE_members": len(pre["members"]),
    "author_seal_sha256": AUTHOR_SEAL_SHA,
    "released_sources": released,
    "reused_prior_source": prior_snapshot,
    "author_dependency_pins_matched_to_prior_evidence": parents,
    "review_scope": "Complete author note/code/output and provenance, conditional on the pinned parent LR and prepared-state estimates. No author execution or unrelated packet read."
}
with (HERE / "POST_SOURCE_PINS.json").open("x") as handle:
    json.dump(pins, handle, indent=2)
    handle.write("\n")
report = {
    "scope": "Independent byte/provenance and recorded arithmetic verification, not an author numerical rerun or a physical simulation.",
    "PRE_seal_and_all_members_unchanged": True,
    "PRE_member_count": len(pre["members"]),
    "prior_microscopic_PRE_POST_unchanged": {"PRE_members": len(micro_pre["members"]), "POST_members": len(micro_post["members"])},
    "released_author_seal_sha256": AUTHOR_SEAL_SHA,
    "released_author_members_verified": len(author_seal["files"]),
    "released_snapshots_including_seal": len(released),
    "all_seven_author_dependency_origins_match_prior_pinned_evidence": True,
    "dependency_source_identity_count": len(parents),
    "author_execution_record": execution,
    "author_result_internal_seconds": result["elapsed_seconds"],
    "binding_limits": "The result has no embedded code/source fingerprint. The frozen external EXECUTION.json and AUTHOR_SEAL.json bind the script and recorded output. This checker did not witness or rerun the author computation; no separate stdout file is claimed.",
    "recorded_formula_arithmetic": arithmetic,
    "register_record_summaries": register,
    "register_histories_reenumerated_by_POST": False,
    "author_module_imported_or_executed": False,
    "new_science_simulations_in_POST": 0,
    "other_active_independent_packets_read": False,
    "author_sources_rechecked_after_snapshotting": True,
    "POST_source_pins": identity(HERE / "POST_SOURCE_PINS.json"),
    "all_binding_checks_passed": True
}
print(json.dumps(report, indent=2, allow_nan=False))
