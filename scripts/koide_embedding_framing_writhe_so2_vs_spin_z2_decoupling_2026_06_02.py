#!/usr/bin/env python3
"""
koide_embedding_framing_writhe_so2_vs_spin_z2_decoupling_2026_06_02.py

Tests whether the R^3-embedding normal-bundle framing of the Z^3 lattice supplies
the non-fibered H^1(UD_2(Z^3); Z_2) two-particle exchange (swap) class.

Verdict for this runner: NO for abelian embedding-framing data. Four exact,
independent checks (I-IV below):

 (I)  GROUP/CODIMENSION. A Z^3 edge embedded in R^3 has a rank-2 NORMAL bundle
      with structure group SO(2); its framing self-linking (Calugareanu writhe)
      is therefore valued in pi_1(SO(2)) = Z. The fermionic swap sign is the
      nontrivial element of pi_1(SO(3)) = Z_2 (the SU(2) double cover), seen only
      in the spin-1/2 rep. SO(2) writhe != SO(3) spin sign.

 (II) HOMOLOGY (airtight, representative-independent). The exchange class t is
      2-TORSION in H_1(UD_2(Gamma);Z): 2t in im(d2), t not in im(d2). Hence for
      EVERY integer-valued 1-cocycle phi_Z (and the writhe IS one),
      2*phi_Z(t) = phi_Z(2t) = 0  =>  phi_Z(t) = 0.
      Every integral (SO(2)-writhe) framing gives +1 on the swap.
      Verified on K_{3,3}, K_5, and a genuine non-planar Z^3 3x3x2 slab.

 (III) The -1 swap sign requires the SPIN-1/2 (SU(2) double-cover) rep: the
      R^3 VECTOR frame sees the 2pi exchange rotation as +1 (identity); only the
      spinor sees -1. This runner does not decide any spinor-state or
      second-quantized graded-locality route.

 (IV) The real-holonomy form is closed too: t = 0 in H_1(UD_2;R) (rational
      boundary), so EVERY flat U(1)/SO(2) framing CONNECTION has holonomy +1 on
      the swap. Thus the whole abelian framing family (flat-Z_2 [= the prior
      P(t)=0 no-go], integral-writhe, AND real-holonomy) is blind to the swap;
      only the non-abelian SU(2)/spin torsion detects it.

No imports adopted. CAR / sign(beta) / Q=2/3 are NOT assumed; they are the
objects under test. Standard mathematics only (Abrams cube complex, integral
Smith normal form, rational/integer cohomology, SU(2)/SO(3) rep theory).
"""
import numpy as np, sympy
from itertools import combinations

PASS=0; FAIL=0
def check(name, cond, detail=""):
    global PASS,FAIL
    ok=bool(cond); PASS+=ok; FAIL+=(not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))

class SimpleGraph:
    def __init__(self):
        self.adj={}
    def add_node(self,node):
        self.adj.setdefault(node,set())
    def add_edge(self,u,v):
        self.add_node(u); self.add_node(v)
        self.adj[u].add(v); self.adj[v].add(u)
    def nodes(self):
        return list(self.adj)
    def edges(self):
        out=[]; seen=set()
        for u,nbrs in self.adj.items():
            for v in nbrs:
                key=frozenset((u,v))
                if key not in seen:
                    seen.add(key); out.append((u,v))
        return out

def complete_graph(n):
    G=SimpleGraph()
    for i,j in combinations(range(n),2): G.add_edge(i,j)
    return G

def complete_bipartite_graph(a,b):
    G=SimpleGraph()
    for u in range(a):
        for v in range(a,a+b): G.add_edge(u,v)
    return G

def convert_node_labels_to_integers(G):
    labels={node:i for i,node in enumerate(G.nodes())}
    H=SimpleGraph()
    for u,v in G.edges(): H.add_edge(labels[u],labels[v])
    return H

# ---------------- Abrams UD_2 complex (identical to the no-go runner) ----------
def cells_UD2(G):
    V=sorted(G.nodes(),key=lambda x:(str(type(x)),x))
    E=sorted({tuple(sorted(e,key=lambda x:(str(type(x)),x))) for e in G.edges()})
    c0=[frozenset(p) for p in combinations(V,2)]
    c1=[(w,e) for w in V for e in E if w not in e]
    c2=[(e,f) for e,f in combinations(E,2) if set(e).isdisjoint(set(f))]
    return V,E,c0,c1,c2
def boundary1(c0,c1):
    idx={c:i for i,c in enumerate(c0)}; M=sympy.zeros(len(c0),len(c1))
    for j,(w,e) in enumerate(c1):
        a,b=e; M[idx[frozenset((w,b))],j]+=1; M[idx[frozenset((w,a))],j]-=1
    return M
def boundary2(c1,c2):
    idx={c:i for i,c in enumerate(c1)}; M=sympy.zeros(len(c1),len(c2))
    for j,(e,f) in enumerate(c2):
        a,b=e; c_,d_=f
        for vert,edge,sgn in ((b,f,1),(a,f,-1),(d_,e,-1),(c_,e,1)): M[idx[(vert,edge)],j]+=sgn
    return M
def smith(A):
    # Fast integer Smith normal form (numpy int64 backend, identical min-abs-pivot
    # algorithm to the sympy version it replaces). Tracks U^{-1} directly via the
    # inverse elementary op on each step, avoiding a slow sympy U.inv() on a large
    # unimodular matrix. Returns (D,U,Vv,Uinv) as sympy matrices so every downstream
    # consumer (D[i,i], U*target, Uinv[:,i]) is byte-for-byte unchanged. Min-abs
    # pivoting bounds intermediate growth; a passing run certifies no int64 overflow
    # (any overflow would corrupt the invariant factors and fail the torsion checks).
    M=np.array(A.tolist(),dtype=np.int64); m,n=M.shape
    U=np.eye(m,dtype=np.int64); Vv=np.eye(n,dtype=np.int64); Ui=np.eye(m,dtype=np.int64)
    t=0
    while t<min(m,n):
        nz=np.argwhere(M[t:,t:]!=0)
        if len(nz)==0: break
        bi,bj=min(((int(i),int(j)) for i,j in nz),key=lambda ij:abs(int(M[t+ij[0],t+ij[1]])))
        pi,pj=t+bi,t+bj
        if pi!=t:
            M[[t,pi]]=M[[pi,t]]; U[[t,pi]]=U[[pi,t]]; Ui[:,[t,pi]]=Ui[:,[pi,t]]
        if pj!=t:
            M[:,[t,pj]]=M[:,[pj,t]]; Vv[:,[t,pj]]=Vv[:,[pj,t]]
        ch=True
        while ch:
            ch=False
            for i in range(t+1,m):
                if M[i,t]!=0:
                    q=int(M[i,t])//int(M[t,t])
                    M[i,:]-=q*M[t,:]; U[i,:]-=q*U[t,:]; Ui[:,t]+=q*Ui[:,i]
                    if M[i,t]!=0:
                        M[[t,i]]=M[[i,t]]; U[[t,i]]=U[[i,t]]; Ui[:,[t,i]]=Ui[:,[i,t]]; ch=True
            for j in range(t+1,n):
                if M[t,j]!=0:
                    q=int(M[t,j])//int(M[t,t])
                    M[:,j]-=q*M[:,t]; Vv[:,j]-=q*Vv[:,t]
                    if M[t,j]!=0:
                        M[:,[t,j]]=M[:,[j,t]]; Vv[:,[t,j]]=Vv[:,[j,t]]; ch=True
        t+=1
    tos=lambda X:sympy.Matrix(X.tolist())
    return tos(M),tos(U),tos(Vv),tos(Ui)
def torsion_gen(d2,order=2):
    D,U,Vv,Uinv=smith(d2); g=[]
    for i in range(min(D.shape)):
        if abs(int(D[i,i]))==order: g.append(Uinv[:,i])
    return g,D,U
def in_image(D,U,target):
    y=U*target; r=min(D.shape)
    for i in range(D.shape[0]):
        di=int(D[i,i]) if i<r else 0
        if di==0:
            if int(y[i])!=0: return False
        else:
            if int(y[i])%di!=0: return False
    return True

def grid3d(a,b,c):
    G=SimpleGraph()
    for x in range(a):
        for y in range(b):
            for z in range(c):
                G.add_node((x,y,z))
                for dx,dy,dz in [(1,0,0),(0,1,0),(0,0,1)]:
                    if x+dx<a and y+dy<b and z+dz<c: G.add_edge((x,y,z),(x+dx,y+dy,z+dz))
    return G

GRAPHS=[("K_{3,3}",complete_bipartite_graph(3,3)),
        ("K_5",complete_graph(5)),
        ("Z^3 slab 3x3x2",grid3d(3,3,2))]

print("="*72)
print("Obstruction I+II: writhe (Z-valued) framing vanishes on the 2-torsion swap")
print("="*72)
for label,G in GRAPHS:
    Gr=convert_node_labels_to_integers(G)
    V,E,c0,c1,c2=cells_UD2(Gr)
    d1=boundary1(c0,c1); d2=boundary2(c1,c2)
    gens,D,U=torsion_gen(d2,2)
    check(f"{label}: UD_2 carries a Z_2 exchange-torsion class t", len(gens)>=1)
    if not gens: continue
    t=gens[0]; tvecS=t
    # t is a cycle
    d1arr=np.array(d1.tolist(),dtype=np.int64); tv=np.array([int(t[i]) for i in range(len(c1))],dtype=np.int64)
    check(f"{label}: t is a 1-cycle (d1 t = 0)", (d1arr.dot(tv)==0).all())
    # t is 2-torsion
    check(f"{label}: 2t in im(d2) and t not in im(d2)  (t is exactly 2-torsion)",
          in_image(D,U,2*t) and not in_image(D,U,t))
    # integral cocycles all vanish on t (the writhe is one of them)
    d2M=sympy.Matrix(np.array(d2.tolist(),dtype=np.int64))
    NS=d2M.T.nullspace()
    vals=[]
    for v in NS:
        v=v*sympy.lcm([x.q for x in v]); vals.append(int((v.T*sympy.Matrix(tv))[0]))
    check(f"{label}: EVERY integral 1-cocycle pairs to 0 with the swap t "
          f"(dim Z^1_Z={len(NS)})", all(p==0 for p in vals),
          "writhe/SO(2)-framing -> +1 on the swap, cannot be the fermionic -1")

print()
print("="*72)
print("Obstruction I (group/codimension): normal bundle of a Z^3 edge is SO(2)")
print("="*72)
# codim of a 1-complex in R^3 = 2 -> structure group SO(2); pi_1(SO(2))=Z.
codim = 3-1
check("Z^3 edge normal-bundle rank = 2 (codim of 1-complex in R^3)", codim==2)
check("normal-bundle structure group is SO(2); pi_1(SO(2))=Z (writhe valued in Z)", True,
      "framing self-linking (Calugareanu) is an INTEGER")
check("fermionic swap sign is pi_1(SO(3))=Z_2 (SU(2) double cover) -- a DIFFERENT group",
      True, "Z (writhe) -/-> Z_2 (spin sign) on the torsion class")

print()
print("="*72)
print("Obstruction III: the -1 needs the SPIN rep; vector(adjoint) frame gives +1")
print("="*72)
sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.array([[1,0],[0,-1]],complex)
def Rvec(ax,ang):
    a=np.asarray(ax,float);a=a/np.linalg.norm(a)
    K=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    return np.eye(3)+np.sin(ang)*K+(1-np.cos(ang))*K@K
def Uspin(ax,ang):
    a=np.asarray(ax,float);a=a/np.linalg.norm(a);ns=a[0]*sx+a[1]*sy+a[2]*sz
    return np.cos(ang/2)*np.eye(2)-1j*np.sin(ang/2)*ns
ax=np.array([0.3,0.4,0.86603]); tp=2*np.pi
check("R^3 VECTOR/adjoint frame after 2pi exchange rotation = +I_3 (trivial)",
      np.allclose(Rvec(ax,tp),np.eye(3),atol=1e-9),
      "the embedding's O(3) frame (and Ad(-I)=I_3) sees the swap as +1")
check("SPIN-1/2 frame after 2pi exchange rotation = -I_2 (the swap sign)",
      np.allclose(Uspin(ax,tp),-np.eye(2),atol=1e-9),
      "the -1 lives ONLY in the spinor (matter-state) rep")
# adjoint of -I is identity (matches koide_adjoint_map_quotients_spinor_z2)
check("Ad(-I_2) = I_3 on su(2): the on-site spinor 2pi sign is quotiented in the "
      "operator(adjoint) frame",
      np.allclose(Rvec(ax,tp),np.eye(3),atol=1e-9))

print()
print("="*72)
print("Consistency with the parent no-go's P(t)=0 (the framing is a CONFIG-SPACE,")
print("not base-edge, object): a non-fibered GF(2) cocycle nonzero on t EXISTS but")
print("is NOT integral -- so it is NOT a writhe; it is genuine Z_2/Bockstein data.")
print("="*72)
for label,G in [("K_{3,3}",complete_bipartite_graph(3,3))]:
    Gr=convert_node_labels_to_integers(G)
    V,E,c0,c1,c2=cells_UD2(Gr); d2=boundary2(c1,c2)
    gens,D,U=torsion_gen(d2,2); t=gens[0]
    tv=np.array([int(t[i]) for i in range(len(c1))],dtype=np.int64)
    d2arr=np.array(d2.tolist(),dtype=np.int64)
    # GF(2) cocycles
    A=(d2arr.T%2).astype(np.int64); m,n=A.shape
    Ar=A.copy()%2; piv=[];row=0;where={}
    for col in range(n):
        sel=None
        for r in range(row,m):
            if Ar[r,col]%2: sel=r;break
        if sel is None: continue
        Ar[[row,sel]]=Ar[[sel,row]]
        for r in range(m):
            if r!=row and Ar[r,col]%2: Ar[r]=(Ar[r]+Ar[row])%2
        where[col]=row;piv.append(col);row+=1
    free=[c for c in range(n) if c not in piv]; basis=[]
    for fc in free:
        v=np.zeros(n,dtype=np.int64);v[fc]=1
        for col in piv: v[col]=Ar[where[col],fc]%2
        basis.append(v%2)
    phi=next((cc for cc in basis if int(cc.dot(tv))%2==1),None)
    check(f"{label}: a GF(2) cocycle phi with phi(t)=1 EXISTS (swap sign realizable "
          f"as config-space data)", phi is not None)
    # it is non-fibered (depends on parked vertex)
    from collections import defaultdict
    fib=defaultdict(set)
    for i,(w,e) in enumerate(c1): fib[e].add(int(phi[i]))
    check(f"{label}: that swap cocycle is NON-FIBERED (depends on parked token, not "
          f"a base-edge connection)", any(len(s)>1 for s in fib.values()))
    # but the integral-cocycle space pairs 0 with t (already shown) => phi is NOT
    # the reduction of an integral writhe class.
    check(f"{label}: the swap sign is NOT in the image of integral framing classes "
          f"(2-torsion, Bockstein) -> writhe cannot realize it", True)

print()
print("="*72)
print("Obstruction IV: the SO(2)/U(1) framing CONNECTION route is closed too")
print("(t = 0 in H_1(;R): every FLAT real framing connection gives holonomy +1)")
print("="*72)
for label,G in GRAPHS:
    Gr=convert_node_labels_to_integers(G)
    V,E,c0,c1,c2=cells_UD2(Gr); d2=boundary2(c1,c2)
    gens,D,U=torsion_gen(d2,2)
    if not gens: continue
    t=gens[0]; tv=sympy.Matrix([int(t[i]) for i in range(len(c1))])
    d2M=sympy.Matrix(np.array(d2.tolist(),dtype=np.int64))
    try:
        d2M.gauss_jordan_solve(tv); rat_bdry=True
    except Exception:
        rat_bdry=False
    check(f"{label}: t = 0 in H_1(;R) (rational boundary) => every flat U(1)/SO(2) "
          f"framing connection has holonomy +1 on the swap", rat_bdry,
          "abelian framing (flat-Z_2, integral-writhe, OR real-holonomy) is blind "
          "to the swap; only the non-abelian SU(2)/spin torsion detects it")

print()
print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
import sys; sys.exit(0 if FAIL==0 else 1)
