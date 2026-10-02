#!/usr/bin/env python3
"""Formation-timing probes on a small ring (exploratory, supplied toy model; ai/probes backlog only).

Question (owner, 2026-10-02): do records form on one universe-wide tick, or locally at any time; and does
it matter when a record forms, given that "the past sets the neighborhood conditions"?

Supplied toy model (none of this is derived; the package leaves preparation, schedule, menu rule and gamma/J open):
  * N qubit sites on a ring.  The shared possibilities of the sites with no record are one joint pure state.
  * Preparation: the ground state of J sum_j sigma_j . sigma_{j+1} (J = 1 > 0).  Every undecided site then has
    equal odds for every menu, and the state does not change until the first record forms.
  * Change between records: exp(-i H t) with that coupling.  A recorded site is locked, so each of its bonds acts on
    the unrecorded neighbour as a steady push J n_k . sigma_j (the bond with the locked possibility n_k in place)
    [push=True]; variant push=False: the recorded site simply drops out of the change.
  * Formation: a two-outcome menu with axis m; odds (1 +- m . r_j)/2 from the site's own part r_j; the shared
    possibilities are compressed to agree with the outcome (record content = +-m).
  * Menu rules: 'fixed' (m = z everywhere); 'own' (m = axis of the site's own part, uniformly random if undecided);
    'field' (m = direction of the summed contents of recorded neighbours, uniformly random if none or cancelled).
  * Simultaneous formations: every menu of the group is set from the state before the group forms; joint Born odds.
Readouts use record contents only: formation times are not recorded.
usage: python3 timing_probes.py A|B1|B2|C|D [M]
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
import sys, json, time, warnings
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply, eigsh
warnings.filterwarnings("ignore")

Z = np.array([0.0, 0.0, 1.0])


def rand_axis(rng):
    v = rng.normal(size=3)
    return v / np.linalg.norm(v)


class Ring:
    def __init__(self, N, J=1.0):
        self.N, self.J, self.dim = N, J, 2 ** N
        pa = [sps.csr_matrix(np.array(m, dtype=complex)) for m in ([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]])]
        I2 = sps.identity(2, dtype=complex, format="csr")
        self.ops = [[self._site(pa[a], j, I2) for a in range(3)] for j in range(N)]
        self.bonds = [(j, (j + 1) % N) for j in range(N)]
        self.bondH = {b: (sum(self.ops[b[0]][a] @ self.ops[b[1]][a] for a in range(3))).tocsr() for b in self.bonds}
        self.H0 = (J * sum(self.bondH.values())).tocsr()
        if self.dim <= 1024:
            w, V = np.linalg.eigh(self.H0.toarray())
            self.gs, self.gap = V[:, 0].astype(complex), w[1] - w[0]
        else:
            w, V = eigsh(self.H0, k=3, which="SA")
            o = np.argsort(w)
            self.gs, self.gap = V[:, o[0]].astype(complex), w[o[1]] - w[o[0]]
        self.gs /= np.linalg.norm(self.gs)
        self._bond_cache = {}

    def _site(self, s, j, I2):
        m = None
        for k in range(self.N):
            f = s if k == j else I2
            m = f if m is None else sps.kron(m, f, format="csr")
        return m

    def nbrs(self, j):
        return ((j - 1) % self.N, (j + 1) % self.N)

    def heff(self, rec, push=True):
        mask = frozenset(rec)
        if mask not in self._bond_cache:
            H = sps.csr_matrix((self.dim, self.dim), dtype=complex)
            for a, b in self.bonds:
                if a not in rec and b not in rec:
                    H = H + self.bondH[(a, b)]
            self._bond_cache[mask] = H.tocsr()
        H = self._bond_cache[mask]
        if push:
            for a, b in self.bonds:
                ra, rb = a in rec, b in rec
                if ra != rb:
                    u, r = (b, a) if ra else (a, b)
                    n = rec[r]
                    H = H + n[0] * self.ops[u][0] + n[1] * self.ops[u][1] + n[2] * self.ops[u][2]
        return (self.J * H).tocsr()

    def bloch(self, psi, j):
        return np.array([np.vdot(psi, self.ops[j][a] @ psi).real for a in range(3)])

    def project(self, psi, j, m, s):
        return 0.5 * (psi + s * (m[0] * (self.ops[j][0] @ psi) + m[1] * (self.ops[j][1] @ psi) + m[2] * (self.ops[j][2] @ psi)))

    def menu(self, psi, j, rule, rng, rec):
        if rule == "fixed":
            return Z
        if rule == "own":
            r = self.bloch(psi, j)
            nr = np.linalg.norm(r)
            return r / nr if nr > 1e-9 else rand_axis(rng)
        if rule == "field":
            h = np.zeros(3)
            for k in self.nbrs(j):
                if k in rec:
                    h = h + rec[k]
            nh = np.linalg.norm(h)
            return h / nh if nh > 1e-9 else rand_axis(rng)
        raise ValueError(rule)

    def form(self, psi, j, m, rng):
        r = self.bloch(psi, j)
        pp = min(1.0, max(0.0, 0.5 * (1.0 + m @ r)))
        s = 1 if rng.random() < pp else -1
        v = self.project(psi, j, m, s)
        return v / np.linalg.norm(v), s * m

    def evolve(self, psi, rec, dt, push=True):
        if dt <= 0 or not rec:          # the preparation is stationary until the first record forms
            return psi
        H = self.heff(rec, push)
        return expm_multiply(-1j * dt * H, psi) if H.nnz else psi

    def run(self, schedule, rule, rng, push=True):
        psi, rec, tnow = self.gs.copy(), {}, 0.0
        for t, group in schedule:
            psi = self.evolve(psi, rec, t - tnow, push)
            tnow = t
            ms = [self.menu(psi, j, rule, rng, rec) for j in group]   # menus set before any member of the group forms
            for j, m in zip(group, ms):
                psi, n = self.form(psi, j, m, rng)
                rec[j] = n
        return rec


# ---------------------------------------------------------------- schedules
def sched_poisson(N, Tbar, rng):
    t = rng.exponential(Tbar, N)
    return [(float(t[j]), [int(j)]) for j in np.argsort(t)]


def sched_ticks(N, p, tau, rng, phase_groups):
    """sites in one phase group share a tick train (phase uniform in [0, tau)); each tick an unrecorded site forms w.p. p."""
    times = np.empty(N)
    for G in phase_groups:
        phi = rng.random() * tau
        for j in G:
            times[j] = phi + (rng.geometric(p) - 1) * tau
    d = {}
    for j in range(N):
        d.setdefault(float(times[j]), []).append(j)
    return [(t, sorted(d[t])) for t in sorted(d)]


def sched_triggered(N, g0, g1, rng):
    rec, t, out = set(), 0.0, []
    while len(rec) < N:
        un = [j for j in range(N) if j not in rec]
        rates = np.array([g0 + g1 * sum(1 for k in ((j - 1) % N, (j + 1) % N) if k in rec) for j in un])
        R = rates.sum()
        t += rng.exponential(1.0 / R)
        j = un[rng.choice(len(un), p=rates / R)]
        rec.add(j)
        out.append((t, [j]))
    return out


def tick_tau(p, Tbar):
    return Tbar / (1.0 / p - 0.5)   # mean per-site waiting time tau (1/p - 1/2) = Tbar


# ---------------------------------------------------------------- readouts (record contents only)
def readout(rec, N, rule):
    n = np.array([rec[j] for j in range(N)])
    out = {}
    if rule == "fixed":
        s = n[:, 2]
        for r in range(1, N // 2 + 1):
            out["c%d" % r] = float(np.mean(s * np.roll(s, -r)))
        out["bond"] = [float(s[j] * s[(j + 1) % N]) for j in range(N)]
    else:
        for r in range(1, N // 2 + 1):
            d = np.sum(n * np.roll(n, -r, axis=0), axis=1)
            out["v%d" % r] = float(np.mean(d))
            out["a%d" % r] = float(np.mean(np.abs(d) > 1 - 1e-6))
        axes = []
        for v in n:
            if not any(abs(v @ a) > 1 - 1e-6 for a in axes):
                axes.append(v)
        out["naxes"] = float(len(axes))
    return out


def summarize(rows):
    keys = [k for k in rows[0] if k != "bond"]
    S = {}
    for k in keys:
        x = np.array([r[k] for r in rows])
        S[k] = (float(x.mean()), float(x.std(ddof=1) / np.sqrt(len(x))))
    if "bond" in rows[0]:
        b = np.array([r["bond"] for r in rows])
        S["bond"] = [(float(b[:, j].mean()), float(b[:, j].std(ddof=1) / np.sqrt(len(b)))) for j in range(b.shape[1])]
    return S


def mc(R, make_sched, rule, M, seed, push=True):
    rng = np.random.default_rng(seed)
    rows = [readout(R.run(make_sched(rng), rule, rng, push), R.N, rule) for _ in range(M)]
    return summarize(rows)


def fmt(S, keys):
    return "  ".join("%s=%+.4f(%.4f)" % (k, S[k][0], S[k][1]) for k in keys)


# ---------------------------------------------------------------- exact two-site pieces
def joint_pair(R, i, k, delta=0.0, first=None, push=True, mi=Z, mk=Z):
    """exact joint odds P(a, b) of records at sites i (menu mi) and k (menu mk).
    first=None: both form at once.  first=i: i forms, the change runs for delta, then k forms (and vice versa)."""
    P = {}
    if first is None:
        for a in (1, -1):
            v = R.project(R.gs, i, mi, a)
            for b in (1, -1):
                w = R.project(v, k, mk, b)
                P[(a, b)] = float(np.vdot(w, w).real)
        return P
    (x, mx), (y, my) = ((i, mi), (k, mk)) if first == i else ((k, mk), (i, mi))
    for a in (1, -1):
        v = R.project(R.gs, x, mx, a)
        pa = float(np.vdot(v, v).real)
        v = v / np.sqrt(pa)
        v = R.evolve(v, {x: a * mx}, delta, push)
        for b in (1, -1):
            w = R.project(v, y, my, b)
            pb = float(np.vdot(w, w).real)
            P[(a, b) if first == i else (b, a)] = pa * pb
    return P


def tv(P, Q):
    return 0.5 * sum(abs(P[k] - Q[k]) for k in P)


def corr(P):
    return sum(a * b * p for (a, b), p in P.items())


# ---------------------------------------------------------------- probes
def probe_A():
    print("=== PROBE A: two neighbouring records -- at once vs one right after the other ===")
    for N in (8, 10):
        R = Ring(N)
        c = float(np.vdot(R.gs, R.ops[0][2] @ (R.ops[1][2] @ R.gs)).real)
        print("\nN = %d ring; gap above the preparation = %.4f; neighbour z-correlation of the preparation c = %+.6f" % (N, R.gap, c))
        Psim = joint_pair(R, 0, 1)
        P0 = joint_pair(R, 0, 1, 0.0, first=0)
        P1 = joint_pair(R, 0, 1, 0.0, first=1)
        print("[fixed menu] at once:            P(++,+-,-+,--) = %s  corr = %+.6f" % ([round(Psim[k], 6) for k in sorted(Psim, reverse=True)], corr(Psim)))
        print("[fixed menu] 0 then 1, no gap:   TV distance to 'at once' = %.2e ; 1 then 0: %.2e" % (tv(P0, Psim), tv(P1, Psim)))
        for push in (True, False):
            lab = "push" if push else "drop"
            for d in (0.1, 0.3, 1.0, 3.0, 10.0):
                Pg = joint_pair(R, 0, 1, d, first=0, push=push)
                Pr = joint_pair(R, 0, 1, d, first=1, push=push)
                print("[fixed menu, %s] 0 then 1 after gap %5.1f/J: corr = %+.4f  TV to 'at once' = %.4f ; order reversed TV = %.2e" % (lab, d, corr(Pg), tv(Pg, Psim), tv(Pg, Pr)))
        # own-state / neighbour-set menu, no gap
        rng = np.random.default_rng(1)
        K = 20000
        acc_sim = 0.0
        for _ in range(K):
            m0, m1 = rand_axis(rng), rand_axis(rng)
            P = joint_pair(R, 0, 1, mi=m0, mk=m1) if N <= 8 else None
            if P is None:
                break
            acc_sim += corr(P) * (m0 @ m1)
        if N <= 8:
            print("[own-state menu] at once: axes independent -> content correlation E[n0 . n1] = %+.4f (closed form c/3 = %+.4f); aligned pairs 0" % (acc_sim / K, c / 3))
        # sequential: first axis random (undecided site), the neighbour's own part then points along it
        m0 = rand_axis(rng)
        v = R.project(R.gs, 0, m0, 1)
        v /= np.linalg.norm(v)
        r1 = R.bloch(v, 1)
        cosang = abs(r1 @ m0) / np.linalg.norm(r1)
        print("[own-state menu] 0 then 1, no gap: after record +m0, site 1's own part = %+.4f m0 (|cos| = %.12f) -> same axis; content correlation = c = %+.4f; aligned pairs 1" % (r1 @ m0, cosang, c))


def probe_B1():
    print("=== PROBE B1 (exact): does the timing of two records matter at a distance?  N = 12 ring, sites 0 and d ===")
    R = Ring(12)
    print("gap above the preparation = %.4f" % R.gap)
    for d in range(1, 7):
        cz = float(np.vdot(R.gs, R.ops[0][2] @ (R.ops[d][2] @ R.gs)).real)
        Psim = joint_pair(R, 0, d)
        line = "d=%d  preparation corr %+.4f | TV(0 first after gap g, vs at once):" % (d, cz)
        for g in (0.05, 0.1, 0.2, 0.3, 0.5, 1.0):
            Pg = joint_pair(R, 0, d, g, first=0)
            line += "  g=%.2f: %.4f" % (g, tv(Pg, Psim))
        Pg = joint_pair(R, 0, d, 2.0, first=0)
        Pr = joint_pair(R, 0, d, 2.0, first=d)
        line += " | order reversed (g=2) TV %.1e" % tv(Pg, Pr)
        print(line, flush=True)


def probe_B2(M):
    N, Tbar = 8, 1.0
    R = Ring(N)
    print("=== PROBE B2 (Monte Carlo, %d histories each): one universe-wide tick vs local timing, N = %d ring, mean wait %.1f/J per site ===" % (M, N, Tbar))
    p = 0.5
    tau = tick_tau(p, Tbar)
    half = list(range(N // 2)), list(range(N // 2, N))
    scheds = {
        "universe-wide ticks (p=0.5)": lambda rng: sched_ticks(N, p, tau, rng, [list(range(N))]),
        "patch ticks (two halves)":    lambda rng: sched_ticks(N, p, tau, rng, [half[0], half[1]]),
        "each site its own ticks":     lambda rng: sched_ticks(N, p, tau, rng, [[j] for j in range(N)]),
        "random times (Poisson)":      lambda rng: sched_poisson(N, Tbar, rng),
        "all at one tick (p=1)":       lambda rng: sched_ticks(N, 1.0, tick_tau(1.0, Tbar), rng, [list(range(N))]),
    }
    res = {}
    for rule in ("fixed", "own", "field"):
        print("\n-- menu rule: %s" % rule, flush=True)
        for i, (name, mk) in enumerate(scheds.items()):
            t0 = time.time()
            S = mc(R, mk, rule, M, seed=1000 + 17 * i + {"fixed": 0, "own": 1, "field": 2}[rule])
            res[(rule, name)] = S
            keys = ["c1", "c2", "c3", "c4"] if rule == "fixed" else ["v1", "a1", "naxes"]
            extra = ""
            if rule == "fixed" and name.startswith("patch"):
                b = S["bond"]
                seam = [3, 7]
                inner = [j for j in range(N) if j not in seam]
                extra = "  [seam bonds %+.4f, inside bonds %+.4f]" % (np.mean([b[j][0] for j in seam]), np.mean([b[j][0] for j in inner]))
            print("  %-30s %s%s  [%.0fs]" % (name, fmt(S, keys), extra, time.time() - t0), flush=True)
    return res


def probe_C(M):
    N = 8
    R = Ring(N)
    c_prep = [float(np.vdot(R.gs, R.ops[0][2] @ (R.ops[r][2] @ R.gs)).real) for r in range(1, N // 2 + 1)]
    print("=== PROBE C (Monte Carlo, %d histories each): does the pace matter?  random (Poisson) times, fixed menu, N = %d ===" % (M, N))
    print("preparation correlations c1..c4 = %s  (what records copy if they all form before any change)" % [round(x, 4) for x in c_prep])
    for push in (True, False):
        print("\n-- recorded sites %s" % ("push their neighbours" if push else "drop out of the change"), flush=True)
        for Tbar in (0.03, 0.1, 0.3, 1.0, 3.0, 10.0):
            t0 = time.time()
            S = mc(R, lambda rng, T=Tbar: sched_poisson(N, T, rng), "fixed", M, seed=int(5000 + 100 * Tbar) + (0 if push else 1), push=push)
            print("  mean wait %5.2f/J (pace gamma/J = %6.2f): %s  [%.0fs]" % (Tbar, 1 / Tbar, fmt(S, ["c1", "c2", "c3", "c4"]), time.time() - t0), flush=True)


def probe_D(M):
    N, Tbar = 8, 1.0
    R = Ring(N)
    print("=== PROBE D (Monte Carlo, %d histories each): does 'one landing encourages another' leave a mark?  N = %d, mean wait %.1f/J per site ===" % (M, N, Tbar))
    rng = np.random.default_rng(7)
    cal = {}
    for kappa in (0.0, 3.0, 30.0):
        ts, gaps = [], []
        for _ in range(20000):
            s = sched_triggered(N, 1.0, kappa, rng)
            t = {j: tt for tt, g in s for j in g}
            ts.append(np.mean(list(t.values())))
            gaps.append(np.mean([abs(t[j] - t[(j + 1) % N]) for j in range(N)]))
        m = float(np.mean(ts))
        g0 = m / Tbar                      # rescale all rates so the mean per-site time is Tbar
        cal[kappa] = (g0, kappa * g0, float(np.mean(gaps)) / g0)
        print("  trigger strength %4.0fx: base rate %.4f, boosted rate per recorded neighbour %.4f; mean time gap between neighbours %.3f/J" % (kappa, *cal[kappa]))
    for rule in ("fixed", "field", "own"):
        print("\n-- menu rule: %s" % rule, flush=True)
        for kappa, (g0, g1, _) in cal.items():
            t0 = time.time()
            S = mc(R, lambda rng, a=g0, b=g1: sched_triggered(N, a, b, rng), rule, M, seed=9000 + int(kappa) + {"fixed": 0, "own": 1, "field": 2}[rule])
            keys = ["c1", "c2", "c3", "c4"] if rule == "fixed" else ["v1", "a1", "naxes"]
            print("  trigger %4.0fx: %s  [%.0fs]" % (kappa, fmt(S, keys), time.time() - t0), flush=True)


if __name__ == "__main__":
    which = sys.argv[1]
    M = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    t0 = time.time()
    {"A": probe_A, "B1": probe_B1}.get(which, lambda: None)()
    if which == "B2":
        probe_B2(M)
    elif which == "C":
        probe_C(M)
    elif which == "D":
        probe_D(M)
    print("[total %.0fs]" % (time.time() - t0))
