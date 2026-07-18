#!/usr/bin/env python3
"""Exact Cycle 14 controls for foundation-licensed equivalence and Weyl walks.

Companion note:
  docs/work_history/repo/review_feedback/
  FOUNDATION_LICENSED_PHYSICAL_EQUIVALENCE_WEYL_PAIR_NOTE_2026-07-14.md

The runner checks finite algebra only: the proper cubic space group action,
fourth-root character orbits, origin versus frame dependence, BCC character
quotients, M2(C) recodings, chiral orientation, record-decoder co-recoding,
local versus relational phase action, Weyl-pair conjugacy and fixed-protocol
separation, torus descent, and note/N1--N8 contracts.

It does not promote a context category to foundation status, select a Weyl
law, amend an axiom, set an audit verdict, mutate a registry or queue, commit,
or open a PR.  Exit code 0 iff FAIL=0.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "FOUNDATION_LICENSED_PHYSICAL_EQUIVALENCE_WEYL_PAIR_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
I = sp.I
ID2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -I], [I, 0]])
SZ = sp.diag(1, -1)
PAULI = (SX, SY, SZ)
SQRT2 = sp.sqrt(2)


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


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return all(
        sp.simplify(sp.expand_complex(value)) == 0
        for value in sp.Matrix(left) - sp.Matrix(right)
    )


def normalized(text: str) -> str:
    return " ".join(
        text.lower().replace("*", "").replace("`", "").replace("_", " ").split()
    )


def parse_table(
    text: str, start: str, end: str
) -> tuple[tuple[str, ...], dict[str, tuple[str, ...]]]:
    body = text.split(start, 1)[1].split(end, 1)[0]
    lines = [line for line in body.splitlines() if line.startswith("|")]
    cells = [
        [item.strip().strip("`") for item in line.strip().strip("|").split("|")]
        for line in lines
    ]
    header = tuple(cells[0])
    rows = {
        row[0]: tuple(row[1:])
        for row in cells[2:]
        if len(row) == len(header) and row[0]
    }
    return header, rows


def signed_permutation_group(determinant: int) -> tuple[sp.Matrix, ...]:
    matrices: list[sp.Matrix] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if matrix.det() == determinant:
                matrices.append(matrix)
    return tuple(matrices)


PROPER = signed_permutation_group(+1)
IMPROPER = signed_permutation_group(-1)
CARDINAL_NEIGHBORS = {
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
}


def vector_tuple(vector: sp.Matrix, modulus: int | None = None) -> tuple[int, int, int]:
    values = tuple(int(value) for value in vector)
    if modulus is not None:
        values = tuple(value % modulus for value in values)
    return values  # type: ignore[return-value]


def lattice_group_probe() -> None:
    section("A - Exact supplied spatial group")
    check("A proper signed-permutation group has 24 elements", len(PROPER) == 24)
    check("A improper complement has 24 elements", len(IMPROPER) == 24)
    check("A every supplied rotation has determinant +1", all(matrix.det() == 1 for matrix in PROPER))
    check("A every excluded mirror has determinant -1", all(matrix.det() == -1 for matrix in IMPROPER))
    check("A proper rotations preserve cardinal neighbors", all({vector_tuple(matrix * sp.Matrix(v)) for v in CARDINAL_NEIGHBORS} == CARDINAL_NEIGHBORS for matrix in PROPER))
    check("A improper maps also preserve the graph but are outside named group", all({vector_tuple(matrix * sp.Matrix(v)) for v in CARDINAL_NEIGHBORS} == CARDINAL_NEIGHBORS for matrix in IMPROPER))
    products_closed = all(any(matrix_equal(left * right, candidate) for candidate in PROPER) for left in PROPER for right in PROPER)
    check("A proper cubic matrices are closed", products_closed)
    check("A identity belongs to proper group", any(matrix_equal(matrix, sp.eye(3)) for matrix in PROPER))


def character_value(q: tuple[int, int, int], x: tuple[int, int, int]) -> sp.Expr:
    return sp.simplify(I ** (sum(a * b for a, b in zip(q, x)) % 4))


def character_orbit(q: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    vector = sp.Matrix(q)
    return {vector_tuple(matrix * vector, 4) for matrix in PROPER}


H_BCC = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)


def add_mod4(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple((a + b) % 4 for a, b in zip(left, right))  # type: ignore[return-value]


def character_definability_probe() -> None:
    section("B - Origin-free adjoint action, frame-dependent fourth root")
    q_chi = (3, 3, 3)  # chi(x)=(-i)^(x+y+z)
    orbit = character_orbit(q_chi)
    check("B chi proper-cubic orbit has eight characters", len(orbit) == 8, repr(sorted(orbit)))
    check("B chi orbit is every +/- pi/2 corner", orbit == set(product((1, 3), repeat=3)))
    stabilizer = sum(vector_tuple(matrix * sp.Matrix(q_chi), 4) == q_chi for matrix in PROPER)
    check("B chi full-cardinal stabilizer has order three", stabilizer == 3)

    invariant: list[tuple[int, int, int]] = []
    for q in product(range(4), repeat=3):
        if all(vector_tuple(matrix * sp.Matrix(q), 4) == q for matrix in PROPER):
            invariant.append(q)
    check("B only trivial and checkerboard characters are proper-cubic invariant", invariant == [(0, 0, 0), (2, 2, 2)], repr(invariant))
    check(
        "B chi squared is checkerboard parity",
        all(
            sp.simplify(character_value(q_chi, x) ** 2)
            == (-1 if sum(x) % 2 else 1)
            for x in CARDINAL_NEIGHBORS
        ),
    )

    sample_positions = tuple(product(range(-1, 2), repeat=3))
    diagonal_origin_zero = sp.diag(*(character_value(q_chi, x) for x in sample_positions))
    for origin in ((1, 0, 0), (1, 2, -1), (-2, 1, 3)):
        shifted = sp.diag(
            *(
                character_value(q_chi, tuple(x[i] - origin[i] for i in range(3)))
                for x in sample_positions
            )
        )
        constant = character_value(q_chi, tuple(-value for value in origin))
        check(f"B origin {origin} changes G only by one scalar", matrix_equal(shifted, constant * diagonal_origin_zero))
        probe = sp.zeros(len(sample_positions))
        probe[0, -1] = 1
        check(f"B origin {origin} leaves Ad_G unchanged", matrix_equal(shifted * probe * shifted.H, diagonal_origin_zero * probe * diagonal_origin_zero.H))

    annihilator = {
        q
        for q in product(range(4), repeat=3)
        if all(sum(q[i] * h[i] for i in range(3)) % 4 == 0 for h in H_BCC)
    }
    expected_annihilator = {(0, 0, 0), (0, 2, 2), (2, 0, 2), (2, 2, 0)}
    check("B BCC sublattice annihilator has four characters", annihilator == expected_annihilator, repr(annihilator))

    def coset_representative(q: tuple[int, int, int]) -> tuple[int, int, int]:
        return min(add_mod4(q, element) for element in annihilator)

    quotient_orbit = {coset_representative(q) for q in orbit}
    check("B eight cardinal roots reduce to two BCC-component classes", len(quotient_orbit) == 2, repr(quotient_orbit))
    for q in orbit:
        same_class = [other for other in orbit if coset_representative(other) == coset_representative(q)]
        check(f"B BCC class of {q} has four cardinal frames", len(same_class) == 4)


def pauli_image(rotation_matrix: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    return tuple(
        sum((rotation_matrix[i, j] * PAULI[j] for j in range(3)), sp.zeros(2))
        for i in range(3)
    )  # type: ignore[return-value]


def orientation(paulis: tuple[sp.Matrix, sp.Matrix, sp.Matrix]) -> sp.Expr:
    return sp.simplify(sp.trace(paulis[0] * paulis[1] * paulis[2]) / (2 * I))


def m2_automorphism_probe() -> None:
    section("C - Common M2 recodings versus improper and local-frame changes")
    check("C canonical Pauli orientation is +1", orientation(PAULI) == 1)
    for index, rotation_matrix in enumerate(PROPER):
        images = pauli_image(rotation_matrix)
        check(f"C proper Pauli frame {index:02d} preserves orientation", orientation(images) == 1)
        check(f"C proper Pauli frame {index:02d} preserves products", all(matrix_equal(images[i] * images[j], (ID2 if i == j else I * sum((sp.LeviCivita(i, j, k) * images[k] for k in range(3)), sp.zeros(2)))) for i in range(3) for j in range(3)))

    conjugate_images = tuple(matrix.applyfunc(sp.conjugate) for matrix in PAULI)
    check("C complex conjugation fixes X", matrix_equal(conjugate_images[0], SX))
    check("C complex conjugation flips Y", matrix_equal(conjugate_images[1], -SY))
    check("C complex conjugation fixes Z", matrix_equal(conjugate_images[2], SZ))
    check("C complex conjugation reverses Pauli orientation", orientation(conjugate_images) == -1)

    # A common inner recoding preserves an isotropic two-site relation; an
    # independent recoding of only one site generally does not.
    heisenberg = sp.kronecker_product(SX, SX) + sp.kronecker_product(SY, SY) + sp.kronecker_product(SZ, SZ)
    hadamard = sp.Matrix([[1, 1], [1, -1]]) / SQRT2
    common = sp.kronecker_product(hadamard, hadamard)
    local = sp.kronecker_product(hadamard, ID2)
    check("C common inner recoding preserves isotropic neighbor relation", matrix_equal(common * heisenberg * common.H, heisenberg))
    check("C site-dependent one-sided recoding changes same relation", not matrix_equal(local * heisenberg * local.H, heisenberg))


def trace_probability(rho: sp.Matrix, effect: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(rho * effect))


def record_and_protocol_recode_probe() -> None:
    section("D - Record-content and complete-protocol co-recoding")
    ket0 = sp.Matrix([1, 0])
    rho0 = ket0 * ket0.H
    effect0 = rho0
    recoder = SX
    rho1 = recoder * rho0 * recoder.H
    effect1 = recoder * effect0 * recoder.H
    check("D original protocol has probability one", trace_probability(rho0, effect0) == 1)
    check("D co-recoded state and effect preserve probability", trace_probability(rho1, effect1) == 1)
    check("D recoded state with fixed decoder changes probability", trace_probability(rho1, effect0) == 0)

    original_decoder = {"c0": 0, "c1": 1}
    content_swap = {"c0": "c1", "c1": "c0"}
    transported_decoder = {content_swap[key]: value for key, value in original_decoder.items()}
    check("D content swap with transported decoder preserves c0 readout", transported_decoder[content_swap["c0"]] == original_decoder["c0"])
    check("D content swap with fixed decoder changes c0 readout", original_decoder[content_swap["c0"]] != original_decoder["c0"])

    positions = ((0, 0, 0), (1, 0, 0))
    state_position = positions[0]
    effect_position = positions[0]
    translation = (1, 0, 0)
    translated_state = tuple(a + b for a, b in zip(state_position, translation))
    translated_effect = tuple(a + b for a, b in zip(effect_position, translation))
    check("D spatially co-translated position record preserves match", translated_state == translated_effect)
    check("D translating state but fixing position decoder changes match", translated_state != effect_position)


ETA_PLUS = (1 + I) / 4
ETA_MINUS = (1 - I) / 4
BASE_POS = (
    sp.Matrix([[1, 0], [1, 0]]),
    sp.Matrix([[0, 1], [0, 1]]),
    sp.Matrix([[0, -1], [0, 1]]),
    sp.Matrix([[1, 0], [-1, 0]]),
)
BASE_NEG = (
    sp.Matrix([[0, -1], [0, 1]]),
    sp.Matrix([[1, 0], [-1, 0]]),
    sp.Matrix([[1, 0], [1, 0]]),
    sp.Matrix([[0, 1], [0, 1]]),
)


def negate(position: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(-value for value in position)  # type: ignore[return-value]


def transitions(branch: str) -> dict[tuple[int, int, int], sp.Matrix]:
    eta_pos, eta_neg = (
        (ETA_PLUS, ETA_MINUS) if branch == "plus" else (ETA_MINUS, ETA_PLUS)
    )
    result: dict[tuple[int, int, int], sp.Matrix] = {}
    for h, positive, negative in zip(H_BCC, BASE_POS, BASE_NEG):
        result[h] = eta_pos * positive
        result[negate(h)] = eta_neg * negative
    return result


def chi(position: tuple[int, int, int]) -> sp.Expr:
    return sp.simplify((-I) ** sum(position))


def rotation(pauli: sp.Matrix, angle: sp.Expr) -> sp.Matrix:
    return sp.cos(angle) * ID2 - I * sp.sin(angle) * pauli


def weyl(qx: sp.Expr, qy: sp.Expr, qz: sp.Expr, hand: int) -> sp.Matrix:
    return rotation(SX, qx) * rotation(SY, hand * qy) * rotation(SZ, qz)


def zero_substitution(matrix: sp.Matrix, symbols: tuple[sp.Symbol, ...]) -> sp.Matrix:
    substitutions = {symbol: 0 for symbol in symbols}
    return matrix.applyfunc(lambda value: sp.simplify(value.subs(substitutions)))


def weyl_pair_probe() -> None:
    section("E - Weyl pair under licensed and conditional transformations")
    plus = transitions("plus")
    minus = transitions("minus")
    for h in H_BCC:
        check(f"E positive {h} uses chi conjugacy", matrix_equal(plus[h], chi(h) * minus[h]))
        check(f"E negative {negate(h)} uses chi conjugacy", matrix_equal(plus[negate(h)], chi(negate(h)) * minus[negate(h)]))

    # Central phases are invisible on each onsite matrix algebra.
    generic = sp.Matrix([[2, 1 + I], [1 - I, -1]])
    for h in H_BCC:
        scalar = chi(h) * ID2
        check(f"E onsite Ad_chi is identity at {h}", matrix_equal(scalar * generic * scalar.H, generic))
    check("E chi changes an intersite link phase", sp.simplify(chi(H_BCC[0]) * sp.conjugate(chi((0, 0, 0)))) == I)

    qx, qy, qz = sp.symbols("qx qy qz", real=True)
    hands: dict[int, sp.Expr] = {}
    for hand in (+1, -1):
        walk = weyl(qx, qy, qz, hand)
        derivatives = tuple(I * zero_substitution(walk.diff(q), (qx, qy, qz)) for q in (qx, qy, qz))
        hands[hand] = orientation(derivatives)  # type: ignore[arg-type]
        check(f"E hand {hand:+d} has expected chiral sign", hands[hand] == hand)
    check("E proper/common-inner transformations cannot identify opposite signs", hands[+1] != hands[-1])
    reflected = (SX, -SY, SZ)
    check("E one improper reflection flips chiral sign", orientation(reflected) == -1)

    plus_x = sp.Matrix([1, 1]) / SQRT2
    minus_x = sp.Matrix([1, -1]) / SQRT2
    h1 = H_BCC[0]
    mh1 = negate(h1)
    psi_plus = sp.Matrix.vstack(plus[h1] * plus_x, plus[mh1] * plus_x)
    psi_minus = sp.Matrix.vstack(minus[h1] * plus_x, minus[mh1] * plus_x)
    G_endpoints = sp.diag(chi(h1), chi(h1), chi(mh1), chi(mh1))
    check("E endpoint state vectors obey psi_plus=G psi_minus", matrix_equal(psi_plus, G_endpoints * psi_minus))

    covariant_effect_minus = sp.Matrix.vstack(plus_x, minus_x) / SQRT2
    covariant_effect_plus = G_endpoints * covariant_effect_minus
    p_minus_cov = sp.simplify(abs((covariant_effect_minus.H * psi_minus)[0]) ** 2)
    p_plus_cov = sp.simplify(abs((covariant_effect_plus.H * psi_plus)[0]) ** 2)
    check("E G-co-transformed coherent effects agree", p_minus_cov == p_plus_cov, f"p={p_plus_cov}")

    fixed_effect = sp.Matrix.vstack(plus_x, I * minus_x) / SQRT2
    p_plus_fixed = sp.simplify(abs((fixed_effect.H * psi_plus)[0]) ** 2)
    p_minus_fixed = sp.simplify(abs((fixed_effect.H * psi_minus)[0]) ** 2)
    check("E fixed coherent effect gives exact plus probability 1/4", p_plus_fixed == sp.Rational(1, 4), str(p_plus_fixed))
    check("E fixed coherent effect gives exact minus probability 0", p_minus_fixed == 0, str(p_minus_fixed))


def boundary_probe() -> None:
    section("F - Boundary and phase-reference controls")
    for length in range(1, 9):
        descends = sp.simplify((-I) ** length) == 1
        check(f"F chi descends on cardinal torus L={length} iff 4 divides L", descends == (length % 4 == 0))

    # Checkerboard parity needs only even periodic length; it is structural but
    # still depends on a compatible finite quotient.
    for length in range(1, 7):
        parity_descends = (-1) ** length == 1
        check(f"F checkerboard parity descends on L={length} iff 2 divides L", parity_descends == (length % 2 == 0))


LICENSE_START = "<!-- license-ledger:start -->"
LICENSE_END = "<!-- license-ledger:end -->"
LICENSE_HEADER = ("transformation_id", "foundation_status", "safe_action", "weyl_pair_effect")
LICENSE_ROWS = {
    "T_TRANSLATION": ("SUPPLIED_COVARIANCE", "CO_TRANSFORM_SITES_RECORDS_PROTOCOL", "PRESERVES_CHIRAL_ORBIT"),
    "R_PROPER_CUBIC": ("SUPPLIED_COVARIANCE", "CO_TRANSFORM_SPATIAL_AND_INTERNAL_PRESENTATION", "PRESERVES_CHIRAL_SIGN"),
    "U_COMMON_M2": ("LICENSED_PRESENTATION_RECODING", "CO_TRANSFORM_RULE_CONTENT_DECODER", "PRESERVES_CHIRAL_SIGN"),
    "U_SITE_DEPENDENT_M2": ("NOT_SUPPLIED_AS_GAUGE", "REQUIRES_RELATIONAL_CONNECTION_OR_RULE_TRANSFORM", "MAY_CHANGE_LINK_LAW"),
    "C_RECORD_BIJECTION": ("CONDITIONAL_PRESENTATION_RECODING", "CO_TRANSFORM_CONTENT_AND_READOUT_DECODER", "NO_LAW_COLLAPSE_BY_ITSELF"),
    "G_CHI_STAGGERED_PHASE": ("NOT_FOUNDATION_SELECTED", "CONDITIONAL_ONE_PARTICLE_LINE_FRAME", "MAPS_WEYL_PAIR_IF_CONTEXT_BOUNDARY_TRANSFORM"),
    "P_REFLECTION": ("NOT_SUPPLIED", "IMPROPER_SPATIAL_TRANSFORM", "FLIPS_CHIRAL_SIGN"),
    "K_ANTIUNITARY": ("NOT_SUPPLIED", "CONJUGATE_LINEAR_OR_ANTI_AUTOMORPHISM", "CAN_FLIP_INTERNAL_ORIENTATION"),
    "B_BOUNDARY_TRANSFORM": ("CONTINGENT_OR_CONDITIONAL", "MAP_BOUNDARY_TWIST_REFERENCE_AND_STATE", "REQUIRED_FOR_GLOBAL_CHI_QUOTIENT"),
    "Q_PROTOCOL_RELABEL": ("CONDITIONAL_OPERATIONAL_EQUIVALENCE", "CO_TRANSFORM_PREPARATION_INSTRUMENT_EFFECT", "EQUAL_TRANSCRIPTS_ONLY_IN_CLOSED_CATEGORY"),
}

REFERENT_START = "<!-- referent-ledger:start -->"
REFERENT_END = "<!-- referent-ledger:end -->"
REFERENT_HEADER = ("candidate_referent", "under_safe_foundation_quotient", "stability", "exact_residual")
REFERENT_ROWS = {
    "ONE_WEYL_CLASS_VIA_REFLECTION": ("NO", "REFLECTION_NOT_LICENSED", "IMPROPER_IDENTIFICATION"),
    "ONE_WEYL_CLASS_VIA_CHI": ("NO_FOUNDATION_DERIVATION", "CONDITIONAL_PROTOCOL_CLASS_ONLY", "FRAME_CONTEXT_AND_BOUNDARY_CLOSURE"),
    "TWO_PROPER_CHIRAL_PRESENTATION_ORBITS": ("YES_CONDITIONALLY", "SMALLEST_PAIRWISE_STABLE_REFERENT", "FULL_CUBIC_GENERATED_LAW_AND_RECORD_CONTEXT"),
    "ONE_FIXED_ORDER_S2_WALK": ("NO", "FAILS_FULL_PROPER_CUBIC_COVARIANCE", "SCHEDULE_OR_CARRIER_ENLARGEMENT"),
}


def document_contract_probe() -> None:
    section("G - Note and formal-ledger contracts")
    check("G companion note exists", NOTE.is_file(), str(NOTE))
    if not NOTE.is_file():
        return
    text = NOTE.read_text(encoding="utf-8")
    flat = normalized(text)
    for source in (
        "https://arxiv.org/abs/1708.00826",
        "https://arxiv.org/abs/1306.1934",
        "https://arxiv.org/abs/1707.08455",
        "https://arxiv.org/abs/quant-ph/0405174",
        "https://arxiv.org/abs/math/9808033",
        "https://arxiv.org/abs/1911.06635",
        "https://arxiv.org/abs/quant-ph/0610030",
        "https://arxiv.org/abs/quant-ph/0310088",
        "https://arxiv.org/abs/0711.0043",
    ):
        check(f"G primary or source theorem linked: {source}", source in text)
    for token in (
        "G_found = Z^3 semidirect O_cubic^+",
        "chi^2=parity",
        "origin-independent but frame-dependent",
        "two proper-chiral presentation orbits",
        "partial-attempt-with-named-untested-routes",
        "no live foundation",
    ):
        check(f"G result token present: {token}", token in text)

    license_header, license_rows = parse_table(text, LICENSE_START, LICENSE_END)
    check("G license-ledger header exact", license_header == LICENSE_HEADER, repr(license_header))
    check("G license-ledger rows exact", license_rows == LICENSE_ROWS, repr(license_rows))
    referent_header, referent_rows = parse_table(text, REFERENT_START, REFERENT_END)
    check("G referent-ledger header exact", referent_header == REFERENT_HEADER, repr(referent_header))
    check("G referent-ledger rows exact", referent_rows == REFERENT_ROWS, repr(referent_rows))

    for path in (
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/work_history/repo/review_feedback/WEYL_PAIR_PHYSICAL_EQUIVALENCE_AND_COMBINED_INTERSECTION_NOTE_2026-07-14.md",
    ):
        check(f"G local authority path exists: {path}", path in text and (ROOT / path).is_file())
    check("G universal physical-equivalence group is withheld", "does not supply a universal physical equivalence group" in flat)


def no_go_discipline_probe() -> None:
    section("H - N1-N8 discipline contract")
    if not NOTE.is_file():
        check("H note required", False)
        return
    text = NOTE.read_text(encoding="utf-8")
    flat = normalized(text)
    for index in range(1, 9):
        check(f"H N{index} heading present", f"n{index} —" in flat)
    check("H N1 has at least five attempted routes", text.count("| ATTEMPTED |") >= 5)
    check("H N2 names collapsed walls", all(wall in text for wall in ("W1 FRAME_EXTENSION", "W2 PROTOCOL_EQUIVALENCE", "W3 FULL_CUBIC_LAW")))
    check("H N2 has three pair rows", sum(text.count(f"| {pair} |") for pair in ("W1-W2", "W1-W3", "W2-W3")) == 3)
    check("H N3 includes every trigger", all(trigger in text for trigger in ("we assume", "by construction", "as is standard", "the framework provides", "bridge context", "background", "naturally", "obviously", "standard QFT", "registered", "canonical")))
    check("H N4 has exact residual exclusions", text.count("excluded as a general witness") >= 2)
    check("H N5 has five resolutions", all(token in text for token in ("per-site", "per-link", "per-protocol", "per-boundary", "lattice-wide")))
    check("H N6 names approved primitives", all(token in text for token in ("scale-reference primitive", "kinetic-isotropy primitive", "realized-state primitive")))
    check("H N7 steelmans chi gauge route", "hostile steelman" in flat and "onsite records" in flat)
    check("H N8 cross-cycle table present", "cross-cycle echo" in flat and "retirement mechanism" in flat)
    check("H status demoted", "partial-attempt-with-named-untested-routes" in text)
    check("H no new axiom conclusion", "does not establish that a new axiom is required" in flat)


def independent_cross_checks() -> None:
    section("I - Independent exact recomputations")
    check("I chi at h1 is i", chi(H_BCC[0]) == I)
    check("I chi at -h1 is -i", chi(negate(H_BCC[0])) == -I)
    check("I chi square on one cardinal step is -1", chi((1, 0, 0)) ** 2 == -1)
    check("I parity is invariant under every proper rotation", all(sum(vector_tuple(matrix * sp.Matrix((1, 0, 0)))) % 2 == 1 for matrix in PROPER))
    check("I common scalar has trivial inner automorphism", matrix_equal((I * ID2) * SX * (I * ID2).H, SX))
    check("I Pauli reflection orientation is minus", orientation((SX, -SY, SZ)) == -1)
    amplitude_plus = sp.simplify((ETA_PLUS + I * ETA_MINUS) / SQRT2)
    amplitude_minus = sp.simplify((ETA_MINUS + I * ETA_PLUS) / SQRT2)
    check("I fixed separator plus recomputes 1/4", sp.simplify(abs(amplitude_plus) ** 2) == sp.Rational(1, 4))
    check("I fixed separator minus recomputes zero", amplitude_minus == 0)


def main() -> int:
    lattice_group_probe()
    character_definability_probe()
    m2_automorphism_probe()
    record_and_protocol_recode_probe()
    weyl_pair_probe()
    boundary_probe()
    document_contract_probe()
    no_go_discipline_probe()
    independent_cross_checks()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
