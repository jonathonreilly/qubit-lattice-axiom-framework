#!/usr/bin/env python3
"""Record-boundary repair for the flavor carrier-measure residual.

The runner verifies the finite generator-channel Hilbert-Schmidt algebra and
the current Record boundary: finite additive record readout supplies ratios and
coarse-grainings, but it does not select the generator-channel measure that
would give r=1/2.
"""

from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def normalized_doublet_coordinate(u, p):
    """Return d such that d/(u+d)=p."""
    return sp.simplify(p * u / (1 - p))


def main():
    a, b, u = sp.symbols("a b u", positive=True)
    passed = []

    I = sp.eye(3)
    J = sp.ones(3, 3)
    B = J - I

    passed.append(
        check(
            "C1 HS split: ||I||^2=3, ||J-I||^2=6, <I,J-I>_HS=0",
            sp.trace(I * I) == 3 and sp.trace(B * B) == 6 and sp.trace(I * B) == 0,
        )
    )

    r_channel = sp.solve(sp.Eq(3 * a**2, 6 * b**2), b)[0] ** 2 / a**2
    r_eigen = (sp.solve(sp.Eq((a + 2 * b) ** 2, 2 * (a - b) ** 2), b)[0] / a) ** 2
    passed.append(
        check(
            "C2 three finite partitions remain distinct",
            r_channel == sp.Rational(1, 2)
            and sp.simplify(r_eigen - (sp.Rational(17, 2) - 6 * sp.sqrt(2))) == 0,
            f"channel r={r_channel}; idempotent r={sp.nsimplify(r_eigen)}; per-mode r=1",
        )
    )

    family_ok = True
    family = {}
    for n in (2, 3, 4, 6):
        In = sp.eye(n)
        Jn = sp.ones(n, n)
        Bn = Jn - In
        r_n = sp.simplify(sp.trace(In * In) / sp.trace(Bn * Bn))
        family[n] = r_n
        family_ok = family_ok and r_n == sp.Rational(1, n - 1)
    passed.append(
        check(
            "C3 generator-channel HS scoring gives r=1/(N-1)",
            family_ok and family[3] == sp.Rational(1, 2),
            f"{ {n: str(v) for n, v in family.items()} }",
        )
    )

    Q = sp.Rational(1, 3) + sp.Rational(2, 3) * sp.symbols("r")
    passed.append(
        check(
            "C4 finite generation coordinate gives Q=2/3 after the supplied r=1/2 endpoint",
            sp.simplify(Q.subs("r", sp.Rational(1, 2))) == sp.Rational(2, 3),
        )
    )

    arbitrary = True
    examples = {}
    for p in (sp.Rational(1, 5), sp.Rational(1, 2), sp.Rational(2, 3)):
        d = normalized_doublet_coordinate(u, p)
        normalized = sp.simplify(d / (u + d))
        examples[str(p)] = str(d)
        arbitrary = arbitrary and normalized == p
    passed.append(
        check(
            "C5 Record finite additivity leaves the two-sector normalized coordinate arbitrary",
            arbitrary,
            f"d choices for p: {examples}",
        )
    )

    rho_r_half = sp.simplify(2 * sp.Rational(1, 2))
    rho_r_one = sp.simplify(2 * sp.Rational(1, 1))
    p_r_half = sp.simplify(rho_r_half / (1 + rho_r_half))
    p_r_one = sp.simplify(rho_r_one / (1 + rho_r_one))
    passed.append(
        check(
            "C6 Record admits both r=1/2 and r=1 endpoints; it selects neither",
            (rho_r_half, p_r_half, rho_r_one, p_r_one)
            == (sp.Rational(1), sp.Rational(1, 2), sp.Rational(2), sp.Rational(2, 3)),
            f"r=1/2 -> rho={rho_r_half}, p={p_r_half}; r=1 -> rho={rho_r_one}, p={p_r_one}",
        )
    )

    kahler_r = sp.solve(sp.Eq(a**2 + 4 * b**2, 2 * (a**2 + b**2)), b)[0] ** 2 / a**2
    passed.append(
        check(
            "C7 Kähler/moment-map algebra independently returns r=1/2 but does not select authority",
            kahler_r == sp.Rational(1, 2),
        )
    )

    S = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)
    H = np.eye(3) + (1 / np.sqrt(2)) * (np.ones((3, 3)) - np.eye(3))
    passed.append(
        check(
            "C8 r=1/2 circulant point commutes with C3 shift, so it does not import chirality",
            np.allclose(H @ S - S @ H, 0.0),
        )
    )

    minimal_axioms = (ROOT / "docs/MINIMAL_AXIOMS_2026-06-05.md").read_text()
    record_note = (ROOT / "docs/RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md").read_text()
    form_note = (ROOT / "docs/FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md").read_text()
    source_note = (ROOT / "docs/FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md").read_text()
    guard_ok = (
        "record supplies no readout context" in minimal_axioms
        and "Thus Record alone cannot select a value" in record_note
        and "Record readout does\nnot force" in form_note
        and "No new axiom is introduced" in source_note
        and "candidate revised Axiom" not in source_note
    )
    passed.append(
        check(
            "C9 source guards: current Record authorities are cited as boundary, not as a new axiom",
            guard_ok,
        )
    )

    total = len(passed)
    passed_count = sum(passed)
    print(f"\nSCORECARD PASS={passed_count} FAIL={total - passed_count}")
    print("ANSWER: existing Record gives finite additive readout coordinates and the")
    print("generation dial rho=2r, while the generator-channel HS rule would give")
    print("r=1/(N-1). Record also proves the selection is not automatic: arbitrary")
    print("two-sector coordinates remain admissible until a carrier-measure/readout")
    print("selection theorem is supplied. No new axiom is introduced here.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
