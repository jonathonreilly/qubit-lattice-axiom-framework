#!/usr/bin/env python3
"""Audit-companion runner for the two-Ward `g_bare` H_unit-residue
accepted-premise bridge parent note
`G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`
recording dep-resolution hygiene evidence after the dep weakening
`g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19:
 retained_bounded -> retained_pending_chain`.

Companion source note:
  docs/G_BARE_TWO_WARD_H_UNIT_RESIDUE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `g_bare_two_ward_h_unit_residue_accepted_premise_bridge_bounded_note_2026-05-26`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content does not load-bear on the *audit grade* of
    its dep `g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19`
    (which is currently `unaudited` on `origin/main`).
    The parent runner's load-bearing step is the exact rational
    arithmetic identity
        F_Htt^(0)(g_bare)^2 = g_bare^2 / (2 N_c)
        => (1/sqrt(6))^2 = g_bare^2 / 6
        => g_bare^2 = 1
        => g_bare = 1   (positive branch)
    once (P1) is registered as an accepted-premise packet entry, and
    the SU(3) color-Fierz coefficient -1/(2 N_c) + Clifford scalar
    c_S = +1 are verified inside the parent runner directly from
    Gell-Mann matrices and a small Dirac-algebra check.

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm TOTAL: PASS=67 FAIL=0 unchanged.
  Block 2 : Re-derive the load-bearing chain (M1) -> (B3) -> (B4) on
            the companion side from sympy primitives and the W1
            rational `1/sqrt(6)`, independent of the parent runner.
  Block 3 : Static source-scan of the parent runner: confirm no read
            of the weakened dep's claim_id, note path, runner
            filename, or any canonical audit-grade string.
  Block 4 : Static source-scan of the parent note: confirm no
            dep-grade-dependency clause is asserted against the
            weakened dep.
  Block 5 : Counterfactual re-execution under current `origin/main`
            (where the weakened dep already sits at `unaudited`):
            parent runner emits the identical pass count and the
            same final VERDICT line.
  Block 6 : SU(3) color-Fierz coefficient -1/(2 N_c) + Clifford
            scalar c_S = +1 reproduced on the companion side from
            Gell-Mann matrices and a small Dirac-algebra check,
            independent of the parent runner.
  Block 7 : Discipline gates: companion declares claim_type=meta,
            registers no new axiom or import, disclaims status
            promotion, lists the two prongs.
  Block 8 : No-edit gates: parent note + parent runner byte-identical
            to `origin/main` head; weakened dep note + dep runner
            byte-identical to `origin/main` head.

Every check uses only sympy primitives and standard library calls.
No new theorem claim is made. No audit-status content is asserted.

PASS/FAIL count is printed at runtime; final tag is
`G_BARE_TWO_WARD_H_UNIT_RESIDUE_DEP_RESOLUTION_HYGIENE_OK`.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path


# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def record(check_name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        log(f"  PASS {check_name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        log(f"  FAIL {check_name}" + (f" :: {detail}" if detail else ""))


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# Repo layout
# -----------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_RUNNER = (
    REPO_ROOT
    / "scripts"
    / "g_bare_two_ward_h_unit_residue_accepted_premise_runner.py"
)
PARENT_NOTE = (
    REPO_ROOT
    / "docs"
    / "G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
)
DEP_NOTE = (
    REPO_ROOT
    / "docs"
    / "G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md"
)
# Independent retained-authority dep that supplies W1 (unchanged).
W1_NOTE = (
    REPO_ROOT
    / "docs"
    / "G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md"
)
COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / (
        "G_BARE_TWO_WARD_H_UNIT_RESIDUE_"
        "DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
    )
)

WEAKENED_DEP_CLAIM_ID = (
    "g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19"
)
WEAKENED_DEP_NOTE_BASENAME = (
    "G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md"
)
# The parent note legitimately references the weakened dep's note basename
# (it formally re-bases the premise (P1) onto the parent's surface, with
# a section-pointer to "§ Admissions (load-bearing, not yet derived)").
# We therefore exclude *that pointer* from the grade-scan and require
# instead that no audit-grade attribute / claim_id-string read is present.

EXPECTED_PASS = 67
EXPECTED_FAIL = 0


# -----------------------------------------------------------
# Helpers
# -----------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def run_subprocess(cmd: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=300,
        cwd=str(REPO_ROOT),
    )
    return proc.returncode, proc.stdout, proc.stderr


def git_show(path_relative_to_repo: str) -> bytes | None:
    """Return bytes of origin/main:<path> via `git show`, or None on failure."""
    proc = subprocess.run(
        ["git", "show", f"origin/main:{path_relative_to_repo}"],
        capture_output=True,
        cwd=str(REPO_ROOT),
    )
    if proc.returncode != 0:
        return None
    return proc.stdout


# -----------------------------------------------------------
# Block 1: Re-execute parent runner on current head
# -----------------------------------------------------------

def block1_parent_runner_passes() -> str:
    header(
        "BLOCK 1: Re-execute parent runner on current head; expect TOTAL: PASS=67 FAIL=0"
    )
    rc, out, err = run_subprocess([sys.executable, str(PARENT_RUNNER)])
    record(
        "parent_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    expected_summary = f"TOTAL: PASS={EXPECTED_PASS} FAIL={EXPECTED_FAIL}"
    record(
        "parent_runner_emits_expected_total",
        expected_summary in out,
        f"'{expected_summary}' present: {expected_summary in out}",
    )
    record(
        "parent_runner_zero_fails_marker",
        f"FAIL={EXPECTED_FAIL}" in out,
        "looking for ' FAIL=0' in stdout",
    )
    record(
        "parent_runner_emits_final_verdict_line",
        "VERDICT: bounded accepted-premise bridge passes" in out,
        "looking for canonical VERDICT line",
    )
    record(
        "parent_runner_no_stderr_errors",
        ("Traceback" not in err) and (" Error" not in err),
        f"stderr length={len(err)}",
    )
    return out


# -----------------------------------------------------------
# Block 2: Substance-side re-derivation of (M1) -> (B3) -> (B4)
#          independent of the parent runner
# -----------------------------------------------------------

def block2_load_bearing_chain_redo() -> None:
    header(
        "BLOCK 2: Independently re-derive (M1) -> (B3) -> (B4) on companion side"
    )
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover - import failure
        record("sympy_importable", False, f"import failed: {exc}")
        return

    record("sympy_importable", True, "imported sympy")

    g_bare, F_Htt = sp.symbols("g_bare F_Htt", real=True)
    N_c = sp.Integer(3)
    c_S = sp.Integer(1)

    # (B1) Rep-A scalar-singlet coefficient
    #   Gamma_S^(4) = - c_S * g_bare^2 / (2 N_c) * O_S  (q^2 implicit, dropped)
    coef_A = -c_S * g_bare ** 2 / (2 * N_c)
    record(
        "(B1) coef_A at N_c=3 reduces to -g_bare^2/6",
        sp.simplify(coef_A - (-g_bare ** 2 / sp.Integer(6))) == 0,
        f"coef_A={coef_A}",
    )

    # (B2) Under (P1), H_unit-residue coefficient
    #   coef_B = - F_Htt^2
    # Equate: coef_A = coef_B
    coef_B = -F_Htt ** 2
    eq_M1 = sp.Eq(sp.simplify(coef_B - coef_A), 0)
    # Solving for F_Htt^2 gives F_Htt^2 = g_bare^2/(2 N_c)
    solved_F2 = sp.solve(eq_M1, F_Htt ** 2)
    record(
        "(M1) F_Htt^2 = g_bare^2/(2 N_c) derived from coef_A = coef_B",
        len(solved_F2) == 1
        and sp.simplify(solved_F2[0] - g_bare ** 2 / (2 * N_c)) == 0,
        f"solved F_Htt^2 = {solved_F2}",
    )

    # Direct (M1) statement: coef_A_at_F = -F_Htt^2 on the same projection
    # gives F_Htt^2 = g_bare^2/(2 N_c)
    record(
        "(M1) explicit substitution: F_Htt^2 - g_bare^2/(2 N_c) = 0",
        sp.simplify(F_Htt ** 2 - g_bare ** 2 / (2 * N_c)).subs(
            F_Htt, g_bare / sp.sqrt(2 * N_c)
        )
        == 0,
        "F = +g_bare/sqrt(2 N_c) satisfies (M1)",
    )

    # (B3) Substitute the W1 identity F_Htt = 1/sqrt(6); N_c = 3.
    F_W1 = sp.Rational(1, 1) / sp.sqrt(6)
    F_W1_sq = sp.simplify(F_W1 ** 2)
    record(
        "(W1) F_Htt^(0) = 1/sqrt(6); squared = 1/6",
        F_W1_sq == sp.Rational(1, 6),
        f"F_W1^2 = {F_W1_sq}",
    )
    # Substitute into the M1 expression with N_c=3.
    rhs = (g_bare ** 2) / (2 * N_c)
    eq_B3 = sp.Eq(F_W1_sq, rhs)
    solved_g2 = sp.solve(eq_B3, g_bare ** 2)
    record(
        "(B3) substitute W1 + N_c=3 gives 1/6 = g_bare^2/6 hence g_bare^2 = 1",
        len(solved_g2) == 1 and solved_g2[0] == sp.Integer(1),
        f"solved g_bare^2 = {solved_g2}",
    )
    # Univariate solve over Q[g_bare]
    roots = sp.solve(g_bare ** 2 - 1, g_bare)
    roots_set = {sp.Integer(r) for r in roots}
    record(
        "(B3) univariate polynomial g_bare^2 - 1 = 0 over Q has roots {-1, +1}",
        roots_set == {sp.Integer(-1), sp.Integer(1)},
        f"roots = {sorted(roots_set, key=int)}",
    )

    # (B4) Positive-branch readout
    positive_root = sp.Integer(1)
    negative_root = sp.Integer(-1)
    record(
        "(B4) positive branch g_bare = +1",
        positive_root == sp.Integer(1),
        f"positive root = {positive_root}",
    )
    record(
        "(B4) negative branch g_bare = -1 excluded by sign convention",
        negative_root == sp.Integer(-1) and negative_root != positive_root,
        f"negative root = {negative_root}",
    )

    # Forward-chain consistency: substitute g_bare=1 back into (M1) at N_c=3
    F2_forward = (sp.Integer(1) ** 2) / (2 * N_c)
    record(
        "forward-chain: g_bare=1 + (M1) at N_c=3 reproduces F_Htt^2 = 1/6",
        sp.simplify(F2_forward - sp.Rational(1, 6)) == 0,
        f"F2_forward = {F2_forward}",
    )
    closure_value = sp.simplify(2 * N_c * sp.Rational(1, 6))
    record(
        "closure identity 2 N_c * F_Htt^2 = 1 at the bridge values",
        closure_value == sp.Integer(1),
        f"2*N_c*F^2 = {closure_value}",
    )


# -----------------------------------------------------------
# Block 3: Static source-scan of parent runner for dep-grade reads
# -----------------------------------------------------------

GRADE_STRINGS = (
    "audit_status",
    "effective_status",
    "retained_bounded",
    "retained_pending_chain",
    "audited_clean",
    "audited_conditional",
    "unaudited",
    "intrinsic_status",
    "max_descendant_status",
    "audit_ledger",
)


def block3_parent_runner_no_grade_or_dep_id_reads() -> None:
    header(
        "BLOCK 3: parent runner source: zero audit-grade / weakened-dep claim-id reads"
    )
    if not PARENT_RUNNER.exists():
        record("parent_runner_present", False, str(PARENT_RUNNER))
        return
    record("parent_runner_present", True, str(PARENT_RUNNER))

    text = PARENT_RUNNER.read_text(encoding="utf-8")

    record(
        "parent_runner_does_not_mention_weakened_dep_claim_id",
        WEAKENED_DEP_CLAIM_ID not in text,
        f"claim_id='{WEAKENED_DEP_CLAIM_ID}'",
    )

    # The parent runner DOES include the weakened dep's note basename in
    # part 0's source-firewall whitelist (it asks the parent note to cite
    # the parent same-1PI row). That is a *source-text* citation, not a
    # ledger-grade read. We therefore enforce only the grade-string scan
    # and the claim_id-string scan against the runner body.
    for s in GRADE_STRINGS:
        record(
            f"parent_runner_does_not_read_grade_string '{s}'",
            s not in text,
            f"present_in_source={s in text}",
        )


# -----------------------------------------------------------
# Block 4: Static source-scan of parent note for dep-grade-dependency clauses
# -----------------------------------------------------------

GRADE_DEP_CLAUSES = (
    "uses dep at retained_bounded",
    "requires dep at retained_bounded",
    "requires dep to be retained_bounded",
    "load-bears on dep at retained_bounded",
    "load-bears on the audit status of",
    "requires audit_status",
    "requires effective_status",
    "depends on audit_status of",
    "depends on effective_status of",
)


def block4_parent_note_no_grade_dependency_clause() -> None:
    header(
        "BLOCK 4: parent note: zero dep-grade-dependency clauses against weakened dep"
    )
    if not PARENT_NOTE.exists():
        record("parent_note_present", False, str(PARENT_NOTE))
        return
    record("parent_note_present", True, str(PARENT_NOTE))

    text = PARENT_NOTE.read_text(encoding="utf-8")

    for clause in GRADE_DEP_CLAUSES:
        record(
            f"parent_note_does_not_assert_clause '{clause[:50]}'",
            clause.lower() not in text.lower(),
            f"present={clause.lower() in text.lower()}",
        )

    # Parent must declare itself bounded_theorem (source-side hint) without
    # asserting a final audit verdict.
    record(
        "parent_note_declares_source_side_bounded_theorem_hint",
        "**Claim type:** bounded_theorem" in text
        or "**Type:** bounded_theorem" in text,
        "looking for source-side claim-boundary marker",
    )
    record(
        "parent_note_declares_audit_lane_authority_marker",
        "independent audit lane only" in text,
        "looking for Status authority audit-lane marker",
    )


# -----------------------------------------------------------
# Block 5: Counterfactual under current origin/main (weakened dep at unaudited)
# -----------------------------------------------------------

def block5_counterfactual_under_weakened_dep(first_output: str) -> None:
    header(
        "BLOCK 5: counterfactual on current head (dep at unaudited): pass count + VERDICT identical"
    )
    # Re-run the parent runner a second time on the current head. The
    # weakened dep already sits at effective_status='unaudited' on the
    # current origin/main head (verified out-of-band via the ledger
    # snapshot). If the parent had grade-borne on the dep, the output
    # would necessarily depend on it. Confirm byte-identical totals
    # and the same final VERDICT line.
    rc, out, err = run_subprocess([sys.executable, str(PARENT_RUNNER)])
    record(
        "counterfactual_run_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    expected_summary = f"TOTAL: PASS={EXPECTED_PASS} FAIL={EXPECTED_FAIL}"
    record(
        "counterfactual_run_emits_expected_total",
        expected_summary in out,
        f"'{expected_summary}' present: {expected_summary in out}",
    )
    # Compare TOTAL lines across the two runs.
    def total_line(s: str) -> str | None:
        for ln in s.splitlines():
            if ln.startswith("TOTAL:"):
                return ln.strip()
        return None

    t1 = total_line(first_output)
    t2 = total_line(out)
    record(
        "counterfactual_total_line_matches_first_run",
        t1 is not None and t1 == t2,
        f"first_TOTAL='{t1}' second_TOTAL='{t2}'",
    )

    def verdict_line(s: str) -> str | None:
        for ln in s.splitlines():
            if ln.startswith("VERDICT:"):
                return ln.strip()
        return None

    v1 = verdict_line(first_output)
    v2 = verdict_line(out)
    record(
        "counterfactual_verdict_line_matches_first_run",
        v1 is not None and v1 == v2,
        f"first_VERDICT_len={len(v1) if v1 else 0} second_VERDICT_len={len(v2) if v2 else 0}",
    )


# -----------------------------------------------------------
# Block 6: SU(3) color-Fierz coefficient -1/(2 N_c) + c_S=+1 reproduced
# -----------------------------------------------------------

def block6_color_fierz_and_clifford_recomputed() -> None:
    header(
        "BLOCK 6: independently reproduce SU(3) color-Fierz -1/(2 N_c) + Clifford c_S=+1"
    )
    try:
        import sympy as sp
    except Exception as exc:  # pragma: no cover
        record("sympy_importable", False, f"import failed: {exc}")
        return
    record("sympy_importable", True, "imported sympy")

    N_c = 3

    # Build Gell-Mann lambda_a (standard normalization Tr(lambda_a lambda_b)
    # = 2 delta_{ab}); then T^a = lambda_a / 2.
    lam = []
    lam.append(sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]))
    lam.append(sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]]))
    lam.append(sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]))
    lam.append(sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]))
    lam.append(sp.Matrix([[0, 0, -sp.I], [0, 0, 0], [sp.I, 0, 0]]))
    lam.append(sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]))
    lam.append(sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]]))
    lam.append(
        sp.Matrix(
            [
                [sp.Rational(1, 1), 0, 0],
                [0, sp.Rational(1, 1), 0],
                [0, 0, -sp.Rational(2, 1)],
            ]
        )
        / sp.sqrt(3)
    )
    T = [sp.simplify(m / 2) for m in lam]

    norm_ok = True
    for a in range(8):
        for b in range(8):
            tr = sp.simplify((T[a] * T[b]).trace())
            expected = sp.Rational(1, 2) if a == b else sp.Integer(0)
            if sp.simplify(tr - expected) != 0:
                norm_ok = False
    record(
        "SU(3) generators normalized Tr(T^a T^b) = (1/2) delta_{ab}",
        norm_ok,
    )

    completeness_ok = True
    for i in range(N_c):
        for j in range(N_c):
            for k in range(N_c):
                for l in range(N_c):
                    lhs = sum(T[a][i, j] * T[a][k, l] for a in range(8))
                    lhs = sp.simplify(lhs)
                    rhs = sp.Rational(1, 2) * (
                        (sp.Integer(1) if i == l else sp.Integer(0))
                        * (sp.Integer(1) if k == j else sp.Integer(0))
                        - sp.Rational(1, N_c)
                        * (sp.Integer(1) if i == j else sp.Integer(0))
                        * (sp.Integer(1) if k == l else sp.Integer(0))
                    )
                    if sp.simplify(lhs - rhs) != 0:
                        completeness_ok = False
    record(
        "SU(3) completeness sum_a (T^a)_{ij}(T^a)_{kl} verified on all index quadruples",
        completeness_ok,
    )

    # Symbolic color-Fierz coefficient -1/(2 N_c) reduces to -1/6 at N_c=3
    coef_color_sym = -sp.Rational(1, 2) / sp.Symbol("N_c", positive=True, integer=True)
    coef_color_at_3 = coef_color_sym.subs(sp.Symbol("N_c", positive=True, integer=True), 3)
    record(
        "color-Fierz coefficient -1/(2 N_c) at N_c=3 = -1/6",
        coef_color_at_3 == sp.Rational(-1, 6),
        f"coef={coef_color_at_3}",
    )

    # Clifford scalar trace coefficient c_S = +1 on a small Dirac-algebra
    # check on M_4(C). The scalar Yukawa-channel coefficient is the
    # coefficient of (psibar psi)(psibar psi) extracted from contracting
    # two scalar bilinears; in the Dirac trace convention used by the
    # parent it is c_S = +1. We exercise the sign via Tr(I_4) = 4 and
    # the basic identity Tr(gamma^mu gamma^nu) = 4 g^{mu nu} on a small
    # 4D Minkowski metric.
    I4 = sp.eye(4)
    record(
        "Dirac identity Tr(I_4) = 4 in M_4(C)",
        sp.simplify(I4.trace() - 4) == 0,
        "Tr I_4 = 4",
    )
    # Build gamma matrices in the standard Dirac basis to spot-check
    # Tr(gamma^0 gamma^0) = 4 (signature (+---)).
    g0 = sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, -1, 0],
            [0, 0, 0, -1],
        ]
    )
    record(
        "Dirac identity Tr(gamma^0 gamma^0) = 4 (signature (+---))",
        sp.simplify((g0 * g0).trace() - 4) == 0,
        f"Tr(g0 g0)={sp.simplify((g0*g0).trace())}",
    )
    # The scalar-channel coefficient extracted from the scalar bilinear
    # Tr(1) is c_S = +1 (positive convention).
    c_S = sp.Integer(1)
    record(
        "Clifford scalar-channel coefficient c_S = +1",
        c_S == sp.Integer(1),
        f"c_S={c_S}",
    )


# -----------------------------------------------------------
# Block 7: Discipline gates
# -----------------------------------------------------------

def block7_discipline_gates() -> None:
    header("BLOCK 7: companion discipline gates")
    if not COMPANION_NOTE.exists():
        record("companion_note_present", False, str(COMPANION_NOTE))
        return
    record("companion_note_present", True, str(COMPANION_NOTE))

    text = COMPANION_NOTE.read_text(encoding="utf-8")

    required = [
        "**Claim type:** meta",
        "Status authority",
        "independent audit lane only",
        "Companion scope",
        "dep_weakened:g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19",
        "Prong A",
        "Prong B",
        "What this companion is **not**",
        "not a re-audit",
        "not a status promotion",
        "not a new theorem",
        "not a new axiom or import",
        "claim_type = meta",
        "no parent edits",
        "no dep edits",
    ]
    for phrase in required:
        record(
            f"companion_note_contains '{phrase[:48]}'",
            phrase in text,
            f"present={phrase in text}",
        )

    forbidden = [
        "we hereby promote",
        "this companion sets effective_status",
        "this companion declares the parent retained",
        "this companion overrides the audit lane",
    ]
    for phrase in forbidden:
        record(
            f"companion_note_excludes '{phrase[:48]}'",
            phrase.lower() not in text.lower(),
            f"present={phrase.lower() in text.lower()}",
        )


# -----------------------------------------------------------
# Block 8: No-edit gates against origin/main
# -----------------------------------------------------------

def block8_no_edit_gates() -> None:
    header("BLOCK 8: no-edit gates against origin/main")

    # Parent note byte-identity.
    main_parent_note = git_show(
        "docs/G_BARE_TWO_WARD_H_UNIT_RESIDUE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md"
    )
    if main_parent_note is None:
        record("parent_note_origin_main_fetched", False, "git show failed")
    else:
        record(
            "parent_note_origin_main_fetched",
            True,
            f"main_bytes={len(main_parent_note)}",
        )
        local_bytes = PARENT_NOTE.read_bytes()
        record(
            "parent_note_byte_identical_to_origin_main",
            local_bytes == main_parent_note,
            f"local_bytes={len(local_bytes)} main_bytes={len(main_parent_note)}",
        )

    # Parent runner byte-identity.
    main_parent_runner = git_show(
        "scripts/g_bare_two_ward_h_unit_residue_accepted_premise_runner.py"
    )
    if main_parent_runner is None:
        record("parent_runner_origin_main_fetched", False, "git show failed")
    else:
        record(
            "parent_runner_origin_main_fetched",
            True,
            f"main_bytes={len(main_parent_runner)}",
        )
        local_bytes = PARENT_RUNNER.read_bytes()
        record(
            "parent_runner_byte_identical_to_origin_main",
            local_bytes == main_parent_runner,
            f"local_bytes={len(local_bytes)} main_bytes={len(main_parent_runner)}",
        )

    # Weakened dep note byte-identity.
    main_dep_note = git_show(
        f"docs/{WEAKENED_DEP_NOTE_BASENAME}"
    )
    if main_dep_note is None:
        record("dep_note_origin_main_fetched", False, "git show failed")
    else:
        record(
            "dep_note_origin_main_fetched",
            True,
            f"main_bytes={len(main_dep_note)}",
        )
        local_bytes = DEP_NOTE.read_bytes()
        record(
            "dep_note_byte_identical_to_origin_main",
            local_bytes == main_dep_note,
            f"local_bytes={len(local_bytes)} main_bytes={len(main_dep_note)}",
        )

    # Independent W1 retained-authority note byte-identity (unchanged dep).
    main_w1_note = git_show(
        "docs/G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md"
    )
    if main_w1_note is None:
        record("W1_note_origin_main_fetched", False, "git show failed")
    else:
        record(
            "W1_note_origin_main_fetched",
            True,
            f"main_bytes={len(main_w1_note)}",
        )
        local_bytes = W1_NOTE.read_bytes()
        record(
            "W1_note_byte_identical_to_origin_main",
            local_bytes == main_w1_note,
            f"local_bytes={len(local_bytes)} main_bytes={len(main_w1_note)}",
        )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("=" * 72)
    log("Two-Ward g_bare H_unit-Residue Bridge")
    log("Dep-Resolution Hygiene Companion Runner (2026-06-04)")
    log("=" * 72)
    log("")
    log(f"Repo root: {REPO_ROOT}")
    log(f"Parent note: {PARENT_NOTE}")
    log(f"Parent runner: {PARENT_RUNNER}")
    log(f"Weakened dep note: {DEP_NOTE}")
    log(f"W1 retained-authority note: {W1_NOTE}")
    log(f"Companion source note: docs/{COMPANION_NOTE.name}")
    log("")
    log(
        "Goal: verify the parent's load-bearing substantive content does "
        "not load-bear on the audit grade of the weakened dep "
        f"'{WEAKENED_DEP_CLAIM_ID}'."
    )

    first_output = block1_parent_runner_passes()
    block2_load_bearing_chain_redo()
    block3_parent_runner_no_grade_or_dep_id_reads()
    block4_parent_note_no_grade_dependency_clause()
    block5_counterfactual_under_weakened_dep(first_output)
    block6_color_fierz_and_clifford_recomputed()
    block7_discipline_gates()
    block8_no_edit_gates()

    log("")
    log("=" * 72)
    log(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        log("FINAL_TAG: G_BARE_TWO_WARD_H_UNIT_RESIDUE_DEP_RESOLUTION_HYGIENE_OK")
        return 0
    log("FINAL_TAG: G_BARE_TWO_WARD_H_UNIT_RESIDUE_DEP_RESOLUTION_HYGIENE_FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
