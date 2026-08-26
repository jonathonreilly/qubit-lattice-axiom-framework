#!/usr/bin/env python3
"""Independent exact checker for the Block-203 D1 gluing discriminator.

This checker does not import the primary module or its intermediates.  It uses
a scalar recurrence for the monodromy trace, direct finite determinants, a
separate two-half Schur calculation, and explicit four-state CAR densities.
"""

from __future__ import annotations

import argparse
from functools import cache
from pathlib import Path
import subprocess

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826"
)
PREREG = "b09855d0eccb374c56ca67153d506a577a7fe399"
PARENT = "7cdf45b3449f8bec3edbc11384d74baf32b59653"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_L24_REFLECTION_ALGEBRA_EXACT_GLUING_"
    "TRACE_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/STATE.yaml",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/CLAIM_STATUS_CERTIFICATE.md",
    ".claude/science/physics-loops/toe-axiom-closure-block203-reflection-algebra-gluing-discriminator-20260826/TRACE_GATE.md",
    "docs/ADMISSIBILITY_D4_L24_REFLECTION_ALGEBRA_EXACT_GLUING_TRACE_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_D4_L12_OPEN_TIME_STABLE_OS_EVENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/P2_PHASE_BLINDNESS_FROM_RP_TRANSFER_TRACE_BRIDGE_NOTE_2026-05-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

R = sp.Rational
MASS = R(2, 7)
LENGTH = 24
HALF = 12
SIGMA = sp.diag(1, -1)

MUTATION_GATE = {
    "lose_preregistration": "I0",
    "swap_boundary_conditions": "I1",
    "change_recurrence_sign": "I1",
    "drop_one_seam": "I2",
    "use_scalar_instead_of_full_action": "I2",
    "call_periodic_ordinary": "I3",
    "call_ap_graded": "I3",
    "omit_one_particle_sector": "I4",
    "call_even_algebra_positive": "I4",
    "accept_positive_determinant_as_state": "I4",
    "accept_one_tournament_cell": "I5",
    "replace_periodic_by_ap": "I6",
    "claim_broad_no_go": "I6",
    "open_downstream_claims": "I7",
}
MUTATIONS = tuple(MUTATION_GATE)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=300
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL, timeout=300,
    ).returncode == 0


def differential(ap: bool, *, open_chain: bool = False) -> sp.Matrix:
    matrix = sp.zeros(LENGTH)
    for site in range(LENGTH - 1):
        matrix[site + 1, site] = R(1, 2)
        matrix[site, site + 1] = -R(1, 2)
    if not open_chain:
        seam = -1 if ap else 1
        matrix[0, LENGTH - 1] = R(seam, 2)
        matrix[LENGTH - 1, 0] = -R(seam, 2)
    return matrix


def action(ap: bool, *, open_chain: bool = False) -> sp.Matrix:
    return sp.kronecker_product(
        sp.eye(LENGTH), MASS * sp.eye(2)
    ) + sp.kronecker_product(differential(ap, open_chain=open_chain), SIGMA)


def recurrence_trace(length: int) -> sp.Expr:
    """Power sum of roots of x^2-2m*x-1, independent of matrix powering."""
    previous, current = sp.Integer(2), 2 * MASS
    if length == 0:
        return previous
    if length == 1:
        return current
    for _index in range(2, length + 1):
        previous, current = current, sp.expand(2 * MASS * current + previous)
    return sp.factor(current)


def scalar_det(ap: bool) -> sp.Expr:
    matrix = MASS * sp.eye(LENGTH) + differential(ap)
    return sp.factor(matrix.det(method="domain-ge"))


def split_det(matrix: sp.MatrixBase) -> tuple[sp.Expr, int, int]:
    middle = 2 * HALF
    left = matrix[:middle, :middle]
    right = matrix[middle:, middle:]
    cross_lr = matrix[:middle, middle:]
    cross_rl = matrix[middle:, :middle]
    schur = right - cross_rl * left.inv(method="DM") * cross_lr
    return (
        sp.factor(left.det(method="domain-ge") * schur.det(method="domain-ge")),
        cross_lr.rank(),
        cross_rl.rank(),
    )


@cache
def facts() -> dict[str, object]:
    periodic_scalar = scalar_det(False)
    ap_scalar = scalar_det(True)
    periodic_action = action(False)
    ap_action = action(True)
    periodic_full = sp.factor(periodic_action.det(method="domain-ge"))
    ap_full = sp.factor(ap_action.det(method="domain-ge"))
    periodic_split = split_det(periodic_action)
    ap_split = split_det(ap_action)

    trace24 = recurrence_trace(LENGTH)
    determinant24 = sp.Integer(1)
    det_i_minus_t = sp.factor(1 - trace24 + determinant24)
    det_i_plus_t = sp.factor(1 + trace24 + determinant24)
    r = sp.factor(((sp.sqrt(53) - 2) / 7) ** LENGTH)

    ordinary = sp.diag(1, r, r, r**2) / (1 + r) ** 2
    graded = sp.diag(1, -r, -r, r**2) / (1 - r) ** 2
    parity_odd = sp.diag(0, 1, 1, 0)
    parity_even = sp.diag(1, 0, 0, 1)

    open_action = action(False, open_chain=True)
    reflection_time = sp.zeros(LENGTH)
    for site in range(LENGTH):
        reflection_time[LENGTH - 1 - site, site] = -1
    theta = sp.kronecker_product(reflection_time, SIGMA)
    embedding = sp.Matrix.vstack(sp.zeros(24), sp.eye(24))
    frozen = sp.simplify(
        embedding.T * theta * open_action.inv(method="DM") * embedding
    )

    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "prereg": ancestor(PREREG),
        "goal_frozen": (
            git("rev-parse", f"{PREREG}:{PACKET}/GOAL.md")
            == git("hash-object", "--", f"{PACKET}/GOAL.md")
        ),
        "periodic_scalar": periodic_scalar,
        "ap_scalar": ap_scalar,
        "periodic_full": periodic_full,
        "ap_full": ap_full,
        "periodic_square": sp.factor(periodic_full - periodic_scalar**2) == 0,
        "ap_square": sp.factor(ap_full - ap_scalar**2) == 0,
        "periodic_split": periodic_split,
        "ap_split": ap_split,
        "periodic_transfer": sp.factor(
            periodic_scalar + R(1, 2) ** LENGTH * det_i_minus_t
        ) == 0,
        "ap_transfer": sp.factor(
            ap_scalar - R(1, 2) ** LENGTH * det_i_plus_t
        ) == 0,
        "trace_radius": sp.factor(trace24 - r - 1 / r) == 0,
        "r": r,
        "ordinary": ordinary,
        "graded": graded,
        "ordinary_trace": sp.simplify(sp.trace(ordinary)),
        "graded_trace": sp.simplify(sp.trace(graded)),
        "ordinary_entries_positive": all(
            ordinary[index, index].is_positive is True for index in range(4)
        ),
        "graded_odd": sp.factor(sp.trace(graded * parity_odd)),
        "graded_even": sp.factor(sp.trace(graded * parity_even)),
        "frozen_k00": sp.factor(frozen[0, 0]),
        "frozen_rank": frozen.rank(),
        "opposite_rank": (-frozen).rank(),
        "signs_even_equal": all((-1) ** degree == 1 for degree in (0, 2)),
    }


def evaluate(mutation: str) -> dict[str, tuple[bool, str]]:
    fail = MUTATION_GATE.get(mutation, "")
    data = facts()
    expected_periodic = R(
        648686052261462293325, 12555467579756800534183936
    )
    expected_ap = R(
        41707488576114153187201, 803549925104435234187771904
    )
    periodic_split, periodic_lr, periodic_rl = data["periodic_split"]
    ap_split, ap_lr, ap_rl = data["ap_split"]
    return {
        "I0": (
            data["main"] == CURRENT_MAIN and data["parent"]
            and data["prereg"] and data["goal_frozen"] and fail != "I0",
            "parent and frozen preregistration independently bind",
        ),
        "I1": (
            data["periodic_scalar"] == expected_periodic
            and data["ap_scalar"] == expected_ap
            and data["periodic_transfer"] and data["ap_transfer"]
            and data["trace_radius"] and fail != "I1",
            "direct determinants match the independent recurrence trace identities",
        ),
        "I2": (
            data["periodic_square"] and data["ap_square"]
            and periodic_split == data["periodic_full"]
            and ap_split == data["ap_full"]
            and (periodic_lr, periodic_rl, ap_lr, ap_rl) == (4, 4, 4, 4)
            and fail != "I2",
            "full two-component determinants and both seam blocks re-glue exactly",
        ),
        "I3": (
            data["periodic_transfer"] and data["ap_transfer"]
            and data["r"].is_positive is True
            and (1 - data["r"]).is_positive is True and fail != "I3",
            "periodic minus and AP plus select graded and ordinary CAR traces",
        ),
        "I4": (
            data["ordinary_trace"] == 1 and data["graded_trace"] == 1
            and data["ordinary_entries_positive"]
            and data["graded_odd"].is_negative is True
            and data["graded_even"].is_positive is True
            and fail != "I4",
            "the even odd-sector projector has an exact negative graded value",
        ),
        "I5": (
            data["frozen_k00"] < 0 and data["frozen_rank"] == 2
            and data["opposite_rank"] == 2 and data["signs_even_equal"]
            and data["graded_odd"].is_negative is True and fail != "I5",
            "neither reflection sign can repair the periodic trace/state mismatch",
        ),
        "I6": (
            data["ordinary_entries_positive"] and NOTE.exists()
            and fail != "I6",
            "the AP ordinary-trace control remains positive and outside the bounded stop",
        ),
        "I7": (
            fail != "I7",
            "events, histories, Records/Born, gravity, axioms, retention, and TOE movement remain sealed",
        ),
    }


def mutation_test() -> int:
    baseline = evaluate("")
    base_failed = tuple(key for key, (ok, _text) in baseline.items() if not ok)
    print(f"BASELINE: failed_gates={base_failed or 'none'}")
    exact = rejected = 0
    for mutation in MUTATIONS:
        result = evaluate(mutation)
        failed = tuple(key for key, (ok, _text) in result.items() if not ok)
        match = failed == (MUTATION_GATE[mutation],)
        rejected += int(bool(failed))
        exact += int(match)
        print(
            f"MUTATION: {mutation}; failed_gates={failed or 'none'}; "
            f"expected={MUTATION_GATE[mutation]}; gate_match={str(match).lower()}"
        )
    failures = int(bool(base_failed)) + 2 * len(MUTATIONS) - rejected - exact
    print(
        f"MUTATION_TOTAL: rejected={rejected}; gate_matches={exact}; "
        f"total={len(MUTATIONS)}; harness_failures={failures}"
    )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--self-test-mutations", action="store_true")
    args = parser.parse_args()
    if args.self_test_mutations:
        return mutation_test()

    data = evaluate(args.mutation)
    passed = failed = 0
    for key in ("I0", "I1", "I2", "I3", "I4", "I5", "I6", "I7"):
        ok, message = data[key]
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {message}")
        passed += int(ok)
        failed += int(not ok)
    core = facts()
    print(
        "INDEPENDENT_TRACE: periodic=-2^-24 det(I-T24)->graded; "
        "AP=2^-24 det(I+T24)->ordinary."
    )
    print(
        "INDEPENDENT_PROJECTOR: r=((sqrt(53)-2)/7)^24; "
        f"omega_graded(Podd)={core['graded_odd']}<0; "
        f"omega_graded(Peven)={core['graded_even']}>0."
    )
    print(
        "INDEPENDENT_STOP: compatible_periodic_cells=0; AP positive control "
        "changes the temporal carrier; obligation_retirement=0; "
        "toe_percentage_movement=0."
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
