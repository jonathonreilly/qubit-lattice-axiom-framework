"""R13-3 (b): linear scalar perturbations of V3 + site creation (unit lapse), symbolic.

Synchronous slicing = V3's physical foliation (unit lapse => normals geodesic).
Ma-Bertschinger (MB 1995, eq. 21) conventions, conformal time tau, Hc = a'/a:
  (H)  k^2 eta - Hc h'/2 + 4 pi G a^2 drho                      [Hamiltonian; NOT imposed in V3]
  (M)  k^2 eta' - 4 pi G a^2 (rho+p) theta                       [momentum; imposed]
  (T)  h'' + 2 Hc h' - 2 k^2 eta + 24 pi G a^2 dp                [spatial trace; NOT imposed]
  (S)  h'' + 6 eta'' + 2 Hc (h' + 6 eta') - 2 k^2 eta + 24 pi G a^2 (rho+p) sigma  [traceless; imposed]
One barotropic fluid, constant w, sound speed cs2 = dp/drho, sigma = 0 (perfect fluid).
Background (P-T / F-law): Hc^2 = (8 pi G/3) a^2 rho_nc + chi  (chi = X a^2 const: the F-law memory),
Hc' = -(4 pi G/3) a^2 (rho + 3p)_nc  (X drops out of Hc', checked below).
A w = -1 vacuum enters T only as -rho_v g, whose divergence vanishes in every metric, so it never
enters the perturbed identities (stated, not computed).

Checks:
 1. (T) follows from (M), (S) and the fluid equations for k != 0  [the nu = j Bianchi component].
 2. (H)' + Hc (H) = [coefficient] * h' + (multiples of (M),(T)) ; coefficient = -chi/2 (memory) -> 0 if chi = 0.
    So V := (H) obeys V ~ 1/a (i.e. delta E^0_0 = V/a^2 ~ a^-3): the C-dust law.
 3. With (H) = C/a (C-dust) added, the closed system (M),(S),(T)+fluid is GR's synchronous system with an
    extra pressureless component at rest on the normals: the C-dust density perturbation
    drho_C = -C/(4 pi G a^3) and, with a mean C-dust rho_C0, delta_C' = -h'/2 (CDM in synchronous gauge).
"""
import sympy as sp

tau, k, G, w, cs2, chi = sp.symbols('tau k G w c_s2 chi', real=True)
a = sp.Function('a')(tau)
rho = sp.Function('rho')(tau)          # background nc density
h = sp.Function('h')(tau)
eta = sp.Function('eta')(tau)
delta = sp.Function('delta')(tau)
theta = sp.Function('theta')(tau)

p = w * rho
Hc = sp.diff(a, tau) / a
# background substitutions
rho_p = -3 * Hc * (rho + p)                       # continuity
Hc2 = sp.Rational(8, 3) * sp.pi * G * a**2 * rho + chi
Hcp = -sp.Rational(4, 3) * sp.pi * G * a**2 * (rho + 3 * p)

# check Hc' from Hc^2 with chi const: d/dtau(Hc^2) = 2 Hc Hc'
lhs = sp.diff(sp.Rational(8, 3) * sp.pi * G * a**2 * rho, tau)
lhs = lhs.subs(sp.Derivative(rho, tau), rho_p)
lhs = sp.simplify(lhs / (2 * Hc))
print('1a. F-law memory: Hc\' from Hc^2 = (8piG/3)a^2 rho + chi (chi const) equals -(4piG/3)a^2(rho+3p):',
      sp.simplify(lhs - Hcp) == 0)

drho = rho * delta
dp = cs2 * drho
# fluid equations (MB eq. 30, constant w, sigma = 0)
delta_p = -(1 + w) * (theta + sp.diff(h, tau) / 2) - 3 * Hc * (cs2 - w) * delta
theta_p = -Hc * (1 - 3 * w) * theta + cs2 / (1 + w) * k**2 * delta

EH = k**2 * eta - Hc * sp.diff(h, tau) / 2 + 4 * sp.pi * G * a**2 * drho
EM = k**2 * sp.diff(eta, tau) - 4 * sp.pi * G * a**2 * (rho + p) * theta
ET = sp.diff(h, tau, 2) + 2 * Hc * sp.diff(h, tau) - 2 * k**2 * eta + 24 * sp.pi * G * a**2 * dp
ES = (sp.diff(h, tau, 2) + 6 * sp.diff(eta, tau, 2) + 2 * Hc * (sp.diff(h, tau) + 6 * sp.diff(eta, tau))
      - 2 * k**2 * eta)


def reduce(expr):
    """Substitute background and fluid equations; keep a', eta', h, h' free."""
    ap = sp.diff(a, tau)
    expr = expr.subs({sp.Derivative(delta, tau): delta_p, sp.Derivative(theta, tau): theta_p})
    expr = expr.subs(sp.Derivative(rho, tau), rho_p)
    # a'' from Hc' = Hcp: a''/a - (a'/a)^2 = Hcp
    expr = expr.subs(sp.Derivative(a, tau, 2), a * (Hcp + Hc**2))
    expr = expr.subs(sp.Derivative(rho, tau), rho_p)
    return sp.simplify(sp.expand(expr))


# Check 1: (S) - (T) = (6/k^2)[ (EM)' + 2 Hc EM ] identically (given fluid eqs) -> (T) implied for k != 0
lhs1 = ES - ET
rhs1 = 6 / k**2 * (sp.diff(EM, tau) + 2 * Hc * EM)
res1 = reduce(sp.expand(lhs1 - rhs1))
print('1. (S) - (T) - (6/k^2)[(M)\' + 2 Hc (M)] =', res1, ' -> (T) follows from (M),(S) for k != 0 (nu=j Bianchi)')

# Check 2: (H)' + Hc (H) in terms of (M), (T)
expr2 = sp.diff(EH, tau) + Hc * EH
# eliminate eta' via (M) and h'' via (T)
hpp = sp.solve(sp.Eq(ET, 0), sp.diff(h, tau, 2))[0]
etap = sp.solve(sp.Eq(EM, 0), sp.diff(eta, tau))[0]
expr2r = reduce(expr2.subs(sp.Derivative(h, tau, 2), hpp).subs(sp.Derivative(eta, tau), etap))
# Hc^2 does not appear explicitly; chi enters only via a'' = a(Hcp + Hc^2) -> Hc^2 = Hc2 substitution:
expr2r = sp.simplify(expr2r.subs((sp.diff(a, tau) / a)**2, Hc2))
expr2r = sp.simplify(sp.expand(expr2r))
print('2. (H)\' + Hc (H), on (M),(T),fluid  =', sp.factor(expr2r))
coef = sp.simplify(expr2r / sp.diff(h, tau))
coef = sp.simplify(coef.subs(sp.Derivative(a, tau), a * sp.sqrt(Hc2)))
print('2b. coefficient of h\' after Hc^2 = (8piG/3)a^2 rho + chi :', coef,
      ' -> (H)\' + Hc (H) = (chi/2) h\'.  chi = 0: (H) ~ 1/a, delta E^0_0 = (H)/a^2 ~ a^-3 (C-dust).')
# 3. Reading of 2b. In GR an extra component C enters (H) as k^2 eta - Hc h'/2 = -4 pi G a^2 (drho + drho_C),
#    so drho_C := -(H)/(4 pi G a^2). Then 2b gives (a^3 drho_C)' = -(chi a/(8 pi G)) h'.
#    A fluid at rest on the normals obeys (a^3 drho)' = -a^3 (rho+p) h'/2 (MB synchronous continuity, theta = 0).
#    Match: (rho+p)_eff = chi/(4 pi G a^2) = 2X/kappa (kappa = 8 pi G, chi = X a^2).
#    (i) curvature-like memory (X ~ a^-2): rho_X = 3X/kappa, w = -1/3, (rho+p) = 2X/kappa  -> consistent;
#    (ii) dust-like memory (X_d ~ a^-3, i.e. H^2 = kappa/3 (rho_hat + rho_d)): repeating 2b with Hc' including rho_d
#         gives a fluid at rest with (rho+p) = rho_d: C-dust with a MEAN clusters exactly like synchronous CDM.
tX = sp.symbols('X', real=True)
kap = 8 * sp.pi * G
rhoX = 3 * tX / kap
print('3(i). (rho+p) of w=-1/3 fluid with rho_X = 3X/kappa minus 2X/kappa =', sp.simplify(rhoX * sp.Rational(2, 3) - 2 * tX / kap))
# 3(ii): dust-like memory: background Hc^2 = (8piG/3) a^2 (rho + rho_d), rho_d ~ a^-3 (memory, NOT in T)
rd = sp.Function('rd')(tau)
Hc2d = sp.Rational(8, 3) * sp.pi * G * a**2 * (rho + rd)
Hcpd = -sp.Rational(4, 3) * sp.pi * G * a**2 * (rho + 3 * p + rd)
e = sp.diff(EH, tau) + Hc * EH
e = e.subs(sp.Derivative(h, tau, 2), hpp).subs(sp.Derivative(eta, tau), etap)
e = e.subs({sp.Derivative(delta, tau): delta_p, sp.Derivative(theta, tau): theta_p})
e = e.subs(sp.Derivative(rho, tau), rho_p)
e = e.subs(sp.Derivative(a, tau, 2), a * (Hcpd + Hc**2))
e = sp.simplify(sp.expand(e))
cd = sp.simplify((e / sp.diff(h, tau)).subs(sp.Derivative(a, tau), a * sp.sqrt(Hc2d)))
print("3(ii). dust-like memory: coefficient of h' in (H)'+Hc(H) =", sp.simplify(cd),
      " ; expected for CDM at rest with rho_C = rho_d: -[-(4 pi G a^2) rho_d/2] ... i.e. 2 pi G a^2 rho_d:",
      sp.simplify(cd - 2 * sp.pi * G * a**2 * rd) == 0)
