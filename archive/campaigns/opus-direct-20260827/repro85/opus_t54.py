"""T54 - DOES THE FRAMEWORK'S OWN VOLUME SELECTOR PICK THE COMPLEX'S DUAL?
Result 1 says: Clifford closure holds iff ALL exterior degree weights are equal
-- one density times the honest induced metric on every degree.  On a cell
complex the degree-k inner product weight is  star_k = |sigma*| / |sigma|  (dual
cell over primal cell), because a k-cochain integrates over sigma.  The "volume"
carried by degree k is then the DIAMOND  |sigma| * |sigma*|.  So Result 1's
uniform-weight condition becomes, concretely:

     sum over 0-cells of |v||v*|  =  sum over 1-cells (1/2)|e||e*|
                                  =  sum over 2-cells |f||f*|   =  total area

i.e. every degree must account for the whole manifold once.  That is a real
condition on the complex, and it is NOT automatic -- it depends on which dual is
used.  Circumcentric (Voronoi) duals tile; barycentric duals do not.

Note the operator used through Results 25-27 was the standard MIXED one: a
BARYCENTRIC vertex area (A/3 per corner) with CIRCUMCENTRIC cotan edge weights.
So there is an inconsistency sitting inside my own construction, and Result 1
says which way to resolve it.  Tested here:
  (S1) which dual satisfies the degree-uniformity condition;
  (S2) whether the operator's quality tracks it -- convergence to l(l+1) on the
       sphere, and the exactness of McKean-Singer."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def circumcentre(p0,p1,p2):
    a=p1-p0; b=p2-p0; n=np.cross(a,b); n2=float(np.dot(n,n))
    if n2<1e-30: return (p0+p1+p2)/3.0
    return p0 + (np.cross(float(np.dot(b,b))*a - float(np.dot(a,a))*b, n))/(2*n2)
def build_dual(V,F,kind):
    """returns star0 (vertex dual areas), star1 (edge dual/primal ratios),
       star2 (1/face area), and the per-degree diamond totals"""
    E={}
    for f in F:
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])):
            E.setdefault((min(a,b),max(a,b)),len(E))
    nv,ne,nf=len(V),len(E),len(F)
    star0=np.zeros(nv); star1=np.zeros(ne); star2=np.zeros(nf)
    dia0=np.zeros(nv); dia1=np.zeros(ne); dia2=np.zeros(nf)
    for k,f in enumerate(F):
        p=[V[f[0]],V[f[1]],V[f[2]]]
        A=0.5*float(np.linalg.norm(np.cross(p[1]-p[0],p[2]-p[0])))
        star2[k]=1.0/A; dia2[k]=A
        cc = circumcentre(*p) if kind=="circumcentric" else (p[0]+p[1]+p[2])/3.0
        for (i,j,o) in ((0,1,2),(1,2,0),(2,0,1)):
            e=E[(min(f[i],f[j]),max(f[i],f[j]))]
            mid=(p[i]+p[j])/2.0
            dstar=float(np.linalg.norm(cc-mid))              # half the dual edge
            lprim=float(np.linalg.norm(p[j]-p[i]))
            star1[e]+=dstar/lprim
            dia1[e]+=0.5*lprim*dstar
            # the vertex dual area contributed by this corner
            tri=0.5*float(np.linalg.norm(np.cross(mid-p[i], cc-p[i])))
            mid2=(p[i]+p[o])/2.0
            tri+=0.5*float(np.linalg.norm(np.cross(mid2-p[i], cc-p[i])))
            star0[f[i]]+=tri
    for k,f in enumerate(F):
        p=[V[f[0]],V[f[1]],V[f[2]]]
        A=0.5*float(np.linalg.norm(np.cross(p[1]-p[0],p[2]-p[0])))
        for i in f: dia0[i]+=0.0
    dia0=star0.copy()
    return star0,star1,star2,float(dia0.sum()),float(dia1.sum()),float(dia2.sum()),E
def bary_star0(V,F):
    s=np.zeros(len(V))
    for f in F:
        p=[V[f[0]],V[f[1]],V[f[2]]]
        A=0.5*float(np.linalg.norm(np.cross(p[1]-p[0],p[2]-p[0])))
        for i in f: s[i]+=A/3.0
    return s
def incidence(V,F,E):
    nv,ne,nf=len(V),len(E),len(F)
    d0=np.zeros((ne,nv)); d1=np.zeros((nf,ne))
    for (a,b),e in E.items(): d0[e,b]=1.0; d0[e,a]=-1.0
    for k,f in enumerate(F):
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])):
            d1[k,E[(min(a,b),max(a,b))]] = 1.0 if a<b else -1.0
    return d0,d1
def analyse(V,F,label,star0,star1,star2,E):
    d0,d1=incidence(V,F,E)
    if np.any(star1<=1e-12) or np.any(star0<=1e-12):
        print(f"     {label:26s} degenerate weights"); return
    A0=np.diag(np.sqrt(star1))@d0@np.diag(1.0/np.sqrt(star0))
    A1=np.diag(np.sqrt(star2))@d1@np.diag(1.0/np.sqrt(star1))
    e0=np.sort(np.clip(np.linalg.eigvalsh(A0.T@A0),0,None))
    e1=np.clip(np.linalg.eigvalsh(A0@A0.T+A1.T@A1),0,None)
    e2=np.clip(np.linalg.eigvalsh(A1@A1.T),0,None)
    nz=e0[e0>1e-9]
    l1=float(np.mean(nz[:3])); l2=float(np.mean(nz[3:8])); l3=float(np.mean(nz[8:15]))
    ms=[float(np.sum(np.exp(-t*e0))-np.sum(np.exp(-t*e1))+np.sum(np.exp(-t*e2))) for t in (0.1,1.0)]
    print(f"     {label:26s} l=1: {l1:.6f} (want 2)   l=2: {l2:.6f} (want 6)   "
          f"l=3: {l3:.6f} (want 12)   MK-S: {ms[0]:+.5f} {ms[1]:+.5f}", flush=True)
print("T54  (S1) does each DEGREE account for the whole manifold once?")
print("     Result 1's uniform-weight condition, read on a complex.")
print()
for k in (2,3):
    V,F=icosphere(k)
    print(f"  icosphere sub={k}  ({len(V)} verts)   polyhedral area = "
          f"{sum(0.5*float(np.linalg.norm(np.cross(V[f[1]]-V[f[0]],V[f[2]]-V[f[0]]))) for f in F):.6f}")
    for kind in ("circumcentric","barycentric"):
        s0,s1,s2,t0,t1,t2,E=build_dual(V,F,kind)
        print(f"     {kind:15s} degree totals:  0-cells {t0:.6f}   1-cells {t1:.6f}   2-cells {t2:.6f}"
              f"    spread {max(t0,t1,t2)-min(t0,t1,t2):.3e}", flush=True)
print()
print("T54  (S2) does the operator's quality track the condition?")
for k in (2,3,4):
    V,F=icosphere(k)
    print(f"  icosphere sub={k} ({len(V)} verts)")
    sc0,sc1,sc2,_,_,_,E=build_dual(V,F,"circumcentric")
    sb0,sb1,sb2,_,_,_,E2=build_dual(V,F,"barycentric")
    analyse(V,F,"circumcentric (uniform)",sc0,sc1,sc2,E)
    analyse(V,F,"barycentric",sb0,sb1,sb2,E2)
    analyse(V,F,"MIXED (used in R25-R27)",bary_star0(V,F),sc1,sc2,E)
