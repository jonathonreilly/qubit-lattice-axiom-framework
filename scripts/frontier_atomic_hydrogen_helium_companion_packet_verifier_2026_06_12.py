#!/usr/bin/env python3
"""Restricted-packet verifier for the hydrogen/helium atomic companion row.

The active post-audit blocker is the helium Hartree Coulomb-normalization
surface.  The diagnostic work-history note needs full hydrogen, helium
Hartree, and helium Jastrow runner sources plus completed runner-cache
certificates visible in the restricted packet, and the Hartree runner must
show which density convention its pair integral uses.

This runner checks packet visibility and source/cache consistency only. It
does not promote the atomic lane, prove continuum control, derive absolute
eV units, or claim a retained hydrogen/helium theorem.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status} {name}{suffix}")


def cache_meta(cache_text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in cache_text.splitlines():
        if ": " in line and not line.startswith("-----"):
            key, value = line.split(": ", 1)
            if key in {"runner", "runner_sha256", "exit_code", "status"}:
                out[key] = value.strip()
    return out


def sha256_file(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


NOTE = "docs/work_history/atomic/HYDROGEN_HELIUM_ATOMIC_COMPANION_NOTE_2026-04-18.md"
HYDROGEN_RUNNER = "scripts/frontier_atomic_hydrogen_lattice_companion.py"
HARTREE_RUNNER = "scripts/frontier_atomic_helium_hartree_companion.py"
JASTROW_RUNNER = "scripts/frontier_atomic_helium_jastrow_companion.py"
DEPENDENCY_RUNNER = (
    "scripts/frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.py"
)

CACHES = {
    HYDROGEN_RUNNER: "logs/runner-cache/frontier_atomic_hydrogen_lattice_companion.txt",
    HARTREE_RUNNER: "logs/runner-cache/frontier_atomic_helium_hartree_companion.txt",
    JASTROW_RUNNER: "logs/runner-cache/frontier_atomic_helium_jastrow_companion.txt",
    DEPENDENCY_RUNNER: (
        "logs/runner-cache/frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.txt"
    ),
}


def main() -> int:
    print("Atomic hydrogen/helium companion packet verifier")
    print("=" * 72)

    note = read(NOTE)
    check("note names diagnostic finite-box work-history scope",
          "diagnostic finite-box work-history numerics only" in note)
    note_flat = " ".join(note.replace("*", "").split())
    check("note states no retained atomic authority",
          "does NOT claim continuum-limit" in note_flat
          and "retained atomic derivation-chain authority" in note_flat
          and "does not propagate as a flagship authority" in note_flat)
    check("note no longer says readouts are not pinned",
          "not pinned against a cached runner stdout" not in note)
    check("note names this packet verifier",
          "frontier_atomic_hydrogen_helium_companion_packet_verifier_2026_06_12.py" in note)

    source_requirements = {
        HYDROGEN_RUNNER: [
            "def build_graph_laplacian",
            "def build_coulomb_potential",
            "def solve_hamiltonian",
        ],
        HARTREE_RUNNER: [
            "def solve_poisson_for_hartree",
            "def helium_variational_scf",
            "E_var = 2",
            "pair_integral_normalization_certificate",
            "one-electron density",
            "quarter_total_density_form",
        ],
        JASTROW_RUNNER: [
            "def make_jastrow",
            "def local_energy",
            "g_EM/4",
            "repaired one-electron-density convention",
        ],
        DEPENDENCY_RUNNER: [
            "C.staggered.square_is_not_minus_laplacian",
            "B.3.coulomb.kernel_form",
            "runner proposes no ledger state",
        ],
    }

    for runner, needles in source_requirements.items():
        path = ROOT / runner
        check(f"{runner} exists", path.exists())
        if path.exists():
            text = read(runner)
            for needle in needles:
                check(f"{runner} contains {needle!r}", needle in text)

    readout_needles = {
        HYDROGEN_RUNNER: [
            "E_2/E",
            "0.25857",
            "0.11132",
            "Emergent Bohr radius",
        ],
        HARTREE_RUNNER: [
            "E(He",
            "1.43102",
            "IE",
            "0.4310",
            "E_pair",
            "pair_norm_direct_ratio=1.000000",
            "hartree_total_density_conversion_guard",
        ],
        JASTROW_RUNNER: [
            "1.41501",
            "1.43653",
            "Jastrow",
            "Full CI",
            "jastrow_inherits_repaired_hartree_normalization",
        ],
        DEPENDENCY_RUNNER: [
            "PASS=28",
            "FAIL=0",
            "All checks passed",
        ],
    }

    for runner, cache in CACHES.items():
        cache_path = ROOT / cache
        check(f"{cache} exists", cache_path.exists())
        if not cache_path.exists():
            continue
        cache_text = read(cache)
        meta = cache_meta(cache_text)
        check(f"{cache} records runner path", meta.get("runner") == runner,
              f"runner={meta.get('runner')}")
        check(f"{cache} exits zero", meta.get("exit_code") == "0",
              f"exit_code={meta.get('exit_code')}")
        check(f"{cache} status ok", meta.get("status") == "ok",
              f"status={meta.get('status')}")
        expected_sha = meta.get("runner_sha256")
        live_sha = sha256_file(runner)
        check(f"{cache} sha matches source", expected_sha == live_sha,
              f"cache={expected_sha}, live={live_sha}")
        for needle in readout_needles[runner]:
            check(f"{cache} contains {needle!r}", needle in cache_text)

    pin_table_rows = [
        "frontier_atomic_hydrogen_lattice_companion.txt",
        "frontier_atomic_helium_hartree_companion.txt",
        "frontier_atomic_helium_jastrow_companion.txt",
        "frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.txt",
    ]
    for row in pin_table_rows:
        check(f"note cites cache {row}", row in note)

    check("note leaves status authority external",
          "Status authority: independent audit lane only" in note_flat)
    check("note says no status lift",
          "no status lift" in note and "confirms source/cache visibility only" in note)

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        return 1
    print("Packet visibility is complete; audit/review owns status movement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
