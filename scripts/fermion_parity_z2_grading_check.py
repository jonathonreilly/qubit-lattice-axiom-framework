#!/usr/bin/env python3
"""Exact evidence for the ordered finite-mode fermion-parity theorem.

The runner uses only finite matrices and exact SymPy arithmetic. It neither
reads the theorem note, audit data, prose/status files, nor external data.

Modes:
  normal               construct Jordan-Wigner operators and verify the theorem
  independent          classify Q and F commutants from occupation sectors
  hostile              require every named scientific mutation to be rejected
  intentional-failure  promote selected hostile fixtures and exit nonzero
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from itertools import product
from pathlib import Path

import sympy as sp


SOURCE_PATH = Path(__file__).resolve()
FIXTURES = (
    "false-converse",
    "odd-number-change",
    "wrong-product-phase",
    "bare-local-car",
    "wrong-sector-dimension",
    "even-means-number-conserving",
    "wrong-pair-order",
)


class Checks:
    def __init__(self) -> None:
        self.passes = 0
        self.failures = 0

    def record(self, label: str, condition: bool, detail: str) -> None:
        status = "PASS" if condition else "FAIL"
        if condition:
            self.passes += 1
        else:
            self.failures += 1
        print(f"[{status}] {label}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passes} FAIL={self.failures}")
        return 0 if self.failures == 0 else 1


@dataclass(frozen=True)
class JWData:
    n_modes: int
    identity: sp.Matrix
    lower: sp.Matrix
    z_local: sp.Matrix
    a: tuple[sp.Matrix, ...]
    adag: tuple[sp.Matrix, ...]
    n_ops: tuple[sp.Matrix, ...]
    q_total: sp.Matrix
    q_values: tuple[int, ...]
    parity_values: tuple[int, ...]
    projectors: tuple[sp.Matrix, ...]
    f_exponential: sp.Matrix
    f_spectral: sp.Matrix
    f_product: sp.Matrix


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_zero(left - right)


def commutator(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return left * right - right * left


def anticommutator(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return left * right + right * left


def kron_all(factors: list[sp.Matrix]) -> sp.Matrix:
    if not factors:
        return sp.ones(1, 1)
    result = factors[0]
    for factor in factors[1:]:
        result = sp.kronecker_product(result, factor)
    return result


def at_site(local: sp.Matrix, site: int, n_modes: int) -> sp.Matrix:
    identity_two = sp.eye(2)
    return kron_all(
        [local if position == site else identity_two for position in range(n_modes)]
    )


def occupation_tuple(index: int, n_modes: int) -> tuple[int, ...]:
    return tuple((index >> (n_modes - 1 - site)) & 1 for site in range(n_modes))


def matrix_unit(dimension: int, row: int, column: int) -> sp.Matrix:
    result = sp.zeros(dimension)
    result[row, column] = 1
    return result


def build_jordan_wigner(n_modes: int) -> JWData:
    if n_modes < 1:
        raise ValueError("n_modes must be at least one")

    identity_two = sp.eye(2)
    lower = sp.Matrix([[0, 1], [0, 0]])
    z_local = sp.diag(1, -1)
    dimension = 2**n_modes

    annihilators: list[sp.Matrix] = []
    for site in range(n_modes):
        factors = [z_local] * site + [lower] + [identity_two] * (n_modes - site - 1)
        annihilators.append(kron_all(factors))
    creators = [operator.H for operator in annihilators]
    number_ops = [creators[site] * annihilators[site] for site in range(n_modes)]
    q_total = sp.zeros(dimension)
    for number_op in number_ops:
        q_total += number_op

    occupations = tuple(occupation_tuple(index, n_modes) for index in range(dimension))
    q_values = tuple(sum(bits) for bits in occupations)
    parity_values = tuple((-1) ** value for value in q_values)

    projectors: list[sp.Matrix] = []
    for charge in range(n_modes + 1):
        projector = sp.zeros(dimension)
        for index, value in enumerate(q_values):
            if value == charge:
                projector[index, index] = 1
        projectors.append(projector)

    f_exponential = sp.zeros(dimension)
    f_spectral = sp.zeros(dimension)
    for charge, projector in enumerate(projectors):
        f_exponential += sp.exp(sp.I * sp.pi * charge) * projector
        f_spectral += ((-1) ** charge) * projector
    f_product = kron_all([z_local] * n_modes)

    return JWData(
        n_modes=n_modes,
        identity=sp.eye(dimension),
        lower=lower,
        z_local=z_local,
        a=tuple(annihilators),
        adag=tuple(creators),
        n_ops=tuple(number_ops),
        q_total=q_total,
        q_values=q_values,
        parity_values=parity_values,
        projectors=tuple(projectors),
        f_exponential=f_exponential,
        f_spectral=f_spectral,
        f_product=f_product,
    )


def direct_pair_hamiltonian(n_modes: int) -> sp.Matrix:
    if n_modes < 2:
        raise ValueError("the pair Hamiltonian requires at least two modes")
    pair = sp.zeros(4)
    pair[0, 3] = 1
    pair[3, 0] = 1
    return kron_all([pair] + [sp.eye(2)] * (n_modes - 2))


def source_firewall_violations() -> list[str]:
    """Reject evidence hazards without reading any theorem or status surface."""

    source = SOURCE_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    violations: list[str] = []
    allowed_imports = {
        "__future__",
        "argparse",
        "ast",
        "dataclasses",
        "itertools",
        "pathlib",
        "sympy",
    }
    imported_roots: set[str] = set()
    read_calls = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_roots.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in {"eval", "exec", "open"}:
                violations.append(f"forbidden call: {node.func.id}")
            if isinstance(node.func, ast.Attribute) and node.func.attr in {
                "read_text",
                "read_bytes",
                "open",
            }:
                read_calls += 1
            if (
                isinstance(node.func, ast.Attribute)
                and node.func.attr == "record"
                and len(node.args) >= 2
                and isinstance(node.args[1], ast.Constant)
                and node.args[1].value is True
            ):
                violations.append("literal-True evidence conclusion")

    unexpected_imports = imported_roots - allowed_imports
    if unexpected_imports:
        violations.append(f"unexpected imports: {sorted(unexpected_imports)}")
    if read_calls != 1:
        violations.append(f"unexpected file-read count: {read_calls}")
    forbidden_markers = (
        "docs/" + "audit",
        "AUDIT_" + "LEDGER",
        "effective_" + "status",
        "http" + "://",
        "https" + "://",
        "REFERENCE_" + "ANSWER",
    )
    for forbidden in forbidden_markers:
        if forbidden in source:
            violations.append(f"forbidden source marker: {forbidden}")
    return violations


def run_normal() -> int:
    checks = Checks()
    data = build_jordan_wigner(3)
    dimension = data.identity.rows
    print("ORDERED FINITE-MODE FERMION PARITY — NORMAL EXACT MODE")

    firewall = source_firewall_violations()
    checks.record(
        "source/import firewall",
        not firewall,
        f"violations={firewall}",
    )

    expected_q = sp.diag(*data.q_values)
    local_number_ok = all(
        matrix_equal(
            data.n_ops[site],
            at_site(sp.diag(0, 1), site, data.n_modes),
        )
        for site in range(data.n_modes)
    )
    checks.record(
        "ordered occupation basis and exact n_x/Q action",
        local_number_ok and matrix_equal(data.q_total, expected_q),
        f"Q diagonal={data.q_values}",
    )

    annihilator_car = all(
        matrix_zero(anticommutator(data.a[x], data.a[y]))
        for x in range(data.n_modes)
        for y in range(data.n_modes)
    )
    creator_car = all(
        matrix_zero(anticommutator(data.adag[x], data.adag[y]))
        for x in range(data.n_modes)
        for y in range(data.n_modes)
    )
    mixed_car = all(
        matrix_equal(
            anticommutator(data.a[x], data.adag[y]),
            data.identity if x == y else sp.zeros(dimension),
        )
        for x in range(data.n_modes)
        for y in range(data.n_modes)
    )
    checks.record(
        "Jordan-Wigner construction realizes the full CAR",
        annihilator_car and creator_car and mixed_car,
        f"checked {3 * data.n_modes**2} exact anticommutators",
    )

    spectral_projectors_ok = (
        matrix_equal(sum(data.projectors, sp.zeros(dimension)), data.identity)
        and all(matrix_equal(projector * projector, projector) for projector in data.projectors)
        and all(
            matrix_zero(data.projectors[left] * data.projectors[right])
            for left in range(len(data.projectors))
            for right in range(len(data.projectors))
            if left != right
        )
    )
    checks.record(
        "integer Q spectral decomposition",
        spectral_projectors_ok
        and set(data.q_values) == set(range(data.n_modes + 1)),
        f"spectrum={sorted(set(data.q_values))}",
    )

    checks.record(
        "F=exp(i*pi*Q) equals spectral signs and tensor-product Z",
        matrix_equal(data.f_exponential, data.f_spectral)
        and matrix_equal(data.f_spectral, data.f_product),
        "three independently constructed exact matrices agree",
    )

    f_properties = (
        matrix_equal(data.f_product.H, data.f_product)
        and matrix_equal(data.f_product.H * data.f_product, data.identity)
        and matrix_equal(data.f_product * data.f_product, data.identity)
    )
    checks.record(
        "F is Hermitian, unitary, and involutive",
        f_properties,
        "F^dagger=F and F^2=I exactly",
    )

    dimension_checks: list[tuple[int, int, int]] = []
    for n_modes in range(1, 7):
        parities = [(-1) ** sum(occupation_tuple(index, n_modes)) for index in range(2**n_modes)]
        dimension_checks.append((n_modes, parities.count(1), parities.count(-1)))
    balanced = all(even == odd == 2 ** (n_modes - 1) for n_modes, even, odd in dimension_checks)
    checks.record(
        "both parity eigenvalues occur with dimensions 2^(N-1)",
        balanced,
        f"sector dimensions={dimension_checks}",
    )

    p_even = (data.identity + data.f_product) / 2
    p_odd = (data.identity - data.f_product) / 2
    grading_ok = (
        matrix_equal(p_even + p_odd, data.identity)
        and matrix_zero(p_even * p_odd)
        and p_even.rank() == p_odd.rank() == 2 ** (data.n_modes - 1)
    )
    checks.record(
        "H_N is the direct sum of exact even/odd projectors",
        grading_ok,
        f"ranks=({p_even.rank()},{p_odd.rank()})",
    )

    odd_action = all(
        matrix_equal(data.f_product * operator * data.f_product, -operator)
        for operator in data.a + data.adag
    )
    checks.record(
        "every a_x and a_x^dagger is parity odd",
        odd_action,
        f"checked {2 * data.n_modes} generators",
    )

    generators = data.a + data.adag
    monomial_total = 0
    nonzero_total = 0
    monomial_grading_ok = True
    for degree in range(5):
        for indices in product(range(len(generators)), repeat=degree):
            monomial = data.identity
            for index in indices:
                monomial *= generators[index]
            monomial_total += 1
            if not matrix_zero(monomial):
                nonzero_total += 1
            expected = ((-1) ** degree) * monomial
            if not matrix_equal(data.f_product * monomial * data.f_product, expected):
                monomial_grading_ok = False
    checks.record(
        "monomials acquire (-1)^degree under F conjugation",
        monomial_grading_ok,
        f"checked={monomial_total}, nonzero={nonzero_total}, degrees=0..4",
    )

    hopping = data.adag[0] * data.a[1] + data.adag[1] * data.a[0]
    checks.record(
        "number-conserving hopping also conserves parity",
        matrix_zero(commutator(hopping, data.q_total))
        and matrix_zero(commutator(hopping, data.f_product)),
        "both exact commutators vanish",
    )

    pair_from_car = data.adag[0] * data.adag[1] + data.a[1] * data.a[0]
    pair_direct = direct_pair_hamiltonian(data.n_modes)
    expected_pair_q_comm = (
        2 * data.adag[0] * data.adag[1] - 2 * data.a[1] * data.a[0]
    )
    pair_ok = (
        matrix_equal(pair_from_car, pair_direct)
        and matrix_equal(pair_from_car.H, pair_from_car)
        and matrix_zero(commutator(pair_from_car, data.f_product))
        and matrix_equal(
            commutator(data.q_total, pair_from_car),
            expected_pair_q_comm,
        )
        and not matrix_zero(commutator(pair_from_car, data.q_total))
    )
    checks.record(
        "exact pair Hamiltonian preserves parity but not number",
        pair_ok,
        "H_pair=|00><11|+|11><00| and [Q,H_pair]=2create-2annihilate",
    )

    q_commuting_units = {
        (row, column)
        for row in range(dimension)
        for column in range(dimension)
        if data.q_values[row] == data.q_values[column]
    }
    f_commuting_units = {
        (row, column)
        for row in range(dimension)
        for column in range(dimension)
        if data.parity_values[row] == data.parity_values[column]
    }
    checks.record(
        "[H,Q]=0 implies [H,F]=0 for the full matrix-unit basis",
        q_commuting_units <= f_commuting_units,
        f"number support={len(q_commuting_units)}, parity support={len(f_commuting_units)}",
    )

    one_mode = build_jordan_wigner(1)
    one_mode_support_equal = {
        (row, column)
        for row in range(2)
        for column in range(2)
        if one_mode.q_values[row] == one_mode.q_values[column]
    } == {
        (row, column)
        for row in range(2)
        for column in range(2)
        if one_mode.parity_values[row] == one_mode.parity_values[column]
    }
    checks.record(
        "N=1 has F=I-2Q and equal commutants",
        matrix_equal(one_mode.f_product, one_mode.identity - 2 * one_mode.q_total)
        and one_mode_support_equal,
        "the two eigenspace decompositions coincide",
    )

    generic_symbols = sp.symbols("h0:16")
    generic_h = sp.Matrix(4, 4, generic_symbols)
    two_mode = build_jordan_wigner(2)
    two_even = (two_mode.identity + two_mode.f_product) / 2
    two_odd = (two_mode.identity - two_mode.f_product) / 2
    block_identity = matrix_equal(
        commutator(generic_h, two_mode.f_product),
        2 * (two_odd * generic_h * two_even - two_even * generic_h * two_odd),
    )
    matrix_unit_iff = all(
        matrix_zero(
            commutator(matrix_unit(4, row, column), two_mode.f_product)
        )
        == (
            matrix_zero(two_even * matrix_unit(4, row, column) * two_odd)
            and matrix_zero(two_odd * matrix_unit(4, row, column) * two_even)
        )
        for row in range(4)
        for column in range(4)
    )
    checks.record(
        "[H,F]=0 iff parity-mixing blocks vanish",
        block_identity and matrix_unit_iff,
        "generic block identity plus a complete matrix-unit basis check",
    )

    h_good = data.q_total + pair_from_car
    h_bad = data.a[0] + data.adag[0]
    dynamics_boundary = (
        matrix_equal(h_good.H, h_good)
        and matrix_zero(sp.I * commutator(h_good, data.f_product))
        and matrix_equal(h_bad.H, h_bad)
        and not matrix_zero(sp.I * commutator(h_bad, data.f_product))
    )
    checks.record(
        "Heisenberg derivative i[H,F] detects parity conservation",
        dynamics_boundary,
        "self-adjoint parity-even and parity-odd Hamiltonians separate exactly",
    )

    q_commutant_dimension = sum(sp.binomial(data.n_modes, charge) ** 2 for charge in range(data.n_modes + 1))
    f_commutant_dimension = 2 ** (2 * data.n_modes - 1)
    checks.record(
        "number commutant is strictly smaller than parity commutant for N=3",
        q_commutant_dimension == len(q_commuting_units)
        and f_commutant_dimension == len(f_commuting_units)
        and q_commutant_dimension < f_commutant_dimension,
        f"dimensions=({q_commutant_dimension},{f_commutant_dimension})",
    )

    return checks.finish()


def run_independent() -> int:
    checks = Checks()
    print("ORDERED FINITE-MODE FERMION PARITY — INDEPENDENT SECTOR MODE")
    summaries: list[tuple[int, int, int, int, int]] = []
    subset_all = True
    strict_all = True

    for n_modes in range(1, 7):
        charges = tuple(
            sum(occupation_tuple(index, n_modes)) for index in range(2**n_modes)
        )
        parities = tuple((-1) ** charge for charge in charges)
        even_dimension = parities.count(1)
        odd_dimension = parities.count(-1)
        q_support = {
            (row, column)
            for row in range(2**n_modes)
            for column in range(2**n_modes)
            if charges[row] == charges[column]
        }
        f_support = {
            (row, column)
            for row in range(2**n_modes)
            for column in range(2**n_modes)
            if parities[row] == parities[column]
        }
        subset_all = subset_all and q_support <= f_support
        if n_modes >= 2:
            strict_all = strict_all and q_support < f_support
        summaries.append(
            (n_modes, even_dimension, odd_dimension, len(q_support), len(f_support))
        )

    checks.record(
        "basis-bit flip independently balances the parity sectors",
        all(even == odd == 2 ** (n_modes - 1) for n_modes, even, odd, _, _ in summaries),
        f"summaries={summaries}",
    )
    checks.record(
        "Q-commuting support is contained in F-commuting support",
        subset_all,
        "classified every matrix unit for N=1..6",
    )
    checks.record(
        "the support inclusion is strict for every N>=2 tested",
        strict_all,
        "a same-parity/different-number matrix unit always exists",
    )

    q_dimension_formula = all(
        q_dimension == sp.binomial(2 * n_modes, n_modes)
        for n_modes, _, _, q_dimension, _ in summaries
    )
    f_dimension_formula = all(
        f_dimension == 2 ** (2 * n_modes - 1)
        for n_modes, _, _, _, f_dimension in summaries
    )
    checks.record(
        "independent commutant dimensions match closed formulas",
        q_dimension_formula and f_dimension_formula,
        "dim{Q}'=binomial(2N,N), dim{F}'=2^(2N-1)",
    )

    q_two = sp.diag(0, 1, 1, 2)
    f_two = sp.diag(1, -1, -1, 1)
    pair = sp.zeros(4)
    pair[0, 3] = 1
    pair[3, 0] = 1
    checks.record(
        "occupation-basis counterexample is exact and self-adjoint",
        matrix_equal(pair.H, pair)
        and matrix_zero(commutator(pair, f_two))
        and not matrix_zero(commutator(pair, q_two)),
        "direct |00><11|+|11><00| construction; no Jordan-Wigner identities used",
    )

    odd_change = sp.zeros(4)
    odd_change[0, 1] = 1
    odd_change[1, 0] = 1
    checks.record(
        "odd number change fails the parity-conservation criterion",
        matrix_equal(odd_change.H, odd_change)
        and not matrix_zero(commutator(odd_change, f_two)),
        "direct Q=0<->Q=1 transition mixes parity blocks",
    )

    q_one = sp.diag(0, 1)
    f_one = sp.diag(1, -1)
    checks.record(
        "independent N=1 classification gives equivalent commutators",
        all(
            matrix_zero(commutator(matrix_unit(2, row, column), q_one))
            == matrix_zero(commutator(matrix_unit(2, row, column), f_one))
            for row in range(2)
            for column in range(2)
        ),
        "complete two-by-two matrix-unit classification",
    )
    return checks.finish()


def hostile_survivals() -> dict[str, bool]:
    data = build_jordan_wigner(3)
    pair = data.adag[0] * data.adag[1] + data.a[1] * data.a[0]
    odd_hamiltonian = data.a[0] + data.adag[0]
    bare_zero = at_site(data.lower, 0, data.n_modes)
    bare_one = at_site(data.lower, 1, data.n_modes)
    wrong_pair = data.adag[0] * data.adag[1] + data.a[0] * data.a[1]

    parity_antecedent = matrix_zero(commutator(pair, data.f_product))
    number_conclusion = matrix_zero(commutator(pair, data.q_total))
    false_converse_survives = (not parity_antecedent) or number_conclusion

    return {
        "false-converse": false_converse_survives,
        "odd-number-change": (
            not matrix_zero(commutator(odd_hamiltonian, data.q_total))
            and matrix_zero(commutator(odd_hamiltonian, data.f_product))
        ),
        "wrong-product-phase": matrix_equal(-data.f_product, data.f_exponential),
        "bare-local-car": matrix_zero(anticommutator(bare_zero, bare_one)),
        "wrong-sector-dimension": data.parity_values.count(1) == 2 ** (data.n_modes - 1) + 1,
        "even-means-number-conserving": matrix_zero(commutator(pair, data.q_total)),
        "wrong-pair-order": matrix_equal(wrong_pair.H, wrong_pair),
    }


def selected_fixtures(fixture: str) -> tuple[str, ...]:
    return FIXTURES if fixture == "all" else (fixture,)


def run_hostile(fixture: str) -> int:
    checks = Checks()
    survivals = hostile_survivals()
    print("ORDERED FINITE-MODE FERMION PARITY — HOSTILE MUTATION MODE")
    print("Each PASS means exact object-level evidence rejected the mutation.")
    for name in selected_fixtures(fixture):
        checks.record(
            f"reject hostile fixture {name}",
            not survivals[name],
            f"mutated claim survives={survivals[name]}",
        )
    return checks.finish()


def run_intentional_failure(fixture: str) -> int:
    checks = Checks()
    survivals = hostile_survivals()
    print("ORDERED FINITE-MODE FERMION PARITY — INTENTIONAL FAILURE MODE")
    print("Selected hostile claims are promoted; every installed fixture must fail.")
    for name in selected_fixtures(fixture):
        checks.record(
            f"promoted hostile claim {name}",
            survivals[name],
            "intentional failure: mutation installed as the theorem conclusion",
        )
    return checks.finish()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile", "intentional-failure"),
        help="evidence mode (default: normal)",
    )
    aliases = parser.add_mutually_exclusive_group()
    aliases.add_argument("--independent", action="store_const", const="independent", dest="alias_mode")
    aliases.add_argument("--hostile", action="store_const", const="hostile", dest="alias_mode")
    aliases.add_argument(
        "--intentional-failure",
        action="store_const",
        const="intentional-failure",
        dest="alias_mode",
    )
    parser.add_argument(
        "--fixture",
        choices=("all",) + FIXTURES,
        default="all",
        help="hostile fixture selector (hostile/intentional-failure modes only)",
    )
    args = parser.parse_args()
    if args.mode and args.alias_mode:
        parser.error("use either --mode or a mode alias, not both")
    args.mode = args.mode or args.alias_mode or "normal"
    if args.mode not in {"hostile", "intentional-failure"} and args.fixture != "all":
        parser.error("--fixture is valid only in hostile or intentional-failure mode")
    return args


def main() -> int:
    args = parse_args()
    if args.mode == "normal":
        return run_normal()
    if args.mode == "independent":
        return run_independent()
    if args.mode == "hostile":
        return run_hostile(args.fixture)
    return run_intentional_failure(args.fixture)


if __name__ == "__main__":
    raise SystemExit(main())
