#!/usr/bin/env python3
"""Authenticate immutable PRE and comparison evidence, then seal the packet.

This bookkeeping script does not rerun scientific controls or alter any source.
The final seal binds every regular file in this owned directory except itself.
"""
from pathlib import Path
import datetime
import hashlib
import json

HERE = Path(__file__).resolve().parent
FINAL = HERE / "FINAL_SEAL.json"
PRE_HASH = "d015c9245087ce39c102c61d859171c58ccd5b4a2ea4d25ea2b9bc37a61493ad"
AUTHOR_HASH = "dcff32f98d26b2cddfdcfa8feeb4dc8907b9174f54f0b51f3ec0cda0a9fa6c4e"
NOTE_HASH = "bf11561362dfd8d4f0298be946efa9ec8c8e198a0f3b2b01e4b811537120ff5f"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((HERE / name).read_text())


def verify_file(path, digest, size=None):
    path = HERE / path
    assert path.is_file() and not path.is_symlink(), str(path)
    assert sha(path) == digest, str(path)
    if size is not None:
        assert path.stat().st_size == size, str(path)


assert not FINAL.exists(), "Refuse to overwrite an existing frozen final seal"
verify_file("PRE_SEAL.json", PRE_HASH)
pre = read("PRE_SEAL.json")
assert len(pre["files"]) == 38
for item in pre["files"]:
    verify_file(item["path"], item["sha256"], item["bytes"])

bindings = read("COMPARISON_SOURCE_BINDINGS.json")
assert bindings["PRE_seal_sha256"] == PRE_HASH
assert bindings["released_author_seal_sha256"] == AUTHOR_HASH
assert len(bindings["sources"]) == 30
for item in bindings["sources"]:
    verify_file(item["snapshot_path"], item["sha256"], item["bytes"])
verify_file("comparison_sources/autonomous_clock_author/AUTHOR_SEAL.json", AUTHOR_HASH)
verify_file(
    "comparison_sources/autonomous_clock_author/"
    "AUTONOMOUS_FINITE_CLOCK_FOR_THE_ORIGINAL_REDUCED_DYNAMICS.md",
    NOTE_HASH,
)

receipt = read("COMPARISON_EXECUTION_RECEIPT.json")
assert receipt["PRE_seal_sha256"] == PRE_HASH
assert receipt["PRE_bytes_unchanged"]
assert receipt["PRE_files_authenticated_before"] == 38
assert receipt["PRE_files_authenticated_after"] == 38
assert receipt["comparison_source_bindings_sha256"] == sha(HERE / "COMPARISON_SOURCE_BINDINGS.json")
assert receipt["author_replay_result_and_stdout_byte_identical"]
assert not receipt["unresolved_execution_failures"]
assert len(receipt["runs"]) == 4
for run in receipt["runs"]:
    assert run["exit_code"] == 0
    for kind in ("script", "stdout", "stderr"):
        verify_file(run[kind], run[kind + "_sha256"])
    assert (HERE / run["stderr"]).stat().st_size == 0
for item in receipt["author_runtime_copies"]:
    verify_file(item["snapshot"], item["sha256"])
    verify_file(item["runtime"], item["sha256"])

for name, replay in (
    ("CLOCK_CONTROL_RESULTS.json", "author_clock_replay.stdout"),
    ("ORIGINAL_STAR_CLOCK_RESULTS.json", "author_original_star_replay.stdout"),
):
    expected = (HERE / "comparison_sources/autonomous_clock_author" / name).read_bytes()
    assert (HERE / "comparison_runtime/author/autonomous_clock_author" / name).read_bytes() == expected
    assert (HERE / replay).read_bytes() == expected

changes = read("REPORTING_CORRECTION_CHECK.json")["changes"]
assert sum(len(rows) for rows in changes.values()) == 30
for rows in changes.values():
    for row in rows:
        assert row["old"] == 0 and row["new"] > 0

star = read("TRAVELING_PROGRAM_AND_STAR_RESULTS.json")["original_star_comparison"]
assert star["max_author_field_difference"] < 2e-8

all_paths = sorted(path for path in HERE.rglob("*") if path.is_file())
assert not any("__pycache__" in path.parts for path in all_paths)
assert not any(path.is_symlink() for path in all_paths)
assert not any(path.is_file() for path in (HERE / "comparison_runtime/tmp").rglob("*"))
files = [
    {"path": str(path.relative_to(HERE)), "bytes": path.stat().st_size, "sha256": sha(path)}
    for path in all_paths
]

seal = {
    "stage": "complete bounded post-PRE source comparison",
    "sealed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "PRE_seal_sha256": PRE_HASH,
    "PRE_files_authenticated_unchanged": 38,
    "released_author_note_sha256": NOTE_HASH,
    "released_author_seal_sha256": AUTHOR_HASH,
    "comparison_source_count": len(bindings["sources"]),
    "comparison_source_bindings_sha256": sha(HERE / "COMPARISON_SOURCE_BINDINGS.json"),
    "comparison_note_sha256": sha(HERE / "COMPARISON.md"),
    "comparison_execution_receipt_sha256": sha(HERE / "COMPARISON_EXECUTION_RECEIPT.json"),
    "scope_supported": [
        "The released traveling finite-clock conditional theorem is supported at its stated uniform physical-time, all-reference one-time reduced-channel scope on [0,T].",
        "Independent endpoint operator action reconstructs the nonzero velocity variance; clipping and finite-chain truncation estimates are valid.",
        "The root system-only counterphase and the independent PRE full-Q convention preserve the original H once; they give identical system/reference one-time channels for a common clock/grid.",
        "Finite positive clock/program Hamiltonian, exact conservation of system-plus-battery free energy, coherent preparation, pure flags, interaction norm and resource costs are accounted for.",
        "The root O(C^5) sufficient clock resource sequence and the distinct PRE O(C^10) spin-clock sequence remain separately attributed conditional constructions.",
        "Twenty original-star rows at the released lambda=0 dressed input and both instruments agree with new calculations from prior independent local matrices to less than 1.51e-12.",
    ],
    "premise_boundaries": [
        "The previously sealed finite-battery/collision theorem is a supplied mathematical premise; this packet does not independently re-prove its entire construction.",
        "General input/reference guarantees come from the analytic isometry/mixture proof, not the stationary-input star numerical shortcut.",
        "The leading star energy limit uses the separately identified prior independent uniform Duhamel derivation.",
        "Author script replay is consistency evidence and is never labeled an independent reconstruction.",
    ],
    "excluded_claims": [
        "Initial reduced-generator, dissipative-power or derivative convergence: every fixed finite specified preparation starts with A and zero system power, generally unlike A+D.",
        "An exact terminal full-prefix instrument for the traveling packet; its terminal state is a clipped-prefix mixture. The PRE spin-clock endpoint statement is distinct.",
        "Exact unbinned event-time instruments, arbitrary-intervention process tensors, uniform normalized rare-record guarantees or permanent irreversible memory.",
        "A fixed-resource all-time reservoir, autonomous thermodynamic lifecycle or reset cost theorem, local/bounded-strength/optimal/robust physical implementation.",
        "A native law, parameter selection, universal no-go, empirical prediction, formal retained status, audit verdict, publication approval or landing decision.",
    ],
    "required_mathematical_corrections": [],
    "scientific_discrepancies": [],
    "limitations_to_retain": [
        "Uniform channel and energy-function convergence need not imply derivative or initial-power convergence; a shrinking small-time boundary layer is allowed.",
        "The finite path commutator [K_M,V_M] is a nonzero endpoint term; exact X(t)=X+tV is used only in the infinite comparison problem.",
        "Both resource upper estimates are sufficient, not optimal; a resource estimate uniform in lambda does not select one fixed bath for all lambda.",
    ],
    "retained_failures_and_repairs": [
        "Immutable PRE retains failed equal-duration nonlinear-clock timing and omitted-counterphase routes, plus endpoint-only and multitime limitations.",
        "The root historical floating underflow changed 30 displayed finite-boundary fields from zero to a conservative positive float floor; exact positive high-precision bounds and unchanged other outputs are preserved.",
    ],
    "unresolved_execution_failures": [],
    "publication_provenance": "This private inventory retains historical instruction snapshots and source metadata. A later public projection may omit instruction/third-party provenance only with its own explicit omission manifest; no public projection is made here.",
    "files": files,
}
FINAL.write_text(json.dumps(seal, indent=2) + "\n")
for item in files:
    verify_file(item["path"], item["sha256"], item["bytes"])
assert len(list(path for path in HERE.rglob("*") if path.is_file())) == len(files) + 1
print(json.dumps({
    "final_seal_sha256": sha(FINAL),
    "comparison_note_sha256": seal["comparison_note_sha256"],
    "bound_files": len(files),
    "PRE_files_unchanged": 38,
    "comparison_sources": len(bindings["sources"]),
    "independent_controls": 2,
    "author_consistency_replays": 2,
    "required_mathematical_corrections": [],
}, indent=2))
