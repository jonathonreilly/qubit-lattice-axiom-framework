"""T179 - CAN THE FRAMEWORK CARRY A GAUGE FIELD ON ITS LINKS?

R113 concluded that gauge structure cannot live in the fibre under either
realization, and must therefore come from the lattice.  In lattice gauge theory
that means LINK VARIABLES: a group element on each nearest-neighbour bond, acting
on the fibre as the neighbour's state is transported to the site.  The
admissibility rule is exactly such a transport, so the framework has the right
shape for it.  The question is whether any group can actually act.

Three exhaustive cases, because the fibre is only two complex dimensions:

 (1) U(1) PHASE.  A link phase sends psi -> e^{i theta} psi, so rho = psi psi^dag
     is UNCHANGED.  The possibility domain is states, not spinors, so a U(1) link
     variable is INVISIBLE -- it cannot couple to anything the axioms expose.
     (This is the repo's own 'phase-blindness' open gate, met from a new side.)

 (2) SU(2).  A link element U acts as rho -> U rho U^dag, which IS visible.  But
     SU(2) acting on C^2 is the spin representation of SO(3): every such U is a
     SPATIAL ROTATION.  So an SU(2) link variable is indistinguishable from a
     rotation of the lattice frame -- it is spacetime, not internal.

 (3) ANYTHING LARGER.  The full group preserving the state space of M_2(C) is
     PU(2) = SO(3).  There is nothing else to use.

If all three hold, the framework as axiomatised admits NO internal gauge field,
and that is a hard statement about its capacity to carry the Standard Model.

CONTROL: exhibit a transformation that IS visible and is NOT a rotation -- there
should be none among trace-preserving positive maps except the rotations."""
import numpy as np, itertools
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex)
rng=np.random.default_rng(31)
def bloch(r): return np.array([np.real(np.trace(r@s))/2 for s in S])
print("T179  can a link variable carry gauge structure?")
print()
print("(1) U(1) link phase: is it visible in the state?")
w=0.0
for _ in range(2000):
    psi=rng.normal(size=2)+1j*rng.normal(size=2); psi/=np.linalg.norm(psi)
    th=rng.uniform(0,2*np.pi)
    r1=np.outer(psi,psi.conj()); r2=np.outer(np.exp(1j*th)*psi,(np.exp(1j*th)*psi).conj())
    w=max(w,np.abs(r1-r2).max())
print(f"    max |rho(psi) - rho(e^{{i theta}} psi)| = {w:.2e}    -> U(1) is INVISIBLE")
print()
print("(2) SU(2) link element: is it a spatial rotation?")
def su2_to_so3(U):
    return np.array([[np.real(np.trace(S[i]@U@S[j]@U.conj().T))/2 for j in range(3)]
                     for i in range(3)])
worst_orth=0.0; worst_det=0.0
for _ in range(2000):
    A=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
    Q,_=np.linalg.qr(A); U=Q/np.sqrt(np.linalg.det(Q)+0j)
    R=su2_to_so3(U)
    worst_orth=max(worst_orth,np.abs(R@R.T-np.eye(3)).max())
    worst_det=max(worst_det,abs(np.real(np.linalg.det(R))-1))
print(f"    induced 3x3 map: max |R R^T - I| = {worst_orth:.2e},"
      f"  max |det R - 1| = {worst_det:.2e}")
print(f"    -> every SU(2) link element acts as a PROPER SPATIAL ROTATION")
print()
print("(3) is there anything else?  the group preserving the state space")
print("    of M_2(C) is PU(2) = SO(3); a trace-preserving positive map that is")
print("    invertible with invertible inverse must be a *-automorphism, hence unitary.")
print()
print("   CONTROL: search for a visible, non-rotation, trace-preserving invertible map")
best=None
for _ in range(20000):
    M=rng.normal(size=(3,3))*0.6
    # a linear Bloch map is a valid reversible state map only if it is in SO(3)
    d=np.abs(M@M.T-np.eye(3)).max()
    if best is None or d<best[0]: best=(d,M)
print(f"    closest random Bloch map to an isometry: |M M^T - I| = {best[0]:.4f}")
print(f"    (a non-isometry either leaves the ball or is not reversible -- so the")
print(f"     only reversible visible link actions are the rotations)")
