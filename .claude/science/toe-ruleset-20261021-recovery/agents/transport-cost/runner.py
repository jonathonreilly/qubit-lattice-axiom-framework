#!/usr/bin/env python3
"""transport-cost: a hop-weighted (optimal-transport) cost for CL-2's transport on the CL-1 cube tick
(supplied models; finite diagnostics; no physical identification).

Rules compared (all keep the odds exactly and use only nonzero elements of the half-tick):
  modes : CL-2 as registered: fewest changed occupations on average, then greatest entropy;
  hop   : fewest hops on average (each change counted by the hops it spans, per block and species; W1), then greatest entropy;
  hop2  : least mean squared hop count (W2 on the hop metric), then greatest entropy;
  ehop2 : entropic transport, least (mean hop^2 - T x entropy): J_ts = a_s exp(-h_ts^2 / T) b_t;
  uni   : least relative entropy to the half-tick's own squared elements |<t|U|s>|^2;  short: greatest entropy on <= 1 hop.
A tick and the hop count; B properties (uniqueness, labels, separability, many-body, stationary states, CHSH, readers);
C relay streams on plane waves and packets; D long jumps (cube tick and the octree ladder); E entropic transport; F pointer tracks.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time, warnings
warnings.filterwarnings('ignore')
from math import comb
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm
from scipy.optimize import linprog
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import spsolve

T0 = time.time(); PASS = FAIL = 0; TOL = 1e-12
rng = np.random.default_rng(20261021)


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))

# ------------------------------------------------------------------ CL-1 cube tick, transports (inlined from transport-f5 / streams-fix)
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = 2.0 * CORN - 1
HOP = np.abs(CORN[:, None, :] - CORN[None, :, :]).sum(-1)          # taxicab hops between cube corners


def coherent(j, n):
    th, ph, d = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])


XI = [coherent(1.5, v / np.sqrt(3)) for v in NV]
W0 = np.zeros((8, 8), complex); Wax = [np.zeros((8, 8), complex) for _ in range(3)]
for a_, b_ in itertools.product(range(8), repeat=2):
    dd = np.abs(CORN[a_] - CORN[b_])
    if dd.sum() == 1:
        g_ = XI[a_].conj() @ XI[b_]; W0[a_, b_] = -g_ / abs(g_) / np.sqrt(3); Wax[int(np.argmax(dd))][a_, b_] = W0[a_, b_]
Rax = [np.sqrt(3) * w for w in Wax]
S_COPY = 1j * Rax[0] @ Rax[1] @ Rax[2] @ W0                          # copy sign s = i R1 R2 R3 R


def cube_even(eps, mu, M):
    F = expm(1j * (M / 4) * (np.eye(8) - S_COPY) @ W0); return F @ expm(-1j * (eps - mu / 2) * W0) @ F
def cube_odd(eps, mu): return expm(1j * (eps + mu / 2) * W0)


def lattice_half(Ls, Ucube, odd):
    Ls = np.array(Ls); X = np.array(list(itertools.product(*[range(l) for l in Ls]))); par = X % 2
    org = ((X - par) if not odd else (X - (1 - par))) % Ls; blk = (org[:, 0] * Ls[1] + org[:, 1]) * Ls[2] + org[:, 2]
    N = X.shape[0]; grp = np.lexsort((np.arange(N), blk)).reshape(-1, 8); pi = (par @ [4, 2, 1])[grp]
    r = np.repeat(grp, 8, 1).ravel(); c = np.tile(grp, (1, 8)).ravel(); v = Ucube[np.repeat(pi, 8, 1).ravel(), np.tile(pi, (1, 8)).ravel()]
    k = abs(v) > TOL
    return sp.csr_matrix((v[k], (r[k], c[k])), shape=(N, N)), X


def incidence(idx, n, m): return sp.csr_matrix((np.ones(m), (idx, np.arange(m))), shape=(n, m))


def lp(cost, A, b):
    o = dict(primal_feasibility_tolerance=1e-10, dual_feasibility_tolerance=1e-10)
    r = linprog(cost, A_eq=A, b_eq=b, bounds=(0, None), method='highs', options=o)
    if r.status != 0: r = linprog(cost, A_eq=A, b_eq=b, bounds=(0, None), method='highs', options=dict(o, presolve=False))
    return r


def scale_plan(p, q, fs, ft, lk, n, tol=1e-14):
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


def transport(p, q, src, tgt, cost=None, rule='lex', w=None):
    """rule 'lex': least mean cost, then greatest entropy on that face; 'prior': least relative entropy to the
    weights w (w = exp(-cost/T) is entropic optimal transport); 'lp': an LP vertex."""
    keep = (p[src] > 0) & (q[tgt] > 0); n = p.size; src, tgt = src[keep], tgt[keep]; m = src.size
    cost = None if cost is None else cost[keep]; w = None if w is None else w[keep]
    nc, lab = connected_components(sp.csr_matrix((np.ones(m), (src, tgt)), shape=(n, n)), directed=False)
    mass = np.bincount(lab, p, minlength=nc); sc = np.where(mass[lab] > 0, mass[lab], 1.0); p, q = p / sc, q / sc
    p, q = np.where(p > 1e-20, p, 0.0), np.where(q > 1e-20, q, 0.0); keep = (p[src] > 0) & (q[tgt] > 0)
    src, tgt = src[keep], tgt[keep]; m = src.size; cost = None if cost is None else cost[keep]; w = None if w is None else w[keep]
    if rule in ('lex', 'lp', 'lexw'):
        A = sp.vstack([incidence(src, n, m), incidence(tgt, n, m)]).tocsr(); r = lp(cost, A, np.concatenate([p, q]))
        if r.status != 0: return None, 1.0
        if rule == 'lp': return (src, tgt, r.x * sc[src]), 0.0
        y = r.eqlin.marginals; face = cost - y[src] - y[n + tgt] < 1e-9 * max(1.0, cost.max())
        fs, ft, fx = src[face], tgt[face], r.x[face]; used = fx > 1e-13
        G = sp.csr_matrix((np.ones(fs.size + used.sum()), (np.concatenate([fs, n + ft[used]]), np.concatenate([n + ft, fs[used]]))), shape=(2 * n, 2 * n))
        scc = connected_components(G, directed=True, connection='strong')[1]; kp = used | (scc[fs] == scc[n + ft])
        fs, ft, lk = fs[kp], ft[kp], (np.zeros(kp.sum()) if rule == 'lex' else np.log(w[face][kp]))
    elif rule == 'maxent': fs, ft, lk = src, tgt, np.zeros(m)
    else: fs, ft, lk = src, tgt, np.log(w)
    J, err = scale_plan(p, q, fs, ft, lk, n)
    return (fs, ft, J * sc[fs]), err


def mat(J, n): M = np.zeros((n, n)); np.add.at(M, (J[1], J[0]), J[2]); return M
def edges(U): t, s = np.nonzero(abs(U) > TOL); return s, t
def rstate(n): v = rng.normal(size=n) + 1j * rng.normal(size=n); return v / np.linalg.norm(v)
def sample(cfg, J, n):
    s, t, w = J; o = np.lexsort((t, s)); s, t, w = s[o], t[o], w[o]; C = np.cumsum(w)
    st, en = np.searchsorted(s, np.arange(n), 'left'), np.searchsorted(s, np.arange(n), 'right')
    base = np.where(st > 0, C[np.maximum(st - 1, 0)], 0.0); u = rng.random(cfg.size) * np.bincount(s, w, minlength=n)[cfg]
    return t[np.clip(np.searchsorted(C, base[cfg] + u, 'right'), st[cfg], en[cfg] - 1)]
def push(rho, J, p): s, t, w = J; return np.bincount(t, w * rho[s] / p[s], minlength=p.size)


def costs(s, t, rule):
    if rule == 'modes': return 2.0 * (s != t)
    return HOP[s, t] + 0.0


def plan(U, x, rule, T=None):
    """one cube / Bloch 8x8 plan; rule in modes, hop (lexicographic), ehopT (entropic, kernel e^-hop/T), uni, maxent"""
    s, t = edges(U); p, q = abs(x) ** 2, abs(U @ x) ** 2
    if rule == 'modes': return transport(p, q, s, t, 2.0 * (s != t), 'lex')
    if rule == 'hop': return transport(p, q, s, t, HOP[s, t] + 0.0, 'lex')
    if rule == 'ehop': return transport(p, q, s, t, None, 'prior', np.exp(-HOP[s, t] / T))
    if rule == 'uni': return transport(p, q, s, t, None, 'prior', abs(U[t, s]) ** 2)
    if rule == 'maxent': return transport(p, q, s, t, None, 'maxent')
    if rule == 'hop2': return transport(p, q, s, t, HOP[s, t] ** 2 + 0.0, 'lex')
    if rule == 'ehop2': return transport(p, q, s, t, None, 'prior', np.exp(-HOP[s, t] ** 2 / T))
    if rule == 'modese2': return transport(p, q, s, t, 2.0 * (s != t), 'lexw', np.exp(-HOP[s, t] ** 2 / T))
    if rule == 'short':
        k = HOP[s, t] <= 1; return transport(p, q, s[k], t[k], None, 'maxent')
    if rule == 'modesuni': return transport(p, q, s, t, 2.0 * (s != t), 'lexw', abs(U[t, s]) ** 2)
    if rule == 'hopuni': return transport(p, q, s, t, HOP[s, t] + 0.0, 'lexw', abs(U[t, s]) ** 2)


# plane waves: per-tick chain on the 8 corner parities
INC = (CORN[None, :, None] - CORN[None, None, :]) + (CORN[None, :, None] - CORN[:, None, None])


def bloch_pair(K, Ue, Uo):
    D = np.exp(1j * (CORN @ K)); return Ue, D[:, None] * Uo * D.conj()[None, :]


def band(K, Ue, Uo, which='light'):
    We, Wo = bloch_pair(K, Ue, Uo); w, V = np.linalg.eig(Wo @ We); ph = -np.angle(w)
    pos = np.sort(ph[ph > 1e-9]); tgt = pos[0] if which == 'light' else pos.max()
    return V[:, np.isclose(ph, tgt, atol=1e-7)]


def chain(a0, K, Ue, Uo, rule, T=None):
    We, Wo = bloch_pair(K, Ue, Uo); a1 = We @ a0; ks = []
    for U, x in ((We, a0), (Wo, a1)):
        J, _ = plan(U, x, rule, T); ks.append(mat(J, 8) / np.where(abs(x) ** 2 > 0, abs(x) ** 2, 1)[None, :])
    Ke, Ko = ks; return Ko @ Ke, np.einsum('ab,bc,abcx->cx', Ko, Ke, INC), Ke, Ko, abs(a0) ** 2


def classes(P, p0):
    live = p0 > 1e-14; lab = connected_components(sp.csr_matrix((P * live[None, :] * live[:, None]) > 1e-12), directed=True, connection='strong')[1]
    return [np.nonzero((lab == k) & live)[0] for k in np.unique(lab[live]) if abs(P[np.ix_(*(2 * [np.nonzero((lab == k) & live)[0]]))].sum(0) - 1).max() < 1e-9]


def streams(P, E1, p0):
    out = []
    for ix in classes(P, p0):
        Pc = P[np.ix_(ix, ix)]; w, V = np.linalg.eig(Pc); st = np.real(V[:, np.argmin(abs(w - 1))]); st = st / st.sum()
        out.append((ix, p0[ix].sum(), st @ E1[ix]))
    return out


def vg_of(K, Ue, Uo, a0):
    def om(Kp):
        We, Wo = bloch_pair(Kp, Ue, Uo); w, V = np.linalg.eig(Wo @ We); return -np.angle(w)[np.argmax(abs(V.conj().T @ a0))]
    return np.array([(om(K + 1e-6 * e) - om(K - 1e-6 * e)) / 2e-6 for e in np.eye(3)]) * 2


def asym_var(a0, K, Ue, Uo, rule, T=None):
    """exact long-time Var(x displacement)/tick for the plane-wave chain (Markov additive process); inf if reducible with distinct class speeds"""
    P, E1, Ke, Ko, p0 = chain(a0, K, Ue, Uo, rule, T); v = p0 @ E1[:, 0]; X = INC[..., 0] - v
    st = streams(P, E1, p0)
    if len(st) > 1 and max(abs(s_[2][0] - v) for s_ in st) > 1e-6: return np.inf, st
    B = np.einsum('ab,bc,abc->ac', Ko, Ke, X); E2 = np.einsum('ab,bc,abc->c', Ko, Ke, X ** 2)
    Z = np.linalg.inv(np.eye(8) - P + np.outer(p0, np.ones(8))); f = E1[:, 0] - v
    return p0 @ E2 + 2 * (f @ Z) @ B @ p0, st


def face_support(p, q, src, tgt, cost):
    """exact support of the least-cost face: one homogenised LP maximising the number of used entries"""
    keep = (p[src] > 0) & (q[tgt] > 0); src, tgt, cost = src[keep], tgt[keep], cost[keep]; n, m = p.size, src.size
    As, At = incidence(src, n, m), incidence(tgt, n, m); opt = lp(cost, sp.vstack([As, At]), np.concatenate([p, q])).fun
    Z = sp.csr_matrix((n, m)); Aeq = sp.vstack([sp.hstack([As, Z, -sp.csr_matrix(p[:, None])]), sp.hstack([At, Z, -sp.csr_matrix(q[:, None])]),
                                                 sp.hstack([sp.csr_matrix(cost[None, :]), sp.csr_matrix((1, m)), sp.csr_matrix([[-opt]])])])
    r = linprog(np.concatenate([np.zeros(m), -np.ones(m), [0.0]]), A_ub=sp.hstack([-sp.eye(m), sp.eye(m), sp.csr_matrix((m, 1))]), b_ub=np.zeros(m),
                A_eq=Aeq, b_eq=np.zeros(2 * n + 1), bounds=[(0, None)] * m + [(0, 1)] * m + [(0, 1e7)], method='highs')
    pos = r.x[m:2 * m] > 0.5; return src[pos], tgt[pos], opt

# ------------------------------------------------------------------ octree ladder (inlined from octree-actuality)
OM = np.exp(2j * np.pi / 3); I8 = np.eye(8)
CL = np.array(list(itertools.product((0, 1), repeat=3))); cc0 = CL - 0.5
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
J3 = Jm(1.5); XIL = []
for i in range(8):
    n_ = (2 * CL[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XIL.append(v_[:, -1])
WL = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(CL[a] - CL[b])) == 1: g = XIL[a].conj() @ XIL[b]; WL[a, b] = -g / abs(g) / np.sqrt(3)
def Lrot(Rm):
    n_, a = axang(Rm); Dm = expm(-1j * a * sum(n_[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = int(np.argmin(np.sum(abs(cc0 - Rm @ cc0[i]), 1))); L[k, i] = XIL[k].conj() @ Dm @ XIL[i]
    return L
def ex(th): return np.cos(th) * I8 + 1j * np.sin(th) * WL
def Dg(K): return np.diag(np.exp(1j * (CL @ K)))
def logH(U):
    w, V = np.linalg.eig(U); H = (V * (-np.angle(w))) @ np.linalg.inv(V); return (H + H.conj().T) / 2
class Tick:   # CL-1 tick: even cube exp(-i st WL), odd cube exp(+i st WL); copy mass F = exp(i M P1 WL / 2) on both sides
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
            F = s.Fc.setdefault(M, expm(1j * M * s.P1 @ WL / 2)); X = F @ X @ F
        return X
    def H(s, K, M=0.0): return logH(s.U(K, M)) / s.st
def lidx(L, x):
    x = np.mod(x, L); return int((x[0] * L + x[1]) * L + x[2])
class Ladder:
    """rung j: torus of L/2^j sites (rung-j site P at fine position 2^j P); steps E = F Ve F (even cubes, all rungs),
    O = Vo (odd cubes, all rungs), X = exp(-i kap st H5) (cell <-> its 8 children, same corner, via Xm/sqrt8)."""
    def __init__(s, L, R, st=0.04, kap=0.5, M=None, theta=(0, 0, 0), orient='L', exch=True):
        tk = Tick(st); s.tk = tk; M = st if M is None else M; Pp = (I8 + tk.g5) / 2; Pm = (I8 - tk.g5) / 2
        Xm = WL @ Pp if orient == 'L' else WL @ Pm; s.Xm = Xm
        Ls = [L >> j for j in range(R + 1)]; Ns = [l ** 3 for l in Ls]; off = np.concatenate([[0], np.cumsum(Ns)]).astype(int)
        s.L, s.R, s.Ls, s.off, s.N = L, R, Ls, off, int(off[-1]); th = np.asarray(theta, float) / L
        s.rung = np.concatenate([np.full(Ns[j], j) for j in range(R + 1)])
        pos = []
        for j in range(R + 1):
            for x in itertools.product(range(Ls[j]), repeat=3): pos.append((2 ** j) * np.array(x))
        s.pos = np.array(pos)                       # fine position of every mode (coarse site P at 2^j P)
        P1W = tk.P1 @ WL; P1W = (P1W + P1W.conj().T) / 2
        def ph(j, x0, x1):   # twist phase along the direct displacement (minimal image), fine units
            d = (np.asarray(x1) - np.asarray(x0)) * 2 ** j; return np.exp(1j * th @ d)   # unwrapped displacement inside the block
        def cubes(j, par):
            Lj = Ls[j]; out = []
            for n in itertools.product(range(Lj // 2), repeat=3):
                o = 2 * np.array(n) + par; xs = [o + cp for cp in CL]; ids = [off[j] + lidx(Lj, x) for x in xs]
                lab = [int(np.argmin(np.abs(CL - np.mod(x, 2)).sum(1))) for x in xs]; Wg = np.zeros((8, 8), complex); Pg = np.zeros((8, 8), complex)
                for i in range(8):
                    for k in range(8):
                        if np.abs(CL[i] - CL[k]).sum() == 1: Wg[i, k] = WL[lab[i], lab[k]] * ph(j, xs[k], xs[i])
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
                for ib, b in enumerate(CL):
                    P = 2 * n + b; ci = off[j + 1] + lidx(Lc, P)
                    for c in CL:
                        for ia, a in enumerate(CL):
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

def light(lad):
    U = lad.tick(); w, V = np.linalg.eig(U); om = -np.angle(w); nrm = np.sum(abs(V) ** 2, 0)
    r0 = np.array([np.sum(abs(V[lad.rung == 0, i]) ** 2) for i in range(lad.N)]) / nrm
    return om, r0, V / np.sqrt(nrm)
def light_state(lad):
    om, r0, V = light(lad); i = [k for k in np.argsort(abs(om)) if r0[k] > 0.9][0]; return V[:, i], 1 - r0[i], om[i]
QD = np.array([.3, .5, .81]) / np.linalg.norm([.3, .5, .81])
LADS = {}
def lad_at(R, qs):
    k = (R, qs)
    if k not in LADS: LADS[k] = Ladder(8, R, theta=8 * qs * QD)
    return LADS[k]

# ================================================================== helpers for the sections
def kern(J, n): return mat(J, n)
def gap(P): w = np.sort(abs(np.linalg.eigvals(P)))[::-1]; return 1 - w[1]
def longmass(K8, p): return (K8 * p[None, :])[HOP >= 2].sum()
PARS = ((np.pi / 2, 0.3, 0.3), (0.3, 0.1, 0.1), (0.04, 0.01, 0.04))
KS = [2 * np.pi * np.array(m) / 8 for m in ((1, 0, 0), (1, 1, 0), (2, 1, 0), (3, 1, 0), (1, 2, 3), (0.25, 0, 0))]
def pols(Ue, Uo, K, k=4):
    Vb = band(K, Ue, Uo); out = []
    for _ in range(k): a = Vb @ rstate(Vb.shape[1]); out.append(a / np.linalg.norm(a))
    return out
def tor(X, Ls, s, t):
    Ls = np.asarray(Ls); d = (X[t] - X[s] + Ls // 2) % Ls - Ls // 2; return np.abs(d).sum(-1)
def lat_plan(U, psi, rule, X, Ls, T=None):
    new = U @ psi; p, q = abs(psi) ** 2, abs(new) ** 2; t, s = U.nonzero(); h = tor(X, Ls, s, t) + 0.0
    if rule == 'modes': J, e = transport(p, q, s, t, 2.0 * (s != t), 'lex')
    elif rule == 'hop2': J, e = transport(p, q, s, t, h ** 2, 'lex')
    elif rule == 'ehop2': J, e = transport(p, q, s, t, None, 'prior', np.exp(-h ** 2 / T))
    else: J, e = transport(p, q, s, t, None, 'prior', abs(np.asarray(U[t, s]).ravel()) ** 2)
    return J, e, p, q, new
def chi2(cfg, P, Mr):
    f = np.bincount(cfg, minlength=P.size); e = Mr * P; k = e >= 5; return ((f[k] - e[k]) ** 2 / e[k]).sum() / (k.sum() - 1)


# ================================================================== A
def section_A():
    print('A. the CL-1 cube tick and the hop count')
    s = S_COPY; Ue, Uo = cube_even(0.3, 0.1, 0.1), cube_odd(0.3, 0.1); U0 = cube_even(0.3, 0.1, 0.0)
    reach = lambda U: sorted(set(HOP[abs(U) > TOL].tolist()))
    check('A1 copy sign s = i R1R2R3R: s = s^+, s^2 = 1, [s,R] = 0, face diagonals only; with the copy mass the even half-tick reaches all corners',
          abs(s - s.conj().T).max() < 1e-14 and abs(s @ s - np.eye(8)).max() < 1e-14 and abs(s @ W0 - W0 @ s).max() < 1e-14 and reach(s) == [2]
          and reach(Ue) == [0, 1, 2, 3] and reach(Uo) == [0, 1] and reach(U0) == [0, 1], f'hops reached: even {reach(Ue)}, odd {reach(Uo)}, M=0 {reach(U0)}')
    dmax = 0; same = 0; tot = 0
    for eps, mu in ((np.pi / 2, 0.3), (0.3, 0.1)):
        Ue, Uo = cube_even(eps, mu, 0.0), cube_odd(eps, mu)
        for K in KS[:4]:
            for a0 in pols(Ue, Uo, K, 3):
                ch = {r: chain(a0, K, Ue, Uo, r) for r in ('modes', 'hop', 'hop2')}
                dmax = max(dmax, max(abs(ch[r][2] - ch['modes'][2]).max() + abs(ch[r][3] - ch['modes'][3]).max() for r in ('hop', 'hop2')))
                n = [len(streams(ch[r][0], ch[r][1], ch[r][4])) for r in ('modes', 'hop', 'hop2')]; same += n[0] == n[1] == n[2]; tot += 1
    check('A2 THEOREM: with M = 0 every one-relay move is a stay or one hop, so hops = modes/2 and the hop rules ARE the registered rule',
          dmax < 1e-8 and same == tot, f'max plan difference {dmax:.0e}; same streams {same}/{tot}')
    Ls = (16, 4, 4); Ue, Uo = cube_even(np.pi / 2, 0.3, 0.3), cube_odd(np.pi / 2, 0.3); UeL, X = lattice_half(Ls, Ue, False); UoL, _ = lattice_half(Ls, Uo, True)
    N = X.shape[0]; psi = np.exp(-((X[:, 0] - 8) ** 2) / 8.0) * np.exp(0.8j * X[:, 0]) * (1 + 0.3 * rstate(N)); psi /= np.linalg.norm(psi)
    Mr = 20000; cfg = rng.choice(N, Mr, p=abs(psi) ** 2); rho = abs(psi) ** 2; err = 0; feas = True
    for h in range(12):
        J, e, p, q, psi = lat_plan(UoL if h % 2 else UeL, psi, 'hop2', X, Ls)
        if J is None: feas = False; break
        rho = push(rho, J, p); err = max(err, abs(rho - q).max()); cfg = sample(cfg, J, N)
    check('A3 THEOREM: the cost never enters the feasible set, so existence is unchanged; hop^2 keeps the odds',
          feas and err < 1e-12 and chi2(cfg, abs(psi) ** 2, Mr) < 1.3, f'16x4x4, 12 half-ticks: feasible {feas}, max |rho - |psi|^2| {err:.0e}, 20000 samples chi2/dof {chi2(cfg, abs(psi) ** 2, Mr):.2f}')


# ================================================================== B
def pair_tools(Ls, U, odd):
    X = np.array(list(itertools.product(*[range(l) for l in Ls]))); N = X.shape[0]; par = X % 2; Lsa = np.array(Ls)
    org = ((X - par) if not odd else (X - (1 - par))) % Lsa; blk = (org[:, 0] * Ls[1] + org[:, 1]) * Ls[2] + org[:, 2]
    I, Jx = np.triu_indices(N, 1); pid = np.zeros((N, N), int); pid[I, Jx] = pid[Jx, I] = np.arange(I.size)
    d = lambda a, b: np.abs((X[a] - X[b] + Lsa // 2) % Lsa - Lsa // 2).sum()
    nb = [np.nonzero(abs(U[:, x]) > TOL)[0] for x in range(N)]; rows = []
    for k in range(I.size):
        x1, x2 = I[k], Jx[k]
        for y1, y2 in itertools.combinations(np.union1d(nb[x1], nb[x2]), 2):
            a = U[y1, x1] * U[y2, x2] - U[y1, x2] * U[y2, x1]
            if abs(a) <= TOL: continue
            m1, m2 = (d(x1, y1), d(x2, y2)), (d(x1, y2), d(x2, y1))
            if blk[x1] != blk[x2]: mb = m1 if blk[y1] == blk[x1] else m2
            else: mb = min(m1, m2, key=lambda m: m[0] ** 2 + m[1] ** 2)
            mg = min(m1, m2, key=lambda m: m[0] ** 2 + m[1] ** 2)
            rows.append((k, pid[y1, y2], abs(a) ** 2, mb[0] ** 2 + mb[1] ** 2, mg[0] ** 2 + mg[1] ** 2, mb[0] + mb[1], len({x1, x2} ^ {y1, y2})))
    R = np.array(rows); return X, I, Jx, R, blk


def section_B():
    print('B. properties of the hop-weighted rules (hop = W1, hop^2 = W2 on the hop metric; counted per block and species)')
    Ue = cube_even(np.pi / 2, 0.3, 0.3); s, t = edges(Ue); rel = 0; uniq = 0
    for _ in range(20):
        a = rstate(8); p, q = abs(a) ** 2, abs(Ue @ a) ** 2; pi = rng.permutation(8); inv = np.argsort(pi); eo = rng.permutation(s.size)
        for c in (HOP[s, t] + 0.0, HOP[s, t] ** 2 + 0.0):
            M1 = mat(transport(p, q, s, t, c, 'lex')[0], 8); M2 = mat(transport(p[inv], q[inv], pi[s][eo], pi[t][eo], c[eo], 'lex')[0], 8)[np.ix_(pi, pi)]
            rel = max(rel, abs(M1 - M2).max())
    check('B1 one plan, independent of labels and edge order', rel < 1e-10, f'relabel/reorder difference {rel:.0e} (20 states x 2 costs)')
    # separability: distinguishable relays (two species, each on its own cube), additive cost
    se = 0
    for _ in range(6):
        UA, UB = cube_even(0.3, 0.1, 0.1), cube_even(0.6, 0.2, 0.2); a, b = rstate(8), rstate(8); UU = np.kron(UA, UB)
        sA, tA = edges(UA); s2, t2 = edges(UU); hA = HOP[s2 // 8, t2 // 8]; hB = HOP[s2 % 8, t2 % 8]
        JA = mat(transport(abs(a) ** 2, abs(UA @ a) ** 2, sA, tA, HOP[sA, tA] ** 2 + 0.0, 'lex')[0], 8)
        J = mat(transport(abs(np.kron(a, b)) ** 2, abs(UU @ np.kron(a, b)) ** 2, s2, t2, hA ** 2 + hB ** 2 + 0.0, 'lex')[0], 64)
        se = max(se, abs(J.reshape(8, 8, 8, 8).sum((1, 3)) - JA).max())
    check('B2 THEOREM: a cost additive over species and blocks gives unentangled relays the product plan',
          se < 1e-9, f'A-plan shift by unentangled B (two species, copy-massed cubes, hop^2) {se:.0e}')
    # same species in adjacent blocks: blockwise vs global matching
    Ls = (4, 4, 4); Ue = cube_even(np.pi / 2, 0.3, 0.6); UeL, X = lattice_half(Ls, Ue, False); UeL = UeL.toarray()
    X, I, Jx, R, blk = pair_tools(Ls, UeL, False); N = X.shape[0]; bA = blk[0]; bB = blk[np.nonzero((X == [2, 0, 0]).all(1))[0][0]]
    f = np.where(blk == bA, rstate(N), 0); g = np.where(blk == bB, rstate(N), 0); f /= np.linalg.norm(f); g /= np.linalg.norm(g)
    Psi = np.outer(f, g) - np.outer(g, f); Psi /= np.linalg.norm(Psi); odds = lambda P: 2 * abs(P[I, Jx]) ** 2; New = UeL @ Psi @ UeL.T
    p, q = odds(Psi), odds(New); src, tgt = R[:, 0].astype(int), R[:, 1].astype(int); sA, tA = edges(UeL)
    hf = tor(X, Ls, sA, tA) + 0.0; Jf = mat(transport(abs(f) ** 2, abs(UeL @ f) ** 2, sA, tA, hf ** 2, 'lex')[0], N)
    def amarg(J):
        Mx = np.zeros((N, N)); k, k2, w = J; x1, x2, y1, y2 = I[k], Jx[k], I[k2], Jx[k2]
        xa = np.where(blk[x1] == bA, x1, x2); ya = np.where(blk[y1] == bA, y1, y2); np.add.at(Mx, (ya, xa), w); return Mx
    dev = {nm: abs(amarg(transport(p, q, src, tgt, R[:, col], 'lex')[0]) - Jf).max() for nm, col in (('blockwise', 3), ('global', 4))}
    cheaper = np.mean(R[:, 4] < R[:, 3])
    check('B3 FINDING: hops must be counted per block; a global matching couples unentangled relays in neighbouring cubes',
          dev['blockwise'] < 1e-9 and dev['global'] > 1e-4, f'A-plan shift by B: blockwise {dev["blockwise"]:.0e}, global {dev["global"]:.1e}; global matching cheaper on {cheaper:.2f} of pair moves')
    # two entangled relays on the copy-massed lattice under hop^2 (blockwise), plus the W1 vs modes/2 count
    Uo = cube_odd(np.pi / 2, 0.3); UoL, _ = lattice_half(Ls, Uo, True); UoL = UoL.toarray(); Ro = pair_tools(Ls, UoL, True)[3]
    ff = [rstate(N) for _ in range(4)]; Psi = np.outer(ff[0], ff[1]) - np.outer(ff[1], ff[0]) + 0.8 * (np.outer(ff[2], ff[3]) - np.outer(ff[3], ff[2])); Psi /= np.linalg.norm(Psi)
    Mr = 20000; rho = odds(Psi); cfg = rng.choice(I.size, Mr, p=rho / rho.sum()); err = 0
    for h in range(4):
        U, RR = (UoL, Ro) if h % 2 else (UeL, R); New = U @ Psi @ U.T; p, q = odds(Psi), odds(New)
        J, _ = transport(p, q, RR[:, 0].astype(int), RR[:, 1].astype(int), RR[:, 3], 'lex'); rho = push(rho, J, p); err = max(err, 0.5 * abs(rho - q).sum()); cfg = sample(cfg, J, I.size); Psi = New
    push_ = np.mean(R[:, 5] != R[:, 6] / 2)
    check('B4 two entangled fermion relays on 4^3 (2016 pairs, copy mass): joint odds kept; hops != modes/2 on push chains',
          err < 1e-10 and chi2(cfg, odds(Psi), Mr) < 1.3 and push_ > 0, f'max TV {err:.0e}, chi2/dof {chi2(cfg, odds(Psi), Mr):.2f}; hop != modes/2 on {push_:.2f} of allowed pair moves')
    # stationary states, CHSH and readers
    jz = {}
    for r, T in (('modes', None), ('hop', None), ('hop2', None), ('ehop2', 0.1), ('uni', None)):
        w_, V_ = np.linalg.eig(Ue); e = V_[:, 0] / np.linalg.norm(V_[:, 0]); jz[r] = 1 - np.trace(mat(plan(Ue, e, r, T)[0], 8))
    check('B5 stationary states frozen under least-cost rules, not entropic ones', max(jz['modes'], jz['hop'], jz['hop2']) < 1e-12 and jz['ehop2'] > 0,
          'jump rate on an eigenstate: ' + ', '.join(f'{k} {v:.1e}' for k, v in jz.items()))
    # CHSH: two cubes, each relay on its body diagonal (corners 0, 7, three hops), Bell state, supplied rotations
    def rot(a):
        G = np.zeros((8, 8), complex); G[0, 7] = G[7, 0] = 1; return expm(-1j * a * G)
    psi0 = np.zeros(64, complex); psi0[0 * 8 + 0] = psi0[7 * 8 + 7] = 1 / np.sqrt(2); E = {}; Mr = 40000
    for a, b in ((0, -np.pi / 8), (0, -3 * np.pi / 8), (np.pi / 4, -np.pi / 8), (np.pi / 4, -3 * np.pi / 8)):
        UU = np.kron(rot(a), rot(b)); s2, t2 = edges(UU); h2 = HOP[s2 // 8, t2 // 8] ** 2 + HOP[s2 % 8, t2 % 8] ** 2 + 0.0
        J, _ = transport(abs(psi0) ** 2, abs(UU @ psi0) ** 2, s2, t2, h2, 'lex'); c = sample(rng.choice(64, Mr, p=abs(psi0) ** 2), J, 64)
        sa, sb = np.where(c // 8 == 0, 1, -1), np.where(c % 8 == 0, 1, -1); E[(a, b)] = (sa * sb).mean()
    S = abs(E[(0, -np.pi / 8)] - E[(0, -3 * np.pi / 8)] + E[(np.pi / 4, -np.pi / 8)] + E[(np.pi / 4, -3 * np.pi / 8)])
    # readers: system relay on corners 0/7 of a cube, two pointers on 3-site lines; controlled shifts; later system-only rotation
    sh = np.roll(np.eye(3), 1, 0); I3 = np.eye(3); P0 = np.zeros((8, 8)); P0[np.arange(8) != 7, np.arange(8) != 7] = 1; P7 = np.eye(8) - P0
    steps = [np.kron(expm(-1j * np.arcsin(np.sqrt(0.3)) * (np.eye(8)[[7]].T @ np.eye(8)[[0]] + np.eye(8)[[0]].T @ np.eye(8)[[7]])), np.eye(9)),
             np.kron(P0, np.eye(9)) + np.kron(P7, np.kron(sh, I3)), np.kron(P0, np.eye(9)) + np.kron(P7, np.kron(I3, sh)), np.kron(rot(1.1), np.eye(9))]
    cs = np.arange(72); hp = lambda a_, b_: (HOP[a_ // 9, b_ // 9] + abs((a_ % 9) // 3 - (b_ % 9) // 3) + abs(a_ % 3 - b_ % 3)) ** 2
    psi = np.zeros(72, complex); psi[0] = 1; cfg = np.zeros(40000, int); moved = 0
    for k, U in enumerate(steps):
        s_, t_ = edges(U); J = transport(abs(psi) ** 2, abs(U @ psi) ** 2, s_, t_, hp(s_, t_) + 0.0, 'lex')[0]; nc = sample(cfg, J, 72)
        if k == 3: moved = int(((nc % 9) != (cfg % 9)).sum())
        cfg = nc; psi = U @ psi
    p1, p2 = (cfg % 9) // 3, cfg % 3
    check('B6 THEOREM (hop^2): joint-configuration outcomes are Born: quantum CHSH, readers agree, system-only steps never move pointers',
          abs(S - 2 * np.sqrt(2)) < 0.04 and (p1 != p2).sum() == 0 and abs((p1 == 1).mean() - 0.3) < 0.01 and moved == 0,
          f'CHSH {S:.3f} (exact 2.828); reader disagreements {(p1 != p2).sum()}, P(read) {(p1 == 1).mean():.4f} vs 0.3; pointer moves {moved}')


# ================================================================== C, D, E (plane waves)
RULES = (('modes', None), ('hop', None), ('hop2', None), ('short', None), ('ehop2', 0.1), ('uni', None))
def sweep():
    out = {}
    for pr in PARS:
        Ue, Uo = cube_even(*pr), cube_odd(pr[0], pr[1]); st_ = {r: [0, 0, 1.0, 0.0] for r in RULES}; fl = 0
        for K in KS:
            for a0 in pols(Ue, Uo, K):
                s, t = edges(Ue); p, q = abs(a0) ** 2, abs(Ue @ a0) ** 2; Jf, _ = transport(p, q, s, t, (HOP[s, t] >= 2) + 0.0, 'lp'); fl = max(fl, Jf[2][HOP[Jf[0], Jf[1]] >= 2].sum())
                for r in RULES:
                    P, E1, Ke, Ko, p0 = chain(a0, K, Ue, Uo, *r); v = st_[r]; v[0] += 1; v[1] += len(streams(P, E1, p0)) > 1; v[2] = min(v[2], gap(P)); v[3] = max(v[3], longmass(Ke, p0))
        out[pr] = (st_, fl)
    return out


def section_C(SW):
    print('C. relay streams on plane waves of the CL-1 tick with the copy mass (8 corner parities, exact per-tick chain)')
    rows = {r: [sum(SW[pr][0][r][1] for pr in PARS), sum(SW[pr][0][r][0] for pr in PARS)] for r in RULES}
    check('C1 FINDING: with the copy mass the registered rule has no closed streams; hop and hop^2 bring them back',
          rows[('modes', None)][0] == 0 and rows[('hop2', None)][0] > 10 and rows[('hop', None)][0] > 10 and rows[('short', None)][0] == 0,
          'split of ' + str(rows[('modes', None)][1]) + ': ' + ', '.join(f'{r[0]}{r[1] or ""} {v[0]}' for r, v in rows.items()))
    Ue, Uo = cube_even(*PARS[0]), cube_odd(*PARS[0][:2]); K0 = np.array([np.pi / 2, 0, 0]); best = None
    for a0 in pols(Ue, Uo, K0, 20):
        st = streams(*[chain(a0, K0, Ue, Uo, 'hop2')[i] for i in (0, 1, 4)])
        if best is None or len(st) > len(best[1]): best = (a0, st)
    CHI, st = best; vg = vg_of(K0, Ue, Uo, CHI)[0]; We, Wo = bloch_pair(K0, Ue, Uo); a1 = We @ CHI; sup = []
    for U, x in ((We, CHI), (Wo, a1)):
        s, t = edges(U); p, q = abs(x) ** 2, abs(U @ x) ** 2; fs, ft, _ = face_support(p, q, s, t, HOP[s, t] ** 2 + 0.0); S_ = np.zeros((8, 8)); S_[ft, fs] = 1; sup.append(S_)
    Pp = (sup[1] @ sup[0]) > 0; lab = connected_components(sp.csr_matrix(Pp), directed=True, connection='strong')[1]
    nface = sum(1 for k in np.unique(lab) if not Pp[np.ix_(lab != k, lab == k)].any()); gs = {}
    for T in (0.3, 0.2, 0.1):
        P = chain(CHI, K0, Ue, Uo, 'modese2', T)[0]; gs[T] = gap(P)
    check('C2 THEOREM: streams = classes of the least-cost face, no tie-break joins them; in the registered face the long moves join them',
          nface == len(st) and gs[0.1] < 1e-10 < gs[0.3], f'hop^2 face classes {nface} = streams {len(st)} (' + ', '.join(f'w {w:.2f} v {v[0]:.3f}' for _, w, v in st) + f' vs v_g {vg:.3f}); registered-face mixing gap at T = 0.3, 0.2, 0.1: ' + ' '.join(f'{g:.0e}' for g in gs.values()))
    Dd = {}
    for r, T in (('modes', None), ('hop2', None), ('ehop2', 0.2), ('ehop2', 0.1), ('uni', None)):
        D, st_ = asym_var(CHI, K0, Ue, Uo, r, T); Dd[(r, T)] = (D, gap(chain(CHI, K0, Ue, Uo, r, T)[0]))
    check('C3 plane-wave asymptotics: irreducible -> one speed v_g, variance D/T; reducible -> spread forever',
          np.isinf(Dd[('hop2', None)][0]) and all(np.isfinite(Dd[k][0]) for k in Dd if k[0] != 'hop2'), 'D site^2/tick (gap): ' + ', '.join(f'{k[0]}{k[1] or ""} {v[0]:.1f} ({v[1]:.0e})' for k, v in Dd.items()))
    return CHI, Ue, Uo, K0


def section_C_packets(CHI, Ue, Uo, K0):
    Ls = (128, 4, 4); NB = np.array(Ls) // 2; X = np.array(list(itertools.product(*[range(l) for l in Ls]))); par = X % 2; n = (X - par) // 2; pidx = par @ [4, 2, 1]
    kx = 2 * np.pi * np.fft.fftfreq(NB[0]); d = (kx - K0[0] + np.pi) % (2 * np.pi) - np.pi; g = np.exp(-d ** 2 * 64); psi0 = np.zeros(X.shape[0], complex); ks = []
    for k_, g_ in zip(kx, g):
        if g_ < 1e-8: continue
        Q, _ = np.linalg.qr(band(np.array([k_, 0, 0]), Ue, Uo)); ph = Q @ (Q.conj().T @ CHI); ph /= np.linalg.norm(ph); psi0 += g_ * np.exp(1j * (n[:, 0] - NB[0] / 2) * k_) * ph[pidx]; ks.append((k_, g_))
    psi0 /= np.linalg.norm(psi0); ks = np.array(ks); N = X.shape[0]; UeL, _ = lattice_half(Ls, Ue, False); UoL, _ = lattice_half(Ls, Uo, True)
    vk = np.array([vg_of(np.array([k, 0, 0]), Ue, Uo, CHI)[0] for k in ks[:, 0]]); wk = ks[:, 1] ** 2 / (ks[:, 1] ** 2).sum(); svg = np.sqrt(wk @ (vk - wk @ vk) ** 2)
    res = {}
    for r, T in (('modes', None), ('hop2', None), ('uni', None)):
        psi = psi0.copy(); cfg = rng.choice(N, 3000, p=abs(psi) ** 2); x = np.zeros(3000); xs = [x.copy()]; lab0 = X[cfg, 1] % 2 * 2 + X[cfg, 2] % 2; err = 0; rho = abs(psi) ** 2
        for h in range(80):
            J, e, p, q, psi = lat_plan(UoL if h % 2 else UeL, psi, r, X, Ls, T); rho = push(rho, J, p); err = max(err, abs(rho - q).max()); nc = sample(cfg, J, N)
            x = x + ((X[nc, 0] - X[cfg, 0] + Ls[0] // 2) % Ls[0] - Ls[0] // 2); cfg = nc
            if h % 2: xs.append(x.copy())
        v = x / 40; res[r] = (v.mean(), v.std(), np.ptp([v[lab0 == j].mean() for j in range(4)]), err)
    check('C4 DIAGNOSTIC packets (40 ticks): track speeds scatter by the zigzag sqrt(D/T) >> momentum spread; hop^2 keeps label-dependent speeds',
          all(v[3] < 1e-12 for v in res.values()) and all(v[1] > 5 * svg for v in res.values()),
          f'momentum spread of v_g {svg:.3f}; ' + '; '.join(f'{r}: v {v[0]:.3f} +- {v[1]:.3f}, label spread {v[2]:.2f}' for r, v in res.items()))


def section_D(SW):
    print('D. long jumps (two or more hops in one half-tick; plane waves never need them: Born floor below)')
    fl = max(SW[pr][1] for pr in PARS)
    row = lambda r: ' '.join(f'{SW[pr][0][r][3]:.0e}' for pr in PARS)
    check('D1 FINDING: long jumps per half-tick: registered rule 1e-2..0.3, hop less, hop^2 at the Born floor',
          fl < 1e-12 and min(SW[pr][0][('modes', None)][3] for pr in PARS) > 5e-3 and max(SW[pr][0][('hop2', None)][3] for pr in PARS) < 1e-12,
          f'max at (eps,mu,M) = ' + ', '.join(f'({a:.2f},{b},{c})' for a, b, c in PARS) + f': floor {fl:.0e}; modes {row(("modes", None))}; hop {row(("hop", None))}; hop^2 {row(("hop2", None))}; uni {row(("uni", None))}')
    Ue, Uo = cube_even(*PARS[0]), cube_odd(*PARS[0][:2]); K = KS[1]; worst = (0, 0)
    for a0 in pols(Ue, Uo, K, 6):
        s, t = edges(Ue); p, q = abs(a0) ** 2, abs(Ue @ a0) ** 2; c = HOP[s, t] + 0.0; J, _ = transport(p, q, s, t, c, 'lex'); opt = (J[2] * HOP[J[0], J[1]]).sum()
        lng = (HOP[s, t] >= 2) + 0.0; kp = (p[s] > 0) & (q[t] > 0)
        r = linprog(lng[kp], A_eq=sp.vstack([incidence(s[kp], 8, kp.sum()), incidence(t[kp], 8, kp.sum())]), b_eq=np.concatenate([p, q]), A_ub=c[kp][None, :], b_ub=[opt * (1 + 1e-9)], bounds=(0, None), method='highs')
        me = J[2][HOP[J[0], J[1]] >= 2].sum()
        if me > worst[0]: worst = (me, r.fun)
    check('D2 THEOREM: hop counts tie a 2-hop jump with two 1-hop moves, so entropy still spreads long jumps; squaring breaks the tie',
          worst[0] > 1e-3 and worst[1] < 1e-9, f'hop face: greatest entropy {worst[0]:.2e} vs least long mass on the same face {worst[1]:.0e}')
    res = {}
    for qs in (0.1, 0.03):
        lad = lad_at(1, qs); S, cw, _ = light_state(lad); x = lad.E @ S; Us = (lad.X @ lad.O).tocsr(); t_, s_ = Us.nonzero(); p, q = abs(x) ** 2, abs(Us @ x) ** 2
        dd = (lad.pos[t_] - lad.pos[s_] + 4) % 8 - 4; lng = (lad.rung[s_] != lad.rung[t_]) | (np.abs(dd).max(-1) >= 2); h = np.where(s_ != t_, np.maximum(1, np.abs(dd).sum(-1)), 0) + 0.0
        def lm(J): kk = np.isin(J[0] * lad.N + J[1], s_[lng] * lad.N + t_[lng]); return J[2][kk].sum()
        Jm_, _ = transport(p, q, s_, t_, (s_ != t_) + 0.0, 'lex'); mv = Jm_[2][Jm_[0] != Jm_[1]].sum(); kp = (p[s_] > 1e-20) & (q[t_] > 1e-20)
        r = linprog(lng[kp] + 0.0, A_eq=sp.vstack([incidence(s_[kp], lad.N, kp.sum()), incidence(t_[kp], lad.N, kp.sum())]).tocsr(), b_eq=np.concatenate([np.where(p > 1e-20, p, 0), np.where(q > 1e-20, q, 0)]),
                    A_ub=sp.csr_matrix((s_[kp] != t_[kp])[None, :] + 0.0), b_ub=[mv * (1 + 1e-9) + 1e-15], bounds=(0, None), method='highs')
        res[qs] = (lm(Jm_), lm(transport(p, q, s_, t_, h ** 2, 'lex')[0]), lm(transport(p, q, s_, t_, None, 'prior', abs(np.asarray(Us[t_, s_]).ravel()) ** 2)[0]), r.fun, cw)
    ex_ = np.log(res[0.1][1] / res[0.03][1]) / np.log(0.1 / 0.03); exc = np.log(res[0.1][4] / res[0.03][4]) / np.log(0.1 / 0.03)
    check(f'D3 octree ladder (R = 1, exchange in the odd half-tick; octree-actuality C2/C3): hop^2 cuts long or rung-changing moves 1e3-fold or more and they then fall as |q|^{ex_:.1f}, like the coarse Born weight (|q|^{exc:.1f})',
          all(v[0] > 100 * v[1] for v in res.values()) and res[0.1][1] < 3 * res[0.1][3] and abs(ex_ - exc) < 1,
          '; '.join(f'|q| {k}: modes {v[0]:.1e}, hop^2 {v[1]:.1e}, uni {v[2]:.1e}, floor {v[3]:.1e}, coarse Born {v[4]:.0e}' for k, v in res.items()))


def section_E(SW, CHI, Ue, Uo, K0):
    print('E. entropic transport: least (mean hop^2 - T x entropy), J_ts = a_s exp(-h_ts^2/T) b_t')
    We, _ = bloch_pair(K0, Ue, Uo); s, t = edges(We); p, q = abs(CHI) ** 2, abs(We @ CHI) ** 2; J0 = mat(transport(p, q, s, t, HOP[s, t] ** 2 + 0.0, 'lex')[0], 8)
    dT = [abs(mat(transport(p, q, s, t, None, 'prior', np.exp(-HOP[s, t] ** 2 / T))[0], 8) - J0).max() for T in (0.2, 0.1, 0.05)]
    Jinf = abs(mat(transport(p, q, s, t, None, 'prior', np.exp(-HOP[s, t] ** 2 / 1e6))[0], 8) - mat(transport(p, q, s, t, None, 'maxent')[0], 8)).max()
    check('E1 THEOREM: T -> 0 gives hop^2, T -> inf greatest entropy', dT[2] < dT[1] < dT[0] and Jinf < 1e-6,
          'plan distance to hop^2 at T = 0.2, 0.1, 0.05: ' + ' '.join(f'{x:.0e}' for x in dT) + f'; to greatest entropy at T = 1e6: {Jinf:.0e}')
    rows = []
    for T in (0.25, 0.15, 0.1):
        P = chain(CHI, K0, Ue, Uo, 'ehop2', T)[0]; w_, V_ = np.linalg.eig(Ue); e = V_[:, 0] / np.linalg.norm(V_[:, 0]); jt = 1 - np.trace(mat(plan(Ue, e, 'ehop2', T)[0], 8)); rows.append((T, gap(P), jt))
    tot = sum(SW[pr][0][('ehop2', 0.1)][1] for pr in PARS)
    check('E2 FINDING: T > 0: no streams; stream mixing rate = stationary jitter ~ 3exp(-1/T)',
          tot == 0 and all(0.05 < g / j < 20 for _, g, j in rows), f'split {tot}/72 at T = 0.1; (T, gap, eigenstate jump): ' + ' '.join(f'({T}, {g:.0e}, {j:.0e})' for T, g, j in rows) + f'; 3 exp(-1/T) at 0.1 = {3 * np.exp(-10):.0e}')
    tot = sum(SW[pr][0][('uni', None)][1] for pr in PARS)
    check('E3 kernel |<t|U|s>|^2 (cost -log|U|^2, T = 1, no constant): no streams, but long jumps above the floor and jitter',
          tot == 0, f'split {tot}/72; long mass per half-tick ' + ' '.join(f'{SW[pr][0][("uni", None)][3]:.0e}' for pr in PARS) + ' (floor 0)')


# ================================================================== F
def section_F():
    print('F. measured tracks are pointer records')
    Ue, Uo = cube_even(np.pi / 2, 0.3, 0.0), cube_odd(np.pi / 2, 0.3); K0 = np.array([np.pi / 2, 0, 0]); best = None
    for a0 in pols(Ue, Uo, K0, 20):
        st = streams(*[chain(a0, K0, Ue, Uo, 'modes')[i] for i in (0, 1, 4)])
        if best is None or len(st) > len(best[1]): best = (a0, st)
    CHI, st = best; Ls = (64, 4, 4); NB = np.array(Ls) // 2; X = np.array(list(itertools.product(*[range(l) for l in Ls]))); par = X % 2; n = (X - par) // 2; pidx = par @ [4, 2, 1]
    kx = 2 * np.pi * np.fft.fftfreq(NB[0]); d = (kx - K0[0] + np.pi) % (2 * np.pi) - np.pi; g = np.exp(-d ** 2 * 36); psi = np.zeros(X.shape[0], complex)
    for k_, g_ in zip(kx, g):
        if g_ < 1e-8: continue
        Q, _ = np.linalg.qr(band(np.array([k_, 0, 0]), Ue, Uo)); ph = Q @ (Q.conj().T @ CHI); ph /= np.linalg.norm(ph); psi += g_ * np.exp(1j * (n[:, 0] - NB[0] / 2) * k_) * ph[pidx]
    psi /= np.linalg.norm(psi); N = X.shape[0]; UeL, _ = lattice_half(Ls, Ue, False); UoL, _ = lattice_half(Ls, Uo, True); I4 = sp.identity(4, format='csr')
    def flip(slab, bit):
        m = np.isin(X[:, 0], slab).astype(float); Fk = sp.kron(np.array([[0, 1], [1, 0]]), sp.identity(2)) if bit == 0 else sp.kron(sp.identity(2), np.array([[0, 1], [1, 0]]))
        return (sp.kron(sp.diags(1 - m), I4) + sp.kron(sp.diags(m), Fk)).tocsr()
    x0 = X[np.argmax(abs(psi)), 0]; H1, H2 = 8, 28; sl1 = np.arange(x0 + 6, x0 + 12) % Ls[0]; sl2 = np.arange(x0 + 14, x0 + 20) % Ls[0]; Mr = 40000; out = {}
    for rule in ('modes', 'uni'):
        Phi = np.kron(psi, np.array([1, 0, 0, 0], complex)); cfg = rng.choice(4 * N, Mr, p=abs(Phi) ** 2); ps = psi.copy(); c = rng.choice(N, Mr, p=abs(ps) ** 2)
        for h in range(36):
            ops = [sp.kron(UoL if h % 2 else UeL, I4).tocsr()] + ([flip(sl1, 0)] if h == H1 else []) + ([flip(sl2, 1)] if h == H2 else [])
            for U in ops:
                new = U @ Phi; t, s = U.nonzero(); p, q = abs(Phi) ** 2, abs(new) ** 2
                J = transport(p, q, s, t, 2.0 * (s != t), 'lex')[0] if rule == 'modes' else transport(p, q, s, t, None, 'prior', abs(np.asarray(U[t, s]).ravel()) ** 2)[0]
                cfg = sample(cfg, J, 4 * N); Phi = new
            U = UoL if h % 2 else UeL; new = U @ ps; t, s = U.nonzero(); p, q = abs(ps) ** 2, abs(new) ** 2
            J = transport(p, q, s, t, 2.0 * (s != t), 'lex')[0] if rule == 'modes' else transport(p, q, s, t, None, 'prior', abs(np.asarray(U[t, s]).ravel()) ** 2)[0]
            c = sample(c, J, N); ps = new
            if h == H1: in1 = np.isin(X[c, 0], sl1)
            if h == H2: in2 = np.isin(X[c, 0], sl2)
        P4 = (abs(Phi) ** 2).reshape(N, 4).sum(0); out[rule] = (P4[3], (cfg % 4 == 3).mean(), (in1 & in2).mean())
    se = np.sqrt(out['modes'][0] * (1 - out['modes'][0]) / Mr)
    check('F1 THEOREM: pointer records persist and the joint configuration is Born, so recorded tracks are quantum under every rule; only unread relay records differ',
          all(abs(v[1] - v[0]) < 4 * se for v in out.values()) and abs(out['modes'][2] - out['modes'][0]) > 10 * se,
          f'{len(st)} streams (M = 0); two-bubble coincidence: Born {out["modes"][0]:.4f}; pointers modes {out["modes"][1]:.4f}, uni {out["uni"][1]:.4f}; relay own records modes {out["modes"][2]:.4f}, uni {out["uni"][2]:.4f}')


if __name__ == '__main__':
    section_A(); print(f'      [{time.time() - T0:.0f} s]')
    section_B(); print(f'      [{time.time() - T0:.0f} s]')
    SW = sweep(); CHI, Ue, Uo, K0 = section_C(SW); section_C_packets(CHI, Ue, Uo, K0); print(f'      [{time.time() - T0:.0f} s]')
    section_D(SW); print(f'      [{time.time() - T0:.0f} s]')
    section_E(SW, CHI, Ue, Uo, K0); section_F(); print(f'      [{time.time() - T0:.0f} s]')
    print('supplied: configuration space; the half-tick as the step; hop metric (taxicab, per block and species); the power 2; T; states, packets, settings, pointer gates.')
    print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
