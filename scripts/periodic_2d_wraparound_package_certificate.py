#!/usr/bin/env python3
"""Certificate for the periodic 2D minimum-image wraparound packet."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.periodic_geometry import (  # noqa: E402
    minimum_image_displacement,
    minimum_image_distance,
)
from scripts.frontier_born_rule_alpha import (  # noqa: E402
    build_hamiltonian as born_build_hamiltonian,
    build_lattice_2d as born_build_lattice_2d,
)
from scripts.frontier_eigenvalue_stats_and_anderson_phase import (  # noqa: E402
    build_hamiltonian as anderson_build_hamiltonian,
    build_lattice_2d as anderson_build_lattice_2d,
)
from scripts.frontier_self_consistency_test import (  # noqa: E402
    build_hamiltonian as self_build_hamiltonian,
    build_lattice_2d as self_build_lattice_2d,
)


RUNNERS = {
    "self_consistency": (
        Path("scripts/frontier_self_consistency_test.py"),
        self_build_lattice_2d,
        self_build_hamiltonian,
    ),
    "anderson_phase": (
        Path("scripts/frontier_eigenvalue_stats_and_anderson_phase.py"),
        anderson_build_lattice_2d,
        anderson_build_hamiltonian,
    ),
    "born_alpha": (
        Path("scripts/frontier_born_rule_alpha.py"),
        born_build_lattice_2d,
        born_build_hamiltonian,
    ),
}

CACHES = {
    "self_consistency": (
        Path("logs/runner-cache/frontier_self_consistency_test.txt"),
        "OVERALL: Self-consistent vs Phase-scrambled null = 3.5 sigma",
    ),
    "anderson_phase": (
        Path("logs/runner-cache/frontier_eigenvalue_stats_and_anderson_phase.txt"),
        "No clear transition: max <r>=",
    ),
    "born_alpha": (
        Path("logs/runner-cache/frontier_born_rule_alpha.txt"),
        "alpha=2.0 is NOT uniquely best across all G.",
    ),
}


def _assert_helper_geometry() -> None:
    disp = minimum_image_displacement((0, 0), (9, 0), (10, 10))
    dist = minimum_image_distance((0, 0), (9, 0), (10, 10))
    diag_dist = minimum_image_distance((0, 0), (9, 9), (10, 10))

    assert disp == (-1.0, 0.0), disp
    assert math.isclose(dist, 1.0, rel_tol=0.0, abs_tol=1e-12), dist
    assert math.isclose(diag_dist, math.sqrt(2.0), rel_tol=0.0, abs_tol=1e-12), diag_dist


def _assert_runner_source(relpath: Path) -> None:
    source = (ROOT / relpath).read_text()
    assert "dx = min(dx, side - dx)" in source, relpath
    assert "dy = min(dy, side - dy)" in source, relpath


def _assert_runner_wrap_edge(name: str, build_lattice_2d, build_hamiltonian) -> None:
    n, pos, adj, col = build_lattice_2d(10)
    phi = np.zeros(n)
    hamiltonian = build_hamiltonian(pos, col, adj, n, phi)

    origin = 0
    x_wrap = 9 * 10
    y_wrap = 9

    assert x_wrap in adj[origin], adj[origin]
    assert y_wrap in adj[origin], adj[origin]
    assert math.isclose(abs(hamiltonian[origin, x_wrap]), 0.5, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(abs(hamiltonian[origin, y_wrap]), 0.5, rel_tol=0.0, abs_tol=1e-12)


def _assert_cache(relpath: Path, required_text: str) -> None:
    text = (ROOT / relpath).read_text()
    assert "exit_code: 0" in text, relpath
    assert required_text in text, relpath


def main() -> None:
    _assert_helper_geometry()
    print("helper: minimum-image wraparound distances PASS")

    for name, (relpath, build_lattice_2d, build_hamiltonian) in RUNNERS.items():
        _assert_runner_source(relpath)
        _assert_runner_wrap_edge(name, build_lattice_2d, build_hamiltonian)
        print(f"{name}: source and wrap-edge Hamiltonian PASS")

    for name, (relpath, required_text) in CACHES.items():
        _assert_cache(relpath, required_text)
        print(f"{name}: cached rerun evidence PASS")

    print("CERTIFICATE PASS: periodic 2D wraparound package evidence is present")


if __name__ == "__main__":
    main()
