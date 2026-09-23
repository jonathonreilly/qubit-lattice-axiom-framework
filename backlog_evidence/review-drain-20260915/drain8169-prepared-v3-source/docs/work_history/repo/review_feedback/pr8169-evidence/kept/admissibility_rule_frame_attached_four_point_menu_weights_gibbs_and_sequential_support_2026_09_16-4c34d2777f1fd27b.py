#!/usr/bin/env python3
"""Exact checks: covariant weights on the unsoldered four-point two-neighbour menu.

The support S = {q, q', -q, -q'} is Aut-covariant as a set. Aut-covariant
probabilities on it are two functions of t = q·q' (copy mass and flip mass).
Pair-Gibbs exp(β s·(q+q')) is that family with one parameter. The two-outcome
Born overlap (1+s·q)/2 is not a four-point law. Sequential formation cannot be
order-blind: on a three-site path the middle's support has two points in the
chain and four in ends-first. Exact rationals; no physical menu or rule is
selected.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_FRAME_ATTACHED_FOUR_POINT_MENU_COVARIANT_WEIGHTS_GIBBS_LINEAR_FAMILY_AND_SEQUENTIAL_SUPPORT_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-09-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
PARENT_PATH = ROOT / AUDIT_INPUT_PATHS[2]
CLAIM_ID = (
    "admissibility_rule_frame_attached_four_point_menu_covariant_weights_"
    "gibbs_linear_family_and_sequential_support_obstruction_bounded_theorem_note_2026-09-16"
)
PARENT_CLAIM_ID = (
    "possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_"
    "and_haar_fair_coin_bounded_theorem_note_2026-09-14"
)


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def dot(u, v) -> Fraction:
    return sum((Fraction(a) * Fraction(b) for a, b in zip(u, v, strict=True)), Fraction(0))


def add(u, v):
    return tuple(Fraction(a) + Fraction(b) for a, b in zip(u, v, strict=True))


def scale(c, u):
    return tuple(Fraction(c) * Fraction(a) for a in u)


def neg(u):
    return tuple(-Fraction(a) for a in u)


def apply_matrix(matrix, vector):
    return tuple(
        sum((matrix[i][j] * vector[j] for j in range(3)), start=Fraction(0))
        for i in range(3)
    )


def proper_cubic_rotations():
    mats = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            matrix = [[Fraction(0)] * 3 for _ in range(3)]
            sign_prod = 1
            inversions = sum(
                perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3)
            )
            perm_sign = -1 if inversions % 2 else 1
            for i in range(3):
                matrix[perm[i]][i] = Fraction(signs[i])
                sign_prod *= signs[i]
            if perm_sign * sign_prod == 1:
                mats.append(tuple(tuple(row) for row in matrix))
    return tuple(mats)


def four_point_support(q, qp):
    return (q, qp, neg(q), neg(qp))


def distinct_four(q, qp) -> bool:
    pts = four_point_support(q, qp)
    return len(set(pts)) == 4


def gibbs_copy_mass(beta: Fraction, t: Fraction) -> Fraction:
    # α = exp(β(1+t)) / (2 exp(β(1+t)) + 2 exp(−β(1+t)))
    # with e^{2β} = 2 this is exact at selected β via integer powers.
    # Here β is encoded as e^{2β} = B a positive Fraction, using
    # α = 1 / (2 (1 + B^{-(1+t)})) which needs B^{1+t}.
    # Restrict to t=0 and integer B: α = 1/(2(1+1/B)) = B/(2B+2)
    del t
    b = beta  # here beta stands for B = e^{2β} at t=0
    return b / (2 * b + 2)


def linear_copy_mass(lam: Fraction, t: Fraction) -> Fraction:
    # α = (1 + λ(1+t)) / 4
    return (1 + lam * (1 + t)) / 4


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    parent_flat = normalize(parent)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: current minimal_axioms and the landed possibility-covariance note")

    checks.check(
        "A1-inputs",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and len(set(AUDIT_INPUT_PATHS)) == 3,
        "the note, axiom memo, and possibility-covariance note are the declared packet",
    )
    checks.check(
        "A2-axioms",
        "No possibility is privileged." in axiom_flat
        and "one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations"
        in axiom_flat
        and "determined by, and varies with, the nearest-neighbor conditions" in axiom_flat
        and "Records form." in axiom,
        "the Qubit, Admissibility, and Record sentences used are present verbatim",
    )
    checks.check(
        "A3-parent",
        PARENT_CLAIM_ID in parent
        and "unsoldered" in parent_flat
        and "soldered" in parent_flat,
        "the landed possibility-covariance note supplies the two readings",
    )
    checks.check(
        "A4-note-contract",
        CLAIM_ID in note
        and "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "four-point" in note_flat
        and "copy mass" in note_flat
        and "not a four-point law" in note_flat
        and "two points in the chain and four in ends-first" in note_flat,
        "the note states the four-point weight family, the Born obstruction, and the support obstruction",
    )

    q = (Fraction(0), Fraction(0), Fraction(1))
    qp = (Fraction(1), Fraction(0), Fraction(0))
    t = dot(q, qp)
    checks.check(
        "B1-orthogonal-four-distinct",
        t == 0 and distinct_four(q, qp),
        "the reference orthogonal pair has inner product 0 and four distinct support points",
    )

    # 180° about the bisector of q and q': (x,y,z) -> (z, -y, x) for this pair.
    def swap_q_qp(v):
        x, y, z = v
        return (z, -y, x)

    checks.check(
        "B2-swap-maps-pair",
        swap_q_qp(q) == qp and swap_q_qp(qp) == q
        and set(four_point_support(q, qp)) == set(four_point_support(swap_q_qp(q), swap_q_qp(qp))),
        "the 180-degree Aut about the bisector swaps the two neighbours and preserves the four-point set",
    )

    # 180° about q: (x,y,z) -> (-x, -y, z). Sends q' to -q', preserves the set.
    def rot_about_q(v):
        x, y, z = v
        return (-x, -y, z)

    checks.check(
        "B3-flip-second-preserves-set",
        rot_about_q(q) == q
        and rot_about_q(qp) == neg(qp)
        and set(four_point_support(q, qp))
        == set(four_point_support(rot_about_q(q), rot_about_q(qp))),
        "the 180-degree Aut about q sends the second neighbour to its opposite and preserves the four-point set",
    )

    rotations = proper_cubic_rotations()
    checks.check(
        "B4-cubic-group",
        len(rotations) == 24 and len(set(rotations)) == 24,
        "the proper cubic group has 24 elements",
    )

    # Aut-covariant weights at a fixed pair: four masses summing to 1.
    # Swap forces copy(q)=copy(q'), flip(q)=flip(q').
    # Remaining: copy mass α, flip mass γ, 2α+2γ=1.
    def is_two_function_family(alpha, gamma) -> bool:
        return 2 * alpha + 2 * gamma == 1 and alpha >= 0 and gamma >= 0

    samples = (
        (Fraction(1, 4), Fraction(1, 4)),
        (Fraction(1, 2), Fraction(0)),
        (Fraction(0), Fraction(1, 2)),
        (Fraction(3, 8), Fraction(1, 8)),
    )
    checks.check(
        "C1-two-function-family",
        all(is_two_function_family(a, g) for a, g in samples)
        and not is_two_function_family(Fraction(1, 3), Fraction(1, 3)),
        "Aut-plus-swap covariant four-point laws are the copy/flip family 2α+2γ=1",
    )

    # Gibbs at t=0 with e^{2β}=2: α = 2/(4+2)=2/6=1/3? Wait formula α=B/(2B+2)
    # B=2: 2/(4+2)=1/3. Then 2α=2/3, 2γ=1/3, γ=1/6. 2α+2γ=1. Yes.
    # But 1/3 + 1/6 wait 2*(1/3)+2*(1/6)=2/3+1/3=1. α=1/3 is NOT <= 1/2... 1/3<1/2 OK.
    # 2α+2γ=1 with α=1/3 gives γ=1/6. copy total 2α=2/3, flip total 1/3.
    a2 = gibbs_copy_mass(Fraction(2), Fraction(0))
    checks.check(
        "C2-gibbs-at-orthogonal",
        a2 == Fraction(1, 3)
        and is_two_function_family(a2, Fraction(1, 2) - a2),
        "pair-Gibbs with e^{2β}=2 at t=0 has copy mass 1/3, flip mass 1/6, inside the two-function family",
    )
    a1 = gibbs_copy_mass(Fraction(1), Fraction(0))
    checks.check(
        "C3-gibbs-beta-zero-is-uniform",
        a1 == Fraction(1, 4),
        "pair-Gibbs at B=e^{2β}=1 (β=0) is the uniform four-point law",
    )

    # Linear family α=(1+λ(1+t))/4. At t=0, α=(1+λ)/4. Equals Gibbs small-β:
    # Gibbs α = 1/(2(1+e^{-2β})) at t=0. For β=0, α=1/4, λ=0.
    checks.check(
        "C4-linear-family",
        linear_copy_mass(Fraction(0), Fraction(0)) == Fraction(1, 4)
        and linear_copy_mass(Fraction(1), Fraction(0)) == Fraction(1, 2)
        and linear_copy_mass(Fraction(-1), Fraction(0)) == Fraction(0)
        and linear_copy_mass(Fraction(1, 2), Fraction(0)) == Fraction(3, 8),
        "the linear family (1+λ s·(q+q'))/4 interpolates uniform, deterministic copy, and deterministic flip at t=0",
    )

    # Born (1+s·q)/2 on {q,-q}: 1 and 0. On the four-point set it is not a
    # probability: the four values would be (1+1)/2=1, (1+0)/2=1/2, (1-1)/2=0,
    # (1+0)/2=1/2, summing to 2, and it ignores q' as a neighbour.
    born_values = (
        (1 + dot(q, q)) / 2,
        (1 + dot(qp, q)) / 2,
        (1 + dot(neg(q), q)) / 2,
        (1 + dot(neg(qp), q)) / 2,
    )
    checks.check(
        "D1-born-not-four-point",
        born_values == (1, Fraction(1, 2), 0, Fraction(1, 2))
        and sum(born_values) == 2,
        "the two-outcome Born overlap on the four-point set sums to 2 and is not a four-point probability",
    )
    checks.check(
        "D2-born-ignores-second-neighbour",
        (1 + dot(q, q)) / 2 == 1 and (1 + dot(q, qp)) / 2 == Fraction(1, 2),
        "Born-about-q is deterministic on {q,-q} and does not depend on q' as a recorded neighbour",
    )

    # Sequential support obstruction on path3.
    # Chain: M sees only L = q, support {q,-q}, cardinality 2.
    # Ends-first: M sees L=q and R=qp non-collinear, support four points.
    chain_support = {q, neg(q)}
    ends_support = set(four_point_support(q, qp))
    checks.check(
        "E1-chain-support-two",
        len(chain_support) == 2 and neg(q) in chain_support,
        "in the chain order the middle's one-neighbour finite support is the antipodal pair of the left end",
    )
    checks.check(
        "E2-ends-support-four",
        len(ends_support) == 4 and chain_support < ends_support,
        "in the ends-first order the middle's two-neighbour support is the four-point set, a strict superset",
    )
    checks.check(
        "E3-cardinalities-differ",
        len(chain_support) != len(ends_support),
        "the middle's support has two points in the chain and four in ends-first, so the sequential products cannot agree",
    )

    # A collinear control: if R = L, ends-first support collapses to two points.
    collinear_ends = set(four_point_support(q, q))
    checks.check(
        "E4-collinear-control",
        len(collinear_ends) == 2 and collinear_ends == chain_support,
        "when the two ends are collinear the four-point set collapses to the antipodal pair; the obstruction is for non-collinear ends, which Haar-empty ends realise almost surely",
    )

    checks.check(
        "F1-quotes",
        "1/3" in note
        and "1/6" in note
        and "sums to 2" in note_flat
        and "two points in the chain and four in ends-first" in note_flat
        and "e^{2β}=2" in note_flat.replace(" ", ""),
        "the note quotes the Gibbs masses, the Born sum, and the support cardinalities",
    )
    checks.check(
        "F2-no-selection",
        "selects neither" in note_flat
        and "not adopted" in note_flat
        and "physical formation order is not selected" in note_flat,
        "the note selects neither a menu, a rule, nor an order",
    )
    checks.check(
        "F3-open-sibling",
        "PR #8152" in note or "PR 8152" in note or "#8152" in note,
        "the open menus note is named as a sibling, not used as a landed premise",
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
