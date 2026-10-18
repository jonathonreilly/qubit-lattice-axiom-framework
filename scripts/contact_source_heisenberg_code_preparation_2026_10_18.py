#!/usr/bin/env python3
"""Exact finite controls for the supplied contact-source preparation model.

Analytic infinite-lattice and all-time conclusions are proved in the note.
This runner imports its declared helper and reads declared source bytes for
integrity. It reads no external scientific data. The canonical cache is written
by runner_cache.execute_and_write_cache, not by this script.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "scripts/contact_source_heisenberg_controls.py",
    "docs/CONTACT_SOURCE_HEISENBERG_CODE_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-18.md",
    "docs/NATIVE_HEISENBERG_NODAL_RECORD_PERSISTENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md",
)

import hashlib
import json
from pathlib import Path

from contact_source_heisenberg_controls import run_checks, run_mutation_checks

ROOT = Path(__file__).resolve().parents[1]


def main():
    result = {
        "scope": "Exact finite controls for a supplied eight-spin Markov instrument on the two-excitation domain; no audit verdict or native formation derivation.",
        "inputs": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},
        "controls": run_checks(),
        "mutations": run_mutation_checks(),
    }
    output = ROOT / "outputs/contact_source_heisenberg_code_preparation_2026_10_18.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    print("per_element: exact source and target coefficients and spin-ladder matrix elements are exercised by the finite controls.")
    print("per_site: the actual-Z3 finite-support generator fixtures check target occupation zeros on the specified nodal plane.")
    print("per_mode: checked and not executed — no Fourier mode classification or spectral-completeness calculation is part of this runner.")
    print("per_block: the full eight-qubit scalar intertwiner and its two-excitation restriction are checked with exact arithmetic.")
    print("lattice_wide: checked and not executed — infinite sums and all-time invariance are analytic proofs in the source note, not finite-fixture conclusions.")


if __name__ == "__main__":
    main()
