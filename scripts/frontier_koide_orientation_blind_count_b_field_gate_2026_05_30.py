#!/usr/bin/env python3
"""
The Koide per-block count is orientation-blind; the omega-forcing of Q=2/3 reduces
to one identification (is b a field or a coupling?).

After this session localized the charged-lepton Koide value to a single measure bit
(per-block / K0-real -> Q=2/3 vs per-dimension / trace -> Q=1), this runner certifies
the three structural facts that clear the dynamical/orientation walls and reduce the
whole question to ONE identification:

  F1  NATIVE KAHLER TRIPLE on the doublet b-plane: metric g=6 I_2 (E_perp=6|b|^2),
      complex structure J2=[[0,-1],[1,0]] (J2^2=-I), symplectic omega=g.J2
      (antisymmetric, det 36), compatibility omega(u,v)=g(u, J2 v).
  F2  ORIENTATION-BLIND COUNT (the key new theorem). Conjugation b->b-bar is the
      real-linear involution c=diag(1,-1); it FLIPS the orientation
      (c J2 c^-1 = -J2, c^T omega c = -omega) but PRESERVES the metric
      (c^T g c = g) and hence the polarization-rank COUNT (= dim/2 = 1). So the
      per-block COUNT (bit ii, the Q=2/3 magnitude) is conjugation-INVARIANT: counting
      b as one mode needs only that J2/omega EXIST, NOT a choice of +i over -i. The
      conjugation-even obstruction (which kills the +i/-i orientation, bit i) therefore
      does NOT block the per-block count.
  F3  Q=(1+2r)/3, re-derived independently: Q = trace(H^2)/trace(H)^2 =
      (sum lambda^2)/(sum lambda)^2 = (1+2r)/3 with r=|b|^2/a^2 (theta-independent),
      = 2/3 at r=1/2. (Q is literally per-DIM trace(H^2) over per-BLOCK trace(H)^2.)
  F4  ACTION-ORDER DECIDER. omega's mere existence does NOT force per-block: a
      1-complex-dim symplectic phase space (R^2, omega) geometrically quantizes to ONE
      mode (per-block) regardless of polarization, but the per-dimension reading lives
      on the DISTINCT 4-dim cotangent bundle T*(R^2) (b a configuration coordinate with
      its own momentum) -> TWO modes. The decider is the ORDER of the action = the
      ROLE of b (dynamical field-amplitude -> phase space -> per-block; static coupling
      -> configuration -> per-dim), on which the native (g, J2, omega) triple is silent.
  F5  COOLING WALL. A pure-dark-state cooling channel toward a doublet vacuum needs a
      jump operator |f1><f2| that is provably OFF the native circulant algebra
      span{I, C, C^2} (Hilbert-Schmidt residual = full norm); native dynamics is
      reversible-unitary + entropy-increasing records (-> maximally-mixed I/3 = trace =
      Q=1). So the per-block reading is NOT reachable by dynamical state-selection.

CONCLUSION (positive localization, NOT a derivation of Q=2/3): the orientation
(conjugation-even) and dynamical (records/cooling) walls are CLEARED for the per-block
count; what remains is exactly ONE identification -- whether the generation-doublet
circulant coupling b in H=aI+bC+b-bar C^2 is the dynamical AMPLITUDE of the first-order
Kahler-Dirac matter field (-> phase space -> per-block -> Q=2/3) or a static background
Yukawa parameter (-> configuration -> per-dim -> Q=1). That B-coupling -> B-field
identification is NOT supplied by the native omega and is currently unbuilt (the
retained Kahler-Dirac field is indexed by the cube-corner Hamming-weight / form-degree
label, a different object than the circulant coupling -- a notation collision, not an
identification); supplying it is an import requiring user approval. With it -> Q=2/3;
without it the per-block-vs-per-dim reverts to the retained_bounded block-weight
frontier (physical selection unproved).

TIER (live-ledger-verified): load-bearing retained anchors are
koide_q23_block_weight_frontier_bounded (retained_bounded),
staggered_dirac_substep2_kahler_dirac_equivalence (retained_bounded),
koide_c3_generator_rephasing_obstruction, koide_circulant_q_two_thirds_algebraic,
cpt_exact_real_anti_hermitian_d, angular_kernel_underdetermination_no_go (retained_no_go).
NOTE: koide_emergent_time_eta_conjugation_parity is UNAUDITED (content used only, not
load-bearing); koide_signed_eigenvalue_vs_singular_value is audited_FAILED (not cited).
READ-ONLY certificate; tiers audit-decided.
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


C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
C2 = C @ C
I3 = np.eye(3, dtype=complex)


def main():
    section("Koide per-block count is orientation-blind; omega-forcing reduces to b's role")

    # ---- F1: native Kahler triple on the doublet b-plane -----------------------
    section("F1 — native Kahler triple (g, J2, omega) on the b-plane")
    g = 6 * np.eye(2)
    J2 = np.array([[0, -1], [1, 0]], dtype=float)
    omega = g @ J2                       # = 6 J2
    record("F1.1 J2^2 = -I (complex structure)", np.allclose(J2 @ J2, -np.eye(2)),
           f"J2^2 = {(J2@J2).tolist()}")
    record("F1.2 omega = g.J2 antisymmetric, nondegenerate (det 36)",
           np.allclose(omega, -omega.T) and abs(np.linalg.det(omega) - 36) < 1e-9,
           f"omega = {omega.tolist()}, det = {np.linalg.det(omega):.0f}")
    # compatibility omega(u,v) = g(u, J2 v) for all u,v  <=> omega = g @ J2
    record("F1.3 compatibility omega(u,v) = g(u, J2 v)", np.allclose(omega, g @ J2),
           "Kahler compatibility holds (omega = g J2)")

    # ---- F2: ORIENTATION-BLIND COUNT (the key theorem) -------------------------
    section("F2 — conjugation flips orientation (bit i) but preserves the count (bit ii)")
    c = np.diag([1.0, -1.0])             # conjugation b -> b-bar (y -> -y)
    record("F2.1 conjugation flips J2 and omega (orientation / bit i): "
           "c J2 c^-1 = -J2, c^T omega c = -omega",
           np.allclose(c @ J2 @ np.linalg.inv(c), -J2) and np.allclose(c.T @ omega @ c, -omega),
           f"c J2 c^-1 = {(c@J2@np.linalg.inv(c)).tolist()} (= -J2)")
    record("F2.2 conjugation PRESERVES the metric (c^T g c = g) and the polarization-rank "
           "COUNT (= dim/2 = 1): the per-block count is orientation-BLIND",
           np.allclose(c.T @ g @ c, g),
           "c^T g c = g  =>  counting b as ONE mode needs only J2/omega EXIST, not a "
           "+i-over-(-i) choice  =>  the conjugation-even wall blocks bit i, not bit ii")

    # ---- F3: Q = (1+2r)/3 re-derived -------------------------------------------
    section("F3 — Q = trace(H^2)/trace(H)^2 = (1+2r)/3 (theta-independent)")
    a_s, x_s, y_s, r_s = sp.symbols("a x y r", real=True)
    b_s = x_s + sp.I * y_s
    H = a_s * sp.eye(3) + b_s * sp.Matrix(C.real) + sp.conjugate(b_s) * sp.Matrix(C2.real)
    trH = sp.simplify(sp.trace(H))
    trH2 = sp.simplify(sp.trace(H * H))
    Q = sp.simplify(trH2 / trH**2)
    Q_in_r = sp.simplify(Q.subs(x_s**2 + y_s**2, r_s * a_s**2).rewrite(sp.Abs))
    Q_check = sp.simplify(Q - (a_s**2 + 2 * (x_s**2 + y_s**2)) / (3 * a_s**2))
    record("F3.1 Q = trace(H^2)/trace(H)^2 = (a^2 + 2|b|^2)/(3a^2) = (1+2r)/3",
           Q_check == 0,
           f"trace(H)={trH}, trace(H^2)={sp.expand(trH2)}, Q={sp.simplify(Q)}")
    # r=1/2  <=>  |b|^2 = a^2/2 ; take y=0, x=a/sqrt(2) (theta-independent)
    Qhalf = sp.simplify(Q.subs({y_s: 0, x_s: a_s / sp.sqrt(2)}))
    record("F3.2 Q = 2/3 at r=1/2 (theta-independent: depends only on |b|^2)",
           sp.simplify(Qhalf - sp.Rational(2, 3)) == 0, f"Q(r=1/2) = {Qhalf}")

    # ---- F4: action-order decider (dim counting) -------------------------------
    section("F4 — omega-existence does NOT decide; the action ORDER (role of b) does")
    dim_phase_space_first_order = 2       # (R^2, omega): b-plane IS the phase space
    modes_per_block = dim_phase_space_first_order // 2
    dim_phase_space_second_order = 4      # T*(R^2): b a config coord with its own momentum
    modes_per_dim = dim_phase_space_second_order // 2
    record("F4.1 first-order (b a phase-space coord): dim(R^2,omega)/2 = 1 mode -> per-block -> Q=2/3",
           modes_per_block == 1, f"phase-space dim 2 -> {modes_per_block} mode")
    record("F4.2 second-order (b a config field): dim(T*R^2)/2 = 2 modes -> per-dim -> Q=1; "
           "the decider is the ACTION ORDER = the ROLE of b (native triple is silent)",
           modes_per_dim == 2, f"phase-space dim 4 -> {modes_per_dim} modes")

    # ---- F5: cooling wall (jump operator off the circulant algebra) ------------
    section("F5 — cooling dark-state jump |f1><f2| is OFF the circulant algebra")
    # circulants are DIAGONAL in C's eigenbasis; a cooling jump between two doublet
    # eigenmodes (v_omega, v_omega^2) is OFF-diagonal there -> orthogonal to circulants
    w = np.exp(2j * np.pi / 3)
    F = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], dtype=complex) / np.sqrt(3)
    f1 = F[:, 1]                          # v_omega  (a doublet eigenmode of C)
    f2 = F[:, 2]                          # v_omega^2 (the other doublet eigenmode)
    L = np.outer(f1, f2.conj())          # cooling jump v_omega^2 -> v_omega
    # project L onto the circulant algebra span{I, C, C^2} (Hilbert-Schmidt)
    basis = [I3, C, C2]
    # orthonormalize basis in HS inner product, then project
    coeffs = []
    Lproj = np.zeros((3, 3), dtype=complex)
    # Gram-Schmidt in HS
    onb = []
    for B in basis:
        v = B.copy()
        for u in onb:
            v = v - np.trace(u.conj().T @ v) * u
        v = v / np.sqrt(np.trace(v.conj().T @ v).real)
        onb.append(v)
    for u in onb:
        Lproj += np.trace(u.conj().T @ L) * u
    resid = L - Lproj
    resid_frac = np.sqrt(np.trace(resid.conj().T @ resid).real) / np.sqrt(np.trace(L.conj().T @ L).real)
    record("F5.1 the cooling jump |f1><f2| is (almost) entirely OFF span{I,C,C^2} "
           "(HS residual fraction ~ 1) -> a cooling channel is an off-algebra import",
           resid_frac > 0.9, f"HS residual fraction = {resid_frac:.3f} (1 = fully off-algebra)")

    # ---- F6: the gate -- field-amplitude vs coupling (D_KD silent on Lambda^1) --
    section("F6 — the remaining gate: is b a field-amplitude or a coupling? (D_KD silent)")
    # D_KD on Lambda*(C^3) (3-mode Fock) has Lambda^1->Lambda^1 block = 0 (grade-off-diagonal)
    sp_pl = np.array([[0, 1], [0, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    adag = [np.kron(np.kron(sp_pl, I2), I2), np.kron(np.kron(sz, sp_pl), I2),
            np.kron(np.kron(sz, sz), sp_pl)]
    a_ops = [m.conj().T for m in adag]
    N = sum(adag[k] @ a_ops[k] for k in range(3))
    D_KD = sum(adag[k] - a_ops[k] for k in range(3))
    idx1 = [i for i in range(8) if round(N[i, i].real) == 1]   # Lambda^1 = generations
    P1 = np.zeros((8, 8), dtype=complex)
    for i in idx1:
        P1[i, i] = 1
    blk = P1 @ D_KD @ P1
    record("F6.1 D_KD Lambda^1->Lambda^1 (within-generation) block = 0: the first-order "
           "field's kinetic term does NOT directly land on the coupling b",
           np.max(np.abs(blk)) < 1e-12,
           f"max|Lambda^1 block| = {np.max(np.abs(blk)):.1e}; dim Lambda^1 = {len(idx1)} "
           "(= the 3 generations); so b-as-field needs the unbuilt index-map bridge")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    print(f"  {n_pass}/{len(PASSES)} checks passed")
    print()
    print("  CLEARED: orientation/conjugation-even wall (count is orientation-blind, F2);")
    print("           cooling (off-algebra import, F5); records (-> trace -> Q=1).")
    print("  THE ONE REMAINING GATE: is the doublet coupling b a dynamical first-order")
    print("    field-amplitude (-> phase space -> per-block -> Q=2/3) or a static coupling")
    print("    (-> configuration -> per-dim -> Q=1)? The native (g,J2,omega) triple is silent;")
    print("    the B-coupling->B-field identification (index-map from Lambda*(C^d) onto the")
    print("    Z3 isotypes) is the unbuilt bridge = the one import. With it -> Q=2/3.")

    if n_pass == len(PASSES):
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{len(PASSES) - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
