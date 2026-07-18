#!/usr/bin/env python3
"""Gate the working final minimum-axiom cut-readiness packet."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import os
from pathlib import Path
import py_compile
import re
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MEASURE_TWICE_FINAL_MINIMUM_AXIOM_CUT_READINESS_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
POLICY = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
AXIOM_RUNNER = ROOT / "scripts" / "audit_companion_minimal_axioms_clean_base_exact.py"
VOCAB_RUNNER = ROOT / "scripts" / "vocab_lint.py"
VOCAB_SOURCE = ROOT / "docs" / "repo" / "controlled_vocabulary.yaml"

EVIDENCE = (
    REVIEW / "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md",
    REVIEW / "EXACT_LAW_IRREDUCIBLE_CONTENT_INDEPENDENCE_TOURNAMENT_NOTE_2026-07-14.md",
    REVIEW / "MINIMUM_CONSTITUTIONAL_CONTENT_EXHAUSTION_LEDGER_NOTE_2026-07-14.md",
    REVIEW / "MINIMUM_AXIOM_UPDATE_EXERCISE_SYNTHESIS_AND_CUT_GATE_NOTE_2026-07-14.md",
    REVIEW / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md",
    REVIEW / "FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md",
    REVIEW / "CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md",
    REVIEW / "TEMPORAL_PROTOCOL_EQUIVALENCE_ALTERNATING_FRAME_CYCLE39_NOTE_2026-07-14.md",
    REVIEW / "CUBIC_ONE_QUBIT_CLIFFORD_QCA_UNIQUENESS_CYCLE40_NOTE_2026-07-14.md",
    REVIEW / "COMPLETE_CANDIDATE_LSTAR_ASSEMBLY_CYCLE41_NOTE_2026-07-14.md",
    REVIEW / "REALIZED_HISTORY_EXACT_LAW_IDENTIFIABILITY_CYCLE42_NOTE_2026-07-14.md",
    REVIEW / "STRICT_NN_RECORD_LAW_COMPILER_CYCLE43_NOTE_2026-07-14.md",
    REVIEW / "PROTECTED_MATTER_TRANSPORT_CYCLE44_NOTE_2026-07-14.md",
    REVIEW / "COMPLETE_HISTORY_RECONSTRUCTION_CYCLE45_NOTE_2026-07-14.md",
    REVIEW / "CAUSAL_ORDER_RECORD_DENSITY_METRIC_RECONSTRUCTION_CYCLE46_NOTE_2026-07-14.md",
    REVIEW / "SEED_ORBIT_WRITE_ONCE_TRANSDUCER_CYCLE47_NOTE_2026-07-14.md",
    REVIEW / "RECORD_DERIVED_COHERENT_CARRIER_DECODER_CYCLE48_NOTE_2026-07-14.md",
    REVIEW / "SELF_DESCRIBING_LAW_FOUNDATION_SELECTION_CYCLE49_NOTE_2026-07-14.md",
    REVIEW / "FRAME_CAGED_LOCAL_MOTIF_CYCLE50_NOTE_2026-07-14.md",
    REVIEW / "OPEN_SITE_RESERVATION_HANDSHAKE_CYCLE51_NOTE_2026-07-14.md",
    REVIEW / "SELF_EXTENDING_FRAME_CAGE_RAIL_CYCLE52_NOTE_2026-07-14.md",
    REVIEW / "OFFICIAL_SEED_TO_RAIL_NUCLEATION_CYCLE53_NOTE_2026-07-14.md",
    REVIEW / "AUXILIARY_PAIR_COMPLETION_GATE_CYCLE54_NOTE_2026-07-14.md",
    REVIEW / "LAUNCHER_LAST_FIRST_ROLE_DIFFERENTIATION_CYCLE55_NOTE_2026-07-14.md",
)


@dataclass(frozen=True)
class RunnerSpec:
    path: Path
    expected_pass: int
    args: tuple[str, ...] = ()
    require_result_marker: bool = True
    timeout_seconds: int = 240


RUNNER_SPECS = (
    RunnerSpec(AXIOM_RUNNER, 68),
    RunnerSpec(
        ROOT / "scripts" / "exact_predictive_specification_tournament_2026_07_14.py",
        156,
    ),
    RunnerSpec(
        ROOT / "scripts" / "exact_law_irreducible_content_independence_tournament_2026_07_14.py",
        308,
    ),
    RunnerSpec(
        ROOT / "scripts" / "minimum_constitutional_content_exhaustion_ledger_2026_07_14.py",
        192,
    ),
    RunnerSpec(
        ROOT / "scripts" / "minimum_axiom_update_exercise_synthesis_cut_gate_2026_07_14.py",
        426,
        timeout_seconds=420,
    ),
    RunnerSpec(
        ROOT / "scripts" / "moving_logical_apparatus_append_front_cycle34_2026_07_14.py",
        591,
    ),
    RunnerSpec(
        ROOT / "scripts" / "final_missing_content_census_constitutional_edit_gate_cycle35_2026_07_14.py",
        171,
    ),
    RunnerSpec(
        ROOT / "scripts" / "cubic_cz_edge_rule_uniqueness_selection_cycle36_2026_07_14.py",
        136,
        require_result_marker=False,
    ),
    RunnerSpec(
        ROOT / "scripts" / "temporal_protocol_equivalence_alternating_frame_cycle39_2026_07_14.py",
        172,
        require_result_marker=False,
    ),
    RunnerSpec(
        ROOT / "scripts" / "cubic_one_qubit_clifford_qca_uniqueness_cycle40_2026_07_14.py",
        127,
        require_result_marker=False,
    ),
    RunnerSpec(
        ROOT / "scripts" / "complete_candidate_lstar_assembly_cycle41_2026_07_14.py",
        205,
    ),
    RunnerSpec(
        ROOT / "scripts" / "realized_history_exact_law_identifiability_cycle42_2026_07_14.py",
        116,
    ),
    RunnerSpec(
        ROOT / "scripts" / "strict_nn_record_law_compiler_cycle43_2026_07_14.py",
        170,
    ),
    RunnerSpec(
        ROOT / "scripts" / "protected_matter_transport_cycle44_2026_07_14.py",
        139,
    ),
    RunnerSpec(
        ROOT / "scripts" / "complete_history_reconstruction_cycle45_2026_07_14.py",
        136,
    ),
    RunnerSpec(
        ROOT / "scripts" / "causal_order_record_density_metric_reconstruction_cycle46_2026_07_14.py",
        115,
    ),
    RunnerSpec(
        ROOT / "scripts" / "seed_orbit_write_once_transducer_cycle47_2026_07_14.py",
        76,
    ),
    RunnerSpec(
        ROOT / "scripts" / "record_derived_coherent_carrier_decoder_cycle48_2026_07_14.py",
        65,
    ),
    RunnerSpec(
        ROOT / "scripts" / "self_describing_law_foundation_selection_cycle49_2026_07_14.py",
        225,
    ),
    RunnerSpec(
        ROOT / "scripts" / "frame_caged_local_motif_cycle50_2026_07_14.py",
        85,
    ),
    RunnerSpec(
        ROOT / "scripts" / "open_site_reservation_handshake_cycle51_2026_07_14.py",
        98,
    ),
    RunnerSpec(
        ROOT / "scripts" / "self_extending_frame_cage_rail_cycle52_2026_07_14.py",
        169,
    ),
    RunnerSpec(
        ROOT / "scripts" / "official_seed_to_rail_nucleation_cycle53_2026_07_14.py",
        97,
    ),
    RunnerSpec(
        ROOT / "scripts" / "auxiliary_pair_completion_gate_cycle54_2026_07_14.py",
        258,
    ),
    RunnerSpec(
        ROOT / "scripts" / "launcher_last_first_role_differentiation_cycle55_2026_07_14.py",
        86,
    ),
)

RUNNERS = tuple(spec.path for spec in RUNNER_SPECS)
FOUNDATION = (AXIOMS, REGISTRY, POLICY, AXIOM_RUNNER)


def unique_paths(paths: tuple[Path, ...]) -> tuple[Path, ...]:
    return tuple(dict.fromkeys(path.resolve() for path in paths))


SCOPED_FILES = unique_paths(
    (
        SELF,
        NOTE,
        *FOUNDATION,
        VOCAB_RUNNER,
        VOCAB_SOURCE,
        *EVIDENCE,
        *RUNNERS,
    )
)
PYTHON_SOURCES = tuple(path for path in SCOPED_FILES if path.suffix == ".py")
VOCAB_TARGETS = (NOTE, SELF)

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    for marker in ("*", "`"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def subprocess_environment() -> dict[str, str]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return env


def relative_paths(paths: tuple[Path, ...]) -> list[str]:
    return [str(path.resolve().relative_to(ROOT)) for path in paths]


def file_hashes(paths: tuple[Path, ...]) -> dict[Path, str]:
    return {
        path: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in paths
        if path.is_file()
    }


def source_contract() -> None:
    section("A - Sources, authority, and live-surface boundary")
    for path in SCOPED_FILES:
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    check("A packet is authority-free", "authority: none" in note)
    check("A packet disclaims axiom amendment", "does not amend an axiom" in note)
    check("A packet disclaims audit verdict", "issue an audit verdict" in note)
    check("A packet records no-PR provenance", "no pr has been created" in note)
    check(
        "A live foundation still has four names",
        all(
            name in axioms
            for name in (
                "lattice / physical locality",
                "qubit / site possibility",
                "admissibility / local constraint",
                "record / fixed reality",
            )
        ),
    )
    check(
        "A live Admissibility remains non-dynamics",
        "admissibility is not a dynamics axiom" in axioms,
    )
    check(
        "A live Record remains unchanged",
        "records form" in axioms and "records are permanent" in axioms,
    )


def decision_contract() -> None:
    section("B - Minimum-content, scope, actuality, and no-cut decision")
    note = normalized(NOTE)
    check(
        "B thirteen-interface record-law-complete scope is defined",
        "record-law complete means" in note,
    )
    check(
        "B TOE-predictively-complete scope is defined",
        "toe-predictively complete means" in note,
    )
    check(
        "B L41 scope is record-law but not TOE-predictive",
        "l41^r3" in note
        and "record-law complete" in note
        and "neither strict-nn record-law complete nor toe-predictively complete"
        in note,
    )
    required = (
        "no other universal axiom content has survived deletion",
        "minimum scientifically justified live edit",
        "none",
        "placeholder, not a predictive completion",
        "the blocker is not wording",
        "absent exact referent",
        "record and qualification remain unchanged",
        "temporal quotient is law-relative",
        "actual history cannot select the missing counterfactual map by itself",
        "realized-state primitive supplies only pointwise state reference",
        "does not prove the distinct state -> h reconstruction",
        "event_readiness_local_causal_domain",
        "first open toe checklist field is physical clock rate/lapse",
        "cycle 44 closes its destructive-reset channel conflict conditionally",
        "record-derived predictive decoder",
        "frame_retaining_open_quartet_phase_transducer",
        "self_extending_frame_cage_rail",
        "one-target reservation handshake",
        "cycle 52 closes autonomous rail renewal",
        "six-site binary macrocode",
        "direct_target_only_exact_nn_nucleator",
        "pair_and_launch_completion_gate",
        "first_role_differentiation",
        "cycle 48 closes the first exit exactly",
        "singleton observed image without coverage",
        "direct foundation-uniqueness theorem remains a separate zero-edit route",
    )
    for phrase in required:
        check(f"B packet contains: {phrase}", phrase in note)
    for rejected in (
        "two witnesses",
        "clock language",
        "storage and recurrence",
        "probability and actuality prose",
    ):
        check(f"B rejected generic clause is classified: {rejected}", rejected in note)


def placement_and_surface_contract() -> None:
    section("C - Placement, compatibility, and synchronized surface")
    note = normalized(NOTE)
    checks = (
        ("C zero-edit route retained", "zero edit" in note and "uniquely derive" in note),
        (
            "C local-law placement retained",
            "retype admissibility" in note and "availability projection" in note,
        ),
        (
            "C global-law placement retained",
            "separate law identification" in note
            and "global history/process/action" in note,
        ),
        ("C Record gate is conditional", "revise record only if" in note),
        ("C Qualification gate is conditional", "revise qualification only if" in note),
        ("C registry surface is named", "axiom_premise_nodes.json" in note),
        ("C policy surface is named", "axiom_minimality_policy.md" in note),
        (
            "C runner surface is named",
            "audit_companion_minimal_axioms_clean_base_exact.py" in note,
        ),
        (
            "C owner wording iteration remains required",
            "iterate its exact constitutional wording with the owner" in note,
        ),
    )
    for label, condition in checks:
        check(label, condition)


def anti_recursion_contract() -> None:
    section("D - Runner-manifest recursion and duplication controls")
    resolved_runners = tuple(path.resolve() for path in RUNNERS)
    check("D final runner excludes itself", SELF not in resolved_runners)
    check(
        "D runner manifest has no duplicates",
        len(resolved_runners) == len(set(resolved_runners)),
    )
    synthesis = next(
        spec.path
        for spec in RUNNER_SPECS
        if spec.path.name
        == "minimum_axiom_update_exercise_synthesis_cut_gate_2026_07_14.py"
    )
    check(
        "D synthesis companion manifest excludes final runner",
        SELF.name not in synthesis.read_text(encoding="utf-8"),
    )


def terminal_counts(output: str) -> tuple[int, int] | None:
    combined = re.findall(
        r"(?m)^(?:TOTAL:\s*)?PASS=(\d+)\s+FAIL=(\d+)\s*$",
        output,
    )
    if combined:
        passed, failed = combined[-1]
        return int(passed), int(failed)
    pass_only = re.findall(r"(?m)^PASS=(\d+)\s*$", output)
    fail_only = re.findall(r"(?m)^FAIL=(\d+)\s*$", output)
    if pass_only and fail_only:
        return int(pass_only[-1]), int(fail_only[-1])
    return None


def runner_regression() -> None:
    section("E - Strict companion-runner regression")
    for spec in RUNNER_SPECS:
        command = [sys.executable, str(spec.path), *spec.args]
        try:
            result = subprocess.run(
                command,
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=spec.timeout_seconds,
                check=False,
                env=subprocess_environment(),
            )
            output = result.stdout + result.stderr
        except subprocess.TimeoutExpired as exc:
            check(
                f"E runner returns: {spec.path.name}",
                False,
                f"timeout after {spec.timeout_seconds}s",
            )
            continue

        counts = terminal_counts(output)
        tail = " | ".join(output.strip().splitlines()[-4:])
        check(
            f"E runner returns zero: {spec.path.name}",
            result.returncode == 0,
            tail,
        )
        check(
            f"E runner strict total: {spec.path.name}",
            counts == (spec.expected_pass, 0),
            f"observed={counts!r} expected=({spec.expected_pass}, 0)",
        )
        if spec.require_result_marker:
            check(
                f"E runner result marker: {spec.path.name}",
                "RESULT: PASS" in output,
            )
        failure_diagnostics = [
            line
            for line in output.splitlines()
            if line.startswith("FAIL") and not re.fullmatch(r"FAIL=0", line.strip())
        ]
        check(
            f"E runner has no failure diagnostics: {spec.path.name}",
            not failure_diagnostics,
            " | ".join(failure_diagnostics[:3]),
        )


def compilation_contract() -> None:
    section("F - Python compilation, vocabulary, whitespace, and diff hygiene")
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="measure-twice-pycompile-") as tmp:
        target = Path(tmp)
        for index, path in enumerate(PYTHON_SOURCES):
            try:
                py_compile.compile(
                    str(path),
                    cfile=str(target / f"{index:03d}-{path.stem}.pyc"),
                    doraise=True,
                )
            except py_compile.PyCompileError as exc:
                failures.append(f"{path.name}: {exc.msg}")
    check(
        "F every scoped Python source compiles into a temporary directory",
        not failures,
        " | ".join(failures[:3]),
    )


def vocabulary_contract() -> None:
    command = [
        sys.executable,
        str(VOCAB_RUNNER),
        "--report-only",
        *relative_paths(VOCAB_TARGETS),
    ]
    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
        env=subprocess_environment(),
    )
    output = result.stdout + result.stderr
    tail = " | ".join(output.strip().splitlines()[-4:])
    check("F packet report-only vocabulary lint returns zero", result.returncode == 0, tail)
    check(
        "F packet report-only vocabulary lint is clean",
        "vocab_lint: 0 files with violations" in output,
        tail,
    )


def whitespace_contract() -> None:
    trailing: list[str] = []
    missing_newline: list[str] = []
    for path in SCOPED_FILES:
        if not path.is_file():
            continue
        data = path.read_bytes()
        if data and not data.endswith(b"\n"):
            missing_newline.append(path.name)
        for line_number, raw_line in enumerate(data.splitlines(keepends=True), 1):
            body = raw_line.rstrip(b"\r\n")
            if body.endswith((b" ", b"\t")):
                trailing.append(f"{path.name}:{line_number}")
    check(
        "F scoped text has no trailing spaces or tabs",
        not trailing,
        ", ".join(trailing[:8]),
    )
    check(
        "F every nonempty scoped file ends with a newline",
        not missing_newline,
        ", ".join(missing_newline[:8]),
    )


def git_hygiene_contract() -> None:
    scoped = relative_paths(SCOPED_FILES)
    for label, command in (
        ("F unstaged scoped git diff-check is clean", ["git", "diff", "--check", "--", *scoped]),
        (
            "F staged scoped git diff-check is clean",
            ["git", "diff", "--cached", "--check", "--", *scoped],
        ),
    ):
        result = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
        detail = " | ".join((result.stdout + result.stderr).strip().splitlines()[-4:])
        check(label, result.returncode == 0, detail)

    foundation_status = subprocess.run(
        [
            "git",
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
            "--",
            *relative_paths(FOUNDATION),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    detail = " | ".join(
        (foundation_status.stdout + foundation_status.stderr).strip().splitlines()[-4:]
    )
    check(
        "F live foundation surfaces have no staged, unstaged, or untracked diff",
        foundation_status.returncode == 0 and not foundation_status.stdout.strip(),
        detail,
    )


def read_only_contract(before: dict[Path, str]) -> None:
    after = file_hashes(SCOPED_FILES)
    changed = [
        path.name
        for path, digest in before.items()
        if after.get(path) != digest
    ]
    created_or_removed = sorted(
        path.name for path in set(before).symmetric_difference(after)
    )
    check(
        "F all scoped source hashes are unchanged by this gate",
        not changed and not created_or_removed,
        "changed=" + ",".join(changed + created_or_removed),
    )


def main() -> int:
    before = file_hashes(SCOPED_FILES)
    source_contract()
    decision_contract()
    placement_and_surface_contract()
    anti_recursion_contract()
    runner_regression()
    compilation_contract()
    vocabulary_contract()
    whitespace_contract()
    git_hygiene_contract()
    read_only_contract(before)
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "CUT_READINESS: HOLD -- no strict-NN record-law-complete referent and "
        "no TOE-predictively-complete referent/uniqueness theorem"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
