#!/usr/bin/env python3
"""A NEW (axis-exchange) parity violation = the C_3-circulant phase delta.

The retained-parity probe showed the framework's EXISTING parity/chiral
violation lives on the 3 <-> 3-bar axis and does not act within the generation
triplet. This asks the follow-up: what would a NEW parity violation that DOES
act within the triplet look like, and is it constrained?

The framework's retained Koide structure puts the generation masses in a
C_3-circulant Hermitian matrix (koide_circulant_character_bridge,
koide_circulant_q_two_thirds):

    H(a, b) = a I + b C + conj(b) C^2 ,   C = 3-cycle,   b = |b| e^{i*delta}.

Its eigenvalues are  lambda_k = a + 2|b| cos(delta + 2*pi*k/3),  k=0,1,2.

Claim under test: the phase  delta  is exactly the AXIS-EXCHANGE PARITY order
parameter of the generation triplet.

  * C (the 3-cycle) always preserves H  -> C_3 is unbroken for any delta.
  * A transposition (reversal C -> C^2) maps b -> conj(b), i.e. delta -> -delta;
    so H is transposition-invariant iff sin(delta)=0. Generic sin(delta) != 0
    is the parity (axis-exchange reflection) violation, acting WITHIN the
    triplet.
  * sin(delta)=0 -> spectrum degenerate (1 + 2), full S_3.
    Generic sin(delta)!=0 -> three distinct masses, C_3 only (the Koide regime).

So a "new parity violation" is a nonzero circulant phase delta: it acts within
the generation triplet (unlike the existing 3<->3-bar parity), it lands on C_3
(not trivial) -- preserving the Koide circulant structure -- and the transposition
acts on it by complex conjugation (delta -> -delta), the same orientation/i flip
seen elsewhere.

Pure finite linear algebra on C^3. No PDG / fitted / scale / mass-value input.
Asserts no audit status. Does NOT derive that delta is nonzero/forced.
"""

from __future__ import annotations

import cmath
import math

import numpy as np

TOL = 1.0e-12
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        st = "PASS"
    else:
        FAIL += 1
        st = "FAIL"
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return cond


# 3-cycle permutation matrix C: e_0->e_1->e_2->e_0
C = np.array([[0, 0, 1],
              [1, 0, 0],
              [0, 1, 0]], dtype=complex)
# a transposition (reversal): swaps e_1,e_2; it conjugates C to C^2 (= C^{-1})
TAU = np.array([[1, 0, 0],
                [0, 0, 1],
                [0, 1, 0]], dtype=complex)


def H(a, b):
    return a * np.eye(3, dtype=complex) + b * C + np.conj(b) * (C @ C)


def distinct_eigs(M):
    ev = np.sort(np.linalg.eigvalsh((M + M.conj().T) / 2).real)
    out = []
    for x in ev:
        if not out or abs(x - out[-1]) > 1e-7:
            out.append(round(float(x), 6))
    return out


def main() -> int:
    print("=" * 76)
    print("NEW (AXIS-EXCHANGE) PARITY VIOLATION = THE C_3-CIRCULANT PHASE delta")
    print("=" * 76)

    a = 5.0
    bmag = 1.3

    # C_3 always preserves H (circulant by construction)
    print("\n" + "-" * 76)
    print("C_3 (the 3-cycle) preserves H for every phase delta")
    print("-" * 76)
    for delta in (0.0, math.pi, 0.4, 1.1):
        b = bmag * cmath.exp(1j * delta)
        Hd = H(a, b)
        ok = np.linalg.norm(C @ Hd @ C.conj().T - Hd) < TOL
        check(f"C H C+ = H at delta={delta}", ok)

    # Transposition maps delta -> -delta (conjugates b); invariant iff sin(delta)=0.
    print("\n" + "-" * 76)
    print("Transposition (reversal) conjugates b: delta -> -delta")
    print("-" * 76)
    for delta in (0.0, 0.4, 1.1):
        b = bmag * cmath.exp(1j * delta)
        Hd = H(a, b)
        Ht = TAU @ Hd @ TAU.conj().T
        Hminus = H(a, np.conj(b))  # delta -> -delta
        check(f"tau H(delta) tau+ = H(-delta) at delta={delta}",
              np.linalg.norm(Ht - Hminus) < TOL)
        inv = np.linalg.norm(Ht - Hd) < TOL
        # invariant under transposition iff delta = 0 or pi mod 2pi.
        expect_inv = abs(math.sin(delta)) < 1e-9
        check(f"H transposition-invariant iff sin(delta)=0  (delta={delta}: inv={inv})",
              inv == expect_inv)

    # Spectrum: reflection fixed loci are degenerate; generic phase is three-distinct (C_3).
    print("\n" + "-" * 76)
    print("Spectrum: sin(delta)=0 degenerate (full S_3); generic phase three distinct (C_3)")
    print("-" * 76)
    eig0 = distinct_eigs(H(a, bmag * cmath.exp(0j)))
    check("delta=0: at most two distinct eigenvalues (forced degeneracy)",
          len(eig0) <= 2, detail=f"eigs={eig0}")
    eigpi = distinct_eigs(H(a, bmag * cmath.exp(1j * math.pi)))
    check("delta=pi: at most two distinct eigenvalues (the other reflection fixed locus)",
          len(eigpi) <= 2, detail=f"eigs={eigpi}")
    eigd = distinct_eigs(H(a, bmag * cmath.exp(1j * 0.4)))
    check("delta=0.4: three distinct eigenvalues", len(eigd) == 3, detail=f"eigs={eigd}")
    # eigenvalue form matches retained koide_circulant_q row (full precision)
    raw = sorted(np.linalg.eigvalsh(H(a, bmag * cmath.exp(1j * 0.4))).real)
    lam = sorted(a + 2 * bmag * math.cos(0.4 + 2 * math.pi * k / 3) for k in range(3))
    check("eigenvalues match a + 2|b| cos(delta + 2pi k/3) (retained circulant form)",
          all(abs(x - y) < 1e-9 for x, y in zip(raw, lam)))

    # delta and -delta give the same mass SET (mirror), different H (orientation)
    print("\n" + "-" * 76)
    print("Parity (delta -> -delta) is a mirror: same masses, opposite orientation")
    print("-" * 76)
    check("delta and -delta give the same eigenvalue set",
          distinct_eigs(H(a, bmag * cmath.exp(1j * 0.4)))
          == distinct_eigs(H(a, bmag * cmath.exp(-1j * 0.4))))
    check("but H(delta) != H(-delta) for delta != 0 (the parity is violated, not absent)",
          np.linalg.norm(H(a, bmag * cmath.exp(1j * 0.4))
                         - H(a, bmag * cmath.exp(-1j * 0.4))) > TOL)

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if FAIL == 0:
        print(
            "  A NEW PARITY VIOLATION HAS A PRECISE ORDER PARAMETER: the C_3-\n"
            "  circulant phase delta of the generation mass matrix.\n"
            "   * C_3 (the 3-cycle) is preserved for every delta -- the Koide\n"
            "     circulant structure is intact.\n"
            "   * A transposition (axis-exchange reflection) conjugates b, i.e.\n"
            "     delta -> -delta; H is transposition-invariant iff sin(delta)=0. So\n"
            "     a generic phase with sin(delta)!=0 IS an axis-exchange parity\n"
            "     violation acting WITHIN the generation triplet (unlike the\n"
            "     existing 3<->3-bar parity).\n"
            "   * sin(delta)=0 -> degenerate (full S_3); generic sin(delta)!=0 ->\n"
            "     three distinct masses, C_3 only -- the Koide-compatible regime,\n"
            "     landing on C_3 (not trivial).\n"
            "   * delta -> -delta (the transposition) is a mirror: same masses,\n"
            "     opposite orientation -- the same orientation/i flip seen before.\n\n"
            "  Honest scope: this identifies WHAT a new parity violation is (a\n"
            "  nonzero circulant phase) and shows it is C_3-preserving / Koide-\n"
            "  compatible. It does NOT derive that delta is nonzero or fixed by the\n"
            "  framework -- whether delta is forced is the open flavor-phase\n"
            "  question (the koide_bae / a3_route1 cluster).\n"
        )
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
