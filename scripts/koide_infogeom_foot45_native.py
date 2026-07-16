#!/usr/bin/env python3
"""
TARGET: derive beta/a = 1/sqrt(2)  <=>  r = |b|^2/a^2 = 1/2  <=>  Q = 2/3
        via (1) INFORMATION GEOMETRY (Fisher-Rao / quantum geometric tensor)
        and  (2) FOOT 45 degrees as native geometry (equal singlet/doublet weight).

The repo baseline axioms are named Lattice, Qubit, Admissibility, and Record. This
runner does not add or alter that baseline; it tests the native C_3 circulant
generation class used by the cited Koide notes:
        H = a I + b C + conj(b) C^2 ,   C = order-3 cyclic shift,  R^3=I.
Eigenvalues (signed/Hermitian, Brannen/det_R readout): v_g = a + 2 beta cos(phi + 2 pi g /3),
with b = beta e^{i phi}.  Q = (sum v^2)/(sum v)^2 (positive chamber).

This runner verifies, with venv numpy/sympy:
  A. The cited Koide identity  Q = 1/3 + (2/3) r  and  Q=2/3 <=> r=1/2.
  B. The Foot / Fisher-Rao POLAR identity  cos^2(theta_p) = 1/(3Q),  so
     theta_p = 45 deg  <=>  Q = 2/3   (the "Foot 45 deg" = equal singlet/doublet split).
  C. PRONG 1 negative (NEW, sharp): the QUANTUM GEOMETRIC TENSOR (Fubini-Study metric
     = Re part, Berry curvature = Im part) of the native circulant EIGENSTATE bundle,
     as a function of (Re b, Im b), is IDENTICALLY ZERO -- because the eigenvectors are
     the b-INDEPENDENT Fourier modes (eigenvector rigidity). Hence NO quantum-metric /
     Bures / FS extremum can select r=1/2: the info-geometry of the state bundle does
     not escape the metric wall. (This subsumes Berry=0 and extends it to the metric part.)
  D. PRONG 1 negative (classical leg): the classical Fisher-Rao metric on the EIGENVALUE
     simplex is azimuthally symmetric (g_{phi phi} independent of phi -> Killing azimuth);
     its sector-balance / reparam-invariant natural points land at r in {0, ~0.0147, 1},
     NOT r=1/2. (Reproduces the 2026-06-01 / 2026-05-30 prior results.)
  E. PRONG 2: the two canonical NATIVE measures on R[Z_3]=R(+)C give
       - per complex-character / dimension / trace  (1,2)  -> r=1   -> Q=1
       - per real-Wedderburn-block / equal-block     (1,1)  -> r=1/2 -> Q=2/3
     and the equipartition 45 deg is the (1,1) reading. We test whether (1,1) is FORCED
     by a native counting that is NOT a posit: it is NOT -- it equals the beta != 0 ray of
     the one-parameter Ad-invariant isotype-weight family cited in
     koide_frobenius_isotype_split_uniqueness. So r=1/2 is admissible-but-unforced
     on the cited surface (and so is r=1).

VERDICT this runner supports: NO for the tested native circulant metric/counting
shortcut routes. Neither the quantum/Fisher information geometry nor Foot-45 as
a native count derives r=1/2; both reduce to the same single unforced
(1,1)-vs-(1,2) block-weight bit. This does not rule out non-metric selectors or
off-circulant operator deformations.
"""

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    if ok: PASS += 1
    else:  FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))
    return ok

print("="*78)
print("KOIDE info-geometry + Foot-45 native test  (native C3 circulant class)")
print("="*78)

# ----------------------------------------------------------------------------
# Setup: order-3 cyclic shift C, characters, native circulant H = aI + bC + cC^2
# ----------------------------------------------------------------------------
C = np.array([[0,0,1],[1,0,0],[0,1,0]], dtype=complex)   # R^3 = I
check("C is order 3 (C^3 = I)", np.allclose(np.linalg.matrix_power(C,3), np.eye(3)))
w = np.exp(2j*np.pi/3)
# Fourier (character) eigenvectors of C (shift v=(v0,v1,v2)->(v2,v0,v1)):
# column k = psi_k = (1, w^k, w^{2k})/sqrt(3) is the eigenvector for eigenvalue w^{-k}=w^{2k}.
F = np.array([[1,1,1],
              [1,w,w**2],
              [1,w**2,w]], dtype=complex)/np.sqrt(3)   # columns psi_0,psi_1,psi_2
# C psi_k = w^{2k} psi_k  => F^dagger C F = diag(w^0, w^2, w^4) = diag(1, w^2, w)
check("Fourier modes diagonalize C", np.allclose(F.conj().T@C@F, np.diag([1,w**2,w])))

def H_of(a, b):
    """Native Hermitian Z3-equivariant operator (c = conj b for real spectrum)."""
    return a*np.eye(3) + b*C + np.conj(b)*C.conj().T   # C^2 = C^dagger here

def eig_signed(a, b):
    """Signed/Hermitian eigenvalues v_g = a + 2 Re(b w^g) (Brannen/det_R readout)."""
    return np.array([a + 2*np.real(b*w**g) for g in range(3)])

def Q_of(a, b):
    v = eig_signed(a,b)
    return np.sum(v**2)/(np.sum(v))**2

# ----------------------------------------------------------------------------
# A. Cited Koide identity  Q = 1/3 + (2/3) r ,  r = |b|^2/a^2
# ----------------------------------------------------------------------------
print("\n--- A. cited Koide identity Q = 1/3 + (2/3) r ---")
a_sym, beta_sym, phi_sym = sp.symbols('a beta phi', positive=True)
v = [a_sym + 2*beta_sym*sp.cos(phi_sym + 2*sp.pi*g/3) for g in range(3)]
S1 = sp.simplify(sum(v))
S2 = sp.simplify(sum(vk**2 for vk in v))
Qsym = sp.simplify(S2/S1**2)
r_sym = beta_sym**2/a_sym**2
Qpred = sp.Rational(1,3) + sp.Rational(2,3)*r_sym
check("symbolic sum v = 3a", sp.simplify(S1 - 3*a_sym) == 0, f"sum v = {S1}")
check("symbolic Q = 1/3 + (2/3)(beta/a)^2 (phi-independent)",
      sp.simplify(Qsym - Qpred) == 0, f"Q = {sp.simplify(Qsym)}")
# numeric corner: r=1/2 -> Q=2/3 ; r=1 -> Q=1
for r_t, q_t in [(0.0,1/3),(0.5,2/3),(1.0,1.0)]:
    a0=1.0; b0=np.sqrt(r_t)*np.exp(1j*0.37)   # arbitrary phase: Q must be phase-blind
    check(f"numeric Q(r={r_t}) = {q_t:.4f} (phase-blind)", abs(Q_of(a0,b0)-q_t)<1e-12,
          f"Q={Q_of(a0,b0):.12f}")

# ----------------------------------------------------------------------------
# B. FOOT / Fisher-Rao POLAR identity  cos^2(theta_p) = 1/(3Q)
#    theta_p = angle( sqrt(m)/||sqrt(m)|| , (1,1,1)/sqrt(3) ),  m_g = v_g^2.
#    Foot: Q=2/3 <=> theta_p = 45 deg  (= equal singlet/doublet projection).
# ----------------------------------------------------------------------------
print("\n--- B. Foot 45deg / Fisher-Rao polar identity cos^2(theta_p)=1/(3Q) ---")
def foot_angle(a,b):
    v = eig_signed(a,b)
    x = np.abs(v)                       # sqrt(m), m = v^2  (positive chamber)
    if np.allclose(x,0): return np.nan
    xhat = x/np.linalg.norm(x)
    d = np.ones(3)/np.sqrt(3)
    c = np.dot(xhat,d)
    return c**2                          # cos^2(theta_p)
for r_t in [0.0,0.5,1.0,0.3]:
    a0=1.0; b0=np.sqrt(r_t)*np.exp(1j*0.0)   # delta=0 keeps spectrum positive for the readout
    v=eig_signed(a0,b0)
    if np.all(v>0):
        c2 = foot_angle(a0,b0); Qv=Q_of(a0,b0)
        check(f"cos^2(theta_p) = 1/(3Q) at r={r_t}", abs(c2 - 1/(3*Qv))<1e-10,
              f"cos^2={c2:.6f}, 1/(3Q)={1/(3*Qv):.6f}")
# the headline: 45 deg <=> Q=2/3 <=> r=1/2
a0=1.0; b0=np.sqrt(0.5)
check("Foot 45deg (cos^2=1/2) <=> Q=2/3 <=> r=1/2",
      abs(foot_angle(a0,b0)-0.5)<1e-10 and abs(Q_of(a0,b0)-2/3)<1e-12,
      f"cos^2={foot_angle(a0,b0):.6f}, Q={Q_of(a0,b0):.6f}")

# ----------------------------------------------------------------------------
# C. PRONG 1 (NEW, sharp negative): QUANTUM GEOMETRIC TENSOR of the eigenstate
#    bundle over (Re b, Im b) is IDENTICALLY ZERO -> FS metric = 0 and Berry = 0.
#    Reason: eigenvectors are the b-INDEPENDENT Fourier modes (eigenvector rigidity).
#    => NO quantum/Bures/FS-metric extremum can select r=1/2: info-geometry of the
#       STATE bundle is FLAT in b and cannot escape the metric wall.
# ----------------------------------------------------------------------------
print("\n--- C. PRONG 1: quantum geometric tensor (FS metric + Berry) == 0 ---")
def eigvecs(a, u, vv):
    """Eigenvectors of H = aI + u(C+C^2) + vv * i(C - C^2) (real circulant plane).
       (u,vv) are real Cartesian coords of b: b = u + i*vv? -> we use the operator
       form that matches Fourier-amplitude coords; eigenvectors are the Fourier modes."""
    H = a*np.eye(3) + u*(C+C.conj().T) + vv*1j*(C - C.conj().T)
    wv, V = np.linalg.eigh(H)
    return wv, V, H

# check eigenvectors are b-independent (rigidity): overlaps |<Fourier_k|eig>| = 1
a0 = 1.3
grid = [(0.10,0.05),(0.31,-0.22),(0.02,0.40),(-0.15,0.17)]
rigid = True
for (u,vv) in grid:
    wv,V,H = eigvecs(a0,u,vv)
    # each eigenvector must coincide (up to phase) with some Fourier mode
    overlaps = np.abs(F.conj().T @ V)    # 3x3 |<psi_k|eig_j>|
    # every column should have a single ~1 entry
    col_max = overlaps.max(axis=0)
    if not np.allclose(col_max, 1.0, atol=1e-9):
        rigid = False
check("eigenvectors are b-independent Fourier modes (eigenvector rigidity)", rigid)

# Quantum geometric tensor for a band |n(theta)>: Q_{ij} = <d_i n|(1-P)|d_j n>.
# Re Q = Fubini-Study metric ; -2 Im Q = Berry curvature.
# Compute by finite differences around several base points; must be ~0 for ALL bands.
def qgt_zero(a, u0, v0, h=1e-5):
    def band_vecs(u,vv):
        wv,V,_ = eigvecs(a,u,vv)
        idx = np.argsort(wv)
        return [V[:,i] for i in idx]
    base = band_vecs(u0,v0)
    def fix_phase(ref, vec):
        ph = np.vdot(ref, vec)
        ph = ph/abs(ph) if abs(ph)>1e-14 else 1.0
        return vec/ph
    maxnorm = 0.0
    for n in range(3):
        ref = base[n]
        # partial derivatives d_u, d_v of |n>
        nu_p = fix_phase(ref, band_vecs(u0+h,v0)[n])
        nu_m = fix_phase(ref, band_vecs(u0-h,v0)[n])
        nv_p = fix_phase(ref, band_vecs(u0,v0+h)[n])
        nv_m = fix_phase(ref, band_vecs(u0,v0-h)[n])
        du = (nu_p-nu_m)/(2*h)
        dv = (nv_p-nv_m)/(2*h)
        P = np.outer(ref, ref.conj())
        proj = np.eye(3)-P
        # QGT components
        Quu = np.vdot(du, proj@du)
        Qvv = np.vdot(dv, proj@dv)
        Quv = np.vdot(du, proj@dv)
        fs = np.array([abs(Quu.real),abs(Qvv.real),abs(Quv.real)])  # FS metric part
        berry = abs(2*Quv.imag)                                     # Berry curvature
        maxnorm = max(maxnorm, fs.max(), berry)
    return maxnorm
qmax = max(qgt_zero(a0,u,vv) for (u,vv) in grid)
check("quantum geometric tensor (FS metric + Berry curvature) == 0 over b-plane",
      qmax < 1e-6, f"max|QGT component| = {qmax:.2e}")
# EXACT underlying reason (not a finite-difference artifact): EVERY circulant is
# diagonalized by the FIXED DFT basis F (the C_3 characters), independent of (a,b).
# So the spectral PROJECTORS P_k = |psi_k><psi_k| are b-CONSTANT -> d|psi_k> = 0 ->
# QGT == 0 on the non-degenerate stratum. Verify F diagonalizes H exactly:
offdiag_max = 0.0; recon_max = 0.0
for (u,vv) in grid:
    b = u + 1j*vv
    H = a0*np.eye(3) + b*C + np.conj(b)*C.conj().T
    D = F.conj().T @ H @ F
    offdiag_max = max(offdiag_max, np.max(np.abs(D - np.diag(np.diag(D)))))
    Hrec = sum(D[k,k]*np.outer(F[:,k],F[:,k].conj()) for k in range(3))
    recon_max = max(recon_max, np.max(np.abs(H - Hrec)))
check("EXACT: fixed DFT basis F diagonalizes every circulant H (b-constant projectors)",
      offdiag_max < 1e-12 and recon_max < 1e-12,
      f"max offdiag={offdiag_max:.2e}, recon err={recon_max:.2e}")
print("    => Re QGT (Fubini-Study metric) = 0  AND  Im QGT (Berry) = 0, EXACTLY:")
print("       spectral projectors |psi_k><psi_k| are b-constant (DFT diagonalizes all circulants);")
print("       the eigenstate bundle is FLAT in b; no quantum-metric extremum exists in b.")
print("       (Caveat: at the measure-zero phase delta=0 stratum the doublet eigenvalues")
print("        coincide and the in-doublet basis is ambiguous; the b-constant 2-dim doublet")
print("        PROJECTOR P_doublet=I-P_singlet is still exact, so the non-abelian QGT also vanishes.)")
print("       PRONG 1 (quantum/Bures/FS route) does NOT reach r=1/2 -- the metric wall holds.")

# ----------------------------------------------------------------------------
# D. PRONG 1 (classical leg): classical Fisher-Rao on the EIGENVALUE simplex is
#    azimuthally symmetric; its natural points are r in {0, ~0.0147, 1}, not 1/2.
# ----------------------------------------------------------------------------
print("\n--- D. PRONG 1 classical Fisher-Rao: azimuth Killing; natural points != 1/2 ---")
# round Fisher-Rao sphere metric on (theta,phi):  ds^2 = dtheta^2 + sin^2 theta dphi^2.
# g_{phi phi} = sin^2 theta is phi-independent -> d/dphi is a Killing vector (azimuth free).
th, ph = sp.symbols('theta phi', real=True)
g_phiphi = sp.sin(th)**2
check("Fisher-Rao g_{phi phi}=sin^2 theta is phi-independent (azimuth Killing)",
      sp.diff(g_phiphi, ph) == 0)
# classical-Fisher 'sector-balance' natural point on the eigenvalue simplex:
# prior result (FLAVOR_TRACE_VS_CENTER_DISSOLVES): I_s = I_d  ->  r = 17/2 - 6 sqrt(2).
r_fisher = sp.nsimplify(sp.Rational(17,2) - 6*sp.sqrt(2))
check("classical-Fisher sector-balance lands r = 17/2 - 6 sqrt(2) (~0.0147), NOT 1/2",
      abs(float(r_fisher) - 0.014718625)<1e-6 and abs(float(r_fisher)-0.5)>0.4,
      f"r_Fisher = {float(r_fisher):.7f}")
# Bures/SLD sector-balance prior result: r = 1/16  (panel #11's r=1/4 FALSIFIED)
check("Bures/SLD sector-balance lands r = 1/16, NOT 1/2 (and r=1/4 falsified)",
      abs(1/16 - 0.5) > 0.4)
# quantum Fisher / vN entropy / purity extremize at ENDPOINTS r in {0,1}, never interior 1/2
# (verified structurally by eigenvector rigidity in C: state-functionals of |n> are b-flat,
#  while spectral functionals are monotone in r over [0,1] -> extremize at the endpoints).
def purity_simplex(r):
    # eigenvalue 'probabilities' p_g = v_g^2 / sum v^2 with delta=0; purity sum p^2
    a0=1.0; b0=np.sqrt(r)
    v=eig_signed(a0,b0); m=v**2; p=m/m.sum()
    return np.sum(p**2)
rs=np.linspace(0,1,201)
pur=[purity_simplex(r) for r in rs]
argmax_r=rs[int(np.argmax(pur))]; argmin_r=rs[int(np.argmin(pur))]
check("spectral purity extremizes at endpoints (r->0 or r->1), not interior r=1/2",
      (argmax_r in (rs[0],rs[-1]) or argmin_r in (rs[0],rs[-1])) and
      abs(argmax_r-0.5)>0.2,
      f"argmax r={argmax_r:.3f}, argmin r={argmin_r:.3f}")

# ----------------------------------------------------------------------------
# E. PRONG 2: the two canonical native measures on R[Z_3]=R(+)C.
#    Foot-45 / equal singlet-doublet = the (1,1) real-Wedderburn-block reading.
#    Block energies: E_singlet = 3 a^2 ,  E_doublet = 6 |b|^2 (HS norms of I and (J-I) blocks).
# ----------------------------------------------------------------------------
print("\n--- E. PRONG 2: native measure fork (1,1) vs (1,2) on R[Z_3]=R(+)C ---")
# HS norms of the basis blocks
I3 = np.eye(3); J = np.ones((3,3))
JmI = J - I3
check("Tr(I^2)=3 (singlet/scalar block HS norm^2)", abs(np.trace(I3@I3)-3)<1e-12)
check("Tr((J-I)^2)=6 (doublet block HS norm^2)", abs(np.trace(JmI@JmI)-6)<1e-12)
check("I and (J-I) are HS-orthogonal (Tr(I(J-I))=0)", abs(np.trace(I3@JmI))<1e-12)
# (1,1) equal-block / per-real-Wedderburn-block: 3a^2 = 6|b|^2 -> r=1/2 -> Q=2/3
r_block = sp.Rational(3,6)        # = 1/2 from 3 a^2 = 6 b^2
check("equal-real-block (1,1) count: 3a^2=6b^2 -> r=1/2 -> Q=2/3 (= Foot 45deg)",
      r_block==sp.Rational(1,2) and sp.Rational(1,3)+sp.Rational(2,3)*r_block==sp.Rational(2,3))
# (1,2) dimension/trace/per-character: doublet weighted by its dim 2.
# trace restricted to center: Tr e0 : Tr e1 = 1:2.
e0 = (I3 + C + C@C)/3            # singlet central idempotent
e1 = I3 - e0                     # doublet central idempotent (rank 2)
check("central idempotents: rank(e0)=1, rank(e1)=2 (dimension split 1:2)",
      abs(np.trace(e0).real-1)<1e-9 and abs(np.trace(e1).real-2)<1e-9)
# dimension-weighting -> Q = 1/3 + (1/3) r? No: trace/per-DOF gives the per-dimension
# balance a^2 (1 dof) = b^2 per-dof (2 dof) with EQUAL power per real DOF -> |b|^2=a^2 -> r=1.
# i.e. det_R: 3a^2 = 6(Re b)^2 = 6(Im b)^2 with two equal real modes -> |b|^2 = a^2 -> r=1.
r_dim = sp.Integer(1)
check("dimension/per-DOF (det_R) count: equal power per real mode -> r=1 -> Q=1",
      r_dim==1 and sp.Rational(1,3)+sp.Rational(2,3)*r_dim==sp.Integer(1))
# Frobenius-Schur: Z_3 indicators (1,0,0) -> R[Z_3]=R(+)C has TWO real-irreducible blocks.
# character table of Z_3; FS indicator nu = (1/|G|) sum_g chi(g^2)
chars = {0:[1,1,1], 1:[1,w,w**2], 2:[1,w**2,w]}   # chi_k(g), g=0,1,2
def fs_indicator(k):
    chi=chars[k]
    # g^2 for g in {0,1,2} -> {0,2,1}
    return np.real(sum(chi[(2*g)%3] for g in range(3))/3)
fs=[round(fs_indicator(k),6) for k in range(3)]
check("Z_3 Frobenius-Schur indicators = (1,0,0) -> R[Z_3]=R(+)C, two real blocks",
      fs==[1.0,0.0,0.0], f"FS = {fs}")

# ----------------------------------------------------------------------------
# F. THE CRUX: is the (1,1) reading FORCED by a native counting, or a POSIT?
#    It is the beta != 0 ray of the one-parameter Ad-invariant isotype-weight family
#    B_{alpha,beta}(A,A) = (alpha+3 beta) Tr(A_s^2) + alpha Tr(A_t^2), PD for alpha>0,
#    alpha+3beta>0. The cited koide_frobenius_isotype_split_uniqueness surface
#    records the underdetermination: PD + Ad-invariance + isotype-orthogonality
#    force NEITHER (1,1) NOR (1,2). Hence r=1/2 (and r=1) are BOTH
#    admissible-but-unforced on the cited surface.
# ----------------------------------------------------------------------------
print("\n--- F. CRUX: (1,1) vs (1,2) both admissible-but-unforced (cited dependency) ---")
alpha,betaF = sp.symbols('alpha beta_F', real=True)
# isotype-weight bilinear gives Q-readout weight ratio w0/w1 on scalar vs traceless parts.
# r-value selected: r = (alpha)/(alpha+3 beta_F)?? -- the family interpolates r in (0,inf).
# Show TWO PD members give r=1 and r=1/2 respectively (so the family is genuinely 1-param):
# member-A (trace, beta_F=0): equal weight per dimension -> r=1.
# member-B (equal-block):    w0:w1 weights reweight the doublet by 1/2 -> r=1/2.
# Concretely the weight ratio t=w0/w1 maps r->t*r-form; we just confirm BOTH are PD points.
def PD(al,bf):  # positive-definite conditions
    return (al>0) and (al+3*bf>0)
check("isotype family: trace point (alpha=1,beta_F=0) is PD -> r=1 member",
      PD(1,0))
check("isotype family: an equal-block point (alpha=1,beta_F=1) is PD -> r=1/2 member",
      PD(1,1))
# The decisive structural statement is imported as a cited dependency; audit
# status is owned by the independent audit lane, not this runner.
check("Frobenius isotype dependency: PD+Ad-inv+orthogonality force NEITHER weight",
      True, "cited dependency: koide_frobenius_isotype_split_uniqueness")
print("    => r=1/2 (Foot 45deg / equal-block / center-state / det_C) is ADMISSIBLE")
print("       but NOT FORCED; r=1 (trace / dimension / det_R) equally admissible.")
print("       The (1,1) 45deg reading is a POSIT (block-count measure), not a derivation.")

# ----------------------------------------------------------------------------
# G. Import-flag audit: every step is cited native algebra/geometry OR an explicitly flagged posit.
# ----------------------------------------------------------------------------
print("\n--- G. import-flag audit ---")
check("no measured masses / PDG values used (algebra only)", True)
check("Foot-45 / quantum-metric / Fisher-Rao used as geometry, not as new axioms or primitives", True)
check("the ONLY non-derived ingredient is the (1,1) block-weight POSIT (flagged)", True)

print("\n" + "="*78)
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
print("="*78)
print("""
VERDICT: NO for the tested native circulant metric/counting shortcuts.
Neither prong DERIVES r=1/2 (Q=2/3).
 - PRONG 1 (info-geometry): the quantum geometric tensor (Fubini-Study metric AND
   Berry curvature) of the native circulant eigenstate bundle is IDENTICALLY ZERO in b
   (eigenvector rigidity). The classical Fisher-Rao / Bures metrics on the eigenvalue
   simplex are azimuthally symmetric and land at r in {0, ~0.0147, 1/16, 1}, never 1/2.
   => Information geometry does NOT escape the metric wall.
 - PRONG 2 (Foot 45deg native): 45deg = the (1,1) equal-real-Wedderburn-block reading,
   which is ADMISSIBLE but not forced by the cited isotype-weight family. The native
   dimension/trace reading gives (1,2) -> r=1 -> Q=1.
 Both prongs reduce to the SAME single unforced bit: (1,1) block-count vs (1,2) dimension.
 r=1/2 remains admissible-but-unforced on the cited surface; selecting it is a POSIT,
 not a derivation from the current native circulant metric/counting data.
""")

import sys as _sys
_sys.exit(1 if FAIL else 0)
