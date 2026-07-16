#!/usr/bin/env python3
"""Cycle 172: bounded matter-lane kinematics of the recurrent row carrier.

The Cycle-175 replacement law is extended through one additional recurrent
period.  The probe asks whether the permanent copy trail contains one exact
payload lineage and one active endpoint, derives its causal-layer propagation
ratio, composes two separated carriers, and preflights a first local
two-lineage junction.

This runner has no authority.  It edits no foundation, axiom, primitive,
registry, policy, audit, queue, predecessor, commit, push, or PR surface.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path

import autonomous_signed_row_recurrent_sidecar_cycle171_2026_07_16 as c171
import clean_row_alphabet_component_replacement_cycle175_2026_07_16 as c175


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "RECURRENT_CARRIER_MATTER_KINEMATICS_CYCLE172_NOTE_2026-07-16.md"
)

b = c171.b
c141 = c171.c141
cell = c171.cell
c53 = c171.c53
Coord = tuple[int, int, int]

ROW_ROLES = tuple(c175.NEW_ROW_ROLES)
PERIODS = 4
SEED_X = 7
COPY_X = tuple(range(8, 10 + 4 * PERIODS))
GENERATION_X = tuple(7 + 4 * generation for generation in range(PERIODS + 1))
PAYLOAD_YZ = c171.PAYLOAD_YZ
GUIDE_YZ = c171.GUIDE_YZ
GUIDE_ROLE = c171.GUIDE_ROLE
REAR_STOP_ROLE = c171.REAR_STOP_ROLE
PARALLEL_OFFSET = (0, 2_000, 0)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def shift(site: Coord, offset: Coord) -> Coord:
    return add(site, offset)


def payload_site(x: int) -> Coord:
    return c141.transform_site(cell.site(x, PAYLOAD_YZ))


def guide_site(x: int) -> Coord:
    return c141.transform_site(cell.site(x, GUIDE_YZ))


def completed_boundary() -> dict[Coord, str]:
    return c171.completed_boundary()


def rail_extension() -> dict[Coord, str]:
    outputs: dict[Coord, str] = {}
    old = "B"
    phases = ("C", "D", "A", "B") * PERIODS
    for x, new in zip(range(10, 10 + 4 * PERIODS), phases, strict=True):
        for yz in cell.PATHS[(old, new)]:
            outputs[cell.site(x, yz)] = cell.CONTENT[(new, yz)]
        for yz in cell.EXTRA_ORDERS[new]:
            outputs[cell.site(x, yz)] = cell.CONTENT[(new, yz)]
        old = new

    for root_x in GENERATION_X[1:]:
        outputs[cell.site(root_x, cell.NOTCH_YZ)] = cell.OZ
        outputs[cell.site(root_x + 1, cell.NOTCH_YZ)] = cell.H1
        outputs[cell.site(root_x + 2, cell.NOTCH_YZ)] = cell.HELPER_CONTENT
        outputs[cell.site(root_x, (-1, 1))] = "R_LB"
        outputs[cell.site(root_x, (-2, 1))] = "R_C22"
        outputs[cell.site(root_x, (-3, 1))] = "J1"
    return {
        c141.transform_site(site): role
        for site, role in outputs.items()
    }


RAIL_EXTENSION = rail_extension()


def physical_root_sidecars() -> dict[Coord, str]:
    outputs = {}
    for period in range(1, PERIODS + 1):
        dx = -4 * period
        for site, role in (*b.SIDECAR_TRUNK, *b.SIDECAR_SHELL):
            outputs[(site[0] + dx, site[1], site[2])] = role
    return outputs


PHYSICAL_ROOT_SIDECARS = physical_root_sidecars()


def source(row_role: str) -> dict[Coord, str]:
    records = completed_boundary()
    records[payload_site(SEED_X)] = row_role
    records[guide_site(SEED_X)] = GUIDE_ROLE
    records[guide_site(SEED_X - 1)] = REAR_STOP_ROLE
    return records


def outputs(row_role: str) -> dict[Coord, str]:
    return {
        **RAIL_EXTENSION,
        **PHYSICAL_ROOT_SIDECARS,
        **{guide_site(x): GUIDE_ROLE for x in COPY_X},
        **{payload_site(x): row_role for x in COPY_X},
    }


def exits() -> dict[Coord, frozenset[str]]:
    next_x = 10 + 4 * PERIODS
    next_yz = cell.PATHS[("B", "C")][0]
    result = {
        c141.transform_site(cell.site(next_x, next_yz)):
        frozenset((cell.CONTENT[("C", next_yz)],)),
    }
    for site, values in b.BIND_IGNORED.items():
        result[(site[0] - 4 * PERIODS, site[1], site[2])] = values
    return result


EXITS = exits()


CARRIER_TABLE = c171.canonical_sidecar_table(ROW_ROLES)
CARRIER_RAW = cell.merge_raw(*(
    cell.raw_orbit(signature, output)
    for signature, output in CARRIER_TABLE.items()
))
FULL_RAW = cell.merge_raw(c175.CANDIDATE169_RAW, CARRIER_RAW)
RAW_CONFLICTS = {
    signature: values
    for signature, values in FULL_RAW.items()
    if len(values) != 1
}


def translated(records: dict[Coord, str], offset: Coord) -> dict[Coord, str]:
    return {
        shift(site, offset): role
        for site, role in records.items()
    }


def translated_values(
    values: dict[Coord, frozenset[str]],
    offset: Coord,
) -> dict[Coord, frozenset[str]]:
    return {
        shift(site, offset): roles
        for site, roles in values.items()
    }


def direct_parents(
    initial: dict[Coord, str],
    expected: dict[Coord, str],
    dependencies: dict[Coord, frozenset[Coord]],
) -> dict[Coord, frozenset[Coord]]:
    return {
        target: frozenset(
            set(parents)
            | {
                neighbor
                for direction in c53.DIRECTIONS
                if (
                    (neighbor := add(target, direction))
                    in initial
                )
            }
        )
        for target, parents in dependencies.items()
    }


def lineage_certificate(certificate, initial, expected):
    dependencies = certificate["dependencies"]
    parents = direct_parents(initial, expected, dependencies)
    payloads = tuple(payload_site(x) for x in range(SEED_X, COPY_X[-1] + 1))
    payload_set = set(payloads)
    row_parent = {}
    children = {site: [] for site in payloads}
    for x in COPY_X:
        target = payload_site(x)
        candidates = tuple(sorted(parents[target] & payload_set))
        row_parent[target] = candidates
        for parent in candidates:
            children[parent].append(target)

    degree_failures = []
    for index, site in enumerate(payloads):
        expected_parents = 0 if index == 0 else 1
        expected_children = 0 if index == len(payloads) - 1 else 1
        observed_parents = 0 if index == 0 else len(row_parent[site])
        observed_children = len(children[site])
        if (
            observed_parents != expected_parents
            or observed_children != expected_children
        ):
            degree_failures.append(
                (
                    site,
                    observed_parents,
                    observed_children,
                    expected_parents,
                    expected_children,
                )
            )

    depth = c171.causal_depths(dependencies)
    generation_depths = tuple(
        0 if x == SEED_X else depth[payload_site(x)]
        for x in GENERATION_X
    )
    depth_increments = tuple(
        right - left
        for left, right in zip(generation_depths, generation_depths[1:])
    )
    displacement = tuple(
        sum(
            abs(a - b)
            for a, b in zip(payload_site(left), payload_site(right))
        )
        for left, right in zip(GENERATION_X, GENERATION_X[1:])
    )
    return {
        "payloads": payloads,
        "row_parent": row_parent,
        "children": children,
        "degree_failures": tuple(degree_failures),
        "generation_depths": generation_depths,
        "depth_increments": depth_increments,
        "displacement": displacement,
        "startup_ratio": Fraction(displacement[0], depth_increments[0]),
        "steady_ratios": tuple(
            Fraction(distance, layers)
            for distance, layers in zip(
                displacement[1:],
                depth_increments[1:],
                strict=True,
            )
        ),
    }


def parallel_certificate(left_role: str, right_role: str):
    left_source = source(left_role)
    left_outputs = outputs(left_role)
    right_source = translated(source(right_role), PARALLEL_OFFSET)
    right_outputs = translated(outputs(right_role), PARALLEL_OFFSET)
    combined_source = {**left_source, **right_source}
    combined_outputs = {**left_outputs, **right_outputs}
    combined_exits = {
        **EXITS,
        **translated_values(EXITS, PARALLEL_OFFSET),
    }
    certificate = c171.causal_certificate(
        combined_source,
        combined_outputs,
        combined_exits,
    )
    return (
        certificate,
        combined_source,
        combined_outputs,
        combined_exits,
    )


def junction_census(certificate, initial, expected, row_role: str):
    target = payload_site(GENERATION_X[1])
    parents = direct_parents(
        initial,
        expected,
        certificate["dependencies"],
    )[target]
    premise = {
        neighbor: initial[neighbor]
        for direction in c53.DIRECTIONS
        if (neighbor := add(target, direction)) in initial
    }
    premise.update({
        parent: expected[parent]
        for parent in certificate["dependencies"][target]
    })
    baseline = FULL_RAW.get(c53.local_signature(premise, target))
    free = tuple(
        add(target, direction)
        for direction in c53.DIRECTIONS
        if add(target, direction) not in premise
    )

    bare = Counter()
    bare_examples = {}
    one_context = Counter()
    one_context_examples = {}
    guide_substitution = Counter()
    guide_substitution_examples = {}
    phase_substitution = Counter()
    phase_substitution_examples = {}
    two_context = Counter()
    two_context_examples = {}
    existing_roles = tuple(sorted(cell.FULL_ROLES))

    def category(observed):
        return (
            "wanted"
            if observed == frozenset((row_role,))
            else "row"
            if observed is not None
            and set(observed) <= set(ROW_ROLES)
            else "quiet"
            if observed is None
            else "other"
        )

    guide_parent = next(
        site for site, role in premise.items()
        if role == GUIDE_ROLE
    )
    phase_parent = next(
        site for site in premise
        if site not in {guide_parent, payload_site(GENERATION_X[1] - 1)}
    )
    for incoming_site in free:
        remaining = tuple(site for site in free if site != incoming_site)
        for incoming_role in ROW_ROLES:
            records = {**premise, incoming_site: incoming_role}
            observed = FULL_RAW.get(c53.local_signature(records, target))
            observed_category = category(observed)
            bare[observed_category] += 1
            bare_examples.setdefault(observed_category, (
                incoming_site,
                incoming_role,
                observed,
            ))

            for context_site in remaining:
                for context_role in existing_roles:
                    contextual = {
                        **records,
                        context_site: context_role,
                    }
                    observed = FULL_RAW.get(
                        c53.local_signature(contextual, target)
                    )
                    observed_category = category(observed)
                    one_context[observed_category] += 1
                    one_context_examples.setdefault(observed_category, (
                        incoming_site,
                        incoming_role,
                        context_site,
                        context_role,
                        observed,
                    ))

            for substitute_role in existing_roles:
                guide_trial = {
                    **records,
                    guide_parent: substitute_role,
                }
                observed = FULL_RAW.get(
                    c53.local_signature(guide_trial, target)
                )
                observed_category = category(observed)
                guide_substitution[observed_category] += 1
                guide_substitution_examples.setdefault(
                    observed_category,
                    (
                        incoming_site,
                        incoming_role,
                        substitute_role,
                        observed,
                    ),
                )

                phase_trial = {
                    **records,
                    phase_parent: substitute_role,
                }
                observed = FULL_RAW.get(
                    c53.local_signature(phase_trial, target)
                )
                observed_category = category(observed)
                phase_substitution[observed_category] += 1
                phase_substitution_examples.setdefault(
                    observed_category,
                    (
                        incoming_site,
                        incoming_role,
                        substitute_role,
                        observed,
                    ),
                )

            left_context, right_context = remaining
            for left_role in existing_roles:
                for right_role in existing_roles:
                    contextual = {
                        **records,
                        left_context: left_role,
                        right_context: right_role,
                    }
                    observed = FULL_RAW.get(
                        c53.local_signature(contextual, target)
                    )
                    observed_category = category(observed)
                    two_context[observed_category] += 1
                    two_context_examples.setdefault(
                        observed_category,
                        (
                            incoming_site,
                            incoming_role,
                            left_context,
                            left_role,
                            right_context,
                            right_role,
                            observed,
                        ),
                    )
    return {
        "target": target,
        "premise": premise,
        "baseline": baseline,
        "free": free,
        "bare": bare,
        "bare_examples": bare_examples,
        "one_context": one_context,
        "one_context_examples": one_context_examples,
        "guide_parent": guide_parent,
        "phase_parent": phase_parent,
        "guide_substitution": guide_substitution,
        "guide_substitution_examples": guide_substitution_examples,
        "phase_substitution": phase_substitution,
        "phase_substitution_examples": phase_substitution_examples,
        "two_context": two_context,
        "two_context_examples": two_context_examples,
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    old_full_raw = c171.FULL_RAW
    c171.FULL_RAW = FULL_RAW
    try:
        print("AUTHORITY AND LAW")
        check("Cycle-172 review note exists", NOTE.is_file())
        check(
            "the Cycle-175 union plus recurrent carrier remains deterministic",
            not RAW_CONFLICTS
            and len(CARRIER_TABLE) == 132
            and len(CARRIER_RAW) == 3_168
            and len(FULL_RAW) == 104_876,
            (
                len(CARRIER_TABLE),
                len(CARRIER_RAW),
                len(FULL_RAW),
                len(RAW_CONFLICTS),
            ),
        )

        print("\nFOUR-PERIOD ALL-32 CARRIER")
        certificates = {}
        shape_counts = Counter()
        failures = {}
        for role in ROW_ROLES:
            initial = source(role)
            expected = outputs(role)
            certificate = c171.causal_certificate(
                initial,
                expected,
                EXITS,
            )
            certificates[role] = certificate
            if not certificate["ok"]:
                failures[role] = certificate
                continue
            shape_counts[(
                certificate["minimum"]["states"],
                certificate["edge_checks"]["edges"],
                len(certificate["unordered"]),
                len(certificate["minimum"]["terminal"]),
            )] += 1
        check(
            "all 32 values close through the fourth recurrent generation",
            not failures
            and len(certificates) == 32
            and len(shape_counts) == 1,
            (shape_counts, tuple(failures)[:3]),
        )

        representative = "ARM"
        representative_source = source(representative)
        representative_outputs = outputs(representative)
        representative_certificate = certificates[representative]

        print("\nLINEAGE AND CAUSAL KINEMATICS")
        lineage = lineage_certificate(
            representative_certificate,
            representative_source,
            representative_outputs,
        )
        check(
            "the permanent payload trail has one exact parent-child lineage and one endpoint",
            not lineage["degree_failures"]
            and len(lineage["payloads"]) == 19
            and sum(not children for children in lineage["children"].values()) == 1,
            (
                lineage["degree_failures"],
                len(lineage["payloads"]),
                tuple(
                    site
                    for site, children in lineage["children"].items()
                    if not children
                ),
            ),
        )
        check(
            "the row value is conserved while the number of payload records grows",
            all(
                representative_outputs.get(site, representative) == representative
                for site in lineage["payloads"]
            )
            and len(lineage["payloads"]) > 1,
            len(lineage["payloads"]),
        )
        check(
            "the fourth generation confirms a steady 4-per-52 causal-layer ratio",
            lineage["generation_depths"] == (0, 19, 71, 123, 175)
            and lineage["depth_increments"] == (19, 52, 52, 52)
            and lineage["displacement"] == (4, 4, 4, 4)
            and lineage["startup_ratio"] == Fraction(4, 19)
            and lineage["steady_ratios"]
            == (Fraction(1, 13),) * 3,
            lineage,
        )

        print("\nSEPARATED PARALLEL CARRIERS")
        (
            parallel,
            parallel_source,
            parallel_outputs,
            parallel_exits,
        ) = parallel_certificate("ARM", "Z0")
        check(
            "two separated unequal carriers close under one common law",
            parallel["ok"]
            and len(parallel_outputs) == 2 * len(representative_outputs)
            and len(parallel["dependencies"]) == len(parallel_outputs)
            and not parallel["unordered"]
            and parallel["minimum"]["terminal"] == parallel_exits
            and parallel["maximum"]["terminal"] == parallel_exits,
            (
                parallel.get("discovery", {}).get("error"),
                len(parallel_source),
                len(parallel_outputs),
                len(parallel.get("unordered", ())),
            ),
        )
        single_edges = representative_certificate["edge_checks"]["edges"]
        check(
            "the separated causal graphs factor with no cross-carrier parent edge",
            parallel["edge_checks"]["edges"] == 2 * single_edges
            and all(
                not (
                    (parent[1] < 1_000 <= target[1])
                    or (target[1] < 1_000 <= parent[1])
                )
                for target, parents in parallel["dependencies"].items()
                for parent in parents
            ),
            (single_edges, parallel["edge_checks"]["edges"]),
        )

        print("\nFIRST LOCAL COLLISION/JUNCTION PREFLIGHT")
        junction = junction_census(
            representative_certificate,
            representative_source,
            representative_outputs,
            representative,
        )
        check(
            "the unperturbed generation target has its exact carrier output",
            junction["baseline"] == frozenset((representative,)),
            junction["baseline"],
        )
        check(
            "a second bare incoming row never preserves the carrier write",
            junction["bare"]["wanted"] == 0
            and sum(junction["bare"].values()) == 3 * 32,
            (junction["bare"], junction["bare_examples"]),
        )
        check(
            "one additional existing context record does not supply a row junction",
            junction["one_context"]["wanted"] == 0
            and junction["one_context"]["row"] == 0
            and sum(junction["one_context"].values())
            == 3 * 32 * 2 * len(cell.FULL_ROLES),
            (
                junction["one_context"],
                junction["one_context_examples"],
            ),
        )
        check(
            "replacing either carrier control with any existing role supplies no row junction",
            junction["guide_substitution"]["wanted"] == 0
            and junction["guide_substitution"]["row"] == 0
            and junction["phase_substitution"]["wanted"] == 0
            and junction["phase_substitution"]["row"] == 0
            and sum(junction["guide_substitution"].values())
            == 3 * 32 * len(cell.FULL_ROLES)
            and sum(junction["phase_substitution"].values())
            == 3 * 32 * len(cell.FULL_ROLES),
            (
                junction["guide_substitution"],
                junction["guide_substitution_examples"],
                junction["phase_substitution"],
                junction["phase_substitution_examples"],
            ),
        )
        check(
            "filling both remaining open faces with existing roles supplies no row junction",
            junction["two_context"]["wanted"] == 0
            and junction["two_context"]["row"] == 0
            and sum(junction["two_context"].values())
            == 3 * 32 * len(cell.FULL_ROLES) ** 2,
            (
                junction["two_context"],
                junction["two_context_examples"],
            ),
        )

        print("\nSCOPE")
        note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
        check(
            "review note carries N1-N8 and denies a particle or axiom claim",
            all(f"### N{index}" in note for index in range(1, 9))
            and "not a particle-identity theorem" in note
            and "No axiom addition follows" in note
            and "one tested junction interface" in note
            and "extensional nonorthogonal M2 labels" in note
            and "orthogonal spatial implementation" in note,
        )

        print("\nACCOUNTING")
        print("ROW_ROLES", ROW_ROLES)
        print("DYNAMIC_RECORDS", len(representative_outputs))
        print(
            "REPRESENTATIVE_GRAPH",
            representative_certificate["minimum"]["states"],
            representative_certificate["edge_checks"]["edges"],
            representative_certificate["minimum"]["max_frontier"],
            representative_certificate["maximum"]["max_frontier"],
        )
        print("LINEAGE", lineage)
        print(
            "PARALLEL_GRAPH",
            parallel["minimum"]["states"],
            parallel["edge_checks"]["edges"],
            parallel["minimum"]["max_frontier"],
            parallel["maximum"]["max_frontier"],
        )
        print("JUNCTION", junction)
        print("PASS", PASS, "FAIL", FAIL)
        print(
            "RESULT",
            "BOUNDED_CARRIER_LINEAGE_KINEMATICS"
            if FAIL == 0
            else "CYCLE172_OPEN",
        )
        return int(FAIL != 0)
    finally:
        c171.FULL_RAW = old_full_raw


if __name__ == "__main__":
    raise SystemExit(main())
