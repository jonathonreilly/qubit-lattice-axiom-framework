exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
GROUP=[]
for Pr,sr in rots:
    for Pt,st in trans:
        GROUP.append((Pt[Pr], sr ^ st[Pr]))   # translation after rotation
def sym_pair(i,j,amp):
    T=np.zeros((nV,nV),complex)
    for P,s in GROUP:
        a=amp*(-1.0)**(int(s[i])+int(s[j]))
        T[P[i],P[j]]+=a; T[P[j],P[i]]+=np.conj(a)
    return T
DIRS6=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
targets=[C.VID[((0,0,0),c)] for c in C.CORNERS]+[C.VID[(tuple(x%L for x in d),c)] for d in DIRS6 for c in C.CORNERS]
terms=[]
for i in loc0[:1]:   # all corners equivalent under O? use orbits from corner 0 and also all corners for safety
    pass
seen=[]
for i in loc0:
  for j in targets:
    if i==j: continue
    for kind in ('re','im'):
        T=sym_pair(j,i,1.0 if kind=='re' else 1j)
        if np.abs(T).max()<1e-9: continue
        T=T/np.abs(T).max()
        dup=any(np.allclose(T,S) or np.allclose(T,-S) for S,_ in seen)
        if not dup: seen.append((T,(kind,C.VERTS[i],C.VERTS[j])))
print(len(seen),"distinct symmetric orbit terms")
# E1/2/E5/2 doublets at k*: from a generic symmetric on-site+link Hermitian
G=Hk(blon,kst)+0.37*Lam+0.23*Hk(blli,kst)
w,V=np.linalg.eigh(G); dbl=[]
i=0
while i<12:
    j=i
    while j+1<12 and w[j+1]-w[i]<1e-8: j+=1
    if j-i+1==2: dbl.append(V[:,i:j+1])
    i=j+1
print("doublets at k*:",len(dbl))
for T,lab in seen:
    bl=blocks_from(T); h=1e-6
    dT=[(Hk(bl,kst+h*e)-Hk(bl,kst-h*e))/(2*h) for e in np.eye(3)]
    vel=[max(np.linalg.norm(Psi.conj().T@d@Psi - np.trace(Psi.conj().T@d@Psi)/2*np.eye(2)) for d in dT) for Psi in dbl]
    T2=T@T; sq=np.allclose(T2,T2[0,0]*np.eye(nV)) if abs(T2[0,0])>1e-9 else False
    onsite=all(C.VERTS[a][0]==C.VERTS[b][0] for a,b in zip(*np.nonzero(np.abs(T)>1e-9)))
    print(lab[0], "onsite" if onsite else "link  ", "doublet velocities", np.round(vel,4), "T^2 prop I:", sq, (np.round(T2[0,0].real,3) if sq else ""), lab[1][1], "->", lab[2])
