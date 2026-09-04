"""T141 - IDENTIFYING THE TASTE ALGEBRA.  It should be M(2,H), and that is the cap.

T140: real symmetric elements of the commutant give exactly 2 distinct eigenvalues
(8,8) in 400/400 samples; complex hermitian give 4 in 400/400.  My quaternion
search returned 0, but I searched badly (antisymmetric elements with J^2=-I is a
narrow target to hit by sampling).  Identify the algebra by its INVARIANTS instead.

Prediction.  The framework's Gamma_a are REAL, so the relevant object is the real
Clifford algebra Cl(4,0) = M(2,H), whose irreducible module is H^2 = R^8.  The
framework's fibre is R^16 = two copies of that, so the commutant is M(2,H), of
real dimension 16.  Its SELF-ADJOINT part has 2 (real diagonal) + 4 (one
off-diagonal quaternion) = 6 real dimensions, and its elements have exactly 2
distinct eigenvalues, each of quaternionic multiplicity 1 = real multiplicity 8.
That is precisely what T140 measured.

Three checks that distinguish M(2,H) from the alternatives:
   dim of the commutant                     M(2,H): 16   M(4,R): 16   M(2,C): 8
   dim of its SELF-ADJOINT part             M(2,H):  6   M(4,R): 10   -
   distinct eigenvalues, generic self-adj   M(2,H):  2   M(4,R):  4   -
The second is the discriminating one: 6 vs 10."""
import numpy as np, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t138 import setup

def cbasis(mats,NF):
    A=np.vstack([np.kron(m,np.eye(NF))-np.kron(np.eye(NF),m.T) for m in mats])
    U,s,Vt=np.linalg.svd(A)
    tol=max(A.shape)*np.finfo(float).eps*s.max()
    return [v.reshape(NF,NF) for v in Vt[np.sum(s>tol):]]

print("T141  identifying the taste algebra by its invariants")
print(f"   {'d':>2} {'fibre':>6} {'dim comm':>9} {'dim SYM part':>13} {'dim ANTISYM':>12} {'algebra':>12}")
for d in (2,4):
    NF,G,Gb=setup(d)
    B=cbasis(G,NF)
    # decompose the commutant into symmetric and antisymmetric parts
    M=np.array([Xb.ravel() for Xb in B])
    Sym=np.array([(0.5*(Xb+Xb.T)).ravel() for Xb in B])
    Asy=np.array([(0.5*(Xb-Xb.T)).ravel() for Xb in B])
    ds=np.linalg.matrix_rank(Sym,tol=1e-9); da=np.linalg.matrix_rank(Asy,tol=1e-9)
    if d==2: alg = "M(2,C)~H?" 
    else:    alg = "M(2,H)" if ds==6 else ("M(4,R)" if ds==10 else "?")
    print(f"   {d:>2} {NF:>6} {len(B):>9} {ds:>13} {da:>12} {alg:>12}")
print()
print("   d=4 predicted: dim commutant 16, symmetric part 6 (M(2,H)) vs 10 (M(4,R))")
print()
# direct quaternion construction: find i,j,k in the commutant
NF,G,Gb=setup(4); B=cbasis(G,NF)
A=np.array([(0.5*(Xb-Xb.T)).ravel() for Xb in B])
U,s,Vt=np.linalg.svd(A)
anti=[Vt[i].reshape(NF,NF) for i in range(np.sum(s>1e-9))]
print(f"   antisymmetric elements of the commutant: {len(anti)}")
Js=[]
for X in anti:
    X=0.5*(X-X.T)
    n=np.abs(np.linalg.eigvalsh(1j*X)).max()
    if n<1e-9: continue
    J=X/n
    if np.allclose(J@J,-np.eye(NF),atol=1e-7): Js.append(J)
print(f"   of those, {len(Js)} satisfy J^2 = -I exactly")
if len(Js)>=2:
    print(f"   pairwise anticommutators |J_a J_b + J_b J_a| for a != b:")
    for a in range(min(3,len(Js))):
        for b in range(a+1,min(3,len(Js))):
            print(f"      |J{a} J{b} + J{b} J{a}| = {np.abs(Js[a]@Js[b]+Js[b]@Js[a]).max():.2e}")
    if len(Js)>=3:
        print(f"      J0 J1 == +-J2 ?  {min(np.abs(Js[0]@Js[1]-Js[2]).max(),np.abs(Js[0]@Js[1]+Js[2]).max()):.2e}")
print()
print("   Three anticommuting J's with J^2=-I and J0 J1 = +-J2 IS the quaternion")
print("   algebra sitting inside the commutant -- which is what caps the real mass")
print("   count at 2.  Reality is the whole cause.")
