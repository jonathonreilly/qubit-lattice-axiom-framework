#!/usr/bin/env python3
"""
Finite Kahler-Dirac form-degree Berry boundary check.

The runner checks a corrected finite algebra boundary. Form parity on
Lambda*(C^3) anticommutes with i*D_KD, but after embedding the circulant
generation mass from the actual N=0 vacuum, the submitted zero-Berry spectator
claim is not supported: the tested Wilson phases are not all zero. This is an
open-gate repair, not a derivation of Q=2/3 and not a verdict.

  F1  FOCK SUBSTRATE. 3-mode Jordan-Wigner Fock space V=Lambda*(C^3) (dim 8):
      CAR {a_j, a_k^dag}=delta, d^2=delta^2=0, and i*D_KD = i*sum_k(a_k^dag - a_k) is
      Hermitian.
  F2  FORM-PARITY GRADING. {i*D_KD, Gamma_F}=0 with Gamma_F=(-1)^N on the form factor.
  F3  LOCAL COMMUTING-DERIVATIVE DIAGNOSTIC. With the Koide circulant mass M[b]=aI+bC+b-bar C^2
      on Lambda^1, the two b-derivative directions COMMUTE: [dH/dRe b, dH/dIm b] = 0
      (because dH/dRe b = C+C^2 and dH/dIm b = i(C-C^2) commute -- C and C^2 commute).
      This local algebra fact is not a zero-curvature Berry theorem without
      band-isolation, Berry-observable, parameter-domain, and gauge/Wilson-loop data.
  F4  CORRECTED ZERO-BERRY CHECK FAILS. The Wilson-loop Berry phase of
      H(b)=kappa*(i*D_KD)+M[b] on the complex-b plane is not zero for every
      tested kappa/band. A positive control still detects curvature.
  F5  THE FORM-PARITY GRADING CANNOT READ KOIDE. Gamma_F restricts to the SCALAR -I on
      Lambda^1 (N=1), so it cannot impose the Koide condition <v|Gamma_chi|v>=0; the
      grading that reads Koide (Gamma_chi=(2/3)J-I, eigenvalues +1,-1,-1) lives on the
      generation R^3, where {C, Gamma_chi} != 0 -> hits comm(C) ∩ anticomm(Gamma_chi)={0}.

CONCLUSION: the form-parity facts remain useful, but the submitted Berry
spectator theorem does not pass with the corrected Lambda^1 embedding.
"""

import sys
from pathlib import Path

import numpy as np

PASSES: list[tuple[str, bool, str]] = []
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KOIDE_DKD_BERRY_SPECTATOR_NOTE_2026-05-31.md"


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
    vac_idx = [i for i in range(8) if round(N[i, i].real) == 0][0]
    vac = np.zeros(8, dtype=complex)
    vac[vac_idx] = 1
    states = [adag[k] @ vac for k in range(3)]
    if not all(np.linalg.norm(s) > 0.5 for s in states):
        raise RuntimeError("Lambda^1 embedding failed: creation from vacuum produced zero state")
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
    section("Kahler-Dirac form-degree coupling: corrected Berry boundary")

    # ---- F1: Fock substrate -----------------------------------------------------
    section("F1 - Fock substrate and Lambda^1 embedding")
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
    lifted_C = lift_to_lambda1(C3)
    lifted_I = lift_to_lambda1(np.eye(3))
    record("F1.2 corrected Lambda^1 embedding is nonzero and has C^3=I on Lambda^1",
           np.linalg.norm(lifted_C) > 1 and np.allclose(lifted_C @ lifted_C @ lifted_C,
                                                        lifted_I),
           f"||lift(C)||_F = {np.linalg.norm(lifted_C):.3f}; "
           f"||lift(C)^3-lift(I)||_max = {np.max(np.abs(lifted_C@lifted_C@lifted_C-lifted_I)):.1e}")

    # ---- F2: form-parity grading ----------------------------------------------
    section("F2 - form-parity grading anticommutes with i*D_KD")
    Gamma_F = np.diag([(-1)**round(N[i, i].real) for i in range(8)]).astype(complex)
    record("F2.1 {i*D_KD, Gamma_F} = 0 with Gamma_F=(-1)^N on the form factor",
           np.allclose(iD @ Gamma_F + Gamma_F @ iD, 0),
           f"max|{{i D_KD, Gamma_F}}| = {np.max(np.abs(iD@Gamma_F + Gamma_F@iD)):.1e}")

    # ---- F3: commuting b-derivatives ------------------------------------------
    section("F3 - the two circulant b-derivatives commute")
    dH_dx = lift_to_lambda1(C3 + C32)            # d/d(Re b) of M[b]
    dH_dy = lift_to_lambda1(1j * (C3 - C32))     # d/d(Im b) of M[b]
    record("F3.1 [dH/dRe b, dH/dIm b] = 0 (C and C^2 commute): local algebra "
           "diagnostic only, not a standalone Berry theorem",
           np.allclose(dH_dx @ dH_dy - dH_dy @ dH_dx, 0),
           f"max|[dH/dx, dH/dy]| = {np.max(np.abs(dH_dx@dH_dy - dH_dy@dH_dx)):.1e}")

    # ---- F4: corrected Berry check (+ positive control) ------------------------
    section("F4 - corrected zero-Berry spectator check fails; positive control nonzero")
    a_v = 1.0
    def H_test(br, bi, kappa=0.7):
        M = lift_to_lambda1(a_v * np.eye(3) + (br + 1j * bi) * C3 + (br - 1j * bi) * C32)
        return kappa * iD + M
    berry_test = [wilson_berry(lambda br, bi: H_test(br, bi, k), bidx)
                    for k in (0.3, 1.0, 2.0) for bidx in (0, 1)]
    record("F4.1 corrected i*D_KD + circulant mass: Wilson phases are NOT all zero, "
           "so the submitted spectator theorem is not certified",
           any(abs(x) > 1e-3 for x in berry_test),
           f"Berry (kappa,band sweep) = {[f'{x:.1e}' for x in berry_test]}")
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
    section("F5 - Gamma_F restricts to scalar -I on Lambda^1")
    idx1 = [i for i in range(8) if round(N[i, i].real) == 1]
    GF_lambda1 = Gamma_F[np.ix_(idx1, idx1)]
    record("F5.1 Gamma_F | Lambda^1 = -I (scalar) -> cannot impose <v|Gamma_chi|v>=0; "
           "the Koide grading Gamma_chi=(2/3)J-I is non-scalar on the generation R^3",
           np.allclose(GF_lambda1, -np.eye(3)),
           f"Gamma_F|Lambda^1 = {np.real(np.diag(GF_lambda1)).tolist()} (= -I)")

    # ---- F6: downstream source-boundary firewall ------------------------------
    section("F6 - downstream source-boundary firewall")
    note_text = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    note_lower = note_flat.lower()
    record("F6.1 note has downstream source-boundary firewall",
           "Downstream Source-Boundary Firewall" in note_text)
    record("F6.2 F3 is local algebra diagnostic, not a zero-curvature Berry theorem",
           "F3 commuting-derivative fact is only a local algebra diagnostic" in note_flat
           and "not, by itself, a zero-curvature Berry theorem" in note_flat)
    record("F6.3 future Berry theorem requires missing band/observable data",
           "inter-grade coupling" in note_lower
           and "band-isolation regime" in note_lower
           and "berry observable" in note_lower
           and "gauge/wilson-loop convention" in note_lower)
    record("F6.4 packet only blocks stale zero-Berry claim and records nonzero sweep",
           "only blocks reuse of the stale zero-berry spectator claim" in note_lower
           and "not identically zero across the tested `kappa` and band choices" in note_lower)

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"  {n_pass}/{len(PASSES)} checks passed")
    print()
    print("  Form-parity anticommutes with i*D_KD, and Gamma_F is scalar on Lambda^1,")
    print("  but the corrected Lambda^1 embedding does not support the zero-Berry")
    print("  spectator theorem: the tested Wilson phases are not all zero.")
    print("  The form-degree Berry role is therefore an open source question.")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
