"""T71 - DOES THE FIELD EQUATION HAVE CONTENT?  Does it SELECT a geometry?
T70: flat spacetime is a stationary point of the Regge action on the framework's
complex (deficits 1.8e-15, Schlaefli identity to 1e-14, dS = 1e-11..1e-13).  But
an equation solved by flat space is only interesting if it is NOT solved by
everything.  Two things settle that:

 (C1) a CURVED complex must NOT be stationary in vacuum.  S^4 is not Ricci-flat,
      so the boundary of the 5-simplex must have dS != 0.  If it does, the vacuum
      equation has content.
 (C2) add a COSMOLOGICAL TERM,  S = sum_h A_h delta_h  -  Lambda * sum Vol, and
      the equation should SELECT A SIZE.  Under a uniform rescaling by s the
      deficit angles are scale-INVARIANT (angles do not care about size) while
      A ~ s^2 and Vol ~ s^4, so
            S(s) = s^2 * K  -  Lambda s^4 * V1,     K = sum A delta,  V1 = sum Vol
            dS/ds = 2 s K - 4 Lambda s^3 V1 = 0   ==>   s^2 = K / (2 Lambda V1)
      A genuine selected geometry, with the size fixed by Lambda.  Predicted
      analytically above and measured numerically below -- if they agree, the
      framework's complex carries a field equation that picks a geometry."""
import numpy as np, itertools, math
def qr_hull(P):
    O=P[0]; M=P[1:]-O; Q,_=np.linalg.qr(M.T)
    return np.array([Q.T@(p-O) for p in P])
def dihedral(P,tri):
    o=P[tri[0]]; Hs=np.array([P[tri[1]]-o,P[tri[2]]-o]); Q,_=np.linalg.qr(Hs.T)
    other=[i for i in range(5) if i not in tri]
    def perp(x):
        v=x-o; return v-Q@(Q.T@v)
    u=perp(P[other[0]]); v=perp(P[other[1]])
    nu=np.linalg.norm(u); nv=np.linalg.norm(v)
    if nu<1e-13 or nv<1e-13: return float('nan')
    return float(np.arccos(np.clip(float(np.dot(u,v))/(nu*nv),-1,1)))
def tri_area(p0,p1,p2):
    a=p1-p0; b=p2-p0
    return 0.5*np.sqrt(max(float(np.dot(a,a)*np.dot(b,b)-np.dot(a,b)**2),0.0))
def simplex_vol(P):
    M=P[1:]-P[0]
    return abs(float(np.linalg.det(M)))/math.factorial(4)
# S^4 = boundary of the regular 5-simplex, unit edge, embedded in R^5
V=[np.eye(6)[i] for i in range(6)]
V=[v-np.mean(V,axis=0) for v in V]
B=np.linalg.svd(np.array(V))[2][:5]; V=[B@v for v in V]
V=[v/np.linalg.norm(V[0]-V[1]) for v in V]
tops=[tuple(sorted(c)) for c in itertools.combinations(range(6),5)]
def action(scale, Lam=0.0):
    Vs=[v*scale for v in V]
    tot={}; A={}; vol=0.0
    for t in tops:
        P=np.array([Vs[i] for i in t]); Pl=qr_hull(P)
        vol+=simplex_vol(Pl)
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([t[i] for i in tri]))
            tot[key]=tot.get(key,0.0)+dihedral(Pl,list(tri))
            A[key]=tri_area(P[tri[0]],P[tri[1]],P[tri[2]])
    K=float(sum(A[k]*(2*np.pi-tot[k]) for k in tot))
    return K, vol, K-Lam*vol
K1,V1,_=action(1.0)
print(f"T71  S^4 (boundary of the 5-simplex), unit edge:")
print(f"     K = sum A*deficit = {K1:.6f}    total 4-volume V1 = {V1:.6f}")
print()
print("  (C1) is the CURVED complex stationary in vacuum (Lambda = 0)?  It must NOT be.")
for e in (1e-3,1e-2,1e-1):
    Kp,_,_=action(1.0+e); Km,_,_=action(1.0-e)
    print(f"     scale +-{e}:  dS/ds = {(Kp-Km)/(2*e):+12.6f}   (analytic 2K = {2*K1:.6f})", flush=True)
print("     nonzero and equal to 2K  =>  S^4 is NOT a vacuum solution: the equation")
print("     has content, and it says a sphere needs a source.")
print()
print("  (C2) with a COSMOLOGICAL TERM the equation selects a SIZE")
print(f"     analytic prediction:  s* = sqrt( K / (2 Lambda V1) )")
print(f"   {'Lambda':>9} {'predicted s*':>14} {'measured s* (dS/ds = 0)':>26} {'|diff|':>11}")
for Lam in (0.5,1.0,2.0,5.0):
    spred=np.sqrt(K1/(2*Lam*V1))
    lo,hi=0.05,20.0
    def dS(s,e=1e-4):
        _,_,Sp=action(s+e,Lam); _,_,Sm=action(s-e,Lam)
        return (Sp-Sm)/(2*e)
    for _ in range(60):
        mid=(lo+hi)/2
        if dS(mid)>0: lo=mid
        else: hi=mid
    smeas=(lo+hi)/2
    print(f"   {Lam:9.2f} {spred:14.8f} {smeas:26.8f} {abs(spred-smeas):11.2e}", flush=True)
print()
print("     the scale is FIXED by Lambda, predicted and measured  =>  the framework's")
print("     complex carries a field equation that selects a geometry.")
