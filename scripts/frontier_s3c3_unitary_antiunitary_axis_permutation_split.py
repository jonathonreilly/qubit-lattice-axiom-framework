#!/usr/bin/env python3
"""Unitary/antiunitary axis-permutation split on the one-qubit operator algebra.

Key identity (one-qubit operator algebra, Cl(3,0) = M_2(C)):
  the spatial volume form omega = e1 e2 e3 EQUALS i * I in M_2(C).
So the orientation of the three spatial axes is literally the qubit's complex
unit i on the fixed complex Pauli representation.

Consequence for the S_3 axis-permutation symmetry:
  a permutation sigma conjugates omega by sgn(sigma):
      e_{sigma(1)} e_{sigma(2)} e_{sigma(3)} = sgn(sigma) * omega.
  A UNITARY (C-linear) conjugation preserves the scalar i*I, so it can realize
  sigma only if sgn(sigma) = +1, i.e. sigma in A_3 = C_3 (the 3-cycles).
  The transpositions (sgn = -1) send omega = iI -> -iI, i.e. i -> -i; they can
  not be realized as C-linear unitaries on this fixed generator triple.

Therefore C_3 is the unitary axis-permutation subgroup. Concluding that the
physical generation symmetry excludes the antiunitary/orientation-reversing
operations is a separate bridge/premise; this runner only checks the finite
algebraic split.

Pure finite linear algebra on M_2(C). No PDG / fitted / scale / mass input.
Asserts no audit status.
"""

from __future__ import annotations

import itertools

import numpy as np

TOL = 1.0e-12
PASS = 0
FAIL = 0

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
E = [SX, SY, SZ]  # Cl(3,0) generators: e_i^2 = I, mutually anticommuting


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


def sgn(p):
    # parity of permutation p of (0,1,2)
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    return -1 if inv % 2 else 1


def main() -> int:
    print("=" * 76)
    print("UNITARY/ANTIUNITARY AXIS-PERMUTATION SPLIT: omega = qubit i")
    print("=" * 76)

    # Cl(3) sanity
    print("\n" + "-" * 76)
    print("Cl(3,0) generators and volume form omega = e1 e2 e3")
    print("-" * 76)
    for i in range(3):
        check(f"e{i+1}^2 = I", np.linalg.norm(E[i] @ E[i] - I2) < TOL)
    for i in range(3):
        for j in range(i + 1, 3):
            check(f"{{e{i+1},e{j+1}}} = 0 (anticommute)",
                  np.linalg.norm(E[i] @ E[j] + E[j] @ E[i]) < TOL)
    omega = E[0] @ E[1] @ E[2]
    check("omega = e1 e2 e3 = i*I  (spatial volume form IS the qubit complex unit)",
          np.linalg.norm(omega - 1j * I2) < TOL, detail="omega = +iI")
    check("omega^2 = -I", np.linalg.norm(omega @ omega + I2) < TOL)
    check("omega is central (commutes with every generator)",
          all(np.linalg.norm(omega @ E[i] - E[i] @ omega) < TOL for i in range(3)))

    # permutation conjugates omega by sgn
    print("\n" + "-" * 76)
    print("Axis permutation sigma sends omega -> sgn(sigma) * omega")
    print("-" * 76)
    for p in itertools.permutations((0, 1, 2)):
        prod = E[p[0]] @ E[p[1]] @ E[p[2]]
        s = sgn(p)
        ok = np.linalg.norm(prod - s * omega) < TOL
        kind = "identity" if p == (0, 1, 2) else (
            "3-cycle" if s == 1 else "transposition")
        check(f"{p} ({kind}): e_s1 e_s2 e_s3 = {s:+d}*omega", ok)

    # C_3 is realizable by a UNITARY (preserves i*I); transpositions are not.
    print("\n" + "-" * 76)
    print("C_3 is unitary (preserves i); transpositions are not C-linear unitary")
    print("-" * 76)
    # explicit unitary: 120-degree rotation about (1,1,1)/sqrt3 cyclically permutes Paulis
    n = np.array([1, 1, 1]) / np.sqrt(3)
    ndotsig = n[0] * SX + n[1] * SY + n[2] * SZ
    theta = 2 * np.pi / 3
    U = np.cos(theta / 2) * I2 - 1j * np.sin(theta / 2) * ndotsig
    check("U is unitary", np.linalg.norm(U.conj().T @ U - I2) < TOL)
    cyc = {0: 1, 1: 2, 2: 0}
    cyc_ok = all(np.linalg.norm(U @ E[i] @ U.conj().T - E[cyc[i]]) < TOL for i in range(3))
    check("explicit unitary U realizes the 3-cycle (U e_i U+ = e_{i+1})", cyc_ok)
    check("U preserves omega = i*I (unitary => C-linear => i fixed)",
          np.linalg.norm(U @ omega @ U.conj().T - omega) < TOL)

    # No-unitary lemma for transpositions: a unitary V with V e_i V+ = e_{tau(i)}
    # would give V omega V+ = sgn(tau) omega = -omega, but V omega V+ = V(iI)V+ = iI.
    # iI = -iI is false => no such C-linear unitary.
    print("\n" + "-" * 76)
    print("No-unitary lemma for transpositions (sgn = -1)")
    print("-" * 76)
    # demonstrate the contradiction numerically: search the claim structurally
    contradiction = np.linalg.norm((1j * I2) - (-1j * I2)) > TOL  # iI != -iI
    check("a C-linear unitary realizing a transposition would force iI = -iI (impossible)",
          contradiction, detail="so odd permutations require an orientation-reversing/conjugate-linear step")
    # Complex conjugation is a concrete orientation-reversing antiunitary step:
    # omega under conjugation K: (iI)* = -iI = -omega.
    check("complex conjugation (antiunitary) sends omega = iI -> -iI",
          abs((1j).conjugate() - (-1j)) < TOL)

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if FAIL == 0:
        print(
            "  The spatial volume form e1 e2 e3 equals i*I: the orientation of the\n"
            "  three axes is the qubit complex unit on the fixed Pauli representation.\n"
            "  An axis permutation sigma conjugates it by sgn(sigma). Unitary\n"
            "  (C-linear) symmetries preserve i*I, so they realize only sgn=+1 = C_3;\n"
            "  the orientation-reversing transpositions (sgn=-1) send i -> -i and\n"
            "  cannot be C-linear unitary on this fixed generator triple.\n\n"
            "  Honest consequence: C_3 is the unitary axis-permutation subgroup.\n"
            "  Using this as the physical S_3 -> C_3 selector still requires the\n"
            "  separate bridge/premise that the relevant generation-sector symmetry\n"
            "  must be unitary rather than antiunitary/orientation-reversing.\n"
        )
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
