#!/usr/bin/env python3
"""Exact supplied-sector checks for outcome-forgotten dilation freedom.

The physical input is the one-excitation sector of two neighboring sites.
Every use appends one fresh classical label; completed labels are thereafter
idle.  The construction supplies a discrete composition step and CP-instrument
weights as hypotheses.  It derives neither a clock nor the Born rule.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label}: {detail}")


I2 = sp.eye(2)
I4 = sp.eye(4)
P_LEFT = sp.diag(1, 0)
P_RIGHT = sp.diag(0, 1)
SWAP_EDGE = sp.Matrix([[0, 1], [1, 0]])
SWAP_FULL = sp.Matrix(
    [
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
    ]
)
Q = sp.Rational(1, 3)


def scalar_exchange(theta: sp.Expr) -> sp.Matrix:
    """exp[-i theta (I-SWAP)] on span{|10>,|01>}."""
    return sp.exp(-sp.I * theta) * (
        sp.cos(theta) * I2 + sp.I * sp.sin(theta) * SWAP_EDGE
    )


def kraus_family(theta: sp.Expr) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    return (
        sp.sqrt(Q) * scalar_exchange(theta),
        sp.sqrt(1 - Q) * P_LEFT,
        sp.sqrt(1 - Q) * P_RIGHT,
    )


def vec(matrix: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(matrix).reshape(matrix.rows * matrix.cols, 1)


def outcome_forgotten_choi(kraus: tuple[sp.Matrix, ...]) -> sp.Matrix:
    return sum((vec(operator) * vec(operator).H for operator in kraus), sp.zeros(4, 4))


def branch_weight(
    theta: sp.Expr,
    history: tuple[int, ...],
    rho: sp.Matrix,
) -> sp.Expr:
    operators = kraus_family(theta)
    product = I2
    for outcome in history:
        product = operators[outcome] * product
    return sp.simplify(sp.trace(product * rho * product.H))


def eventual_first_outcome_weight(
    theta: sp.Expr,
    period: int,
    outcome_projector: sp.Matrix,
    rho: sp.Matrix,
) -> sp.Expr:
    """Sum the absorbing first-nonempty-outcome weight exactly.

    For the two angles used below, the displayed outcome probabilities are
    periodic with the supplied period.  The geometric denominator performs
    the infinite sum exactly.
    """
    unitary = scalar_exchange(theta)
    one_period = sp.Integer(0)
    for attempt in range(period):
        evolved = unitary**attempt * rho * (unitary.H) ** attempt
        one_period += Q**attempt * sp.trace(outcome_projector * evolved)
    return sp.simplify((1 - Q) * one_period / (1 - Q**period))


def classification_checks() -> None:
    theta = sp.symbols("theta", real=True)
    unitary = scalar_exchange(theta)
    check("C01", sp.simplify(unitary.H * unitary - I2) == sp.zeros(2), "U_theta is unitary for real theta")
    check("C02", sp.simplify(scalar_exchange(sp.pi / 2) - SWAP_EDGE) == sp.zeros(2), "theta=pi/2 is exactly the edge SWAP")
    pauli = (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.diag(1, -1),
    )
    common_frame_ok = all(
        sp.simplify(
            SWAP_FULL * (sp.kronecker_product(axis, I2) + sp.kronecker_product(I2, axis))
            - (sp.kronecker_product(axis, I2) + sp.kronecker_product(I2, axis)) * SWAP_FULL
        )
        == sp.zeros(4)
        for axis in pauli
    )
    check("C03a", common_frame_ok, "full two-qubit SWAP commutes with all common-frame su(2) generators")
    check("C03b", sp.simplify(SWAP_FULL * (I4 - SWAP_FULL) - (I4 - SWAP_FULL) * SWAP_FULL) == sp.zeros(4), "I-SWAP is even under reversal of the unoriented edge")

    for suffix, angle in (("a", sp.pi / 4), ("b", sp.pi / 2)):
        kraus = kraus_family(angle)
        resolution = sum((operator.H * operator for operator in kraus), sp.zeros(2))
        dilation = sp.Matrix.vstack(*kraus)
        span_rank = sp.Matrix.hstack(*(vec(operator) for operator in kraus)).rank()
        choi_rank = outcome_forgotten_choi(kraus).rank()
        check(f"C04{suffix}", sp.simplify(resolution - I2) == sp.zeros(2), f"full three-outcome instrument is normalized at theta={angle}")
        check(f"C05{suffix}", sp.simplify(dilation.H * dilation - I2) == sp.zeros(2), f"block-column dilation is an isometry at theta={angle}")
        check(f"C06{suffix}", span_rank == 3, f"K_empty,K_left,K_right are linearly independent at theta={angle}")
        check(f"C07{suffix}", choi_rank == 3, f"outcome-forgotten channel has minimal Kraus/Stinespring rank three at theta={angle}")

    # Exact one-Kraus completion classification: after the two fixed nonempty
    # effects consume (1-q)I, normalization leaves K_empty^dag K_empty=qI.
    residual = I2 - (1 - Q) * (P_LEFT + P_RIGHT)
    check("C08", residual == Q * I2, "normalization fixes the no-record effect to qI")
    for suffix, angle in (("a", sp.pi / 4), ("b", sp.pi / 2)):
        k_empty = kraus_family(angle)[0]
        check(f"C09{suffix}", sp.simplify(k_empty.H * k_empty - Q * I2) == sp.zeros(2), "K_empty=sqrt(q)U realizes the complete one-Kraus polar family")


def one_step_and_history_checks() -> None:
    angles = (sp.pi / 4, sp.pi / 2)
    families = tuple(kraus_family(angle) for angle in angles)

    for outcome, name in enumerate(("empty", "left", "right")):
        effects = tuple(sp.simplify(family[outcome].H * family[outcome]) for family in families)
        check(f"E{outcome + 1:02d}", effects[0] == effects[1], f"one-step {name} effect is theta-independent")

    r00, r01, r10, r11 = sp.symbols("r00 r01 r10 r11")
    rho_generic = sp.Matrix([[r00, r01], [r10, r11]])
    for outcome, name in ((1, "left"), (2, "right")):
        branches = tuple(
            sp.simplify(family[outcome] * rho_generic * family[outcome].H)
            for family in families
        )
        check(f"E{outcome + 3:02d}", branches[0] == branches[1], f"one-step nonempty outcome branch {name} is theta-independent")

    no_record_branches = tuple(
        sp.simplify(family[0] * P_LEFT * family[0].H)
        for family in families
    )
    check("E06", no_record_branches[0] != no_record_branches[1], "the full instruments differ in their no-record operation")

    # History labels: 0=empty, 1=left, 2=right.  The raw
    # twice-composed channel check below is an auxiliary TP algebra check.  The
    # physical stopping process instead terminates at the first nonempty outcome; its
    # horizon-two tree and eventual distribution are checked separately.
    rho_left = P_LEFT
    p_quarter_right = branch_weight(sp.pi / 4, (0, 2), rho_left)
    p_half_right = branch_weight(sp.pi / 2, (0, 2), rho_left)
    p_quarter_left = branch_weight(sp.pi / 4, (0, 1), rho_left)
    p_half_left = branch_weight(sp.pi / 2, (0, 1), rho_left)
    check("H01", p_quarter_right == sp.Rational(1, 9), "p_pi/4(empty,right)=q(1-q)/2=1/9")
    check("H02", p_half_right == sp.Rational(2, 9), "p_pi/2(empty,right)=q(1-q)=2/9")
    check("H03", p_quarter_left == sp.Rational(1, 9), "p_pi/4(empty,left)=q(1-q)/2=1/9")
    check("H04", p_half_left == 0, "p_pi/2(empty,left)=0")
    check("H05", p_quarter_right != p_half_right, "exchange angle changes an outcome-resolved two-step label weight")

    for suffix, angle in (("a", sp.pi / 4), ("b", sp.pi / 2)):
        total = sum(
            (branch_weight(angle, (first, second), rho_left) for first in range(3) for second in range(3)),
            sp.Integer(0),
        )
        check(f"H06{suffix}", sp.simplify(total - 1) == 0, f"auxiliary twice-composed TP-map weights normalize at theta={angle}")
        absorbing_total = (
            branch_weight(angle, (1,), rho_left)
            + branch_weight(angle, (2,), rho_left)
            + sum(
                (branch_weight(angle, (0, second), rho_left) for second in range(3)),
                sp.Integer(0),
            )
        )
        check(f"H06{suffix}A", sp.simplify(absorbing_total - 1) == 0, f"absorbing horizon-two terminal tree normalizes at theta={angle}")

    coarse_quarter = p_quarter_left + p_quarter_right
    coarse_half = p_half_left + p_half_right
    check("H07", coarse_quarter == coarse_half == Q * (1 - Q), "side-forgotten outcome coarse graining cannot distinguish theta")

    # The exchange branch is channel-intrinsic rather than Stinespring gauge:
    # it changes the system output on a fixed input and therefore cannot be
    # removed by an environment-unitary change of Kraus representation.
    channel_outputs = []
    for family in families:
        channel_outputs.append(sum((operator * rho_left * operator.H for operator in family), sp.zeros(2)))
    check("H08", channel_outputs[0] != channel_outputs[1], "outcome-forgotten CP channels differ, so theta is not dilation gauge")

    eventual_quarter_right = eventual_first_outcome_weight(sp.pi / 4, 4, P_RIGHT, rho_left)
    eventual_half_right = eventual_first_outcome_weight(sp.pi / 2, 2, P_RIGHT, rho_left)
    eventual_quarter_left = eventual_first_outcome_weight(sp.pi / 4, 4, P_LEFT, rho_left)
    eventual_half_left = eventual_first_outcome_weight(sp.pi / 2, 2, P_LEFT, rho_left)
    check("H09", eventual_quarter_right == sp.Rational(1, 5), "absorbing eventual first-nonempty-outcome right weight is 1/5 at theta=pi/4")
    check("H10", eventual_half_right == sp.Rational(1, 4), "absorbing eventual first-nonempty-outcome right weight is 1/4 at theta=pi/2")
    check("H11", eventual_quarter_right != eventual_half_right, "exchange angle changes the eventual absorbing label distribution")
    check("H12", eventual_quarter_left + eventual_quarter_right == 1, "eventual first-nonempty-outcome labels normalize at theta=pi/4")
    check("H13", eventual_half_left + eventual_half_right == 1, "eventual first-nonempty-outcome labels normalize at theta=pi/2")


def source_boundary_checks() -> None:
    note = Path("docs/MINIMAL_RECORD_INSTRUMENT_DILATION_SCALAR_EXCHANGE_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md")
    check("S01", note.exists(), "source note exists")
    text = note.read_text() if note.exists() else ""
    required = (
        "one-excitation sector of one unoriented edge",
        "fresh append-only outcome register",
        "does not construct a simultaneous translation-covariant cubic QCA",
        "does not derive the Born rule",
        "does not establish that the axioms require amendment",
        "Minimal outcome-forgotten-channel rank does not select the exchange angle",
    )
    for index, marker in enumerate(required, 1):
        check(f"S{index + 1:02d}", marker in text, f"source contains boundary marker: {marker}")


def main() -> int:
    classification_checks()
    one_step_and_history_checks()
    source_boundary_checks()
    print("BOUNDARY: minimality is relative to the supplied finite CP instrument/channel, not a derivation of that instrument from the axioms.")
    print("BOUNDARY: absorbing label histories use a fresh append-only register that is not derived as a framework Record.")
    print("BOUNDARY: the witness is a supplied one-excitation edge sector, not the full edge algebra, a cubic QCA, or a continuum theory.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
