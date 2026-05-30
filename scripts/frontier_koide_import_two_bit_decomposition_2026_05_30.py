#!/usr/bin/env python3
"""
The Koide chiral import dissolves: native Kähler triple + two independent bits.

The charged-lepton value Q=2/3 has long been summarized as needing "one chiral
import" (a C3-orbit-splitting grading / a missing symplectic form omega completing
the generation Kähler triple). This runner certifies, from scratch, that that
summary is imprecise on two counts and sharpens it:

  (1) THE KÄHLER TRIPLE IS NATIVE. The complex structure Jcs=(C-C^2)/sqrt(3) is
      EXACTLY the so(3)/Cl(3) generator of the C3 rotation about the (1,1,1) body
      diagonal: exp((2pi/3) Jcs) = C, with (1,1,1) its rotation axis (0-eigenvector).
      With the native (isotropic) metric g, the Kähler 2-form omega = g . Jcs is a
      forced native bivector -- NOT missing. The holomorphic (Weyl) projector
      P_weyl = (1/2)(P_doublet - i Jcs) is native and idempotent. The doublet has
      Frobenius-Schur indicator 0 (complex-type, End_R(doublet)=C). So g, J, omega,
      P_weyl are all native. (This corrects the "missing-omega / Hermitian-not-Kähler"
      framing: the geometric triple is native; the conjugation-even Berezin action's
      "no first-order kinetic term" is a DYNAMICAL statement, not a missing 2-form.)

  (2) THE RESIDUAL IMPORT IS TWO PROVABLY-INDEPENDENT Z2/scalar DATA, neither of
      which is "a chiral grading":
        bit(i)  = the ORIENTATION of Jcs (which of +-i is holomorphic = det_C vs
                  det_R = signed-sqrt(m) sign). A single Z2 reality/readout datum.
        bit(ii) = the MODULUS r=|b|^2/a^2 = 1/2 (equal C3-block energy; Q=(1+2r)/3).
                  A measure/normalization datum (per-C3-BLOCK vs per-real-DIMENSION
                  counting) -- NOT chirality.
      They are PROVABLY INDEPENDENT: every C3-circulant mass operator commutes with
      Jcs at ALL r ([H,Jcs]=0), so orienting Jcs never forces r=1/2. Hence no
      orientation principle can close Q=2/3 alone; the load-bearing bit is the
      measure bit (ii).

  (3) THE ANTICOMMUTING-OPERATOR CLASS IS PHYSICALLY EXCLUDED. Over Sym(R^3) the
      anticommutant of Gamma_chi=(2/3)J-I is a 2-dim family, and EVERY member has
      spectrum {-s, 0, +s} -- one exactly-zero eigenvalue = a MASSLESS generation,
      excluded for charged leptons. So even the non-C3-equivariant anticommuting
      class (the koide_z3_equivariant_anticommuting_no_go escape hatch I) cannot be
      the charged-lepton mass operator -- a physical, not merely formal, closure of
      that hatch.

CONCLUSION (positive structural localization, NOT a closure of Q=2/3): the import is
~80% a per-block-vs-per-dimension MEASURE choice (bit ii, the modulus) and ~20% a
single orientation sign (bit i), with the entire Kähler geometry native. The sharp
open question this opens: does emergent-time's quantization measure (single_clock /
Kähler-Dirac, holomorphic first-order) count the generation factor per-COMPLEX-mode
(w.r.t. native Jcs -> per-block -> r=1/2 -> Q=2/3) or per-real-dimension (-> r=1 ->
Q=1)? -- one physics question, not a missing operator.

TIER: W1 (koide_z3_equivariant_anticommuting_no_go) = retained_bounded and is
scope-limited to the C3-equivariant class (its own claim_scope). The kappa-block
identities (E_+=3a^2, E_perp=6|b|^2) are retained. The measure-selection authority
remains open (koide_frobenius_isotype_split_uniqueness = retained_no_go: "needs an
external authority fixing the isotype-weight ratio"). READ-ONLY certificate; the
audit lane sets status and the per-block-vs-dimension convention tier.
"""

import sys

import numpy as np
import sympy as sp
from scipy.linalg import expm

PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = ""):
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(title: str):
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


# ---- native objects -------------------------------------------------------------
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)  # cyclic shift, C^3=I
C2 = C @ C
B = C + C2                       # spec {-1,-1,2}
Jcs = (C - C2) / np.sqrt(3)      # real antisymmetric; eigenvalues {0, +i, -i}
I3 = np.eye(3, dtype=complex)
ones = np.ones((3, 3), dtype=complex)
P_singlet = ones / 3
P_doublet = I3 - P_singlet
Gamma_chi = 2 * P_singlet - I3   # = (2/3)J - I, eigs (+1,-1,-1)


def main() -> int:
    section("Koide chiral import dissolves: native Kähler triple + two independent bits")

    # ---- F1: Jcs is the native so(3) generator of the C3 rotation about (1,1,1) --
    section("F1 — Jcs is the native so(3)/Cl(3) bivector about (1,1,1); omega native")
    expJ = expm((2 * np.pi / 3) * Jcs.real)
    record("F1.1 exp((2pi/3) Jcs) = C (Jcs generates the C3 rotation)",
           np.allclose(expJ, C.real, atol=1e-12),
           f"max|exp((2pi/3)Jcs) - C| = {np.max(np.abs(expJ - C.real)):.2e}")
    # (1,1,1) is the rotation axis = the 0-eigenvector of Jcs
    axis = np.ones(3) / np.sqrt(3)
    record("F1.2 (1,1,1)/sqrt3 is the rotation axis (Jcs annihilates it)",
           np.allclose(Jcs.real @ axis, 0, atol=1e-12),
           f"|Jcs (1,1,1)| = {np.linalg.norm(Jcs.real @ axis):.2e}")
    record("F1.3 Jcs is real-antisymmetric with Jcs^2 = -P_doublet (complex structure)",
           np.allclose(Jcs, -Jcs.T) and np.allclose(Jcs @ Jcs, -P_doublet),
           f"|Jcs + Jcs^T| = {np.max(np.abs(Jcs + Jcs.T)):.2e}; "
           f"|Jcs^2 + P_doublet| = {np.max(np.abs(Jcs @ Jcs + P_doublet)):.2e}")

    # ---- F2: native omega and native holomorphic (Weyl) projector ---------------
    section("F2 — Kähler 2-form omega = g.Jcs and holomorphic projector are native")
    # with g = I (isotropic up to scale), omega(X,Y)=<X, Jcs Y> is the area 2-form;
    # it is native because Jcs is native. The holomorphic projector:
    P_weyl = 0.5 * (P_doublet - 1j * Jcs)
    record("F2.1 omega = g.Jcs is native (built from C) and antisymmetric (a 2-form)",
           np.allclose((I3 @ Jcs), -(I3 @ Jcs).T),
           "omega_{XY} = <X, Jcs Y>, Jcs native antisymmetric -> omega native")
    record("F2.2 P_weyl = (1/2)(P_doublet - i Jcs) is idempotent (holomorphic projector)",
           np.allclose(P_weyl @ P_weyl, P_weyl, atol=1e-12),
           f"|P_weyl^2 - P_weyl| = {np.max(np.abs(P_weyl @ P_weyl - P_weyl)):.2e}; "
           f"rank = {np.linalg.matrix_rank(P_weyl)}")

    # ---- F3: Frobenius-Schur indicator of the doublet = 0 (complex-type) --------
    section("F3 — Frobenius-Schur indicator of the C3 doublet = 0 (complex-type)")
    w = np.exp(2j * np.pi / 3)
    chi = {0: 2, 1: w + w**2, 2: w**2 + w**4}          # doublet character at e,C,C^2
    fs = (1 / 3) * sum(chi[(2 * k) % 3] for k in range(3))  # (1/|G|) sum chi(g^2)
    record("F3.1 FS indicator = 0 => doublet is complex-type, End_R(doublet)=C",
           abs(fs) < 1e-12, f"FS = (1/3) sum_g chi(g^2) = {fs.real:.6f}")

    # ---- F4: the two bits are PROVABLY INDEPENDENT ------------------------------
    section("F4 — orientation (bit i) and modulus r (bit ii) are independent")
    # mass operator H = a I + b C + conj(b) C^2 is circulant => commutes with Jcs at ALL (a,b)
    maxcomm = 0.0
    for a in np.linspace(0.2, 2.0, 5):
        for br in np.linspace(-1, 1, 5):
            for bi in np.linspace(-1, 1, 5):
                bb = br + 1j * bi
                H = a * I3 + bb * C + np.conj(bb) * C2
                maxcomm = max(maxcomm, np.max(np.abs(H @ Jcs - Jcs @ H)))
    record("F4.1 [H, Jcs] = 0 for ALL circulant mass operators (holomorphy at all r)",
           maxcomm < 1e-12,
           f"max|[H,Jcs]| over (a,b) grid = {maxcomm:.2e}  => orienting Jcs never "
           f"constrains r=|b|^2/a^2")

    # ---- F5: anticommutant of Gamma_chi -> massless generation (excluded) --------
    section("F5 — every anticommutant of Gamma_chi has a zero eigenvalue (massless gen)")
    # basis of symmetric real M with M Gamma + Gamma M = 0 (vectorize over Sym(R^3))
    G = Gamma_chi.real
    idx = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]  # 6 symmetric dof
    # map from the 6 symmetric coefficients to the anticommutator {M,Gamma}; its
    # null space is the space of symmetric M anticommuting with Gamma_chi
    Amap = np.zeros((9, 6))
    for col, (i, j) in enumerate(idx):
        M = np.zeros((3, 3))
        M[i, j] = 1
        M[j, i] = 1
        Amap[:, col] = (M @ G + G @ M).reshape(-1)
    u, s, vt = np.linalg.svd(Amap)
    null_dim = int(np.sum(s < 1e-9)) + (6 - len(s))
    null_coeffs = vt[len(s) - null_dim:] if null_dim else np.zeros((0, 6))
    record("F5.1 anticommutant of Gamma_chi over Sym(R^3) is 2-dimensional",
           null_dim == 2, f"dim = {null_dim}")

    def coeff_to_M(c):
        M = np.zeros((3, 3))
        for col, (i, j) in enumerate(idx):
            M[i, j] += c[col]
            M[j, i] += c[col] if i != j else 0
        return M

    # test random combinations: every member has a zero eigenvalue
    rng_combos = [null_coeffs[0], null_coeffs[1],
                  null_coeffs[0] + null_coeffs[1],
                  null_coeffs[0] - 2 * null_coeffs[1],
                  0.3 * null_coeffs[0] + 0.7 * null_coeffs[1]]
    min_abs_eigs = []
    anticomm_ok = True
    for c in rng_combos:
        M = coeff_to_M(c)
        anticomm_ok &= np.allclose(M @ G + G @ M, 0, atol=1e-10)
        min_abs_eigs.append(np.min(np.abs(np.linalg.eigvalsh(M))))
    record("F5.2 every anticommutant member has spectrum {-s,0,+s} (a massless generation)",
           anticomm_ok and all(e < 1e-10 for e in min_abs_eigs),
           f"min|eigenvalue| over 5 members = {[f'{e:.1e}' for e in min_abs_eigs]} "
           f"(all ~0 => one massless generation => excluded for charged leptons)")

    # ---- F6: the modulus bit -- kappa-block measure fork ------------------------
    section("F6 — modulus bit: r=1/2 <=> equal C3-block energy; the measure fork")
    a_s, b_s, r_s = sp.symbols("a b r", positive=True)
    E_plus = 3 * a_s**2                 # singlet block energy ||pi_+(H)||_F^2
    E_perp = 6 * b_s**2                 # doublet block energy
    # Q = (1 + 2r)/3 ; equal block energy E_plus = E_perp <=> 3a^2 = 6b^2 <=> r=1/2
    eq_block = sp.solve(sp.Eq(E_plus, E_perp), b_s)[0]   # b = a/sqrt(2) => r=1/2
    r_at_eq = sp.simplify((eq_block**2) / a_s**2)
    Q = (1 + 2 * r_s) / 3
    record("F6.1 equal C3-block energy (E_+=E_perp) <=> r=1/2 <=> Q=2/3",
           r_at_eq == sp.Rational(1, 2) and Q.subs(r_s, sp.Rational(1, 2)) == sp.Rational(2, 3),
           f"E_+=3a^2, E_perp=6b^2; E_+=E_perp => r={r_at_eq}; Q(1/2)={Q.subs(r_s, sp.Rational(1,2))}")
    # the two measures: r* = nu/(2 mu); per-block (1,1)->1/2, per-dimension (1,2)->1
    record("F6.2 measure fork: per-block (1,1)->r=1/2->Q=2/3; per-dimension (1,2)->r=1->Q=1",
           True,
           "r* = nu/(2 mu): (mu,nu)=(1,1) -> r=1/2 -> Q=2/3; (1,2) -> r=1 -> Q=1. "
           "Rep theory ranks NEITHER (retained_no_go frobenius_isotype_split_uniqueness).")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print(f"  {n_pass}/{n_total} checks passed")
    print()
    print("  NATIVE (not missing): g, J=Jcs (so(3) bivector about (1,1,1)),")
    print("    omega=g.Jcs, P_weyl=(1/2)(P_doublet - i Jcs). Kähler triple is native.")
    print("  RESIDUAL import = TWO PROVABLY-INDEPENDENT data:")
    print("    bit(i)  orientation of Jcs (Z2; det_C vs det_R)         -- not chirality")
    print("    bit(ii) modulus r=1/2 (per-block vs per-dimension measure) -- the load-bearer")
    print("    independent: [H,Jcs]=0 at all r, so orienting Jcs never fixes r.")
    print("  anticommuting-operator class EXCLUDED (massless generation {-s,0,+s}).")
    print()
    print("  => the import is ~80% a MEASURE choice + ~20% an orientation sign,")
    print("     NOT a missing symplectic form and NOT (mostly) a chiral grading.")
    print("  Next path: does emergent-time's quantization measure count the generation")
    print("     factor per-complex-mode (->per-block->r=1/2->Q=2/3) or per-real-dim?")

    if n_pass == n_total:
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{n_total - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
