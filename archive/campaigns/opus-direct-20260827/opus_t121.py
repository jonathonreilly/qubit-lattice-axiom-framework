"""T121 - DOES A PIECEWISE-FLAT COMPLEX HAVE THE CONTINUUM a_1?  (the whole question)

Sakharov's induced Einstein-Hilbert term IS the a_1 heat-kernel coefficient.  For
a SMOOTH d-manifold,   K(tau) ~ (4 pi tau)^{-d/2}[ Vol + (tau/6) int R sqrt(g) + ...].
The framework's arena is not smooth: it is piecewise flat, with all curvature
concentrated on codimension-2 hinges as deficit angles.  So the question that
decides the induced Newton constant is not "can we measure a_1" but

        does a piecewise-flat complex have the SAME a_1 as the smooth manifold
        it approximates, or a different one?

If different, the framework induces gravity with a different coefficient -- a
physical statement about the framework, not a numerical nuisance.

4D cannot answer this: T119/T120 showed the usable tau-window closes between the
lattice floor (tau >> h^2) and the torus winding sum, and Vol is not resolvable
to the needed 1e-5 at any reachable L.  2D CAN answer it, cleanly, because:
  * in d=2 the a_1 term is the CONSTANT term of K(tau) -- no slope fit needed;
  * Gauss-Bonnet makes it purely topological, int R dA = 4 pi chi, so the smooth
    prediction is c_smooth = chi/6, with NO free parameters and no metric input;
  * a sphere at subdivision level 5 has 10242 vertices -- fully diagonalisable.

Two candidate answers, both sharp:
    c = chi/6 = 1/3   -> piecewise-flat reproduces the smooth a_1 exactly.
    c = chi/3 = 2/3   -> the naive small-deficit expansion of Cheeger's cone term
                         sum_v (1/12)(2 pi/theta_v - theta_v/2 pi), which is what
                         one gets by treating each vertex as an isolated cone.
Whichever it is, it is the coefficient the framework actually induces."""
import numpy as np, itertools

def icosphere(k):
    t=(1+5**0.5)/2
    V=[(-1,t,0),(1,t,0),(-1,-t,0),(1,-t,0),(0,-1,t),(0,1,t),(0,-1,-t),(0,1,-t),
       (t,0,-1),(t,0,1),(-t,0,-1),(-t,0,1)]
    V=[np.array(v,dtype=float) for v in V]
    Fc=[(0,11,5),(0,5,1),(0,1,7),(0,7,10),(0,10,11),(1,5,9),(5,11,4),(11,10,2),
        (10,7,6),(7,1,8),(3,9,4),(3,4,2),(3,2,6),(3,6,8),(3,8,9),(4,9,5),
        (2,4,11),(6,2,10),(8,6,7),(9,8,1)]
    for _ in range(k):
        mid={}; NF=[]
        def m(i,j):
            key=(min(i,j),max(i,j))
            if key not in mid:
                V.append(V[i]+V[j]); mid[key]=len(V)-1
            return mid[key]
        for a,b,c in Fc:
            ab,bc,ca=m(a,b),m(b,c),m(c,a)
            NF+=[(a,ab,ca),(b,bc,ab),(c,ca,bc),(ab,bc,ca)]
        Fc=NF
    P=np.array([v/np.linalg.norm(v) for v in V])
    return P,Fc

def spec2d(P,Fc):
    """Intrinsic cotangent Laplacian of the piecewise-flat surface (same formula
    as the general-d code: K_ab = V (G^-1)_ab from edge lengths alone)."""
    N=len(P); K=np.zeros((N,N)); Mv=np.zeros(N); area=0.0; ang={}
    for f in Fc:
        p=[P[i] for i in f]
        l2=np.array([[float((p[i]-p[j])@(p[i]-p[j])) for j in range(3)] for i in range(3)])
        G=np.array([[0.5*(l2[0,a+1]+l2[0,b+1]-l2[a+1,b+1]) for b in range(2)] for a in range(2)])
        dg=np.linalg.det(G)
        if dg<=0: return None,None,None
        V=np.sqrt(dg)/2.0; area+=V
        Gi=np.linalg.inv(G)
        loc=np.zeros((3,3)); loc[1:,1:]=V*Gi
        loc[0,1:]=-loc[1:,1:].sum(axis=0); loc[1:,0]=loc[0,1:]; loc[0,0]=V*Gi.sum()
        idx=list(f); K[np.ix_(idx,idx)]+=loc; Mv[idx]+=V/3.0
        # interior angles, for the deficit / cone-term comparison
        for a in range(3):
            b,c=(a+1)%3,(a+2)%3
            u=p[b]-p[a]; v=p[c]-p[a]
            ang[f[a]]=ang.get(f[a],0.0)+float(np.arccos(np.clip(u@v/(np.linalg.norm(u)*np.linalg.norm(v)),-1,1)))
    s=1.0/np.sqrt(Mv); A=(K*s[None,:])*s[:,None]
    return np.linalg.eigvalsh(0.5*(A+A.T)), area, ang

TAUS=np.array([0.002,0.004,0.008,0.015,0.03,0.06,0.10])
print("T121  the a_1 coefficient of a piecewise-flat complex (2D sphere, chi=2)")
print(f"      smooth prediction   c = chi/6 = {2/6:.6f}")
print(f"      isolated-cone sum   c = chi/3 = {2/3:.6f}")
print()
for k in (3,4,5):
    P,Fc=icosphere(k); lam,area,ang=spec2d(P,Fc)
    if lam is None: print(f"   k={k}: degenerate"); continue
    defs=np.array([2*np.pi-ang[i] for i in range(len(P))])
    cone=float(np.sum([(1.0/12.0)*(2*np.pi/(2*np.pi-dd)-(2*np.pi-dd)/(2*np.pi)) for dd in defs]))
    print(f"   subdivision k={k}: {len(P)} vertices, {len(Fc)} triangles")
    print(f"      polyhedron area {area:.6f}  (sphere 4 pi = {4*np.pi:.6f});"
          f"  sum of deficits {defs.sum():.9f}  (4 pi chi = {4*np.pi:.9f})")
    print(f"      Cheeger cone-term sum  sum_v (1/12)(2pi/theta - theta/2pi) = {cone:.6f}")
    K=np.array([float(np.sum(np.exp(-t*lam))) for t in TAUS])
    c=K-area/(4*np.pi*TAUS)
    print(f"      {'tau':>8} " + " ".join(f"{t:9.4g}" for t in TAUS))
    print(f"      {'c(tau)':>8} " + " ".join(f"{x:9.5f}" for x in c), flush=True)
    print()
print("   c(tau) plateauing at 1/3 says the framework's piecewise-flat arena induces")
print("   exactly the continuum Einstein-Hilbert coefficient.  Plateauing at 2/3 says")
print("   it induces twice it.  Either is a definite, checkable physical statement.")
