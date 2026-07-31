#!/usr/bin/env python3
"""Cycle 857: census theorem and exact initial-selection bit accounting.

The Cycle-719 core is a SHA-pinned text/AST-only primary.  This runner never
imports or executes it.  Instead it independently rebuilds the two-bank
geometry, proves the circular-gap counting law, enumerates every admissible
setup, and audits the information needed to select one setup.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

from hashlib import sha1, sha256
import ast
import importlib.abc
from itertools import combinations
import json
from math import ceil, comb, isclose, log2
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockF22-20260729"
EXPECTED_PARENT_HEAD = "db6bb282202f049030056e3a26bc2c68280bbae8"
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}
FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
MIN_CIRCULAR_DISTANCE = 2
CORE_PHASE_COUNT = 2 * FIXTURE_BANKS
EXPECTED_STRATUM_COUNTS = {2: 176, 3: 308, 4: 220, 5: 44}
EXPECTED_STRATUM_FAMILIES = {2: 16, 3: 28, 4: 20, 5: 4}

Setup = tuple[int, int, tuple[int, ...]]


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any cited source primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)
PRIMARY_FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, PRIMARY_FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def git_text(*arguments: str) -> str:
    return subprocess.run(
        ("git", *arguments), cwd=ROOT, check=True, capture_output=True,
        text=True, timeout=20,
    ).stdout.strip()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def function_map(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def has_core_event_range(function: ast.FunctionDef) -> bool:
    """Recognize the pinned core expression ``range(2 * bank_count)``."""

    for node in ast.walk(function):
        if not (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "range"
            and len(node.args) == 1
        ):
            continue
        argument = node.args[0]
        if (
            isinstance(argument, ast.BinOp)
            and isinstance(argument.op, ast.Mult)
            and isinstance(argument.left, ast.Constant)
            and argument.left.value == 2
            and isinstance(argument.right, ast.Name)
            and argument.right.id == "bank_count"
        ):
            return True
    return False


def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    core_functions = function_map(trees[AUDIT_INPUT_PATHS[0]])
    sha_rows = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "access": "SHA_PINNED_WORKTREE_TEXT_AST_ONLY_BLOCKLISTED",
        "sha256": sha_rows[path],
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact": sha_rows[path] == EXPECTED_SHA256[path],
        "git_blob": blob_rows[path],
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact": blob_rows[path] == EXPECTED_GIT_BLOBS[path],
        "head_git_blob": git_text("rev-parse", f"HEAD:{path}"),
    } for path in AUDIT_INPUT_PATHS)
    ast_markers = {
        "interleaved_program_present": "interleaved_program" in core_functions,
        "held_certificate_present": "held_certificate" in core_functions,
        "held_certificate_has_range_2_times_bank_count": (
            "held_certificate" in core_functions
            and has_core_event_range(core_functions["held_certificate"])
        ),
    }
    blocked_loaded = tuple(sorted(
        module for module in sys.modules
        if module.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    result = {
        "finding": (
            "The sole cited primary is SHA/blob pinned and parsed as text/AST "
            "only; its module is BLOCKLISTED and never imported. Literal "
            "AUDIT_INPUT_PATHS exist worktree-relative; full replay is exact; "
            "runtime is below 1400 s and stdout below 150 KB."
        ),
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": (
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS
        ),
        "all_AUDIT_INPUT_PATHS_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"] for row in rows
        ),
        "source_rows": rows,
        "core_AST_markers": ast_markers,
        "BLOCKLISTED_MODULES": BLOCKLISTED_MODULES,
        "direct_frontier_imports": direct_frontier_imports,
        "blocked_modules_loaded": blocked_loaded,
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
        "git_branch": git_text("branch", "--show-current"),
        "expected_git_branch": EXPECTED_BRANCH,
        "parent_merge_base": git_text(
            "merge-base", "HEAD", "physics-loop/proof-grade-blockF21-20260729"
        ),
        "expected_parent_head": EXPECTED_PARENT_HEAD,
        "pass": False,
    }
    result["pass"] = bool(
        result["AUDIT_INPUT_PATHS_literal"]
        and result["all_AUDIT_INPUT_PATHS_existing_worktree_relative"]
        and all(
            row["sha256_exact"]
            and row["git_blob_exact"]
            and row["head_git_blob"] == row["expected_git_blob"]
            for row in rows
        )
        and all(ast_markers.values())
        and not direct_frontier_imports
        and not blocked_loaded
        and not PRIMARY_FIREWALL.hits
        and result["git_branch"] == EXPECTED_BRANCH
        and result["parent_merge_base"] == EXPECTED_PARENT_HEAD
    )
    return result


def derived_719_program_labels(bank_count: int) -> tuple[tuple[str, int], ...]:
    """Independent label-only reconstruction of Cycle-719 interleaving."""

    prefix = [("source", 0)]
    for bank in range(bank_count):
        prefix.append(("bank", bank))
        if bank:
            prefix.append(("cross", bank - 1))
        if bank < bank_count - 1:
            prefix.extend((
                ("handoff", bank),
                ("relay_latch", bank),
                ("relay_swap", bank),
            ))
    reverse: list[tuple[str, int]] = []
    for edge in reversed(range(bank_count - 1)):
        reverse.extend((
            ("relay_swap", edge),
            ("relay_unlatch", edge),
            ("handoff_return", edge),
        ))
    return tuple(prefix + reverse + [("finalizer", 0)])


def graph_distance(left: int, right: int, stations: int) -> int:
    return min((left - right) % stations, (right - left) % stations)


def separated(
    positions: tuple[int, ...], stations: int, minimum_distance: int,
) -> bool:
    return all(
        graph_distance(left, right, stations) >= minimum_distance
        for left, right in combinations(positions, 2)
    )


def enumerate_setups(
    stations: int,
    phase_count: int,
    minimum_sources: int,
    maximum_sources: int,
    minimum_distance: int,
) -> tuple[Setup, ...]:
    return tuple(
        (count, phase, positions)
        for count in range(minimum_sources, maximum_sources + 1)
        for positions in combinations(range(stations), count)
        if separated(positions, stations, minimum_distance)
        for phase in range(phase_count)
    )


def translate(setup: Setup, shift: int, stations: int) -> Setup:
    count, phase, positions = setup
    moved = tuple(sorted((site + shift) % stations for site in positions))
    return count, phase, moved


def orbit(setup: Setup, stations: int) -> tuple[Setup, ...]:
    return tuple(sorted({
        translate(setup, shift, stations) for shift in range(stations)
    }))


def orbit_partition(
    setups: tuple[Setup, ...], stations: int,
) -> tuple[tuple[Setup, ...], ...]:
    universe = set(setups)
    remaining = set(setups)
    rows = []
    while remaining:
        representative = min(remaining)
        row = orbit(representative, stations)
        if not set(row) <= universe:
            raise AssertionError(("translation closure failure", representative))
        rows.append(row)
        remaining.difference_update(row)
    return tuple(sorted(rows, key=lambda row: row[0]))


def prime(number: int) -> bool:
    return number >= 2 and all(
        number % divisor for divisor in range(2, int(number ** 0.5) + 1)
    )


def count_law() -> tuple[dict[str, object], tuple[Setup, ...]]:
    program_labels = derived_719_program_labels(FIXTURE_BANKS)
    stations = len(program_labels)
    phases = tuple(range(CORE_PHASE_COUNT))
    setups = enumerate_setups(
        stations, len(phases), MIN_SOURCES, MAX_SOURCES,
        MIN_CIRCULAR_DISTANCE,
    )
    orbits = orbit_partition(setups, stations)
    rows = []
    for count in range(MIN_SOURCES, MAX_SOURCES + 1):
        placements = tuple({setup[2] for setup in setups if setup[0] == count})
        empty_zero_term = comb(stations - count, count)
        occupied_zero_term = comb(stations - count - 1, count - 1)
        positive_gap_compositions = comb(stations - count - 1, count - 1)
        if positive_gap_compositions % count:
            raise AssertionError(("nonintegral translation shapes", count))
        shape_families = positive_gap_compositions // count
        cycle_closed_form = (
            stations * comb(stations - count, count) // (stations - count)
        )
        family_count = shape_families * len(phases)
        enumerated_count = sum(setup[0] == count for setup in setups)
        rows.append({
            "k": count,
            "site_0_empty_path_term": {
                "formula": "binom(n-k,k)",
                "value": empty_zero_term,
                "role": "site 0 empty leaves a length-(n-1) path",
            },
            "site_0_occupied_path_term": {
                "formula": "binom(n-k-1,k-1)",
                "value": occupied_zero_term,
                "role": "site 0 occupied forces both circular neighbors empty",
            },
            "enumerated_pairwise_separated_site_choices": len(placements),
            "closed_form_site_choices": {
                "formula": (
                    "binom(n-k,k)+binom(n-k-1,k-1)="
                    "n/(n-k)*binom(n-k,k)"
                ),
                "value": cycle_closed_form,
            },
            "cyclic_positive_gap_compositions": positive_gap_compositions,
            "translation_shape_family_choices": shape_families,
            "shape_formula": "binom(n-k-1,k-1)/k",
            "core_event_phase_choices": len(phases),
            "restored_origin_choices": stations,
            "named_product": (
                f"{shape_families} site-shape choices x {len(phases)} phases "
                f"x {stations} origins"
            ),
            "closed_form_setup_formula": (
                "[binom(n-k-1,k-1)/k] * p * n"
            ),
            "closed_form_setup_count": shape_families * len(phases) * stations,
            "enumerated_setup_count": enumerated_count,
            "free_C11_family_count": family_count,
            "formula_equals_enumeration": bool(
                len(placements) == empty_zero_term + occupied_zero_term
                == cycle_closed_form == shape_families * stations
                and enumerated_count == shape_families * len(phases) * stations
                == EXPECTED_STRATUM_COUNTS[count]
                and family_count == EXPECTED_STRATUM_FAMILIES[count]
            ),
        })
    orbit_sizes: dict[int, int] = {}
    for row in orbits:
        orbit_sizes[len(row)] = orbit_sizes.get(len(row), 0) + 1
    all_proper_nonempty = all(0 < setup[0] < stations for setup in setups)
    free_theorem = bool(
        prime(stations)
        and all_proper_nonempty
        and orbit_sizes == {stations: len(orbits)}
    )
    finding = (
        "For n=11 and p=4, N_k=[binom(10-k,k-1)/k]x4x11: "
        "k=2 is 4x4x11=176, k=3 is 7x4x11=308, k=4 is "
        "5x4x11=220, and k=5 is 1x4x11=44. Thus N=748. The "
        "nonempty proper subsets have free C11 translation action, so the "
        "census is exactly 68=748/11 families."
    )
    certificate = {
        "finding": finding,
        "derivation": (
            "Positive circular gaps enforce pairwise separation. Equivalently, "
            "split on site 0 to obtain two path-binomial terms. Dividing the "
            "positive-gap compositions by the k choices of distinguished source "
            "gives translation shapes; cross with the four core event phases and "
            "restore the eleven origins."
        ),
        "constraint_roles": {
            "unlabeled_simple_site_set": (
                "itertools.combinations supplies distinct sites and introduces "
                "neither collision nor k! label factors"
            ),
            "multi_source_lower_bound": "k>=2 removes the zero/one-source sectors",
            "pairwise_separation": (
                "circular distance>=2 is exactly one positive empty-site gap "
                "between successive sources"
            ),
            "packing_ceiling": (
                "positive gaps imply 2k<=11, hence k<=5; no k=6 placement exists"
            ),
            "core_phase_membership": (
                "Cycle-719 held_certificate ranges over 2*bank_count=4 events"
            ),
            "origin_restoration": (
                "C11 translates each site shape through all eleven allocations"
            ),
        },
        "fixture_banks": FIXTURE_BANKS,
        "derived_program_station_labels": program_labels,
        "derived_ring_size": stations,
        "derived_phase_set": phases,
        "rows": tuple(rows),
        "enumerated_total": len(setups),
        "closed_form_total": sum(
            row["closed_form_setup_count"] for row in rows
        ),
        "orbit_count": len(orbits),
        "orbit_size_histogram": orbit_sizes,
        "free_action_theorem": (
            "Because 11 is prime, every nonidentity translation generates C11. "
            "An invariant subset is therefore empty or all of C11; k=2..5 is "
            "neither, so every stabilizer is trivial. The phase label is fixed "
            "by translation."
        ),
        "free_action_conditions_exact": free_theorem,
        "census_sha256": digest(setups),
        "orbit_partition_sha256": digest(orbits),
        "pass": bool(
            all(row["formula_equals_enumeration"] for row in rows)
            and {row["k"]: row["enumerated_setup_count"] for row in rows}
            == EXPECTED_STRATUM_COUNTS
            and len(setups) == 748
            and len(orbits) == 68
            and len(setups) == stations * len(orbits)
            and free_theorem
        ),
    }
    return certificate, setups


def selection_bits(
    count: int, family_count: int, origins: int,
) -> dict[str, object]:
    total_bits = log2(count)
    family_bits = log2(family_count)
    origin_bits = log2(origins)
    return {
        "setup_count": count,
        "family_count": family_count,
        "exact_identity": (
            f"log2({count})=log2({family_count})+log2({origins})"
        ),
        "total_selection_bits": round(total_bits, 12),
        "family_choice_bits": round(family_bits, 12),
        "within_family_allocation_bits": round(origin_bits, 12),
        "minimum_fixed_width_code_bits": ceil(total_bits),
        "identity_exact": bool(
            count == family_count * origins
            and isclose(total_bits, family_bits + origin_bits, abs_tol=1e-14)
        ),
    }


def bit_accounting(
    count_certificate: dict[str, object], setups: tuple[Setup, ...],
) -> dict[str, object]:
    stations = int(count_certificate["derived_ring_size"])
    generating_description = {
        "one_source_atom": {
            "value": "one indistinguishable occupied-site atom",
            "provenance": (
                "CENSUS AXIOM: the bounded multi-source extension; Cycle-719 "
                "supplies one controller token and explicitly leaves distant "
                "multiple-token composition open"
            ),
        },
        "placement_rule": {
            "value": (
                "unlabeled simple k-subsets of C11, k>=2, with circular "
                "pair distance>=2; k<=5 follows from packing"
            ),
            "provenance": (
                "CENSUS AXIOM: pairwise-separated placement admissibility; "
                "the upper endpoint is derived from 2k<=11"
            ),
        },
        "phase_set": {
            "value": tuple(range(CORE_PHASE_COUNT)),
            "provenance": (
                "CORE CONSTANT: Cycle-719 held_certificate uses "
                "range(2*bank_count), specialized at the scope axiom bank_count=2"
            ),
        },
        "ring_size": {
            "value": stations,
            "provenance": (
                "CORE DERIVATION: independent interleaved_program(2) label "
                "reconstruction has eleven stations"
            ),
        },
    }
    description_text = compact(generating_description)
    total = selection_bits(len(setups), 68, stations)
    rows = []
    for stratum in count_certificate["rows"]:
        count = int(stratum["enumerated_setup_count"])
        families = int(stratum["free_C11_family_count"])
        row = selection_bits(count, families, stations)
        row["k"] = stratum["k"]
        rows.append(row)
    finding = (
        "Only the setup selection is input: log2(748)=log2(68)+log2(11) "
        "=6.087462841250+3.459431618637=9.546894459887 bits. The 68-way "
        "choice selects a source-shape/phase family and the 11-way choice "
        "allocates its origin. The generating space is fixed by the named "
        "census axioms and SHA-pinned Cycle-719 core constants."
    )
    certificate = {
        "finding": finding,
        "information_measure": (
            "Ideal uniform choice information log2(N); this is not a claim of "
            "integer fixed-width or prefix-code length. A direct fixed-width "
            "index needs ceil(log2(748))=10 bits."
        ),
        "space_is_derived_selection_only_is_input": True,
        "parameter_selection_input_bits": 0,
        "total": total,
        "per_stratum": tuple(rows),
        "generating_description": generating_description,
        "generating_description_measure": {
            "measure": (
                "exact UTF-8 length of the canonical sorted compact JSON shown "
                "in canonical_text; a serialization length, not Kolmogorov complexity"
            ),
            "canonical_text": description_text,
            "utf8_bytes": len(description_text.encode("utf-8")),
            "utf8_bits": 8 * len(description_text.encode("utf-8")),
            "selection_bits_contributed": 0,
        },
        "pass": bool(
            total["identity_exact"]
            and total["setup_count"] == 748
            and total["family_count"] == 68
            and all(row["identity_exact"] for row in rows)
            and {row["k"]: row["setup_count"] for row in rows}
            == EXPECTED_STRATUM_COUNTS
            and {row["k"]: row["family_count"] for row in rows}
            == EXPECTED_STRATUM_FAMILIES
            and len(description_text.encode("utf-8")) > 0
        ),
    }
    return certificate


def constraint_contributions(stations: int) -> dict[str, object]:
    """Audit each predicate inside one explicit finite ambient universe."""

    ambient = tuple(
        (count, phase, positions)
        for count in range(1, 7)
        for positions in combinations(range(stations), count)
        for phase in range(CORE_PHASE_COUNT + 1)
    )
    predicates = {
        "MIN_MULTISOURCE_k_ge_2": lambda setup: setup[0] >= 2,
        "PACKING_WINDOW_k_le_5": lambda setup: setup[0] <= 5,
        "PAIRWISE_SEPARATION_distance_ge_2": lambda setup: separated(
            setup[2], stations, 2
        ),
        "CORE_PHASE_MEMBERSHIP_phase_lt_4": lambda setup: setup[1] < 4,
    }
    tightened = {
        "MIN_MULTISOURCE_k_ge_2": lambda setup: setup[0] >= 3,
        "PACKING_WINDOW_k_le_5": lambda setup: setup[0] <= 4,
        "PAIRWISE_SEPARATION_distance_ge_2": lambda setup: separated(
            setup[2], stations, 3
        ),
        "CORE_PHASE_MEMBERSHIP_phase_lt_4": lambda setup: setup[1] < 3,
    }
    roles = {
        "MIN_MULTISOURCE_k_ge_2": "excludes the zero/one-source sector",
        "PACKING_WINDOW_k_le_5": (
            "names the packing ceiling; relaxing to k=6 adds nothing because "
            "distance>=2 already makes k=6 impossible on C11"
        ),
        "PAIRWISE_SEPARATION_distance_ge_2": (
            "forbids adjacent occupied sites; relaxing admits every simple subset"
        ),
        "CORE_PHASE_MEMBERSHIP_phase_lt_4": (
            "admits exactly the four core event phases; the ambient fifth phase "
            "is a formal one-notch counterfactual"
        ),
    }

    def accepted(replacements: dict[str, object] | None = None) -> tuple[Setup, ...]:
        active = dict(predicates)
        active.update(replacements or {})
        return tuple(
            setup for setup in ambient
            if all(predicate(setup) for predicate in active.values())
        )

    intersection = accepted()
    rows = []
    for name in predicates:
        relaxed = tuple(
            setup for setup in ambient
            if all(
                predicate(setup)
                for other, predicate in predicates.items()
                if other != name
            )
        )
        one_notch_tight = accepted({name: tightened[name]})
        rows.append({
            "constraint": name,
            "role": roles[name],
            "intersection_count": len(intersection),
            "relaxed_count": len(relaxed),
            "marginal_exclusion_count": len(relaxed) - len(intersection),
            "tightened_one_notch_count": len(one_notch_tight),
            "tightening_exclusion_count": len(intersection) - len(one_notch_tight),
        })
    expected = {
        "MIN_MULTISOURCE_k_ge_2": (792, 44, 572, 176),
        "PACKING_WINDOW_k_le_5": (748, 0, 704, 44),
        "PAIRWISE_SEPARATION_distance_ge_2": (4048, 3300, 220, 528),
        "CORE_PHASE_MEMBERSHIP_phase_lt_4": (935, 187, 561, 187),
    }
    exact_rows = {
        row["constraint"]: (
            row["relaxed_count"],
            row["marginal_exclusion_count"],
            row["tightened_one_notch_count"],
            row["tightening_exclusion_count"],
        ) for row in rows
    }
    finding = (
        "The exact intersection is 748. One-at-a-time relaxation gives "
        "MIN_MULTISOURCE 792 (+44), k<=5 packing window 748 (+0), "
        "PAIRWISE_SEPARATION 4048 (+3300), and CORE_PHASE_MEMBERSHIP "
        "935 (+187). One-notch tightening gives respectively 572, 704, "
        "220, and 561."
    )
    return {
        "finding": finding,
        "ambient_universe": (
            "all (k,phase,simple-site-subset) with k=1..6, phase=0..4, C11 sites"
        ),
        "ambient_count": len(ambient),
        "intersection_count": len(intersection),
        "intersection_sha256": digest(intersection),
        "rows": tuple(rows),
        "pass": bool(len(intersection) == 748 and exact_rows == expected),
    }


def derive_suite() -> tuple[
    dict[str, object], dict[str, object], dict[str, object], tuple[Setup, ...]
]:
    certificate_a, setups = count_law()
    certificate_b = bit_accounting(certificate_a, setups)
    certificate_c = constraint_contributions(
        int(certificate_a["derived_ring_size"])
    )
    return certificate_a, certificate_b, certificate_c, setups


def render(
    certificates: dict[str, dict[str, object]], report: dict[str, object],
) -> str:
    lines = []
    for name, certificate in certificates.items():
        lines.append(
            f"{'PASS' if certificate['pass'] else 'FAIL'} {name} :: "
            + compact(certificate)
        )
        lines.append(f"FINDING {name} :: {certificate['finding']}")
    for row in certificates["A_COUNT_LAW"]["rows"]:
        lines.append(
            f"FORMULA k={row['k']} :: {row['named_product']} = "
            f"{row['enumerated_setup_count']}"
        )
    total = certificates["B_BIT_ACCOUNTING"]["total"]
    lines.append(
        "BITS total :: " + total["exact_identity"] + " :: "
        f"{total['family_choice_bits']} + "
        f"{total['within_family_allocation_bits']} = "
        f"{total['total_selection_bits']}"
    )
    for row in certificates["C_CONSTRAINT_CONTRIBUTIONS"]["rows"]:
        lines.append(
            f"CONSTRAINT {row['constraint']} :: base={row['intersection_count']} "
            f"relaxed={row['relaxed_count']} "
            f"excluded={row['marginal_exclusion_count']} "
            f"tightened={row['tightened_one_notch_count']} "
            f"tightened_excluded={row['tightening_exclusion_count']}"
        )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(
        "CYCLE857_CENSUS_THEOREM_PASS"
        if report["pass"] else "CYCLE857_CENSUS_THEOREM_FAIL"
    )
    return "\n".join(lines) + "\n"


def stable_render(
    certificates: dict[str, dict[str, object]],
    report: dict[str, object],
    controls_base: bool,
) -> str:
    controls = certificates["D_CONTROLS"]
    for _attempt in range(20):
        controls["pass"] = bool(
            controls_base and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
        )
        report["pass"] = all(
            certificate["pass"] for certificate in certificates.values()
        )
        output = render(certificates, report)
        size = len(output.encode("utf-8"))
        if controls["stdout_bytes"] == size and report["stdout_bytes"] == size:
            return output
        controls["stdout_bytes"] = size
        report["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    controls = source_controls()
    source_controls_pass = bool(controls["pass"])
    certificate_a, certificate_b, certificate_c, setups = derive_suite()
    replay_a, replay_b, replay_c, replay_setups = derive_suite()
    deterministic = bool(
        certificate_a == replay_a
        and certificate_b == replay_b
        and certificate_c == replay_c
        and setups == replay_setups
    )
    elapsed = monotonic() - started
    blocked_loaded_end = tuple(sorted(
        module for module in sys.modules
        if module.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    controls.update({
        "source_controls_pass": source_controls_pass,
        "determinism_replay": {
            "method": (
                "repeat independent geometry reconstruction, exhaustive census, "
                "orbit partition, closed forms, bit ledger, and all ambient "
                "constraint counterfactuals"
            ),
            "full_replay_exact": deterministic,
        },
        "blocked_modules_loaded_at_end": blocked_loaded_end,
        "firewall_hits_at_end": tuple(PRIMARY_FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "exact_arithmetic": (
            "All census counts, binomials, C11 translations, intersections, "
            "digests, and integer identities are exact. Decimal log2 values and "
            "monotonic runtime are the only floating-point displays."
        ),
        "certificate_digest_sha256": digest((
            certificate_a, certificate_b, certificate_c
        )),
        "pass": False,
    })
    controls_base = bool(
        source_controls_pass
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not blocked_loaded_end
        and not PRIMARY_FIREWALL.hits
    )
    certificates = {
        "A_COUNT_LAW": certificate_a,
        "B_BIT_ACCOUNTING": certificate_b,
        "C_CONSTRAINT_CONTRIBUTIONS": certificate_c,
        "D_CONTROLS": controls,
    }
    report = {
        "cycle": 857,
        "question": "the census theorem (why exactly 748 starting conditions)",
        "formula": "N_k=[binom(10-k,k-1)/k]*4*11",
        "stratum_counts": EXPECTED_STRATUM_COUNTS,
        "total": 748,
        "free_C11_families": 68,
        "selection_bit_identity": "log2(748)=log2(68)+log2(11)",
        "runtime_seconds": round(elapsed, 6),
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    }
    output = stable_render(certificates, report, controls_base)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(
            "FAIL D_CONTROLS :: " + compact({
                "exception_type": type(error).__name__,
                "exception": str(error),
                "pass": False,
            }) + "\nCYCLE857_CENSUS_THEOREM_FAIL\n"
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
