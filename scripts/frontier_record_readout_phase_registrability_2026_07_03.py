#!/usr/bin/env python3
"""Bounded runner for doublet phase registrability readout screen."""

from __future__ import annotations

import cmath
import math
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SOURCE_PATHS = {
    "axioms": Path("docs/MINIMAL_AXIOMS_2026-06-29.md"),
    "k_blindness": Path(
        "docs/ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02.md"
    ),
    "p_phase": Path(
        "docs/KOIDE_OCCUPANCY_DERIVED_FROM_POSSIBILITY_INDIVIDUATION_BOUNDED_NOTE_2026-07-03.md"
    ),
    "determinant": Path(
        "docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md"
    ),
    "slot": Path(
        "docs/KOIDE_SLOT_FREEDOM_CLASSIFICATION_UNDER_CONJUGATION_READING_BOUNDED_NOTE_2026-07-03.md"
    ),
}

OUTPUT_FILES = (
    Path("docs/RECORD_READOUT_PHASE_REGISTRABILITY_AT_DOUBLET_GRADE_BOUNDED_NOTE_2026-07-03.md"),
    Path("scripts/frontier_record_readout_phase_registrability_2026_07_03.py"),
)

# The fork/transport ruling is carried by the note's prose, not computed here.
# These checks certify only quoted-inventory guards and numerical exhibits.
VERDICT = (
    "NO-GO HOLDS at the enumerated-inventory grade: no quoted axiom sentence "
    "supplies an orientation of the derived doublet phase plane, so every "
    "readout constructible from quoted sentences at the doublet grade is "
    "K-even there and factors through `|b|^2` on the covered functional class."
)
OPEN_DEFEAT_ROUTES = (
    "open_defeat_routes: (1) adopt the complex-presentation reading of the "
    "Qubit sentence and supply a quoted transport law from the one-site "
    "orientation to the doublet phase plane; (2) supply a quoted transport law "
    "from history-index orientation (record accumulation) to the doublet phase "
    "plane."
)
FORK_DISPOSITION = (
    'fork_disposition: The site-level presentation fork ("does naming `M_2(C)` '
    "supply a preferred `i`?\") is a textual-clarity question about the Qubit "
    "axiom wording; if it ever becomes load-bearing on its own, it is a "
    "candidate for an axiom-clarity sentence."
)

P_TRANSPORT_QUOTE = (
    "P-transport: the one-site individuation discipline transports to the "
    "derived generation doublet."
)
P_TRANSPORT_NON_DERIVED_QUOTE = (
    "This note no longer claims that sentence is derived."
)
P_PHASE_QUOTE = (
    "P-phase: record content fixes the orbit magnitude `|b|^2` and not the "
    "conjugate-sector relative phase."
)
DOWNSTREAM_SECTOR_QUOTE = (
    "`K`/CPT orbit structure, central-sector decomposition, and any sector "
    "generation rule are downstream readout-context content, not generic axiom "
    "content."
)


def squash(text: str) -> str:
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    return re.sub(r"\s+", " ", text.strip())


def contains_quote(text: str, quote: str) -> bool:
    return squash(quote) in squash(text)


def section(text: str, start: str, end: str) -> str:
    try:
        return text.split(start, 1)[1].split(end, 1)[0]
    except IndexError:
        return ""


def rho(z: complex) -> float:
    return z.real * z.real + z.imag * z.imag


def close(a: complex | float, b: complex | float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


Matrix = list[list[complex]]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [
            sum(a[row][k] * b[k][col] for k in range(2))
            for col in range(2)
        ]
        for row in range(2)
    ]


def matadd(a: Matrix, b: Matrix) -> Matrix:
    return [[a[row][col] + b[row][col] for col in range(2)] for row in range(2)]


def matscale(alpha: complex | float, a: Matrix) -> Matrix:
    return [[alpha * a[row][col] for col in range(2)] for row in range(2)]


def matconj(a: Matrix) -> Matrix:
    return [[a[row][col].conjugate() for col in range(2)] for row in range(2)]


def matclose(a: Matrix, b: Matrix, tol: float = 1e-12) -> bool:
    return all(close(a[row][col], b[row][col], tol) for row in range(2) for col in range(2))


class CheckRunner:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.index = 1

    def check(self, condition: bool, description: str) -> None:
        status = "PASS" if condition else "FAIL"
        print(f"CHECK {self.index:02d}: {status} -- {description}")
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        self.index += 1


def cubic_real(z: complex) -> float:
    return (z**3).real


def main() -> int:
    runner = CheckRunner()

    texts: dict[str, str] = {}
    for key, rel_path in SOURCE_PATHS.items():
        path = ROOT / rel_path
        try:
            texts[key] = path.read_text(encoding="utf-8")
            loaded = True
        except OSError:
            texts[key] = ""
            loaded = False
        runner.check(loaded, f"source readable: {rel_path}")

    output_texts: dict[str, str] = {}
    for rel_path in OUTPUT_FILES:
        path = ROOT / rel_path
        try:
            output_texts[str(rel_path)] = path.read_text(encoding="utf-8")
            loaded = True
        except OSError:
            output_texts[str(rel_path)] = ""
            loaded = False
        runner.check(loaded, f"allowed output file readable: {rel_path}")

    axioms = texts["axioms"]
    k_blindness = texts["k_blindness"]
    p_phase = texts["p_phase"]
    determinant = texts["determinant"]
    slot = texts["slot"]
    note = output_texts[str(OUTPUT_FILES[0])]

    note_required_phrases = [
        "**Claim type:** bounded no_go at the enumerated-inventory grade.",
        "An adversarial three-seat pass refuted the draft's failure-report verdict; this is the repaired wording.",
        VERDICT,
        "This note does not decide the fork.",
        "The doublet-grade verdict does not require deciding that textual question, because an oriented doublet readout also needs the missing transport law.",
        "The site-level presentation fork (\"does naming `M_2(C)` supply a preferred `i`?\") is a textual-clarity question about the Qubit axiom wording; if it ever becomes load-bearing on its own, it is a candidate for an axiom-clarity sentence.",
        "The same standard applies to algebra orientation and time orientation.",
        "At this grade, that premise is consistent with the quoted inventory but is not derived from it.",
        "No `r`-branch pressure materializes from the current text.",
        "The boundary witness `Re(b^3)` is `C3`-invariant and K-even:",
    ]
    for phrase in note_required_phrases:
        runner.check(contains_quote(note, phrase), f"note repaired phrase present: {phrase[:72]}")
    runner.check("THEOREM FAILS" not in note, "note does not contain THEOREM FAILS verdict")

    axiom_quotes = [
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.",
        "No site is privileged. Sites are distinguished by the supplied lattice structure alone.",
        "Each site has a domain of local possibilities.",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
        "A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and adds no further primitive structure.",
        "No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone.",
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
        "For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions.",
        "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent.",
        "Only records are readable. A readout value is determined by record content alone. For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.",
        "These axioms state only their named primitive content. Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration before use as a premise.",
        "A state is a configuration of records.",
        "A law privileges no states. Its domain is a supplied condition, and at every state where the condition holds it gives exactly one answer.",
        DOWNSTREAM_SECTOR_QUOTE,
        "Admissibility is not a dynamics axiom. It determines availability by a nearest-neighbor rule: for each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions. It does not choose a Hamiltonian or transfer operator, supply transition probabilities or weights, select a scalar or nonzero kinetic branch, assert a Dirac-square carrier, define a time metric, or provide a record-production process or physical persistence dynamics.",
        "the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`;",
        "the strong-CP theta admission;",
        "P2/modulus/phase-blindness and any log-det readout theorem;",
        "context selection, measurement basis selection, Born weights, probability rules, update laws, decoherence mechanisms, and occurrence rules;",
        "arrow, record-production dynamics, physical persistence dynamics, time metric, and local observability of records;",
        "source/action and physical-observable identification;",
        "`g_bare = 1` convention handling;",
        "the scale-reference primitive and the separate gravity self-consistency question that the framework's natural unit equals the Planck length.",
    ]
    for quote in axiom_quotes:
        runner.check(contains_quote(axioms, quote), f"axiom quote guarded: {quote[:72]}")

    open_gate_disposals = [
        "That is a realization gate, not a supplied orientation or doublet transport.",
        "That is phase-blind or channel-specific readout content, not a supplied\ndoublet phase-plane orientation.",
        "Those are selection, probability, and update gates, not a transport law from\nsite-level orientation or record history to the doublet phase plane.",
        "Those are time/history gates, not a quoted transport law to the doublet phase\nplane.",
        "That is an observable-identification gate, not a supplied orientation or\ndoublet transport.",
    ]
    for phrase in open_gate_disposals:
        runner.check(phrase in note, f"open-gate non-supplier disposition present: {phrase[:72]}")

    qubit_block = section(
        axioms,
        "### Qubit / Site Possibility",
        "### Admissibility / Local Constraint",
    )
    qubit_full_quote = """Each site has a domain of local possibilities.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and
adds no further primitive structure.

No possibility is privileged. Possibilities are distinguished by the supplied
algebraic structure alone."""
    runner.check(
        contains_quote(qubit_block, qubit_full_quote),
        "Qubit axiom full block guarded",
    )

    transport_gap_quotes = [
        (p_phase, P_TRANSPORT_QUOTE, "P-transport named premise guarded"),
        (
            p_phase,
            P_TRANSPORT_NON_DERIVED_QUOTE,
            "P-transport non-derivation sentence guarded",
        ),
        (axioms, DOWNSTREAM_SECTOR_QUOTE, "downstream-sector sentence guarded"),
        (
            axioms,
            "arrow, record-production dynamics, physical persistence dynamics, time metric, and local observability of records;",
            "time/history open-gate quote guarded",
        ),
        (
            axioms,
            "These axioms state only their named primitive content. Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration before use as a premise.",
            "supplied-structure discipline guarded for transport gap",
        ),
    ]
    for text, quote, description in transport_gap_quotes:
        runner.check(contains_quote(text, quote), description)
    runner.check(
        not contains_quote(axioms, P_TRANSPORT_QUOTE),
        "transport gap: P-transport is not quoted as axiom content",
    )

    adjacent_quotes = [
        (
            k_blindness,
            "This covers adjacency matrices, scalar graph Laplacians, and every real function `f(Delta)` of the scalar Laplacian.",
            "K-blindness class sentence guarded",
        ),
        (
            k_blindness,
            "No scalar-ambient functional on that surface separates the conjugate isotypes.",
            "K-blindness scalar separation sentence guarded",
        ),
        (
            p_phase,
            P_PHASE_QUOTE,
            "P-phase target sentence guarded",
        ),
        (
            determinant,
            "The determinant phase is erased inside this determinant-channel readout class.",
            "determinant erasure result guarded",
        ),
        (
            slot,
            "Under hypothetical H-conj, conjugate configurations are one possibility. That decides P-phase in the negative for this classification.",
            "slot-classification hypothetical H-conj sentence guarded",
        ),
        (
            slot,
            "The remaining question is the slot convention: one slot per possibility gives `r = 1/2`, while one slot per real coordinate gives `r = 1`.",
            "slot r-branch consequence guarded",
        ),
    ]
    for text, quote, description in adjacent_quotes:
        runner.check(contains_quote(text, quote), description)

    a = [[1 + 2j, -3 + 0.5j], [4 - 1j, 2j]]
    b_mat = [[-2 + 1j, 0.25 - 3j], [1.5 + 0j, -1 - 2j]]
    identity = [[1 + 0j, 0 + 0j], [0 + 0j, 1 + 0j]]
    i_identity = matscale(1j, identity)
    neg_i_identity = matscale(-1j, identity)
    alpha = 2.5
    beta = -0.75
    runner.check(
        matclose(matconj(matmul(a, b_mat)), matmul(matconj(a), matconj(b_mat))),
        "real-algebra branch: entrywise conjugation preserves products on sample M_2(C)",
    )
    runner.check(
        matclose(
            matconj(matadd(matscale(alpha, a), matscale(beta, b_mat))),
            matadd(matscale(alpha, matconj(a)), matscale(beta, matconj(b_mat))),
        ),
        "real-algebra branch: entrywise conjugation preserves real-linear combinations",
    )
    runner.check(
        matclose(matconj(i_identity), neg_i_identity),
        "real-algebra branch: conjugation sends iI to -iI",
    )
    runner.check(
        matclose(matmul(i_identity, i_identity), matscale(-1, identity))
        and matclose(matmul(neg_i_identity, neg_i_identity), matscale(-1, identity)),
        "real-algebra branch: both central orientations square to -I on the sample identity",
    )

    z = complex(2, 3)
    kz = z.conjugate()
    runner.check(close(z.imag, 3.0), "real-algebra branch single-valuedness: Im(2+3i) = 3")
    runner.check(close(kz.imag, -3.0), "real-algebra branch single-valuedness: Im(conj(2+3i)) = -3")
    runner.check(
        close(z.imag, -kz.imag),
        "real-algebra branch single-valuedness failure: Im flips sign under K",
    )
    runner.check(
        z.imag != -z.imag,
        "real-algebra branch single-valuedness failure: orientation reversal changes Im(b)",
    )

    records_a = [complex(2, 3), complex(-1, 4)]
    records_b = [complex(5, -2)]

    def oriented_readout(records: list[complex]) -> float:
        return sum(sample.imag for sample in records)

    additive_left = oriented_readout(records_a + records_b)
    additive_right = oriented_readout(records_a) + oriented_readout(records_b)
    runner.check(
        close(oriented_readout([]), 0.0),
        "orientation-supplied branch only: negative control has I(empty)=0",
    )
    runner.check(
        close(additive_left, additive_right),
        "orientation-supplied branch only: negative control is finite-additive on disjoint records",
    )
    runner.check(
        isinstance(oriented_readout(records_a), float),
        "orientation-supplied branch only: negative control returns a real scalar",
    )
    runner.check(
        oriented_readout([z]) != oriented_readout([kz]),
        "orientation-supplied branch only: separates b from conj(b) if orientation and doublet transport are quoted",
    )

    omega = cmath.exp(2j * math.pi / 3)
    b_values = [complex(2, 3), complex(-1, 0.5), complex(0, 1.25), complex(-2, -2)]
    radial_samples = [
        ("polynomial", lambda r: 7.0 + 3.0 * r + 2.0 * r * r),
        ("rational", lambda r: (r + 1.0) / (r + 3.0)),
        ("exp", lambda r: math.exp(-0.1 * r)),
    ]
    for name, func in radial_samples:
        runner.check(
            all(close(func(rho(sample)), func(rho(sample.conjugate()))) for sample in b_values),
            f"covered class additive radial scalars F(|b|^2): {name} sample is K-even over several b",
        )
        runner.check(
            all(close(func(rho(omega * sample)), func(rho(sample))) for sample in b_values),
            f"covered class additive radial scalars F(|b|^2): {name} sample is C3-invariant over several b",
        )
        finite_sum = sum(func(rho(sample)) for sample in b_values)
        finite_sum_k = sum(func(rho(sample.conjugate())) for sample in b_values)
        finite_sum_c3 = sum(func(rho(omega * sample)) for sample in b_values)
        runner.check(
            close(finite_sum, finite_sum_k) and close(finite_sum, finite_sum_c3),
            f"covered class finite disjoint sums of radial scalars: {name} sample remains K-even and C3-invariant",
        )

    runner.check(
        all(close(cubic_real(omega * sample), cubic_real(sample)) for sample in b_values),
        "boundary witness: Re(b^3) is C3-invariant over sample b values",
    )
    runner.check(
        all(close(cubic_real(sample.conjugate()), cubic_real(sample)) for sample in b_values),
        "boundary witness: Re(b^3) is K-even, not K-odd",
    )
    runner.check(
        close(rho(complex(1, 0)), rho(complex(0, 1)))
        and not close(cubic_real(complex(1, 0)), cubic_real(complex(0, 1))),
        "boundary witness: Re(b^3) is not a function of |b|^2 alone",
    )

    print(f"TOTAL: PASS={runner.passed} FAIL={runner.failed}")
    print(f"SUMMARY 1 files: {OUTPUT_FILES[0]} ; {OUTPUT_FILES[1]}")
    print(f"SUMMARY 2 check_count: {runner.passed + runner.failed} mechanical checks")
    print(f"SUMMARY 3 VERDICT: {VERDICT} [prose-carried by note; not computed]")
    print(f"SUMMARY 4 {OPEN_DEFEAT_ROUTES}")
    print(f"SUMMARY 5 {FORK_DISPOSITION}")
    return 0 if runner.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
