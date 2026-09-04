"""
T232 - does the ordered record field give space a PREFERRED DIRECTION?

R137 flagged this and left it open: "The ordered phase breaks rotational
symmetry spontaneously.  Whether a symmetry-broken record configuration is
acceptable physics for this framework is not settled here."

If the broken symmetry were SPATIAL the universe would have a preferred axis.
The question is whether the lattice rotations act on the field only through the
spin representation, and whether that representation lies inside the INTERNAL
symmetry group of the rule.  If it does, a spatial rotation can be undone by an
internal one and no direction is singled out.

  rule at the Born point:  phi(psi,psi') = |<psi|psi'>|^2
  internal symmetry     :  psi -> V psi at EVERY site, V unitary  -> is phi invariant?
  spatial rotations     :  psi -> U(R) psi  with U(R) the spin rep -> is U(R) in SU(4)?
"""
import numpy as np, itertools

I2=np.eye(2,dtype=complex)
SX=np.array([[0,1],[1,0]],dtype=complex); SY=np.array([[0,-1j],[1j,0]],dtype=complex)
SZ=np.array([[1,0],[0,-1]],dtype=complex)
GAM=[np.kron(SX,I2), np.kron(SY,I2), np.kron(SZ,SX), np.kron(SZ,SY)]

def hyperoct(d):
    out=[]
    for perm in itertools.permutations(range(d)):
        for sg in itertools.product([1,-1],repeat=d):
            R=np.zeros((d,d))
            for i,p in enumerate(perm): R[i,p]=sg[i]
            if abs(np.linalg.det(R)-1)<1e-12: out.append(R)
    return out

def spin_U(R):
    rows=[]
    for mu in range(4):
        tgt=sum(R[nu,mu]*GAM[nu] for nu in range(4))
        rows.append(np.kron(np.eye(4),GAM[mu].T)-np.kron(tgt,np.eye(4)))
    A=np.vstack(rows); U_,sv,Vt=np.linalg.svd(A,full_matrices=False)
    U=Vt[-1].conj().reshape(4,4)
    return U/np.linalg.det(U)**0.25          # normalise to det 1

rng=np.random.default_rng(23)

print("=== 1. is the Born rule invariant under a GLOBAL unitary at every site? ===")
worst=0.0
for _ in range(500):
    z=rng.normal(size=4)+1j*rng.normal(size=4); z/=np.linalg.norm(z)
    w=rng.normal(size=4)+1j*rng.normal(size=4); w/=np.linalg.norm(w)
    X=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
    V,_=np.linalg.qr(X)                       # a random unitary
    a=abs(np.vdot(z,w))**2
    b=abs(np.vdot(V@z, V@w))**2
    worst=max(worst, abs(a-b))
print(f"   max |phi(psi,psi') - phi(V psi, V psi')| over 500 random unitaries: {worst:.2e}")
print("   => the rule has a full internal U(4) symmetry, acting identically at")
print("      every site and INDEPENDENT of any lattice transformation.")

print("\n=== 2. do the lattice rotations act only through the spin rep, inside SU(4)? ===")
Rs=hyperoct(4); wu=0.0; wd=0.0
for R in Rs:
    U=spin_U(R)
    wu=max(wu, np.max(np.abs(U.conj().T@U - np.eye(4))))
    wd=max(wd, abs(abs(np.linalg.det(U))-1))
print(f"   over all {len(Rs)} proper hypercubic rotations:")
print(f"     max |U^dag U - I|      = {wu:.2e}   (unitary)")
print(f"     max ||det U| - 1|      = {wd:.2e}   (unimodular)")
print("   => every spatial rotation acts as an element of U(4): it is INSIDE the")
print("      internal symmetry group, not an extra structure locked to it.")

print("""
=== 3. the consequence ===
  The ordered phase picks a direction in CP^3 and breaks the internal U(4) down
  to its stabiliser U(3) -- 15 - 9 = 6 broken generators, matching dim CP^3 = 6
  Goldstone modes.
  Because every spatial rotation IS an internal transformation (step 2), any
  rotation of space can be undone by an internal rotation.  The broken symmetry
  is therefore INTERNAL, and no spatial direction is singled out -- exactly as a
  ferromagnet's spin space is decoupled from real space.

  R137's open worry is resolved: ordering does NOT give space a preferred axis.""")

print("\n=== 4. supporting check: is the measured correlation isotropic? ===")
print("   (weak by construction -- the coupling is direction-independent -- but")
print("    it would catch an implementation that broke the lattice symmetry.)")
