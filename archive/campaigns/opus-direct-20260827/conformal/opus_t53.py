"""T53 - DOES ANYTHING PICK THE GEOMETRY?  Stationarity, done properly this time.
Result 26 withdrew a stationarity claim because the deformation family was crude
and the mesh degraded as it grew.  Do it right:

  * an EXACTLY area-preserving one-parameter family.  Rather than deform then
    rescale (which mixes shape and size), use ellipsoids of revolution with the
    area held fixed by solving for the polar axis -- a clean 1-parameter family
    through the round sphere at eps = 0.
  * the deformation applied to the SAME mesh, so combinatorics never change.
  * mesh quality tracked explicitly (min triangle angle, min cotan weight), so a
    degrading mesh cannot be mistaken for physics.
  * observables from Result 26 that are known chopping-independent: E1 and the
    l=1, l=2 level means.
  * and a FINITE-DIFFERENCE derivative in eps at several step sizes, so the
    linear term can be read off rather than eyeballed.

If the round sphere is a critical point, the antisymmetric part of the response
must go to zero as the step shrinks, and the symmetric part must scale as eps^2
with a stable coefficient.  Both are checked.  Hersch's theorem says the round
sphere MAXIMISES lambda1 * Area among genus-0 surfaces, so a maximum is the
expected answer and finding it would validate the whole apparatus against a known
theorem -- an independent check that costs nothing extra."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def spheroid_area(a,c):
    """exact area of a spheroid with equatorial radius a and polar radius c"""
    if abs(c-a)<1e-12: return 4*np.pi*a*a
    if c<a:
        e=np.sqrt(1-(c*c)/(a*a)); return 2*np.pi*a*a*(1+((1-e*e)/e)*np.arctanh(e))
    e=np.sqrt(1-(a*a)/(c*c)); return 2*np.pi*a*a*(1+(c/(a*e))*np.arcsin(e))
def fixed_area_spheroid(eps, A0):
    """c = 1+eps ; solve for a so the exact area equals A0"""
    c=1.0+eps; lo,hi=0.2,3.0
    for _ in range(80):
        mid=(lo+hi)/2
        if spheroid_area(mid,c)<A0: lo=mid
        else: hi=mid
    return (lo+hi)/2, c
def mesh_quality(V,F):
    mn=np.pi
    for f in F:
        p=[V[f[0]],V[f[1]],V[f[2]]]
        for a,b,c in ((0,1,2),(1,2,0),(2,0,1)):
            u=p[b]-p[a]; v=p[c]-p[a]
            mn=min(mn,float(np.arccos(np.clip(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)),-1,1))))
    return mn
def obs(V,F):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,None)
    if np.any(s1<=1e-12): return None
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    e=np.sort(np.clip(np.linalg.eigvalsh(A0.T@A0),0,None)); nz=e[e>1e-9]
    lvl1=[z for z in nz if abs(z-nz[0])<0.35*max(1.0,nz[0])]
    lvl2=[z for z in nz if 4.0<z<8.5]
    return float(nz[0]), float(np.mean(lvl1)), (float(np.mean(lvl2)) if lvl2 else np.nan), float(np.sum(s0)), float(np.sum(s1.min()))
for k in (3,4):
    V0,F=icosphere(k)
    r0=obs(V0,F); A_disc=r0[3]
    A_exact=4*np.pi
    print(f"\n=== icosphere sub={k}  ({len(V0)} verts)  round: E1={r0[0]:.8f} "
          f"l1={r0[1]:.8f} l2={r0[2]:.8f}  min angle={mesh_quality(V0,F)*180/np.pi:.2f} deg")
    print(f"   {'eps':>8} {'a':>9} {'c':>9} {'exact area':>12} {'dE1/E1':>14} "
          f"{'d(l1)/l1':>14} {'min ang':>9} {'min cotan':>11}")
    res={}
    for eps in (-0.08,-0.04,-0.02,-0.01,0.01,0.02,0.04,0.08):
        a,c=fixed_area_spheroid(eps,A_exact)
        V=[np.array([p[0]*a,p[1]*a,p[2]*c]) for p in V0]
        r=obs(V,F)
        if r is None:
            print(f"   {eps:+8.3f} {a:9.5f} {c:9.5f}  degenerate"); continue
        res[eps]=r
        print(f"   {eps:+8.3f} {a:9.5f} {c:9.5f} {spheroid_area(a,c):12.6f} "
              f"{(r[0]-r0[0])/r0[0]:+14.6e} {(r[1]-r0[1])/r0[1]:+14.6e} "
              f"{mesh_quality(V,F)*180/np.pi:9.2f} {r[4]:11.5f}", flush=True)
    print(f"   {'step':>8} {'antisym part':>16} {'sym part':>16} {'sym/eps^2':>14}")
    for h in (0.01,0.02,0.04,0.08):
        if h in res and -h in res:
            fp=(res[h][0]-r0[0])/r0[0]; fm=(res[-h][0]-r0[0])/r0[0]
            print(f"   {h:8.3f} {(fp-fm)/2:16.6e} {(fp+fm)/2:16.6e} {(fp+fm)/2/h**2:14.4f}", flush=True)
print()
print("  antisym -> 0 as the step shrinks  =>  round sphere IS a critical point")
print("  sym/eps^2 stable and NEGATIVE     =>  it is a MAXIMUM, which is Hersch's")
print("  theorem (lambda1 * Area <= 8 pi for genus 0, equality on the round sphere)")
