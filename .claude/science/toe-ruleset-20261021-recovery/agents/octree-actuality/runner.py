#!/usr/bin/env python3
"""octree-actuality: CL-2 actuality (transport + records) on the octree ladder that carries octree-16's light family
(supplied models; finite diagnostics; no physical identification).
 A  the ladder (8^3 fine sites, R = 0..2) and its light content; internal labels are spectators
 B  existence and Born exactness of the transport on every ladder step; the exchange's two-hop elements are needed
 C  jump statistics of the actual configuration vs |q|; tie-break vs Born floor; one-cell source = Born leak
 D  no-signalling: Born level exact; event-level dependence = shared transport component; pointers decouple it
 E  records of coarse-rung modes: count per mode and per site"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm
from scipy.optimize import linprog
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import spsolve

T0 = time.monotonic(); PASS = FAIL = 0; RNG = np.random.default_rng(20261021)
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
OM = np.exp(2j * np.pi / 3); I8 = np.eye(8)
C = np.array(list(itertools.product((0, 1), repeat=3))); cc0 = C - 0.5
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        Rm = np.zeros((3, 3))
        for i in range(3): Rm[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(Rm), 1): rots.append(Rm)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def axang(Rm):
    a = np.arccos(np.clip((np.trace(Rm) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((Rm + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([Rm[2, 1] - Rm[1, 2], Rm[0, 2] - Rm[2, 0], Rm[1, 0] - Rm[0, 1]]) / (2 * np.sin(a)), a
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: g = XI[a].conj() @ XI[b]; W[a, b] = -g / abs(g) / np.sqrt(3)
def Lrot(Rm):
    n_, a = axang(Rm); Dm = expm(-1j * a * sum(n_[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = int(np.argmin(np.sum(abs(cc0 - Rm @ cc0[i]), 1))); L[k, i] = XI[k].conj() @ Dm @ XI[i]
    return L
def ex(th): return np.cos(th) * I8 + 1j * np.sin(th) * W
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def logH(U):
    w, V = np.linalg.eig(U); H = (V * (-np.angle(w))) @ np.linalg.inv(V); return (H + H.conj().T) / 2
class Tick:   # CL-1 tick: even cube exp(-i st W), odd cube exp(+i st W); copy mass F = exp(i M P1 W / 2) on both sides
    def __init__(s, st):
        s.st, s.Ve, s.Vo = st, ex(-st), ex(st); h = 1e-5; al = []
        U0 = lambda K: Dg(K) @ ex(st) @ Dg(K).conj().T @ ex(-st)
        for a in range(3):
            e = np.zeros(3); e[a] = h; A = (logH(U0(e)) - logH(U0(-e))) / (2 * h); al.append((A + A.conj().T) / 2)
        s.v = np.sqrt(np.trace(al[0] @ al[0]).real / 8); s.al = [A / s.v for A in al]
        g5 = 1j * s.al[0] @ s.al[1] @ s.al[2]; s.g5 = (g5 + g5.conj().T) / 2
        iC3 = [i for i, Rm in enumerate(rots) if np.isclose(np.trace(Rm), 0) and np.allclose(axang(Rm)[0], np.ones(3) / np.sqrt(3))][0]
        Sig = [-1j * s.al[1] @ s.al[2], -1j * s.al[2] @ s.al[0], -1j * s.al[0] @ s.al[1]]; L3 = Lrot(rots[iC3]); s.Sig = Sig
        Mr = np.array([[np.trace(L3 @ s.al[a] @ L3.conj().T @ s.al[b]).real / 8 for b in range(3)] for a in range(3)]); nax, ang = axang(np.round(Mr).T)
        best = min((max(np.abs(Sx @ s.al[q] @ Sx.conj().T - L3 @ s.al[q] @ L3.conj().T).max() for q in range(3)), k, Sx) for k, Sx in
                   enumerate(expm(-1j * sgn * ang / 2 * sum(nax[k_] * Sig[k_] for k_ in range(3))) for sgn in (1, -1)))
        wr, Vr = np.linalg.eig(best[2].conj().T @ L3); Vl = Vr[:, np.abs(wr - OM) < 1e-5]; P1 = Vl @ np.linalg.pinv(Vl)
        s.P1 = (P1 + P1.conj().T) / 2; s.Fc = {}
    def U(s, K, M=0.0):
        X = Dg(K) @ s.Vo @ Dg(K).conj().T @ s.Ve
        if M:
            F = s.Fc.setdefault(M, expm(1j * M * s.P1 @ W / 2)); X = F @ X @ F
        return X
    def H(s, K, M=0.0): return logH(s.U(K, M)) / s.st
def s_amp(q): return np.prod((1 + np.exp(-1j * np.asarray(q))) / 2)
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



# ---------------- real-space ladder with a uniform twist (background link theta/L on every fine bond)
def lidx(L, x):
    x = np.mod(x, L); return int((x[0] * L + x[1]) * L + x[2])
class Ladder:
    """rung j: torus of L/2^j sites (rung-j site P at fine position 2^j P); steps E = F Ve F (even cubes, all rungs),
    O = Vo (odd cubes, all rungs), X = exp(-i kap st H5) (cell <-> its 8 children, same corner, via Xm/sqrt8)."""
    def __init__(s, L, R, st=0.04, kap=0.5, M=None, theta=(0, 0, 0), orient='L', exch=True):
        tk = Tick(st); s.tk = tk; M = st if M is None else M; Pp = (I8 + tk.g5) / 2; Pm = (I8 - tk.g5) / 2
        Xm = W @ Pp if orient == 'L' else W @ Pm; s.Xm = Xm
        Ls = [L >> j for j in range(R + 1)]; Ns = [l ** 3 for l in Ls]; off = np.concatenate([[0], np.cumsum(Ns)]).astype(int)
        s.L, s.R, s.Ls, s.off, s.N = L, R, Ls, off, int(off[-1]); th = np.asarray(theta, float) / L
        s.rung = np.concatenate([np.full(Ns[j], j) for j in range(R + 1)])
        pos = []
        for j in range(R + 1):
            for x in itertools.product(range(Ls[j]), repeat=3): pos.append((2 ** j) * np.array(x))
        s.pos = np.array(pos)                       # fine position of every mode (coarse site P at 2^j P)
        P1W = tk.P1 @ W; P1W = (P1W + P1W.conj().T) / 2
        def ph(j, x0, x1):   # twist phase along the direct displacement (minimal image), fine units
            d = (np.asarray(x1) - np.asarray(x0)) * 2 ** j; return np.exp(1j * th @ d)   # unwrapped displacement inside the block
        def cubes(j, par):
            Lj = Ls[j]; out = []
            for n in itertools.product(range(Lj // 2), repeat=3):
                o = 2 * np.array(n) + par; xs = [o + cp for cp in C]; ids = [off[j] + lidx(Lj, x) for x in xs]
                lab = [int(np.argmin(np.abs(C - np.mod(x, 2)).sum(1))) for x in xs]; Wg = np.zeros((8, 8), complex); Pg = np.zeros((8, 8), complex)
                for i in range(8):
                    for k in range(8):
                        if np.abs(C[i] - C[k]).sum() == 1: Wg[i, k] = W[lab[i], lab[k]] * ph(j, xs[k], xs[i])
                        Pg[i, k] = P1W[lab[i], lab[k]] * ph(j, xs[k], xs[i])
                out.append((ids, Wg, Pg))
            return out
        def assemble(blocks):
            r, c, v = [], [], []; cov = np.zeros(s.N, bool)
            for ids, B in blocks:
                ii, jj = np.meshgrid(ids, ids, indexing='ij'); r.append(ii.ravel()); c.append(jj.ravel()); v.append(B.ravel()); cov[ids] = True
            free = np.where(~cov)[0]; r.append(free); c.append(free); v.append(np.ones(free.size))
            Mx = sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(s.N, s.N)); Mx.data[np.abs(Mx.data) < 1e-15] = 0; Mx.eliminate_zeros(); return Mx
        eb, ob = [], []
        for j in range(R + 1):
            for ids, Wg, Pg in cubes(j, 0):
                Fm = expm(1j * M * Pg / 2); eb.append((ids, Fm @ expm(-1j * st * Wg) @ Fm))
            for ids, Wg, Pg in cubes(j, 1): ob.append((ids, expm(1j * st * Wg)))
        s.E, s.O = assemble(eb), assemble(ob)
        H5 = sp.lil_matrix((s.N, s.N), dtype=complex)
        for j in range(R if exch else 0):
            Lc = Ls[j + 1]; Lf = Ls[j]
            for n in itertools.product(range(Lc // 2), repeat=3):
                n = np.array(n)
                for ib, b in enumerate(C):
                    P = 2 * n + b; ci = off[j + 1] + lidx(Lc, P)
                    for c in C:
                        for ia, a in enumerate(C):
                            x = 2 * (2 * n + c) + a; fi = off[j] + lidx(Lf, x); v = Xm[ia, ib] / np.sqrt(8)
                            if abs(v) > 1e-15:
                                v = v * ph(j, 2 * P, x); H5[fi, ci] += v; H5[ci, fi] += np.conj(v)
        H5 = H5.tocsr(); s.H5 = H5; blocks = []
        if R and exch:
            nc, lab = connected_components(H5 != 0, directed=False)
            for k in range(nc):
                ids = np.where(lab == k)[0]
                if len(ids) > 1:
                    Hb = H5[ids][:, ids].toarray(); w, V = np.linalg.eigh(Hb); blocks.append((list(ids), (V * np.exp(-1j * kap * st * w)) @ V.conj().T))
        s.X = assemble(blocks) if blocks else sp.identity(s.N, dtype=complex, format='csr')
    def tick(s): return (s.X @ (s.O @ s.E)).toarray()

def sample(cfg, J, n):
    s, t, w = J; o = np.lexsort((t, s)); s, t, w = s[o], t[o], w[o]; Cw = np.cumsum(w)
    a0, a1 = np.searchsorted(s, np.arange(n), 'left'), np.searchsorted(s, np.arange(n), 'right')
    base = np.where(a0 > 0, Cw[np.maximum(a0 - 1, 0)], 0.0); u = RNG.random(cfg.size) * np.bincount(s, w, minlength=n)[cfg]
    return t[np.clip(np.searchsorted(Cw, base[cfg] + u, 'right'), a0[cfg], a1[cfg] - 1)]
def plan(Us, ph, cost=None, tb='entropy'):
    new = Us @ ph; p, q = abs(ph) ** 2, abs(new) ** 2; t, s = Us.nonzero(); c = (s != t) + 0.0 if cost is None else cost(s, t)
    J, fun, err = f5(p, q, s, t, c, tb); return J, fun, err, p, q, new
def cheb(lad, s, t):
    d = (lad.pos[t] - lad.pos[s] + lad.L // 2) % lad.L - lad.L // 2; return np.abs(d).max(-1)
def light(lad):
    U = lad.tick(); w, V = np.linalg.eig(U); om = -np.angle(w); nrm = np.sum(abs(V) ** 2, 0)
    r0 = np.array([np.sum(abs(V[lad.rung == 0, i]) ** 2) for i in range(lad.N)]) / nrm
    return om, r0, V / np.sqrt(nrm)
def light_state(lad):
    om, r0, V = light(lad); i = [k for k in np.argsort(abs(om)) if r0[k] > 0.9][0]; return V[:, i], 1 - r0[i], om[i]
def steps(lad, sl): return [lad.E, lad.O, lad.X] if sl == 'sep' else [lad.E, (lad.X @ lad.O).tocsr()]
def rstate(n): v = RNG.normal(size=n) + 1j * RNG.normal(size=n); return v / np.linalg.norm(v)
QD = np.array([.3, .5, .81]) / np.linalg.norm([.3, .5, .81])
LADS = {}
def lad_at(R, qs):
    k = (R, qs)
    if k not in LADS: LADS[k] = Ladder(8, R, theta=8 * qs * QD)
    return LADS[k]

# ============================================================ A
print('== A. the octree ladder carrying the light family (8^3 fine sites, R rungs, st = 0.04, kap = 0.5, M = st, exchange X\' = W(1+g5)/2)')
rows = []
for R in (0, 1, 2):
    lad = lad_at(R, 0.1); U = lad.tick(); om, r0, V = light(lad); w0 = lad.tk.v * 2 * 0.1
    lw = np.sort(abs(om[(abs(om) < 1.5 * w0)])); n0 = int(np.sum((abs(om) < 1.5 * w0) & (r0 > 0.9)))
    mir = np.sort(abs(om[(r0 < 0.1) & (abs(om) < 0.03)]))
    rows.append((R, lad.N, abs(U @ U.conj().T - np.eye(lad.N)).max(), n0, lw[0] / w0, mir[0] / lw[0] if mir.size else None))
check('A1 ladder unitary; at |q| = 0.1: R = 0 one Dirac copy (4 levels), R = 1, 2 one Weyl pair (2) on the fine rung at omega = 2v|q|, mirror ~2^R higher on the top rung',
      all(r[2] < 1e-13 for r in rows) and [r[3] for r in rows] == [4, 2, 2] and all(abs(r[4] - 1) < 0.01 for r in rows) and abs(rows[1][5] - 2) < 0.1 and 3.3 < rows[2][5] < 4.2,
      '; '.join(f'R={r[0]}: {r[1]} modes, unit {r[2]:.0e}, light {r[3]}, omega/2v|q| {r[4]:.4f}' + (f', mirror x{r[5]:.2f}' if r[5] else '') for r in rows))
lad = lad_at(1, 0.1); E2 = sp.kron(sp.identity(2), lad.E).tocsr(); ps = rstate(2 * lad.N); J2, *_ = plan(E2, ps)
M2 = sp.csr_matrix((J2[2], (J2[1], J2[0])), shape=(2 * lad.N,) * 2).toarray(); dsum = 0
for f in range(2):
    sl_ = slice(f * lad.N, (f + 1) * lad.N); Jf, *_ = plan(lad.E, ps[sl_]); Mf = sp.csr_matrix((Jf[2], (Jf[1], Jf[0])), shape=(lad.N,) * 2).toarray()
    dsum = max(dsum, abs(M2[sl_, sl_] - Mf).max(), abs(M2[sl_, :]).sum() - abs(M2[sl_, sl_]).sum())
check('A2 THEOREM with trivial links each step is A (x) 1_16: no element changes the internal label, so the transport is the one-species one per label (2 labels)',
      dsum < 1e-12, f'max deviation from the direct sum {dsum:.1e}')

# ============================================================ B
print('== B. existence and Born exactness of the CL-2 transport on the ladder')
worst = 0; feas = True; serr = 0; cnt = 0
for R in (1, 2):
    for nm in ('light', 'random', 'cell'):
        lad = lad_at(R, 0.1); S, _, _ = light_state(lad)
        if nm == 'light': ph = S
        elif nm == 'random': ph = rstate(lad.N)
        else: ph = np.zeros(lad.N, complex); cb = [lidx(8, c) for c in C]; ph[cb] = S[cb]; ph /= np.linalg.norm(ph)
        for sl in ('sep', 'merged'):
            x = ph.copy()
            for _ in range(2):
                for Us in steps(lad, sl):
                    J, fun, err, p, q, x = plan(Us, x); cnt += 1
                    if J is None: feas = False; continue
                    worst = max(worst, abs(np.bincount(J[1], J[2], minlength=lad.N) - q).max()); serr = max(serr, err)
check('B1 THEOREM existence (Hall: q(S) = |P_S U P_N(S) psi|^2 <= p(N(S)), then max-flow) on every ladder step; the distribution stays the odds',
      feas and worst < 1e-9, f'{cnt} steps (R = 1, 2; light, random, one-cell; both slicings): all feasible, max |rho - |psi|^2| {worst:.1e}, scaling residual {serr:.0e}')
lad = lad_at(2, 0.1); Mr = 20000; ph = rstate(lad.N); cfg = RNG.choice(lad.N, Mr, p=abs(ph) ** 2); chis = []
for sl in ('merged',):
    for _ in range(3):
        for Us in steps(lad, sl): J, fun, err, p, q, ph = plan(Us, ph); cfg = sample(cfg, J, lad.N)
    P = abs(ph) ** 2; fr = np.bincount(cfg, minlength=lad.N); e = Mr * P; k = e >= 5; chis.append(((fr[k] - e[k]) ** 2 / e[k]).sum() / (k.sum() - 1))
    coarse_s, coarse_b = np.mean(lad.rung[cfg] > 0), P[lad.rung > 0].sum()
check('B2 sampled actual configurations (20000 relays, R = 2, 3 ticks) match the odds; the fraction on coarse rungs is their Born weight',
      chis[0] < 1.3 and abs(coarse_s - coarse_b) < 4 * np.sqrt(coarse_b / Mr), f'chi2/dof {chis[0]:.2f}; on coarse rungs {coarse_s:.4f} vs Born {coarse_b:.4f}')
inf = []
for R in (1, 2):
    lad = lad_at(R, 0.1); S, _, _ = light_state(lad); phi = lad.O @ (lad.E @ S); one = (abs(lad.H5) > 1e-15).astype(float) + sp.identity(lad.N)
    t1, s1 = one.nonzero(); p, q = abs(phi) ** 2, abs(lad.X @ phi) ** 2; inf.append(f5(p, q, s1, t1, (s1 != t1) + 0.0, 'lp')[0] is None)
check('B3 X = 1 - i sin(tau) H5 + (cos tau - 1) H5^2 (H5^3 = H5); its two-hop elements are needed: no transport on the one-hop support 1 + H5 for the light state',
      all(inf), f'one-hop support infeasible: R = 1 {inf[0]}, R = 2 {inf[1]}')

# ============================================================ C
print('== C. jump statistics of the actual configuration (fine-site record moves by Chebyshev distance d in one tick)')
def tick_pd(lad, psi, sl):
    p0 = abs(psi) ** 2; K = None; ph = psi; mv = []
    for Us in steps(lad, sl):
        J, fun, err, p, q, ph = plan(Us, ph); mv.append(fun); k = sp.csr_matrix((J[2] / p[J[0]], (J[1], J[0])), shape=(lad.N,) * 2); K = k if K is None else k @ K
    Jt = (K @ sp.diags(p0)).tocoo(); s, t, w = Jt.col, Jt.row, Jt.data; ff = (lad.rung[s] == 0) & (lad.rung[t] == 0); d = cheb(lad, s, t)
    return np.array([w[ff & (d == k)].sum() for k in range(5)]), mv
tab = {}
for R, qlist in ((0, (0.1,)), (1, (0.1, 0.03, 0.01, 0.003)), (2, (0.1,))):
    for qs in qlist:
        lad = lad_at(R, qs); S, cw, _ = light_state(lad)
        for sl in (('sep', 'merged') if R else ('sep',)): tab[(R, qs, sl)] = tick_pd(lad, S, sl) + (cw,)
print(f'   R=0 (fine lattice): P(d=1..4) ' + ' '.join(f'{x:.1e}' for x in tab[(0, 0.1, "sep")][0][1:]))
for R in (1, 2):
    for qs in ((0.1, 0.03, 0.01, 0.003) if R == 1 else (0.1,)):
        a, b = tab[(R, qs, 'sep')], tab[(R, qs, 'merged')]
        print(f'   R={R} |q|={qs:<5} coarse {a[2]:.1e} | X separate: P(d=1..4) ' + ' '.join(f'{x:.1e}' for x in a[0][1:]) + f', X moves {a[1][2]:.1e} | X in odd: ' + ' '.join(f'{x:.1e}' for x in b[0][1:]))
q1 = (0.1, 0.03, 0.01, 0.003); sl3 = np.polyfit(np.log(q1), np.log([tab[(1, q, 'sep')][0][3] for q in q1]), 1)[0]; slc = np.polyfit(np.log(q1), np.log([tab[(1, q, 'sep')][2] for q in q1]), 1)[0]
mlong = [tab[(1, q, 'merged')][0][2:].sum() for q in q1]
check('C1 DIAGNOSTIC exchange X as its own step: records jump beyond the fine cone (d = 3) at ~|q|^2 per tick; coarse occupation is ~|q|^4 (jumps track the coarse amplitude)',
      abs(sl3 - 2) < 0.15 and abs(slc - 4) < 0.25, f'exponents: P(d=3) {sl3:.2f}, coarse Born weight {slc:.2f}; P(d=3) = {tab[(1, 0.1, "sep")][0][3] / 0.01:.1e} |q|^2')
check('C2 DIAGNOSTIC X inside the odd half-tick: d >= 2 jumps take most of the moved mass at every |q| (no smoothness suppression)',
      np.ptp(mlong) < 1e-3 * max(mlong) and min(mlong) > 0.02 and tab[(0, 0.1, 'sep')][0][3:].sum() == 0, f'P(d >= 2) per tick {min(mlong):.4f}..{max(mlong):.4f} for |q| = 0.1..0.003; fine lattice: P(d >= 3) = 0')
fl = []
for R in (1, 2):
    lad = lad_at(R, 0.1); S, _, _ = light_state(lad); phi = lad.O @ (lad.E @ S)
    for nm, Us, x in (('X', lad.X, phi), ('XO', (lad.X @ lad.O).tocsr(), lad.E @ S)):
        J, fun, err, p, q, _ = plan(Us, x); s, t, w = J; lng = (lad.rung[s] != lad.rung[t]) | (cheb(lad, s, t) >= 2); act = w[lng].sum()
        t_, s_ = Us.nonzero(); kp = (p[s_] > 1e-20) & (q[t_] > 1e-20); s_, t_ = s_[kp], t_[kp]; L_ = ((lad.rung[s_] != lad.rung[t_]) | (cheb(lad, s_, t_) >= 2)) + 0.0
        A_ = sp.vstack([incidence(s_, lad.N, s_.size), incidence(t_, lad.N, s_.size)]).tocsr()
        r = linprog(L_, A_eq=A_, b_eq=np.concatenate([p, q]), A_ub=sp.csr_matrix((s_ != t_)[None, :] + 0.0), b_ub=[fun * (1 + 1e-9) + 1e-15], bounds=(0, None), method='highs')
        fl.append((R, nm, act, r.fun))
check('C3 DIAGNOSTIC the spread is the entropy tie-break, not Born: least long-move mass (d >= 2 or rung change) among fewest-change plans vs greatest entropy',
      all(f[2] > 30 * f[3] for f in fl), '; '.join(f'R={f[0]} {f[1]}: {f[2]:.1e} vs least {f[3]:.1e}' for f in fl))
lad = lad_at(2, 0.1); S, _, _ = light_state(lad); ph = np.zeros(lad.N, complex); cb = [lidx(8, c) for c in C]; ph[cb] = S[cb]; ph /= np.linalg.norm(ph)
inside = (lad.rung == 0) & np.all(((lad.pos + 1) % 8) <= 3, 1); x = ph.copy(); recs = []
for sl in ('sep', 'merged'):
    x = ph.copy(); K = None
    for Us in steps(lad, sl):
        J, fun, err, p, q, x = plan(Us, x); k = sp.csr_matrix((J[2] / np.where(p[J[0]] > 0, p[J[0]], 1), (J[1], J[0])), shape=(lad.N,) * 2); K = k if K is None else k @ K
    recs.append(1 - (K @ abs(ph) ** 2)[inside].sum())
born = 1 - (abs(x) ** 2)[inside].sum()
check('C4 THEOREM from a one-cell source, P(record beyond the fine cone after one tick) IS the Born leak (both slicings)',
      max(abs(r - born) for r in recs) < 1e-11, f'leak {born:.2e} (st = 0.04, R = 2); records {recs[0]:.2e}, {recs[1]:.2e}; |diff| {max(abs(r - born) for r in recs):.0e} (solver tolerance)')
print('   THEOREM (support) per tick a fine record moves <= 1 + 1 + 3 sites per axis unless it passes a coarse mode, whose chance is its Born weight')

# ============================================================ D
print('== D. no-signalling: a setting U_A on 8 fine sites inside one rung-1 cube; B = the fine sites of the opposite rung-1 cube')
from scipy.stats import unitary_group
UAs = [np.eye(8)] + [unitary_group.rvs(8, random_state=s_) for s_ in (11, 12)]; ev = {}
for R in (1, 2):
    lad = lad_at(R, 0.1); f = lad.rung == 0; r1 = np.array([tuple((x // 4) % 2) for x in lad.pos])
    inA = np.where(f & np.all((lad.pos >= 1) & (lad.pos <= 2), 1))[0]; Bf = np.where(f & np.all(r1 == 1, 1))[0]; far = ~np.all(r1 == 0, 1) & (lad.rung < 2)
    for nm in ('light', 'random'):
        S = light_state(lad)[0] if nm == 'light' else rstate(lad.N)
        for st_, Us, pre in (('X', lad.X, lad.O @ (lad.E @ S)), ('XO', (lad.X @ lad.O).tocsr(), lad.E @ S)):
            res = []
            for Ua in UAs:
                x = pre.copy(); x[inA] = Ua @ x[inA]; J, fun, err, p, q, _ = plan(Us, x)
                res.append((q, sp.csr_matrix((J[2], (J[1], J[0])), shape=(lad.N,) * 2)[:, Bf].toarray(), p))
            ev[(R, nm, st_)] = (max(abs(r[0][far] - res[0][0][far]).max() for r in res[1:]),
                                max((abs(r[1] - res[0][1]).sum(0) / res[0][2][Bf]).max() / 2 for r in res[1:]))
born = max(v[0] for v in ev.values())
check('D1 THEOREM Born level: no step element joins A\'s rung-1 cube to another\'s fine or rung-1 modes, so the odds (= record statistics) there ignore U_A',
      born < 1e-15, f'max change {born:.0e}')
comp = {}
for R in (0, 1, 2):
    lad = lad_at(R, 0.1)
    for nm, Us in (('E', lad.E), ('X', lad.X), ('XO', (lad.X @ lad.O).tocsr())):
        G = (abs(Us) > 0); nc, lab = connected_components(G, directed=False); comp[(R, nm)] = np.bincount(lab).max()
print('   largest component of a step (modes): ' + ', '.join(f'R={k[0]} {k[1]}: {v}' for k, v in comp.items() if not (k[0] == 0 and k[1] != 'E')))
check('D2 FINDING event level: B\'s one-step kernel depends on U_A iff A, B share a step component: not for R = 1 with X separate; yes for R = 2 (top-rung cubes; unbounded '
      'on the infinite ladder) and with X in the odd half-tick (global already at R = 1)',
      ev[(1, 'light', 'X')][1] < 1e-12 and ev[(1, 'random', 'X')][1] < 1e-12 and all(ev[k][1] > 1e-9 for k in ((2, 'random', 'X'), (2, 'light', 'X'), (1, 'random', 'XO'), (2, 'random', 'XO'))),
      '; '.join(f'R={k[0]} {k[1]} {k[2]}: {v[1]:.1e}' for k, v in ev.items()))
lad = lad_at(2, 0.1); f = lad.rung == 0; r1 = np.array([tuple((x // 4) % 2) for x in lad.pos]); N = lad.N
inA = np.where(f & np.all((lad.pos >= 1) & (lad.pos <= 2), 1))[0]; Bf = np.where(f & np.all(r1 == 1, 1))[0]; X2 = sp.kron(sp.identity(2), lad.X).tocsr()
pre = lad.O @ (lad.E @ rstate(N)); tr, pt = [], []
for Ua in UAs:
    x = pre.copy(); x[inA] = Ua @ x[inA]; J, *_ = plan(lad.X, x); tr.append(sp.csr_matrix((J[2], (J[1], J[0])), shape=(N, N))[:, Bf].toarray())
    v = np.zeros(2 * N, complex); v[:N] = x; v[N + Bf] = x[Bf]; v[Bf] = 0
    J, fun, err, p, q, _ = plan(X2, v); pt.append((sp.csr_matrix((J[2], (J[1], J[0])), shape=(2 * N, 2 * N))[:, N + Bf].toarray(), q[N:].sum()))
dtr = max(abs(t - tr[0]).sum() / 2 for t in tr[1:]); dpt = max(abs(t[0] - pt[0][0]).sum() / 2 for t in pt[1:]); dpo = max(abs(t[1] - pt[0][1]) for t in pt[1:])
check('D3 a pointer copying "relay in B" before the step puts B\'s branch in its own component: B\'s flows no longer depend on U_A; pointer odds are Born',
      dtr > 1e-9 and dpt < 1e-15 and dpo < 1e-14, f'B two-time joint without pointer: change {dtr:.1e}; with pointer: {dpt:.0e}; pointer odds change {dpo:.0e}')
print('   readable facts = functions of readers\' present configuration, which is Born (B1): no readable signal beyond the update\'s reach (D1)')

# ============================================================ E
print('== E. records of coarse-rung modes')
rate = {sl: len(steps(lad_at(1, 0.1), sl)) for sl in ('sep', 'merged')}
co = {R: R + 1 for R in (1, 2)}; dens = {R: sum(8.0 ** -j for j in range(R + 1)) for R in (1, 2)}
lad = lad_at(2, 0.1); occ = np.bincount([lidx(8, x) for x in lad.pos], minlength=512)
check('E1 coarse modes are modes, so CL-2 records each every step (2 per tick with X in the odd half-tick, 3 with X separate); placed on Z^3 at 2^j P, a site holds up to R + 1 modes',
      rate == {'sep': 3, 'merged': 2} and occ.max() == 3 and abs(occ.sum() / 512 - dens[2]) < 1e-12,
      f'records per mode per tick {rate}; max modes per site {occ.max()} (R = 2); records per fine site per half-tick {occ.sum() / 512:.4f} (8/7 on the infinite ladder)')
print(f'   the share of records that register an occupied coarse mode = coarse Born weight: {tab[(1, 0.1, "sep")][2]:.1e} at |q| = 0.1, {tab[(1, 0.003, "sep")][2]:.1e} at 0.003 (R = 1)')
print('supplied: coarse sites (axiom-level), fine rate, kap, M = st, st = 0.04, X\', where X sits, twist, states, settings, pointer; 8^3 torus.')
print(f'[{time.monotonic() - T0:.0f} s]')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
