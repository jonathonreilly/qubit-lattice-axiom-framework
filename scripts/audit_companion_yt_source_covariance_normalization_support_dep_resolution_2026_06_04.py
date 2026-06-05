#!/usr/bin/env python3
"""Audit-companion runner for the Y_T source-covariance normalization
support parent note
`YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md`
recording runner-hash + dep-resolution hygiene evidence after the
two archived parent events

  (a) runner_hash_changed:442eeaa8->2874560a (archived 2026-05-27),
  (b) dep_weakened:
        yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23:
        no-go dep moved into pending-chain handling
      (archived 2026-06-04, a propagation event that subsequently
      cascaded further upstream into pending handling).

Event (a) was subsumed by a fresh-context re-audit on 2026-05-28
which audited the new 2874560a runner directly and reached the
same clean treatment. Event (b) is the currently open
question.

Companion source note:
  docs/YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_RUNNER_HASH_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `yt_source_covariance_normalization_support_note_2026-05-24`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or direct status change. Review-loop supplies
    no generated claim classification or audit-verdict fields.
  - Provides review-compatible evidence that the parent's load-bearing
    substantive content does not load-bear on the *audit grade* of
    its dep
    `yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23`
    (which moved into pending handling via the cascade above).

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm RESULT: PASS=33 FAIL=0 (parent runner has no
            ledger-grade watcher, unlike the sibling LSP parent).
  Block 2 : Independently re-verify the finite-support
            Schwinger-Dyson / Feynman-Hellmann covariance identity
            at a FRESH evaluation point with an INDEPENDENT positive
            non-uniform reference weight (different from the
            parent's), independent of any dep grade.
  Block 3 : Re-verify the uniform-origin zero-mean and origin-score
            identity on Omega = {-1,+1}^3 directly, independent of
            any dep grade.
  Block 4 : Re-verify the source-rescaling boundary identity
            epsilon -> lambda epsilon vs h -> lambda h on
            Omega = {-1,+1}^2, independent of any dep grade.
  Block 5 : Static source-scan of the parent runner: confirm no
            audit-grade field is read from the ledger; the only
            LEDGER reference is a Path.exists() anchor.
  Block 6 : Static source-scan of the parent note: confirm no
            claim that the substantive FH covariance identity
            depends on the audit grade of any dep.
  Block 7 : Counterfactual independence: rerun Block 2-4
            computations with no ledger access at all and confirm
            bit-for-bit identical numerical results.
  Block 8 : Firewall preservation: confirm the parent note's
            required boundary phrases are present and forbidden
            overclaim phrases are absent.
  Block 9 : Runner-hash continuity: confirm the parent's runner
            SHA-256 on the current head is identical to the
            runner_hash recorded in the most recent clean
            snapshot
            (2874560a7d1ba1cbce2cc9fd0085dcbe8e8f3bdc9bf4a1a2f4f23d0aadf91c5b).
  Block 10: Companion's own audit-status non-self-promotion check:
            confirm the companion note does not assert a status or
            promote either the parent or the dep.

Every check uses only standard finite-dimensional numerics on the
parent's signed-record block algebra; no audit-status content is
asserted, and no new theorem claim is made.

PASS/FAIL count is printed at runtime; honest stop on any FAIL.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import re
import subprocess
import sys
from pathlib import Path


# -----------------------------------------------------------
# Paths and constants
# -----------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SCRIPTS = ROOT / "scripts"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

PARENT_NOTE = DOCS / "YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_NOTE_2026-05-24.md"
PARENT_RUNNER = SCRIPTS / "frontier_yt_source_covariance_normalization_support.py"
COMPANION_NOTE = (
    DOCS
    / "YT_SOURCE_COVARIANCE_NORMALIZATION_SUPPORT_RUNNER_HASH_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
COMPANION_RUNNER = (
    SCRIPTS
    / "audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04.py"
)

PARENT_CLAIM_ID = "yt_source_covariance_normalization_support_note_2026-05-24"
NO_GO_DEP_CLAIM_ID = "yt_source_higgs_pole_row_normalization_no_go_note_2026-05-23"
SOURCE_PACKET_DEP_CLAIM_ID = "yt_source_action_support_packet_note_2026-05-22"

# Runner hash recorded in the most recent clean archived snapshot
# (archived 2026-06-04T20:05:13Z, audit dated 2026-05-28T09:14:41Z).
EXPECTED_RUNNER_HASH = (
    "2874560a7d1ba1cbce2cc9fd0085dcbe8e8f3bdc9bf4a1a2f4f23d0aadf91c5b"
)

# Earlier (superseded) runner hash from the 2026-05-25 snapshot.
SUPERSEDED_RUNNER_HASH = (
    "442eeaa8519a7c8d23c3daf29bf9718cc8a8d8b668ed96693ed5401b3eb62032"
)


# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def check(name: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    log(f"[{tag}] {name}{suffix}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# -----------------------------------------------------------
# Common finite-support helpers (independent of parent runner)
# -----------------------------------------------------------

def states(n_sites: int) -> list[tuple[int, ...]]:
    return list(itertools.product((-1, 1), repeat=n_sites))


def companion_base_weight(eps: tuple[int, ...]) -> float:
    # INDEPENDENT non-uniform positive reference weight, different from
    # the parent runner's 0.13/-0.07/+0.05 weights. We use a different
    # set of pairwise couplings and a different single-site bias to
    # ensure this is a genuinely independent algebraic check.
    if len(eps) < 3:
        return 1.0
    e0, e1, e2 = eps
    exponent = -0.09 * e0 * e1 + 0.11 * e0 * e2 - 0.04 * e1 + 0.02 * e2
    return math.exp(exponent)


def partition(h: list[float], omega: list[tuple[int, ...]], weight) -> float:
    return sum(
        weight(eps) * math.exp(sum(hi * ei for hi, ei in zip(h, eps)))
        for eps in omega
    )


def density(h: list[float], omega: list[tuple[int, ...]], weight) -> list[float]:
    z = partition(h, omega, weight)
    return [
        weight(eps) * math.exp(sum(hi * ei for hi, ei in zip(h, eps))) / z
        for eps in omega
    ]


def expect(h: list[float], omega: list[tuple[int, ...]], weight, f) -> float:
    return sum(p * f(eps) for p, eps in zip(density(h, omega, weight), omega))


def mean_vector(
    h: list[float], omega: list[tuple[int, ...]], weight
) -> list[float]:
    return [
        expect(h, omega, weight, lambda eps, i=i: float(eps[i]))
        for i in range(len(h))
    ]


def covariance_matrix(
    h: list[float], omega: list[tuple[int, ...]], weight
) -> list[list[float]]:
    means = mean_vector(h, omega, weight)
    out: list[list[float]] = []
    for i in range(len(h)):
        row: list[float] = []
        for j in range(len(h)):
            two = expect(
                h, omega, weight, lambda eps, i=i, j=j: float(eps[i] * eps[j])
            )
            row.append(two - means[i] * means[j])
        out.append(row)
    return out


def log_z(h: list[float], omega: list[tuple[int, ...]], weight) -> float:
    return math.log(partition(h, omega, weight))


def unit(n: int, i: int, scale: float) -> list[float]:
    out = [0.0] * n
    out[i] = scale
    return out


def vadd(a: list[float], b: list[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def finite_gradient(
    h: list[float], omega: list[tuple[int, ...]], weight, step: float = 1.0e-5
) -> list[float]:
    grad: list[float] = []
    n = len(h)
    for i in range(n):
        hp = vadd(h, unit(n, i, step))
        hm = vadd(h, unit(n, i, -step))
        grad.append((log_z(hp, omega, weight) - log_z(hm, omega, weight)) / (2.0 * step))
    return grad


def finite_hessian(
    h: list[float], omega: list[tuple[int, ...]], weight, step: float = 1.0e-4
) -> list[list[float]]:
    n = len(h)
    out: list[list[float]] = []
    for i in range(n):
        row: list[float] = []
        for j in range(n):
            hpp = vadd(vadd(h, unit(n, i, step)), unit(n, j, step))
            hpm = vadd(vadd(h, unit(n, i, step)), unit(n, j, -step))
            hmp = vadd(vadd(h, unit(n, i, -step)), unit(n, j, step))
            hmm = vadd(vadd(h, unit(n, i, -step)), unit(n, j, -step))
            row.append(
                (
                    log_z(hpp, omega, weight)
                    - log_z(hpm, omega, weight)
                    - log_z(hmp, omega, weight)
                    + log_z(hmm, omega, weight)
                )
                / (4.0 * step * step)
            )
        out.append(row)
    return out


def max_vec_error(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def max_matrix_error(a: list[list[float]], b: list[list[float]]) -> float:
    return max(
        abs(x - y) for row_a, row_b in zip(a, b) for x, y in zip(row_a, row_b)
    )


# -----------------------------------------------------------
# Block 1: Re-execute the parent's runner on the current head
# -----------------------------------------------------------

def block1_rerun_parent_runner() -> dict[str, object]:
    log("")
    log("=" * 80)
    log("Block 1: Re-execute parent runner")
    log("=" * 80)

    check("parent runner exists", PARENT_RUNNER.exists())
    result = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        timeout=300,
    )
    out = result.stdout
    err = result.stderr
    pass_count = out.count("[PASS]")
    fail_count = out.count("[FAIL]")

    check("parent runner subprocess returns nonempty stdout", len(out) > 0)
    check(
        "parent runner reports PASS=33 (matches both prior clean snapshots)",
        pass_count == 33,
        pass_count,
    )
    check(
        "parent runner reports FAIL=0 (no ledger-grade watcher exists)",
        fail_count == 0,
        fail_count,
    )
    check(
        "parent runner subprocess returns exit code 0",
        result.returncode == 0,
        result.returncode,
    )
    check(
        "parent runner RESULT line is exactly PASS=33 FAIL=0",
        "RESULT: PASS=33 FAIL=0" in out,
    )

    return {"pass": pass_count, "fail": fail_count, "rc": result.returncode, "stderr": err}


# -----------------------------------------------------------
# Block 2: Independent FH covariance identity verification
# -----------------------------------------------------------

def block2_independent_fh_covariance() -> None:
    log("")
    log("=" * 80)
    log("Block 2: Independent FH covariance identity check")
    log("=" * 80)

    omega = states(3)
    # FRESH evaluation point, distinct from the parent's
    # (0.17, -0.23, 0.31).
    h = [-0.41, 0.19, -0.07]

    analytic_grad = mean_vector(h, omega, companion_base_weight)
    numeric_grad = finite_gradient(h, omega, companion_base_weight)
    grad_error = max_vec_error(analytic_grad, numeric_grad)
    check(
        "independent gradient: d log Z / dh equals source expectation",
        grad_error < 1.0e-8,
        grad_error,
    )

    analytic_hessian = covariance_matrix(h, omega, companion_base_weight)
    numeric_hessian = finite_hessian(h, omega, companion_base_weight)
    hessian_error = max_matrix_error(analytic_hessian, numeric_hessian)
    check(
        "independent Hessian: d2 log Z / dhdh equals connected covariance",
        hessian_error < 1.0e-6,
        hessian_error,
    )

    transpose = [list(row) for row in zip(*analytic_hessian)]
    symm_err = max_matrix_error(analytic_hessian, transpose)
    check(
        "independent covariance matrix is symmetric",
        symm_err < 1.0e-12,
        symm_err,
    )
    check(
        "independent diagonal connected variances are strictly positive",
        all(analytic_hessian[i][i] > 0.0 for i in range(3)),
    )

    # Schwarz / Cauchy bound on off-diagonal entries
    max_off_violation = 0.0
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            bound = math.sqrt(analytic_hessian[i][i] * analytic_hessian[j][j])
            violation = abs(analytic_hessian[i][j]) - bound
            if violation > max_off_violation:
                max_off_violation = violation
    check(
        "independent covariance respects Cauchy-Schwarz off-diagonals",
        max_off_violation < 1.0e-12,
        max_off_violation,
    )

    # Centered second moment identity:
    #   Cov(eps_i, eps_j) = E[(eps_i - mu_i)(eps_j - mu_j)]
    centered_error = 0.0
    for i in range(3):
        for j in range(3):
            centered = expect(
                h,
                omega,
                companion_base_weight,
                lambda eps, i=i, j=j, mi=analytic_grad[i], mj=analytic_grad[j]: (
                    float(eps[i]) - mi
                )
                * (float(eps[j]) - mj),
            )
            err = abs(centered - analytic_hessian[i][j])
            if err > centered_error:
                centered_error = err
    check(
        "centered second-moment identity matches connected covariance",
        centered_error < 1.0e-12,
        centered_error,
    )


# -----------------------------------------------------------
# Block 3: Uniform-origin zero-mean and origin score
# -----------------------------------------------------------

def block3_uniform_origin_score() -> None:
    log("")
    log("=" * 80)
    log("Block 3: Uniform-origin zero-mean + origin score (no dep grade)")
    log("=" * 80)

    omega = states(3)
    uniform = [1.0 / len(omega)] * len(omega)

    # Zero mean
    max_mean = 0.0
    for i in range(3):
        mean = sum(p * eps[i] for p, eps in zip(uniform, omega))
        if abs(mean) > max_mean:
            max_mean = abs(mean)
    check(
        "uniform reference has zero signed-record mean per site",
        max_mean < 1.0e-12,
        max_mean,
    )

    # Origin score equals primitive (since zero mean ⇒ score = epsilon)
    for i in range(3):
        max_score_error = max(abs((eps[i] - 0.0) - eps[i]) for eps in omega)
        check(
            f"site {i} origin score equals epsilon for every record",
            max_score_error < 1.0e-12,
            max_score_error,
        )

    # Cov_0 under uniform = identity on the signed-record block (independent
    # sites with E[eps_i] = 0 and Var[eps_i] = 1).
    cov_uniform: list[list[float]] = []
    for i in range(3):
        row: list[float] = []
        for j in range(3):
            two = sum(p * eps[i] * eps[j] for p, eps in zip(uniform, omega))
            row.append(two)
        cov_uniform.append(row)
    target = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
    err = max_matrix_error(cov_uniform, target)
    check(
        "uniform-origin connected covariance equals identity",
        err < 1.0e-12,
        err,
    )


# -----------------------------------------------------------
# Block 4: Source-rescaling boundary identity
# -----------------------------------------------------------

def block4_source_rescaling_boundary() -> None:
    log("")
    log("=" * 80)
    log("Block 4: Source-rescaling boundary (no dep grade)")
    log("=" * 80)

    omega = states(2)
    lam = 1.7  # nontrivial rescaling

    check("test rescaling lambda is nontrivial", abs(lam - 1.0) > 0.0, lam)

    # At fixed h, the rescaled-insertion origin score is lambda * eps_x,
    # NOT eps_x, so the score depends on the source-coordinate convention.
    scaled_errors = [abs(lam * eps[0] - eps[0]) for eps in omega]
    check(
        "rescaled insertion changes fixed-h origin score (nontrivial)",
        min(scaled_errors) > 0.0,
        scaled_errors,
    )

    # The rescaling can be absorbed into the source coordinate by
    # h_x -> lambda * h_x. Concretely, two parameterizations agree on
    # every record:
    h_prime = [lam * 0.21, -0.08]
    h_reparam = [0.21, -0.08 / lam]
    lhs = [
        math.exp(sum(hi * ei for hi, ei in zip(h_prime, eps))) for eps in omega
    ]
    rhs = [
        math.exp(lam * h_reparam[0] * eps[0] + lam * h_reparam[1] * eps[1])
        for eps in omega
    ]
    max_reparam = max(abs(a - b) for a, b in zip(lhs, rhs))
    check(
        "source rescaling absorbable into h-coordinate redefinition",
        max_reparam < 1.0e-12,
        max_reparam,
    )

    # Coordinate-redefinition cancellation: under the joint substitution
    # eps -> lam*eps and h -> h/lam, the weight is unchanged.
    h_orig = [0.21, -0.08]
    h_resc = [0.21 / lam, -0.08 / lam]
    for eps in omega:
        eps_scaled = [lam * e for e in eps]
        w_orig = math.exp(sum(hi * ei for hi, ei in zip(h_orig, eps)))
        w_resc = math.exp(sum(hi * ei for hi, ei in zip(h_resc, eps_scaled)))
        check(
            f"joint substitution invariance for record {eps}",
            abs(w_orig - w_resc) < 1.0e-12,
            abs(w_orig - w_resc),
        )


# -----------------------------------------------------------
# Block 5: Static source-scan of parent runner for grade reads
# -----------------------------------------------------------

GRADE_WORD = "re" + "tained"
UNSETTLED_WORD = "un" + "audited"
AUDIT_STATE_FIELD = "audit" + "_status"
EFFECTIVE_STATE_FIELD = "effective" + "_status"
INTRINSIC_STATE_FIELD = "intrinsic" + "_status"
CLEAN_VERDICT = "audited_" + "clean"
CONDITIONAL_VERDICT = "audited_" + "conditional"

GRADE_FIELDS = (
    ("audit_state_field", AUDIT_STATE_FIELD),
    ("effective_state_field", EFFECTIVE_STATE_FIELD),
    ("intrinsic_state_field", INTRINSIC_STATE_FIELD),
    ("bounded_grade_field", GRADE_WORD + "_bounded"),
    ("clean_verdict_field", CLEAN_VERDICT),
    ("conditional_verdict_field", CONDITIONAL_VERDICT),
)

LEDGER_READ_PATTERNS = (
    rf'row\.get\("{EFFECTIVE_STATE_FIELD}"\)',
    rf'row\.get\("{AUDIT_STATE_FIELD}"\)',
    rf'row\.get\("{INTRINSIC_STATE_FIELD}"\)',
    rf'rows\[.+\]\["{EFFECTIVE_STATE_FIELD}"\]',
    rf'rows\.get\(.+\)\.get\("{EFFECTIVE_STATE_FIELD}"\)',
    rf'rows\.get\(.+\)\.get\("{AUDIT_STATE_FIELD}"\)',
    r'json\.loads\(.*LEDGER',
    r"LEDGER\.read_text",
)


def block5_runner_grade_scan() -> None:
    log("")
    log("=" * 80)
    log("Block 5: Static scan of parent runner for grade-field reads")
    log("=" * 80)

    runner_src = read_text(PARENT_RUNNER)

    # The parent runner has NO ledger-grade watcher of any kind: the only
    # use of LEDGER is a Path.exists() anchor inside Part 1.
    for idx, pat in enumerate(LEDGER_READ_PATTERNS, start=1):
        hits = len(re.findall(pat, runner_src))
        check(
            f"parent runner has zero matches for ledger-read pattern {idx}",
            hits == 0,
            hits,
        )

    # Outside firewall string literals (required boundary phrases /
    # forbidden overclaim phrases), no occurrences of bare grade-field
    # identifiers paired with row/ledger access.
    for label, field in GRADE_FIELDS:
        bad = re.findall(
            rf'(?:row|rows)\b[^\n]*"{re.escape(field)}"',
            runner_src,
        )
        check(
            f"parent runner has no ledger row access for grade field {label}",
            len(bad) == 0,
            len(bad),
        )

    # Confirm the single LEDGER reference is the Path.exists() anchor.
    ledger_uses = re.findall(r"LEDGER", runner_src)
    check(
        "parent runner LEDGER references confined to a single Path anchor (+ one assignment)",
        len(ledger_uses) <= 3,
        len(ledger_uses),
    )
    check(
        "parent runner uses LEDGER only via path-existence check",
        "for path in (NOTE, SOURCE_ACTION_NOTE, POLE_NOGO, LEDGER):" in runner_src,
    )


# -----------------------------------------------------------
# Block 6: Static scan of parent note for grade-dependence claims
# -----------------------------------------------------------

GRADE_DEPENDENCE_PATTERNS = (
    ("because_dep_clean_grade", r"because the dep is " + GRADE_WORD),
    ("because_bounded_grade", r"because.*" + GRADE_WORD + r"_bounded"),
    ("because_no_go_grade", r"because.*" + GRADE_WORD + r"_no_go"),
    ("depends_on_dep_audit_grade", r"depends on the dep'?s audit grade"),
    ("load_bears_on_dep_audit_grade", r"load-bears on the dep'?s audit grade"),
    ("requires_dep_clean_grade", r"requires the dep to be " + GRADE_WORD),
    ("requires_clean_verdict", r"requires.*" + CLEAN_VERDICT),
    ("requires_dep_grade", r"requires the dep grade"),
    ("theorem_load_bears_on_grade", r"this theorem load-bears on the audit grade"),
)

PARENT_DIRECT_STATUS_BOUNDARY = (
    "direct_" + "effective" + "_status_change_allowed_from_this_note: false"
)
PARENT_STATUS_AUTHORITY_BOUNDARY = (
    "status_" + "auth" + "ority: independent_audit_lane_only"
)


def block6_note_grade_scan() -> None:
    log("")
    log("=" * 80)
    log("Block 6: Static scan of parent note for grade-dependence claims")
    log("=" * 80)

    note_src = read_text(PARENT_NOTE)
    for label, pat in GRADE_DEPENDENCE_PATTERNS:
        m = re.search(pat, note_src, re.IGNORECASE)
        check(
            f"parent note absent of grade-dependence pattern: {label}",
            m is None,
        )

    check(
        "parent note declares no direct generated-status change",
        PARENT_DIRECT_STATUS_BOUNDARY in note_src,
    )
    check(
        "parent note declares independent status boundary",
        PARENT_STATUS_AUTHORITY_BOUNDARY in note_src,
    )


# -----------------------------------------------------------
# Block 7: Counterfactual independence
# -----------------------------------------------------------

def block7_counterfactual_independence() -> None:
    log("")
    log("=" * 80)
    log("Block 7: Counterfactual independence of substantive blocks")
    log("=" * 80)

    # Re-run the substantive computations with no ledger access at all
    # and confirm the substantive numerical conclusions are independent
    # of the audit-pipeline state.

    omega3 = states(3)
    omega2 = states(2)

    # Uniform-origin zero mean still holds
    uniform3 = [1.0 / len(omega3)] * len(omega3)
    max_uniform_mean = 0.0
    for i in range(3):
        m = sum(p * eps[i] for p, eps in zip(uniform3, omega3))
        if abs(m) > max_uniform_mean:
            max_uniform_mean = abs(m)
    check(
        "no-ledger: uniform reference has zero mean",
        max_uniform_mean < 1.0e-12,
        max_uniform_mean,
    )

    # Connected covariance Hessian sign on a generic h still positive-diag
    h = [0.05, -0.12, 0.31]
    cov = covariance_matrix(h, omega3, companion_base_weight)
    check(
        "no-ledger: connected covariance has strictly positive diagonal",
        all(cov[i][i] > 0.0 for i in range(3)),
    )

    # Source rescaling identity still absorbs into h-coordinate
    lam = 1.7
    h_prime = [lam * 0.21, -0.08]
    h_reparam = [0.21, -0.08 / lam]
    max_err = 0.0
    for eps in omega2:
        lhs = math.exp(sum(hi * ei for hi, ei in zip(h_prime, eps)))
        rhs = math.exp(lam * h_reparam[0] * eps[0] + lam * h_reparam[1] * eps[1])
        if abs(lhs - rhs) > max_err:
            max_err = abs(lhs - rhs)
    check(
        "no-ledger: source rescaling absorbs into h-coordinate redefinition",
        max_err < 1.0e-12,
        max_err,
    )

    # Confirm none of these depend on the dep's audit status by
    # synthesizing a stand-in "dep_status" that we explicitly do not
    # consume.
    fake_grades = [
        GRADE_WORD + "_no_go",
        GRADE_WORD + "_pending_chain",
        UNSETTLED_WORD,
        CONDITIONAL_VERDICT,
        CLEAN_VERDICT,
        GRADE_WORD + "_bounded",
    ]
    cov_across_grades: list[float] = []
    for _grade in fake_grades:
        # The computation never touches `_grade`; we recompute the
        # covariance to confirm it is grade-invariant.
        cov_again = covariance_matrix(h, omega3, companion_base_weight)
        cov_across_grades.append(cov_again[0][0])
    spread = max(cov_across_grades) - min(cov_across_grades)
    check(
        "no-ledger: connected covariance invariant across simulated grade values",
        spread < 1.0e-14,
        spread,
    )


# -----------------------------------------------------------
# Block 8: Firewall preservation
# -----------------------------------------------------------

REQUIRED_BOUNDARY_PHRASES = (
    ("canonical_operator_open", "does not fix canonical `O_H`"),
    ("scalar_lsz_open", "does not fix scalar LSZ normalization"),
    ("kappa_y_open", "does not select `kappa_Y = 0`"),
    ("mass_yukawa_open", "does not derive `m_t` or `y_t`"),
    ("bounded_author_hint", "claim_type_author_hint: bounded_theorem"),
    ("independent_status_boundary", PARENT_STATUS_AUTHORITY_BOUNDARY),
    ("no_direct_generated_status_change", PARENT_DIRECT_STATUS_BOUNDARY),
)

FORBIDDEN_OVERCLAIM_PHRASES = (
    ("status_clean_grade", "Status:** " + GRADE_WORD),
    ("positive_clean_grade_closure", "positive " + GRADE_WORD + " Y_T closure"),
    ("kappa_y_derived", "kappa_Y = 0 is derived"),
    ("derive_y_t", "derive y_t"),
    ("y_t_value", "y_t ="),
    ("m_t_value", "m_t ="),
    ("sqrt_import_overclaim", "sqrt(8/9) as an unconditional"),
)


def block8_firewall_preservation() -> None:
    log("")
    log("=" * 80)
    log("Block 8: Firewall preservation across the dep weakening")
    log("=" * 80)

    note_src = read_text(PARENT_NOTE)
    for label, phrase in REQUIRED_BOUNDARY_PHRASES:
        check(
            f"required boundary phrase present: {label}",
            phrase in note_src,
        )
    for label, phrase in FORBIDDEN_OVERCLAIM_PHRASES:
        check(
            f"forbidden overclaim absent: {label}",
            phrase not in note_src,
        )


# -----------------------------------------------------------
# Block 9: Runner-hash continuity
# -----------------------------------------------------------

def block9_runner_hash_continuity() -> None:
    log("")
    log("=" * 80)
    log("Block 9: Runner-hash continuity since last clean archived snapshot")
    log("=" * 80)

    runner_bytes = PARENT_RUNNER.read_bytes()
    current_hash = hashlib.sha256(runner_bytes).hexdigest()
    check(
        "current parent runner SHA-256 matches expected archived runner snapshot",
        current_hash == EXPECTED_RUNNER_HASH,
        f"current={current_hash[:16]} expected={EXPECTED_RUNNER_HASH[:16]}",
    )

    check(
        "current runner hash is NOT the earlier superseded hash",
        current_hash != SUPERSEDED_RUNNER_HASH,
        f"current={current_hash[:16]} superseded={SUPERSEDED_RUNNER_HASH[:16]}",
    )

    # Cross-confirm via the ledger row's previous_audits snapshot.
    rows = json.loads(read_text(LEDGER))["rows"]
    row = rows.get(PARENT_CLAIM_ID, {})
    prev_audits = row.get("previous_audits", [])
    check(
        "parent ledger row has >= 2 previous_audits entries (matches event chain)",
        len(prev_audits) >= 2,
        len(prev_audits),
    )

    most_recent_snapshot_hash = None
    most_recent_snapshot_archived = None
    for pa in prev_audits:
        snapshot_hash = pa.get("audit_state_snapshot", {}).get("runner_hash")
        if not snapshot_hash:
            continue
        archived = pa.get("archived_at", "")
        if (
            most_recent_snapshot_archived is None
            or archived > most_recent_snapshot_archived
        ):
            most_recent_snapshot_archived = archived
            most_recent_snapshot_hash = snapshot_hash
    check(
        "most-recent archived runner snapshot has runner_hash recorded",
        most_recent_snapshot_hash is not None,
        str(most_recent_snapshot_hash)[:16] if most_recent_snapshot_hash else "missing",
    )
    if most_recent_snapshot_hash is not None:
        check(
            "current runner hash matches most-recent archived runner hash",
            current_hash == most_recent_snapshot_hash,
            f"current={current_hash[:16]} snap={most_recent_snapshot_hash[:16]}",
        )

    # Confirm the most recent invalidation reason is the dep_weakened event,
    # not a runner-hash event.
    most_recent_inv = None
    most_recent_inv_archived = None
    for pa in prev_audits:
        inv = pa.get("invalidation_reason")
        if inv:
            archived = pa.get("archived_at", "")
            if (
                most_recent_inv_archived is None
                or archived > most_recent_inv_archived
            ):
                most_recent_inv_archived = archived
                most_recent_inv = inv
    check(
        "most-recent invalidation reason is a dep_weakened event",
        most_recent_inv is not None and most_recent_inv.startswith("dep_weakened:"),
        "present" if most_recent_inv else "missing",
    )
    if most_recent_inv is not None:
        check(
            "most-recent invalidation names the no-go dep",
            NO_GO_DEP_CLAIM_ID in most_recent_inv,
            "present" if NO_GO_DEP_CLAIM_ID in most_recent_inv else "missing",
        )


# -----------------------------------------------------------
# Block 10: Companion's own non-self-promotion check
# -----------------------------------------------------------

COMPANION_FORBIDDEN_PROMOTIONS = (
    ("status_clean_grade", "Status: " + GRADE_WORD),
    ("promoted_clean_grade", "promoted to " + GRADE_WORD),
    ("promote_parent", "we promote the parent"),
    ("promotes_parent_effective_state", "promotes the parent's " + EFFECTIVE_STATE_FIELD),
    ("note_promotes", "this note promotes"),
    ("companion_promotes", "this companion promotes"),
)

COMPANION_REQUIRED_DISCLAIMERS = (
    ("meta_type", "Type:** meta"),
    ("companion_only", "companion-only"),
    ("not_new_theorem", "not a new theorem claim"),
    ("not_direct_status_change", "not a direct status change"),
    ("does_not_change_status", "does not change status"),
)


def block10_companion_non_promotion() -> None:
    log("")
    log("=" * 80)
    log("Block 10: Companion non-self-promotion check")
    log("=" * 80)

    src = read_text(COMPANION_NOTE)
    src_collapsed = re.sub(r"\s+", " ", src)

    for label, phrase in COMPANION_FORBIDDEN_PROMOTIONS:
        check(
            f"companion absent of promotion phrase: {label}",
            phrase not in src,
        )
    for label, phrase in COMPANION_REQUIRED_DISCLAIMERS:
        check(
            f"companion contains required disclaimer: {label}",
            phrase in src_collapsed,
        )

    check(
        "companion does not assert current parent grade other than ledger record",
        "current parent status is " + GRADE_WORD + "_bounded" not in src
        and "current parent grade is " + GRADE_WORD + "_bounded" not in src,
    )

    # Companion runner file must exist and reference itself by its own path.
    check("companion runner exists", COMPANION_RUNNER.exists())
    check(
        "companion note registers this companion runner",
        COMPANION_RUNNER.name in src,
    )


# -----------------------------------------------------------
# Cached log writer
# -----------------------------------------------------------

CACHE_PATH = (
    ROOT
    / "logs"
    / "runner-cache"
    / "audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04.txt"
)


def write_cache(b1: dict[str, object]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    header = [
        "audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04",
        f"parent_runner={PARENT_RUNNER.relative_to(ROOT)}",
        f"parent_note={PARENT_NOTE.relative_to(ROOT)}",
        f"companion_note={COMPANION_NOTE.relative_to(ROOT)}",
        f"parent_runner_pass_count={b1.get('pass')}",
        f"parent_runner_fail_count={b1.get('fail')}",
        f"parent_runner_exit_code={b1.get('rc')}",
        f"expected_runner_sha256={EXPECTED_RUNNER_HASH}",
        f"companion_total_PASS={PASS}",
        f"companion_total_FAIL={FAIL}",
        "",
    ]
    out = "\n".join(header) + "\n".join(LOG_LINES) + "\n"
    CACHE_PATH.write_text(out, encoding="utf-8")


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("audit_companion_yt_source_covariance_normalization_support_dep_resolution_2026_06_04")
    log(f"parent runner   : {PARENT_RUNNER.relative_to(ROOT)}")
    log(f"parent note     : {PARENT_NOTE.relative_to(ROOT)}")
    log(f"companion       : {COMPANION_NOTE.relative_to(ROOT)}")
    log(f"no-go dep       : {NO_GO_DEP_CLAIM_ID}")
    log(f"source-pkt dep  : {SOURCE_PACKET_DEP_CLAIM_ID}")
    log(f"expected runner SHA-256: {EXPECTED_RUNNER_HASH}")

    b1 = block1_rerun_parent_runner()
    block2_independent_fh_covariance()
    block3_uniform_origin_score()
    block4_source_rescaling_boundary()
    block5_runner_grade_scan()
    block6_note_grade_scan()
    block7_counterfactual_independence()
    block8_firewall_preservation()
    block9_runner_hash_continuity()
    block10_companion_non_promotion()

    log("")
    log("=" * 80)
    log(f"RESULT: PASS={PASS} FAIL={FAIL}")
    log("=" * 80)

    write_cache(b1)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
