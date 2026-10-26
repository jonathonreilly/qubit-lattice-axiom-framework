from t22 import *
import sys
def sector_eigs(o):
    Nn=o['nullvecs']; X=Nn.conj().T@PEX@Nn; X=(X+X.conj().T)/2
    w,U=np.linalg.eigh(X)
    out=[]
    for s in (-1,1):
        idx=np.where(np.abs(w-s)<1e-3)[0]
        if len(idx)==0: continue
        Us=U[:,idx]
        ev=np.linalg.eigvalsh(Us.conj().T@o['Wsum']@Us)
        out.append((s,ev))
    return out
def fit_branches(M,E_lo=25.0,tol=1e-3):
    Mall=build_M_all(M)
    M24=np.zeros((24,24),complex)
    for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
    data=[]
    for tab in tabs:
        if tab['E']<E_lo: continue
        gl=levels_tab(tab,M24,tauTol=1e-14)
        row=[]
        for cl in clusters_of(gl,tol):
            g=float(np.mean(cl))
            o=weights_tab(tab,g,M24,tolN=5*tol)
            se=sector_eigs(o)
            row.append((g,se))
        data.append(row)
    nb=len(data[0])
    out=[]
    for b in range(nb):
        for si,s in enumerate((-1,1)):
            if not any(x[0]==s for x in data[0][b][1]): continue
            gs=np.array([row[b][0] for row in data])
            ev=np.array([[x[1] for x in row[b][1] if x[0]==s][0] for row in data])  # (nE, k)
            for k in range(ev.shape[1]):
                y=ev[:,k]; X=np.vstack([np.ones_like(gs),1/gs**2,1/gs**4]).T
                c=np.linalg.lstsq(X,y,rcond=None)[0]
                out.append(('F' if s<0 else 'B',b,k,c[0],c[1]))
    return out
if __name__=="__main__":
    for name in sys.argv[1:]:
        print('==',name)
        for s,b,k,w2,w4 in fit_branches(fams[name]): print('   %s level#%d state#%d W2=%.5f W4=%.4f'%(s,b,k,w2,w4))
