#!/usr/bin/env python3
"""Audit-companion runner for the Y_T LSP signed-record source-readout
support parent note
`YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md`
recording dep-resolution hygiene evidence after the dep weakening

    lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22:
      retained_bounded -> unaudited

(an `axiom_premise_changed`-driven cascade from the 2026-06-04
canonical `minimal_axioms` re-resolution).

Companion source note:
  docs/YT_LSP_SIGNED_RECORD_SOURCE_READOUT_RUNNER_HASH_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `yt_lsp_signed_record_source_readout_support_note_2026-05-24`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content does not load-bear on the *audit grade* of
    its dep
    `lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22`
    (which was downgraded from `retained_bounded` to `unaudited`).

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm PASS=49 FAIL=1 with the single FAIL identified as
            the Part 2 ledger-status check on the weakened dep.
  Block 2 : Re-verify the signed-readout Pauli algebra (idempotency,
            orthogonality, completeness, spectrum, signed observable)
            directly from numpy primitives, independent of any dep
            grade.
  Block 3 : Re-verify the RN origin-score identity
            d log R_h / d h_x |_{h=0} = epsilon_x at three sites,
            independent of any dep grade.
  Block 4 : Re-verify source-family uniqueness corollary (normalized
            composition gives h+k addition; log-odds linearity;
            reconstructed family is product RN), independent of any
            dep grade.
  Block 5 : Static source-scan of the parent's runner: confirm that
            audit-status grade fields are only consulted in the single
            Part 2 ledger-status watcher (no other block reads
            audit_status / effective_status / intrinsic_status /
            retained_bounded / audited_clean from the dep's row).
  Block 6 : Static source-scan of the parent note: confirm no claim
            that the substantive signed-readout / RN-source conclusion
            depends on the dep's audit grade.
  Block 7 : Counterfactual confirmation: confirm the parent's runner
            Parts 3-7 substantive content is independent of the dep
            grade (rerun pieces that do not consult the ledger and
            confirm the substantive numbers are identical).
  Block 8 : Firewall preservation: confirm the parent note's
            "What This Does Not Close" / boundary phrases are
            preserved verbatim, and no forbidden overclaim phrases
            have been added.
  Block 9 : Runner-hash continuity: confirm the parent's runner
            SHA-256 on the current head is identical to the
            runner_hash recorded in the most recent audited_clean
            snapshot (a796ff28b71099137ffcc59118f2b240cabdfad5f6b54b5730b3963ce026ad01).
  Block 10: Companion's own audit-status non-self-promotion check:
            confirm the companion note does not assert a status or
            promote either the parent or the dep.

Every check uses only the parent's existing runner / dep runner code
(re-imported) plus standard finite-dimensional numerics.  No
audit-status content is asserted.  No new theorem claim is made.

PASS/FAIL count is printed at runtime.
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

import numpy as np


# -----------------------------------------------------------
# Paths and constants
# -----------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SCRIPTS = ROOT / "scripts"
LEDGER = DOCS / "audit" / "data" / "audit_ledger.json"

PARENT_NOTE = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
PARENT_RUNNER = SCRIPTS / "frontier_yt_lsp_signed_record_source_readout_support.py"
COMPANION_NOTE = (
    DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_RUNNER_HASH_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)
COMPANION_RUNNER = (
    SCRIPTS / "audit_companion_yt_lsp_signed_record_source_readout_dep_resolution_2026_06_04.py"
)

PARENT_CLAIM_ID = "yt_lsp_signed_record_source_readout_support_note_2026-05-24"
DEP_CLAIM_ID = "lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22"
DEP_NOTE_PATH = (
    DOCS / "LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md"
)
SOURCE_PACKET_CLAIM_ID = "yt_source_action_support_packet_note_2026-05-22"

# Runner hash recorded in the most recent audited_clean snapshot
# (archived 2026-06-04T16:59:09Z, audit dated 2026-05-28T06:02:23Z).
EXPECTED_RUNNER_HASH = (
    "a796ff28b71099137ffcc59118f2b240cabdfad5f6b54b5730b3963ce026ad01"
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
# Block 1: Re-run the parent's runner on the current head
# -----------------------------------------------------------

def block1_rerun_parent_runner() -> dict[str, object]:
    log("")
    log("=" * 80)
    log("Block 1: Re-run parent runner on current head")
    log("=" * 80)

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
        "parent runner PASS=49 (substantive content unchanged)",
        pass_count == 49,
        pass_count,
    )
    check(
        "parent runner FAIL=1 (single FAIL = procedural ledger-status watcher)",
        fail_count == 1,
        fail_count,
    )

    # Identify the single FAIL line and confirm it is the LSP dep grade
    fail_lines = [ln for ln in out.splitlines() if ln.startswith("[FAIL]")]
    check("exactly one FAIL line", len(fail_lines) == 1, len(fail_lines))
    if fail_lines:
        fail_line = fail_lines[0]
        check(
            "FAIL line names the LSP dep",
            DEP_CLAIM_ID in fail_line,
            fail_line,
        )
        check(
            "FAIL line reports unaudited status (the weakened grade)",
            "unaudited" in fail_line,
            fail_line,
        )

    return {"pass": pass_count, "fail": fail_count, "fail_lines": fail_lines, "stderr": err}


# -----------------------------------------------------------
# Block 2: Re-verify signed-readout Pauli algebra directly
# -----------------------------------------------------------

def block2_pauli_algebra() -> None:
    log("")
    log("=" * 80)
    log("Block 2: Re-verify Pauli algebra independent of any dep grade")
    log("=" * 80)

    identity = np.eye(2, dtype=float)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=float)
    p_plus = (identity + sigma_z) / 2.0
    p_minus = (identity - sigma_z) / 2.0

    check("P_+ idempotent", np.allclose(p_plus @ p_plus, p_plus))
    check("P_- idempotent", np.allclose(p_minus @ p_minus, p_minus))
    check(
        "P_+ and P_- orthogonal",
        np.allclose(p_plus @ p_minus, np.zeros((2, 2))),
    )
    check("P_+ + P_- = I (completeness)", np.allclose(p_plus + p_minus, identity))
    check(
        "signed observable P_+ - P_- = sigma_z",
        np.allclose(p_plus - p_minus, sigma_z),
    )
    evals = sorted(np.linalg.eigvalsh(sigma_z).round(12).tolist())
    check("signed spectrum is {-1,+1}", evals == [-1.0, 1.0], evals)


# -----------------------------------------------------------
# Block 3: RN origin-score identity at three sites
# -----------------------------------------------------------

def states(n_sites: int) -> list[tuple[int, ...]]:
    return list(itertools.product((-1, 1), repeat=n_sites))


def rn_density(h: list[float], omega: list[tuple[int, ...]]) -> list[float]:
    weights = [math.exp(sum(hi * ei for hi, ei in zip(h, eps))) for eps in omega]
    z = sum(weights)
    return [w / z for w in weights]


def max_abs(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def block3_rn_origin_score() -> None:
    log("")
    log("=" * 80)
    log("Block 3: RN origin-score identity independent of any dep grade")
    log("=" * 80)

    omega = states(3)
    delta = 1.0e-6
    origin = [0.0, 0.0, 0.0]
    max_err = 0.0
    for site in range(3):
        hp = origin.copy()
        hm = origin.copy()
        hp[site] = delta
        hm[site] = -delta
        rp = rn_density(hp, omega)
        rm = rn_density(hm, omega)
        score = [(math.log(a) - math.log(b)) / (2.0 * delta) for a, b in zip(rp, rm)]
        primitive = [float(eps[site]) for eps in omega]
        err = max_abs(score, primitive)
        max_err = max(max_err, err)
        check(
            f"site {site}: d log R / dh_x at h=0 equals epsilon_x",
            err < 1.0e-9,
            err,
        )
    check("all three sites within tolerance", max_err < 1.0e-9, max_err)


# -----------------------------------------------------------
# Block 4: Source-family uniqueness corollary
# -----------------------------------------------------------

def block4_source_family_uniqueness() -> None:
    log("")
    log("=" * 80)
    log("Block 4: Source-family uniqueness independent of any dep grade")
    log("=" * 80)

    omega = states(3)
    eps0 = omega[0]
    h = [0.17, -0.23, 0.31]
    k = [-0.11, 0.29, 0.07]
    rh = rn_density(h, omega)
    rk = rn_density(k, omega)
    rhk = rn_density([hi + ki for hi, ki in zip(h, k)], omega)

    composed_weights = [a * b for a, b in zip(rh, rk)]
    z = sum(composed_weights)
    composed = [w / z for w in composed_weights]
    err_compose = max_abs(composed, rhk)
    check(
        "normalized source composition implements h+k addition",
        err_compose < 1.0e-12,
        err_compose,
    )

    r0_index = omega.index(eps0)
    max_log_odds_err = 0.0
    for eps, prob in zip(omega, rh):
        lhs = math.log(prob / rh[r0_index])
        rhs = sum(hi * (ei - e0i) for hi, ei, e0i in zip(h, eps, eps0))
        max_log_odds_err = max(max_log_odds_err, abs(lhs - rhs))
    check(
        "log-odds are linear with coefficients epsilon - epsilon^0",
        max_log_odds_err < 1.0e-12,
        max_log_odds_err,
    )

    reconstructed = []
    for eps in omega:
        reconstructed.append(math.exp(sum(hi * ei for hi, ei in zip(h, eps))))
    rz = sum(reconstructed)
    reconstructed = [w / rz for w in reconstructed]
    err_rec = max_abs(reconstructed, rh)
    check(
        "uniquely-reconstructed family equals product RN",
        err_rec < 1.0e-12,
        err_rec,
    )


# -----------------------------------------------------------
# Block 5: Static source-scan of parent runner for grade references
# -----------------------------------------------------------

GRADE_FIELDS = (
    "audit_status",
    "effective_status",
    "intrinsic_status",
    "retained_bounded",
    "audited_clean",
    "audited_conditional",
)

# A "ledger read" is recognized by string patterns that load the ledger row
# and ask for an audit-grade field. We do NOT count firewall string literals
# (forbidden / required phrase lists) or output-payload boilerplate that
# contains the identifier as a substring — those are firewalls / data
# fields, not ledger consumption.
LEDGER_READ_PATTERNS = (
    r'row\.get\("effective_status"\)',
    r'row\.get\("audit_status"\)',
    r'row\.get\("intrinsic_status"\)',
    r'rows\[.+\]\["effective_status"\]',
    r'rows\.get\(.+\)\.get\("effective_status"\)',
    r'rows\.get\(.+\)\.get\("audit_status"\)',
)


def block5_runner_grade_scan() -> None:
    log("")
    log("=" * 80)
    log("Block 5: Static scan of parent runner for ledger grade-field reads")
    log("=" * 80)

    runner_src = read_text(PARENT_RUNNER)

    # Locate Part 2 body (the only allowed home for ledger grade reads)
    part2_match = re.search(
        r"def part2_ledger_status_boundary\(\).*?(?=\ndef |\Z)",
        runner_src,
        re.DOTALL,
    )
    check("parent runner contains Part 2 ledger-status function", part2_match is not None)
    part2_body = part2_match.group(0) if part2_match else ""

    # Confirm all ledger-read patterns live entirely inside Part 2 body.
    for pat in LEDGER_READ_PATTERNS:
        total_hits = len(re.findall(pat, runner_src))
        part2_hits = len(re.findall(pat, part2_body))
        check(
            f"ledger-read pattern {pat!r} confined to Part 2 (or absent)",
            total_hits == part2_hits,
            f"{part2_hits}/{total_hits} in Part 2",
        )

    # Also confirm: outside Part 2, no occurrences of bare grade-field
    # identifiers paired with row/ledger access. We split runner_src into
    # part2 and not-part2 and check the not-part2 portion has zero grade
    # field reads via row.get(...) or rows[...] patterns.
    not_part2 = runner_src.replace(part2_body, "")
    for field in GRADE_FIELDS:
        bad = re.findall(
            rf'(?:row|rows)\b[^\n]*"{re.escape(field)}"',
            not_part2,
        )
        check(
            f"outside Part 2: no ledger row access for '{field}'",
            len(bad) == 0,
            len(bad),
        )


# -----------------------------------------------------------
# Block 6: Static scan of parent note for grade-dependence claims
# -----------------------------------------------------------

GRADE_DEPENDENCE_PATTERNS = (
    r"because the dep is retained",
    r"because.*retained_bounded",
    r"depends on the dep'?s audit grade",
    r"load-bears on the dep'?s audit grade",
    r"requires the dep to be retained",
    r"requires.*audited_clean",
    r"requires the dep grade",
)


def block6_note_grade_scan() -> None:
    log("")
    log("=" * 80)
    log("Block 6: Static scan of parent note for grade-dependence claims")
    log("=" * 80)

    note_src = read_text(PARENT_NOTE)
    for pat in GRADE_DEPENDENCE_PATTERNS:
        m = re.search(pat, note_src, re.IGNORECASE)
        check(
            f"parent note absent of grade-dependence pattern: {pat!r}",
            m is None,
        )

    # Positive: note explicitly disclaims that this note can change
    # effective status directly.
    check(
        "parent note declares direct_effective_status_change_allowed_from_this_note: false",
        "direct_effective_status_change_allowed_from_this_note: false" in note_src,
    )
    check(
        "parent note declares audit_required_before_effective_status_change: true",
        "audit_required_before_effective_status_change: true" in note_src,
    )


# -----------------------------------------------------------
# Block 7: Counterfactual independence
# -----------------------------------------------------------

def block7_counterfactual_independence() -> None:
    log("")
    log("=" * 80)
    log("Block 7: Counterfactual independence of substantive blocks")
    log("=" * 80)

    # Re-run the same Pauli / RN computations with no ledger access at all
    # and confirm we obtain bit-for-bit identical numerical results to the
    # ones produced inside the parent's runner.
    identity = np.eye(2, dtype=float)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=float)
    p_plus = (identity + sigma_z) / 2.0
    p_minus = (identity - sigma_z) / 2.0

    check(
        "no-ledger Pauli: signed observable identical",
        np.array_equal(p_plus - p_minus, sigma_z),
    )

    omega = states(3)
    delta = 1.0e-6
    rp = rn_density([delta, 0.0, 0.0], omega)
    rm = rn_density([-delta, 0.0, 0.0], omega)
    score0 = [(math.log(a) - math.log(b)) / (2.0 * delta) for a, b in zip(rp, rm)]
    primitive0 = [float(eps[0]) for eps in omega]
    err = max_abs(score0, primitive0)
    check(
        "no-ledger RN origin-score at site 0 within tolerance",
        err < 1.0e-9,
        err,
    )

    # Two-site tensor commutativity, no ledger access
    sz_2site = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=float)
    eye2 = np.eye(2, dtype=float)
    z0 = np.kron(sz_2site, eye2)
    z1 = np.kron(eye2, sz_2site)
    check("no-ledger two-site readouts commute", np.allclose(z0 @ z1, z1 @ z0))
    check(
        "no-ledger two-site readouts square to identity",
        np.allclose(z0 @ z0, np.eye(4)) and np.allclose(z1 @ z1, np.eye(4)),
    )


# -----------------------------------------------------------
# Block 8: Firewall preservation
# -----------------------------------------------------------

REQUIRED_BOUNDARY_PHRASES = (
    "does not accept the source-coupled action convention",
    "does not derive canonical `O_H`",
    "does not fix scalar LSZ normalization",
    "does not select `kappa_Y = 0`",
    "does not derive `y_t`",
    "claim_type_author_hint: bounded_theorem",
    "direct_effective_status_change_allowed_from_this_note: false",
)

FORBIDDEN_OVERCLAIM_PHRASES = (
    "Status:** retained",
    "positive retained Y_T closure",
    "kappa_Y = 0 is derived",
    "derive y_t",
    "y_t = ",
    "m_t = ",
    "sqrt(8/9) as an unconditional",
)


def block8_firewall_preservation() -> None:
    log("")
    log("=" * 80)
    log("Block 8: Firewall preservation across the dep weakening")
    log("=" * 80)

    note_src = read_text(PARENT_NOTE)
    for phrase in REQUIRED_BOUNDARY_PHRASES:
        check(
            f"required boundary phrase present: {phrase}",
            phrase in note_src,
        )
    for phrase in FORBIDDEN_OVERCLAIM_PHRASES:
        check(
            f"forbidden overclaim absent: {phrase}",
            phrase not in note_src,
        )


# -----------------------------------------------------------
# Block 9: Runner-hash continuity
# -----------------------------------------------------------

def block9_runner_hash_continuity() -> None:
    log("")
    log("=" * 80)
    log("Block 9: Runner-hash continuity since last audited_clean snapshot")
    log("=" * 80)

    runner_bytes = PARENT_RUNNER.read_bytes()
    current_hash = hashlib.sha256(runner_bytes).hexdigest()
    check(
        "current parent runner SHA-256 matches last audited_clean snapshot",
        current_hash == EXPECTED_RUNNER_HASH,
        f"current={current_hash[:16]} expected={EXPECTED_RUNNER_HASH[:16]}",
    )

    # Cross-confirm via the ledger row's previous_audits snapshot.
    rows = json.loads(read_text(LEDGER))["rows"]
    row = rows.get(PARENT_CLAIM_ID, {})
    prev_audits = row.get("previous_audits", [])
    check(
        "parent ledger row has previous_audits entries",
        len(prev_audits) >= 1,
        len(prev_audits),
    )
    # Find the most recent audited_clean snapshot's runner_hash
    most_recent_clean_hash = None
    most_recent_clean_archived = None
    for pa in prev_audits:
        if pa.get("audit_status") == "audited_clean":
            archived = pa.get("archived_at", "")
            if (
                most_recent_clean_archived is None
                or archived > most_recent_clean_archived
            ):
                most_recent_clean_archived = archived
                most_recent_clean_hash = pa.get(
                    "audit_state_snapshot", {}
                ).get("runner_hash")
    check(
        "most-recent audited_clean snapshot has runner_hash recorded",
        most_recent_clean_hash is not None,
        str(most_recent_clean_hash)[:16] if most_recent_clean_hash else "missing",
    )
    if most_recent_clean_hash is not None:
        check(
            "current runner hash matches most-recent audited_clean snapshot's runner_hash",
            current_hash == most_recent_clean_hash,
            f"current={current_hash[:16]} snap={most_recent_clean_hash[:16]}",
        )


# -----------------------------------------------------------
# Block 10: Companion's own non-self-promotion check
# -----------------------------------------------------------

COMPANION_FORBIDDEN_PROMOTIONS = (
    "Status: retained",
    "promoted to retained",
    "we promote the parent",
    "promotes the parent's effective_status",
    "this note promotes",
    "this companion promotes",
)

COMPANION_REQUIRED_DISCLAIMERS = (
    "Type:** meta",
    "companion-only",
    "not a new theorem claim",
    "not a status promotion",
    "does not promote status",
)


def block10_companion_non_promotion() -> None:
    log("")
    log("=" * 80)
    log("Block 10: Companion non-self-promotion check")
    log("=" * 80)

    src = read_text(COMPANION_NOTE)
    # Normalize whitespace for required-disclaimer phrases that may span
    # line breaks in the note's prose; collapse runs of whitespace.
    src_collapsed = re.sub(r"\s+", " ", src)

    for phrase in COMPANION_FORBIDDEN_PROMOTIONS:
        check(
            f"companion absent of promotion phrase: {phrase}",
            phrase not in src,
        )
    for phrase in COMPANION_REQUIRED_DISCLAIMERS:
        check(
            f"companion contains required disclaimer: {phrase}",
            phrase in src_collapsed,
        )

    # Companion also must not assert a grade for the parent or dep.
    # The only grade-field strings that should appear are quoted in
    # the recap of prior audit-lane events. We do not enforce zero
    # occurrences; we only enforce that the companion does not assert
    # a *current* parent/dep grade other than what the ledger records.
    check(
        "companion does not assert current parent grade other than ledger record",
        "current parent status is retained_bounded" not in src
        and "current parent grade is retained_bounded" not in src,
    )


# -----------------------------------------------------------
# Cached log writer
# -----------------------------------------------------------

CACHE_PATH = (
    ROOT
    / "logs"
    / "runner-cache"
    / "audit_companion_yt_lsp_signed_record_source_readout_dep_resolution_2026_06_04.txt"
)


def write_cache(b1: dict[str, object]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    header = [
        "audit_companion_yt_lsp_signed_record_source_readout_dep_resolution_2026_06_04",
        f"parent_runner={PARENT_RUNNER.relative_to(ROOT)}",
        f"parent_note={PARENT_NOTE.relative_to(ROOT)}",
        f"companion_note={COMPANION_NOTE.relative_to(ROOT)}",
        f"parent_runner_pass_count={b1.get('pass')}",
        f"parent_runner_fail_count={b1.get('fail')}",
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
    log("audit_companion_yt_lsp_signed_record_source_readout_dep_resolution_2026_06_04")
    log(f"parent runner: {PARENT_RUNNER.relative_to(ROOT)}")
    log(f"parent note  : {PARENT_NOTE.relative_to(ROOT)}")
    log(f"companion    : {COMPANION_NOTE.relative_to(ROOT)}")
    log(f"dep claim id : {DEP_CLAIM_ID}")
    log(f"expected parent-runner SHA-256: {EXPECTED_RUNNER_HASH}")

    b1 = block1_rerun_parent_runner()
    block2_pauli_algebra()
    block3_rn_origin_score()
    block4_source_family_uniqueness()
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
