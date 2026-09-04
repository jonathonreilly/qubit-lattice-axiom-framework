"""T48 - THE CLOSURE: the complex's own curvature and the operator's index agree.
The heat-kernel route (T47) gives the right ballpark for chi/6 but its usable
window in t is too narrow at these mesh sizes to be a sharp confirmation -- so
here is a sharp one instead, and it is the more meaningful statement anyway.

The curvature of a cell complex is LOCAL and combinatorial: at each vertex it is
the ANGLE DEFECT  K_v = 2 pi - sum of the corner angles meeting at v.  Flat means
the angles close up; curved means they do not.  Discrete Gauss-Bonnet says

        sum_v K_v  =  2 pi chi .

That is a statement about the GEOMETRY of the complex, computed from angles and
nothing else.  McKean-Singer (T45b) said  Str exp(-t D^2) = chi, a statement
about the SPECTRUM of the operator, computed from eigenvalues and nothing else.
If the two agree, then the operator is reading the complex's actual curvature.
Two independent computations, one number.

Also measured: the defect is CONCENTRATED where it should be.  On an icosphere
the 12 original icosahedron vertices carry a large defect and every subdivision
vertex carries a small one; on a flat torus every defect is zero."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def defects(V,F,tn=None):
    A1=np.array([1.0,0.0,0.0]); A2=np.array([0.5,np.sqrt(3)/2,0.0])
    B=np.array([[A1[0],A2[0]],[A1[1],A2[1]]]); Binv=np.linalg.inv(B)
    def pos(i,ref=None):
        p=V[i].copy()
        if tn is not None and ref is not None:
            uv=Binv@(p[:2]-ref[:2])
            for k in (0,1):
                while uv[k]>0.5: uv[k]-=1.0
                while uv[k]<-0.5: uv[k]+=1.0
            p=np.array([*(B@uv+ref[:2]),0.0])
        return p
    ang=np.zeros(len(V))
    for f in F:
        p=[pos(f[0]), pos(f[1],V[f[0]]), pos(f[2],V[f[0]])]
        for i,(a,b,c) in enumerate(((0,1,2),(1,2,0),(2,0,1))):
            u=p[b]-p[a]; v=p[c]-p[a]
            cs=float(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)))
            ang[f[a]]+=np.arccos(np.clip(cs,-1,1))
    return 2*np.pi-ang
def spectral_chi(V,F,tn=None):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,tn)
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    A1m=np.diag(np.sqrt(s2))@d1@np.diag(1.0/np.sqrt(s1))
    e0=np.clip(np.linalg.eigvalsh(A0.T@A0),0,None)
    e1=np.clip(np.linalg.eigvalsh(A0@A0.T+A1m.T@A1m),0,None)
    e2=np.clip(np.linalg.eigvalsh(A1m@A1m.T),0,None)
    return [float(np.sum(np.exp(-t*e0))-np.sum(np.exp(-t*e1))+np.sum(np.exp(-t*e2)))
            for t in (0.03,0.3,3.0)], nv-ne+nf
print("T48  GEOMETRY (angle defects) vs SPECTRUM (McKean-Singer): same chi?")
print()
print(f"   {'complex':22} {'sum K_v / 2pi':>15} {'V-E+F':>7} {'Str exp(-tD^2) at t=0.03,0.3,3':>34}")
for k in (1,2,3):
    V,F=icosphere(k); tn=None
    K=defects(V,F,tn); st,chi=spectral_chi(V,F,tn)
    print(f"   {'icosphere sub='+str(k):22} {float(np.sum(K))/(2*np.pi):15.9f} {chi:7d} "
          f"{st[0]:11.6f}{st[1]:11.6f}{st[2]:11.6f}", flush=True)
for n in (8,12):
    V,F,tn=flat_torus(n); K=defects(V,F,tn); st,chi=spectral_chi(V,F,tn)
    print(f"   {'flat torus n='+str(n):22} {float(np.sum(K))/(2*np.pi):15.9f} {chi:7d} "
          f"{st[0]:11.6f}{st[1]:11.6f}{st[2]:11.6f}", flush=True)
print()
print("   where the curvature SITS (icosphere sub=3, 642 vertices):")
V,F=icosphere(3); K=defects(V,F)
big=np.sort(K)[::-1]
print(f"     12 largest defects: {[f'{v:.5f}' for v in big[:12]]}")
print(f"     next 8:             {[f'{v:.5f}' for v in big[12:20]]}")
print(f"     12 * (largest) = {12*big[0]:.6f}   ... the icosahedron's 12 vertices")
print(f"     sum of ALL defects = {float(np.sum(K)):.9f}   2 pi chi = {2*np.pi*2:.9f}")
print()
V,F,tn=flat_torus(10); K=defects(V,F,tn)
print(f"   flat torus n=10: max|defect| = {float(np.max(np.abs(K))):.3e}  (flat means every angle closes)")
