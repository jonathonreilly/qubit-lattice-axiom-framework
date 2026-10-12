"""R5-3 numbers: phase-transition tuning, Lemma PT check (FRW, sympy), Baum-Hawking
exponent, fixed-4-volume (unimodular microcanonical) saddle, equilibrium identity.
All numbers labelled; comparator inputs marked."""
import math
import sympy as sp

print("== constants (CODATA-level, comparator)")
GeV_to_inv_m = 1/(1.97327e-16)       # 1 GeV = 1/(1.97327e-16 m)
M_Pl = 1.220890e19                   # GeV (non-reduced)
Mbar = M_Pl/math.sqrt(8*math.pi)
l_P = 1.616255e-35
H0 = 67.4*1e3/3.0857e22              # s^-1
c = 2.99792458e8
Om_L = 1-0.3153
Lam_obs = 3*Om_L*H0**2/c**2          # m^-2
rho_crit_GeV4 = 3*(H0*6.582119569e-25)**2*Mbar**2   # 3 H0^2 Mbar^2 in GeV^4
rho_L = Om_L*rho_crit_GeV4
print(f"Lambda_obs = {Lam_obs:.4e} m^-2 ; Lambda_obs*l_P^2 = {Lam_obs*l_P**2:.4e}")
print(f"rho_Lambda = {rho_L:.4e} GeV^4 = ({rho_L**0.25*1e12:.3f} meV)^4")

print("\n== (1) phase-transition shifts that an initial-datum (UG integration constant) must pre-cancel")
mH, v = 125.25, 246.22
dV_EW = mH**2*v**2/8                 # tree-level SM: V(0)-V(v) = lambda v^4/4, lambda = mH^2/(2 v^2)
print(f"EW: Delta V = mH^2 v^2/8 = {dV_EW:.4e} GeV^4 = ({dV_EW**0.25:.1f} GeV)^4 ; /rho_Lambda = {dV_EW/rho_L:.3e}")
for name, B in [("QCD bag B^(1/4)=145 MeV", 0.145**4), ("QCD bag B^(1/4)=235 MeV", 0.235**4),
                ("QCD trace anomaly (9/32)<a_s G^2/pi>, <..>=0.012 GeV^4", 9/32*0.012)]:
    print(f"{name}: {B:.3e} GeV^4 ; /rho_Lambda = {B/rho_L:.3e}")
V_inf_max = 1.6e16**4  # r<0.036 (BICEP/Keck 2021) -> V^(1/4) < ~1.6e16 GeV (comparator, from memory)
print(f"inflation (upper, comparator from memory) V^(1/4)<1.6e16 GeV: {V_inf_max:.3e} GeV^4 ; /rho_Lambda = {V_inf_max/rho_L:.3e}")
print(f"Planck-cell tadpole O(1) lattice units ~ Mbar^4 = {Mbar**4:.3e} GeV^4 ; /rho_Lambda = {Mbar**4/rho_L:.3e}")

print("\n== (2) Lemma PT on FRW (sympy): S = T + f(t) g, Bianchi forces Lambda(t) - 8 pi G f(t) = const")
t = sp.symbols('t', real=True)
G = sp.symbols('G', positive=True)
a = sp.Function('a')(t); rho = sp.Function('rho')(t); p = sp.Function('p')(t)
f = sp.Function('f')(t); Lam = sp.Function('Lam')(t)
H = sp.diff(a, t)/a
# flat FRW, c=1: G_00 = 3H^2 ; G_ij = -(2 a'' /a + H^2) a^2 delta_ij (mostly plus)
# Source S = T + f g : S_00 = rho - f ; S_ij = (p + f) a^2 delta_ij
# Field eqs with Lambda(t): 3H^2 - Lam = 8 pi G (rho - f) ; -(2a''/a + H^2) + Lam = 8 pi G (p + f)
E00 = 3*H**2 - Lam - 8*sp.pi*G*(rho - f)
Eii = -(2*sp.diff(a, t, 2)/a + H**2) + Lam - 8*sp.pi*G*(p + f)
# conservation of the TRUE T: rho' = -3H(rho+p)
cons = {sp.diff(rho, t): -3*H*(rho + p)}
# time derivative of E00 combined with Eii: d/dt E00 + 3H(E00 + Eii) should reduce to -(Lam' - 8 pi G f')
expr = sp.diff(E00, t) + 3*H*(E00 + Eii)
expr = sp.simplify(expr.subs(cons))
print("d/dt E00 + 3H(E00+Eii) on T-conserving matter =", sp.simplify(expr))
print("=> consistency (E00=Eii=0 for all t) requires Lam' = 8 pi G f' : Lam - 8 pi G f = Lam_c, and then")
print("   3H^2 = 8 pi G rho + Lam_c : the subtraction f(t) is invisible; only Lam_c and the true T matter.")

print("\n== (3) Baum-Hawking: I_E(S^4) = -3 pi/(G Lambda) [hbar=c=1]")
x = Lam_obs*l_P**2
IE = 3*math.pi/x
print(f"3 pi/(l_P^2 Lambda_obs) = {IE:.4e}  ; P(Lambda_obs/2)/P(Lambda_obs) = exp({IE:.3e})")
r, Lm = sp.symbols('r Lambda', positive=True)
I_r = -(sp.Rational(1, 16)/(sp.pi*G))*(12/r**2 - 2*Lm)*sp.Rational(8, 3)*sp.pi**2*r**4
sol = sp.solve(sp.diff(I_r, r), r)
Istar = sp.simplify(I_r.subs(r, sol[0]))
print("S^4 action I(r) =", sp.simplify(I_r), "; stationary r =", sol, "; I* =", Istar,
      "; d2I/dr2 at r* =", sp.simplify(sp.diff(I_r, r, 2).subs(r, sol[0])))

print("\n== (4) fixed total 4-volume V (unimodular 'microcanonical', count = V/l^4):")
print("   Z(V) = int dLambda exp(Lambda V/(8 pi G)) exp(3 pi/(G Lambda)); saddle Lambda* = sqrt(24 pi^2 / V)")
Vs = sp.symbols('V', positive=True)
fexp = Lm*Vs/(8*sp.pi*G) + 3*sp.pi/(G*Lm)
print("   saddle:", sp.solve(sp.diff(fexp, Lm), Lm))
Vlc = 6.3894e242; VH = 5.2000e243; Vct = 4.2417e243   # l_P^4, from R4-5 r45_numbers.out
for name, V in [("V_lc (past cone)", Vlc), ("(c/H0)^4", VH), ("(c t0)^4", Vct)]:
    Ls = math.sqrt(24*math.pi**2/V)
    print(f"   N = {name} = {V:.3e} l_P^4 -> Lambda* l_P^2 = {Ls:.3e} = {Ls/x:.2f} Lambda_obs")
Vneed = 24*math.pi**2/x**2
print(f"   total 4-volume giving Lambda* = Lambda_obs: {Vneed:.3e} l_P^4 = {Vneed/VH:.1f} (c/H0)^4 ;"
      f" (Euclidean S^4 of radius sqrt(3/Lambda_obs): 8 pi^2 r^4/3 = {8*math.pi**2/3*(3/x)**2:.3e})")

print("\n== (5) equilibrium (Gibbs-Duhem) identity: E(N,V)=V eps(N/V); dE/dV|_N = eps - n eps'(n) = -p")
n = sp.symbols('n', positive=True)
eps = sp.Function('eps')
N_, V_ = sp.symbols('N V', positive=True)
E = V_*eps(N_/V_)
dEdV = sp.simplify(sp.diff(E, V_).subs(N_, n*V_))
print("   dE/dV at fixed N =", dEdV, " (= eps - n eps'(n); vanishes at the zero-pressure equilibrium)")
# example: an arbitrary eps(n) with a minimum of eps/n (self-bound medium)
e1 = n*(n-1)**2 - n/2   # sample energy density with a minimum of eps/n at n=1
n0 = [s for s in sp.solve(sp.diff(e1/n, n), n) if s.is_real and s > 0]
for s in n0:
    print(f"   sample eps(n) = n(n-1)^2 - n/2: equilibrium n0 = {float(s):.6f}, eps(n0) = {float(e1.subs(n, s)):.6f}"
          f", eps - n eps' = {float((e1 - n*sp.diff(e1, n)).subs(n, s)):.2e}")
print("   fixed density (one record per site, fixed spacing): n = n_max is not a variable;"
      " eps(n_max) - mu n_max has no condition setting it to zero.")
