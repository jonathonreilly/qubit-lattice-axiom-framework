"""T67 - does the 4D construction carry GEOMETRY, not just topology?
T66 established the topological side in d=4: d o d = 0 at every degree, chi = 0,
Betti = [1,4,6,4,1] with total kernel exactly 16 -- the doubler-free property in
four dimensions.  Topology is not geometry, so: does the operator reproduce the
known SPECTRUM of the flat 4-torus?

'Cells weigh, faces compare' at degree 0 is exactly the linear-element stiffness
and mass pair on the simplicial mesh (the d-dimensional cotan Laplacian):
   stiffness  K_ij = sum_simplices vol * grad(phi_i) . grad(phi_j)
   mass       M    = the cell weights (lumped: vol/(d+1) per vertex)
and the generalised eigenproblem K x = lambda M x approximates the Laplacian.
On the unit 4-torus the exact spectrum is 4 pi^2 |n|^2 for integer vectors n:
   0,  4pi^2 = 39.478 (multiplicity 8),  8pi^2 = 78.957 (multiplicity 24), ...
The multiplicities are the sharp part -- 8 and 24 are the counts of integer
4-vectors of norm^2 = 1 and 2, and no flat-space accident produces them."""
import numpy as np, itertools, math
def kuhn_torus(L,d=4):
    verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
    tops=[]
    for base in verts:
        for perm in itertools.permutations(range(d)):
            chain=[base]; cur=list(base)
            for a in perm:
                cur=list(cur); cur[a]=(cur[a]+1)%L; chain.append(tuple(cur))
            tops.append((tuple(vid[c] for c in chain), tuple(perm), base))
    return verts,vid,tops
def fem(L,d=4):
    verts,vid,tops=kuhn_torus(L,d)
    n=len(verts); K=np.zeros((n,n)); M=np.zeros(n)
    h=1.0/L
    for (ids,perm,base) in tops:
        # local coordinates of the chain: p_0 = 0, then unit steps h*e_{perm[j]}
        P=np.zeros((d+1,d)); cur=np.zeros(d)
        for j,a in enumerate(perm):
            cur=cur.copy(); cur[a]+=h; P[j+1]=cur
        Jm=(P[1:]-P[0]).T                       # d x d
        detJ=abs(float(np.linalg.det(Jm)))
        vol=detJ/math.factorial(d)
        Jinv=np.linalg.inv(Jm)
        # gradients of the barycentric basis functions
        G=np.zeros((d+1,d))
        G[1:]=Jinv          # rows of Jinv are the barycentric gradients
        G[0]=-np.sum(G[1:],axis=0)
        for a in range(d+1):
            M[ids[a]]+=vol/(d+1)
            for b in range(d+1):
                K[ids[a],ids[b]]+=vol*float(np.dot(G[a],G[b]))
    return K,M
def fem_d(L,d):
    verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
    n=len(verts); K=np.zeros((n,n)); M=np.zeros(n); h=1.0/L
    for base in verts:
        for perm in itertools.permutations(range(d)):
            ids=[vid[base]]; cur=list(base); P=[np.zeros(d)]; c=np.zeros(d)
            for a in perm:
                cur=list(cur); cur[a]=(cur[a]+1)%L; ids.append(vid[tuple(cur)])
                c=c.copy(); c[a]+=h; P.append(c)
            P=np.array(P); Jm=(P[1:]-P[0]).T
            vol=abs(float(np.linalg.det(Jm)))/math.factorial(d)
            Jinv=np.linalg.inv(Jm); G=np.zeros((d+1,d)); G[1:]=Jinv; G[0]=-np.sum(G[1:],axis=0)
            for a in range(d+1):
                M[ids[a]]+=vol/(d+1)
                for b in range(d+1): K[ids[a],ids[b]]+=vol*float(np.dot(G[a],G[b]))
    return K,M
print("T67  SANITY: same assembly in d=1 and d=2, where the answer is elementary")
for d,L,want,mult in ((1,16,4*np.pi**2,2),(1,32,4*np.pi**2,2),(2,12,4*np.pi**2,4),(2,20,4*np.pi**2,4)):
    K,M=fem_d(L,d)
    A=np.diag(1.0/np.sqrt(M))@K@np.diag(1.0/np.sqrt(M))
    e=np.sort(np.clip(np.linalg.eigvalsh(A),0,None)); nz=e[e>1e-8]
    g=[z for z in nz if abs(z-nz[0])<0.06*max(1.0,nz[0])]
    print(f"   d={d} L={L:3d}: lowest nonzero = {np.mean(g):10.5f} x{len(g)}   "
          f"exact {want:.5f} x{mult}", flush=True)
print()
print("T67  flat 4-torus (side 1).  exact: 4 pi^2 |n|^2 = 0, 39.478(x8), 78.957(x24), ...")
print(f"   {'L':>4} {'verts':>7} " + "".join(f"{s:>22}" for s in ("level 1 (want 39.478 x8)","level 2 (want 78.957 x24)")))
for L in (3,4,5,6,8):
    K,M=fem(L)
    n=len(M)
    A=np.diag(1.0/np.sqrt(M))@K@np.diag(1.0/np.sqrt(M))
    e=np.sort(np.clip(np.linalg.eigvalsh(A),0,None))
    nz=e[e>1e-8]
    def clus(x0,arr,tol=0.06):
        g=[z for z in arr if abs(z-x0)<tol*max(1.0,x0)]
        return float(np.mean(g)),len(g)
    c1=clus(nz[0],nz)
    rest=[z for z in nz if z>c1[0]*(1+0.06)]
    c2=clus(rest[0],rest) if rest else (float('nan'),0)
    print(f"   {L:4d} {n:7d} {c1[0]:14.5f} x{c1[1]:<6d} {c2[0]:14.5f} x{c2[1]:<6d}", flush=True)
print()
print("   multiplicities 8 and 24 are the counts of integer 4-vectors with |n|^2 = 1")
print("   and 2 -- getting those right is a genuinely four-dimensional statement.")
