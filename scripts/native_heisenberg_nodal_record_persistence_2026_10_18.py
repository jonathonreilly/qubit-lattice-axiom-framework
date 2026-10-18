#!/usr/bin/env python3
"""Finite exact controls for conditional native nodal persistence.

Reads only declared source/helper bytes for integrity plus imported helper.
The all-size and infinite-lattice claims rest on analytic proofs, not fixtures.
Canonical cache is produced externally by runner_cache.execute_and_write_cache.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "scripts/native_heisenberg_nodal_controls.py",
    "scripts/native_heisenberg_many_particle_controls.py",
    "docs/NATIVE_HEISENBERG_NODAL_RECORD_PERSISTENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md",
)
import hashlib
import json
import platform
from pathlib import Path
from native_heisenberg_nodal_controls import one_particle_fixture, two_particle_fixture

from native_heisenberg_many_particle_controls import many_particle_fixtures

ROOT = Path(__file__).resolve().parents[1]

def main():
    result = {
        "kind": "conditional exact finite controls; no audit verdict",
        "python": platform.python_version(),
        "inputs": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},
        "one_excitation": [one_particle_fixture(n) for n in (4, 6, 8)],
        "two_excitation": [two_particle_fixture(l, m) for l, m in ((6, 3), (8, 4), (10, 3))],
        "actual_Z3_finite_support": many_particle_fixtures(),
        "scope": "Full-spin integer intertwining, normalization and preserved failed controls. Infinite-volume self-adjointness and arbitrary-size statements require the note proofs. No physical preparation, Record formation or Hamiltonian selection derived.",
    }
    out = ROOT / "outputs/native_heisenberg_nodal_record_persistence_2026_10_18.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
