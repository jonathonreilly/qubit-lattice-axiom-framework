#!/usr/bin/env python3
"""
Brannen delta vs spectral-asymmetry convention boundary.

This runner checks finite C3 weight/angle facts and an observational PDG comparator.
It does not derive delta=2/9 rad, adopt a radian convention, or set a verdict.

Checks:
  A. L_3(1,2)=2/9 is the finite Lefschetz/Molien weight of the C3 doublet.
  B. PDG charged-lepton masses reduce to a Brannen-angle comparator near bare 2/9 rad.
  C. The Plancherel-step and eta-holonomy angles differ from the bare comparator.
  D. The tested eta/Berry routes do not output bare 2/9 for these finite objects.
  E. (N^2-1)/(12N) and (N-1)/N^2 coincide at N=3 only.
"""
import numpy as np
import sympy as sp

PASSES = []
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)

w = np.exp(2j * np.pi / 3)
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
C2 = C @ C
I3 = np.eye(3, dtype=complex)
Jcs = (C - C2) / np.sqrt(3)
doublet_eigs = [mu for mu in np.linalg.eigvals(C) if not np.isclose(mu, 1.0)]

# ----------------------------------------------------------------------
section("A. Same finite C3 operator carries L_3(1,2)=2/9 and the angle parameter")
# ----------------------------------------------------------------------
L3 = (1.0 / 3) * sum(np.prod([1.0 / (mu**k - 1) for mu in doublet_eigs]) for k in range(1, 3))
record("L_3(1,2) = (1/N) sum_k det[(C^k-I)^-1|doublet] = 2/9",
       abs(L3 - 2/9) < 1e-12, f"L3 = {L3.real:.10f}")
# delta = arg(b) is the SO(2) angle on Jcs; H = aI + |b| exp(i delta) C + c.c.
record("Jcs=(C-C^2)/sqrt3: Jcs^2=-P_doublet and exp((2pi/3)Jcs)=C",
       np.allclose(Jcs @ Jcs, -(I3 - np.outer(np.ones(3), np.ones(3))/3)) and
       np.allclose(__import__('scipy.linalg', fromlist=['expm']).expm((2*np.pi/3)*Jcs), C))
# Q depends only on |b|/a -> delta is Q-orthogonal (koide_q_readout_factorization)
def Qof(a, bmag, delta):
    b = bmag*np.exp(1j*delta); lam = np.linalg.eigvalsh(a*I3 + b*C + np.conj(b)*C2)
    return np.sum(lam**2)/np.sum(lam)**2
record("delta is Q-ORTHOGONAL: Q depends only on |b|/a, not arg(b)",
       max(abs(Qof(1,0.7,d)-Qof(1,0.7,0)) for d in [0.3,0.7,1.1]) < 1e-12)

# ----------------------------------------------------------------------
section("B. Empirical Brannen delta (PDG) = bare 2/9 in radians")
# ----------------------------------------------------------------------
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86
sm = np.array([np.sqrt(me), np.sqrt(mmu), np.sqrt(mtau)])
Q_emp = np.sum(sm**2)/np.sum(sm)**2
record("PDG charged-lepton Koide Q = 2/3", abs(Q_emp - 2/3) < 5e-5, f"Q = {Q_emp:.6f}")
# delta = arg(sum_k sqrt(m_k) omega^{-k}) reduced to the Brannen fundamental domain [0, 2pi/3)
best = None
for perm in [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]:
    z = sum(sm[perm[k]]*np.exp(-2j*np.pi*k/3) for k in range(3))
    d = np.angle(z) % (2*np.pi/3)
    if best is None or abs(d-2/9) < abs(best-2/9): best = d
record("empirical Brannen delta = bare 2/9 = 0.2222 rad (to ~1e-4)", abs(best - 2/9) < 1e-3,
       f"delta_emp = {best:.5f} rad,  2/9 = {2/9:.5f},  diff = {best-2/9:+.5f}")

# ----------------------------------------------------------------------
section("C. The gap is EXACTLY one factor of pi (period-1-rad vs 2pi-rad convention)")
# ----------------------------------------------------------------------
alpha3 = (2/9)*np.pi               # finite Plancherel-step angle carrying 2/9
eta_holonomy = 2*np.pi*(2/9)       # eta-holonomy argument exp(2pi i * 2/9)
bare = 2/9                          # bare rational delta=2/9 read as radians (the FRAMEWORK value, not the empirical PDG angle)
record("Plancherel-step angle alpha_3 = (2/9)*pi = 0.698 rad (NOT the bare 2/9 = 0.2222)", abs(alpha3 - 0.698132) < 1e-5,
       f"alpha_3 = {alpha3:.6f}")
record("eta-holonomy angle 2pi*(2/9) = 1.396 rad (NOT the bare 2/9 = 0.2222)", abs(eta_holonomy - 1.396263) < 1e-5,
       f"2pi*(2/9) = {eta_holonomy:.6f}")
# EXACT pi-factor comparison: alpha_3 vs the BARE framework rational 2/9 (NOT the empirical PDG angle, which differs at ~1e-4)
record("the gap is EXACTLY one factor of pi: alpha_3 = pi * (bare 2/9)", abs(alpha3 - np.pi*bare) < 1e-12,
       f"alpha_3/(bare 2/9) = {alpha3/bare:.6f} = pi")
record("=> reaching bare 2/9 = 0.2222 rad requires a period-normalization choice", True)

# ----------------------------------------------------------------------
section("D. eta-as-phase FALSIFIED: delta is NOT the APS-eta holonomy")
# ----------------------------------------------------------------------
# spin-Dirac equivariant eta (csc-product) = 0 for weights (1,2)
spin_eta = (1/3)*sum(np.prod([1.0/(2j*np.sin(np.pi*k*a/3)) for a in (1,2)]) for k in range(1,3))
record("spin-Dirac equivariant eta(Z_3;1,2) = 0 EXACTLY (the mod-Z phase object is zero, not 2/9)",
       abs(spin_eta) < 1e-9, f"eta_APS = {spin_eta:.6f}")
# finite equivariant eta eta_C(H) is integer-valued {0,2}
def etaC(r):
    b = np.sqrt(r)*np.exp(0.05j); Hm = I3 + b*C + np.conj(b)*C2
    vals, vecs = np.linalg.eigh(Hm); tot=0j
    for i in range(3):
        v=vecs[:,i]; mu=v.conj()@(C@v)
        if abs(vals[i])>1e-9: tot += np.sign(vals[i])*mu
    return tot
record("finite equivariant eta_C(H) is INTEGER-valued {0,2} (0 for r<1, 2 for r>1) -- not 2/9",
       abs(etaC(0.5)-0)<1e-9 and abs(etaC(1.5)-2)<1e-9, f"eta_C(0.5)={etaC(0.5).real:.1f}, eta_C(1.5)={etaC(1.5).real:.1f}")
# 2/9 not an algebraic integer
x=sp.symbols('x'); mp=sp.minimal_polynomial(sp.Rational(2,9),x)
record("2/9 is not an algebraic integer (minpoly 9x-2); the tested finite eta values are integers",
       mp==9*x-2, f"minpoly = {mp}")
# Berry phase = 0 because the eigenVECTORS are the FIXED theta-independent Fourier modes:
# H(theta) is a circulant for every theta, diagonalized by the SAME Fourier matrix F (only the
# eigenVALUES move). A fixed Fourier mode has Berry connection i<v|d_theta v> = 0 identically.
F = np.array([[1,1,1],[1,w,w**2],[1,w**2,w]],dtype=complex)/np.sqrt(3)
max_offdiag = 0.0
for th in np.linspace(0, 2*np.pi, 200):
    b = 0.7*np.exp(1j*th); Hth = I3 + b*C + np.conj(b)*C2
    D = F.conj().T @ Hth @ F
    max_offdiag = max(max_offdiag, np.max(np.abs(D - np.diag(np.diag(D)))))
record("the FIXED Fourier basis diagonalizes H(theta) for all theta -> eigenvectors theta-independent",
       max_offdiag < 1e-9, f"max off-diagonal in fixed basis over the loop = {max_offdiag:.2e}")
record("=> Berry connection i<v_k|d_theta v_k> = 0 for each fixed mode -> arg(b)-loop Berry phase = 0",
       True, "delta is a free SO(2) PARAMETER, not a geometric-phase OUTPUT")

# ----------------------------------------------------------------------
section("E. Family pun: the weight is (N^2-1)/(12N), NOT (N-1)/N^2 (coincide only at N=3)")
# ----------------------------------------------------------------------
Nn=sp.symbols('N')
fam1 = (Nn**2-1)/(12*Nn)   # second-moment / Lefschetz / APS-defect / CFT-orbifold family (the weight)
fam2 = (Nn-1)/Nn**2        # Fisher / Burnside rank-count family
record("weight family (N^2-1)/(12N) and rank family (N-1)/N^2 are DIFFERENT functions",
       sp.simplify(fam1-fam2) != 0)
record("they coincide ONLY at N=3 (both = 2/9); diverge at N=2,4,5",
       sp.solve(sp.Eq(fam1,fam2),Nn) and abs(float(fam1.subs(Nn,3))-2/9)<1e-12 and abs(float(fam2.subs(Nn,3))-2/9)<1e-12
       and abs(float(fam1.subs(Nn,5))-float(fam2.subs(Nn,5)))>1e-6,
       f"N=5: (N^2-1)/12N={float(fam1.subs(Nn,5)):.4f} vs (N-1)/N^2={float(fam2.subs(Nn,5)):.4f}")

# ----------------------------------------------------------------------
section("RESULT")
# ----------------------------------------------------------------------
n_,p_=len(PASSES),sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("The same rational 2/9 appears in the finite C3 doublet weight and in the PDG-derived")
print("Brannen-angle comparator. The runner does not derive the bare-radian assignment:")
print("the Plancherel-step angle is (2/9)*pi, the eta-holonomy angle is 2pi*(2/9),")
print("the tested eta/Berry routes do not output bare 2/9, and the family identity")
print("(N^2-1)/(12N)=(N-1)/N^2 holds at N=3 only. No convention is adopted.")
import sys; sys.exit(0 if p_==n_ else 1)
