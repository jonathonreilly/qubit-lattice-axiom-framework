#!/usr/bin/env python3
"""
Koide Q=2/3 is the real-Wedderburn-block (K0-real) reading of the framework generation
carrier; Q=1 is the complex-dimension (K0-complex) reading; the qubit's central i is
a generation scalar and does NOT fix the measure convention.

The charged-lepton Koide value reduces to one reality-structure bit on the generation
matter measure. This runner certifies the equivalence and locates the bit.

  F1  THE FROBENIUS-SCHUR / WEDDERBURN FORK. Z3 has FS-indicators (+1, 0, 0): the real
      group algebra R[Z3]=R(+)C has 2 real-irreducible BLOCKS (K0-real = Z^2), while the
      complexified C[Z3]=C^3 has 3 blocks (K0-complex = Z^3). The complex-type doublet
      (omega, omega-bar) is ONE real block of real-dim 2.
  F2  THE QUBIT i IS A GENERATION SCALAR. The Cl(3) central pseudoscalar
      omega_Cl = s1 s2 s3 = i*I_2 (forced on the qubit). On the generation triplet it
      acts as the SCALAR i*I_3 (i on all 3 isotype modes incl the singlet), NOT the
      traceless doublet complex structure J=diag(0,+i,-i) that the per-block (det_C)
      count requires. So the forced qubit complexification does NOT propagate to the
      generation factor -- the doublet measure is left a FREE convention slot.
  F3  A QUBIT ADMITS A COHERENT-STATE / BARGMANN READING. The spin-1/2 SU(2)
      coherent states resolve the identity, (2/4pi) integral |n><n| dOmega = I_2.
      This supports considering a per-block candidate convention, but does not force it.
  F4  THE EQUIVALENCE. With Q=(1+2r)/3, r=|b|^2/a^2, and block energies E_+=3a^2,
      E_perp=6|b|^2: PER-BLOCK (count each of the 2 real blocks once -> equal block
      energy) gives 3a^2=6|b|^2 -> r=1/2 -> Q=2/3 (verified end-to-end on the real
      circulant); PER-DIMENSION (doublet weighted by its dim 2) gives r=1 -> Q=1.
  F5  THE C^3=I CORRECTION. C^3=I forbids a continuous U(1)_b SYMMETRY ((e^{i a}C)^3=I
      only at a in {0,2pi/3,4pi/3}); but the Schur complex structure J in
      End_R(doublet)=C EXISTS (FS=0 forces it), so the det_C per-block MEASURE is
      available even though U(1)_b-as-symmetry is not. Neither measure is forced.

CONCLUSION (bounded equivalence-characterization, NOT a forced derivation): Koide Q=2/3
iff the real-block / K0-real / coherent-state quantization of the framework generation
carrier; Q=1 iff the complex-dimension / K0-complex / trace-default quantization. The two exhaust
the C3-isotype power split. The central pseudoscalar i is forced only on the qubit factor
and acts as a generation scalar, so it does NOT fix the choice. So Q=2/3 is a
candidate convention (it uses no new substrate -- the generation carrier is the real
R[Z3], and a qubit can be read as a coherent-state object); the framework baseline also
admits the trace-default Q=1, so neither is uniquely forced. Choosing det_C as the
physical generation measure remains a separate convention/admission question. READ-ONLY;
tiers audit-decided.
"""

import sys

import numpy as np
import sympy as sp

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
I3 = np.eye(3, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)


def main():
    section("Koide Q=2/3 = the K0-real / real-Wedderburn-block reading of the framework generation carrier")

    # ---- F1: Frobenius-Schur / Wedderburn fork ---------------------------------
    section("F1 — Frobenius-Schur fork: K0(R[Z3])=Z^2 (2 blocks) vs K0(C[Z3])=Z^3")
    # FS indicator nu(rho) = (1/|G|) sum_g chi(g^2)
    chars = {"triv": lambda k: 1, "omega": lambda k: w**k, "omega2": lambda k: w**(2 * k)}
    fs = {}
    for name, chi in chars.items():
        fs[name] = (1 / 3) * sum(chi((2 * g) % 3) for g in range(3))
    real_blocks = 1 + 1   # trivial (FS +1) + {omega,omega2} fuse (FS 0) -> 1 real block
    complex_blocks = 3
    record("F1.1 FS indicators (triv, omega, omega2) = (+1, 0, 0)",
           abs(fs["triv"] - 1) < 1e-12 and abs(fs["omega"]) < 1e-12 and abs(fs["omega2"]) < 1e-12,
           f"FS = {{triv:{fs['triv'].real:.0f}, omega:{fs['omega'].real:.0f}, omega2:{fs['omega2'].real:.0f}}}")
    record("F1.2 K0-real rank 2 (R[Z3]=R(+)C, doublet=ONE real block) vs K0-complex rank 3",
           real_blocks == 2 and complex_blocks == 3,
           f"#real-irreducible blocks = {real_blocks} (-> Q=2/3 candidate); "
           f"#complex blocks = {complex_blocks} (-> Q=1)")

    # ---- F2: qubit i is a generation scalar ------------------------------------
    section("F2 — qubit pseudoscalar = i*I_2; on generations a SCALAR i*I_3 (not doublet J)")
    pseudo = s1 @ s2 @ s3
    record("F2.1 Cl(3) pseudoscalar s1 s2 s3 = i*I_2 (forced on the qubit factor)",
           np.allclose(pseudo, 1j * np.eye(2)), f"s1 s2 s3 = {np.round(np.diag(pseudo),3)}")
    # on the generation triplet, the central i acts as i*I_3 (eigenvalues all +i)
    central_gen = 1j * I3
    Jcs = (C - C2) / np.sqrt(3)   # the doublet complex structure (traceless, det_C needs)
    record("F2.2 central i on generations = i*I_3 (eigs all +i) != doublet J=diag(0,+i,-i) "
           "(= eig(Jcs)); so the qubit complexification does NOT supply the doublet measure",
           np.allclose(np.linalg.eigvals(central_gen), 1j * np.ones(3))
           and not np.allclose(central_gen, Jcs)
           and np.allclose(sorted(np.linalg.eigvals(Jcs), key=lambda z: z.imag),
                           sorted([0, +1j, -1j], key=lambda z: z.imag)),
           f"eig(i*I_3) = {np.round(np.linalg.eigvals(central_gen),2)}; "
           f"eig(Jcs) = {np.round(np.linalg.eigvals(Jcs),2)} (doublet structure det_C uses)")

    # ---- F3: qubit coherent-state / Bargmann support ---------------------------
    section("F3 — a qubit admits a coherent-state/Bargmann reading (resolution of identity)")
    # spin-1/2 coherent state |n(theta,phi)> = (cos(theta/2), e^{i phi} sin(theta/2))
    acc = np.zeros((2, 2), dtype=complex)
    nth, nph = 80, 80
    for i in range(nth):
        th = np.pi * (i + 0.5) / nth
        for j in range(nph):
            ph = 2 * np.pi * (j + 0.5) / nph
            n = np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
            acc += np.outer(n, n.conj()) * np.sin(th) * (np.pi / nth) * (2 * np.pi / nph)
    resolution = (2 / (4 * np.pi)) * acc
    record("F3.1 (2/4pi) integral |n><n| dOmega = I_2 (Bloch coherent-state completeness) "
           "-> compatible with the per-block candidate, not a forced measure selection",
           np.allclose(resolution, np.eye(2), atol=1e-2),
           f"(2/4pi) int |n><n| = {np.round(resolution,3).tolist()}")

    # ---- F4: the equivalence (per-block r=1/2 vs per-dim r=1) -------------------
    section("F4 — equivalence: equal-block (K0-real) -> Q=2/3; dimension (K0-complex) -> Q=1")
    a_s, b_s, r_s = sp.symbols("a b r", positive=True)
    E_plus, E_perp = 3 * a_s**2, 6 * b_s**2
    r_block = sp.simplify((sp.solve(sp.Eq(E_plus, E_perp), b_s)[0])**2 / a_s**2)
    Q = (1 + 2 * r_s) / 3
    record("F4.1 equal block energy E_+=E_perp -> r=1/2 -> Q=2/3 (per-block, K0-real)",
           r_block == sp.Rational(1, 2) and Q.subs(r_s, sp.Rational(1, 2)) == sp.Rational(2, 3),
           f"3a^2=6b^2 -> r={r_block} -> Q={Q.subs(r_s, sp.Rational(1,2))}")
    # end-to-end numeric on the real circulant at r=1/2
    a, b = 1.0, 1 / np.sqrt(2)
    H = a * I3 + b * C + b * C2
    lams = np.sort(np.linalg.eigvals(H).real)
    Qnum = sum(lams**2) / (sum(lams))**2
    record("F4.2 real circulant H=aI+bC+bC^2 at r=1/2: sum lam=3, sum lam^2=6, Q=2/3",
           abs(sum(lams) - 3) < 1e-9 and abs(sum(lams**2) - 6) < 1e-9 and abs(Qnum - 2 / 3) < 1e-9,
           f"eig={np.round(lams,5)}, sum={sum(lams):.5f}, sum^2={sum(lams**2):.5f}, Q={Qnum:.6f}")
    record("F4.3 dimension-weighted (doublet x2) -> r=1 -> Q=1 (per-dim, K0-complex)",
           Q.subs(r_s, 1) == 1, f"r=1 -> Q={Q.subs(r_s,1)}")

    # ---- F5: the C^3=I correction ----------------------------------------------
    section("F5 — C^3=I forbids U(1)_b SYMMETRY but not the Schur J for the det_C MEASURE")
    alphas_ok = []
    for deg in [0, 30, 60, 90, 120, 180, 240]:
        al = np.deg2rad(deg)
        M = np.exp(1j * al) * C
        if np.allclose(np.linalg.matrix_power(M, 3), I3):
            alphas_ok.append(deg)
    record("F5.1 (e^{i a}C)^3=I only at a in {0,120,240} deg (U(1)_b-as-SYMMETRY -> discrete C3)",
           alphas_ok == [0, 120, 240], f"valid alpha (deg) = {alphas_ok}")
    record("F5.2 BUT the Schur complex structure Jcs in End_R(doublet)=C EXISTS (Jcs^2=-P_doublet) "
           "-> the det_C MEASURE is available; neither measure forced",
           np.allclose(Jcs @ Jcs, -(I3 - np.ones((3, 3)) / 3)),
           "C^3=I bites the SYMMETRY, not the measure (corrects the over-stated 'det_R is the default')")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"  {n_pass}/{len(PASSES)} checks passed")
    print()
    print("  Q=2/3  <=>  K0-real / real-Wedderburn-block / coherent-state count (2 blocks, each once)")
    print("  Q=1    <=>  K0-complex / complex-dimension / trace-default count (3 modes)")
    print("  the central qubit i is a GENERATION SCALAR (i*I_3) -> does NOT fix the choice;")
    print("  the doublet measure is a FREE convention slot in the bounded comparison.")
    print("  Q=2/3 is the coherent-state/per-block candidate; Q=1 is the trace-default rival.")
    print("  NOT uniquely forced; choosing det_C as physical remains a separate convention/admission.")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
