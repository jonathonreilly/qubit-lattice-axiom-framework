#!/usr/bin/env python3
"""Independent Block-8 fixed-carrier/QND boundary check.

This checker rebuilds the A/B effects and programs directly, uses explicit
closed-form two-qubit unitary completions rather than importing the primary
implementation, and independently reconstructs the four-site writers,
presence code, central masses, QND controls, and reversible absorption wall.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "FIXED_CARRIER_PRESENCE_SEPARATED_NONDEMOLITION_RECORD_UPDATE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)

AUDIT_INPUT_PATHS = (
    "docs/FIXED_CARRIER_PRESENCE_SEPARATED_NONDEMOLITION_RECORD_UPDATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/FRESH_ANCILLA_STAGED_CQ_RECORD_INTERTWINER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/fixed_carrier_presence_separated_nondemolition_record_update_boundary_2026_08_20.py",
)

PASS = 0
FAIL = 0

I2 = sp.eye(2)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -sp.I), (sp.I, 0)))
Z = sp.diag(1, -1)
P0 = sp.diag(1, 0)
P1 = sp.diag(0, 1)

E0 = sp.diag(sp.Rational(1, 2), 0)
EA1 = sp.Matrix(
    ((sp.Rational(1, 10), sp.sqrt(2) / 5),
     (sp.sqrt(2) / 5, sp.Rational(4, 5)))
)
EA2 = sp.Matrix(
    ((sp.Rational(2, 5), -sp.sqrt(2) / 5),
     (-sp.sqrt(2) / 5, sp.Rational(1, 5)))
)
EB1 = sp.Matrix(
    ((sp.Rational(1, 4), sp.sqrt(2) / 4),
     (sp.sqrt(2) / 4, sp.Rational(1, 2)))
)
EB2 = sp.Matrix(
    ((sp.Rational(1, 4), -sp.sqrt(2) / 4),
     (-sp.sqrt(2) / 4, sp.Rational(1, 2)))
)
MENUS = {"A": (E0, EA1, EA2), "B": (E0, EB1, EB2)}

KRAUS = {
    context: tuple(
        sp.simplify(effect / sp.sqrt(sp.trace(effect))) for effect in menu
    )
    for context, menu in MENUS.items()
}
K0 = KRAUS["A"][0]
B = sp.diag(1 / sp.sqrt(2), 1)
RESIDUAL = {
    context: tuple(sp.simplify(kraus * B.inv()) for kraus in program[1:])
    for context, program in KRAUS.items()
}

U_FRONT = sp.Matrix(
    (
        (sp.sqrt(2) / 2, 0, 0, -sp.sqrt(2) / 2),
        (0, 0, 1, 0),
        (sp.sqrt(2) / 2, 0, 0, sp.sqrt(2) / 2),
        (0, 1, 0, 0),
    )
)
U_RESIDUAL = {
    "A": sp.Matrix(
        (
            (sp.sqrt(5) / 15, 2 * sp.sqrt(5) / 15, -2 * sp.sqrt(2) / 3, 0),
            (2 * sp.sqrt(10) / 15, 4 * sp.sqrt(10) / 15, sp.Rational(1, 3), 0),
            (2 * sp.sqrt(30) / 15, -sp.sqrt(30) / 15, 0, sp.sqrt(3) / 3),
            (-2 * sp.sqrt(15) / 15, sp.sqrt(15) / 15, 0, sp.sqrt(6) / 3),
        )
    ),
    "B": sp.Matrix(
        (
            (sp.sqrt(6) / 6, sp.sqrt(6) / 6, -sp.sqrt(6) / 3, 0),
            (sp.sqrt(3) / 3, sp.sqrt(3) / 3, sp.sqrt(3) / 3, 0),
            (sp.sqrt(6) / 6, -sp.sqrt(6) / 6, 0, sp.sqrt(6) / 3),
            (-sp.sqrt(3) / 3, sp.sqrt(3) / 3, 0, sp.sqrt(3) / 3),
        )
    ),
}

BLANK = "000"
PENDING = "100"
TERMINALS = ("010", "110", "111")
RHO_STAR = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def zero(matrix: sp.Matrix) -> bool:
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


def ket(word: str) -> sp.Matrix:
    result = sp.zeros(8, 1)
    result[int(word, 2), 0] = 1
    return result


def embedding(word: str) -> sp.Matrix:
    return sp.kronecker_product(ket(word), I2)


def projector(word: str) -> sp.Matrix:
    vector = ket(word)
    return sp.kronecker_product(vector * vector.H, I2)


def stacked(pair: tuple[sp.Matrix, sp.Matrix]) -> sp.Matrix:
    return sp.Matrix.vstack(*pair)


def embed_front() -> sp.Matrix:
    """Independent basis enumeration for M1,F,M2,S logical order."""

    result = sp.zeros(16)
    for source in range(16):
        bits = tuple((source >> shift) & 1 for shift in (3, 2, 1, 0))
        m1, flag, m2, system = bits
        pair_source = 2 * m1 + system
        for pair_target in range(4):
            target_m1, target_system = divmod(pair_target, 2)
            target = 8 * target_m1 + 4 * flag + 2 * m2 + target_system
            result[target, source] = U_FRONT[pair_target, pair_source]
    return result


def completion(context: str) -> sp.Matrix:
    return sp.simplify(
        sp.kronecker_product(P0, X, sp.eye(4))
        + sp.kronecker_product(P1, X, U_RESIDUAL[context])
    )


def writer(context: str) -> sp.Matrix:
    return sp.simplify(completion(context) * embed_front())


def expected_isometry(context: str) -> sp.Matrix:
    result = sp.zeros(16, 2)
    for word, operator in zip(TERMINALS, KRAUS[context], strict=True):
        index = 2 * int(word, 2)
        result[index : index + 2, :] = operator
    return result


def environment_copy() -> sp.Matrix:
    codes = {2: 0, 6: 1, 7: 2}
    result = sp.zeros(32)
    for memory in range(8):
        for environment in range(4):
            source = 4 * memory + environment
            target = 4 * memory + (environment ^ codes.get(memory, 3))
            result[target, source] = 1
    return result


def environment_dilation(isometry: sp.Matrix) -> sp.Matrix:
    blank = sp.zeros(64, 2)
    for memory in range(8):
        for system in range(2):
            blank[8 * memory + system, :] = isometry[2 * memory + system, :]
    return sp.kronecker_product(environment_copy(), I2) * blank


def discard_environment(state: sp.Matrix) -> sp.Matrix:
    result = sp.zeros(16)
    for ml in range(8):
        for mr in range(8):
            for sl in range(2):
                for sr in range(2):
                    result[2 * ml + sl, 2 * mr + sr] = sp.simplify(
                        sum(
                            state[(ml * 4 + e) * 2 + sl, (mr * 4 + e) * 2 + sr]
                            for e in range(4)
                        )
                    )
    return result


PB = projector(BLANK)
PT_ATOMS = tuple(projector(word) for word in TERMINALS)
PT = sum(PT_ATOMS, sp.zeros(16))
E_BLANK = embedding(BLANK)


def independent_program_controls() -> None:
    failures = 0
    for context, program in KRAUS.items():
        failures += not zero(sum((k.H * k for k in program), sp.zeros(2)) - I2)
        failures += not zero(
            sum((j.H * j for j in RESIDUAL[context]), sp.zeros(2)) - I2
        )
        failures += any(
            not zero(j * B - k)
            for j, k in zip(RESIDUAL[context], program[1:], strict=True)
        )
    check(
        "independent-exact-A-B-programs",
        failures == 0 and KRAUS["A"][0] == KRAUS["B"][0] == K0,
        "the effects, Kraus programs, common front, residual completeness, and residual composition are rebuilt without importing either Block-8 implementation",
    )


def explicit_completion_controls() -> None:
    failures = int(not zero(U_FRONT.H * U_FRONT - sp.eye(4)))
    failures += not zero(U_FRONT[:, 0:2] - stacked((K0, B)))
    for context in ("A", "B"):
        residual_unitary = U_RESIDUAL[context]
        failures += not zero(residual_unitary.H * residual_unitary - sp.eye(4))
        failures += not zero(
            residual_unitary[:, 0:2] - stacked(RESIDUAL[context])
        )
        full = writer(context)
        failures += not zero(full.H * full - sp.eye(16))
        failures += not zero(full * E_BLANK - expected_isometry(context))
    check(
        "independent-closed-form-unitaries",
        failures == 0,
        "explicit radical-valued front and A/B residual completions independently reproduce the repaired four-site path writer",
    )


def presence_and_stage_controls() -> None:
    old_zero = projector("000")
    words = (BLANK, PENDING) + TERMINALS
    projectors = tuple(projector(word) for word in words)
    check(
        "independent-old-presence-collision",
        old_zero == PB and K0.rank() == 1,
        "the old terminal-0 word is exactly the full blank word sector and carries a nonzero outcome range",
    )
    check(
        "independent-repaired-presence-code",
        len(set(words)) == 5
        and all(
            zero(projectors[i] * projectors[j])
            for i in range(5)
            for j in range(i + 1, 5)
        )
        and zero(PB * PT),
        "blank, pending, and all three terminal atoms are pairwise disjoint after moving only outcome 0 to 010",
    )

    front_image = sp.simplify(embed_front() * E_BLANK)
    check(
        "independent-pending-stage",
        zero(front_image[0:2, :] - K0)
        and zero(front_image[8:10, :] - B)
        and all(
            zero(front_image[2 * index : 2 * index + 2, :])
            for index in range(8)
            if index not in (0, 4)
        ),
        "the separately enumerated front has only the old-zero and pending-100 supports before completion",
    )


def center_and_qnd_controls() -> None:
    target_weights = {
        "A": (sp.Rational(3, 10), sp.Rational(19, 50), sp.Rational(8, 25)),
        "B": (sp.Rational(3, 10), sp.Rational(7, 20), sp.Rational(7, 20)),
    }
    failures = 0
    for context in ("A", "B"):
        isometry = expected_isometry(context)
        state = sp.simplify(isometry * RHO_STAR * isometry.H)
        weights = tuple(sp.simplify(sp.trace(atom * state)) for atom in PT_ATOMS)
        failures += weights != target_weights[context]
    check(
        "independent-central-masses",
        failures == 0,
        "the repaired word decoder independently reproduces all exact A/B central masses",
    )

    copy = environment_copy()
    export_failures = int(not zero(copy.H * copy - sp.eye(32)))
    ranks: list[int] = []
    terminal_codes = {
        int("010", 2): 0,
        int("110", 2): 1,
        int("111", 2): 2,
    }
    code_values = tuple(terminal_codes.get(memory, 3) for memory in range(8))
    terminal_indices = tuple(int(word, 2) for word in TERMINALS)
    export_failures += any(
        (code_values[left] == code_values[right])
        != (
            (left == right and left in terminal_indices)
            or (left not in terminal_indices and right not in terminal_indices)
        )
        for left in range(8)
        for right in range(8)
    )
    rho_family = (I2 / 2, (I2 + X) / 2, (I2 + Y) / 2, (I2 + Z) / 2)
    for context in ("A", "B"):
        isometry = expected_isometry(context)
        branch_vectors = sp.Matrix.hstack(
            *(
                sp.Matrix(embedding(word) * operator).reshape(32, 1)
                for word, operator in zip(TERMINALS, KRAUS[context], strict=True)
            )
        )
        ranks.append(branch_vectors.rank())
        dilation = environment_dilation(isometry)
        for rho in rho_family:
            coherent = sp.simplify(isometry * rho * isometry.H)
            pinched = sum((atom * coherent * atom for atom in PT_ATOMS), sp.zeros(16))
            exported = sp.simplify(dilation * rho * dilation.H)
            export_failures += not zero(discard_environment(exported) - pinched)
    check(
        "independent-cq-export-rank",
        export_failures == 0 and ranks == [3, 3],
        "a separately enumerated four-code two-qubit environment realizes full-carrier Q_perp/terminal pinching, is tomographically exact on the terminal path-output channel, and confirms its pure-environment rank three",
    )

    future = sp.diag(
        I2,
        I2,
        Z,
        I2,
        I2,
        I2,
        X,
        -Z,
    )
    qnd_failures = int(not zero(future.H * future - sp.eye(16)))
    qnd_failures += sum(
        not zero(future.H * atom * future - atom) for atom in PT_ATOMS
    )
    check(
        "independent-qnd-live-evolution",
        qnd_failures == 0 and not zero(PT_ATOMS[1] * future - PT_ATOMS[1]),
        "a second block-controlled future update fixes each logical atom but remains nontrivial inside terminal live-system blocks",
    )

    memory = sp.eye(8)
    memory[:, 6], memory[:, 7] = memory[:, 7], memory[:, 6]
    hostile = sp.kronecker_product(memory, I2)
    check(
        "independent-setwise-not-pointwise-hostile",
        zero(hostile.H * hostile - sp.eye(16))
        and zero(hostile.H * PT * hostile - PT)
        and not zero(hostile.H * PT_ATOMS[1] * hostile - PT_ATOMS[1]),
        "a terminal-label swap preserves the terminal set and occupancy while violating content permanence",
    )


def reversible_boundary_controls() -> None:
    failures = 0
    double_use_failures = 0
    for context in ("A", "B"):
        full = writer(context)
        image = expected_isometry(context)
        failures += not zero((sp.eye(16) - PT) * image)
        failures += not zero(full.H * image - E_BLANK)
        failures += zero(full.H * PT * full - PT)
        second = sp.simplify(full * image)
        leak = sp.simplify((sp.eye(16) - PT) * second)
        double_use_failures += not zero(PT * second)
        double_use_failures += not zero(leak.H * leak - I2)
    check(
        "independent-inverse-erasure",
        failures == 0,
        "both exact writer inverses return the coherent terminal image to blank and neither writer leaves the full terminal sector invariant",
    )
    check(
        "independent-double-use-hostile",
        double_use_failures == 0,
        "both writers send their complete two-dimensional written images into the terminal complement with unit leak Gram on immediate second use",
    )
    check(
        "independent-finite-absorption-premises",
        PB.rank() == 2 and PT.rank() == 6 and zero(PB * PT),
        "the exact finite dimensions and orthogonality instantiate the subspace proof that one unitary cannot both enter and absorb into T",
    )

    k0 = sp.Matrix(((0, 0), (1, 0)))
    k1 = sp.Matrix(((0, 0), (0, 1)))

    def reset(rho: sp.Matrix) -> sp.Matrix:
        return sp.simplify(k0 * rho * k0.H + k1 * rho * k1.H)

    check(
        "independent-irreversible-escape",
        zero(k0.H * k0 + k1.H * k1 - I2)
        and reset(sp.diag(1, 0)) == sp.diag(0, 1)
        and reset(sp.diag(0, 1)) == sp.diag(0, 1),
        "an independently written finite two-Kraus reset enters and fixes a terminal atom, so the obstruction cannot be widened beyond reversibility",
    )


def scope_controls() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "single finite-dimensional reversible update",
        "scheduled reversible write/future pair",
        "finite irreversible instrument",
        "infinite/increasing archive",
        "regional pointer algebra",
        "not a framework site record",
        "central-restriction compatibility",
        "actual-member correlation",
        "no axiom amendment",
        "obligation retirement: zero",
        "toe percentage movement: zero",
        "fail / do not ship",
    )
    check(
        "independent-honesty-boundary",
        all(phrase in text for phrase in required),
        "the note preserves every positive escape and separates the bounded carrier theorem from Record registration, law equality, actuality, and axiom status",
    )


def main() -> int:
    independent_program_controls()
    explicit_completion_controls()
    presence_and_stage_controls()
    center_and_qnd_controls()
    reversible_boundary_controls()
    scope_controls()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
