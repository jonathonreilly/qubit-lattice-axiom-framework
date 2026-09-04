"""T171 - DOES THE ADMISSIBILITY RULE PRESERVE THE LOCAL MINKOWSKI STRUCTURE?

R97/R98 are unconditional axiom content: each site's algebra is the proper Lorentz
algebra and its state is a Minkowski 4-vector with invariant det rho = t^2 - |v|^2.
But each site has its OWN copy.  For those local structures to assemble into a
spacetime, the map connecting neighbouring sites must relate them compatibly -- and
the admissibility rule is that map.

So ask the sharp question: does the rule preserve det rho?  A Lorentz
transformation does, by definition.  A CPTP channel generally does not, because
channels contract.

For the V channel with all six neighbours in the same state, v_out = alpha v and
t_out = 1/2, so
     det_out = 1/4 - alpha^2 |v|^2   vs   det_in = 1/4 - |v|^2
which agree only when alpha^2 = 1.  Inside the CP range [-1/3, 1] that means
alpha = 1 exactly -- and R99 showed alpha = 1 forces delta_max = 0.

If that holds, the conclusion is sharp: PRESERVING THE LOCAL LORENTZ STRUCTURE
FORCES ZERO PROPAGATION, so any framework dynamics necessarily breaks the very
structure R97/R98 established.  Measure it, and measure how badly it is broken at
the R99 optimum.

CONTROL: a genuine Lorentz transformation applied to the same state must preserve
det exactly, or the diagnostic is not measuring what it claims."""
import numpy as np
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex)
def rho(t,v): return t*I2+sum(v[i]*S[i] for i in range(3))
def det(t,v): return t*t-v@v
print("T171  does the rule preserve the Minkowski invariant?")
print()
print("   CONTROL: a real Lorentz boost on the same state")
v0=np.array([0.0,0.0,0.35]); t0=0.5
for th in (0.0,0.5,1.0):
    B=np.cosh(th/2)*I2+np.sinh(th/2)*S[2]
    r=B@rho(t0,v0)@B.conj().T
    t=np.trace(r).real/2; v=np.array([np.trace(r@S[i]).real/2 for i in range(3)])
    print(f"      theta={th:4.1f}   det = {det(t,v):.10f}   (input {det(t0,v0):.10f})")
print()
print("   THE RULE, all six neighbours in the same state (t=1/2, |v|=0.35)")
print(f"   {'alpha':>8} {'|v| out':>9} {'det in':>10} {'det out':>10} {'preserved?':>12} {'max delta (R99)':>16}")
for al in (1.0,0.8,1/3,0.0,-1/3):
    vo=al*v0
    pres = abs(det(0.5,vo)-det(t0,v0))<1e-12
    dmax=np.sqrt(max((1-al)*(1+3*al),0))/2
    print(f"   {al:8.4f} {np.linalg.norm(vo):9.4f} {det(t0,v0):10.6f} {det(0.5,vo):10.6f}"
          f" {str(pres):>12} {dmax:16.6f}")
print()
print("   the invariant is preserved only at alpha = 1, where R99 gives delta_max = 0.")
print()
print("   HOW BADLY is it broken at the R99 optimum (alpha = 1/3)?")
print(f"   {'|v| in':>8} {'det in':>10} {'det out':>10} {'ratio':>9} {'|v| lost':>10}")
for m in (0.5,0.4,0.3,0.2,0.1):
    vi=np.array([0,0,m]); vo=vi/3
    print(f"   {m:8.3f} {det(0.5,vi):10.6f} {det(0.5,vo):10.6f} {det(0.5,vo)/max(det(0.5,vi),1e-12):9.4f}"
          f" {m-m/3:10.4f}")
print()
print("   det -> 1/4 (maximally mixed) is the fixed point: the rule drives every state")
print("   to the CENTRE of the light cone, i.e. maximally far from null.")
