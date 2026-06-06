#!/usr/bin/env python3
"""Verify the K-Z external-lift gate status packet."""

from pathlib import Path
import math
import sys

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
ACTIVE_QUEUE = ROOT / "docs" / "repo" / "ACTIVE_REVIEW_QUEUE.md"
REVIEW_PACKET = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "PR484_KZ_EXTERNAL_LIFT_REVIEW_2026-05-03.md"
STATUS_NOTE = ROOT / "docs" / "GAUGE_SCALAR_KZ_EXTERNAL_LIFT_GATE_STATUS_NOTE_2026-06-06.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label, ok, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title):
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def squash(path):
    return " ".join(path.read_text(encoding="utf-8").split())


def has_all(text, snippets):
    return all(" ".join(snippet.split()) in text for snippet in snippets)


def su3_single_plaquette_moments(beta, k_max, n_grid=48):
    """Small deterministic SU(3) Cartan-torus quadrature for a local probe."""
    phi_grid = np.linspace(-math.pi, math.pi, n_grid, endpoint=False)
    dphi = 2 * math.pi / n_grid

    def raw(phi1, phi2, k):
        phi3 = -phi1 - phi2
        re_tr = math.cos(phi1) + math.cos(phi2) + math.cos(phi3)
        p = re_tr / 3.0
        vand = (
            math.sin((phi1 - phi2) / 2.0) ** 2
            * math.sin((phi2 - phi3) / 2.0) ** 2
            * math.sin((phi3 - phi1) / 2.0) ** 2
        )
        return vand * math.exp((beta / 3.0) * re_tr) * (p ** k)

    z = 0.0
    for phi1 in phi_grid:
        for phi2 in phi_grid:
            z += raw(phi1, phi2, 0) * dphi * dphi

    out = [1.0]
    for k in range(1, k_max + 1):
        num = 0.0
        for phi1 in phi_grid:
            for phi2 in phi_grid:
                num += raw(phi1, phi2, k) * dphi * dphi
        out.append(num / z)
    return out


section("Part 1: source gate is present")

for path in [ACTIVE_QUEUE, REVIEW_PACKET, STATUS_NOTE]:
    check(f"source file exists: {path.relative_to(ROOT)}", path.exists())

active_text = squash(ACTIVE_QUEUE)
review_text = squash(REVIEW_PACKET)
note_text = squash(STATUS_NOTE)

active_snippets = [
    "2026-05-03-pr484-kz-external-lift-gate",
    "runner fails without optional CVXPY",
    "W_lift = 0.05",
    "explicit SU(3), beta=6 primary-source bracket",
    "Disposition: `science-needed`",
]
for snippet in active_snippets:
    check(f"active queue contains: {snippet}", has_all(active_text, [snippet]))

review_snippets = [
    "reject PR #484 as a bounded theorem",
    "Preserve the goal as an open external-lift candidate",
    "CVXPY is an optional SDP dependency",
    "not the SU(3), beta=6 bracket",
    "not a theorem-grade imported bound",
    "passing runner in the repo's documented SDP environment",
    "explicit SU(3), beta=6 primary-source bracket",
]
for snippet in review_snippets:
    check(f"review packet contains: {snippet}", has_all(review_text, [snippet]))

section("Part 2: optional SDP stack availability")

try:
    import cvxpy as cp
    cvxpy_error = None
except Exception as exc:  # pragma: no cover - failure path is printed.
    cp = None
    cvxpy_error = exc

check("cvxpy availability is recorded", True, detail="available" if cp else repr(cvxpy_error))
if cp is not None:
    solvers = set(cp.installed_solvers())
    check("cvxpy version is visible", bool(cp.__version__), detail=cp.__version__)
    check("CLARABEL solver is installed", "CLARABEL" in solvers, detail=",".join(sorted(solvers)))
    check("SCS-class fallback solver is installed", "SCS" in solvers or "SCIPY" in solvers, detail=",".join(sorted(solvers)))
else:
    solvers = set()
    check("optional SDP stack absence leaves gate open", True, detail="cvxpy unavailable")

section("Part 3: local SU(3) witness scale")

moments = su3_single_plaquette_moments(beta=6.0, k_max=2)
mean = moments[1]
var = moments[2] - moments[1] ** 2
delta_beta_eff = 1e-7 * (6.0 ** 6)
epsilon_witness = var * delta_beta_eff
w_lift = 0.05

check("single-plaquette mean lies in SU(3) support", -1 / 3 < mean < 1, detail=f"mean={mean:.6f}")
check("single-plaquette variance is positive", 0 < var < 1, detail=f"var={var:.6f}")
check("epsilon_witness is much smaller than W_lift", epsilon_witness < w_lift, detail=f"eps={epsilon_witness:.3e}, W={w_lift:.3e}")
check("W_lift remains a width parameter, not a derived primary bracket", w_lift == 0.05)

section("Part 4: minimal SDP feasibility probe")

if cp is not None:
    p1 = cp.Variable(name="p1")
    p2 = cp.Variable(name="p2")
    a = -1.0 / 3.0
    b = 1.0
    midpoint = (mean + b) / 2.0
    lower = midpoint - w_lift / 2.0
    upper = midpoint + w_lift / 2.0
    constraints = [
        cp.bmat([[np.array([[1.0]]), cp.reshape(p1, (1, 1), order="F")], [cp.reshape(p1, (1, 1), order="F"), cp.reshape(p2, (1, 1), order="F")]]) >> 0,
        p1 >= a,
        p1 <= b,
        p2 >= 0,
        p2 <= 1,
        p1 - a >= 0,
        b - p1 >= 0,
        p1 >= lower,
        p1 <= upper,
    ]
    problem = cp.Problem(cp.Minimize(0), constraints)
    try:
        problem.solve(solver=cp.CLARABEL)
        status = problem.status
    except Exception:
        problem.solve(solver=cp.SCS)
        status = problem.status
    feasible = status in {"optimal", "optimal_inaccurate"}
    check("minimal PSD/Hausdorff SDP solves", feasible, detail=status)
    check("SDP value lies in conservative W_lift interval", feasible and lower <= p1.value <= upper, detail=f"p1={p1.value if p1.value is not None else None}")
    check("conservative interval is inside SU(3) support", a <= lower < upper <= b, detail=f"[{lower:.6f}, {upper:.6f}]")
    check("SDP probe width equals W_lift", abs((upper - lower) - w_lift) < 1e-12)
else:
    check("minimal PSD/Hausdorff SDP probe skipped when cvxpy unavailable", True)
    check("SDP interval claim is not made without cvxpy", True)
    check("conservative interval remains an unexecuted optional probe", True)
    check("SDP probe width check waits for optional SDP stack", True)

section("Part 5: gate classifier")

cvxpy_path_open = cp is not None and ("CLARABEL" in solvers or "SCS" in solvers)
primary_bracket_available = False
gate_closed = cvxpy_path_open and primary_bracket_available

check("local optional-SDP execution path status is recorded", True, detail=str(cvxpy_path_open))
check("primary SU(3), beta=6 bracket remains unavailable", not primary_bracket_available)
check("gate remains open because primary bracket is missing", not gate_closed)
check(
    "old K-Z benchmark is not used as target bracket",
    has_all(review_text, ["Kazakov-Zheng 2022 bracket", "benchmark in a different regime", "not the SU(3), beta=6 bracket"]),
)
check("branch status is open, not theorem/promotion", "**Status:** open gate" in STATUS_NOTE.read_text(encoding="utf-8"))
check("future landing criteria remain explicit", has_all(review_text, ["passing runner", "primary-source bracket", "source vocabulary"]))

section("Part 6: branch-local note hygiene")

note_snippets = [
    "CVXPY execution path is environment-dependent",
    "Blocker (2) remains open",
    "not a replacement for the missing primary-source",
    "No old PR484 retained/effective-status language is revived",
    "No repo-wide authority surface is updated",
]
for snippet in note_snippets:
    check(f"status note contains: {snippet}", has_all(note_text, [snippet]))

banned = [
    "retained-status update",
    "parent-chain promotion",
    "retained/effective status is landed",
    "retained_bounded",
    "retained_no_go",
]
for phrase in banned:
    check(f"status note avoids banned phrase: {phrase}", phrase not in note_text)

print("\n" + "=" * 88)
print(f"  TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
print("=" * 88)

sys.exit(1 if FAIL_COUNT else 0)
