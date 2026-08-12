"""Regression tests for the repaired Cycle-970 evidence packet."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


REPO_ROOT = Path(__file__).resolve().parents[4]
PRIMARY = "scripts/frontier_cycle970_inter_site_gate_2026_08_09.py"
CHECKER = "scripts/frontier_cycle970_gate_independent_check_2026_08_09.py"
ALIAS_HOP = (
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
)
SEMANTICS = (
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py"
)
AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"


def link_or_copy(source: str, destination: str) -> str:
    try:
        os.link(source, destination)
    except OSError:
        shutil.copy2(source, destination)
    return destination


class Cycle970PacketTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        shutil.copytree(
            REPO_ROOT / "scripts",
            self.root / "scripts",
            copy_function=link_or_copy,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
        )
        axiom_target = self.root / AXIOMS
        axiom_target.parent.mkdir(parents=True)
        shutil.copy2(REPO_ROOT / AXIOMS, axiom_target)
        (self.root / "logs/runner-cache").mkdir(parents=True)
        (self.root / "outputs").mkdir()

    def execute_and_cache(self, runner: str) -> subprocess.CompletedProcess[str]:
        code = (
            "import sys; sys.path.insert(0, 'scripts'); "
            "from runner_cache import execute_and_write_cache; "
            f"result, _ = execute_and_write_cache({runner!r}, 300); "
            "raise SystemExit(0 if result.get('status') == 'ok' "
            "and result.get('exit_code') == 0 else 1)"
        )
        return subprocess.run(
            [sys.executable, "-c", code],
            cwd=self.root,
            text=True,
            capture_output=True,
            timeout=60,
            check=False,
        )

    def cache_status(self, runner: str) -> str:
        code = (
            "import sys; sys.path.insert(0, 'scripts'); "
            "from runner_cache import cache_status; "
            f"print(cache_status({runner!r}))"
        )
        result = subprocess.run(
            [sys.executable, "-c", code],
            cwd=self.root,
            text=True,
            capture_output=True,
            timeout=30,
            check=True,
        )
        return result.stdout.strip()

    def direct_failure(self) -> None:
        primary = subprocess.run(
            [sys.executable, PRIMARY],
            cwd=self.root,
            text=True,
            capture_output=True,
            timeout=30,
            check=False,
        )
        self.assertNotEqual(primary.returncode, 0, primary.stdout)
        self.assertNotIn(
            "VERDICT: CYCLE719_BOUND_ONE_CNOT_INTER_SITE_WITNESS",
            primary.stdout,
        )
        self.assertIn("VERDICT: CYCLE970_CHECKS_INCOMPLETE", primary.stdout)
        checker = subprocess.run(
            [sys.executable, CHECKER],
            cwd=self.root,
            text=True,
            capture_output=True,
            timeout=30,
            check=False,
        )
        self.assertNotEqual(checker.returncode, 0, checker.stdout)

    def test_fresh_pair_and_alias_substrate_local_mutations_fail_closed(self):
        primary = self.execute_and_cache(PRIMARY)
        self.assertEqual(primary.returncode, 0, primary.stdout + primary.stderr)
        checker = self.execute_and_cache(CHECKER)
        self.assertEqual(checker.returncode, 0, checker.stdout + checker.stderr)
        self.assertEqual(self.cache_status(PRIMARY), "fresh")
        self.assertEqual(self.cache_status(CHECKER), "fresh")

        alias_path = self.root / ALIAS_HOP
        alias_original = alias_path.read_text(encoding="utf-8")
        alias_mutated = alias_original.replace(
            "A = M.A",
            "A = M.A\nA.apply_semantic = lambda state, word: tuple(state)",
            1,
        )
        self.assertNotEqual(alias_original, alias_mutated, "alias mutation did not apply")
        alias_path.unlink()
        alias_path.write_text(alias_mutated, encoding="utf-8")

        self.assertEqual(self.cache_status(PRIMARY), "input_mismatch")
        self.assertEqual(self.cache_status(CHECKER), "input_mismatch")
        self.direct_failure()

        alias_path.unlink()
        alias_path.write_text(alias_original, encoding="utf-8")
        self.assertEqual(self.cache_status(PRIMARY), "fresh")
        self.assertEqual(self.cache_status(CHECKER), "fresh")

        semantics_path = self.root / SEMANTICS
        semantics_original = semantics_path.read_text(encoding="utf-8")
        semantics_mutated = semantics_original.replace(
            "state[gate.wires[1]] ^= state[gate.wires[0]]",
            "state[gate.wires[1]] ^= 0",
            1,
        )
        self.assertNotEqual(
            semantics_original, semantics_mutated, "substrate mutation did not apply"
        )
        semantics_path.unlink()
        semantics_path.write_text(semantics_mutated, encoding="utf-8")
        self.assertEqual(self.cache_status(PRIMARY), "input_mismatch")
        self.assertEqual(self.cache_status(CHECKER), "input_mismatch")
        self.direct_failure()

        semantics_path.unlink()
        semantics_path.write_text(semantics_original, encoding="utf-8")
        self.assertEqual(self.cache_status(PRIMARY), "fresh")
        self.assertEqual(self.cache_status(CHECKER), "fresh")

        primary_path = self.root / PRIMARY
        primary_original = primary_path.read_text(encoding="utf-8")
        primary_mutated = primary_original.replace(
            "output[gate.wires[1]] ^= output[gate.wires[0]]",
            "output[gate.wires[1]] ^= 0",
            1,
        )
        self.assertNotEqual(primary_original, primary_mutated, "local CNOT mutation did not apply")
        primary_path.unlink()
        primary_path.write_text(primary_mutated, encoding="utf-8")

        self.assertEqual(self.cache_status(PRIMARY), "sha_mismatch")
        self.assertEqual(self.cache_status(CHECKER), "input_mismatch")
        self.direct_failure()


if __name__ == "__main__":
    unittest.main()
