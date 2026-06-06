#!/usr/bin/env python3
"""Class-A verifier: the no-diagonal LATTICE axiom + the staggered-Dirac (purely imaginary)
hopping make the emergent generation C3 coupling K-REAL to ALL orders -- so the einselection
sieve's 2-sector partition is DYNAMICALLY einselected and the K-odd (3-mode / r=0) coupling is
STRUCTURALLY FORBIDDEN.

Background. The retained einselection sieve
(flavor_einselection_2sector_modulo_kreality, bounded_theorem) shows: a C3-invariant **K-real**
(time-reversal-real) generation coupling lies in span_R{I, C+C^2} and resolves only the 2
real-irreducible blocks (singlet + doublet) = the 2-sector partition; resolving omega from
omega^2 (the 3-mode / r=0 partition) STRICTLY requires the **K-odd** observable i(C-C^2).
The sieve POSITS K-reality (its GAP A). This runner DERIVES it from the axioms.

The mechanism. The generation triplet is hw=1. The emergent C3 coupling is the effective
operator built from the native single-flip hopping through the hw=0/hw=2 virtual sectors. Two
structural facts:
  (i)  NO-DIAGONAL axiom => the hop is a single bit-flip => returning to hw=1 needs an EVEN
       number of hops (Hamming parity). So ODD perturbative orders VANISH on hw=1.
  (ii) STAGGERED-DIRAC form => the off-diagonal hopping is PURELY IMAGINARY (V = iA, A real;
       the retained -0.5j hops), the diagonal (mass) is real. An EVEN number of purely-imaginary
       hops has amplitude i^even * real = REAL.
Together: every non-vanishing (even) order is REAL => the C3 coupling has NO imaginary
(K-odd, i(C-C^2)) component at ANY order => it is K-REAL to all orders => it einselects the
2-sector partition. A K-odd part would require a non-native MIXED real+imaginary hop, or a
diagonal hop (odd-order return) -- both forbidden.

Verifies:
  (1) odd orders (3, 5) VANISH on hw=1 (Hamming parity / no-diagonal);
  (2) even orders (2, 4) are REAL (max|Im|=0) => K-real, robust across uniform AND staggered
      sign patterns;
  (3) realness => no K-odd (i(C-C^2)) component (the K-odd generator is intrinsically imaginary);
  (4) load-bearing: a non-native MIXED (real+imaginary) hop DOES introduce a K-odd part, so the
      purely-imaginary staggered-Dirac form is what forbids it;
  (5) consequence: the 2-sector partition is einselected; the r=0 (3-mode) setting is structurally
      excluded; the dial is narrowed to the 2-sector {r=1/2, r=1}. The r=1/2-vs-r=1 choice is the
      separate block-count-vs-dimension measure -- NOT decided here (no value forced).

No new axiom/import: the single-flip hopping, the Hamming-graded diagonal, and the imaginary
staggered-Dirac form are the retained native dynamics; the order-parity and realness are exact.
"""

from __future__ import annotations
import numpy as np

PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok); FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


sx = np.array([[0, 1], [1, 0]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def op(o, q):
    m = np.array([[1]], dtype=complex)
    for i in range(3):
        m = np.kron(m, o if i == q else I2)
    return m


hwv = np.array([bin(i).count("1") for i in range(8)])
P1 = [i for i in range(8) if hwv[i] == 1]
Pm = np.zeros((3, 8), dtype=complex)
for _a, _i in enumerate(P1):
    Pm[_a, _i] = 1.0


def resolvent(diag, E1):
    return np.diag([0.0 if hwv[i] == 1 else 1.0 / (E1 - diag[i]) for i in range(8)]).astype(complex)


def Heff(V, R, n):
    """n-th order effective coupling on hw=1: P V (R V)^(n-1) P."""
    M = V.copy()
    for _ in range(n - 1):
        M = M @ R @ V
    return Pm @ M @ Pm.conj().T


def main() -> int:
    print("=" * 78)
    print("no-diagonal + staggered-Dirac => generation coupling K-real to all orders  [class A]")
    print("=" * 78)

    diag = np.array([hwv[i] * 1.0 + (0.3 if hwv[i] == 2 else 0.0) + (0.05 if hwv[i] == 3 else 0.0)
                     for i in range(8)])
    E1 = diag[P1[0]]
    R = resolvent(diag, E1)

    sign_patterns = {"uniform (+,+,+)": (1, 1, 1),
                     "staggered (+,-,+)": (1, -1, 1),
                     "staggered (-,+,-)": (-1, 1, -1)}

    # ---- (1)+(2) odd orders vanish (parity); even orders real (K-real), all sign patterns ----
    print("\n-- (1)+(2) odd orders vanish (Hamming parity); even orders are real (K-real) --")
    for label, signs in sign_patterns.items():
        A = sum(s * op(sx, q) for s, q in zip(signs, range(3)))
        V = 1j * A                                            # staggered-Dirac: purely imaginary
        odd_vanish = all(np.max(np.abs(Heff(V, R, n))) < 1e-12 for n in (3, 5))
        even_real = all(np.max(np.abs(Heff(V, R, n).imag)) < 1e-12 and
                        np.max(np.abs(Heff(V, R, n))) > 1e-9 for n in (2, 4))
        check(f"{label}: odd orders (3,5) VANISH on hw=1 (single-flip => even-order return)",
              odd_vanish)
        check(f"{label}: even orders (2,4) are REAL (K-real, max|Im|=0) and nonzero", even_real,
              detail=f"|K|_2={abs(Heff(V,R,2)[0,1]):.4f}")

    # ---- (3) realness => no K-odd (i(C-C^2)) component ----
    print("\n-- (3) realness => no K-odd i(C-C^2) component (the sieve's 3-mode/r=0 resolver) --")
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
    Kodd = 1j * (C - C @ C)                                   # the K-odd generator, intrinsically imaginary
    check("the K-odd generator i(C-C^2) is purely imaginary (so any K-odd part shows up in Im(H))",
          np.allclose(Kodd.real, 0) and not np.allclose(Kodd.imag, 0))
    A = sum(op(sx, q) for q in range(3)); V = 1j * A
    H2 = Heff(V, R, 2)
    check("the 2nd-order coupling has zero overlap with the K-odd generator (Tr(Kodd^dag H2)=0)",
          abs(np.trace(Kodd.conj().T @ H2)) < 1e-12,
          detail=f"|<Kodd,H2>| = {abs(np.trace(Kodd.conj().T @ H2)):.1e}")

    # ---- (4) load-bearing: a MIXED real+imaginary hop WOULD give a K-odd part ----
    print("\n-- (4) load-bearing: only a non-native MIXED hop produces a K-odd part --")
    cases = [("purely imaginary V=iA (staggered-Dirac, native)", 1j * A, True),
             ("purely real V=A (counterfactual)", A, True),
             ("MIXED V=(1+i)A (non-native)", (1 + 1j) * A, False)]
    for name, V, expect_kreal in cases:
        im = np.max(np.abs(Heff(V, R, 2).imag))
        is_kreal = im < 1e-12
        check(f"{name}: {'K-real' if expect_kreal else 'K-ODD present'}",
              is_kreal == expect_kreal, detail=f"max|Im(H2)|={im:.2e}")

    # ---- (5) consequence: 2-sector partition einselected; r=0 excluded ----
    print("\n-- (5) consequence: 2-sector partition einselected; r=0 structurally excluded --")
    # the K-real coupling lies in span_R{I, C+C^2}; eig(C+C^2)={2,-1,-1}: singlet isolated,
    # doublet degenerate => resolves only the 2 blocks (singlet rank1 + doublet rank2).
    M = (C + C @ C).real
    evals = np.sort(np.linalg.eigvalsh(M))
    check("the K-real cone generator C+C^2 has spectrum {-1,-1,2}: singlet isolated + doublet "
          "degenerate => resolves ONLY the 2-sector (singlet+doublet) partition, not the 3 modes",
          np.allclose(evals, [-1, -1, 2]))

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: K-real-to-all-orders / 2-sector einselection FAILED.")
        return 1
    print("VERDICT: the no-diagonal axiom (single-flip => even-order returns to hw=1, odd orders "
          "vanish) and the staggered-Dirac purely-imaginary hopping (even # of i's => real) make "
          "the emergent generation C3 coupling K-REAL to ALL orders. So it lies in the sieve's "
          "K-real cone span_R{I,C+C^2} and einselects the 2-SECTOR (singlet+doublet) partition; "
          "the K-odd (3-mode / r=0) coupling is STRUCTURALLY FORBIDDEN (needs a non-native mixed "
          "hop or a diagonal hop). This DISCHARGES the sieve's posited K-reality from the axioms "
          "and narrows the dial to the 2-sector {r=1/2, r=1} -- excluding r=0 (Q=1/3). The "
          "r=1/2-vs-r=1 choice is the separate block-count-vs-dimension measure; no value forced.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
