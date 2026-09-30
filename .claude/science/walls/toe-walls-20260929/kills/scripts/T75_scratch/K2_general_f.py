"""Kill-round test: 1D stopped half-line, general weight-one bond energy sqrt(w_x w_y) f(u_x-u_y).
Stationarity at x: sum_y exp(-d_y/2)[f(d_y)/2 + f'(d_y)] = 0, d_y = u_x-u_y.
Dirichlet u_0 = ln(eps), u_N = 0.  Local exponent p(n)."""
import numpy as np
from scipy.optimize import root
fs = {
 "d^2 (f2>0)":   (lambda d: d**2,               lambda d: 2*d),
 "F1 4sinh^2(d/4)": (lambda d: 2*np.cosh(d/2)-2, lambda d: np.sinh(d/2)),
 "F2 2sinh^2(d/2)/cosh(d/2)": (lambda d: 2*np.sinh(d/2)**2/np.cosh(d/2), lambda d: 2*np.sinh(d/2)*(1+ 1/np.cosh(d/2)**2 - 0)*0.5*1 if False else (np.sinh(d/2)*(2+ (np.sinh(d/2)**2)/np.cosh(d/2)**2 *0 ) )),
 "d^4 (f2=0)":   (lambda d: d**4,               lambda d: 4*d**3),
 "d^2+d^4":      (lambda d: d**2+d**4,          lambda d: 2*d+4*d**3),
 "d^6 (f2=f4=0)":(lambda d: d**6,               lambda d: 6*d**5),
}
# F2 derivative done properly via numeric
def fprime_num(f):
    h=1e-6
    return lambda d:(f(d+h)-f(d-h))/(2*h)
def run(name,f,fp,N=400,eps=1e-9,guess="sq"):
    n=np.arange(N+1,dtype=float)
    def resid(u):
        U=np.empty(N+1);U[0]=np.log(eps);U[N]=0;U[1:N]=u
        x=U[1:N];r=0
        for y in (U[:N-1],U[2:]):
            d=x-y
            r=r+np.exp(-d/2)*(f(d)/2+fp(d))
        return r
    p=2.0 if guess=="sq" else 1.0
    u0=p*np.log(np.maximum(n[1:N]/N,1e-6))
    sol=root(resid,u0,method="hybr",tol=1e-13,options={"maxfev":200000})
    U=np.empty(N+1);U[0]=np.log(eps);U[N]=0;U[1:N]=sol.x
    return U,sol.success,np.max(np.abs(resid(sol.x)))
ns=[2,3,5,10,20,40,80]
for name,(f,fp) in fs.items():
    if name.startswith("F2"): fp=fprime_num(f)
    for guess in ("sq","lin"):
        U,ok,r=run(name if False else name,f,fp,guess=guess)
        p=[(U[n+1]-U[n-1])/(np.log(n+1)-np.log(n-1)) for n in ns]
        print(f"{name:28s} start={guess:3s} ok={ok!s:5s} res={r:8.1e} p(n)="+" ".join(f"{x:6.3f}" for x in p))
