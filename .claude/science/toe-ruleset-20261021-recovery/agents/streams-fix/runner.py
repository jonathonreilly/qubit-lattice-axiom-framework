#!/usr/bin/env python3
"""Relay streams under CL-5 and a one-clause transport that removes them (supplied models; finite diagnostics;
no physical identification).

Rules compared (all keep the odds exactly and use only nonzero elements of the half-tick U):
  f5     : CL-5 as registered: fewest changed occupations on average, then greatest entropy on that face;
  maxent : greatest entropy over all nonzero elements (no cost stage);
  uni    : least relative entropy to the half-tick's own squared elements |<t|U|s>|^2 (no cost stage);
           equivalently J_ts = a_s |<t|U|s>|^2 b_t with a, b fixed by the odds (a static Schroedinger bridge).
Sections: A plane waves and the cause; B wave packets under f5; C the uni transport on plane waves and packets;
D properties of uni (uniqueness, continuity, separability, support, entangled relays, readers, stationary states).
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 150
AUDIT_INPUT_PATHS = ('docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

import itertools, os, signal, sys, time, warnings
warnings.filterwarnings('ignore')
from math import comb
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import spsolve
from scipy.stats import unitary_group

T0 = time.time(); PASS = FAIL = 0; TOL = 1e-12
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ------------------------------------------------------------------ the tick (own construction, CL-3)
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = 2.0 * CORN - 1


def coherent(j, n):
    th, ph, d = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])


XI = [coherent(1.5, v / np.sqrt(3)) for v in NV]
W0 = np.zeros((8, 8), complex)
for a_, b_ in itertools.product(range(8), repeat=2):
    if abs(CORN[a_] - CORN[b_]).sum() == 1:
        g_ = XI[a_].conj() @ XI[b_]; W0[a_, b_] = -g_ / abs(g_) / np.sqrt(3)
def Wmu(mu, b=0.0, odd=False): a = mu / 2 + (-b if odd else b); return np.cos(a) * W0 + 1j * np.sin(a) * np.eye(8)


def lattice_half(Ls, mu, odd, b=0.0):
    Wm = Wmu(mu, b, odd); Ls = np.array(Ls); X = np.array(list(itertools.product(*[range(l) for l in Ls]))); par = X % 2
    org = ((X - par) if not odd else (X - (1 - par))) % Ls; blk = (org[:, 0] * Ls[1] + org[:, 1]) * Ls[2] + org[:, 2]
    N = X.shape[0]; grp = np.lexsort((np.arange(N), blk)).reshape(-1, 8); pi = (par @ [4, 2, 1])[grp]
    r = np.repeat(grp, 8, 1).ravel(); c = np.tile(grp, (1, 8)).ravel(); v = Wm[np.repeat(pi, 8, 1).ravel(), np.tile(pi, (1, 8)).ravel()]
    k = abs(v) > TOL
    return sp.csr_matrix((v[k], (r[k], c[k])), shape=(N, N)), X


# ------------------------------------------------------------------ transports
def incidence(idx, n, m): return sp.csr_matrix((np.ones(m), (idx, np.arange(m))), shape=(n, m))


def lp(cost, A, b):
    o = dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10)
    r = linprog(cost, A_eq=A, b_eq=b, bounds=(0, None), method='highs', options=o)
    if r.status != 0: r = linprog(cost, A_eq=A, b_eq=b, bounds=(0, None), method='highs', options=dict(o, presolve=False))
    return r


def scale_plan(p, q, fs, ft, lk, n, tol=1e-14):
    """I-projection J_e = exp(lk_e + a_s + b_t) with row sums p, column sums q: Sinkhorn warm start, damped Newton on the dual."""
    lp_, lq_ = np.log(np.where(p > 0, p, 1.0)), np.log(np.where(q > 0, q, 1.0))
    def lse(gr, v):
        mx = np.full(n, -np.inf); np.maximum.at(mx, gr, v); s_ = np.bincount(gr, np.exp(v - mx[gr]), minlength=n)
        return np.where(s_ > 0, mx + np.log(np.where(s_ > 0, s_, 1.0)), -np.inf)
    la = np.zeros(n); lb = np.zeros(n)
    for _ in range(300): la = lp_ - lse(fs, lb[ft] + lk); lb = lq_ - lse(ft, la[fs] + lk)
    S_, T_ = np.unique(fs), np.unique(ft); iS = -np.ones(n, int); iT = -np.ones(n, int); iS[S_] = np.arange(S_.size); iT[T_] = S_.size + np.arange(T_.size)
    x = np.concatenate([la[S_], lb[T_]]); a_, b_ = iS[fs], iT[ft]; tv = np.concatenate([p[S_], q[T_]]); N_ = x.size
    f = lambda x: np.exp(x[a_] + x[b_] + lk).sum() - tv @ x
    for _ in range(80):
        Jf = np.exp(x[a_] + x[b_] + lk); g = np.bincount(a_, Jf, minlength=N_) + np.bincount(b_, Jf, minlength=N_) - tv
        if abs(g).max() < tol: break
        H = sp.csr_matrix((np.concatenate([Jf, Jf]), (np.concatenate([a_, b_]), np.concatenate([b_, a_]))), shape=(N_, N_))
        H = H + sp.diags(np.bincount(a_, Jf, minlength=N_) + np.bincount(b_, Jf, minlength=N_) + 1e-13)
        d = -spsolve(H.tocsc(), g); st = 1.0; f0 = f(x)
        while f(x + st * d) > f0 + 1e-4 * st * (g @ d) and st > 1e-8: st *= 0.5
        x = x + st * d
    Jf = np.exp(x[a_] + x[b_] + lk)
    return Jf, max(abs(np.bincount(fs, Jf, minlength=n) - p).max(), abs(np.bincount(ft, Jf, minlength=n) - q).max())


def transport(p, q, src, tgt, cost=None, rule='f5', w=None):
    keep = (p[src] > 0) & (q[tgt] > 0); n = p.size; src, tgt = src[keep], tgt[keep]; m = src.size
    cost = None if cost is None else cost[keep]; w = None if w is None else w[keep]
    nc, lab = connected_components(sp.csr_matrix((np.ones(m), (src, tgt)), shape=(n, n)), directed=False)
    mass = np.bincount(lab, p, minlength=nc); sc = np.where(mass[lab] > 0, mass[lab], 1.0); p, q = p / sc, q / sc
    p, q = np.where(p > 1e-20, p, 0.0), np.where(q > 1e-20, q, 0.0); keep = (p[src] > 0) & (q[tgt] > 0)
    src, tgt = src[keep], tgt[keep]; m = src.size; cost = None if cost is None else cost[keep]; w = None if w is None else w[keep]
    if rule in ('f5', 'lp'):
        A = sp.vstack([incidence(src, n, m), incidence(tgt, n, m)]).tocsr(); r = lp(cost, A, np.concatenate([p, q]))
        if rule == 'lp': return (src, tgt, r.x * sc[src]), 0.0
        y = r.eqlin.marginals; face = cost - y[src] - y[n + tgt] < 1e-9 * max(1.0, cost.max())
        fs, ft, fx = src[face], tgt[face], r.x[face]; used = fx > 1e-13
        G = sp.csr_matrix((np.ones(fs.size + used.sum()), (np.concatenate([fs, n + ft[used]]), np.concatenate([n + ft, fs[used]]))), shape=(2 * n, 2 * n))
        scc = connected_components(G, directed=True, connection='strong')[1]; kp = used | (scc[fs] == scc[n + ft])
        fs, ft, lk = fs[kp], ft[kp], np.zeros(kp.sum())
    elif rule == 'maxent': fs, ft, lk = src, tgt, np.zeros(m)
    else: fs, ft, lk = src, tgt, np.log(w)
    J, err = scale_plan(p, q, fs, ft, lk, n)
    return (fs, ft, J * sc[fs]), err


def face_support(p, q, src, tgt, cost):
    """exact support of the least-cost face (independent of Sinkhorn): one homogenised LP maximising the used entries."""
    keep = (p[src] > 0) & (q[tgt] > 0); src, tgt, cost = src[keep], tgt[keep], cost[keep]; n, m = p.size, src.size
    As, At = incidence(src, n, m), incidence(tgt, n, m); opt = lp(cost, sp.vstack([As, At]), np.concatenate([p, q])).fun
    Z = sp.csr_matrix((n, m)); Aeq = sp.vstack([sp.hstack([As, Z, -sp.csr_matrix(p[:, None])]), sp.hstack([At, Z, -sp.csr_matrix(q[:, None])]),
                                                 sp.hstack([sp.csr_matrix(cost[None, :]), sp.csr_matrix((1, m)), sp.csr_matrix([[-opt]])])])
    r = linprog(np.concatenate([np.zeros(m), -np.ones(m), [0.0]]), A_ub=sp.hstack([-sp.eye(m), sp.eye(m), sp.csr_matrix((m, 1))]), b_ub=np.zeros(m),
                A_eq=Aeq, b_eq=np.zeros(2 * n + 1), bounds=[(0, None)] * m + [(0, 1)] * m + [(0, 1e7)], method='highs')
    pos = r.x[m:2 * m] > 0.5; return src[pos], tgt[pos], opt


def mat(J, n): M = np.zeros((n, n)); np.add.at(M, (J[1], J[0]), J[2]); return M
def edges(U): t, s = np.nonzero(abs(U) > TOL); return s, t
def rstate(n): v = rng.normal(size=n) + 1j * rng.normal(size=n); return v / np.linalg.norm(v)
def sample(cfg, J, n):
    s, t, w = J; o = np.lexsort((t, s)); s, t, w = s[o], t[o], w[o]; C = np.cumsum(w)
    st, en = np.searchsorted(s, np.arange(n), 'left'), np.searchsorted(s, np.arange(n), 'right')
    base = np.where(st > 0, C[np.maximum(st - 1, 0)], 0.0); u = rng.random(cfg.size) * np.bincount(s, w, minlength=n)[cfg]
    return t[np.clip(np.searchsorted(C, base[cfg] + u, 'right'), st[cfg], en[cfg] - 1)]
def push(rho, J, p): s, t, w = J; return np.bincount(t, w * rho[s] / p[s], minlength=p.size)
def chi2(cfg, P, M):
    f = np.bincount(cfg, minlength=P.size); e = M * P; k = e >= 5; return ((f[k] - e[k]) ** 2 / e[k]).sum() / (k.sum() - 1)
def plan(U, x, rule):
    s, t = edges(U); p, q = abs(x) ** 2, abs(U @ x) ** 2; return transport(p, q, s, t, (s != t) + 0.0, rule, abs(U[t, s]) ** 2)


# ------------------------------------------------------------------ plane waves: the exact per-tick chain on the 8 corner parities
def bloch_pair(K, mu, b=0.0):
    D = np.exp(1j * (CORN @ K)); return Wmu(mu, b, False), D[:, None] * Wmu(mu, b, True) * D.conj()[None, :]
def band(K, mu, b=0.0):
    We, Wo = bloch_pair(K, mu, b); w, V = np.linalg.eig(Wo @ We); ph = -np.angle(w); return V[:, np.isclose(ph, ph.max(), atol=1e-7)]
INC = (CORN[None, :, None] - CORN[None, None, :]) + (CORN[None, :, None] - CORN[:, None, None])   # [c2, c1, c] displacement per tick


def chain(a0, K, mu, b=0.0, rule='f5'):
    We, Wo = bloch_pair(K, mu, b); a1 = We @ a0; ks = []
    for U, x in ((We, a0), (Wo, a1)):
        J, _ = plan(U, x, rule); ks.append(mat(J, 8) / np.where(abs(x) ** 2 > 0, abs(x) ** 2, 1)[None, :])
    Ke, Ko = ks; return Ko @ Ke, np.einsum('ab,bc,abcx->cx', Ko, Ke, INC), Ke, Ko, abs(a0) ** 2


def classes(P, p0):
    live = p0 > 1e-14; lab = connected_components(sp.csr_matrix((P * live[None, :] * live[:, None]) > 1e-12), directed=True, connection='strong')[1]
    return [np.nonzero((lab == k) & live)[0] for k in np.unique(lab[live]) if abs(P[np.ix_(*(2 * [np.nonzero((lab == k) & live)[0]]))].sum(0) - 1).max() < 1e-9]


def streams(P, E1, p0): return [(ix, p0[ix].sum(), p0[ix] @ E1[ix] / p0[ix].sum()) for ix in classes(P, p0)]


def vg_of(K, mu, b, a0):
    def om(Kp):
        We, Wo = bloch_pair(Kp, mu, b); w, V = np.linalg.eig(Wo @ We); return -np.angle(w)[np.argmax(abs(V.conj().T @ a0))]
    return np.array([(om(K + 1e-6 * e) - om(K - 1e-6 * e)) / 2e-6 for e in np.eye(3)]) * 2


def omega(K, mu): return np.arccos(np.clip(np.cos(mu / 2) ** 2 * np.cos(K).sum(-1) / 3 - np.sin(mu / 2) ** 2, -1, 1))
def vg_b0(K, mu): return 2 * np.cos(mu / 2) ** 2 * np.sin(K) / (3 * np.sin(omega(K, mu)))[..., None]


def asym_var(a0, K, mu, rule):
    """exact long-time growth rate of Var(x displacement) per tick for the plane-wave chain (Markov additive process)."""
    P, E1, Ke, Ko, p0 = chain(a0, K, mu, 0, rule); v = p0 @ E1[:, 0]; X = INC[..., 0] - v
    B = np.einsum('ab,bc,abc->ac', Ko, Ke, X); E2 = np.einsum('ab,bc,abc->c', Ko, Ke, X ** 2)
    Z = np.linalg.inv(np.eye(8) - P + np.outer(p0, np.ones(8))); f = E1[:, 0] - v
    return p0 @ E2 + 2 * (f @ Z) @ B @ p0


# ------------------------------------------------------------------ A
def section_A():
    print('A. plane waves (exact per-tick chain on the 8 corner parities) and the cause of the streams')
    E = np.diag((-1.0) ** CORN.sum(1))
    anti = abs(E @ W0 @ E + W0).max(); okc = []; rates = []
    for m in ((1, 0, 0), (1, 1, 0), (2, 1, 0)):
        K = 2 * np.pi * np.array(m) / 4; Vb = band(K, 0.0)
        for _ in range(6):
            a0 = Vb @ rstate(Vb.shape[1]); a0 /= np.linalg.norm(a0); vg = vg_of(K, 0.0, 0.0, a0)
            for r in ('f5', 'maxent', 'uni'):
                st = streams(*[chain(a0, K, 0.0, 0.0, r)[i] for i in (0, 1, 4)])
                okc.append(len(st) == 2 and max(np.linalg.norm(v - vg) for *_, v in st) < 1e-7)
    check('A1 mu = b = 0: (-1)^(x+y+z) anticommutes with W, so every support transport keeps two classes, each at v_g exactly (harmless)',
          anti < 1e-15 and all(okc), f'|eps W eps + W| {anti:.0e}; 2 classes at v_g in {sum(okc)}/{len(okc)} (polarisation x rule)')
    rows = []; ex = None
    for mu, b in ((0.3, 0.0), (1.0, 0.0), (0.3, 0.2), (0.0, 0.15)):
        for m in ((1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0)):
            K = 2 * np.pi * np.array(m) / 4; Vb = band(K, mu, b); ns = 0; dv = 0
            for _ in range(10):
                a0 = Vb @ rstate(Vb.shape[1]); a0 /= np.linalg.norm(a0); vg = vg_of(K, mu, b, a0); P, E1, Ke, Ko, p0 = chain(a0, K, mu, b, 'f5')
                st = streams(P, E1, p0); d = max(np.linalg.norm(v - vg) for *_, v in st); sp_ = len(st) > 1 and d > 0.05; ns += sp_; dv = max(dv, d)
                if sp_ and (ex is None or len(st) > len(ex[0])): ex = (st, vg, a0, K, mu, b)
            rows.append((mu, b, m, ns, dv))
    Kg = np.stack(np.meshgrid(*[np.linspace(-np.pi, np.pi, 41)] * 3, indexing='ij'), -1).reshape(-1, 3); vmax = np.linalg.norm(vg_b0(Kg, 0.3), axis=1).max()
    fast = max(np.linalg.norm(v) for *_, v in ex[0])
    check('A2 FINDING: under CL-5 (f5) many plane waves split into closed streams of different speed; staggered b does not cure it',
          sum(r[3] for r in rows) > 20 and any(r[3] > 0 for r in rows if r[1] > 0),
          'split of 10: ' + ', '.join(f'mu{r[0]} b{r[1]} K~{"".join(map(str, r[2]))}:{r[3]}' for r in rows))
    print(f'      e.g. mu {ex[4]}, K~{np.round(ex[3] * 4 / (2 * np.pi)).astype(int)}: ' + ', '.join(f'{len(ix)} parities w {w:.2f} v_x {v[0]:.3f}' for ix, w, v in ex[0]) + f'; v_g {ex[1][0]:.3f}; '
          f'fastest stream {fast:.3f} > largest group speed {vmax:.3f} site/tick (mu 0.3)')
    # the locker is the least-change face itself
    st, vg, a0, K, mu, b = ex; We, Wo = bloch_pair(K, mu, b); a1 = We @ a0; sup = []; lpv = []; win = []
    for U, x in ((We, a0), (Wo, a1)):
        s, t = edges(U); p, q = abs(x) ** 2, abs(U @ x) ** 2; fs, ft, opt = face_support(p, q, s, t, (s != t) + 0.0)
        S = np.zeros((8, 8)); S[ft, fs] = 1; sup.append(S); J, _ = transport(p, q, s, t, (s != t) + 0.0, 'lp'); lpv.append(mat(J, 8)); win.append(opt)
    nface = len(classes(sup[1] @ sup[0], abs(a0) ** 2)); nlp = len(classes((lpv[1] / np.maximum(abs(a1) ** 2, 1e-300)[None, :]) @ (lpv[0] / (abs(a0) ** 2)[None, :]), abs(a0) ** 2))
    s0, t0 = edges(We); s1, t1 = edges(Wo); paths = [(c, c1, c2) for c, c1 in zip(s0, t0) for c1b, c2 in zip(s1, t1) if c1b == c1]; npth = len(paths); Pth = np.array(paths)
    A = sp.vstack([incidence(Pth[:, i], 8, npth) for i in range(3)]); bb = np.concatenate([abs(a0) ** 2, abs(a1) ** 2, abs(Wo @ a1) ** 2])
    wopt = lp((Pth[:, 0] != Pth[:, 1]) + (Pth[:, 1] != Pth[:, 2]) + 0.0, A, bb).fun
    check('A3 THEOREM + check: the streams are the classes of the least-change face itself, so no tie-break inside it can join them',
          nface == len(st) and nlp >= len(st) and abs(wopt - sum(win)) < 1e-9,
          f'classes: face support {nface}, f5 {len(st)}, LP vertex {nlp}; two-half-tick window optimum {wopt:.6f} = sum of half-tick optima {sum(win):.6f}')
    print('      (window entropy: the window optimum is the sum of the half-tick optima, so every window-optimal path uses each half-tick face;\n'
          '       odds-weighted entropy sum J log(p_s/J) = H(J) - H(p) on fixed marginals: same maximiser; displacement cost: one hop = one bond, = modes/2)')


# ------------------------------------------------------------------ packets
def make_packet(Ls, K0, sig, mu, chi):
    Ls = np.array(Ls); NB = Ls // 2; X = np.array(list(itertools.product(*[range(l) for l in Ls]))); par = X % 2; n = (X - par) // 2
    pidx = par @ [4, 2, 1]; psi = np.zeros(X.shape[0], complex); kx = 2 * np.pi * np.fft.fftfreq(NB[0]); d = (kx - K0[0] + np.pi) % (2 * np.pi) - np.pi
    g = np.exp(-d ** 2 * sig ** 2); ks = []
    for k_, g_ in zip(kx, g):
        if g_ < 1e-8: continue
        K = np.array([k_, 0, 0]); Q, _ = np.linalg.qr(band(K, mu)); ph = Q @ (Q.conj().T @ chi); ph /= np.linalg.norm(ph)
        psi += g_ * np.exp(1j * ((n[:, 0] - NB[0] / 2) * k_)) * ph[pidx]; ks.append((k_, g_))
    return psi / np.linalg.norm(psi), X, np.array(ks)


def run_packet(Ls, mu, psi, X, ticks, M, rule):
    Ls = np.array(Ls); Ue, _ = lattice_half(Ls, mu, False); Uo, _ = lattice_half(Ls, mu, True); N = X.shape[0]
    cfg = rng.choice(N, M, p=abs(psi) ** 2); x = np.zeros(M); xs = [x.copy()]; labs = [X[cfg, 1] % 2 * 2 + X[cfg, 2] % 2]; rho = abs(psi) ** 2; err = 0; jump = 0
    for h in range(2 * ticks):
        U = Uo if h % 2 else Ue; new = U @ psi; p, q = abs(psi) ** 2, abs(new) ** 2; t, s = U.nonzero()
        J, _ = transport(p, q, s, t, (s != t) + 0.0, rule, abs(np.asarray(U[t, s]).ravel()) ** 2)
        rho = push(rho, J, p); err = max(err, abs(rho - q).max()); nc = sample(cfg, J, N); jump += (nc != cfg).mean()
        x = x + ((X[nc, 0] - X[cfg, 0] + Ls[0] // 2) % Ls[0] - Ls[0] // 2); cfg = nc; psi = new
        if h % 2: xs.append(x.copy()); labs.append(X[cfg, 1] % 2 * 2 + X[cfg, 2] % 2)
    lab = np.array(labs); w0 = np.bincount(lab[0], minlength=4) / M; base = (w0 ** 2).sum()
    return dict(x=np.array(xs), lab=lab, pers=((lab == lab[0]).mean(1) - base) / (1 - base), err=err, jump=jump / (2 * ticks))


def half_time(pers):
    k = np.argmax(pers < 0.5); return np.nan if pers[k] >= 0.5 else (k - 1) + (pers[k - 1] - 0.5) / (pers[k - 1] - pers[k])


MU = 0.3; K0 = np.array([np.pi / 2, 0, 0]); CHI = None


def pick_chi():
    global CHI
    Vb = band(K0, MU)
    for _ in range(40):
        c = Vb @ rstate(Vb.shape[1]); c /= np.linalg.norm(c)
        if len(streams(*[chain(c, K0, MU, 0, 'f5')[i] for i in (0, 1, 4)])) == 4: CHI = c; return


def section_B():
    print('B. band-projected wave packets on Lx x 4 x 4 tori (K0 = pi/2 along x, mu = 0.3, polarisation with four f5 streams), f5')
    pick_chi(); st = streams(*[chain(CHI, K0, MU, 0, 'f5')[i] for i in (0, 1, 4)])
    print('      plane-wave streams (y,z parity): ' + ', '.join(f'w {w:.2f} v_x {v[0]:.3f}' for _, w, v in st) + f'; v_g {vg_b0(K0, MU)[0]:.4f}')
    res = {}
    for sig, Lx, T in ((4, 64, 24), (8, 128, 44), (12, 192, 64)):
        psi, X, _ = make_packet((Lx, 4, 4), K0, sig, MU, CHI); o = run_packet((Lx, 4, 4), MU, psi, X, T, 3000, 'f5'); res[sig] = o
    th = {s: half_time(o['pers']) for s, o in res.items()}
    check('B1 FINDING: in packets the f5 streams persist and mix only at the packet edges: label half-life grows with the packet width',
          all(o['err'] < 1e-12 for o in res.values()) and th[12] > th[8] > th[4] > 5,
          'half-life (ticks): ' + ', '.join(f'sigma {s} blocks: {th[s]:.1f} ({th[s] / s:.2f} sigma)' for s in th) + f'; Born max err {max(o["err"] for o in res.values()):.0e}')
    o = res[8]; lab0 = o['lab'][0]
    for T in (5, 20, 44):
        v = o['x'][T] / T; print(f'      sigma 8, T={T}: track v_x mean {v.mean():.3f} std {v.std():.3f}; by stream label ' + ' '.join(f'{v[lab0 == j].mean():.3f}' for j in range(4)))
    return res


# ------------------------------------------------------------------ C
def section_C(resB):
    print('C. the uni transport (closest to the half-tick\'s own squared elements)')
    one = []; dv = 0
    for mu, b in ((0.3, 0.0), (1.0, 0.0), (0.3, 0.2), (0.0, 0.15)):
        for m in ((1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0)):
            K = 2 * np.pi * np.array(m) / 4; Vb = band(K, mu, b)
            for _ in range(5):
                a0 = Vb @ rstate(Vb.shape[1]); a0 /= np.linalg.norm(a0); st = streams(*[chain(a0, K, mu, b, 'uni')[i] for i in (0, 1, 4)])
                one.append(len(st) == 1); dv = max(dv, np.linalg.norm(st[0][2] - vg_of(K, mu, b, a0)))
    check('C1 every tested plane wave with mu or b nonzero gives one class (irreducible per-tick chain) at v_g', all(one) and dv < 1e-7, f'{sum(one)}/{len(one)} single; max |v - v_g| {dv:.0e}')
    s2 = asym_var(CHI, K0, MU, 'uni'); psi, X, ks = make_packet((128, 4, 4), K0, 8, MU, CHI); o = run_packet((128, 4, 4), MU, psi, X, 44, 3000, 'uni')
    th = half_time(o['pers']); vt = {T: o['x'][T] / T for T in (5, 11, 22, 44)}
    vk = vg_b0(np.c_[ks[:, 0], 0 * ks[:, :2]], MU)[:, 0]; wk = ks[:, 1] ** 2 / (ks[:, 1] ** 2).sum(); svg = np.sqrt(wk @ (vk - wk @ vk) ** 2)
    rat = [vt[T].var() * T / s2 for T in vt]
    check('C2 packets: the stream label mixes within about one tick, and the track-velocity variance falls as (exact plane-wave diffusion)/T',
          th < 1.5 and o['err'] < 1e-12 and all(0.75 < r < 1.3 for r in rat),
          f'label half-life {th:.2f} ticks (f5: {half_time(resB[8]["pers"]):.1f}); exact growth {s2:.3f} site^2/tick; var*T/exact at T=5,11,22,44: ' + ' '.join(f'{r:.2f}' for r in rat))
    print(f'      jumps per half-tick: uni {o["jump"]:.3f}, f5 {resB[8]["jump"]:.3f}; packet group-velocity spread {svg:.4f} site/tick; track spread std '
          + ' '.join(f'{vt[T].std():.3f}' for T in vt) + f'; the two are equal at T* = {s2 / svg ** 2:.0f} ticks')
    tP = 5.39e-44
    for lab_, Tm in (('1 ps', 1e-12), ('1 ns', 1e-9)):
        print(f'      if a tick is a Planck time: uni track-speed jitter over {lab_} = {np.sqrt(s2 / (Tm / tP)) / (2 / np.sqrt(3)):.1e} c')


# ------------------------------------------------------------------ D
def section_D():
    print('D. properties of uni')
    U = Wmu(0.3); s, t = edges(U); w = abs(U[t, s]) ** 2; rel = 0; cont = 0
    for _ in range(30):
        a = rstate(8); p, q = abs(a) ** 2, abs(U @ a) ** 2; M = mat(transport(p, q, s, t, None, 'uni', w)[0], 8)
        pi = rng.permutation(8); inv = np.argsort(pi); eo = rng.permutation(s.size)
        Mr = mat(transport(p[inv], q[inv], pi[s][eo], pi[t][eo], None, 'uni', w[eo])[0], 8)[np.ix_(pi, pi)]; rel = max(rel, abs(M - Mr).max())
        a2 = a + 1e-6 * rstate(8); a2 /= np.linalg.norm(a2); cont = max(cont, abs(mat(transport(abs(a2) ** 2, abs(U @ a2) ** 2, s, t, None, 'uni', w)[0], 8) - M).max() / 1e-6)
    a = rstate(8); jr = {}
    for r in ('f5', 'maxent', 'uni'):
        jr[r] = [1 - np.trace(mat(plan(Wmu(mu), a, r)[0], 8)) for mu in (0.0, 1e-4, 1e-2)]
    check('D1 uni is one plan, relabelling-equivariant and continuous, also in the update: its jump rate is continuous at mu -> 0, f5 and maxent jump',
          rel < 1e-12 and cont < 10 and abs(jr['uni'][1] - jr['uni'][0]) < 1e-6 and abs(jr['f5'][1] - jr['f5'][0]) > 0.1 and abs(jr['maxent'][1] - jr['maxent'][0]) > 0.1,
          f'relabel {rel:.0e}; |dJ|/|dpsi| {cont:.2f}; jump rate at mu = 0, 1e-4, 1e-2: ' + '; '.join(f'{r} ' + ' '.join(f'{x:.3f}' for x in v) for r, v in jr.items()))
    se = 0
    for _ in range(8):
        UA, UB = (unitary_group.rvs(4, random_state=int(rng.integers(1 << 30))) for _ in range(2)); a, b = rstate(4), rstate(4)
        s1, t1 = np.repeat(np.arange(4), 4), np.tile(np.arange(4), 4); s2_, t2_ = np.repeat(np.arange(16), 16), np.tile(np.arange(16), 16); UU = np.kron(UA, UB)
        JA = transport(abs(a) ** 2, abs(UA @ a) ** 2, s1, t1, None, 'uni', abs(UA[t1, s1]) ** 2)[0]
        J = transport(abs(np.kron(a, b)) ** 2, abs(UU @ np.kron(a, b)) ** 2, s2_, t2_, None, 'uni', abs(UU[t2_, s2_]) ** 2)[0]
        se = max(se, abs(mat(J, 16).reshape(4, 4, 4, 4).sum((1, 3)) - mat(JA, 4)).max())
    UA = unitary_group.rvs(4, random_state=3); UU = np.kron(UA, np.eye(4)); s2_, t2_ = edges(UU); psi = rstate(16)
    J = transport(abs(psi) ** 2, abs(UU @ psi) ** 2, s2_, t2_, None, 'uni', abs(UU[t2_, s2_]) ** 2)[0]; bmv = J[2][(J[0] % 4) != (J[1] % 4)].sum()
    check('D2 THEOREM + check: product prior and product odds give the product plan (unentangled relays move independently); a step on A alone never moves B',
          se < 1e-10 and bmv == 0, f'A-plan shift by unentangled B {se:.1e}; B mass moved by an A-only step on an entangled state {bmv}')
    L = 4; N = L ** 3; Ue, _ = lattice_half((L, L, L), 0.3, False); Uo, _ = lattice_half((L, L, L), 0.3, True); Ue, Uo = Ue.toarray(), Uo.toarray()
    I, Jx = np.triu_indices(N, 1); NP = I.size; pid = np.zeros((N, N), int); pid[I, Jx] = pid[Jx, I] = np.arange(NP)
    def pedges(U):
        S, T, Wt = [], [], []; nb = [np.nonzero(abs(U[:, x]) > TOL)[0] for x in range(N)]
        for k in range(NP):
            for y1, y2 in itertools.combinations(np.union1d(nb[I[k]], nb[Jx[k]]), 2):
                d = U[y1, I[k]] * U[y2, Jx[k]] - U[y1, Jx[k]] * U[y2, I[k]]
                if abs(d) > TOL: S.append(k); T.append(pid[y1, y2]); Wt.append(abs(d) ** 2)
        return np.array(S), np.array(T), np.array(Wt)
    E = (pedges(Ue), pedges(Uo)); f = [rstate(N) for _ in range(4)]
    Psi = np.outer(f[0], f[1]) - np.outer(f[1], f[0]) + 0.8 * (np.outer(f[2], f[3]) - np.outer(f[3], f[2])); Psi /= np.linalg.norm(Psi)
    odds = lambda P: 2 * abs(P[I, Jx]) ** 2; M = 20000; rho = odds(Psi); cfg = rng.choice(NP, M, p=rho / rho.sum()); err = 0
    for h in range(6):
        U = Uo if h % 2 else Ue; S, T, Wt = E[h % 2]; New = U @ Psi @ U.T; p, q = odds(Psi), odds(New)
        J, _ = transport(p, q, S, T, None, 'uni', Wt); rho = push(rho, J, p); err = max(err, 0.5 * abs(rho - q).sum()); cfg = sample(cfg, J, NP); Psi = New
    ch = chi2(cfg, odds(Psi), M)
    check('D3 two entangled fermion relays on 4^3 (2016 pair configurations, prior |det|^2): joint odds kept, samples match', err < 1e-10 and ch < 1.3, f'max TV {err:.0e}, chi2/dof {ch:.2f}')
    # readers: system qubit x two 3-position pointers; rotation, two controlled shifts, then a system-only rotation
    def Ry(th): return np.array([[np.cos(th / 2), -np.sin(th / 2)], [np.sin(th / 2), np.cos(th / 2)]])
    sh = np.roll(np.eye(3), 1, 0); I3 = np.eye(3); P0, P1 = np.diag([1.0, 0]), np.diag([0, 1.0])
    steps = [np.kron(Ry(2 * np.arcsin(np.sqrt(0.3))), np.eye(9)), np.kron(P0, np.eye(9)) + np.kron(P1, np.kron(sh, I3)), np.kron(P0, np.eye(9)) + np.kron(P1, np.kron(I3, sh)), np.kron(Ry(1.1), np.eye(9))]
    psi = np.zeros(18, complex); psi[0] = 1; cfg = np.zeros(40000, int); moved = 0
    for k, U in enumerate(steps):
        s_, t_ = edges(U); J = transport(abs(psi) ** 2, abs(U @ psi) ** 2, s_, t_, None, 'uni', abs(U[t_, s_]) ** 2)[0]; nc = sample(cfg, J, 18)
        if k == 3: moved = int(((nc % 9) != (cfg % 9)).sum())
        cfg = nc; psi = U @ psi
    p1, p2 = (cfg % 9) // 3, cfg % 3
    check('D4 two readers of one system agree and read Born odds; a later system-only step never moves the pointers',
          (p1 != p2).sum() == 0 and abs((p1 == 1).mean() - 0.3) < 0.01 and moved == 0, f'disagreements {(p1 != p2).sum()}, P(read 1) {(p1 == 1).mean():.4f} vs 0.3, pointer moves {moved}')
    U = Wmu(0.3); w_, V_ = np.linalg.eig(U); e = V_[:, 0] / np.linalg.norm(V_[:, 0]); jf = 1 - np.trace(mat(plan(U, e, 'f5')[0], 8)); ju = 1 - np.trace(mat(plan(U, e, 'uni')[0], 8))
    check('D5 FINDING (knock-on): a stationary state is frozen under f5 but not under uni', jf < 1e-12 and ju > 0.1, f'jump rate on a half-tick eigenstate: f5 {jf:.0e}, uni {ju:.3f}')


if __name__ == '__main__':
    section_A(); print(f'      [{time.time() - T0:.0f} s]')
    rb = section_B(); print(f'      [{time.time() - T0:.0f} s]')
    section_C(rb); print(f'      [{time.time() - T0:.0f} s]')
    section_D(); print(f'      [{time.time() - T0:.0f} s]')
    print('supplied: configuration space; the half-tick as the step; the uni prior |<t|U|s>|^2 (the power 2 is chosen, not forced); states, packets, pointer gates.')
    print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
