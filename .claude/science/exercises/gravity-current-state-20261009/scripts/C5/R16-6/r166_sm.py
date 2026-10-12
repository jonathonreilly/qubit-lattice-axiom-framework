"""R16-6: SM-like radiation history pieces, homogeneous, kappa = 1, u = ln a.  Units MeV.
(1) QCD crossover with a RECALLED HotQCD-2014 parametrization of p/T^4 (u,d,s + gluons; 2+1 flavour), plus a
    free massive gas for the rest.  Single-temperature equilibrium fluid.  Literal P-EoS reader
    R = rho_EoS(T(h)) - rho_EoS(0) is exact by the identity (r166_identity.out:3); here we check numerically and
    report how big the trace-anomaly ("vacuum-like") part is, i.e. what P-EoS lets gravitate and what an
    h-only reader without the EoS must absorb.
(2) e+e- annihilation with neutrinos decoupled instantaneously at T_dec = 2 MeV (RECALLED approximation).
    Two temperatures after T_dec.  Readers: literal P-EoS (single-T equilibrium map incl. nu at the same T),
    IE (integrator started in equilibrium above T_dec: exact by construction), MR (R15-6).
"""
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
pi2 = np.pi**2
def fermi(T, m, g):
    if T <= 0: return 0, 0
    f = lambda p, k: (p**2*np.sqrt(p*p+m*m) if k == 0 else p**4/np.sqrt(p*p+m*m)/3)/(np.exp(np.sqrt(p*p+m*m)/T)+1)
    pmax = 60*T + 10*m
    rho = g/(2*pi2)*quad(f, 0, pmax, args=(0,), limit=200)[0]
    p = g/(2*pi2)*quad(f, 0, pmax, args=(1,), limit=200)[0]
    return rho, p
import warnings; warnings.filterwarnings('ignore')
def bose(T, m, g):
    if T <= 0: return 0, 0
    f = lambda p, k: (p**2*np.sqrt(p*p+m*m) if k == 0 else p**4/np.sqrt(p*p+m*m)/3)/np.expm1(np.sqrt(p*p+m*m)/T)
    pmax = 60*T + 10*m
    rho = g/(2*pi2)*quad(f, 1e-12*T, pmax, args=(0,), limit=200)[0]
    p = g/(2*pi2)*quad(f, 1e-12*T, pmax, args=(1,), limit=200)[0]
    return rho, p
me = 0.511
# ---------------- (2) e+e- annihilation -----------------
Tg = np.geomspace(5.0, 0.005, 1500)
ee = np.array([fermi(T, me, 4) for T in Tg])
rho_g = pi2/15*Tg**4
rho_pl = rho_g + ee[:, 0]; p_pl = rho_g/3 + ee[:, 1]
s_pl = (rho_pl + p_pl)/Tg
rho_nu1 = lambda T: 7/8*2*pi2/30*T**4            # one flavour nu + nubar
rho_eq = rho_pl + 3*rho_nu1(Tg); p_eq = p_pl + rho_nu1(Tg)
h_eq = rho_eq + p_eq
# equilibrium map h -> rho (monotone: d(Ts)/dT = s + c_V > 0)
lh = np.log(h_eq[::-1]); lr = np.log(rho_eq[::-1])
assert np.all(np.diff(lh) > 0)
map_eq = CubicSpline(lh, lr)
Tdec = 2.0
# actual history: above T_dec all at T; below, nu free (T_nu ∝ 1/a), plasma entropy conserved
i_dec = np.argmin(abs(Tg - Tdec))
S_pl = s_pl[i_dec]*1.0                     # a = 1 at T_dec
# solve s_pl(T) a^3 = S_pl for each a on a u-grid
lsp = CubicSpline(np.log(Tg[::-1]), np.log(s_pl[::-1]))
u = np.linspace(-np.log(Tdec/4.0), np.log(Tdec/0.008), 20001)    # from T=4 MeV to T~8 keV (nu temperature)
Tgam = np.empty_like(u); Tnu = np.empty_like(u)
from scipy.optimize import brentq
for i, uu in enumerate(u):
    if uu <= 0:
        Tgam[i] = Tdec*np.exp(-uu); Tnu[i] = Tgam[i]       # approx: before T_dec treat T ∝ 1/a (tiny e± effect above 2 MeV)
    else:
        target = np.log(S_pl) - 3*uu
        Tgam[i] = np.exp(brentq(lambda lt: lsp(lt) - target, np.log(0.005), np.log(5.0)))
        Tnu[i] = Tdec*np.exp(-uu)
eeA = np.array([fermi(T, me, 4) for T in Tgam[::20]])
uA = u[::20]
rho_plA = pi2/15*Tgam[::20]**4 + eeA[:, 0]; p_plA = pi2/45*Tgam[::20]**4 + eeA[:, 1]
rho_nuA = 3*rho_nu1(Tnu[::20])
rho_nc = rho_plA + rho_nuA
h = rho_plA + p_plA + 4/3*rho_nuA
# readers
R_peos = np.exp(map_eq(np.log(h)))
dlnR = np.gradient(np.log(R_peos), uA)
g_peos = -3*h/R_peos - dlnR
eps_peos = R_peos/rho_nc - 1
# MR (R15-6): R = 3/4 h + 1/4 mhat e^{-3u}
hp = np.gradient(h, uA)
val = np.exp(3*uA)*(4*h + hp)
mhat = np.minimum.accumulate(val)
R_mr = 0.75*h + 0.25*mhat*np.exp(-3*uA)
g_mr = -3*h/R_mr - np.gradient(np.log(R_mr), uA)
eps_mr = R_mr/rho_nc - 1
# rho conservation check of the constructed history
cons = (np.gradient(rho_nc, uA) + 3*h)/(3*h)
print("(2) e+e- annihilation, nu decoupled at T_dec = 2 MeV (instantaneous; RECALLED approximation)")
print("    history conservation check max|rho'+3h|/3h (excluding the T_dec kink) = %.2e" % np.max(abs(cons[(uA > 0.05) | (uA < -0.05)][3:-3])))
print("    final T_nu/T_gamma = %.4f  ((4/11)^(1/3) = %.4f)" % (Tnu[::20][-1]/Tgam[::20][-1], (4/11)**(1/3)))
for name, eps, g in [('PEoS(literal)', eps_peos, g_peos), ('MR', eps_mr, g_mr)]:
    sel = slice(3, -3)
    print("    %-14s eps=R/rho_nc-1: final %+.4e, range [%+.3e, %+.3e];  g/H^2 range [%+.3e, %+.3e]"
          % (name, eps[-4], eps[sel].min(), eps[sel].max(), g[sel].min(), g[sel].max()))
# Neff-equivalent of a final fractional error eps in the radiation era
r = 7/8*(4/11)**(4/3)
for name, eps in [('PEoS(literal)', eps_peos[-4]), ('MR', eps_mr[-4])]:
    print("    %-14s Delta N_eff equivalent of the final error = %+.3f  (comparator: Planck ~0.2-0.3, RECALLED)" % (name, eps*(1 + 3*r)/r))
print("    IE: started in equilibrium above T_dec, R' = -3h: exact for any decoupling history (identity); g = 0.")
# ---------------- (1) QCD crossover (RECALLED HotQCD 2014 parametrization) -----------------
Tc = 154.0
ct, an, bn, cn, dn, t0, ad, bd, cd, dd = 3.8706, -8.7704, 3.9200, 0.0, 0.3419, 0.9761, -1.2600, 0.8425, 0.0, -0.0475
pid = 95*pi2/180
def pT4(T):
    t = T/Tc
    return 0.5*(1+np.tanh(ct*(t-t0)))*(pid + an/t + bn/t**2 + cn/t**3 + dn/t**4)/(1 + ad/t + bd/t**2 + cd/t**3 + dd/t**4)
T = np.geomspace(1000.0, 60.0, 4001)
pq = pT4(T)*T**4
lpq = CubicSpline(np.log(T[::-1]), np.log(pq[::-1]))
dp = lpq(np.log(T), 1)*pq/T          # dp/dT
sq = dp; rq = T*sq - pq
# add photons, leptons (e, mu, 3 nu) as ideal massless/massive gas (mu massive)
mu_m = 105.66
lep = np.array([fermi(x, mu_m, 4) for x in T[::40]])
rest_r = (pi2/15 + 7/8*4*pi2/30 + 3*rho_nu1(1.0))*T**4
rest_p = rest_r/3
lep_r = np.interp(np.log(T), np.log(T[::40])[::-1], lep[::-1, 0]); lep_p = np.interp(np.log(T), np.log(T[::40])[::-1], lep[::-1, 1])
rho = rq + rest_r + lep_r; p = pq + rest_p + lep_p
I = (rq - 3*pq)/rho          # QCD trace anomaly fraction of the total ("vacuum-like" part the EoS lets gravitate)
print("(1) QCD crossover, HotQCD-2014 p/T^4 parametrization (RECALLED coefficients), T = 1000 -> 60 MeV")
print("    QCD trace anomaly (rho-3p)_QCD / rho_tot: max %.4f at T = %.0f MeV" % (I.max(), T[np.argmax(I)]))
# adiabatic history and literal P-EoS: exact by construction (single-T equilibrium); numerical check
s = (rho + p)/T
lst = CubicSpline(np.log(T[::-1]), np.log(s[::-1]))
uq = np.linspace(1e-4, np.log(s[0]/np.exp(lst(np.log(65.0))))/3, 3001)
Tu = np.empty_like(uq)
for i, uu in enumerate(uq):
    target = np.log(s[0]) - 3*uu
    Tu[i] = np.exp(brentq(lambda lt: lst(lt) - target, np.log(60.0), np.log(1000.0)))
rhoI = CubicSpline(np.log(T[::-1]), rho[::-1]); pI = CubicSpline(np.log(T[::-1]), p[::-1])
rho_u = rhoI(np.log(Tu)); h_u = rho_u + pI(np.log(Tu))
cons = (np.gradient(rho_u, uq) + 3*h_u)/(3*h_u)
print("    adiabatic history: max|rho'+3h|/3h = %.2e  (P-EoS reads R = rho_EoS(T(h)) = rho exactly, so V' = rho'+3h - 0 -> g/H^2 = this/R scale)" % abs(cons[2:-2]).max())
gq = -(np.gradient(rho_u, uq) + 3*h_u)/rho_u
print("    literal P-EoS g/H^2 from the numerical history: max |g/H^2| = %.2e (finite-difference level)" % abs(gq[2:-2]).max())
dlnrho = -3*h_u/rho_u
print("    an h-only reader WITHOUT the EoS must absorb the trace-anomaly change; R15-4's linear reader residual at QCD was 8.89e-5 (vR15-4:21; count once)")
