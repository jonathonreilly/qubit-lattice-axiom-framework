"""Separable (Laplace/Gamma) evaluators for mu_E and Xi: exact rewriting of the 3D zone means via
eps^{-s} = Gamma(s/2)^{-1} int_0^inf t^{s/2-1} e^{-t eps^2} dt, with 1D zone means on a fine periodic grid.
  mu_E = (1/12) Gamma(3/2)^{-1} int dt t^{1/2} e^{-t m^2} [3 F2^2 E0 - F4 E0^2]
  Xi_v = (1/32) int dt e^{-t m^2} T_v(t) [5 F2 t^{5/2}/Gamma(7/2) - E0 t^{3/2}/Gamma(5/2)]
  T: M,T2g 4 G1^2 ; M,Eg 2 G2 E0 - 2 G1^2 ; U,T2g 4 F2^2 ; U,Eg 2 F4 E0 - 2 F2^2
  (E0, F2, F4, G1, G2)(t) = <(1, f^2, f^4, g, g^2) e^{-t g}>_1D.
"""
import numpy as np
from math import gamma

def moments(law, n=1 << 16):
    k = 2*np.pi*(np.arange(n)+0.5)/n - np.pi
    g, f, fp = law.gff(k)
    return g, f

def evaluate(law, m, n=1 << 16, nu=3000, umin=-18.0):
    g, f = moments(law, n)
    umax = np.log(60.0/min(m*m, 1.0)) + 2
    u = np.linspace(umin, umax, nu); t = np.exp(u); du = u[1]-u[0]
    E0 = np.empty(nu); F2 = np.empty(nu); F4 = np.empty(nu); G1 = np.empty(nu); G2 = np.empty(nu)
    f2, f4, g2 = f*f, f**4, g*g
    for i, ti in enumerate(t):
        w = np.exp(-ti*g)
        E0[i] = w.mean(); F2[i] = (f2*w).mean(); F4[i] = (f4*w).mean(); G1[i] = (g*w).mean(); G2[i] = (g2*w).mean()
    em = np.exp(-t*m*m)
    jac = t*du   # dt = t du
    mu = (1/12)/gamma(1.5)*np.sum(jac*t**0.5*em*(3*F2**2*E0 - F4*E0**2))
    zf = 5*F2*t**2.5/gamma(3.5) - E0*t**1.5/gamma(2.5)
    T = {'M,T2g': 4*G1**2, 'M,Eg': 2*G2*E0 - 2*G1**2, 'U,T2g': 4*F2**2, 'U,Eg': 2*F4*E0 - 2*F2**2}
    Xi = {v: (1/32)*np.sum(jac*em*Tv*zf) for v, Tv in T.items()}
    return mu, Xi

def IBcurve(law, Bs, n=1 << 16):
    g, f = moments(law, n)
    return np.array([2*np.pi*np.mean((5*f*f-(B+g))/(B+g)**3.5) for B in Bs])
