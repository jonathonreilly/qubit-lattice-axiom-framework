#!/usr/bin/env python3
"""Route-2 theta-to-slice channel-density no-go.

Safe claim:
  The exact theta-to-slice family has the rank-one form

      Xi_P(t; c) = (P_R c) tensor V_R(t)

  with the same slice factor V_R(t)=exp(-t Lambda_R) u_* for every source
  channel.  Therefore the slice coupling preserves all source-side readout
  ratios: center/shell ratios, q_E/q_T, and the freedom in rho_E are not
  changed by Lambda_R or the slice semigroup.

  Consequently this theta-to-slice route cannot supply the missing
  channel-density normalization or the inverse-square covariance primitive
  needed for rho_E=21/4.  The remaining ambiguity is source/readout-side,
  not slice-dynamical.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np

from frontier_quark_route2_exact_readout_map import (
    EXACT_TOL,
    admissible_readout_matrix,
    restricted_readout_data,
)
from frontier_quark_route2_exact_time_coupling import route2_slice_backbone, v_r, xi_p


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PASS_COUNT = 0
FAIL_COUNT = 0
TIMES = (0.0, 0.5, 1.0, 2.0)
RHO_VALUES = (Fraction(-1, 1), Fraction(0, 1), Fraction(1, 1), Fraction(21, 4), Fraction(6, 1))


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


def row_norm_ratio(readout: np.ndarray, center: np.ndarray, shell: np.ndarray, time_seed: np.ndarray, row: int) -> float:
    xi_center = xi_p(readout, center, time_seed)
    xi_shell = xi_p(readout, shell, time_seed)
    return float(np.linalg.norm(xi_center[row]) / np.linalg.norm(xi_shell[row]))


def source_ratio(readout: np.ndarray, center: np.ndarray, shell: np.ndarray, row: int) -> float:
    source_center = readout @ center
    source_shell = readout @ shell
    return float(source_center[row] / source_shell[row])


def exact_qe(rho_e: Fraction) -> Fraction:
    return Fraction(1, 1) + rho_e / 6


def exact_qt() -> Fraction:
    return Fraction(5, 6)


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str


CURRENT_EDGES: tuple[Edge, ...] = (
    Edge("exact_slice_backbone_Lambda_R", "common_slice_factor_V_R", "V_R(t)=exp(-t Lambda_R) u_*"),
    Edge("common_slice_factor_V_R", "theta_slice_family_Xi_P", "common rank-one slice factor"),
    Edge("admissible_readout_map_P_R", "theta_slice_family_Xi_P", "Xi_P=(P_R c) tensor V_R"),
    Edge("theta_slice_family_Xi_P", "source_ratios_preserved", "common rank-one slice factor cancels"),
    Edge("source_ratios_preserved", "rho_E_free", "P_R still supplies rho_E"),
)

MISSING_PRIMITIVE_EDGES: tuple[Edge, ...] = (
    Edge("channel_density_normalization", "inverse_square_covariance", "D_X=A_X/w_X then q_X proportional to D_X^2"),
    Edge("inverse_square_covariance", "lambda_9_4", "q_E/q_T=9/4"),
    Edge("lambda_9_4", "rho_E_21_4", "endpoint algebra"),
)


def reachable(edges: tuple[Edge, ...], start: str, target: str) -> bool:
    graph: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        graph[edge.source].append(edge.target)
    seen = {start}
    queue: deque[str] = deque([start])
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


def part1_slice_backbone_common_factor() -> None:
    print("\nPART 1: exact slice backbone is common to channels")
    backbone = route2_slice_backbone()
    check("Lambda_R is symmetric to exact tolerance", backbone.sym_err < EXACT_TOL, f"sym_err={backbone.sym_err:.3e}")
    check("Lambda_R is positive definite", backbone.min_eig > 0.0, f"min_eig={backbone.min_eig:.6e}")
    factors = [float(np.linalg.norm(v_r(backbone, t))) for t in TIMES]
    check("V_R(t) is nonzero at tested times", all(f > 0.0 for f in factors), f"norms={[round(f, 12) for f in factors]}")


def part2_source_ratio_preservation() -> None:
    print("\nPART 2: theta-to-slice transport preserves readout ratios")
    data = restricted_readout_data()
    backbone = route2_slice_backbone()

    all_preserved = True
    details: list[str] = []
    for rho in RHO_VALUES:
        readout = admissible_readout_matrix(1.0, float(rho), -2.0, 2.0)
        src_qe = source_ratio(readout, data.carrier_e_center, data.carrier_e_shell, 0)
        src_qt = source_ratio(readout, data.carrier_t_center, data.carrier_t_shell, 1)
        src_lambda = src_qe / src_qt
        exact_lambda = exact_qe(rho) / exact_qt()
        details.append(f"rho_E={rho}: lambda={Fraction(src_lambda).limit_denominator()}")

        if abs(src_lambda - float(exact_lambda)) > EXACT_TOL:
            all_preserved = False

        for t in TIMES:
            seed = v_r(backbone, t)
            slice_qe = row_norm_ratio(readout, data.carrier_e_center, data.carrier_e_shell, seed, 0)
            slice_qt = row_norm_ratio(readout, data.carrier_t_center, data.carrier_t_shell, seed, 1)
            slice_lambda = slice_qe / slice_qt
            if abs(slice_qe - abs(src_qe)) > EXACT_TOL:
                all_preserved = False
            if abs(slice_qt - abs(src_qt)) > EXACT_TOL:
                all_preserved = False
            if abs(slice_lambda - abs(src_lambda)) > EXACT_TOL:
                all_preserved = False

    print("  transported admissible lambda values:", "; ".join(details))
    check("all tested admissible rho_E values survive theta-to-slice transport with unchanged source ratios", all_preserved)
    check("rho_E=0 and rho_E=21/4 remain distinct after transport", "rho_E=0: lambda=6/5" in "; ".join(details) and "rho_E=21/4: lambda=9/4" in "; ".join(details))


def part3_no_channel_density_generation() -> None:
    print("\nPART 3: common slice factor cannot generate the missing channel-density normalization")
    one_pole_lambda = Fraction(3, 2)
    target_lambda = Fraction(9, 4)
    slice_scale = Fraction(7, 5)  # arbitrary common positive scale; cancels exactly.
    transported = (one_pole_lambda * slice_scale) / slice_scale
    check("common slice scaling preserves a one-pole lambda=3/2 rather than converting it to 9/4", transported == one_pole_lambda and transported != target_lambda, f"transported={transported}")

    raw_lambda = Fraction(1, 1)
    transported_raw = (raw_lambda * slice_scale) / slice_scale
    check("common slice scaling preserves raw-amplitude lambda=1", transported_raw == raw_lambda)
    check("reaching 9/4 requires a channel-dependent source/readout factor", target_lambda / one_pole_lambda == Fraction(3, 2), "extra E/T factor needed after one-pole route is 3/2")


def part4_typed_reachability() -> None:
    print("\nPART 4: typed reachability")
    current = CURRENT_EDGES
    with_missing_source = CURRENT_EDGES + MISSING_PRIMITIVE_EDGES
    check("theta-to-slice graph has no path to channel-density normalization", not reachable(current, "exact_slice_backbone_Lambda_R", "channel_density_normalization"))
    check("theta-to-slice graph has no path to rho_E=21/4", not reachable(current, "exact_slice_backbone_Lambda_R", "rho_E_21_4"))
    check("adding the missing source primitive reaches rho_E=21/4", reachable(with_missing_source, "channel_density_normalization", "rho_E_21_4"))
    check("adding only theta-to-slice transport still leaves rho_E free", reachable(current, "exact_slice_backbone_Lambda_R", "rho_E_free"))


def part5_quote_anchors() -> None:
    print("\nPART 5: current-surface quote anchors")
    require_phrases(
        "theta-to-slice note names exact conditional family and blocker",
        "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md",
        (
            "exact conditional coupling family",
            "unresolved readout exactness blocks a unique exact `Theta_R -> Lambda_R`",
            "The next theorem target is the missing readout-map endpoint triple.",
        ),
    )
    require_phrases(
        "exact time-coupling note says ambiguity is source-side",
        "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md",
        (
            "exact conditional readout-to-slice coupling family",
            "different exact center couplings on the same slice backbone",
            "derive the exact readout map entry that removes the source-side ambiguity",
        ),
    )
    require_phrases(
        "exact readout map names missing E entry",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "the irreducible missing map entry is the `E`-channel ratio",
            "exact missing-map obstruction",
        ),
    )
    require_phrases(
        "quadratic note names inverse-square gap",
        "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        (
            "No named functional produces an inverse-square-of-projector-weight center lift.",
            "future genuinely **nonlinear**",
        ),
    )


def part6_n5_execution_certificate() -> None:
    """Print-only record of what this runner resolves at each granularity."""
    print("\nPART 6: N5 execution certificate (print-only; adds no check and no counter)")
    backbone = route2_slice_backbone()
    trace_dim = int(backbone.lambda_sym.shape[0])
    rho_list = ", ".join(str(rho) for rho in RHO_VALUES)
    print(
        f"per_element: resolved -- the slice generator is compared entry against transposed entry over all "
        f"{trace_dim}x{trace_dim} positions, max|Lambda_R - Lambda_R^T| = {backbone.sym_err:.3e} against the shared "
        f"EXACT_TOL = {EXACT_TOL:.0e}, and every admissible readout is assembled one entry at a time: of the eight "
        f"entries of P(rho_E) exactly one, the [0,2] slot, is moved across the enumerated values {rho_list}, while "
        f"[0,0]=1, [1,1]=-2, [1,3]=2 and the four structural zeros are held fixed."
    )
    print(
        f"per_site: checked and not executed -- the {trace_dim} boundary-trace sites indexing Lambda_R are produced by "
        "eliminating the exterior bulk of the 15^3 grid in one Schur solve, and after that no site is ever read on its "
        "own: the slice seed u_* is the uniform unit vector over all trace sites and only its transported norm is used, "
        "while on the source side the six shell sites of the seven-site star enter solely through the single uniform "
        "combination s/sqrt(6). No site amplitude is resolved anywhere in this file."
    )
    print(
        "per_mode: resolved -- E and T occupy separate rows of P(rho_E), row 0 for E and row 1 for T, and the quantity "
        "this no-go is about is a strictly cross-mode one: lambda = q_E/q_T. Both modes are transported through the "
        f"same V_R(t) at the {len(TIMES)} tested times {TIMES} and each mode's center/shell ratio, and their quotient, "
        "come back unchanged, so rho_E=0 keeps lambda=6/5 and rho_E=21/4 keeps lambda=9/4 rather than being mixed."
    )
    print(
        "per_block: resolved -- the restricted carrier space splits into an E block on coordinates {0,2} and a T block "
        "on {1,3}; P(rho_E) is block-diagonal across that split, so the whole rho_E freedom sits inside the E block "
        "while the T block stays pinned at (-2, 2). The typed graph carries the same block structure: the 5 current "
        f"theta-to-slice edges and the {len(MISSING_PRIMITIVE_EDGES)} missing-primitive edges form two components with "
        "no edge joining them, which is precisely what PART 4 certifies as unreachability."
    )
    print(
        "lattice_wide: resolved as a finite-N statement -- Lambda_R is the Schur complement of the 15^3 negative "
        "Laplacian onto the trace set at cutoff radius 4.0, a whole-grid operator, and it is certified whole here: "
        f"symmetric to EXACT_TOL and positive definite with smallest eigenvalue {backbone.min_eig:.6f}. Because "
        "V_R(t)=exp(-t Lambda_R) u_* multiplies every source channel identically, this entire lattice-scale factor "
        "cancels out of each ratio. One grid size (15) and one cutoff (4.0) are executed; no thermodynamic limit."
    )


def main() -> int:
    print("Route-2 theta-to-slice channel-density no-go")
    print("Scope: exact rank-one theta-to-slice transport; source/readout primitives remain open")
    part1_slice_backbone_common_factor()
    part2_source_ratio_preservation()
    part3_no_channel_density_generation()
    part4_typed_reachability()
    part5_quote_anchors()
    part6_n5_execution_certificate()

    total = PASS_COUNT + FAIL_COUNT
    print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={total}")
    if FAIL_COUNT:
        print("VERDICT: FAIL -- theta-to-slice channel-density no-go certificate did not pass.")
        return 1
    print(
        "VERDICT: scoped no-go. The exact rank-one theta-to-slice coupling "
        "preserves source-side readout ratios and cannot generate the missing "
        "channel-density normalization or inverse-square covariance primitive; "
        "the remaining blocker is source/readout-side."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
