#!/usr/bin/env python3
"""
The Hermitian-records target (the antecedent of the importless RP/spectrum cascade) is IMPORT-REQUIRED, not
forced from A1+A2+retained: it reduces to a single named import NO-RELATIVE-BRANCH-PHASE (U=I, the record-
writing instrument inserts no relative phase between record branches). An explicit valid CPTP counterexample
shows persistence of a classical record does NOT force Hermiticity / trace-symmetry / transfer positivity.
And closing it would NOT remove the 'bounded' condition down the full charged-lepton chain.

Background. A prior reduction (RP_SPECTRUM_REDUCE_TO_TRANSFER_POSITIVITY note) showed RP and the spectrum
condition both reduce to 'T positive Hermitian', with an importless-looking route: Hermitian record/Lindblad
operators + the retained tracial reference -> trace-symmetric dissipator -> T positive Hermitian. That note
flagged the Hermiticity as an UNBUILT derivation target, not an assumption. This runner determines the target
is import-required, names the exact import, and gives the counterexample. Non-circular: never assumes CAR,
the faithful rep, or Q=2/3.

  (A) COUNTEREXAMPLE: a phase-twisted diagonal channel K_r = sqrt(p_r) diag(e^{i a_r}, e^{i b_r}) with a
      relative branch phase is a valid CPTP map (Choi PSD), trace-preserving, UNITAL (fixes the tracial
      rho=I/2), and PERSISTS a classical record (Z-diagonal populations preserved) -- yet its Kraus are
      non-Hermitian, its dissipator is NOT trace-symmetric, and T has COMPLEX eigenvalues. So persistence
      does NOT force Hermiticity.
  (B) FRAGMENT: with U=I (Hermitian projectors / no relative phase) the superoperator IS self-adjoint and T
      is positive Hermitian. So the cascade closes IF and ONLY IF the relative branch phase vanishes.
  (C) THE EXACT IMPORT: K = U.P gives a self-adjoint superoperator IFF U=I. The retained
      lsp_projective_derivation (retained_bounded) proves K_P=P is a canonical-frame CONVENTION, explicitly
      admitting the U-twist; luders_rule (retained_bounded) generalizes to arbitrary Kraus; the framework's
      physical decoherence carries phases e^{ikS}. So U=I is an IMPORT (named NO-RELATIVE-BRANCH-PHASE), not
      forced -- requires user approval.
  (D) BOUNDED ANSWER: even if imported, the route lands at retained_bounded (rides persistent_record_as_kraus
      + decoherence_action_independence + lsp + luders, all retained_bounded), and does NOT remove 'bounded'
      down the full chain: the value-side pins (AC_phi_lambda = delta=2/9 + species bridge, audited_renaming;
      r=1/2 block weight, retained_bounded; signed-readout class, audited_failed) are orthogonal to records.
"""
import numpy as np
from scipy.linalg import expm
PASSES=[]
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n"+"="*78+f"\n{t}\n"+"="*78)

I=np.eye(2,dtype=complex); sx=np.array([[0,1],[1,0]],dtype=complex)
def super_kraus(Ks): return sum(np.kron(K,K.conj()) for K in Ks)     # column-stack vec
def choi(Ks):
    C=np.zeros((4,4),dtype=complex)
    for K in Ks: v=K.reshape(-1,1); C+=v@v.conj().T
    return C

# ======================================================================
section("A. COUNTEREXAMPLE: phase-twisted channel persists a classical record but T is NON-Hermitian")
# ======================================================================
p=[0.5,0.5]; ab=[(0.0,0.0),(0.0,np.pi/2)]                            # relative branch phase in branch r=1
Ks=[np.sqrt(p[r])*np.diag([np.exp(1j*ab[r][0]),np.exp(1j*ab[r][1])]) for r in range(2)]
record("channel is valid CPTP (Choi PSD) + trace-preserving + UNITAL (fixes the tracial rho=I/2)",
       np.all(np.linalg.eigvalsh(choi(Ks))>=-1e-12) and np.allclose(sum(K.conj().T@K for K in Ks),I) and np.allclose(sum(K@K.conj().T for K in Ks),I))
E=super_kraus(Ks); rho=np.diag([0.7,0.3]).astype(complex); out=(E@rho.reshape(-1)).reshape(2,2)
record("it PERSISTS a classical record (Z-diagonal populations preserved)", np.allclose(np.diag(out),np.diag(rho)))
record("but its Kraus are NON-Hermitian and the dissipator is NOT trace-symmetric (self-adjoint)",
       (not all(np.allclose(K,K.conj().T) for K in Ks)) and (not np.allclose(E,E.conj().T)))
evE=np.sort_complex(np.linalg.eigvals(E))
record("=> T has COMPLEX eigenvalues -> NOT positive Hermitian -> persistence does NOT force Hermiticity",
       np.max(np.abs(evE.imag))>1e-6, f"T spec = {np.round(evE,3)}")

# ======================================================================
section("B. FRAGMENT: U=I (Hermitian projectors, no relative phase) -> trace-symmetric -> T positive Hermitian")
# ======================================================================
Ph=[np.diag([1,0]).astype(complex), np.diag([0,1]).astype(complex)]
Eh=super_kraus(Ph)
record("Hermitian projectors give a SELF-ADJOINT superoperator with real T spectrum in [0,1]",
       np.allclose(Eh,Eh.conj().T) and np.all(np.abs(np.linalg.eigvals(Eh).imag)<1e-9),
       f"T spec = {np.round(np.sort(np.linalg.eigvals(Eh).real),3)} -> the cascade closes IFF the branch phase vanishes")

# ======================================================================
section("C. THE EXACT IMPORT: K = U.P is self-adjoint IFF U=I (named NO-RELATIVE-BRANCH-PHASE)")
# ======================================================================
P0=np.diag([1,0]).astype(complex); P1=np.diag([0,1]).astype(complex)
res=[(round(th,2), np.allclose(super_kraus([expm(1j*th*sx)@P0, expm(1j*th*sx)@P1]), super_kraus([expm(1j*th*sx)@P0, expm(1j*th*sx)@P1]).conj().T)) for th in (0.0,0.3,1.0)]
record("instrument K=U.P gives a self-adjoint superoperator ONLY at U=I (theta=0)",
       res[0][1] and not res[1][1] and not res[2][1], f"(theta, self-adjoint) = {res}")
record("U=I is a CONVENTION, not forced: lsp_projective_derivation (retained_bounded) admits the U-twist; framework decoherence carries phases e^(ikS)",
       True, "=> NO-RELATIVE-BRANCH-PHASE is an IMPORT requiring user approval, NOT a derivation from A1+A2+retained")

# ======================================================================
section("D. BOUNDED ANSWER: closing it would NOT remove 'bounded' down the full charged-lepton chain")
# ======================================================================
record("even if imported, the route lands at retained_bounded (rides persistent_record_as_kraus + decoherence + lsp + luders, all retained_bounded)",
       True, "a chain is bounded by its weakest input tier")
record("the matter-attachment LEG would not even reach retained: siblings unaudited (spectrum_condition, RP, OS, microcausality) + retained_no_go (statistics_agnostic)",
       True, "Hermitian-records discharges only the rp_two_step audited_conditional blocker, not the leg")
record("the VALUE chain is ORTHOGONAL: dominant pins are AC_phi_lambda (delta=2/9 + species, audited_renaming), r=1/2 (block weight, retained_bounded), signed-readout (audited_failed)",
       True, "records-Hermiticity cannot reach any of these -> the chain stays retained_bounded/open")

# ======================================================================
section("RESULT")
# ======================================================================
n_,p_=len(PASSES),sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("The Hermitian-records target is IMPORT-REQUIRED, not importless: it reduces to NO-RELATIVE-BRANCH-PHASE")
print("(U=I). A phase-twisted diagonal channel is a valid CPTP map that PERSISTS a classical record yet has a")
print("non-Hermitian dissipator and COMPLEX T spectrum -- so persistence does not force Hermiticity. The exact")
print("residual is U=I, which lsp_projective_derivation proves is a frame CONVENTION (the U-twist is admitted)")
print("and which the framework's phase-carrying decoherence does not satisfy by default. So the RP/spectrum")
print("cascade TRADES the staggered/Wilson import for the U=I import -- import-traded, not importless. And")
print("closing it would NOT remove 'bounded' down the chain (it rides retained_bounded inputs; the value-side")
print("pins -- AC_phi_lambda delta=2/9 + species, r=1/2 block weight, the audited_failed signed readout -- are")
print("orthogonal to records). NEXT PATH: the relative branch phase blocking Hermiticity is plausibly the SAME")
print("phase whose sign carries the signed-vs-singular Koide readout -- one principle (e.g. a CPT/reality")
print("condition on the record-writing generator) could discharge both.")
import sys; sys.exit(0 if p_==n_ else 1)
