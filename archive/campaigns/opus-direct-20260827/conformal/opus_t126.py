"""T126 - NEWTON'S CONSTANT.  The number the whole gravity lane has been aiming at.

R66 gave a covariant regulator; R69 showed the arena carries the continuum a_1.
Put them together in the proper-time (Schwinger) form of the matter effective
action and the induced Newton constant falls out with no fitting:

   W(tau_0) = -(1/2) int_{tau_0}^{inf} (ds/s) K(s),    K(s) = Tr e^{-s(Delta+m^2)}

Subtract the volume term and use K(s) - (4 pi s)^{-2} Vol -> int R sqrt(g)/(96 pi^2 s):

   I(tau_0) = -(1/2) int_{tau_0}^{inf} (ds/s)[K(s) - (4 pi s)^{-2} Vol]
            -> - int R sqrt(g) / (192 pi^2 tau_0)

so the observable   tau_0 * I(tau_0)  ->  - int R sqrt(g) / (192 pi^2),  a pure
number with NOTHING adjustable.  On S^2 x T^2, int R sqrt(g) = 8 pi exactly, so

        TARGET:   tau_0 I(tau_0)  ->  -8 pi/(192 pi^2) = -1/(24 pi) = -0.01326291

And matching the coefficient against -(1/16 pi G) int R sqrt(g) gives

        1/(16 pi G) = 1/(192 pi^2 tau_0)   =>   G = 12 pi tau_0 = 12 pi / Lambda^2

i.e. with the framework's own cutoff being the lattice spacing, tau_0 ~ a^2,
NEWTON'S CONSTANT IS THE LATTICE SPACING SQUARED times 12 pi -- the Planck length
IS the spacing, not a separate scale put in by hand.  That is the statement to
test, and the numerical target above is what decides it.

IR: the s -> inf end diverges logarithmically (the zero mode), cured by m > 0.
The mass also shifts the answer at O(m^2 log m^2), so the m-dependence is scanned
rather than assumed away."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")

def K_sph(s,LMAX=4000):
    l=np.arange(LMAX+1.0); return float(np.sum((2*l+1)*np.exp(-s*l*(l+1))))
def K_tor(s,W=14):
    t=0.0
    for w in itertools.product(range(-W,W+1),repeat=2): t+=np.exp(-(w[0]**2+w[1]**2)/(4.0*s))
    return t/(4*np.pi*s)

VOL=4*np.pi*1.0
TARGET=-8*np.pi/(192*np.pi**2)
print("T126  the induced Newton constant on S^2 x T^2")
print(f"      int R sqrt(g) = 8 pi = {8*np.pi:.6f}   (exact, Gauss-Bonnet)")
print(f"      TARGET  tau_0 * I(tau_0) -> -1/(24 pi) = {TARGET:.8f}")
print()
def I_of(tau0,m2,NQ=4000,SMAX=60.0):
    """-(1/2) int_{tau0}^{inf} ds/s [K(s) e^{-s m^2} - (4 pi s)^{-2} Vol e^{-s m^2}]
    on a log grid; the mass factor multiplies BOTH terms (it is in the operator)."""
    ss=np.exp(np.linspace(np.log(tau0),np.log(SMAX),NQ))
    f=np.empty(NQ)
    for i,s in enumerate(ss):
        f[i]=(K_sph(s)*K_tor(s)-VOL/(4*np.pi*s)**2)*np.exp(-s*m2)/s
    return -0.5*np.trapezoid(f,ss) if hasattr(np,'trapezoid') else -0.5*np.trapz(f,ss)

print(f"    {'m^2':>8} " + " ".join(f"{'t0=%g'%t:>12}" for t in (0.02,0.01,0.005,0.002,0.001)))
for m2 in (0.5,0.2,0.1,0.05):
    vals=[]
    for t0 in (0.02,0.01,0.005,0.002,0.001):
        vals.append(t0*I_of(t0,m2))
    print(f"    {m2:8.3f} " + " ".join(f"{v:12.6f}" for v in vals),flush=True)
print()
print("    extrapolate tau_0 -> 0 at each mass (linear in tau_0), then m^2 -> 0")
print(f"    {'m^2':>8} {'tau_0 -> 0':>14} {'% from target':>15}")
ext=[]
for m2 in (0.5,0.2,0.1,0.05):
    a=t0a=0.002; b=0.001
    va=a*I_of(a,m2); vb=b*I_of(b,m2)
    e=vb+(vb-va)*b/(a-b)
    ext.append((m2,e))
    print(f"    {m2:8.3f} {e:14.6f} {100*(e-TARGET)/abs(TARGET):15.2f}")
print()
m2s=np.array([x[0] for x in ext]); es=np.array([x[1] for x in ext])
c=np.polyfit(m2s,es,1)
print(f"    linear in m^2 -> m^2 = 0 :  {c[1]:.8f}   target {TARGET:.8f}"
      f"   ({100*(c[1]-TARGET)/abs(TARGET):+.2f}%)")
print()
print(f"    If this lands on {TARGET:.6f}, then G = 12 pi tau_0: Newton's constant is")
print("    the squared cutoff, and the Planck length is the framework's own spacing.")
