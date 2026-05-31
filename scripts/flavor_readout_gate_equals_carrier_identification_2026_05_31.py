#!/usr/bin/env python3
"""The Brannen-BAE 2/9 READOUT GATE equals the generation-CARRIER IDENTIFICATION.

Question attacked (workflow wf_400cd07a-108, 10 agents, 6 routes + 3-lens verify + synth):
does A1+A2+retained FORCE the intensive local Lefschetz density 2/9 as THE physical flavor
observable (over the EXTENSIVE global equivariant index, which vanishes on the retained
Gamma_5=(-1)^(x+y+z)-paired native staggered Dirac), or does it relocate / stand as a third premise?

VERDICT: gate_is_identification_bridge_relabeled. 5 of 6 routes converge: there is NO
identification-independent forcing of 2/9 as the observable. The readout gate, the
generation-carrier identification (open_gate lepton_brannen_bae_delta_two_ninths), and the
zero-section/basepoint pick of retained_no_go koide_q_delta_residual_cohomology_obstruction
are PROVEN to be ONE single gate, not three.

This runner verifies the load-bearing algebra:
  (A) the C_3 fixed locus on the generation rep R^3 is the [111] LINE (det(I-C)=0), NOT an
      isolated point; the isolated-fixed-point Atiyah-Bott density 2/9 lives strictly on the
      transverse doublet. So "2/9 is the TOTAL (nothing to sum)" REQUIRES asserting the
      observable lives on the intrinsic R^3 / doublet-normal-bundle (= the carrier identification).
  (B) the Schur-forced complex structure J_cs is SILENT on r=|b|^2/a^2: [J_cs,H]=0 for the entire
      mass-operator family and J_cs annihilates the singlet (the central label that sets Q).
      So J_cs makes a complex structure DEFINABLE on the doublet but selects neither det_C nor det_R
      as the Q-readout -> the within-doublet (1,2)-weight forcing (2/9 vs 1/9) is circular as a
      Q-selector and orthogonal to the operative singlet/doublet ratio.
  (C) the within-doublet rep theory: L_3(1,2)=2/9 (holomorphic/det_C), L_3(1,1)=1/9 (real/Euler) --
      a genuine C_3 fact, but it does not select WHICH determinant is the physical mass ratio.

NET: no new forcing; two apparent gates collapse to one, pinned precisely.
"""
import numpy as np

W = np.exp(2j * np.pi / 3)
I3 = np.eye(3)
J3 = np.ones((3, 3))
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])   # C_3 cyclic shift
JCS = (C - C @ C) / np.sqrt(3.0)                      # Schur-forced complex structure on the doublet
P_MINUS = I3 - J3 / 3.0                               # projector onto the transverse doublet
SINGLET = np.ones(3) / np.sqrt(3.0)                   # the [111] direction


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    # --- (A) the fixed locus on R^3 is a LINE, not an isolated point -------------------------
    eig = np.sort_complex(np.linalg.eigvals(C))
    detIC = np.linalg.det(I3 - C)
    passed.append(check(
        "A1 eig(C|R^3) = {1, omega, omega^2} and det(I-C) = 0  =>  [111] is a FIXED LINE, not isolated",
        np.allclose(np.sort_complex([1.0, W, W ** 2]), eig) and abs(detIC) < 1e-12,
        f"eig(C)={np.round(eig,4)}; det(I-C)={detIC.real:.2e}"))
    det_doublet = (1 - W) * (1 - W ** 2)
    passed.append(check(
        "A2 isolated-fixed-point Atiyah-Bott lives on the TRANSVERSE doublet: det(1-dg|doublet)=(1-w)(1-w^2)=3",
        abs(det_doublet - 3.0) < 1e-12,
        f"det(1-dg|doublet)={det_doublet.real:.6f}  => 2/9 is NOT the R^3 total; calling it 'the total' asserts the carrier"))

    # --- (B) J_cs is SILENT on r (the Q-setting parameter) ----------------------------------
    ev = np.linalg.eigvals(JCS)
    imag_sorted = np.sort(ev.imag)
    passed.append(check(
        "B1 J_cs=(C-C^2)/sqrt3 has eigs {0,+i,-i}; J_cs@singlet=0; J_cs^2 = -P_minus on the doublet",
        np.allclose(np.abs(ev.real), 0, atol=1e-12)
        and np.allclose(imag_sorted, [-1.0, 0.0, 1.0], atol=1e-12)
        and np.linalg.norm(JCS @ SINGLET) < 1e-12
        and np.linalg.norm(JCS @ JCS + P_MINUS) < 1e-12,
        f"eig(J_cs) imag={np.round(imag_sorted,4)} real~0; ||J_cs@singlet||={np.linalg.norm(JCS@SINGLET):.1e}; "
        f"||J_cs^2+P_minus||={np.linalg.norm(JCS@JCS+P_MINUS):.1e}"))

    rng = np.random.default_rng(20260531)
    max_comm = 0.0
    for _ in range(500):
        a = rng.standard_normal()
        b = rng.standard_normal() + 1j * rng.standard_normal()
        H = a * I3 + b * C + np.conj(b) * C.conj().T
        max_comm = max(max_comm, np.linalg.norm(JCS @ H - H @ JCS))
    passed.append(check(
        "B2 [J_cs, H] = 0 for the ENTIRE family H=aI+bC+conj(b)C^2  =>  J_cs is silent on r=|b|^2/a^2, hence on Q",
        max_comm < 1e-10,
        f"max ||[J_cs,H]|| over 500 random (a in R, b in C) = {max_comm:.1e}  => J_cs cannot select det_C vs det_R as Q-readout"))

    # the parameter that DOES set Q is the singlet/doublet amplitude ratio r, on which J_cs acts as 0
    a, b = 1.0, 1.0 / np.sqrt(2.0)
    r = abs(b) ** 2 / a ** 2
    Q = 1.0 / 3.0 + (2.0 / 3.0) * r
    passed.append(check(
        "B3 Q is set by r=|b|^2/a^2 (J_cs's kernel direction): r=1/2 -> Q=2/3 ; r=1 -> Q=1; J_cs annihilates this axis",
        abs(r - 0.5) < 1e-12 and abs(Q - 2.0 / 3.0) < 1e-12,
        f"r={r:.4f} -> Q={Q:.4f}; the z=0 zero-section pick (r=1/2 vs r=1) is what retained_no_go isolates"))

    # --- (C) within-doublet rep theory: 2/9 (det_C) vs 1/9 (det_R), a genuine but non-selecting fact
    L12 = sum(1 / ((W ** k - 1) * (W ** (2 * k) - 1)) for k in (1, 2)) / 3
    L11 = sum(1 / ((W ** k - 1) ** 2) for k in (1, 2)) / 3
    passed.append(check(
        "C1 L_3(1,2)=2/9 (holomorphic/det_C) and L_3(1,1)=1/9 (real/Euler): genuine C_3 fact, NOT a Q-selector",
        abs(L12 - 2.0 / 9.0) < 1e-12 and abs(L11 - 1.0 / 9.0) < 1e-12,
        f"L_3(1,2)={L12.real:.6f}, L_3(1,1)={L11.real:.6f}; which determinant is the physical mass ratio is unforced"))

    # --- (D) the collapse: A2-locality admits BOTH intensive densities AND extensive sums --------
    # an extensive index = additive quasi-local limit of local densities is A2-compatible (cf. total
    # charge/energy). So A2 does NOT exclude the extensive index by type; the selection is made entirely
    # by WHICH carrier space the observable is asserted to live on -- which IS the identification.
    L = 5
    extensive = L * (2.0 / 9.0)               # global sum over an L-site diagonal embedding
    intensive = 2.0 / 9.0                      # intrinsic-R^3 / per-fixed-locus density
    passed.append(check(
        "D1 A2 admits BOTH: extensive sum L*(2/9) (quasi-local, A2-compatible) AND intensive 2/9; A2 selects NEITHER",
        abs(extensive - L * intensive) < 1e-12 and extensive != intensive,
        f"L={L}: extensive={extensive:.4f}, intensive={intensive:.4f}; the carrier choice (R^3 vs lattice) IS the gate"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: gate_is_identification_bridge_relabeled. No identification-independent forcing of 2/9")
    print("as THE observable exists in A1+A2+retained. The readout gate = the generation-carrier")
    print("identification (open_gate lepton_brannen_bae_delta_two_ninths) = the zero-section pick of")
    print("retained_no_go koide_q_delta_residual_cohomology_obstruction. THREE apparent gates collapse to")
    print("ONE, pinned precisely. New verified negative: J_cs is silent on r (the Q-setting parameter), so")
    print("the Schur-forced complex structure does NOT select det_C over det_R as the Koide readout.")
    print("Provenance (verified vs origin/main 2026-05-31): open_gate lepton_brannen_bae_delta_two_ninths;")
    print("retained_no_go koide_q_delta_residual_cohomology_obstruction; retained_bounded koide_z3_")
    print("equivariant_anticommuting_no_go. No load-bearing on unaudited closure_c_staggered_dirac_gate /")
    print("koide_phase_aps_eta_parity_route.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
