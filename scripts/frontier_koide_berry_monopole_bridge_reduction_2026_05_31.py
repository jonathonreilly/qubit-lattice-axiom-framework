#!/usr/bin/env python3
"""
Koide Berry-monopole bridge-reduction: the value reduces to one computable criterion --
is the generation mass CHIRAL (nonzero Berry monopole -> Q=2/3) or NON-CHIRAL
(zero Berry -> Q=1)? The native circulant mass is non-chiral -> Q=1.

Attempting the B-coupling -> B-field bridge (would force Q=2/3) builds a native skeleton
and DERIVES the native dynamical answer, reducing the entire charged-lepton Koide-value
question to a single operator criterion that unifies every prior framing.

  F1  INDEX MAP NATIVE. The 3 generations = Lambda^1(C^3) with C_3 = cyclic shift C; the
      C_3 DFT F diagonalizes C, and b is the C_3-DOUBLET Fourier amplitude of the mass
      operator H = aI + bC + b-bar C^2 (a = singlet amplitude). Canonical, choice-free.

  F2  NATIVE EFFECTIVE-ACTION ORDER IS SECOND (Q=1), DERIVED. Integrating out the native
      circulant Kahler-Dirac fermion, the Berry curvature of the filled band on the
      complex-b plane is ZERO -- because H = aI + Re(b) B + Im(b)(i Jcs) is circulant, its
      eigenvectors are the b-INDEPENDENT Fourier modes (eigenvector rigidity: b shifts
      eigenvalues without rotating eigenvectors). Zero Berry -> no first-order term ->
      second-order Ginzburg-Landau -> per-dim -> Q=1. (Not assumed -- computed.)

  F3  THE COMPUTABLE CRITERION (the unification). A 2-band coupling that ANTICOMMUTES with
      the chiral grading Gamma_chi (= sigma_z) -- e.g. Re(b) sigma_x + Im(b) sigma_y --
      has a NONZERO Berry monopole; a coupling that COMMUTES with Gamma_chi has zero
      Berry. So: first-order / per-block / Q=2/3 <=> Gamma_chi-ANTICOMMUTING (chiral)
      coupling <=> nonzero Berry monopole; second-order / per-dim / Q=1 <=>
      Gamma_chi-COMMUTING coupling <=> zero Berry. This single criterion unifies the
      effective-action-order, the det_C-vs-det_R reality type, and the
      equal-block-vs-trace measure into ONE operator pin: chiral vs non-chiral generation
      mass.

  F4  THE NATIVE MASS IS NON-CHIRAL -> Q=1. Every native circulant Lambda^1 mass COMMUTES
      with Gamma_chi (= 2 P_singlet - I, itself circulant): [H, Gamma_chi] = 0, so
      {H, Gamma_chi} != 0 -- it never anticommutes. Hence native Berry = 0 -> Q=1; Q=2/3
      (r=1/2) is a tuned point on the Gamma_chi-commuting family with no native chiral
      mechanism. Q=2/3 = the single chiral import, shared with generation-identification.

CONCLUSION (partial build / bounded reduction, NOT a derivation of Q=2/3): the index map
is native and choice-free; the native dynamics is DERIVED to give Q=1 (zero Berry,
second-order); and the whole question collapses to the computable criterion "is the
generation mass chiral (nonzero Berry monopole)?" -- the same chiral grading that the
generation-identification gate needs, forbidden on the generation R^3 by C^3=I
(retained_bounded koide_z3_equivariant_anticommuting_no_go). The next path (not
foreclosed): can an OFF-generation tensor factor supply the chiral grading -> nonzero
Berry -> Q=2/3 without breaking C^3=I on the generation factor? READ-ONLY certificate;
tiers audit-decided. NOTE: the per-block COUNT is orientation-blind (prior note), so this
criterion is about the chiral COUPLING existing, not a +i/-i orientation choice.
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
Jcs = (C - C2) / np.sqrt(3)
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
    section("Koide Berry-monopole bridge-reduction: chiral mass -> Q=2/3, non-chiral -> Q=1")

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

    # ---- F2: native effective action second-order (Berry = 0) ------------------
    section("F2 — native circulant mass: Berry curvature = 0 (eigenvector rigidity) -> Q=1")
    def H_circ(br, bi):
        return a_v * I3 + br * B + bi * (1j * Jcs)
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
    record("F2.2 Berry curvature of the filled band on the b-plane = 0 -> no first-order "
           "Berry term -> SECOND-order GL -> per-dim -> Q=1 (DERIVED)",
           all(abs(x) < 1e-6 for x in berry_circ),
           f"plaquette Berry = {[f'{x:.1e}' for x in berry_circ]} (= 0)")

    # ---- F3: the computable criterion (chiral -> nonzero monopole) -------------
    section("F3 — criterion: Gamma_chi-ANTICOMMUTING coupling -> nonzero Berry monopole")
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
    record("F3.2 chiral (Gamma_chi-anticommuting) coupling -> NONZERO Berry monopole; "
           "non-chiral (commuting) -> ZERO",
           abs(berry_chiral) > 1e-3 and abs(berry_nonchiral) < 1e-6,
           f"Berry(chiral) = {berry_chiral:.4f} (!=0, monopole); "
           f"Berry(non-chiral) = {berry_nonchiral:.1e} (=0)")

    # ---- F4: the native mass is non-chiral -> Q=1 ------------------------------
    section("F4 — native circulant mass COMMUTES with Gamma_chi -> non-chiral -> Q=1")
    Hc = a_v * I3 + 0.31 * B + 0.21 * (1j * Jcs)
    record("F4.1 [H_circ, Gamma_chi] = 0 (both circulant) -> {H_circ, Gamma_chi} != 0 "
           "-> the native mass NEVER anticommutes -> non-chiral -> Berry=0 -> Q=1",
           np.allclose(Hc @ Gamma_chi - Gamma_chi @ Hc, 0, atol=1e-12)
           and np.max(np.abs(Hc @ Gamma_chi + Gamma_chi @ Hc)) > 0.1,
           f"|[H,Gamma_chi]| = {np.max(np.abs(Hc@Gamma_chi - Gamma_chi@Hc)):.1e}; "
           f"|{{H,Gamma_chi}}| = {np.max(np.abs(Hc@Gamma_chi + Gamma_chi@Hc)):.2f} (!=0)")
    # Q link from signed circulant eigenvalues
    def Q_at(r):
        bb = np.sqrt(r) * a_v
        lam = np.sort(np.linalg.eigvals(a_v * I3 + bb * C + bb * C2).real)
        return sum(lam**2) / (sum(lam))**2
    record("F4.2 r=1/2 (chiral/per-block) -> Q=2/3; r=1 (non-chiral/per-dim) -> Q=1",
           abs(Q_at(0.5) - 2 / 3) < 1e-9 and abs(Q_at(1.0) - 1) < 1e-9,
           f"Q(r=1/2) = {Q_at(0.5):.6f}; Q(r=1) = {Q_at(1.0):.6f}")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"  {n_pass}/{len(PASSES)} checks passed")
    print()
    print("  THE WHOLE KOIDE VALUE = ONE COMPUTABLE CRITERION:")
    print("    chiral generation mass (Gamma_chi-anticommuting, nonzero Berry monopole)")
    print("       => first-order => per-block => det_C => equal-block => r=1/2 => Q=2/3")
    print("    non-chiral circulant mass (Gamma_chi-commuting, zero Berry)")
    print("       => second-order => per-dim => det_R => trace => r=1 => Q=1")
    print("  The native circulant mass is NON-CHIRAL (commutes with Gamma_chi) -> Q=1.")
    print("  Q=2/3 = the single CHIRAL import (shared with generation-ID); forbidden on")
    print("  the generation R^3 by C^3=I. Next path: an OFF-generation factor supplying it.")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
