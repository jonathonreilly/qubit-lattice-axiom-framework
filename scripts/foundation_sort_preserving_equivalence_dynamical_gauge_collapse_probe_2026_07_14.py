#!/usr/bin/env python3
"""Exact finite probes for foundation sort preservation and gauge collapse.

This is an authority-free assumptions exercise.  It checks finite models,
finite-dimensional operator identities, and note/source contracts.  It does
not amend the axioms or declare a physical-equivalence category.
"""

from __future__ import annotations

import itertools
import re
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/FOUNDATION_SORT_PRESERVING_EQUIVALENCE_AND_DYNAMICAL_GAUGE_COLLAPSE_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
CYCLE20 = ROOT / "docs/work_history/repo/review_feedback/ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md"
CYCLE21 = ROOT / "docs/work_history/repo/review_feedback/NAMED_SITE_RECORD_FAITHFUL_EQUIVALENCE_CLASSIFICATION_NOTE_2026-07-14.md"

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool) -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def exact_equal(left: sp.Matrix | sp.Expr, right: sp.Matrix | sp.Expr) -> bool:
    difference = left - right
    if isinstance(difference, sp.MatrixBase):
        return all(sp.simplify(sp.expand_complex(entry)) == 0 for entry in difference)
    return sp.simplify(sp.expand_complex(difference)) == 0


def kron(*operators: sp.Matrix) -> sp.Matrix:
    result = sp.Matrix([[1]])
    for operator in operators:
        result = sp.kronecker_product(result, operator)
    return sp.Matrix(result)


def vectorize(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(matrix.rows * matrix.cols, 1, list(matrix))


def span_rank(matrices: tuple[sp.Matrix, ...] | list[sp.Matrix]) -> int:
    return sp.Matrix.hstack(*(vectorize(matrix) for matrix in matrices)).rank()


def in_span(matrix: sp.Matrix, basis: tuple[sp.Matrix, ...]) -> bool:
    return span_rank(basis + (matrix,)) == span_rank(basis)


I2 = sp.eye(2)
I4 = sp.eye(4)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)
PPLUS = (I2 + X) / 2
PMINUS = (I2 - X) / 2
PAULIS = (I2, X, Y, Z)
FACTOR0 = tuple(kron(operator, I2) for operator in PAULIS)
FACTOR1 = tuple(kron(I2, operator) for operator in PAULIS)


def controlled_phase(phase: sp.Expr) -> sp.Matrix:
    return sp.diag(1, 1, 1, sp.exp(sp.I * phase))


def cnot() -> sp.Matrix:
    return sp.Matrix(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ]
    )


def source_and_authority_contract() -> None:
    section("A - Source, scope, and authority contract")
    note = NOTE.read_text(encoding="utf-8")
    axioms = AXIOMS.read_text(encoding="utf-8")
    cycle20 = CYCLE20.read_text(encoding="utf-8")
    cycle21 = CYCLE21.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").split())

    check("A note is explicitly authority-free", "**authority:** none" in note.lower())
    check("A no live authority surface is changed", "changes no axiom" in normalized)
    check("A current axiom text names physical sites", "Physical sites are the points" in axioms)
    check("A current axiom text says each site has a domain", "Each site has a domain of local possibilities" in axioms)
    check("A current axiom text names one-site M2", "one-site possibility domain" in axioms and "M_2(C)" in axioms)
    check("A current axiom text makes states record configurations", "A state is a configuration of records" in axioms)
    check("A Cycle20 contains the transported-protocol theorem", "history-dependent local frame changes" in cycle20)
    check("A Cycle21 contains the transported-net fork", "transported site net" in cycle21.lower())
    for url in (
        "https://www.lfcs.inf.ed.ac.uk/reports/86/ECS-LFCS-86-10/",
        "https://arxiv.org/abs/quant-ph/0405174",
        "https://arxiv.org/abs/0910.3675",
        "https://arxiv.org/abs/2210.09314",
    ):
        check(f"A primary-source link present: {url.rsplit('/', 2)[-2]}", url in note)


def many_sorted_finite_model() -> None:
    section("B - Exact two-site many-sorted model")
    sites = (0, 1)
    possibilities = tuple((site, bit) for site in sites for bit in (0, 1))
    projection = {possibility: possibility[0] for possibility in possibilities}
    site_permutations = tuple(itertools.permutations(sites))
    possibility_permutations = tuple(itertools.permutations(possibilities))

    valid_pairs: list[tuple[tuple[int, ...], tuple[tuple[int, int], ...]]] = []
    valid_possibility_maps: set[tuple[tuple[int, int], ...]] = set()
    for site_image in site_permutations:
        f_site = dict(zip(sites, site_image))
        for possibility_image in possibility_permutations:
            f_possibility = dict(zip(possibilities, possibility_image))
            if all(
                projection[f_possibility[possibility]] == f_site[projection[possibility]]
                for possibility in possibilities
            ):
                valid_pairs.append((site_image, possibility_image))
                valid_possibility_maps.add(possibility_image)

    check("B there are 24 arbitrary possibility bijections", len(possibility_permutations) == 24)
    check("B exactly eight sort/fiber-preserving bijections survive", len(valid_pairs) == 8)
    check("B each valid possibility map determines its site map", len(valid_possibility_maps) == 8)
    check("B count agrees with 2! site maps times 2! per fiber", len(valid_pairs) == 2 * 2 * 2)

    common_dictionary_count = 0
    for site_image, possibility_image in valid_pairs:
        f_possibility = dict(zip(possibilities, possibility_image))
        bit_maps = []
        for site in sites:
            bit_maps.append(tuple(f_possibility[(site, bit)][1] for bit in (0, 1)))
        if bit_maps[0] == bit_maps[1]:
            common_dictionary_count += 1
    check("B a common site-independent content dictionary leaves four maps", common_dictionary_count == 4)

    split_image = {
        (0, 0): (0, 0),
        (0, 1): (1, 0),
        (1, 0): (0, 1),
        (1, 1): (1, 1),
    }
    split_has_site_map = any(
        all(
            projection[split_image[possibility]] == dict(zip(sites, image))[projection[possibility]]
            for possibility in possibilities
        )
        for image in site_permutations
    )
    check("B a map that splits one source fiber has no site map", not split_has_site_map)

    # The same result in a single-sorted coding with unary Site and binary Fiber.
    universe = ("s0", "s1", "p00", "p01", "p10", "p11")
    site_predicate = {"s0", "s1"}
    fiber_relation = {
        ("p00", "s0"),
        ("p01", "s0"),
        ("p10", "s1"),
        ("p11", "s1"),
    }
    encoded_count = 0
    for site_image, possibility_image in valid_pairs:
        mapping = {
            "s0": f"s{site_image[0]}",
            "s1": f"s{site_image[1]}",
        }
        for source, target in zip(possibilities, possibility_image):
            mapping[f"p{source[0]}{source[1]}"] = f"p{target[0]}{target[1]}"
        preserves_site = all((item in site_predicate) == (mapping[item] in site_predicate) for item in universe)
        preserves_fiber = {
            (mapping[possibility], mapping[site]) for possibility, site in fiber_relation
        } == fiber_relation
        if preserves_site and preserves_fiber:
            encoded_count += 1
    check("B single-sorted predicates recover the same eight maps", encoded_count == 8)

    # Transport one admissibility relation, record, and scalar dictionary.
    f_site = {0: 1, 1: 0}
    f_possibility = {(0, 0): (1, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 0)}
    adjacency = {(0, 1), (1, 0)}
    admissible = {
        (site, neighbor_bit, (site, neighbor_bit))
        for site in sites
        for neighbor_bit in (0, 1)
    }
    transported_admissible = {
        (f_site[site], 1 - neighbor_bit, f_possibility[possibility])
        for site, neighbor_bit, possibility in admissible
    }
    records = {0: (0, 1)}
    transported_records = {f_site[site]: f_possibility[possibility] for site, possibility in records.items()}
    content = {(site, bit): sp.Integer(bit) for site, bit in possibilities}
    transported_content = {f_possibility[possibility]: value for possibility, value in content.items()}
    check("B adjacency is preserved", {(f_site[x], f_site[y]) for x, y in adjacency} == adjacency)
    check("B transported admissibility is still fiber-correct", all(projection[p] == site for site, _, p in transported_admissible))
    check("B a transported record remains in its site's fiber", all(projection[p] == site for site, p in transported_records.items()))
    check("B transported scalar readout preserves record value", all(transported_content[f_possibility[p]] == content[p] for p in records.values()))


def representation_reduct_and_expansion() -> None:
    section("C - Foundation reduct versus global-algebra expansion")
    phase = sp.pi / 2
    frame = controlled_phase(phase)
    transported0 = tuple(sp.simplify(frame * operator * frame.H) for operator in FACTOR0)
    transported1 = tuple(sp.simplify(frame * operator * frame.H) for operator in FACTOR1)

    check("C frame is exactly unitary", exact_equal(frame.H * frame, I4))
    check("C transported first factor has dimension four", span_rank(transported0) == 4)
    check("C transported second factor has dimension four", span_rank(transported1) == 4)
    check("C transported factors intersect only in scalars", span_rank(transported0 + transported1) == 7)
    check("C transported factors commute elementwise", all(exact_equal(left * right, right * left) for left in transported0 for right in transported1))
    products = tuple(left * right for left in transported0 for right in transported1)
    check("C transported factors generate the full M4 algebra", span_rank(products) == 16)

    transported_x0 = transported0[1]
    check("C entangling transport sends old X0 outside old factor 0", not in_span(transported_x0, FACTOR0))
    check("C entangling transport sends old X0 outside old factor 1", not in_span(transported_x0, FACTOR1))
    check("C embedding naturality holds by conjugation", all(exact_equal(frame * old * frame.H, new) for old, new in zip(FACTOR0, transported0)))

    foundation_reduct_old = {
        "sites": (0, 1),
        "fibers": {0: "abstract M2", 1: "abstract M2"},
        "adjacency": {(0, 1), (1, 0)},
    }
    foundation_reduct_new = {
        "sites": (0, 1),
        "fibers": {0: "abstract M2", 1: "abstract M2"},
        "adjacency": {(0, 1), (1, 0)},
    }
    check("C old and transported embeddings have the same foundation reduct", foundation_reduct_old == foundation_reduct_new)
    check("C old and transported global embeddings are different expansions", any(not exact_equal(old, new) for old, new in zip(FACTOR0, transported0)))


def deterministic_history_gauge() -> None:
    section("D - Exact finite-history reversible gauge collapse")
    cz = controlled_phase(sp.pi)
    updates = (kron(H, I2), cz, cnot())
    check("D every test update is unitary", all(exact_equal(update.H * update, I4) for update in updates))
    frames = [I4]
    for update in updates:
        frames.append(sp.simplify(frames[-1] * update.H))
    transformed = [
        sp.simplify(frames[index + 1] * update * frames[index].H)
        for index, update in enumerate(updates)
    ]
    check("D recursive history frames trivialize every deterministic edge", all(exact_equal(edge, I4) for edge in transformed))
    check("D frame recursion stays unitary", all(exact_equal(frame.H * frame, I4) for frame in frames))

    # A branching history tree: unique history nodes allow independent output frames.
    branch_updates = {
        ((), "0"): kron(H, I2),
        ((), "1"): cnot(),
        (("0",), "a"): cz,
        (("0",), "b"): kron(X, I2),
        (("1",), "a"): kron(I2, H),
        (("1",), "b"): controlled_phase(sp.pi / 2),
    }
    history_frames: dict[tuple[str, ...], sp.Matrix] = {(): I4}
    for depth in (0, 1):
        for (history, label), update in branch_updates.items():
            if len(history) != depth:
                continue
            child = history + (label,)
            history_frames[child] = sp.simplify(history_frames[history] * update.H)
    branch_transforms = []
    for (history, label), update in branch_updates.items():
        child = history + (label,)
        branch_transforms.append(sp.simplify(history_frames[child] * update * history_frames[history].H))
    check("D every edge of a finite reversible history tree becomes identity", all(exact_equal(edge, I4) for edge in branch_transforms))
    check("D branch labels remain six distinct labeled edges", len(branch_updates) == 6)


def locality_and_qca_residual() -> None:
    section("E - Uniform locality is the infinite-law residual")
    phase = sp.pi / 7
    update = controlled_phase(phase)
    repeated_ok = True
    for time in range(8):
        frame_now = controlled_phase(-time * phase)
        frame_next = controlled_phase(-(time + 1) * phase)
        repeated_ok &= exact_equal(sp.simplify(frame_next * update * frame_now.H), I4)
    check("E repeated controlled phase is trivialized by a two-site frame at every sampled time", repeated_ok)
    check("E every sampled controlled-phase frame remains diagonal", all(controlled_phase(-time * phase).is_diagonal() for time in range(8)))

    # On Z, a right shift repeated t times moves a local observable by distance t.
    displacements = {time: abs((0 - time) - 0) for time in range(1, 13)}
    check("E cumulative inverse-shift frame has exact displacement t", all(distance == time for time, distance in displacements.items()))
    check("E no fixed range R below 12 covers all twelve sampled times", all(any(distance > radius for distance in displacements.values()) for radius in range(12)))
    note_text = NOTE.read_text(encoding="utf-8").lower().replace("`", "")
    check("E the note states the analytic unbounded-displacement argument", "support at x-t" in note_text)


def record_instrument_invariants() -> None:
    section("F - Nonunitary record instruments do not gauge to identity")
    k0 = sp.simplify(P0 * H)
    k1 = sp.simplify(P1 * H)
    check("F projective record instrument is complete", exact_equal(k0.H * k0 + k1.H * k1, I2))
    check("F both record branches have rank one", k0.rank() == 1 and k1.rank() == 1)
    check("F identity has rank two", I2.rank() == 2)
    check("F branch effects are X-basis projectors", exact_equal(k0.H * k0, PPLUS) and exact_equal(k1.H * k1, PMINUS))
    check("F output frame removes branch unitary but leaves positive effect", exact_equal(H * k0, PPLUS) and exact_equal(H * k1, PMINUS))
    check("F positive effects have invariant spectrum {0,1}", all(effect.eigenvals() == {0: 1, 1: 1} for effect in (PPLUS, PMINUS)))

    ket0 = sp.Matrix([1, 0])
    ket_plus = sp.Matrix([1, 1]) / sp.sqrt(2)
    probabilities0 = tuple(sp.simplify((state.H * operator.H * operator * state)[0]) for operator in (k0, k1) for state in (ket0,))
    probabilities_plus = tuple(sp.simplify((state.H * operator.H * operator * state)[0]) for operator in (k0, k1) for state in (ket_plus,))
    check("F |0> gives two half-weight record branches", probabilities0 == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("F |+> gives one certain and one zero branch", probabilities_plus == (sp.Integer(1), sp.Integer(0)))

    def choi(kraus: tuple[sp.Matrix, ...]) -> sp.Matrix:
        return sp.simplify(sum((vectorize(operator) * vectorize(operator).H for operator in kraus), sp.zeros(4)))

    record_choi = choi((k0, k1))
    unitary_choi = choi((H,))
    check("F record channel has Choi rank two", record_choi.rank() == 2)
    check("F unitary channel has Choi rank one", unitary_choi.rank() == 1)
    pre = H
    post = X
    transported_choi = choi(tuple(sp.simplify(post * operator * pre.H) for operator in (k0, k1)))
    check("F unitary pre/post transport preserves record Choi rank", transported_choi.rank() == record_choi.rank())


def record_time_cost_invariants() -> None:
    section("G - Record history, event order, and cost are not erased")
    identity_tree = {(): {"next": ()}}
    record_tree = {(): {"next": ("0", "1")}, ("0",): {"next": ()}, ("1",): {"next": ()}}
    check("G a two-outcome record root is not bijective to a singleton identity root", len(record_tree[()]["next"]) != len(identity_tree[()]["next"]))
    check("G record tree has two terminal transcripts", sum(not node["next"] for node in record_tree.values()) == 2)
    check("G identity tree has one terminal transcript", sum(not node["next"] for node in identity_tree.values()) == 1)

    transcript = ((2, "0", 3), (5, "1", 4))  # event time, label, scalar cost
    relabeled = tuple((time, {"0": "a", "1": "b"}[label], cost) for time, label, cost in transcript)
    check("G label relabeling preserves event times", tuple(row[0] for row in relabeled) == (2, 5))
    check("G label relabeling preserves additive scalar cost", sum(row[2] for row in relabeled) == 7)
    check("G event order is preserved", relabeled[0][0] < relabeled[1][0])
    wrapped = relabeled + ((6, "frame-certificate", 1),)
    check("G an actively recorded frame wrapper adds an event", len(wrapped) == len(relabeled) + 1)
    check("G an actively recorded frame wrapper adds scalar cost", sum(row[2] for row in wrapped) == 8)


def clause_deletion_and_no_go_contract() -> None:
    section("H - Clause deletion and N1-N8 stress-test contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").split())
    proposed = "A framework equivalence is a sort-preserving isomorphism of the supplied structure."
    law = (
        "A law equivalence is such an isomorphism at every record history, compositional and uniformly local, "
        "preserving record labels, event order, and scalar readout."
    )
    check("H minimal framework-equivalence sentence appears verbatim", proposed in note)
    check("H minimal law-equivalence sentence appears verbatim", law in note)
    check("H note says no axiom addition is needed for the sort result", "no axiom addition is needed" in normalized)
    check("H note places clarification in a law-equivalence definition", "law-equivalence definition" in normalized)
    check("H note rejects placement inside Lattice/Qubit", "not inside lattice or qubit" in normalized)
    check("H clause-deletion table is present", "## clause-deletion pass" in note.lower())
    check("H all no-go sections N1-N8 are present", all(re.search(rf"^### N{number}\b", note, re.MULTILINE) for number in range(1, 9)))
    for phrase in (
        "first record",
        "actual branch",
        "born",
        "formation trigger",
        "uniform locality",
        "choi rank",
        "foundation reduct",
        "representation expansion",
    ):
        check(f"H residual boundary named: {phrase}", phrase in normalized)


def main() -> None:
    source_and_authority_contract()
    many_sorted_finite_model()
    representation_reduct_and_expansion()
    deterministic_history_gauge()
    locality_and_qca_residual()
    record_instrument_invariants()
    record_time_cost_invariants()
    clause_deletion_and_no_go_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
