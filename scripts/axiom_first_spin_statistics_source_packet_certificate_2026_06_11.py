#!/usr/bin/env python3
"""Source-packet certificate for the re-scoped spin-statistics row.

This runner does not apply an audit verdict. It verifies the repair target
named by the audit backlog for
AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md:

  * the superseded 2026-04-11 axiom surface is not a load-bearing dependency;
  * the current registered axiom surface is linked;
  * the single-module theorem supplies the explicit `k = 1 => dim_C H_x = 2`
    one-hop authority used by the free-boson/CCR exclusion;
  * the primary spin-statistics runner cache is fresh and passing;
  * the note remains bounded to CCR exclusion plus Grassmann-frame
    consequences and does not reintroduce statistics forcing.
"""

from __future__ import annotations

from pathlib import Path
import hashlib
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md"
PRIMARY_RUNNER = ROOT / "scripts" / "axiom_first_spin_statistics_check.py"
PRIMARY_CACHE = ROOT / "logs" / "runner-cache" / "axiom_first_spin_statistics_check.txt"
MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-05.md"
CL3_NOTE = ROOT / "docs" / "AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md"
NO_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md"
SINGLE_MODULE = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md"
GLF_NOTE = ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {label}{suffix}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def links(text: str) -> set[str]:
    return set(re.findall(r"\]\(([^)]+)\)", text))


def contains_words(text: str, phrase: str) -> bool:
    pattern = r"\s+".join(re.escape(part) for part in phrase.split())
    return re.search(pattern, text) is not None


def section(text: str, heading: str, next_heading_prefix: str = "\n## ") -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    end = text.find(next_heading_prefix, start + len(heading))
    return text[start:] if end < 0 else text[start:end]


def main() -> int:
    print("axiom-first spin-statistics source-packet certificate 2026-06-11")

    for path in [
        NOTE,
        PRIMARY_RUNNER,
        PRIMARY_CACHE,
        MINIMAL_AXIOMS,
        CL3_NOTE,
        NO_FORCING,
        SINGLE_MODULE,
        GLF_NOTE,
    ]:
        check(f"exists: {path.relative_to(ROOT)}", path.exists())

    note = read_text(NOTE)
    primary_cache = read_text(PRIMARY_CACHE)
    single_module = read_text(SINGLE_MODULE)
    minimal_axioms = read_text(MINIMAL_AXIOMS)
    note_links = links(note)

    # Source-note status and scope firewall.
    for phrase in [
        "**Type:** bounded_theorem",
        "**Claim type:** bounded_theorem",
        "Status authority:** independent audit lane only",
        "does not set or predict an audit outcome",
        "source-note proposal",
        "free-boson/CCR exclusion",
        "statistics *forcing* claim is WITHDRAWN",
        "No statistics forcing",
        "No hard-core exclusion",
        "Sets, promotes, or changes **no** row's effective status",
    ]:
        check(f"note contains status/scope phrase: {phrase}", contains_words(note, phrase))

    for phrase in [
        "**Status:** retained",
        "**Status:** source-note proposal",
        "retained branch-local",
        "would become retained",
        "promoted to retained",
        "anticommutation is forced by the baseline",
        "hard-core boson is excluded",
        "Grassmann Fock space is the only finite-dimensional alternative",
    ]:
        check(f"note excludes overclaim: {phrase}", phrase not in note)

    # The exact audit-blocker repair: current axiom surface plus one-hop
    # single-module authority, with the superseded 2026-04-11 note historical.
    expected_links = [
        "../scripts/axiom_first_spin_statistics_check.py",
        "MINIMAL_AXIOMS_2026-06-05.md",
        "AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md",
        "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md",
        "STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md",
    ]
    for target in expected_links:
        check(f"note markdown link present: {target}", target in note_links)
    check(
        "superseded 2026-04-11 axiom file is not a markdown dependency",
        "MINIMAL_AXIOMS_2026-04-11.md" not in note_links,
    )
    check(
        "superseded 2026-04-11 cite is historical only",
        "historical pointer only" in note
        and contains_words(note, "superseded 2026-04-11 axiom cite is replaced"),
    )
    check(
        "current minimal axiom supplies one-qubit-per-site clause",
        "one qubit per site" in minimal_axioms.lower() or "one-qubit" in minimal_axioms.lower(),
    )

    proof = section(note, "## 3. Proof")
    for phrase in [
        "canonical CCR (6) has no finite-dimensional realization",
        "Quantum axiom's one-qubit-per-site content",
        "`k = 1 ⇒ dim_C H_x = 2`",
        "explicit one-hop\nauthority for the finite/dim-2 hypothesis",
        "free boson is excluded",
    ]:
        check(f"proof contains repaired bridge phrase: {phrase}", contains_words(proof, phrase))

    authorities = section(note, "## 4. Cited authorities")
    for phrase in [
        "MINIMAL_AXIOMS_2026-06-05.md",
        "STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md",
        "Quantum axiom",
        "one-qubit-per-site clause",
        "k = 1",
        "dim_C H_x = 2",
        "Grassmann choice remains a",
        "declared frame hypothesis",
    ]:
        check(f"authorities section contains: {phrase}", phrase in authorities)

    packet = section(note, "## 2.1 2026-06-11 Source-Packet Dependency Certificate")
    for phrase in [
        "does not apply an audit verdict",
        "current registered axiom surface",
        "single-module `k = 1 => dim_C H_x = 2` authority",
        "superseded 2026-04-11 axiom file is historical only",
        "hard-core/CAR selection remains out of scope",
    ]:
        check(f"packet section contains: {phrase}", contains_words(packet, phrase))

    for phrase in [
        "**Claim type:** positive_theorem",
        "If* the per-site Hilbert space `H_x`",
        "`k(x) = 1`",
        "`dim_C H_x = 2` exactly",
        "U4 statement that this note does not close",
        "No new",
        "axioms",
    ]:
        check(f"single-module authority contains: {phrase}", contains_words(single_module, phrase))

    # Primary runner/cache is the computational certificate; this companion
    # verifies it is pinned to current source and passed.
    if PRIMARY_RUNNER.exists() and PRIMARY_CACHE.exists():
        runner_sha = sha256(PRIMARY_RUNNER)
        check("primary cache header is v1", primary_cache.startswith("===== runner cache v1 ====="))
        check("primary cache names runner", "runner: scripts/axiom_first_spin_statistics_check.py" in primary_cache)
        check("primary cache pins current runner SHA", f"runner_sha256: {runner_sha}" in primary_cache)
        check("primary cache exit code zero", "exit_code: 0" in primary_cache)
        check("primary cache status ok", "status: ok" in primary_cache)
        check("primary cache has expected total", "TOTAL: PASS=20 FAIL=0" in primary_cache)
        for tag in ["[S2] PASS", "[FALS] PASS", "[S1] PASS", "[S1-CAR] PASS", "[S3] PASS", "[S4] PASS", "[CTX] PASS"]:
            check(f"primary cache contains tag: {tag}", tag in primary_cache)
    else:
        check("primary cache contract can be checked", False, "runner/cache missing")

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
