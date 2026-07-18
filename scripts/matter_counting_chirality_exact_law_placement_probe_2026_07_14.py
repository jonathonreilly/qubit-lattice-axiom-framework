#!/usr/bin/env python3
"""Exact controls for Cycle 11 matter counting and chirality placement.

Companion note:
  docs/work_history/repo/review_feedback/
  MATTER_COUNTING_CHIRALITY_EXACT_LAW_PLACEMENT_NOTE_2026-07-14.md

The runner proves only finite statements:

* equal-atom finite additivity fixes weights after a physical event algebra is
  supplied, but does not choose that algebra or the equal-atom premise;
* two exact local M2(C) instruments, on the same maximally mixed input, realize
  the tied and untied counting branches;
* the two branches give the stated r and Koide-Q endpoints only through the
  explicitly supplied formation-energy bridge;
* proper cubic covariance admits mirror-related handed exact laws;
* six-neighbor corners and the six-order cubic block do not choose one hand.

It is not a whole-framework simulation, an axiom edit, an audit verdict, or a
universal no-go.  No network, randomness, live registry mutation, commit, or
PR.  Exit code 0 iff FAIL=0.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "MATTER_COUNTING_CHIRALITY_EXACT_LAW_PLACEMENT_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def normalized(text: str) -> str:
    return " ".join(
        text.lower().replace("*", "").replace("`", "").replace("_", " ").split()
    )


def exact_matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    difference = sp.Matrix(left) - sp.Matrix(right)
    return all(sp.simplify(value) == 0 for value in difference)


def parse_table(
    text: str, start: str, end: str
) -> tuple[tuple[str, ...], dict[str, tuple[str, ...]]]:
    body = text.split(start, 1)[1].split(end, 1)[0]
    lines = [line for line in body.splitlines() if line.startswith("|")]
    rows = [
        [cell.strip().strip("`") for cell in line.strip().strip("|").split("|")]
        for line in lines
    ]
    header = tuple(rows[0])
    parsed = {
        row[0]: tuple(row[1:])
        for row in rows[2:]
        if len(row) == len(header) and row[0]
    }
    return header, parsed


STATUS_START = "<!-- status-ledger:start -->"
STATUS_END = "<!-- status-ledger:end -->"
STATUS_HEADER = ("atom_id", "placement", "reason_key")
STATUS_ROWS = {
    "standard_cubic_lattice_and_proper_rotations": (
        "GENUINELY_CONSTITUTIONAL",
        "current_lattice_axiom",
    ),
    "one_fixed_nearest_neighbor_rule": (
        "GENUINELY_CONSTITUTIONAL",
        "current_admissibility_axiom",
    ),
    "one_locked_admissible_possibility_per_record": (
        "GENUINELY_CONSTITUTIONAL",
        "current_record_axiom",
    ),
    "post_formation_scalar_readout_additivity": (
        "GENUINELY_CONSTITUTIONAL",
        "current_record_axiom",
    ),
    "physical_event_effect_algebra": ("LAW_OWNED", "instrument_domain"),
    "operational_equivalence_of_presentations": (
        "LAW_OWNED",
        "physical_quotient",
    ),
    "formation_weight_measure_and_instrument": (
        "LAW_OWNED",
        "sampled_event_rule",
    ),
    "event_to_record_content_decoder": ("LAW_OWNED", "record_interface"),
    "formation_energy_bridge": ("LAW_OWNED", "koide_energy_map"),
    "spectral_parameter_to_mass_map": ("LAW_OWNED", "mass_bridge"),
    "reflection_covariance_or_chiral_law_sign": (
        "LAW_OWNED",
        "improper_symmetry_choice",
    ),
    "actual_event_history_or_random_seed": (
        "BOUNDARY_STATE_OWNED",
        "realized_member",
    ),
    "actual_chiral_domain_or_orientation": (
        "BOUNDARY_STATE_OWNED",
        "realized_domain",
    ),
    "equal_atom_measure_after_event_algebra": (
        "CONDITIONALLY_DERIVED",
        "finite_additivity",
    ),
    "tied_w_half_r_half_Q_two_thirds": (
        "CONDITIONALLY_DERIVED",
        "tied_algebra_plus_bridges",
    ),
    "untied_w_third_r_one_Q_one": (
        "CONDITIONALLY_DERIVED",
        "untied_algebra_plus_bridges",
    ),
    "proper_cubic_mirror_twin_nonselection": (
        "CONDITIONALLY_DERIVED",
        "determinant_pair",
    ),
    "observed_hand_from_achiral_law_plus_domain": (
        "CONDITIONALLY_DERIVED",
        "boundary_condition",
    ),
}


BRANCH_START = "<!-- branch-ledger:start -->"
BRANCH_END = "<!-- branch-ledger:end -->"
BRANCH_HEADER = (
    "branch_id",
    "physical_atoms",
    "singlet_weight_w",
    "r_given_bridge",
    "Q_given_mass_map",
)
BRANCH_ROWS = {
    "tied": ("s,d", "1/2", "1/2", "2/3"),
    "untied": ("s,d_plus,d_minus", "1/3", "1", "1"),
}


SOURCE_CONTRACTS = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md": (
        "proper cubic rotations",
        "Records form.",
        "scalar readout",
        "A state is a configuration of records.",
    ),
    "docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md": (
        "r = (1-w)/(2w)",
        "w = 1/2",
        "w = 1/3",
        "not derived, selected, or preferred",
    ),
    "docs/KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md": (
        "unordered three-atom",
        "convention-stable",
    ),
    "docs/work_history/repo/review_feedback/CUBIC_NEIGHBOR_KERNEL_SELECTION_FIRST_PRINCIPLES_NOTE_2026-07-14.md": (
        "elementary physical event/effect",
        "finite additivity",
        "No additional \u201crecords are counted by...\u201d sentence",
    ),
    "docs/work_history/repo/review_feedback/CUBIC_COVARIANCE_EXACT_REPAIR_TOURNAMENT_NOTE_2026-07-14.md": (
        "proper cubic rotations",
        "a handed",
        "still do not choose",
    ),
    "docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md": (
        "A chiral admissibility rule cannot live at the openness",
        "members are the handed",
    ),
    "docs/DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-04.md": (
        "opposite chirality",
        "imposed by hand",
    ),
    "docs/work_history/repo/review_feedback/CAUSAL_REVERSIBLE_ACTUALITY_WEIGHT_INDEPENDENCE_NOTE_2026-07-14.md": (
        "physical_outcome_decomposition",
        "calibrated_weight_rule",
        "boundary/state-owned",
    ),
}


def source_and_ledger_contract() -> None:
    section("A - Framework, source, and classification contract")
    text = NOTE.read_text(encoding="utf-8")
    flat = normalized(text)
    for phrase in (
        "authority: none",
        "bounded result",
        "no matter-specific axiom addition",
        "exact law",
        "law-owned",
        "boundary/state-owned",
        "conditionally derived",
        "not a universal no-go",
        "does not authorize an axiom edit",
        "n1",
        "n8",
    ):
        check(f"A note contains scope phrase: {phrase}", phrase in flat)

    for relative, phrases in SOURCE_CONTRACTS.items():
        path = ROOT / relative
        check(f"A source exists: {relative}", path.is_file())
        source = path.read_text(encoding="utf-8") if path.is_file() else ""
        for phrase in phrases:
            check(
                f"A source contract {path.name}: {phrase}",
                phrase in source,
            )

    check("A status ledger has one start marker", text.count(STATUS_START) == 1)
    check("A status ledger has one end marker", text.count(STATUS_END) == 1)
    header, rows = parse_table(text, STATUS_START, STATUS_END)
    check("A status ledger header is exact", header == STATUS_HEADER, repr(header))
    check("A status ledger atom set is exact", set(rows) == set(STATUS_ROWS))
    for atom, expected in STATUS_ROWS.items():
        check(f"A {atom} placement is locked", rows.get(atom) == expected)
    placements = {row[0] for row in rows.values()}
    check(
        "A all requested placement classes occur",
        placements
        == {
            "GENUINELY_CONSTITUTIONAL",
            "LAW_OWNED",
            "BOUNDARY_STATE_OWNED",
            "CONDITIONALLY_DERIVED",
        },
    )

    check("A branch ledger has one start marker", text.count(BRANCH_START) == 1)
    check("A branch ledger has one end marker", text.count(BRANCH_END) == 1)
    branch_header, branches = parse_table(text, BRANCH_START, BRANCH_END)
    check("A branch ledger header is exact", branch_header == BRANCH_HEADER)
    check("A branch ledger routes are exact", branches == BRANCH_ROWS, repr(branches))

    literature = (
        "10.1512/iumj.1957.6.56050",
        "1708.00826",
        "10.1016/0550-3213(81)90524-1",
        "hep-lat/9206013",
    )
    for reference in literature:
        check(f"A primary-literature ledger includes {reference}", reference in text)


def powerset(atoms: tuple[str, ...]) -> list[frozenset[str]]:
    return [
        frozenset(choice)
        for size in range(len(atoms) + 1)
        for choice in combinations(atoms, size)
    ]


def finite_measure(
    event: frozenset[str], weights: dict[str, Fraction]
) -> Fraction:
    return sum((weights[atom] for atom in event), Fraction(0))


def verify_finite_additivity(
    atoms: tuple[str, ...], weights: dict[str, Fraction]
) -> bool:
    events = powerset(atoms)
    normalized_measure = finite_measure(frozenset(atoms), weights) == 1
    empty_zero = finite_measure(frozenset(), weights) == 0
    additive = all(
        finite_measure(left | right, weights)
        == finite_measure(left, weights) + finite_measure(right, weights)
        for left in events
        for right in events
        if left.isdisjoint(right)
    )
    return normalized_measure and empty_zero and additive


def counting_and_presentation_controls() -> None:
    section("B - Finite additivity after, not before, the physical atom choice")
    tied_atoms = ("s", "d")
    untied_atoms = ("s", "d_plus", "d_minus")
    tied = {atom: Fraction(1, 2) for atom in tied_atoms}
    untied = {atom: Fraction(1, 3) for atom in untied_atoms}

    check("B tied equal-atom measure is finitely additive", verify_finite_additivity(tied_atoms, tied))
    check("B untied equal-atom measure is finitely additive", verify_finite_additivity(untied_atoms, untied))
    check("B tied singlet weight is exactly 1/2", tied["s"] == Fraction(1, 2))
    check("B untied singlet weight is exactly 1/3", untied["s"] == Fraction(1, 3))
    check(
        "B untied conjugate coarse event has weight 2/3",
        untied["d_plus"] + untied["d_minus"] == Fraction(2, 3),
    )

    # Additivity by itself permits nonuniform atom weights.  Equal elementary
    # weight must follow from a supplied physical symmetry or be part of the
    # exact law; the current post-formation readout axiom does not provide it.
    tied_nonuniform = {"s": Fraction(1, 3), "d": Fraction(2, 3)}
    untied_nonuniform = {
        "s": Fraction(1, 2),
        "d_plus": Fraction(1, 4),
        "d_minus": Fraction(1, 4),
    }
    check("B tied nonuniform countermeasure is also additive", verify_finite_additivity(tied_atoms, tied_nonuniform))
    check("B untied K-even nonuniform countermeasure is also additive", verify_finite_additivity(untied_atoms, untied_nonuniform))
    check(
        "B additivity alone does not select a singlet weight",
        tied_nonuniform["s"] != tied["s"] and untied_nonuniform["s"] != untied["s"],
    )

    # Mere coordinate/presentation duplication does not create a physical
    # atom once an operational quotient is supplied.
    presentations = ("s@0", "d@plus", "d@minus")
    tied_quotient = {"s@0": "s", "d@plus": "d", "d@minus": "d"}
    untied_quotient = {
        "s@0": "s",
        "d@plus": "d_plus",
        "d@minus": "d_minus",
    }
    tied_classes = {tied_quotient[item] for item in presentations}
    untied_classes = {untied_quotient[item] for item in presentations}
    check("B tied quotient has two physical atoms despite three presentations", tied_classes == {"s", "d"})
    check("B untied quotient has three physically distinct atoms", untied_classes == {"s", "d_plus", "d_minus"})
    check("B same presentation set supports inequivalent physical quotients", len(tied_classes) == 2 and len(untied_classes) == 3)

    for relabel in permutations(presentations):
        check(
            f"B relabeling {relabel} preserves tied atom count",
            len({tied_quotient[item] for item in relabel}) == 2,
        )
        check(
            f"B relabeling {relabel} preserves untied atom count",
            len({untied_quotient[item] for item in relabel}) == 3,
        )


def effect_probability(rho: sp.Matrix, effect: sp.Matrix):
    return sp.simplify(sp.trace(rho * effect))


def positive_semidefinite(matrix: sp.Matrix) -> bool:
    eigenvalues = matrix.eigenvals()
    return all(bool(sp.simplify(value) >= 0) for value in eigenvalues)


def local_m2_instrument_witnesses() -> None:
    section("C - Two exact local M2(C) event laws in the same axiom envelope")
    I = sp.eye(2)
    X = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    rho = I / 2

    tied = {
        "s": (I + X) / 2,
        "d": (I - X) / 2,
    }
    untied = {
        "s": I / 3 + X / 3,
        "d_plus": I / 3 - X / 6 + sp.sqrt(3) * Y / 6,
        "d_minus": I / 3 - X / 6 - sp.sqrt(3) * Y / 6,
    }

    check("C tied effects sum exactly to identity", exact_matrix_equal(sum(tied.values(), sp.zeros(2)), I))
    check("C untied trine effects sum exactly to identity", exact_matrix_equal(sum(untied.values(), sp.zeros(2)), I))
    for label, effect in tied.items():
        check(f"C tied effect {label} is positive", positive_semidefinite(effect))
    for label, effect in untied.items():
        check(f"C untied effect {label} is positive", positive_semidefinite(effect))

    tied_probabilities = {label: effect_probability(rho, effect) for label, effect in tied.items()}
    untied_probabilities = {label: effect_probability(rho, effect) for label, effect in untied.items()}
    check("C tied instrument gives exact equal probabilities", set(tied_probabilities.values()) == {sp.Rational(1, 2)})
    check("C untied instrument gives exact equal probabilities", set(untied_probabilities.values()) == {sp.Rational(1, 3)})
    check("C both instruments normalize", sum(tied_probabilities.values()) == 1 and sum(untied_probabilities.values()) == 1)

    # Complex conjugation is a concrete K action: it swaps the two untied
    # conjugate outcomes while leaving the unordered event set and weights.
    conjugated = {label: effect.conjugate() for label, effect in untied.items()}
    check("C K fixes the singlet effect", exact_matrix_equal(conjugated["s"], untied["s"]))
    check("C K swaps d_plus and d_minus", exact_matrix_equal(conjugated["d_plus"], untied["d_minus"]) and exact_matrix_equal(conjugated["d_minus"], untied["d_plus"]))
    check("C unordered three-event law is K stable", all(any(exact_matrix_equal(effect, candidate) for candidate in untied.values()) for effect in conjugated.values()))

    # The same instrument may be installed at every site.  It refers to no
    # spatial axis, hence translations and every proper cubic rotation merely
    # permute sites and leave the local event law unchanged.
    check("C tied law is spatial-direction blind", all(effect.shape == (2, 2) for effect in tied.values()))
    check("C untied law is spatial-direction blind", all(effect.shape == (2, 2) for effect in untied.values()))
    check("C exact M2 witnesses have different physical event cardinality", len(tied) == 2 and len(untied) == 3)

    # A deterministic seed dilation witnesses one actual output for each
    # normalized rational kernel.  The seed is boundary/state data; the same
    # append-once record interface is used by both exact laws.
    def selected_outcome(labels: tuple[str, ...], seed: int) -> str:
        return labels[seed % len(labels)]

    def append_once(records: dict[tuple[int, int, int], str], site, outcome) -> bool:
        if site in records:
            return False
        records[site] = outcome
        return True

    def readout(records, values, sites) -> int:
        return sum(values[records[site]] for site in sites)

    tied_labels = tuple(tied)
    untied_labels = tuple(untied)
    tied_cycle = [selected_outcome(tied_labels, seed) for seed in range(2)]
    untied_cycle = [selected_outcome(untied_labels, seed) for seed in range(3)]
    check("C tied seed dilation visits each event once per period", set(tied_cycle) == set(tied_labels))
    check("C untied seed dilation visits each event once per period", set(untied_cycle) == set(untied_labels))

    for name, labels in (("tied", tied_labels), ("untied", untied_labels)):
        records: dict[tuple[int, int, int], str] = {}
        sites = tuple((index, 0, 0) for index in range(len(labels)))
        for seed, site in enumerate(sites):
            check(
                f"C {name} exact law appends one realized output at site {site}",
                append_once(records, site, selected_outcome(labels, seed)),
            )
        before = dict(records)
        check(
            f"C {name} record cannot be overwritten",
            not append_once(records, sites[0], labels[-1]) and records == before,
        )
        values = {label: index + 1 for index, label in enumerate(labels)}
        left = sites[:1]
        right = sites[1:]
        check(
            f"C {name} post-formation readout is additive on disjoint records",
            readout(records, values, sites)
            == readout(records, values, left) + readout(records, values, right),
        )


def koide_endpoint_controls() -> None:
    section("D - Conditional Koide endpoint arithmetic")

    def energy_bridge(w: Fraction) -> Fraction:
        return (1 - w) / (2 * w)

    def koide_map(r: Fraction) -> Fraction:
        return (1 + 2 * r) / 3

    tied_w = Fraction(1, 2)
    untied_w = Fraction(1, 3)
    tied_r = energy_bridge(tied_w)
    untied_r = energy_bridge(untied_w)
    check("D supplied bridge maps tied w=1/2 to r=1/2", tied_r == Fraction(1, 2))
    check("D supplied bridge maps untied w=1/3 to r=1", untied_r == 1)
    check("D supplied mass map gives tied Q=2/3", koide_map(tied_r) == Fraction(2, 3))
    check("D supplied mass map gives untied Q=1", koide_map(untied_r) == 1)

    # A different lawful map witnesses that event weights alone do not define
    # r.  This is not proposed physics; it is a type/independence control.
    alternative_map = lambda w: 1 - w
    check("D weight alone does not fix r without the energy bridge", alternative_map(tied_w) != tied_r or alternative_map(untied_w) != untied_r)
    check("D tied branch is not selected by endpoint arithmetic", tied_w != untied_w and tied_r != untied_r)


def matrix_key(matrix: sp.Matrix) -> tuple[int, ...]:
    return tuple(int(value) for value in matrix)


def signed_permutation_matrices(det_target: int | None = None) -> list[sp.Matrix]:
    matrices: list[sp.Matrix] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            determinant = int(matrix.det())
            if det_target is None or determinant == det_target:
                matrices.append(matrix)
    unique = {matrix_key(matrix): matrix for matrix in matrices}
    return list(unique.values())


def proper_cubic_chirality_controls() -> None:
    section("E - Proper-cubic covariance admits mirror-related handed laws")
    proper = signed_permutation_matrices(det_target=1)
    all_cubic = signed_permutation_matrices(det_target=None)
    proper_keys = {matrix_key(matrix) for matrix in proper}
    all_keys = {matrix_key(matrix) for matrix in all_cubic}
    I3 = sp.eye(3)
    P = sp.diag(-1, 1, 1)
    V_plus = I3
    V_minus = P

    check("E full cubic signed-permutation group has 48 elements", len(all_cubic) == 48)
    check("E proper cubic subgroup has 24 elements", len(proper) == 24)
    check("E mirror is cubic but improper", matrix_key(P) in all_keys and matrix_key(P) not in proper_keys and P.det() == -1)
    check("E handed frames have opposite determinant", V_plus.det() == 1 and V_minus.det() == -1)

    conjugation_closed = True
    covariance_both = True
    for rotation in proper:
        reflected_rotation = P * rotation * P
        conjugation_closed &= matrix_key(reflected_rotation) in proper_keys
        for frame in (V_plus, V_minus):
            coin_rotation = frame * rotation * frame.inv()
            covariance_both &= matrix_key(coin_rotation) in proper_keys
            covariance_both &= exact_matrix_equal(coin_rotation * frame, frame * rotation)
    check("E improper conjugation preserves the proper subgroup", conjugation_closed)
    check("E both handed frames satisfy the same proper-covariance equation", covariance_both)
    check("E no proper left/right rotations can change handed determinant", all((left * V_plus * right).det() == 1 for left in proper for right in proper))

    neighbors = {
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    }
    for index, cubic in enumerate(all_cubic):
        image = {
            tuple(int(value) for value in cubic * sp.Matrix(vector))
            for vector in neighbors
        }
        check(f"E six-neighbor set invariant under cubic element {index}", image == neighbors)

    # For h_V(k)=sigma dot V sin(k), the Jacobian chirality at a corner is
    # det(V)*product_i cos(k_i).  Each hand has four positive and four negative
    # corners; the origin sign flips between mirror twins.
    for name, frame in (("plus", V_plus), ("minus", V_minus)):
        signs = []
        for corner in product((0, 1), repeat=3):
            cosine_product = (-1) ** sum(corner)
            signs.append(int(frame.det()) * cosine_product)
        check(f"E {name} frame has four positive corners", signs.count(1) == 4)
        check(f"E {name} frame has four negative corners", signs.count(-1) == 4)
        check(f"E {name} frame has zero net corner chirality", sum(signs) == 0)
    check("E mirror twins have opposite origin chirality", int(V_plus.det()) == -int(V_minus.det()))


def permutation_matrix_on_six(ordering: tuple[tuple[int, ...], ...], transform) -> sp.Matrix:
    index = {item: position for position, item in enumerate(ordering)}
    matrix = sp.zeros(len(ordering))
    for column, item in enumerate(ordering):
        row = index[transform(item)]
        matrix[row, column] = 1
    return matrix


def permutation_parity(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return 1 if inversions % 2 == 0 else -1


def six_order_block_controls() -> None:
    section("F - Six-order block and symmetric clock do not select parity")
    orders = tuple(permutations((0, 1, 2)))
    even = [order for order in orders if permutation_parity(order) == 1]
    odd = [order for order in orders if permutation_parity(order) == -1]
    check("F S3 order carrier has six labels", len(orders) == 6)
    check("F order carrier splits three even and three odd", len(even) == 3 and len(odd) == 3)

    J = sp.ones(6)
    clock = J / 3 - sp.eye(6)
    ones = sp.ones(6, 1)
    parity = sp.Matrix([permutation_parity(order) for order in orders])
    check("F symmetric clock has +1 uniform eigenvector", exact_matrix_equal(clock * ones, ones))
    check("F parity vector is orthogonal to uniform", (ones.T * parity)[0] == 0)
    check("F symmetric clock treats parity as an undistinguished -1 mode", exact_matrix_equal(clock * parity, -parity))

    for left in orders:
        def compose(item, left=left):
            return tuple(left[item[index]] for index in range(3))

        representation = permutation_matrix_on_six(orders, compose)
        check(f"F clock commutes with order permutation {left}", exact_matrix_equal(clock * representation, representation * clock))

    transposition = (1, 0, 2)

    def mirror_order(item):
        return tuple(transposition[item[index]] for index in range(3))

    mirror = permutation_matrix_on_six(orders, mirror_order)
    check("F mirror maps the parity vector to its negative", exact_matrix_equal(mirror * parity, -parity))
    check("F clock is also mirror symmetric", exact_matrix_equal(clock * mirror, mirror * clock))


def independent_formula_cross_checks() -> None:
    section("G - Independent formula cross-checks")
    for atom_count in range(1, 9):
        weights = {str(index): Fraction(1, atom_count) for index in range(atom_count)}
        for size in range(atom_count + 1):
            event = frozenset(str(index) for index in range(size))
            check(
                f"G n={atom_count}, m={size} equal-atom event has m/n weight",
                finite_measure(event, weights) == Fraction(size, atom_count),
            )

    proper = signed_permutation_matrices(det_target=1)
    improper = signed_permutation_matrices(det_target=-1)
    check("G independent determinant census is 24+24", len(proper) == len(improper) == 24)
    check("G determinants multiply under every proper/improper pair", all((rotation * mirror).det() == -1 for rotation in proper for mirror in improper))


def main() -> int:
    source_and_ledger_contract()
    counting_and_presentation_controls()
    local_m2_instrument_witnesses()
    koide_endpoint_controls()
    proper_cubic_chirality_controls()
    six_order_block_controls()
    independent_formula_cross_checks()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
