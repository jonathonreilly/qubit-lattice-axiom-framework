"""Multi-tick moving-record LPs (supplied two-record toy; not framework content).

Model
-----
* Two distant regions A (n_A sites) and B (n_B sites).  One record in each.
* Possibilities: psi in C^{n_A} (x) C^{n_B}  (two-excitation sector, one excitation per
  region; linked = entangled).  Never cut by moves (reading R3).
* Tick k with settings (s, r): psi_{k+1} = (UA[k][s] (x) UB[k][r]) psi_k.
* Born odds P_k(a, b) = |psi_k(a, b)|^2.
* A record moves at most one site per tick: allowed one-tick moves are given by boolean
  matrices movA[k] (n_A x n_A) and movB[k] (n_B x n_B).

A rule is a causal stochastic process on configurations x_k = (a_k, b_k), one law
Q_sigma(x_0..x_T) per setting sequence sigma = ((s_0, r_0), ..., (s_{T-1}, r_{T-1})).

Constraints available
---------------------
* C  : time-k marginal of Q_sigma equals P_k^sigma, every k, every sigma.
* CAUS: marginal on x_0..x_k depends only on sigma_{<k} (no retro-causation).
* NS : law of (b_0..b_T) independent of A's settings; law of (a_0..a_T) independent of
       B's settings.
* Markov-L (per tick, separate LP): coupling pi_k with Born marginals and
       sum_{a'} pi((a,b),(a',b')) = P_k(a,b) TB_k[r_{<=k}](b, b')
       sum_{b'} pi((a,b),(a',b')) = P_k(a,b) TA_k[s_{<=k}](a, a')
  i.e. each record's move odds given the full configuration do not depend on the other
  record's position nor on the other side's settings.  (Relaxation of "depends only on
  local data": a necessary condition, so infeasibility is a valid no-go.)
"""
import itertools
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

TOL_SUPPORT = 1e-13


class Model:
    def __init__(self, psi0, UA, UB, movA, movB):
        self.nA = movA[0].shape[0]
        self.nB = movB[0].shape[0]
        self.psi0 = np.asarray(psi0, complex).reshape(self.nA * self.nB)
        self.UA, self.UB, self.movA, self.movB = UA, UB, movA, movB
        self.T = len(UA)
        self.SA = [len(u) for u in UA]          # number of A settings per tick
        self.SB = [len(u) for u in UB]

    # ---- possibilities -------------------------------------------------------
    def psi(self, sig):
        v = self.psi0.copy()
        for k, (s, r) in enumerate(sig):
            v = np.kron(self.UA[k][s], self.UB[k][r]) @ v
        return v

    def born(self, sig):
        return (np.abs(self.psi(sig)) ** 2).reshape(self.nA, self.nB)

    def sigmas(self, T=None):
        T = self.T if T is None else T
        per_tick = [list(itertools.product(range(self.SA[k]), range(self.SB[k]))) for k in range(T)]
        return list(itertools.product(*per_tick))

    # ---- histories -----------------------------------------------------------
    def histories(self, sig):
        """All allowed histories x_0..x_T with every x_k in the support of P_k^sig."""
        T = len(sig)
        supp = [self.born(sig[:k]) > TOL_SUPPORT for k in range(T + 1)]
        hist = [((a, b),) for a in range(self.nA) for b in range(self.nB) if supp[0][a, b]]
        for k in range(T):
            new = []
            for h in hist:
                a, b = h[-1]
                for a2 in np.nonzero(self.movA[k][a])[0]:
                    for b2 in np.nonzero(self.movB[k][b])[0]:
                        if supp[k + 1][a2, b2]:
                            new.append(h + ((int(a2), int(b2)),))
            hist = new
        return hist


class LP:
    """Sparse equality-constrained LP builder.  Rows carry a tag; rows whose tag is in
    `soft` get a +/- slack pair and the objective minimises the total slack (L1 violation)."""

    def __init__(self):
        self.nv = 0
        self.rows, self.cols, self.vals, self.b, self.tags = [], [], [], [], []
        self.nr = 0

    def add_vars(self, n):
        start = self.nv
        self.nv += n
        return start

    def add_row(self, coeffs, rhs, tag='hard'):
        for j, c in coeffs:
            self.rows.append(self.nr)
            self.cols.append(j)
            self.vals.append(c)
        self.b.append(rhs)
        self.tags.append(tag)
        self.nr += 1

    def solve(self, c=None, bounds=(0, None), method='highs-ipm', soft=()):
        """soft: iterable of tags (weight 1) or dict tag -> weight.  Slack totals per tag
        are returned in res.slack_by_tag (when soft is used)."""
        rows, cols, vals = list(self.rows), list(self.cols), list(self.vals)
        nv = self.nv
        cvec = np.zeros(nv) if c is None else np.asarray(c, float).copy()
        weights = dict(soft) if isinstance(soft, dict) else {t: 1.0 for t in soft}
        slack_tag = []
        if weights:
            wv = []
            for i, t in enumerate(self.tags):
                if t in weights:
                    rows += [i, i]
                    cols += [nv, nv + 1]
                    vals += [1.0, -1.0]
                    nv += 2
                    wv += [weights[t], weights[t]]
                    slack_tag += [t, t]
            cvec = np.concatenate([cvec, np.array(wv)])
        A = coo_matrix((vals, (rows, cols)), shape=(self.nr, nv)).tocsr()
        res = linprog(cvec, A_eq=A, b_eq=np.array(self.b), bounds=bounds, method=method)
        if weights and res.status == 0:
            s = res.x[self.nv:]
            res.slack_by_tag = {t: float(sum(v for v, tt in zip(s, slack_tag) if tt == t)) for t in weights}
        return res


def history_lp(model, ns=True, caus=True, extra=None):
    """Build the history LP. Returns (lp, index) where index[sig] = (start, histories)."""
    lp = LP()
    sigs = model.sigmas()
    T = model.T
    index = {}
    for sig in sigs:
        H = model.histories(sig)
        start = lp.add_vars(len(H))
        index[sig] = (start, H)
    # C: Born marginals at each time
    for sig in sigs:
        start, H = index[sig]
        for k in range(T + 1):
            P = model.born(sig[:k])
            groups = {}
            for i, h in enumerate(H):
                groups.setdefault(h[k], []).append(start + i)
            for a in range(model.nA):
                for b in range(model.nB):
                    if P[a, b] > TOL_SUPPORT:
                        idx = groups.get((a, b), [])
                        lp.add_row([(j, 1.0) for j in idx], P[a, b], tag='BORN')
                    # zero-support cells have no variables by construction
    # CAUS: marginal on x_0..x_k depends only on sig_{<k}
    if caus:
        for k in range(1, T):
            classes = {}
            for sig in sigs:
                classes.setdefault(sig[:k], []).append(sig)
            for pref, members in classes.items():
                ref = members[0]
                rs, rH = index[ref]
                refm = {}
                for i, h in enumerate(rH):
                    refm.setdefault(h[:k + 1], []).append(rs + i)
                for sig in members[1:]:
                    st, H = index[sig]
                    m = {}
                    for i, h in enumerate(H):
                        m.setdefault(h[:k + 1], []).append(st + i)
                    keys = set(refm) | set(m)
                    for key in keys:
                        coeffs = [(j, 1.0) for j in m.get(key, [])] + [(j, -1.0) for j in refm.get(key, [])]
                        if coeffs:
                            lp.add_row(coeffs, 0.0, tag='CAUS')
    # NS: B-history law independent of A settings; A-history law independent of B settings
    if ns:
        for side in ('B', 'A'):
            classes = {}
            for sig in sigs:
                key = tuple(x[1] for x in sig) if side == 'B' else tuple(x[0] for x in sig)
                classes.setdefault(key, []).append(sig)
            for key, members in classes.items():
                ref = members[0]
                rs, rH = index[ref]
                proj = (lambda h: tuple(x[1] for x in h)) if side == 'B' else (lambda h: tuple(x[0] for x in h))
                refm = {}
                for i, h in enumerate(rH):
                    refm.setdefault(proj(h), []).append(rs + i)
                for sig in members[1:]:
                    st, H = index[sig]
                    m = {}
                    for i, h in enumerate(H):
                        m.setdefault(proj(h), []).append(st + i)
                    for kk in set(refm) | set(m):
                        coeffs = [(j, 1.0) for j in m.get(kk, [])] + [(j, -1.0) for j in refm.get(kk, [])]
                        if coeffs:
                            lp.add_row(coeffs, 0.0, tag='NS' + side)
    if extra is not None:
        extra(lp, index, model)
    return lp, index


def markov_local_lp(model, k, c_fn=None, soft=(), method='highs-ipm'):
    """Markov-L feasibility at tick k, jointly over all sigma_{<=k}.

    Variables: pi^{sig}((a,b),(a',b')) for allowed moves between supports, plus
    TB[r_{<=k}][b, b'] and TA[s_{<=k}][a, a'] (shared across the other side's settings).
    """
    lp = LP()
    sigs = model.sigmas(k + 1)
    nA, nB = model.nA, model.nB
    TB, TA = {}, {}
    for sig in sigs:
        rk = tuple(x[1] for x in sig)
        sk = tuple(x[0] for x in sig)
        if rk not in TB:
            TB[rk] = {}
            for b in range(nB):
                for b2 in np.nonzero(model.movB[k][b])[0]:
                    TB[rk][(b, int(b2))] = lp.add_vars(1)
        if sk not in TA:
            TA[sk] = {}
            for a in range(nA):
                for a2 in np.nonzero(model.movA[k][a])[0]:
                    TA[sk][(a, int(a2))] = lp.add_vars(1)
    # kernel rows sum to one
    for d in list(TB.values()) + list(TA.values()):
        rowsum = {}
        for (x, y), j in d.items():
            rowsum.setdefault(x, []).append(j)
        for x, js in rowsum.items():
            lp.add_row([(j, 1.0) for j in js], 1.0)
    pis = {}
    for sig in sigs:
        P0 = model.born(sig[:k])
        P1 = model.born(sig)
        rk = tuple(x[1] for x in sig)
        sk = tuple(x[0] for x in sig)
        var = {}
        for a in range(nA):
            for b in range(nB):
                if P0[a, b] <= TOL_SUPPORT:
                    continue
                for a2 in np.nonzero(model.movA[k][a])[0]:
                    for b2 in np.nonzero(model.movB[k][b])[0]:
                        if P1[a2, b2] > TOL_SUPPORT:
                            var[(a, b, int(a2), int(b2))] = lp.add_vars(1)
        pis[sig] = var
        # Born marginals
        rows = {}
        cols = {}
        for (a, b, a2, b2), j in var.items():
            rows.setdefault((a, b), []).append(j)
            cols.setdefault((a2, b2), []).append(j)
        for a in range(nA):
            for b in range(nB):
                if P0[a, b] > TOL_SUPPORT:
                    lp.add_row([(j, 1.0) for j in rows.get((a, b), [])], P0[a, b], tag='BORN')
                if P1[a, b] > TOL_SUPPORT:
                    lp.add_row([(j, 1.0) for j in cols.get((a, b), [])], P1[a, b], tag='BORN')
        # Markov-L for B: sum_{a'} pi((a,b),(a',b')) = P0(a,b) TB(b,b')  (and same for A)
        gB, gA = {}, {}
        for (a, b, a2, b2), j in var.items():
            gB.setdefault((a, b, b2), []).append(j)
            gA.setdefault((a, b, a2), []).append(j)
        for a in range(nA):
            for b in range(nB):
                if P0[a, b] <= TOL_SUPPORT:
                    continue
                for b2 in np.nonzero(model.movB[k][b])[0]:
                    coeffs = [(j, 1.0) for j in gB.get((a, b, int(b2)), [])]
                    coeffs.append((TB[rk][(b, int(b2))], -P0[a, b]))
                    lp.add_row(coeffs, 0.0, tag='MLB')
                for a2 in np.nonzero(model.movA[k][a])[0]:
                    coeffs = [(j, 1.0) for j in gA.get((a, b, int(a2)), [])]
                    coeffs.append((TA[sk][(a, int(a2))], -P0[a, b]))
                    lp.add_row(coeffs, 0.0, tag='MLA')
    c = None
    if c_fn is not None:
        c = c_fn(lp, pis, TA, TB, model, k)
    res = lp.solve(c=c, soft=soft, method=method)
    return res, pis, TA, TB


# ---- helpers ------------------------------------------------------------------
def haar_unitary(n, rng):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def rand_state(n, rng):
    v = rng.normal(size=n) + 1j * rng.normal(size=n)
    return v / np.linalg.norm(v)


def block_unitary(n, blocks, gates):
    U = np.zeros((n, n), complex)
    covered = set()
    for blk, G in zip(blocks, gates):
        U[np.ix_(blk, blk)] = G
        covered |= set(blk)
    for x in range(n):
        if x not in covered:
            U[x, x] = 1.0
    return U


def ring_adj(n):
    a = np.zeros((n, n), bool)
    for x in range(n):
        for d in (-1, 0, 1):
            a[x, (x + d) % n] = True
    return a


def line_adj(n):
    a = np.zeros((n, n), bool)
    for x in range(n):
        for d in (-1, 0, 1):
            if 0 <= x + d < n:
                a[x, x + d] = True
    return a


def tick_support_adj(U, tol=1e-12):
    """Moves only along the tick's own support (records follow the flow)."""
    return np.abs(U) > tol


def rot(theta):
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]], complex)


H2 = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
