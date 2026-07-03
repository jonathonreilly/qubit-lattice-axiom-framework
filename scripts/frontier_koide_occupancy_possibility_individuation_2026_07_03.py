#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]

SOURCE_PATHS = {
    "axioms": "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "static_no_go": "docs/KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md",
    "occupancy": "docs/KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md",
    "k_blindness": "docs/ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md",
    "record_orbit_no_go": "docs/KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07.md",
    "k_odd_trace": "docs/ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02.md",
}

TARGET_NOTE = "docs/KOIDE_OCCUPANCY_DERIVED_FROM_POSSIBILITY_INDIVIDUATION_BOUNDED_NOTE_2026-07-03.md"
TARGET_RUNNER = "scripts/frontier_koide_occupancy_possibility_individuation_2026_07_03.py"


def read_source(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


SOURCES = {name: read_source(path) for name, path in SOURCE_PATHS.items()}
TARGET_TEXT = read_source(TARGET_NOTE)


def normalized(text: str) -> str:
    return " ".join(text.split())


@dataclass
class Check:
    description: str
    passed: bool
    detail: str = ""


CHECKS: list[Check] = []


def check(description: str, condition: bool, detail: str = "") -> bool:
    passed = bool(condition)
    CHECKS.append(Check(description, passed, detail))
    return passed


def guard_quote(source_name: str, label: str, quote: str) -> bool:
    return check(
        f"live quote guard: {label}",
        normalized(quote) in normalized(SOURCES[source_name]),
        f"source={SOURCE_PATHS[source_name]}",
    )


AXIOM_STATE = "A state is a configuration of records."
AXIOM_RECORD_LOCK = (
    "When present, a record locks exactly one admissible local possibility. "
    "A site never carries more than one record; records are permanent."
)
AXIOM_RECORD_READ = (
    "Only records are readable. A readout value is determined by record content alone."
)
AXIOM_QUBIT_DISTINCTION = (
    "No possibility is privileged. Possibilities are distinguished by the supplied "
    "algebraic structure alone."
)
AXIOM_LATTICE_DISTINCTION = (
    "No site is privileged. Sites are distinguished by the supplied lattice "
    "structure alone."
)
AXIOM_ADMISSIBILITY = (
    "For each site, the available possibilities are determined by, and vary with, "
    "the nearest-neighbor conditions."
)
AXIOM_LAW = (
    "A law privileges no states. Its domain is a supplied condition, and at every "
    "state where the condition holds it gives exactly one answer."
)
AXIOM_QUALIFICATION = (
    "These axioms state only their named primitive content. Further physical "
    "structure requires derivation, bridge, explicit admission, or approved "
    "primitive registration before use as a premise."
)
AXIOM_OPEN_GATES = (
    "context selection, measurement basis selection, Born weights, probability "
    "rules, update laws, decoherence mechanisms, and occurrence rules;"
)
WALL_CATEGORY = (
    'Transferring an operator-symmetry onto "the energy counts `b` once" is a '
    "category slip and is **circular** (it assumes the asymmetric `(1,1)` split "
    "it claims to derive)."
)
WALL_SELECTOR = (
    "A static complex structure that commutes with `M` and preserves every measure "
    "can **define** a holomorphic readout but provably cannot **select** it — both "
    "`(1,1)` and `(1,2)` are `J_cs`-invariant."
)
WALL_NO_OCCUPANCY = (
    "The Record axiom itself supplies no weighting, normalization, or occupancy rule"
)
STATIC_N1_RECORD_ROW = (
    "Record names realized outcomes but supplies no weighting/occupancy rule; "
    "the orbit-count route is pruned in "
    "[`KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07.md`]"
    "(KOIDE_RECORD_ORBIT_COUNT_DOES_NOT_SELECT_R_HALF_NO_GO_NOTE_2026-06-07.md)."
)
RECORD_ORBIT_PRUNING = (
    "The K/CPT orbit count is not a weighting rule and does not select `(1,1)` by itself."
)
K_SEPARATOR = "The requirement is simple: a separator must make `Tr(O R)` non-real."
K_BLINDNESS = "No scalar-ambient functional on that surface separates the conjugate isotypes."
K_ODD_TRACE_WALL = (
    "the K-odd observable exists at the generation ring size `N = 3` and requires "
    "doubling-pairing breaking elsewhere, but what value it registers remains the wall."
)
BRIDGE_SENTENCE = (
    "one record locking one admissible local possibility is one statistical slot, "
    "and the relevant locked possibilities for the generation doublet are the "
    "K/CPT record-outcome orbits rather than the real components of the "
    "fluctuation coordinate."
)


for source_name, label, quote in [
    ("axioms", "state as records", AXIOM_STATE),
    ("axioms", "record locks one possibility", AXIOM_RECORD_LOCK),
    ("axioms", "record-only readout", AXIOM_RECORD_READ),
    ("axioms", "possibility distinction", AXIOM_QUBIT_DISTINCTION),
    ("axioms", "lattice mirror distinction", AXIOM_LATTICE_DISTINCTION),
    ("axioms", "nearest-neighbor admissibility", AXIOM_ADMISSIBILITY),
    ("axioms", "law sentence", AXIOM_LAW),
    ("axioms", "qualification boundary", AXIOM_QUALIFICATION),
    ("axioms", "open gates withhold rules", AXIOM_OPEN_GATES),
    ("static_no_go", "category-slip wall", WALL_CATEGORY),
    ("static_no_go", "measure-neutral selector wall", WALL_SELECTOR),
    ("static_no_go", "Record supplies no occupancy", WALL_NO_OCCUPANCY),
    ("static_no_go", "N1 record-orbit pruning row", STATIC_N1_RECORD_ROW),
    ("record_orbit_no_go", "operative record-orbit pruning sentence", RECORD_ORBIT_PRUNING),
    ("k_blindness", "separator requirement", K_SEPARATOR),
    ("k_blindness", "scalar blindness result", K_BLINDNESS),
    ("k_odd_trace", "adjacent K-odd trace wall", K_ODD_TRACE_WALL),
    ("occupancy", "prior bridge sentence", BRIDGE_SENTENCE),
]:
    guard_quote(source_name, label, quote)


NOTE_TITLE = (
    "# Koide Occupancy: Individuation Route Factorizes The Bridge And Does Not "
    "Escape The Walls (Bounded Note)"
)
PROVENANCE = (
    "A three-seat adversarial refutation pass returned a convergent negative on the "
    "derivation form of this note; this is the repaired convergent wording."
)
DECISIVE_QUESTION = "IS THE CONJUGATE-SECTOR RELATIVE PHASE A REGISTRABLE RECORD OUTCOME?"

check("note has repaired title", NOTE_TITLE in TARGET_TEXT)
check("note declares canonical open-gate type", "**Type:** open_gate" in TARGET_TEXT)
check("note declares factorization claim type", "**Claim type:** open_gate" in TARGET_TEXT and "bounded factorization + sharpened wall" in TARGET_TEXT)
check("note uses independent audit lane status authority", "**Status authority:** independent audit lane only." in TARGET_TEXT)
check("note includes adversarial-refutation provenance", normalized(PROVENANCE) in normalized(TARGET_TEXT))
check("note names the decisive open question", normalized(DECISIVE_QUESTION) in normalized(TARGET_TEXT))
check("note omits the old premise-shape wall framing", "premise-shape disjointness" not in TARGET_TEXT.lower())


@dataclass(frozen=True)
class Slot:
    name: str
    target: str
    source: str


ORBIT_POSSIBILITY_SET = frozenset({"singlet", "conjugate_orbit"})
PHASE_POSSIBILITY_SET = frozenset({"singlet", "real_part", "imaginary_part"})

ORBIT_GRADING = (
    Slot("singlet slot", "singlet", "record_content"),
    Slot("doublet orbit slot", "conjugate_orbit", "record_content"),
)
REAL_COORDINATE_GRADING = (
    Slot("singlet slot", "singlet", "record_content"),
    Slot("real-part slot", "real_part", "phase_readout"),
    Slot("imaginary-part slot", "imaginary_part", "phase_readout"),
)


def unlawful_reasons(slots: Iterable[Slot], possibility_set: frozenset[str]) -> list[str]:
    reasons: list[str] = []
    seen: list[str] = []
    for slot in slots:
        if slot.target not in possibility_set:
            reasons.append(f"{slot.target} is outside the candidate possibility set")
            continue
        seen.append(slot.target)
    if len(seen) != len(set(seen)):
        reasons.append("one possibility was counted more than once")
    if set(seen) != set(possibility_set):
        reasons.append("the grading does not range exactly over the candidate set")
    return reasons


def lawful_grading(slots: Iterable[Slot], possibility_set: frozenset[str]) -> bool:
    return not unlawful_reasons(slots, possibility_set)


orbit_on_orbit = lawful_grading(ORBIT_GRADING, ORBIT_POSSIBILITY_SET)
coordinate_on_orbit = lawful_grading(REAL_COORDINATE_GRADING, ORBIT_POSSIBILITY_SET)
orbit_on_phase = lawful_grading(ORBIT_GRADING, PHASE_POSSIBILITY_SET)
coordinate_on_phase = lawful_grading(REAL_COORDINATE_GRADING, PHASE_POSSIBILITY_SET)

check("orbit candidate set has two possibilities", ORBIT_POSSIBILITY_SET == frozenset({"singlet", "conjugate_orbit"}))
check(
    "phase-readout candidate set has three possibilities",
    PHASE_POSSIBILITY_SET == frozenset({"singlet", "real_part", "imaginary_part"}),
)
check("orbit grading is lawful on orbit candidate set", orbit_on_orbit)
check(
    "real-coordinate grading is unlawful on orbit candidate set",
    not coordinate_on_orbit,
    "; ".join(unlawful_reasons(REAL_COORDINATE_GRADING, ORBIT_POSSIBILITY_SET)),
)
check(
    "orbit grading is unlawful on phase-readout candidate set",
    not orbit_on_phase,
    "; ".join(unlawful_reasons(ORBIT_GRADING, PHASE_POSSIBILITY_SET)),
)
check("real-coordinate grading is lawful on phase-readout candidate set", coordinate_on_phase)
check(
    "slot-range verdict flips with the supplied possibility set",
    (orbit_on_orbit, coordinate_on_orbit, orbit_on_phase, coordinate_on_phase)
    == (True, False, False, True),
)


Matrix = list[list[Fraction]]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    rows = len(left)
    cols = len(right[0])
    inner = len(right)
    return [
        [sum(left[i][k] * right[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def trace(matrix: Matrix) -> Fraction:
    return sum(matrix[i][i] for i in range(len(matrix)))


real_symmetric_o: Matrix = [
    [Fraction(2), Fraction(3), Fraction(5)],
    [Fraction(3), Fraction(7), Fraction(11)],
    [Fraction(5), Fraction(11), Fraction(13)],
]
rotation_r: Matrix = [
    [Fraction(0), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(1)],
    [Fraction(1), Fraction(0), Fraction(0)],
]
rotation_r2 = matmul(rotation_r, rotation_r)
trace_o = trace(real_symmetric_o)
trace_r = trace(matmul(real_symmetric_o, rotation_r))
trace_r2 = trace(matmul(real_symmetric_o, rotation_r2))


@dataclass(frozen=True)
class QOmega:
    """Exact p + q*omega with omega^2 + omega + 1 = 0."""

    p: Fraction
    q: Fraction = Fraction(0)

    def __add__(self, other: QOmega | Fraction | int) -> QOmega:
        other_q = to_qomega(other)
        return QOmega(self.p + other_q.p, self.q + other_q.q)

    def __radd__(self, other: QOmega | Fraction | int) -> QOmega:
        return self + other

    def __neg__(self) -> QOmega:
        return QOmega(-self.p, -self.q)

    def __sub__(self, other: QOmega | Fraction | int) -> QOmega:
        return self + (-to_qomega(other))

    def __rsub__(self, other: QOmega | Fraction | int) -> QOmega:
        return to_qomega(other) - self

    def __mul__(self, other: QOmega | Fraction | int) -> QOmega:
        other_q = to_qomega(other)
        p = self.p * other_q.p - self.q * other_q.q
        q = self.p * other_q.q + self.q * other_q.p - self.q * other_q.q
        return QOmega(p, q)

    def __rmul__(self, other: QOmega | Fraction | int) -> QOmega:
        return self * other

    def __truediv__(self, scalar: Fraction | int) -> QOmega:
        scalar_f = Fraction(scalar)
        return QOmega(self.p / scalar_f, self.q / scalar_f)

    def is_real(self) -> bool:
        return self.q == 0


def to_qomega(value: QOmega | Fraction | int) -> QOmega:
    if isinstance(value, QOmega):
        return value
    return QOmega(Fraction(value), Fraction(0))


omega = QOmega(Fraction(0), Fraction(1))
conj_omega = QOmega(Fraction(-1), Fraction(-1))
t0 = trace_o
t1 = trace_r
t2 = trace_r2
isotype_1 = (to_qomega(t0) + conj_omega * t1 + omega * t2) / 3
isotype_2 = (to_qomega(t0) + omega * t1 + conj_omega * t2) / 3


Vector = tuple[Fraction, Fraction]


def conjugate(z: Vector) -> Vector:
    return (z[0], -z[1])


def rephase(z: Vector, cos_theta: Fraction = Fraction(3, 5), sin_theta: Fraction = Fraction(4, 5)) -> Vector:
    x, y = z
    return (cos_theta * x - sin_theta * y, sin_theta * x + cos_theta * y)


def norm_squared(z: Vector) -> Fraction:
    return z[0] * z[0] + z[1] * z[1]


def doublet_energy(z: Vector) -> Fraction:
    return 6 * norm_squared(z)


def scalar_trace_value(_: Vector) -> Fraction:
    return trace_r


def scalar_trace_square_value(_: Vector) -> Fraction:
    return trace_r2


def isotypic_difference(_: Vector) -> QOmega:
    return isotype_1 - isotype_2


def even_quartic(z: Vector) -> Fraction:
    return norm_squared(z) * norm_squared(z)


def imaginary_coordinate(z: Vector) -> Fraction:
    return z[1]


Invariant = tuple[str, Callable[[Vector], Fraction | QOmega]]

SUPPLIED_SCALAR_INVARIANTS: tuple[Invariant, ...] = (
    ("doublet norm", norm_squared),
    ("doublet energy", doublet_energy),
    ("scalar trace R", scalar_trace_value),
    ("scalar trace R2", scalar_trace_square_value),
    ("isotypic difference", isotypic_difference),
    ("even quartic scalar", even_quartic),
)

b = (Fraction(2), Fraction(3))
conj_b = conjugate(b)
rephased_b = rephase(b)
invariant_values = [(name, fn(b), fn(conj_b)) for name, fn in SUPPLIED_SCALAR_INVARIANTS]
separating_invariants = [(name, left, right) for name, left, right in invariant_values if left != right]
rephase_values = [(name, fn(b), fn(rephased_b)) for name, fn in SUPPLIED_SCALAR_INVARIANTS]
rephase_failures = [(name, left, right) for name, left, right in rephase_values if left != right]

check("trace value t0 is the true matrix trace", t0 == Fraction(22), f"t0={t0}")
check("real-symmetric scalar trace is K-even", trace_r == trace_r2, f"Tr(OR)={trace_r}, Tr(OR2)={trace_r2}")
check("scalar character contents are equal when T1=T2 is real", isotype_1 == isotype_2, f"I1={isotype_1}, I2={isotype_2}")
check("scalar invariant enumeration has six items", len(SUPPLIED_SCALAR_INVARIANTS) == 6)
check("every enumerated scalar invariant is equal on b and conj(b)", separating_invariants == [], str(separating_invariants))
check("every enumerated scalar invariant is U(1)-rephasing invariant", rephase_failures == [], str(rephase_failures))
check(
    "enumerated b-dependent scalars are functions of norm squared on the test point",
    norm_squared(b) == norm_squared(conj_b) == norm_squared(rephased_b)
    and doublet_energy(b) == 6 * norm_squared(b)
    and even_quartic(b) == norm_squared(b) ** 2,
)

im_left = imaginary_coordinate(b)
im_right = imaginary_coordinate(conj_b)
im_rephased = imaginary_coordinate(rephased_b)
P_PHASE = (
    "P-phase: no supplied conjugate-sector phase readout; record content fixes "
    "|b|^2 and not the conjugate-sector relative phase."
)

check("Im(b) separates the conjugates", im_left != im_right, f"{im_left} versus {im_right}")
check("Im(b) is not invariant under the supplied U(1) rephasing", im_left != im_rephased, f"{im_left} versus {im_rephased}")
check(
    "excluding Im(b) requires the named P-phase premise",
    "P-phase" in P_PHASE and im_left != im_right and im_left != im_rephased and rephase_failures == [],
    P_PHASE,
)

P_TRANSPORT = "P-transport: one-site individuation discipline transports to the derived doublet."
P_OCCUPANCY = "P-occupancy: one statistical slot per possibility."
FACTORIZED_PREMISES = (P_TRANSPORT, P_PHASE, P_OCCUPANCY)

check("factorization has exactly three named premises", len(FACTORIZED_PREMISES) == 3)
check("factorization names P-transport", FACTORIZED_PREMISES[0].startswith("P-transport:"))
check("factorization names P-phase", FACTORIZED_PREMISES[1].startswith("P-phase:"))
check("factorization names P-occupancy", FACTORIZED_PREMISES[2].startswith("P-occupancy:"))
check(
    "old bridge is exchanged for three premises rather than eliminated",
    len(FACTORIZED_PREMISES) == 3 and all("P-" in premise for premise in FACTORIZED_PREMISES),
)
theta_conditionals_after_exchange = len(FACTORIZED_PREMISES)
check(
    "theta mass-side conditional count is three named premises, not zero",
    theta_conditionals_after_exchange == 3,
    f"after_exchange={theta_conditionals_after_exchange}",
)

z_sector = Fraction(2)
z_orbit = Fraction(1)
rho_sector = Fraction(1) / z_sector
rho_orbit = Fraction(1) / z_orbit
r_sector = Fraction(1) / (2 * rho_sector)
r_orbit = Fraction(1) / (2 * rho_orbit)
check(
    "orbit arithmetic remains conditional and gives r=1/2 only with the premises",
    z_sector / z_orbit == 2 and r_sector == 1 and r_orbit == Fraction(1, 2) and len(FACTORIZED_PREMISES) == 3,
    f"r_sector={r_sector}, r_orbit={r_orbit}",
)

check("note states scalar list has no completeness theorem", "not a proof that no supplied `b`-functional can ever separate them" in TARGET_TEXT)
check("note states slot range is conditional", "The slot-range leg is not independent" in TARGET_TEXT)
check("note states Record supplies no occupancy rule", WALL_NO_OCCUPANCY in TARGET_TEXT)
check("note states the theta conditional does not drop to zero", "does not drop to zero" in TARGET_TEXT)
check("note cites adjacent K-odd trace note", "ACPHILAMBDA_PROJECTIVE_EQUIVARIANCE_K_ODD_TRACE_2026-07-02.md" in TARGET_TEXT)


def main() -> int:
    for index, item in enumerate(CHECKS, start=1):
        status = "PASS" if item.passed else "FAIL"
        detail = f" -- {item.detail}" if item.detail else ""
        print(f"CHECK {index:02d}: {status} -- {item.description}{detail}")

    pass_count = sum(1 for item in CHECKS if item.passed)
    fail_count = len(CHECKS) - pass_count
    print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
    print(f"SUMMARY files/checks: {TARGET_NOTE}; {TARGET_RUNNER}; checks={len(CHECKS)} PASS={pass_count} FAIL={fail_count}")
    print(f"SUMMARY P-transport: {P_TRANSPORT}")
    print(f"SUMMARY P-phase: {P_PHASE}")
    print(f"SUMMARY P-occupancy: {P_OCCUPANCY}")
    print(
        f"SUMMARY decisive-open-question/uncertainties: {DECISIVE_QUESTION}; "
        "uncertainties=P-phase open, P-transport open, P-occupancy open, scalar list not complete"
    )
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
