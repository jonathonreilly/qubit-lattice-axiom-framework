exec(open('b18lib.py').read())
def Bloch(k):
    B=np.zeros((nV,12),complex)
    for a,(v,c) in enumerate(C.VERTS): B[a,CI[c]]=np.exp(1j*np.dot(k,v))/np.sqrt(L**3)
    return B
Bst=Bloch(kst)
Rm=[]
for P,s_ in rots:
    M=np.zeros((nV,nV)); M[P,np.arange(nV)]=(-1.0)**s_; Rm.append(M)
rho=[Bst.conj().T@M@Bst for M in Rm]
print("rho unitary",all(np.allclose(r@r.conj().T,np.eye(12)) for r in rho))
B,_=intertwiners(blli,shifted(blli,EX[0],1),r=0); D=[np.diag(b[(0,0,0)]) for b in B]; D=[d/d[np.argmax(np.abs(d))] for d in D]
Bm,_=intertwiners(blli,shifted(blli,EX[0],-1),r=0); Dm=[np.diag(b[(0,0,0)]) for b in Bm]; Dm=[d/d[np.argmax(np.abs(d))] for d in Dm]
sites=np.array([v for v,c in C.VERTS]); cid=np.array([CI[c] for v,c in C.VERTS])
def analyse(vx,label):
    t=np.array([(-1.0)**v[0] for v,c in C.VERTS])*vx[cid]
    taus=[]; shifts={}
    for M in Rm:
        d=np.diag(M@np.diag(t)@M.T)
        # decompose d(v,c) = (-1)^{e.v} tau(c)
        tau=d[[C.VID[((0,0,0),c)] for c in C.CORNERS]]
        e=None
        for ee in itertools.product((0,1),repeat=3):
            if np.allclose(d,(-1.0)**(sites@np.array(ee))*tau[cid]): e=ee
        assert e is not None
        shifts.setdefault(e,[]).append(tau)
    for e,ts in shifts.items():
        for a in ts:
            for b in ts: taus.append(a*np.conj(b))
    # commutant at k* of <rho(O), diag(taus)>
    ut={tuple(np.round(x,8)):x for x in taus}; taus=list(ut.values())
    gens=rho+[np.diag(x) for x in taus]
    I=np.eye(12); A=np.vstack([np.kron(g.T,I)-np.kron(I,g) for g in gens]); w_,U_=np.linalg.eigh(A.conj().T@A)
    cb=[U_[:,j].reshape(12,12,order='F') for j in range(144) if w_[j]<1e-9]
    _cb=[v.conj().reshape(12,12,order='F') for v in []]
    r_=np.random.default_rng(0); X=sum((r_.normal()+1j*r_.normal())*b for b in cb); X=X+X.conj().T
    w=np.linalg.eigvalsh(X); mult=[]; 
    for x in w:
        if mult and abs(x-mult[-1][0])<1e-8: mult[-1][1]+=1
        else: mult.append([x,1])
    nt=len({tuple(np.round(x,6)) for x in taus})
    print(f"{label}: shift classes {sorted(shifts)}; {nt} distinct momentum-preserving on-site taus; commutant dim {len(cb)}; generic multiplicities {[m for _,m in mult]}")
analyse(D[0]+D[1]+D[2],"canonical V_x (w=+1)")
for al in [(1,1,-1),(1,-1,1),(1,1j,1),(1j,1,1),(1,1,1j)]:
    analyse(sum(a*d for a,d in zip(al,D)),f"alpha {al} (w=+1)")
analyse(Dm[0]+Dm[1]+Dm[2],"w=-1 canonical")
