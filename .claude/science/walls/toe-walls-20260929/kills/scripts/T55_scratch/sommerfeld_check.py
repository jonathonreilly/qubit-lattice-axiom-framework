# Independent check of the Coulomb Sommerfeld factor convention (units: m=1, hbar=c=1; reduced mass mu=1/2).
# s-wave u'' + (k^2 + 2 mu alpha/r) u = 0, k = mu*v_rel. S = |psi(0)|^2/|psi_free(0)|^2 = (k/u'(0))^2 * ... via matching to sin(kr+delta)
import numpy as np
from scipy.integrate import solve_ivp
def S_num(alpha, vrel):
    mu=0.5; k=mu*vrel
    f=lambda r,y:[y[1], -(k*k+2*mu*alpha/r)*y[0]]
    r0=1e-6; y0=[r0, 1.0]         # u ~ r near 0 with u'(0)=1
    r1=200/k+50/(mu*alpha)
    sol=solve_ivp(f,[r0,r1],y0,rtol=1e-11,atol=1e-13,dense_output=True)
    # asymptotic amplitude A: u ~ A sin(kr + phase - eta ln 2kr); use energy-like invariant A^2 = u^2 + (u'/k)^2 corrected slowly: take large r
    r=np.linspace(r1*0.9,r1,4000); u=sol.sol(r)[0]; up=sol.sol(r)[1]
    A2=np.mean(u**2+(up/k)**2)
    # free: u=sin(kr)/k with u'(0)=1 => A^2=1/k^2 ; S=|psi(0)|^2 ratio = (1/A^2)/(k^2) => S = 1/(A2*k^2)
    return 1.0/(A2*k*k)
for eta in (0.1,0.25,0.5):
    vrel=0.05; alpha=eta*vrel
    s=S_num(alpha,vrel); s2=2*np.pi*eta/(1-np.exp(-2*np.pi*eta)); s1=np.pi*eta/(1-np.exp(-np.pi*eta))
    print(f"eta=alpha/v_rel={eta}: numeric S={s:.4f}  2pi form={s2:.4f}  pi form={s1:.4f}")
