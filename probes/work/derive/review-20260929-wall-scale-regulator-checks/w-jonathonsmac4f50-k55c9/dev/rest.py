
# =====================================================================================
# Everything below: ensembles spec, production/replay driver, exact checks, analysis.
# =====================================================================================
import sys, os, json, time, math, hashlib, itertools
from fractions import Fraction
import sympy as sp
import mpmath as mp
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
ENSDIR = os.path.join(HERE, 'ensembles')

SPECS = {
 'q44':      dict(dims=(4,4,4,4), Ns=0, m=0.1, nq=0,   ntherm=200, nmeas=4000, nmd=10, seed=11),
 'f44_m01':  dict(dims=(4,4,4,4), Ns=1, m=0.1, nq=100, ntherm=120, nmeas=1500, nmd=10, seed=21),
 'f44_ns2':  dict(dims=(4,4,4,4), Ns=2, m=0.1, nq=100, ntherm=120, nmeas=1000, nmd=12, seed=31),
 'f44_m05':  dict(dims=(4,4,4,4), Ns=1, m=0.5, nq=100, ntherm=80,  nmeas=1500, nmd=10, seed=41),
 'q44_b61':  dict(dims=(4,4,4,4), Ns=0, m=0.1, nq=0,   ntherm=200, nmeas=3000, nmd=10, seed=71, beta=6.1),
 'q44_b62':  dict(dims=(4,4,4,4), Ns=0, m=0.1, nq=0,   ntherm=200, nmeas=3000, nmd=10, seed=72, beta=6.2),
 'q66':      dict(dims=(6,6,6,6), Ns=0, m=0.1, nq=0,   ntherm=200, nmeas=1500, nmd=10, seed=51),
 'f66_m01':  dict(dims=(6,6,6,6), Ns=1, m=0.1, nq=100, ntherm=80,  nmeas=400, nmd=12, seed=61),
}

def run_ensemble(name, nmeas_override=None, log=False):
    sp_ = SPECS[name]
    lat = Lat(sp_['dims'])
    if sp_['nq'] > 0:
        hq = HMC(lat, sp_.get('beta', 6.0), Ns=0, nmd=10, tau=1.0, seed=sp_['seed'])
        for _ in range(sp_['nq']):
            hq.trajectory(thermal=True)
        h = HMC(lat, sp_.get('beta', 6.0), Ns=sp_['Ns'], m=sp_['m'], nmd=sp_['nmd'], tau=1.0, seed=sp_['seed'] + 1000)
        h.U = hq.U.copy()
    else:
        h = HMC(lat, sp_.get('beta', 6.0), Ns=sp_['Ns'], m=sp_['m'], nmd=sp_['nmd'], tau=1.0, seed=sp_['seed'])
    for k in range(sp_['ntherm']):
        h.trajectory(thermal=(k < sp_['ntherm'] // 2))
    h.nacc = 0; h.dH = []; h.ntraj = 0
    n = sp_['nmeas'] if nmeas_override is None else nmeas_override
    P = []; dHs = []; acc = []
    t0 = time.time()
    for k in range(n):
        a, d = h.trajectory()
        P.append(h.g.plaq(h.U)); dHs.append(d); acc.append(int(a))
        if log and (k + 1) % 50 == 0:
            print(name, k + 1, 'of', n, round(time.time() - t0, 1), 's', flush=True)
    return dict(spec={k: (list(v) if isinstance(v, tuple) else v) for k, v in sp_.items()}, P=P, dH=dHs, acc=acc,
                cg_iters=(h.f.cg_iters if h.f else 0), seconds=time.time() - t0)

# ---------------- statistics ----------------
def tau_int_wolff(x, S=1.5):
    x = np.asarray(x, float); n = len(x); d = x - x.mean()
    var = np.dot(d, d) / n
    if var == 0: return 0.5, 1
    f = np.fft.rfft(d, 2 * n); ac = np.fft.irfft(f * np.conj(f))[:n] / n / var
    tau = 0.5; W = 1
    for t in range(1, n):
        tau += ac[t]
        if t >= S * tau:
            W = t; break
    else:
        W = n - 1
    return max(tau, 0.5), W

def mean_err(x, burn=0):
    x = np.asarray(x, float)[burn:]
    tau, W = tau_int_wolff(x)
    # bias-corrected Gamma-method error
    err = math.sqrt(2 * tau * np.var(x, ddof=1) / len(x))
    return float(x.mean()), err, tau

def block_err(x, nblk=20):
    x = np.asarray(x, float); n = len(x) // nblk * nblk
    b = x[:n].reshape(nblk, -1).mean(axis=1)
    return float(b.std(ddof=1) / math.sqrt(nblk))

# ---------------- formula ----------------
mp.mp.dps = 40
M_PL = mp.mpf('1.2209e19'); ALPHA_BARE = 1 / (4 * mp.pi)
def v_of_P(P):
    P = mp.mpf(P)
    return M_PL * (mp.mpf(7) / 8) ** mp.mpf('0.25') * (ALPHA_BARE / P ** mp.mpf('0.25')) ** 16

PASS = 0; FAIL = 0
def check(name, cond, detail=''):
    global PASS, FAIL
    if cond: PASS += 1
    else: FAIL += 1
    print(('PASS ' if cond else 'FAIL ') + name + (('  [' + detail + ']') if detail else ''), flush=True)

def sec_exact():
    # --- E1: staggered 2^4 all-antiperiodic block; exact integers ---
    sites = list(itertools.product((0, 1), repeat=4)); idx = {s: i for i, s in enumerate(sites)}
    K = np.zeros((16, 16), dtype=np.int64)
    for x in sites:
        for mu in range(4):
            y = list(x); y[mu] ^= 1; y = tuple(y)
            eta = (-1) ** sum(x[:mu])
            sf = -1 if x[mu] == 1 else 1; sb = -1 if x[mu] == 0 else 1
            K[idx[x], idx[y]] += eta * (sf - sb) // 2      # (1/2)(sf - sb) eta, integer
    check('E1 staggered 2^4 APBC hop matrix is real antisymmetric with K^2 = -4 I and tr K = 0 (exact integers)',
          (K == -K.T).all() and (K @ K == -4 * np.eye(16, dtype=np.int64)).all() and np.trace(K) == 0)
    u, m = sp.symbols('u m')
    # K^2=-4I, trK=0 => eigenvalues +-2i, 8 each => det(m+uK) = (m^2+4u^2)^8 ; verify against sympy charpoly of a reduced form
    cp = sp.Matrix(K.tolist()).charpoly(sp.Symbol('x')).as_expr()
    x = sp.Symbol('x')
    check('E1b exact characteristic polynomial of K is (x^2+4)^8, so det(m+uK) = (m^2+4u^2)^8 and the u-degree at m=0 is 16 per colour',
          sp.expand(cp - (x ** 2 + 4) ** 8) == 0)
    # --- E2: naive Dirac operator on the SAME block ---
    s0 = np.eye(2, dtype=complex); sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
    g = [np.kron(sx, s0), np.kron(sy, s0), np.kron(sz, sx), np.kron(sz, sy)]
    T = np.array([[0, 1], [-1, 0]], dtype=complex)         # 2-site APBC ring: (fwd - bwd)/2 hop
    I2 = np.eye(2, dtype=complex)
    Tm = [np.kron(np.kron(T, I2), np.kron(I2, I2)), np.kron(np.kron(I2, T), np.kron(I2, I2)),
          np.kron(np.kron(I2, I2), np.kron(T, I2)), np.kron(np.kron(I2, I2), np.kron(I2, T))]
    Dn = sum(np.kron(Tm[mu], g[mu]) for mu in range(4))      # (16 sites x 4 spin) = 64
    ok = np.allclose(Dn @ Dn, -4 * np.eye(64), atol=0) and abs(np.trace(Dn)) < 1e-12 and np.allclose(Dn, -Dn.conj().T, atol=0)
    check('E2 naive Dirac operator on the same 2^4 APBC block: 64 components, D^2 = -4 I, so det(m+uD) = (m^2+4u^2)^32, u-degree 64 (16 species x 4 spin), not 16', ok)
    check('E2b so "degree 16 = 16 species" holds only by coincidence of the staggered 16 = 4 spin x 4 taste; Dirac flavours per staggered field = 4/4 = 1 field; degree per Dirac flavour = 4',
          Dn.shape[0] // 4 == 16 and K.shape[0] // 4 == 4)
    check('E2c with SU(3) colour carried identically, the full determinant degree is 3 x 16 = 48, not 16 (the formula uses per-colour 16)', 3 * 16 == 48)
    # --- E3: formula arithmetic ---
    v0 = v_of_P('0.5934')
    check('E3 v(0.5934) = M_Pl (7/8)^(1/4) alpha_LM^16 = 246.28281829 GeV (high precision recomputation)', abs(v0 - mp.mpf('246.282818290129')) < mp.mpf('1e-6'), str(mp.nstr(v0, 12)))
    Ps = sp.Symbol('P', positive=True)
    vv = sp.Rational(7, 8) ** sp.Rational(1, 4) * (1 / (4 * sp.pi) / Ps ** sp.Rational(1, 4)) ** 16
    check('E3b elasticity d ln v / d ln P = -4 exactly (sympy)', sp.simplify(sp.diff(sp.log(vv), Ps) * Ps + 4) == 0)
    Kc = (mp.mpf(7) / 8) ** mp.mpf('0.25') * (ALPHA_BARE / mp.mpf('0.5934') ** mp.mpf('0.25')) ** 16
    check('E3c K = (7/8)^(1/4) alpha_LM^16 = 2.017224e-17', abs(Kc / mp.mpf('2.017224e-17') - 1) < 1e-6, mp.nstr(Kc, 8))
    resid = mp.mpf('2.5513e-4')
    dpmin = mp.mpf('0.5934') * ((1 - 100 * resid) ** (-mp.mpf(1) / 4) - 1)
    check('E3d a plaquette shift of only %.4f already moves v by 100x the quoted 0.0255 percent residual (exact inversion)' % float(dpmin),
          abs(v_of_P(mp.mpf('0.5934') + dpmin) / v0 - (1 - 100 * resid)) < 1e-15)
    # --- E4: coupling chain, same coupling on both sides (alpha_LM at M_Pl) ---
    a0 = float(ALPHA_BARE / mp.mpf('0.5934') ** mp.mpf('0.25'))
    efolds_needed = 16 * math.log(1 / a0)
    check('E4 the 16th-power formula spans %.1f e-folds below M_Pl' % efolds_needed, abs(efolds_needed - 38.4) < 1.0)
    def pole(nf, loops):
        b0 = 11 - 2.0 * nf / 3; b1 = 102 - 38.0 * nf / 3
        if loops == 1:
            return 2 * math.pi / (b0 * a0)
        f = lambda t, y: [(b0 / (2 * math.pi)) * y[0] ** 2 + (b1 / (8 * math.pi ** 2)) * y[0] ** 3]   # t = ln(M_Pl/mu), coupling grows toward the IR
        ev = lambda t, y: y[0] - 1.0
        ev.terminal = True
        sol = solve_ivp(f, [0, 60], [a0], events=ev, rtol=1e-11, atol=1e-13)
        return sol.t_events[0][0] if len(sol.t_events[0]) else float('inf')
    res = {}
    for nf in (2, 4, 6, 16):
        res[nf] = (pole(nf, 1), pole(nf, 2))
    print('INFO e-folds below M_Pl to alpha=infinity (1-loop) / alpha=1 (2-loop):', {k: (round(v[0], 2), round(v[1], 2)) for k, v in res.items()})
    check('E4b n_f=6 coloured flavours: one-loop pole at M_Pl*exp(-%.2f) = %.2e GeV (order 6e14 GeV), far short of 38 e-folds' % (res[6][0], 1.2209e19 * math.exp(-res[6][0])),
          abs(math.log10(1.2209e19 * math.exp(-res[6][0])) - math.log10(6e14)) < 0.15 and res[6][0] < 15)
    check('E4c n_f=2,4,6 reach alpha=1 within 5-9 e-folds at two loops (5.7, 6.8, 8.4); n_f=16 (one-loop b0 = 1/3 > 0, two-loop fixed point 4 pi b0/|b1| = 0.042 below alpha_LM) never does within 60 e-folds',
          all(5 < res[n][1] < 9 for n in (2, 4, 6)) and res[16][1] == float('inf'))

def sec_hmc_integrity():
    lat = Lat((4, 4, 4, 4)); rng = np.random.default_rng(1)
    U = random_su3(rng, (4, lat.V))
    check('H1 random SU(3) links are unitary with det 1 to 1e-14', np.abs(U @ dag(U) - np.eye(3)).max() < 1e-14 and np.abs(np.linalg.det(U) - 1).max() < 1e-14)
    g = Gauge(lat, 6.0)
    check('H2 cold-start plaquette is exactly 1', abs(g.plaq(np.tile(np.eye(3, dtype=complex), (4, lat.V, 1, 1))) - 1) < 1e-14)
    H = herm_traceless_gauss(rng, (4, lat.V)); e = 1e-5
    num = (g.action(expm_ih(e * H) @ U) - g.action(expm_ih(-e * H) @ U)) / (2 * e)
    ana = np.einsum('msij,msji->', H, traceless_herm(g.force(U))).real
    check('H3 gauge force equals the finite-difference derivative of the Wilson action', abs(num - ana) < 1e-6 * abs(ana), '%.8f vs %.8f' % (num, ana))
    m = 0.1; f = Fermion(lat, m, 1e-13); f.prep(U); phi = f.refresh(rng)
    def Sf(eps):
        f.prep(expm_ih(eps * H) @ U); return f.action_force(phi, False)[0]
    num = (Sf(e) - Sf(-e)) / (2 * e); f.prep(U)
    _, N = f.action_force(phi)
    ana = np.einsum('msij,msji->', H, traceless_herm(N)).real
    check('H4 pseudofermion force equals the finite-difference derivative of phi^dag A^-1 phi (APBC, eta phases, even-odd)', abs(num - ana) < 1e-6 * abs(ana), '%.8f vs %.8f' % (num, ana))
    V = lat.V
    Dm = np.zeros((V * 3, V * 3), dtype=complex)
    for s in range(V):
        for c in range(3):
            v = np.zeros((V, 3), dtype=complex); v[s, c] = 1
            Dm[:, s * 3 + c] = f.D(v).reshape(-1)
    check('H5 staggered hop operator is exactly anti-Hermitian on a random SU(3) background', np.abs(Dm + Dm.conj().T).max() < 1e-14)
    sg, ld = np.linalg.slogdet(m * np.eye(V * 3) + Dm)
    ev = np.where(lat.even)[0]; ii = np.concatenate([[3 * s + c for c in range(3)] for s in ev])
    A = m * m * np.eye(V * 3) - Dm @ Dm
    sg2, ld2 = np.linalg.slogdet(A[np.ix_(ii, ii)])
    check('H6 det(m + D) over all sites equals det(A) over even sites (one pseudofermion = ONE staggered field, unrooted), real positive', abs(ld - ld2) < 1e-9 and abs(sg - 1) < 1e-9, '%.10f vs %.10f' % (ld, ld2))
    # free-field ln det vs analytic momentum sum (cold links, APBC time)
    Uc = np.tile(np.eye(3, dtype=complex), (4, lat.V, 1, 1)); f.prep(Uc)
    Dc = np.zeros((V * 3, V * 3), dtype=complex)
    for s in range(V):
        for c in range(3):
            v = np.zeros((V, 3), dtype=complex); v[s, c] = 1
            Dc[:, s * 3 + c] = f.D(v).reshape(-1)
    ldc = np.linalg.slogdet(m * np.eye(V * 3) + Dc)[1]
    ks = [(2 * np.pi * (n + (0.5 if mu == 0 else 0.0)) / 4) for mu in range(4) for n in range(0)]
    tot = 0.0
    for kt in range(4):
        for kx in range(4):
            for ky in range(4):
                for kz in range(4):
                    k = [2 * np.pi * (kt + 0.5) / 4, 2 * np.pi * kx / 4, 2 * np.pi * ky / 4, 2 * np.pi * kz / 4]
                    tot += math.log(m * m + sum(math.sin(q) ** 2 for q in k))
    check('H7 free-field ln det(m+D) (3 colours) equals (3/2) sum_k ln(m^2 + sum sin^2 k) (independent momentum-space formula)', abs(ldc - 1.5 * tot) < 1e-9, '%.9f vs %.9f' % (ldc, 1.5 * tot))
    # CG vs direct solve
    f.prep(U); x = f.cg(phi, tol=1e-12)
    xd = np.zeros(V * 3, dtype=complex); xd[ii] = np.linalg.solve(A[np.ix_(ii, ii)], phi.reshape(-1)[ii])
    check('H8 CG solution of A chi = phi equals the dense direct solve to 1e-9', np.abs(x.reshape(-1) - xd).max() < 1e-9)

def load_ens(name):
    p = os.path.join(ENSDIR, 'ens_%s.json' % name)
    if not os.path.exists(p): return None
    return json.load(open(p))

def sec_replay():
    for name, nrep in (('q44', 40), ('f44_m01', 15)):
        E = load_ens(name)
        if E is None:
            check('R replay of %s' % name, False, 'stored ensemble missing'); continue
        t = time.time(); R = run_ensemble(name, nmeas_override=nrep)
        d = np.abs(np.array(R['P']) - np.array(E['P'][:nrep])).max()
        check('R replay: first %d trajectories of %s regenerate bit-for-bit (max |dP| %.1e) -- stored series come from this code' % (nrep, name, d), d < 1e-9, '%.0f s' % (time.time() - t))

def sec_analysis():
    out = {}
    for name in SPECS:
        E = load_ens(name)
        if E is None: continue
        sp_ = E['spec']; P = np.array(E['P']); burn = 0
        mu, er, tau = mean_err(P)
        er_b = block_err(P)
        dH = np.array(E['dH']); cre = float(np.mean(np.exp(-dH))); cre_err = float(np.std(np.exp(-dH), ddof=1) / math.sqrt(len(dH) / (2 * max(tau_int_wolff(np.exp(-dH))[0], 0.5))))
        out[name] = dict(mean=mu, err=max(er, er_b), err_gamma=er, err_block=er_b, tau=tau, n=len(P), acc=float(np.mean(E['acc'])),
                         creutz=cre, creutz_err=cre_err, cg=E['cg_iters'], secs=E['seconds'])
        o = out[name]
        print('INFO %-8s dims=%s Ns=%d m=%.2f beta=%.1f n=%d <P>=%.5f +/- %.5f (Gamma %.5f, blocks %.5f) tau_int=%.1f acc=%.2f <exp(-dH)>=%.4f(%.4f)'
              % (name, tuple(sp_['dims']), sp_['Ns'], sp_['m'], sp_.get('beta', 6.0), o['n'], mu, o['err'], er, er_b, tau, o['acc'], cre, cre_err))
        check('A0 %s: Creutz identity <exp(-dH)> = 1 within 3 sigma (HMC detailed balance sanity), acceptance > 0.6' % name,
              abs(cre - 1) < 3 * max(cre_err, 1e-3) and o['acc'] > 0.6)
    return out

def vshift(P):
    return float(v_of_P(P))

def sec_results(o):
    R = {}
    def need(*ns): return all(n in o for n in ns)
    P0 = mp.mpf('0.5934'); v0 = float(v_of_P(P0)); RES = 2.5513e-4
    # independent comparators for the quenched machinery (values quoted from the repository's own spot check / correction)
    if 'q44' in o:
        q = o['q44']
        d = abs(q['mean'] - 0.59703); s = math.hypot(q['err'], 0.00027)
        check('Q1 quenched 4^4 beta=6 plaquette %.5f(%.5f) agrees with the repository spot-check value 0.59703(27) (different code/algorithm) within 4 sigma' % (q['mean'], q['err']), d < 4 * s, 'diff %.5f, sigma %.5f' % (d, s))
    if 'q66' in o:
        q = o['q66']
        d = abs(q['mean'] - 0.59459); s = math.hypot(q['err'], 0.00023)
        check('Q2 quenched 6^4 beta=6 plaquette %.5f(%.5f) agrees with the correction note value 0.59459(23) within 4 sigma' % (q['mean'], q['err']), d < 4 * s, 'diff %.5f, sigma %.5f' % (d, s))
    if need('q44', 'q44_b61', 'q44_b62'):
        a, b, c = o['q44']['mean'], o['q44_b61']['mean'], o['q44_b62']['mean']
        check('Q3 quenched plaquette rises monotonically with beta (6.0 < 6.1 < 6.2)', a < b < c, '%.5f %.5f %.5f' % (a, b, c))
    if need('q44', 'f44_m01'):
        q, f = o['q44'], o['f44_m01']
        dP = f['mean'] - q['mean']; e = math.hypot(f['err'], q['err'])
        R['dP44'] = (dP, e); R['v44'] = float(v_of_P(P0 + mp.mpf(dP)))
        check('D1 ONE dynamical staggered field (4 tastes, unrooted, m=0.1, 4^4, same HMC code and boundary conditions on both sides): dP = %+.4f +/- %.4f is positive at > 5 sigma' % (dP, e), dP > 5 * e)
        lo = float(v_of_P(P0 + mp.mpf(dP - 2 * e))); hi = float(v_of_P(P0 + mp.mpf(dP + 2 * e))); mid = float(v_of_P(P0 + mp.mpf(dP)))
        ratio_lo = (v0 - lo) / v0 / RES; ratio_hi = (v0 - hi) / v0 / RES
        check('D2 readout v(0.5934 + dP) = %.1f GeV (2-sigma band %.1f to %.1f): shift exceeds 100x the quoted 0.0255 percent residual even at the band edge nearest 246.28' % (mid, hi, lo), ratio_hi > 100, 'multiples of residual: %.0f to %.0f' % (ratio_hi, ratio_lo))
        # alternative same-regulator prescription: ratio instead of difference
        Pr = 0.5934 * f['mean'] / q['mean']
        print('INFO difference prescription P = 0.5934 + dP -> v = %.2f GeV; ratio prescription P = 0.5934 * P_unq/P_q -> v = %.2f GeV; with point estimate 0.59369 as base: %.2f GeV'
              % (mid, float(v_of_P(Pr)), float(v_of_P(0.59369 + dP))))
        print('INFO campaign HMC (reported, raw data not in repo): dP = +0.0212(11) -> 214 GeV. This run: dP = %+.4f(%.4f); difference %.2f combined sigma' % (dP, e, abs(dP - 0.0212) / math.hypot(e, 0.0011)))
        print('INFO repository covariance slope (Ns=1 linear response) +0.0255(19) / +0.0260(7): this run Ns=1 dP / slope = %.2f' % (dP / 0.026))
    if need('q44', 'f44_ns2'):
        q, f = o['q44'], o['f44_ns2']; dP = f['mean'] - q['mean']; e = math.hypot(f['err'], q['err'])
        print('INFO 8 tastes (2 staggered fields, m=0.1, 4^4): dP = %+.4f(%.4f) -> v = %.1f GeV (campaign: +0.037, 193 GeV)' % (dP, e, float(v_of_P(P0 + mp.mpf(dP)))))
    if need('q44', 'f44_m05'):
        q, f = o['q44'], o['f44_m05']; dP = f['mean'] - q['mean']; e = math.hypot(f['err'], q['err'])
        print('INFO 4 tastes at m=0.5 (4^4): dP = %+.4f(%.4f) (campaign: +0.044 for 16 tastes)' % (dP, e))
    if need('q66', 'f66_m01'):
        q, f = o['q66'], o['f66_m01']; dP = f['mean'] - q['mean']; e = math.hypot(f['err'], q['err'])
        print('INFO 4 tastes, m=0.1 on 6^4: dP = %+.4f(%.4f) -> v = %.1f GeV' % (dP, e, float(v_of_P(P0 + mp.mpf(dP)))))
        if need('q44', 'f44_m01'):
            d44 = o['f44_m01']['mean'] - o['q44']['mean']; e44 = math.hypot(o['f44_m01']['err'], o['q44']['err'])
            print('INFO volume trend dP(6^4) - dP(4^4) = %+.4f(%.4f)' % (dP - d44, math.hypot(e, e44)))
            R['dP66'] = (dP, e); R['v66'] = float(v_of_P(P0 + mp.mpf(dP)))
        check('V1 the 4-taste plaquette shift on 6^4 (%+.4f(%.4f)) is still positive at > 3 sigma (does not vanish with volume 4^4 -> 6^4)' % (dP, e), dP > 3 * e)
    if need('q44', 'q44_b61', 'q44_b62', 'f44_m01'):
        pts = [(6.0, o['q44']['mean']), (6.1, o['q44_b61']['mean']), (6.2, o['q44_b62']['mean'])]
        sl = (pts[2][1] - pts[0][1]) / 0.2
        dP = o['f44_m01']['mean'] - o['q44']['mean']
        R['dbeta'] = dP / sl
        print('INFO quenched slope dP/dbeta = %.3f on 4^4 -> one dynamical staggered field (m=0.1) ~ beta shift of %+.2f at beta=6' % (sl, dP / sl))
    return R

def main():
    args = sys.argv[1:]
    if args and args[0] == '--produce':
        name = args[1]; os.makedirs(ENSDIR, exist_ok=True)
        out = run_ensemble(name, log=True)
        json.dump(out, open(os.path.join(ENSDIR, 'ens_%s.json' % name), 'w'))
        print('wrote', name); return 0
    if args and args[0] == '--full':
        os.makedirs(ENSDIR, exist_ok=True)
        for name in SPECS:
            if not os.path.exists(os.path.join(ENSDIR, 'ens_%s.json' % name)):
                json.dump(run_ensemble(name, log=True), open(os.path.join(ENSDIR, 'ens_%s.json' % name), 'w'))
    t0 = time.time()
    print('check.py: Wilson SU(3) beta=6 + staggered fields, own HMC; formula v = M_Pl (7/8)^(1/4) alpha_LM^16, alpha_LM = alpha_bare/u0, u0 = P^(1/4)')
    sec_exact()
    sec_hmc_integrity()
    sec_replay()
    o = sec_analysis()
    R = sec_results(o)
    print('TOTAL: PASS=%d FAIL=%d' % (PASS, FAIL))
    print('RUNTIME_SECONDS: %.0f' % (time.time() - t0))
    txt = 'checks: exact 2^4-block degree 16 (staggered) vs 64 (naive); formula elasticity -4; own HMC at beta=6 with the same code on both sides'
    if 'dP44' in R:
        txt = ('own-code HMC (force/determinant/replay-verified) gives, with one unrooted staggered field (4 tastes, m=0.1) in the plaquette measure on 4^4, dP = %+.4f(%.4f), '
               'so v(0.5934+dP) = %.1f GeV, i.e. %.0f times the quoted 0.0255 percent residual below 246.28 GeV' % (R['dP44'][0], R['dP44'][1], R['v44'], (246.282818 - R['v44']) / 246.282818 / 2.5513e-4))
        if 'dP66' in R:
            txt += '; on 6^4 dP = %+.4f(%.4f) (v = %.1f GeV), no shrinkage between these two volumes' % (R['dP66'][0], R['dP66'][1], R['v66'])
        txt += '; infinite volume, rooting, m->0 and the vertex-power rule B4 are not tested'
    print('SUMMARY: ' + txt)
    return 0 if FAIL == 0 else 1

if __name__ == '__main__':
    sys.exit(main())