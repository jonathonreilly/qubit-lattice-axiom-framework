#!/usr/bin/env python3
"""bell-records: CL-2's record statistics for constant records, a two-path interferometer and a CHSH test
(supplied models; finite diagnostics; no physical identification).

CL-2 as registered: one actual configuration distributed as its odds; each half-tick it moves by the transport that
keeps it so, along nonzero elements of the half-tick only, with the fewest changed mode occupations on average and,
of those, greatest entropy; every matter mode's occupation is then recorded. Records never condition the odds.

Model: one fermion per disjoint set of modes (a 'register'); within a set the hop has no Jordan-Wigner string, so the
occupation configurations are exactly the tuples of positions, and one changed position = two changed occupations.
A. constant records versus Zeno (one fermion, two modes, small hop per half-tick)
B. two-path interferometer: fringes from records; bare which-path records; pointer couplings (V^2 + D^2 = 1); eraser
C. CHSH: source BS + supplied link-mediated controlled phase + hop-out to two detector regions; settings chosen by
   local coin records (coin-controlled rotations); outcomes = detector-mode records; no-signalling of marginals
D. bare two-time records at A versus B's setting; the same with a pointer copy at A
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/RECORDS_THAT_NEVER_CONDITION_THE_ODDS_GIVE_NO_ZENO_FULL_FRINGES_AND_CHSH_2_SQRT_2_WHILE_BARE_TWO_TIME_RECORDS_NEED_A_POINTER_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 90
import os, signal, sys, itertools, warnings
warnings.filterwarnings('ignore')
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm
from scipy.optimize import linprog

rng = np.random.default_rng(20261022)
NP = [0, 0]
TOL = 1e-12


def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")


# ---------------------------------------------------------------- registers and half-ticks
class Space:
    def __init__(self, dims):
        self.dims = list(dims); self.n = int(np.prod(dims))
        self.cfg = np.array(list(itertools.product(*[range(d) for d in dims])))
        # occupation changes between configurations: 2 per register whose particle moved
        self.cost = 2.0 * (self.cfg[:, None, :] != self.cfg[None, :, :]).sum(-1)

    def op(self, parts):
        M = np.eye(1)
        for r, d in enumerate(self.dims): M = np.kron(M, parts.get(r, np.eye(d)))
        return M

    def ctrl(self, c, t, Us):
        return sum(self.op({c: np.diag(np.eye(self.dims[c])[k]), t: U}) for k, U in enumerate(Us))


def hop(d, i, j, th, real=False):
    """exp(-i th (c_i^+ c_j + h.c.)) on one register (real=True: link phase i, a real rotation)"""
    G = np.zeros((d, d), complex)
    if real: G[i, j], G[j, i] = -1j, 1j
    else: G[i, j] = G[j, i] = 1.0
    return expm(-1j * th * G)


# ---------------------------------------------------------------- CL-2 transport
def lp(c, A, b, **kw):
    return linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method='highs', **kw)


def transport(p, q, U):
    """least mean occupation change, then greatest entropy on the least-cost face (exact face by one LP, then IPF)"""
    n = p.size
    t, s = np.nonzero((abs(U) > TOL) & (q[:, None] > 1e-15) & (p[None, :] > 1e-15))
    m = s.size; cost = COST[s, t]
    As = sp.csr_matrix((np.ones(m), (s, np.arange(m))), shape=(n, m)); At = sp.csr_matrix((np.ones(m), (t, np.arange(m))), shape=(n, m))
    A = sp.vstack([As, At]).tocsr(); b = np.concatenate([p, q])
    r = lp(cost, A, b); assert r.status == 0, r.message; opt = r.fun
    # face support: maximise the number of entries used in some least-cost plan (homogenised)
    Z = sp.csr_matrix((n, m))
    Aeq = sp.vstack([sp.hstack([As, Z, -sp.csr_matrix(p[:, None])]), sp.hstack([At, Z, -sp.csr_matrix(q[:, None])]),
                     sp.hstack([sp.csr_matrix(cost[None, :]), sp.csr_matrix((1, m)), sp.csr_matrix([[-opt]])])])
    rr = linprog(np.concatenate([np.zeros(m), -np.ones(m), [0.0]]), A_ub=sp.hstack([-sp.eye(m), sp.eye(m), sp.csr_matrix((m, 1))]),
                 b_ub=np.zeros(m), A_eq=Aeq, b_eq=np.zeros(2 * n + 1), bounds=[(0, None)] * m + [(0, 1)] * m + [(0, 1e7)], method='highs')
    face = rr.x[m:2 * m] > 0.5; s, t = s[face], t[face]
    J = np.ones(s.size)
    for _ in range(20000):  # iterative proportional fitting = greatest entropy with these marginals on the face
        rs = np.bincount(s, J, minlength=n); J *= np.where(rs[s] > 0, p[s] / rs[s], 0)
        ct = np.bincount(t, J, minlength=n); J *= np.where(ct[t] > 0, q[t] / ct[t], 0)
        if abs(np.bincount(s, J, minlength=n) - p).max() < 1e-13: break
    K = np.zeros((n, n)); np.add.at(K, (t, s), J / p[s])  # K[t, s] = P(t | s)
    return K, opt


def run(psi0, steps):
    """exact record chain: list of odds and transition kernels"""
    psi, P, Ks = psi0, [abs(psi0) ** 2], []
    for U in steps:
        nxt = U @ psi; K, _ = transport(abs(psi) ** 2, abs(nxt) ** 2, U); Ks.append(K); psi = nxt; P.append(abs(psi) ** 2)
    return psi, P, Ks


def joint(P0, Ks, times):
    """exact joint law of the actual configuration at the given half-tick indices (0 = start)"""
    rec = {(): P0.copy()}
    for k, K in enumerate(Ks, start=1):
        rec = {key: K @ v for key, v in rec.items()}
        if k in times: rec = {key + (c,): np.eye(len(P0))[c] * v[c] for key, v in rec.items() for c in np.nonzero(v > 1e-15)[0]}
    out = {}
    for key, v in rec.items(): out[key] = out.get(key, 0) + v.sum()
    return out


def sample(P0, Ks, N):
    n = P0.size; c = rng.choice(n, N, p=P0 / P0.sum()); tr = [c]
    for K in Ks:
        C = np.cumsum(K[:, c], axis=0); u = rng.random(N); c = np.minimum((C < u).sum(0), n - 1); tr.append(c)
    return np.array(tr)


# ================================================================ A. constant records versus Zeno
def section_A():
    global COST
    print('A. constant records: one fermion, two modes, hop th = pi/40 per half-tick, a record every half-tick')
    S = Space([2]); COST = S.cost; th = np.pi / 40; T = 20
    psi0 = np.array([1, 0], complex); U = hop(2, 0, 1, th)
    psi, P, Ks = run(psi0, [U] * T)
    born = np.sin(th * np.arange(T + 1)) ** 2
    rec = np.array([Pk[1] for Pk in P])  # law of the actual configuration = record law
    tr = sample(P[0], Ks, 20000); emp = (tr == 1).mean(1)
    zeno = (1 - (1 - 2 * np.sin(th) ** 2) ** np.arange(T + 1)) / 2  # if each record conditioned the odds
    flips = (np.diff(tr, axis=0) != 0).sum(0)
    check('A1 THEOREM: records never condition the odds, so the record law is Born at every half-tick: full transfer, no Zeno freezing',
          abs(rec - born).max() < 1e-12 and abs(emp - born).max() < 0.015,
          f'P(R) at t=20: records {rec[-1]:.6f}, sampled {emp[-1]:.3f}, Born {born[-1]:.3f}; if records conditioned the odds {zeno[-1]:.3f}')
    check('A2 the fewest-change transport moves each actual track once (monotone transfer); the odds keep the superposition',
          flips.max() == 1, f'flips per track: mean {flips.mean():.3f}, max {flips.max()}; |psi| = ({abs(psi[0]):.2e}, {abs(psi[1]):.3f})')


# ================================================================ B. interferometer
def mz_steps(S, phi, alpha=None, eraser=False):
    """particle register dims 4: 0,1 first splitter ports; 2,3 arms after hop-out; output = arm modes after 2nd splitter.
    optional pointer register (dims 2) rotated by alpha when the particle is in arm 1 (supplied coupling)."""
    d = 4; P = 0
    bs1 = S.op({P: hop(d, 0, 1, np.pi / 4, real=True)})
    out = np.diag([1, 1, 1, np.exp(1j * phi)]) @ hop(d, 0, 2, np.pi / 2) @ hop(d, 1, 3, np.pi / 2)
    st = [bs1]
    if alpha is not None: st.append(S.ctrl(0, 1, [np.eye(2), hop(2, 0, 1, alpha), np.eye(2), np.eye(2)]))
    st += [S.op({P: out}), S.op({P: hop(d, 2, 3, np.pi / 4, real=True)})]
    if eraser: st.append(S.op({1: hop(2, 0, 1, np.pi / 4, real=True)}))
    return st


def section_B():
    global COST
    print('B. two-path interferometer from records (supplied splitters = quarter hops, arm phase phi = a link phase)')
    S = Space([4]); COST = S.cost; phis = np.linspace(0, 2 * np.pi, 9)[:-1]
    pd = []
    for ph in phis:
        _, P, Ks = run(np.eye(4)[0].astype(complex), mz_steps(S, ph)); pd.append(P[-1][2])
    pd = np.array(pd); V = (pd.max() - pd.min()) / (pd.max() + pd.min())
    tr = sample(P[0], Ks, 20000)
    check('B1 fringes from the output records: visibility 1, P(D1) = cos^2(phi/2) up to the splitter phase', abs(V - 1) < 1e-9
          and abs(np.sort(pd) - np.sort(np.cos(phis / 2) ** 2)).max() < 1e-9, f'V = {V:.6f}; P(D1) over phi {np.round(pd, 3).tolist()}')
    _, P, Ks = run(np.eye(4)[0].astype(complex), mz_steps(S, 0.0))
    jt = joint(P[0], Ks, {1, 3}); pa = {a: sum(v for k, v in jt.items() if k[0] == a) for a in (0, 1)}
    cond = {a: jt.get((a, 2), 0) / pa[a] for a in (0, 1)}
    check('B2 FINDING: every track carries a definite bare which-path record AND full fringes: path known to K = 1 with V = 1,'
          ' V^2 + K^2 = 2 > 1 (measured complementarity bound 1) if the bare record were readable',
          abs(pa[0] - 0.5) < 1e-12 and V > 1 - 1e-9, f'P(path 0) {pa[0]:.3f}; P(D1 | bare path record 0, 1) = {cond[0]:.3f}, {cond[1]:.3f} at phi = 0')
    S2 = Space([4, 2]); COST = S2.cost; rows = []
    for al in (np.pi / 2, np.pi / 3, np.pi / 6, 0.0):
        pdd = []
        for ph in phis:
            _, P, Ks = run(np.kron(np.eye(4)[0], np.eye(2)[0]).astype(complex), mz_steps(S2, ph, alpha=al))
            pdd.append(P[-1].reshape(4, 2)[2].sum())
        pdd = np.array(pdd); Va = (pdd.max() - pdd.min()) / (pdd.max() + pdd.min()); rows.append((al, Va))
        if al == np.pi / 2:
            jt = joint(P[0], Ks, {2})
            agree = sum(v for k, v in jt.items() if S2.cfg[k[0]][1] == (1 if S2.cfg[k[0]][0] == 1 else 0))
    check('B3 a pointer that the update couples to the path removes fringes in the odds and the records: V = cos(alpha), V^2 + D^2 = 1',
          all(abs(Va - abs(np.cos(al))) < 1e-9 for al, Va in rows), ' '.join(f'a={al:.2f}:V={Va:.3f}' for al, Va in rows) + f'; full pointer agrees with path record {agree:.6f}')
    # eraser: full which-path pointer, then pointer read in a rotated basis: conditional fringes and anti-fringes
    cf = []
    for ph in phis:
        _, P, Ks = run(np.kron(np.eye(4)[0], np.eye(2)[0]).astype(complex), mz_steps(S2, ph, alpha=np.pi / 2, eraser=True))
        Q = P[-1].reshape(4, 2)[2:]; cf.append([Q[0, 0] / Q[:, 0].sum(), Q[0, 1] / Q[:, 1].sum()])
    cf = np.array(cf); Ve = [(cf[:, k].max() - cf[:, k].min()) / (cf[:, k].max() + cf[:, k].min()) for k in (0, 1)]
    check('B4 eraser: sorted by the rotated pointer record, fringes and anti-fringes return with V = 1 (single-time joint records are Born)',
          min(Ve) > 1 - 1e-9 and abs(cf[:, 0] + cf[:, 1] - 1).max() < 1e-9, f'V = {Ve[0]:.6f}, {Ve[1]:.6f}; complementary')


# ================================================================ C. CHSH with coin-record settings
def bell_space(pointer=False):
    dims = [4, 4, 2, 2] + ([2] if pointer else [])  # rail A (sA0 sA1 dA0 dA1), rail B, coin A, coin B, [pointer A]
    return Space(dims)


def bell_steps(S, ang, pointer=False, split=True):
    """h1 splitters (rails at source, coins); h2 supplied controlled phase on (sA1, sB1); h3 B's source splitter then hop-out to detectors;
    h4, h5 coin-controlled rotations of the detector pair, half the setting angle each, A and B in the same half-tick"""
    A_, B_, cA, cB = 0, 1, 2, 3
    h1 = S.op({A_: hop(4, 0, 1, np.pi / 4, real=True), B_: hop(4, 0, 1, np.pi / 4, real=True), cA: hop(2, 0, 1, np.pi / 4, real=True), cB: hop(2, 0, 1, np.pi / 4, real=True)})
    ph = np.ones(S.n); ph[(S.cfg[:, 0] == 1) & (S.cfg[:, 1] == 1)] = -1; h2 = np.diag(ph).astype(complex)
    out = hop(4, 0, 2, np.pi / 2) @ hop(4, 1, 3, np.pi / 2); h3 = S.op({A_: out, B_: out @ hop(4, 0, 1, np.pi / 4, real=True)})
    rot = lambda th: hop(4, 2, 3, th, real=True)
    fr = (0.5, 0.5) if split else (1.0, 0.0)
    steps = [h1, h2, h3]
    for k, f in enumerate(fr):
        RA = S.ctrl(cA, A_, [rot(f * ang['A'][0]), rot(f * ang['A'][1])]); RB = S.ctrl(cB, B_, [rot(f * ang['B'][0]), rot(f * ang['B'][1])])
        steps.append(RA @ RB)
        if pointer and k == 0:  # copy A's detector occupation into the pointer (supplied coupling), A-only half-tick
            steps.append(S.ctrl(A_, 4, [np.eye(2), np.eye(2), np.eye(2), hop(2, 0, 1, np.pi / 2)]))
    return steps


def corr(prob, S, coinA, coinB):
    """E(x, y) from a law over configurations (detector modes 2, 3 -> outcome +1, -1)"""
    E = np.zeros((2, 2)); pm = np.zeros((2, 2))
    for c, w in enumerate(prob):
        a, b, x, y = S.cfg[c][:4]
        if a < 2 or b < 2: continue
        E[x, y] += w * (1 if a == 2 else -1) * (1 if b == 2 else -1); pm[x, y] += w
    return E / pm


def chsh(E): return E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1]


def section_C():
    global COST
    print('C. CHSH: settings chosen by local coin records, outcomes = detector-mode records, A and B steps share half-ticks')
    S = bell_space(); COST = S.cost
    psi0 = np.zeros(S.n, complex); psi0[0] = 1.0
    ang = {'A': (0.0, np.pi / 4), 'B': (np.pi / 8, -np.pi / 8)}
    # sign convention fixed once on exact odds (supplied settings)
    best = None
    for sa, sb in itertools.product((1, -1), repeat=2):
        a2 = {'A': tuple(sa * v for v in ang['A']), 'B': tuple(sb * v for v in ang['B'])}
        psi, P, Ks = run(psi0, bell_steps(S, a2)); Sv = chsh(corr(P[-1], S, 0, 0))
        if best is None or abs(Sv) > abs(best[0]): best = (Sv, a2, P, Ks)
    Sx, ang, P, Ks = best
    jt = joint(P[0], Ks, {1, 5})
    lawc = np.zeros(S.n)  # law over final configurations, but settings taken from the coin RECORDS at h1
    agree = 0.0
    for (c1, c5), w in jt.items():
        lawc[c5] += w; agree += w * (tuple(S.cfg[c1][2:4]) == tuple(S.cfg[c5][2:4]))
    Sr = chsh(corr(lawc, S, 0, 0))
    tr = sample(P[0], Ks, 40000); fin = tr[-1]
    emp = np.bincount(fin, minlength=S.n) / fin.size; Ss = chsh(corr(emp, S, 0, 0))
    check('C1 THEOREM (support): a register the half-tick acts on only as a control keeps its occupation, so the coin record at h1 IS the setting',
          abs(agree - 1) < 1e-12, f'P(coin record at h1 = coin record at h5) = {agree:.12f}')
    check('C2 CHSH from records reaches the quantum value 2 sqrt 2 (exact chain and 40000 sampled tracks)',
          abs(abs(Sr) - 2 * np.sqrt(2)) < 1e-9 and abs(abs(Ss) - 2 * np.sqrt(2)) < 0.06, f'S exact odds {Sx:.6f}, record chain {Sr:.6f}, sampled {Ss:.3f}')
    # no-signalling of single-time record marginals
    ns = 0.0
    for x in (0, 1):
        pa = []
        for y in (0, 1):
            m = (S.cfg[:, 2] == x) & (S.cfg[:, 3] == y); pa.append(lawc[m & (S.cfg[:, 0] == 2)].sum() / lawc[m].sum())
        ns = max(ns, abs(pa[0] - pa[1]))
    check('C3 THEOREM: single-time record marginals at A do not depend on B\'s setting (Born marginals of a product local step)',
          ns < 1e-12, f'max |P(a|x,y=0) - P(a|x,y=1)| = {ns:.1e}')
    return S, ang


# ================================================================ D. bare two-time records
def twotime(S, ang, pointer=False, split=True):
    psi0 = np.zeros(S.n, complex); psi0[0] = 1.0
    psi, P, Ks = run(psi0, bell_steps(S, ang, pointer=pointer, split=split))
    tA = 4; tF = len(Ks)
    jt = joint(P[0], Ks, {tA, tF}); dep = 0.0; L = {}
    for (c4, cF), w in jt.items():
        a4, a5, x, y = S.cfg[c4][0], S.cfg[cF][0], S.cfg[cF][2], S.cfg[cF][3]
        L[(x, y, a4, a5)] = L.get((x, y, a4, a5), 0) + w
    for x in (0, 1):
        v = []
        for y in (0, 1):
            tot = sum(L.get((x, y, a, b), 0) for a in (2, 3) for b in (2, 3))
            v.append(np.array([L.get((x, y, a, b), 0) / tot for a in (2, 3) for b in (2, 3)]))
        dep = max(dep, 0.5 * abs(v[0] - v[1]).sum())
    return dep, L


def section_D(S, ang):
    global COST
    print('D. A\'s bare records at h4 (half rotated) and h5 (outcome) versus B\'s setting')
    COST = S.cost
    dep, L = twotime(S, ang)
    check('D1 FINDING (event-level remote dependence): the joint law of A\'s own two bare records depends on B\'s distant setting',
          dep > 1e-3, f'max TV over x between y = 0 and y = 1: {dep:.4f} (single-time marginals: 0, C3)')
    devs = []
    for k in range(6):
        a2 = {'A': tuple(rng.uniform(-np.pi / 2, np.pi / 2, 2)), 'B': tuple(rng.uniform(-np.pi / 2, np.pi / 2, 2))}
        devs.append(twotime(S, a2)[0])
    check('D2 generic: random settings give the same dependence (not a tuned case)', min(devs) > 1e-3, f'TV {np.round(devs, 3).tolist()}')
    a3 = {'A': ang['A'], 'B': ang['B']}
    S0 = bell_space(); COST = S0.cost
    d_seq, _ = twotime(S0, a3, split=False)
    check('D3 control: if A\'s step at h4 is whole and h5 idle, A has nothing to move at h5 and no dependence appears',
          d_seq < 1e-12, f'TV {d_seq:.1e}')
    Sp = bell_space(pointer=True); COST = Sp.cost
    dp, Lp = twotime(Sp, a3, pointer=True)
    # quantum sequential prediction: A measured (pointer) at h4, then outcome; from the final single-time Born joint
    psi0 = np.zeros(Sp.n, complex); psi0[0] = 1.0; psi, P, Ks = run(psi0, bell_steps(Sp, a3, pointer=True))
    sq = max(abs(sum(P[-1][(Sp.cfg[:, 0] == b) & (Sp.cfg[:, 2] == x) & (Sp.cfg[:, 3] == y) & (Sp.cfg[:, 4] == a - 2)]) - Lp.get((x, y, a, b), 0))
             for x in (0, 1) for y in (0, 1) for a in (2, 3) for b in (2, 3))
    check('D4 THEOREM: after a pointer copy at A the two-time records equal (pointer, outcome) at one half-tick: Born, quantum sequential, no dependence',
          dp < 1e-12 and sq < 1e-12, f'TV {dp:.1e}; |two-time law - Born(pointer, outcome)| {sq:.1e}')


if __name__ == '__main__':
    section_A(); section_B(); S, ang = section_C(); section_D(S, ang)
    print('supplied: registers (one fermion per mode set), splitter and rotation angles, the controlled phase standing for a '
          'link-mediated gate, coin-controlled rotations, pointer couplings, the half-tick schedule. forced: the transport.')
    print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
