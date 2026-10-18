"""M1 corrections-to-scaling: joint fit of Q(beta,L) = Q* + a1 t L^yt + a2 (t L^yt)^2 + c L^-omega, t = beta - beta_c, Q in {R, xi/L},
over reweighted points in a window around beta_c. Jackknife (20 bins) for errors. Also fit with omega fixed at 0.2 to test the 0.2 boundary."""
import numpy as np, sys
from scipy.optimize import least_squares
from fss import load, Obs, NJ
D=load(); O={L:Obs(L,*D[L]) for L in sorted(D)}
Lmin=int(sys.argv[1]) if len(sys.argv)>1 else 8
Ls=[L for L in sorted(O) if L>=Lmin]
def pts(mask_j=None):
    X=[];Y=[]
    for L in Ls:
        o=O[L]; m=None if mask_j is None else (o.blk!=mask_j)
        w=1.5e-3*(16/L)**1.4  # window shrinks with L
        for b in np.linspace(0.5561-w,0.5561+w,7):
            q=o.q(b,m); X.append((L,b)); Y.append(q[:2])
    return np.array(X),np.array(Y)
def model(p,X,fix_om=None):
    Qs,bc,yt,a1,a2,c,om=p if fix_om is None else (*p,fix_om)
    L=X[:,0]; t=(X[:,1]-bc)*L**yt
    return Qs+a1*t+a2*t*t+c*L**(-om)
def fit(X,y,sig,fix_om=None,p0=None):
    p0=p0 if p0 is not None else ([y.mean(),0.5561,1.4,-0.5,0,0.05,0.8] if fix_om is None else [y.mean(),0.5561,1.4,-0.5,0,0.05])
    r=least_squares(lambda p:(model(p,X,fix_om)-y)/sig,p0,max_nfev=20000)
    return r.x, (r.fun**2).sum(), len(y)-len(p0)
X,Y=pts(); JK=[pts(j)[1] for j in range(NJ)]
JK=np.array(JK); SIG=np.sqrt((NJ-1)/NJ*((JK-JK.mean(0))**2).sum(0))
for k,name in [(0,'R'),(1,'xi/L')]:
    p,chi2,dof=fit(X,Y[:,k],SIG[:,k])
    pj=np.array([fit(X,JK[j][:,k],SIG[:,k],p0=p)[0] for j in range(NJ)])
    e=np.sqrt((NJ-1)/NJ*((pj-pj.mean(0))**2).sum(0))
    print(f'{name} Lmin={Lmin}: Q*={p[0]:.4f}({e[0]:.4f}) beta_c={p[1]:.6f}({e[1]:.6f}) y_t={p[2]:.3f}({e[2]:.3f}) omega={p[6]:.3f}({e[6]:.3f}) c={p[5]:.3f}  chi2/dof={chi2:.1f}/{dof} (points correlated; chi2 indicative)')
    for om in (0.2,):
        p2,chi22,dof2=fit(X,Y[:,k],SIG[:,k],fix_om=om)
        print(f'   omega fixed {om}: chi2/dof={chi22:.1f}/{dof2}  (vs free {chi2:.1f}/{dof})')
