exec(open('b18lib.py').read())
def comm_basis(ops):
    I=np.eye(12); M=np.vstack([np.kron(A.T,I)-w*np.kron(I,A) for A,w in ops]); _,s,Vh=np.linalg.svd(M); s=np.concatenate([s,np.zeros(144-len(s))])
    return [v.conj().reshape(12,12,order='F') for v in Vh[s<1e-9]]
loc_reps=[]
for P,s_ in rots:
    Mx=np.zeros((nV,nV)); Mx[P,np.arange(nV)]=(-1.0)**s_; loc_reps.append(Mx[np.ix_(loc0,loc0)])
Osym=comm_basis([(R,1) for R in loc_reps]); print("Osym dim",len(Osym))
for om in (1,-1):
    B,_=intertwiners(blli,shifted(blli,EX[0],om),r=0); D=[np.diag(b[(0,0,0)]) for b in B]
    D=[d/d[np.argmax(np.abs(d))] for d in D]
    best=None
    for al in itertools.product((1,-1,1j,-1j),repeat=3):
        V=np.diag(sum(a*d for a,d in zip(al,D)))
        for wU in (1,-1,1j,-1j):
            # U in span(Osym) with V U V^-1 = wU U
            I=np.eye(12); K=np.kron(np.eye(12),V)@np.kron(np.conj(V),I)  # unused
            A=np.array([ (V@b@np.linalg.inv(V)-wU*b).reshape(-1) for b in Osym]).T
            _,s,Vh=np.linalg.svd(A); s=np.concatenate([s,np.zeros(len(Osym)-len(s))])
            dim=int(np.sum(s<1e-9))
            if dim and (best is None or dim>best[0]): best=(dim,al,wU)
            if dim: print("omega_L",om,"alpha",al,"omega_U",wU,"dim of O-symmetric on-site ops taste-covariant:",dim)
    print("omega_L",om,"best",best)
