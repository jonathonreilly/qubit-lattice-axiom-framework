#!/usr/bin/env python3
"""R18-11 [1]-[4]: per-mode O(G noise^2) mean source of E1 + N_c, Poisson-gauge law vs harmonic-gauge law.

Setting (G = c = 1, kappa = 8 pi): Minkowski background, eta = diag(-1,1,1,1), coordinates (t,x,y,z).
One frame mode theta = k z - w t of the recorded noise J^{mu nu} (flat-conserved), amplitudes on cos(theta).
Free data (R15-2 Lemma A): rho = J^00 (S), Tp = transverse trace (S), j = J^0x (V), tp = TT plus amplitude.
Derived by flat conservation: J^0z = x rho, J^zz = x^2 rho, J^zx = x j, with x = w/k.

Law (R18-7 section 3, readout gauge varied):  G_{mu nu}[g] = 8 pi T_eff_{mu nu},
   T^{ab} = (-g)^{a/4 - 1} J^{ab}  (insertion family: a = 4 meter measures T; a = 0 meter measures (-g)T;
   a = 2 tensor density), + K (conserving completion; its homogeneous mean is fixed separately, see [3]).
Second-order mean source (coarse-grained, per mode):  tau_{mu nu} = <T^(2)_{mu nu}> - <G^(2)_{mu nu}[h1,h1]>/(8 pi).
Long-wave active density (Raychaudhuri / R_00 of the long-wave metric):  rho_act = tau_00 + tau_kk.
Subtraction: none; every mean is the theta-average of an exact second-order expansion.
"""
import sympy as sp, time
t0 = time.time()
w, k = sp.symbols('omega k', positive=True)
a = sp.Symbol('a')
eps = sp.Symbol('epsilon')
c, s = sp.symbols('c s')        # cos(theta), sin(theta)
x = w / k

def dth(f):
    f = sp.expand(f)
    return sp.diff(f, c) * (-s) + sp.diff(f, s) * c
def D(mu, f):
    # partial derivative along coordinate mu of a function of theta = k z - w t
    if mu == 0:
        return -w * dth(f)
    if mu == 3:
        return k * dth(f)
    return sp.Integer(0)
def avg(expr):
    """theta-average of a polynomial in c, s (c^2 + s^2 = 1)."""
    p = sp.Poly(sp.expand(expr), c, s)
    out = 0
    for (i, j), coef in p.terms():
        if i % 2 or j % 2:
            continue
        # <c^i s^j> for even i, j up to degree 4
        m = {(0, 0): 1, (2, 0): sp.Rational(1, 2), (0, 2): sp.Rational(1, 2), (4, 0): sp.Rational(3, 8),
             (0, 4): sp.Rational(3, 8), (2, 2): sp.Rational(1, 8)}[(i, j)]
        out += coef * m
    return sp.simplify(out)

eta = sp.diag(-1, 1, 1, 1)

def einstein_to_2(h):
    """G_{mu nu} of g = eta + eps h to O(eps^2); h a 4x4 sympy Matrix of polynomials in c, s."""
    g = eta + eps * h
    hu = eta * h * eta                       # h^{mu nu}
    ginv = eta - eps * hu + eps**2 * hu * eta * h * eta   # inverse to O(eps^2)
    n = 4
    dg = [[[D(l, g[m, nn]) for l in range(n)] for nn in range(n)] for m in range(n)]   # dg[m][nn][l] = d_l g_{m nn}
    Gam = [[[0]*n for _ in range(n)] for _ in range(n)]
    for al in range(n):
        for m in range(n):
            for nn in range(m, n):
                val = 0
                for b in range(n):
                    if ginv[al, b] == 0:
                        continue
                    val += ginv[al, b] * (dg[b][m][nn] + dg[b][nn][m] - dg[m][nn][b])
                val = sp.expand(val / 2)
                val = sum(val.coeff(eps, p) * eps**p for p in (1, 2))
                Gam[al][m][nn] = val; Gam[al][nn][m] = val
    Ric = sp.zeros(n, n)
    for m in range(n):
        for nn in range(m, n):
            val = 0
            for al in range(n):
                val += D(al, Gam[al][m][nn]) - D(nn, Gam[al][m][al])
                for b in range(n):
                    val += Gam[al][al][b] * Gam[b][m][nn] - Gam[al][nn][b] * Gam[b][m][al]
            val = sp.expand(val)
            val = sum(val.coeff(eps, p) * eps**p for p in (1, 2))
            Ric[m, nn] = val; Ric[nn, m] = val
    R = sp.expand(sum(ginv[m, nn] * Ric[m, nn] for m in range(n) for nn in range(n)))
    R = sum(R.coeff(eps, p) * eps**p for p in (1, 2))
    Gt = [[None]*n for _ in range(n)]
    for m in range(n):
        for nn in range(n):
            val = sp.expand(Ric[m, nn] - g[m, nn] * R / 2)
            Gt[m][nn] = [val.coeff(eps, 1), val.coeff(eps, 2)]
    return Gt

# ---------------- sources ----------------
rho, Tp, jx, tp = sp.symbols('rho T_perp j t_p', real=True)
def J_upper(rho, Tp, jx, tp):
    J = sp.zeros(4, 4)
    J[0, 0] = rho; J[0, 3] = J[3, 0] = x * rho; J[3, 3] = x**2 * rho
    J[0, 1] = J[1, 0] = jx; J[1, 3] = J[3, 1] = x * jx
    J[1, 1] = Tp / 2 + tp; J[2, 2] = Tp / 2 - tp
    return J * c          # all channels in phase on cos(theta)

# ---------------- [1] linear Poisson-gauge solution ----------------
Phc, Phs, Psc, Pss, Sxc, Sxs, hpc, hps = sp.symbols('Phc Phs Psc Pss Sxc Sxs hpc hps', real=True)
def h_poisson(Phi, Psi, Sx, hp):
    h = sp.zeros(4, 4)
    h[0, 0] = -2 * Phi
    h[0, 1] = h[1, 0] = Sx
    for i in (1, 2, 3):
        h[i, i] = -2 * Psi
    h[1, 1] += hp; h[2, 2] += -hp
    return h
hP_trial = h_poisson(Phc*c + Phs*s, Psc*c + Pss*s, Sxc*c + Sxs*s, hpc*c + hps*s)
Jup = J_upper(rho, Tp, jx, tp)
Jlow = eta * Jup * eta
print("[1] Poisson gauge: Phi, Psi instantaneous (S), S_x (V), h_+ (TT); solve G^(1) = 8 pi J_low per mode")
G1 = einstein_to_2(hP_trial)
eqs = []
for m in range(4):
    for nn in range(m, 4):
        e = sp.expand(G1[m][nn][0] - 8 * sp.pi * Jlow[m, nn])
        eqs += [e.coeff(c, 1).coeff(s, 0), e.coeff(s, 1).coeff(c, 0)]
eqs = [sp.simplify(e) for e in eqs if sp.simplify(e) != 0]
solP = sp.solve(eqs, [Phc, Phs, Psc, Pss, Sxc, Sxs, hpc, hps], dict=True)
assert len(solP) == 1, solP
solP = {kk: sp.simplify(v) for kk, v in solP[0].items()}
for kk in (Phc, Psc, Sxc, hpc):
    print("    %s = %s" % (kk, sp.factor(solP[kk])))
print("    sin amplitudes:", [sp.simplify(solP[kk]) for kk in (Phs, Pss, Sxs, hps)], "(all channels in phase)")
print("    residual of all 10 linear equations:", [sp.simplify(e.subs(solP)) for e in eqs].count(0), "of", len(eqs), "vanish")
hP = hP_trial.subs(solP)

# ---------------- harmonic-gauge (Lorenz) linear solution: hbar^{mu nu} = 16 pi J^{mu nu}/(k^2 - w^2) ----------------
hbar = 16 * sp.pi * Jup / (k**2 - w**2)
hbar_low = eta * hbar * eta
trb = sum(eta[i, i] * hbar_low[i, i] for i in range(4))
hH = sp.simplify(hbar_low - eta * trb / 2)
G1H = einstein_to_2(hH)
resH = [sp.simplify(G1H[m][nn][0] - 8 * sp.pi * Jlow[m, nn]) for m in range(4) for nn in range(4)]
print("    harmonic law check: G^(1)[h_H] - 8 pi J vanishes in", resH.count(0), "of 16 components")

# ---------------- [2] second-order mean source per mode ----------------
def mean_tau(h, label):
    G = einstein_to_2(h)
    hu_tr = sp.expand(sum(eta[i, i] * h[i, i] for i in range(4)))   # eta^{mu nu} h_{mu nu} = (-g)^(1)
    Tl = sp.zeros(4, 4)
    for m in range(4):
        for nn in range(4):
            val = (a / 4 - 1) * hu_tr * Jlow[m, nn]
            for al in range(4):
                for b in range(4):
                    # T_{mn} = g_{m al} g_{n b} T^{al b}; O(eps^2): h_{m al} eta_{n b} J^{al b} + eta_{m al} h_{n b} J^{al b}
                    val += h[m, al] * eta[nn, b] * Jup[al, b] + eta[m, al] * h[nn, b] * Jup[al, b]
            Tl[m, nn] = val
    tau = sp.zeros(4, 4)
    for m in range(4):
        for nn in range(4):
            tau[m, nn] = sp.simplify(avg(Tl[m, nn]) - avg(G[m][nn][1]) / (8 * sp.pi))
    return tau

u1 = sp.pi * rho**2 / k**2          # per-mode <|grad Psi|^2>/(8 pi) of the rho channel (cos amplitude): pi rho^2 / k^2
out = {}
for h, lab in ((hP, "Poisson law"), (hH, "harmonic law")):
    tau = mean_tau(h, lab)
    t00 = sp.factor(sp.expand(tau[0, 0])); tkk = sp.factor(sp.expand(tau[1, 1] + tau[2, 2] + tau[3, 3]))
    off = [sp.simplify(tau[0, i]) for i in (1, 2, 3)]
    out[lab] = (t00, tkk, tau)
    print("\n[2] %s: per-mode mean source (all channels in phase; quadratic form in rho, T_perp, j, t_p)" % lab)
    print("    tau_00 =", t00)
    print("    tau_kk =", tkk)
    print("    tau_0i (momentum; nonzero means a mean energy flux along k) =", off)

# ---------------- [3] checks against R18-7 (static, rho only) and the a-dependence ----------------
print("\n[3] static limit w -> 0, rho channel only, in units of the per-mode u1 = pi rho^2/k^2")
for lab in out:
    t00, tkk, _ = out[lab]
    s00 = sp.simplify(t00.subs({Tp: 0, jx: 0, tp: 0}).subs(w, 0) / u1)
    skk = sp.simplify(tkk.subs({Tp: 0, jx: 0, tp: 0}).subs(w, 0) / u1)
    print("    %-12s: tau_00/u1 = %s ; tau_kk/u1 = %s ; (tau_00 + tau_kk)/u1 = %s   [R18-7: 2a-7, -1, 2a-8]"
          % (lab, sp.expand(s00), sp.expand(skk), sp.expand(s00 + skk)))
print("\n    rho channel only, general x = w/k (time-dependent), units u1:")
for lab in out:
    t00, tkk, _ = out[lab]
    s00 = sp.factor(sp.simplify(t00.subs({Tp: 0, jx: 0, tp: 0}) / u1).subs(w, x * k).subs(x, sp.Symbol('x')))
    skk = sp.factor(sp.simplify(tkk.subs({Tp: 0, jx: 0, tp: 0}) / u1))
    print("    %-12s: tau_00/u1 = %s" % (lab, sp.factor(sp.simplify(t00.subs({Tp: 0, jx: 0, tp: 0}) / u1))))
    print("    %-12s: tau_kk/u1 = %s" % (lab, skk))
    print("    %-12s: d(tau_kk)/da /u1 = %s ; d(tau_00)/da /u1 = %s" % (lab, sp.factor(sp.diff(skk, a)),
          sp.factor(sp.diff(sp.simplify(t00.subs({Tp: 0, jx: 0, tp: 0}) / u1), a))))
print("\n    law difference (Poisson - harmonic), rho channel, units u1:")
d00 = sp.factor(sp.simplify((out["Poisson law"][0] - out["harmonic law"][0]).subs({Tp: 0, jx: 0, tp: 0}) / u1))
dkk = sp.factor(sp.simplify((out["Poisson law"][1] - out["harmonic law"][1]).subs({Tp: 0, jx: 0, tp: 0}) / u1))
print("    Delta tau_00/u1 =", d00); print("    Delta tau_kk/u1 =", dkk)

# ---------------- [4] channel-resolved coefficients of the Poisson law (for the spectral integral) ----------------
print("\n[4] Poisson law, coefficients of the quadratic form (units: 1/k^2), as functions of x = w/k and a")
X = sp.Symbol('x', positive=True)
t00, tkk, tau = out["Poisson law"]
mons = [rho**2, rho*Tp, Tp**2, jx**2, tp**2, rho*jx, Tp*jx, rho*tp, Tp*tp, jx*tp]
for lab, ex in (("tau_00", t00), ("tau_kk", tkk)):
    P = sp.Poly(sp.expand(ex * k**2), rho, Tp, jx, tp)
    for mon in mons:
        cf = P.coeff_monomial(mon)
        cf = sp.factor(sp.simplify(sp.sympify(cf).subs(w, X * k)))
        print("    %s [%s] = %s" % (lab, mon, cf))
print("\nruntime %.1f s" % (time.time() - t0))
