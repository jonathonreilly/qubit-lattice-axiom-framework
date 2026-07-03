#!/usr/bin/env python3
"""Supplied-carrier boundary for Koide tracial standard form.

The runner checks exact finite algebra on a specified tracial standard-form
R[Z_3] carrier. It also verifies the source-note boundary: no Tier-A admission,
no axiom proposal, and no physical Majorana/Kahler/readout claim is
load-bearing here.
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


def regular_rep(n):
    S = sp.zeros(n, n)
    for k in range(n):
        S[(k + 1) % n, k] = 1
    return S


def main():
    passed = []
    n = 3
    S = regular_rep(n)
    I = sp.eye(n)
    J = sp.ones(n, n)
    powers = {k: S**k for k in range(n)}
    tau = lambda M: sp.Rational(1, n) * M.trace()
    Omega = sp.zeros(n, 1)
    Omega[0] = 1

    gns_state = all(
        sp.simplify((Omega.T * (powers[k] * Omega))[0] - tau(powers[k])) == 0
        for k in range(n)
    )
    onb = all(
        sp.simplify(tau(powers[i].T * powers[j]) - (1 if i == j else 0)) == 0
        for i in range(n)
        for j in range(n)
    )
    cyclic = sp.Matrix.hstack(*[powers[k] * Omega for k in range(n)]).rank() == n
    separating = all(not (powers[k] * Omega).is_zero_matrix for k in range(n))
    passed.append(
        check(
            "C1 tracial GNS standard form reproduces tau and has Omega=e cyclic+separating",
            gns_state and onb and cyclic and separating,
        )
    )

    P_id = Omega * Omega.T
    P_nonid = I - P_id
    split_ok = (
        sp.simplify(P_id * P_id - P_id).is_zero_matrix
        and sp.simplify(P_nonid * P_nonid - P_nonid).is_zero_matrix
        and sp.simplify(P_id * P_nonid).is_zero_matrix
        and sp.trace(P_id) == 1
        and sp.trace(P_nonid) == n - 1
    )
    passed.append(
        check(
            "C2 C.Omega (+) Omega^perp gives the group-element (1,N-1) split without diagonalization",
            split_ok,
        )
    )

    p0 = sum(powers.values(), sp.zeros(n, n)) / n
    democratic = sp.Matrix([1] * n) / sp.sqrt(n)
    p0_line = sp.simplify(p0[:, 0] * n - sp.Matrix([1] * n)).is_zero_matrix
    overlap = sp.simplify((Omega.T * democratic)[0])
    passed.append(
        check(
            "C3 idempotent singlet is democratic and misaligned with Omega",
            p0_line and overlap == 1 / sp.sqrt(n) and overlap not in (0, 1),
            f"<Omega,democratic>={overlap}",
        )
    )

    auts = [u for u in range(1, n) if sp.gcd(u, n) == 1]
    aut_ok = True
    for u in auts:
        images = [(k * u) % n for k in range(n)]
        aut_ok = aut_ok and images[0] == 0 and sorted(images[1:]) == list(range(1, n))
    passed.append(
        check(
            "C4 Aut(Z_3) fixes e and permutes non-identity elements",
            aut_ok,
            f"units={auts}",
        )
    )

    B = J - I
    hs_ok = sp.trace(I.T * I) == n and sp.trace(B.T * B) == n * (n - 1) and sp.trace(I.T * B) == 0
    a, b = sp.symbols("a b", positive=True)
    r_channel = sp.solve(sp.Eq(n * a**2, n * (n - 1) * b**2), b)[0] ** 2 / a**2
    passed.append(
        check(
            "C5 Hilbert-Schmidt channel scoring gives r=1/(N-1)",
            hs_ok and r_channel == sp.Rational(1, 2),
            f"N=3 r={r_channel}",
        )
    )

    Q = sp.Rational(1, 3) + sp.Rational(2, 3) * sp.symbols("r")
    passed.append(
        check(
            "C6 finite Koide coordinate gives Q=2/3 after supplied r=1/2",
            sp.simplify(Q.subs("r", sp.Rational(1, 2))) == sp.Rational(2, 3),
        )
    )

    r_direction = sp.solve(sp.Eq(a**2, b**2), b)[0] ** 2 / a**2
    r_idempotent = (sp.solve(sp.Eq((a + 2 * b) ** 2, 2 * (a - b) ** 2), b)[0] / a) ** 2
    residual_ok = (
        r_direction == 1
        and sp.simplify(r_idempotent - (sp.Rational(17, 2) - 6 * sp.sqrt(2))) == 0
    )
    passed.append(
        check(
            "C7 residual options remain expressible: direction-count r=1, idempotent r=17/2-6sqrt2",
            residual_ok,
            f"direction={r_direction}; idempotent={sp.nsimplify(r_idempotent)}",
        )
    )

    kahler_r = sp.solve(sp.Eq(a**2 + 4 * b**2, 2 * (a**2 + b**2)), b)[0] ** 2 / a**2
    passed.append(
        check(
            "C8 Kahler identity is algebraic corroborator only",
            kahler_r == sp.Rational(1, 2),
        )
    )

    Sn = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=float)
    Hn = np.eye(3) + (1 / np.sqrt(2)) * (np.ones((3, 3)) - np.eye(3))
    passed.append(
        check(
            "C9 r=1/2 circulant point commutes with C3 shift",
            np.allclose(Hn @ Sn - Sn @ Hn, 0.0),
        )
    )

    source_note = (ROOT / "docs/KOIDE_TRACIAL_STANDARD_FORM_CARRIER_NARROW_NOTE_2026-06-02.md").read_text()
    minimal = (ROOT / "docs/MINIMAL_AXIOMS_2026-06-05.md").read_text()
    record_note = (ROOT / "docs/RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md").read_text()
    guard_ok = (
        "not a Tier-A admission" in source_note
        and "not a framework-axiom revision" in source_note
        and "not used as\n   physical predictions" in source_note
        and "record supplies no readout context" in minimal
        and "Thus Record alone cannot select a value" in record_note
    )
    passed.append(
        check(
            "C10 source guards keep this as supplied-carrier bounded support",
            guard_ok,
        )
    )

    n_pass = sum(passed)
    print(f"\nSCORECARD PASS={n_pass} FAIL={len(passed) - n_pass}")
    print("ANSWER: the supplied tracial standard-form carrier distinguishes the")
    print("(1,N-1) group-element split via Omega=e. Equal channel scoring then")
    print("gives r=1/(N-1), but scoring and physical carrier selection remain")
    print("outside the current axioms. This is bounded support, not an axiom")
    print("proposal or unbounded Koide-value derivation.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
