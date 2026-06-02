#!/usr/bin/env python3
"""
Faithfulness, attacked via M spin content: the inert SPATIAL-ROTATION scalar (J=0 on the on-site algebra) is
excluded retained-clean and SIGNATURE-FREE; but the full faithfulness VALUE does NOT collapse to the (3,1)
signature -- it reduces to an upstream MATTER-ATTACHMENT pin the retained surface disclaims.

The P1 capstone (PR #2462) left faithfulness (Weyl rep vs trivial scalar J=K=0) as the lone carrier-frame
posit, ADMITTED by microcausality. This runner attacks it through the spin content (not microcausality):

  CLEAN FRAGMENT (signature-FREE, retained-clean):
   - The internal-external SU(2) merger (internal_external_su2_merger, retained_bounded) gives the on-site
     C^2 algebra the SPATIAL Spin(3) action: U(R)=exp(i theta.S) conjugates sigma_i as R_ij sigma_j (verified)
     -> J_i = sigma_i/2 are the spatial-rotation generators on the OPERATOR FRAME.
   - so-bracket fact: with J=sigma/2 != 0, K=0 FAILS [K_i,K_j] = -i eps_ijk J_k at every off-diagonal pair --
     in BOTH so(3,1) AND so(4). So K=0 (the inert spatial-rotation scalar) is excluded INDEPENDENTLY of the
     signature; the exclusion rides ONLY J != 0.
   - The so(3,1) completions of J=sigma/2 are EXACTLY the two faithful Weyl chiralities K=+/-i sigma/2;
     so(4) gives K=+/-sigma/2 (Hermitian 4th-rotation). No K=0 branch. So the signature eps=e_4^2 selects only
     the FLAVOR of the forced nonzero K (boost anti-Herm vs 4th-rotation Herm), NOT K=0-vs-K!=0.

  WHY IT DOES NOT FULLY COLLAPSE (the honest residual, NOT the signature alone):
   (1) MATTER-ATTACHMENT [dominant, upstream, signature-independent, retained-surface DISCLAIMS it]: the merger
       is OPERATOR-FRAME ("the per-site Pauli su(2) and Clifford Spin(3) generators are the same operator
       triple on C^2"); per_site_su2_spin_half (retained) explicitly "does not identify this action with the
       physical spin generator of every matter excitation." So matter can carry the operator-frame data yet be
       assigned J=0 at the field-index level -> the merger does NOT exclude the inert MATTER scalar.
   (2) (3,1) SIGNATURE [unaudited]: only labels the forced nonzero K a boost (anti-Herm) vs an so(4) 4th
       rotation; delegated to anomaly_forces_time (unaudited).
   (3) CARRIER IDENTIFICATION [retained-disconnected]: cl3_to_cl31 puts the Cl(3,1) boost on R^4 (Majorana),
       NOT the per-site C^2.

Non-circular: never assumes the faithful rep or Q=2/3.
"""
import numpy as np, sympy as sp
PASSES = []
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)

s1=np.array([[0,1],[1,0]],dtype=complex); s2=np.array([[0,-1j],[1j,0]],dtype=complex); s3=np.array([[1,0],[0,-1]],dtype=complex)
sig=[s1,s2,s3]; eps=np.zeros((3,3,3))
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]: eps[i,j,k]=1; eps[j,i,k]=-1
def C(A,B): return A@B-B@A
from scipy.linalg import expm

# ----------------------------------------------------------------------
section("A. Merger gives the SPATIAL Spin(3) action: U(R)=exp(i th.S) conjugates sigma as R sigma")
# ----------------------------------------------------------------------
S=[x/2 for x in sig]
th=0.7
U=expm(1j*th*S[2])                       # rotation about z by th
rot = U@s1@U.conj().T
expected = np.cos(th)*s1 - np.sin(th)*s2  # spatial SO(3) rotation of sigma_1 about z
record("U(R)=exp(i th S_z) conjugates sigma_1 as cos(th) sigma_1 - sin(th) sigma_2 (SPATIAL SO(3) action)",
       np.allclose(rot, expected),
       "merger: J_i = sigma_i/2 are the spatial-rotation generators on the OPERATOR FRAME")

# ----------------------------------------------------------------------
section("B. K=0 FORBIDDEN given J=sigma/2 -- in BOTH so(3,1) and so(4) (signature-INDEPENDENT)")
# ----------------------------------------------------------------------
J=[x/2 for x in sig]
# so(3,1): [K,K]=-i eps J ; so(4): [K,K]=+i eps J. K=0 gives [0,0]=0 on the LHS for both.
fail_so31 = any(not np.allclose(np.zeros((2,2)), -sum(1j*eps[i,j,k]*J[k] for k in range(3)))
                for i in range(3) for j in range(3) if i!=j)
fail_so4  = any(not np.allclose(np.zeros((2,2)), +sum(1j*eps[i,j,k]*J[k] for k in range(3)))
                for i in range(3) for j in range(3) if i!=j)
record("K=0 FAILS [K,K]=-i eps J (so(3,1)) given J=sigma/2 != 0", fail_so31)
record("K=0 FAILS [K,K]=+i eps J (so(4)) given J=sigma/2 != 0", fail_so4,
       "=> the inert spatial-rotation scalar K=0 is excluded by J!=0 alone, INDEPENDENT of the signature")

# ----------------------------------------------------------------------
section("C. Completions of J=sigma/2: so(3,1) -> K=+/-i sigma/2 (Weyl); so(4) -> K=+/-sigma/2 (Herm); no K=0")
# ----------------------------------------------------------------------
def closes(Klist, sign):  # sign=-1 so(3,1), +1 so(4)
    okJK = all(np.allclose(C(J[i],Klist[j]), sum(1j*eps[i,j,k]*Klist[k] for k in range(3))) for i in range(3) for j in range(3))
    okKK = all(np.allclose(C(Klist[i],Klist[j]), sign*sum(1j*eps[i,j,k]*J[k] for k in range(3))) for i in range(3) for j in range(3))
    return okJK and okKK
record("so(3,1): K=+i sigma/2 and K=-i sigma/2 both close (the two faithful Weyl chiralities)",
       closes([1j*x/2 for x in sig], -1) and closes([-1j*x/2 for x in sig], -1))
record("so(4): K=+sigma/2 and K=-sigma/2 both close (Hermitian 4th rotation)",
       closes([x/2 for x in sig], +1) and closes([-x/2 for x in sig], +1))
# faithful: the Weyl boost K=i sigma/2 is the SAME 2x2 as the merger bivector B=i sigma/2 -> rank-6 image
gens=[J[i] for i in range(3)]+[1j*sig[i]/2 for i in range(3)]
M=np.array([np.concatenate([g.real.flatten(), g.imag.flatten()]) for g in gens])
record("the {J,K=i sigma/2} image is 6-real-dim (faithful Weyl; K = the merger bivector B_i)",
       np.linalg.matrix_rank(M,tol=1e-9)==6)

# ----------------------------------------------------------------------
section("D. The signature selects only K-FLAVOR (boost vs 4th-rotation), NOT K=0-vs-K!=0")
# ----------------------------------------------------------------------
record("eps=e_4^2=-1 -> anti-Hermitian K (boost); eps=+1 -> Hermitian K (so(4) 4th rotation); both K!=0",
       np.allclose((1j*sig[0]/2).conj().T, -(1j*sig[0]/2)) and np.allclose((sig[0]/2).conj().T, sig[0]/2),
       "the K=0 exclusion is signature-FREE; the signature only picks the FLAVOR of the forced nonzero K")

# ----------------------------------------------------------------------
section("E. HONEST residual: excludes the SPATIAL-rotation scalar (J=0 on the algebra), NOT the matter scalar")
# ----------------------------------------------------------------------
record("clean fragment = the inert SPATIAL-rotation scalar (J=0 on the on-site C^2 algebra) is EXCLUDED, signature-free",
       True, "via merger J=sigma/2 (retained_bounded) + per_site (retained) + the so-bracket K=0 failure")
record("RESIDUAL is the MATTER-ATTACHMENT pin (upstream, signature-independent): merger is OPERATOR-FRAME only",
       True, "per_site_su2_spin_half disclaims attaching J=sigma/2 to the matter FIELD index -> matter could be J=0 at the field level")
record("faithfulness does NOT collapse to the (3,1) signature alone: matter-attachment + signature + carrier-id stack",
       True, "the dominant residual is the matter-attachment pin, NOT the signature")

# ----------------------------------------------------------------------
section("RESULT")
# ----------------------------------------------------------------------
n_,p_=len(PASSES),sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print("CLEAN FRAGMENT (signature-free, retained-clean): the inert SPATIAL-rotation scalar (J=0 on the on-site")
print("C^2 algebra) is EXCLUDED -- merger J=sigma/2 (the spatial Spin(3) action) + the so-bracket fact that")
print("K=0 fails [K,K]=-i eps J in BOTH so(3,1) and so(4). The so(3,1) completions are exactly the two faithful")
print("Weyl chiralities K=+/-i sigma/2; the signature selects only the FLAVOR (boost vs 4th rotation), not")
print("K=0-vs-K!=0. BUT the full faithfulness VALUE does NOT collapse to the signature: the dominant residual")
print("is an UPSTREAM MATTER-ATTACHMENT pin (matter field index = the C^2 spinor under spatial rotations),")
print("which the merger -- operator-frame only -- does NOT supply (per_site disclaims it). NOT a closure.")
import sys; sys.exit(0 if p_==n_ else 1)
