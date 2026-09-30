import numpy as np, scipy.sparse as sp, itertools
exec(open('indep_census.py').read().split("print(\"\\nFull decomposition")[0].replace('print(','(lambda *a,**k:None)('))
# now C3q, C2q, Yq, N exist. lift accidental degeneracies with incommensurate weights
a,b=np.sqrt(2)/7,np.sqrt(3)/11
print("Full (C3, j(j+1), Y) census, all states, using incommensurate mixing weights")
for k in range(n+1):
    idx=np.where(N==k)[0]
    C3k=C3q[idx][:,idx].toarray(); C2k=C2q[idx][:,idx].toarray(); Yk=Yq[idx][:,idx].toarray()
    H=C3k+a*C2k+b*Yk
    w,v=np.linalg.eigh(H)
    cnt={}
    for c in range(len(idx)):
        x=v[:,c]
        key=(round(float((x.conj()@C3k@x).real),3)+0.0,round(float((x.conj()@C2k@x).real),3)+0.0,round(float((x.conj()@Yk@x).real),3)+0.0)
        cnt[key]=cnt.get(key,0)+1
    print(f" k={k} dim={len(idx)}: colour-singlets:",{kk:vv for kk,vv in cnt.items() if abs(kk[0])<1e-6}, "| n keys total",len(cnt))
    # Rank check: dimension of colour-singlet subspace via kernel of C3
    ev=np.linalg.eigvalsh(C3k); print("      dim ker C3 =",int((ev<1e-9).sum()))
