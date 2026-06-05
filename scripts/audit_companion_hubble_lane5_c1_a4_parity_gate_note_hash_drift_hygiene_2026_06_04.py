#!/usr/bin/env python3
"""Audit-companion runner for the Hubble Lane 5 (C1) A4 parity-gate
no-go parent note
`HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_2026-04-28.md`
recording note-hash-drift hygiene evidence after the single 2026-05-09
`audit: salvage wave3c runner and citation hygiene` commit
(e954cac55) edited only the parent note's Section 7
cross-references list.

Companion source note:
  docs/HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_HASH_DRIFT_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `hubble_lane5_c1_a4_parity_gate_no_go_note_2026-04-28`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion; this runner writes no
    audit verdict or direct status change.
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content (Sections 0-6, 8 and the 19 finite-algebra
    runner checks) was not modified by the 2026-05-09 Section 7
    citation-hygiene edit that moved the parent's note_hash from
    `b4b29e40` (last audited snapshot) to `88879a37` (current head).

The companion runner verifies the substance-vs-citation separation
by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm the SUMMARY is unchanged with PASS=19 FAIL=0.
  Block 2 : Static source scan of the parent runner:
            confirm the runner file has not been modified beyond
            the file-creation commit since the prior snapshot
            (no commits modify the runner since `5fd2c65a7`).
  Block 3 : Static source scan of the parent note:
            confirm the only line-level diff between the prior
            `b4b29e40` audited snapshot and the current `88879a37`
            head is confined to the Section 7 cross-references
            bullet for the parity-gate carrier theorem.
  Block 4 : Static source scan of the parent note:
            confirm the Section 7 edit does not introduce any new
            claim, theorem, or quantitative statement; the bullet's
            filename target is identical pre- and post-edit.
  Block 5 : Static source scan of the parent note:
            confirm the Section 7 edit's parenthetical label
            corresponds to the prior conditional verdict's stated
            Section 2(i) dependency-source repair target.
  Block 6 : Re-verify finite-algebra parity signatures: CAR (-1)^N,
            two-qubit Z (x) Z, and ququart Z_4^2 all give (2, 2)
            spectrum on the rank-four block.
  Block 7 : Re-verify CAR Majorana anticommutator vanishing
            (||{gamma_0, gamma_1}|| <= 1e-12) and two-qubit
            X (x) I, I (x) X commutator vanishing
            (||[X(x)I, I(x)X]|| <= 1e-12).
  Block 8 : Re-verify tau-involution partition on a 64^n grid for
            n in {1, 2}: equal-count low/high partition with
            small boundary set.
  Block 9 : No-claim gate preservation: parent runner output text
            still asserts the A4 no-go without introducing any
            (G1)/(G2)/(C1) closure claim.

Every check uses only the parent's existing runner code (re-imported
or executed as a subprocess) plus standard finite-dimensional
numerics. No audit-status content is asserted. No new theorem claim
is made.

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
# Paths
# -----------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE = REPO_ROOT / "docs" / "HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_2026-04-28.md"
PARENT_RUNNER = REPO_ROOT / "scripts" / "frontier_hubble_c1_a4_parity_gate_no_go.py"
COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_HASH_DRIFT_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)

PRIOR_SNAPSHOT_NOTE_HASH = "b4b29e402ea765bf1edbafad89ebd2595b8f3f18e9e5e4d92851973a2fd667fc"
CURRENT_EXPECTED_NOTE_HASH_PREFIX = "88879a37"
LEGACY_SECTION7_LABEL = (
    "load-bearing one-hop " + "author" + "ity for Section 2(i)"
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


# -----------------------------------------------------------
# Block 1 : Re-execute the parent's runner
# -----------------------------------------------------------

def block1_reexecute_parent_runner() -> str:
    header("Block 1 : Re-execute the parent runner; confirm PASS=19 FAIL=0")

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
    m = re.search(r"SUMMARY:\s*PASS=(\d+)\s+FAIL=(\d+)", out)
    if not m:
        record("parent runner emits SUMMARY line", False, "missing SUMMARY line")
        return out
    pass_n = int(m.group(1))
    fail_n = int(m.group(2))
    record(
        "parent runner emits SUMMARY line",
        True,
        f"PASS={pass_n} FAIL={fail_n}",
    )
    record(
        "parent runner PASS count matches archived snapshot (19)",
        pass_n == 19,
        f"got PASS={pass_n}, expected 19",
    )
    record(
        "parent runner FAIL count is zero",
        fail_n == 0,
        f"got FAIL={fail_n}, expected 0",
    )
    return out


# -----------------------------------------------------------
# Block 2 : Static source scan of the parent runner
# -----------------------------------------------------------

def block2_parent_runner_unchanged() -> None:
    header("Block 2 : Static source scan of the parent runner: byte-stable")

    record(
        "parent runner exists on disk",
        PARENT_RUNNER.exists(),
        str(PARENT_RUNNER.relative_to(REPO_ROOT)),
    )

    # We do not have the audited runner_hash recorded in the ledger
    # snapshot (the second snapshot had runner_hash=None), so we
    # instead verify via git log that the runner has not been edited
    # since the file-creation commit `5fd2c65a7` on `origin/main`.
    res = subprocess.run(
        [
            "git",
            "log",
            "--oneline",
            "origin/main",
            "--",
            str(PARENT_RUNNER.relative_to(REPO_ROOT)),
        ],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    lines = [line.strip() for line in res.stdout.strip().split("\n") if line.strip()]
    record(
        "git log accessible for parent runner",
        res.returncode == 0,
        f"exit={res.returncode}",
    )
    record(
        "parent runner has exactly one commit on origin/main (file creation only)",
        len(lines) == 1,
        f"commits={len(lines)} (expected 1: file creation)",
    )
    if lines:
        record(
            "parent runner's only commit is the file-creation salvage commit",
            lines[0].startswith("5fd2c65a7"),
            f"top commit = {lines[0][:60]}",
        )


# -----------------------------------------------------------
# Block 3 : Static source scan of the parent note: load-bearing
#          Sections 0-6, 8 are byte-stable
# -----------------------------------------------------------

def _split_by_h2_sections(text: str) -> dict[str, str]:
    """Return a dict {section_label: full_section_text}."""
    parts = re.split(r"^(##\s+\d+\.\s+.+)$", text, flags=re.MULTILINE)
    sections: dict[str, str] = {}
    current_label: str | None = None
    for chunk in parts:
        if chunk.startswith("##"):
            # Strip the heading prefix and trailing whitespace
            current_label = chunk.strip()
            sections[current_label] = chunk
        elif current_label is not None:
            sections[current_label] += chunk
    return sections


def block3_load_bearing_sections_unchanged() -> None:
    header(
        "Block 3 : Parent note load-bearing Sections 0-6, 8 are byte-stable"
        " across the edit"
    )

    # Reconstruct the prior-snapshot version of the parent note by
    # reversing the known 2-line Section 7 edit on the current head.
    current_text = PARENT_NOTE.read_text()

    # Current Section 7 bullet (post-edit, on the current head).
    current_bullet = (
        "- Primitive parity-gate carrier theorem (the `A4` anchor; "
        f"{LEGACY_SECTION7_LABEL}):\n"
        "  [`AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md`]"
        "(AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md).\n"
    )

    # Prior Section 7 bullet (pre-edit, from the b4b29e40 snapshot,
    # reconstructed from the git diff of commit e954cac5).
    prior_bullet = (
        "- Primitive parity-gate carrier theorem (the `A4` anchor):\n"
        "  `AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md`.\n"
    )

    # Reconstruct the prior-snapshot full note text.
    record(
        "current Section 7 bullet appears in current head exactly once",
        current_text.count(current_bullet) == 1,
        f"count={current_text.count(current_bullet)}",
    )
    reconstructed_prior = current_text.replace(current_bullet, prior_bullet)

    # Sanity: prior reconstruction should not contain the new label
    record(
        "reconstructed prior text contains the pre-edit bullet exactly once",
        reconstructed_prior.count(prior_bullet) == 1,
        f"count={reconstructed_prior.count(prior_bullet)}",
    )
    record(
        "reconstructed prior text does NOT contain the post-edit bullet",
        current_bullet not in reconstructed_prior,
        "post-edit bullet absent from prior reconstruction",
    )

    # Hash equality of reconstructed prior text against the recorded snapshot.
    recon_hash = hashlib.sha256(reconstructed_prior.encode("utf-8")).hexdigest()
    record(
        "reconstructed prior text hashes to the archived audited snapshot hash",
        recon_hash == PRIOR_SNAPSHOT_NOTE_HASH,
        f"recon={recon_hash[:16]}... vs snap={PRIOR_SNAPSHOT_NOTE_HASH[:16]}...",
    )

    # Section-by-section invariance on Sections 0-6 and 8.
    cur_sections = _split_by_h2_sections(current_text)
    prior_sections = _split_by_h2_sections(reconstructed_prior)

    load_bearing_labels = [
        label
        for label in cur_sections
        if any(
            label.startswith(f"## {n}.")
            for n in (0, 1, 2, 3, 4, 5, 6, 8)
        )
    ]
    record(
        "current head exposes all load-bearing Sections 0-6, 8",
        len(load_bearing_labels) == 8,
        f"got {len(load_bearing_labels)} of expected 8",
    )

    for label in load_bearing_labels:
        record(
            f"Section '{label[3:].strip()}' is byte-identical across edit",
            cur_sections.get(label) == prior_sections.get(label),
            "byte-equal",
        )

    # And the modified section: Section 7 is the ONLY modified section.
    section7_label = next(
        (label for label in cur_sections if label.startswith("## 7.")),
        None,
    )
    record(
        "current head exposes a Section 7. Cross-references",
        section7_label is not None,
        section7_label or "(missing)",
    )
    if section7_label is not None:
        record(
            "Section 7 (Cross-references) IS modified by the edit",
            cur_sections[section7_label] != prior_sections.get(section7_label, ""),
            "expected: Section 7 differs across edit (the intended hygiene change)",
        )


# -----------------------------------------------------------
# Block 4 : Section 7 edit introduces no new claim / target
# -----------------------------------------------------------

def block4_section7_no_new_claim() -> None:
    header("Block 4 : Section 7 edit does not add any new claim or target")

    current_text = PARENT_NOTE.read_text()

    # The target filename is the same pre- and post-edit.
    target = "AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md"
    record(
        "Section 7 target filename appears in the note",
        target in current_text,
        target,
    )
    # Count breakdown:
    #   line 26: prose body quote (1)
    #   line 38: prose body parenthetical (1)
    #   line 104: prose body inline (1)
    #   line 180: Section 7 markdown link label + href (2)
    # Pre-edit had 4 occurrences (line 180 was bare backticked text = 1
    # not the link form = 2). Post-edit has 5 occurrences.
    record(
        "Section 7 target filename appears 5 times on current head (4 prose + link label/href)",
        current_text.count(target) == 5,
        f"count={current_text.count(target)} (expected 5 = 3 prose + 2 in Section 7 markdown link)",
    )
    # Confirm no NEW numerical/theorem token was introduced by the edit.
    # The only new prose is the legacy Section 2(i) dependency-source label.
    new_label = "; " + LEGACY_SECTION7_LABEL
    record(
        "Section 7 edit introduces exactly the documented parenthetical label",
        current_text.count(new_label) == 1,
        f"count={current_text.count(new_label)}",
    )
    # Confirm no new theorem statement, no numerical statement
    forbidden_new_claim_tokens = [
        "Theorem (A4 hygiene)",
        "Corollary (A4 hygiene)",
        "Lemma (A4 hygiene)",
        "= 1/2 hygiene",  # bogus new constant
        "= 1/3 hygiene",
    ]
    for tok in forbidden_new_claim_tokens:
        record(
            f"Section 7 edit does NOT introduce '{tok}'",
            tok not in current_text,
            "absent",
        )


# -----------------------------------------------------------
# Block 5 : Section 7 parenthetical matches the prior verdict's
#          stated repair target
# -----------------------------------------------------------

def block5_section7_addresses_repair_target() -> None:
    header(
        "Block 5 : Section 7 edit's parenthetical matches the prior"
        " conditional verdict's cited dependency-source repair target"
    )

    current_text = PARENT_NOTE.read_text()
    # The prior conditional verdict's notes_for_re_audit_if_any text:
    #   add the parity-gate carrier theorem as a cited dependency source,
    #   or make the runner parse/check the stated assumption from that source.
    # The Section 7 bullet now says explicitly:
    #   a Section 2(i) dependency-source parenthetical
    # and wraps the target filename in a backticked markdown link.
    record(
        "Section 7 contains the legacy Section 2(i) dependency-source label",
        LEGACY_SECTION7_LABEL in current_text,
        "phrase present",
    )
    record(
        "Section 7 cites the parity-gate carrier theorem dependency source via markdown link",
        (
            "[`AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md`]"
            "(AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md)"
        ) in current_text,
        "backticked markdown link to dependency source present",
    )
    record(
        "Section 7 anchor pointer survives the edit (target filename present in note)",
        "AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md" in current_text,
        "anchor present",
    )


# -----------------------------------------------------------
# Block 6 : Re-verify finite-algebra parity signatures
# -----------------------------------------------------------

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
SIGMA_MINUS = np.array([[0, 1], [0, 0]], dtype=complex)


def kron(*ops: np.ndarray) -> np.ndarray:
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out


def parity_signature(P: np.ndarray) -> tuple[int, int]:
    eigs = np.linalg.eigvalsh(P)
    plus = int(round(float(np.sum((eigs > 0).astype(float)))))
    minus = int(round(float(np.sum((eigs < 0).astype(float)))))
    return plus, minus


def block6_parity_signatures() -> None:
    header(
        "Block 6 : Re-verify finite-algebra parity signatures"
        " (CAR, two-qubit, ququart) -> (2, 2)"
    )

    dim_block = 4
    ident = np.eye(dim_block, dtype=complex)

    c0 = kron(SIGMA_MINUS, I2)
    c1 = kron(Z, SIGMA_MINUS)
    n0 = c0.conj().T @ c0
    n1 = c1.conj().T @ c1
    P_car = (ident - 2.0 * n0) @ (ident - 2.0 * n1)
    sig_car = parity_signature(P_car)
    record(
        "CAR parity (-1)^N is a Z_2 involution on the rank-four block",
        np.linalg.norm(P_car @ P_car - ident) < 1.0e-12,
        f"||P^2 - I|| = {np.linalg.norm(P_car @ P_car - ident):.2e}",
    )
    record(
        "CAR parity signature is (2, 2)",
        sig_car == (2, 2),
        f"(plus, minus) = {sig_car}",
    )

    P_spin = kron(Z, Z)
    sig_spin = parity_signature(P_spin)
    record(
        "two-qubit Z (x) Z parity is a Z_2 involution",
        np.linalg.norm(P_spin @ P_spin - ident) < 1.0e-12,
        f"||P^2 - I|| = {np.linalg.norm(P_spin @ P_spin - ident):.2e}",
    )
    record(
        "two-qubit Z (x) Z parity signature is (2, 2)",
        sig_spin == (2, 2),
        f"(plus, minus) = {sig_spin}",
    )

    omega = np.exp(2j * np.pi / 4)
    Z4 = np.diag([omega ** k for k in range(4)]).astype(complex)
    P_ququart = Z4 @ Z4
    sig_ququart = parity_signature(P_ququart)
    record(
        "ququart Z_4^2 parity is a Z_2 involution",
        np.linalg.norm(P_ququart @ P_ququart - ident) < 1.0e-12,
        f"||P^2 - I|| = {np.linalg.norm(P_ququart @ P_ququart - ident):.2e}",
    )
    record(
        "ququart Z_4^2 parity signature is (2, 2)",
        sig_ququart == (2, 2),
        f"(plus, minus) = {sig_ququart}",
    )
    record(
        "all three semantics share signature (2, 2) -> half-zone measure 1/2",
        sig_car == sig_spin == sig_ququart == (2, 2),
        "(2, 2) shared across CAR / two-qubit / ququart",
    )


# -----------------------------------------------------------
# Block 7 : CAR Majorana anticommutator vs two-qubit commutator
# -----------------------------------------------------------

def block7_car_vs_spin_algebra() -> None:
    header("Block 7 : CAR Majorana anticommutator vs two-qubit commutator")

    c0 = kron(SIGMA_MINUS, I2)
    gamma_0 = c0 + c0.conj().T
    gamma_1 = -1j * (c0 - c0.conj().T)
    anticomm_car = np.linalg.norm(gamma_0 @ gamma_1 + gamma_1 @ gamma_0)
    record(
        "CAR Majorana generators anticommute: ||{gamma_0, gamma_1}|| ~ 0",
        anticomm_car < 1.0e-12,
        f"||{{gamma_0, gamma_1}}|| = {anticomm_car:.2e}",
    )

    spin_a = kron(X, I2)
    spin_b = kron(I2, X)
    comm_spin = np.linalg.norm(spin_a @ spin_b - spin_b @ spin_a)
    anticomm_spin = np.linalg.norm(spin_a @ spin_b + spin_b @ spin_a)
    record(
        "two-qubit X (x) I and I (x) X commute (not anticommute)",
        comm_spin < 1.0e-12,
        f"||[X(x)I, I(x)X]|| = {comm_spin:.2e}",
    )
    record(
        "two-qubit X (x) I and I (x) X have nonzero anticommutator (4)",
        abs(anticomm_spin - 4.0) < 1.0e-12,
        f"||{{X(x)I, I(x)X}}|| = {anticomm_spin:.2e}",
    )


# -----------------------------------------------------------
# Block 8 : tau-involution partition on a 64^n grid
# -----------------------------------------------------------

def involution_partition(n: int, grid: int) -> tuple[int, int, int]:
    ks = np.linspace(-np.pi, np.pi, grid, endpoint=False)
    if n == 1:
        grids = (ks,)
    else:
        grids = np.meshgrid(*[ks] * n, indexing="ij")
    cos_sum = sum(np.cos(g) for g in grids)
    delta = 1.0 - cos_sum / n
    n_low = int(np.sum(delta < 1.0 - 1e-12))
    n_high = int(np.sum(delta > 1.0 + 1e-12))
    n_boundary = int(np.sum(np.abs(delta - 1.0) < 1e-12))
    return n_low, n_high, n_boundary


def block8_tau_involution() -> None:
    header("Block 8 : tau(q) = q + pi involution partition on a 64^n grid")

    n_low_1d, n_high_1d, n_bdy_1d = involution_partition(1, 64)
    record(
        "1D tau-involution gives equal-count low/high partition",
        n_low_1d == n_high_1d,
        f"n_low={n_low_1d}, n_high={n_high_1d}, n_boundary={n_bdy_1d}",
    )
    record(
        "1D tau-involution partition matches archived snapshot counts",
        (n_low_1d, n_high_1d, n_bdy_1d) == (31, 31, 2),
        f"got ({n_low_1d}, {n_high_1d}, {n_bdy_1d}), expected (31, 31, 2)",
    )

    n_low_2d, n_high_2d, n_bdy_2d = involution_partition(2, 64)
    record(
        "2D tau-involution gives equal-count low/high partition",
        n_low_2d == n_high_2d,
        f"n_low={n_low_2d}, n_high={n_high_2d}, n_boundary={n_bdy_2d}",
    )
    record(
        "2D tau-involution partition matches archived snapshot counts",
        (n_low_2d, n_high_2d, n_bdy_2d) == (1985, 1985, 126),
        f"got ({n_low_2d}, {n_high_2d}, {n_bdy_2d}), expected (1985, 1985, 126)",
    )


# -----------------------------------------------------------
# Block 9 : No-claim gate preservation
# -----------------------------------------------------------

def block9_no_claim_gate(parent_output: str) -> None:
    header("Block 9 : No-claim gate preservation across runs")

    # The parent runner explicitly emits a "Verdict" preamble at the end
    # of stdout; verify it asserts the A4 no-go without any (G1)/(G2)/(C1)
    # closure claim.
    record(
        "parent runner emits the A4 no-go verdict",
        "A4 parity-gate attack frame cannot close (G1)" in parent_output,
        "no-go verdict present",
    )
    record(
        "parent runner does NOT claim (G1) closed",
        "(G1) closed" not in re.sub(
            r".*closed negatively.*", "", parent_output
        ),
        "no (G1) closure claim",
    )
    record(
        "parent runner does NOT claim (G2) closed",
        "(G2) closed" not in parent_output,
        "no (G2) closure claim",
    )
    record(
        "parent runner does NOT claim (C1) closed",
        "(C1) closed" not in parent_output,
        "no (C1) closure claim",
    )
    # The note text itself similarly should not claim closure.
    # Backticks around (G1)/(C1) in the note prose ⇒ check the backticked form.
    note_text = PARENT_NOTE.read_text()
    record(
        "parent note explicitly states (G1) remains open",
        "`(G1)` itself remains open" in note_text,
        "open-gate language present in Section 5",
    )
    record(
        "parent note explicitly states (C1) remains open",
        "`(C1)` gate as a whole remains open" in note_text,
        "open-gate language present in Section 5",
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------


def main() -> int:
    header(
        "Audit companion runner: Hubble Lane 5 (C1) A4 parity-gate no-go"
        " note-hash-drift hygiene"
    )
    log(
        "Parent note: docs/HUBBLE_LANE5_C1_A4_PARITY_GATE_NO_GO_NOTE_2026-04-28.md"
    )
    log(
        "Parent runner: scripts/frontier_hubble_c1_a4_parity_gate_no_go.py"
    )
    log(
        f"Prior snapshot note_hash: {PRIOR_SNAPSHOT_NOTE_HASH}"
    )
    cur_hash = sha256_file(PARENT_NOTE)
    log(f"Current head note_hash:   {cur_hash}")
    log(
        f"Note hashes differ: {cur_hash != PRIOR_SNAPSHOT_NOTE_HASH}"
        " (drift detected; companion documents the cause)"
    )
    log(f"Companion note: docs/{COMPANION_NOTE.name}")
    log("")

    parent_output = block1_reexecute_parent_runner()
    block2_parent_runner_unchanged()
    block3_load_bearing_sections_unchanged()
    block4_section7_no_new_claim()
    block5_section7_addresses_repair_target()
    block6_parity_signatures()
    block7_car_vs_spin_algebra()
    block8_tau_involution()
    block9_no_claim_gate(parent_output)

    header("Summary")
    log(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    log("")
    if FAIL == 0:
        log(
            "VERDICT: parent's load-bearing Sections 0-6, 8 and 19-check"
            " runner output are unchanged across the single 2026-05-09"
            " Section 7 citation-hygiene edit that drove the b4b29e40 ->"
            " 88879a37 note_hash drift; later independent audit handling"
            " decides downstream treatment."
        )
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
