"""Newton with tridiagonal (analytic-ish) Jacobian: 1D stationarity for sqrt(wx wy) f(u_x-u_y), f=|d|^q.
Asymptotic expansion predicts p = q (q = 2,4,6); test with u in log variables, Dirichlet u0=ln eps, uN=0."""
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
def make(q):
    f=lambda d: np.abs(d)**q
    fp=lambda d: q*np.abs(d)**(q-1)*np.sign(d)
    return f,fp
def G(a,b,f,fp):
    d=a-b; return np.exp(-d/2)*(f(d)/2+fp(d))   # d/du_a of bond(a,b) / sqrt(..)
def resid(U,f,fp):
    x=U[1:-1]; return G(x,U[:-2],f,fp)+G(x,U[2:],f,fp)
def solve(q,N=300,eps=1e-9):
    f,fp=make(q); n=np.arange(N+1.)
    U=np.zeros(N+1); U[0]=np.log(eps)
    U[1:N]=q*np.log(n[1:N]/N)
    U[1:N]=np.maximum(U[1:N],np.log(eps))
    h=1e-6
    for it in range(400):
        r=resid(U,f,fp)
        if np.max(np.abs(r))<1e-12: break
        # jacobian tridiagonal by finite diff
        Ud=U.copy(); 
        diag=np.empty(N-1); lo=np.empty(N-2); up=np.empty(N-2)
        def rr(Uv): return resid(Uv,f,fp)
        for k,off in ((0,0),):
            pass
        Up=U.copy();Up[1:-1]+=h;Um=U.copy();Um[1:-1]-=h
        diag=(rr(Up)-rr(Um))/(2*h)
        # off diagonals: derivative of r_i wrt u_{i-1}, u_{i+1}
        x=U[1:-1]; 
        def dG_db(a,b):
            return (G(a,b+h,f,fp)-G(a,b-h,f,fp))/(2*h)
        lo=dG_db(x,U[:-2])[1:]; up=dG_db(x,U[2:])[:-1]
        J=diags([lo,diag,up],[-1,0,1],format="csc")
        dU=spsolve(J,-r)
        t=1.0
        r0=np.max(np.abs(r))
        while t>1e-4:
            Un=U.copy();Un[1:-1]+=t*dU
            if np.max(np.abs(resid(Un,f,fp)))<r0: break
            t/=2
        U=Un
    return U,np.max(np.abs(resid(U,f,fp)))
for q in (2,4,6):
    U,res=solve(q)
    ns=[3,5,10,20,40,80]
    p=[(U[n+1]-U[n-1])/(np.log(n+1)-np.log(n-1)) for n in ns]
    print("q=",q,"res",f"{res:.1e}","p(n):",np.round(p,3))
