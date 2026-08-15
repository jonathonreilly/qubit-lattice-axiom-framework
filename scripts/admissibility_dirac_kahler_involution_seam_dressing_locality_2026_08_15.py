#!/usr/bin/env python3
"""Block 108: exact involution and seam-dressing locality obstruction.

The left-placement convention for a reflection dressing is fixed by embedding
the exact Block 107 central repair.  On the displayed antiperiodic reflection
torus, exact symbolic and rational calculations then reduce involutivity to
``A**2 = I`` and prove that every dressing supported on the four-slice seam
window leaves a non-decaying far-block Hermiticity defect untouched.  This is
a bounded seam-local emptiness theorem, not a curved OS no-go or a completion
of the globally supported ADM/history transporter.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_adm_seam_two_history_gram_"
    "2026_08_15.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_adm_seam_two_history_gram_"
    "2026_08_15.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_INVOLUTION_SEAM_DRESSING_LOCALITY_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_adm_seam_two_history_gram_2026_08_15.py",
    "logs/runner-cache/admissibility_dirac_kahler_adm_seam_two_history_gram_2026_08_15.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "5f081b997f5eb682082a373e9c49a944bf80e14e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block107-adm-seam-two-history-gram-20260815"
)
PARENT_COMMIT = "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"
PARENT_NOTE_BLOB = "cefc3be28430a9069ef572eb992f2605e58fccd5"
PARENT_RUNNER_BLOB = "1c156cb2970417dae67a69686a4cb07d4fac0998"
PARENT_CACHE_BLOB = "daa8a4c86c02b392ecaa41f9d9027231976ce3dd"
ANCESTOR_106 = "22d6d90ec2279e5868c9c825149b2a20beea3797"
ANCESTOR_105 = "d06066c2b908aaca0779625d831dfb10620cf34d"
ANCESTOR_104 = "7fe07db6c03fad1191893c942f708c5cb9a54c43"
ANCESTOR_103 = "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 190 else detail[:187] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_parent = (
        "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    )
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        "ancestor_106": is_ancestor(ANCESTOR_106, "HEAD"),
        "ancestor_105": is_ancestor(ANCESTOR_105, "HEAD"),
        "ancestor_104": is_ancestor(ANCESTOR_104, "HEAD"),
        "ancestor_103": is_ancestor(ANCESTOR_103, "HEAD"),
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


I = sp.I
LX = 4
TT = 4
SIZE = 2 * TT * LX
WINDOW_TIMES = (-2, -1, 0, 1)
POSITIVE_TIMES = (0, 1, 2, 3)
OFFSETS = ((0, 0), (0, 1), (1, 0), (1, 1))


def parity(integer: int) -> sp.Integer:
    """Return the staggered sign without exponentiation at negative sites."""
    return sp.Integer(-1 if integer % 2 else 1)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    if left.shape != right.shape:
        return False
    return all(sp.expand(entry) == 0 for entry in left - right)


def exact_rank(matrix: sp.Matrix) -> int:
    """Rank over the exact domain selected from an exact SymPy matrix."""
    return DomainMatrix.from_Matrix(matrix).rank()


def max_abs_entry(matrix: sp.Matrix) -> sp.Expr:
    values = [sp.simplify(sp.Abs(entry)) for entry in matrix]
    return max(values, default=sp.Integer(0))


def h_site(shear: sp.Expr, volume: sp.Expr) -> sp.Matrix:
    metric = sp.Matrix([[1, shear], [shear, 1]])
    return sp.diag(volume, volume * metric.inv(), 1 / volume)


def torus_objects(
    mass: sp.Expr,
    field_c: dict[int, sp.Expr],
    volume: sp.Expr,
    half_time: int,
    boundary_sign: int,
    spatial_extent: int = LX,
) -> tuple[sp.Matrix, sp.Matrix, object]:
    """Build exact Q, P, and the site map on the reflection torus."""
    size = 2 * half_time * spatial_extent

    def site_index(time_value: int, space: int) -> int:
        return ((time_value + half_time) % (2 * half_time)) * spatial_extent + (
            space % spatial_extent
        )

    def temporal_hop_sign(target_time_raw: int) -> sp.Integer:
        return sp.Integer(
            boundary_sign
            if target_time_raw >= half_time or target_time_raw < -half_time
            else 1
        )

    staggered = sp.zeros(size, size)
    for time_value in range(-half_time, half_time):
        for space in range(spatial_extent):
            index = site_index(time_value, space)
            staggered[index, index] += mass
            staggered[index, site_index(time_value + 1, space)] += (
                sp.Rational(1, 2) * temporal_hop_sign(time_value + 1)
            )
            staggered[index, site_index(time_value - 1, space)] += (
                -sp.Rational(1, 2) * temporal_hop_sign(time_value - 1)
            )
            staggered[index, site_index(time_value, space + 1)] += (
                parity(time_value) * sp.Rational(1, 2)
            )
            staggered[index, site_index(time_value, space - 1)] += (
                -parity(time_value) * sp.Rational(1, 2)
            )

    degrees = {
        site_index(time_value, space): (time_value % 2) + (space % 2)
        for time_value in range(-half_time, half_time)
        for space in range(spatial_extent)
    }
    kernel = staggered - mass * sp.eye(size)
    raising_kernel = sp.zeros(size, size)
    for row in range(size):
        for column in range(size):
            if kernel[row, column] != 0 and degrees[row] == degrees[column] + 1:
                raising_kernel[row, column] = kernel[row, column]
    differential = -I * raising_kernel

    hodge = sp.zeros(size, size)
    for anchor_time in range(-half_time, half_time):
        for anchor_space in range(spatial_extent):
            block = h_site(field_c[anchor_time], volume)
            for row_offset, (row_time, row_space) in enumerate(OFFSETS):
                for column_offset, (column_time, column_space) in enumerate(OFFSETS):
                    if block[row_offset, column_offset] == 0:
                        continue
                    hodge[
                        site_index(anchor_time + row_time, anchor_space + row_space),
                        site_index(
                            anchor_time + column_time, anchor_space + column_space
                        ),
                    ] += block[row_offset, column_offset] / 4

    operator = mass * hodge + I * (
        hodge * differential + differential.H * hodge
    )
    reflection = sp.zeros(size, size)
    for time_value in range(-half_time, half_time):
        for space in range(spatial_extent):
            reflection[
                site_index(-1 - time_value, space), site_index(time_value, space)
            ] = 1
    return operator, reflection, site_index


def step_profile(half_time: int, shear: sp.Expr) -> dict[int, sp.Expr]:
    return {
        time_value: (
            sp.Integer(0)
            if time_value in (-1, half_time - 1)
            else (shear if time_value >= 0 else -shear)
        )
        for time_value in range(-half_time, half_time)
    }


def spatial_factors() -> tuple[sp.Matrix, ...]:
    cyclic_shift = sp.zeros(LX, LX)
    for space in range(LX):
        cyclic_shift[(space + 1) % LX, space] = 1
    return (
        sp.eye(LX),
        sp.diag(*(parity(space) for space in range(LX))),
        cyclic_shift + cyclic_shift.T,
        cyclic_shift - cyclic_shift.T,
    )


# Exact Block 107 Stage-H certificate, in factor/block/real-imag order.
DRESSING_CERTIFICATE_PARAMS = (
    sp.Integer(507968644026955530085904130509337010540515817873788319311345515383612296029720079811810132653552),
    sp.Integer(41532452335260334034957746615889889690141434198992020757127483010426721818108364308425298585240),
    sp.Integer(41385182270195709174736265631465163934297334634942112413026201220858061429793417133170586290840),
    sp.Integer(-99516981857048688256249971796779510257767571680017059012842643361723281883552835866630003281646),
    sp.Integer(1833417318393208695828568805895558222747355122178331594308500486778470789047226029468070931680),
    sp.Integer(49534066411967129048632336601892334125920831929632587776519163897056228339957906900848719808600),
    sp.Integer(583767067596676525810620669726200150411964788957764188321891010476389121880969423915023775555800),
    sp.Integer(-46762561091094320816555106519491637698970558945336688478301137068354391186814368133036915388440),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(0),
    sp.Integer(-92960679527218549712063123648860240924804580124293876596738494826013816450206947628786021433420),
    sp.Integer(-6569810041034990666397887436556810085064577129273936941551768108135948329034687859174023071605),
    sp.Integer(133516288783768367469283644911877346264106372353413436532524148686263056273769626431868334990822),
    sp.Integer(26742410356895126745535006571044757690289091385775689900022386467043627087667933340911979773690),
    sp.Integer(1141840098923108606599239406887185095350960538229366092543131324331321934064787023154467642900),
    sp.Integer(-10543458475696290351592926717261960542828614152490703288304052005311823243958105442678533563450),
    sp.Integer(-7927787670195359755557189516226228108576859033834767431124876154442883641974756457673417862700),
    sp.Integer(11674104500194566881743916578595078230869856330134760975432605685370682360799228233700344384600),
    sp.Integer(12777217829042196308049921249039261245126781699759011073564588287232440929641832936058662863900),
    sp.Integer(51641136209626860803571044139848886376972040538507485453284935047479173999665019715384101841455),
    sp.Integer(-1513412767693811407321557218629570743956855060170988787741252444125600093131000377482643574200),
    sp.Integer(-40650934460081410399681180537301940677600066415371305320275889098941410910127407570312503495600),
    sp.Integer(13715642233382803381407015868476235218978164944954642113991959874450106937210517757938581639300),
    sp.Integer(-439377900298203311803032740892456022439086952952867712570041032165496801231580754753025553800),
    sp.Integer(13626139327766502706780472161998142325518350936019798691061025590120098329552232789377780137600),
    sp.Integer(11486206220758586577073108998021921327342797813304905942803233155684437982813237631969526051500),
)


def block107_dressing(corrupt: bool = False) -> sp.Matrix:
    parameters = list(DRESSING_CERTIFICATE_PARAMS)
    if corrupt:
        parameters[0] += 1
    dressing = sp.zeros(8, 8)
    offset = 0
    for factor in spatial_factors():
        block = sp.Matrix(
            2,
            2,
            lambda row, column: parameters[offset + 2 * (2 * row + column)]
            + I * parameters[offset + 2 * (2 * row + column) + 1],
        )
        offset += 8
        dressing += sp.Matrix(
            8,
            8,
            lambda row, column: block[row // 4, column // 4]
            * factor[row % 4, column % 4],
        )
    return dressing


def window_basis() -> tuple[list[sp.Matrix], list[tuple[int, int, int, str]]]:
    """The 128-real-parameter complex W4 ansatz from the solve construction."""
    basis: list[sp.Matrix] = []
    labels: list[tuple[int, int, int, str]] = []
    for slice_i in range(4):
        for slice_j in range(4):
            for factor_index, factor in enumerate(spatial_factors()):
                for part, scalar in (("re", sp.Integer(1)), ("im", I)):
                    item = sp.zeros(16, 16)
                    item[
                        4 * slice_i : 4 * (slice_i + 1),
                        4 * slice_j : 4 * (slice_j + 1),
                    ] = scalar * factor
                    basis.append(item)
                    labels.append((slice_i, slice_j, factor_index, part))
    return basis, labels


def window_reflection() -> sp.Matrix:
    reflection = sp.zeros(16, 16)
    for slice_index in range(4):
        for space in range(LX):
            reflection[4 * (3 - slice_index) + space, 4 * slice_index + space] = 1
    return reflection


def reality_coefficient_matrix() -> sp.Matrix:
    """Linear equations for J*conjugate(A)*J=A in all 128 coordinates."""

    def parameter_index(
        slice_i: int, slice_j: int, factor_index: int, imaginary: int
    ) -> int:
        return 2 * (4 * (4 * slice_i + slice_j) + factor_index) + imaginary

    rows: list[list[int]] = []
    for slice_i in range(4):
        for slice_j in range(4):
            reflected_i, reflected_j = 3 - slice_i, 3 - slice_j
            for factor_index in range(4):
                real_row = [0] * 128
                imag_row = [0] * 128
                real_row[parameter_index(slice_i, slice_j, factor_index, 0)] += 1
                real_row[
                    parameter_index(reflected_i, reflected_j, factor_index, 0)
                ] -= 1
                imag_row[parameter_index(slice_i, slice_j, factor_index, 1)] += 1
                imag_row[
                    parameter_index(reflected_i, reflected_j, factor_index, 1)
                ] += 1
                rows.extend((real_row, imag_row))
    return sp.Matrix(rows)


def reality_parametrization(mutation: str) -> dict[str, object]:
    """Build A=B+J*conjugate(B)*J over 64 free real parameters."""
    parameters = sp.symbols("b0:64", real=True)
    parameter_index = 0
    seen: set[tuple[int, int]] = set()
    free_half = sp.zeros(16, 16)
    for slice_i in range(4):
        for slice_j in range(4):
            pair = (3 - slice_i, 3 - slice_j)
            if (slice_i, slice_j) in seen:
                continue
            seen.add((slice_i, slice_j))
            seen.add(pair)
            for factor in spatial_factors():
                for scalar in (sp.Integer(1), I):
                    free_half[
                        4 * slice_i : 4 * (slice_i + 1),
                        4 * slice_j : 4 * (slice_j + 1),
                    ] += parameters[parameter_index] * scalar * factor
                    parameter_index += 1
    reflection = window_reflection()
    parametrized = (
        free_half
        if mutation == "break_reality_parametrization"
        else free_half + reflection * free_half.conjugate() * reflection
    )
    reflected = reflection * parametrized.conjugate() * reflection
    left_square = sp.expand(parametrized * reflected)
    right_square = (
        sp.expand(parametrized * parametrized.conjugate())
        if mutation == "break_involution_identity"
        else sp.expand(parametrized * parametrized)
    )
    original_basis, _ = window_basis()
    return {
        "original_parameter_count": len(original_basis),
        "free_parameter_count": len(parameters),
        "free_parameters_used": parameter_index,
        "reality": matrix_equal(reflected, parametrized),
        "operator_identity": matrix_equal(left_square, right_square),
    }


@dataclass(frozen=True)
class Fixture:
    shear: sp.Rational
    propagator: sp.Matrix
    reflection: sp.Matrix
    site_index: object
    window: tuple[int, ...]
    positive: tuple[int, ...]
    reflected: tuple[int, ...]
    raw_gram: sp.Matrix


def history_gram(
    propagator: sp.Matrix,
    positive: tuple[int, ...] | list[int],
    reflected: tuple[int, ...] | list[int],
) -> sp.Matrix:
    return sp.Matrix(
        len(positive),
        len(reflected),
        lambda row, column: sp.conjugate(
            propagator[positive[row], reflected[column]]
        ),
    )


def fixture_data(shear: sp.Rational) -> Fixture:
    operator, reflection, site_index = torus_objects(
        sp.Rational(9, 20),
        step_profile(TT, shear),
        sp.Integer(1),
        TT,
        -1,
    )
    propagator = operator.inv(method="DM")
    window = tuple(
        site_index(time_value, space)
        for time_value in WINDOW_TIMES
        for space in range(LX)
    )
    positive = tuple(
        site_index(time_value, space)
        for time_value in POSITIVE_TIMES
        for space in range(LX)
    )
    reflected = tuple(
        site_index(-1 - time_value, space)
        for time_value in POSITIVE_TIMES
        for space in range(LX)
    )
    raw_gram = history_gram(propagator, positive, reflected)
    return Fixture(
        shear,
        propagator,
        reflection,
        site_index,
        window,
        positive,
        reflected,
        raw_gram,
    )


def central_extension(block: sp.Matrix, fixture: Fixture) -> sp.Matrix:
    """Identity off slices {0,1}, with ``block`` on their 8x8 restriction."""
    extension = sp.eye(SIZE)
    central = fixture.positive[:8]
    for row, full_row in enumerate(central):
        for column, full_column in enumerate(central):
            extension[full_row, full_column] = block[row, column]
    return extension


def convention_certificate(fixture: Fixture, mutation: str) -> dict[str, object]:
    raw_central = history_gram(
        fixture.propagator, fixture.positive[:8], fixture.reflected[:8]
    )
    canonical_dressing = block107_dressing()
    transcribed_dressing = block107_dressing(
        corrupt=mutation == "break_certificate_transcription"
    )
    extension = central_extension(transcribed_dressing.conjugate(), fixture)
    left_placement = history_gram(
        extension * fixture.propagator,
        fixture.positive[:8],
        fixture.reflected[:8],
    )
    transpose_placement = history_gram(
        fixture.propagator * extension,
        fixture.positive[:8],
        fixture.reflected[:8],
    )
    target = canonical_dressing * raw_central
    selected = (
        transpose_placement
        if mutation == "flip_dressing_placement"
        else left_placement
    )

    canonical_extension = central_extension(canonical_dressing.conjugate(), fixture)
    canonical_embedding = history_gram(
        canonical_extension * fixture.propagator,
        fixture.positive[:8],
        fixture.reflected[:8],
    )
    return {
        "raw_central": raw_central,
        "target": target,
        "selected_matches": matrix_equal(selected, target),
        "transpose_invisible": matrix_equal(transpose_placement, raw_central),
        "target_nontrivial": not matrix_equal(target, raw_central),
        "canonical_embedding": canonical_embedding,
        "canonical_embedding_matches": matrix_equal(canonical_embedding, target),
    }


@dataclass(frozen=True)
class HermiticityLabel:
    row: int
    column: int
    part: str


def real_imaginary(value: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    real_part, imaginary_part = sp.expand_complex(value).as_real_imag()
    return sp.expand(real_part), sp.expand(imaginary_part)


def independent_hermiticity_values(
    matrix: sp.Matrix,
) -> tuple[list[HermiticityLabel], list[sp.Expr]]:
    """Return the 16^2 independent real equations for matrix=matrix.H."""
    labels: list[HermiticityLabel] = []
    values: list[sp.Expr] = []
    for row in range(matrix.rows):
        _, diagonal_imaginary = real_imaginary(matrix[row, row])
        labels.append(HermiticityLabel(row, row, "im"))
        values.append(diagonal_imaginary)
        for column in range(row + 1, matrix.cols):
            difference = sp.expand(
                matrix[row, column] - sp.conjugate(matrix[column, row])
            )
            real_part, imaginary_part = real_imaginary(difference)
            labels.extend(
                (
                    HermiticityLabel(row, column, "re"),
                    HermiticityLabel(row, column, "im"),
                )
            )
            values.extend((real_part, imaginary_part))
    return labels, values


@dataclass(frozen=True)
class HermiticitySystem:
    constant_gram: sp.Matrix
    gram_basis: tuple[sp.Matrix, ...]
    labels: tuple[HermiticityLabel, ...]
    constant_values: tuple[sp.Expr, ...]
    coefficients: sp.Matrix
    right_hand_side: sp.Matrix


def affine_hermiticity_system(
    fixture: Fixture, basis: list[sp.Matrix]
) -> HermiticitySystem:
    """K_A=conjugate((A_ext*G)[S4,P S4]), identity off W4."""
    constant = sp.zeros(16, 16)
    for row in range(8, 16):
        for column in range(16):
            constant[row, column] = fixture.raw_gram[row, column]

    window_to_reflected = fixture.propagator.extract(
        fixture.window, fixture.reflected
    )
    gram_basis: list[sp.Matrix] = []
    basis_values: list[list[sp.Expr]] = []
    labels: list[HermiticityLabel] | None = None
    for item in basis:
        active_rows = item.extract(range(8, 16), range(16))
        top = (active_rows * window_to_reflected).conjugate()
        gram_item = top.col_join(sp.zeros(8, 16))
        item_labels, item_values = independent_hermiticity_values(gram_item)
        if labels is None:
            labels = item_labels
        gram_basis.append(gram_item)
        basis_values.append(item_values)

    constant_labels, constant_values = independent_hermiticity_values(constant)
    assert labels == constant_labels
    coefficients = sp.Matrix(
        len(constant_values),
        len(basis_values),
        lambda row, column: sp.cancel(basis_values[column][row]),
    )
    right_hand_side = sp.Matrix([-sp.cancel(value) for value in constant_values])
    return HermiticitySystem(
        constant,
        tuple(gram_basis),
        tuple(constant_labels),
        tuple(constant_values),
        coefficients,
        right_hand_side,
    )


def identity_window_coordinates() -> sp.Matrix:
    coordinates = sp.zeros(128, 1)
    for slice_index in range(4):
        index = 2 * (4 * (4 * slice_index + slice_index))
        coordinates[index] = 1
    return coordinates


def parameter_free_obstruction_rows(system: HermiticitySystem) -> list[int]:
    zero_row = sp.zeros(1, system.coefficients.cols)
    return [
        row
        for row in range(system.coefficients.rows)
        if matrix_equal(system.coefficients[row, :], zero_row)
        and system.right_hand_side[row] != 0
    ]


def structural_far_row_certificate(
    fixture: Fixture, system: HermiticitySystem
) -> dict[str, object]:
    coefficient_submatrix = sp.Matrix(
        8 * 16,
        128,
        lambda entry, parameter: system.gram_basis[parameter][
            8 + entry // 16, entry % 16
        ],
    )
    embedding = sp.zeros(SIZE, 16)
    for local, full in enumerate(fixture.window):
        embedding[full, local] = 1
    far_selector = sp.zeros(8, SIZE)
    for local, full in enumerate(fixture.positive[8:16]):
        far_selector[local, full] = 1
    support_incidence = far_selector * embedding
    return {
        "ansatz_coefficient_submatrix_zero": matrix_equal(
            coefficient_submatrix, sp.zeros(8 * 16, 128)
        ),
        "arbitrary_support_incidence_zero": matrix_equal(
            support_incidence, sp.zeros(8, 16)
        ),
    }


def homogeneous_and_flat_structure(
    basis: list[sp.Matrix],
    reality: sp.Matrix,
    primary: HermiticitySystem,
    flat: HermiticitySystem,
    mutation: str,
) -> dict[str, object]:
    primary_joint = reality.col_join(primary.coefficients)
    primary_rank = exact_rank(primary_joint)
    primary_dimension = len(basis) - primary_rank

    flat_joint = reality.col_join(flat.coefficients)
    flat_right_hand_side = sp.zeros(reality.rows, 1).col_join(
        flat.right_hand_side
    )
    flat_rank = exact_rank(flat_joint)
    flat_augmented_rank = exact_rank(flat_joint.row_join(flat_right_hand_side))
    flat_dimension = len(basis) - flat_rank

    identity_coordinates = identity_window_coordinates()
    reconstructed_identity = sp.zeros(16, 16)
    for coordinate, item in zip(identity_coordinates, basis, strict=True):
        if coordinate != 0:
            reconstructed_identity += coordinate * item
    identity_membership = matrix_equal(
        flat_joint * identity_coordinates, flat_right_hand_side
    )
    asserted_identity_membership = (
        False if mutation == "drop_flat_identity_membership" else identity_membership
    )
    expected_primary_dimension = (
        6 if mutation == "claim_homogeneous_dim_wrong" else 4
    )
    homogeneous_outside_rows_zero = all(
        item[row, column] == 0
        for item in primary.gram_basis
        for row in range(8, 16)
        for column in range(16)
    )
    return {
        "parameter_count": len(basis),
        "reality_rank": exact_rank(reality),
        "primary_rank": primary_rank,
        "primary_dimension": primary_dimension,
        "expected_primary_dimension": expected_primary_dimension,
        "homogeneous_outside_rows_zero": homogeneous_outside_rows_zero,
        "flat_rank": flat_rank,
        "flat_augmented_rank": flat_augmented_rank,
        "flat_dimension": flat_dimension,
        "identity_reconstructed": matrix_equal(reconstructed_identity, sp.eye(16)),
        "identity_membership": asserted_identity_membership,
    }


def seam_local_emptiness(
    fixture: Fixture, system: HermiticitySystem, mutation: str
) -> dict[str, object]:
    obstruction_rows = parameter_free_obstruction_rows(system)
    labels = [system.labels[row] for row in obstruction_rows]
    coefficient_rank = exact_rank(system.coefficients)
    augmented_rank = exact_rank(
        system.coefficients.row_join(system.right_hand_side)
    )
    structural = structural_far_row_certificate(fixture, system)
    general_support_zero = structural["arbitrary_support_incidence_zero"]
    if mutation == "narrow_certificate_to_ansatz":
        general_support_zero = False
    return {
        "obstruction_count": len(obstruction_rows),
        "expected_obstruction_count": (
            0 if mutation == "claim_seam_local_feasible" else 24
        ),
        "all_obstructions_far": all(
            label.row >= 8 and label.column >= 8 for label in labels
        ),
        "coefficient_rank": coefficient_rank,
        "augmented_rank": augmented_rank,
        "expected_augmented_rank": 60 if mutation == "break_rank_gap" else 61,
        "ansatz_coefficient_submatrix_zero": structural[
            "ansatz_coefficient_submatrix_zero"
        ],
        "general_support_zero": general_support_zero,
    }


SECOND_FIXTURE_ENTRY = sp.Rational(
    -946372553273520360000, 274776247965351513030373
)


def second_fixture_certificate(
    fixture: Fixture, system: HermiticitySystem, mutation: str
) -> dict[str, object]:
    obstruction_rows = parameter_free_obstruction_rows(system)
    labels = [system.labels[row] for row in obstruction_rows]
    coefficient_rank = exact_rank(system.coefficients)
    augmented_rank = exact_rank(
        system.coefficients.row_join(system.right_hand_side)
    )
    far_defect = sp.factor(
        fixture.raw_gram[8, 9] - sp.conjugate(fixture.raw_gram[9, 8])
    )
    expected_entry = (
        SECOND_FIXTURE_ENTRY + 1
        if mutation == "mismatch_second_fixture"
        else SECOND_FIXTURE_ENTRY
    )
    return {
        "obstruction_count": len(obstruction_rows),
        "all_obstructions_far": all(
            label.row >= 8 and label.column >= 8 for label in labels
        ),
        "coefficient_rank": coefficient_rank,
        "augmented_rank": augmented_rank,
        "far_defect": far_defect,
        "expected_entry": expected_entry,
    }


def nondecay_certificate(fixture: Fixture, mutation: str) -> dict[str, object]:
    defect = fixture.raw_gram - fixture.raw_gram.H
    near = sp.factor(max_abs_entry(defect[:8, :8]))
    far = sp.factor(max_abs_entry(defect[8:16, 8:16]))
    cross = sp.factor(
        max(
            max_abs_entry(defect[:8, 8:16]),
            max_abs_entry(defect[8:16, :8]),
        )
    )
    central = history_gram(
        fixture.propagator, fixture.positive[:8], fixture.reflected[:8]
    )
    block107_value = sp.factor(max_abs_entry(central - central.H))
    claimed_ordering = (
        far < near
        if mutation == "claim_defect_decays"
        else far > near > cross > 0
    )
    return {
        "near": near,
        "far": far,
        "cross": cross,
        "block107_value": block107_value,
        "exact_fractions": all(
            value.is_rational is True for value in (near, far, cross)
        ),
        "ordering": claimed_ordering,
        "far_exceeds_near": far > near,
    }


def central_repair_context(fixture: Fixture, mutation: str) -> dict[str, object]:
    dressing = block107_dressing(corrupt=mutation == "break_central_repair")
    raw_central = history_gram(
        fixture.propagator, fixture.positive[:8], fixture.reflected[:8]
    )
    extension = central_extension(dressing.conjugate(), fixture)
    embedded = history_gram(
        extension * fixture.propagator,
        fixture.positive[:8],
        fixture.reflected[:8],
    )
    dressed = sp.expand(dressing * raw_central)
    equation = matrix_equal(
        sp.expand(dressing * raw_central),
        sp.expand(raw_central.H * dressing.H),
    )
    if equation:
        leading_minors = tuple(
            sp.factor(dressed[:size, :size].det(method="domain-ge"))
            for size in range(1, 9)
        )
        positive = all(bool(minor > 0) for minor in leading_minors)
    else:
        leading_minors = ()
        positive = False
    return {
        "embedding": matrix_equal(embedded, dressed),
        "equation": equation,
        "hermitian": matrix_equal(dressed, dressed.H),
        "leading_minor_count": len(leading_minors),
        "positive": positive,
    }


SCOPE_KEYS = (
    "involution_reduction",
    "seam_local_emptiness",
    "nondecay",
    "global_support",
    "modular_transfer",
    "curved_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity",
    "adm",
    "n1_n8",
    "walls",
    "n5_resolution",
)


def scope_certificate(mutation: str) -> dict[str, bool]:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return {key: False for key in SCOPE_KEYS}
    note = " ".join(raw_note.lower().split())
    result = {
        "involution_reduction": "involution reduction" in note,
        "seam_local_emptiness": (
            "seam-local emptiness" in note
            or "parameter-free obstruction rows" in note
        ),
        "nondecay": "does not decay" in note,
        "global_support": (
            "global support" in note or "globally supported dressing" in note
        ),
        "modular_transfer": "modular" in note or "transfer" in note,
        "curved_boundary": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": "retained-positive end-to-end theory count remains zero"
        in note,
        "gravity": "gravity constraint quotient remains unexecuted" in note,
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "walls": "w1" in note,
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
    }
    if mutation == "weaken_no_go_packet":
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_adm_link_derived":
        result["adm"] = False
    if mutation == "claim_curved_os_closed":
        result["curved_boundary"] = False
    if mutation == "claim_axiom_amendment":
        result["axiom"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    if mutation == "claim_obligation_retirement":
        result["zero_retirement"] = False
    return result


MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "flip_dressing_placement",
    "break_certificate_transcription",
    "break_reality_parametrization",
    "break_involution_identity",
    "claim_homogeneous_dim_wrong",
    "drop_flat_identity_membership",
    "claim_seam_local_feasible",
    "break_rank_gap",
    "narrow_certificate_to_ansatz",
    "mismatch_second_fixture",
    "claim_defect_decays",
    "break_central_repair",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_adm_link_derived",
    "claim_curved_os_closed",
    "claim_axiom_amendment",
    "claim_toe_progress",
    "claim_obligation_retirement",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority-and-Block107-parent",
        "current axioms, registries, ancestry, and the Block107 parent triple are content-bound",
        authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and authority["ancestor_106"]
        and authority["ancestor_105"]
        and authority["ancestor_104"]
        and authority["ancestor_103"]
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
        f"parent={authority['parent']}; origin/main={authority['main']}",
    )

    primary_fixture = fixture_data(sp.Rational(5, 13))
    convention = convention_certificate(primary_fixture, mutation)
    checks.check(
        "B-convention-and-block107-embedding",
        "left placement embeds Block107 R*K exactly while transpose placement is undressed",
        convention["selected_matches"]
        and convention["transpose_invisible"]
        and convention["target_nontrivial"],
        "K_A=conj((A_ext G)[pos,P pos]); G A_ext leaves the central Gram exactly unchanged",
    )

    involution = reality_parametrization(mutation)
    checks.check(
        "C-involution-reduction",
        "the 128-parameter reality ansatz has a free 64-parameter form and (A P conj)^2=A^2",
        involution["original_parameter_count"] == 128
        and involution["free_parameter_count"] == 64
        and involution["free_parameters_used"] == 64
        and involution["reality"]
        and involution["operator_identity"],
        "A=B+P conj(B) P is checked entrywise symbolically; theta'^2=1 iff A^2=I",
    )

    basis, _ = window_basis()
    reality = reality_coefficient_matrix()
    primary_system = affine_hermiticity_system(primary_fixture, basis)
    flat_fixture = fixture_data(sp.Rational(0))
    flat_system = affine_hermiticity_system(flat_fixture, basis)
    structure = homogeneous_and_flat_structure(
        basis, reality, primary_system, flat_system, mutation
    )
    checks.check(
        "D-homogeneous-window-structure",
        "the homogeneous joint system has dimension four; the flat affine control has dimension ten and A=I",
        structure["parameter_count"] == 128
        and structure["reality_rank"] == 64
        and structure["primary_rank"] == 124
        and structure["primary_dimension"]
        == structure["expected_primary_dimension"]
        and structure["homogeneous_outside_rows_zero"]
        and structure["flat_rank"] == 118
        and structure["flat_augmented_rank"] == 118
        and structure["flat_dimension"] == 10
        and structure["identity_reconstructed"]
        and structure["identity_membership"],
        f"homogeneous rank/dim={structure['primary_rank']}/{structure['primary_dimension']}; flat rank/dim={structure['flat_rank']}/{structure['flat_dimension']}",
    )

    emptiness = seam_local_emptiness(primary_fixture, primary_system, mutation)
    checks.check(
        "E-seam-local-emptiness",
        "twenty-four parameter-free far-block rows make every W4-supported dressing exactly infeasible",
        emptiness["obstruction_count"] == emptiness["expected_obstruction_count"]
        and emptiness["all_obstructions_far"]
        and emptiness["coefficient_rank"] == 60
        and emptiness["augmented_rank"] == emptiness["expected_augmented_rank"]
        and emptiness["ansatz_coefficient_submatrix_zero"]
        and emptiness["general_support_zero"],
        f"obstruction rows={emptiness['obstruction_count']}; rank[M|b]={emptiness['coefficient_rank']}|{emptiness['augmented_rank']}; far rows equal undressed rows for any W4 support",
    )

    second_fixture = fixture_data(sp.Rational(3, 5))
    second_system = affine_hermiticity_system(second_fixture, basis)
    second = second_fixture_certificate(second_fixture, second_system, mutation)
    checks.check(
        "F-second-fixture",
        "the c=3/5 fixture has the same exact twenty-four-row rank obstruction and pinned witness",
        second["obstruction_count"] == 24
        and second["all_obstructions_far"]
        and second["coefficient_rank"] == 60
        and second["augmented_rank"] == 61
        and second["far_defect"] == second["expected_entry"],
        f"rank[M|b]={second['coefficient_rank']}|{second['augmented_rank']}; D[8,9]={second['far_defect']}",
    )

    nondecay = nondecay_certificate(primary_fixture, mutation)
    checks.check(
        "G-nondecay-of-the-obstruction",
        "the exact far defect exceeds the Block107 near defect, so the obstruction does not decay",
        nondecay["exact_fractions"]
        and nondecay["near"] == nondecay["block107_value"]
        and nondecay["ordering"]
        and nondecay["far_exceeds_near"],
        f"far > near > cross: {nondecay['far']} > {nondecay['near']} > {nondecay['cross']}",
    )
    print(
        "DEFECT_BLOCKS_EXACT: "
        f"near={nondecay['near']} far={nondecay['far']} cross={nondecay['cross']}"
    )

    central = central_repair_context(primary_fixture, mutation)
    checks.check(
        "H-central-repair-context",
        "the exact Block107 central positive repair stands, but no W4-supported extension exists",
        central["embedding"]
        and central["equation"]
        and central["hermitian"]
        and central["leading_minor_count"] == 8
        and central["positive"]
        and emptiness["obstruction_count"] == 24
        and emptiness["coefficient_rank"] < emptiness["augmented_rank"],
        "R107*K is Hermitian with eight positive leading minors; the central repair is essentially maximal for seam-local dressings",
    )

    scope = scope_certificate(mutation)
    checks.check(
        "I-scope",
        "the bounded note preserves involution, locality, N1--N8, W1, N5, ADM, gravity, audit, and TOE walls",
        all(scope.values()),
        "note scope is guarded against absence; no curved-OS, global transporter, or TOE completion is inferred",
    )

    print(
        f"AXIOM_AUTHORITY: origin/main={authority['main']} axiom={CURRENT_AXIOM_BLOB} registry={CURRENT_REGISTRY_BLOB}; Block107 parent={PARENT_COMMIT}"
    )
    print(
        "per_element: exact convention, involution-reduction, dimension, infeasibility, and non-decay identities are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: the Block 107 central certificate is embedded and re-verified exactly"
    )
    print(
        "per_block: twenty-four parameter-free far-block obstruction rows certify seam-local emptiness at both fixtures"
    )
    print(
        "lattice_wide: checked and not executed — the globally supported transfer/modular seam dressing, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the involution reduction and convention are exact and the two-history Hermiticity obstruction is global — every seam-local dressing class on the displayed window is exactly empty while the central-window repair stands"
    )
    print(
        "DECISION_CUT: advance the globally supported transfer/modular dressing as the only surviving seam mechanism; reject finite-window dressing routes"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
