"""T124b - THE LORENTZIAN CHECK, WITH TEETH THIS TIME.

T124's control did not fail, and that is itself the finding: sum(f(E) - f(D))
around a closed fan telescopes to zero for ANY single-valued f, so replacing the
signed rapidity with its magnitude changed nothing.  My test (2) therefore
verified only that sum(dk) = 4, not the rapidity assignment.  Recorded as a
weak test, not a passing one.

The real content is the link my test skipped: that the wedge angle computed from
the GEOMETRY,
      cos(dphi) = <D,E> / (c_D c_E),     c_v = sqrt(<v,v>_eta),
equals the sector/rapidity form  dk*pi/2 - i(q_E - q_D).  That link is where a
wrong prescription dies, so that is what must be tested.  Branch: c is real for
spacelike v and -i|v| for timelike v (checked below against u(pi/2 - iq)), and
the -i pi/2 per light-cone crossing is exactly that branch choice, not an extra
rule bolted on.

Controls that MUST fail (or the test has no teeth):
   (a) c = |<v,v>|^{1/2} always positive  -- drops the timelike branch factor
   (b) dphi = |dk| pi/2 with unsigned rapidity INSIDE the arccos"""
import numpy as np
rng=np.random.default_rng(31415)

def cc(v):
    """c_v = sqrt(<v,v>_eta) on the branch that sends a unit timelike vector to -i."""
    n2=-v[0]**2+v[1]**2
    return np.sqrt(n2+0j) if n2>0 else -1j*np.sqrt(-n2)
def sec_rap(v):
    t,x=v
    if abs(x)>abs(t): k=0 if x>0 else 2
    else:             k=1 if t>0 else 3
    q=[np.arctanh(t/x) if k==0 else 0,np.arctanh(x/t) if k==1 else 0,
       np.arctanh(t/x) if k==2 else 0,np.arctanh(x/t) if k==3 else 0][k]
    return k,q

print("T124b  does the GEOMETRIC wedge angle equal the sector/rapidity form?")
print("       (this is the link a wrong prescription dies on; T124 never tested it)")
print()
print("   first: the branch, checked against u(phi) = (i sin phi, cos phi)")
for q in (0.0,0.7,-1.3):
    vs=np.array([np.sinh(q),np.cosh(q)]);  vt=np.array([np.cosh(q),np.sinh(q)])
    us=vs/cc(vs); ut=vt/cc(vt)
    u=lambda p: np.array([1j*np.sin(p),np.cos(p)])
    print(f"      q={q:5.2f}  spacelike: |v/c - u(-iq)| = {np.abs(us-u(-1j*q)).max():.2e}"
          f"   timelike: |v/c - u(pi/2-iq)| = {np.abs(ut-u(np.pi/2-1j*q)).max():.2e}")
print()
print("   now the test: random ray pairs, geometric dphi vs sector/rapidity dphi")
print(f"   {'case':>22} {'worst |geometric - sector form|':>34}")
def run(cfun,signed=True,n=4000):
    worst=0.0
    for _ in range(n):
        while True:
            D=rng.normal(size=2); E=rng.normal(size=2)
            if abs(abs(D[0])-abs(D[1]))>1e-2 and abs(abs(E[0])-abs(E[1]))>1e-2: break
        kD,qD=sec_rap(D); kE,qE=sec_rap(E)
        if (kE-kD)%4 not in (0,1): continue        # adjacent wedges only
        ip=(-D[0]*E[0]+D[1]*E[1])/(cfun(D)*cfun(E))
        dphi_geo=np.arccos(np.clip(ip.real,-1,1)+0j) if abs(ip.imag)<1e-12 else -1j*np.log(ip+np.sqrt(ip*ip-1+0j))
        dk=(kE-kD)%4
        dphi_sec=dk*np.pi/2-1j*((qE-qD) if signed else (abs(qE)-abs(qD)))
        worst=max(worst,min(abs(dphi_geo-dphi_sec),abs(-dphi_geo-dphi_sec)))
    return worst
print(f"   {'CORRECT branch+signed':>22} {run(cc,True):34.3e}")
print(f"   {'(a) |.| branch':>22} {run(lambda v: np.sqrt(abs(-v[0]**2+v[1]**2))+0j,True):34.3e}   <- must be O(1)")
print(f"   {'(b) unsigned rapidity':>22} {run(cc,False):34.3e}   <- must be O(1)")
print()
print("   A small first row with BOTH controls O(1) is the check T124 failed to be.")
