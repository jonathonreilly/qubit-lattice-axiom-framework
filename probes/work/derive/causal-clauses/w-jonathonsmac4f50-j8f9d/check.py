#!/usr/bin/env python3
"""causal-clauses, attempt a2: exact checks for ATTEMPT.md.

Setting (block 01's records-only formation law, block 14's clocks, block 15's joint units, block 24's unrecorded sites): six-axis
menu (value index = direction, order +x,-x,+y,-y,+z,-z), product rule phi = p, q, r for equal, opposite, orthogonal values,
K(b, a) = phi/Z1, r(a | A) = prod_{y in A} K(v_y, a) / K_|A|(v_A), r(a | {}) = 1/6.  The causal event lattice is level-ordered Z^3
(level x1 + x2 + x3; the parents of x are x - e_i): every nearest-neighbour pair is a parent-child pair, and two sites of one level are
never neighbours.  A window is a finite set of sites with the induced parent structure; its causal law is
prod_x r(v_x | v_{parents in the window}).

Sections (step numbers of ATTEMPT.md in brackets):
 A  (a) causal policies: every value-dependent clock law restricted to formable sites, and every value-dependent choice of antichain
    units formed jointly by block 15's rule-consistent law, finishes in the causal law, exactly, on six windows [S1-S4];
 B  (b) block 14's executed clock laws (uniform, seeded, attracting, parallel growth), block 15's covariant unit and whole-window
    (static) readings, block 24's integrated exterior: exact total variations from the causal law on the three-site windows (the
    smallest windows where any clause can act) and on the oriented plaquette [S5-S7];
 C  (c) the unrecorded-site fork: on down-closed windows the free window equals the integrated (causal) exterior; the static exterior
    acts backward in level time [S8].
"""
import itertools
import random
import sys
import time
from fractions import Fraction as F
from itertools import permutations, product

FAILS = []
T0 = time.time()
M = 6
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
IDX = {d: i for i, d in enumerate(STEPS)}


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


def rel(a, b):
    return 0 if a == b else (1 if a // 2 == b // 2 else 2)


class Rule:
    def __init__(self, p, q, r):
        self.p, self.q, self.r = p, q, r
        self.w = (p, q, r)
        self.Z1 = p + q + 4 * r
        self.phi = [[self.w[rel(a, b)] for b in range(M)] for a in range(M)]
        self.K = [[F(self.phi[a][s], self.Z1) for s in range(M)] for a in range(M)]
        self._c = {}

    def __repr__(self):
        return f"({self.p},{self.q},{self.r})"

    def Kk(self, vals):
        t = F(0)
        for s in range(M):
            u = F(1)
            for v in vals:
                u *= self.K[v][s]
            t += u
        return t

    def cond(self, rec, a):
        key = (rec, a)
        if key not in self._c:
            if not rec:
                self._c[key] = F(1, M)
            else:
                num = F(1)
                for v in rec:
                    num *= self.K[v][a]
                self._c[key] = num / self.Kk(rec)
        return self._c[key]


def add(x, d):
    return tuple(x[i] + d[i] for i in range(3))


class Window:
    def __init__(self, name, sites):
        self.name, self.sites = name, list(sites)
        self.n = len(self.sites)
        self.pos = {x: i for i, x in enumerate(self.sites)}
        self.par = [[self.pos[add(x, (-d[0], -d[1], -d[2]))] for d in STEPS[0::2] if add(x, (-d[0], -d[1], -d[2])) in self.pos] for x in self.sites]
        self.nb = [[self.pos[add(x, d)] for d in STEPS if add(x, d) in self.pos] for x in self.sites]
        self.edges = sorted({tuple(sorted((i, j))) for i in range(self.n) for j in self.nb[i]})
        # sanity: every neighbour pair is a parent-child pair (levels differ by one)
        lev = [sum(x) for x in self.sites]
        assert all(abs(lev[i] - lev[j]) == 1 for i, j in self.edges)

    def pats(self):
        return product(range(M), repeat=self.n)


def causal_law(W, R):
    return {v: _prod(R.cond(tuple(sorted(v[j] for j in W.par[i])), v[i]) for i in range(W.n)) for v in W.pats()}


def _prod(it):
    t = F(1)
    for x in it:
        t *= x
    return t


def seq_law_given_order(W, R, order, v):
    """block 01's law of one order: each site draws given its recorded neighbours (any direction)"""
    done, pr = set(), F(1)
    for i in order:
        rec = tuple(sorted(v[j] for j in W.nb[i] if j in done))
        pr *= R.cond(rec, v[i])
        done.add(i)
    return pr


def clock_law(W, R, rate):
    """block 14's clock model: rate(i, done, v) >= 0 for unrecorded i; the finished law, exactly (sum over formation sequences)"""
    law = {}
    for v in W.pats():
        tot = F(0)
        for order in permutations(range(W.n)):
            done, pr = set(), F(1)
            for i in order:
                lam = {j: rate(j, frozenset(done), v) for j in range(W.n) if j not in done}
                s = sum(lam.values())
                if s == 0 or lam[i] == 0:
                    pr = F(0)
                    break
                pr *= F(lam[i]) / s
                pr *= R.cond(tuple(sorted(v[j] for j in W.nb[i] if j in done)), v[i])
                done.add(i)
            tot += pr
        law[v] = tot
    return law


def static_law(W, R):
    w = {v: _prod(R.phi[v[i]][v[j]] for i, j in W.edges) for v in W.pats()}
    Z = sum(w.values())
    return {v: F(x, Z) for v, x in w.items()}


def tv(a, b):
    return sum((abs(a[v] - b[v]) for v in a), F(0)) / 2


def joint_unit(W, R, unit, done, v):
    """block 15's joint law of a unit given the recorded sites (U1: product of phi over the unit's internal edges and its edges to
    recorded sites, normalized), evaluated at v"""
    unit = list(unit)
    def weight(vals):
        t = 1
        for a_, i in enumerate(unit):
            for j in W.nb[i]:
                if j in done:
                    t *= R.phi[vals[a_]][v[j]]
                elif j in unit and unit.index(j) > a_:
                    t *= R.phi[vals[a_]][vals[unit.index(j)]]
        return t
    Z = sum(weight(vals) for vals in product(range(M), repeat=len(unit)))
    return F(weight([v[i] for i in unit]), Z)


def unit_policy_law(W, R, choose):
    """units chosen by choose(done, v) -> list of (unit, probability); each unit formed jointly by joint_unit"""
    law = {}
    for v in W.pats():
        def rec(done):
            if len(done) == W.n:
                return F(1)
            t = F(0)
            for unit, pr in choose(frozenset(done), v):
                t += pr * joint_unit(W, R, unit, done, v) * rec(done | set(unit))
            return t
        law[v] = rec(frozenset())
    return law


WINDOWS = [
    Window("chain x->y->z (bent)", [(0, 0, 0), (1, 0, 0), (1, 1, 0)]),
    Window("chain x->y->z (straight)", [(0, 0, 0), (1, 0, 0), (2, 0, 0)]),
    Window("V x->y<-z", [(0, 1, 0), (1, 0, 0), (1, 1, 0)]),
    Window("Lambda x<-y->z", [(1, 0, 0), (0, 0, 0), (0, 1, 0)]),
    Window("plaquette (diamond)", [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)]),
    Window("claw (three parents)", [(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]),
]
R312, R512 = Rule(3, 1, 2), Rule(5, 1, 2)


# ============================================================================================ A
def section_A():
    print("=" * 100)
    print("A  (a) causal clock laws and antichain units finish in the causal law")
    rng = random.Random(20260919)
    ok_topo = ok_clock = ok_unit = True
    n_pol = 0
    for W in WINDOWS:
        for R in (R312, R512):
            C = causal_law(W, R)
            # the GIVEN: every linear extension
            lin = [o for o in permutations(range(W.n)) if all(o.index(p) < o.index(i) for i in range(W.n) for p in W.par[i])]
            for o in lin:
                ok_topo &= all(seq_law_given_order(W, R, o, v) == C[v] for v in W.pats())
            # random value-dependent clocks restricted to formable sites
            for _ in range(3):
                table = {}
                def rate(i, done, v, table=table):
                    if any(p not in done for p in W.par[i]):
                        return 0
                    key = (i, done, tuple(v[j] for j in sorted(done)))
                    if key not in table:
                        table[key] = rng.randint(1, 9)
                    return table[key]
                L = clock_law(W, R, rate)
                ok_clock &= all(L[v] == C[v] for v in L)
                n_pol += 1
            # random value-dependent antichain units of formable sites
            for _ in range(2):
                memo = {}
                def choose(done, v, memo=memo):
                    key = (done, tuple(v[j] for j in sorted(done)))
                    if key not in memo:
                        formable = [i for i in range(W.n) if i not in done and all(p in done for p in W.par[i])]
                        units = [u for k in range(1, len(formable) + 1) for u in itertools.combinations(formable, k)]
                        units = [u for u in units if all(j not in W.nb[i] for i in u for j in u)]
                        wts = [rng.randint(1, 5) for _ in units]
                        s = sum(wts)
                        memo[key] = [(u, F(w, s)) for u, w in zip(units, wts)]
                    return memo[key]
                L = unit_policy_law(W, R, choose)
                ok_unit &= all(L[v] == C[v] for v in L)
                n_pol += 1
    check("A1", ok_topo, "the GIVEN re-checked: every linear extension of six windows gives the causal law exactly, at (3,1,2) and (5,1,2)")
    check("A2", ok_clock and ok_unit, f"{n_pol} random value-dependent policies (clocks with random integer rates keyed by the recorded set and "
          "values, zero on non-formable sites; random antichain units of formable sites, formed by block 15's rule-consistent joint law) "
          "on six windows and two rules: every finished law equals the causal law exactly")


# ============================================================================================ B
def block14_rates(W):
    uniform = lambda i, done, v: 1
    seeded = lambda i, done, v: 1 if (not done or any(j in done for j in W.nb[i])) else 0
    attracting = lambda i, done, v: 1 + sum(1 for j in W.nb[i] if j in done)
    def parallel(i, done, v):
        x = W.sites[i]
        hit = 0
        for j in W.nb[i]:
            if j in done:
                y = W.sites[j]
                d = tuple(x[k] - y[k] for k in range(3))
                if v[j] == IDX[d]:
                    hit = 1
        return 1 + hit
    return {"uniform": uniform, "seeded": seeded, "attracting": attracting, "parallel growth": parallel}


def section_B():
    print("=" * 100)
    print("B  (b) the recorded clause candidates against the causal law")
    R = R312
    rows = {}
    ok = True
    expect = {("V x->y<-z", "static"): F(1, 72), ("V x->y<-z", "uniform"): F(1, 108), ("V x->y<-z", "seeded"): F(1, 72),
              ("V x->y<-z", "attracting"): F(7, 648), ("chain x->y->z (bent)", "uniform"): F(1, 216),
              ("chain x->y->z (bent)", "attracting"): F(1, 324), ("chain x->y->z (bent)", "seeded"): F(0),
              ("chain x->y->z (bent)", "static"): F(0), ("Lambda x<-y->z", "static"): F(0), ("Lambda x<-y->z", "seeded"): F(0)}
    for W in WINDOWS[:5]:
        C = causal_law(W, R)
        res = {}
        for name, rate in block14_rates(W).items():
            res[name] = tv(clock_law(W, R, rate), C)
        res["static"] = tv(static_law(W, R), C)
        rows[W.name] = res
        for (wn, cand), val in expect.items():
            if wn == W.name:
                ok &= res[cand] == val
    # block 15's covariant unit on the V: the domino {x, y} formed jointly after z
    V = WINDOWS[2]
    C = causal_law(V, R)
    xi, zi, yi = 0, 1, 2
    dom = {}
    for v in V.pats():
        dom[v] = R.cond((), v[zi]) * joint_unit(V, R, (xi, yi), {zi}, v)
    tv_dom = tv(dom, C)
    ok &= tv_dom == F(1, 72) and tv(dom, static_law(V, R)) == 0
    # block 24's integrated exterior under the static law: x, z recorded, y their unrecorded common child
    mxz_static = {}
    S = static_law(V, R)
    for v in V.pats():
        mxz_static[(v[xi], v[zi])] = mxz_static.get((v[xi], v[zi]), F(0)) + S[v]
    Mfac = sorted({int(144 * R.Kk((a, b))) for a in range(M) for b in range(M)})
    tv_ext = sum((abs(mxz_static[(a, b)] - F(1, 36)) for a in range(M) for b in range(M)), F(0)) / 2
    ok &= tv_ext == F(1, 72) and Mfac == [22, 24, 26]
    for wn, res in rows.items():
        print(f"     {wn}: " + ", ".join(f"{k} {v}" for k, v in res.items()))
    check("B1", ok, "exact TVs from the causal law at (3,1,2): on the V (one site with two parents) static 1/72, uniform clocks 1/108, seeded 1/72, "
          "attracting 7/648; on the bent chain uniform 1/216, attracting 1/324, seeded and static 0 (a tree formed along the chain); "
          f"block 15's domino unit {{x, y}} formed after z on the V: {tv_dom} (it is the static law there); block 24's static exterior (y "
          f"unrecorded, integrated): TV {tv_ext} with the factor 144 K_2(v_x, v_z) in {Mfac}")
    # two-site windows: nothing can act (every site has at most one recorded neighbour)
    D = Window("domino", [(0, 0, 0), (1, 0, 0)])
    C = causal_law(D, R)
    two = all(tv(clock_law(D, R, rate), C) == 0 for rate in block14_rates(D).values()) and tv(static_law(D, R), C) == 0
    check("B2", two, "on every two-site window each candidate gives the causal law (both orders give each site at most one recorded "
          "neighbour): three sites is the smallest window where any clause acts")
    return rows


# ============================================================================================ C
def section_C():
    print("=" * 100)
    print("C  (c) the unrecorded-site fork on down-closed windows")
    R = R312
    ok = True
    for W in WINDOWS:
        C = causal_law(W, R)
        # every down-closed subset S: the marginal of the causal law on S equals the causal law of the sub-window
        for k in range(1, W.n):
            for S in itertools.combinations(range(W.n), k):
                if not all(p in S for i in S for p in W.par[i]):
                    continue
                marg = {}
                for v in W.pats():
                    key = tuple(v[i] for i in S)
                    marg[key] = marg.get(key, F(0)) + C[v]
                sub = Window("sub", [W.sites[i] for i in S])
                Cs = causal_law(sub, R)
                ok &= all(marg[key] == Cs[key] for key in marg)
    check("C1", ok, "on six windows, for every down-closed (ancestor-closed) subset S, the marginal of the causal law on S equals the "
          "free-window causal law of S: integrating unrecorded (later) sites under the causal law changes nothing")


def main():
    section_A()
    section_B()
    section_C()
    print("=" * 100)
    print(f"runtime {time.time() - T0:.0f}s")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("on a causal event lattice (every parent recorded before its child, no record re-formed) every clock law acting on formable "
            "sites (any rates, value-dependent included) and every antichain-unit clause finish in the product of one-site kernels given "
            "parents; the recorded candidates that change the law are exactly those that let a child form before a parent or condition "
            "on unformed sites: block 14's executed clocks (uniform 1/108, seeded 1/72, attracting 7/648 on the V at (3,1,2)), block 15's "
            "units with a parent-child pair and the whole-window (static) unit (1/72 on the V), block 24's static exterior (1/72); none "
            "re-forms records; on down-closed windows the free window and the integrated exterior coincide, so causality settles block 24's fork")
    print("SUMMARY: PROVED (ATTEMPT.md S1-S8, finite facts CHECKED here) " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
