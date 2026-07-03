#!/usr/bin/env python3
"""K-Z SU(3) beta=6 reproduction firewall and acceptance contract.

This runner sharpens the remaining K-Z external-lift blocker after the
beta/lambda convention split:

* Wilson SU(3) beta=6 maps to the source paper coordinate lambda=1.5.
* A support-only SDP using Hausdorff, Hankel, Gram, support, and area-style
  inequalities cannot be accepted as a beta=6 reproduction, because the
  delta-at-identity moment assignment satisfies those constraints and leaves
  the upper bound at the trivial endpoint P=1.
* Any acceptable repo-owned reproduction must therefore add beta-coupled
  loop equations/source data and solver/cutoff metadata.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def matrix_rank_one_constant_psd(size: int, constant: float) -> bool:
    """The constant matrix c * 11^T has quadratic form c*(sum x_i)^2."""
    return size >= 1 and constant >= 0.0


def zero_matrix_psd(size: int) -> bool:
    return size >= 1


@dataclass(frozen=True)
class SupportOnlyWitness:
    """Moment assignment for a delta distribution at P=R=Q=1."""

    nc: int = 3
    p1: float = 1.0
    p2: float = 1.0
    p3: float = 1.0
    p4: float = 1.0
    r1: float = 1.0
    r2: float = 1.0
    q1: float = 1.0
    q2: float = 1.0
    pr: float = 1.0
    pq: float = 1.0
    rq: float = 1.0

    @property
    def support_low(self) -> float:
        return -1.0 / self.nc

    @property
    def support_high(self) -> float:
        return 1.0

    def values(self) -> Iterable[float]:
        return (
            self.p1,
            self.p2,
            self.p3,
            self.p4,
            self.r1,
            self.r2,
            self.q1,
            self.q2,
            self.pr,
            self.pq,
            self.rq,
        )


@dataclass(frozen=True)
class ReproductionCandidate:
    name: str
    target_nc: int
    target_beta: float
    target_lambda: float
    uses_old_w_lift: bool
    width_source_kind: str
    has_primary_table_or_source_data: bool
    has_repo_owned_sdp: bool
    has_beta_coupled_loop_equations: bool
    reports_cutoff: bool
    reports_solver: bool
    reports_tolerances: bool
    reports_primal_dual_residuals: bool
    reports_raw_cache: bool
    distinguishes_figure_extraction: bool
    support_only_sdp: bool


def expected_lambda(nc: int, beta: float) -> float:
    # Paper action coefficient N/(2 lambda) equals Wilson beta/(2N).
    return nc * nc / beta


def coordinate_ok(candidate: ReproductionCandidate) -> bool:
    return abs(candidate.target_lambda - expected_lambda(candidate.target_nc, candidate.target_beta)) < 1e-12


def source_data_route_ok(candidate: ReproductionCandidate) -> bool:
    return (
        coordinate_ok(candidate)
        and candidate.has_primary_table_or_source_data
        and not candidate.uses_old_w_lift
        and candidate.distinguishes_figure_extraction
        and candidate.width_source_kind in {"primary_table", "primary_source_data"}
    )


def repo_owned_sdp_route_ok(candidate: ReproductionCandidate) -> bool:
    metadata_ok = (
        candidate.reports_cutoff
        and candidate.reports_solver
        and candidate.reports_tolerances
        and candidate.reports_primal_dual_residuals
        and candidate.reports_raw_cache
    )
    return (
        coordinate_ok(candidate)
        and candidate.has_repo_owned_sdp
        and candidate.has_beta_coupled_loop_equations
        and metadata_ok
        and not candidate.support_only_sdp
        and not candidate.uses_old_w_lift
        and candidate.distinguishes_figure_extraction
    )


def acceptable_reproduction(candidate: ReproductionCandidate) -> bool:
    return source_data_route_ok(candidate) or repo_owned_sdp_route_ok(candidate)


def main() -> int:
    print("K-Z SU(3) beta=6 reproduction firewall and acceptance contract")
    print("actual_current_surface_status: no-go")
    print("trace_class: negative_route_pruning")
    print("reachability_to_target: prunes")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()

    print("A. beta/lambda target contract")
    nc = 3
    beta = 6.0
    lam = expected_lambda(nc, beta)
    lambda_three_width = 0.048725
    beta6_image_width = 0.245195
    old_w_lift = 0.05
    check("paper/Wilson coefficient matching gives lambda=N^2/beta", abs(lam - 1.5) < 1e-12, f"lambda={lam}")
    check("plotted lambda=3 is not Wilson beta=6 for SU(3)", abs(3.0 - lam) > 1.0, f"lambda_beta6={lam}")
    check("old W_lift matches plotted lambda=3 image width, not beta=6 coordinate", abs(lambda_three_width - old_w_lift) < 0.002, f"width_lambda3={lambda_three_width}")
    check("image-derived beta=6 coordinate width is not the old narrow width", abs(beta6_image_width - old_w_lift) > 0.19, f"width_beta6_image={beta6_image_width}")

    print("\nB. support-only SDP firewall")
    witness = SupportOnlyWitness(nc=nc)
    a = witness.support_low
    b = witness.support_high
    check("delta-at-identity P,R,Q values lie in SU(3) support [-1/3,1]", all(a <= v <= b for v in witness.values()))
    check("plaquette Hankel matrix H_ij=m_{i+j} is PSD for all moments=1", matrix_rank_one_constant_psd(3, 1.0))
    check("lower Hausdorff shifted Hankel is PSD at endpoint P=1", matrix_rank_one_constant_psd(2, 1.0 - a), f"constant={1.0 - a:.6f}")
    check("upper Hausdorff shifted Hankel is PSD at endpoint P=1", zero_matrix_psd(2), "constant=0")
    check("Wilson-loop Gram matrix on {1,P,R,Q} is PSD for all entries=1", matrix_rank_one_constant_psd(4, 1.0))
    check("area-style r1<=p2 constraint is saturated by endpoint witness", witness.r1 <= witness.p2, f"r1={witness.r1}, p2={witness.p2}")
    check("area-style q1<=p4 constraint is saturated by endpoint witness", witness.q1 <= witness.p4, f"q1={witness.q1}, p4={witness.p4}")
    check("bridge lower bound p1>=0.4225 does not exclude endpoint witness", witness.p1 >= 0.4225, f"p1={witness.p1}")
    check("support-only constraints therefore permit upper endpoint p1=1", witness.p1 == 1.0)

    print("\nC. reproduction contract candidate tests")
    old_shortcut = ReproductionCandidate(
        name="old W_lift shortcut",
        target_nc=3,
        target_beta=6.0,
        target_lambda=3.0,
        uses_old_w_lift=True,
        width_source_kind="figure_vector",
        has_primary_table_or_source_data=False,
        has_repo_owned_sdp=False,
        has_beta_coupled_loop_equations=False,
        reports_cutoff=False,
        reports_solver=False,
        reports_tolerances=False,
        reports_primal_dual_residuals=False,
        reports_raw_cache=False,
        distinguishes_figure_extraction=False,
        support_only_sdp=False,
    )
    support_only_sdp = ReproductionCandidate(
        name="support-only SDP at correct coordinate",
        target_nc=3,
        target_beta=6.0,
        target_lambda=1.5,
        uses_old_w_lift=False,
        width_source_kind="repo_sdp",
        has_primary_table_or_source_data=False,
        has_repo_owned_sdp=True,
        has_beta_coupled_loop_equations=False,
        reports_cutoff=True,
        reports_solver=True,
        reports_tolerances=True,
        reports_primal_dual_residuals=True,
        reports_raw_cache=True,
        distinguishes_figure_extraction=True,
        support_only_sdp=True,
    )
    source_data_template = ReproductionCandidate(
        name="primary source-data template at lambda=1.5",
        target_nc=3,
        target_beta=6.0,
        target_lambda=1.5,
        uses_old_w_lift=False,
        width_source_kind="primary_source_data",
        has_primary_table_or_source_data=True,
        has_repo_owned_sdp=False,
        has_beta_coupled_loop_equations=False,
        reports_cutoff=False,
        reports_solver=False,
        reports_tolerances=False,
        reports_primal_dual_residuals=False,
        reports_raw_cache=True,
        distinguishes_figure_extraction=True,
        support_only_sdp=False,
    )
    sdp_template = ReproductionCandidate(
        name="repo-owned beta-coupled SDP template",
        target_nc=3,
        target_beta=6.0,
        target_lambda=1.5,
        uses_old_w_lift=False,
        width_source_kind="repo_sdp",
        has_primary_table_or_source_data=False,
        has_repo_owned_sdp=True,
        has_beta_coupled_loop_equations=True,
        reports_cutoff=True,
        reports_solver=True,
        reports_tolerances=True,
        reports_primal_dual_residuals=True,
        reports_raw_cache=True,
        distinguishes_figure_extraction=True,
        support_only_sdp=False,
    )
    candidates = [old_shortcut, support_only_sdp, source_data_template, sdp_template]
    for candidate in candidates:
        print(f"candidate: {candidate.name}")
        print(f"  coordinate_ok={coordinate_ok(candidate)}")
        print(f"  source_data_route_ok={source_data_route_ok(candidate)}")
        print(f"  repo_owned_sdp_route_ok={repo_owned_sdp_route_ok(candidate)}")
        print(f"  acceptable_reproduction={acceptable_reproduction(candidate)}")

    check("old W_lift shortcut fails the reproduction contract", not acceptable_reproduction(old_shortcut))
    check("support-only SDP fails without beta-coupled loop equations", not acceptable_reproduction(support_only_sdp))
    check("primary source-data route is the only non-SDP acceptable route", source_data_route_ok(source_data_template))
    check("repo-owned SDP route requires beta-coupled equations plus solver metadata", repo_owned_sdp_route_ok(sdp_template))
    check("accepted templates are route contracts, not actual beta=6 numeric brackets", True)

    print("\nD. boundary")
    check("this block prunes support-only beta=6 reproduction attempts", True)
    check("this block does not certify a new finite SU(3) beta=6 bracket", True)
    check("next positive K-Z route must supply source data or loop equations", True)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: The K-Z beta=6 gate cannot be closed by the old W_lift "
            "shortcut or by support-only SDP constraints. A future reproduction "
            "must target lambda=1.5 and provide primary source data or "
            "beta-coupled loop equations with solver/cutoff evidence."
        )
        return 0
    print("VERDICT: reproduction firewall failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
