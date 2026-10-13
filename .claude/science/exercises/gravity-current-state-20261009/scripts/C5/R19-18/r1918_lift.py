#!/usr/bin/env python3
"""R19-18 [L]: the FRW lifts of E2's friction, symbolically.
 E2 law (R12-7/R19-8): (box - gamma u.d) h^{ab} = -16 pi G tau^{ab}, h^{ab} = eta^{ab} - gothic g^{ab} (Poisson-Will sign; = hbar at O(h)),
 equivalently G^{ab} = 8 pi G T_eff with the friction stress Xt^{ab} = -(gamma/16 pi G) u.d h^{ab} (R19-8 sec 3.2).
 [L1] homogeneous mode, FRW ds^2 = -N^2 dt^2 + a^2 dx^2, friction evaluated with a LOCAL reference (a(t0)=1, N(t0)=1 at the epoch):
      Xt^{00}, Xt^{ij} -> rho_X, p_X = kappa_p gamma H/(4 pi G), for three slicings: harmonic (N = a^3, E2's law gauge), synchronous (N = 1),
      and L0 (friction on the deviation from the FRW background: zero by definition).
 [L2] GLOBAL fixed reference (a_ref, harmonic N = C a^3): p_X = (gamma H/4 pi G)(a_ref/a)^6 / C  (not scale-free).
 [L3] TT mode: cosmic-time friction gamma*hdot -> conformal h'' + (2 + nu) calH h' + k^2 h = 0 with nu = gamma/H; gothic-lift mass terms.
 [L4] Lemma F0 (R19-2, lift A, Pi's k=0 part pressureless): rho_sink = -a^-3 int p_X d(a^3); matter era / radiation era closed forms.
Subtraction: none.  G = c = 1 where marked.  Run: OMP_NUM_THREADS=2 python3 r1918_lift.py
"""
import sympy as sp, time
t0 = time.time()
t, gam, G = sp.symbols('t gamma G', positive=True)
a = sp.Function('a', positive=True)(t)
H = sp.Symbol('H')

def gothic(N):
    # gothic g^{00} = -sqrt(-g)/N^2 = -a^3/N ; gothic g^{ij} = sqrt(-g) g^{ij} = N a^3 / a^2 = N a
    return -a**3 / N, N * a

def local_friction(N, label):
    g00, gij = gothic(N)
    h00 = -1 - g00          # eta^{00} - gothic^{00}, eta^{00} = -1
    hij = 1 - gij           # eta^{ij} - gothic^{ij}
    ud = lambda f: sp.diff(f, t) / N      # u.d = (1/N) d_t
    X00 = -(gam / (16 * sp.pi * G)) * ud(h00)
    Xij = -(gam / (16 * sp.pi * G)) * ud(hij)
    # (-g) T^{ab} = Xt^{ab}; (-g) = N^2 a^6 ; T^{00} = rho/N^2 ; T^{ij} = p/a^2
    rho = sp.simplify(X00 / a**6)   # (-g) T^{00} = Xt^{00}, T^{00} = rho/N^2, (-g) = N^2 a^6
    p = sp.simplify(Xij * a**2 / (N**2 * a**6))
    sub = {sp.diff(a, t): N * H * a}   # H = (1/a) da/dtau, dtau = N dt
    rho0 = sp.simplify(rho.subs(sub).subs(a, 1))
    p0 = sp.simplify(p.subs(sub).subs(a, 1))
    kr = sp.simplify(rho0 / (gam * H / (4 * sp.pi * G)))
    kp = sp.simplify(p0 / (gam * H / (4 * sp.pi * G)))
    print("     %-34s rho_X = %-28s p_X = %-24s kappa_rho = %s, kappa_p = %s" % (label, rho0, p0, kr, kp))
    return kr, kp

print("[L1] local-reference friction stress of the homogeneous mode (a = 1, N = 1 at the epoch):")
kh = local_friction(a**3, "harmonic (N = a^3, E2's law gauge)")
ks = local_friction(sp.Integer(1), "synchronous (N = 1)")
print("     L0 (friction on the deviation from the FRW background): Xt_{k=0} = 0 identically -> kappa_p = 0")
print("     check harmonic gauge: d_t gothic^{00} with N = a^3:", sp.simplify(sp.diff(gothic(a**3)[0], t)))
# ---------------- [L2] ----------------
C, aref = sp.symbols('C a_ref', positive=True)
N = C * (a / aref)**3
# literal: gothic^{ij} = C a^4 in coordinates where eta^{ij} = delta^{ij} is the metric at a = a_ref, C chosen there
gij_lit = C * (a / aref)**4
Xij = -(gam / (16 * sp.pi * G)) * sp.diff(1 - gij_lit, t) / N
p_lit = sp.simplify((Xij * (a / aref)**2 / (N**2 * (a / aref)**6)).subs(sp.diff(a, t), N * H * a))   # dtau = N dt
print("[L2] global fixed reference (harmonic N = C a^3, eta at a = a_ref): p_X =", sp.simplify(p_lit),
      "  [= (gamma H/4 pi G)(a_ref/a)^6/C : not invariant under a -> lambda a]")
# ---------------- [L3] ----------------
eta_c = sp.Symbol('eta')
hT = sp.Function('h')
# cosmic-time equation hdd + (3H + gamma) hd + (k^2/a^2 + m2) h = 0 ; dt = a d eta ; calH = a H
k, m2, calH, A = sp.symbols('k m2 calH A', positive=True)
hp, hpp = sp.symbols('hp hpp')        # h', h'' in conformal time
hd = hp / A
hdd = (hpp - calH * hp) / A**2
expr = sp.expand((hdd + (3 * calH / A + gam) * hd + (k**2 / A**2 + m2) * hT(eta_c)) * A**2)
print("[L3] conformal TT equation:", sp.collect(expr, [hpp, hp]))
print("     => h'' + (2 + nu) calH h' + (k^2 + a^2 m2) h = 0 with nu = a gamma / calH = gamma / H ; d_L^GW/d_L^EM = exp(int nu/2 dln(1+z)) = exp(gamma t_lb/2)")
# gothic TT lifts: delta gothic^{ij} = -N a h_ij ; friction on it adds -gamma (hdot + (H + Ndot/N) h) to the TT equation (local reference)
for lab, Nn in (("harmonic N = a^3", a**3), ("synchronous N = 1", sp.Integer(1))):
    extra = sp.simplify((sp.diff(Nn * a * hT(t), t) / Nn).subs(sp.diff(a, t), H * a).subs(a, 1))
    print("     gothic TT lift (%s): friction term gamma*(%s) -> mass term m^2 = %s" % (lab, extra, sp.simplify(sp.expand(extra).coeff(hT(t)) * gam)))
# ---------------- [L4] ----------------
ap, kp_ = sp.symbols("a' kappa_p", positive=True)
# matter era E = Om^(1/2) a^(-3/2) (units H0): Omega_s a^3 = -2 g int E a^2 da, g = kappa_p gamma/H0
Om, g = sp.symbols('Omega_m g_L', positive=True)
aa = sp.Symbol('a', positive=True)
Es = sp.sqrt(Om) * ap**sp.Rational(-3, 2)
Ys = -2 * g * sp.integrate(Es * ap**2, (ap, 0, aa))
Os = sp.simplify(Ys / aa**3)
Ea = sp.sqrt(Om) * aa**sp.Rational(-3, 2)
print("[L4] Lemma F0 (lift A), matter era: Omega_s =", Os, " ; Omega_s/(g_L/E) =", sp.simplify(Os / (g / Ea)),
      " ; p_X/rho_c0 = (2/3) g_L E ; w_sink = p/rho =", sp.simplify((sp.Rational(2, 3) * g * Ea) / Os))
Er = sp.sqrt(sp.Symbol('Omega_r', positive=True)) * ap**-2
Ysr = -2 * g * sp.integrate(Er * ap**2, (ap, 0, aa))
Ear = Er.subs(ap, aa)
print("     radiation era: Omega_s/(g_L/E) =", sp.simplify((Ysr / aa**3) / (g / Ear)), "(-> negligible early: |Omega_s|/E^2 ~ g_L/E)")
print("     sink NEC: rho_s + p_X = (-4/3 + 2/3) g_L/E rho_c(t) -> sign(-kappa_p): kappa_p > 0 sink violates NEC (phantom-like)")
print("    runtime %.1f s" % (time.time() - t0))
