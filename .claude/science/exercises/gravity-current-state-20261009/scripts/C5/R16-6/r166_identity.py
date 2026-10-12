"""R16-6 identity checks (sympy).  kappa kept symbolic.
1. Homogeneous R14-5 bookkeeping: g = -2 Hdot - kappa (rho+p)_tot (w=-1 c-number drops out),
   with 3H^2 = kappa R  =>  g = (kappa/3) dV/du,  V := rho_tot - R   (R15-6 Lemma I, re-derived).
2. Integrating reader IE: R' = -3 h  (h = (rho+p)_tot)  =>  V' = 0 identically  => g = 0 for every history.
3. Equilibrium P-EoS reader: R = rho_EoS(T(h)) - rho_EoS(0); thermodynamic consistency
   (rho = T p' - p, h = T s = T p') gives d rho_EoS/du = -3 h along any adiabatic history => V' = 0.
4. Converse: g == 0 on an interval  <=>  R' = -3h on it  <=> R = rho_tot - const.
"""
import sympy as sp
u, kap = sp.symbols('u kappa', positive=True)
rho_nc = sp.Function('rho_nc')(u)     # conserved non-vacuum content, any history
rho_v  = sp.Function('rho_v')(u)      # w=-1 stress (may change; total conserved)
Rr     = sp.Function('R')(u)          # reader output
# total conservation in u: rho_tot' = -3 h, h = (rho+p)_tot = (rho+p)_nc since w=-1 part has rho+p=0
h = sp.Function('h')(u)
rho_tot = rho_nc + rho_v
cons = sp.Eq(sp.diff(rho_tot, u), -3*h)
H = sp.sqrt(kap*Rr/3)
Hdot = H*sp.diff(H, u)                # d/dt = H d/du
g = -2*Hdot - kap*h
V = rho_tot - Rr
lemmaI = sp.simplify(g - (kap/3)*sp.diff(V, u).subs(sp.diff(rho_tot,u), -3*h))
# sp.diff(V,u) contains rho_nc'+rho_v'; replace their sum by -3h:
dV = sp.diff(Rr, u)*(-1) + (-3*h)
lemmaI = sp.simplify(g - (kap/3)*dV)
print("1. g - (kappa/3) V'(u) =", lemmaI)
# 2. IE reader
gIE = sp.simplify(g.subs(sp.diff(Rr, u), -3*h))
print("2. IE reader (R' = -3h): g =", gIE)
# 3. P-EoS on an equilibrium barotropic fluid: p(T) arbitrary smooth, T(u) any (adiabatic: d(s a^3)=0)
T = sp.Function('T')(u); p = sp.Function('p')
s = sp.diff(p(T), T)                   # entropy density s = dp/dT (mu = 0)
rho = T*s - p(T)
# adiabatic: s(T(u)) e^{3u} = const  =>  T' = -3 s / s_T
sT = sp.diff(s, T)
Tprime = -3*s/sT
drho = sp.diff(rho, u).subs(sp.diff(T, u), Tprime)
hval = rho + p(T)
print("3. equilibrium fluid: rho' + 3h =", sp.simplify(drho + 3*hval))
print("   d(Ts)/dT - (s + c_V) =", sp.simplify(sp.diff(T*s, T) - (s + T*sT)), "(monotone h(T) iff s + c_V > 0)")
# 4. converse
print("4. g == 0  <=>  R' = -3h:  solve g=0 for R' ->", sp.solve(sp.Eq(g, 0), sp.diff(Rr, u)))
