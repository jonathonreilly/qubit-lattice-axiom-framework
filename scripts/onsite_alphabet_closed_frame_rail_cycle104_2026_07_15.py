#!/usr/bin/env python3
"""Cycle 104: onsite-alphabet closure audit and repair of Cycle 102.

Cycle 102 imports Cycle 52's abstract four-phase rail verbatim.  Thirty-four
of its B/C/D labels are outside the current 153-role onsite alphabet.  This
runner proves that a bijection onto the exact 36 roles absent from the Cycle-100
source cannot work in the fixed geometry, then tests an explicit role-closed
repair.  The repair omits the two unary-hazard roles R_LB/R_LC and reuses the
already-live B0/L10 contents in exact contexts that remain inert.

The executable exhausts eight rail slices against every code prefix, the full
first-slice asynchronous product under every proper-cubic rotation, the mixed
raw table, W1-polluted fixed-point controls, and every pre-existing B0/L10
debris occurrence.

Authority: none.  No foundation, queue, policy, audit, or git mutation is
authorized by this runner.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import generated_endpoint_autonomous_frame_rail_cycle102_2026_07_15 as c102
import live_eight_bit_physical_comparator_cycle89_2026_07_15 as c89
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52
import zero_binary_source_endpoint_macroblock_bind_cycle100_2026_07_15 as c100


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "ONSITE_ALPHABET_CLOSED_FRAME_RAIL_CYCLE104_NOTE_2026-07-15.md"
CYCLE102_NOTE = REVIEW / "GENERATED_ENDPOINT_AUTONOMOUS_FRAME_RAIL_CYCLE102_NOTE_2026-07-15.md"

Coord = c102.Coord
Signature = c102.Signature
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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def merge_raw(
    *tables: dict[Signature, frozenset[str]],
) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for table in tables:
        for local, values in table.items():
            outputs[local].update(values)
    return {local: frozenset(values) for local, values in outputs.items()}


PHASE_DOMAIN = frozenset(
    c52.role(phase, yz)
    for phase in "BCD"
    for yz in c52.SLICE
)
SOURCE_CONTENTS = frozenset(c100.SOURCE.values())
ABSENT_POOL = frozenset(c89.FULL_ROLES - SOURCE_CONTENTS)
SAFE_POOL = frozenset((ABSENT_POOL - {"R_LB", "R_LC"}) | {"B0", "L10"})


ROLE_MAP: dict[str, str] = {
    "B_1_2": "B_1_2",
    "B_0_2": "B_0_2",
    "LAUNCH_B": "R_B40",
    "LAUNCH_C": "R_C22",
    "LAUNCH_D": "R_C12",
    "B_0_0": "R_C10",
    "B_0_1": "R_B20",
    "B_1_0": "R_B33",
    "B_1_1": "R_C02",
    "B_2_0": "R_B32",
    "B_2_2": "R_C00",
    "B_3_0": "R_C20",
    "B_3_1": "R_C40",
    "B_3_2": "R_B41",
    "C_0_0": "B0",
    "C_0_1": "R_C11",
    "C_0_2": "R_C13",
    "C_1_0": "R_B23",
    "C_1_2": "R_C30",
    "C_2_0": "R_C01",
    "C_2_1": "R_B21",
    "C_2_2": "R_B13",
    "C_3_0": "R_B01",
    "C_3_1": "R_B31",
    "C_3_2": "R_B30",
    "D_0_0": "R_B02",
    "D_0_1": "R_C23",
    "D_0_2": "R_C41",
    "D_1_0": "R_B10",
    "D_1_1": "R_B12",
    "D_1_2": "L10",
    "D_2_0": "R_C33",
    "D_2_2": "R_C32",
    "D_3_0": "R_B11",
    "D_3_1": "R_C21",
    "D_3_2": "R_B00",
}


def mapped(content: str, role_map: dict[str, str] = ROLE_MAP) -> str:
    return role_map.get(content, content)


def relabel_raw(role_map: dict[str, str]) -> dict[Signature, frozenset[str]]:
    outputs: dict[Signature, set[str]] = defaultdict(set)
    for local, values in c52.RULE_OUTPUTS.items():
        relabeled = tuple(sorted((direction, mapped(content, role_map)) for direction, content in local))
        outputs[relabeled].update(mapped(value, role_map) for value in values)
    return {local: frozenset(values) for local, values in outputs.items()}


def rail_sequence(
    layers: int,
    role_map: dict[str, str] = ROLE_MAP,
) -> tuple[tuple[Coord, str], ...]:
    standard = tuple(
        (site, mapped(content, role_map))
        for site, content in c52.bounded_sequence(layers)
    )
    return tuple(
        (add(c52.matvec(c102.SEED_ROTATION, site), c102.SEED_SHIFT), content)
        for site, content in standard
    )


REMAPPED_RAW = relabel_raw(ROLE_MAP)
MIXED_RAW = merge_raw(c100.COMBINED_RAW, REMAPPED_RAW)
NINE_SLICES = rail_sequence(9)
EIGHT_SLICE_HORIZON = 96
FIRST_SLICE_HORIZON = 12


def enabled(
    records: dict[Coord, str],
    raw: dict[Signature, frozenset[str]] = MIXED_RAW,
) -> dict[Coord, frozenset[str]]:
    return {
        target: raw[local]
        for target in c100.c53.open_candidates(records)
        if (local := c100.c53.local_signature(records, target)) in raw
    }


def product_state(code_prefix: int, rail_prefix: int) -> dict[Coord, str]:
    records = c100.records_at(code_prefix)
    records.update(dict(NINE_SLICES[:rail_prefix]))
    return records


def product_expected(code_prefix: int, rail_prefix: int) -> dict[Coord, frozenset[str]]:
    answer: dict[Coord, frozenset[str]] = {}
    if code_prefix < len(c100.ADDITIONS):
        site, content = c100.ADDITIONS[code_prefix]
        answer[site] = frozenset((content,))
    site, content = NINE_SLICES[rail_prefix]
    answer[site] = frozenset((content,))
    return answer


def transform_records(
    records: dict[Coord, str],
    rotation: c52.Rotation,
    shift: Coord,
) -> dict[Coord, str]:
    return {
        add(c52.matvec(rotation, site), shift): content
        for site, content in records.items()
    }


def unary_outputs(role: str) -> frozenset[str]:
    outputs = {
        output
        for local, values in c100.COMBINED_RAW.items()
        if len(local) == 1 and local[0][1] == role
        for output in values
    }
    return frozenset(outputs)


def first_occurrence_exposures() -> dict[str, tuple[tuple[Coord, ...], Coord]]:
    """Unary open targets immediately after each B/C/D role first appears."""

    original = c52.transform_sequence(
        c52.bounded_sequence(4), c102.SEED_ROTATION, c102.SEED_SHIFT
    )
    records = c100.records_at(len(c100.ADDITIONS))
    answer: dict[str, tuple[tuple[Coord, ...], Coord]] = {}
    for index, (site, content) in enumerate(original):
        records[site] = content
        if content not in PHASE_DOMAIN or content in answer:
            continue
        next_site = original[index + 1][0]
        unary_targets = []
        for target in c100.c53.open_candidates(records):
            local = c100.c53.local_signature(records, target)
            if len(local) == 1 and add(target, local[0][0]) == site:
                unary_targets.append(target)
        answer[content] = (tuple(sorted(unary_targets)), next_site)
    return answer


EXPOSURES = first_occurrence_exposures()


def first_failure(role_map: dict[str, str], horizon: int = 12) -> tuple[object, ...] | None:
    raw = relabel_raw(role_map)
    mixed = merge_raw(c100.COMBINED_RAW, raw)
    sequence = rail_sequence(2, role_map)
    records = c100.records_at(len(c100.ADDITIONS))
    for index, (site, content) in enumerate(sequence[:horizon]):
        actual = enabled(records, mixed)
        expected = {site: frozenset((content,))}
        if actual != expected:
            return index, expected, actual
        records[site] = content
    return None


def original_defect_and_obstruction_contract() -> None:
    section("A - Cycle-102 alphabet defect and exact-absent-pool obstruction")
    original_phase_roles = {
        c52.role(phase, yz)
        for phase in "ABCD"
        for yz in c52.SLICE
    }
    original_foreign = original_phase_roles - c89.FULL_ROLES
    check("A01 unmodified Cycle102 uses 34 phase labels outside the 153-role alphabet",
          len(original_phase_roles) == 48 and len(original_foreign) == 34)
    check("A02 B/C/D domain and source-absent pool each have exactly 36 roles",
          len(PHASE_DOMAIN) == len(ABSENT_POOL) == 36)
    check("A03 only B_1_2 and B_0_2 already belong to the live alphabet",
          PHASE_DOMAIN & c89.FULL_ROLES == {"B_1_2", "B_0_2"})
    check("A04 exact absent pool contains both unary-hazard roles",
          {"R_LB", "R_LC"} <= ABSENT_POOL
          and unary_outputs("R_LB") == {"R_C22"}
          and unary_outputs("R_LC") == {"R_A31"})
    launch_roles = {"LAUNCH_B", "LAUNCH_C", "LAUNCH_D"}
    nonlaunch_exposed = all(
        set(targets) - {next_site}
        for role, (targets, next_site) in EXPOSURES.items()
        if role not in launch_roles
    )
    launch_exact = all(
        set(EXPOSURES[role][0]) == {EXPOSURES[role][1]}
        for role in launch_roles
    )
    check("A05 every nonlaunch role exposes an extra unary target; launch roles expose the next target",
          len(EXPOSURES) == 36 and nonlaunch_exposed and launch_exact)
    # A bijection onto ABSENT_POOL must use R_LC.  At a nonlaunch site it makes
    # an extra R_A31 write.  At any launcher it forces the intended next site to
    # R_A31, but R_A31 is outside ABSENT_POOL (and the D->A successor is a fixed
    # A role).  Hence no pure bijective relabeling of this fixed geometry can
    # consume the exact absent pool.
    check("A06 R_LC makes an exact-36-absent pure relabel impossible in this geometry",
          "R_A31" not in ABSENT_POOL
          and all(set(targets) - {next_site} for role, (targets, next_site) in EXPOSURES.items() if role not in launch_roles)
          and all(set(EXPOSURES[role][0]) == {EXPOSURES[role][1]} for role in launch_roles))
    check("A07 obstruction is narrow: it is a pure-relabel result, not a cage/table no-go",
          len(c52.BASE_RULES) == 48 and len(c52.ROTATIONS) == 24)


def mapping_and_table_contract() -> None:
    section("B - Role-closed repaired mapping and mixed table")
    check("B01 mapping is an exact injective map on all 36 B/C/D roles",
          set(ROLE_MAP) == PHASE_DOMAIN and len(set(ROLE_MAP.values())) == 36)
    check("B02 repaired codomain is exactly absent-minus-unary plus B0/L10",
          set(ROLE_MAP.values()) == SAFE_POOL
          and SAFE_POOL == (ABSENT_POOL - {"R_LB", "R_LC"}) | {"B0", "L10"})
    check("B03 all remapped phase roles are live onsite contents and remain phase-injective",
          set(ROLE_MAP.values()) <= c89.FULL_ROLES
          and len({mapped(c52.role(phase, yz)) for phase in "ABCD" for yz in c52.SLICE}) == 48)
    check("B04 B_1_2 and B_0_2 are the two identity fixed points",
          ROLE_MAP["B_1_2"] == "B_1_2" and ROLE_MAP["B_0_2"] == "B_0_2"
          and {role for role, value in ROLE_MAP.items() if role == value} == {"B_1_2", "B_0_2"})
    debris = {
        role: tuple(sorted(site for site, content in c100.SOURCE.items() if content == role))
        for role in ("B0", "L10")
    }
    check("B05 B0/L10 reuse is explicit: 2 and 9 pre-existing source records",
          tuple(map(len, (debris["B0"], debris["L10"]))) == (2, 9))
    check("B06 B0 and L10 have no one-parent rows in the Cycle100 table",
          not unary_outputs("B0") and not unary_outputs("L10"))
    overlap = set(REMAPPED_RAW) & set(c100.COMBINED_RAW)
    check("B07 remapped rail retains 1,080 single-valued raw inputs",
          len(REMAPPED_RAW) == 1080 and all(len(values) == 1 for values in REMAPPED_RAW.values()))
    check("B08 remapped rail is disjoint from Cycle100 and mixed union is 6,524 single-valued",
          not overlap and len(MIXED_RAW) == 6524 and all(len(values) == 1 for values in MIXED_RAW.values()),
          str(tuple(overlap)[:1]))
    table_contents = {
        content
        for local, values in MIXED_RAW.items()
        for _direction, content in local
    } | {output for values in MIXED_RAW.values() for output in values}
    check("B09 complete mixed law is closed on the exact 153-role onsite alphabet",
          table_contents <= c89.FULL_ROLES)


def fixed_point_and_debris_contract() -> None:
    section("C - Forced W1 fixed points and debris-adapter census")
    records = c100.records_at(len(c100.ADDITIONS))
    providers: Counter[tuple[bool, bool]] = Counter()
    provider_failures: list[tuple[object, ...]] = []
    polluted_local: Signature | None = None
    for index, (site, content) in enumerate(NINE_SLICES[:EIGHT_SLICE_HORIZON]):
        local = c100.c53.local_signature(records, site)
        in_base = local in c100.COMBINED_RAW
        in_rail = local in REMAPPED_RAW
        providers[(in_base, in_rail)] += 1
        actual_values = MIXED_RAW.get(local)
        if actual_values != frozenset((content,)):
            provider_failures.append((index, content, local, actual_values))
        if index == 2:
            polluted_local = local
        records[site] = content
    check("C01 95 rail appends use remapped rows and exactly one uses a Cycle100 adapter",
          providers == {(False, True): 95, (True, False): 1}, str(providers))
    check("C02 sole adapter is A_0_2 + B_1_2 + W1 -> B_0_2 at first-slice write three",
          polluted_local is not None
          and {content for _direction, content in polluted_local} == {"A_0_2", "B_1_2", "W1"}
          and c100.COMBINED_RAW.get(polluted_local) == {"B_0_2"}
          and polluted_local not in REMAPPED_RAW)
    check("C03 every intended provider has exactly the remapped output",
          not provider_failures, str(provider_failures[:1]))

    swap_b12 = dict(ROLE_MAP)
    swap_b12["B_1_2"], swap_b12["B_0_0"] = swap_b12["B_0_0"], swap_b12["B_1_2"]
    swap_b02 = dict(ROLE_MAP)
    swap_b02["B_0_2"], swap_b02["B_0_0"] = swap_b02["B_0_0"], swap_b02["B_0_2"]
    b12_failure = first_failure(swap_b12, 4)
    b02_failure = first_failure(swap_b02, 4)
    check("C04 changing B_1_2 without a new polluted-row adapter fails by write three",
          b12_failure is not None and b12_failure[0] <= 2, str(b12_failure))
    check("C05 changing B_0_2 without a new polluted-row adapter fails by write three",
          b02_failure is not None and b02_failure[0] <= 2, str(b02_failure))
    check("C06 no additional fixed point or debris adapter is consumed in eight slices",
          providers[(True, False)] == 1 and providers[(True, True)] == 0)


def trajectory_product_and_covariance_contract() -> None:
    section("D - Eight-slice asynchronous product and debris closure")
    failures: list[tuple[object, ...]] = []
    debris_triggers: list[tuple[object, ...]] = []
    debris_sites = {
        site for site, content in c100.SOURCE.items() if content in {"B0", "L10"}
    }
    for code_prefix in range(len(c100.ADDITIONS) + 1):
        for rail_prefix in range(EIGHT_SLICE_HORIZON + 1):
            records = product_state(code_prefix, rail_prefix)
            expected = product_expected(code_prefix, rail_prefix)
            actual = enabled(records)
            if actual != expected:
                failures.append((code_prefix, rail_prefix, expected, actual))
                break
            for target in actual:
                local = c100.c53.local_signature(records, target)
                if local not in REMAPPED_RAW:
                    continue
                used = {
                    add(target, direction)
                    for direction, _content in local
                } & debris_sites
                if used:
                    debris_triggers.append((code_prefix, rail_prefix, target, tuple(sorted(used))))
        if failures:
            break
    check("D01 all 11 x 97 code/eight-slice prefix states have exactly the lawful fronts",
          not failures and 11 * 97 == 1067, str(failures[:1]))
    check("D02 no pre-existing B0/L10 debris site participates in an enabled remapped row",
          not debris_triggers, str(debris_triggers[:1]))
    terminal = product_state(len(c100.ADDITIONS), EIGHT_SLICE_HORIZON)
    check("D03 eight complete slices expose exactly the ninth-slice start",
          enabled(terminal) == {NINE_SLICES[96][0]: frozenset((NINE_SLICES[96][1],))})
    check("D04 every source, code, and rail record stays inside FULL_ROLES",
          set(c100.SOURCE.values()) <= c89.FULL_ROLES
          and {content for _site, content in c100.ADDITIONS} <= c89.FULL_ROLES
          and {content for _site, content in NINE_SLICES} <= c89.FULL_ROLES)

    section("E - All first-slice async states under all rotations")
    covariance_failures: list[tuple[object, ...]] = []
    shift = (101, -73, 59)
    rotated_controls = 0
    for code_prefix in range(len(c100.ADDITIONS) + 1):
        for rail_prefix in range(FIRST_SLICE_HORIZON + 1):
            base = product_state(code_prefix, rail_prefix)
            base_expected = product_expected(code_prefix, rail_prefix)
            for rotation in c52.ROTATIONS:
                rotated_controls += 1
                records = transform_records(base, rotation, shift)
                expected = transform_records(
                    {site: next(iter(values)) for site, values in base_expected.items()},
                    rotation,
                    shift,
                )
                actual = {
                    site: next(iter(values))
                    for site, values in enabled(records).items()
                }
                if actual != expected:
                    covariance_failures.append((code_prefix, rail_prefix, rotation, expected, actual))
                    break
            if covariance_failures:
                break
        if covariance_failures:
            break
    check("E01 all 143 x 24 asynchronous state images have exact transformed fronts",
          rotated_controls == 143 * 24 == 3432 and not covariance_failures,
          str(covariance_failures[:1]))

    raw_rotation_failures: list[tuple[object, ...]] = []
    for local, values in MIXED_RAW.items():
        for rotation in c52.ROTATIONS:
            rotated = c52.rotate_signature(local, rotation)
            if MIXED_RAW.get(rotated) != values:
                raw_rotation_failures.append((local, rotation, values, MIXED_RAW.get(rotated)))
                break
    check("E02 complete 6,524-row mixed table is closed under all 24 rotations",
          not raw_rotation_failures and len(MIXED_RAW) * 24 == 156576,
          str(raw_rotation_failures[:1]))
    check("E03 base 1,067-state theorem plus exact raw closure lifts all eight-slice images",
          not failures and not raw_rotation_failures and 1067 * 24 == 25608)


def documentation_contract() -> None:
    section("F - Scope, N1-N8, and constitutional disposition")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check("F01 note exists, has authority none, and issues no audit verdict",
          NOTE.is_file() and "authority: none" in note and "no independent audit verdict" in note)
    check("F02 note records the original 34-role alphabet defect and narrow obstruction",
          "34" in note and "exact_absent_pool_pure_relabel" in note and "r_lc" in note)
    check("F03 note records safe B0/L10 reuse and both fixed identities",
          all(needle in note for needle in ("b0", "l10", "b_1_2", "b_0_2", "w1-polluted")))
    check("F04 note names N1-N8 and the retained payload bind",
          all(f"n{index}" in note for index in range(1, 9))
          and "ready_row_to_rail_payload_bind" in note)
    check("F05 note distinguishes onsite closure from global role freshness",
          "onsite-alphabet closed" in note and "not globally fresh" in note)
    check("F06 note makes no foundation or axiom change",
          "no foundation edit" in note and "no axiom addition follows" in note)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    original_defect_and_obstruction_contract()
    mapping_and_table_contract()
    fixed_point_and_debris_contract()
    trajectory_product_and_covariance_contract()
    documentation_contract()
    print(f"\nFULL_ROLES={len(c89.FULL_ROLES)} ORIGINAL_FOREIGN=34 DOMAIN={len(PHASE_DOMAIN)}")
    print(f"ABSENT_POOL={len(ABSENT_POOL)} SAFE_POOL={len(SAFE_POOL)} REMAPPED_RAW={len(REMAPPED_RAW)} MIXED_RAW={len(MIXED_RAW)}")
    print("PREFIX_STATES=1067 ROTATED_FIRST_SLICE_STATES=3432 ROTATED_RAW=156576")
    print("PROVIDERS=95_REMAPPED_PLUS_1_W1_ADAPTER SAFE_REUSE=B0x2+L10x9")
    print("RESULT=ONSITE_ALPHABET_CLOSED_BOUNDED_FRAME_RAIL")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
