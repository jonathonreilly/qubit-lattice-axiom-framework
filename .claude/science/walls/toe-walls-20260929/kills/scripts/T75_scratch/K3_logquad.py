import numpy as np
from scipy.optimize import root
f=lambda d:d**2; fp=lambda d:2*d
def run(N,eps):
    def resid(u):
        U=np.empty(N+1);U[0]=np.log(eps);U[N]=0;U[1:N]=u
        x=U[1:N];r=0
        for y in (U[:N-1],U[2:]):
            d=x-y; r=r+np.exp(-d/2)*(f(d)/2+fp(d))
        return r
    n=np.arange(N+1.)
    u0=np.log(eps)*(1-n[1:N]/N)
    sol=root(resid,u0,method="hybr",tol=1e-13,options={"maxfev":10**6})
    U=np.empty(N+1);U[0]=np.log(eps);U[N]=0;U[1:N]=sol.x
    return U,sol.success,np.max(np.abs(resid(sol.x)))
for N,eps in ((400,1e-3),(400,1e-1),(2000,1e-3),(4000,1e-9)):
    U,ok,r=run(N,eps)
    ns=[2,5,10,20,50,100,200,400]
    ns=[n for n in ns if n<N-1]
    p=[(U[n+1]-U[n-1])/(np.log(n+1)-np.log(n-1)) for n in ns]
    print(N,eps,ok,f"{r:.1e}","p(n):",dict(zip(ns,np.round(p,3))))
