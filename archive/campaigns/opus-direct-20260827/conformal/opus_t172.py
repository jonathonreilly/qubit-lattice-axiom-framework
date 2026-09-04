"""T172 - IS R105's CRITERION THE RIGHT ONE?  Checking my own strong claim.

R105 concluded that 'propagation necessarily breaks the local Lorentz structure',
on the criterion that the admissibility rule does not preserve det rho.  That
claim deserves scrutiny before it is handed on, because the criterion may be too
strong.

THE PROBLEM WITH IT.  Lorentz invariance of a DYNAMICS means the equations are
covariant -- not that every map preserves the norm of every state.  Ordinary
diffusion does not preserve any state's norm and nobody calls it
Lorentz-violating; a CPTP channel contracts BY CONSTRUCTION, since that is what
'trace-preserving and completely positive' does to the Bloch ball.  So 'the rule
is not a Lorentz transformation' may be a statement about it being a CHANNEL
rather than about Lorentz symmetry at all.

TEST THAT DIRECTLY.  If contraction alone is the cause, then EVERY nontrivial CPTP
qubit channel should fail R105's criterion -- including ones with no connection to
propagation or to the framework.  Take three unrelated channels and check:
   * amplitude damping
   * pure dephasing
   * depolarising
If all of them 'break the Minkowski structure' by R105's test, the test is
measuring contractivity, not a broken symmetry, and R105 overstates."""
import numpy as np
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex)
def det_of(r): return float(np.real(np.linalg.det(r)))
def bloch(r): return np.array([np.trace(r@S[i]).real/2 for i in range(3)])
def rho(v): return 0.5*I2+sum(v[i]*S[i] for i in range(3))
def kraus_apply(Ks,r): return sum(K@r@K.conj().T for K in Ks)
print("T172  is R105 measuring a broken symmetry, or just contractivity?")
print()
g=0.3
AD=[np.array([[1,0],[0,np.sqrt(1-g)]],dtype=complex),
    np.array([[0,np.sqrt(g)],[0,0]],dtype=complex)]
p=0.25
DEPH=[np.sqrt(1-p)*I2, np.sqrt(p)*S[2]]
q=0.4
DEPOL=[np.sqrt(1-3*q/4)*I2]+[np.sqrt(q/4)*S[i] for i in range(3)]
tests=[("amplitude damping (gamma=0.3)",AD),
       ("pure dephasing (p=0.25)",DEPH),
       ("depolarising (q=0.4)",DEPOL)]
v0=np.array([0.2,0.1,0.3])
print(f"   {'channel':>32} {'TP?':>6} {'det in':>10} {'det out':>10} {'preserved?':>12}")
for nm,Ks in tests:
    r=rho(v0); out=kraus_apply(Ks,r)
    tp=abs(np.trace(out).real-1)<1e-12
    print(f"   {nm:>32} {str(tp):>6} {det_of(r):10.6f} {det_of(out):10.6f}"
          f" {str(abs(det_of(out)-det_of(r))<1e-12):>12}")
print()
print("   and the framework's own rule, for comparison:")
print(f"   {'V channel alpha=1/3':>32} {'True':>6} {det_of(rho(v0)):10.6f}"
      f" {det_of(rho(v0/3)):10.6f} {'False':>12}")
print()
print("   CONTROL: the only det-preserving CPTP qubit maps are the UNITARIES")
print("   (rotations); a boost is NOT trace-preserving, so it is not a channel:")
for th in (0.5,1.0):
    B=np.cosh(th/2)*I2+np.sinh(th/2)*S[2]
    r=B@rho(v0)@B.conj().T
    print(f"      boost theta={th}: Tr = {np.trace(r).real:.6f} (channels need 1),"
          f"  det = {det_of(r):.6f} (input {det_of(rho(v0)):.6f})")
print()
print("   If every unrelated channel also fails, R105's criterion detects")
print("   CONTRACTIVITY, which every channel has, not a broken Lorentz symmetry.")
