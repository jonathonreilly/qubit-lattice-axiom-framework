"""T50 - A FIELD EQUATION ON THE CURVED ARENA?  The question Results 19-22 could
not even ask, now that Result 25 supplies a covariant, doubler-free, curved
complex that knows its own topology.

Same programme as Result 17, but in the language that works.  The effective
action is  W = log |det (D + m)|  on the complex; the geometry is the complex's
own vertex positions.  Vary the GEOMETRY and ask what the action wants.

The crucial difference from the rigid-lattice attempt: there the metric was a
field on a fixed grid, the volume selector V^2 = det g told us which variation
was physical, and no repair made it diffeomorphism invariant.  Here the
reparametrisation freedom is ALREADY quotiented out -- Results 23-25 showed the
spectrum does not care how the same geometry is chopped -- so any response that
survives is a response to GEOMETRY, not to a coordinate choice.

Probe 1 (the control that Results 19-22 failed): move the vertices ALONG the
surface (a reparametrisation -- pure gauge).  W must not move.
Probe 2 (the physics): move the surface OFF itself -- deform the sphere's shape
at fixed area.  W must move, and the way it moves is the field equation.
Probe 3: is the flat/round configuration STATIONARY at fixed area?"""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def W_of(V,F,m,tn=None):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,tn)
    if np.any(s1<=1e-12): return None,None
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    A1=np.diag(np.sqrt(s2))@d1@np.diag(1.0/np.sqrt(s1))
    N=nv+ne+nf; D=np.zeros((N,N))
    D[nv:nv+ne,0:nv]=A0; D[0:nv,nv:nv+ne]=A0.T
    D[nv+ne:,nv:nv+ne]=A1; D[nv:nv+ne,nv+ne:]=A1.T
    ev=np.linalg.eigvalsh(D+0.0)
    return float(np.sum(np.log(np.abs(ev+ 0.0)+0.0j).real*0.0 + np.log(np.sqrt(ev**2+m*m)))), float(np.sum(s0))
def sph_harm_real(p,l,mm):
    x,y,z=p
    if l==2 and mm==0: return 3*z*z-1.0
    if l==2 and mm==2: return x*x-y*y
    if l==1 and mm==0: return z
    if l==3 and mm==0: return z*(5*z*z-3)
    if l==4 and mm==0: return 35*z**4-30*z*z+3
    return 0.0
def renorm_area(V,F,target):
    _,_,s0,_,_,_,_,_=geometry(V,F,None); a=float(np.sum(s0))
    f=np.sqrt(target/a); return [p*f for p in V]
V0,F=icosphere(3); m=0.6
_,A0area=W_of(V0,F,m); Wr,_=W_of(V0,F,m)
print(f"T50  icosphere sub=3, m={m}.  round sphere: W = {Wr:.8f}, area = {A0area:.6f}")
print()
print("Probe 1 - PURE GAUGE: slide vertices ALONG the sphere (reparametrisation).")
print("   Result 19's rigid-lattice analogue failed this by 54%.")
rng=np.random.default_rng(3)
for eps in (0.02,0.05,0.10):
    Vg=[]
    for p in V0:
        t=np.cross(p,np.array([0.0,0.0,1.0]))
        n=np.linalg.norm(t); t=t/n if n>1e-9 else np.array([1.0,0.0,0.0])
        q=p+eps*t*np.sin(3*np.arccos(np.clip(p[2],-1,1)))
        Vg.append(q/np.linalg.norm(q))                      # stay exactly ON the sphere
    Wg,ag=W_of(Vg,F,m)
    if Wg is None: print(f"   eps={eps}: degenerate mesh"); continue
    print(f"   eps={eps:.2f}: area={ag:.6f} (d={ag-A0area:+.2e})   W-W_round = {Wg-Wr:+.6e}"
          f"   relative {abs(Wg-Wr)/abs(Wr):.3e}", flush=True)
print()
print("Probe 2 - PHYSICS: deform the SHAPE at fixed area (l=2 and l=4 harmonics).")
for l,mm in ((2,0),(2,2),(4,0)):
    print(f"   l={l},m={mm}:", end="")
    for eps in (-0.06,-0.03,0.03,0.06):
        Vd=[p*(1.0+eps*sph_harm_real(p,l,mm)) for p in V0]
        Vd=renorm_area(Vd,F,A0area)
        Wd,ad=W_of(Vd,F,m)
        print(f"  eps={eps:+.2f}: dW={Wd-Wr:+.5e}" if Wd is not None else f"  eps={eps:+.2f}: degen", end="")
    print(flush=True)
print()
print("   Probe 1 ~ 0 and Probe 2 != 0 would mean: the action is blind to how the")
print("   surface is chopped and sensitive to what SHAPE it is -- i.e. a genuine")
print("   geometric functional, which is what a field equation needs.")
print("   Probe 2 symmetric in +-eps => the round sphere is STATIONARY (a solution).")
