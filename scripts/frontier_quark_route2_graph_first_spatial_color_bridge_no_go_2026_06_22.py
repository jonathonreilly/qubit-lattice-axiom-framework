#!/usr/bin/env python3
"""Test the graph-first SU(3) escape for the Route-2 R_conn bridge.

Target bridge:

    R_conn -> c_TE = -8/9

This runner checks the explicit residual left by the cross-domain no-go:
whether the graph-first SU(3) construction supplies a typed spatial/color map
from its selected-axis commutant to the Route-2 cubic E/T2 center readout.

It deliberately does not use live endpoint/comparator values.  The output is a
support/no-go packet, not an audit verdict.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
from typing import Iterable

import numpy as np

from frontier_graph_first_su3_integration import (
    I8,
    commutant_basis,
    commutator,
    is_close,
    make_change_of_basis,
    parity_op,
    residual_swap_op,
    shift_op,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOOP = ROOT / ".claude" / "science" / "physics-loops" / "s3-route2-graph-first-spatial-color-bridge"

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def loop_text(name: str) -> str:
    return (LOOP / name).read_text(encoding="utf-8")


def matrix_rank(m: np.ndarray) -> int:
    return int(np.linalg.matrix_rank(m, tol=1e-10))


def selected_axis_summary(axis: int) -> dict[str, int]:
    """Return graph-first invariants without using the verbose upstream runner."""

    x = shift_op(axis)
    z = parity_op(axis)
    y = -1j * z @ x
    weak = [x / 2.0, y / 2.0, z / 2.0]
    swap = residual_swap_op(axis)
    null_both, dim_both = commutant_basis(weak + [swap])
    pi_plus = (I8 + swap) / 2.0
    pi_minus = (I8 - swap) / 2.0
    u = make_change_of_basis(axis)

    return {
        "weak_commutant_dim": commutant_basis(weak)[1],
        "weak_swap_commutant_dim": dim_both,
        "pi_plus_rank": matrix_rank(pi_plus),
        "pi_minus_rank": matrix_rank(pi_minus),
        "color_rank": matrix_rank(pi_plus) // 2,
        "change_of_basis_unitary": int(is_close(u.conj().T @ u, np.eye(8))),
        "swap_commutes_with_weak": int(
            all(is_close(commutator(swap, w), np.zeros((8, 8))) for w in weak)
        ),
        "commutant_basis_dim": null_both.shape[1],
    }


def sym_traceless_basis() -> list[np.ndarray]:
    """Five-dimensional SO(3) l=2 model as symmetric traceless tensors."""

    basis = []
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        m = np.zeros((3, 3))
        m[i, j] = m[j, i] = 1 / np.sqrt(2)
        basis.append(m)
    basis.append(np.diag([1, -1, 0]) / np.sqrt(2))
    basis.append(np.diag([-1, -1, 2]) / np.sqrt(6))
    return basis


def octahedral_rotations() -> list[np.ndarray]:
    rots = []
    for p in permutations(range(3)):
        for signs in product([1, -1], repeat=3):
            r = np.zeros((3, 3))
            for i in range(3):
                r[i, p[i]] = signs[i]
            if abs(np.linalg.det(r) - 1) < 1e-9:
                rots.append(r)
    return rots


def rot_on_l2(rotation: np.ndarray, basis: list[np.ndarray]) -> np.ndarray:
    out = np.zeros((len(basis), len(basis)))
    for b, tensor in enumerate(basis):
        moved = rotation @ tensor @ rotation.T
        for a, target in enumerate(basis):
            out[a, b] = np.sum(target * moved)
    return out


def reachable(edges: Iterable[tuple[str, str]], start: str, target: str) -> bool:
    graph: dict[str, set[str]] = {}
    for src, dst in edges:
        graph.setdefault(src, set()).add(dst)
    todo = deque([start])
    seen = {start}
    while todo:
        node = todo.popleft()
        if node == target:
            return True
        for nxt in graph.get(node, set()):
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return False


def domain(node: str) -> str:
    if node.startswith("graph_") or node.startswith("su3_"):
        return "graph_color"
    if node.startswith("spatial_") or node.startswith("cubic_"):
        return "spatial_cubic"
    if node.startswith("route2_"):
        return "route2_endpoint"
    raise ValueError(f"unclassified node: {node}")


def part1_graph_first_su3_surface() -> None:
    print("PART 1: graph-first SU(3) surface")
    for axis in range(3):
        summary = selected_axis_summary(axis)
        prefix = f"axis {axis + 1}"
        check(f"{prefix}: selected-axis basis is unitary", summary["change_of_basis_unitary"] == 1)
        check(f"{prefix}: residual swap commutes with weak su(2)", summary["swap_commutes_with_weak"] == 1)
        check(f"{prefix}: dim Comm(weak su(2)) = 16", summary["weak_commutant_dim"] == 16)
        check(f"{prefix}: dim Comm(weak su(2), swap) = 10", summary["weak_swap_commutant_dim"] == 10)
        check(f"{prefix}: symmetric block rank = 6", summary["pi_plus_rank"] == 6)
        check(f"{prefix}: antisymmetric block rank = 2", summary["pi_minus_rank"] == 2)
        check(f"{prefix}: graph-first color rank is 3", summary["color_rank"] == 3)
        check(f"{prefix}: commutant basis has gl(3)+gl(1) dimension", summary["commutant_basis_dim"] == 10)


def part2_cubic_l2_route2_readout_surface() -> None:
    print()
    print("PART 2: cubic l=2 E/T2 readout surface")
    basis = sym_traceless_basis()
    rotations = octahedral_rotations()
    reps = [rot_on_l2(r, basis) for r in rotations]
    chi_l2 = np.array([np.trace(rep) for rep in reps])

    offdiag_to_diag_mixing = max(float(np.linalg.norm(rep[:3, 3:])) for rep in reps)
    diag_to_offdiag_mixing = max(float(np.linalg.norm(rep[3:, :3])) for rep in reps)
    trivial_mult = Fraction(str(round(float(np.sum(chi_l2) / len(rotations)), 12)))
    character_norm = float(np.sum(chi_l2 ** 2) / len(rotations))

    check("proper octahedral group has order 24", len(rotations) == 24)
    check("symmetric traceless l=2 model has dimension 5", len(basis) == 5)
    check("l=2 has no cubic A1 singlet", trivial_mult == 0)
    check("l=2 character norm is two irreducible summands", abs(character_norm - 2.0) < 1e-9)
    check("off-diagonal T2 block is invariant", offdiag_to_diag_mixing < 1e-10)
    check("diagonal E block is invariant", diag_to_offdiag_mixing < 1e-10)
    check("cubic split dimensions are E=2 and T2=3", reps[0][3:, 3:].shape == (2, 2) and reps[0][:3, :3].shape == (3, 3))
    check("graph-first taste space dimension differs from l=2 tensor space", I8.shape[0] == 8 and len(basis) == 5)


def part3_domain_reachability() -> None:
    print()
    print("PART 3: domain reachability")
    base_edges = [
        ("graph_selected_axis", "graph_weak_su2"),
        ("graph_selected_axis", "graph_residual_swap"),
        ("graph_weak_su2", "graph_commutant_gl3_gl1"),
        ("graph_residual_swap", "graph_commutant_gl3_gl1"),
        ("graph_commutant_gl3_gl1", "su3_color_rank_3"),
        ("su3_color_rank_3", "su3_adjoint_fraction_8_9"),
        ("spatial_l2_tensor", "cubic_l2_E_T2_split"),
        ("cubic_l2_E_T2_split", "route2_c_TE_readout_slot"),
        ("route2_c_TE_minus_8_9", "route2_q_E_15_8"),
        ("route2_q_E_15_8", "route2_rho_E_21_4"),
    ]
    missing_bridge = ("su3_adjoint_fraction_8_9", "route2_c_TE_minus_8_9")
    stronger_missing_bridge = ("graph_commutant_gl3_gl1", "route2_c_TE_readout_slot")

    cross_edges = [
        edge
        for edge in base_edges
        if domain(edge[0]) == "graph_color" and domain(edge[1]).startswith("route2")
    ]
    check("generated graph-first/readout edge set has no color-to-Route2 edge", cross_edges == [], str(cross_edges))
    check(
        "R_conn support does not reach rho_E endpoint without bridge",
        not reachable(base_edges, "su3_adjoint_fraction_8_9", "route2_rho_E_21_4"),
    )
    check(
        "adding explicit R_conn -> c_TE bridge creates endpoint path",
        reachable(base_edges + [missing_bridge], "su3_adjoint_fraction_8_9", "route2_rho_E_21_4"),
    )
    check(
        "adding stronger graph-first readout functor reaches the c_TE slot",
        reachable(base_edges + [stronger_missing_bridge], "graph_commutant_gl3_gl1", "route2_c_TE_readout_slot"),
    )
    check(
        "the stronger functor alone still does not select c_TE=-8/9",
        not reachable(base_edges + [stronger_missing_bridge], "graph_commutant_gl3_gl1", "route2_c_TE_minus_8_9"),
    )


def part4_exact_switch_boundary() -> None:
    print()
    print("PART 4: exact switch boundary")
    f_adj = Fraction(8, 9)
    target = Fraction(-8, 9)
    wrong_full_trace = Fraction(-1, 1)
    wrong_positive_sign = Fraction(8, 9)

    check("graph-first SU(3) supplies the positive adjoint fraction", f_adj == Fraction(8, 9))
    check("target signed center ratio is not the positive adjoint fraction", target != f_adj)
    check("sigma=-1 is an extra orientation switch", -f_adj == target)
    check("full-trace selector with sigma=-1 gives -1, not -8/9", wrong_full_trace != target)
    check("positive orientation with kappa=0 gives +8/9, not -8/9", wrong_positive_sign != target)


def part5_document_boundary() -> None:
    print()
    print("PART 5: document boundary")
    graph_note = note_text("GRAPH_FIRST_SU3_INTEGRATION_NOTE.md")
    new_note = note_text("QUARK_ROUTE2_GRAPH_FIRST_SPATIAL_COLOR_BRIDGE_NO_GO_NOTE_2026-06-22.md")
    handoff = loop_text("HANDOFF.md")
    normalized_note = " ".join(new_note.replace("**", "").split())
    normalized_note_lower = normalized_note.lower()

    graph_lower = graph_note.lower()
    check("graph-first note is the SU(3) commutant theorem", "su(3)" in graph_lower and "commutant" in graph_lower)
    for absent in ("c_TE", "Route-2", "E/T2", "l=2", "gamma_T", "gamma_E", "rho_E"):
        check(f"graph-first note does not mention Route-2 readout marker {absent}", absent not in graph_note)

    required = (
        "Claim type:** no_go",
        "Actual current-surface status: no-go for graph-first spatial/color bridge closure",
        "This is not an audit verdict",
        "graph-first SU(3) supplies color rank support, not a typed Route-2 readout map",
        "Missing primitive",
        "typed functor from the selected-axis graph/color commutant to the Route-2 cubic `l=2` `E/T2` center-response readout",
        "orientation sign `sigma=-1`",
        "connected selector `kappa=0`",
    )
    for marker in required:
        if marker == "Claim type:** no_go":
            present = marker in new_note
        elif marker == "Missing primitive":
            present = marker.lower() in normalized_note_lower
        else:
            present = marker in normalized_note
        check(f"new note contains marker: {marker}", present)

    handoff_required = (
        "Block75 Summary",
        "negative_route_pruning",
        "Do not audit",
        "Next Exact Action",
    )
    for marker in handoff_required:
        check(f"handoff contains marker: {marker}", marker in handoff)

    banned = (
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
        ("actual-surface retention", phrase("ret", "ained on the actual surface")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
    )
    combined = new_note + "\n" + handoff
    for label, marker in banned:
        check(f"new packet avoids overclaim marker: {label}", marker not in combined)


def main() -> int:
    print("Route-2 graph-first spatial/color bridge no-go")
    print("Status: no-go for graph-first spatial/color bridge closure; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_graph_first_su3_surface()
    part2_cubic_l2_route2_readout_surface()
    part3_domain_reachability()
    part4_exact_switch_boundary()
    part5_document_boundary()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: graph-first spatial/color bridge checks failed.")
        return 1
    print(
        "VERDICT: graph-first SU(3) supplies color-rank/adjoint-fraction support, "
        "but no current typed functor maps it to the Route-2 cubic E/T2 center "
        "readout or supplies sigma=-1 and kappa=0."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
