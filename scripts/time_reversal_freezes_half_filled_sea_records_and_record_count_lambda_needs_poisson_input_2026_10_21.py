#!/usr/bin/env python3
"""Is the record set a Poisson causal set? (supplied model; finite diagnostic; no physical identification)

Tests the proposal "the geometry's 4-volume is the number of records" against the CANDIDATE_LAWS_v3 rules
(CL-3 Margolus half-ticks, CL-4 a record at each occupied mode per half-tick, CL-5 Born-following transport
that leaves the most in place), and the Sorkin estimate rho_Lambda ~ hbar / delta V that it would feed.
 A  the Sorkin estimate rederived: unimodular conjugacy, Poisson delta N, element-volume and Fano dependence;
 B  1D Margolus walk, half-filled Floquet sea, exact many-body odds and sampled CL-5 trajectories: record counts;
 C  3D spin-3/2 Margolus tick (CL-3), half-filled gapped sea: frozen-vacuum theorem, area law, past-cone variance;
 D  predicted Lambda with the rules' own normalisation, three readings, against the measured 1.13e-123 rho_P;
 E  measured constraints on a Sorkin-type (everpresent) Lambda: today's value, w, BBN and recombination.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

T0 = time.monotonic(); PASS = FAIL = 0
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ---------------------------------------------------------------- constants and the rules' unit map (supplied)
hbar, c, Gn = 1.054571817e-34, 2.99792458e8, 6.67430e-11
lP, tP = np.sqrt(hbar * Gn / c ** 3), np.sqrt(hbar * Gn / c ** 5); rhoP = c ** 7 / (hbar * Gn ** 2)
a_site = np.sqrt(8 * np.pi) * lP                 # CL-6: G = a^2 / (8 pi) per cell
tau = 2 * a_site / (np.sqrt(3) * c)              # one tick: light speed 1/sqrt3 block (= 2a) per tick
KAPPA = a_site ** 3 * (tau / 2) / 0.5 / (lP ** 3 * tP)   # 4-volume per record: a^3 tau/2 per site half-tick, 1/2 occupied
H0 = 67.4e3 / 3.0857e22; Om, OL = 0.315, 0.6847; Or = 4.18e-5 / 0.674 ** 2; Ok = 1 - Om - OL - Or
rhoL_meas = OL * 3 * H0 ** 2 / (8 * np.pi * Gn) * c ** 2 / rhoP

print('== A. the Sorkin estimate, rederived')
# Unimodular action S = (1/16 pi G) int sqrt(-g) R - rho_L V + matter, with V = int sqrt(-g) d^4x the only place rho_L enters.
# rho_L is then the momentum conjugate to V ("energy" to "time"): psi(V) ~ exp(-i rho_L V / hbar), so delta rho_L delta V >= hbar/2.
# Check the conjugacy numerically: a Gaussian packet in rho_L, Fourier-transformed to V, saturates the bound.
s = 0.37; r = np.linspace(-40, 40, 4001); psi = np.exp(-r ** 2 / (4 * s ** 2)); Vg = np.fft.fftshift(np.fft.fftfreq(r.size, r[1] - r[0])) * 2 * np.pi
phi = np.fft.fftshift(np.fft.fft(psi)); pr, pv = psi ** 2 / np.sum(psi ** 2), abs(phi) ** 2 / np.sum(abs(phi) ** 2)
dr = np.sqrt(np.sum(pr * r ** 2)); dv = np.sqrt(np.sum(pv * Vg ** 2))
check('unimodular conjugacy: a minimum-uncertainty packet in rho_L has delta rho_L delta V = hbar/2 (hbar = 1)', abs(dr * dv - 0.5) < 1e-6, f'{dr * dv:.8f}')
# If V = v0 N and N is Poisson, delta V = v0 sqrt(N) = sqrt(v0 V). With Fano factor F (Var N = F <N>):
#   conjugacy reading (U):  rho_L ~ hbar / delta V        = hbar / sqrt(F v0 V)
#   classical-sum reading (C, Lambda = S/V of Ahmed-Dodelson-Greene-Sorkin): rho_L ~ hbar delta N / V = hbar sqrt(F) / sqrt(v0 V)
VP_test, F_test = 1e10, np.array([0.01, 1.0, 100.0])
U_, C_ = 1 / np.sqrt(F_test * KAPPA * VP_test), np.sqrt(F_test) / np.sqrt(KAPPA * VP_test)
check('the two readings agree only for Poisson counting (F = 1); for F != 1 they move in opposite directions (ratio F)',
      abs(U_[1] / C_[1] - 1) < 1e-12 and np.allclose(C_ / U_, F_test), f'(C)/(U) = {np.round(C_ / U_, 3)}')
check(f'coarser elements lower the estimate: rho_L/rho_P = 1/sqrt(F kappa V_P), kappa = {KAPPA:.1f} Planck 4-volumes per record '
      '(not 1/sqrt(N_cells), which is larger by kappa)', abs(KAPPA - 2 * (8 * np.pi) ** 2 / np.sqrt(3)) < 1e-6)

print('== B. 1D Margolus walk, half-filled Floquet sea, exact odds, CL-5 trajectories (L = 12, 924 configurations)')
L, F1 = 12, 6; m1, m2 = 0.9, 0.3
def upair(m): return np.cos(m / 2) * np.array([[0, 1], [1, 0]]) + 1j * np.sin(m / 2) * np.eye(2)
def Uhalf(m, odd, flux=0.0):
    U = np.zeros((L, L), complex)
    for j in range(L // 2):
        a, b = (2 * j + odd) % L, (2 * j + 1 + odd) % L; U[np.ix_([a, b], [a, b])] = upair(m)
    if odd and flux: U[0, L - 1] *= np.exp(1j * flux); U[L - 1, 0] *= np.exp(-1j * flux)
    return U
confs = np.array(list(itertools.combinations(range(L), F1))); nc = len(confs)
occ = np.zeros((nc, L), bool); [occ.__setitem__((i, cf), True) for i, cf in enumerate(confs)]
def sea(Ue, Uo):
    w, V = np.linalg.eig(Uo @ Ue); om = -np.angle(w); Q, _ = np.linalg.qr(V[:, om < 0]); return Q, (om < 0).sum()
def odds(Phi): return abs(np.linalg.det(Phi[confs])) ** 2
def kernel(pa, pb, odd, rule):
    """CL-5: keep the odds, use only half-tick-connected moves (same pair occupations), leave the most in place.
    The surplus is routed by a supplied tie-break: 'prop' (to deficits in proportion) or 'nw' (north-west corner)."""
    prs = [((2 * j + odd) % L, (2 * j + 1 + odd) % L) for j in range(L // 2)]
    key = np.unique(np.stack([occ[:, x].astype(int) + occ[:, y] for x, y in prs], 1), axis=0, return_inverse=True)[1].ravel()
    rows = [None] * nc; gapmax = 0.0
    for g in np.unique(key):
        idx = np.where(key == g)[0]; a, b = pa[idx], pb[idx]; gapmax = max(gapmax, abs(a.sum() - b.sum()))
        st = np.minimum(a, b); sp = a - st; dm = b - st; D = sp.sum()
        for ii, cc in enumerate(idx): rows[cc] = [(cc, st[ii] / a[ii] if a[ii] > 0 else 1.0)]
        if D <= 1e-300: continue
        if rule == 'prop':
            for ii in np.where(sp > 0)[0]: rows[idx[ii]] += [(idx[jj], sp[ii] / a[ii] * dm[jj] / D) for jj in np.where(dm > 0)[0]]
        else:
            si, di = list(np.where(sp > 0)[0]), list(np.where(dm > 0)[0]); ss, dd = sp.copy(), dm.copy(); i0 = j0 = 0
            while i0 < len(si) and j0 < len(di):
                ii, jj = si[i0], di[j0]; f = min(ss[ii], dd[jj]); rows[idx[ii]].append((idx[jj], f / a[ii])); ss[ii] -= f; dd[jj] -= f
                i0 += ss[ii] <= 1e-18 * D; j0 += dd[jj] <= 1e-18 * D
    return rows, gapmax
def sampler(rows):
    mx = max(len(x) for x in rows); nxt = np.zeros((nc, mx), np.int32); cum = np.ones((nc, mx))
    for cc, rr in enumerate(rows):
        t = np.array([x[0] for x in rr]); cs = np.cumsum([x[1] for x in rr]); cs /= cs[-1]
        nxt[cc, :len(rr)] = t; nxt[cc, len(rr):] = t[-1]; cum[cc, :len(rr)] = cs
    return nxt, cum
def push(p, rows):
    q = np.zeros(nc)
    for cc, rr in enumerate(rows):
        for t, x in rr: q[t] += p[cc] * x
    return q
def run_chain(flux, rule, M=1500, Tm=520):
    Ue, Uo = Uhalf(m1, 0), Uhalf(m2, 1, flux); Phi0, nf = sea(Ue, Uo); p0, p1 = odds(Phi0), odds(Ue @ Phi0)
    Ke, ge = kernel(p0, p1, 0, rule); Ko, go = kernel(p1, p0, 1, rule)
    merr = max(abs(push(p0, Ke) - p1).max(), abs(push(p1, Ko) - p0).max())
    stay = sum(p0[cc] * rr[0][1] for cc, rr in enumerate(Ke))
    Se, So = sampler(Ke), sampler(Ko); cur = rng.choice(nc, M, p=p0 / p0.sum()); traj = np.zeros((Tm, M), np.int32)
    for t in range(Tm):
        traj[t] = cur; nxt, cum = Se if t % 2 == 0 else So
        k = np.minimum((cum[cur] < rng.random(M)[:, None]).sum(1), nxt.shape[1] - 1); cur = nxt[cur, k]
    n = occ[traj]; fano = {}
    for ell, T in ((2, 2), (6, 2), (2, 512), (6, 512), (6, 6)):
        Ns = np.array([n[:T][:, :, [(x0 + i) % L for i in range(ell)]].sum((0, 2)) for x0 in range(0, L, 2)])
        fano[(ell, T)] = Ns.var(1).mean() / Ns.mean()
    s4 = n[:, :, :4].sum(2).astype(float); s4 -= s4.mean(); ac = np.mean(s4[:-256] * s4[256:]) / np.mean(s4 * s4)
    return dict(nf=nf, tv=0.5 * abs(p0 - p1).sum(), gap=max(ge, go), merr=merr, stay=stay, fano=fano, ac256=ac)
R0p, R0n, R1p = run_chain(0.0, 'prop'), run_chain(0.0, 'nw'), run_chain(1.0, 'prop')
check('the half-tick conserves each pair\'s occupation, so CL-5 splits into independent groups; both tie-breaks keep the odds',
      max(R0p['gap'], R1p['gap']) < 1e-12 and max(R0p['merr'], R0n['merr'], R1p['merr']) < 1e-12, f"filled modes {R0p['nf']}/{L}")
check('THEOREM (1D): the pair unitaries are symmetric, so U_e U_o = (U_o U_e)^T and the sea has identical odds at both half-ticks',
      R0p['tv'] < 1e-12, f"TV(p0, p1) = {R0p['tv']:.1e}")
check('so CL-5 moves nothing: the vacuum configuration, hence every vacuum record, is frozen (stay = 1, any tie-break)',
      abs(R0p['stay'] - 1) < 1e-12 and abs(R0n['stay'] - 1) < 1e-12 and R0p['ac256'] > 0.99, f"autocorrelation at 256 half-ticks {R0p['ac256']:.3f}")
check('control: a ring flux breaks the antiunitary; the odds then change, CL-5 moves the configuration, correlations decay',
      R1p['tv'] > 0.01 and R1p['stay'] < 0.99 and R1p['ac256'] < 0.5, f"TV {R1p['tv']:.3f}, stay {R1p['stay']:.3f}, autocorr(256) {R1p['ac256']:.2f}")
fs = lambda R: ', '.join(f'{k[0]}x{k[1]}: {v:.2f}' for k, v in R['fano'].items())
print(f"   Fano Var/mean of records in sites x half-ticks windows. frozen: {fs(R0p)}\n   moving (flux 1): {fs(R1p)}")
check('record counts are not Poisson in either case: the Fano factor depends on the window shape (Poisson: 1 for every window)',
      all(min(R['fano'].values()) < 0.4 and max(R['fano'].values()) > 20 for R in (R0p, R1p)))
# frozen sea on a long ring, exact: Var(sum_x w_x n_x) = w.Cov.w, Cov = diag(C) - |C|^2. Causal diamond weights w_x = max(0, T - |x|).
Lr = 400
def Uh(m, odd, LL):
    U = np.zeros((LL, LL), complex)
    for j in range(LL // 2):
        a, b = (2 * j + odd) % LL, (2 * j + 1 + odd) % LL; U[np.ix_([a, b], [a, b])] = upair(m)
    return U
w_, V_ = np.linalg.eig(Uh(m2, 1, Lr) @ Uh(m1, 0, Lr)); Q_, _ = np.linalg.qr(V_[:, -np.angle(w_) < 0]); Cr = Q_ @ Q_.conj().T
Cov = np.diag(np.real(np.diag(Cr))) - abs(Cr) ** 2; xs = np.arange(Lr) - Lr // 2; vd = []
for T in (8, 16, 32, 64, 128):
    w = np.maximum(0, T - abs(xs)).astype(float); vd.append((T, w @ Cov @ w, w.sum() / 2))
ex1 = np.polyfit(np.log([v[0] for v in vd[2:]]), np.log([v[1] for v in vd[2:]]), 1)[0]
check('1+1D frozen sea, past-cone (diamond) records: Var grows as T^1 while the mean grows as T^2 (Poisson would need T^2)',
      abs(ex1 - 1) < 0.1, f'exponent {ex1:.3f}; Fano at T=128: {vd[-1][1] / vd[-1][2]:.4f}')

print('== C. 3D spin-3/2 Margolus tick (CL-3), gapped half-filled sea (mu = 0.4, b = 0.3)')
from math import comb
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = (2 * CORN - 1).astype(float); OPP = 7 - np.arange(8)
def coherent(j, nv):
    th, ph, d = np.arccos(np.clip(nv[2], -1, 1)), np.arctan2(nv[1], nv[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])
XI = [coherent(1.5, v / np.sqrt(3)) for v in NV]; W0 = np.zeros((8, 8), complex)
for s_, t_ in itertools.product(range(8), repeat=2):
    if abs(CORN[s_] - CORN[t_]).sum() == 1: g = XI[s_].conj() @ XI[t_]; W0[s_, t_] = -g / abs(g) / np.sqrt(3)
def Wmu(m): return np.cos(m / 2) * W0 + 1j * np.sin(m / 2) * np.eye(8)
mu, bst = 0.4, 0.3; We, Wo = Wmu(2 * (mu / 2 + bst)), Wmu(2 * (mu / 2 - bst))
def half(psi, Wm, odd):
    X, Y, Z = psi.shape; p = np.roll(psi, -1, (0, 1, 2)) if odd else psi
    b_ = p.reshape(X // 2, 2, Y // 2, 2, Z // 2, 2).transpose(0, 2, 4, 1, 3, 5).reshape(-1, 8) @ (Wm[np.ix_(OPP, OPP)] if odd else Wm).T
    p = b_.reshape(X // 2, Y // 2, Z // 2, 2, 2, 2).transpose(0, 3, 1, 4, 2, 5).reshape(X, Y, Z)
    return np.roll(p, 1, (0, 1, 2)) if odd else p
Ls = 8; Ns_ = Ls ** 3; E = np.eye(Ns_).reshape(Ns_, Ls, Ls, Ls)
Ue3 = np.stack([half(e, We, 0).ravel() for e in E], 1); Uo3 = np.stack([half(e, Wo, 1).ravel() for e in E], 1)
# antiunitary G K with G U^* G^dag = U^dag for both half-ticks: solve g on a spanning tree, then verify every entry
gph = np.full(Ns_, np.nan); gph[0] = 0.0; stack = [0]; nz = [(abs(U) > 1e-12) for U in (Ue3, Uo3)]
while stack:
    x = stack.pop()
    for U, Z in zip((Ue3, Uo3), nz):
        for y in np.where(Z[x])[0]:
            if np.isnan(gph[y]): gph[y] = gph[x] - np.angle(np.conj(U[y, x]) / np.conj(U[x, y])); stack.append(y)
G = np.diag(np.exp(1j * gph)); aerr = max(abs(G @ U.conj() @ G.conj().T - U.conj().T).max() for U in (Ue3, Uo3))
check('THEOREM (3D): a site-diagonal antiunitary G K reverses both half-ticks (all hop holonomies are real, faces -1)',
      not np.isnan(gph).any() and aerr < 1e-12, f'max entry error {aerr:.1e} on the {Ls}^3 torus')
# hence Theta U Theta^-1 = (U_e U_o)^dag: the sea of U_e U_o is G P* G^dag, every principal minor (configuration odds) unchanged
Lb = 16; ks = 2 * np.pi * np.arange(Lb) / Lb; P = np.zeros((Lb, Lb, Lb, 8, 8), complex); nfill = set()
for i, j, k in itertools.product(range(Lb), repeat=3):
    K = np.array([ks[i], ks[j], ks[k]]); Dk = np.exp(1j * (CORN @ K)); w, V = np.linalg.eig((Dk[:, None] * Wo * Dk.conj()[None, :]) @ We)
    sel = -np.angle(w) < 0; nfill.add(int(sel.sum())); Q, _ = np.linalg.qr(V[:, sel]); P[i, j, k] = Q @ Q.conj().T
C0 = np.fft.ifftn(P, axes=(0, 1, 2)); C1 = np.fft.ifftn(np.einsum('ab,ijkbc,dc->ijkad', We, P, We.conj()), axes=(0, 1, 2))
def Cxy(C, x, y):
    nx, cx = np.divmod(x, 2); ny, cy = np.divmod(y, 2); rr = (nx - ny) % Lb
    return C[rr[0], rr[1], rr[2], 4 * cx[0] + 2 * cx[1] + cx[2], 4 * cy[0] + 2 * cy[1] + cy[2]]
md = 0.0
for _ in range(200):
    x0 = rng.integers(0, 2 * Lb, 3); xs3 = [x0, x0 + rng.integers(0, 3, 3), x0 + rng.integers(0, 3, 3), rng.integers(0, 2 * Lb, 3)]
    md = max(md, abs(np.linalg.det(np.array([[Cxy(C0, x, y) for y in xs3] for x in xs3])) - np.linalg.det(np.array([[Cxy(C1, x, y) for y in xs3] for x in xs3]))))
check('3D sea (4 of 8 bands filled at every K): odds identical at both half-ticks, so the 3D vacuum records are frozen too',
      nfill == {4} and np.max(abs(abs(C1) ** 2 - abs(C0) ** 2)) < 1e-12 and md < 1e-12, f'|C|^2 diff {np.max(abs(abs(C1) ** 2 - abs(C0) ** 2)):.1e}, 4x4 minors {md:.1e}')
FA = np.fft.fftn(abs(C0) ** 2, axes=(0, 1, 2)); dg = np.real(np.diagonal(C0[0, 0, 0]))
def var_w(w):
    Fw = np.fft.fftn(w, axes=(0, 1, 2)); return np.sum(w ** 2 * dg) - np.real(np.einsum('ijka,ijkab,ijkb->', Fw.conj(), FA, Fw)) / Lb ** 3, np.sum(w * dg)
nn = np.stack(np.meshgrid(*[np.arange(Lb)] * 3, indexing='ij'), -1); X3 = 2 * nn[:, :, :, None, :] + CORN[None, None, None]
cub = [(l, *var_w(np.all(X3 < l, -1).astype(float))) for l in (4, 6, 8, 10)]
check('equal-time vacuum records in a cube of side l: Var = 0.50 l^2 (area law), not the volume law l^3/4 of independent sites',
      all(abs(v / l ** 2 - 0.5) < 0.01 for l, v, _ in cub), ', '.join(f'l={l}: {v:.2f} vs {l ** 3 / 4:.0f}' for l, v, _ in cub))
dx = (X3 - (Lb - 0.5) + Lb) % (2 * Lb) - Lb; rr3 = np.sqrt((dx ** 2).sum(-1)); cone = []
for Tc in (12, 16, 20, 24):
    w = np.maximum(0, Tc - np.sqrt(3) * rr3); v, m = var_w(w); cone.append((Tc / np.sqrt(3), v, m))
ex3 = np.polyfit(np.log([x[0] for x in cone]), np.log([x[1] for x in cone]), 1)[0]; A3 = cone[-1][1] / cone[-1][0] ** 3
check('past-cone vacuum records (frozen): Var ~ R^3 while the mean ~ R^4, so delta N ~ V^(3/8), not the Poisson V^(1/2)',
      abs(ex3 - 3) < 0.15, f'exponent {ex3:.2f}, Var/R^3 = {A3:.3f}, Fano {cone[0][1] / cone[0][2]:.3f} -> {cone[-1][1] / cone[-1][2]:.3f}')

print('== D. predicted Lambda with the rules\' normalisation (measured: %.3e rho_P)' % rhoL_meas)
# flat LCDM-like background, conformal time in 1/H0; past light-cone 4-volume V(eta) = (4 pi/3) int a^4 (eta - eta')^3 d eta'
la = np.linspace(np.log(1e-12), 0, 20001); aa = np.exp(la); Ha = np.sqrt(Or / aa ** 4 + Om / aa ** 3 + OL + Ok / aa ** 2)
eta = np.concatenate([[0], np.cumsum(np.diff(la) * 0.5 * (1 / (aa * Ha))[1:] + np.diff(la) * 0.5 * (1 / (aa * Ha))[:-1])]) + 1e-12 / Or ** 0.5
tt = np.concatenate([[0], np.cumsum(np.diff(la) * 0.5 * (1 / Ha[1:] + 1 / Ha[:-1]))]) + 0.5e-24 / Or ** 0.5
def Vcone(i):
    e = eta[:i + 1]; return 4 * np.pi / 3 * np.trapezoid(aa[:i + 1] ** 4 * (eta[i] - e) ** 3, e)
VH4 = 1 / H0 ** 4 * c ** 3 / (lP ** 3 * tP)        # Planck 4-volumes per (1/H0)^4 (c = 1)
V0 = Vcone(len(aa) - 1); VP0 = V0 * VH4; t0 = tt[-1] / H0
print(f'   past light-cone 4-volume today {V0:.4f} H0^-4 = {VP0:.2e} Planck; Hubble 4-volume (4pi/3) t0 / H0^3 = {4 * np.pi / 3 * tt[-1]:.3f} H0^-4')
poi = 1 / np.sqrt(KAPPA * VP0)
check('(i) IF records were Poisson (F = 1) at the rule density (one per 729 Planck 4-volumes): rho_L within a factor 10 of measured',
      0.1 < poi / rhoL_meas < 10, f'{poi:.2e} rho_P = {poi / rhoL_meas:.2f} x measured')
Teq = (3 * V0 / np.pi) ** 0.25 / H0; Req = c * Teq / a_site; dN = np.sqrt(A3 * Req ** 3); Nmean = VP0 / KAPPA
fU, fC = 1 / (KAPPA * dN), dN / VP0
check('(ii) the rules\' frozen sea: delta N is 30 orders below Poisson; reading (U) overshoots by ~1e31, reading (C) undershoots by ~1e-31',
      fU / rhoL_meas > 1e25 and fC / rhoL_meas < 1e-25, f'delta N = {dN:.1e} vs sqrt(N) = {np.sqrt(Nmean):.1e}; (U) {fU:.1e}, (C) {fC:.1e} rho_P')
ncm = (410.7 + 336) * 1e6; nb = 0.25 + 0.22                 # photons + relic neutrinos, baryons + electrons, per m^3 today
wcone = 4 * np.pi / 3 * aa ** 4 * (eta[-1] - eta) ** 3
Nrel = np.trapezoid(wcone * (ncm + nb * 1) / aa ** 3 * (c / H0) ** 3, eta) / H0 / (tau / 2)
fM = np.sqrt(Nrel) / VP0
check('(iii) matter-relay normalisation (records = relays x half-ticks): Poisson in N_relay gives rho_L ~ 1e-47 x measured',
      fM / rhoL_meas < 1e-40, f'N_relay = {Nrel:.1e} in the past cone; rho_L = {fM:.1e} rho_P')
print('   (iv) empty vacuum (main has none): zero occupation odds means zero records, so "volume = record count" gives voids no volume')

print('== E. a Sorkin-type Lambda against measured constraints (reading (i), S/V random walk, nested past cones)')
def idx(z): return int(np.argmin(abs(aa - 1 / (1 + z))))
zs = [4e8, 1090, 1.0, 0.75, 0.5, 0.25, 0.0]; ii = [idx(z) for z in zs]; Vs = np.array([Vcone(i) for i in ii])
rc = 3 * Ha[ii] ** 2 * H0 ** 2 / (8 * np.pi * Gn) * c ** 2 / rhoP       # critical density at each epoch / rho_P
sig = 1 / np.sqrt(KAPPA * Vs * VH4) / rc                                  # sd of Omega_L at each epoch
print('   sd of Omega_L(z):', ', '.join(f'z={z:g}: {s_:.2f}' for z, s_ in zip(zs, sig)))
check('rho_L ~ 1/sqrt(V) tracks the critical density: the same O(1) sd of Omega_L at BBN, recombination and today',
      0.2 < sig.min() and sig.max() < 5)
from math import erf, sqrt as msqrt
print('   V(z)/V(0):', ', '.join(f'z={z:g}: {v / Vs[-1]:.2e}' for z, v in zip(zs, Vs)))
Nmc = 200000
def conditional(alpha):
    """condition on today's Omega_L window exactly, then run the Brownian motion S(V) backward (exact bridge to S(0) = 0)."""
    lo, hi = (OL - 0.0146) / (alpha * sig[-1]), (OL + 0.0146) / (alpha * sig[-1])
    p_today = 0.5 * (erf(hi / msqrt(2)) - erf(lo / msqrt(2)))
    u = rng.random(Nmc); X0 = lo + (hi - lo) * u; wt = np.exp(-X0 ** 2 / 2); wt /= wt.sum()
    S = np.zeros((Nmc, len(Vs))); S[:, -1] = X0 * np.sqrt(Vs[-1])
    for k in range(len(Vs) - 2, -1, -1):
        f = Vs[k] / Vs[k + 1]; S[:, k] = f * S[:, k + 1] + np.sqrt(Vs[k] * (1 - f)) * rng.standard_normal(Nmc)
    OmL = alpha * S / np.sqrt(Vs) * sig; rho = OmL * rc; rat = rho[:, 2:6] / rho[:, -1:]; zz = np.array(zs[2:6])
    ok_w = np.all((rat > (1 + zz) ** (3 * (1 - 1.09))) & (rat < (1 + zz) ** (3 * (1 - 0.97))), 1)   # w in [-1.09, -0.97]
    ok_b = abs(OmL[:, 0]) < 0.046         # BBN, radiation era: |rho_L / rho_rad| < 0.046 (Delta N_eff < 0.34)
    ok_r = abs(OmL[:, 1]) < 0.02          # recombination: early dark energy below about 2 percent (approximate bound)
    r5 = rat[:, 2]; weff = -1 + np.log(np.where(r5 > 0, r5, np.nan)) / (3 * np.log(1.5))
    q = np.nanpercentile(weff, [16, 50, 84])
    return p_today, np.sum(wt * ok_w), np.sum(wt * ok_b) * np.sum(wt * ok_r), np.sum(wt * (ok_w & ok_b & ok_r)), q, np.sum(wt * (r5 <= 0))
res = {}
for al in (0.1, 0.3, 1.0, 3.0):
    pt, pw, pbr, pall, q, neg = res[al] = conditional(al)
    print(f'   alpha={al:<3g}: P(today) {pt:.1e}; given today: P(w) {pw:.1e}, P(BBN)P(rec) {pbr:.1e}; joint {pt * pall:.1e}; '
          f'w_eff(z=0.5) {q[1]:+.2f} [{q[0]:+.2f},{q[2]:+.2f}], rho_L(0.5)<=0 {neg:.2f}')
best = max(v[0] * max(v[1], 1e-12) * v[2] for v in res.values())
check('a Sorkin-type Lambda that matches today scatters w by O(1): the measured w = -1.03 +- 0.03 holds in under 5% of such histories',
      all(v[1] < 0.05 for v in res.values()), f'alpha = 1: P(w | today) = {res[1.0][1]:.3f}')
check('together with BBN and recombination, a matching history has probability below 1e-5 at every coefficient tried',
      best < 1e-5, f'alpha = 1: {res[1.0][0] * res[1.0][1] * res[1.0][2]:.1e}; best (factorised) {best:.1e}')
print('supplied: the 1D pair walk and masses, mu and b, the half-filled sea (main has no vacuum), the CL-5 tie-breaks (shown not to matter),')
print('  the unit map a = sqrt(8 pi) l_P, tau = 2a/(sqrt3 c), the volume-count rule itself, the S/V dynamics, LCDM background, bounds used.')
print('elapsed_seconds', round(time.monotonic() - T0, 1))
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
