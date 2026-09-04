"""T127b - the induced 1/G ratio, extrapolated the way T126 was.

T127 part (3) gave 2.91, 2.64, 2.42 -- drifting with m^2 and nowhere near the 8
that parts (1) and (2) pin exactly.  That is unconverged numerics, not a
disagreement: a single tau_0 = 0.001 with no extrapolation, on a quantity whose
free-subtraction and IR behaviour differ between rank 1 and rank 16.  Redo it
with T126's procedure (linear in tau_0 -> 0, then linear in m^2 -> 0) so the
number is measured rather than asserted from the algebra.

The algebra says what it must be.  The proper-time integral is LINEAR in a_1, so
   induced (1/G)_KD / (1/G)_scalar = (statistics sign) x (a_1 ratio)
                                   = (-1) x (-8) = +8,
giving  1/(16 pi G) = 8/(192 pi^2 tau_0),  i.e.  G = (3 pi/2) tau_0.

STATED ASSUMPTION, not a computed result: that the Kahler-Dirac field is
FERMIONIC.  That is a framework fact (the fibre is an irreducible Cl(d,d) module,
spin (x) flavour -- 4 Dirac flavours in d=4), not something this probe derives.
If it were bosonic the sign flips and the induced gravity is repulsive.  The
sign of induced gravity in this framework rests on that one statement."""
import numpy as np, itertools
def K0_sph(s,LMAX=4000):
    l=np.arange(LMAX+1.0); return float(np.sum((2*l+1)*np.exp(-s*l*(l+1))))
def K0_tor(s,W=14):
    t=0.0
    for w in itertools.product(range(-W,W+1),repeat=2): t+=np.exp(-(w[0]**2+w[1]**2)/(4.0*s))
    return t/(4*np.pi*s)
Kscal=lambda s: K0_sph(s)*K0_tor(s)
Kform=lambda s: (4*K0_sph(s)-2.0)*(4*K0_tor(s))
VOL=4*np.pi
def tauI(tau0,m2,Kfun,rank,NQ=3000,SMAX=60.0):
    ss=np.exp(np.linspace(np.log(tau0),np.log(SMAX),NQ))
    f=np.array([(Kfun(s)-rank*VOL/(4*np.pi*s)**2)*np.exp(-s*m2)/s for s in ss])
    tr=np.trapezoid if hasattr(np,'trapezoid') else np.trapz
    return -0.5*tau0*tr(f,ss)

print("T127b  induced 1/G: Kahler-Dirac fibre vs one scalar, properly extrapolated")
print(f"       algebraic target: (-1)_statistics x (-8)_a1  =  +8")
print()
print(f"    {'m^2':>7} " + " ".join(f"{'t0=%g'%t:>11}" for t in (0.004,0.002,0.001,0.0005)))
ext=[]
for m2 in (0.4,0.2,0.1,0.05):
    rs=[]
    for t0 in (0.004,0.002,0.001,0.0005):
        a=tauI(t0,m2,Kscal,1); b=tauI(t0,m2,Kform,16)
        rs.append((-b)/a)          # (-1) for fermi statistics, then ratio
    print(f"    {m2:7.3f} " + " ".join(f"{r:11.5f}" for r in rs),flush=True)
    e=rs[-1]+(rs[-1]-rs[-2])*0.0005/(0.001-0.0005)
    ext.append((m2,e))
print()
print(f"    {'m^2':>7} {'tau_0 -> 0':>13}")
for m2,e in ext: print(f"    {m2:7.3f} {e:13.5f}")
m2s=np.array([x[0] for x in ext]); es=np.array([x[1] for x in ext])
c=np.polyfit(m2s,es,1)
print(f"    linear in m^2 -> 0 :  {c[1]:.5f}     target 8      ({100*(c[1]-8)/8:+.2f}%)")
print()
print(f"    => 1/(16 pi G) = 8/(192 pi^2 tau_0),   G = (3 pi/2) tau_0 = {1.5*np.pi:.6f} tau_0")
print("       positive, attractive, and 8x a single scalar.")
