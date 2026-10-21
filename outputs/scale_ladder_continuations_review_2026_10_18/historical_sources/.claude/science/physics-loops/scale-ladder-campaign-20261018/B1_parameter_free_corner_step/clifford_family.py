exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,k)
GROUP=[]
for Pr,sr in rots:
    for Pt,st in trans: GROUP.append((Pt[Pr], sr ^ st[Pr]))
def sym_directed(i,j):
    T=np.zeros((nV,nV))
    for P,s in GROUP: T[P[j],P[i]]+=(-1.0)**(int(s[i])+int(s[j]))
    return T
X,Y=(1,0,0),(0,1,0)
c0=frozenset((X,Y)); i0=C.VID[((0,0,0),c0)]
ons={}
for tgt in C.CORNERS:
    j=C.VID[((0,0,0),tgt)]
    T=sym_directed(i0,j)
    if np.abs(T).max()<1e-9: continue
    T/=np.abs(T).max()
    if np.allclose(T@T.T,np.eye(nV)): ons[tuple(sorted(map(tuple,tgt)))]=Hk(blocks_from(T),np.zeros(3)).real
print("O-equivariant on-site signed permutations:",list(ons.keys()))
base=list(ons.values())
mons=[]
for M in base:
    for p in (1,1j,-1,-1j): mons.append(p*M)
# also include the identity times phases is global phase -> skip; products of perms
words=[]
facts={"S":SK,"Si":lambda k:SK(k).conj().T,"R":RL}
import itertools as it
found=[]
for L_ in (2,3,4):
  for seq in it.product(["S","Si","R","M"],repeat=L_):
    if not any(x in ("S","Si") for x in seq): continue
    nM=seq.count("M")
    for ms in it.product(range(len(base)),repeat=nM):
      for phs in it.product((1,1j),repeat=nM):
        def W(k,seq=seq,ms=ms,phs=phs):
            M=np.eye(12,dtype=complex); c=0
            for x in seq:
                if x=="M": M=M@(phs[c]*base[ms[c]]); c+=1
                else: M=M@facts[x](k)
            return M
        lv=levels(W,kst)
        for E,m in lv:
            if m!=2: continue
            sp=[]
            for d in DIRS[:6]:
                ee=wrap(np.angle(np.linalg.eigvals(W(kst+1e-3*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05]); sp.append((ee[-1]-ee[0])/2e-3 if len(ee)==2 else np.nan)
            sp=np.array(sp)
            if np.isnan(sp).any() or sp.min()<1e-3: continue
            found.append((seq,ms,phs,round(E,4),round(sp.mean(),6),round(np.ptp(sp),8)))
print(len(found),"Weyl doublet hits in the Clifford(+T link) family")
seen=set()
for f in found:
    key=(f[0],f[4])
    if key in seen: continue
    seen.add(key); print(f)
