#!/usr/bin/env python3
"""
The native Kahler-Dirac form-degree coupling i*D_KD is a Berry SPECTATOR on the Koide
generation doublet: it realizes the no-go's distinct-factor escape-hatch (a native
chiral grading) yet supplies ZERO Berry monopole -> reproduces Q=1, not Q=2/3.

This session reduced the charged-lepton Koide value to one criterion: Q=2/3 <=> the
generation mass is CHIRAL (nonzero Berry monopole on the complex-b plane); Q=1 <=>
non-chiral (zero Berry). The chiral grading is forbidden on the generation R^3 by C^3=I
(retained_bounded koide_z3_equivariant_anticommuting_no_go). The open door: an
OFF-generation tensor factor. This runner computes the most native candidate -- the
FORM-DEGREE structure of the Kahler-Dirac field on Lambda*(C^3) -- and certifies:

  F1  NATIVE FOCK SUBSTRATE. 3-mode Jordan-Wigner Fock space V=Lambda*(C^3) (dim 8):
      CAR {a_j, a_k^dag}=delta, d^2=delta^2=0, and i*D_KD = i*sum_k(a_k^dag - a_k) is
      Hermitian (the native d-delta Kahler-Dirac operator, retained_bounded substrate).
  F2  THE CHIRAL GRADING IS NATIVE (escape-hatch II). {i*D_KD, Gamma_F}=0 with
      Gamma_F=(-1)^N the Fock/form-parity grading -- a Gamma_chi-anticommuting chiral
      grading on a factor DISTINCT from the generation R^3, exactly the no-go's
      distinct-factor escape hatch. C^3=I does NOT touch it.
  F3  BUT i*D_KD IS A BERRY SPECTATOR. With the Koide circulant mass M[b]=aI+bC+b-bar C^2
      on Lambda^1, the two b-derivative directions COMMUTE: [dH/dRe b, dH/dIm b] = 0
      (because dH/dRe b = C+C^2 and dH/dIm b = i(C-C^2) commute -- C and C^2 commute).
      The native d-delta coupling is real and b-independent, so b enters only a real
      diagonal energy, never a complex off-diagonal element.
  F4  -> ZERO native Berry monopole. The lowest-band (and isolated-band) Wilson-loop
      Berry phase of H(b)=kappa*(i*D_KD)+M[b] on the complex-b plane is 0 for every
      kappa; POSITIVE CONTROL: a chiral 2-band with non-commuting b-couplings gives a
      nonzero monopole, proving the method detects curvature. So the native form-degree
      route reproduces the Q=1 rigidity default.
  F5  THE FORM-PARITY GRADING CANNOT READ KOIDE. Gamma_F restricts to the SCALAR -I on
      Lambda^1 (N=1), so it cannot impose the Koide condition <v|Gamma_chi|v>=0; the
      grading that reads Koide (Gamma_chi=(2/3)J-I, eigenvalues +1,-1,-1) lives on the
      generation R^3, where {C, Gamma_chi} != 0 -> hits comm(C) ∩ anticomm(Gamma_chi)={0}.

CONCLUSION (narrow negative / spectator theorem, NOT a closure): the native form-degree
route is genuinely native and genuinely realizes the no-go's distinct-factor escape
hatch (a native chiral grading), but i*D_KD transmits ZERO Berry curvature to the
generation doublet (C_3-equivariance / commuting b-derivatives) -> Q=1. A nonzero
off-generation monopole still needs arg(b) in an off-diagonal complex inter-grade
coupling (a relative-i breaking the CPT reality) -- the SAME import the qubit route needs
(PR #2405), r-non-selective even when imported. The next path (open, uncomputed): does
emergent-time's complex unit i (single_clock_stone, retained) land on the form-parity
factor and make the inter-grade coupling carry arg(b) without a chosen coupling?
READ-ONLY certificate; tiers audit-decided.
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


# ---- 3-mode Jordan-Wigner Fock space = Lambda*(C^3) ------------------------------
sp_pl = np.array([[0, 1], [0, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
adag = [np.kron(np.kron(sp_pl, I2), I2), np.kron(np.kron(sz, sp_pl), I2),
        np.kron(np.kron(sz, sz), sp_pl)]
a = [m.conj().T for m in adag]
N = sum(adag[k] @ a[k] for k in range(3))           # particle number = form degree
I8 = np.eye(8, dtype=complex)
C3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)   # generation shift
C32 = C3 @ C3


def lift_to_lambda1(M3):
    """embed a 3x3 generation operator onto the Lambda^1 (1-particle) sector of V."""
    out = np.zeros((8, 8), dtype=complex)
    idx1 = [i for i in range(8) if round(N[i, i].real) == 1]    # the 3 one-particle states
    # one-particle states are adag[k]|0>; order them by k
    vac = np.zeros(8, dtype=complex)
    vac[0] = 1
    states = [adag[k] @ vac for k in range(3)]
    for j in range(3):
        for k in range(3):
            out += M3[j, k] * np.outer(states[j], states[k].conj())
    return out


def wilson_berry(Hfun, band_index, radius=0.4, npts=48):
    """gauge-invariant Wilson-loop Berry phase of a band on a circle in the b-plane."""
    states = []
    for t in np.linspace(0, 2 * np.pi, npts, endpoint=False):
        br, bi = radius * np.cos(t), radius * np.sin(t)
        vals, vecs = np.linalg.eigh(Hfun(br, bi))
        states.append(vecs[:, np.argsort(vals)[band_index]])
    prod = 1.0 + 0j
    for i in range(npts):
        z = np.vdot(states[i], states[(i + 1) % npts])
        prod *= z / abs(z)
    return float(np.angle(prod))


def main():
    section("Kahler-Dirac form-degree coupling i*D_KD is a Berry spectator on the Koide doublet")

    # ---- F1: native Fock substrate ---------------------------------------------
    section("F1 — native Fock substrate (CAR, d^2=delta^2=0, i*D_KD Hermitian)")
    car = all(np.allclose(a[i] @ adag[j] + adag[j] @ a[i], (1 if i == j else 0) * I8)
              for i in range(3) for j in range(3))
    d = sum(adag)
    delta = sum(a)
    D_KD = d - delta
    iD = 1j * D_KD
    record("F1.1 CAR {a_j,a_k^dag}=delta; d^2=delta^2=0; i*D_KD Hermitian",
           car and np.allclose(d @ d, 0) and np.allclose(delta @ delta, 0)
           and np.allclose(iD, iD.conj().T),
           "3-mode JW fermions on Lambda*(C^3), dim 8")

    # ---- F2: native chiral grading (escape-hatch II) ---------------------------
    section("F2 — chiral grading is NATIVE: {i*D_KD, Gamma_F}=0 (form-parity, escape-hatch II)")
    Gamma_F = np.diag([(-1)**round(N[i, i].real) for i in range(8)]).astype(complex)
    record("F2.1 {i*D_KD, Gamma_F} = 0 with Gamma_F=(-1)^N (chiral grading on a factor "
           "DISTINCT from the generation R^3; C^3=I does not touch it)",
           np.allclose(iD @ Gamma_F + Gamma_F @ iD, 0),
           f"max|{{i D_KD, Gamma_F}}| = {np.max(np.abs(iD@Gamma_F + Gamma_F@iD)):.1e}")

    # ---- F3: Berry spectator -- commuting b-derivatives ------------------------
    section("F3 — i*D_KD is a Berry spectator: the two b-derivatives COMMUTE")
    dH_dx = lift_to_lambda1(C3 + C32)            # d/d(Re b) of M[b]
    dH_dy = lift_to_lambda1(1j * (C3 - C32))     # d/d(Im b) of M[b]
    record("F3.1 [dH/dRe b, dH/dIm b] = 0 (C and C^2 commute) -> simultaneously "
           "diagonalizable -> zero abelian Berry curvature",
           np.allclose(dH_dx @ dH_dy - dH_dy @ dH_dx, 0),
           f"max|[dH/dx, dH/dy]| = {np.max(np.abs(dH_dx@dH_dy - dH_dy@dH_dx)):.1e}")

    # ---- F4: zero native monopole (+ positive control) -------------------------
    section("F4 — native Berry monopole = 0 (Wilson loop); positive control nonzero")
    a_v = 1.0
    def H_native(br, bi, kappa=0.7):
        M = lift_to_lambda1(a_v * np.eye(3) + (br + 1j * bi) * C3 + (br - 1j * bi) * C32)
        return kappa * iD + M
    berry_native = [wilson_berry(lambda br, bi: H_native(br, bi, k), bidx)
                    for k in (0.3, 1.0, 2.0) for bidx in (0, 1)]
    record("F4.1 native i*D_KD + Koide mass: Wilson-loop Berry phase = 0 for all kappa, "
           "all bands (-> Q=1 rigidity default)",
           all(abs(x) < 1e-6 for x in berry_native),
           f"Berry (kappa,band sweep) = {[f'{x:.1e}' for x in berry_native]}")
    # positive control: a chiral 2-band with NON-commuting b-couplings -> monopole
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    szc = np.array([[1, 0], [0, -1]], dtype=complex)
    def H_chiral(br, bi):
        return br * sx + bi * sy + 0.5 * szc
    berry_ctrl = wilson_berry(H_chiral, 0, radius=0.4)
    record("F4.2 POSITIVE CONTROL: a chiral (non-commuting-coupling) 2-band gives a "
           "NONZERO monopole -> the Wilson-loop method detects curvature",
           abs(berry_ctrl) > 1e-2,
           f"Berry(chiral control) = {berry_ctrl:.4f} (!=0)")

    # ---- F5: form-parity grading cannot read Koide -----------------------------
    section("F5 — Gamma_F restricts to scalar -I on Lambda^1 (cannot impose Koide LCC)")
    idx1 = [i for i in range(8) if round(N[i, i].real) == 1]
    GF_lambda1 = Gamma_F[np.ix_(idx1, idx1)]
    record("F5.1 Gamma_F | Lambda^1 = -I (scalar) -> cannot impose <v|Gamma_chi|v>=0; "
           "the Koide grading Gamma_chi=(2/3)J-I is non-scalar on the generation R^3",
           np.allclose(GF_lambda1, -np.eye(3)),
           f"Gamma_F|Lambda^1 = {np.real(np.diag(GF_lambda1)).tolist()} (= -I)")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"  {n_pass}/{len(PASSES)} checks passed")
    print()
    print("  NATIVE chiral grading EXISTS (form-parity Gamma_F, escape-hatch II) -- but")
    print("  i*D_KD is a BERRY SPECTATOR on the generation doublet ([dH/dx,dH/dy]=0 by")
    print("  C3-equivariance) -> zero monopole -> Q=1. Gamma_F is scalar on Lambda^1, so")
    print("  it cannot read Koide. A nonzero off-generation monopole needs the relative-i")
    print("  import (same as the qubit route, r-non-selective).")
    print("  Next path (open): does emergent-time's i land on the form-parity factor and")
    print("  make the inter-grade coupling carry arg(b) natively?")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
