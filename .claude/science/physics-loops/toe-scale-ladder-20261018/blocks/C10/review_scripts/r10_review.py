#!/usr/bin/env python3
"""C10 independent review checks (reviewer code; walk rebuilt from the parent note's G(b)).
R1 domain: hop DFT, ranks, overlaps, commutator certificate.  R2 E-K / E-W statistics.
R3 identities by the eigen-route at 50 digits.  R4 O(a^2) comparison.  R5 clock spot check."""
import itertools, time, sys
import numpy as np, mpmath as mp, sympy as sp
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r10_walk import Walk, Ump, GAM, GAMmp, bpoints

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)

t0 = time.time()
B, ustar = bpoints(50)
print(f'u* = {ustar}')
WK = {nm: Walk(b) for nm, b in B.items()}
for nm, w in WK.items():
    errs = max(abs(np.linalg.norm(w.U(k, th, ch) @ w.U(k, th, ch).conj().T - np.eye(4)))
               for k in np.random.default_rng(1).uniform(-3, 3, (20, 3)) for th, ch in ((0, 0), (0.2, 0), (0.2, np.pi/2)))
    print(f'   {nm}: s = {w.s_n:.8f}, |W| = {float(mp.sqrt(w.W[0]**2+w.W[1]**2)):.6f} (s sqrt(1-s^2) = {w.s_n*np.sqrt(1-w.s_n**2):.6f}), unitarity err {errs:.1e}')
check('R0: rebuilt walk unitary at all three points; |W| = s sqrt(1-s^2)',
      all(max(abs(np.linalg.norm(w.U(k, 0.2, 1.0) @ w.U(k, 0.2, 1.0).conj().T - np.eye(4))) for k in np.random.default_rng(2).uniform(-3, 3, (10, 3))) < 1e-13
          and abs(float(mp.sqrt(w.W[0]**2+w.W[1]**2)) - w.s_n*np.sqrt(1-w.s_n**2)) < 1e-12 for w in WK.values()))

NS = list(itertools.product((-1, 0, 1), repeat=3))
def hops(w, th, ch):
    grid = [2*np.pi*j/3 for j in range(3)]
    A = {}
    for n in NS:
        S = np.zeros((4, 4), complex)
        for k in itertools.product(grid, repeat=3):
            S += np.exp(1j*np.dot(k, n)) * w.U(np.array(k), th, ch)
        A[n] = S/27
    return A

# ---------------- R1 domain
print('R1 domain test')
dom_ok = True; HOPS = {}
for nm, w in WK.items():
    for th, ch in ((0.0, 0.0), (0.2, 0.0), (0.2, np.pi/2)):
        A = hops(w, th, ch); HOPS[(nm, th, ch)] = A
        rec = max(np.abs(sum(np.exp(-1j*np.dot(k, n))*A[n] for n in NS) - w.U(k, th, ch)).max() for k in np.random.default_rng(3).uniform(-3, 3, (5, 3)))
        nz = [n for n in NS if np.abs(A[n]).max() > 1e-12]
        rk = sum(np.linalg.matrix_rank(A[n], tol=1e-10) for n in nz)
        ov = max(np.linalg.norm(A[n] @ A[m].conj().T, 2) for n in nz for m in nz if n != m)
        ove = max(np.abs(A[n] @ A[m].conj().T).max() for n in nz for m in nz if n != m)   # basis-dependent element measure
        kr = np.abs(sum(A[n].conj().T @ A[n] for n in NS) - np.eye(4)).max()
        # basis-free certificate: shift-coin => U(k) U(0)^dag = diag phases for all k => pairwise commuting
        C0 = w.U(np.zeros(3), th, ch)
        ks = np.random.default_rng(4).uniform(-2, 2, (6, 3))
        Ms = [w.U(k, th, ch) @ C0.conj().T for k in ks]
        comm = max(np.linalg.norm(a @ b - b @ a, 2) for a in Ms for b in Ms)
        print(f'   {nm} th={th} chi={ch:.2f}: rec {rec:.1e}, Kraus {kr:.1e}, nonzero hops {len(nz)}, rank sum {rk}, max ||A_n A_m^+||_2 {ov:.3f} (max element {ove:.3f}, basis-dependent), max ||[U(k)C^+, U(k\')C^+]|| {comm:.3f}')
        dom_ok &= (rec < 1e-12 and kr < 1e-12 and len(nz) == 27 and comm > 1e-2)
        HOPS[(nm, th, ch, 'stats')] = (rk, ov)
check('R1: 27 nonzero hops at every point/mass setting; U(k)U(0)^+ do not commute (basis-free: not shift-coin under any constant internal basis)', dom_ok)
rk0 = [HOPS[(nm, 0.0, 0.0, 'stats')][0] for nm in WK]
print(f'   rank sums (massless): {rk0}; all rank sums: {[HOPS[k][0] for k in HOPS if len(k) == 4]}')
check('R1b: rank sum = 92 at all points and mass settings (author: 92)', all(HOPS[k][0] == 92 for k in HOPS if len(k) == 4))
ovs = [HOPS[k][1] for k in HOPS if len(k) == 4]
check('R1c: overlaps nonzero; basis-invariant spectral norm max ||A_n A_m^+||_2 is theta-independent (A_n(th) = M A_n(0) M) and in [0.2, 0.26] '
      '(author quotes 0.16-0.23, a basis-dependent element measure)', min(ovs) > 0.2 and max(ovs) < 0.26 and
      all(abs(HOPS[(nm, 0.2, ch, 'stats')][1] - HOPS[(nm, 0.0, 0.0, 'stats')][1]) < 1e-12 for nm in WK for ch in (0.0, np.pi/2)), f'range {min(ovs):.3f}-{max(ovs):.3f}')

# ---------------- R2 E-K and E-W
print('R2 extensions')
def band(w, k, th, ch):
    """upper band: eigenvalue exp(-i om), om in (0, pi); returns om, 4x2 orthonormal basis."""
    ev, V = np.linalg.eig(w.U(k, th, ch))
    ph = -np.angle(ev)
    sel = [i for i in range(4) if ph[i] > 0]
    assert len(sel) == 2
    Q, _ = np.linalg.qr(V[:, sel])
    return float(np.mean(ph[sel])), Q
def omega(w, k, th, ch):
    ev = np.linalg.eigvals(w.U(k, th, ch)); ph = -np.angle(ev); return float(np.mean(ph[ph > 0]))
def vgrp(w, k, th, ch, hstep=1e-5):
    return np.array([(omega(w, k+hstep*e, th, ch) - omega(w, k-hstep*e, th, ch))/(2*hstep) for e in np.eye(3)])
dirs = [np.array(d, float)/np.linalg.norm(d) for d in ((1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 3))]
rng = np.random.default_rng(5)
ratK, devK, imW, reW, mWdev = [], [], [], [], []
ratK_massless = []
for nm, w in WK.items():
    for th, ch in ((0.0, 0.0), (0.2, 0.0), (0.2, np.pi/2)):
        A = HOPS[(nm, th, ch)]
        for d in dirs:
            for kk in (0.05, 0.2, 0.5):
                k = kk*d; om, Q = band(w, k, th, ch); v = vgrp(w, k, th, ch)
                for trial in range(12):
                    c = rng.normal(size=2) + 1j*rng.normal(size=2); u = Q @ (c/np.linalg.norm(c))
                    P = {n: np.linalg.norm(A[n] @ u)**2 for n in NS}
                    wv = {n: np.exp(1j*om)*np.exp(-1j*np.dot(k, n))*(u.conj() @ A[n] @ u) for n in NS}
                    mK = sum(P[n]*np.array(n) for n in NS); mW = sum(wv[n]*np.array(n) for n in NS)
                    assert abs(sum(P.values()) - 1) < 1e-12 and abs(sum(wv.values()) - 1) < 1e-12
                    ratK.append(np.linalg.norm(mK)/np.linalg.norm(v)); devK.append(np.linalg.norm(mK - v)/np.linalg.norm(v))
                    if th == 0: ratK_massless.append(np.linalg.norm(mK)/np.linalg.norm(v))
                    imW.append(max(abs(x.imag) for x in wv.values())); reW.append(min(x.real for x in wv.values()))
                    mWdev.append(np.abs(mW - v).max())
print(f'   E-K |m|/|v|: massless [{min(ratK_massless):.3f}, {max(ratK_massless):.3f}] mean {np.mean(ratK_massless):.3f}; all [{min(ratK):.3f}, {max(ratK):.3f}]; min rel |m-v|/|v| {min(devK):.3f}')
print(f'   E-W: max |mean - v| {max(mWdev):.1e}; max |Im w| {max(imW):.3f}; min Re w {min(reW):.3f}')
check('R2a: E-W mean step = group velocity (eigenphase FD) to 1e-8, all points, random band vectors', max(mWdev) < 1e-8)
check('R2b: E-W weights complex: max |Im w_n| in [0.55, 0.70] (author: up to 0.62), min Re w < -0.6 (author -0.68)', 0.55 < max(imW) < 0.70 and min(reW) < -0.6, f'{max(imW):.3f}, {min(reW):.3f}')
check('R2c: E-K mean step is 10-20% of |v| for massless members (author: |m| 0.12-0.16 vs |v| ~0.9)', 0.10 < min(ratK_massless) and max(ratK_massless) < 0.20)
check('R2d: E-K min relative deviation |m-v|/|v| >= 0.6 over the declared set (author: >= 0.63)', min(devK) > 0.6, f'{min(devK):.3f}')
# reduction on a shift-coin walk (BT's 1D walk with random coin): E-K = E-W = |u_d|^2
cth = 0.37; C = np.array([[np.cos(cth), -1j*np.sin(cth)], [-1j*np.sin(cth), np.cos(cth)]])
red = 0
for k in (0.3, 1.1, -2.0):
    Uk = np.diag([np.exp(-1j*k), np.exp(1j*k)]) @ C; ev, V = np.linalg.eig(Uk)
    Ad = {+1: np.diag([1, 0]) @ C, -1: np.diag([0, 1]) @ C}
    for i in range(2):
        u = V[:, i]/np.linalg.norm(V[:, i]); om = -np.angle(ev[i])
        for d in (1, -1):
            pB = abs(u[0 if d == 1 else 1])**2
            red = max(red, abs(np.linalg.norm(Ad[d] @ u)**2 - pB), abs(np.exp(1j*om)*np.exp(-1j*k*d)*(u.conj() @ Ad[d] @ u) - pB))
check('R2e: on a 1D shift-coin walk both extensions reduce to the Born odds |u_d|^2', red < 1e-14, f'{red:.1e}')

# ---------------- R3 identities, eigen-route, 50 digits
print('R3 identities (mpmath, dps 50; v by numerical derivative of the eigenphase of the explicit 4x4 U)')
mp.mp.dps = 50
def om_mp(w, k, th, ch):
    E = mp.eig(Ump(w, k, th, ch), left=False, right=False)
    ph = [-mp.arg(e) for e in E]; ph = [p for p in ph if p > 0]
    return (ph[0] + ph[1])/2
def band_mp(w, k, th, ch):
    E, ER = mp.eig(Ump(w, k, th, ch))
    idx = [i for i in range(4) if -mp.arg(E[i]) > 0]
    return [ER[:, i] for i in idx]
def expv(u, Mx):
    return (u.H * Mx * u)[0] / (u.H * u)[0]
rngm = np.random.default_rng(7)
worst_alpha = worst_D = worst_E4 = mp.mpf(0)
for nm, w in WK.items():
    b0, b1, b2 = w.b; s = w.s
    beta = -s*(b0-b1-2*b2)/3; Cc = -3*b0*b1 + 2*b0*b2 - 3*b1**2 + 7*b1*b2 + 5*b2**2
    for (th, ch) in ((0, 0), (mp.mpf('0.3'), 0), (mp.mpf('0.3'), mp.pi/2), (mp.mpf('0.2'), mp.mpf('0.7'))):
        hv = (mp.cos(ch), mp.sin(ch))
        cv = [hv[0]*w.H[0, j] + hv[1]*w.H[1, j] for j in range(4)]
        hW = cv[1] + 2*cv[2] + cv[3]
        lam = mp.cos(th) - mp.sin(th)*hW/s**2
        E1 = -3*beta*mp.cos(th) + mp.sin(th)*(cv[2]+cv[3] - hW*(b1+b2)/s)
        E2 = Cc*mp.cos(th) - mp.sin(th)*(cv[3] - hW*b2/s)
        for trial in range(2):
            k = [mp.mpf(str(x)) for x in rngm.uniform(-1.2, 1.2, 3)]
            om = om_mp(w, k, th, ch)
            v = [mp.diff(lambda t, a=a: om_mp(w, [k[j] + (t if j == a else 0) for j in range(3)], th, ch), 0) for a in range(3)]
            D = [v[a]*mp.sin(om) for a in range(3)]
            f, h, g = w.comps(k, M=mp)
            # <alpha_i> for two random band vectors (alpha = -tau3 sigma = -Gamma_{3..5})
            us = band_mp(w, k, th, ch)
            for _ in range(2):
                c1, c2 = [mp.mpc(*rngm.normal(size=2)) for _ in range(2)]
                u = c1*us[0] + c2*us[1]
                for a in range(3):
                    worst_alpha = max(worst_alpha, abs(expv(u, -GAMmp[2+a]) - g[a]/mp.sin(om)))
            x = [1 - mp.cos(kk) for kk in k]
            for a in range(3):
                bb, cc = (a+1) % 3, (a+2) % 3
                rhs = lam*s*g[a] + mp.sin(k[a])*(E1*(x[bb]+x[cc]) + E2*x[bb]*x[cc])
                worst_E4 = max(worst_E4, abs(D[a] - rhs))
print(f'   max |<alpha_i> - g_i/sin om| = {mp.nstr(worst_alpha, 3)}; max |D - lam s g - sin k[E1(x+x)+E2 xx]| = {mp.nstr(worst_E4, 3)}')
check('R3a: <alpha_i> = g_i/sin(omega) for random vectors of the upper band (massless and massive, 3 points) to 1e-30', worst_alpha < mp.mpf('1e-30'))
check('R3b: v sin(omega) (eigen-route) = lam s g + sin k_a [E1(x_b+x_c) + E2 x_b x_c], 3 points x 4 mass settings x random k, to 1e-25', worst_E4 < mp.mpf('1e-25'))
# beta = C7 anisotropy: omega^2 of the massless member, coefficient of sum k^4 (sympy, symbolic b)
b0s, b1s, b2s = sp.symbols('b0 b1 b2'); ks = sp.symbols('k1:4'); ep = sp.Symbol('e')
from r10_walk import Gmat
Gs = sp.Matrix(Gmat(b0s, b1s, b2s, sp)); cs = [sp.cos(ep*x) for x in ks]
ph = [1, sum(cs), cs[0]*cs[1]+cs[0]*cs[2]+cs[1]*cs[2], cs[0]*cs[1]*cs[2]]
f0 = sum((Gs*sp.Matrix([1, 3, 3, 1]))[i]*ph[i] for i in range(4))
y = sp.expand(sp.series(1 - f0, ep, 0, 7).removeO())   # 1 - cos om
# om^2 = 2y + y^2/3 + ...  (arccos(1-y)^2 series)
om2 = sp.expand(sp.series(2*y + y**2/3, ep, 0, 5).removeO()).coeff(ep, 4)
P = sp.Poly(om2, *ks)
sk4 = P.coeff_monomial(ks[0]**4); k2k2 = P.coeff_monomial(ks[0]**2*ks[1]**2)
# om2 quartic = alpha |k|^4 + beta' sum k^4 => coeff k1^4 = alpha + beta', coeff k1^2k2^2 = 2 alpha
betap = sp.factor(sk4 - k2k2/2)
sv = b0s + 2*b1s + b2s
print(f"   omega^2 quartic: sum k^4 coefficient = {betap}")
check("R3c: the sum k^4 coefficient of omega^2 (own series) equals beta = -s(b0-b1-2b2)/3 exactly (C7's anisotropy coefficient)",
      sp.simplify(betap + sv*(b0s-b1s-2*b2s)/3) == 0)
# massless identity in polynomial form: dF/dc1 - s(b0+b1(c2+c3)+b2c2c3) = -3beta(x2+x3) + C x2 x3
c1, c2, c3 = sp.symbols('c1:4')
F0 = sum((Gs*sp.Matrix([1, 3, 3, 1]))[i]*[1, c1+c2+c3, c1*c2+c1*c3+c2*c3, c1*c2*c3][i] for i in range(4))
betas = -sv*(b0s-b1s-2*b2s)/3; Cs = -3*b0s*b1s + 2*b0s*b2s - 3*b1s**2 + 7*b1s*b2s + 5*b2s**2
res = sp.expand(sp.diff(F0, c1) - sv*(b0s + b1s*(c2+c3) + b2s*c2*c3) - (-3*betas*((1-c2)+(1-c3)) + Cs*(1-c2)*(1-c3)))
check('R3d: E3 as a polynomial identity in (c, b) via D_1 = sin k1 df/dc1 (sympy)', res == 0)
Ciso = Cs.subs({b0s: (sp.sqrt(6)+2*sp.sqrt(15))/27, b1s: (5*sp.sqrt(6)-2*sp.sqrt(15))/27, b2s: (2*sp.sqrt(15)-2*sp.sqrt(6))/27})
check('R3e: C(b_iso) = (10 sqrt10 - 32)/27', sp.simplify(sp.radsimp(sp.expand(Ciso)) - (10*sp.sqrt(10)-32)/27) == 0 or abs(float(Ciso) - (10*np.sqrt(10)-32)/27) < 1e-14, f'{float(Ciso):.8f}')

# ---------------- R4 comparison (massless; tensors from eigen-route v, <alpha>)
print('R4 comparison: T^BT,W = om v v (dust); T^M1 = om <a><a>/... built from eigen-route quantities')
def tensors(w, k, th=0, ch=0):
    om = om_mp(w, k, th, ch)
    v = [mp.diff(lambda t, a=a: om_mp(w, [k[j] + (t if j == a else 0) for j in range(3)], th, ch), 0) for a in range(3)]
    us = band_mp(w, k, th, ch); al = [expv(us[0], -GAMmp[2+a]) .real for a in range(3)]
    rho = om/mp.sin(om); g = [al[a]*mp.sin(om) for a in range(3)]; sk = [mp.sin(x) for x in k]; s = w.s
    sym = lambda p, q: mp.matrix([[(p[i]*q[j] + p[j]*q[i])/2 for j in range(3)] for i in range(3)])
    T = {'BT': om*sym(v, v), 'M1': rho*sym(al, g), 'M2': sym(al, g), 'M3': s*sym(al, sk), 'M4': sym(v, sk)}
    return T, om, v, al, g
def relmis(T, X, cst):
    d = T[X] - T['BT']/cst
    return max(abs(d[i, j]) for i in range(3) for j in range(3))/max(abs(T[X][i, j]) for i in range(3) for j in range(3))
slopes = {}
for nm, w in WK.items():
    s = w.s; b0, b1, b2 = w.b; beta = -s*(b0-b1-2*b2)/3
    for dn, d in (('123', (1, 2, 3)), ('111', (1, 1, 1)), ('100', (1, 0, 0))):
        n = [mp.mpf(x)/mp.sqrt(sum(y*y for y in d)) for x in d]
        Ds = {}
        for kap in (mp.mpf('0.02'), mp.mpf('0.01')):
            T, om, v, al, g = tensors(w, [kap*x for x in n])
            Ds[kap] = {X: relmis(T, X, s**2) for X in ('M1', 'M2', 'M3', 'M4')}
            Ds[kap]['asgiven'] = relmis(T, 'M1', 1)
            if kap == mp.mpf('0.01'):
                # kappa^4 coefficient of (g g - D D / s^2)_xx, D = v sin om
                Dv = [x*mp.sin(om) for x in v]
                c4 = (g[0]*g[0] - Dv[0]*Dv[0]/s**2)/kap**4
                pred = 3*beta*n[0]**2*(n[1]**2+n[2]**2)
                slopes[(nm, dn, 'c4')] = (c4, pred)
        for X in ('M1', 'M2', 'M3', 'M4'):
            a, b_ = Ds[mp.mpf('0.02')][X], Ds[mp.mpf('0.01')][X]
            slopes[(nm, dn, X)] = (float(mp.log(a/b_)/mp.log(2)) if b_ > 0 else float('nan'), float(b_))
        slopes[(nm, dn, 'asgiven')] = float(Ds[mp.mpf('0.01')]['asgiven'])
    print(f'   {nm}: ' + '; '.join(f'{dn} ' + ' '.join(f'{X} sl {slopes[(nm, dn, X)][0]:.2f} (D {slopes[(nm, dn, X)][1]:.1e})' for X in ('M1', 'M2', 'M3', 'M4')) for dn in ('123', '111', '100')))
    print(f'      as-given M1 rel dev at kappa=.01 (123): {slopes[(nm, "123", "asgiven")]:.4f} vs 1 - s^2 = {float(1-s**2):.4f};  '
          f'kappa^4 xx coeff (123): {mp.nstr(slopes[(nm, "123", "c4")][0], 8)} vs 3 beta n1^2(n2^2+n3^2) = {mp.nstr(slopes[(nm, "123", "c4")][1], 8)}')
check('R4a: as-given continuum deviation = 1 - s^2 (b* 0.164, b_iso 1/3, b_gold 0) within 2e-3',
      all(abs(slopes[(nm, '123', 'asgiven')] - float(1-WK[nm].s**2)) < 2e-3 for nm in WK))
check('R4b: M1 O(a^2) mismatch coefficient = 3 beta n1^2(n2^2+n3^2) (xx, generic dir), b* and b_gold, to 1%; ~0 at b_iso',
      all(abs(slopes[(nm, '123', 'c4')][0]/slopes[(nm, '123', 'c4')][1] - 1) < 1e-2 for nm in ('bstar', 'gold')) and abs(slopes[('iso', '123', 'c4')][0]) < 1e-3)
check('R4c: M1 slope ~2 off-axis at b*, b_gold; ~4 at b_iso; M2-M4 slope ~2 along (123) at all points',
      all(1.9 < slopes[(nm, dn, 'M1')][0] < 2.1 for nm in ('bstar', 'gold') for dn in ('123', '111')) and
      all(3.8 < slopes[('iso', dn, 'M1')][0] < 4.2 for dn in ('123', '111')) and
      all(1.9 < slopes[(nm, '123', X)][0] < 2.1 for nm in WK for X in ('M2', 'M3', 'M4')))
check('R4d: on the axis (100) M1 agrees exactly (D < 1e-25) at all points; at b_iso (111) M3, M4 slope ~4, M2 ~2',
      all(slopes[(nm, '100', 'M1')][1] < 1e-25 for nm in WK) and all(3.8 < slopes[('iso', '111', X)][0] < 4.2 for X in ('M3', 'M4')) and 1.9 < slopes[('iso', '111', 'M2')][0] < 2.1)
# massive, b_iso, registered constant s^2: Wilson-aligned slope 1, maximal twist slope 2
mm = {}
for ch in (0, mp.pi/2):
    w = WK['iso']; s = w.s; n = [mp.mpf(x)/mp.sqrt(14) for x in (1, 2, 3)]
    Dk = []
    for kap in (mp.mpf('0.02'), mp.mpf('0.01')):
        T = tensors(w, [kap*x for x in n], kap, ch)[0]
        Dk.append(relmis(T, 'M1', s**2))
    mm[float(ch)] = float(mp.log(Dk[0]/Dk[1])/mp.log(2))
print(f'   b_iso massive (theta = kappa), M1 at constant s^2: slopes Wilson-aligned {mm[0.0]:.2f}, maximal twist {mm[float(mp.pi/2)]:.2f}')
check('R4e: b_iso massive at registered constant: M1 mismatch O(a) Wilson-aligned, O(a^2) maximal twist', 0.9 < mm[0.0] < 1.15 and 1.85 < mm[float(mp.pi/2)] < 2.15)

# ---------------- R5 clock at rest
print('R5 clock spot check: E-K turn action at rest = om (<|n|^2>_K - |m_K|^2)')
mp.mp.dps = 15
act = {}
for nm, w in WK.items():
    for th, ch in ((0.2, 0.0), (0.2, np.pi/2), (0.05, np.pi/2)):
        A = HOPS[(nm, th, ch)] if (nm, th, ch) in HOPS else hops(w, th, ch)
        k = np.zeros(3); om, Q = band(w, k, th, ch)
        vals = []
        for _ in range(6):
            c = rng.normal(size=2) + 1j*rng.normal(size=2); u = Q @ (c/np.linalg.norm(c))
            P = {n: np.linalg.norm(A[n] @ u)**2 for n in NS}
            n2 = sum(P[n]*np.dot(n, n) for n in NS); m = sum(P[n]*np.array(n) for n in NS)
            vals.append((om*(n2 - m @ m)/th, n2, np.linalg.norm(m), om))
        act[(nm, th, ch)] = vals
        print(f'   {nm} th={th} chi={ch:.2f}: action/theta in [{min(x[0] for x in vals):.4f}, {max(x[0] for x in vals):.4f}], <|n|^2>_K [{min(x[1] for x in vals):.4f}, {max(x[1] for x in vals):.4f}], |m_K| max {max(x[2] for x in vals):.2e}, om/theta {vals[0][3]/th:.6f}')
n2K = {nm: np.mean([x[1] for k_, vs in act.items() if k_[0] == nm for x in vs]) for nm in WK}
check('R5a: <|n|^2>_K at rest = 0.539 (b*), 0.519 (b_iso), 0.640 (b_gold) to 2e-3, band- and theta-independent to 1e-10',
      abs(n2K['bstar'] - 0.539) < 2e-3 and abs(n2K['iso'] - 0.519) < 2e-3 and abs(n2K['gold'] - 0.640) < 2e-3 and
      all(max(x[1] for x in vs) - min(x[1] for x in vs) < 1e-10 for vs in act.values()) and
      all(abs(np.mean([x[1] for x in act[(nm, a, b)]]) - n2K[nm]) < 1e-10 for (nm, a, b) in act), str({k: round(v, 5) for k, v in n2K.items()}))
check('R5b: at rest the E-K action/theta (= m^2/eps target 1) is far from 1 (< 0.7) at all points', all(max(x[0] for x in vs) < 0.7 for vs in act.values()))
print(f'elapsed {time.time()-t0:.0f} s')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
