"""Audit-ready verification backbone for the det multiplicative-character form selection (the FACTOR-2
content of the log-det generator W = log|det(D+J)|). Backs the existing claim of
OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION (read-only; not edited here) with
finite computational checks plus the standard GL(n) abelianization proof sketch stated in the companion
note, and states the honest two-premise bound:

  STEP (i)  COMPOSITION-axis selection [clean math, GL(n) abelianization]:
            chi(A.S)=chi(A)chi(S) selects the determinant generator; regular algebraic characters of
            GL_n(C) are integer powers det^m. tr, power-traces tr(M^s), and elementary symmetric e_k
            (k<n) all FAIL multiplicativity-under-composition and are excluded.
  STEP (ii) ADDITIVE-of-MULTIPLICATIVE -> log [Record axis + regularity]:
            a continuous/smooth scalar W additive over independent patches, applied to a positive
            scalar Z multiplicative over patches, is W = c*log Z (Cauchy). With Z = |det| this gives
            W = c*log|det|. Record supplies additivity, not the regularity hypothesis or Z=det.

HONEST BOUND (Pattern L): additivity over DIRECT SUMS alone does NOT exclude tr (tr(A(+)B)=tr(A)+tr(B)),
so the Record axiom (additivity) does NOT by itself select det -- the COMPOSITION-multiplicativity
premise (M) is required. In the intended chain, (M) is the still-needed statement that the relevant
partition amplitude is a Berezin/Grassmann determinant amplitude Z=det(D+J) multiplying over independent
source patches (a fermionic-frame property). So FACTOR 2 = clean abelianization math GIVEN the
fermionic-frame multiplicativity (M); the residual is the fermionic/Berezin origin of Z=det (overlapping
the source-coupling factor 3), NOT the det-selection math itself.

Sets no audit status (independent audit lane owns that); edits/re-cites no existing row.
"""
import numpy as np

rng = np.random.default_rng(19)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def close(lhs, rhs, tol=1e-8):
    scale = max(1.0, abs(lhs), abs(rhs))
    return abs(lhs - rhs) <= tol * scale


def gl(n):
    while True:
        M = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        if abs(np.linalg.det(M)) > 1e-3:
            return M


def main():
    passed = []
    n = 4
    A, S = gl(n), gl(n)

    # STEP (i) COMPOSITION axis: det multiplicative; tr, power-trace, elementary-symmetric FAIL.
    passed.append(check(
        "det is multiplicative under COMPOSITION: det(A.S)=det(A)det(S)",
        abs(np.linalg.det(A @ S) - np.linalg.det(A) * np.linalg.det(S)) < 1e-8))

    passed.append(check(
        "tr FAILS composition-multiplicativity: tr(A.S) != tr(A)tr(S) (so tr is EXCLUDED on this axis)",
        abs(np.trace(A @ S) - np.trace(A) * np.trace(S)) > 1e-3))

    passed.append(check(
        "power-trace tr(M^2) FAILS composition-multiplicativity (excluded)",
        abs(np.trace((A @ S) @ (A @ S)) - np.trace(A @ A) * np.trace(S @ S)) > 1e-3))

    # elementary symmetric e_2 (coeff of char poly) fails composition multiplicativity.
    def e2(M):
        ev = np.linalg.eigvals(M)
        return sum(ev[i] * ev[j] for i in range(len(ev)) for j in range(i + 1, len(ev)))
    passed.append(check(
        "elementary symmetric e_2 FAILS composition-multiplicativity (excluded)",
        abs(e2(A @ S) - e2(A) * e2(S)) > 1e-3))

    # Integer powers of det are the regular algebraic character family; the finite
    # check below is only a sanity check for the companion note's proof sketch.
    passed.append(check(
        "integer powers det^m obey composition-multiplicativity (regular GL(n) characters)",
        all(close(np.linalg.det(A @ S) ** k, (np.linalg.det(A) ** k) * (np.linalg.det(S) ** k), 1e-7)
            for k in (-2, -1, 0, 1, 2, 3))))

    F = np.diag([-1, 1, 1, 1]).astype(complex)
    sqrt_lhs = complex(np.linalg.det(F @ F)) ** 0.5
    sqrt_rhs = complex(np.linalg.det(F)) ** 0.5 * complex(np.linalg.det(F)) ** 0.5
    passed.append(check(
        "fractional complex branches such as det^(1/2) are NOT global composition characters",
        abs(sqrt_lhs - sqrt_rhs) > 1e-6,
        f"sqrt(det(F.F))={sqrt_lhs}, sqrt(det F)sqrt(det F)={sqrt_rhs}"))

    # HONEST BOUND (Pattern L): additivity over DIRECT SUMS does NOT exclude tr.
    def dsum(X, Y):
        Z = np.zeros((X.shape[0] + Y.shape[0],) * 2, dtype=complex)
        Z[:X.shape[0], :X.shape[0]] = X
        Z[X.shape[0]:, X.shape[0]:] = Y
        return Z
    AB = dsum(A, S)
    passed.append(check(
        "PATTERN L (honest bound): tr IS additive over direct sums (tr(A(+)B)=tr(A)+tr(B)) -- so additivity ALONE cannot exclude tr; the COMPOSITION premise is required",
        abs(np.trace(AB) - (np.trace(A) + np.trace(S))) < 1e-9))

    # STEP (ii) ADDITIVE-of-MULTIPLICATIVE -> log: Z multiplies over patches, and a regular additive
    # scalar readout W is c log Z. Verify: |Z|^p multiplies (does NOT add); log|Z| adds.
    ZA, ZB = abs(np.linalg.det(A)), abs(np.linalg.det(S))
    passed.append(check(
        "Z=|det| multiplies over patches; regular additive readout is W=c log|det| (Record axis + regularity)",
        abs(abs(np.linalg.det(AB)) - ZA * ZB) < 1e-8
        and abs(np.log(abs(np.linalg.det(AB))) - (np.log(ZA) + np.log(ZB))) < 1e-9
        and abs((abs(np.linalg.det(AB))) ** 2 - (ZA ** 2 + ZB ** 2)) > 1e-3))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("AUDIT-READY TARGET: det-selection on the COMPOSITION axis is clean GL(n)-abelianization math")
    print("(integer det powers; tr/power-trace/elementary-symmetric excluded; fractional complex branches")
    print("are not global characters). Additive-of-multiplicative plus regularity fixes W=c*log|det|.")
    print("HONEST BOUND: additivity alone can't exclude tr (Pattern L); the composition premise (M) is")
    print("the residual fermionic/Berezin origin of Z=det, not the det-selection math. Sets no audit")
    print("status; edits no existing row.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
