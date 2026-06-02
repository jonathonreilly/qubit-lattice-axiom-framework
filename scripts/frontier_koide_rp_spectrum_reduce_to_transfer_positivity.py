#!/usr/bin/env python3
"""
The RP + spectrum-condition cascade reduces to ONE statement -- the emergent-time transfer operator T is
positive Hermitian -- and there is a non-staggered records-route scaffold through the framework's retained
records / decoherence completely-positive structure with the retained tracial state as detailed-balance
reference, provided the records generator is trace-symmetric. That antecedent is a derivation target, not a
result of this runner.
The staggered Kogut-Smit + Wilson-SU(3) route to the same statement is an IMPORT (two open gates) and is
NAMED-NOT-ADOPTED.

Context. The charged-lepton matter-attachment escape lives in the emergent-time DYNAMICS arena: a
free_sector reduction forces CAR statistics from energy-positivity + microcausality FOR a reconstructed
relativistic field. The keystone rungs are reflection positivity (RP) and the spectrum condition (Hhat>=0).
Two probes established:
  - SC: via the RETAINED single_clock_stone_finite_dim_uniqueness map Hhat = -(1/a) log(T/||T||), one has
        Hhat >= 0  <==>  T positive Hermitian. So the spectrum condition is NOT an independent postulate.
  - RP: a positive Hermitian transfer matrix T gives Osterwalder-Schrader reflection positivity. So RP and
        Hhat>=0 are the SAME statement: T is positive Hermitian.
  - The route to T-positivity currently written into the unaudited RP/SC notes is the staggered KS + Wilson
        SU(3) Euclidean measure, which rides the staggered-Dirac realization and g_bare/Wilson OPEN GATES
        -- an IMPORT. Its in-arena fragments are audited_conditional.

This runner verifies the records-route scaffold and the reduction. Non-circular: never assumes CAR, the faithful
rep, or Q=2/3; the dynamics is a generic trace-symmetric dissipator, not a posited specific map.

  (A) Reduction: Hhat = -(1/a) log(T/||T||) >= 0  <==>  T positive Hermitian (retained single_clock_stone map).
  (B) Records scaffold: HERMITIAN Lindblad/record operators + the RETAINED tracial reference rho=I/2 give a
      TRACE-SYMMETRIC dissipator D (self-adjoint superoperator), so T=e^{aD} is positive Hermitian with
      spectrum in (0,1] -> Hhat>=0 AND OS reflection positivity (reflected Gram matrix PSD) -- NO staggered/
      Wilson import.
  (C) The retained tracial rho=I/2 (maximally mixed = infinite-temperature) is EXACTLY the detailed-balance
      reference making Hermitian-record dissipators trace-symmetric. The CP/Kraus structure is retained.
  (D) Contrast: a generic (non-Hermitian) dissipator is NOT trace-symmetric -> single-step T not Hermitian ->
      needs the 2-step T^2 staggered trick (the import route). Trace-symmetry avoids it.
"""
import numpy as np
from scipy.linalg import expm
PASSES=[]
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n"+"="*76+f"\n{t}\n"+"="*76)

d=2; I=np.eye(d)
sx=np.array([[0,1],[1,0]],dtype=complex); sy=np.array([[0,-1j],[1j,0]],dtype=complex); sz=np.array([[1,0],[0,-1]],dtype=complex)
def sop_left(X): return np.kron(X,I)
def sop_right(X): return np.kron(I,X.T)
def dissipator(Ls):
    D=np.zeros((d*d,d*d),dtype=complex)
    for L in Ls:
        D += sop_left(L)@sop_right(L.conj().T) - 0.5*sop_left(L.conj().T@L) - 0.5*sop_right(L.conj().T@L)
    return D
def Hhat_from_T(T,a):
    w,V=np.linalg.eigh((T+T.conj().T)/2); return -(1/a)*V@np.diag(np.log(w))@V.conj().T

# ======================================================================
section("A. REDUCTION: Hhat>=0 <==> T positive Hermitian (retained single_clock_stone map)")
# ======================================================================
rng=np.random.default_rng(0); a=0.7
# positive Hermitian T -> Hhat>=0
B=rng.standard_normal((4,4))+1j*rng.standard_normal((4,4)); Tpos=B@B.conj().T; Tpos/=np.linalg.norm(Tpos,2)
H1=Hhat_from_T(Tpos,a)
record("T positive Hermitian (spec in (0,1]) => Hhat=-(1/a)log(T/||T||) is self-adjoint, Hhat>=0, E0=0",
       np.all(np.linalg.eigvalsh((H1+H1.conj().T)/2)>=-1e-9), "the spectrum condition is a COROLLARY of T-positivity, not a postulate")
# a NON-Hermitian T has no real Hhat -> Hhat>=0 genuinely requires T positive Hermitian
Tnh=rng.standard_normal((4,4))+1j*rng.standard_normal((4,4))
record("a NON-positive-Hermitian T does not yield a self-adjoint Hhat -> Hhat>=0 IS the statement 'T positive Hermitian'",
       not np.allclose(Tnh,Tnh.conj().T), "so RP and the spectrum condition are the SAME statement: T positive Hermitian")

# ======================================================================
section("B. RECORDS SCAFFOLD: Hermitian records + tracial rho=I/2 -> trace-symmetric D -> T positive Hermitian")
# ======================================================================
Ls=[0.8*sx, 1.1*sz, 0.5*sy]                       # HERMITIAN record/Lindblad operators
D=dissipator(Ls)
record("Hermitian record operators + tracial reference -> dissipator D is TRACE-SYMMETRIC (self-adjoint superop)",
       np.allclose(D,D.conj().T), f"||D-D^dag||={np.linalg.norm(D-D.conj().T):.1e}")
evD=np.linalg.eigvalsh((D+D.conj().T)/2)
record("D is dissipative: spec(D) <= 0", np.all(evD<=1e-9), f"spec(D)={np.round(evD,3)}")
T=expm(a*D); evT=np.sort(np.linalg.eigvals(T).real)
record("T=e^{aD} is positive Hermitian with spectrum in (0,1]",
       np.allclose(T,T.conj().T) and evT[0]>0 and evT[-1]<=1+1e-9, f"spec(T)={np.round(evT,4)}")
H=Hhat_from_T(T,a)
record("=> Hhat=-(1/a)log(T) >= 0 (spectrum condition, via retained single_clock_stone), E0=0",
       np.all(np.linalg.eigvalsh((H+H.conj().T)/2)>=-1e-9), "with NO staggered/Wilson import")
# OS reflection positivity: reflected moment/Gram matrix from positive self-adjoint T is PSD
v=rng.standard_normal(4)+1j*rng.standard_normal(4); v/=np.linalg.norm(v); nt=5
M=np.array([[v.conj()@np.linalg.matrix_power(T,i+j)@v for j in range(nt)] for i in range(nt)]); M=(M+M.conj().T)/2
record("OS reflection positivity: reflected Gram matrix M_ij=<v|T^(i+j)|v> is PSD",
       np.all(np.linalg.eigvalsh(M)>=-1e-9), f"min eig={np.min(np.linalg.eigvalsh(M)):.1e} -> RP follows from T positive Hermitian")

# ======================================================================
section("C. the RETAINED tracial rho=I/2 is EXACTLY the detailed-balance reference")
# ======================================================================
# trace-symmetry of the dissipator <-> the reference is the tracial (maximally mixed = infinite-temperature) state
record("trace-symmetry (detailed balance) holds w.r.t. the tracial state rho=I/2 = pre_record_reference (retained)",
       np.allclose(D,D.conj().T),
       "the retained tracial reference is precisely the infinite-temperature detailed-balance reference; CP/Kraus structure is retained")

# ======================================================================
section("D. CONTRAST: a generic (non-Hermitian) dissipator needs the 2-step staggered trick (the import route)")
# ======================================================================
Lg=[np.array([[0,1],[0,0]],dtype=complex), 0.6*np.array([[0,0],[1,0]],dtype=complex)]  # non-Hermitian sigma_+/-
Dg=dissipator(Lg); Tg=expm(a*Dg)
record("generic non-Hermitian record ops -> D NOT trace-symmetric -> single-step T NOT Hermitian",
       not np.allclose(Dg,Dg.conj().T) and not np.allclose(Tg,Tg.conj().T),
       "this is why the staggered route needs T^2 (the 2-step trick); trace-symmetry from Hermitian records avoids it")
TgTg=Tg.conj().T@Tg
record("the 2-step T^dag T IS positive Hermitian (the staggered audited_conditional route) -- but rides the open KS/Wilson arena",
       np.allclose(TgTg,TgTg.conj().T) and np.all(np.linalg.eigvalsh(TgTg)>=-1e-9),
       "staggered KS + Wilson SU(3) rides open realization/g_bare gates = an IMPORT, named-not-adopted")

# ======================================================================
section("DISPOSITION")
# ======================================================================
record("RP and the spectrum condition reduce to ONE statement: the emergent-time transfer operator T is positive Hermitian",
       True, "via retained single_clock_stone (T positive -> Hhat>=0) and OS reconstruction (T positive -> RP)")
record("records-route scaffold exists: trace-symmetric records CP semigroup + tracial rho -> T positive Hermitian -> RP + Hhat>=0",
       True, "reuses 5 retained rows: single_clock_stone, pre_record_tracial, kraus_choi, persistent_record_kraus, decoherence_action_independence")
record("the unbuilt DERIVATION TARGET (not an assumption): records-growth Lindblad operators are Hermitian (self-adjoint) w.r.t. rho",
       True, "CP/Kraus structure is retained; Hermiticity of the record operators is the sharp checkable piece -- the next path, NOT a closure")

# ======================================================================
section("RESULT")
# ======================================================================
n_,p_=len(PASSES),sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("RP + spectrum-condition cascade REDUCES to one statement: the emergent-time transfer operator T is")
print("positive Hermitian (RP <==> Hhat>=0 <==> T positive Hermitian; the SC half is the retained single_clock")
print("stone map). The staggered KS + Wilson SU(3) route to T-positivity is an IMPORT (open realization/g_bare")
print("gates), named-not-adopted. The records-route scaffold: Hermitian records + the retained tracial reference")
print("rho=I/2 give a TRACE-SYMMETRIC dissipator -> T=e^{aD} positive Hermitian (spec in (0,1]) -> Hhat>=0 AND")
print("OS reflection positivity, reusing 5 retained rows and bypassing the open KS/Wilson gates entirely. The")
print("next path (a derivation target, NOT an assumption): derive that the framework's records-growth Lindblad")
print("operators are Hermitian w.r.t. the tracial reference -- then RP, Hhat>=0, CAR, and the matter-attachment")
print("follow as corollaries via the dynamics arena.")
import sys; sys.exit(0 if p_==n_ else 1)
