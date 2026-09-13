"""Small native feedback checks supporting the accompanying analytical theorem.

No external scientific data is read. Each directly imported helper reads its
own source for an integrity hash. The cache additionally binds the declared
source-note and helper bytes; those integrity reads are not physical inputs.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/NATIVE_FEEDBACK_FINITE_APPARATUS_BOUNDED_THEOREM_NOTE_2026-09-13.md",
    "docs/NATIVE_EDGE_RECORD_OCCUPATION_FEEDBACK_SHARED_BATTERY_BOUNDED_THEOREM_NOTE_2026-09-07.md",
    "docs/NATIVE_EDGE_RECORD_AMBIENT_GENERATOR_ERASURE_BOUNDED_THEOREM_NOTE_2026-09-07.md",
    "docs/NATIVE_EDGE_RECORD_LOCAL_QUENCH_FINITE_LADDER_BOUNDED_THEOREM_NOTE_2026-09-07.md",
    "docs/NATIVE_EDGE_RECORD_FINITE_COLLISION_APPARATUS_BOUNDED_THEOREM_NOTE_2026-09-07.md",
    "scripts/native_feedback_cap_check_2026_09_13.py",
    "scripts/native_feedback_collision_check_2026_09_13.py",
    ".claude/science/physics-loops/native-feedback-finite-apparatus-20260913/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/native-feedback-finite-apparatus-20260913/mutations/RESULTS.json",
)

import json
import os
import signal

for variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[variable] = "1"

from native_feedback_cap_check_2026_09_13 import run as cap_check
from native_feedback_collision_check_2026_09_13 import run as collision_check


def main():
    signal.alarm(AUDIT_TIMEOUT_SEC)
    cap = cap_check()
    collision = collision_check()
    # The helpers raise immediately on a failed mathematical predicate.
    total = cap["check_count"] + collision["check_count"]
    print(json.dumps({
        "scope": "same-agent small native algebra and state checks; general channel bound proved in the note",
        "cap": {key: value for key, value in cap.items() if key != "checks"},
        "collision": {key: value for key, value in collision.items() if key != "checks"},
    }, indent=2))
    print("per_element: Exact native two-edge cap identities and rounded square jump matrices are exercised.")
    print("per_site: Old and newly written native edge Record guards are checked on the stated finite inputs.")
    print("per_mode: The small positive battery cells and their real dark boundary are included in the operators.")
    print("per_block: Two fixed legal square preparations are compared by explicit unitary and GKSL evolution.")
    print("lattice_wide: checked and not executed — the full cube resource count is analytical, with no large apparatus simulation.")
    print(f"TOTAL: PASS={total} FAIL=0")


if __name__ == "__main__":
    main()
