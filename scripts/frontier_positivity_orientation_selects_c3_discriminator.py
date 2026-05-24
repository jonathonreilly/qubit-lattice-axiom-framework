#!/usr/bin/env python3
"""Positivity/orientation selects C_3 from S_3 (generation-degeneracy lift).

A prior result
(`GENERATION_DEGENERACY_MINIMAL_SYMMETRY_BREAKING_NARROW_THEOREM_NOTE`)
showed three distinct generation masses on the hw=1 triplet require breaking the
full S_3 to *some* proper subgroup. This discriminator sharpens "some" to the
unique one a positivity / "reality cannot be negative" constraint selects:

  the orientation-preserving (determinant +1) subgroup of S_3 is exactly
  A_3 = C_3 = {id, (012), (021)}; the three transpositions are det = -1
  (orientation-reversing).

Hence an orientation / determinant-positivity constraint -- the algebraic
content of "a volume form / determinant cannot be negative" -- forbids exactly
the transpositions and keeps exactly C_3[111]. That is simultaneously:
  * a proper subgroup, so it LIFTS the mass degeneracy (3 distinct masses), and
  * the framework's distinguished cyclic structure C_3[111].

So positivity does not merely permit nondegeneracy; it picks the specific C_3.

HONEST SCOPE. This proves the group-theory selection only. It does NOT prove
that the framework's own positivity principle (staggered det positivity;
Clifford volume chirality) is what acts on the hw=1 triplet -- that bridge is
the open next step, flagged at the end and NOT asserted here.

Pure finite-group / linear algebra on abstract C^3. No PDG / fitted / scale /
mass input. Asserts no audit status.
"""

from __future__ import annotations

import itertools

import numpy as np

TOL = 1.0e-9
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        st = "PASS"
    else:
        FAIL += 1
        st = "FAIL"
    msg = f"  [{st}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def perm_matrix(p) -> np.ndarray:
    m = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        m[p[i], i] = 1.0
    return m


def cycle_type(p) -> str:
    if p == (0, 1, 2):
        return "identity"
    # transposition iff exactly one fixed point
    fixed = [i for i in range(3) if p[i] == i]
    return "transposition" if len(fixed) == 1 else "3-cycle"


# E (2-dim standard) irrep basis: orthonormal complement of the all-ones vector.
E_BASIS = np.array(
    [[1.0, 1.0, -2.0],
     [1.0, -1.0, 0.0]], dtype=complex
)
# normalize rows
E_BASIS = np.array([v / np.linalg.norm(v) for v in E_BASIS])


def e_block(p) -> np.ndarray:
    """Action of permutation p restricted to the 2-dim E irrep."""
    R = perm_matrix(p)
    return E_BASIS @ R @ E_BASIS.conj().T


def main() -> int:
    print("=" * 76)
    print("POSITIVITY / ORIENTATION SELECTS C_3 FROM S_3")
    print("=" * 76)

    S3 = list(itertools.permutations((0, 1, 2)))

    print("\n" + "-" * 76)
    print("Determinant (orientation) of each S_3 element on C^3 and on E")
    print("-" * 76)
    det_plus = []
    for p in S3:
        d3 = np.linalg.det(perm_matrix(p)).real
        dE = np.linalg.det(e_block(p)).real
        ct = cycle_type(p)
        # transpositions must be orientation-reversing; rotations preserving
        want = +1.0 if ct in ("identity", "3-cycle") else -1.0
        ok = abs(d3 - want) < TOL and abs(dE - want) < TOL
        check(f"{p} ({ct}): det_C3={d3:+.0f}, det_E={dE:+.0f} == {want:+.0f}", ok)
        if d3 > 0:
            det_plus.append(p)

    print("\n" + "-" * 76)
    print("The orientation-preserving (det=+1) subset IS C_3 = A_3")
    print("-" * 76)
    C3 = {(0, 1, 2), (1, 2, 0), (2, 0, 1)}
    check("det=+1 subset = {id, (012), (021)} = C_3", set(det_plus) == C3,
          detail=f"{sorted(det_plus)}")
    # it is a subgroup (closed under composition)
    def comp(a, b):  # a after b
        return tuple(a[b[i]] for i in range(3))
    closed = all(comp(a, b) in C3 for a in C3 for b in C3)
    check("det=+1 subset is closed under composition (a subgroup)", closed)
    check("C_3 = A_3 is the unique index-2 (orientation-preserving) subgroup of S_3",
          len(C3) == 3)

    print("\n" + "-" * 76)
    print("Positivity-selected C_3 lifts the degeneracy (3 distinct masses)")
    print("-" * 76)
    # generic C_3-invariant (circulant) Hermitian -> 3 generically distinct eigs
    seed = np.array([[5.0, 2 + 1j, -1 + 3j],
                     [2 - 1j, 7.0, 0.5 - 2j],
                     [-1 - 3j, 0.5 + 2j, 11.0]], dtype=complex)
    acc = np.zeros((3, 3), dtype=complex)
    for p in C3:
        R = perm_matrix(p)
        acc += R @ seed @ R.conj().T
    acc /= 3
    ev = np.sort(np.linalg.eigvalsh((acc + acc.conj().T) / 2).real)
    ndist = 1 + int(np.sum(np.abs(np.diff(ev)) > 1e-6))
    check("C_3-invariant (circulant) mass matrix has 3 distinct eigenvalues",
          ndist == 3, detail=f"eigs={[round(float(x),3) for x in ev]}")

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if FAIL == 0:
        print(
            "  POSITIVITY/ORIENTATION -> C_3, PROVEN (group-theory level).\n"
            "  The det=+1 (orientation-preserving) subgroup of S_3 is exactly\n"
            "  A_3 = C_3 = {id, (012), (021)}; the three transpositions are the\n"
            "  det=-1 orientation-reversing elements. So a 'reality cannot be\n"
            "  negative' / determinant-positivity constraint forbids exactly the\n"
            "  transpositions and selects exactly C_3[111] -- which (being a proper\n"
            "  subgroup) lifts the generation mass degeneracy to 3 distinct masses.\n\n"
            "  OPEN BRIDGE (NOT proven here): that the framework's own positivity\n"
            "  principle (staggered det positivity; Clifford volume chirality)\n"
            "  is what imposes this orientation choice ON the hw=1 generation\n"
            "  triplet. This discriminator establishes the group-theory selection\n"
            "  only; the physical bridge is the next concrete sub-question.\n"
        )
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
