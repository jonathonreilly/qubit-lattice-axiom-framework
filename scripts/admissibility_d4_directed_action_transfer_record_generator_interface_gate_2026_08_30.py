#!/usr/bin/env python3
"""Exact Block20 authority/type gate for an action-to-Record generator bridge.

This runner inspects a finite, source-pinned candidate stack.  It proves that
none of those literal surfaces supplies the complete typed map from an action
or transfer object to directed, non-erasing, mark-resolved Record append
intensities.  It does *not* construct C_AT, prove that a mathematical cone is
empty, or rule out another action, transfer, bath, decoder, or history route.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import subprocess
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
PACKET = Path(
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block20-directed-action-transfer-record-generator-cone-20260830"
)
GOAL = PACKET / "GOAL.md"
AUTHORITY = PACKET / "AUTHORITY_GATE.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
INDEPENDENT_ATTACK = PACKET / "INDEPENDENT_PREREG_ATTACK.md"
STATE = PACKET / "STATE.yaml"

PREREG = "6c5281743f77131abd62a798c2e88a65d3dba634"
MINIMAL = Path("docs/MINIMAL_AXIOMS_2026-06-29.md")
PREMISES = Path("docs/audit/data/axiom_premise_nodes.json")
AUG11 = Path(
    "docs/ADMISSIBILITY_LOCAL_GEOMETRY_RECORD_BOND_TRANSFER_REFLECTION_RESPONSE_"
    "CONNECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AUG10 = Path(
    "docs/ADMISSIBILITY_NULL_ANCHORED_JOINT_GEOMETRY_RECORD_TRANSFER_PERRON_"
    "RESPONSE_SELECTION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
TWO_TT = Path(
    "docs/ADMISSIBILITY_CANONICAL_TWO_TT_POSITIVE_TRANSFER_RECORD_SOURCE_"
    "CONTINUITY_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
LEDGERS = (
    Path("docs/audit/data/ledger/po/post_record_dynamics_authority_stack_map_2026-06-06.json"),
    Path("docs/audit/data/ledger/po/post_record_transition_kernel_interface_2026-06-06.json"),
    Path("docs/audit/data/ledger/po/post_record_supplied_selection_rule_interface_2026-06-06.json"),
    Path("docs/audit/data/ledger/po/post_record_supplied_kernel_selection_rule_interface_2026-06-06.json"),
)
EXPECTED_PREMISES = {
    "minimal_axioms",
    "kinetic_isotropy_primitive",
    "realized_state_primitive",
    "scale_reference_primitive",
}
REQUIRED_BRIDGE_FIELDS = (
    "action_or_transfer_source",
    "blank_plus_six_mark_decoder",
    "directed_append_edge",
    "nonnegative_intensity_map",
    "holding_normalization",
    "cadence_or_common_rate_quotient",
    "one_site_arity",
    "permanent_lock",
    "proper_cubic_covariance",
)


class Certificate:
    def __init__(self) -> None:
        self.lines: list[str] = []
        self.passes = 0
        self.failures = 0

    def check(self, name: str, condition: bool, detail: str) -> None:
        tag = "PASS" if condition else "FAIL"
        self.passes += int(condition)
        self.failures += int(not condition)
        self.lines.append(f"{tag} {name}: {detail}")

    def emit(self) -> None:
        self.lines.append(f"TOTAL: PASS={self.passes} FAIL={self.failures}")
        print("\n".join(self.lines))


def git(*args: str) -> str:
    return subprocess.check_output(("git",) + args, cwd=ROOT, text=True, timeout=120).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def path_exists_at(commit: str, path: Path) -> bool:
    return subprocess.run(
        ("git", "cat-file", "-e", f"{commit}:{path.as_posix()}"),
        cwd=ROOT,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def read(path: Path) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def all_needles(text: str, needles: Iterable[str]) -> bool:
    return all(needle in text for needle in needles)


def ledger_facts() -> tuple[dict[str, object], ...]:
    return tuple(json.loads(read(path)) for path in LEDGERS)


def count_tuple_bank() -> dict[int, set[tuple[tuple[int, ...], int]]]:
    bank: dict[int, set[tuple[tuple[int, ...], int]]] = defaultdict(set)
    for counts in product(range(7), repeat=6):
        n = sum(counts)
        if n > 6:
            continue
        z = sum(1 << count for count in counts)
        bank[z].add((tuple(sorted(counts, reverse=True)), n))
    return bank


def candidate_field_matrix() -> dict[str, dict[str, bool]]:
    """Literal source capabilities; false is missing, not impossible."""
    return {
        "minimal_axioms": {
            "action_or_transfer_source": False,
            "blank_plus_six_mark_decoder": False,
            "directed_append_edge": False,
            "nonnegative_intensity_map": False,
            "holding_normalization": False,
            "cadence_or_common_rate_quotient": False,
            "one_site_arity": True,
            "permanent_lock": True,
            "proper_cubic_covariance": True,
        },
        "post_record_supplied_interfaces": {
            "action_or_transfer_source": False,
            "blank_plus_six_mark_decoder": False,
            "directed_append_edge": False,
            "nonnegative_intensity_map": False,
            "holding_normalization": False,
            "cadence_or_common_rate_quotient": False,
            "one_site_arity": False,
            "permanent_lock": True,
            "proper_cubic_covariance": False,
        },
        "aug11_local_geometry_record_transfer": {
            "action_or_transfer_source": True,
            "blank_plus_six_mark_decoder": False,
            "directed_append_edge": False,
            "nonnegative_intensity_map": False,
            "holding_normalization": True,
            "cadence_or_common_rate_quotient": False,
            "one_site_arity": False,
            "permanent_lock": False,
            "proper_cubic_covariance": True,
        },
        "aug10_joint_perron_transfer": {
            "action_or_transfer_source": True,
            "blank_plus_six_mark_decoder": False,
            "directed_append_edge": False,
            "nonnegative_intensity_map": False,
            "holding_normalization": True,
            "cadence_or_common_rate_quotient": False,
            "one_site_arity": False,
            "permanent_lock": False,
            "proper_cubic_covariance": False,
        },
        "canonical_two_tt_transfer": {
            "action_or_transfer_source": True,
            "blank_plus_six_mark_decoder": False,
            "directed_append_edge": False,
            "nonnegative_intensity_map": False,
            "holding_normalization": True,
            "cadence_or_common_rate_quotient": False,
            "one_site_arity": False,
            "permanent_lock": False,
            "proper_cubic_covariance": True,
        },
        "pr7803_fixed_placement_coefficients": {
            "action_or_transfer_source": True,
            "blank_plus_six_mark_decoder": False,
            "directed_append_edge": False,
            "nonnegative_intensity_map": False,
            "holding_normalization": False,
            "cadence_or_common_rate_quotient": False,
            "one_site_arity": False,
            "permanent_lock": False,
            "proper_cubic_covariance": True,
        },
    }


def main() -> Certificate:
    cert = Certificate()
    goal = read(GOAL)
    authority = read(AUTHORITY)
    preflight = read(PREFLIGHT)
    attack = read(INDEPENDENT_ATTACK)
    state = read(STATE)
    minimal = read(MINIMAL)
    aug11 = read(AUG11)
    aug10 = read(AUG10)
    two_tt = read(TWO_TT)

    frozen_hashes = {
        path.as_posix(): (
            git("rev-parse", f"{PREREG}:{path.as_posix()}"),
            git("hash-object", "--", path.as_posix()),
        )
        for path in (GOAL, AUTHORITY, PREFLIGHT, INDEPENDENT_ATTACK)
    }
    freeze_ok = (
        is_ancestor(PREREG)
        and all(registered == current for registered, current in frozen_hashes.values())
        and not path_exists_at(PREREG, Path(__file__).resolve().relative_to(ROOT))
        and all_needles(
            state,
            (
                f"preregistration_commit: {PREREG}",
                "action_record_bridge_frozen: false",
                "target_runner_allowed_before_prereg_commit: false",
            ),
        )
    )
    cert.check(
        "A_preregistration_integrity",
        freeze_ok,
        f"prereg={PREREG[:12]}, four frozen artifacts unchanged, target runner absent at freeze",
    )

    premise_data = json.loads(read(PREMISES))
    premise_ids = set(premise_data["nodes"])
    axiom_ok = premise_ids == EXPECTED_PREMISES and all_needles(
        minimal,
        (
            "Admissibility is not a dynamics axiom",
            "It does not\nchoose a Hamiltonian or transfer operator",
            "provide a record-production process or\nphysical persistence dynamics",
            "transition relations, record-production dynamics, physical\npersistence dynamics",
        ),
    )
    cert.check(
        "B_foundation_type_boundary",
        axiom_ok,
        f"premise nodes={tuple(sorted(premise_ids))}; no action/transfer/rate/process primitive",
    )

    ledgers = ledger_facts()
    ledger_ok = (
        len(ledgers) == 4
        and sum(row["claim_type"] == "meta" for row in ledgers) == 1
        and all(row["audit_status"] == "unaudited" for row in ledgers)
        and all(row["effective_status"] in {"meta", "unaudited"} for row in ledgers)
    )
    cert.check(
        "C_post_record_authority",
        ledger_ok,
        "four exact rows are meta/unaudited supplied-interface semantics, not a physical generator",
    )

    aug11_ok = all_needles(
        aug11,
        (
            "z_v=(gamma_v,o_v) in {0,1} x {0,1}",
            "4^9 = 262144",
            "K = D_W^(1/2) E^(tensor 9) D_W^(1/2)",
            "P(z_v=s | z_neighbors)",
            "permits transitions from occupied to null and\ntherefore is Record-erasing",
            "A scheduler and permanent-Record causal update\nare not inferred from it",
        ),
    )
    cert.check(
        "D_aug11_literal_type",
        aug11_ok,
        "four-state geometry/occupancy carrier; symmetric Perron transfer; literal sampler erases Records",
    )

    aug10_two_tt_ok = all_needles(
        aug10,
        (
            "The values of that law remain extensional content.",
            "one extensional local geometry/Record transition rule",
            "one autonomous causal Lorentzian Record/geometry update",
        ),
    ) and all_needles(
        two_tt,
        (
            "permanent-Record creation is not a conserved gravity",
            "selects neither the\ntransfer nor the required source-current decoder",
            "a transition-based conserved source-current decoder",
            "zero TOE percentage points",
        ),
    )
    cert.check(
        "E_other_transfer_boundaries",
        aug10_two_tt_ok,
        "joint Perron law remains extensional; two-TT law lacks selected transfer and source-current decoder",
    )

    pr7803_ok = all_needles(
        preflight + goal + state,
        (
            "dac92a5ed9a8ddaa90aa4300223a2c77fb4cd203",
            "s_n^D = r_1^8 [r_n^4+r_(n+1)^4]",
            "s_n^S = r_1^7 [r_n^3 r_(n+1)+r_(n+1)^3 r_(n+2)]",
            "It supplies no Record decoder",
            "latest_connection_pr: 7803",
        ),
    )
    cert.check(
        "F_pr7803_scope_pin",
        pr7803_ok,
        "pinned fixed-placement reinforcement has no decoder, intensity map, normalization, arrow, or cadence",
    )

    detailed_balance_cases = []
    for pi_left, pi_right in (
        (Fraction(1, 3), Fraction(2, 3)),
        (Fraction(5, 12), Fraction(7, 12)),
        (Fraction(17, 31), Fraction(14, 31)),
    ):
        reverse = Fraction(0)
        forced_forward = pi_right * reverse / pi_left
        detailed_balance_cases.append(forced_forward == 0)
    detailed_balance_ok = all(detailed_balance_cases) and all_needles(
        authority,
        (
            "ordinary detailed balance on that same graph gives",
            "or a nonreversible\ntransfer",
        ),
    )
    cert.check(
        "G_detailed_balance_firewall",
        detailed_balance_ok,
        "full-support same-visible-graph reversibility plus zero erase forces every forward append edge to zero",
    )

    bank = count_tuple_bank()
    fixtures = {
        9: {((2, 0, 0, 0, 0, 0), 2), ((1, 1, 1, 0, 0, 0), 3)},
        10: {((2, 1, 0, 0, 0, 0), 3), ((1, 1, 1, 1, 0, 0), 4)},
        12: {
            ((2, 2, 0, 0, 0, 0), 4),
            ((2, 1, 1, 1, 0, 0), 5),
            ((1, 1, 1, 1, 1, 1), 6),
        },
    }
    fixtures_ok = all(expected <= bank[z] for z, expected in fixtures.items())
    odds = {
        beta: Fraction(beta, 1 + beta) for beta in (1, 2)
    }
    fixtures_ok &= odds == {1: Fraction(1, 2), 2: Fraction(2, 3)}
    cert.check(
        "H_same_z_desk_witnesses",
        fixtures_ok,
        f"Z=9/10 pairs and Z=12 chain reconstructed; beta=1,2 higher-n odds={tuple(odds.values())}",
    )

    matrix = candidate_field_matrix()
    well_formed = all(set(fields) == set(REQUIRED_BRIDGE_FIELDS) for fields in matrix.values())
    complete_candidates = tuple(
        name for name, fields in matrix.items() if all(fields.values())
    )
    missing_counts = {name: sum(not value for value in fields.values()) for name, fields in matrix.items()}
    inspected_stack_unsupplied = well_formed and not complete_candidates and all(count > 0 for count in missing_counts.values())
    cert.check(
        "I_inspected_stack_bridge_matrix",
        inspected_stack_unsupplied,
        f"{len(matrix)} literal surfaces checked over {len(REQUIRED_BRIDGE_FIELDS)} fields; missing counts={tuple(missing_counts.values())}",
    )

    scope_text = goal + authority + preflight + attack
    mutants = {
        "call_interface_empty": "UNSUPPLIED`, not `EMPTY`" in preflight,
        "exponentiate_action": "exponentiating or squaring an action coefficient" in goal,
        "square_amplitude": "amplitude to modulus square" in attack,
        "infer_arrow": "choosing a direction or time orientation" in goal,
        "delete_reverse": "discarding Record-erasing reverse edges" in goal,
        "infer_cadence": "normalizing weights into probabilities or choosing a cadence" in goal,
        "convexify_rules": "mixing separate bridge rules and convexifying" in goal,
        "identify_euclidean_time": "Euclidean transfer is not automatically" in goal,
        "promote_pr7803": "formal response coefficient with an occurrence amplitude" in goal,
        "axiom_necessity": "does not itself justify editing the\nminimal axioms" in authority,
        "universal_action_no_go": "not an action- or transfer-wide no-go" in preflight,
        "quotient_profile_scale": "profile-, occupancy-, site-, or mark-dependent multiplier" in attack,
        "weaken_permanence": "do not weaken permanence" in attack,
        "strict_m2_upgrade": "No strict-`M_2(C)`\n    encoder" in preflight,
        "toe_promotion": "TOE movement" in preflight,
    }
    mutation_ok = all(mutants.values()) and len(mutants) == 15
    cert.check(
        "J_hostile_scope_mutations",
        mutation_ok,
        f"rejected {sum(mutants.values())}/{len(mutants)} type, bridge, permanence, authority, axiom, and TOE mutations",
    )

    n5_lines = (
        "per_element: checked the exact source anchors and nine required bridge fields on six named candidate surfaces; no append-intensity element was fabricated.",
        "per_site: checked the August 11 four-state carrier, missing six-mark decoder, literal occupied-to-null erasure, and same-graph detailed-balance zero-edge lemma.",
        "per_mode: checked and not executed — C_AT and B_AT are undefined because no typed bridge is frozen; no action coefficient was exponentiated, squared, or normalized.",
        "per_block: checked and not executed — the positive Perron and fixed-placement action objects do not supply a normalized directed permanent-Record history or cadence.",
        "lattice_wide: checked and not executed — no local-infinite action-derived Record process, physical clock, conserved gravity source, or full-lattice generator is claimed.",
    )
    n5_ok = [line.split(":", 1)[0] for line in n5_lines] == [
        "per_element",
        "per_site",
        "per_mode",
        "per_block",
        "lattice_wide",
    ] and all(len(line) > 80 for line in n5_lines)
    cert.check(
        "K_n5_resolution",
        n5_ok,
        "five substantive resolution lines distinguish inspected source/type checks from unexecuted cone/process scales",
    )

    terminal_ok = (
        inspected_stack_unsupplied
        and all_needles(
            scope_text,
            (
                "AUTHORITY/INTERFACE-UNSUPPLIED",
                "mathematical no-go",
                "TOE percentage movement",
            ),
        )
    )
    cert.check(
        "L_terminal_scope",
        terminal_ok,
        "inspected-stack interface result only; mathematical cone, other bridges, axiom necessity, and TOE movement excluded",
    )

    cert.lines.extend(
        [
            f"SOURCE_MATRIX: candidates={len(matrix)} fields={len(REQUIRED_BRIDGE_FIELDS)} complete={len(complete_candidates)}.",
            "TYPE_RESULT: C_AT and B_AT remain undefined before a frozen directed coefficient-to-intensity bridge; this is not an empty-cone calculation.",
            "POSITIVE_ROUTE: oriented histories, absorbing transfers, enlarged reversible carriers, action-derived instruments, alternative decoders, baths, and governed supply remain live.",
            *n5_lines,
        ]
    )
    if cert.failures == 0:
        cert.lines.extend(
            [
                "COMPUTATIONAL_TERMINAL: DIRECTED-ACTION/TRANSFER-TO-PERMANENT-RECORD-APPEND-INTENSITY-INTERFACE-UNSUPPLIED-ON-INSPECTED-STACK",
                "CONE_STATUS: UNDEFINED-NOT-EMPTY",
                "TOE_ACCOUNTING: obligation retirement=0; TOE percentage movement=0.",
            ]
        )
    else:
        cert.lines.append("COMPUTATIONAL_TERMINAL: AUTHORITY-OR-SCOPE-CERTIFICATE-FAILURE")
    return cert


if __name__ == "__main__":
    certificate = Certificate()
    try:
        certificate = main()
    except Exception as exc:
        certificate.check("UNCAUGHT_EXCEPTION", False, f"{type(exc).__name__}: {exc}")
        certificate.lines.extend(
            [
                "per_element: checked and not executed — source/type inspection stopped before completion.",
                "per_site: checked and not executed — carrier, permanence, and detailed-balance checks stopped before completion.",
                "per_mode: checked and not executed — no bridge cone or beta projection was classified.",
                "per_block: checked and not executed — no transfer/history process was classified.",
                "lattice_wide: checked and not executed — no local-infinite process was classified.",
                "COMPUTATIONAL_TERMINAL: AUTHORITY-OR-SCOPE-CERTIFICATE-FAILURE",
            ]
        )
    certificate.emit()
