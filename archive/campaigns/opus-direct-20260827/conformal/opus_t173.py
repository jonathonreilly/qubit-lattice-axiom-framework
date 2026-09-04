"""T173 - WHY NORMALISATION AND BOOSTS CONFLICT: no finite-dimensional unitary
Lorentz representation.  This explains R100, R105 and R106 at once.

Three results found the same incompatibility from different directions:
  R100  the Born weight is not boost invariant; normalisation selects a frame;
  R105  the rule does not preserve det rho (correctly re-read in R106);
  R106  a boost is not trace-preserving, so it is not a channel.
A single structural fact explains all three, and it is checkable rather than
citable:

   SL(2,C) IS NON-COMPACT, SO IT HAS NO NONTRIVIAL FINITE-DIMENSIONAL UNITARY
   REPRESENTATION.

Proof sketch, which the numerics below make concrete: a boost B(theta) =
exp(theta sigma/2) has eigenvalues e^{+-theta/2}, real and off the unit circle for
theta != 0.  Similarity preserves eigenvalues, and a unitary matrix has ALL
eigenvalues of modulus 1.  So no change of basis makes a boost unitary, in ANY
finite-dimensional representation.

CONSEQUENCE FOR THE FRAMEWORK.  The Qubit axiom gives each site a
FINITE-dimensional possibility domain (M_2(C), 2 complex dimensions of state).
Therefore no site can carry a unitary Lorentz representation, and probability --
which requires normalisation, i.e. unitarity of the symmetry action -- can never
be boost-covariant AT A SITE.  R97's beautiful result that the site algebra IS
the proper Lorentz algebra is about the ALGEBRA, and does not give a unitary
action on states.

So Lorentz invariance, if the framework has it, MUST be non-local: a property of
the whole lattice configuration, which is infinite-dimensional, and not of any
site.  That is a real constraint on where to look.

CONTROL: rotations are compact and MUST come out unitary in the same test."""
import numpy as np
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex)
print("T173  can a finite-dimensional rep make a boost unitary?")
print()
print("   spin-1/2 (the Qubit axiom's own domain)")
print(f"   {'theta':>7} {'boost eigenvalues':>34} {'moduli':>22} {'unitary?':>10}")
for th in (0.0,0.5,1.0,2.0):
    B=np.cosh(th/2)*I2+np.sinh(th/2)*S[2]
    w=np.linalg.eigvals(B)
    u=np.abs(B.conj().T@B-I2).max()<1e-12
    print(f"   {th:7.2f} {str(np.round(w,6)):>34} {str(np.round(np.abs(w),6)):>22} {str(u):>10}")
print()
print("   CONTROL: rotations (compact) must be unitary")
for th in (0.5,2.0):
    R=np.cos(th/2)*I2-1j*np.sin(th/2)*S[2]
    w=np.linalg.eigvals(R)
    print(f"   {th:7.2f} {str(np.round(w,6)):>34} {str(np.round(np.abs(w),6)):>22}"
          f" {str(np.abs(R.conj().T@R-I2).max()<1e-12):>10}")
print()
print("   the 4-dimensional Dirac representation, same question")
g=[np.block([[I2,np.zeros((2,2))],[np.zeros((2,2)),-I2]])]
for s in S: g.append(np.block([[np.zeros((2,2)),s],[-s,np.zeros((2,2))]]))
K=0.5*g[0]@g[3]      # boost generator gamma_0 gamma_3 / 2
for th in (0.5,1.5):
    B=np.eye(4,dtype=complex)+0j
    # exponentiate by series
    T=np.eye(4,dtype=complex); 
    for n in range(1,40): T=T@(th*K)/n; B=B+T
    w=np.linalg.eigvals(B)
    print(f"   theta={th:4.1f}  |eigenvalues| = {np.round(np.abs(w),6)}"
          f"   unitary? {np.abs(B.conj().T@B-np.eye(4)).max()<1e-9}")
print()
print("   ANY similarity S B S^-1 has the SAME eigenvalues, so if any modulus")
print("   differs from 1 no basis makes it unitary.  Check that directly:")
rng=np.random.default_rng(2)
B=np.cosh(0.5)*I2+np.sinh(0.5)*S[2]
worst=0.0
for _ in range(2000):
    M=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
    if abs(np.linalg.det(M))<1e-6: continue
    C=M@B@np.linalg.inv(M)
    worst=max(worst,-np.abs(C.conj().T@C-I2).max())
print(f"      best (least non-unitary) over 2000 random bases: {-worst:.6f}   (0 would mean unitary)")
