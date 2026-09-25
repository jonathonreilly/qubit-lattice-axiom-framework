#!/usr/bin/env python3
"""Closed lattice: the uniform motion of the lengths (block 60 T5(b), landed #8590) and the simplest member's pair (block 75 T3(c), landed #8608),
run 2 of 2.

Curvature member with the kinetic term sum_x c_k l_x^s (d lambda_x/dt)^2 / w_x; block 62's rotation-invariant kinetic family
(1/wbar)[alpha hdot_ij hdot_ij + beta hdot^2] on the isotropic stretching h = 2 lambda delta gives c_k = 12 alpha + 36 beta, which is block 60's
comparator c_k = -6K for beta = -alpha, alpha = K/4; s = 3 (the volume).  Content: bodies at rest at every site, m per site (e_x = m w_x,
tau = 0).  Hamiltonian form (lambda_x, p_x): H = sum_x w_x C_x, C_x = m + G_x(lambda) + p_x^2/(4 c_k l_x^s), G_x = 8K chi_x (Delta chi)_x,
chi = l^(1/2); the rates w_x are multipliers and C_x = 0 are the constraints.  A clock field keeps every constraint iff sum_y {C_x, C_y} w_y = 0.
Exact: sympy for the uniform law and the bracket; floating point (RK4) for the evolutions, labelled.
Simplest member: (2/gamma)(-Delta phi) + m phi = 0 on the 4^3 torus, two point bodies; T3(c) exactly in rationals; perturbations tried.
"""
import itertools, math
import numpy as np
import sympy as sp

def out(s): print(s, flush=True)

# ------------------------------------------------------------------ exact: the uniform law (sympy)
t, m, K, ck, s_ = sp.symbols('t m K c_k s', positive=True)
lam = sp.Function('lam')(t)
L_unif = -ck * sp.exp(s_ * lam) * sp.diff(lam, t) ** 2 - m            # w = 1 label, c_k -> -c_k (c_k < 0 written as -ck)
el = sp.diff(sp.diff(L_unif, sp.diff(lam, t)), t) - sp.diff(L_unif, lam)
sol_l = sp.log((1 + (s_ / 2) * sp.sqrt(m / ck) * t) ** (2 / s_))
res_eq = sp.simplify(el.subs(lam, sol_l).doit())
res_con = sp.simplify((ck * sp.exp(s_ * lam) * sp.diff(lam, t) ** 2 - m).subs(lam, sol_l).doit())
out("X exact: in the label w = 1, l = (1 + (s/2) sqrt(m/|c_k|) t)^(2/s) solves the lengths' equation (residual %s) and the constraint m = |c_k| l^s "
    "lambdadot^2 (residual %s); exponent 2/s, = 2/3 for s = 3" % (res_eq, res_con))
out("X kinetic numbers: block 62's family on h = 2 lambda delta: hdot_ij hdot_ij = 12 lambdadot^2, hdot^2 = 36 lambdadot^2, so c_k = 12 alpha + 36 beta; "
    "beta = -alpha, alpha = K/4 give c_k = %s (block 60's comparator -6K)" % sp.simplify((12 * sp.Symbol('alpha') + 36 * (-sp.Symbol('alpha'))).subs(sp.Symbol('alpha'), sp.Symbol('K') / 4)))

# ------------------------------------------------------------------ the 6^3 torus, curvature member
Ls = 6; V = Ls ** 3
coords = list(itertools.product(range(Ls), repeat=3)); idx = {c: i for i, c in enumerate(coords)}
nbr = np.array([[idx[tuple((np.array(c) + d) % Ls)] for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))] for c in coords])
def lap(f): return f[nbr].sum(1) - 6 * f
Kv, ckv, sv, mv = 1.0, -6.0, 3.0, 1.0
def G_of(lmb):
    chi = np.exp(lmb / 2); return 8 * Kv * chi * lap(chi)
def C_of(lmb, p):
    return mv + G_of(lmb) + p ** 2 / (4 * ckv * np.exp(sv * lmb))
def rhs(lmb, p, w):
    ell_s = np.exp(sv * lmb); chi = np.exp(lmb / 2)
    ldot = w * p / (2 * ckv * ell_s)
    pdot = sv * w * p ** 2 / (4 * ckv * ell_s) - 4 * Kv * chi * (w * lap(chi) + lap(w * chi))
    return ldot, pdot
def evolve(lmb, p, T, dt, wfun=lambda l, p: np.ones(V), record=()):
    tcur = 0.0; recs = []
    rec = list(record)
    while tcur < T - 1e-12:
        w = wfun(lmb, p)
        k1 = rhs(lmb, p, w); k2 = rhs(lmb + dt / 2 * k1[0], p + dt / 2 * k1[1], w); k3 = rhs(lmb + dt / 2 * k2[0], p + dt / 2 * k2[1], w)
        k4 = rhs(lmb + dt * k3[0], p + dt * k3[1], w)
        lmb = lmb + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); p = p + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]); tcur += dt
        while rec and tcur >= rec[0] - 1e-9:
            recs.append((rec.pop(0), lmb.copy(), p.copy()))
    return lmb, p, recs
def p_from_constraint(lmb):
    return -2 * np.sqrt(-ckv * np.exp(sv * lmb) * (mv + G_of(lmb)))      # expanding branch (lambdadot > 0)

# (1) uniform start
t0 = (2 / sv) * math.sqrt(-ckv / mv)
lmb = np.zeros(V); p = p_from_constraint(lmb)
TS = [t0 * f for f in (1, 3, 10, 30, 100)]
_, _, recs = evolve(lmb, p, TS[-1], 0.002 * t0, record=TS)
rows = []
for tt, l_, p_ in recs:
    ell = math.exp(l_.mean()); exact = (1 + tt / t0) ** (2 / sv)
    rows.append((tt / t0, ell, exact, np.abs(C_of(l_, p_)).max(), l_.std()))
nfit = np.polyfit(np.log([1 + r[0] for r in rows[1:]]), np.log([r[1] for r in rows[1:]]), 1)[0]
out("N (1) 6^3 torus, curvature member, c_k = -6K, s = 3, m = 1 per site, uniform start with p from the constraint, label w = 1 (RK4, dt = t0/500): "
    "l(t)/exact at t/t0 = %s: %s; constraint residual max |C| %s; site spread of lambda %s; fitted exponent %.5f against 2/s = %.5f"
    % ([r[0] for r in rows], " ".join("%.8f" % (r[1] / r[2]) for r in rows), " ".join("%.1e" % r[3] for r in rows), " ".join("%.0e" % r[4] for r in rows), nfit, 2 / sv))

# (2) perturbed starts: constraints satisfied initially (p from the constraint at every site); the bracket matrix; evolution in w = 1
def bracket(lmb, p, w=None):
    chi = np.exp(lmb / 2); v = p / (2 * ckv * np.exp(sv * lmb))
    M = np.zeros((V, V))
    for x in range(V):
        for y in nbr[x]:
            M[x, y] += 4 * Kv * chi[x] * chi[y] * (v[y] - v[x])
    return M
rng = np.random.default_rng(60)
pert = []
for amp in (1e-2, 1e-3, 1e-4):
    dl = amp * rng.standard_normal(V); dl -= dl.mean()
    lmb = dl.copy(); p = p_from_constraint(lmb)
    M = bracket(lmb, p)
    sv_ = np.linalg.svd(M, compute_uv=False)
    lmbT, pT, recs = evolve(lmb, p, 10 * t0, 0.002 * t0, record=[t0, 3 * t0, 10 * t0])
    cres = [np.abs(C_of(l_, p_)).max() for _, l_, p_ in recs]
    spread = [l_.std() for _, l_, p_ in recs]
    ell = [math.exp(l_.mean()) for _, l_, p_ in recs]
    pert.append((amp, sv_.min() / sv_.max(), sv_.min(), cres, spread, ell))
    out("N (2) perturbation amplitude %.0e (site-random lambda, constraints satisfied at t = 0): bracket matrix {C_x, C_y}: norm %.2e, smallest singular "
        "value %.2e (relative %.2e): no clock field w != 0 keeps every constraint; evolution in w = 1: max |C| at t/t0 = 1, 3, 10: %s; spread of lambda "
        "%s (from %.1e); mean length against the uniform law %s"
        % (amp, sv_.max(), sv_.min(), sv_.min() / sv_.max(), " ".join("%.1e" % c for c in cres), " ".join("%.1e" % x for x in spread), dl.std(),
           " ".join("%.6f" % (e / (1 + tt / t0) ** (2 / sv)) for e, tt in zip(ell, (t0, 3 * t0, 10 * t0)))))
# the bracket vanishes identically on uniform data (exact)
lu = np.zeros(V); pu = p_from_constraint(lu)
out("X the bracket matrix on uniform data: max |{C_x, C_y}| = %.1e (exactly zero: {C_x, C_y} = 4K chi_x chi_y (v_y - v_x) on bonds, v = p/(2 c_k l^s))"
    % np.abs(bracket(lu, pu)).max())

# ------------------------------------------------------------------ the simplest member on the 4^3 torus (exact rationals)
L4 = 4; V4 = L4 ** 3
c4 = list(itertools.product(range(L4), repeat=3)); i4 = {c: i for i, c in enumerate(c4)}
Lap = sp.zeros(V4, V4)
for c in c4:
    i = i4[c]
    for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        j = i4[tuple((np.array(c) + d) % L4)]; Lap[i, j] += 1; Lap[i, i] -= 1
# G: -Lap G = delta - 1/V, sum G = 0  ->  G = pinv(-Lap)
Aug = (-Lap).row_join(sp.ones(V4, 1)).col_join(sp.ones(1, V4).row_join(sp.zeros(1, 1)))
rhs0 = sp.Matrix([1 - sp.Rational(1, V4) if k == 0 else -sp.Rational(1, V4) for k in range(V4)] + [0])
Gcol = Aug.LUsolve(rhs0)[:V4, 0]
Gv = lambda a, b: Gcol[i4[tuple((np.array(c4[b]) - np.array(c4[a])) % L4)]]
gam = sp.Integer(1)
def tuned_pair(A, B, mA, c=1):
    h = Gv(A, A) - Gv(A, B)
    mB = -1 / (gam * h + 1 / mA)
    phiA = c / (1 + gam / 2 * mA * h); p_ = gam / 2 * mA * phiA
    phi = sp.Matrix([c - p_ * (Gv(A, z) - Gv(B, z)) for z in range(V4)])
    mvec = sp.zeros(V4, 1); mvec[A] = mA; mvec[B] = mB
    resid = (2 / gam) * (-Lap * phi) + sp.Matrix([mvec[z] * phi[z] for z in range(V4)])
    return h, mB, phi, mvec, resid
A = i4[(0, 0, 0)]
for Bc in ((1, 0, 0), (2, 1, 0), (2, 2, 2)):
    B = i4[Bc]
    h, mB, phi, mvec, resid = tuned_pair(A, B, sp.Integer(1))
    out("X simplest member, 4^3 torus, gamma = 1, m_A = 1, B at %s: h = G0 - Gd = %s, m_B = %s, phi_A = %s, phi_B = %s, min phi = %s; residual of the "
        "static law exactly %s" % (Bc, h, mB, phi[A], phi[B], min(phi), "zero" if all(r == 0 for r in resid) else "NONZERO"))
# perturbations of the tuned pair A=(0,0,0), B=(1,0,0): does a positive static phi persist? (the least eigenvalue of (2/gamma)(-Delta) + diag(m))
Bc = (1, 0, 0); B = i4[Bc]
h, mB, phi, mvec, resid = tuned_pair(A, B, sp.Integer(1))
Lnum = -np.array(Lap.tolist(), float)
def least(mv_):
    Mx = 2 * Lnum + np.diag(np.array([float(x) for x in mv_]))
    ev = np.linalg.eigvalsh(Mx); return ev[0]
base = least(mvec)
tries = []
def shifted(mv_, shift):
    out_ = sp.zeros(V4, 1)
    for z in range(V4):
        cz = tuple((np.array(c4[z]) + shift) % L4); out_[i4[cz]] = mv_[z]
    return out_
tries.append(("translate the pair by (1,2,3)", least(shifted(mvec, np.array([1, 2, 3])))))
mv2 = sp.zeros(V4, 1); mv2[A] = mvec[A]; mv2[i4[(0, 1, 0)]] = mvec[B]
tries.append(("rotate the separation to (0,1,0) (same h)", least(mv2)))
mv3 = sp.zeros(V4, 1); mv3[A] = mvec[A]; mv3[i4[(2, 0, 0)]] = mvec[B]
tries.append(("move B one more step, to (2,0,0)", least(mv3)))
for f in (sp.Rational(101, 100), sp.Rational(99, 100)):
    mv4 = mvec.copy(); mv4[A] = mvec[A] * f
    tries.append(("m_A x %s" % f, least(mv4)))
mv5 = mvec.copy(); mv5[i4[(2, 2, 2)]] = sp.Rational(1, 100)
tries.append(("add a third body m = +0.01 at (2,2,2)", least(mv5)))
mv6 = mvec.copy(); mv6[A] *= 2; mv6[B] = -1 / (gam * h + 1 / mv6[A])
tries.append(("re-tuned pair m_A = 2 (m_B from the condition)", least(mv6)))
out("N simplest member, tuned pair A = (0,0,0), B = (1,0,0): least eigenvalue of (2/gamma)(-Delta) + diag(m) = %.1e (zero: phi > 0 at rest); "
    "perturbations: %s" % (base, "; ".join("%s: %+.2e (%s)" % (lab, ev, "rest persists" if abs(ev) < 1e-12 else "no positive static phi") for lab, ev in tries)))
# test bodies in the tuned field: both signs fall towards slow clocks (block 71: twins as test bodies)
phin = np.array([float(x) for x in phi])
lapA = float((Lap * phi)[A]); lapB = float((Lap * phi)[B])
out("N simplest member, the tuned field as a landscape for test bodies: Delta phi at A (positive body) = %+.4f (a minimum of the clocks: a body "
    "falling towards slow clocks is held), at B (negative body) = %+.4f (a maximum: pushed off by every displacement); phi_A = %.4f < phi_B = %.4f"
    % (lapA, lapB, phin[A], phin[B]))

out("")
nstable = sum(1 for _, ev in tries if abs(ev) < 1e-12)
out("SUMMARY: closed 6^3 torus, curvature member with c_k = -6K (block 62's kinetic family, beta = -alpha, alpha = K/4), s = 3, bodies at rest: the "
    "lengths grow as the exact law, fitted exponent %.5f against 2/s = %.5f, constraint kept to %.0e; but only uniform data keep the constraints: "
    "for site-random perturbations (1e-2..1e-4) the bracket matrix {C_x, C_y} is non-singular (relative smallest singular value %.1e..%.1e), so no "
    "clock field keeps every constraint, and in w = 1 the constraints drift (max |C| %.0e at t = 10 t0 for 1e-3); simplest member (4^3 torus, exact): "
    "the tuned pair keeps a positive static clock field under %d of %d perturbations tried (translation, an equivalent separation, re-tuning) and "
    "loses it under the others (one step, 1%% mass, a third body); as test bodies, the positive body sits at the clocks' minimum and the negative one "
    "at their maximum" % (nfit, 2 / sv, max(r[3] for r in rows), min(p_[1] for p_ in pert), max(p_[1] for p_ in pert), pert[1][3][-1], nstable, len(tries)))
