"""M2: Swendsen linearised MCRG. T = C(n+1,n+1)^-1 C(n+1,n), y = ln(lambda)/ln 2. Jackknife (20 bins)."""
import numpy as np, sys
NJ=20
EVEN=['nn','face','body','ax2','nn^2','plaq']; ODD=['s','s(s.h_nn)','s(s.h_face)']
def load(f,nlev):
    w=np.fromfile(f).reshape(-1,4+15*nlev); n=len(w)//NJ*NJ; w=w[:n]
    lev={}
    for l in range(1,nlev+1):
        o=w[:,4+15*(l-1):4+15*l]; lev[l]=(o[:,:6], o[:,6:15].reshape(-1,3,3))  # odd: [meas, op, comp]
    return lev,n
def Tmat(lev,n0,k,sector,mask):
    if sector=='even':
        X=lev[n0+1][0][mask][:,:k]; Y=lev[n0][0][mask][:,:k]
        X=X-X.mean(0); Y=Y-Y.mean(0); B=X.T@X; A=X.T@Y
    else:
        X=lev[n0+1][1][mask][:,:k,:]; Y=lev[n0][1][mask][:,:k,:]
        X=X-X.mean(0); Y=Y-Y.mean(0); B=np.einsum('mac,mbc->ab',X,X); A=np.einsum('mac,mbc->ab',X,Y)
    return np.linalg.solve(B,A)
def ys(T):
    lam=np.linalg.eigvals(T); lam=lam[np.argsort(-lam.real)]
    return lam, np.log(lam.astype(complex))/np.log(2)
def run(f,nlev,steps,label):
    lev,n=load(f,nlev); blk=np.arange(n)//(n//NJ)
    out=[]
    for n0 in steps:
        for sector,kmax in [('even',6),('odd',3)]:
            for k in range(1,kmax+1):
                lam,y=ys(Tmat(lev,n0,k,sector,slice(None)))
                jy=np.array([ys(Tmat(lev,n0,k,sector,blk!=j))[1] for j in range(NJ)])
                ere=np.sqrt((NJ-1)/NJ*((jy.real-jy.real.mean(0))**2).sum(0))
                eim=np.sqrt((NJ-1)/NJ*((np.abs(jy.imag)-np.abs(jy.imag).mean(0))**2).sum(0))
                ncomplex=int((np.abs(jy.imag)>1e-12).any(1).sum())
                s=' '.join(f'{v.real:+.3f}({er:.3f})'+(f'{v.imag:+.3f}i({ei:.3f})' if abs(v.imag)>1e-12 else '') for v,er,ei in zip(y,ere,eim))
                print(f'{label} step {n0}->{n0+1} (final {lev[n0+1][0].shape[0] and ""}) {sector} k={k}: y = {s}   [jk samples with complex: {ncomplex}/{NJ}]')
                out.append((label,n0,sector,k,y,ere,eim))
    return out
if __name__=='__main__':
    for spec in sys.argv[1:]:
        f,nlev,steps,label=spec.split(':'); run(f,int(nlev),[int(x) for x in steps.split(',')],label)
