#!/usr/bin/env python3
"""Cycle 746: bounded three-generation locked-archive junction certificate.

The Cycle-741 newest-first shift is realized as an address-map update over
three physical 303-cell regions.  Each exhausted image is deposited in the
next fresh region through a tiled Cycle-745 WRITE_WORD, so no locked region is
physically shifted or reused.  Cycle 742 sees only the ordered D-rail
projection; all six added lock/request rails per archive site are invisible to
that readout embedding.
"""

from __future__ import annotations

import ast
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter

import frontier_cycle745_enforced_dual_rail_lock_2026_07_28 as L745
import frontier_cycle741_physical_bank_renewal_2026_07_28 as N741
import frontier_cycle742_archive_record_readout_feed_2026_07_28 as F742


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/LOCKED_ARCHIVE_CYCLE746_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle745_enforced_dual_rail_lock_2026_07_28.py",
    "scripts/frontier_cycle741_physical_bank_renewal_2026_07_28.py",
    "scripts/frontier_cycle742_archive_record_readout_feed_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STDOUT_LIMIT_BYTES = 150 * 1024
LOCKED_WRITE_WORD = L745.WRITE_WORD
ARCHIVE_ALPHABET = (
    "IDLE",
    "READ",
    "STRAY_WRITE[0]",
    "STRAY_WRITE[1]",
    "RENEWAL_ATTEMPT[g1]",
    "RENEWAL_ATTEMPT[g2]",
    "RENEWAL_ATTEMPT[g3]",
)
W5_RESIDUAL = "axiom-level permanence semantics beyond the declared alphabet"
INDUCTION_STATEMENT = (
    "Base: all occupied archive cells have their archived D bit and "
    "(U,L)=LOCKED. Step: every declared archive-level word preserves every "
    "cell's (D,U,L); hence arbitrary finite words over ARCHIVE_ALPHABET "
    "preserve the complete locked archive."
)
READOUT_EXTENSION = (
    "D-only projection: for every composite tile address "
    "(archive_site, local_745_site), Cycle 742 receives the D value at local "
    "site L745.SITE_LAYOUT['D']; V,U,L,Q_in,Q_accept,Q_refuse are invisible."
)

CHECKS: dict[str, bool] = {}
CHECK_DETAILS: dict[str, dict[str, object]] = {}
OUTPUT_LINES: list[str] = []

Persistent = tuple[int, int, int]
ArchiveState = tuple[Persistent, ...]


def check(label: str, condition: bool, details: dict[str, object]) -> bool:
    """Record one named certificate and emit exactly one PASS/FAIL line."""

    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    CHECK_DETAILS[label] = {"passed": passed, **details}
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label}")
    return passed


def digest(bits: tuple[int, ...]) -> str:
    return sha256(bytes(bits)).hexdigest()


def blank_locked_archive() -> ArchiveState:
    return tuple(
        (0, *L745.UNLOCKED) for _ in range(N741.ARCHIVE_WIDTH)
    )


def archive_d_bits(storage: ArchiveState) -> tuple[int, ...]:
    return tuple(cell[0] for cell in storage)


def physical_slots(
    storage: ArchiveState,
) -> tuple[tuple[int, ...], ...]:
    bits = archive_d_bits(storage)
    return tuple(
        bits[
            slot * N741.RECORD_WIDTH:
            (slot + 1) * N741.RECORD_WIDTH
        ]
        for slot in range(N741.ARCHIVE_SLOTS)
    )


def logical_newest_first(
    storage: ArchiveState,
    occupied_slots: int,
) -> tuple[tuple[int, ...], ...]:
    """Expose append-only physical regions in Cycle-741 newest-first order."""

    slots = physical_slots(storage)
    occupied = tuple(reversed(slots[:occupied_slots]))
    blanks = (N741.ZERO_ARCHIVE_SLOT,) * (
        N741.ARCHIVE_SLOTS - occupied_slots
    )
    return occupied + blanks


def tiled_layout_certificate() -> dict[str, object]:
    """Declare a disjoint composite-address tile above every archive D site."""

    archive_sites = F742.archive_sites()
    local_sites = tuple(
        (rail, L745.SITE_LAYOUT[rail]) for rail in L745.RAILS
    )
    addresses = tuple(
        (base_site, local_site)
        for base_site in archive_sites
        for _rail, local_site in local_sites
    )
    d_addresses = tuple(
        (base_site, L745.SITE_LAYOUT["D"])
        for base_site in archive_sites
    )
    return {
        "archive_payload_sites": len(archive_sites),
        "cells_per_tile": len(local_sites),
        "composite_M2_sites": len(addresses),
        "all_composite_addresses_unique":
            len(addresses) == len(set(addresses)),
        "archive_base_sites_unique":
            len(archive_sites) == len(set(archive_sites)),
        "D_projection_sites": len(d_addresses),
        "D_projection_unique": len(d_addresses) == len(set(d_addresses)),
        "lock_rails_in_layout": all(
            rail in dict(local_sites) for rail in ("U", "L")
        ),
        "transient_rails_in_layout": all(
            rail in dict(local_sites)
            for rail in ("V", "Q_in", "Q_accept", "Q_refuse")
        ),
        "address_model":
            "(Cycle-742 archive base site, Cycle-745 local rail site)",
        "readout_extension": READOUT_EXTENSION,
    }


def own_ast_same_word_certificate() -> dict[str, object]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    aliases = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "LOCKED_WRITE_WORD"
            for target in node.targets
        )
    ]
    exact_alias = (
        len(aliases) == 1
        and isinstance(aliases[0].value, ast.Attribute)
        and aliases[0].value.attr == "WRITE_WORD"
        and isinstance(aliases[0].value.value, ast.Name)
        and aliases[0].value.value.id == "L745"
    )
    separate_lock_assignments = [
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name) and target.id == "LOCK_WORD"
    ]
    landed = L745.ast_same_word_certificate()
    return {
        "exact_L745_WRITE_WORD_alias": exact_alias,
        "separate_LOCK_WORD_assignments": len(separate_lock_assignments),
        "landed_same_word_AST": landed,
        "pass":
            exact_alias
            and not separate_lock_assignments
            and bool(landed["ok"]),
    }


def run_locked_generations() -> dict[str, object]:
    """Run three lawful fills, fresh deposits, locks, and Cycle-742 reads."""

    word = N741.renewal_word()
    data = N741.GENESIS_STATE
    logical_reference = (
        N741.ZERO_ARCHIVE_SLOT,
    ) * N741.ARCHIVE_SLOTS
    storage = blank_locked_archive()
    generation_rows: list[dict[str, object]] = []
    archived_images: list[tuple[int, ...]] = []
    fill_rows: list[dict[str, object]] = []
    direct_refusal_rows = 0
    direct_refusals = 0
    direct_same_value = 0
    direct_opposite_value = 0
    accepted_first_writes = 0
    blocked_first_writes = 0

    for generation, directions in enumerate(
        N741.GENERATION_DIRECTIONS, start=1
    ):
        data_started_genesis = data == N741.GENESIS_STATE
        exhausted, fill = N741.fill_generation(data, directions)
        fill_rows.append(fill)
        source_banks, _source_links = N741.K.M.unpack_state(
            exhausted, N741.FIXTURE_BANKS
        )
        source_payloads = N741.cell_payloads(source_banks)
        image = N741.record_image(exhausted)

        # N741's output is the semantic reference for operating restoration
        # and newest-first archive ordering.  The physical archive side below
        # realizes that same output by fresh-region append plus address relabel.
        combined = N741.pack_combined(exhausted, logical_reference)
        renewed = N741.K.A.apply_semantic(combined, word)
        renewed_data, renewed_reference = N741.split_combined(renewed)

        target_slot = generation - 1
        start = target_slot * N741.RECORD_WIDTH
        end = start + N741.RECORD_WIDTH
        before_storage = storage
        mutable = list(storage)
        first_tags: list[str] = []
        fresh_before = 0
        for offset, offered in enumerate(image):
            index = start + offset
            before = mutable[index]
            fresh_before += int(
                before[0] == 0 and before[1:] == L745.UNLOCKED
            )
            event = L745.apply_word(
                L745.packet(before, offered),
                LOCKED_WRITE_WORD,
            )
            tag = L745.output_tag(event)
            first_tags.append(tag)
            accepted_first_writes += int(tag == "ACCEPTED")
            blocked_first_writes += int(tag != "ACCEPTED")
            mutable[index] = L745.persistent(event)
        storage = tuple(mutable)

        previous_regions_preserved = (
            storage[:start] == before_storage[:start]
            and storage[end:] == before_storage[end:]
        )
        newly_locked = all(
            storage[index] == (image[index - start], *L745.LOCKED)
            for index in range(start, end)
        )

        generation_refusal_rows = 0
        generation_refusals = 0
        for index in range(start, end):
            d_bit = storage[index][0]
            for offered in (0, 1):
                event = L745.apply_word(
                    L745.packet(storage[index], offered),
                    LOCKED_WRITE_WORD,
                )
                refused = (
                    L745.output_tag(event) == "REFUSED"
                    and L745.persistent(event) == storage[index]
                )
                generation_refusal_rows += 1
                generation_refusals += int(refused)
                direct_refusal_rows += 1
                direct_refusals += int(refused)
                direct_same_value += int(refused and offered == d_bit)
                direct_opposite_value += int(refused and offered != d_bit)

        view = logical_newest_first(storage, generation)
        records = F742.embed_archive(view)
        flat_readout = F742.readout_bits(records)
        read_archives = F742.split_archive_bits(flat_readout)
        read_payloads = F742.payloads_from_record_image(read_archives[0])
        packet_matches = tuple(
            bytes(observed) == bytes(expected)
            for observed, expected in zip(read_payloads, source_payloads)
        )
        readout_exact = (
            read_archives == view == renewed_reference
            and bytes(flat_readout)
            == bytes(bit for slot in view for bit in slot)
            and len(records) == N741.ARCHIVE_WIDTH
            and all(packet_matches)
        )

        archived_images.append(image)
        logical_reference = renewed_reference
        data = renewed_data
        generation_rows.append({
            "generation": generation,
            "target_physical_slot": target_slot,
            "fresh_cells_before": fresh_before,
            "first_write_accepts": sum(
                tag == "ACCEPTED" for tag in first_tags
            ),
            "first_write_blocks": sum(
                tag != "ACCEPTED" for tag in first_tags
            ),
            "newly_locked": newly_locked,
            "prior_locked_regions_preserved": previous_regions_preserved,
            "direct_overwrite_rows": generation_refusal_rows,
            "direct_overwrite_refusals": generation_refusals,
            "data_started_genesis": data_started_genesis,
            "operating_data_restored": renewed_data == N741.GENESIS_STATE,
            "fill_orbits": fill["orbit_count"],
            "fill_violations": fill["violation_count"],
            "record_image_sha256": digest(image),
            "logical_archive_sha256":
                tuple(digest(slot) for slot in view),
            "readout_909_bits_exact": readout_exact,
            "readout_packet_matches": packet_matches,
        })

    expected_physical = tuple(
        bit for image in archived_images for bit in image
    )
    all_locked = all(cell[1:] == L745.LOCKED for cell in storage)
    content_exact = archive_d_bits(storage) == expected_physical
    return {
        "storage": storage,
        "archived_images": tuple(archived_images),
        "logical_reference": logical_reference,
        "generation_rows": tuple(generation_rows),
        "fill_rows": tuple(fill_rows),
        "renewal_word": word,
        "accepted_first_writes": accepted_first_writes,
        "blocked_first_writes": blocked_first_writes,
        "direct_refusal_rows": direct_refusal_rows,
        "direct_refusals": direct_refusals,
        "direct_same_value": direct_same_value,
        "direct_opposite_value": direct_opposite_value,
        "all_909_cells_locked": all_locked,
        "physical_content_byte_exact": content_exact,
        "final_data_genesis": data == N741.GENESIS_STATE,
    }


def renewal_attempt_patterns(
    run: dict[str, object],
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    final_logical = run["logical_reference"]
    images = run["archived_images"]
    patterns = []
    for generation, image in enumerate(images, start=1):
        attempted_logical = (image,) + final_logical[:-1]
        attempted_physical_slots = tuple(reversed(attempted_logical))
        patterns.append((
            f"RENEWAL_ATTEMPT[g{generation}]",
            tuple(
                bit
                for slot in attempted_physical_slots
                for bit in slot
            ),
        ))
    return tuple(patterns)


def apply_archive_word(
    storage: ArchiveState,
    label: str,
    renewal_patterns: dict[str, tuple[int, ...]],
) -> tuple[ArchiveState, int]:
    output: list[Persistent] = []
    refusals = 0
    if label in ("IDLE", "READ"):
        for cell in storage:
            after, _event = L745.apply_macro(cell, label)
            output.append(after)
        return tuple(output), refusals
    if label == "STRAY_WRITE[0]":
        offered_bits = (0,) * len(storage)
    elif label == "STRAY_WRITE[1]":
        offered_bits = (1,) * len(storage)
    elif label in renewal_patterns:
        offered_bits = renewal_patterns[label]
    else:
        raise ValueError(("out-of-alphabet archive word", label))
    for cell, offered in zip(storage, offered_bits):
        event = L745.apply_word(
            L745.packet(cell, offered),
            LOCKED_WRITE_WORD,
        )
        output.append(L745.persistent(event))
        refusals += int(L745.output_tag(event) == "REFUSED")
    return tuple(output), refusals


def induction_and_renewal_census(
    run: dict[str, object],
) -> dict[str, object]:
    storage = run["storage"]
    images = run["archived_images"]
    expected = tuple(
        (bit, *L745.LOCKED)
        for image in images
        for bit in image
    )
    base_ok = storage == expected and len(storage) == N741.ARCHIVE_WIDTH
    patterns = dict(renewal_attempt_patterns(run))
    step_rows = []
    renewal_rows = 0
    renewal_refusals = 0
    for label in ARCHIVE_ALPHABET:
        after, refusals = apply_archive_word(storage, label, patterns)
        write_like = label.startswith(("STRAY_WRITE", "RENEWAL_ATTEMPT"))
        row_ok = after == storage and (
            not write_like or refusals == N741.ARCHIVE_WIDTH
        )
        step_rows.append({
            "word": label,
            "archive_preserved": after == storage,
            "refusals": refusals,
            "expected_refusals":
                N741.ARCHIVE_WIDTH if write_like else 0,
            "step_ok": row_ok,
        })
        if label.startswith("RENEWAL_ATTEMPT"):
            renewal_rows += N741.ARCHIVE_WIDTH
            renewal_refusals += refusals
    return {
        "base_cases": N741.ARCHIVE_WIDTH,
        "base_ok": base_ok,
        "step_archive_words": len(step_rows),
        "step_cell_transitions":
            len(step_rows) * N741.ARCHIVE_WIDTH,
        "step_ok": all(row["step_ok"] for row in step_rows),
        "step_rows": tuple(step_rows),
        "renewal_attempt_family":
            "all 3 landed generation images as candidate renewal inputs "
            "x all 909 locked target sites",
        "renewal_attempt_rows": renewal_rows,
        "renewal_attempt_refusals": renewal_refusals,
        "induction_statement": INDUCTION_STATEMENT,
        "arbitrary_finite_composition_derived":
            base_ok and all(row["step_ok"] for row in step_rows),
    }


def certificate_a(run: dict[str, object]) -> tuple[bool, dict[str, object]]:
    first = L745.apply_word(
        L745.packet((0, *L745.UNLOCKED), 1),
        LOCKED_WRITE_WORD,
    )
    second = L745.apply_word(
        L745.packet(L745.persistent(first), 0),
        LOCKED_WRITE_WORD,
    )
    first_fill = run["fill_rows"][0]
    first_generation = run["generation_rows"][0]
    l745_ok = (
        first == L745.expected_first_write(1)
        and L745.output_tag(first) == "ACCEPTED"
        and L745.output_tag(second) == "REFUSED"
        and L745.persistent(second) == (1, *L745.LOCKED)
    )
    n741_ok = (
        first_fill["orbits"][0]["all_invariants"]
        and first_fill["violation_count"] == 0
        and first_generation["operating_data_restored"]
    )
    f742_ok = first_generation["readout_909_bits_exact"]
    details = {
        "L745_one_lawful_case": l745_ok,
        "N741_one_lawful_orbit_and_renewal": n741_ok,
        "F742_one_909_site_readout_case": f742_ok,
    }
    return l745_ok and n741_ok and f742_ok, details


def certificate_b(run: dict[str, object]) -> tuple[bool, dict[str, object]]:
    layout = tiled_layout_certificate()
    ast_result = own_ast_same_word_certificate()
    behavior = (
        run["accepted_first_writes"] == N741.ARCHIVE_WIDTH
        and run["blocked_first_writes"] == 0
        and run["all_909_cells_locked"]
    )
    details = {
        "archive_payload_sites": layout["archive_payload_sites"],
        "cells_per_tile": layout["cells_per_tile"],
        "composite_M2_sites": layout["composite_M2_sites"],
        "layout_unique": layout["all_composite_addresses_unique"],
        "lock_rails_in_layout": layout["lock_rails_in_layout"],
        "readout_extension": layout["readout_extension"],
        "same_word_AST": ast_result,
        "same_word_behavior_all_sites": behavior,
        "tiled_lock_gate_actions_per_generation":
            N741.RECORD_WIDTH * len(LOCKED_WRITE_WORD),
    }
    passed = (
        layout["archive_payload_sites"] == 909
        and layout["cells_per_tile"] == 7
        and layout["composite_M2_sites"] == 6363
        and layout["all_composite_addresses_unique"]
        and layout["archive_base_sites_unique"]
        and layout["D_projection_unique"]
        and layout["lock_rails_in_layout"]
        and layout["transient_rails_in_layout"]
        and ast_result["pass"]
        and behavior
    )
    return bool(passed), details


def certificate_c(
    run: dict[str, object],
    induction: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    direct_expected = 2 * N741.ARCHIVE_WIDTH
    renewal_expected = (
        len(run["archived_images"]) * N741.ARCHIVE_WIDTH
    )
    details = {
        "direct_overwrite_family":
            "both offered bits x every one of 909 locked sites",
        "direct_rows_exhausted": run["direct_refusal_rows"],
        "direct_refusals": run["direct_refusals"],
        "direct_same_value_refusals": run["direct_same_value"],
        "direct_opposite_value_refusals":
            run["direct_opposite_value"],
        "renewal_attempt_family":
            induction["renewal_attempt_family"],
        "renewal_rows_exhausted":
            induction["renewal_attempt_rows"],
        "renewal_refusals":
            induction["renewal_attempt_refusals"],
        "full_product_not_enumerated":
            "2^909 offered archive vectors; replaced by an exhaustive "
            "per-site binary census plus the complete landed-image family",
    }
    passed = (
        run["direct_refusal_rows"] == direct_expected
        and run["direct_refusals"] == direct_expected
        and run["direct_same_value"] == N741.ARCHIVE_WIDTH
        and run["direct_opposite_value"] == N741.ARCHIVE_WIDTH
        and induction["renewal_attempt_rows"] == renewal_expected
        and induction["renewal_attempt_refusals"] == renewal_expected
    )
    return bool(passed), details


def certificate_d(
    induction: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    details = {
        "alphabet": ARCHIVE_ALPHABET,
        "base_cases": induction["base_cases"],
        "base_ok": induction["base_ok"],
        "step_archive_words": induction["step_archive_words"],
        "step_cell_transitions":
            induction["step_cell_transitions"],
        "step_ok": induction["step_ok"],
        "induction_statement": induction["induction_statement"],
        "arbitrary_finite_composition_derived":
            induction["arbitrary_finite_composition_derived"],
    }
    passed = (
        induction["base_cases"] == 909
        and induction["base_ok"]
        and induction["step_archive_words"] == len(ARCHIVE_ALPHABET)
        and induction["step_cell_transitions"]
        == 909 * len(ARCHIVE_ALPHABET)
        and induction["step_ok"]
        and induction["arbitrary_finite_composition_derived"]
    )
    return bool(passed), details


def certificate_e(run: dict[str, object]) -> tuple[bool, dict[str, object]]:
    rows = run["generation_rows"]
    exact = all(
        row["readout_909_bits_exact"]
        and all(row["readout_packet_matches"])
        for row in rows
    )
    details = {
        "generations": len(rows),
        "readout_bits_per_generation": N741.ARCHIVE_WIDTH,
        "byte_exact_by_generation":
            tuple(row["readout_909_bits_exact"] for row in rows),
        "four_payloads_exact_by_generation":
            tuple(
                all(row["readout_packet_matches"]) for row in rows
            ),
        "lock_rails_readout_policy": "invisible under D-only projection",
        "embedding_extension": READOUT_EXTENSION,
    }
    return bool(len(rows) == 3 and exact), details


def certificate_f(run: dict[str, object]) -> tuple[bool, dict[str, object]]:
    rows = run["generation_rows"]
    fresh = all(
        row["fresh_cells_before"] == N741.RECORD_WIDTH
        and row["first_write_accepts"] == N741.RECORD_WIDTH
        and row["first_write_blocks"] == 0
        and row["newly_locked"]
        and row["prior_locked_regions_preserved"]
        and row["data_started_genesis"]
        and row["operating_data_restored"]
        and row["fill_violations"] == 0
        for row in rows
    )
    details = {
        "fresh_cells_by_generation":
            tuple(row["fresh_cells_before"] for row in rows),
        "accepted_first_writes_by_generation":
            tuple(row["first_write_accepts"] for row in rows),
        "blocked_first_writes_by_generation":
            tuple(row["first_write_blocks"] for row in rows),
        "prior_locked_regions_preserved":
            tuple(
                row["prior_locked_regions_preserved"] for row in rows
            ),
        "operating_data_restored":
            tuple(row["operating_data_restored"] for row in rows),
        "physical_content_byte_exact":
            run["physical_content_byte_exact"],
        "final_data_genesis": run["final_data_genesis"],
        "fourth_generation_claimed": False,
    }
    return bool(
        len(rows) == 3
        and fresh
        and run["accepted_first_writes"] == 909
        and run["blocked_first_writes"] == 0
        and run["physical_content_byte_exact"]
        and run["final_data_genesis"]
    ), details


def certificate_g() -> tuple[bool, dict[str, object]]:
    indices = {
        gate.name: index
        for index, gate in enumerate(LOCKED_WRITE_WORD)
    }
    controls = []
    for role, gate_name in (
        ("lock_gate", "lock_transfer"),
        ("cascade_gate", "cascade_lift"),
    ):
        index = indices[gate_name]
        mutant = (
            LOCKED_WRITE_WORD[:index]
            + LOCKED_WRITE_WORD[index + 1:]
        )
        failures = L745.write_behavior_failures(mutant)
        controls.append({
            "role": role,
            "deleted_gate": gate_name,
            "deleted_gate_index": index,
            "failure_count": len(failures),
            "first_failure": failures[0] if failures else None,
            "detected": bool(failures),
        })
    details = {
        "controls": tuple(controls),
        "controls_run": len(controls),
        "all_detected": all(row["detected"] for row in controls),
    }
    return bool(
        len(controls) == 2
        and controls[0]["role"] == "lock_gate"
        and controls[1]["role"] == "cascade_gate"
        and all(row["detected"] for row in controls)
    ), details


def certificate_h(
    earlier_pass: bool,
    run: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    supplies = (
        "Cycle-741 held two-bank/four-packet fixture and its fixed "
        "three-renewal semantic word",
        "one initially blank finite archive payload register: 3*303=909 "
        "binary D sites",
        "one Cycle-745 V,U,L,Q_in,Q_accept,Q_refuse rail extension per D "
        "site, initialized with UNLOCKED and clean request rails",
        "declared finite archive alphabet: IDLE, READ, binary stray writes, "
        "and the three landed-image renewal attempts",
        "Cycle-742 D-only sitewise Record embedding and mathematical readout "
        "conventions",
        "fresh-slot address relabeling for exactly three generations; no "
        "fourth renewal or unbounded archive claim",
    )
    boundary = {
        "locked_archive_derived": True,
        "record_permanence_claimed": False,
        "w5_residual": W5_RESIDUAL,
        "mechanism_scope":
            "archive immutability under ARCHIVE_ALPHABET at event boundaries",
        "supplies": supplies,
        "renewal_generations_verified":
            len(run["generation_rows"]),
        "fourth_renewal_or_unbounded_archive_claimed": False,
    }
    details = {"claim_boundary": boundary}
    passed = (
        earlier_pass
        and boundary["locked_archive_derived"] is True
        and boundary["record_permanence_claimed"] is False
        and boundary["w5_residual"]
        == "axiom-level permanence semantics beyond the declared alphabet"
        and len(boundary["supplies"]) == 6
        and boundary["renewal_generations_verified"] >= 3
        and not boundary[
            "fourth_renewal_or_unbounded_archive_claimed"
        ]
    )
    return bool(passed), details


def main() -> int:
    started = perf_counter()
    try:
        run = run_locked_generations()
        induction = induction_and_renewal_census(run)
        build_error = None
    except Exception as error:
        run = {}
        induction = {}
        build_error = f"{type(error).__name__}: {error}"

    certificates = (
        ("A_landed_anchors_L745_N741_F742", lambda: certificate_a(run)),
        (
            "B_tiling_and_locked_write_same_word_AST_behavior",
            lambda: certificate_b(run),
        ),
        (
            "C_post_archive_refusal_censuses",
            lambda: certificate_c(run, induction),
        ),
        (
            "D_archive_level_induction_base_and_step",
            lambda: certificate_d(induction),
        ),
        (
            "E_readout_byte_exact_all_generations",
            lambda: certificate_e(run),
        ),
        (
            "F_lawful_first_writes_fresh_cells",
            lambda: certificate_f(run),
        ),
        ("G_deletion_controls_lock_and_cascade", certificate_g),
    )
    for label, certificate in certificates:
        try:
            passed, details = certificate()
        except Exception as error:
            passed = False
            details = {
                "error": f"{type(error).__name__}: {error}",
                "build_error": build_error,
            }
        check(label, passed, details)

    earlier_pass = all(CHECKS.values())
    try:
        passed_h, details_h = certificate_h(earlier_pass, run)
    except Exception as error:
        passed_h = False
        details_h = {
            "error": f"{type(error).__name__}: {error}",
            "build_error": build_error,
        }
    check("H_honest_boundary_keys_and_supplies", passed_h, details_h)

    elapsed = perf_counter() - started
    boundary = (
        CHECK_DETAILS["H_honest_boundary_keys_and_supplies"]
        .get("claim_boundary", {
            "locked_archive_derived": False,
            "record_permanence_claimed": False,
            "w5_residual": W5_RESIDUAL,
            "supplies": (),
        })
    )
    generation_rows = run.get("generation_rows", ())
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "all_pass": all(CHECKS.values()),
        "archive_alphabet": ARCHIVE_ALPHABET,
        "archive_payload_sites": N741.ARCHIVE_WIDTH,
        "bounded": True,
        "checks": dict(sorted(CHECK_DETAILS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "claim_boundary": boundary,
        "censuses": {
            "direct_overwrite_rows":
                run.get("direct_refusal_rows", 0),
            "direct_overwrite_refusals":
                run.get("direct_refusals", 0),
            "renewal_attempt_rows":
                induction.get("renewal_attempt_rows", 0),
            "renewal_attempt_refusals":
                induction.get("renewal_attempt_refusals", 0),
        },
        "generation_summary": tuple({
            "generation": row["generation"],
            "fresh_cells": row["fresh_cells_before"],
            "first_write_accepts": row["first_write_accepts"],
            "direct_refusals": row["direct_overwrite_refusals"],
            "readout_exact": row["readout_909_bits_exact"],
            "operating_data_restored":
                row["operating_data_restored"],
        } for row in generation_rows),
        "induction": {
            "base_cases": induction.get("base_cases", 0),
            "base_ok": induction.get("base_ok", False),
            "step_archive_words":
                induction.get("step_archive_words", 0),
            "step_cell_transitions":
                induction.get("step_cell_transitions", 0),
            "step_ok": induction.get("step_ok", False),
            "statement": INDUCTION_STATEMENT,
        },
        "locked_archive_derived":
            boundary.get("locked_archive_derived", False),
        "readout_extension": READOUT_EXTENSION,
        "record_permanence_claimed": False,
        "renewal_generations_verified": len(generation_rows),
        "runtime_seconds": round(elapsed, 6),
        "terminal":
            "CYCLE746_LOCKED_ARCHIVE_PASS"
            if all(CHECKS.values())
            else "CYCLE746_LOCKED_ARCHIVE_HONEST_FAIL",
        "tiling": {
            "payload_tiles": N741.ARCHIVE_WIDTH,
            "rails_per_tile": len(L745.RAILS),
            "total_M2_sites":
                N741.ARCHIVE_WIDTH * len(L745.RAILS),
        },
        "w5_residual": W5_RESIDUAL,
        "word_sizes": {
            "L745_IDLE": len(L745.IDLE_WORD),
            "L745_READ": len(L745.READ_WORD),
            "L745_WRITE": len(LOCKED_WRITE_WORD),
            "N741_RENEWAL": len(run.get("renewal_word", ())),
            "tiled_LOCKED_WRITE_per_generation":
                N741.RECORD_WIDTH * len(LOCKED_WRITE_WORD),
        },
    }
    preliminary = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    estimated_bytes = (
        sum(len(line.encode()) + 1 for line in OUTPUT_LINES)
        + len(preliminary.encode())
        + 4096
    )
    check(
        "OUTPUT_stdout_under_150KB",
        estimated_bytes < STDOUT_LIMIT_BYTES,
        {
            "estimated_upper_bound_bytes": estimated_bytes,
            "limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    report["checks"] = dict(sorted(CHECK_DETAILS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["all_pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE746_LOCKED_ARCHIVE_PASS"
        if report["all_pass"]
        else "CYCLE746_LOCKED_ARCHIVE_HONEST_FAIL"
    )
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    output = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        # This branch should be unreachable because the estimate includes
        # slack; it is still an honest nonzero exit rather than silent output.
        sys.stderr.write(
            f"stdout bound exceeded: {len(output.encode())} bytes\n"
        )
        return 1
    sys.stdout.write(output)
    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
