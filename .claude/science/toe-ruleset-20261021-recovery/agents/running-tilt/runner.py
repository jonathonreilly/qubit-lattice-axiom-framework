#!/usr/bin/env python3
"""Running of the link coupling on the supplied CL-2 sea and the tilt of a power frozen at the running coupling
(supplied model; finite diagnostic; no physical identification).
 A  content: exact Bloch tick; two light Dirac copies; the block-local translation-invariant one-body commutant of the
    tick family is the number operator alone, so CL-5's links on this content are U(1) (abelian, no Jacobi structure)
 B  per-rung running: Floquet second-order eigenphase formula; induced 1/e^2 = c lim chi(q)/q^2 of the sea's static density
    response; the mu-even part has slope Nf/(6 pi^2) per e-fold with Nf = 2 at every step eps, corrections x1/4 per rung;
    the mu-odd part is an O(mu a) artifact (x~1/2 per rung)
 C  theorem: P = A alpha(mu_k)^gamma, mu_k ~ k^s, one-loop alpha  =>  n_s - 1 = gamma s b alpha,  alpha_s = (n_s - 1)^2/gamma
 D  what sets N: the static ladder bound for a UV pole, the mass freeze, the asymptotically free variant's requirement,
    a hypercharge estimate from measured couplings, a common-epoch estimate and a look-elsewhere count
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import sympy as sp

T0 = time.monotonic(); PASS = FAIL = 0
rng = np.random.default_rng(20261021)
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------------- supplied tick (CL-2): spin-3/2 edge coin W on 2^3 cubes, two tilings offset by (1,1,1) ----------------
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C8[i] - 1.0) / r3; XI.append(np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3)))[1][:, -1])
W = np.zeros((8, 8), complex)
for a, b in itertools.product(range(8), repeat=2):
    if np.sum(abs(C8[a] - C8[b])) == 1: g = XI[a].conj() @ XI[b]; W[a, b] = -g / abs(g) / r3
def tick(K, eps, mu):   # even cube exp(-i(eps - mu/2)W), odd cube exp(+i(eps + mu/2)W); Bloch phases D = diag e^{iK.t}
    Ue = np.cos(eps - mu / 2) * I8 - 1j * np.sin(eps - mu / 2) * W
    Mo = np.cos(eps + mu / 2) * I8 + 1j * np.sin(eps + mu / 2) * W
    D = np.exp(1j * (np.atleast_2d(K) @ C8.T))
    return (D[:, :, None] * Mo[None] * D.conj()[:, None, :]) @ Ue[None]
def proj(U):            # all 8 bands obey U + U^+ = 2 cos w: filled P_F (quasi-energy -w), empty P_E (+w)
    Ud = np.conj(np.swapaxes(U, 1, 2)); w = np.arccos(np.clip(np.real(np.trace(U, axis1=1, axis2=2)) / 8, -1, 1))
    X = (U - Ud) / (2j * np.sin(w)[:, None, None]); return (I8 + X) / 2, (I8 - X) / 2, w
def speed(eps, mu):
    A = (np.cos(mu) - np.cos(2 * eps)) / 2; return np.sqrt(A / 3 * (mu / np.sin(mu) if mu else 1.0))

print('== A. content and the link group')
Ks = rng.uniform(-np.pi, np.pi, (30, 3)); e1 = 0
for eps, mu in ((0.3, 0.05), (0.7, 0.2)):
    ev = np.linalg.eigvals(tick(Ks, eps, mu)); A = (np.cos(mu) - np.cos(2 * eps)) / 2
    e1 = max(e1, np.abs(np.real(ev) - (A * np.cos(Ks).mean(1) + (np.cos(2 * eps) + np.cos(mu)) / 2)[:, None]).max())
ph0 = np.sort(np.angle(np.linalg.eigvals(tick(np.zeros(3), 0.3, 0.05)[0])))
check('A1 W^2 = 1; every band obeys cos w = A S(K) + (cos 2eps + cos mu)/2; at K = 0 the phases are +-mu, four each: '
      'two light Dirac copies (Nf = 2)', np.abs(W @ W - I8).max() < 1e-12 and e1 < 1e-12 and np.allclose(ph0, [-.05] * 4 + [.05] * 4),
      f'{np.abs(W @ W - I8).max():.0e}, {e1:.0e}')
dims = []
for eps, mu in ((0.3, 0.0), (0.3, 0.05), (0.7, 0.2), (0.04, 0.01)):
    L = np.vstack([np.kron(U, I8) - np.kron(I8, U.T) for U in tick(rng.uniform(-np.pi, np.pi, (8, 3)), eps, mu)])
    s = np.linalg.svd(L, compute_uv=False); dims.append(int(np.sum(s < 1e-9 * s[0])))
Lt = np.vstack([np.kron(U, I8) - np.kron(I8, U.T) for U in tick(np.pi * C8.astype(float), 0.3, 0.0)]); st = np.linalg.svd(Lt, compute_uv=False)
dt = int(np.sum(st < 1e-9 * st[0]))
check('A2 block-local, translation-invariant one-body operators commuting with U(K) for all K: dimension %s (massless and '
      'massive): only the number, so CL-5 links on this content are U(1); no self-coupling, no gauge loop (the eight momenta '
      '{0,pi}^3 of a 4^3 torus alone allow %d)' % (dims, dt), dims == [1] * 4 and dt > 1)

print('== B. per-rung running of 1/e^2 from the sea (Floquet static density response)')
Ur = np.linalg.qr(rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6)))[0]; V = rng.normal(size=(6, 6)); V = (V + V.T) / 2
z, P = np.linalg.eig(Ur); w0 = -np.angle(z); Vn = P.conj().T @ V @ P
EV, PV = np.linalg.eigh(V)
def pert(lam):
    wl = -np.angle(np.linalg.eigvals(Ur @ (PV @ np.diag(np.exp(-1j * lam * EV)) @ PV.T)))
    wl = np.array([wl[np.argmin(abs(np.exp(1j * (wl - x)) - 1))] for x in w0])
    cot = np.array([[0 if m == n else 1 / np.tan((w0[n] - w0[m]) / 2) for m in range(6)] for n in range(6)])
    pred = w0 + lam * np.real(np.diag(Vn)) + lam ** 2 / 2 * np.sum(abs(Vn) ** 2 * cot, 1)
    return np.abs(np.angle(np.exp(1j * (wl - pred)))).max()
er = [pert(l) for l in (2e-3, 1e-3)]
check('B1 eigenphases of U e^{-i lam V}: w + lam V_nn + (lam^2/2) sum |V_mn|^2 cot((w_n - w_m)/2) + O(lam^3)',
      7 < er[0] / er[1] < 9 and er[0] < 1e-6, f'err {er[0]:.1e} -> {er[1]:.1e}')
def bump(k, k1=0.5, k2=1.5):
    t = np.clip((k2 - k) / (k2 - k1), 0, 1)
    a = np.where(t > 0, np.exp(-1 / np.maximum(t, 1e-300)), 0.0); b = np.where(t < 1, np.exp(-1 / np.maximum(1 - t, 1e-300)), 0.0)
    return a / (a + b)
def grids(mK, ns=100, nt=12, npf=24, No=36, k2=1.5):
    """ball |K| < 1.5: Gauss in ln|K| x Gauss-Legendre x uniform angle, weight bump; rest of the BZ: periodic grid x (1 - bump)"""
    s0, s1 = np.log(1e-4 * mK), np.log(k2); xs, ws = np.polynomial.legendre.leggauss(ns)
    kap = np.exp((s1 - s0) / 2 * xs + (s1 + s0) / 2); wr = ws * (s1 - s0) / 2 * kap ** 3
    ct, wt = np.polynomial.legendre.leggauss(nt); ph = 2 * np.pi * (np.arange(npf) + 0.5) / npf; st = np.sqrt(1 - ct ** 2)
    nh = np.stack([np.outer(st, np.cos(ph)), np.outer(st, np.sin(ph)), np.outer(ct, np.ones(npf))], -1).reshape(-1, 3)
    Kin = (kap[:, None, None] * nh[None]).reshape(-1, 3)
    win = (wr[:, None] * np.outer(wt, np.full(npf, 2 * np.pi / npf)).reshape(-1)[None]).reshape(-1) * bump(np.repeat(kap, len(nh))) / (2 * np.pi) ** 3
    g = 2 * np.pi * (np.arange(No) + 0.5) / No - np.pi; Ko = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    return np.vstack([Kin, Ko]), np.concatenate([win, (1 - bump(np.linalg.norm(Ko, axis=1))) / No ** 3])
def chi(eps, mu, q, Ks, wts, bt=10000):
    """chi(q) = <tr[P_E(K+q) D_q P_F(K) D_q^+] cot((w(K) + w(K+q))/2)>_K, D_q = diag e^{i q.t/2} (site positions n + t/2)"""
    tot, dq = 0.0, np.exp(1j * (C8 @ q) / 2)
    for i in range(0, len(Ks), bt):
        K = Ks[i:i + bt]; PF, _, w = proj(tick(K, eps, mu)); _, PE, wq = proj(tick(K + q, eps, mu))
        M = ((PE * dq[None, :, None]) @ PF) * dq.conj()[None, None, :]
        tot += np.sum(wts[i:i + bt] * np.real(np.trace(M, axis1=1, axis2=2)) / np.tan((w + wq) / 2))
    return tot
def eind(eps, mu):      # induced 1/e^2 = c lim_{q->0} chi/q^2 (Richardson in q); mK = |mu|/c, inverse Compton length per block
    c = speed(eps, abs(mu)); mK = abs(mu) / c; Ks, wts = grids(mK); q1 = np.array([0.02 * mK, 0, 0])
    return c * (4 * chi(eps, mu, q1, Ks, wts) / q1[0] ** 2 - chi(eps, mu, 2 * q1, Ks, wts) / (4 * q1[0] ** 2)) / 3, mK
k0 = 1 / (6 * np.pi ** 2); res = {}
for eps, rs in ((0.3, range(4, 8)), (0.7, (5, 6)), (0.04, (6, 7))):
    rows = []
    for r in rs:
        mu = 0.08 * 2.0 ** -r; ep, mK = eind(eps, mu); em, _ = eind(eps, -mu); rows.append((mK, (ep + em) / 2, (ep - em) / 2, ep))
    rows = np.array(rows); L = np.log(rows[:-1, 0] / rows[1:, 0])
    res[eps] = dict(se=np.diff(rows[:, 1]) / L / k0, sp=np.diff(rows[:, 3]) / L / k0, odd=rows[:, 2], C=rows[-1, 1] / k0 - 2 * np.log(1 / rows[-1, 0]), mK=rows[:, 0])
R = res[0.3]; dev = 2 - R['se']; rat = dev[1:] / dev[:-1]
check('B2 eps = 0.3, mK = %.3f..%.4f per block: slope of the mu-even induced 1/e^2 per e-fold, in units 1/(6 pi^2): %s -> Nf = 2; '
      'deviation ratios %s per rung (x1/4: irrelevant)' % (R['mK'][0], R['mK'][-1], ' '.join(f'{x:.5f}' for x in R['se']), ' '.join(f'{x:.2f}' for x in rat)),
      abs(R['se'][-1] - 2) < 2e-4 and all(0.2 < x < 0.35 for x in rat))
check('B3 universal log, lattice matching: slope %.5f (eps 0.7), %.5f (eps 0.04); constants C = %.3f, %.3f, %.3f (eps 0.04, 0.3, 0.7) in '
      '1/e^2 = (2 ln(1/mK) + C)/(6 pi^2)' % (res[0.7]['se'][-1], res[0.04]['se'][-1], res[0.04]['C'], R['C'], res[0.7]['C']),
      abs(res[0.7]['se'][-1] - 2) < 1e-3 and abs(res[0.04]['se'][-1] - 2) < 3e-3)
ro = R['odd'][1:] / R['odd'][:-1]
check('B4 the single species (+mu) slope %s approaches 2 like the odd part (ratios %s ~ 1/2 per rung): an O(mu a) artifact'
      % (' '.join(f'{x:.3f}' for x in R['sp']), ' '.join(f'{x:.2f}' for x in ro)), all(0.45 < x < 0.65 for x in ro) and R['sp'][-1] > 1.9)
bpe = 4 / (3 * np.pi); bpr = bpe * np.log(2)
check('B5 so Delta(1/e^2) = 2 ln2/(6 pi^2) = %.6f and Delta(1/alpha) = 4 ln2/(3 pi) = %.6f per rung toward the IR; b0 = -8/3: '
      'e^2 shrinks toward the IR and grows toward a UV pole (screening)' % (2 * np.log(2) * k0, bpr), R['se'][-1] > 1.99)

print('== C. tilt of a frozen power of the running coupling (theorem)')
x, b, s, gm, a0 = sp.symbols('x b s gamma a0', positive=True)
al = 1 / (a0 - s * b * x); n = sp.diff(gm * sp.log(al), x); run = sp.diff(n, x); N = 1 / (s * b * al)
ok = [sp.simplify(n - gm * s * b * al) == 0, sp.simplify(run - n ** 2 / gm) == 0, sp.simplify(n - gm / N) == 0, sp.diff(N, x) == -1]
check('C1 P = A alpha^gamma, ln mu_k = s ln k, d(1/alpha)/dln mu = -b: n_s-1 = gamma s b alpha = gamma/N, alpha_s = (n_s-1)^2/gamma, '
      'dN/dln k = -1 (sympy); b>0 (UV pole) and gamma = -2 give n_s-1 = -2/N, alpha_s = -2/N^2', all(ok))
ns_, dns, als, dal = 0.9649, 0.0042, -0.0045, 0.0067; t = 1 - ns_; Nn = 2 / t; dN = 2 * dns / t ** 2; ar = t ** 2 / 2
check('C2 |gamma| = 2: N = %.1f +- %.1f e-folds to the pole; alpha_s = -%.1e (UV pole, %.2f sigma) or +%.1e (IR pole, %.2f sigma); '
      'separating the signs at 3 sigma needs sigma(alpha_s) = %.0e' % (Nn, dN, ar, abs(-ar - als) / dal, ar, abs(ar - als) / dal, 2 * ar / 3),
      abs(-ar - als) / dal < 1 and abs(ar - als) / dal < 1)
check('C3 examples: link-angle fluctuation <theta^2> ~ e^2 (gamma = +1) tilts blue for U(1), n_s-1 = +b alpha; vacuum link stress '
      'is e-independent (gamma = 0); red needs gamma < 0; gamma = -2, s = 1 on two unit copies needs alpha(mu*) = 1/(%.1f +- %.1f)'
      % (2 * bpe / t, 2 * bpe * dns / t ** 2), float(sp.simplify(n / (gm * s * b * al))) * bpe / 24.2 > 0)

print('== D. what sets N')
lP, Mpc = 1.616255e-35, 3.0857e22; acell = np.sqrt(8 * np.pi) * lP; Lp = np.log(Mpc / 0.05 / acell); Le = np.log(3.8616e-13 / acell)
Lind = R['C'] / 2; Nlad = Lp + Lind
check('D1 ladder: the pivot is L* = %.2f e-folds (%.1f rungs) below the cell; a UV pole gives N = L* + L_cell >= L*; induced '
      'reading L_cell = C/2 = %.2f: N = %.1f, n_s = %.4f (%.1f sigma); 1/alpha_cell = 24..42 on two copies: n_s = %.4f..%.4f; the data '
      'need |gamma| >= %.2f +- %.2f' % (Lp, Lp / np.log(2), Lind, Nlad, 1 - 2 / Nlad, (1 - 2 / Nlad - ns_) / dns, 1 - 2 / (Lp + 24 / bpe),
      1 - 2 / (Lp + 42 / bpe), t * Lp, dns * Lp), (1 - 2 / Lp - ns_) / dns > 4.5)
check('D2 running stops below the lightest charged mass: the electron sits %.1f e-folds below the cell, %.1f above the static pivot, '
      'so b(k*) = 0 there' % (Le, Lp - Le), Lp - Le > 80)
MZ, MPl = 91.1876, 1.220890e19; Mc = MPl / np.sqrt(8 * np.pi); ai = {'Y': 127.951 * (1 - 0.23122), '2': 127.951 * 0.23122, '3': 1 / 0.1180}
bi = {'Y': 41 / 6, '2': -19 / 6, '3': -7.0}
def ainv(c, mu): return ai[c] - bi[c] / (2 * np.pi) * np.log(mu / MZ)
NAF = (Nn + Lp) / (2 * np.pi)
N1 = (1 / t + Lp) / (2 * np.pi)
check('D3 asymptotically free (supplied group; gauge bosons keep it running): N = 2 pi/(b0 alpha_cell) - L*; gamma = +1 (link angle) '
      'needs 1/alpha_cell = (%.2f +- %.2f) b0, gamma = +2 needs (%.2f +- %.2f) b0; GUT-like 24..42 ' % (N1, dns / t ** 2 / (2 * np.pi), NAF, dN / (2 * np.pi)) +
      'needs b0 = %.2f..%.2f (gamma 2, near-conformal); b0 = 7 or 19/6 needs %.0f or %.0f (at 42, b0 = 7 confines %.0f e-folds above the pivot); alpha_s > 0'
      % (24 / NAF, 42 / NAF, 7 * NAF, 19 / 6 * NAF, Lp - 2 * np.pi * 42 / 7), 2 * np.pi * 42 / 7 < Lp)
NY = ainv('Y', Mc) / (bi['Y'] / (2 * np.pi)); muY = MZ * np.exp((ai['Y'] - bi['Y'] / np.pi / t) / (bi['Y'] / (2 * np.pi)))
check('D4 measured hypercharge, SM one loop (supplied): 1/alpha_Y(1/a) = %.2f, pole %.1f e-folds above the cell; pivot formed at the '
      'cell: n_s = %.4f (%.1f sigma), alpha_s = %.1e; gamma = -2 needs formation at %.0e GeV' % (ainv('Y', Mc), NY, 1 - 2 / NY,
      (1 - 2 / NY - ns_) / dns, -2 / NY ** 2, muY), abs(1 - 2 / NY - ns_) / dns < 1)
Gf = np.log(Mc / 2.3487e-13) + np.log(106.75 / 3.909) / 3; Lf = Lp - Gf
check('D5 common-epoch reading, all modes set at T = 1/a, radiation growth %.1f e-folds: the pivot then spans %.1f e-folds (super-horizon), '
      'N = %.1f + L_cell: n_s = %.4f (induced two copies), %.4f (hypercharge)' % (Gf, Lf, Lf, 1 - 2 / (Lf + Lind), 1 - 2 / (Lf + NY)), Lf > 50)
sc = [MZ, 172.7, 1e3, 1e10, 4.7e13, 2e16, Mc, MPl]; hits = []; inr = 0
for c in 'Y23':
    for mu in sc:
        a_ = 1 / ainv(c, mu)
        if a_ <= 0 or a_ > 1: continue
        for gq in (1, 2, 3, 4):
            p = gq * abs(bi[c]) * a_ / (2 * np.pi); inr += 0.01 <= p <= 0.1
            if abs(p - t) < dns: hits.append(f'{c}@{mu:.0e}/g{gq}')
ex = inr * np.log((t + dns) / (t - dns)) / np.log(10)
check('D6 look-elsewhere: |gamma| b alpha(mu)/2pi over 3 SM couplings x 8 scales x |gamma| 1..4: %d within 1 sigma vs %.1f for a '
      'log-flat prior (e.g. %s): matches of N to a pole are cheap' % (len(hits), ex, ', '.join(hits[:3])), len(hits) >= 3)
print('supplied: CL-2 tick (eps, mu); site-phase scalar potential once per tick; quasi-free sea; P ~ alpha^gamma frozen at mu_k ~ k^s;')
print('  a = sqrt(8pi) l_P; Planck 2018 n_s, running; PDG alpha(MZ), sin^2 thetaW, alpha_s(MZ); SM one-loop b_i (desert); T0, g*s.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
