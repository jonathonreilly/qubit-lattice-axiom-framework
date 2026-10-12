"""R6-3: past-cone variance split into the 'Bragg-aligned base' part (timelike shells, cone-frame |k| < K, i.e. a
timelike reciprocal vector within ~K/T of the cone's time axis) and the rest ('typical frames').
J_tl,rest(m) = J_tl(m) - 4 pi m int_0^{asinh(K/sqrt m)} sinh^2 |P^|^2 d eta."""
import numpy as np, sys
sys.path.insert(0, '.')
from r63_formfactor import P_abs2
exec(open('r63_variance.py').read().split("vol = {'D'")[0])
def J_rest_part(m, K, n=200001):
    sm = np.sqrt(m); emax = np.arcsinh(K/sm)
    e = np.linspace(1e-7, emax, n)
    return np.trapezoid(4*np.pi*m*np.sinh(e)**2*P_abs2(sm*np.cosh(e), sm*np.sinh(e)), e)
for K in (2.0, 4.0, 8.0):
    for T in (13, 27, 54, 108, 1000, 1e4):
        ts = tt[tt < 0][-400:]       # |t| <= 400 suffices for the aligned part
        Cs_ = CC[tt < 0][-400:]
        al = rho**2*T**3*np.sum(Cs_*np.array([J_rest_part(c*abs(t)*T**2, K) for t in ts]))*T**3
        tot = Var('P', T)
        print("K=%g T=%6g  Var/T^3: total %.4f  aligned-base part %.4f  rest %.4f   rest/(T^2 lnT) = %.4f" % (K, T, tot/T**3, al/T**3, (tot-al)/T**3, (tot-al)/(T**2*np.log(T))), flush=True)
