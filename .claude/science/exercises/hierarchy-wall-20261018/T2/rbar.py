"""M1 leading irrelevant exponent: R at fixed xi/L = Z (Z chosen inside the data range, not a literature value).
Rbar(L) = R* + c L^-omega. Points at different L are independent runs, so chi2 is meaningful. Compare omega free vs fixed 0.2."""
import numpy as np, sys
from scipy.optimize import brentq, curve_fit
from fss import load, Obs, NJ
D=load(); O={L:Obs(L,*D[L]) for L in sorted(D)}
for Z in (0.565,0.570,0.575):
    rows=[]
    for L in sorted(O):
        o=O[L]
        def rb(m):
            w=max(0.0012,0.004*(16/L)**1.4); b=brentq(lambda b:o.q(b,m)[1]-Z,o.b0-w,o.b0+w); return o.q(b,m)[0], b
        f,b=rb(None); jk=np.array([rb(o.blk!=j)[0] for j in range(NJ)])
        e=np.sqrt((NJ-1)/NJ*((jk-jk.mean())**2).sum()); rows.append((L,f,e,b))
    rows=np.array(rows); print(f'Z={Z}: '+'  '.join(f'L{int(L)}:{r:.4f}({e:.4f})@{b:.5f}' for L,r,e,b in rows))
    for Lmin in (8,12,16):
        s=rows[rows[:,0]>=Lmin]; L,y,e=s[:,0],s[:,1],s[:,2]
        if len(s)<4: continue
        try:
            p,cv=curve_fit(lambda L,a,c,w:a+c*L**(-w),L,y,p0=[1.14,0.05,0.8],sigma=e,absolute_sigma=True,maxfev=20000)
            c2=(((p[0]+p[1]*L**(-p[2]))-y)/e)**2; c2=c2.sum(); pe=np.sqrt(np.diag(cv))
        except Exception as ex: p=[np.nan]*3; pe=p; c2=np.nan
        q,cq=curve_fit(lambda L,a,c:a+c*L**(-0.2),L,y,p0=[1.1,0.05],sigma=e,absolute_sigma=True)
        c20=((((q[0]+q[1]*L**(-0.2))-y)/e)**2).sum()
        q2,_=curve_fit(lambda L,a:a+0*L,L,y,p0=[1.14],sigma=e,absolute_sigma=True); c2c=(((q2[0]-y)/e)**2).sum()
        print(f'   Lmin={Lmin} n={len(s)}: free: R*={p[0]:.4f}({pe[0]:.4f}) omega={p[2]:.3f}({pe[2]:.3f}) chi2={c2:.2f}/{len(s)-3};  omega=0.2: R*={q[0]:.4f} chi2={c20:.2f}/{len(s)-2};  constant: chi2={c2c:.2f}/{len(s)-1}')
