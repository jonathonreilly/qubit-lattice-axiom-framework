"""T75 - WHAT MATTER DOES THE FRAMEWORK'S RULE ACTUALLY CARRY?
A different thread, and one the campaign has never touched: the rule's MATTER
CONTENT.  In the continuum the Kahler-Dirac operator in d=4 is equivalent to
FOUR degenerate Dirac fermions -- its 2^4 = 16 components are 4 flavours x 4
spinor components.  That is a prediction-shaped statement about what the
framework contains.

But Results 25 and 30 showed the COMPLEX-native operator is DOUBLER-FREE (kernel
= Betti sum exactly, 16 on T^4 rather than 16 doublers per mode).  Doubler-free
and single-flavour together would violate Nielsen-Ninomiya, so the flavours must
still be there in some form.  Which is it, and where do they sit?

Test on the flat 4-torus, where the exact answer is known: the Hodge-de Rham
spectrum on k-forms is |2 pi n|^2 with multiplicity C(4,k) per momentum, so at
each momentum level the 16 cochain components split as 1,4,6,4,1 across degrees.
If the operator is 4 Dirac flavours, every level's multiplicity must be
divisible by 4, and the DEGREE profile at each level must be exactly 1:4:6:4:1."""
import numpy as np, itertools, math
L=3; d=4; h=1.0/L
verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
tops=[]
for base in verts:
    for perm in itertools.permutations(range(d)):
        ids=[vid[base]]; cur=list(base)
        for a in perm:
            cur=list(cur); cur[a]=(cur[a]+1)%L; ids.append(vid[tuple(cur)])
        tops.append(tuple(ids))
cells=[dict() for _ in range(5)]
for t in tops:
    for k in range(5):
        for f in itertools.combinations(sorted(t),k+1):
            cells[k].setdefault(f,len(cells[k]))
print(f"T75  flat 4-torus L={L}: cells by degree {[len(c) for c in cells]}")
print(f"     ratio to the vertex count: {[len(c)/len(cells[0]) for c in cells]}")
print(f"     continuum Kahler-Dirac fibre in d=4 is C(4,k) = [1, 4, 6, 4, 1], total 16")
print()
def cob(k):
    lo,hi=cells[k],cells[k+1]; D=np.zeros((len(hi),len(lo)))
    for f,j in hi.items():
        for i_ in range(len(f)):
            face=f[:i_]+f[i_+1:]
            if face in lo: D[j,lo[face]]+=(-1)**i_
    return D
Ds=[cob(k) for k in range(4)]
print("   degree-by-degree Hodge Laplacian spectra (unweighted combinatorial):")
print(f"   {'degree':>7} {'dim':>7} {'zero modes':>12} {'first level':>14} {'multiplicity':>13}")
for k in range(5):
    L_k=np.zeros((len(cells[k]),len(cells[k])))
    if k<4: L_k=L_k+Ds[k].T@Ds[k]
    if k>=1: L_k=L_k+Ds[k-1]@Ds[k-1].T
    e=np.sort(np.clip(np.linalg.eigvalsh(L_k),0,None))
    nz=e[e>1e-8]
    g=[z for z in nz if abs(z-nz[0])<1e-6*max(1,nz[0])] if len(nz) else []
    print(f"   {k:7d} {len(cells[k]):7d} {int(np.sum(e<1e-8)):12d} "
          f"{(nz[0] if len(nz) else float('nan')):14.6f} {len(g):13d}", flush=True)
print()
print("   zero modes by degree should be the Betti numbers [1,4,6,4,1];")
print("   if the FIRST LEVEL multiplicities are also in the ratio 1:4:6:4:1 then the")
print("   16 components organise as the continuum Kahler-Dirac fibre -- i.e. the")
print("   framework's rule carries FOUR Dirac flavours in four dimensions.")
