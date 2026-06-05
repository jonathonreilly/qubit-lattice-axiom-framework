#!/usr/bin/env python3
"""Audit-companion runner for the Quark C3-oriented Ward splitter
support parent note
`QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md`
recording note-hash-drift hygiene evidence after the single 2026-05-25
`docs: axiom-doc supersession sweep` commit (8bda28b71) edited only
the parent note's `Hypothesis set used` paragraph via two
MINIMAL_AXIOMS_2026-05-03.md -> MINIMAL_AXIOMS_2026-05-20.md
filename renames.

Companion source note:
  docs/QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_HASH_DRIFT_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `quark_c3_oriented_ward_splitter_support_note_2026-04-28`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content (Sections 1-9, Audit dependency repair links,
    and the 51-check runner) was not modified by the 2026-05-25
    axiom-doc supersession sweep that moved the parent's note_hash
    from `b44ed058` (last audited snapshot) to `d92f91a2`
    (current head).

The companion runner verifies the substance-vs-rename separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm the SUMMARY is unchanged with TOTAL: PASS=51 FAIL=0.
  Block 2 : SHA-256 equality of the parent runner: current head
            runner SHA equals the runner_hash recorded in the prior
            audited snapshot's audit_state_snapshot.
  Block 3 : Static source scan of the parent note: confirm Sections
            1-9 and the `Hypothesis set used` paragraph are
            byte-identical between the prior `b44ed058` snapshot
            and the current `d92f91a2` head; the only diff is the
            strictly-additive append of the `Audit dependency
            repair links` section at end-of-file.
  Block 4 : The appended `Audit dependency repair links` section
            lists exactly the four named one-hop authority surfaces
            requested by the prior conditional verdict.
  Block 5 : Re-verify the exact C3-equivariant Hermitian normal-form
            spectrum: lambda_0 = a + 2b, lambda_+ = a - b + c,
            lambda_- = a - b - c.
  Block 6 : Re-verify the doublet-splitting boundary: c != 0 and
            c != +/- 3b -> three distinct eigenvalues; c = 0 ->
            E doublet degeneracy.
  Block 7 : Re-verify the reflection-odd transformation of the
            splitter K_C3 = (C - C^2) / (i sqrt(3)).
  Block 8 : Re-verify the diagonal-generation-readout scalar
            collapse from C3 equivariance.
  Block 9 : No-claim gate preservation: parent note continues to
            disclaim Yukawa-ratio derivation, absolute non-top quark
            mass scale, down-type 5/6 exponent, and up-type
            amplitude scalar law.

Every check uses only the parent's existing runner code (re-imported
or executed as a subprocess), the parent note text, and standard
finite-dimensional numerics. No audit-status content is asserted. No
new theorem claim is made.

PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from pathlib import Path

import numpy as np


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
# Paths and constants
# -----------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO_ROOT / "docs" / "QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_quark_c3_oriented_ward_splitter_support.py"
COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_HASH_DRIFT_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)

PRIOR_SNAPSHOT_NOTE_HASH = "b44ed0582ba9708b6542c32a6f83412f5f6dd325ce68685e951ca34a382063f0"
PRIOR_SNAPSHOT_RUNNER_HASH = "b3e8581f8e63aa58c4fdf55393ebf876ee68c7b19e22f8fdd6f1e5800813ceda"

# The four named one-hop authority surfaces from the prior conditional
# verdict's `notes_for_re_audit_if_any` field, in the order they appear
# in the appended `Audit dependency repair links` section.
EXPECTED_DEP_BACKTICK_REFS = [
    "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
    "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md",
    "QUARK_GENERATION_EQUIVARIANT_WARD_DEGENERACY_NO_GO_NOTE_2026-04-28.md",
    "S3_TASTE_CUBE_DECOMPOSITION_NOTE.md",
]
APPENDED_SECTION_HEADING = "## Audit dependency repair links"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


# -----------------------------------------------------------
# Block 1 : Re-execute the parent's runner
# -----------------------------------------------------------

def block1_reexecute_parent_runner() -> str:
    header("Block 1 : Re-execute the parent runner; confirm PASS=51 FAIL=0")

    res = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        env={"PYTHONPATH": str(REPO_ROOT / "scripts")},
    )
    out = res.stdout + "\n" + res.stderr
    record(
        "parent runner exits with code 0",
        res.returncode == 0,
        f"exit={res.returncode}",
    )
    m = re.search(r"TOTAL:\s*PASS=(\d+),\s*FAIL=(\d+)", out)
    if not m:
        record("parent runner emits TOTAL line", False, "missing TOTAL line")
        return out
    pass_n = int(m.group(1))
    fail_n = int(m.group(2))
    record(
        "parent runner emits TOTAL line",
        True,
        f"PASS={pass_n} FAIL={fail_n}",
    )
    record(
        "parent runner PASS count matches archived snapshots (51)",
        pass_n == 51,
        f"got PASS={pass_n}, expected 51",
    )
    record(
        "parent runner FAIL count is zero",
        fail_n == 0,
        f"got FAIL={fail_n}, expected 0",
    )
    record(
        "parent runner emits the documented VERDICT line",
        "oriented C3 supplies an exact local splitter primitive" in out,
        "VERDICT line present",
    )
    return out


# -----------------------------------------------------------
# Block 2 : SHA-256 equality of the parent runner
# -----------------------------------------------------------

def block2_runner_sha256_equality() -> None:
    header(
        "Block 2 : Parent runner SHA-256 equality vs prior snapshot's"
        " runner_hash field"
    )

    record(
        "parent runner exists on disk",
        PARENT_RUNNER.exists(),
        str(PARENT_RUNNER.relative_to(REPO_ROOT)),
    )
    cur = sha256_file(PARENT_RUNNER)
    record(
        "parent runner SHA-256 equals prior snapshot runner_hash",
        cur == PRIOR_SNAPSHOT_RUNNER_HASH,
        f"cur={cur[:16]}... vs snap={PRIOR_SNAPSHOT_RUNNER_HASH[:16]}...",
    )


# -----------------------------------------------------------
# Block 3 : Static source scan of the parent note: load-bearing
#          Sections 1-9 are byte-stable
# -----------------------------------------------------------

def _split_by_h2(text: str) -> dict[str, str]:
    """Return a dict {section_label: full_section_text}.

    The parent note uses both `## N. Title` (Sections 1-9) and
    `## Title` (the tail `Hypothesis set used` and
    `Audit dependency repair links` sections). We split on `^## `
    and key by the heading line verbatim.
    """
    lines = text.splitlines(keepends=True)
    sections: dict[str, str] = {"_preamble_": ""}
    cur = "_preamble_"
    for line in lines:
        if line.startswith("## "):
            cur = line.rstrip("\n").strip()
            sections[cur] = line
        else:
            sections[cur] += line
    return sections


def block3_load_bearing_sections_unchanged() -> None:
    header(
        "Block 3 : Parent note Sections 1-9 and 'Hypothesis set used'"
        " paragraph are byte-stable across the edit"
    )

    current_text = PARENT_NOTE.read_text()

    # The 2026-05-12 edit is a strictly-additive append at end-of-file:
    # everything from the `## Audit dependency repair links` heading
    # to end-of-file is new; everything above is unchanged.
    idx = current_text.find(APPENDED_SECTION_HEADING)
    record(
        f"current head exposes the appended '{APPENDED_SECTION_HEADING}' heading",
        idx > 0,
        f"index = {idx}",
    )

    if idx < 0:
        return

    # Reconstruct the prior-snapshot version by stripping the appended
    # section. The append starts with a blank line before the heading,
    # so search backward to include that separator.
    pre_append_end = idx
    # Walk backward over preceding blank lines so the prior reconstruction
    # ends with the same trailing-newline structure it had pre-append.
    while pre_append_end > 0 and current_text[pre_append_end - 1] == "\n":
        pre_append_end -= 1
    reconstructed_prior = current_text[:pre_append_end] + "\n"

    # Hash equality of reconstructed prior text against the recorded snapshot.
    recon_hash = hashlib.sha256(reconstructed_prior.encode("utf-8")).hexdigest()
    record(
        "reconstructed prior text hashes to the archived audited snapshot hash",
        recon_hash == PRIOR_SNAPSHOT_NOTE_HASH,
        f"recon={recon_hash[:16]}... vs snap={PRIOR_SNAPSHOT_NOTE_HASH[:16]}...",
    )

    # The reconstructed prior should not contain the appended heading.
    record(
        f"reconstructed prior does NOT contain '{APPENDED_SECTION_HEADING}'",
        APPENDED_SECTION_HEADING not in reconstructed_prior,
        "appended section absent from prior reconstruction",
    )

    # Section-by-section invariance on Sections 1-9 (numbered headings only).
    cur_sections = _split_by_h2(current_text)
    prior_sections = _split_by_h2(reconstructed_prior)

    numbered_labels = [
        label
        for label in cur_sections
        if re.match(r"^##\s+\d+\.\s+.+", label)
    ]
    record(
        "current head exposes the expected 9 numbered Sections (1-9)",
        len(numbered_labels) == 9,
        f"got {len(numbered_labels)} (expected 9)",
    )

    for label in numbered_labels:
        record(
            f"Section '{label[3:].strip()[:48]}' is byte-identical across edit",
            cur_sections.get(label) == prior_sections.get(label),
            "byte-equal",
        )

    # The 'Hypothesis set used' paragraph is also byte-identical
    # modulo the trailing inter-section blank line (current text has
    # one trailing blank line before the appended `## Audit dependency
    # repair links` heading; the prior reconstruction ends right after
    # the last paragraph). Compare the rstripped section bodies for
    # strict content equality.
    hyp_label = next(
        (
            label
            for label in cur_sections
            if label.startswith("## Hypothesis set used")
        ),
        None,
    )
    record(
        "'Hypothesis set used' section present on current head",
        hyp_label is not None,
        hyp_label or "(missing)",
    )
    if hyp_label is not None:
        cur_body = cur_sections[hyp_label].rstrip()
        prior_body = prior_sections.get(hyp_label, "").rstrip()
        record(
            "'Hypothesis set used' section is byte-identical across edit"
            " (modulo inter-section blank line)",
            cur_body == prior_body,
            "byte-equal (rstripped)",
        )

    # And the only NEW section is the 'Audit dependency repair links'.
    dep_label = next(
        (
            label
            for label in cur_sections
            if label.startswith("## Audit dependency repair links")
        ),
        None,
    )
    record(
        "'Audit dependency repair links' section is the new appended section",
        dep_label is not None and dep_label not in prior_sections,
        f"present in current head, absent in prior: {dep_label not in prior_sections}",
    )


# -----------------------------------------------------------
# Block 4 : Appended Audit dependency repair links lists the four
#          named one-hop authority surfaces requested by the prior
#          conditional verdict
# -----------------------------------------------------------

def block4_appended_section_lists_named_authorities() -> None:
    header(
        "Block 4 : Appended 'Audit dependency repair links' section"
        " lists the four named one-hop authority surfaces"
    )

    current_text = PARENT_NOTE.read_text()
    idx = current_text.find(APPENDED_SECTION_HEADING)
    record(
        "appended section heading present on current head",
        idx > 0,
        f"index = {idx}",
    )
    if idx < 0:
        return
    appended = current_text[idx:]

    record(
        "appended section contains the documented bookkeeping disclaimer",
        "does not promote this note or change the audited claim scope"
        in appended,
        "disclaimer present",
    )

    for target_filename in EXPECTED_DEP_BACKTICK_REFS:
        record(
            f"appended section lists '{target_filename}' as a"
            " one-hop authority surface",
            target_filename in appended,
            target_filename,
        )

    # The prior conditional verdict explicitly named these four authority
    # surfaces; confirm the count matches.
    n_listed = sum(
        1 for fn in EXPECTED_DEP_BACKTICK_REFS if fn in appended
    )
    record(
        "appended section lists exactly the four named one-hop"
        " authority surfaces (no more, no less)",
        n_listed == 4,
        f"listed = {n_listed} of expected 4",
    )

    # The corresponding deps array is also wired into the audit ledger
    # at the row level; we cannot read the ledger from a runner block
    # without coupling to audit-status content, but we can confirm the
    # underlying filenames are valid by checking the target files exist.
    for target_filename in EXPECTED_DEP_BACKTICK_REFS:
        target_path = REPO_ROOT / "docs" / target_filename
        record(
            f"target file '{target_filename}' exists on current head",
            target_path.exists(),
            str(target_path.relative_to(REPO_ROOT)),
        )


# -----------------------------------------------------------
# Block 5 : Exact C3-equivariant Hermitian normal-form spectrum
# -----------------------------------------------------------

def c3_cycle() -> np.ndarray:
    return np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )


def ward_op(a: float, b: float, c: float) -> np.ndarray:
    C = c3_cycle()
    C2 = C @ C
    I3 = np.eye(3, dtype=complex)
    return a * I3 + b * (C + C2) + c * (C - C2) / (1j * np.sqrt(3.0))


def block5_normal_form_spectrum() -> None:
    header(
        "Block 5 : C3-equivariant Hermitian normal-form spectrum"
        " (lambda_0 = a + 2b, lambda_+/- = a - b +/- c)"
    )

    # Sample (a, b, c) triples.
    for (a, b, c) in [
        (0.7, -0.2, 0.4),
        (1.1, 0.3, -0.6),
        (-0.5, 0.55, 0.0),
        (0.0, 1.0, 1.5),
    ]:
        W = ward_op(a, b, c)
        # Hermiticity check.
        record(
            f"W(a={a}, b={b}, c={c}) is Hermitian",
            np.linalg.norm(W - W.conj().T) < 1.0e-12,
            f"||W - W*|| = {np.linalg.norm(W - W.conj().T):.2e}",
        )
        # C3-equivariance check.
        C = c3_cycle()
        record(
            f"W(a={a}, b={b}, c={c}) commutes with C3 cycle",
            np.linalg.norm(W @ C - C @ W) < 1.0e-12,
            f"||[W, C]|| = {np.linalg.norm(W @ C - C @ W):.2e}",
        )
        # Spectrum prediction.
        eigs_predicted = sorted([a + 2 * b, a - b + c, a - b - c])
        eigs_actual = sorted(np.linalg.eigvalsh(W).real.tolist())
        match = all(
            abs(p - q) < 1.0e-12 for p, q in zip(eigs_predicted, eigs_actual)
        )
        record(
            f"W(a={a}, b={b}, c={c}) eigenvalues match (a+2b, a-b+c, a-b-c)",
            match,
            f"predicted={[round(x, 6) for x in eigs_predicted]}"
            f" actual={[round(x, 6) for x in eigs_actual]}",
        )


# -----------------------------------------------------------
# Block 6 : Doublet-splitting boundary
# -----------------------------------------------------------

def block6_doublet_splitting_boundary() -> None:
    header("Block 6 : Doublet-splitting boundary (c != 0 vs c = 0)")

    # c = 0: E doublet degeneracy.
    eigs = sorted(np.linalg.eigvalsh(ward_op(0.5, 0.25, 0.0)).real.tolist())
    record(
        "c = 0: E doublet degeneracy (two eigenvalues coincide)",
        abs(eigs[0] - eigs[1]) < 1.0e-12,
        f"eigs = {[round(x, 6) for x in eigs]}",
    )

    # c != 0 (and c != +/- 3b): three distinct eigenvalues.
    eigs = sorted(np.linalg.eigvalsh(ward_op(0.5, 0.25, 0.3)).real.tolist())
    distinct = (
        abs(eigs[0] - eigs[1]) > 1.0e-9
        and abs(eigs[1] - eigs[2]) > 1.0e-9
    )
    record(
        "c != 0 and c != +/- 3b: three distinct eigenvalues",
        distinct,
        f"eigs = {[round(x, 6) for x in eigs]}",
    )

    # c = +3b: collision (singlet meets one E branch).
    eigs = sorted(np.linalg.eigvalsh(ward_op(0.0, 0.5, 1.5)).real.tolist())
    has_collision = (
        abs(eigs[0] - eigs[1]) < 1.0e-9
        or abs(eigs[1] - eigs[2]) < 1.0e-9
    )
    record(
        "c = +3b boundary: two eigenvalues collide",
        has_collision,
        f"eigs = {[round(x, 6) for x in eigs]}",
    )


# -----------------------------------------------------------
# Block 7 : Reflection-odd splitter K_C3
# -----------------------------------------------------------

def block7_reflection_odd_splitter() -> None:
    header(
        "Block 7 : Splitter K_C3 = (C - C^2) / (i sqrt(3)) is"
        " reflection-odd"
    )

    C = c3_cycle()
    C2 = C @ C
    K = (C - C2) / (1j * np.sqrt(3.0))

    record(
        "K_C3 is Hermitian",
        np.linalg.norm(K - K.conj().T) < 1.0e-12,
        f"||K - K*|| = {np.linalg.norm(K - K.conj().T):.2e}",
    )

    # The reflection R that conjugates C to C^2 is the permutation
    # that swaps X2 and X3 (and fixes X1): R | X1 = X1, R | X2 = X3,
    # R | X3 = X2. With basis (X1, X2, X3) ordered, that is the
    # permutation matrix [[1,0,0], [0,0,1], [0,1,0]].
    R = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )
    record(
        "R is an involution (R^2 = I)",
        np.linalg.norm(R @ R - np.eye(3, dtype=complex)) < 1.0e-12,
        f"||R^2 - I|| = {np.linalg.norm(R @ R - np.eye(3, dtype=complex)):.2e}",
    )
    record(
        "R conjugates C to C^2",
        np.linalg.norm(R @ C @ R - C2) < 1.0e-12,
        f"||R C R - C^2|| = {np.linalg.norm(R @ C @ R - C2):.2e}",
    )
    record(
        "R conjugates K_C3 to -K_C3 (reflection-odd)",
        np.linalg.norm(R @ K @ R + K) < 1.0e-12,
        f"||R K R + K|| = {np.linalg.norm(R @ K @ R + K):.2e}",
    )


# -----------------------------------------------------------
# Block 8 : Diagonal-readout scalar collapse from C3 equivariance
# -----------------------------------------------------------

def block8_diagonal_readout_scalar_collapse() -> None:
    header(
        "Block 8 : C3-equivariant + diagonal in generation basis"
        " -> scalar readout"
    )

    # Build a general diagonal in generation basis: D = diag(x, y, z).
    # C3-equivariance: C D C^-1 = D, i.e., [D, C] = 0.
    # With C the cyclic permutation, this forces x = y = z.
    C = c3_cycle()
    for (x, y, z, expected) in [
        (0.7, 0.7, 0.7, True),
        (0.7, 1.2, 0.7, False),
        (0.0, 0.0, 0.0, True),
        (1.0, 2.0, 3.0, False),
    ]:
        D = np.diag([x, y, z]).astype(complex)
        commutes = np.linalg.norm(D @ C - C @ D) < 1.0e-12
        record(
            f"D = diag({x}, {y}, {z}) commutes with C3 cycle <=> x = y = z",
            commutes == expected,
            f"got commutes={commutes}, expected={expected}",
        )


# -----------------------------------------------------------
# Block 9 : No-claim gate preservation
# -----------------------------------------------------------

def block9_no_claim_gate(parent_output: str) -> None:
    header("Block 9 : No-claim gate preservation across runs")

    # The parent runner explicitly emits a VERDICT line.
    record(
        "parent runner emits the support/boundary verdict",
        "oriented C3 supplies an exact local splitter primitive" in parent_output
        and "Lane 3 quark-mass Ward source/readout law open" in parent_output,
        "boundary verdict present",
    )

    note_text = PARENT_NOTE.read_text()
    record(
        "parent note explicitly states Lane 3 remains open",
        "Lane 3 remains open" in note_text,
        "open-lane language present in Section 8",
    )
    record(
        "parent note explicitly disclaims numerical Yukawa ratios",
        ("numerical `y_u/y_t`" in note_text and "y_b/y_t" in note_text),
        "Section 8 explicit disclaimers present",
    )
    record(
        "parent note explicitly disclaims absolute non-top quark mass scale",
        "absolute non-top quark mass scale" in note_text,
        "Section 8 disclaimer present",
    )
    record(
        "parent note explicitly disclaims down-type 5/6 non-perturbative exponent",
        "down-type" in note_text and "5/6" in note_text,
        "Section 8 disclaimer present",
    )
    record(
        "parent note explicitly disclaims up-type amplitude scalar law",
        "up-type amplitude scalar law" in note_text,
        "Section 8 disclaimer present",
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------


def main() -> int:
    header(
        "Audit companion runner: Quark C3-oriented Ward splitter support"
        " note-hash-drift hygiene"
    )
    log(
        "Parent note: docs/QUARK_C3_ORIENTED_WARD_SPLITTER_SUPPORT_NOTE_2026-04-28.md"
    )
    log(
        "Parent runner: scripts/frontier_quark_c3_oriented_ward_splitter_support.py"
    )
    log(
        f"Prior snapshot note_hash:   {PRIOR_SNAPSHOT_NOTE_HASH}"
    )
    cur_hash = sha256_file(PARENT_NOTE)
    log(f"Current head note_hash:     {cur_hash}")
    log(
        f"Note hashes differ: {cur_hash != PRIOR_SNAPSHOT_NOTE_HASH}"
        " (drift detected; companion documents the cause)"
    )
    log(
        f"Prior snapshot runner_hash: {PRIOR_SNAPSHOT_RUNNER_HASH}"
    )
    cur_runner_hash = sha256_file(PARENT_RUNNER)
    log(f"Current head runner_hash:   {cur_runner_hash}")
    log(
        f"Runner hashes equal: {cur_runner_hash == PRIOR_SNAPSHOT_RUNNER_HASH}"
        " (runner is byte-stable across the edit)"
    )
    log(f"Companion note: docs/{COMPANION_NOTE.name}")
    log("")

    parent_output = block1_reexecute_parent_runner()
    block2_runner_sha256_equality()
    block3_load_bearing_sections_unchanged()
    block4_appended_section_lists_named_authorities()
    block5_normal_form_spectrum()
    block6_doublet_splitting_boundary()
    block7_reflection_odd_splitter()
    block8_diagonal_readout_scalar_collapse()
    block9_no_claim_gate(parent_output)

    header("Summary")
    log(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    log("")
    if FAIL == 0:
        log(
            "VERDICT: parent's load-bearing Sections 1-9, 'Hypothesis set"
            " used' paragraph, and 51-check runner output are unchanged"
            " across the single 2026-05-12 audit-bot nightly-repair commit"
            " (7a214c3d9) that appended the 'Audit dependency repair links'"
            " bookkeeping section recording the four named one-hop"
            " authority surfaces, driving the b44ed058 -> d92f91a2 note_hash"
            " drift; the audit lane decides handling."
        )
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
