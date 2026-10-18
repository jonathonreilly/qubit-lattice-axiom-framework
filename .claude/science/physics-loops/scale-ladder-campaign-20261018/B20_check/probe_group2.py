from chklib import *
B=ONSITE_BASIS
comm=max(np.abs(a@b-b@a).max() for a in B for b in B); print('onsite algebra commutative?',comm)
# minimal projectors: joint eigenspaces of a generic element
X=sum(np.random.default_rng(0).normal()*(b+b.conj().T) for b in B); w,V=np.linalg.eigh(X)
print('generic onsite hermitian eigenvalues', np.round(w,4))
# little group at k*: rotation x translation products; collect 12x12 reps
reps=[]
for P,s in rots:
    for Pt,st in trans:
        kk,U=op_bloch(P,s,kst)
        # compose with translation: (Pt,st) after rotation -- just use separately (translations are phases at k*)
    reps.append(U if False else op_bloch(P,s,kst)[1])
for Pt,st in trans: reps.append(op_bloch(Pt,st,kst)[1])
# group closure to be safe
G=[np.eye(12,dtype=complex)]
def known(M): return any(np.allclose(M,g) for g in G)
frontier=list(reps)
for g in reps:
    if not known(g): G.append(g)
changed=True
while changed:
    changed=False
    for a in list(G):
        for b in reps:
            c=a@b
            if not known(c): G.append(c); changed=True
print('group order (as matrices at k*)',len(G))
# commutant dimension
A=np.array([np.kron(g,np.eye(12))-np.kron(np.eye(12),g.T) for g in G]).reshape(-1,144)
sv=np.linalg.svd(A,compute_uv=False); print('commutant dim',np.sum(sv<1e-8))
# character norm
chi=np.array([np.trace(g) for g in G]); print('sum |chi|^2/|G| =',np.sum(np.abs(chi)**2)/len(G))
# scalars? projective phases: centre
