"""S1b: is the factor 4 between S1 (6.695) and the worker/referee (1.674) a Jacobian error or a region convention?
A^2(T) = rho * Int_{past region} E[w^2] d^4y, Milne coords d^4y = tau^3 sinh^2(eta) dtau deta dOmega.
Slab of depth T:   y in past of x with t_x - t_y <= T      -> cosh(eta) <= T/tau.
Diamond height T:  y in past of x and future of x-(T,0)    -> cosh(eta) <= (T^2+tau^2)/(2 T tau).
Small-eps weights: E[w^2] = eps^2 f_inf(eps*m)^2, m = rho*pi*tau^4/24, rho = 1/eps (l_k = 1).
"""
from mpmath import mp, mpf, quad, exp, sinh, acosh, pi, inf
mp.dps = 20
eps = mpf('1e-4'); rho = 1/eps
def f_inf(u): return exp(-u)*(1 - 9*u + 8*u**2 - mpf(4)/3*u**3)
def Ew2(tau): return eps**2*f_inf(eps*rho*pi*tau**4/24)**2
def sinh2int(etamax):  # int_0^etamax sinh^2 = sinh(2e)/4 - e/2
    return sinh(2*etamax)/4 - etamax/2
def A2(T, region):
    def g(tau):
        if region == 'slab':
            c = T/tau
        else:
            c = (T**2 + tau**2)/(2*T*tau)
        if c <= 1: return mpf(0)
        return rho*tau**3*4*pi*sinh2int(acosh(c))*Ew2(tau)
    taumax = T if region == 'slab' else T  # diamond: tau <= T
    return quad(g, [0, 0.5, 1, 1.5, 2, 3, 5, taumax])
for T in [20, 40, 80]:
    T = mpf(T)
    print(f"T={float(T):5.0f}  slab A2/(eps T^2) = {float(A2(T,'slab')/(eps*T**2)):.5f}   diamond A2/(eps T^2) = {float(A2(T,'diamond')/(eps*T**2)):.5f}")
