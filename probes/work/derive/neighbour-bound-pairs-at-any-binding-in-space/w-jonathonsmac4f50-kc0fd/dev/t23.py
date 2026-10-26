from t22 import *
dl=np.array([t['E']-EC for t in tabs])
def extrap(deg,dmax=0.6,dmin=0.0):
    idx=[i for i in range(len(tabs)) if dmin<=dl[i]<=dmax]
    s=np.sqrt(dl[idx])
    X=np.vander(s,deg+1,increasing=True)
    G=np.array([tabs[i]['G1'].ravel() for i in idx])
    coef,res,rk,sv=np.linalg.lstsq(X,G,rcond=None)
    return coef[0].reshape(24,24),len(idx)
Gs={}
for deg in (6,8,10):
    Gs[deg],n=extrap(deg); print(deg,n)
print('diff 8 vs 10',np.abs(Gs[8]-Gs[10]).max(),' 6 vs 8',np.abs(Gs[6]-Gs[8]).max())
Gc=Gs[10]
print('hermitian err',np.abs(Gc-Gc.conj().T).max())
# thresholds
def thresholds(M):
    Mall=build_M_all(M)
    M24=np.zeros((24,24),complex)
    for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
    R=herm_sqrt((Gc+Gc.conj().T)/2)
    T=R@M24@R
    tau,U=np.linalg.eigh((T+T.conj().T)/2)
    # classify sector by exchange on x=R v ... use PEX on Gc^{1/2}-vectors
    out=[]
    for k in range(24):
        if tau[k]>1e-8:
            v=R@U[:,k]; v/=np.linalg.norm(v)
            ex=(v.conj()@PEX@v).real
            out.append((1/tau[k],round(ex,3)))
    return sorted(out)
res={}
for name,M in fams.items():
    th=thresholds(M)
    # group
    grp=[]
    for g,ex in th:
        if grp and abs(grp[-1][0]-g)<2e-4*max(1,g): grp[-1][1]+=1; grp[-1][2].append(ex)
        else: grp.append([g,1,[ex]])
    print(name,[(round(a,4),b,round(float(np.mean(c)),2)) for a,b,c in grp])
