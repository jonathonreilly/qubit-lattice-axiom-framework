from t8 import *
import sys
up=np.array([1,0],complex); dn=np.array([0,1],complex)
UU=np.kron(up,up); DD=np.kron(dn,dn); UD=np.kron(up,dn); DU=np.kron(dn,up)
S=(UD-DU)/np.sqrt(2); T0=(UD+DU)/np.sqrt(2)
def proj(v): return np.outer(v,v.conj())
def ray(c,ph=0.0):
    s=np.sqrt(1-c*c); return proj(c*S+np.exp(1j*ph)*s*T0)
fams={'coin-blind':np.eye(4,dtype=complex),'Ppm':proj(UU)+proj(DD),'zero-spin-plane':proj(S)+proj(T0),'S':proj(S),'t0':proj(T0),'ray1/4':ray(0.5),'ray1/2':ray(np.sqrt(.5),.3),'ray3/4':ray(np.sqrt(.75),.7)}
def clusters_of(gl,tol=1e-3):
    gl=sorted(gl,reverse=True); cl=[]
    for g in gl:
        if cl and abs(cl[-1][-1]-g)<tol: cl[-1].append(g)
        else: cl.append([g])
    return cl
def branches(M,E_lo=20.0,tol=1e-3):
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
            if o is None: row.append(None); continue
            ev=np.sort(np.linalg.eigvalsh(o['Wsum']))
            row.append((g,o['null'],ev))
        data.append((tab['E'],row))
    return data
if __name__=="__main__":
    for name in sys.argv[1:]:
        data=branches(fams[name])
        nb=len(data[0][1])
        print('==',name,'nbranches',nb,[len(r) for E,r in data][:5])
        for b in range(nb):
            gs=[];ws=[]
            for E,row in data:
                if b<len(row) and row[b] is not None:
                    gs.append(row[b][0]); ws.append(row[b][2])
            nul=len(ws[0])
            # fit each distinct eigenvalue index
            gs=np.array(gs); 
            for k in range(nul):
                if any(len(w)!=nul for w in ws): print('  branch size varies'); break
                y=np.array([w[k] for w in ws])
                X=np.vstack([np.ones_like(gs),1/gs**2,1/gs**4]).T
                coef,res,_,_=np.linalg.lstsq(X,y,rcond=None)
                print(f'  branch {b} null={nul} eig#{k}: W2={coef[0]:.6f} W4={coef[1]:.5f} W6={coef[2]:.2f} (n={len(y)}, g in [{gs.min():.1f},{gs.max():.1f}])')
