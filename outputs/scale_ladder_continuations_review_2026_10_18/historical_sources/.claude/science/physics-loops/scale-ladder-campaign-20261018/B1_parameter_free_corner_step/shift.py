exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
GROUP=[]
for Pr,sr in rots:
    for Pt,st in trans: GROUP.append((Pt[Pr], sr ^ st[Pr]))
def sym_directed(i,j):   # amplitude on (j <- i)
    T=np.zeros((nV,nV))
    for P,s in GROUP:
        T[P[j],P[i]]+=(-1.0)**(int(s[i])+int(s[j]))
    return T
X,Y,Z=(1,0,0),(0,1,0),(0,0,1)
def neg(d): return tuple(-x for x in d)
c0=frozenset((X,Y)); i0=C.VID[((0,0,0),c0)]
results={}
for shiftv in ((1,1,0),(1,-1,0),(0,0,1),(1,0,0),(0,0,0)):
  for tgt in (frozenset((X,Y)),frozenset((neg(X),neg(Y))),frozenset((neg(X),Y)),frozenset((X,neg(Y))),frozenset((X,Z)),frozenset((neg(X),Z))):
    j=C.VID[(tuple(x%L for x in shiftv),tgt)]
    if j==i0: continue
    S=sym_directed(i0,j)
    if np.abs(S).max()<1e-9: print("shift",shiftv,"target",sorted(map(tuple,tgt)),": cancels (PSG-inconsistent)"); continue
    S/=np.abs(S).max()
    unit=np.allclose(S@S.T,np.eye(nV)); perm=np.all(np.isin(np.round(np.abs(S),9),[0,1]))
    comm=all(np.allclose(conj(S,P,s),S) for P,s in rots+trans[:4])
    print("shift",shiftv,"target",sorted(map(tuple,tgt)),"unitary",unit,"signed perm",perm,"symmetric",comm)
    if unit: np.save(f"S_{shiftv[0]}{shiftv[1]}{shiftv[2]}_{len(results)}.npy",S); results[(shiftv,tuple(sorted(map(tuple,tgt))))]=S
print(len(results),"unitary symmetric shift QCAs")
