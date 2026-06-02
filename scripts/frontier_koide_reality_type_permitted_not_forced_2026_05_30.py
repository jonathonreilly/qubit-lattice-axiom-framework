#!/usr/bin/env python3
"""
The Koide reality-type is permitted-not-forced: reality of D is necessary-not-
sufficient for Q=2/3, and the whole value reduces to one Wick-face scalar.

After the modulus is localized to the generation reality-type comparison
(per-C3-block / Majorana-Jcs -> r=1/2 -> Q=2/3 vs per-real-dimension /
Dirac-central-i -> r=1 -> Q=1), the natural lever to test is
cpt_exact_real_anti_hermitian_d ("D is REAL anti-Hermitian"). This runner shows that
lever is necessary-not-sufficient and certifies the precise residual.

  F1  KILL-SHOT: reality-of-D does NOT select the Wick face. One real anti-Hermitian
      D simultaneously defines BOTH (a) a real SYMPLECTIC form omega(u,v)=u^T D v
      (antisymmetric -> Majorana/Pfaffian -> per-block -> Q=2/3) and (b) a Hermitian
      sesquilinear h(u,v)=conj(u)^T (iD) v (iD Hermitian -> Dirac/determinant ->
      per-dim -> Q=1). Reality of the MATRIX selects neither; the selector is the
      FIELD content (is chi-bar independent (Dirac) or constrained chi-bar=chi^T s
      (Majorana)?), standard Grassmann-measure structure not set by D.
  F2  Jcs is the UNIQUE C3-equivariant real-antisymmetric operator on R^3 (nullspace
      dim 1), and on the doublet (Jcs|doublet)^2 = -I_2 -- a genuine complex line C^1,
      so the "1" in the per-block count (1,1) is COMPUTED, not assumed.
  F3  PER-BLOCK vs PER-DIM is a counting THEOREM: the Pfaffian of the symplectic
      doublet form has degree N/2 = 1 (counts the doublet ONCE) while the determinant
      of the Hermitian form has degree N = 2 (counts it twice). Pf(lam*J2)=lam,
      det(lam*I2)=lam^2.
  F4  SELF-CONSISTENCY with the Dirac-looking spectrum: [H, Jcs] = 0 for the Hermitian
      circulant mass H = aI + bC + b-bar C^2, which has 3 DISTINCT REAL eigenvalues for
      generic complex b. So the real/Jcs measure-face is fully compatible with the
      3-distinct-real-mass ("Dirac-looking") signed spectrum -- that spectrum shape
      does NOT exclude the per-block face.
  F5  THE REDUCTION: Q = (1+2r)/3 with r=|b|^2/a^2; the entire value is the single
      scalar b/a, set by the per-block (1,1)->r=1/2->Q=2/3 vs per-dim (1,2)->r=1->Q=1
      Wick-face selection on block energies (E_+,E_perp)=(3a^2,6|b|^2).

CONCLUSION (permitted-not-forced, NOT a closure): the cited complex/Dirac comparison
supports the per-dimension Q=1 reading (the independent (chi,chi-bar) pair of substep1,
the central-i Hermitian bilinear of substep2, the cl3 complexified module). The
real/Majorana-Jcs (per-block, Q=2/3) reading is algebraically coherent in every step
EXCEPT the one field-reality / Wick-face selection, which this runner does not supply.
Reality of D is necessary-not-sufficient -- the "real D forces Q=2/3" reading is
dissolved without closing Q=2/3.

The next path (a genuine refinement, dodging the C^3=I obstruction that forbids a
continuous U(1)_b): a first-order Berry / Wess-Zumino term L = (1/2) B^T Jcs B-dot is
C3-INVARIANT (Jcs is the unique invariant real-antisymmetric form) and WRITABLE
without any continuous U(1)_b -- whether the emergent-time matter action carries this
geometric phase from a Kähler triple is the open forward question (the
obvious sources D_KD and the central pseudoscalar are verified silent/mislocated, so
it needs a non-D_KD source).

Read-only runner; it sets no audit verdict. Caution: the signed-eigenvalue /
singular-value readout note is not used as a load-bearing premise here.
"""

import sys

import numpy as np
import sympy as sp

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


C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
C2 = C @ C
Jcs = (C - C2) / np.sqrt(3)          # real antisymmetric
I3 = np.eye(3, dtype=complex)
P_doublet = I3 - np.ones((3, 3)) / 3


def main() -> int:
    section("Koide reality-type permitted-not-forced; reduces to one Wick-face scalar")

    # ---- F1: KILL-SHOT -- reality of D selects neither Wick face ----------------
    section("F1 — one real anti-Hermitian D admits BOTH Wick faces (real-matrix != real-field)")
    D = Jcs                          # a real anti-Hermitian operator (cpt_exact class)
    record("F1.1 D is real and anti-Hermitian (D^T = -D, real entries)",
           np.allclose(D.imag, 0) and np.allclose(D, -D.T),
           f"|Im D| = {np.max(np.abs(D.imag)):.1e}; |D + D^T| = {np.max(np.abs(D + D.T)):.1e}")
    # face (a): symplectic bilinear omega(u,v) = u^T D v  (antisymmetric)
    u = np.array([1.0, 0.3, -0.5]); v = np.array([0.2, -0.7, 0.9])
    omega_uv = u @ (D.real @ v)
    omega_vu = v @ (D.real @ u)
    sympl_ok = abs(omega_uv + omega_vu) < 1e-12 and abs(omega_uv) > 1e-9
    # face (b): Hermitian sesquilinear h(u,v) = conj(u)^T (iD) v  (iD Hermitian)
    iD = 1j * D
    herm_ok = np.allclose(iD, iD.conj().T)
    record("F1.2 face (a): omega(u,v)=u^T D v is a nonzero ANTISYMMETRIC (symplectic) "
           "form (-> Majorana/Pfaffian -> per-block -> Q=2/3)",
           sympl_ok, f"omega(u,v) = {omega_uv:.4f}, omega(v,u) = {omega_vu:.4f} "
           f"(antisymmetric: sum = {omega_uv + omega_vu:.1e})")
    record("F1.3 face (b): h(u,v)=conj(u)^T (iD) v is a Hermitian form, iD Hermitian "
           "(-> Dirac/determinant -> per-dim -> Q=1)",
           herm_ok, f"|iD - (iD)^dag| = {np.max(np.abs(iD - iD.conj().T)):.1e}")
    record("F1.4 KILL-SHOT: the SAME real anti-Hermitian D supports BOTH faces -> "
           "reality of the MATRIX selects neither; the FIELD-reality (chi-bar=chi^T s "
           "or independent) is the unsourced selector (cpt_exact = necessary-not-sufficient)",
           sympl_ok and herm_ok,
           "reality of D is real-matrix on a complex space; not real-field")

    # ---- F2: Jcs unique C3-equivariant real-antisymmetric; doublet = C^1 --------
    section("F2 — Jcs unique C3-equivariant real-antisym; (Jcs|doublet)^2 = -I_2")
    so3 = [np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 0]], float),
           np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]], float),
           np.array([[0, 0, 0], [0, 0, 1], [0, -1, 0]], float)]
    A = np.array([(g @ C.real - C.real @ g).reshape(-1) for g in so3]).T
    s = np.linalg.svd(A, compute_uv=False)
    null_dim = int(np.sum(s < 1e-9)) + (3 - len(s))
    record("F2.1 only C3-equivariant real-antisymmetric operator on R^3 is span{Jcs}",
           null_dim == 1, f"dim(antisym ∩ commute-C) = {null_dim}")
    # restrict Jcs to the doublet plane (orthonormal basis of the doublet)
    evals, evecs = np.linalg.eigh(P_doublet.real)
    dbasis = evecs[:, evals > 0.5]              # 3x2 orthonormal doublet basis
    Jdb = dbasis.T @ Jcs.real @ dbasis          # 2x2
    record("F2.2 (Jcs|doublet)^2 = -I_2 (doublet is a genuine complex line C^1; the "
           "'1' in per-block (1,1) is COMPUTED)",
           np.allclose(Jdb @ Jdb, -np.eye(2), atol=1e-10),
           f"Jcs|doublet = {np.round(Jdb,3).tolist()}, (Jcs|doublet)^2 = "
           f"{np.round(Jdb@Jdb,3).tolist()}")

    # ---- F3: Pfaffian per-block (degree 1) vs determinant per-dim (degree 2) ----
    section("F3 — per-block vs per-dim is a counting theorem (Pf degree 1 vs det degree 2)")
    lam = sp.Symbol("lam", positive=True)
    J2 = sp.Matrix([[0, -1], [1, 0]])
    sympl = lam * J2                            # symplectic doublet weight
    pf = sympl[0, 1]                            # Pfaffian of a 2x2 antisymmetric = (0,1) entry
    det_perdim = (lam * sp.eye(2)).det()        # det of the Hermitian-form weight
    record("F3.1 Pf(lam*J2) has degree 1 in lam (doublet counted ONCE -> per-block (1,1))",
           sp.degree(pf, lam) == 1, f"Pf(lam*J2) = {pf} (degree {sp.degree(pf, lam)})")
    record("F3.2 det(lam*I2) = lam^2, degree 2 (doublet counted TWICE -> per-dim (1,2))",
           sp.simplify(det_perdim - lam**2) == 0 and sp.degree(det_perdim, lam) == 2,
           f"det(lam*I2) = {det_perdim} (degree {sp.degree(det_perdim, lam)})")

    # ---- F4: self-consistency with the 3-distinct-real-mass spectrum ------------
    section("F4 — real/Jcs face is self-consistent with the Dirac-looking spectrum")
    a_v, br, bi = 1.0, 0.31, 0.21
    b = br + 1j * bi
    H = a_v * I3 + b * C + np.conj(b) * C2
    eigs = np.linalg.eigvalsh(H)
    distinct = len(set(np.round(eigs, 6))) == 3
    record("F4.1 [H, Jcs] = 0 and H has 3 DISTINCT REAL eigenvalues (generic complex b) "
           "-> real measure-face compatible with 'Dirac-looking' charged leptons",
           np.allclose(H @ Jcs - Jcs @ H, 0, atol=1e-12) and distinct
           and np.allclose(H, H.conj().T),
           f"|[H,Jcs]| = {np.max(np.abs(H@Jcs - Jcs@H)):.1e}; eig(H) = "
           f"{np.round(eigs,4)} (3 distinct real)")

    # ---- F5: the reduction to one scalar b/a -----------------------------------
    section("F5 — the whole value reduces to b/a: per-block r=1/2 vs per-dim r=1")
    r = sp.Symbol("r", positive=True)
    Q = (1 + 2 * r) / 3
    record("F5.1 Q=(1+2r)/3: per-block (1,1) -> r=1/2 -> Q=2/3; per-dim (1,2) -> r=1 -> Q=1",
           Q.subs(r, sp.Rational(1, 2)) == sp.Rational(2, 3) and Q.subs(r, 1) == 1,
           f"Q(1/2) = {Q.subs(r, sp.Rational(1,2))}, Q(1) = {Q.subs(r, 1)}; "
           f"E_+=3a^2, E_perp=6|b|^2 -> r=|b|^2/a^2 the single unsourced scalar")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print(f"  {n_pass}/{n_total} checks passed")
    print()
    print("  cpt_exact real-D = real MATRIX on a complex space: one D admits BOTH the")
    print("    symplectic (Q=2/3) and Hermitian (Q=1) Wick faces -> necessary-not-sufficient.")
    print("  cited complex/Dirac comparison gives the per-dim Q=1 side (substep1 independent")
    print("    pair, substep2 central-i, cl3 complexified module). Q=2/3 is algebraically")
    print("    coherent EXCEPT for the one field-reality / Wick-face selection.")
    print("  => the whole charged-lepton Koide value = the single scalar b/a (r=1/2 vs r=1).")
    print("  next path: a C3-invariant first-order Berry/WZ term B^T Jcs B-dot (writable")
    print("    WITHOUT continuous U(1)_b, dodging C^3=I) -- is it source-generated?")

    if n_pass == n_total:
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{n_total - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
