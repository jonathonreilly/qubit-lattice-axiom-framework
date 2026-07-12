#!/usr/bin/env python3
"""Exact checks for convention-invariant fixed-label selector constancy."""

from itertools import product
from pathlib import Path
import re
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
MEMO = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SIBLING = ROOT / "docs" / (
    "ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_"
    "BOUNDED_THEOREM_NOTE_2026-07-11.md"
)
BRIDGE = ROOT / "docs" / (
    "KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_"
    "SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md"
)

PASS = 0
FAIL = 0


def flat(text):
    collapsed = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"(?<=\w)- (?=\w)", "-", collapsed)


def matrix_zero(matrix):
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrix_equal(left, right):
    return matrix_zero(left - right)


def check(name, condition):
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {name}")
    else:
        FAIL += 1
        print(f"FAIL {name}")


memo_text = flat(MEMO.read_text(encoding="utf-8"))
sibling_source = SIBLING.read_text(encoding="utf-8")
sibling_text = flat(re.sub(r"(?m)^> ?", "", sibling_source))
bridge_text = flat(BRIDGE.read_text(encoding="utf-8"))

# V1: exact memo text, matched only after whitespace flattening.
real_presentation = (
    "A `Cl(3,0)`-compatible real-algebra presentation may be used "
    "equivalently and adds no further primitive structure."
)
no_privilege = "No possibility is privileged."
qualification = (
    "A choice not fixed by the supplied structure remains a named "
    "conditional or open dependency."
)
record_additivity = (
    "For any finite collection of pairwise-disjoint records, scalar readout "
    "`I` is additive, with `I(empty)=0`."
)
check("V1.1 Qubit real-presentation clause verbatim", real_presentation in memo_text)
check("V1.2 no-possibility-privileged clause verbatim", no_privilege in memo_text)
check("V1.3 Qualification choice clause verbatim", qualification in memo_text)
check("V1.4 Record additivity clause verbatim", record_additivity in memo_text)
named_content = (
    "These axioms state only their named primitive content. Further physical "
    "structure requires a retained derivation or bridge, or explicit "
    "approved-primitive registration, before use as a premise."
)
check("V1.5 named-primitive-content burden clause verbatim", named_content in memo_text)

# V2: Pauli realization of Cl(3,0), its pseudoscalar, and conjugation.
I = sp.I
sqrt3 = sp.sqrt(3)
eye2 = sp.eye(2)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])
sigmas = (s1, s2, s3)

clifford = []
for j, left in enumerate(sigmas):
    for k, right in enumerate(sigmas):
        target = 2 * eye2 if j == k else sp.zeros(2)
        clifford.append(matrix_equal(left * right + right * left, target))
check("V2.1 Pauli generators satisfy Cl(3,0)", all(clifford))

ps = s1 * s2 * s3
check("V2.2 pseudoscalar equals iI", matrix_equal(ps, I * eye2))
check("V2.3 pseudoscalar squares to -I", matrix_equal(ps**2, -eye2))

conjugated = tuple(s.conjugate() for s in sigmas)
conjugated_clifford = []
for j, left in enumerate(conjugated):
    for k, right in enumerate(conjugated):
        target = 2 * eye2 if j == k else sp.zeros(2)
        conjugated_clifford.append(
            matrix_equal(left * right + right * left, target)
        )
check(
    "V2.4 conjugated generators satisfy Cl(3,0)",
    all(conjugated_clifford),
)
conjugated_ps = conjugated[0] * conjugated[1] * conjugated[2]
check("V2.5 conjugated pseudoscalar equals -iI", matrix_equal(conjugated_ps, -I * eye2))

a, b = sp.symbols("a b", real=True)
root_equations = (a**2 - b**2 + 1, 2 * a * b)
real_roots = set(sp.solve(root_equations, (a, b), domain=sp.S.Reals))
expected_roots = {(sp.Integer(0), sp.Integer(-1)), (sp.Integer(0), sp.Integer(1))}
check("V2.6 real-span central square roots are exactly +/-ps", real_roots == expected_roots)

x11, x12, x21, x22 = sp.symbols("x11 x12 x21 x22")
generic_matrix = sp.Matrix([[x11, x12], [x21, x22]])
central_checks = []
root_checks = []
for a_value, b_value in sorted(real_roots, key=str):
    candidate = a_value * eye2 + b_value * ps
    central_checks.append(matrix_zero(candidate * generic_matrix - generic_matrix * candidate))
    root_checks.append(matrix_equal(candidate**2, -eye2))
check("V2.7 both roots are central and square to -I", all(central_checks + root_checks))
check("V2.8 entrywise conjugation exchanges the two roots", matrix_equal(ps.conjugate(), -ps))

# Two-model witness: entrywise conjugation is a real-algebra automorphism --
# multiplicative over the full 8-monomial spanning basis — so the standard
# and conjugated presentations are two models of the named Qubit content
# agreeing on every named clause and differing only in orientation.
monomials = [eye2, s1, s2, s3, s1 * s2, s1 * s3, s2 * s3, s1 * s2 * s3]
conj_mult = all(
    matrix_equal((m1 * m2).conjugate(), m1.conjugate() * m2.conjugate())
    for m1 in monomials
    for m2 in monomials
)
check("V2.9 two-model witness: conjugation is multiplicative over all 64 monomial products", conj_mult)
r_coeff, s_coeff = sp.symbols("r_coeff s_coeff", real=True)
conj_rlinear = all(
    matrix_equal(
        (r_coeff * m1 + s_coeff * m2).conjugate(),
        r_coeff * m1.conjugate() + s_coeff * m2.conjugate(),
    )
    for m1 in monomials
    for m2 in monomials
)
check("V2.10 two-model witness: conjugation is R-linear over the spanning basis", conj_rlinear)

# V3: grade involution on all 8x8 basis-monomial products.
words = ((), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2))


def rebuild(word, generators):
    result = eye2
    for index in word:
        result = result * generators[index]
    return result


negative_sigmas = tuple(-s for s in sigmas)
basis_matrices = tuple(rebuild(word, sigmas) for word in words)
alpha_basis_matrices = tuple(rebuild(word, negative_sigmas) for word in words)


def real_vector(matrix):
    entries = []
    for entry in matrix:
        entries.extend((sp.re(entry), sp.im(entry)))
    return sp.Matrix(entries)


basis_coordinate_matrix = sp.Matrix.hstack(
    *(real_vector(matrix) for matrix in basis_matrices)
)
basis_coordinate_inverse = basis_coordinate_matrix.inv()


def alpha_linear(matrix):
    coefficients = basis_coordinate_inverse * real_vector(matrix)
    return sp.simplify(
        sum(
            (coefficient * image for coefficient, image in zip(
                coefficients, alpha_basis_matrices
            )),
            sp.zeros(2),
        )
    )


alpha_multiplicative = []
for left_index, left_matrix in enumerate(basis_matrices):
    for right_index, right_matrix in enumerate(basis_matrices):
        alpha_of_product = alpha_linear(left_matrix * right_matrix)
        product_of_alphas = (
            alpha_basis_matrices[left_index]
            * alpha_basis_matrices[right_index]
        )
        alpha_multiplicative.append(
            matrix_equal(alpha_of_product, product_of_alphas)
        )
check("V3.1 grade involution multiplicative on all 8x8 basis products", all(alpha_multiplicative))
alpha_ps = rebuild((0, 1, 2), negative_sigmas)
check("V3.2 grade involution sends ps to -ps", matrix_equal(alpha_ps, -ps))

# V4: exact C3 character projectors and conjugation action.
C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
eye3 = sp.eye(3)
w = -sp.Rational(1, 2) + sqrt3 * I / 2
wbar = sp.conjugate(w)


def character_projector(character):
    return sp.simplify(
        (eye3 + sp.conjugate(character) * C
         + sp.conjugate(character**2) * C**2) / 3
    )


P1 = character_projector(sp.Integer(1))
Pw = character_projector(w)
Pwbar = character_projector(wbar)
projectors = (P1, Pw, Pwbar)
check("V4.1 character projectors resolve identity", matrix_equal(sum(projectors, sp.zeros(3)), eye3))
check("V4.2 character projectors are idempotent", all(matrix_equal(P * P, P) for P in projectors))
check(
    "V4.3 character projectors are pairwise orthogonal",
    all(matrix_zero(projectors[j] * projectors[k]) for j in range(3) for k in range(3) if j != k),
)
check("V4.4 C Pw = w Pw", matrix_equal(C * Pw, w * Pw))
check("V4.5 C and P1 are conjugation-fixed", matrix_equal(C.conjugate(), C) and matrix_equal(P1.conjugate(), P1))
check("V4.6 conjugation swaps Pw and P_wbar", matrix_equal(Pw.conjugate(), Pwbar))
doublet = sp.simplify(Pw + Pwbar)
check("V4.7 doublet block is conjugation-fixed", matrix_equal(doublet.conjugate(), doublet))
check("V4.8 doublet block has rank 2", doublet.rank() == 2)

# V5: exhaustive fixed-label selectors and their fiber partitions.
selectors = list(product(range(3), repeat=3))
sector_swap = (0, 2, 1)


def pullback_by_sector_swap(selector):
    return tuple(selector[sector_swap[index]] for index in range(3))


invariant_selectors = [
    selector
    for selector in selectors
    if pullback_by_sector_swap(selector) == selector
]
check("V5.1 exactly 9 of 27 selectors are swap-invariant", len(selectors) == 27 and len(invariant_selectors) == 9)
check(
    "V5.2 fixed-label swap invariance forces doublet constancy",
    all(selector[1] == selector[2] for selector in invariant_selectors)
    and any(selector[1] != selector[2] for selector in selectors),
)


def fiber_partition(selector):
    blocks = []
    for label in sorted(set(selector)):
        blocks.append(tuple(index for index, value in enumerate(selector) if value == label))
    return tuple(sorted(blocks))


induced_partitions = {fiber_partition(f) for f in invariant_selectors}
expected_partitions = {((0, 1, 2),), ((0,), (1, 2))}
block_counts = {len(partition) for partition in induced_partitions}
check("V5.3 invariant fixed-label selector fibers give exactly two partitions", induced_partitions == expected_partitions)
check("V5.4 finest fixed-label scalar-selector fiber partition has 2 blocks", max(block_counts) == 2 and ((0,), (1, 2)) in induced_partitions)

# V6: convention-odd resolver and convention-even surviving distinction.
odd_observable = sp.simplify(I * (C - C**2))
odd_eigenvalues = set(odd_observable.eigenvals())
check("V6a.1 i(C-C^2) is Hermitian", matrix_equal(odd_observable.conjugate().T, odd_observable))
check("V6a.2 i(C-C^2) is conjugation-odd", matrix_equal(odd_observable.conjugate(), -odd_observable))
check("V6a.3 i(C-C^2) has the resolving spectrum", odd_eigenvalues == {-sqrt3, sp.Integer(0), sqrt3})


def matrix_collection_equal(left, right):
    return len(left) == len(right) and all(
        any(matrix_equal(candidate, target) for target in right)
        for candidate in left
    )


unordered_pvm = tuple(projectors)
conjugated_unordered_pvm = tuple(P.conjugate() for P in projectors)
check(
    "V6a.4 unordered three-atom PVM is conjugation-stable",
    matrix_collection_equal(unordered_pvm, conjugated_unordered_pvm)
    and len(unordered_pvm) == 3,
)

even_observable = C + C**2
even_eigenvalues = set(even_observable.eigenvals())
check("V6b.1 C+C^2 is conjugation-even", matrix_equal(even_observable.conjugate(), even_observable))
check("V6b.2 C+C^2 has singlet-doublet spectrum", even_eigenvalues == {sp.Integer(2), sp.Integer(-1)})
check("V6b.3 C+C^2 retains a rank-1/rank-2 distinction", even_observable.eigenvals()[2] == 1 and even_observable.eigenvals()[-1] == 2)

assignment = (sp.Integer(1), w, wbar)
conjugated_assignment = tuple(sp.conjugate(value) for value in assignment)
w_selector = tuple(int(sp.simplify(value - w) == 0) for value in assignment)
conjugated_w_selector = tuple(int(sp.simplify(value - w) == 0) for value in conjugated_assignment)
check("V6c character-w selector flips under conjugation", w_selector == (0, 1, 0) and conjugated_w_selector == (0, 0, 1))

# V7: exact consumed-scope source text.
sibling_declaration = (
    "The charged-lepton 2-sector occupancy surface is the K/CPT-orbit "
    "partition `{singlet sector, doublet orbit}` with occupancy distribution "
    "`(p_s,p_d)`, `p_s+p_d=1`, where the equal-power-per-block grain reads "
    "`r=1/2` at `p_s=p_d`."
)
orbit_indexing = (
    "**ORBIT-INDEXING:** the context's record contents are indexed by "
    "`K`-orbits, so `K`-conjugate outcomes carry the same record content;"
)
supplied_framing = (
    "ORBIT-INDEXING and the determinant-character/log-character "
    "homomorphism boundary are supplied context structure. They are not "
    "derived from Record."
)
check("V7.1 sibling supplied-context declaration verbatim", sibling_declaration in sibling_text)
check("V7.2 bridge supplied ORBIT-INDEXING bullet verbatim", orbit_indexing in bridge_text)
check("V7.3 bridge supplied-context framing verbatim", supplied_framing in bridge_text)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(int(FAIL != 0))
