#!/usr/bin/env python3
"""
Koide Berry-monopole finite-matrix support packet. The native circulant
generation mass has a choice-free C3 index map, b-independent Fourier
eigenvectors, and zero Berry curvature. A separate two-band comparator shows
that a Gamma_chi-anticommuting coupling can carry nonzero Berry curvature. The
runner also checks the standalone Q(r=1/2)=2/3 and Q(r=1)=1 identities.

It does not derive a Berry/chirality-to-r weighting rule, select a physical Q
branch, derive a framework chiral coupling, approve an import, or set an audit
verdict.

  F1  INDEX MAP NATIVE. The 3 generations = Lambda^1(C^3) with C_3 = cyclic shift C; the
      C_3 DFT F diagonalizes C, and b is the C_3-DOUBLET Fourier amplitude of the mass
      operator H = aI + bC + b-bar C^2 (a = singlet amplitude). Canonical, choice-free.

  F2  NATIVE CIRCULANT BERRY CURVATURE IS ZERO, DERIVED. On the real
      circulant coordinate plane H = aI + u(C+C^2) + v i(C-C^2), matching the
      Fourier-amplitude coordinates in F1, the Berry curvature of the filled
      band is ZERO. The eigenvectors are the (u,v)-INDEPENDENT Fourier modes:
      the doublet coordinate shifts eigenvalues without rotating eigenvectors.

  F3  THE COMPUTABLE CRITERION. A 2-band coupling that ANTICOMMUTES with the
      chiral grading Gamma_chi (= sigma_z), e.g. u sigma_x + v sigma_y, has a
      NONZERO Berry monopole; a coupling that COMMUTES with Gamma_chi has zero
      Berry. This is a finite comparator, not a rule selecting a Koide branch.

  F4  THE NATIVE MASS IS NON-CHIRAL. Every native circulant Lambda^1
      mass COMMUTES with Gamma_chi (= 2 P_singlet - I, itself circulant):
      [H, Gamma_chi] = 0, so {H, Gamma_chi} != 0 -- it never anticommutes.
      Hence the native circulant algebra supplies the zero-Berry/commuting
      side of the finite comparison. The Q(r) identities are checked
      separately and do not select a physical branch.

CONCLUSION (bounded finite-matrix support, NOT a derivation of Q=2/3 or Q=1):
the index map is native and choice-free; the native circulant Berry curvature
is zero; an anticommuting two-band comparator has nonzero Berry curvature; and
the finite Q(r) identities hold. The missing positive route is the retained
bridge from Berry/chirality data to the physical r weighting and readout. The
generation R^3 circulant algebra cannot supply that anticommuting operator, but
an off-generation tensor factor remains an open route. READ-ONLY certificate;
tiers audit-decided.
"""

import sys

import numpy as np

PASSES: list[tuple[str, bool, str]] = []


def record(name, ok, detail=""):
    PASSES.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(t):
    print("\n" + "=" * 88 + f"\n{t}\n" + "=" * 88)


w = np.exp(2j * np.pi / 3)
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
C2 = C @ C
B = C + C2
S_im = 1j * (C - C2)
I3 = np.eye(3, dtype=complex)
P_singlet = np.ones((3, 3), dtype=complex) / 3
Gamma_chi = 2 * P_singlet - I3
F = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], dtype=complex) / np.sqrt(3)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)


def plaquette_berry(Hfun, b0r, b0i, h=0.01):
    """Fukui-Hatsugai lowest-band Berry phase on a small plaquette in the b-plane."""
    def gs(br, bi):
        vals, vecs = np.linalg.eigh(Hfun(br, bi))
        return vecs[:, np.argmin(vals)]
    p = [gs(b0r, b0i), gs(b0r + h, b0i), gs(b0r + h, b0i + h), gs(b0r, b0i + h)]
    prod = 1.0 + 0j
    for i in range(4):
        z = np.vdot(p[i], p[(i + 1) % 4])
        prod *= z / abs(z)
    return float(np.angle(prod))


def main():
    section("Koide Berry-monopole finite-matrix support: Q-branch selection remains open")

    # ---- F1: native index-map --------------------------------------------------
    section("F1 — index-map native: b = the C3-doublet Fourier amplitude of H")
    diag = F.conj().T @ C @ F
    record("F1.1 the C3 DFT diagonalizes the shift C (F^dag C F = diag(1,w,w^2))",
           np.allclose(diag, np.diag([1, w, w**2]), atol=1e-12),
           f"max off-diag = {np.max(np.abs(diag - np.diag(np.diag(diag)))):.1e}")
    a_v, b_v = 0.7, 0.3 + 0.2j
    H = a_v * I3 + b_v * C + np.conj(b_v) * C2
    grade1 = np.trace(np.linalg.matrix_power(C, -1) @ H) / 3   # Fourier-grade-1 = b
    record("F1.2 Fourier-grade projection (1/3)Tr(C^-1 H) = b (the doublet amplitude); "
           "grade-0 = a (singlet)",
           abs(grade1 - b_v) < 1e-12 and abs(np.trace(H) / 3 - a_v) < 1e-12,
           f"grade1 = {grade1:.3f} = b; grade0 = {np.trace(H)/3:.3f} = a")

    # ---- F2: native Berry curvature is zero ------------------------------------
    section("F2 — native circulant mass: Berry curvature = 0 (eigenvector rigidity)")
    def H_circ(br, bi):
        return a_v * I3 + br * B + bi * S_im
    # eigenvectors are the b-INDEPENDENT Fourier modes
    v_at_1 = np.linalg.eigh(H_circ(0.3, 0.2))[1]
    v_at_2 = np.linalg.eigh(H_circ(0.5, -0.1))[1]
    # each eigenvector matches a fixed Fourier column up to phase
    overlaps = [max(abs(np.vdot(F[:, k], v_at_1[:, j])) for k in range(3)) for j in range(3)]
    record("F2.1 eigenvectors of H_circ(b) are the b-INDEPENDENT Fourier modes "
           "(eigenvector rigidity)",
           all(abs(o - 1) < 1e-9 for o in overlaps),
           f"|<Fourier_k | eigvec_j>| = {[f'{o:.4f}' for o in overlaps]} (all 1)")
    berry_circ = [plaquette_berry(H_circ, 0.3, 0.2), plaquette_berry(H_circ, 0.4, -0.3)]
    record("F2.2 Berry curvature of the filled band on the native doublet plane = 0 "
           "(finite native algebra; no Q-branch selection)",
           all(abs(x) < 1e-6 for x in berry_circ),
           f"plaquette Berry = {[f'{x:.1e}' for x in berry_circ]} (= 0)")

    # ---- F3: the computable criterion (chiral -> nonzero monopole) -------------
    section("F3 — finite comparator: Gamma_chi-ANTICOMMUTING coupling -> nonzero Berry monopole")
    m = 0.5
    def H_chiral(br, bi):                       # Re(b) sx + Im(b) sy anticommute with sz
        return br * sx + bi * sy + m * sz
    def H_nonchiral(br, bi):                    # commutes with sz -> zero Berry
        return (a_v + br) * sz + 0 * sx
    record("F3.1 the b-coupling sigma_x, sigma_y ANTICOMMUTE with Gamma_chi=sigma_z; "
           "the mass m sigma_z COMMUTES",
           np.allclose(sx @ sz + sz @ sx, 0) and np.allclose(sy @ sz + sz @ sy, 0)
           and np.allclose(sz @ sz - sz @ sz, 0),
           "{sx,sz}={sy,sz}=0 (chiral coupling); [sz,sz]=0 (commuting mass)")
    berry_chiral = plaquette_berry(H_chiral, 0.3, 0.2, h=0.05)
    berry_nonchiral = plaquette_berry(H_nonchiral, 0.3, 0.2, h=0.05)
    record("F3.2 chiral (Gamma_chi-anticommuting) coupling has NONZERO Berry; "
           "non-chiral (commuting) has ZERO Berry",
           abs(berry_chiral) > 1e-3 and abs(berry_nonchiral) < 1e-6,
           f"Berry(chiral) = {berry_chiral:.4f} (!=0, monopole); "
           f"Berry(non-chiral) = {berry_nonchiral:.1e} (=0)")

    # ---- F4: the native mass is non-chiral; Q(r) identities are separate --------
    section("F4 — native circulant mass COMMUTES with Gamma_chi; Q(r) identities are separate")
    Hc = a_v * I3 + 0.31 * B + 0.21 * S_im
    record("F4.1 [H_circ, Gamma_chi] = 0 (both circulant) -> {H_circ, Gamma_chi} != 0 "
           "-> the native mass NEVER anticommutes -> non-chiral -> Berry=0",
           np.allclose(Hc @ Gamma_chi - Gamma_chi @ Hc, 0, atol=1e-12)
           and np.max(np.abs(Hc @ Gamma_chi + Gamma_chi @ Hc)) > 0.1,
           f"|[H,Gamma_chi]| = {np.max(np.abs(Hc@Gamma_chi - Gamma_chi@Hc)):.1e}; "
           f"|{{H,Gamma_chi}}| = {np.max(np.abs(Hc@Gamma_chi + Gamma_chi@Hc)):.2f} (!=0)")
    # Q link from signed circulant eigenvalues
    def Q_at(r):
        bb = np.sqrt(r) * a_v
        lam = np.sort(np.linalg.eigvals(a_v * I3 + bb * C + bb * C2).real)
        return sum(lam**2) / (sum(lam))**2
    record("F4.2 finite Koide algebra identities: Q(r=1/2)=2/3 and Q(r=1)=1 "
           "(no branch-selection rule asserted)",
           abs(Q_at(0.5) - 2 / 3) < 1e-9 and abs(Q_at(1.0) - 1) < 1e-9,
           f"Q(r=1/2) = {Q_at(0.5):.6f}; Q(r=1) = {Q_at(1.0):.6f}")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"  {n_pass}/{len(PASSES)} checks passed")
    print()
    print("  BOUNDED FINITE-MATRIX SUPPORT:")
    print("    native circulant generation mass: C3-native, Fourier-rigid, Berry=0")
    print("    toy anticommuting two-band comparator: nonzero Berry monopole")
    print("    finite Koide algebra: Q(r=1/2)=2/3 and Q(r=1)=1")
    print("  No Berry/chirality-to-r weighting rule or physical Q branch is derived.")
    print("  The generation R^3 circulant algebra cannot supply the anticommuting")
    print("  operator. Next route remains an off-generation factor plus a retained")
    print("  readout/weighting bridge.")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
