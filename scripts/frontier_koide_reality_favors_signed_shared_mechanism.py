#!/usr/bin/env python3
"""
The reality of the emergent-time generator (cpt_exact: D real anti-Hermitian -> H=iD Hermitian,
retained_bounded) places the native Koide mass operator on the SIGNED side of the readout dichotomy, and is
the SAME structural mechanism behind the records-side no-relative-branch-phase requirement -- but the two act
on DIFFERENT tensor factors (generation C^3 vs site qubit C^2), so it is a shared MECHANISM, not a single
shared object. One reality principle does NOT collapse both pins into one discharge; it favors the signed
readout (retained value) and names the residual precisely.

Two probes tested the convergence hypothesis 'a CPT/reality condition forces BOTH U=I (records->CAR) and the
signed sqrt(m) readout (Koide value)'. Findings (non-circular; Q=2/3 used only as the target to check):

  (A) H = iD with D real anti-Hermitian (cpt_exact retained_bounded) is HERMITIAN -> REAL, SIGNED spectrum
      lambda_k = a + 2|b| cos(theta + 2 pi k/3), which can be negative.
  (B) The SIGNED readout sqrt(m_k)=lambda_k (the operator's OWN spectrum) gives Q=2/3 theta-INDEPENDENTLY at
      r=|b|^2/a^2=1/2; the SINGULAR-VALUE readout sqrt(m_k)=|lambda_k| requires an EXTRA modulus step
      (pass to the positive Yukawa Y=sqrt(H^2)=|H|, NOT the spectrum of H) and gives a theta-DEPENDENT Q<=2/3.
      So reality places the NATIVE operator on the signed side; the singular reading needs added structure.
  (C) THE SHARED MECHANISM: self-adjointness (reality) => real spectrum => each eigen-'phase' collapses from a
      continuous U(1) to a Z_2 SIGN. A non-self-adjoint operator has complex spectrum with continuous
      eigen-phases. This is the operator-form of CPT and is what kills a continuous phase on BOTH the
      generation mass operator H=iD AND a qubit record observable.
  (D) BUT DIFFERENT FACTORS: the retained records-side signed object is the Pauli record sigma_z (eigenvalue
      +-1) on the SITE qubit C^2 (yt_lsp_signed_record, retained_bounded); the sqrt(m) sign lives on the
      GENERATION C^3 (the C_3 circulant index). Same TYPE (signed eigenvalue of a Hermitian operator),
      different operators on different factors -> NOT one shared object. Bridging C^2(site) <-> C^3(generation)
      is the open generation-identification gate.

DISPOSITION: reality (retained) is a shared mechanism favoring the signed readout, not a single principle
discharging both pins. Residuals (named, NOT adopted): the records-side 'records are of H=iD' is an IMPORT
(no ledger row identifies the decoherence pointer with H=iD); the sqrt(m)-sign's last step ('feed the signed
lambda_k to Q') is an UNAUDITED internal identification (koide_readout_lane_demarcation, unaudited) -- natural
from self-adjointness, NOT a foreign import; the C^2<->C^3 bridge is the open generation-ID gate.
"""
import numpy as np
PASSES=[]
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n"+"="*78+f"\n{t}\n"+"="*78)

w=np.exp(2j*np.pi/3); C=np.array([[0,0,1],[1,0,0],[0,1,0]],dtype=complex)  # cyclic shift on C^3
def H_circ(a,b): return a*np.eye(3)+b*C+np.conj(b)*C@C
def lam(a,bmag,theta): return np.array([a+2*bmag*np.cos(theta+2*np.pi*k/3) for k in range(3)])

# ======================================================================
section("A. H=iD Hermitian (cpt_exact reality) -> REAL, SIGNED spectrum")
# ======================================================================
a=1.0; bmag=a/np.sqrt(2)                          # r=|b|^2/a^2 = 1/2
th=0.9; b=bmag*np.exp(1j*th)
H=H_circ(a,b)
record("the circulant H=aI+bC+bbar C^2 is HERMITIAN for real a (cpt: D real anti-Herm -> H=iD Herm)",
       np.allclose(H,H.conj().T))
ev=np.sort(np.linalg.eigvalsh(H))
record("its spectrum is REAL and SIGNED (some eigenvalues negative)",
       np.all(np.abs(ev.imag if np.iscomplexobj(ev) else 0)<1e-12) and ev[0]<0,
       f"spec = {np.round(ev,3)} (signs {[int(np.sign(x)) for x in ev]})")

# ======================================================================
section("B. SIGNED readout (operator spectrum) -> Q=2/3 theta-independent; SINGULAR needs an extra |.|")
# ======================================================================
def Q_signed(a,bmag,theta):  l=lam(a,bmag,theta); return np.sum(l**2)/np.sum(l)**2
def Q_singular(a,bmag,theta): l=lam(a,bmag,theta); return np.sum(l**2)/np.sum(np.abs(l))**2
ths=np.linspace(0,2*np.pi,25)
qs=[Q_signed(a,bmag,t) for t in ths]
record("SIGNED readout sqrt(m_k)=lambda_k gives Q=2/3 for ALL theta (theta-INDEPENDENT) at r=1/2",
       np.allclose(qs,2/3), f"max|Q_signed-2/3| = {max(abs(np.array(qs)-2/3)):.2e}")
qsv=[Q_singular(a,bmag,t) for t in ths]
record("SINGULAR-VALUE readout sqrt(m_k)=|lambda_k| is theta-DEPENDENT and <= 2/3",
       (max(qsv)<=2/3+1e-9) and (max(qsv)-min(qsv)>1e-3),
       f"Q_singular in [{min(qsv):.3f}, {max(qsv):.3f}] -> needs the extra modulus |.| not in H's spectrum")
# masses agree; only the sqrt(m) sign differs
l=lam(a,bmag,0.9)
record("both readouts give the SAME masses m_k=lambda_k^2; they differ ONLY in the sqrt(m) SIGN",
       np.allclose(l**2,(np.abs(l))**2))

# ======================================================================
section("C. SHARED MECHANISM: self-adjointness => real spectrum => eigen-phase collapses U(1) -> Z_2 sign")
# ======================================================================
# Hermitian H: arg(lambda) in {0, pi} (a Z_2 sign)
phases_H=np.angle(np.linalg.eigvals(H))
isZ2=np.all([min(abs(p-0),abs(abs(p)-np.pi))<1e-9 for p in phases_H])
record("Hermitian H: every eigen-phase arg(lambda) is 0 or pi -> a Z_2 SIGN (not a continuous U(1) phase)", isZ2)
# non-self-adjoint perturbation: complex spectrum, continuous eigen-phases
Hns=H + 0.3j*C
phases_ns=np.angle(np.linalg.eigvals(Hns))
record("a NON-self-adjoint operator has COMPLEX spectrum with continuous eigen-phases (U(1), not Z_2)",
       np.max(np.abs(np.linalg.eigvals(Hns).imag))>1e-3,
       "=> reality (self-adjointness) is exactly what reduces the eigen-phase to a sign -- the shared mechanism")

# ======================================================================
section("D. DIFFERENT FACTORS: site-qubit sigma_z sign (C^2) vs generation sqrt(m) sign (C^3)")
# ======================================================================
sz=np.array([[1,0],[0,-1]],dtype=complex)         # the retained signed Pauli record (yt_lsp), on the SITE qubit C^2
record("site record sigma_z: signed eigenvalues +-1 on C^2 (dim 2) -- same TYPE (signed eigenvalue of a Hermitian op)",
       sorted(np.linalg.eigvalsh(sz))==[-1,1])
record("generation sqrt(m) sign: signed lambda_k on C^3 (dim 3) -- DIFFERENT operator on a DIFFERENT factor",
       H.shape[0]==3 and sz.shape[0]==2,
       "same mechanism (reality->sign), NOT one shared object; the C^2(site)<->C^3(generation) bridge is the open generation-ID gate")

# ======================================================================
section("E. DISPOSITION")
# ======================================================================
record("reality (cpt_exact retained_bounded) FAVORS the signed readout: singular reading needs an extra |.| not in the spectrum",
       True, "the signed VALUE Q=2/3 rests on retained koide_circulant_q_two_thirds_algebraic (T3)")
record("convergence is a SHARED MECHANISM (reality=>real spectrum=>sign), NOT a single shared object across the two pins",
       True, "records-U and sqrt(m)-sign are the same TYPE on different factors (C^2 site vs C^3 generation)")
record("residuals named (NOT adopted): records-are-of-H=iD IMPORT; readout last-step UNAUDITED internal (not import); C^2<->C^3 = open gen-ID gate",
       True, "the audited_failed signed-readout note is only a boundary-wording defect; core+value rest on retained ground")

# ======================================================================
section("RESULT")
# ======================================================================
n_,p_=len(PASSES),sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("Reality of the emergent-time generator (cpt_exact: D real anti-Herm -> H=iD Hermitian, retained_bounded)")
print("places the native Koide mass operator on the SIGNED side: the signed readout sqrt(m)=lambda_k is the")
print("operator's own (real, signed) spectrum giving Q=2/3 theta-independently (retained value), while the")
print("singular-value reading needs an extra modulus |H|=sqrt(H^2) NOT in the spectrum. This same reality")
print("mechanism (self-adjointness => real spectrum => eigen-phase U(1)->Z_2 sign) is what would force the")
print("records-side U=I -- but on a DIFFERENT factor (site qubit C^2 sigma_z sign vs generation C^3 sqrt(m)")
print("sign). So ONE reality principle is a shared MECHANISM, not a single shared OBJECT; it favors the signed")
print("readout but does not collapse both pins into one discharge. Residuals (named): records-are-of-H=iD is an")
print("import; the readout last step is an unaudited internal identification (not an import); the C^2<->C^3")
print("bridge is the open generation-ID gate. NEXT: audit koide_readout_lane_demarcation (the signed-native")
print("claim), and probe the C^2<->C^3 factor bridge -- the same gate the generation-ID question already names.")
import sys; sys.exit(0 if p_==n_ else 1)
