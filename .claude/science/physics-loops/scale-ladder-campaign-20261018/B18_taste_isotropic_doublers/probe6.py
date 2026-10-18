exec(open('b18lib.py').read())
# planar decomposition check and S^2 R_L words
S2=lambda k: SK(k)@SK(k)
W=lambda k: S2(k)@RL(k)
print("S2 R_L levels at k*:",[(round(E,4),m) for E,m in levels(W,kst)])
pl={p:[i for i,c in enumerate(C.CORNERS) if all(any(d[j]!=0 for d in c) for j in p)] for p in ((0,1),(0,2),(1,2))}
print(pl)
k=np.array([0.3,-0.4,0.9]); 
for p,idx in pl.items():
    o=[i for i in range(12) if i not in idx]
    Wk=W(k); blockdiag=np.allclose(Wk[np.ix_(idx,o)],0)
    nrm=[j for j in range(3) if j not in p][0]
    k2=k.copy(); k2[nrm]+=1.234
    print(p,"block-diagonal",blockdiag,"block independent of normal momentum",np.allclose(W(k)[np.ix_(idx,idx)],W(k2)[np.ix_(idx,idx)]))
