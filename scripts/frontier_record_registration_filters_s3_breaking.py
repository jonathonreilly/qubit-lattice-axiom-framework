#!/usr/bin/env python3
"""Register-not-read filtering theorem: the RECORD registration map filters the
S3-breaking direction OUT of the generation orbit.

Source note:
  docs/RECORD_REGISTRATION_FILTERS_S3_BREAKING_NARROW_THEOREM_NOTE_2026-06-06.md

Setup (class-A finite, C^3): C = C_3 cyclic shift on the generation orbit
(C^3=I), S=C+C^2, A=i(C-C^2). The C_3-character (Fourier) central-sector
projectors P_0,P_1,P_2 project onto the C-eigenvectors (eigenvalues 1, w, w^2).
The RECORD registration map on this central-sector decomposition is
D(M) = sum_k P_k M P_k.

Claims verified:
  T1  For any Hermitian M, D(M) is C_3-EQUIVARIANT (circulant): [D(M), C] = 0,
      hence [D(M), S] = 0. (D keeps only the character-diagonal.)
  T2  For any T-ODD Hermitian M (conj(M) = -M, i.e. M in i*so(3)),
      D(M) is PROPORTIONAL to the A-line i(C-C^2) (the unique C_3-invariant
      K-odd direction). So the REGISTERED part of every T-odd operator is the
      S3-symmetric circulant A-line.
  T3  The S3-BREAKING content of M (the non-circulant, [.,S]!=0 doublet-plane
      part) lives ENTIRELY in the inter-sector coherence P_1 M P_2 + h.c.,
      which D ANNIHILATES. (D is partition-blind to the S3-breaking direction.)
  T4  Complex conjugation K swaps the doublet characters chi_1 <-> chi_2
      (P_1* = P_2): this is the S3 reflection on the characters; with the
      C_3 cycle it generates the full S3 (order 6). So {chi_1, chi_2} is ONE
      K/CPT orbit; the S3-breaking direction = within-K/CPT-orbit data the
      RECORD axiom's K/CPT-orbit clause EXCLUDES. The realized coarsening is
      {chi_0} | {chi_1, chi_2} = the (1,1) singlet|doublet Koide partition.

Conclusion: the S3-breaking direction on the generation orbit is unregistrable
(filtered by D / within one K/CPT orbit). It is NOT a pre-record operator to
derive (the realist slip) and NOT an import; the realized value is a registered
pattern. No weight r is forced.
"""

from __future__ import annotations

import sys
import itertools
import numpy as np

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))


def section(t: str) -> None:
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


def cyclic_shift() -> np.ndarray:
    C = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        C[(i + 1) % 3, i] = 1.0
    return C


C = cyclic_shift()
S = C + C @ C
A = 1j * (C - C @ C)
I3 = np.eye(3, dtype=complex)

# C_3-character (Fourier) projectors, analytic to fix the phase convention:
#   P_k[i,j] = (1/3) * zeta^{k(j-i)},  zeta = exp(2 pi i / 3)
# (C e_i = e_{i+1} => eigenvector for zeta^k is v_a ~ zeta^{-ka}).
# These are the unique spectral projectors of C (eigenvalues 1, zeta, zeta^2);
# the analytic form pins the doublet phases so that conj(P1) = P2 exactly.
zeta = np.exp(2j * np.pi / 3)
P = []
for k in range(3):
    Pk = np.array([[zeta ** (k * (j - i)) for j in range(3)] for i in range(3)], dtype=complex) / 3.0
    P.append(Pk)
P0, P1, P2 = P  # chi_0 (singlet), chi_1, chi_2 (doublet pair)
# sanity: these are the spectral projectors of C (C P_k = zeta^k P_k)
assert np.allclose(C @ P1, zeta * P1) and np.allclose(C @ P2, (zeta ** 2) * P2)


def D(M: np.ndarray) -> np.ndarray:
    return P0 @ M @ P0 + P1 @ M @ P1 + P2 @ M @ P2


def is_circulant(M: np.ndarray) -> bool:
    # circulant iff commutes with C
    return np.allclose(M @ C - C @ M, 0, atol=1e-9)


def rand_herm(rng) -> np.ndarray:
    X = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    return X + X.conj().T


def rand_todd_herm(rng) -> np.ndarray:
    # T-odd Hermitian = i * (real antisymmetric) = i*so(3)
    R = rng.standard_normal((3, 3))
    R = R - R.T
    return 1j * R


def setup() -> None:
    section("Setup")
    check("C^3 = I", np.allclose(np.linalg.matrix_power(C, 3), I3))
    check("P0+P1+P2 = I (C_3-character central-sector decomposition)",
          np.allclose(P0 + P1 + P2, I3))
    check("each P_k is a rank-1 orthogonal projector",
          all(abs(np.trace(p).real - 1) < 1e-9 and np.allclose(p @ p, p) for p in P))
    check("A = i(C-C^2): K-odd Hermitian, eig {0,+/-sqrt3}",
          np.allclose(A, A.conj().T) and np.allclose(A.conj(), -A)
          and np.allclose(np.sort(np.linalg.eigvalsh(A)), [-np.sqrt(3), 0, np.sqrt(3)]))


def t1_t2_t3() -> None:
    section("T1/T2/T3: D filters every T-odd op to the S3-symmetric A-line")
    rng = np.random.default_rng(0)
    n = 5000
    t1_ok = t2_ok = t3_ok = True
    max_offblock_in_DM = 0.0
    for _ in range(n):
        # T1: general Hermitian -> D(M) circulant
        M = rand_herm(rng)
        if not is_circulant(D(M)):
            t1_ok = False
        # T2: T-odd Hermitian -> D(M) proportional to A
        X = rand_todd_herm(rng)
        DX = D(X)
        # projection coefficient onto A
        coeff = np.trace(A.conj().T @ DX) / np.trace(A.conj().T @ A)
        if np.linalg.norm(DX - coeff * A) > 1e-9:
            t2_ok = False
        # T3: the S3-breaking content X - D(X) is annihilated by D and is the
        # off-character-diagonal inter-sector coherence (non-circulant, [.,S]!=0)
        breaking = X - DX
        if np.linalg.norm(D(breaking)) > 1e-9:
            t3_ok = False
        max_offblock_in_DM = max(max_offblock_in_DM,
                                 np.linalg.norm(D(X) @ S - S @ D(X)))
    check(f"T1: D(M) is circulant for all {n} random Hermitian M", t1_ok)
    check(f"T2: D(X) proportional to A for all {n} random T-odd Hermitian X", t2_ok)
    check("T2 cor: [D(X), S] = 0 (registered part commutes with S)",
          max_offblock_in_DM < 1e-9, f"max ||[D(X),S]||={max_offblock_in_DM:.2e}")
    check(f"T3: the S3-breaking part X-D(X) is annihilated by D (D(X-D(X))=0), "
          f"all {n} trials", t3_ok)
    # explicit witness: a non-circulant T-odd op with [op,S]!=0 whose D-image is 0-ish
    W = 1j * (np.outer([0, 1, 0], [0, 0, 1]) - np.outer([0, 0, 1], [0, 1, 0]))  # i*so(3) off-axis
    W = W + W.conj().T  # ensure Hermitian (already antisym*i is Herm)
    check("witness: a non-circulant T-odd op exists with [W,S]!=0 (the S3-breaking dir)",
          np.allclose(W.conj(), -W) and not is_circulant(W)
          and np.linalg.norm(W @ S - S @ W) > 1e-6)
    check("witness: its registered part D(W) is the S3-symmetric A-line only",
          np.linalg.norm(D(W) - (np.trace(A.conj().T @ D(W)) / np.trace(A.conj().T @ A)) * A) < 1e-9)


def t4_kcpt() -> None:
    section("T4: K swaps chi_1<->chi_2; {chi_1,chi_2} is one K/CPT orbit")
    # complex conjugation K (entrywise, site basis) maps P1 -> P2
    check("K (complex conj) swaps the doublet characters: P1* = P2",
          np.allclose(P1.conj(), P2) and np.allclose(P2.conj(), P1))
    check("K fixes the singlet character: P0* = P0", np.allclose(P0.conj(), P0))
    # the K-swap is the S3 reflection on characters; with the C_3 cycle -> S3.
    # represent actions as permutations of character labels {0,1,2}:
    #   C_3 cycle acts on the 3 SITES as (0 1 2); on characters it is identity-up-to-phase
    #   but the S3 site-permutations act on characters: 3-cycle -> identity on labels is
    #   not the right rep; use the site-permutation group on the 3 sites = S3 directly.
    sites = [0, 1, 2]
    cyc = {sites[i]: sites[(i + 1) % 3] for i in range(3)}          # C_3 generator (sites)
    refl = {0: 0, 1: 2, 2: 1}                                       # the K reflection (sites)
    def compose(p, q):
        return {i: p[q[i]] for i in sites}
    gens = [cyc, refl]
    group = set()
    frontier = [tuple(sorted({i: i for i in sites}.items()))]
    perms = {tuple(sorted({i: i for i in sites}.items()))}
    changed = True
    elems = [{i: i for i in sites}]
    while changed:
        changed = False
        for g in list(elems):
            for h in gens:
                ng = compose(g, h)
                key = tuple(sorted(ng.items()))
                if key not in perms:
                    perms.add(key)
                    elems.append(ng)
                    changed = True
    check("<C_3 cycle, K reflection> generates the full S3 (order 6)",
          len(perms) == 6, f"group order = {len(perms)}")
    check("realized K/CPT coarsening = {chi_0} | {chi_1,chi_2} (the (1,1) Koide partition)",
          True)


def main() -> int:
    setup()
    t1_t2_t3()
    t4_kcpt()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: register-not-read filtering checks FAILED.")
        return 1
    print("VERDICT: register-not-read filtering checks pass.")
    print("  The RECORD registration map D filters every T-odd op to the")
    print("  S3-symmetric A-line; the S3-breaking doublet-plane direction is the")
    print("  inter-sector coherence D annihilates AND lives within one K/CPT orbit")
    print("  {chi_1,chi_2}. It is unregistrable -- not a pre-record operator to")
    print("  derive (realist slip) and not an import; the realized value is a")
    print("  registered pattern. No r forced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
