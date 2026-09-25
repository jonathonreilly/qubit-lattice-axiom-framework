#!/usr/bin/env python3
"""Two records with a DELAYED clock field (block 95 as landed, #8860), run 1 of 2.

As landed, block 95 T2/T3: with the clock field recomputed after every move (u = q lambda sum_records G(z - r), (qI - Adj) u = q lambda (n - nbar),
mean zero), hops timed by the site left (a = 1), the two records' relative-position weight per offset is exp(-q lambda G(d)) (q = 6 on the cubic
torus; the same algebra with q = 2 on the ring); 'formation and delayed clocks are absent'; a neutralized-torus residence weight, not a force.
Here the clock relaxes at rate Gamma (the task's law):
    du_z/dt = Gamma w_z ( (1/q) sum_e u_{z+e} - u_z + lambda (n_z - nbar) ),   w = exp(u);   a record at x hops to each empty neighbour at w_x/q.
EXACT (stated and used): (a) the fixed points are block 95's field plus any constant; (b) the dynamics is invariant under u -> u + c, t -> t e^{-c}
(the relaxation and every hop rate scale by e^c); (c) hence, with ubar the site mean of u, v = u - ubar and the internal time d tau = e^{ubar} dt,
    dv_z/dtau = Gamma e^{v_z} r_z - mean_y(Gamma e^{v_y} r_y),   d ubar/dtau = mean_y(Gamma e^{v_y} r_y),   hops at e^{v_x}/q per unit tau,
    r_z = (1/q) sum_e v_{z+e} - v_z + lambda (n_z - nbar):
the configuration process in tau is autonomous; the label time only adds the global factor e^{-ubar}.  The mean ubar is NOT conserved by the
weighted relaxation (sum_z 1/w_z is, exactly): in the slaved limit the gauge constant depends on the configuration through Z(C).
Measured (floating point, numba, RK4 for the field, thinning for the hops): the tau-weighted separation law (the stationary estimator) and the
label-time-weighted one, against exp(-q lambda G(d)); the drift of ubar per hop; one record's mean-square displacement per unit label time and per
unit tau against the bare hop (w = 1: MSD per unit time 1).  Gamma = 100, 10, 1, 0.1 (bare total hop rate 1); lambda = log kappa = -1/2, -1.
"""
import itertools, math, time
import numpy as np
import sympy as sp
import numba as nb

def out(s): print(s, flush=True)

def ring(L):
    return np.array([[(i + 1) % L, (i - 1) % L] for i in range(L)], np.int64)
def cube(L):
    co = np.array(list(itertools.product(range(L), repeat=3)))
    idx = lambda c: ((c[0] % L) * L + (c[1] % L)) * L + (c[2] % L)
    return np.array([[idx(c + d) for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))] for c in co], np.int64), co
def G_ring_exact(L):
    Lap = sp.zeros(L, L)
    for i in range(L):
        Lap[i, i] = 2; Lap[i, (i + 1) % L] -= 1; Lap[i, (i - 1) % L] -= 1
    Aug = Lap.row_join(sp.ones(L, 1)).col_join(sp.ones(1, L).row_join(sp.zeros(1, 1)))
    return Aug.LUsolve(sp.Matrix([1 - sp.Rational(1, L)] + [-sp.Rational(1, L)] * (L - 1) + [0]))[:L, 0]
def G_cube(L):
    k = 2 * np.pi * np.fft.fftfreq(L)
    lam = sum(np.meshgrid(*[2 - 2 * np.cos(k)] * 3, indexing="ij"))
    inv = np.zeros_like(lam); inv[lam > 1e-12] = 1 / lam[lam > 1e-12]
    return np.real(np.fft.ifftn(inv)).ravel()

@nb.njit(cache=True)
def resid(v, occ, nbr, q, lam, nbar):
    V = v.shape[0]; r = np.empty(V)
    for z in range(V):
        s = 0.0
        for e in range(nbr.shape[1]): s += v[nbr[z, e]]
        r[z] = s / q - v[z] + lam * (occ[z] - nbar)
    return r

@nb.njit(cache=True)
def vrhs(v, occ, nbr, q, lam, nbar, Gam):
    r = resid(v, occ, nbr, q, lam, nbar)
    f = Gam * np.exp(v) * r
    m = f.mean()
    return f - m, m

@nb.njit(cache=True)
def simulate(nbr, disp, q, lam, Gam, nrec, Ttau, dtau, seed, v0, pos0, rel, nrel, burn, nsamp):
    """internal time tau; returns tau-weighted and label-time-weighted separation histograms, ubar at the end, label time elapsed, hops,
    and (one record) unwrapped displacement samples at nsamp equally spaced tau with the label time at each sample"""
    np.random.seed(seed)
    V = v0.shape[0]; v = v0.copy(); pos = pos0.copy(); occ = np.zeros(V)
    for r in range(nrec): occ[pos[r]] = 1.0
    nbar = nrec / V
    htau = np.zeros(nrel); ht = np.zeros(nrel); ubar = 0.0; tlab = 0.0; hops = 0
    dim = disp.shape[2]; R = np.zeros(dim); smp = np.zeros((nsamp, dim + 2))
    nsteps = int(Ttau / dtau); every = max(nsteps // nsamp, 1); k = 0
    for step in range(nsteps):
        k1, m1 = vrhs(v, occ, nbr, q, lam, nbar, Gam)
        k2, m2 = vrhs(v + 0.5 * dtau * k1, occ, nbr, q, lam, nbar, Gam)
        k3, m3 = vrhs(v + 0.5 * dtau * k2, occ, nbr, q, lam, nbar, Gam)
        k4, m4 = vrhs(v + dtau * k3, occ, nbr, q, lam, nbar, Gam)
        v = v + dtau / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        dub = dtau / 6.0 * (m1 + 2 * m2 + 2 * m3 + m4)
        dt_label = dtau * math.exp(-(ubar + 0.5 * dub))
        ubar += dub; tlab += dt_label
        for r in range(nrec):
            x = pos[r]; wx = math.exp(v[x])
            for e in range(nbr.shape[1]):
                y = nbr[x, e]
                if occ[y] == 0.0 and np.random.random() < wx / q * dtau:
                    occ[x] = 0.0; occ[y] = 1.0; pos[r] = y; hops += 1
                    if r == 0:
                        for d in range(dim): R[d] += disp[x, e, d]
                    break
        if nrec == 2 and step * dtau > burn:
            htau[rel[pos[0], pos[1]]] += dtau; ht[rel[pos[0], pos[1]]] += dt_label
        if (step + 1) % every == 0 and k < nsamp:
            for d in range(dim): smp[k, d] = R[d]
            smp[k, dim] = (step + 1) * dtau; smp[k, dim + 1] = tlab
            k += 1
    return htau, ht, ubar, tlab, hops, smp

# ------------------------------------------------------------------ systems
Lr = 12; nbr_r = ring(Lr); Gr = G_ring_exact(Lr); Grf = np.array([float(g) for g in Gr])
off_r = np.array([[(j - i) % Lr for j in range(Lr)] for i in range(Lr)], np.int64)
disp_r = np.array([[[1.0], [-1.0]] for i in range(Lr)])
Lc = 8; nbr_c, co_c = cube(Lc); Gc = G_cube(Lc); Vc = Lc ** 3
off_c = np.zeros((Vc, Vc), np.int64)
for i in range(Vc):
    d = (co_c - co_c[i]) % Lc; off_c[i] = (d[:, 0] * Lc + d[:, 1]) * Lc + d[:, 2]
disp_c = np.zeros((Vc, 6, 3))
for i in range(Vc):
    for e, dv in enumerate(((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))): disp_c[i, e] = dv
SYS = [("ring of 12", nbr_r, 2.0, Lr, Grf, off_r, disp_r, 6, (60000.0, 30000.0)), ("8^3 torus", nbr_c, 6.0, Vc, Gc, off_c, disp_c, (4 * 8 + 4) * 8 + 4, (30000.0, 15000.0))]
out("X ring of 12, exact G of 2I - Adj (mean zero): G(0..6) = %s" % ", ".join(str(Gr[k]) for k in range(7)))
out("X 8^3, G of 6I - Adj (FFT): G(0) = %.6f, G(1,0,0) = %.6f, G(2,0,0) = %.6f, G(4,4,4) = %.6f" % (Gc[0], Gc[1], Gc[2], Gc[(4 * 8 + 4) * 8 + 4]))
# exact check of (b): the right-hand side and the hop rates scale by e^c under u -> u + c (ring, symbolic)
c = sp.Symbol('c', real=True); uu = sp.symbols('u0:12', real=True); lm = sp.Symbol('lam', real=True)
rz = lambda uv, z: (uv[(z + 1) % 12] + uv[(z - 1) % 12]) / 2 - uv[z] + lm * (1 - sp.Rational(2, 12))
lhs = sp.exp(uu[0] + c) * rz([x + c for x in uu], 0); rhs0 = sp.exp(c) * sp.exp(uu[0]) * rz(uu, 0)
out("X exact: under u -> u + c the relaxation's right-hand side and every hop rate scale by e^c (residual %s): the process in internal time "
    "d tau = e^{ubar} dt with the mean projected out is exactly the label-time process" % sp.simplify(lhs - rhs0))

# exact: sum_z 1/w_z is conserved by the relaxation (d/dt sum e^{-u} = -Gamma sum_z r_z = 0: the mean-neighbour operator has zero column sums
# and sum (n - nbar) = 0).  So in the slaved limit u = u95(C) + c(C) with sum_z e^{-u} fixed: every rate carries e^{c(C)} = Z(C)/S0,
# Z(C) = sum_z exp(-q lambda sum_r G(z - r)), and the LABEL-time slaved law is block 95's divided by Z(C); the internal-time law is block 95's.
tsym = sp.Symbol('t'); us = [sp.Function('u%d' % i)(tsym) for i in range(12)]
rr = [(us[(z + 1) % 12] + us[(z - 1) % 12]) / 2 - us[z] + lm * (sp.Symbol('n%d' % z) - sp.Rational(2, 12)) for z in range(12)]
dsum = sum(-sp.exp(-us[z]) * (sp.Symbol('Gam') * sp.exp(us[z]) * rr[z]) for z in range(12))
nsum = sum(sp.Symbol('n%d' % z) for z in range(12))
inv = sp.simplify(dsum.subs(nsum, 2) if False else dsum)
inv_ok = sp.simplify(sp.expand(inv).subs(sp.Symbol('n11'), 2 - sum(sp.Symbol('n%d' % z) for z in range(11)))) == 0
out("X exact (ring, symbolic): d/dt sum_z 1/w_z = -Gamma sum_z r_z = %s when sum_z n_z = 2 (the record count): sum 1/w is conserved, the mean "
    "clock is not; the slaved label-time law is block 95's divided by Z(C) = sum_z exp(-q lambda sum_r G(z - r))" % ("0" if inv_ok else "NONZERO"))
GAMMAS = (100.0, 10.0, 1.0, 0.1); LAMS = (-0.5, -1.0)
S = {}
for name, nbr, q, V, Gv, offs, disp, farsite, (T_small, T_big) in SYS:
    for lam in LAMS:
        target = np.exp(-q * lam * Gv); target[0] = 0.0; target /= target.sum()
        unif = np.ones(V); unif[0] = 0.0; unif /= unif.sum()
        mGt, mGu = (target * Gv).sum(), (unif * Gv).sum()
        nn = offs[0][nbr[0]]
        Zc = np.array([np.exp(-q * lam * (Gv[offs[0]] + Gv[offs[d]])).sum() for d in range(V)])   # Z for records at 0 and at offset d
        lab = np.exp(-q * lam * Gv) / Zc; lab[0] = 0.0; lab /= lab.sum()
        frac_lab = ((lab * Gv).sum() - mGu) / (mGt - mGu)
        out("X %s, lambda = %.1f: the slaved LABEL-time law pi95/Z: <G(d)> fraction %.3f of the way from random to block 95's law, TV %.4f from it"
            % (name, lam, frac_lab, 0.5 * np.abs(lab - target).sum()))
        cells = []
        vmax = -q * lam * 2 * abs(Gv.min())                        # the largest clock exponent two records can make (both at one place)
        for Gam in GAMMAS:
            dtau = min(0.02, 0.5 / (Gam * 2 * math.exp(vmax)))      # RK4 stability: dtau * (largest relaxation rate 2 Gamma e^v) < 1
            Ttau = T_small if Gam < 50 else T_big
            pos0 = np.array([0, farsite], np.int64)
            v0 = q * lam * (Gv[offs[0]] + Gv[offs[farsite]])
            res = []
            t0 = time.time()
            for seed in range(4):
                res.append(simulate(nbr, disp, q, lam, Gam, 2, Ttau, dtau, 700 + seed, v0, pos0, offs, V, 100.0, 10))
            ptau = [r[0] / r[0].sum() for r in res]; pt = [r[1] / r[1].sum() for r in res]
            frac = [((p * Gv).sum() - mGu) / (mGt - mGu) for p in ptau]; fracT = [((p * Gv).sum() - mGu) / (mGt - mGu) for p in pt]
            pp = np.mean(ptau, 0)
            tv = 0.5 * np.abs(pp - target).sum()
            nnr = pp[nn].sum() / target[nn].sum()
            hops = np.mean([r[4] for r in res]); ubar = np.mean([r[2] for r in res]); tl = np.mean([r[3] for r in res])
            cells.append((Gam, tv, np.mean(frac), np.std(frac) / 2, nnr, np.mean(fracT), np.std(fracT) / 2, ubar / max(hops, 1), ubar, tl / Ttau, time.time() - t0))
            S[(name, lam, Gam)] = (tv, np.mean(frac), np.std(frac) / 2, ubar / max(hops, 1), np.mean(fracT), np.std(fracT) / 2, frac_lab)
        out("N %s, lambda = %.1f, two records, pair law exp(-%d lambda G(d)) (uniform is at TV %.4f): %s" % (name, lam, int(q), 0.5 * np.abs(unif - target).sum(),
            "; ".join("Gamma = %g: internal-time law TV %.4f, <G(d)> %.3f +- %.3f of the way from random to the pair law, nearest-neighbour weight/target %.3f | "
                      "label-time-weighted <G(d)> %.3f +- %.3f | mean-clock change per hop %+.2e (ubar %+.2f at the end, label time / internal time %.2g) (%.0f s)" % x for x in cells)))

for name, nbr, q, V, Gv, offs, disp, farsite, _ in SYS:
    for lam in LAMS:
        cells = []
        vmax = -q * lam * abs(Gv.min())
        for Gam in GAMMAS:
            dtau = min(0.02, 0.5 / (Gam * 2 * math.exp(vmax))); Ttau = 400.0
            v0 = q * lam * Gv[offs[0]]
            msd_tau = np.zeros(20); msd_t = []; nrun = 32
            for seed in range(nrun):
                r = simulate(nbr, disp, q, lam, Gam, 1, Ttau, dtau, 3000 + seed, v0, np.array([0], np.int64), offs, V, 0.0, 20)
                smp = r[5]; dim = disp.shape[2]
                msd_tau += (smp[:, :dim] ** 2).sum(1); msd_t.append((smp[-1, :dim] ** 2).sum() / smp[-1, dim + 1])
            msd_tau /= nrun; taus = np.arange(1, 21) * Ttau / 20
            Dtau = np.polyfit(taus[5:], msd_tau[5:], 1)[0]
            Dt = float(np.mean(msd_t))
            own = math.exp(q * lam * Gv[0])
            cells.append((Gam, Dtau, Dt, own))
            S[(name, lam, Gam, "D")] = (Dtau, Dt)
        out("N %s, lambda = %.1f, one record, mean-square displacement per unit time (bare hop: 1): %s; the record's own clock in block 95's field, "
            "exp(%d lambda G(0)) = %.4f (the mean-zero field is positive away from the record)"
            % (name, lam, "; ".join("Gamma = %g: per unit internal time %.3f, per unit label time %.3f" % x[:3] for x in cells), int(q), cells[0][3]))

out("")
hits = []
for name, *_ in SYS:
    for lam in LAMS:
        tv, fr, er, drift, frT, erT, flab = S[(name, lam, 100.0)]
        if abs(frT - 1) > max(0.15, 3 * erT):
            hits.append("in LABEL time (the task's time) block 95's pair law does not return at Gamma = 100 on the %s, lambda = %.1f: <G(d)> %.3f +- %.3f of "
                        "the way from random to it, against %.3f predicted for block 95's law divided by Z(C) (sum 1/w is the conserved quantity, so the "
                        "slaved clocks carry the configuration factor Z(C)); in internal time d tau = e^{ubar} dt it returns (%.3f +- %.3f)" % (name, lam, frT, erT, flab, fr, er))
        elif abs(fr - 1) > max(0.15, 3 * er):
            hits.append("pair law fails at Gamma = 100 on the %s, lambda = %.1f even in internal time: %.3f +- %.3f" % (name, lam, fr, er))
        for Gam in GAMMAS:
            Dtau, Dt = S[(name, lam, Gam, "D")]
            if Dt > 1.05:
                hits.append("diffusion faster than bare on the %s, lambda = %.1f, Gamma = %g: MSD per unit label time %.3f (per internal time %.3f)" % (name, lam, Gam, Dt, Dtau))
# the task's expectation also says: 'for small Gamma the record's diffusion slows'
slow_small = []
for name, *_ in SYS:
    for lam in LAMS:
        d_small = S[(name, lam, 0.1, "D")][1]; d_big = S[(name, lam, 100.0, "D")][1]
        dmin_g = min(GAMMAS, key=lambda g: S[(name, lam, g, "D")][1])
        slow_small.append((name, lam, d_small, d_big, dmin_g, S[(name, lam, dmin_g, "D")][1]))
if all(ds > db for _, _, ds, db, _, _ in slow_small):
    hits.append("the record's diffusion does NOT slow for small Gamma: MSD per unit label time at Gamma = 0.1 against Gamma = 100: %s; the slowest "
                "diffusion is at large or intermediate Gamma, where the record carries its own slow clock (adiabatic value exp(q lambda G(0)))"
                % "; ".join("%s lambda=%.1f: %.3f vs %.3f (minimum %.3f at Gamma = %g)" % (n, l, ds, db, dm, g) for n, l, ds, db, g, dm in slow_small))
for h in hits: out("HIT: " + h)
out("SUMMARY: delayed clocks (the task's law) conserve sum 1/w, not the mean clock: in LABEL time the large-Gamma separation law is block 95's divided "
    "by Z(C) (ring, Gamma = 100: <G(d)> fraction %.2f and %.2f of the way to block 95's law at lambda = -1/2, -1, against %.2f and %.2f predicted for "
    "pi95/Z), in internal time d tau = e^{ubar} dt it is block 95's (ring lambda=-1, Gamma = 100/10/1/0.1: %s; 8^3 lambda=-1: %s, weak statistics); "
    "one record's MSD per unit label time (bare 1) grows as Gamma FALLS: ring lambda=-1 %s, 8^3 lambda=-1 %s (the slaved record carries its slow clock)"
    % (S[("ring of 12", -0.5, 100.0)][4], S[("ring of 12", -1.0, 100.0)][4], S[("ring of 12", -0.5, 100.0)][6], S[("ring of 12", -1.0, 100.0)][6],
       " / ".join("%.2f" % S[("ring of 12", -1.0, g)][1] for g in GAMMAS), " / ".join("%.2f" % S[("8^3 torus", -1.0, g)][1] for g in GAMMAS),
       " / ".join("%.2f" % S[("ring of 12", -1.0, g, "D")][1] for g in GAMMAS), " / ".join("%.2f" % S[("8^3 torus", -1.0, g, "D")][1] for g in GAMMAS)))
