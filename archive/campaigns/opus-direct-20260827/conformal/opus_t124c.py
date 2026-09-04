"""T124c - the Lorentzian check, branch fixed.  (T124b's failure was mine.)

T124b compared the geometric wedge angle to the sector/rapidity form using cos
alone and got 4.19 for the CORRECT case -- i.e. no discrimination at all.  The
fault was mine, not the prescription's: cos(dphi) pins a complex angle only up
to sign and 2 pi.  Both cos AND sin are needed, exactly as the source lane said.

Derive the pinning rather than guess its sign.  With D = u(a), E = u(b),
u(phi) = (i sin phi, cos phi):
   <D,E>_eta = cos(b-a)
   D ^ E = D_t E_x - D_x E_t = i sin a cos b - i cos a sin b = -i sin(b-a)
so  sin(b-a) = i (D ^ E), and
   z = cos(dphi) + i sin(dphi) = [ <D,E> - (D ^ E) ] / (c_D c_E),    dphi = -i log z.
No convention is fitted: the sign falls out of the parametrisation.  Verified on
u(a), u(b) directly before it is used on anything else."""
import numpy as np
rng=np.random.default_rng(31415)
u=lambda p: np.array([1j*np.sin(p),np.cos(p)])
ip=lambda D,E: -D[0]*E[0]+D[1]*E[1]
wg=lambda D,E: D[0]*E[1]-D[1]*E[0]
def cc(v):
    n2=(-v[0]**2+v[1]**2)
    n2=n2.real if np.iscomplexobj(n2) else n2
    return np.sqrt(n2+0j) if n2>0 else -1j*np.sqrt(-n2)

print("T124c  Lorentzian wedge angle, both cos and sin, sign derived not fitted")
print()
print("   (0) verify z = [<D,E> - D^E]/(c_D c_E) = e^{i(b-a)} on the parametrisation itself")
w=0.0
for a,b in [(0.3,1.1),(-0.7,0.2),(0.4+0.9j,1.2-0.3j),(2.0,0.5)]:
    D,E=u(a),u(b); z=(ip(D,E)-wg(D,E))/(1.0*1.0)
    w=max(w,abs(z-np.exp(1j*(b-a))))
print(f"       worst |z - e^{{i(b-a)}}| over 4 cases (real and complex a,b): {w:.3e}")
print()
def sec_rap(v):
    t,x=v
    if abs(x)>abs(t): k=0 if x>0 else 2
    else:             k=1 if t>0 else 3
    q=np.arctanh(t/x) if k in (0,2) else np.arctanh(x/t)
    return k,q
def test(cfun,signed=True,n=6000):
    worst=0.0; cnt=0
    for _ in range(n):
        while True:
            D=rng.normal(size=2); E=rng.normal(size=2)
            if abs(abs(D[0])-abs(D[1]))>1e-2 and abs(abs(E[0])-abs(E[1]))>1e-2: break
        kD,qD=sec_rap(D); kE,qE=sec_rap(E)
        if (kE-kD)%4 not in (0,1): continue
        z=(ip(D,E)-wg(D,E))/(cfun(D)*cfun(E))
        dgeo=-1j*np.log(z)
        dk=(kE-kD)%4
        dsec=dk*np.pi/2-1j*((qE-qD) if signed else (abs(qE)-abs(qD)))
        worst=max(worst,abs(dgeo-dsec)); cnt+=1
    return worst,cnt
print("   (1) geometric dphi vs sector/rapidity dphi, and the two controls")
print(f"   {'case':>24} {'worst |geometric - sector|':>30}")
w0,c0=test(cc,True)
print(f"   {'CORRECT branch + signed':>24} {w0:30.3e}   ({c0} pairs)")
w1,_=test(lambda v: np.sqrt(abs(-v[0]**2+v[1]**2))+0j,True)
print(f"   {'(a) positive-|.| branch':>24} {w1:30.3e}   <- control, must be O(1)")
w2,_=test(cc,False)
print(f"   {'(b) unsigned rapidity':>24} {w2:30.3e}   <- control, must be O(1)")
print()
if w0<1e-10 and w1>1e-2 and w2>1e-2:
    print("   PASS with teeth: the geometric angle and the sector/rapidity form are the")
    print("   same function, and both controls break it.  The prescription is verified")
    print("   by a route independent of the 4-torus sector count it was built on.")
else:
    print(f"   NOT a clean pass -- correct case {w0:.2e}, controls {w1:.2e} / {w2:.2e}.")
