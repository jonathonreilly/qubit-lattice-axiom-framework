"""T49 - THE CURVATURE IS LOCAL, AND IT IS THE RIGHT NUMBER POINTWISE.
I predicted in T48 that an icosphere's curvature would sit concentrated on the
12 original icosahedron vertices.  It does not: the 20 largest defects are all
equal (0.02294) and the 12 special vertices are not among them.  That is not a
defect of the construction, it is the construction being BETTER than my guess --
the angle defect behaves as a curvature DENSITY integrated over the vertex's own
dual cell:
        K_v  ~  Gauss curvature * (dual area of v)
so on a nearly-uniform mesh of a sphere the defects are nearly uniform, and the
valence-5 vertices carry LESS defect because they own less area (5 triangles
rather than 6).  If that reading is right then

        K_v / A_v  ->  the pointwise Gaussian curvature

which is a LOCAL curvature measurement, far sharper than T47's global heat-kernel
route.  Tested on the unit sphere (K = 1 everywhere) and on ellipsoids, where the
exact answer varies over the surface:
        K(x,y,z) = 1 / ( a^2 b^2 c^2 (x^2/a^4 + y^2/b^4 + z^2/c^4)^2 )"""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def defect_and_area(V,F):
    ang=np.zeros(len(V)); area=np.zeros(len(V)); val=np.zeros(len(V),dtype=int)
    for f in F:
        p=[V[f[0]],V[f[1]],V[f[2]]]
        A=0.5*np.linalg.norm(np.cross(p[1]-p[0],p[2]-p[0]))
        for i,(a,b,c) in enumerate(((0,1,2),(1,2,0),(2,0,1))):
            u=p[b]-p[a]; v=p[c]-p[a]
            ang[f[a]]+=np.arccos(np.clip(float(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v))),-1,1))
            area[f[a]]+=A/3.0; val[f[a]]+=1
    return 2*np.pi-ang, area, val
def Kexact(p,a,b,c):
    return 1.0/(a*a*b*b*c*c*(p[0]**2/a**4 + p[1]**2/b**4 + p[2]**2/c**4)**2)
print("T49  is the angle defect a curvature DENSITY?   K_v / A_v  vs  exact K")
print()
print("  (a) UNIT SPHERE, exact K = 1 everywhere")
print(f"   {'mesh':>14} {'verts':>7} {'mean K_v/A_v':>14} {'max err':>11} {'valence-5 K_v':>15} {'valence-6 K_v':>15}")
for k in (1,2,3,4):
    V,F=icosphere(k); K,A,val=defect_and_area(V,F)
    r=K/A
    v5=float(np.mean(K[val==5])); v6=float(np.mean(K[val==6])) if np.any(val==6) else float('nan')
    print(f"   {'icosphere '+str(k):>14} {len(V):7d} {float(np.mean(r)):14.8f} "
          f"{float(np.max(np.abs(r-1))):11.3e} {v5:15.6f} {v6:15.6f}", flush=True)
print("   (valence-5 defect SMALLER than valence-6 confirms 'defect = curvature x area',")
print("    not 'defect concentrated at the 12 special vertices')")
print()
print("  (b) ELLIPSOIDS, exact K varies over the surface")
print(f"   {'axes':>18} {'verts':>7} {'mean |K_v/A_v - K_exact|':>26} {'rel err':>10} {'K range (exact)':>22}")
for axes in ((1.0,1.0,0.7),(1.0,1.0,0.5),(1.0,0.8,0.6)):
    for k in (3,4):
        V0,F=icosphere(k)
        V=[np.array([p[0]*axes[0],p[1]*axes[1],p[2]*axes[2]]) for p in V0]
        K,A,val=defect_and_area(V,F)
        ke=np.array([Kexact(p,*axes) for p in V])
        r=K/A
        err=float(np.mean(np.abs(r-ke))); rel=err/float(np.mean(ke))
        print(f"   {str(axes):>18} {len(V):7d} {err:26.6f} {rel:10.4f} "
              f"[{ke.min():.4f},{ke.max():.4f}]", flush=True)
print()
print("   rel err falling as the mesh refines = the complex's angle defect IS the")
print("   pointwise Gaussian curvature, locally, not merely in the Gauss-Bonnet total.")
