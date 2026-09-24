#!/usr/bin/env python3
"""Do records fall with a universal weight: checks for ATTEMPT.md (attempt 1 of 2), worker w-macbookpro9927a-j4d29 (claude-opus-5-5).

Objects (block 95, PR #8860): records hop x -> x+e at rate w_x^a w_{x+e}^(1-a) h/6, h = W(C')/(W(C) + W(C')), W the product of the
pair weights over occupied bonds (block 40's working values c0 omega = 3/2, 1/2, 1 for equal, opposite, orthogonal contents, as quoted in
block 104). A uniform gradient: u = log w = g.x, held fixed. A cluster: n records whose relative configuration sigma ranges over a finite
set; X its centre. Everything exact: sympy rationals and symbols; the cluster chains are solved by exact linear algebra.
"""
from __future__ import annotations

import itertools
import json
import subprocess
import sys

import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


R = sp.Rational
B95 = ("f9b34475df", "docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_"
       "OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md",
       ["A move `C → C'` takes a record at `x` to an empty neighbour `y`, with heat-bath factor `h = W(C')/(W(C) + W(C'))`.",
        "A move `x → y` runs at the rate `w_x^a w_y^(1−a) · h / 6`",
        "*Statement.* In a rate field `w` that does not depend on the configuration, the chain of P1 and P3 is in detailed balance with "
        "`π(C) = W(C) Π_{z∈C} w_z^(1−2a)`.",
        "In a fixed field on the infinite lattice, with rates bounded above and below and no other record in the way, a lone record's "
        "position is a martingale: its expected position never moves.",
        "`W(C) > 0` is the motion rule's weight: block 39's (#8530) product of the rule's pair weights over occupied bonds, or `W ≡ 1` "
        "for records with exclusion only."])
B104 = ("705d466f49", "docs/ADMISSIBILITY_RULE_THE_RULES_OWN_CLOCK_HAS_NO_FAR_FIELD_THE_PULL_NEEDS_A_RATE_LAW_WITH_A_MONOPOLE_A_REST_"
        "ENERGY_AND_A_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-23.md",
        ["the pair weights are `c₀ω = 3/2, 1/2, 1` for equal, opposite and orthogonal contents"])
TASK_Q = ["(a) the drift velocity of a record in a uniform gradient of u as a function of its content and of the neighbourhood (isolated "
          "vs in a cluster), exactly at first order; (b) whether two records of different content (or a record and a pair) acquire the "
          "same drift per unit gradient - a universal weight - or not."]


def family_q() -> None:
    miss = []
    for tag, (sha, path, qs) in (("b95", B95), ("b104", B104)):
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"{tag}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:do-records-fall-with-a-universal-weight:a1"), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, f"block 95 (head f9b34475), block 104's pair-weight line and the task quoted verbatim ({len(B95[2]) + 2} lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
OMEGA = {"equal": R(3, 2), "opposite": R(1, 2), "orthogonal": R(1)}


def add(u, v, s=1):
    return tuple(a + s * b for a, b in zip(u, v))


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


# ------------------------------------------------------------------------------------------------ L: one record's local drift
def family_l() -> None:
    g1, g2, g3, a = sp.symbols("g1 g2 g3 a")
    g = (g1, g2, g3)
    ok = True
    res = {}
    for label, occ in (("isolated", None), *[(k, k) for k in OMEGA]):
        # record at 0; one neighbour at +e1 of the given content relation (all its five moves break that bond), or none
        v = [0, 0, 0]
        for e in E6:
            if occ is not None and e == (1, 0, 0):
                continue
            h = R(1, 2) if occ is None else 1 / (1 + OMEGA[occ])
            rate = sp.exp((1 - a) * dot(g, e)) * h / 6          # w_0 = 1 at the record's own site
            v = [v[k] + e[k] * rate for k in range(3)]
        s = [sp.expand(sp.series(vk.subs({g1: sp.Symbol("s") * g1, g2: sp.Symbol("s") * g2, g3: sp.Symbol("s") * g3}), sp.Symbol("s"), 0, 2)
                       .removeO().subs(sp.Symbol("s"), 1)) for vk in v]
        h = R(1, 2) if occ is None else 1 / (1 + OMEGA[occ])
        M = sp.eye(3) * 2 * h - (sp.zeros(3, 3) if occ is None else sp.diag(h, 0, 0))
        b0 = [0, 0, 0] if occ is None else [-h / 6, 0, 0]
        want = [b0[k] + (1 - a) / 6 * sum(M[k, j] * g[j] for j in range(3)) for k in range(3)]
        ok &= all(sp.expand(s[k] - want[k]) == 0 for k in range(3))
        ok &= all(sp.expand(s[k].subs(a, 1) - b0[k]) == 0 for k in range(3))     # a = 1: no gradient term at all
        res[label] = (h, M)
    check("L", ok, "a record's mean velocity at its site (w = 1) is b(C) + ((1 - a)/6) M(C) g + O(g^2), M = sum over free moves of h e e^T: "
          "isolated M = I (h = 1/2, any content); one neighbour of equal/opposite/orthogonal content: h = 2/5, 2/3, 1/2 on its five moves, "
          "M = h(2I - e1 e1^T), contact bias b = -(h/6) e1; at a = 1 the gradient term vanishes identically")


# ------------------------------------------------------------------------------------------------ the cluster chains
class Cluster:
    """finite internal chain: states sigma, moves (target, record i, e, q0, r_i); centre moves by e/n."""

    def __init__(self, n, states, moves, W):
        self.n, self.states, self.moves, self.W = n, states, moves, W
        self.ix = {s: i for i, s in enumerate(states)}

    def gen(self, weight):
        N = len(self.states)
        L = sp.zeros(N, N)
        for s in self.states:
            for (t, i, e, q0, r) in self.moves[s]:
                val = q0 * weight(i, e, r)
                L[self.ix[s], self.ix[t]] += val
                L[self.ix[s], self.ix[s]] -= val
        return L


def stationary(L, rhs_extra=None, p0=None):
    N = L.shape[0]
    A = L.T.copy()
    A[N - 1, :] = sp.ones(1, N)
    b = sp.zeros(N, 1)
    if rhs_extra is None:
        b[N - 1] = 1
    else:
        b = -rhs_extra
        b[N - 1] = 0
    return A.LUsolve(b)


def poisson(L, f, p0):
    N = L.shape[0]
    A = -L
    A[N - 1, :] = p0.T
    b = f.copy()
    b[N - 1] = 0
    return A.LUsolve(b)


def cluster_response(cl: Cluster, a, ghat):
    """first-order centre velocity V1 (per unit g along ghat) and the diffusion tensor D0, exactly."""
    n = cl.n
    N = len(cl.states)
    L0 = cl.gen(lambda i, e, r: 1)
    p0 = stationary(L0)
    L1 = cl.gen(lambda i, e, r: dot(ghat, r) + (1 - a) * dot(ghat, e))
    p1 = stationary(L0, rhs_extra=(p0.T * L1).T)
    V1 = [0, 0, 0]
    for s in cl.states:
        k = cl.ix[s]
        for (t, i, e, q0, r) in cl.moves[s]:
            for c in range(3):
                V1[c] += (p1[k] * q0 + p0[k] * q0 * (dot(ghat, r) + (1 - a) * dot(ghat, e))) * R(e[c], n)
    V1 = [sp.nsimplify(v) for v in V1]
    # D0 from the second order of the principal eigenvalue of the tilted generator at g = 0
    def lam2(k):
        f = sp.zeros(N, 1)
        for s in cl.states:
            f[cl.ix[s]] = sum(q0 * R(dot(k, e), n) for (t, i, e, q0, r) in cl.moves[s])
        psi = poisson(L0, f, p0)
        tot = 0
        for s in cl.states:
            for (t, i, e, q0, r) in cl.moves[s]:
                ke = R(dot(k, e), n)
                tot += p0[cl.ix[s]] * q0 * (ke ** 2 / 2 + ke * psi[cl.ix[t]])
        return sp.nsimplify(tot)
    D = sp.zeros(3, 3)
    for i in range(3):
        ei = tuple(1 if j == i else 0 for j in range(3))
        D[i, i] = lam2(ei)
    for i, j in ((0, 1), (0, 2), (1, 2)):
        eij = tuple(1 if m in (i, j) else 0 for m in range(3))
        D[i, j] = D[j, i] = (lam2(eij) - D[i, i] - D[j, j]) / 2
    return V1, D, p0


def lone() -> Cluster:
    st = [()]
    mv = {(): [((), 0, e, R(1, 12), (0, 0, 0)) for e in E6]}
    return Cluster(1, st, mv, {(): R(1)})


def tethered_pair(omega) -> Cluster:
    NN = [e for e in E6]
    FD = [tuple(v) for v in set(itertools.product((-1, 0, 1), repeat=3)) if sum(abs(x) for x in v) == 2 and max(abs(x) for x in v) == 1]
    S = NN + sorted(FD)
    Sset = set(S)
    W = {d: (omega if d in NN else R(1)) for d in S}
    mv = {}
    for d in S:
        lst = []
        for i in (0, 1):
            for e in E6:
                d2 = add(d, e, -1) if i == 0 else add(d, e, 1)
                if d2 in Sset:
                    h = W[d2] / (W[d] + W[d2])
                    r = tuple(R(-x, 2) for x in d) if i == 0 else tuple(R(x, 2) for x in d)
                    lst.append((d2, i, e, h / 6, r))
        mv[d] = lst
    return Cluster(2, S, mv, W)


def family_c() -> dict:
    ok = True
    out = {}
    for a in (R(1), R(3, 4), R(0)):
        for name, cl in [("lone", lone())] + [(f"pair-{k}", tethered_pair(w)) for k, w in OMEGA.items()]:
            c = (2 * a - 1) * cl.n - 1
            for ghat in ((1, 0, 0), (1, 2, 3)):
                V1, D, p0 = cluster_response(cl, a, ghat)
                want = [-c * sum(D[k, j] * ghat[j] for j in range(3)) for k in range(3)]
                ok &= all(sp.simplify(V1[k] - want[k]) == 0 for k in range(3))
            ok &= D == D[0, 0] * sp.eye(3)
            # the stationary law at g = 0 is W / Z
            Z = sum(cl.W[s] for s in cl.states)
            ok &= all(p0[cl.ix[s]] == cl.W[s] / Z for s in cl.states)
            out[(name, a)] = D[0, 0]
    check("C", ok, "first-order centre velocity in tau time V1 = -((2a - 1)n - 1) D0 g for the lone record and the tethered pair (18 relative "
          "states, contact weight 3/2, 1/2, 1) at a = 1, 3/4, 0, g along x and along (1,2,3); D0 isotropic; p0 = W/Z. "
          f"D0: lone {out[('lone', R(1))]}, pairs {out[('pair-equal', R(1))]}, {out[('pair-opposite', R(1))]}, {out[('pair-orthogonal', R(1))]}")
    return out


def family_i() -> None:
    """the tilted invariant measure W(sigma) exp(-c g.X) of the tau chain: every move balances, symbolically in g and a."""
    g1, g2, g3, a = sp.symbols("g1 g2 g3 a")
    g = (g1, g2, g3)
    ok = True
    for cl in (lone(), tethered_pair(R(3, 2))):
        n = cl.n
        c = (2 * a - 1) * n - 1
        for s in cl.states:
            for (t, i, e, q0, r) in cl.moves[s]:
                back = [m for m in cl.moves[t] if m[0] == s and m[1] == i and m[2] == tuple(-x for x in e)]
                ok &= len(back) == 1
                (_, _, eb, qb, rb) = back[0]
                lhs = sp.log(cl.W[s] * q0) + dot(g, r) + (1 - a) * dot(g, e)
                rhs = sp.log(cl.W[t] * qb) - c * dot(g, tuple(R(x, n) for x in e)) + dot(g, rb) + (1 - a) * dot(g, eb)
                ok &= sp.simplify(sp.expand_log(lhs - rhs, force=True)) == 0
    check("I", ok, "the tau-time chain (rates divided by the centre's clock w(X)) is in detailed balance with W(sigma) exp(-c g.X), c = (2a - 1)n - 1, "
          "move by move, symbolic in g and a (lone record and tethered pair): so Lambda(0) = Lambda(c g) = 0 for its tilted generator")


def family_x() -> None:
    """a = 1, exclusion only, two records in contact along the gradient: the instantaneous centre velocity points up the gradient."""
    g = sp.Symbol("g")
    # records at 0 and e1, W = 1 (h = 1/2), rates w/12; w = exp(g x1)
    v1 = -R(1, 12) * 1                   # record at 0: pushed to -e1 on balance, clock w = 1
    v2 = R(1, 12) * sp.exp(g)            # record at e1: pushed to +e1, clock exp(g)
    V = (v1 + v2) / 2
    ok = sp.expand(sp.series(V, g, 0, 2).removeO() - g / 24) == 0
    check("X", ok, "a = 1, exclusion only, two records in contact along the gradient: instantaneous centre velocity (e^g - 1)/24, up the "
          "gradient (the faster record is pushed off more often), although a bound pair's long-time drift is down the gradient")


def main() -> int:
    family_q()
    family_l()
    family_i()
    out = family_c()
    family_x()
    print("Do records fall with a universal weight - checks; worker w-macbookpro9927a-j4d29 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {len(OUT) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    d = [out[(k, R(1))] for k in ("pair-equal", "pair-opposite", "pair-orthogonal")]
    print("SUMMARY: PARTIAL exact at first order in a uniform gradient u = g.x (block 95's chain, timing a): (i) one record at its site moves "
          "with b(C) + ((1 - a)/6) M(C) g, M = sum of h e e^T over its free moves (content and neighbours enter through h and exclusion; at "
          "a = 1 no gradient term at all); (ii) the equilibrium weight is (2a - 1) per record, content-blind; (iii) a cluster of n records "
          "whose relative configuration stays in a finite set has long-time centre velocity -((2a - 1)n - 1) D_cm g per tick of the clock at "
          "its centre, D_cm its field-free diffusion constant, from the two zeros Lambda(0) = Lambda(((2a - 1)n - 1)g) = 0 of its tilted "
          f"generator; at a = 1 a lone record does not fall and a bound pair falls at D_pair g, with D_pair = {d[0]}, {d[1]}, {d[2]} for "
          "tethered pairs of equal, opposite, orthogonal content")
    print("HIT: at first order in a uniform gradient g, a cluster of n records on block 95's clocks whose relative configuration stays in a "
          "finite set drifts at -((2a - 1)n - 1) D_cm g per tick of the clock at its centre; at a = 1 a lone record does not fall and a bound "
          "pair falls at D_pair g, D_pair set by its contents: the equilibrium weight is one per record, the drift per unit gradient is not "
          "universal")
    return 0


if __name__ == "__main__":
    sys.exit(main())
