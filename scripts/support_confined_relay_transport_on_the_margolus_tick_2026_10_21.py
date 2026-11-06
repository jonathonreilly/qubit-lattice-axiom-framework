#!/usr/bin/env python3
"""F5 transport on the spin-3/2 Margolus tick (supplied models; finite diagnostic; no physical identification).

F5 as implemented here.  Configurations: sites (one relay), unordered site pairs (two fermion relays), or mode
occupations (relay number free).  Each half-tick U the actual configuration moves by a plan J[t, s] >= 0 with
  (i)   J[t, s] > 0 only if <t|U|s> != 0  (staying s -> s only if <s|U|s> != 0);
  (ii)  row sums |psi_s|^2, column sums |(U psi)_t|^2  (keeps the distribution equal to the odds);
  (iii) least expected cost: c = 1 - [t == s] ('joint identity') or c = number of modes whose occupation
        changes ('modes moved', = 2 x relays moved);
  (iv)  tie-break: maximum entropy on the optimal face (Sinkhorn on the zero-reduced-cost pattern of an optimal
        LP dual, every support component normalised to unit mass).
Sections: A existence and the two earlier rules; B uniqueness and the tie-break; C one relay on the lattice;
D two entangled fermion relays; E relay number free (pair creation); F readers and CHSH.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/SUPPORT_CONFINED_RELAY_TRANSPORT_ON_THE_MARGOLUS_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120


import itertools, os, signal, sys, time, warnings
warnings.filterwarnings('ignore')
from functools import reduce
from math import comb
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog, lsq_linear
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import spsolve
from scipy.stats import unitary_group

T0 = time.time(); PASS = FAIL = 0; TOL = 1e-12
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ------------------------------------------------------------------ the tick (own construction)
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = 2.0 * CORN - 1; OPP = 7 - np.arange(8)


def coherent(j, n):
    th, ph, d = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])


XI = [coherent(1.5, v / np.sqrt(3)) for v in NV]
W0 = np.zeros((8, 8), complex)
for a_, b_ in itertools.product(range(8), repeat=2):
    if abs(CORN[a_] - CORN[b_]).sum() == 1:
        g_ = XI[a_].conj() @ XI[b_]; W0[a_, b_] = -g_ / abs(g_) / np.sqrt(3)
Wmu = lambda mu: np.cos(mu / 2) * W0 + 1j * np.sin(mu / 2) * np.eye(8)


def lattice_half(L, mu, odd):
    """sparse half-tick on L^3 sites: element W[parity(t), parity(s)] for t, s in one even (odd) block."""
    Wm = Wmu(mu); X = np.array(list(itertools.product(range(L), repeat=3))); par = X % 2
    org = ((X - par) if not odd else (X - (1 - par))) % L; blk = (org[:, 0] * L + org[:, 1]) * L + org[:, 2]
    grp = np.lexsort((np.arange(L ** 3), blk)).reshape(-1, 8); pi = (par @ [4, 2, 1])[grp]
    r = np.repeat(grp, 8, 1).ravel(); c = np.tile(grp, (1, 8)).ravel(); v = Wm[np.repeat(pi, 8, 1).ravel(), np.tile(pi, (1, 8)).ravel()]
    k = abs(v) > TOL
    return sp.csr_matrix((v[k], (r[k], c[k])), shape=(L ** 3, L ** 3)), X


# ------------------------------------------------------------------ F5 transport
def incidence(idx, n, m): return sp.csr_matrix((np.ones(m), (idx, np.arange(m))), shape=(n, m))


def lp(cost, A, b):
    o = dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10)
    r = linprog(cost, A_eq=A, b_eq=b, bounds=(0, None), method='highs', options=o)
    if r.status != 0:   # HiGHS presolve can misjudge rows with odds near 1e-16; re-solve without presolve
        r = linprog(cost, A_eq=A, b_eq=b, bounds=(0, None), method='highs', options=dict(o, presolve=False))
    return r


def f5(p, q, src, tgt, cost, tiebreak='entropy', iters=20000, tol=1e-14):
    keep = (p[src] > 0) & (q[tgt] > 0); src, tgt, cost = src[keep], tgt[keep], cost[keep]; n, m = p.size, src.size
    nc, lab = connected_components(sp.csr_matrix((np.ones(m), (src, tgt)), shape=(n, n)), directed=False)
    mass = np.bincount(lab, p, minlength=nc); sc = np.where(mass[lab] > 0, mass[lab], 1.0); p, q = p / sc, q / sc
    # odds below 1e-20 of their component are rounding noise of exact zeros (e.g. band polarisations with nodes): drop
    p, q = np.where(p > 1e-20, p, 0.0), np.where(q > 1e-20, q, 0.0); keep = (p[src] > 0) & (q[tgt] > 0)
    src, tgt, cost = src[keep], tgt[keep], cost[keep]; m = src.size
    A = sp.vstack([incidence(src, n, m), incidence(tgt, n, m)]).tocsr(); b = np.concatenate([p, q])
    if tiebreak == 'lp':
        r = lp(cost, A, b)
        if r.status != 0: return None, None, 1.0
        return (src, tgt, r.x * sc[src]), float((r.x * sc[src] * cost).sum()), 0.0
    r = lp(cost, A, b)
    if r.status != 0: return None, None, 1.0
    fun = float((r.x * sc[src] * cost).sum())
    y = r.eqlin.marginals; face = cost - y[src] - y[n + tgt] < 1e-9 * max(1.0, cost.max())   # every plan on it is optimal
    lp_, lq_ = np.log(np.where(p > 0, p, 1.0)), np.log(np.where(q > 0, q, 1.0))
    def lse(gr, v):
        mx = np.full(n, -np.inf); np.maximum.at(mx, gr, v); s_ = np.bincount(gr, np.exp(v - mx[gr]), minlength=n)
        return np.where(s_ > 0, mx + np.log(np.where(s_ > 0, s_, 1.0)), -np.inf)
    def sinkhorn(fs, ft, its):
        """max-entropy plan on pattern (fs, ft): Sinkhorn warm start, then damped Newton on the convex dual
        f(a, b) = sum_e exp(a_s + b_t) - p.a - q.b (thin faces make plain Sinkhorn crawl)."""
        la = np.zeros(n); lb = np.zeros(n)
        for it in range(min(its, 300)):
            la = lp_ - lse(fs, lb[ft]); lb = lq_ - lse(ft, la[fs])
        S_, T_ = np.unique(fs), np.unique(ft); iS = -np.ones(n, int); iT = -np.ones(n, int); iS[S_] = np.arange(S_.size); iT[T_] = S_.size + np.arange(T_.size)
        x = np.concatenate([la[S_], lb[T_]]); a_, b_ = iS[fs], iT[ft]; tgtv = np.concatenate([p[S_], q[T_]]); N_ = x.size
        f = lambda x: np.exp(x[a_] + x[b_]).sum() - tgtv @ x
        for k in range(60):
            Jf = np.exp(x[a_] + x[b_]); g = np.bincount(a_, Jf, minlength=N_) + np.bincount(b_, Jf, minlength=N_) - tgtv
            err = abs(g).max()
            if err < tol: break
            H = sp.csr_matrix((np.concatenate([Jf, Jf]), (np.concatenate([a_, b_]), np.concatenate([b_, a_]))), shape=(N_, N_))
            H = H + sp.diags(np.bincount(a_, Jf, minlength=N_) + np.bincount(b_, Jf, minlength=N_) + 1e-13)
            d = -spsolve(H.tocsc(), g); st = 1.0; f0 = f(x)
            while f(x + st * d) > f0 + 1e-4 * st * (g @ d) and st > 1e-8: st *= 0.5
            x = x + st * d
        Jf = np.exp(x[a_] + x[b_])
        err = max(abs(np.bincount(fs, Jf, minlength=n) - p).max(), abs(np.bincount(ft, Jf, minlength=n) - q).max())
        return Jf, err
    # a vertex dual can leave entries in the pattern that are zero on the whole face (no strict complementarity);
    # remove them exactly: an unused entry (s, t) can become positive iff an alternating cycle exists, i.e. iff t
    # reaches s in the digraph with arcs s -> t for pattern entries and t -> s for entries the optimal plan uses.
    fs, ft, fx = src[face], tgt[face], r.x[face]; used = fx > 1e-13
    G = sp.csr_matrix((np.ones(fs.size + used.sum()), (np.concatenate([fs, n + ft[used]]), np.concatenate([n + ft, fs[used]]))), shape=(2 * n, 2 * n))
    scc = connected_components(G, directed=True, connection='strong')[1]
    kp = used | (scc[fs] == scc[n + ft]); fs, ft = fs[kp], ft[kp]
    Jf, err = sinkhorn(fs, ft, iters)
    return (fs, ft, Jf * sc[fs]), fun, err


def face_dim(p, q, src, tgt, cost):
    """optimal-face dimension: one homogenised LP finds every entry positive somewhere on the face (E+);
    dim = |E+| - (#nodes - #components) of the bipartite graph on E+."""
    keep = (p[src] > 0) & (q[tgt] > 0); src, tgt, cost = src[keep], tgt[keep], cost[keep]; n, m = p.size, src.size
    As, At = incidence(src, n, m), incidence(tgt, n, m); opt = lp(cost, sp.vstack([As, At]), np.concatenate([p, q])).fun
    Z = sp.csr_matrix((n, m)); Aeq = sp.vstack([sp.hstack([As, Z, -sp.csr_matrix(p[:, None])]), sp.hstack([At, Z, -sp.csr_matrix(q[:, None])]),
                                                 sp.hstack([sp.csr_matrix(cost[None, :]), sp.csr_matrix((1, m)), sp.csr_matrix([[-opt]])])])
    r = linprog(np.concatenate([np.zeros(m), -np.ones(m), [0.0]]), A_ub=sp.hstack([-sp.eye(m), sp.eye(m), sp.csr_matrix((m, 1))]), b_ub=np.zeros(m),
                A_eq=Aeq, b_eq=np.zeros(2 * n + 1), bounds=[(0, None)] * m + [(0, 1)] * m + [(0, 1e7)], method='highs')
    pos = r.x[m:2 * m] > 0.5; es, et = src[pos], n + tgt[pos]; nodes = np.unique(np.concatenate([es, et]))
    ncp = connected_components(sp.csr_matrix((np.ones(es.size), (es, et)), shape=(2 * n, 2 * n)), directed=False)[1]
    return int(pos.sum()) - (nodes.size - np.unique(ncp[nodes]).size), opt


def sample(cfg, J, n):
    s, t, w = J; o = np.lexsort((t, s)); s, t, w = s[o], t[o], w[o]; C = np.cumsum(w)
    st, en = np.searchsorted(s, np.arange(n), 'left'), np.searchsorted(s, np.arange(n), 'right')
    base = np.where(st > 0, C[np.maximum(st - 1, 0)], 0.0); u = rng.random(cfg.size) * np.bincount(s, w, minlength=n)[cfg]
    return t[np.clip(np.searchsorted(C, base[cfg] + u, 'right'), st[cfg], en[cfg] - 1)]


def push(rho, J, p): s, t, w = J; return np.bincount(t, w * rho[s] / p[s], minlength=p.size)
def mat(J, n): M = np.zeros((n, n)); np.add.at(M, (J[1], J[0]), J[2]); return M
def edges(U): t, s = np.nonzero(abs(U) > TOL); return s, t
def rstate(n): v = rng.normal(size=n) + 1j * rng.normal(size=n); return v / np.linalg.norm(v)
def chi2(cfg, P, M):
    f = np.bincount(cfg, minlength=P.size); e = M * P; k = e >= 5; return ((f[k] - e[k]) ** 2 / e[k]).sum() / (k.sum() - 1)


# ------------------------------------------------------------------ A
def section_A():
    print('A. one Margolus block (8 sites): existence, and the two earlier rules')
    cyc = [0, 1, 3, 2]; hol = np.prod([XI[cyc[(i + 1) % 4]].conj() @ XI[cyc[i]] for i in range(4)])
    check('A1 W is Hermitian with W^2 = 1, face holonomy -1', abs(W0 - W0.conj().T).max() < 1e-14 and abs(W0 @ W0 - np.eye(8)).max() < 1e-12 and abs(hol / abs(hol) + 1) < 1e-12)
    subsets = [list(s) for r in range(1, 8) for s in itertools.combinations(range(8), r)]
    hall = 0; perr = 0; zfrac = []
    for mu in (0.0, 0.3):
        U = Wmu(mu); conn = abs(U) > TOL
        for _ in range(150):
            psi = rstate(8); p, q = abs(psi) ** 2, abs(U @ psi) ** 2
            hall = max(hall, max(q[S].sum() - p[conn[S, :].any(0)].sum() for S in subsets))
            fall, rise = np.clip(p - q, 0, None), np.clip(q - p, 0, None); inflow = np.zeros(8)
            for s in range(8):
                tg = [t for t in range(8) if rise[t] > 0 and conn[t, s] and t != s]; tot = rise[tg].sum()
                if fall[s] > 0 and tot == 0: perr = max(perr, fall[s])
                for t in tg: inflow[t] += fall[s] * rise[t] / tot
            perr = max(perr, abs(inflow - rise).max())
            # margolus-relays 'straight pairing' minimal switching: in-site j -> out-site OPP[k]
            po = q[OPP]; keepm = np.minimum(p, po); ex, sh = p - keepm, po - keepm
            F = np.diag(keepm) + (np.outer(ex, sh / sh.sum()) if sh.sum() > 1e-300 else 0)
            zfrac.append((F * (~conn[OPP][:, :].T)).sum())   # F[j, k] uses element <OPP k|U|j>
    check('A2 Hall condition q(S) <= p(N^-1 S) for all 254 target sets (P_S U = P_S U P_N^-1(S), U unitary): a support transport exists',
          hall < 1e-14, f'max excess {hall:.1e} (mu = 0, 0.3; 300 states)')
    check('A3 earlier rule 1 (proportional shortfall switching restricted to connected targets) does not keep Born', perr > 0.1, f'max inflow error {perr:.3f}')
    check('A4 earlier rule 2 (margolus-relays straight-pairing minimal switching) keeps Born only by using transitions along ZERO elements of W',
          min(zfrac) > 0.3, f'mass on zero elements per half-tick: min {min(zfrac):.3f}, mean {np.mean(zfrac):.3f}')
    bad = {}
    for a in (0.5, 2.0):
        for mu in (0.0, 0.3):
            U = Wmu(mu); s, t = edges(U); n_ = 0
            for _ in range(150):
                psi = rstate(8); p = abs(psi) ** (2 * a); q = abs(U @ psi) ** (2 * a)
                n_ += f5(p / p.sum(), q / q.sum(), s, t, (s != t).astype(float), 'lp')[0] is None
            bad[(a, mu)] = n_
    check('A5 a distribution |psi|^(2a), a != 1, has no support transport at mu = 0 for any tested state (W maps even sites onto odd sites)',
          bad[(0.5, 0.0)] == 150 and bad[(2.0, 0.0)] == 150, 'infeasible of 150: ' + ', '.join(f'a={a} mu={m}: {v}' for (a, m), v in bad.items()))


# ------------------------------------------------------------------ B
def section_B():
    print('B. does "leaves the most in place" give one answer?')
    res = {}
    for mu in (0.0, 0.3):
        U = Wmu(mu); s, t = edges(U); c = (s != t).astype(float); dims = []; dlp = []; dme = []; cont = []; dl2 = []
        for k in range(60):
            psi = rstate(8); p, q = abs(psi) ** 2, abs(U @ psi) ** 2; dims.append(face_dim(p, q, s, t, c)[0])
            pi = rng.permutation(8); inv = np.argsort(pi); eo = rng.permutation(s.size)
            for tb, store in (('lp', dlp), ('entropy', dme)):
                M = mat(f5(p, q, s, t, c, tb)[0], 8); Mr = mat(f5(p[inv], q[inv], pi[s][eo], pi[t][eo], c[eo], tb)[0], 8)[np.ix_(pi, pi)]
                store.append(abs(M - Mr).max())
            J, opt, _ = f5(p, q, s, t, c); ps2 = psi + 1e-6 * rstate(8); ps2 /= np.linalg.norm(ps2)
            cont.append(abs(mat(f5(abs(ps2) ** 2, abs(U @ ps2) ** 2, s, t, c)[0], 8) - mat(J, 8)).max() / 1e-6)
            if k < 20:
                A = np.vstack([np.eye(8)[s].T, np.eye(8)[t].T, c[None, :]]); b = np.concatenate([p, q, [opt]])
                x = lsq_linear(np.vstack([np.eye(s.size), 1e5 * A]), np.concatenate([np.zeros(s.size), 1e5 * b]), bounds=(0, np.inf), method='bvls', tol=1e-14).x
                M2 = np.zeros((8, 8)); M2[t, s] = x; dl2.append(abs(M2 - mat(J, 8)).max())
        res[mu] = (dims, dlp, dme, cont, dl2)
    d0, d3 = res[0.0][0], res[0.3][0]
    check('B1 the max-stay plan is never unique: optimal-face dimension 10 at mu = 0 (no stays allowed), >= 1 at mu = 0.3',
          min(d0) == 10 and max(d0) == 10 and min(d3) >= 1, f'mu=0: {min(d0)}..{max(d0)}; mu=0.3: {min(d3)}..{max(d3)} (60 states each)')
    lpd = res[0.0][1] + res[0.3][1]
    check('B2 an LP vertex privileges labels: relabelling the configurations changes the plan', np.mean(np.array(lpd) > 1e-6) > 0.5,
          f'changed in {np.mean(np.array(lpd) > 1e-6):.2f} of cases, max {max(lpd):.3f}')
    check('B3 max-entropy tie-break: one plan (strictly concave), relabelling-equivariant, continuous',
          max(res[0.0][2] + res[0.3][2]) < 1e-12 and max(res[0.0][3] + res[0.3][3]) < 10,
          f'relabel error {max(res[0.0][2] + res[0.3][2]):.1e}; max |dJ|/|dpsi| {max(res[0.0][3] + res[0.3][3]):.2f}')
    l2 = res[0.0][4] + res[0.3][4]
    check('B4 the least-squares tie-break is also unique and equivariant but gives a different plan', np.median(l2) > 1e-3, f'median |J_L2 - J_maxent| {np.median(l2):.3f}')
    # separability: two independent relays (product state, product half-tick)
    U = Wmu(0.3); s1, t1 = edges(U); UU = np.kron(U, U); s2, t2 = edges(UU); sep = {'identity': 0, 'modes': 0}; xs = 0
    for _ in range(20):
        a, b = rstate(8), rstate(8); p, q = abs(np.kron(a, b)) ** 2, abs(UU @ np.kron(a, b)) ** 2
        MA = mat(f5(abs(a) ** 2, abs(U @ a) ** 2, s1, t1, (s1 != t1).astype(float))[0], 8)
        for nm, c in (('identity', (s2 != t2).astype(float)), ('modes', (s2 // 8 != t2 // 8).astype(float) + (s2 % 8 != t2 % 8))):
            M = mat(f5(p, q, s2, t2, c)[0], 64); sep[nm] = max(sep[nm], abs(M.reshape(8, 8, 8, 8).sum((1, 3)) - MA).max())
            if nm == 'identity': xs = max(xs, M.diagonal().sum() - (1 - f5(abs(a) ** 2, abs(U @ a) ** 2, s1, t1, (s1 != t1).astype(float))[1]) * (1 - f5(abs(b) ** 2, abs(U @ b) ** 2, s1, t1, (s1 != t1).astype(float))[1]))
    check('B5 counting the configuration as one thing correlates independent relays; counting relays (modes) left in place does not',
          sep['identity'] > 1e-2 and sep['modes'] < 1e-10, f"A's plan shift by unentangled B: identity cost {sep['identity']:.3f} (joint stay exceeds product by up to {xs:.3f}), modes cost {sep['modes']:.1e}")
    se = 0; sl = 0
    for _ in range(8):
        UA, UB = (unitary_group.rvs(4, random_state=int(rng.integers(1 << 30))) for _ in range(2)); a, b = rstate(4), rstate(4)
        s1, t1 = np.repeat(np.arange(4), 4), np.tile(np.arange(4), 4); c1 = (s1 != t1) + 0.0
        s2, t2 = np.repeat(np.arange(16), 16), np.tile(np.arange(16), 16); c2 = (s2 // 4 != t2 // 4).astype(float) + (s2 % 4 != t2 % 4)
        pa, qa = abs(a) ** 2, abs(UA @ a) ** 2; p, q = np.kron(pa, abs(b) ** 2), np.kron(qa, abs(UB @ b) ** 2)
        JA, oA, _ = f5(pa, qa, s1, t1, c1); J, o, _ = f5(p, q, s2, t2, c2)
        se = max(se, abs(mat(J, 16).reshape(4, 4, 4, 4).sum((1, 3)) - mat(JA, 4)).max())
        def l2(p_, q_, s_, t_, c_, o_, n_):
            A = np.vstack([np.eye(n_)[s_].T, np.eye(n_)[t_].T, c_[None, :]]); b_ = np.concatenate([p_, q_, [o_]])
            x = lsq_linear(np.vstack([np.eye(s_.size), 1e5 * A]), np.concatenate([np.zeros(s_.size), 1e5 * b_]), bounds=(0, np.inf), method='bvls', tol=1e-14).x
            M = np.zeros((n_, n_)); M[t_, s_] = x; return M
        sl = max(sl, abs(l2(p, q, s2, t2, c2, o, 16).reshape(4, 4, 4, 4).sum((1, 3)) - l2(pa, qa, s1, t1, c1, oA, 4)).max())
    check('B6 with the modes cost, max entropy moves independent relays independently; least squares does not', se < 1e-10 and sl > 1e-3,
          f'A-plan shift by unentangled B: max-entropy {se:.1e}, least-squares {sl:.1e} (dense 4-config half-ticks)')

    U = Wmu(0.3); I8 = np.eye(8); lab = np.array(list(itertools.product(range(8), range(8)))); dm = []; dmv = []
    cost64 = (lab[:, None, :] != lab[None, :, :]).sum(2)
    def plan(V, ps):
        s, t = edges(V); return mat(f5(abs(ps) ** 2, abs(V @ ps) ** 2, s, t, (lab[s] != lab[t]).sum(1) + 0.0)[0], 64), V @ ps
    for _ in range(15):
        psi = rstate(64); Mj, _ = plan(np.kron(U, U), psi); M1, mid = plan(np.kron(U, I8), psi); M2, _ = plan(np.kron(I8, U), mid)
        Ms = (M2 / np.maximum(abs(mid) ** 2, 1e-300)[None, :]) @ M1; dm.append(abs(Mj - Ms).max()); dmv.append(((Ms - Mj) * cost64).sum())
    check('B7 the step is load-bearing: one transport per half-tick differs from two block-by-block transports of the same unitary',
          min(dmv) > 0.05, f'max plan difference {max(dm):.3f}; slicing moves {min(dmv):.2f}..{max(dmv):.2f} more modes (2 entangled relays)')


# ------------------------------------------------------------------ C
def omega(K, mu): return np.arccos(np.clip(np.cos(mu / 2) ** 2 * np.cos(K).sum(-1) / 3 - np.sin(mu / 2) ** 2, -1, 1))
def bloch_U(K, Wm): D = np.exp(1j * (CORN @ K)); return (D[:, None] * Wm * D.conj()[None, :]) @ Wm


def run_lattice(L, mu, psi, H, M=20000, also_lp=False):
    Ue, X = lattice_half(L, mu, False); Uo, _ = lattice_half(L, mu, True); N = L ** 3
    cfg = rng.choice(N, M, p=abs(psi) ** 2); rho = abs(psi) ** 2; disp = np.zeros((M, 3)); plen = np.zeros(M)
    out = dict(err=0, jump=[], ed=np.zeros(3), edlp=np.zeros(3), var=[], serr=0); hist = [cfg[:2000].copy()]
    for h in range(H):
        U = Uo if h % 2 else Ue; new = U @ psi; p, q = abs(psi) ** 2, abs(new) ** 2; t, s = U.nonzero(); c = (s != t) + 0.0
        J, opt, se = f5(p, q, s, t, c); out['serr'] = max(out['serr'], se)
        dv = lambda JJ: (((X[JJ[1]] - X[JJ[0]] + L // 2) % L - L // 2) * JJ[2][:, None]).sum(0)
        out['ed'] += dv(J)
        if also_lp: out['edlp'] += dv(f5(p, q, s, t, c, 'lp')[0])
        rho = push(rho, J, p); out['err'] = max(out['err'], abs(rho - q).max()); out['jump'].append(opt)
        nc = sample(cfg, J, N); dd = (X[nc] - X[cfg] + L // 2) % L - L // 2; disp += dd; plen += np.linalg.norm(dd, axis=1); cfg = nc; psi = new; hist.append(cfg[:2000].copy())
        if h % 2: out['var'].append(disp.var(0).sum())
    hs = np.array(hist); rev = np.mean([np.any(hs[:k] == hs[k], 0).mean() for k in range(1, len(hs))])
    out.update(cfg=cfg, psi=psi, disp=disp, plen=plen, chi=chi2(cfg, abs(psi) ** 2, M), rev=rev); return out


def section_C():
    print('C. one relay on the lattice')
    L = 12; NB = L // 2; X = np.array(list(itertools.product(range(L), repeat=3))); par = X % 2; n = (X - par) // 2; revs = []
    for mu in (0.3, 0.0):
        K0 = np.array([0.6, 0.0, 0.0]); w, V = np.linalg.eig(bloch_U(K0, Wmu(mu))); phi = V[:, np.argmax(-np.angle(w))]
        dn = (n - NB / 2 + NB / 2) % NB - NB / 2; psi = np.exp(-(dn ** 2).sum(1) / 4.5) * np.exp(1j * (n @ K0)) * phi[par @ [4, 2, 1]]
        o = run_lattice(L, mu, psi / np.linalg.norm(psi), 16, also_lp=True)
        check(f'C1 mu={mu}: packet on 12^3, 16 half-ticks: distribution stays the odds; 20000 samples match',
              o['err'] < 1e-12 and o['chi'] < 1.3, f"max |rho - |psi|^2| {o['err']:.1e}, chi2/dof {o['chi']:.2f}, "
              f"jump/half-tick {np.mean(o['jump']):.3f}; revisit {o['rev']:.3f}; drift max-entropy {o['ed'][0] / 8:.4f} = LP vertex {o['edlp'][0] / 8:.4f} site/tick")
        revs.append(o['rev'])
    check('C6 FINDING: F5 relays return to sites they already burnt (stays, zigzags); one record per site forbids it',
          min(revs) > 0.01, f'half-ticks landing on an own burnt site: mu=0.3 {revs[0]:.3f}, mu=0 {revs[1]:.3f}')
    L = 8; NB = 4; X = np.array(list(itertools.product(range(L), repeat=3))); par = X % 2; n = (X - par) // 2; rows = []
    for mu, m in ((0.3, (1, 0, 0)), (0.3, (1, 1, 0)), (0.0, (1, 0, 0)), (0.6, (1, 1, 1))):
        K = 2 * np.pi * np.array(m) / NB; w, V = np.linalg.eig(bloch_U(K, Wmu(mu))); sel = np.where(-np.angle(w) > 1e-9)[0]
        phi = V[:, sel] @ rstate(sel.size); vg = np.array([(omega(K + 1e-6 * e, mu) - omega(K - 1e-6 * e, mu)) / 2e-6 for e in np.eye(3)])
        psi = np.exp(1j * (n @ K)) * phi[par @ [4, 2, 1]]; o = run_lattice(L, mu, psi / np.linalg.norm(psi), 32)
        rows.append((mu, m, abs(o['ed'] / 16 - 2 * vg).max(), np.linalg.norm(o['disp'].mean(0) / 16 - 2 * vg), np.mean(o['jump']), o['var'], o['plen'].mean() / 16,
                     np.mean(np.linalg.norm(o['disp'], axis=1) / np.maximum(o['plen'], 1e-9)), 2 * vg))
    check('C2 plane waves: exact mean drift = group velocity 2 grad w site/tick (any block-confined transport)',
          max(r[2] for r in rows) < 1e-9 and max(r[3] for r in rows) < 0.03, ', '.join(f'mu {r[0]} K~{r[1]}: |v|={np.linalg.norm(r[8]):.3f} err {r[2]:.0e}' for r in rows))
    check('C3 relays jump at most half-ticks (all at mu = 0: <s|W|s> = 0); paths zigzag',
          all(r[4] > 0.5 for r in rows) and all(r[7] < 0.9 for r in rows),
          '; '.join(f'mu {r[0]}: jump {r[4]:.2f}, path {r[6]:.2f}/tick, net/path {r[7]:.2f}' for r in rows))
    # exact per-relay long-run motion for plane waves: the per-tick chain on the 8 site parities and its closed classes
    def streams(mu, m, NB=4):
        K = 2 * np.pi * np.array(m) / NB; Wm = Wmu(mu); w, V = np.linalg.eig(bloch_U(K, Wm)); sel = np.where(-np.angle(w) > 1e-9)[0]
        a0 = V[:, sel] @ rstate(sel.size); a0 /= np.linalg.norm(a0); D = np.exp(1j * (CORN @ K)); a1 = Wm @ a0; a2 = (D[:, None] * Wm * D.conj()[None, :]) @ a1
        s, t = edges(Wm); Ke = mat(f5(abs(a0) ** 2, abs(a1) ** 2, s, t, (s != t) + 0.0)[0], 8) / (abs(a0) ** 2)[None, :]
        Ko = mat(f5(abs(a1) ** 2, abs(a2) ** 2, s, t, (s != t) + 0.0)[0], 8) / (abs(a1) ** 2)[None, :]
        P = Ko @ Ke; inc = (CORN[None, :, None] - CORN[None, None, :]) + (CORN[None, :, None] - CORN[:, None, None])   # [c2, c1, c]
        E1 = np.einsum('ab,bc,abcx->cx', Ko, Ke, inc); ncl, lab = connected_components(sp.csr_matrix(P > 1e-12), directed=True, connection='strong')
        vg = np.array([(omega(K + 1e-6 * e, mu) - omega(K - 1e-6 * e, mu)) / 2e-6 for e in np.eye(3)]) * 2; out = []
        for k in range(ncl):
            idx = np.nonzero(lab == k)[0]; Pk = P[np.ix_(idx, idx)]
            if abs(Pk.sum(0) - 1).max() > 1e-9: continue
            ww, VV = np.linalg.eig(Pk); pi_ = np.real(VV[:, np.argmin(abs(ww - 1))]); pi_ /= pi_.sum(); out.append((pi_ @ E1[idx], (abs(a0[idx]) ** 2).sum()))
        return out, vg
    st = {}
    for mu, m in ((0.3, (1, 0, 0)), (0.3, (1, 1, 0)), (0.0, (1, 0, 0)), (0.6, (1, 1, 1))):
        res = [streams(mu, m) for _ in range(8)]; split = [r for r in res if len(r[0]) > 1 and max(np.linalg.norm(v - r[1]) for v, _ in r[0]) > 0.05]
        st[(mu, m)] = (len(split), max(split, key=lambda r: max(np.linalg.norm(v - r[1]) for v, _ in r[0])) if split else None, max(np.linalg.norm(sum(wt * v for v, wt in r[0]) - r[1]) for r in res))
    ex = st[(0.3, (1, 0, 0))][1] or st[(0.3, (1, 1, 0))][1]
    check('C5 FINDING: for some plane waves the relays split into two sublattice streams that never mix, moving at different velocities (Born mean = v_g)',
          ex is not None and max(v[2] for v in st.values()) < 1e-6 and st[(0.0, (1, 0, 0))][0] == 0,
          'split polarisations of 8: ' + ', '.join(f'mu {k[0]} K~{k[1]}: {v[0]}' for k, v in st.items()) +
          (f'; e.g. streams {np.round(ex[0][0][0], 3)} (weight {ex[0][0][1]:.2f}) and {np.round(ex[0][1][0], 3)} vs v_g {np.round(ex[1], 3)}' if ex else ''))
    Ue, _ = lattice_half(L, 0.3, False); psi = rstate(L ** 3); p, q = abs(psi) ** 2, abs(Ue @ psi) ** 2; t, s = Ue.nonzero(); c = (s != t) + 0.0
    sh = np.array([((x + 2) % L) * L * L + y * L + z for x, y, z in X]); inv = np.argsort(sh)
    J = mat(f5(p, q, s, t, c)[0], L ** 3); Js = mat(f5(p[inv], q[inv], s, t, c)[0], L ** 3)   # state translated by one block
    check('C4 no block privileged: translating the state by one block translates the plan', abs(Js[np.ix_(sh, sh)] - J).max() < 1e-12, f'{abs(Js[np.ix_(sh, sh)] - J).max():.1e}')


# ------------------------------------------------------------------ D
def section_D():
    print('D. two entangled fermion relays on 4^3 (2016 pair configurations, cost = relays moved)')
    L = 4; N = L ** 3; Ue, _ = lattice_half(L, 0.3, False); Uo, _ = lattice_half(L, 0.3, True); Ue, Uo = Ue.toarray(), Uo.toarray()
    I, Jx = np.triu_indices(N, 1); NP = I.size; pid = np.zeros((N, N), int); pid[I, Jx] = pid[Jx, I] = np.arange(NP)
    def pedges(U):
        S, T = [], []; nb = [np.nonzero(abs(U[:, x]) > TOL)[0] for x in range(N)]
        for k in range(NP):
            cand = np.union1d(nb[I[k]], nb[Jx[k]])
            for y1, y2 in itertools.combinations(cand, 2):
                if abs(U[y1, I[k]] * U[y2, Jx[k]] - U[y1, Jx[k]] * U[y2, I[k]]) > TOL: S.append(k); T.append(pid[y1, y2])
        return np.array(S), np.array(T)
    E = (pedges(Ue), pedges(Uo)); occ = np.zeros((NP, N), bool); occ[np.arange(NP), I] = occ[np.arange(NP), Jx] = True
    f = [rstate(N) for _ in range(4)]; Psi = np.outer(f[0], f[1]) - np.outer(f[1], f[0]) + 0.8 * (np.outer(f[2], f[3]) - np.outer(f[3], f[2])); Psi /= np.linalg.norm(Psi)
    odds = lambda P: 2 * abs(P[I, Jx]) ** 2; M = 20000; rho = odds(Psi); rhom = rho.copy(); cfg = rng.choice(NP, M, p=rho / rho.sum())
    err = errm = 0; st = np.zeros(3)
    for h in range(8):
        U = Uo if h % 2 else Ue; S, T = E[h % 2]; New = U @ Psi @ U.T; p, q = odds(Psi), odds(New)
        J, opt, se = f5(p, q, S, T, (occ[S] != occ[T]).sum(1) / 2.0); rho = push(rho, J, p); err = max(err, 0.5 * abs(rho - q).sum())
        d0, d1 = np.zeros(N), np.zeros(N); np.add.at(d0, I, p); np.add.at(d0, Jx, p); np.add.at(d1, I, q); np.add.at(d1, Jx, q)
        t1, s1 = np.nonzero(abs(U) > TOL); J1 = f5(d0 / 2, d1 / 2, s1, t1, (s1 != t1) + 0.0)[0]; K1 = mat(J1, N) / np.where(d0 > 0, d0 / 2, 1)[None, :]
        R = np.zeros((N, N)); R[I, Jx] = rhom / 2; R = K1 @ (R + R.T) @ K1.T; rhom = 2 * R[I, Jx]; errm = max(errm, 0.5 * abs(rhom - q).sum())
        nc = sample(cfg, J, NP); st += np.bincount((occ[nc] != occ[cfg]).sum(1) // 2, minlength=3)[:3]; cfg = nc; Psi = New
    ch = chi2(cfg, odds(Psi), M)
    check('D1 joint F5 keeps the joint odds of two entangled relays exactly; 20000 sampled pairs match', err < 1e-12 and ch < 1.3, f'max TV {err:.1e}, chi2/dof {ch:.2f}')
    check('D2 control: each relay moved by its own one-relay F5 kernel does not keep the joint odds', errm > 0.05, f'TV {errm:.3f}')
    print(f'      per half-tick: both stay {st[0] / st.sum():.3f}, one moves {st[1] / st.sum():.3f}, both move {st[2] / st.sum():.3f}')


# ------------------------------------------------------------------ E
def section_E():
    print('E. relay number free: ring of 3 blocks x 4 fermion modes (4096 occupations), shift + pair-pulse coins (relay-number model)')
    L, NM = 3, 12; DIM = 1 << NM; bits = ((np.arange(DIM)[:, None] >> (NM - 1 - np.arange(NM))) & 1).astype(np.int8)
    VAL, DIRR = np.array([1, 1, -1, -1]), np.array([1, 0, 1, 0])
    pi_S = np.array([4 * ((i // 4 + (1 if DIRR[i % 4] else -1)) % L) + i % 4 for i in range(NM)]); tgt = np.zeros(DIM, int); sgn = np.ones(DIM)
    for s in range(DIM):
        img = pi_S[np.nonzero(bits[s])[0]]; tgt[s] = int(sum(1 << (NM - 1 - j) for j in img))
        sgn[s] = (-1.0) ** sum(1 for i in range(len(img)) for j in range(i + 1, len(img)) if img[i] > img[j])
    def _sh(v): o = np.zeros_like(v); o[tgt] = sgn * v; return o
    def loc(k): return reduce(np.kron, [np.diag([1.0, -1.0]) if j < k else (np.array([[0, 1], [0, 0.0]]) if j == k else np.eye(2)) for j in range(4)])
    c4 = [loc(k) for k in range(4)]
    def coin(E):
        H = 0.4 * (c4[0].T @ c4[1] + c4[2].T @ c4[3]) + E * (c4[0].T @ c4[3].T + c4[1].T @ c4[2].T); w, V = np.linalg.eigh(H + H.T)
        C = (V * np.exp(-1j * w)) @ V.conj().T; C[abs(C) < 1e-12] = 0; return C
    lc = np.stack([(np.arange(DIM) >> (4 * (L - 1 - b))) & 15 for b in range(L)], 1)
    def cedges(C):
        sup = [np.nonzero(abs(C[:, a]) > 0)[0] for a in range(16)]; S, T = [], []
        for x in range(DIM):
            tg = np.zeros(1, int)
            for b in range(L): tg = (tg[:, None] * 16 + sup[lc[x, b]][None, :]).ravel()
            S.append(np.full(tg.size, x)); T.append(tg)
        return np.concatenate(S), np.concatenate(T)
    Et = lambda t: 0.8 * np.sin(np.pi * (t + 0.5) / 8) ** 2 if t < 8 else 0.0
    Qb = np.stack([bits[:, 4 * b:4 * b + 4] @ VAL for b in range(L)], 1); Nr = bits.sum(1)
    psi = np.zeros(DIM, complex); psi[1 << (NM - 1)] = 1 / np.sqrt(2); psi[1 << (NM - 6)] = 1j / np.sqrt(2)
    M = 6000; cfg = rng.choice(DIM, M, p=abs(psi) ** 2); rho = abs(psi) ** 2; err = se_ = 0; viol = 0; ev = np.zeros(4); cache = {}
    for t in range(14):
        psi = _sh(psi); cfg = tgt[cfg]; r2 = np.zeros(DIM); r2[tgt] = rho; rho = r2; C = coin(Et(t)); new = psi.copy()
        for b in range(L): new = np.einsum('ij,ajb->aib', C, new.reshape(16 ** b, 16, 16 ** (L - 1 - b))).ravel()
        if Et(t) not in cache: cache[Et(t)] = cedges(C)
        S, T = cache[Et(t)]; p, q = abs(psi) ** 2, abs(new) ** 2; J, opt, se = f5(p, q, S, T, (bits[S] != bits[T]).sum(1) + 0.0, iters=6000)
        se_ = max(se_, se); rho = push(rho, J, p); err = max(err, 0.5 * abs(rho - q).sum()); nc = sample(cfg, J, DIM)
        viol += int(np.any(Qb[nc] != Qb[cfg], 1).sum()); dN = Nr[nc] - Nr[cfg]
        ev += [(nc == cfg).sum(), ((nc != cfg) & (dN == 0)).sum(), (dN > 0).sum(), (dN < 0).sum()]; cfg = nc; psi = new
    PT = abs(psi) ** 2; pe = np.bincount(Nr, PT, minlength=13); pm = np.bincount(Nr[cfg], minlength=13) / M
    z = np.abs(pm - pe).max() / np.sqrt(0.25 / M)
    check('E1 F5 on whole half-ticks of occupation configurations keeps Born while relays are created and end; each event keeps every block value',
          err < 1e-9 and z < 5 and viol == 0 and ev[2] > 0 and ev[3] > 0,
          f'max TV {err:.1e} (Sinkhorn {se_:.0e}); P(N=1,3,5) {pe[1]:.3f},{pe[3]:.3f},{pe[5]:.3f} vs {pm[1]:.3f},{pm[3]:.3f},{pm[5]:.3f}; block-value violations {viol}')
    ev = ev / ev.sum(); print(f'      coin events per relay-tick: stay {ev[0]:.3f}, switch {ev[1]:.3f}, pair begun {ev[2]:.3f}, pair ended {ev[3]:.3f}')


# ------------------------------------------------------------------ F
def labels(dims): return np.array(list(itertools.product(*[range(d) for d in dims])))
def jstep(U, psi, lab, cfg):
    s, t = edges(U); new = U @ psi; J = f5(abs(psi) ** 2, abs(new) ** 2, s, t, (lab[s] != lab[t]).sum(1) + 0.0)[0]
    return new, sample(cfg, J, psi.size), J
def Ry2(th, d, i, j):
    R = np.eye(d, dtype=complex); c, s = np.cos(th / 2), np.sin(th / 2); R[i, i], R[i, j], R[j, i], R[j, j] = c, -s, s, c; return R


def section_F():
    print('F. readers and CHSH (relays on two Margolus blocks; supplied basis rotations and pointer couplings)')
    lab = labels((8, 8)); I8 = np.eye(8); psi0 = np.zeros(64, complex); psi0[1] = 1 / np.sqrt(2); psi0[8] = -1 / np.sqrt(2); sg = np.where(np.arange(8) == 0, 1, -1)
    def run(a, b, M, order):
        psi = psi0.copy(); cfg = rng.choice(64, M, p=abs(psi) ** 2); bm = 0; RA, RB = Ry2(a, 8, 0, 1), Ry2(b, 8, 0, 1)
        if order == 'sim': psi, cfg, J = jstep(np.kron(RA, RB), psi, lab, cfg)
        else:
            psi, cfg, J = jstep(np.kron(I8, RB), psi, lab, cfg); b0 = lab[cfg, 1].copy(); psi, cfg, _ = jstep(np.kron(RA, I8), psi, lab, cfg); bm = int((lab[cfg, 1] != b0).sum())
        P = abs(psi.reshape(8, 8)) ** 2; MB = np.zeros((8, 8)); np.add.at(MB, (lab[J[1], 1], lab[J[0], 1]), J[2])
        return (P * np.outer(sg, sg)).sum(), (sg[lab[cfg, 0]] * sg[lab[cfg, 1]]).mean(), bm, MB
    A_, B_ = (0.0, np.pi / 2), (np.pi / 4, -np.pi / 4); out = {}
    for order in ('sim', 'seq'):
        R = {(a, b): run(a, b, 40000, order) for a in A_ for b in B_}
        S = [abs(R[A_[0], B_[0]][i] + R[A_[0], B_[1]][i] + R[A_[1], B_[0]][i] - R[A_[1], B_[1]][i]) for i in (0, 1)]
        out[order] = (S, sum(r[2] for r in R.values()), abs(R[A_[0], B_[0]][3] - R[A_[1], B_[0]][3]).max())
    (Ss, _, dB), (Sq, bm, _) = out['sim'], out['seq']
    check('F1 CHSH: sampled relay outcomes reach the quantum value, settings applied in one half-tick or one after the other',
          abs(Ss[0] - 2 * np.sqrt(2)) < 1e-12 and Ss[1] > 2.75 and Sq[1] > 2.75, f'exact {Ss[0]:.6f}; relays {Ss[1]:.3f} (same half-tick), {Sq[1]:.3f} (B first)')
    check('F2 support: a later step acting on A alone never moves B, so B\'s recorded outcome stands', bm == 0, f'B moves {bm} of 160000')
    print(f"      untested prediction: same-half-tick settings shift B's own turn odds by {dB:.4f} between a = 0 and pi/2 (B's outcome odds unchanged)")
    NP_ = 12; dims = (2, NP_, NP_); lab = labels(dims); IP = np.eye(NP_); sw = IP.copy(); sw[[5, 6]] = sw[[6, 5]]
    def m1d(mu, odd):
        Wl = np.cos(mu / 2) * np.array([[0, 1], [1, 0]]) + 1j * np.sin(mu / 2) * np.eye(2); U = np.zeros((NP_, NP_), complex)
        for b in range(NP_ // 2): ij = [(2 * b + odd) % NP_, (2 * b + 1 + odd) % NP_]; U[np.ix_(ij, ij)] = Wl
        return U
    CP1 = np.kron(np.diag([1, 0]), np.eye(NP_ ** 2)) + np.kron(np.diag([0, 1]), np.kron(sw, IP)); CP2 = np.kron(np.diag([1, 0]), np.eye(NP_ ** 2)) + np.kron(np.diag([0, 1]), np.kron(IP, sw))
    res = {}
    for muP in (0.0, 0.4):
        for rule in ('joint', 'own'):
            psi = np.zeros(2 * NP_ ** 2, complex); i0 = 5 * NP_ + 5; psi[i0] = 1; M = 20000; cfg = np.full(M, i0); pm = 0
            steps = [np.kron(Ry2(2 * np.arcsin(np.sqrt(0.7)), 2, 0, 1), np.eye(NP_ ** 2)), CP1, CP2] + [np.kron(np.eye(2), np.kron(m1d(muP, h % 2), m1d(muP, h % 2))) for h in range(6)]
            steps.append(np.kron(Ry2(1.1, 2, 0, 1), np.eye(NP_ ** 2)))
            for k, U in enumerate(steps):
                if rule == 'joint':
                    prev = lab[cfg].copy(); psi, cfg, _ = jstep(U, psi, lab, cfg)
                    if k == len(steps) - 1: pm = int((lab[cfg][:, 1:] != prev[:, 1:]).sum())
                else:
                    new = U @ psi; P0, P1 = abs(psi.reshape(dims)) ** 2, abs(new.reshape(dims)) ** 2; Lc = lab[cfg].copy()
                    for fct in range(3):
                        ax = tuple(x for x in range(3) if x != fct); Uf = abs(U).reshape(dims + dims).max(axis=tuple(x for x in range(6) if x not in (fct, 3 + fct)))
                        t, s = np.nonzero(Uf > TOL); Lc[:, fct] = sample(Lc[:, fct], f5(P0.sum(ax), P1.sum(ax), s, t, (s != t) + 0.0)[0], dims[fct])
                    cfg = (Lc[:, 0] * NP_ + Lc[:, 1]) * NP_ + Lc[:, 2]; psi = new
            P = abs(psi.reshape(dims)) ** 2; Lc = lab[cfg]; side = np.arange(NP_) >= 6
            res[(muP, rule)] = (np.mean(side[Lc[:, 1]] != side[Lc[:, 2]]), P[:, side][:, :, ~side].sum() + P[:, ~side][:, :, side].sum(), side[Lc[:, 1]].mean(), P[:, side].sum(), pm)
    j0, o0, j4, o4 = res[(0.0, 'joint')], res[(0.0, 'own')], res[(0.4, 'joint')], res[(0.4, 'own')]
    check('F3 two readers of one system: joint F5 gives Born reading odds and never-disagreeing readers; later system steps never move pointers',
          j0[0] == 0 and abs(j0[2] - 0.3) < 0.015 and j0[4] == 0 and abs(j4[0] - j4[1]) < 0.015,
          f'ballistic pointers: P(read) {j0[2]:.4f} vs 0.3, disagreement {j0[0]:.4f}; massive pointers: disagreement {j4[0]:.4f} vs Born {j4[1]:.4f}')
    check('F4 control: pointers moved by their own marginal odds disagree (2p(1-p) = 0.42 when Born says 0)', abs(o0[0] - 0.42) < 0.02 and o4[0] > j4[1] + 0.1,
          f'{o0[0]:.4f}; massive {o4[0]:.4f} vs Born {o4[1]:.4f}')


if __name__ == '__main__':
    for sec in (section_A, section_B, section_C, section_D, section_E, section_F):
        sec(); print(f'      [{time.time() - T0:.0f} s]')
    print('supplied: configuration space; cost (modes moved); max-entropy tie-break; the half-tick as the step; gates, coins, pulse; states.')
    print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
