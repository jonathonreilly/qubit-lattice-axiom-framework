import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from b24base import *
B=ONSITE_BASIS; print(len(B))
fcI=fc.astype(int); Z=[np.diag(np.where(fcI[:,i]!=0,-1.,1.)) for i in range(3)]; Y=np.diag((-1.)**(fcI.sum(1)//2))
J=np.zeros((12,12));
for a in range(12):
    for b in range(12):
        if np.all(fcI[a]==-fcI[b]): J[a,b]=1
def proj_sub(cond):
    # subspace of span(B) satisfying linear cond(X)=0
    A=np.array([np.concatenate([cond(b).ravel().real,cond(b).ravel().imag]) for b in B]).T
    u,s,vh=np.linalg.svd(A); null=vh[np.sum(s>1e-9):]
    return [sum(c*b for c,b in zip(n,B)) for n in null]
cz=proj_sub(lambda X: sum(np.abs(Zi@X-X@Zi) for Zi in Z)+0j)
print('dim comm Z', len(proj_sub(lambda X: np.concatenate([Zi@X-X@Zi for Zi in Z]))))
czy=proj_sub(lambda X: np.concatenate([Zi@X-X@Zi for Zi in Z]+[Y@X-X@Y]))
print('dim comm Z,Y', len(czy))
print('J support pattern in algebra?', np.linalg.matrix_rank(np.array([b.ravel() for b in B]+[J.ravel()]))==len(B))
# which on-site symmetric elements have J-like (antipodal) support
print('sym algebra element supports (corner pairs relation):')
for b in B:
    nz=np.argwhere(np.abs(b)>1e-9); rel=set()
    for a,c in nz: rel.add(tuple(np.abs(fcI[a]-fcI[c])) if True else 0)
    print(sorted(rel))
print('Hon eig', np.round(np.linalg.eigvalsh(Hon0),4)); print('Lam eig', np.round(np.linalg.eigvalsh(Lam),4))
L202=onL(2,0,2); print('L202 commutes Z', all(np.allclose(Zi@L202,L202@Zi) for Zi in Z))
print('PC entries commuting with all Z:', [n for n,M in PC.items() if all(np.allclose(Zi@M,M@Zi) for Zi in Z)])
print('PC entries anticommuting with Y up to phase / commuting:', [n for n,M in PC.items() if np.allclose(Y@M@Y,M)], [n for n,M in PC.items() if np.allclose(Y@M@Y,-M)])
print('P6 plane-diag count', sum(1 for n,M in P6.items() if all(np.allclose(Zi@M,M@Zi) for Zi in Z)))
# PLm projector structure
for i,P in enumerate(PLm): print('PLm',i,'rank',round(np.trace(P).real), 'commZ', all(np.allclose(Zi@P,P@Zi) for Zi in Z))
for i,P in enumerate(PH): print('PH',i,'rank',round(np.trace(P).real), 'commZ', all(np.allclose(Zi@P,P@Zi) for Zi in Z))
