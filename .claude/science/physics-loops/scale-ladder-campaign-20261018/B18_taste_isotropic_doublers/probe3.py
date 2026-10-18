exec(open('b18lib.py').read())
def orth(vecs):
    if not vecs: return []
    M=np.array([v.reshape(-1) for v in vecs]).T; U,s,_=np.linalg.svd(M,full_matrices=False); U=U[:,s>1e-9]
    return [U[:,i].reshape(12,12) for i in range(U.shape[1])]
def comm_basis(ops):  # on-site V with V A = w_A A V for each (A,w_A)
    B=None
    rows=[]
    I=np.eye(12)
    for A,w in ops: rows.append(np.kron(A.T,I)-w*np.kron(I,A))
    M=np.vstack(rows); _,s,Vh=np.linalg.svd(M); s=np.concatenate([s,np.zeros(144-len(s))])
    return [v.conj().reshape(12,12,order='F') for v in Vh[s<1e-9]]
# NB: reshape with order F matches kron convention; test
b=comm_basis([(Hon0,1)]); print("comm(H_on) dim",len(b), all(np.allclose(x@Hon0,Hon0@x) for x in b))
sets={"H_on":[(Hon0,1)],"Lam(+)":[(Lam,1)],"Lam(-)":[(Lam,-1)],"H_on,Lam(+)":[(Hon0,1),(Lam,1)],"H_on,Lam(-)":[(Hon0,1),(Lam,-1)]}
for i,P in enumerate(Ps): sets[f"P{i}"]=[(P,1)]
for i,Q in enumerate(Qs): sets[f"Q{i}"]=[(Q,1)]
sets["UH23"]=[(UH,1)]; sets["UL110"]=[(UL,1)]; sets["UH23,UL110"]=[(UH,1),(UL,1)]
# O-symmetric on-site algebra = commutant of the site-rotation PSG rep at a site
loc_reps=[]
for P,s_ in rots:
    Mx=np.zeros((nV,nV)); Mx[P,np.arange(nV)]=(-1.0)**s_; loc_reps.append(Mx[np.ix_(loc0,loc0)])
Osym=comm_basis([(R,1) for R in loc_reps]); print("O-symmetric on-site algebra dim",len(Osym))
for e in (EX[0],np.ones(3)):
    for wL in (1,-1):
        tgt=shifted(blli,e,wL)
        for nm,ops in sets.items():
            bas=comm_basis(ops)
            for r in (0,1):
                B,_=intertwiners(blli,tgt,r=r,basis=bas)
                print(f"e={e.astype(int)} wL={wL:+d} {nm:12s} r={r}: dim {len(B):3d} generic sigma_min {generic_invertible(B):.3f}",flush=True)
