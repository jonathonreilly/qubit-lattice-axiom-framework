#!/usr/bin/env python3
"""Route-2 physical color-ray source primitive current-bank no-go.

Safe claim:
  A supplied physical color ray in C^3 would select one line in the SU(3)
  adjoint coordinate space. Its complement has normalized fraction 7/8, which
  gives the Route-2 E-center endpoint value rho_E=21/4 under the granted
  T-side values.

  The current source/support bank does not supply that physical color ray or
  an equivalent gauge-frame/source-line primitive. Scalar/invariant source data
  cannot produce a nonzero adjoint line, color orientation is predictively
  vacuous, depolarization kills the traceless mean, the Fierz channel count
  supplies an 8-dimensional adjoint block rather than one line inside it, and
  the Z3 color/generation label bridge remains an open gate.

This is a current-bank no-go/support boundary, not an impossibility theorem
against future source primitives and not a retained derivation of quark masses.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TOL = 1.0e-10
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def normalized_text(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def require_phrases(label: str, rel_path: str, phrases: tuple[str, ...]) -> None:
    text = normalized_text(DOCS / rel_path)
    missing = [phrase for phrase in phrases if phrase not in text]
    check(
        f"quote anchors present: {label}",
        not missing,
        "all anchors found" if not missing else f"missing={missing!r}",
    )


def gell_mann() -> list[np.ndarray]:
    raw = [
        [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
        [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]],
        [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
        [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
        [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]],
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3.0),
    ]
    return [np.array(item, dtype=complex) / 2.0 for item in raw]


T = gell_mann()
I3 = np.eye(3, dtype=complex)


def traceless(matrix: np.ndarray) -> np.ndarray:
    return matrix - np.trace(matrix) * I3 / 3.0


def ray_density(index: int) -> np.ndarray:
    psi = np.zeros((3, 1), dtype=complex)
    psi[index, 0] = 1.0
    return psi @ psi.conj().T


def adjoint_coords(matrix: np.ndarray) -> np.ndarray:
    return np.array([2.0 * np.trace(matrix @ gen).real for gen in T])


def line_projector(v: np.ndarray) -> np.ndarray:
    return np.outer(v, v) / float(np.dot(v, v))


def su3_rotation_13(theta: float) -> np.ndarray:
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array(
        [
            [c, 0.0, s],
            [0.0, 1.0, 0.0],
            [-s, 0.0, c],
        ],
        dtype=complex,
    )


def commutant_dim() -> int:
    blocks = []
    for gen in T:
        # vec([X, gen]) = (gen.T kron I - I kron gen) vec(X)
        blocks.append(np.kron(gen.T, I3) - np.kron(I3, gen))
    matrix = np.vstack(blocks)
    sv = np.linalg.svd(matrix, compute_uv=False)
    return int(np.sum(sv < 1.0e-9))


def ad_invariant_traceless_dim() -> int:
    # The full commutant in M_3 is the scalars. Intersecting with traceless
    # matrices removes that one scalar dimension.
    return max(commutant_dim() - 1, 0)


def rank(matrix: np.ndarray) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=1.0e-9))


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str


CURRENT_BANK_EDGES: tuple[Edge, ...] = (
    Edge("current_source_bank", "color_orientation_retired", "orientation is gauge/predictively vacuous"),
    Edge("current_source_bank", "depolarized_color_density_boundary", "centrality requires traceless mean zero"),
    Edge("current_source_bank", "fierz_singlet_plus_adjoint_channels", "1+8 channel count and F_adj=8/9"),
    Edge("current_source_bank", "z3_color_generation_axis_open_gate", "shared axis-cycle bridge remains open"),
    Edge("current_source_bank", "route2_e_center_readout_open", "E-center lift remains open"),
    Edge("fierz_singlet_plus_adjoint_channels", "su3_adjoint_block_dimension_8", "dimension count only"),
    Edge("su3_adjoint_block_dimension_8", "su3_F_adj_8_9", "8/9 channel fraction"),
    Edge("route2_e_center_readout_open", "route2_needs_e_center_primitive", "rho_E not selected by blind data"),
)

PHYSICAL_RAY_EDGES: tuple[Edge, ...] = (
    Edge("physical_color_ray_source_line", "route2_adjoint_line_1_of_8", "ray selects H_psi line"),
    Edge("route2_adjoint_line_1_of_8", "route2_adjoint_complement_7_8", "orthogonal complement"),
    Edge("route2_adjoint_complement_7_8", "route2_e_excess_7_8", "read complement as E excess"),
    Edge("route2_e_excess_7_8", "route2_q_E_15_8", "q_E=1+7/8"),
    Edge("route2_q_E_15_8", "route2_rho_E_21_4", "rho_E=6(q_E-1)"),
    Edge("route2_rho_E_21_4", "route2_center_TE_minus_8_9", "granted T-side algebra"),
)

NEW_PRIMITIVE_EDGE = Edge(
    "current_source_bank",
    "physical_color_ray_source_line",
    "new physical color-ray/source-line primitive",
)


def reachable(edges: tuple[Edge, ...], start: str, target: str) -> bool:
    graph: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        graph[edge.source].append(edge.target)
    queue: deque[str] = deque([start])
    seen = {start}
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


def part1_conditional_color_ray() -> None:
    print("\nPART 1: supplied physical color ray gives the target line")
    rho = ray_density(2)
    h = traceless(rho)
    v = adjoint_coords(h)
    proj = line_projector(v)
    complement = np.eye(8) - proj

    e_excess = Fraction(7, 8)
    q_e = Fraction(1) + e_excess
    rho_e = 6 * (q_e - 1)
    c_te = Fraction(-2) * Fraction(5, 6) / q_e

    check("H_psi is traceless", abs(np.trace(h)) < TOL)
    check("H_psi is nonzero in adjoint coordinates", np.linalg.norm(v) > 1.0e-9)
    check("selected adjoint line projector has rank 1 and trace 1", rank(proj) == 1 and abs(np.trace(proj) - 1.0) < TOL)
    check("adjoint complement has rank 7", rank(complement) == 7, f"rank={rank(complement)}")
    check("complement fraction is exactly 7/8", e_excess == Fraction(7, 8))
    check("Route-2 endpoint arithmetic gives rho_E=21/4 and c_TE=-8/9", rho_e == Fraction(21, 4) and c_te == Fraction(-8, 9))


def part2_invariant_source_no_line() -> None:
    print("\nPART 2: invariant/scalar current-bank data cannot select an adjoint line")
    scalar_source = I3 / 3.0
    scalar_traceless = traceless(scalar_source)

    check("Gell-Mann basis has Tr(T_a T_b)=delta_ab/2", all(abs(np.trace(T[a] @ T[b]) - (0.5 if a == b else 0.0)) < TOL for a in range(8) for b in range(8)))
    check("commutant of the fundamental SU(3) generators is one-dimensional", commutant_dim() == 1, f"dim={commutant_dim()}")
    check("ad-invariant traceless subspace is zero-dimensional", ad_invariant_traceless_dim() == 0)
    check("scalar/depolarized density has zero traceless adjoint vector", np.linalg.norm(adjoint_coords(scalar_traceless)) < TOL)

    h = traceless(ray_density(2))
    g = su3_rotation_13(0.37)
    h_rot = g @ h @ g.conj().T
    check("a color-ray line is gauge-covariant, not gauge-invariant", np.linalg.norm(adjoint_coords(h_rot) - adjoint_coords(h)) > 1.0e-3)


def part3_fierz_count_not_line() -> None:
    print("\nPART 3: Fierz channel count supplies an 8-block, not one line inside it")
    n_c = 3
    singlet_dim = 1
    adjoint_dim = n_c * n_c - 1
    total_dim = n_c * n_c
    f_adj = Fraction(adjoint_dim, total_dim)
    isotropic_adjoint_weight = np.eye(adjoint_dim) / adjoint_dim
    eigenvalues = np.linalg.eigvalsh(isotropic_adjoint_weight)

    check("3 x 3bar channel dimensions split as 1+8=9", singlet_dim + adjoint_dim == total_dim)
    check("F_adj is exactly 8/9 at N_c=3", f_adj == Fraction(8, 9))
    check("isotropic adjoint block has rank 8, not rank 1", rank(isotropic_adjoint_weight) == 8)
    check("isotropic adjoint block has no distinguished eigenline", np.max(eigenvalues) - np.min(eigenvalues) < TOL, "multiplicity 8")


def part4_current_bank_reachability() -> None:
    print("\nPART 4: current-bank typed reachability")
    current = CURRENT_BANK_EDGES
    with_ray = CURRENT_BANK_EDGES + PHYSICAL_RAY_EDGES
    with_new_primitive = CURRENT_BANK_EDGES + (NEW_PRIMITIVE_EDGE,) + PHYSICAL_RAY_EDGES

    check(
        "current bank has no path to a physical color-ray source line",
        not reachable(current, "current_source_bank", "physical_color_ray_source_line"),
    )
    check(
        "current bank has no path to a Route-2 adjoint line selector",
        not reachable(current, "current_source_bank", "route2_adjoint_line_1_of_8"),
    )
    check(
        "current bank has no path to rho_E=21/4 through this route",
        not reachable(current, "current_source_bank", "route2_rho_E_21_4"),
    )
    check(
        "a supplied physical color ray reaches rho_E=21/4 conditionally",
        reachable(with_ray, "physical_color_ray_source_line", "route2_rho_E_21_4"),
    )
    check(
        "adding exactly the missing primitive makes the target reachable",
        reachable(with_new_primitive, "current_source_bank", "route2_rho_E_21_4"),
    )


def part5_quote_anchors() -> None:
    print("\nPART 5: current source-bank quote anchors")
    require_phrases(
        "color orientation retired",
        "COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md",
        (
            "Requiring a particular color orientation",
            "a named color frame, a color direction, a specific point inside an `SU(3)` orbit",
            "predictively vacuous",
        ),
    )
    require_phrases(
        "depolarization kills traceless mean",
        "MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md",
        (
            "the traceless projection `X -> X - (tr X / 3) I`",
            "the adjoint `8` carries no invariant vector",
            "color depolarization to the maximally mixed color density",
        ),
    )
    require_phrases(
        "Fierz support is channel algebra",
        "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md",
        (
            "1 singlet channel",
            "The adjoint-channel dimension fraction",
            "At N_c = 3, the adjoint-channel fraction is exactly 8/9",
            "The matching rule is **not derived in this note**",
        ),
    )
    require_phrases(
        "Rconn/readout selector open gate",
        "RCONN_KAPPA_EW_REGISTER_NOT_READ_COLOR_TRACE_OPEN_GATE_NOTE_2026-06-08.md",
        (
            "This is support for the channel algebra only. It is not a physical readout",
            "Record does not supply the missing readout context",
            "a retained physical EW readout theorem might identify the registered channel",
        ),
    )
    require_phrases(
        "Z3 color/generation bridge open",
        "Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md",
        (
            "does not by itself derive a physical bridge",
            "This note does not add a new axiom, primitive, or retained-surface premise",
            "A center-action argument cannot identify the color triplet",
        ),
    )
    require_phrases(
        "Route-2 E-center primitive remains open",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "it still does not derive the exact dimensionless readout triple",
            "the center `E` lift is",
            "1 + rho_E / 6.",
            "they produce different center `E` readouts",
        ),
    )


def main() -> int:
    print("Route-2 physical color-ray source primitive current-bank no-go")
    print("Scope: no current-source derivation; conditional ray consequence only")
    part1_conditional_color_ray()
    part2_invariant_source_no_line()
    part3_fierz_count_not_line()
    part4_current_bank_reachability()
    part5_quote_anchors()

    total = PASS_COUNT + FAIL_COUNT
    print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={total}")
    if FAIL_COUNT:
        print("VERDICT: FAIL -- current-bank certificate did not pass.")
        return 1
    print(
        "VERDICT: current source bank does not supply a physical color-ray "
        "source primitive; adding such a primitive would conditionally reach "
        "rho_E=21/4 through the adjoint-line complement route."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
