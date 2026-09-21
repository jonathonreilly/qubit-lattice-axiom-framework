#!/usr/bin/env python3
"""Verify the four narrow prose fixes by reconstructing the frozen source hash."""
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE = "docs/MOBILE_RECORDS_EMPTY_START_MOTION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-21.md"
RUNNER = "scripts/mobile_records_empty_start_motion_response_2026_09_21.py"
INITIAL = "693f13683a377cbc81587122f0d4568458736c5901dfd9a0503806ff1486c890"
CORRECTED = "a8e9d26399a8c810a7bb919edaaa9e9a5554f18139e601c790c2b23c24177a74"
RUNNER_HASH = "56aeb1083d9a66a5dba5ad68b625f539e67fbd9fa458e835ca4fae60ee697156"
fixes = [
    ("Fourier formula on the stated L>=6 family",
     "On a periodic cubic graph, for Fourier mode k this is\n",
     "On the above cubic family with side L>=6, for Fourier mode k this is\n"),
    ("Common vector eigenvalue is an explicit hypothesis",
     "coefficient. Positive theta thus creates nearest-neighbor correlations from\n",
     "coefficient when all three content-coordinate functions are eigenfunctions\n"
     "of W with the same theta, in particular for the j-family with theta=2j.\n"
     "Positive theta thus creates nearest-neighbor correlations from\n"),
    ("Relative generator uses unit proposals on a simple nearest-neighbor torus",
     "For a translation-invariant torus of volume V, let r!=0 be the displacement\n",
     "For a simple translation-invariant nearest-neighbor torus of volume V, with\n"
     "side at least three and unit symmetric proposals, let r!=0 be the displacement\n"),
    ("Independent and portable block suites are distinguished",
     "the fifteen new block-coefficient cases themselves all have three sites.\n",
     "the separately sealed independent check has fifteen block-coefficient cases,\n"
     "all with three sites. The portable primary runner has twelve such cases,\n"
     "including one four-cycle; these are distinct suites.\n"),
]

current = (ROOT/NOTE).read_text()
assert sha256(current.encode()).hexdigest() == CORRECTED
assert sha256((ROOT/RUNNER).read_bytes()).hexdigest() == RUNNER_HASH
reconstructed = current
for label, before, after in fixes:
    assert reconstructed.count(after) == 1, label
    reconstructed = reconstructed.replace(after, before)
assert sha256(reconstructed.encode()).hexdigest() == INITIAL
result = {
    "initial_note_sha256": INITIAL, "corrected_note_sha256": CORRECTED,
    "unchanged_runner_sha256": RUNNER_HASH,
    "only_changes_are_the_four_reviewed_corrections": True,
    "fixes": [{"finding": label, "before": before, "after": after}
              for label, before, after in fixes],
}
(HERE/"SOURCE_CORRECTION_RECEIPT.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
