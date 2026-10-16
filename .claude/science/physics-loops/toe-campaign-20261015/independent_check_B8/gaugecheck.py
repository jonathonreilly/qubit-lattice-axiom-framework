import itertools, numpy as np
exec(open('setup.py').read().split("Pz, Px = perm(Rz), perm(Rx)")[0])
Pz,Px=perm(Rz),perm(Rx)
good=[]
for sz in itertools.product([1,-1],repeat=8):
    Dz=np.diag(sz)@Pz
    if not np.array_equal(np.linalg.matrix_power(Dz,4),-np.eye(8,dtype=int)): continue
    for sx in itertools.product([1,-1],repeat=8):
        Dx=np.diag(sx)@Px
        if not np.array_equal(np.linalg.matrix_power(Dx,4),-np.eye(8,dtype=int)): continue
        G=gen_group([(Rz,Dz),(Rx,Dx)])
        if G is not None and len(G)==48: good.append((Dz,Dx))
Dz0,Dx0=good[0]
Ss=[np.diag(s) for s in itertools.product([1,-1],repeat=8)]
neq=0
for Dz,Dx in good:
    ok=any(np.array_equal(Dz,e*S@Dz0@S) and np.array_equal(Dx,e*S@Dx0@S) for S in Ss for e in (1,-1))
    neq+= not ok
print(len(good),"reps; not gauge(+character) equivalent to first:",neq)
def gset(Dz,Dx):
    return frozenset(D.tobytes() for R,D in gen_group([(Rz,Dz),(Rx,Dx)]))
groups={}
for Dz,Dx in good: groups.setdefault(gset(Dz,Dx),(Dz,Dx))
print("distinct groups:",len(groups))
reps=list(groups.items())
g0=reps[0][0]
cls=[]
for g,(Dz,Dx) in reps:
    found=None
    for k,h in enumerate(cls):
        for S in Ss:
            if frozenset((S@np.frombuffer(b,dtype=int).reshape(8,8)@S).tobytes() for b in g)==h: found=k;break
        if found is not None: break
    if found is None: cls.append(g)
print("gauge classes of groups:",len(cls))
# representative generators for each class, and test inversion relation
rep_of=[]
for h in cls:
    for g,(Dz,Dx) in reps:
        if g==h: rep_of.append((Dz,Dx)); break
for i,(Dz,Dx) in enumerate(rep_of): print("class",i,"sz",[int(Dz[cidx[act_corner(Rz,v)],cidx[v]]) for v in corners],"sx",[int(Dx[cidx[act_corner(Rx,v)],cidx[v]]) for v in corners])
Pinv=np.zeros((8,8),dtype=int)
for v in corners: Pinv[cidx[tuple(1-a for a in v)],cidx[v]]=1
h1=cls[1]
ok=False
for S in Ss:
    T=S@Pinv
    if frozenset((T@np.frombuffer(b,dtype=int).reshape(8,8)@T.T).tobytes() for b in cls[0])==h1: ok=True;break
print("class1 = signed-inversion conjugate of class0:",ok)
okc=False
G0=[np.frombuffer(b,dtype=int).reshape(8,8) for b in cls[0]]
for s in itertools.product([1,1j],repeat=8):
    S=np.diag(s)
    imgs=[S@D@np.conj(S) for D in G0]
    if all(np.allclose(M.imag,0) for M in imgs):
        if frozenset(np.rint(M.real).astype(int).tobytes() for M in imgs)==cls[1]: okc=True;print("phase gauge",s);break
print("class1 = complex-phase gauge of class0:",okc)
for i,(Dz,Dx) in enumerate(rep_of):
    print("class",i,"setup-convention sz",list(np.diag(Dz@Pz.T).astype(int)),"sx",list(np.diag(Dx@Px.T).astype(int)))
