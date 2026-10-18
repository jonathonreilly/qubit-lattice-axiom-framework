#!/usr/bin/env python3
"""C4: does the repo's microscopic realisation fix the scale of h?

Exact sympy checks. Prints PASS/FAIL per check and a TOTAL line.

Part A  the walker's coupling to h (block 62 frame; block 64 / block 73 bond couplings with
        block 120's normalisation B = -(a_R/2) phi h): which matter-coupling strength a_s,
        defined by "the matter propagates on the metric delta + a_s h", does the walker have?
Part B  the member's lapse identity (block 134 / block 120 T4) re-derived with SEPARATE
        coefficients K1 (on u R1) and K2 (on R2) and a source (a_s/2) sum Theta h:
        which combination does the walker's content have to match?  TT cone with K2.
        Behaviour under the canonical rescaling Phi_rho of B21.
Part C  independent plane-wave check that block 62's R1, R2 are the first- and second-order
        parts of sqrt(g) R[g] for g = delta + h (so the B21 one-parameter family is one metric
        theory in delta + h/r), giving the reading a_s = 1/r for universal coupling.

Nothing here is fitted; every expected constant is fixed by the stated definitions.
"""
import itertools
import sys
import time

import sympy as sp

T0 = time.time()
RESULTS = []


def check(tag, ok, msg):
    RESULTS.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}", flush=True)


# ----------------------------------------------------------------------------- common objects
s1, s2, s3 = sp.symbols('s1 s2 s3', real=True)
svec = sp.Matrix([s1, s2, s3])
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
I2 = sp.eye(2)


def symm(name):
    a = sp.symbols(f'{name}11 {name}22 {name}33 {name}12 {name}13 {name}23', real=True)
    M = sp.Matrix([[a[0], a[3], a[4]], [a[3], a[1], a[5]], [a[4], a[5], a[2]]])
    return M, list(a)


h, hv = symm('h')

# ============================================================================ PART A
print("== Part A: the walker's coupling strength to h")

# A1 block 62 T1(a): uniform frame E (E[a, j] = E_a^j), H(k) = sum_j (E^j . sigma) s_j,
#    H^2 = (s^T E^T E s) 1, i.e. g^{ij} = sum_a E_a^i E_a^j.  Exact for a general 3x3 frame.
E = sp.Matrix(3, 3, lambda a, j: sp.Symbol(f'E{a+1}{j+1}', real=True))
Hk = sp.zeros(2, 2)
for j in range(3):
    for a in range(3):
        Hk += E[a, j] * sig[a] * svec[j]
lhs = sp.expand(Hk * Hk)
rhs = sp.expand((svec.T * E.T * E * svec)[0, 0]) * I2
check("A1", sp.simplify(lhs - rhs) == sp.zeros(2, 2),
      "uniform frame: H(k)^2 = s^T (E^T E) s * 1 exactly (Clifford relation of the coin); the walker's cone is g^{-1} = E^T E")

# A2 With E = 1 + t*eps (general eps), h := (E^T E)^{-1} - delta.  Matter on the metric
#    delta + a h has omega^2 = s^T (delta + a h)^{-1} s.  The order-t match with the walker fixes a.
t, a_cpl = sp.symbols('t a', real=True)
eps = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'e{i+1}{j+1}', real=True))
Ef = sp.eye(3) + t * eps
ginv_walker = Ef.T * Ef
h1 = -(eps + eps.T)  # first-order h from h = (E^T E)^{-1} - 1
g_series = sp.eye(3) - t * (eps + eps.T)  # (1 + t X)^{-1} to first order, X = eps + eps^T
chk_h1 = sp.expand((g_series * ginv_walker - sp.eye(3)).applyfunc(lambda z: sp.expand(z).coeff(t, 1)))
check("A2a", chk_h1 == sp.zeros(3, 3),
      "h = (E^T E)^{-1} - delta = -(eps + eps^T) t + O(t^2): only the symmetric part of the tilt enters (block 62 T3(a))")
om2_walker = sp.expand((svec.T * ginv_walker * svec)[0, 0])
om2_matter_first = sp.expand((svec.T * (sp.eye(3) - a_cpl * t * h1) * svec)[0, 0])  # (delta + a t h1)^{-1} to O(t)
eq = sp.expand(om2_walker.coeff(t, 1) - om2_matter_first.coeff(t, 1))
sol = sp.solve(sp.Poly(eq, *list(eps), s1, s2, s3).coeffs(), a_cpl, dict=True)
check("A2b", sol == [{a_cpl: 1}],
      f"order-t match of the walker's cone with matter on delta + a h for all eps, s: solution {sol} (a_s = 1 uniquely)")

# A2c exact to all orders: (delta + h)^{-1} = E^T E by definition, so the walker's uniform cone is
#     exactly that of g = delta + h.  Check at second order explicitly (not just definitional).
X = eps + eps.T
g2 = sp.eye(3) - t * X + t**2 * (X * X - eps.T * eps)  # (1 + tX + t^2 eps^T eps)^{-1} to O(t^2)
prod = (g2 * ginv_walker).applyfunc(lambda z: sp.expand(z))
ok = all(sp.expand(prod[i, j]).coeff(t, 2) == 0 and sp.expand(prod[i, j]).coeff(t, 1) == 0
         for i in range(3) for j in range(3))
check("A2c", ok, "second order: (delta + h)(E^T E) = 1 + O(t^3) with h = -tX + t^2(X^2 - eps^T eps); unit coupling persists beyond first order")

# A3 block 62 T2: plane wave positive branch, identity frame, Theta_ij = s_i s_j/|s|.
#    Fixed-state shift d<H> = sum E Theta with E = 1 - h/2 (symmetric tilt) = -(1/2) sum Theta h.
#    Matter on delta + a h: d omega = d sqrt(s^T (1 - a h) s) = -(a/2) s^T h s/|s|.
nrm = sp.sqrt(s1**2 + s2**2 + s3**2)
Theta = svec * svec.T / nrm
dH_walker = sum(Theta[i, j] * (-h[i, j] / 2) for i in range(3) for j in range(3))
dom_matter = sp.diff(sp.sqrt((svec.T * (sp.eye(3) - a_cpl * t * h) * svec)[0, 0]), t).subs(t, 0)
sol3 = sp.solve(sp.simplify(dH_walker - dom_matter).subs({h[0, 0]: 1, h[1, 1]: 0, h[2, 2]: 0,
                                                          h[0, 1]: 0, h[0, 2]: 0, h[1, 2]: 0, s1: 1, s2: 0, s3: 0}), a_cpl)
resid3 = sp.simplify((dH_walker - dom_matter).subs(a_cpl, 1))
check("A3", sol3 == [1] and resid3 == 0,
      "block 62's source -(1/2) sum Theta_(ij) h_ij is the metric-variational stress at unit strength: a_s = 1")

# A4/A5 bond couplings with the realisation B = -(a_R/2) h (uniform, phi_j = 1 at q = 0):
#   block 64 (one-step):  H(k) = sum_a sigma_a [ s_a + sum_j B_aj c_a s_j ]
#   block 73 (two-step):  H(k) = sum_a sigma_a [ s_a + sum_j B_aj c_a P_j ],  P_j = s_j c_j
k1, k2, k3, d1, d2, d3, aR, lam = sp.symbols('k1 k2 k3 d1 d2 d3 a_R lam', real=True)
kk = [k1, k2, k3]
sk = [sp.sin(x) for x in kk]
ck = [sp.cos(x) for x in kk]
Pk = [sk[i] * ck[i] for i in range(3)]


def h2_first_order(xvec, bond=True):
    B = -(aR / 2) * h
    vec = [sk[a] + lam * sum(B[a, j] * (ck[a] if bond else 1) * xvec[j] for j in range(3)) for a in range(3)]
    H2 = sum(v**2 for v in vec)
    return sp.expand(sp.diff(H2, lam).subs(lam, 0))


first_two = h2_first_order(Pk)
target_two = -aR * sum(Pk[i] * h[i, j] * Pk[j] for i in range(3) for j in range(3))
check("A5a", sp.simplify(first_two - sp.expand(target_two)) == 0,
      "two-step coupling: H^2 = |s|^2 - a_R P^T h P + O(h^2) at every wave vector (s_a c_a = P_a)")


def corner_form(first, K):
    # quadratic form in delta-k at the species corner K (entries 0 or pi)
    sub = {kk[i]: K[i] + [d1, d2, d3][i] * t for i in range(3)}
    ser = sp.series(first.subs(sub), t, 0, 3).removeO()
    return sp.expand(sp.expand(ser).coeff(t, 2))


dvec = sp.Matrix([d1, d2, d3])
first_site = h2_first_order(sk, bond=False)   # block 62 site frame E = 1 + B
first_one = h2_first_order(sk, bond=True)     # block 64 one-step bond coupling
ok_two = ok_site = ok_one = True
unit_species = {'site': 0, 'one-step': 0, 'two-step': 0}
for K in itertools.product([0, sp.pi], repeat=3):
    eta = [sp.cos(x) for x in K]
    q2 = corner_form(first_two, K)
    ok_two &= sp.simplify(q2 - sp.expand(-aR * (dvec.T * h * dvec)[0, 0])) == 0
    qs = corner_form(first_site, K)
    ok_site &= sp.simplify(qs - sp.expand(-aR * sum(eta[i] * dvec[i] * h[i, j] * eta[j] * dvec[j]
                                                     for i in range(3) for j in range(3)))) == 0
    q1 = corner_form(first_one, K)
    ok_one &= sp.simplify(q1 - sp.expand(-aR * sum(dvec[i] * h[i, j] * eta[j] * dvec[j]
                                                    for i in range(3) for j in range(3)))) == 0
    unit = sp.expand(-aR * (dvec.T * h * dvec)[0, 0])
    unit_species['two-step'] += int(sp.simplify(q2 - unit) == 0)
    unit_species['site'] += int(sp.simplify(qs - unit) == 0)
    unit_species['one-step'] += int(sp.simplify(q1 - unit) == 0)
check("A5b", ok_two,
      "two-step coupling at all eight species corners: H^2 = dk^T (1 - a_R h) dk + O(dk^3, h^2) -> a_s = a_R for every species")
check("A4", ok_site and ok_one and unit_species == {'site': 2, 'one-step': 1, 'two-step': 8},
      "species corners: site frame (block 62) sees eta h eta (diagonals unit, mixed off-diagonals flipped); "
      f"one-step bond (block 64) sees sym(h eta); species seeing exactly delta + a_R h: {unit_species}")
long_wave = sp.expand(sp.series(first_two.subs({k1: d1 * t, k2: d2 * t, k3: d3 * t}), t, 0, 3).removeO().coeff(t, 2))
check("A5c", sp.simplify(long_wave + aR * (dvec.T * h * dvec)[0, 0]) == 0,
      "long wavelength: the realisation's normalisation clause 'Lambda R(0) = 1' (block 120 note) is a_R = 1, i.e. a_s = 1")

# ============================================================================ PART B
print("== Part B: the member's lapse identity with K1 != K2 and source strength a_s")
p1, p2, p3 = sp.symbols('p1 p2 p3', real=True)
pv = sp.Matrix([p1, p2, p3])
pp = p1**2 + p2**2 + p3**2
K1, K2, al, be, a_s, u = sp.symbols('K1 K2 alpha beta a_s u', real=True)
Th, thv = symm('Th')


def R1(M):
    return pp * M.trace() - (pv.T * M * pv)[0, 0]


def R2(M):
    return (-(pp / 4) * (M.T * M).trace() + sp.Rational(1, 2) * ((M * pv).T * (M * pv))[0, 0]
            - sp.Rational(1, 2) * (pv.T * M * pv)[0, 0] * M.trace() + (pp / 4) * M.trace()**2)


# B1 relabelling invariance of R2 and transversality of its gradient
xi = sp.Matrix(sp.symbols('x1 x2 x3', real=True))
shift = pv * xi.T + xi * pv.T
inv_R2 = sp.expand(R2(h + shift) - R2(h))
inv_R1 = sp.expand(R1(shift))
grad = sp.Matrix(3, 3, lambda i, j: sp.diff(R2(h), hv[[0, 3, 4, 3, 1, 5, 4, 5, 2][3 * i + j]])
                 * (1 if i == j else sp.Rational(1, 2)))
transverse = sp.simplify(grad * pv)
check("B1", inv_R2 == 0 and inv_R1 == 0 and transverse == sp.zeros(3, 1),
      "R1, R2 invariant under h -> h + p xi + xi p; p_i dR2/dh_ij = 0 (block 62 T3(b))")

# Lagrangian on the 6 independent components (off-diagonals counted twice in traces)
hd = sp.Matrix(sp.symbols('hd11 hd22 hd33 hd12 hd13 hd23', real=True))
Hd = sp.Matrix([[hd[0], hd[3], hd[4]], [hd[3], hd[1], hd[5]], [hd[4], hd[5], hd[2]]])
eu = sp.Symbol('e_u', real=True)


def lapse_demand(beta_val):
    kin = al * (Hd * Hd).trace() + beta_val * Hd.trace()**2
    pot = K1 * u * R1(h) + K2 * R2(h) - eu * u + (a_s / 2) * (Th * h).trace()
    Mkin = sp.hessian(kin, list(hd))
    force = sp.Matrix([sp.diff(pot, c) for c in hv])
    hdd = Mkin.LUsolve(force)
    Hdd = sp.Matrix([[hdd[0], hdd[3], hdd[4]], [hdd[3], hdd[1], hdd[5]], [hdd[4], hdd[5], hdd[2]]])
    # lapse equation dL/du = K1 R1(h) - e_u = 0  =>  e_u'' = K1 R1(h'')
    return sp.simplify(K1 * R1(Hdd))


demand = lapse_demand(-al)
target = -(K1 * a_s / (4 * al)) * (pv.T * Th * pv)[0, 0]
resB2 = sp.simplify(demand - target)
check("B2", resB2 == 0 and not demand.has(K2) and not demand.has(u) and all(not demand.has(c) for c in hv),
      "at beta = -alpha: e_u'' = -(K1 a_s/(4 alpha)) p.Theta.p identically; no K2, no h, no u dependence")

demand_gen = lapse_demand(be)
resB3 = sp.simplify(demand_gen - target)
check("B3", resB3 != 0 and sp.simplify(resB3.subs(be, -al)) == 0,
      "control: for generic beta the identity acquires trace terms (vanishing only at beta = -alpha)")

# B4 TT cone with K2: p along 3, h11 = -h22 = A, h12 = B
Pz, A_, B_ = sp.symbols('P A B', real=True)
subsTT = {p1: 0, p2: 0, p3: Pz}
hTT = {hv[0]: A_, hv[1]: -A_, hv[2]: 0, hv[3]: B_, hv[4]: 0, hv[5]: 0}
R2TT = sp.expand(R2(h).subs(subsTT).subs(hTT))
kinTT = sp.expand((al * (Hd * Hd).trace() + be * Hd.trace()**2).subs(
    {hd[0]: sp.Symbol('Ad'), hd[1]: -sp.Symbol('Ad'), hd[2]: 0, hd[3]: sp.Symbol('Bd'), hd[4]: 0, hd[5]: 0}))
MA = sp.diff(kinTT, sp.Symbol('Ad'), 2)
QA = sp.diff(K2 * R2TT, A_, 2)
om2 = sp.simplify(-QA / MA)
R1TT = sp.simplify(R1(h).subs(subsTT).subs(hTT))
check("B4", sp.simplify(om2 - K2 * Pz**2 / (4 * al)) == 0 and R1TT == 0,
      f"TT disturbance: omega^2 = {om2} (K1 does not enter: R1 vanishes on TT)")

# B5 canonical rescaling Phi_rho (h = rho h', P = P'/rho): K1 -> rho K1, K2 -> rho^2 K2,
#    alpha -> rho^2 alpha, a_s -> rho a_s.  Verify by substituting into the action.
rho = sp.Symbol('rho', positive=True)
hp, hpv = symm('hp')
hdp = sp.Matrix(sp.symbols('hpd11 hpd22 hpd33 hpd12 hpd13 hpd23', real=True))
Hdp = sp.Matrix([[hdp[0], hdp[3], hdp[4]], [hdp[3], hdp[1], hdp[5]], [hdp[4], hdp[5], hdp[2]]])


def action(Hm, Hdm, k1, k2, alpha_, asv):
    return (alpha_ * (Hdm * Hdm).trace() - alpha_ * Hdm.trace()**2 + k1 * u * R1(Hm) + k2 * R2(Hm)
            + (asv / 2) * (Th * Hm).trace())


Lold = action(rho * hp, rho * Hdp, K1, K2, al, a_s)
Lnew = action(hp, Hdp, rho * K1, rho**2 * K2, rho**2 * al, rho * a_s)
check("B5a", sp.expand(Lold - Lnew) == 0,
      "Phi_rho: the member+source in h = rho h' is the member+source in h' with (rho K1, rho^2 K2, rho^2 alpha, rho a_s)")
inv = {
    'K1 a_s/alpha (lapse identity, B2)': K1 * a_s / al,
    'K2/alpha (TT cone, B4)': K2 / al,
    'K1 a_s/K2': K1 * a_s / K2,
    'K1/K2': K1 / K2,
    'a_s': a_s,
}
scal = {K1: rho * K1, K2: rho**2 * K2, al: rho**2 * al, a_s: rho * a_s}
inv_status = {name: sp.simplify(expr.subs(scal, simultaneous=True) / expr) == 1 for name, expr in inv.items()}
check("B5b", inv_status == {'K1 a_s/alpha (lapse identity, B2)': True, 'K2/alpha (TT cone, B4)': True,
                            'K1 a_s/K2': True, 'K1/K2': False, 'a_s': False},
      f"invariance under Phi_rho: {inv_status}")

# B6 static pull with separate K1, K2 (block 62 T5(c) generalised): Theta = 0, source e on the clock.
#    u-equation K1 R1(h) = e; h-equation K1 u grad R1 + K2 grad R2 = 0.  Isotropic representative h = 2 lam delta.
lam_s, e_s = sp.symbols('lam e', real=True)
hiso = {hv[0]: 2 * lam_s, hv[1]: 2 * lam_s, hv[2]: 2 * lam_s, hv[3]: 0, hv[4]: 0, hv[5]: 0}
potS = K1 * u * R1(h) + K2 * R2(h) - e_s * u
eqs = [sp.diff(potS, u).subs(hiso)] + [sp.expand(sp.diff(potS, c).subs(hiso)) for c in hv]
solS = sp.solve(eqs, [lam_s, u], dict=True)
ok6 = (len(solS) == 1 and sp.simplify(solS[0][lam_s] - e_s / (4 * K1 * pp)) == 0
       and sp.simplify(solS[0][u] + (K2 / K1) * solS[0][lam_s]) == 0)
# matter on spatial metric delta + a_s h = (1 + 2 a_s lam) delta and clock 1 + u: gamma = a_s lam / (-u)
gam = sp.simplify(a_s * solS[0][lam_s] / (-solS[0][u])) if ok6 else None
gam_inv = sp.simplify(gam.subs(scal, simultaneous=True) - gam) == 0 if ok6 else False
check("B6", ok6 and sp.simplify(gam - a_s * K1 / K2) == 0 and gam_inv,
      f"static pull: lam = e/(4 K1 p^2), u = -(K2/K1) lam; the matter's space/time curvature ratio gamma = {gam} "
      "(Phi_rho-invariant); block 62 (K1 = K2, a_s = 1) gives gamma = 1")

# ============================================================================ PART C
print("== Part C: R1, R2 are the expansion of sqrt(g) R for g = delta + h (plane-wave route)")
x1, x2, x3 = sp.symbols('y1 y2 y3', real=True)
X3 = [x1, x2, x3]
ep = sp.Symbol('ep')
Amp, av = symm('A')
# a fixed rational wave vector and rational amplitudes keep this fast and exact
pnum = [1, 2, 2]
phase = sum(pnum[i] * X3[i] for i in range(3))


def sqrtgR_series(Amat):
    hx = Amat * sp.cos(phase)
    g = sp.eye(3) + ep * hx
    ginv = sp.eye(3) - ep * hx + ep**2 * hx * hx
    detg = g.det()
    sqrtg = sp.series(sp.sqrt(detg), ep, 0, 3).removeO()
    dg = [[[sp.diff(g[i, j], X3[k]) for k in range(3)] for j in range(3)] for i in range(3)]
    Gam = [[[sp.expand(sum(ginv[l, m] * (dg[m][i][j] + dg[m][j][i] - dg[i][j][m]) for m in range(3)) / 2)
             for j in range(3)] for i in range(3)] for l in range(3)]
    Ric = 0
    for i in range(3):
        for j in range(3):
            rij = 0
            for l in range(3):
                rij += sp.diff(Gam[l][i][j], X3[l]) - sp.diff(Gam[l][i][l], X3[j])
                for m in range(3):
                    rij += Gam[l][l][m] * Gam[m][i][j] - Gam[l][j][m] * Gam[m][i][l]
            Ric += ginv[i, j] * rij
    dens = sp.expand(sp.series(sp.expand(sqrtg * Ric), ep, 0, 3).removeO())
    return dens.coeff(ep, 1), dens.coeff(ep, 2)


def period_average(expr):
    # average over the plane-wave phase: substitute y = (theta, 0, 0)/... -> expression depends on phase only
    th = sp.Symbol('th')
    e = sp.expand(expr.subs({x1: th, x2: 0, x3: 0}))  # phase = th since pnum[0] = 1
    return sp.simplify(sp.integrate(e, (th, 0, 2 * sp.pi)) / (2 * sp.pi))


pnv = sp.Matrix(pnum)
ppn = sum(c**2 for c in pnum)
ok1, ratios = True, []
for trial in [(1, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0), (2, -1, 3, 1, -2, 1), (1, 1, -2, 0, 1, 0)]:
    Am = sp.Matrix([[trial[0], trial[3], trial[4]], [trial[3], trial[1], trial[5]], [trial[4], trial[5], trial[2]]])
    first, second = sqrtgR_series(Am)
    R1num = ppn * Am.trace() - (pnv.T * Am * pnv)[0, 0]
    ok1 &= sp.simplify(first - R1num * sp.cos(phase)) == 0
    R2num = (-(ppn / sp.Integer(4)) * (Am.T * Am).trace() + sp.Rational(1, 2) * ((Am * pnv).T * (Am * pnv))[0, 0]
             - sp.Rational(1, 2) * (pnv.T * Am * pnv)[0, 0] * Am.trace() + (ppn / sp.Integer(4)) * Am.trace()**2)
    avg2 = period_average(second)
    ratios.append((avg2, R2num))
check("C1", ok1, "order-1 part of sqrt(g)R[delta + h] is R1(h) pointwise (unit coefficient), four amplitudes at p = (1,2,2)")
# a trial with R2(A) = 0 must also have zero average (run1 harness bug: 0/0 was scored as a failure)
rat = [sp.nsimplify(a / b) if b != 0 else ('0=0' if a == 0 else 'inf') for a, b in ratios]
check("C2", all(r == sp.Rational(1, 2) or r == '0=0' for r in rat) and sum(r == sp.Rational(1, 2) for r in rat) >= 3,
      f"period average of the order-2 part / block-62 R2(A) = {rat} (1/2 = <cos^2>): R2 is [sqrt(g)R]^(2) of delta + h")

print(f"TOTAL: PASS={sum(ok for _, ok in RESULTS)} FAIL={sum(not ok for _, ok in RESULTS)}  ({time.time() - T0:.1f} s)")
sys.exit(0 if all(ok for _, ok in RESULTS) else 1)
