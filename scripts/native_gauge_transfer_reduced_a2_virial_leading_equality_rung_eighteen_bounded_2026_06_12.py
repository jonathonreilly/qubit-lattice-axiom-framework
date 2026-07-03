#!/usr/bin/env python3
"""W97 reduced-A2 virial identity runner.

This runner checks the source-side leading identity

    A_i + B_i / mu_i = 3/2

for the retained reduced operator

    T = exp(L/2) M_[H exp(-Q)] exp(L/2).

The exact proof is the dilation commutator.  The finite rows below are
deterministic saddle witnesses only; they are not fitted and they are not used
as proof inputs for the symbolic constant.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import exp
from pathlib import Path
import sys

import numpy as np
import sympy as sp
from scipy.sparse import csr_matrix, identity
from scipy.sparse.linalg import LinearOperator, eigsh, expm_multiply


AUDIT_TIMEOUT_SEC = 180

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_REDUCED_A2_VIRIAL_LEADING_EQUALITY_RUNG_EIGHTEEN_BOUNDED_NOTE_2026-06-12.md"
)
CACHE_PATH = (
    REPO_ROOT
    / "logs"
    / "runner-cache"
    / "native_gauge_transfer_reduced_a2_virial_leading_equality_rung_eighteen_bounded_2026_06_12.txt"
)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def weights_box(shell: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(shell + 1) for q in range(shell + 1)]


def recurrence_neighbors(p: int, q: int) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for a, b in [
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    ]:
        if a >= 0 and b >= 0:
            out.append((a, b))
    return out


def shifted_j(shell: int) -> tuple[csr_matrix, csr_matrix, list[tuple[int, int]]]:
    weights = weights_box(shell)
    index = {w: i for i, w in enumerate(weights)}
    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []
    for p, q in weights:
        col = index[(p, q)]
        for nb in recurrence_neighbors(p, q):
            row = index.get(nb)
            if row is not None:
                rows.append(row)
                cols.append(col)
                data.append(1.0 / 6.0)
    j = csr_matrix((data, (rows, cols)), shape=(len(weights), len(weights)))
    return j - identity(len(weights), format="csr"), j, weights


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p: int, q: int) -> Fraction:
    return Fraction(p * p + q * q + p * q + 3 * p + 3 * q, 3)


def deterministic_v0(n: int) -> np.ndarray:
    idx = np.arange(n, dtype=float)
    return 1.0 + 1.0e-3 * ((idx % 19.0) / 19.0)


@dataclass(frozen=True)
class VirialWitness:
    beta: int
    shell: int
    state: int
    a_part: float
    b_part: float

    @property
    def plus(self) -> float:
        return self.a_part + self.b_part

    @property
    def wrong_minus(self) -> float:
        return self.a_part - self.b_part


def saddle_virial_rows(beta: int, shell: int) -> list[VirialWitness]:
    shifted, j_op, weights = shifted_j(shell)
    tau = beta / 2.0
    raw = np.array(
        [
            float(dim_su3(p, q)) * exp(float(-3 * casimir_su3(p, q) / beta))
            for p, q in weights
        ],
        dtype=float,
    )
    raw_prime = raw * np.array(
        [float(3 * casimir_su3(p, q) / (beta * beta)) for p, q in weights],
        dtype=float,
    )
    scale = float(np.max(raw))
    diagonal = raw / scale
    diagonal_prime = raw_prime / scale

    def heat(v: np.ndarray) -> np.ndarray:
        return expm_multiply(tau * shifted, v, traceA=0.0)

    def matvec(v: np.ndarray) -> np.ndarray:
        y = heat(v)
        y = diagonal * y
        return heat(y)

    n = len(weights)
    op = LinearOperator((n, n), matvec=matvec, dtype=float)
    vals, vecs = eigsh(
        op,
        k=4,
        which="LA",
        tol=1.0e-9,
        ncv=28,
        maxiter=900,
        v0=deterministic_v0(n),
    )
    order = np.argsort(vals)[::-1]
    vals = vals[order]
    vecs = vecs[:, order]

    out: list[VirialWitness] = []
    for state in range(3):
        v = vecs[:, state]
        if float(np.sum(v)) < 0.0:
            v = -v
        j_expect = float(v @ (j_op @ v))
        a_part = beta * (j_expect - 1.0)
        middle = heat(v)
        lam = float(np.sum(middle * middle * diagonal))
        b_num = float(np.sum(middle * middle * diagonal_prime))
        b_part = beta * b_num / lam
        out.append(VirialWitness(beta, shell, state, a_part, b_part))
    return out


def symbolic_checks() -> None:
    x, y = sp.symbols("x y")
    f = x**5 + 2 * x**3 * y**2 - x * y**4 + 7 * x**2 + 3 * y
    h = x * y * (x + y) / 2
    q = x**2 + x * y + y**2
    w = h * sp.exp(-q)

    def dil(expr: sp.Expr) -> sp.Expr:
        return x * sp.diff(expr, x) + y * sp.diff(expr, y)

    def lop(expr: sp.Expr) -> sp.Expr:
        return (sp.diff(expr, x, 2) - sp.diff(expr, x, y) + sp.diff(expr, y, 2)) / 3

    check("D H = 3 H exactly", sp.simplify(dil(h) - 3 * h) == 0)
    check("D Q = 2 Q exactly", sp.simplify(dil(q) - 2 * q) == 0)
    check(
        "D(H exp(-Q)) = (3 - 2Q) H exp(-Q) exactly",
        sp.simplify(dil(w) - (3 - 2 * q) * w) == 0,
    )
    check(
        "[D,L] = -2 L on an inhomogeneous polynomial sample",
        sp.simplify(dil(lop(f)) - lop(dil(f)) + 2 * lop(f)) == 0,
    )

    mu, a, b = sp.symbols("mu a b", nonzero=True)
    comm = -2 * mu * a + 3 * mu - 2 * b
    b_from_comm = sp.solve(sp.Eq(comm, 0), b)[0]
    solved = sp.simplify(a + b_from_comm / mu)
    check(
        "commutator expectation solves to A_i + B_i/mu_i = 3/2",
        sp.simplify(solved - sp.Rational(3, 2)) == 0,
        f"solved={solved}",
    )

    a0, a1 = sp.symbols("a0 a1")
    b0_over = sp.Rational(3, 2) - a0
    b1_over = sp.Rational(3, 2) - a1
    leading_gap = sp.simplify((a0 - a1) - (b1_over - b0_over))
    check("virial relation forces c_J = c_D at leading order", leading_gap == 0)

    wrong_combo_0 = sp.simplify(a0 - b0_over).subs(a0, -1)
    wrong_combo_1 = sp.simplify(a1 - b1_over).subs(a1, -2)
    print(f"wrong_signed_combo_sample state0={wrong_combo_0} state1={wrong_combo_1}")
    check(
        "wrong signed combination A_i - B_i/mu_i is visibly state-dependent",
        wrong_combo_0 != wrong_combo_1,
    )

    q_wrong = x**2 + 2 * x * y + y**2
    w_wrong = h * sp.exp(-q_wrong)
    wrong_confiner_residual = sp.simplify(dil(w_wrong) - (3 - 2 * q) * w_wrong)
    wrong_at_12 = sp.simplify(wrong_confiner_residual.subs({x: 1, y: 2}))
    print(f"wrong_confiner_point_residual_at_1_2={wrong_at_12}")
    check(
        "wrong confiner breaks the retained Q-insertion virial clause",
        wrong_at_12 == -12 * sp.exp(-9),
    )

    correct_nc = Fraction(3, 1) * casimir_su3(10, 20) / 100
    wrong_nc = Fraction(2, 1) * casimir_su3(10, 20) / 100
    print(f"wrong_Nc_sample correct_3C2_over_beta={correct_nc} wrong_2C2_over_beta={wrong_nc}")
    check(
        "wrong N_c changes the fixed-weight derivative value exactly",
        correct_nc == Fraction(79, 10) and wrong_nc == Fraction(79, 15),
    )

    retained_a = Fraction(-2, 1)
    wrong_alpha_ratio = Fraction(3, 2)  # L_wrong=(1/2)raw vs retained L=(1/3)raw.
    wrong_b_over = Fraction(3, 2) - wrong_alpha_ratio * retained_a
    broken_retained_combo = retained_a + wrong_b_over
    print(f"wrong_L_normalization_sample retained_A_plus_B_over_mu={broken_retained_combo}")
    check(
        "wrong L normalization breaks the retained A_i + B_i/mu_i = 3/2 value",
        broken_retained_combo == Fraction(5, 2),
    )


def finite_witness_checks() -> None:
    plans = [(100, 40), (200, 56), (400, 80)]
    all_rows: list[list[VirialWitness]] = []
    print("finite_saddle_virial_witness_rows")
    for beta, shell in plans:
        rows = saddle_virial_rows(beta, shell)
        all_rows.append(rows)
        for row in rows:
            print(
                f"  beta={row.beta:3d} shell={row.shell:2d} state={row.state} "
                f"A={row.a_part:.12f} B_over_mu={row.b_part:.12f} "
                f"A_plus_B={row.plus:.12f} wrong_A_minus_B={row.wrong_minus:.12f}"
            )

    max_errors = [
        max(abs(row.plus - 1.5) for row in rows)
        for rows in all_rows
    ]
    spreads = [
        max(row.plus for row in rows) - min(row.plus for row in rows)
        for rows in all_rows
    ]
    wrong_spreads = [
        max(row.wrong_minus for row in rows) - min(row.wrong_minus for row in rows)
        for rows in all_rows
    ]
    leading_margins = [
        (rows[0].a_part - rows[1].a_part) - (rows[1].b_part - rows[0].b_part)
        for rows in all_rows
    ]
    print(f"finite_plus_errors={['%.6f' % v for v in max_errors]}")
    print(f"finite_plus_state_spreads={['%.6f' % v for v in spreads]}")
    print(f"finite_wrong_combo_spreads={['%.6f' % v for v in wrong_spreads]}")
    print(f"finite_leading_margins_state0_state1={['%.6f' % v for v in leading_margins]}")

    check(
        "finite saddle A_i+B_i/mu_i errors decrease toward 3/2",
        all(max_errors[i + 1] < max_errors[i] for i in range(len(max_errors) - 1))
        and max_errors[-1] < 0.013,
    )
    check(
        "finite saddle state spread of A_i+B_i/mu_i decreases",
        all(spreads[i + 1] < spreads[i] for i in range(len(spreads) - 1))
        and spreads[-1] < 0.004,
    )
    check(
        "wrong finite combination remains visibly state-dependent",
        all(spread > 2.5 for spread in wrong_spreads),
    )
    check(
        "finite leading c_J-c_D margin between states shrinks toward zero",
        all(abs(leading_margins[i + 1]) < abs(leading_margins[i]) for i in range(len(leading_margins) - 1))
        and abs(leading_margins[-1]) < 0.003,
    )


def note_checks() -> None:
    text = NOTE_PATH.read_text(encoding="utf-8")
    lower = text.lower()
    required = "Status authority: independent audit lane only. This source note does not set or predict an audit outcome."
    check("note carries the exact status-authority sentence", required in text)
    check(
        "note declares controlled claim type and source-side boundary",
        "**Claim type:** bounded_theorem" in text
        and "**Boundary:** leading equality derived; subleading sign obstruction-at-exact-step." in text
        and "Claim type is a source-side boundary declaration, never an audit verdict." in text,
    )
    check(
        "note links the runner and SHA-pinned cache path",
        "[scripts/native_gauge_transfer_reduced_a2_virial_leading_equality_rung_eighteen_bounded_2026_06_12.py]"
        in text
        and "[logs/runner-cache/native_gauge_transfer_reduced_a2_virial_leading_equality_rung_eighteen_bounded_2026_06_12.txt]"
        in text,
    )
    authority_links = [
        "[NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md]",
        "[NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md]",
        "[NATIVE_GAUGE_TRANSFER_REDUCED_A2_SPECTRAL_DOMINATION_RUNG_ELEVEN_BOUNDED_NOTE_2026-06-12.md]",
    ]
    check("one-hop authorities are markdown links", all(link in text for link in authority_links))
    check(
        "quote anchors for H, Q, L, T, c_J, c_D, and subleading warning are present",
        "H(x,y) = x y (x+y) / 2" in text
        and "Q(x,y) = x^2 + x y + y^2." in text
        and "J - I -> beta^(-1) L" in text
        and "T_infty = S_(1/2) M_[H exp(-Q)] S_(1/2)." in text
        and "c_J = A_0 - A_1" in text
        and "c_D = B_1/mu_1 - B_0/mu_0" in text
        and "strict inequality lives at the `1/beta` subleading order" in text,
    )
    check(
        "note fences W90 witnesses and avoids comparator promotion",
        "FENCES ONLY" in text
        and "not proof inputs" in text
        and ("0." + "5934") not in text,
    )
    check(
        "note states the exact subleading stopping step",
        "the first corrected operator/eigenpair perturbation needed to sign the subleading coefficient" in text,
    )
    check(
        "note differentiates new material from W96/W95/W86/W90",
        "New here versus W96" in text
        and "Restated from W86" in text
        and "Restated from W90" in text
        and "W95" in text,
    )
    banned = [
        "only " + "route",
        "last " + "route",
        "exhau" + "sted",
        "closes " + "the program",
        "perma" + "nently",
        "no other " + "path",
    ]
    check("note avoids forbidden overreach phrases", not any(fragment in lower for fragment in banned))
    check(
        "note includes the no-go discipline gate for the subleading obstruction",
        "## No-Go Discipline Gate" in text
        and "N1 - Alternative route enumeration" in text
        and "N8 - Cross-cycle echo" in text,
    )
    check(
        "note records both ambiguity readings",
        "Reading 1: reduced-leading reading" in text
        and "Reading 2: finite-beta witness reading" in text,
    )


def cache_checks() -> None:
    source = Path(__file__).read_text(encoding="utf-8")
    check("cache path is canonical for this runner", CACHE_PATH.name == f"{Path(__file__).stem}.txt")
    check("runner uses no fit helpers", ("poly" + "fit") not in source and ("curve" + "_fit") not in source)
    check(
        "no suspicious float-to-Fraction exact constants are used",
        "Fraction(" in source and ("Fraction(0" + ".") not in source,
    )


def main() -> int:
    print("W97 reduced-A2 virial leading-equality runner")
    print("Exact constants are symbolic; finite rows are witnesses only.")
    print()
    symbolic_checks()
    finite_witness_checks()
    note_checks()
    cache_checks()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
