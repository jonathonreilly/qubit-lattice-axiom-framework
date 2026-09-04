"""T51 - THE IR-SAFE VERSION, which is also open item (c): a chopping-independent
action.
T50 used W = sum over ALL modes of log sqrt(lambda^2+m^2).  That is dominated by
the UV end -- thousands of modes at the mesh scale -- so it measures mesh QUALITY,
not geometry, and a pure-gauge vertex slide moved it.  (It moved as eps^2, so the
FIRST-order gauge response already vanishes; the residue is second order.)  This
is the same lesson the heat-kernel route taught in Result 25: observables that
weight the mesh scale are not physics.

Use the IR end instead, exactly as Results 23-25 did:
    E1     = first nonzero eigenvalue of the 0-form Laplacian
    S_50   = sum of its lowest 50 eigenvalues
Both are far below the mesh cutoff and both were already validated (they gave
l(l+1) and the O(h^2) refinement convergence).

  PROBE 1 (gauge): slide the vertices ALONG the sphere.  Physics must not move,
     and any residue must DIE as the mesh refines.
  PROBE 2 (shape): deform the surface at FIXED AREA by an l=2 harmonic.  Physics
     must move, and must CONVERGE to a nonzero limit as the mesh refines.
  PROBE 3 (stationarity): is the response symmetric in +-eps, i.e. is the round
     sphere a stationary point of the geometry at fixed area?"""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def low(V,F,nmodes=50):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,None)
    if np.any(s1<=1e-12): return None
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    e=np.clip(np.linalg.eigvalsh(A0.T@A0),0,None)
    e=np.sort(e); nz=e[e>1e-9]
    return float(nz[0]), float(np.sum(e[:nmodes])), float(np.sum(s0))
def slide(V,eps):
    out=[]
    for p in V:
        t=np.cross(p,np.array([0.0,0.0,1.0])); n=np.linalg.norm(t)
        t=t/n if n>1e-9 else np.array([1.0,0.0,0.0])
        q=p+eps*t*np.sin(3*np.arccos(np.clip(p[2],-1,1)))
        out.append(q/np.linalg.norm(q))            # exactly on the unit sphere
    return out
def shape(V,F,eps,area0):
    Vd=[p*(1.0+eps*(3*p[2]*p[2]-1.0)) for p in V]     # l=2, m=0
    _,_,s0,_,_,_,_,_=geometry(Vd,F,None)
    f=np.sqrt(area0/float(np.sum(s0)))
    return [p*f for p in Vd]
print("T51  IR-safe observables on the 0-form Laplacian.  eps = 0.05 throughout.")
print()
print(f"   {'mesh':>12} {'verts':>6} | {'GAUGE dE1/E1':>14} {'GAUGE dS50/S50':>16}"
      f" | {'SHAPE dE1/E1':>14} {'SHAPE dS50/S50':>16}")
for k in (2,3,4):
    V,F=icosphere(k)
    b=low(V,F)
    if b is None: continue
    E1,S50,area=b
    g=low(slide(V,0.05),F); s=low(shape(V,F,0.05,area),F)
    if g is None or s is None:
        print(f"   {'icosphere '+str(k):>12} {len(V):6d}   degenerate"); continue
    print(f"   {'icosphere '+str(k):>12} {len(V):6d} | {(g[0]-E1)/E1:+14.3e} {(g[1]-S50)/S50:+16.3e}"
          f" | {(s[0]-E1)/E1:+14.3e} {(s[1]-S50)/S50:+16.3e}", flush=True)
print()
print("   GAUGE column -> 0 with refinement  =  the action does not care how the")
print("   surface is chopped.  SHAPE column -> a nonzero limit  =  it does care")
print("   what shape the surface is.  That pair is what a field equation needs.")
print()
print("T51 PROBE 3  stationarity: is the round sphere a critical point at fixed area?")
V,F=icosphere(3); E1,S50,area=low(V,F)
print(f"   {'eps':>7} {'dE1/E1':>14} {'dS50/S50':>16}")
for eps in (-0.06,-0.04,-0.02,0.02,0.04,0.06):
    r=low(shape(V,F,eps,area),F)
    if r is None: print(f"   {eps:+7.2f}   degenerate"); continue
    print(f"   {eps:+7.2f} {(r[0]-E1)/E1:+14.6e} {(r[1]-S50)/S50:+16.6e}", flush=True)
print()
print("   symmetric in +-eps and one-signed  =>  stationary, and the round sphere")
print("   is an extremum of the spectrum at fixed area.")
