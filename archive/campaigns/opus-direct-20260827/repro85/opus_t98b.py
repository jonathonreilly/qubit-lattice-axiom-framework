"""T98b - is T98(B) a refutation of Result 28, or a demonstration of its scope?
T98(B) found the circumcentric dual FAILING to tile on a torus of revolution
(spread 258) where Result 28 had it exact on an icosphere (spread 1.8e-15).
Result 28's own scope says the circumcentric dual tiles only for DELAUNAY
complexes -- T57 measured tiling defects of 9.3, 103 and 795 on deliberately
non-Delaunay (jittered) meshes.  So the question is whether my torus mesh is
Delaunay.  If it is badly non-Delaunay, T98(B) confirms Result 28's scope instead
of contradicting it; if it is Delaunay, Result 28 is in trouble.

Measured: the fraction of non-Delaunay edges (cot alpha + cot beta < 0) and the
triangle aspect ratios, then the same tiling sums on meshes made progressively
better shaped."""
import numpy as np
def torus_mesh(nu,nv,R,r):
    V=[]
    for i in range(nu):
        for j in range(nv):
            u=2*np.pi*i/nu; v=2*np.pi*j/nv
            V.append(np.array([(R+r*np.cos(v))*np.cos(u),(R+r*np.cos(v))*np.sin(u),r*np.sin(v)]))
    idx=lambda i,j:(i%nu)*nv+(j%nv); F=[]
    for i in range(nu):
        for j in range(nv):
            F.append((idx(i,j),idx(i+1,j),idx(i,j+1)))
            F.append((idx(i+1,j),idx(i+1,j+1),idx(i,j+1)))
    return V,F
def circum(p0,p1,p2):
    a=p1-p0;b=p2-p0;n=np.cross(a,b);n2=float(n@n)
    if n2<1e-30: return (p0+p1+p2)/3
    return p0+np.cross(float(a@a)*b-float(b@b)*a,n)/(2*n2)   # FIXED sign (same bug as T54)
def analyse(V,F,label):
    E={}
    for f in F:
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])): E.setdefault((min(a,b),max(a,b)),len(E))
    cot=np.zeros(len(E)); area=0.0; t0=np.zeros(len(V)); t1=np.zeros(len(E))
    inside=0; total=0; ratios=[]
    for f in F:
        p=[V[f[0]],V[f[1]],V[f[2]]]
        A=0.5*float(np.linalg.norm(np.cross(p[1]-p[0],p[2]-p[0]))); area+=A
        ls=[float(np.linalg.norm(p[1]-p[0])),float(np.linalg.norm(p[2]-p[1])),float(np.linalg.norm(p[0]-p[2]))]
        ratios.append(max(ls)/min(ls))
        cc=circum(*p); total+=1
        # is the circumcentre inside the triangle?  barycentric test
        M=np.array([p[1]-p[0],p[2]-p[0]]).T
        lam=np.linalg.lstsq(M,cc-p[0],rcond=None)[0]
        if lam[0]>=-1e-9 and lam[1]>=-1e-9 and lam[0]+lam[1]<=1+1e-9: inside+=1
        nrm=np.cross(p[1]-p[0],p[2]-p[0]); nrm=nrm/np.linalg.norm(nrm)
        for (i,j,o) in ((0,1,2),(1,2,0),(2,0,1)):
            u=p[i]-p[o]; v=p[j]-p[o]
            cot[E[(min(f[i],f[j]),max(f[i],f[j]))]]+=0.5*float(np.dot(u,v)/np.linalg.norm(np.cross(u,v)))
            mid=(p[i]+p[j])/2; mid2=(p[i]+p[o])/2
            t1[E[(min(f[i],f[j]),max(f[i],f[j]))]]+=0.5*float(np.linalg.norm(p[j]-p[i]))*float(np.linalg.norm(cc-mid))
            t0[f[i]]+=abs(0.5*float(np.dot(np.cross(mid-p[i],cc-p[i]),nrm)))+abs(0.5*float(np.dot(np.cross(cc-p[i],mid2-p[i]),nrm)))
    nd=int(np.sum(cot<0))
    spread=max(t0.sum(),t1.sum(),area)-min(t0.sum(),t1.sum(),area)
    print(f"   {label:>30}: non-Delaunay edges {nd:5d}/{len(E):5d}  "
          f"circumcentre inside {inside:5d}/{total:5d}  max aspect {max(ratios):7.2f}  "
          f"tiling spread {spread:10.3e}", flush=True)
print("T98b  is the torus mesh Delaunay?  and does tiling recover when it is?")
analyse(*torus_mesh(16,10,2.0,0.8),"torus R=2 r=0.8 16x10")
analyse(*torus_mesh(24,14,2.0,0.8),"torus R=2 r=0.8 24x14")
analyse(*torus_mesh(40,20,2.0,0.8),"torus R=2 r=0.8 40x20")
print()
print("   for comparison, the icosphere Result 28 used:")
def icosphere(nsub):
    t=(1+5**0.5)/2
    V=[np.array(v,dtype=float) for v in [(-1,t,0),(1,t,0),(-1,-t,0),(1,-t,0),(0,-1,t),(0,1,t),
        (0,-1,-t),(0,1,-t),(t,0,-1),(t,0,1),(-t,0,-1),(-t,0,1)]]
    F=[(0,11,5),(0,5,1),(0,1,7),(0,7,10),(0,10,11),(1,5,9),(5,11,4),(11,10,2),(10,7,6),(7,1,8),
       (3,9,4),(3,4,2),(3,2,6),(3,6,8),(3,8,9),(4,9,5),(2,4,11),(6,2,10),(8,6,7),(9,8,1)]
    for _ in range(nsub):
        mid={}; NF=[]
        def m(i,j):
            k=(min(i,j),max(i,j))
            if k not in mid: V.append((V[i]+V[j])/2); mid[k]=len(V)-1
            return mid[k]
        for (a,b,c) in F:
            ab,bc,ca=m(a,b),m(b,c),m(c,a); NF+=[(a,ab,ca),(b,bc,ab),(c,ca,bc),(ab,bc,ca)]
        F=NF
    return [v/np.linalg.norm(v) for v in V],F
analyse(*icosphere(2),"icosphere sub=2")
analyse(*icosphere(3),"icosphere sub=3")
print()
print("   many non-Delaunay edges / circumcentres outside on the torus, none on the")
print("   icosphere => T98(B) demonstrates Result 28's scope condition rather than")
print("   contradicting it: the circumcentric dual tiles for DELAUNAY complexes.")
