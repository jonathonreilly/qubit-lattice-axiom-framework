#!/usr/bin/env python3
"""check.py for J:derive:collisional-viscosity-and-eta:a1 (worker w-jonathonsmac4f50-ja2b2, claude-opus-5-5).

Section E is exact (sympy): sphere moments, the linearized re-draw on the second harmonic, the Chapman-Enskog stress,
the product-state momentum currents with exchange, and the resulting eta.
Section F is floating-point evidence: decay of transverse momentum waves in probes/lib/inertial.py (tick_s, periodic, no bodies).
"""
import os, sys, time, math
import numpy as np
import sympy as sp

PASS, FAIL = [], []
t_start = time.time()
def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print(("PASS " if ok else "FAIL ") + name + ((": " + detail) if detail else "") + "  [%.0f s]" % (time.time() - t_start), flush=True)

th, ph = sp.symbols("theta phi", real=True)
S = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
def sph(expr):
    """average over the uniform unit sphere"""
    return sp.simplify(sp.integrate(sp.integrate(expr * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)) / (4 * sp.pi))

# ---------------------------------------------------------------- E1 moments (block 51 T2's, plus the ones used here)
sx, sy, sz = S
def upper(expr):
    """integral over the upper hemisphere (s_z > 0), normalized by the sphere's area"""
    return sp.simplify(sp.integrate(sp.integrate(expr * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi / 2)) / (4 * sp.pi))
m_abs = 2 * upper(sz)                     # <|s_z|>, by the symmetry s_z -> -s_z
m_pos = upper(sz)                         # <max(s_z, 0)>
m_ii = 2 * upper(sz ** 3)                 # <s_z^2 |s_z|>
m_ik = 2 * upper(sx ** 2 * sz)            # <s_x^2 |s_z|>
m_pos2 = upper(sz ** 2)                   # <s_z^2 1(s_z > 0)>
m4 = [sph(sz ** 4), sph(sx ** 2 * sz ** 2)]
check("E1 sphere moments: <|s_k|> = 1/2, <max(s_k,0)> = 1/4, <s_i^2|s_i|> = 1/4, <s_i^2|s_k|> = 1/8, <s_k^2 1(s_k>0)> = 1/6, <s_k^4> = 1/5, <s_i^2 s_k^2> = 1/15",
      [sp.simplify(x_) for x_ in (m_abs, m_pos, m_ii, m_ik, m_pos2, m4[0], m4[1])] == [sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 8), sp.Rational(1, 6), sp.Rational(1, 5), sp.Rational(1, 15)])

# ---------------------------------------------------------------- E2 the re-draw on the second harmonic
# pair (s1, s2), P = s1 + s2, output P/2 +- r w, r^2 = 1 - |P|^2/4, w uniform on the unit circle orthogonal to P.
# E_w[w w^T] = (I - Phat Phat^T)/2 (w = cos(psi) e1 + sin(psi) e2 with e1, e2 an orthonormal basis of P's orthogonal plane).
psi = sp.Symbol("psi", real=True)
e1v = sp.Matrix([1, 0, 0]); e2v = sp.Matrix([0, 1, 0])
Ew = sp.simplify(sp.integrate((sp.cos(psi) * e1v + sp.sin(psi) * e2v) * (sp.cos(psi) * e1v + sp.sin(psi) * e2v).T, (psi, 0, 2 * sp.pi)) / (2 * sp.pi))
check("E2a E_w[w w^T] = (I - Phat Phat^T)/2 for w uniform on the circle orthogonal to Phat (Phat = z shown; covariance gives the general case)",
      Ew == sp.diag(sp.Rational(1, 2), sp.Rational(1, 2), 0))
# for s1 = z-hat, average over s2 uniform: out = P P^T/2 + r^2 (I - Phat Phat^T);  Delta = out - s1 s1^T - s2 s2^T
s1 = sp.Matrix([0, 0, 1]); s2 = S; P = s1 + s2; P2 = sp.simplify((P.T * P)[0])
r2 = 1 - P2 / 4
out = P * P.T / 2 + r2 * sp.eye(3) - r2 / P2 * (P * P.T)
Delta = out - s1 * s1.T - s2 * s2.T
avgD = sp.Matrix(3, 3, lambda i, j: sph(sp.simplify(Delta[i, j])))
target = -sp.Rational(1, 2) * (s1 * s1.T - sp.eye(3) / 3)
check("E2b averaging the re-draw of (s1, s2) over an isotropic partner s2: <Delta(s s^T summed over the pair)> = -(1/2)(s1 s1^T - I/3) (s1 = z-hat; rotation covariance of the clause gives every s1)",
      sp.simplify(avgD - target) == sp.zeros(3, 3), str(avgD.tolist()))
avgP = sp.Matrix(3, 1, lambda i, j: sph(sp.simplify((P / 2 * 2 - s1 - s2)[i])))
check("E2c the re-draw keeps the pair's momentum (out1 + out2 = P) and number: the first harmonic and the density are not relaxed", avgP == sp.zeros(3, 1))
# per record the events come at 6 gamma rho (six bonds, the partner present with probability rho, rate gamma per bond), each halving the record's
# second harmonic on average: omega_2 = 3 gamma rho
gam, rho = sp.symbols("gamma rho", positive=True)
omega2 = 6 * gam * rho * sp.Rational(1, 2)

# ---------------------------------------------------------------- E3 Chapman-Enskog stress and nu_coll
# f0 = (n/4pi)(1 + 3 s.U);  streaming (1/sqrt3) s.grad f0 has second-harmonic part (1/sqrt3)(3n/4pi)(s_k s_l - d_kl/3) d_l U_k;
# f1 = -(1/omega2) x that;  delta Pi_ij = (1/sqrt3) int s_i s_j f1 = -(n/omega2) <s_i s_j (s_k s_l - d_kl/3)> d_l U_k
n_ = sp.Symbol("n", positive=True)
Ugrad = sp.Matrix(3, 3, lambda k, l: sp.Symbol("G_%d%d" % (k, l)))       # G_kl = d_l U_k
dl = lambda i, j: 1 if i == j else 0
four = lambda i, j, k, l: sp.Rational(1, 15) * (dl(i, j) * dl(k, l) + dl(i, k) * dl(j, l) + dl(i, l) * dl(j, k))
dPi = sp.Matrix(3, 3, lambda i, j: -(n_ / omega2) * sum((four(i, j, k, l) - sp.Rational(1, 9) * dl(i, j) * dl(k, l)) * Ugrad[k, l] for k in range(3) for l in range(3)))
Ssym = (Ugrad + Ugrad.T) / 2; divU = Ugrad.trace()
expect = -(n_ / omega2) * (sp.Rational(2, 15) * Ssym + (sp.Rational(1, 15) - sp.Rational(1, 9)) * divU * sp.eye(3))
check("E3 Chapman-Enskog: delta Pi_ij = -(n/omega_2)[(2/15) S_ij - (2/45) delta_ij div U], so d_t g_i gets (1/(15 omega_2)) (Lap g_i + (1/3) d_i div g): nu_coll = 1/(15 omega_2) = 1/(45 gamma rho), isotropic",
      sp.simplify(dPi - expect) == sp.zeros(3, 3))
nu_coll = sp.Rational(1, 15) / omega2
nu_lat = sp.sqrt(3) / 16

# ---------------------------------------------------------------- E4 exclusion: product-state momentum current across a bond, with exchange
# bond x -> x + e_k, product state with content law rho(s) at each site.  Forward attempts from x at rate max(s_k,0)/sqrt3:
#   empty target: s crosses (weight 1 - rho_{x+e});  occupied target with content s': s crosses forward, s' crosses back.
#   momentum current (component i) = (1/sqrt3)[ sum_s rho_x(s) s_i max(s_k,0) (1 - rho_{x+e}) + sum_{s,s'} rho_x(s) rho_{x+e}(s') max(s_k,0)(s_i - s'_i) ]
#                                   = (1/sqrt3)[ sum_s rho_x(s) s_i max(s_k,0) - A+_x g_i(x+e) ],  A+ = sum_s rho(s) max(s_k,0)
# (the exclusion loss is restored exactly by the forward carry of the exchange), minus the mirror term from x + e.
rx, ry = sp.symbols("rho_x rho_y", positive=True)
Ax = sp.Symbol("A_x"); Tx = sp.Symbol("T_x"); gy = sp.Symbol("g_y")      # T_x = sum rho_x(s) s_i max(s_k,0)
free_part = Tx * (1 - ry) + Tx * ry - Ax * gy                             # sum over s' of rho_y(s') = rho_y; of rho_y(s') s'_i = g_i(y)
check("E4a the exchange's forward carry restores exactly what exclusion removes: current = (1/sqrt3)[T_x - A+_x g_i(x + e)] - (mirror)",
      sp.expand(free_part - (Tx - Ax * gy)) == 0)
# in local equilibrium A+ = rho/4 + g_k/2 (from <max(s_k,0)> = 1/4, <s_k^2 1(s_k>0)> = 1/6):
Ueq = sp.Symbol("U_k")
Aplus = sp.simplify(rho * (m_pos + 3 * Ueq * m_pos2))
check("E4b in local equilibrium A+- = rho/4 +- g_k/2 (g = rho U)", sp.simplify(Aplus - (rho / 4 + rho * Ueq / 2)) == 0)
# linear part of the backflow: -(1/sqrt3)(rho/4)(g_i(x+e) - g_i(x)) per bond: a content-blind diffusion of momentum with coefficient rho/(4 sqrt3)
a0, a1, a2 = sp.symbols("a0 a1 a2")
gq = lambda x_: a0 + a1 * x_ + a2 * x_ ** 2                              # a quadratic profile along the bond axis
xx = sp.Symbol("x")
J = lambda x_: -(1 / sp.sqrt(3)) * (rho / 4) * (gq(x_ + 1) - gq(x_))      # linear backflow current through the bond (x, x+1)
lin = sp.expand(-(J(xx) - J(xx - 1)))                                     # its contribution to d_t g(x)
check("E4c the backflow adds (rho/(4 sqrt3)) Lap g_i to the momentum equation, the same along every axis and for every component: isotropic",
      sp.simplify(lin - rho / (4 * sp.sqrt(3)) * sp.diff(gq(xx), xx, 2)) == 0)

# ---------------------------------------------------------------- E5 eta
nu_iso0 = nu_lat + nu_coll
nu_iso = nu_lat + rho / (4 * sp.sqrt(3)) + nu_coll
eta0 = sp.simplify(nu_lat / nu_iso0); eta = sp.simplify(nu_lat / nu_iso)
vals = {}
for rv, gv in ((sp.Rational(1, 10), 2), (sp.Rational(3, 10), 1), (sp.Rational(1, 10), 1), (sp.Rational(3, 10), 4)):
    vals[(rv, gv)] = (float(nu_iso0.subs({rho: rv, gam: gv})), float(eta0.subs({rho: rv, gam: gv})), float(nu_iso.subs({rho: rv, gam: gv})), float(eta.subs({rho: rv, gam: gv})))
print("   E5 eta = nu_lat / nu_iso;  nu_lat = sqrt3/16 = %.5f;  nu_coll = 1/(45 gamma rho)" % float(nu_lat))
for k_, v_ in vals.items():
    print("      (rho, gamma) = (%s, %s): small-density nu_iso %.4f, eta %.3f;  with the exclusion backflow nu_iso %.4f, eta %.3f" % (k_[0], k_[1], *v_))
check("E5 eta at (0.1, 2) and (0.3, 1) is 0.46-0.60 (exact expressions), inside or at the edge of block 51's executed 0.3-0.5",
      all(0.4 < vals[k_][3] < 0.61 and 0.4 < vals[k_][1] < 0.61 for k_ in ((sp.Rational(1, 10), 2), (sp.Rational(3, 10), 1))))
# transverse waves: the operator nu_iso Lap g_i + nu_lat d_i^2 g_i on g = e cos(q.x):
def damping(nvec, evec):
    nvec = sp.Matrix(nvec) / sp.sqrt(sum(x_ ** 2 for x_ in nvec)); evec = sp.Matrix(evec) / sp.sqrt(sum(x_ ** 2 for x_ in evec))
    L_ = sp.diag(*[nvec[i] ** 2 for i in range(3)])                         # cubic part acting on the polarization, per unit q^2
    val = sp.simplify((evec.T * L_ * evec)[0]); resid = sp.simplify(L_ * evec - val * evec)
    return val, resid == sp.zeros(3, 1)
d_ax, e_ax = damping([1, 0, 0], [0, 1, 0]); d_fi, e_fi = damping([1, 1, 0], [1, -1, 0]); d_fo, e_fo = damping([1, 1, 0], [0, 0, 1])
check("E6 transverse waves are eigenpolarizations with damping q^2 (nu_iso + nu_lat c): c = 0 along an axis, 1/2 along a face diagonal polarized in the face, 0 polarized across it; "
      "so the in-face over across-face ratio at the same q is 1 + eta/2", (d_ax, d_fi, d_fo) == (0, sp.Rational(1, 2), 0) and e_ax and e_fi and e_fo)

# ---------------------------------------------------------------- F: executed transverse waves (floating point evidence)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "lib")))
from inertial import tick_s, seed_compiled
def run_wave(rho0, gamma, mode, pol, A=0.3, T=120, runs=12, seed=1, L=32):
    rng = np.random.default_rng(seed); seed_compiled(seed)
    q = 2 * np.pi * np.array(mode) / L; e = np.array(pol, float); e /= np.linalg.norm(e)
    X = np.indices((L, L, L)).reshape(3, -1).T
    phase = X @ q; wave = np.exp(-1j * phase)
    curves = []
    solid = np.zeros((L, L, L), np.int8); force = np.zeros((3, 3))
    for r in range(runs):
        occ = rng.random((L, L, L)) < rho0
        # contents from (1/4pi)(1 + 3 s.U(x)), U = A e cos(q.x), by rejection
        V = rng.normal(size=(L ** 3, 3)); V /= np.linalg.norm(V, axis=1, keepdims=True)
        Ux = A * np.cos(phase)
        acc = rng.random(L ** 3) < (1 + 3 * Ux * (V @ e)) / (1 + 3 * A)
        while not acc.all():
            nb = (~acc).sum(); W = rng.normal(size=(nb, 3)); W /= np.linalg.norm(W, axis=1, keepdims=True)
            V[~acc] = W; acc[~acc] = rng.random(nb) < (1 + 3 * Ux[~acc] * (W @ e)) / (1 + 3 * A)
        sx_ = V[:, 0].reshape(L, L, L).copy(); sy_ = V[:, 1].reshape(L, L, L).copy(); sz_ = V[:, 2].reshape(L, L, L).copy()
        amp = []
        for t in range(T + 1):
            if t % 4 == 0:
                ge = (sx_ * e[0] + sy_ * e[1] + sz_ * e[2]) * occ
                amp.append(np.real((ge.reshape(-1) * wave).sum()))
            if t < T: tick_s(occ, sx_, sy_, sz_, solid, force, L, True, gamma, False)
        curves.append(amp)
    c = np.array(curves); m = c.mean(0); se_ = c.std(0, ddof=1) / np.sqrt(runs)
    ts = np.arange(0, T + 1, 4)
    sel = (ts >= 12) & (m > 3 * se_)
    slope, icpt = np.polyfit(ts[sel], np.log(m[sel]), 1, w=(m[sel] / se_[sel]))
    # jackknife error of the rate
    rates = []
    for j in range(runs):
        mj = np.delete(c, j, 0).mean(0); s2 = sel & (mj > 0)
        rates.append(-np.polyfit(ts[s2], np.log(mj[s2]), 1)[0])
    rates = np.array(rates); err = np.sqrt((runs - 1) / runs * ((rates - rates.mean()) ** 2).sum())
    qq = float(q @ q)
    return -slope / qq, err / qq
from inertial import scatter_pair
rngm = np.random.default_rng(5); seed_compiled(5)
nmc = 100000; S2m = rngm.normal(size=(nmc, 3)); S2m /= np.linalg.norm(S2m, axis=1, keepdims=True); totm = np.zeros(3)
for i in range(nmc):
    a_, b_, c_, a2_, b2_, c2_ = scatter_pair(0.0, 0.0, 1.0, S2m[i, 0], S2m[i, 1], S2m[i, 2])
    totm += np.array([a_ * a_ + a2_ * a2_, b_ * b_ + b2_ * b2_, c_ * c_ + c2_ * c2_]) - np.array([S2m[i, 0] ** 2, S2m[i, 1] ** 2, 1 + S2m[i, 2] ** 2])
totm /= nmc
check("F0 (evidence) the lib's scatter_pair with s1 = z and an isotropic partner: mean change (%.4f, %.4f, %.4f) against E2b's exact (1/6, 1/6, -1/3), 1e5 samples"
      % tuple(totm), np.max(np.abs(totm - np.array([1 / 6, 1 / 6, -1 / 3]))) < 0.01)
print("   F (floating-point evidence): transverse momentum waves in probes/lib/inertial.py tick_s, periodic side 32, 12 runs of 120 ticks each; nu = decay rate / q^2")
F_ok = True
for (rv, gv) in ((0.1, 2.0), (0.3, 1.0)):
    nuA, eA = run_wave(rv, gv, (1, 0, 0), (0, 1, 0), seed=11)
    nuFi, eFi = run_wave(rv, gv, (1, 1, 0), (1, -1, 0), seed=12)
    nuFo, eFo = run_wave(rv, gv, (1, 1, 0), (0, 0, 1), seed=13)
    pred0 = vals[(sp.Rational(int(rv * 10), 10), int(gv))]
    ratio = nuFi / nuFo; rerr = ratio * math.hypot(eFi / nuFi, eFo / nuFo)
    print("      (rho, gamma) = (%.1f, %.0f): axis (q along x, g along y) nu = %.4f +- %.4f; face diagonal in-face nu = %.4f +- %.4f, across-face nu = %.4f +- %.4f; "
          "in/across = %.3f +- %.3f" % (rv, gv, nuA, eA, nuFi, eFi, nuFo, eFo, ratio, rerr))
    print("         predicted: nu_iso %.4f (small density) or %.4f (with the exclusion backflow); in/across 1 + eta/2 = %.3f or %.3f"
          % (pred0[0], pred0[2], 1 + pred0[1] / 2, 1 + pred0[3] / 2))
    F_ok = F_ok and ratio > 1
check("F1 (evidence) the in-face polarization of a face-diagonal wave decays faster than the across-face one at both (rho, gamma), as the cubic term requires", F_ok)
# F2: the gamma scan at rho = 0.1 -- molecular chaos predicts nu_coll proportional to 1/gamma
print("   F2 (evidence) axis waves at rho = 0.1 against gamma; molecular chaos: nu = sqrt3/16 + rho/(4 sqrt3) + 1/(45 gamma rho)")
scan = {}
for gv in (1.0, 2.0, 4.0, 8.0):
    scan[gv] = run_wave(0.1, gv, (1, 0, 0), (0, 1, 0), seed=21 + int(gv), T=120)
    mc = float(nu_iso.subs({rho: sp.Rational(1, 10), gam: sp.nsimplify(gv)}))
    print("      gamma %.0f: nu = %.4f +- %.4f; molecular chaos %.4f" % (gv, scan[gv][0], scan[gv][1], mc))
nu48 = run_wave(0.1, 2.0, (1, 0, 0), (0, 1, 0), seed=31, T=200, runs=8, L=48)
print("      side 48, gamma 2 (smaller q): nu = %.4f +- %.4f against %.4f at side 32" % (nu48[0], nu48[1], scan[2.0][0]))
mc8 = float(nu_iso.subs({rho: sp.Rational(1, 10), gam: 8}))
sat = scan[8.0][0] / scan[2.0][0]
check("F2 (evidence, counterexample to the molecular-chaos closure) at rho = 0.1 the transverse viscosity saturates in gamma: nu(8)/nu(2) = %.3f "
      "against the closure's %.3f, and nu(8) = %.3f exceeds the closure's %.3f by %.0f standard errors; side 48 agrees with side 32 (hydrodynamic)"
      % (sat, mc8 / float(nu_iso.subs({rho: sp.Rational(1, 10), gam: 2})), scan[8.0][0], mc8, (scan[8.0][0] - mc8) / scan[8.0][1]),
      sat > 0.85 and (scan[8.0][0] - mc8) > 5 * scan[8.0][1] and abs(nu48[0] - scan[2.0][0]) < 3 * math.hypot(nu48[1], scan[2.0][1]))
# F3: direct decay of a uniform stress (s_z^2 - 1/3) from a product start at rho = 0.1, gamma = 2
def stress_decay(L, rho0, gamma, T=6, runs=8, eps=0.8, seed=41):
    rng = np.random.default_rng(seed); seed_compiled(seed)
    solid = np.zeros((L, L, L), np.int8); force = np.zeros((3, 3)); out = []
    for r in range(runs):
        occ = rng.random((L, L, L)) < rho0
        N = L ** 3; V = rng.normal(size=(N, 3)); V /= np.linalg.norm(V, axis=1, keepdims=True)
        acc = rng.random(N) < (1 + eps * (1.5 * V[:, 2] ** 2 - 0.5)) / (1 + eps)
        while not acc.all():
            nb = (~acc).sum(); W = rng.normal(size=(nb, 3)); W /= np.linalg.norm(W, axis=1, keepdims=True)
            V[~acc] = W; acc[~acc] = rng.random(nb) < (1 + eps * (1.5 * W[:, 2] ** 2 - 0.5)) / (1 + eps)
        sx_, sy_, sz_ = [V[:, i].reshape(L, L, L).copy() for i in range(3)]
        curve = []
        for t in range(T + 1):
            curve.append(((sz_ ** 2 - 1 / 3) * occ).sum() / occ.sum())
            tick_s(occ, sx_, sy_, sz_, solid, force, L, True, gamma, False)
        out.append(curve)
    return np.array(out).mean(0)
cst = stress_decay(48, 0.1, 2.0)
r1 = -math.log(cst[1] / cst[0]); r6 = -math.log(cst[6] / cst[0]) / 6
print("   F3 (evidence) uniform stress <s_z^2 - 1/3> from a product start, rho 0.1, gamma 2, side 48: %s; rate over tick 1 %.3f, mean over 6 ticks %.3f; "
      "molecular chaos 3 gamma rho = 0.600; first-tick estimate for pairs re-drawn at most once, 3 rho (1 - e^-gamma) = %.3f"
      % (" ".join("%.4f" % x_ for x_ in cst), r1, r6, 3 * 0.1 * (1 - math.exp(-2))))
check("F3 (evidence) the uniform stress relaxes at about 0.3 per tick, not 3 gamma rho = 0.6: re-draws of a pair already re-drawn relax nothing (exact: the pair's law given P is already the re-draw's)",
      r1 < 0.45 and r6 < 0.45)
print("")
print("TOTAL: PASS=%d FAIL=%d (%.0f s)" % (len(PASS), len(FAIL), time.time() - t_start))
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("HIT: for block 51's bond re-draw, exact: one re-draw with an isotropic partner removes exactly half of the pair's second harmonic, and a pair already re-drawn is "
          "unchanged in law by further re-draws; the molecular-chaos (product-state) Chapman-Enskog value nu_coll = 1/(45 gamma rho) (isotropic) is therefore not the gas's: "
          "executed transverse waves give nu saturating in gamma (0.45, 0.41, 0.41 at gamma 2, 4, 8, rho 0.1, against 0.23, 0.18, 0.15), eta = nu_lat/nu about 0.24 at "
          "(0.1, 2) and 0.31 at (0.3, 1); exact product-state exchange currents: forward carry = free streaming, backflow adds the isotropic rho/(4 sqrt3), cubic part sqrt3/16 unchanged")
    print("SUMMARY: ROUTE FAILS AT step 4 (the molecular-chaos rate 6 gamma rho of independent re-draws): repeated re-draws of the same adjacent pair are redundant, the "
          "stress relaxes at the rate new adjacencies form; exact partial results: the halving identity, the Chapman-Enskog form nu = 1/(15 omega_2), the exchange backflow, "
          "the transverse eigen-dampings; measured eta about 0.24-0.31")
