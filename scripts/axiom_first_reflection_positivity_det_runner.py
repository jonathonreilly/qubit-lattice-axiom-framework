"""Numerical companion for the Case A eigenvalue-pairing det-positivity argument.

This runner verifies the replacement Case A argument in
docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md.

Case A claim: for M = M_KS + m * I with M_KS real anti-symmetric (the
staggered Kogut-Susskind hop in the real component basis is anti-hermitian),
the eigenvalues of M_KS are pure imaginary and come in conjugate pairs
(i*lambda, -i*lambda). Therefore eigenvalues of M come in pairs
(m + i*lambda, m - i*lambda), each pair contributing (m+i*lambda)(m-i*lambda)
= m^2 + lambda^2 > 0 to det(M). Hence det(M) > 0 for all m > 0.

Cross-check: det(M^dagger M) = |det(M)|^2 by the singular-value /
det(A^dagger A) = det(A)^2 (in the complex-conjugation sense) identity.

The runner picks a small 4x4 real anti-symmetric M_KS, adds m*I across a
spread of mass values, and verifies both (a) det(M) > 0 and (b)
det(M^dagger M) = |det(M)|^2 to floating-point precision.
"""

import numpy as np


def main() -> int:
    np.random.seed(42)
    A = np.random.randn(4, 4)
    M_KS = A - A.T  # real anti-symmetric; eigenvalues are pure imaginary
    # Sanity: anti-symmetry holds
    assert np.allclose(M_KS, -M_KS.T), "M_KS must be anti-symmetric"

    masses = [0.1, 0.5, 1.0, 2.0, 5.0]
    pass_count = 0
    fail_count = 0

    for m in masses:
        M = M_KS + m * np.eye(4)
        detM = np.linalg.det(M)
        detMdM = np.linalg.det(M.conj().T @ M)

        # Check 1: det(M) > 0 for m > 0.
        if np.isreal(detM) or np.isclose(detM.imag, 0.0):
            detM_real = float(np.real(detM))
            if detM_real > 0:
                pass_count += 1
                print(f"  m={m:>4}: det(M) = {detM_real:+.6f}  > 0  PASS")
            else:
                fail_count += 1
                print(f"  m={m:>4}: det(M) = {detM_real:+.6f}  <= 0  FAIL")
        else:
            fail_count += 1
            print(f"  m={m:>4}: det(M) has imaginary part {detM.imag:.3e}  FAIL")

        # Check 2: det(M^dagger M) == |det(M)|^2.
        lhs = float(np.real(detMdM))
        rhs = float(abs(detM) ** 2)
        if np.isclose(lhs, rhs, rtol=1e-10, atol=1e-12):
            pass_count += 1
            print(
                f"  m={m:>4}: det(M^dagger M) = {lhs:.6f}  vs |det(M)|^2 = {rhs:.6f}  PASS"
            )
        else:
            fail_count += 1
            print(
                f"  m={m:>4}: det(M^dagger M) = {lhs:.6f}  vs |det(M)|^2 = {rhs:.6f}  FAIL"
            )

    print(f"\nPASS={pass_count} FAIL={fail_count}")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
