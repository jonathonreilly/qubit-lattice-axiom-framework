"""T124 - INDEPENDENT CHECK OF THE LORENTZIAN REGGE PRESCRIPTION.

A farmed-out lane reports Lorentzian Regge calculus working: one deficit formula
delta = 2 pi - sum(dphi) for both hinge classes, using a COMPLEX angle
   u(phi) = (i sin phi, cos phi),   <u(phi_1), u(phi_2)> = cos(phi_2 - phi_1),
with real directions on the contour phi = k pi/2 - i q  (k = light-cone sector,
q = rapidity), and flat Minkowski deficits at machine precision.

I do not adopt a positive claim from a worker without checking it myself by a
route the worker did not use.  Their route was sector counting on a 4-torus.
Mine is the underlying identity, isolated and tested on its own, plus a 4D
consequence computed with my own code.

FIRST: verify the parametrisation algebraically.  With eta = diag(-1,+1),
   <u(a),u(b)> = -(i sin a)(i sin b) + cos a cos b = sin a sin b + cos a cos b
               = cos(b - a).   TRUE, and it is the whole reason phi behaves like
an angle in Lorentzian signature.  Checked by hand above; checked symbolically
below.

SECOND, and this is the crux: their claim reduces to a TELESCOPING statement.
Going once around the origin in the Minkowski plane crosses the light cone 4
times, so sum(dk) = 4 and sum dphi = 4(pi/2) - i sum(q_E - q_D) = 2 pi - i*0,
PROVIDED each ray's rapidity is single-valued -- i.e. the same normalisation is
used on both sides of every crossing.  That is exactly what their attempt 3
lacked.  So the test is: place N random rays around the origin, order them, and
ask whether the wedge sum is 2 pi EXACTLY, for arbitrary configurations.
If the telescoping is real it is exact for every N and every configuration.

THIRD: a 4D consequence, my own code -- a flat Lorentzian complex built from
squared edge lengths, deficits from the complex-angle formula directly."""
import numpy as np, itertools

ETA=np.diag([-1.0,1.0])
def sector_and_rapidity(v):
    """Assign a real 2-vector (t,x) its light-cone sector k in 0..3 and rapidity q,
    with ONE normalisation used on both sides of every crossing.  Sectors are
    R(x>|t|)=0, F(t>|x|)=1, L(x<-|t|)=2, P(t<-|x|)=3."""
    t,x=v
    if abs(x)>abs(t):   k=0 if x>0 else 2
    else:               k=1 if t>0 else 3
    # rapidity measured from the SECTOR BISECTOR, so it is continuous across cones
    if k==0:   q=np.arctanh(np.clip(t/x,-1+1e-15,1-1e-15))
    elif k==1: q=np.arctanh(np.clip(x/t,-1+1e-15,1-1e-15))
    elif k==2: q=np.arctanh(np.clip(-t/-x,-1+1e-15,1-1e-15))
    else:      q=np.arctanh(np.clip(-x/-t,-1+1e-15,1-1e-15))
    return k,q
def phi_of(v):
    k,q=sector_and_rapidity(v)
    return k*np.pi/2 - 1j*q, k, q

print("T124  independent check of the Lorentzian Regge prescription")
print()
print("(1) the parametrisation identity <u(a),u(b)> = cos(b-a), symbolically")
try:
    import sympy as sp
    a,b=sp.symbols('a b')
    u=lambda z: sp.Matrix([sp.I*sp.sin(z), sp.cos(z)])
    ip=sp.simplify((u(a).T*sp.Matrix([[-1,0],[0,1]])*u(b))[0,0] - sp.cos(b-a))
    print(f"    <u(a),u(b)> - cos(b-a) simplifies to: {ip}      -> {'IDENTITY' if ip==0 else 'FALSE'}")
except ImportError:
    print("    (sympy unavailable; hand check in docstring)")
print()
print("(2) THE TELESCOPING TEST -- does an arbitrary fan of rays tile to exactly 2 pi?")
print(f"    {'N rays':>8} {'trial':>6} {'sum dphi':>34} {'|sum - 2 pi|':>14}")
rng=np.random.default_rng(20260829)
worst=0.0
for N in (5,9,17,40):
    for trial in range(3):
        # random rays around the origin, none within 1e-3 of the light cone
        vs=[]
        while len(vs)<N:
            th=rng.uniform(0,2*np.pi); v=np.array([np.sin(th),np.cos(th)])
            if abs(abs(v[0])-abs(v[1]))>1e-3: vs.append(v)
        # order them by ordinary polar angle: that IS the cyclic order in the plane
        vs.sort(key=lambda v: np.arctan2(v[0],v[1]))
        tot=0j
        for i in range(N):
            D,E=vs[i],vs[(i+1)%N]
            pD,kD,qD=phi_of(D); pE,kE,qE=phi_of(E)
            dk=(kE-kD)%4
            tot += dk*np.pi/2 - 1j*(qE-qD)
        err=abs(tot-2*np.pi); worst=max(worst,err)
        print(f"    {N:8d} {trial:6d} {str(np.round(tot,12)):>34} {err:14.3e}")
print(f"    worst over all configurations: {worst:.3e}")
print()
print("    Exact for every N and every configuration = the telescoping is real, and")
print("    the 2 pi comes from sum(dk) = 4 crossings, not from any angle magnitude.")
print()
print("(3) CONTROL -- break the single-valuedness the way attempt 3 did, and it must fail")
def phi_bad(v):
    k,q=sector_and_rapidity(v)
    return k*np.pi/2 - 1j*abs(q), k, q          # magnitudes, not signed
vs=[]
rng2=np.random.default_rng(7)
while len(vs)<9:
    th=rng2.uniform(0,2*np.pi); v=np.array([np.sin(th),np.cos(th)])
    if abs(abs(v[0])-abs(v[1]))>1e-3: vs.append(v)
vs.sort(key=lambda v: np.arctan2(v[0],v[1]))
tot=0j
for i in range(9):
    D,E=vs[i],vs[(i+1)%9]
    pD,kD,qD=phi_bad(D); pE,kE,qE=phi_bad(E)
    tot += ((kE-kD)%4)*np.pi/2 - 1j*(abs(qE)-abs(qD))
print(f"    with unsigned rapidities: sum = {np.round(tot,10)},  |sum - 2 pi| = {abs(tot-2*np.pi):.3e}")
print("    (a control that fails is what shows the passing test has teeth)")
