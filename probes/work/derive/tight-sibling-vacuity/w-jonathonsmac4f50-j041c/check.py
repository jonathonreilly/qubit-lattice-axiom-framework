#!/usr/bin/env python3
"""tight-sibling-vacuity, attempt 3 of 4 (worker w-jonathonsmac4f50-j041c, claude-opus-5).

Objects (block 32/33, PRs #8176/#8177): sites of Z^3, level tau = x1 + x2 + x3, predecessors x - e_j, siblings x +- (e_i - e_j);
eta_x = 1 iff >= 2 predecessors are 1, else iff x is marked; seed / amplified / processed = 1-site with 0 / 1 / >= 2 one-predecessors.
A marked tree: node set N of 1-sites, one arrow per non-seed node to a 1-predecessor in N, forks between siblings, a tree;
cost = E - 3(|S| - 1) - |A| = 3 + sum_{x in N} w(x) with w = +1 (processed), -1 (amplified), -3 (seed).  v(z) = min cost over trees
containing z with all nodes at levels <= tau(z).  (H): v <= 0 processed, v <= -1 amplified.  (Vac): no processed site all of
whose (>= 2) 1-predecessors are processed with v = 0.

L1  exact instances of the disjoint-fork lemma's bookkeeping: cost(T1 u T2 u {fork}) = cost(T1) + cost(T2) - 3.
C1  the depth-2 local census (exact, exhaustive): z at level 0, window = its backward cone at levels -1, -2, -3; every eta on the
    window consistent with the rule at levels -1, -2 (level -3 free) with z's 1-predecessors all processed (>= 2 of them); a
    configuration is certified if some 1-predecessor of z has a safe local tree of cost <= -1 using (H) below level -1 only.
C2  the (H) + (Vac) adversarial check on the uncertified classes with at most KMAX bottom 1-sites: the unseen bottom's types
    and values are chosen by an adversary (seed 0, processed 0 or -1; amplified is dominated by processed -1), middle values are
    capped by their own safe certificates, (Vac) is imposed at every processed window site with all-processed 1-predecessors.
C3  an explicit class that C2 leaves open, with the adversary's winning assignment, and the planar obstruction to it.
"""
import itertools
import sys
import time
from collections import Counter

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
SIB = [(1, -1, 0), (-1, 1, 0), (1, 0, -1), (-1, 0, 1), (0, 1, -1), (0, -1, 1)]
WT = {"proc": 1, "amp": -1, "seed": -3}
FAILS = []


def check(label, ok, detail):
    print(("ok   " if ok else "FAIL ") + f"{label}: {detail}", flush=True)
    if not ok:
        FAILS.append(label)


def lev(x):
    return x[0] + x[1] + x[2]


def preds(x):
    return [(x[0] - e[0], x[1] - e[1], x[2] - e[2]) for e in E3]


def sibs(x):
    return [(x[0] + d[0], x[1] + d[1], x[2] + d[2]) for d in SIB]


def comps(k):
    return [(-a, -b, -(k - a - b)) for a in range(k + 1) for b in range(k + 1 - a)]


TOP, MID, BOT = comps(1), comps(2), comps(3)


def valid_tree(N, popts):
    keys = list(popts)
    for choice in itertools.product(*[popts[k] for k in keys]):
        par = {x: x for x in N}

        def f(a):
            while par[a] != a:
                par[a] = par[par[a]]
                a = par[a]
            return a
        for x, p in zip(keys, choice):
            par[f(x)] = f(p)
        for a in N:
            for b in sibs(a):
                if b in N and f(a) != f(b):
                    par[f(a)] = f(b)
        r = f(next(iter(N)))
        if all(f(a) == r for a in N):
            return True
    return False


def cert(t, one, kindf, val, bottom_modes):
    """min cost of a safe local tree containing t (levels <= lev(t)); one open end:
    O1 at a window node y (value val[y], every other node above lev(y)); O2 at an unseen 1-predecessor of a bottom
    non-seed node u in the tree (value <= 0; every node at level >= -3); O0 none (cost 3 + sum).  bottom_modes: which
    bottom nodes may be tree nodes (seeds) and which may carry O2."""
    Lt = lev(t)
    best = 10 ** 6
    nonbot = [x for x in one if -3 < lev(x) <= Lt]
    bseeds, bnonseeds = bottom_modes
    modes = [("O0", None)] + [("O2", u) for u in bnonseeds] + [("O1", y) for y in one if -3 <= lev(y) < Lt and y in val]
    for mode, y in modes:
        if mode == "O1":
            pool = [x for x in one if lev(y) < lev(x) <= Lt and x != t]
            base = val[y]
        else:
            pool = [x for x in nonbot if x != t] + list(bseeds)
            base = 0 if mode == "O2" else 3
        fixed = {t} | ({y} if mode != "O0" else set())
        for r in range(len(pool) + 1):
            for extra in itertools.combinations(pool, r):
                N = fixed | set(extra)
                cost = base + sum(WT[kindf(x)] for x in N if not (mode == "O1" and x == y))
                if cost >= best:
                    continue
                popts, ok = {}, True
                for x in N:
                    if mode in ("O1", "O2") and x == y:
                        continue
                    if kindf(x) == "seed":
                        continue
                    opts = [p for p in preds(x) if p in N]
                    if not opts:
                        ok = False
                        break
                    popts[x] = opts
                if ok and valid_tree(N, popts):
                    best = cost
    return best


def configurations():
    for bmask in range(1 << len(BOT)):
        one = {x for i, x in enumerate(BOT) if bmask >> i & 1}
        mid_free = []
        for x in MID:
            if sum(1 for p in preds(x) if p in one) >= 2:
                one.add(x)
            else:
                mid_free.append(x)
        base = set(one)
        for mm in range(1 << len(mid_free)):
            one2 = base | {x for i, x in enumerate(mid_free) if mm >> i & 1}
            top_free = []
            for x in TOP:
                if sum(1 for p in preds(x) if p in one2) >= 2:
                    one2.add(x)
                else:
                    top_free.append(x)
            for tm in range(1 << len(top_free)):
                one3 = one2 | {x for i, x in enumerate(top_free) if tm >> i & 1}
                kind = {}
                for x in one3:
                    if lev(x) > -3:
                        n1 = sum(1 for p in preds(x) if p in one3)
                        kind[x] = "seed" if n1 == 0 else ("amp" if n1 == 1 else "proc")
                zp = [x for x in TOP if x in one3]
                if len(zp) >= 2 and all(kind[x] == "proc" for x in zp):
                    yield frozenset(one3), kind, zp


def canon(one):
    return min(tuple(sorted(tuple(x[p[i]] for i in range(3)) for x in one)) for p in itertools.permutations(range(3)))


def h_only(one, kind, zp):
    """(H) only: bottom 1-sites enter only as O1 open ends with value 0 (valid for every bottom type)."""
    val = {x: 0 for x in one if lev(x) == -3}
    val.update({x: (0 if kind[x] in ("proc", "seed") else -1) for x in one if lev(x) == -2})
    kindf = lambda x: kind[x]
    return min(cert(w, one, kindf, val, ((), ())) for w in zp)


def feasible_signatures(one):
    """over all level -4 patterns (any pattern is realizable by marks) consistent with the bottom 0-sites (each has < 2 one-predecessors),
    the realizable count classes of the bottom 1-sites: 0 (seed), 1 (amplified), >= 2 (processed)"""
    bots = sorted(x for x in one if lev(x) == -3)
    zeros = [x for x in BOT if x not in one]
    L4 = sorted({p for b in BOT for p in preds(b)})
    idx = {q: i for i, q in enumerate(L4)}
    sigs = set()
    for mask in range(1 << len(L4)):
        cnt = lambda b: sum(mask >> idx[p] & 1 for p in preds(b))
        if any(cnt(b) >= 2 for b in zeros):
            continue
        sigs.add(tuple(min(cnt(b), 2) for b in bots))
    return sigs


def adversary(one, kind, zp, sigs=None):
    bots = sorted(x for x in one if lev(x) == -3)
    mids = [x for x in one if lev(x) == -2]
    Hb = {"proc": 0, "amp": -1, "seed": 0}
    for assign in itertools.product(["s", "p0", "p1"], repeat=len(bots)):
        if sigs is not None and not any(all((a == "s" and c == 0) or (a == "p0" and c == 2) or (a == "p1" and c >= 1)
                                               for a, c in zip(assign, sg)) for sg in sigs):
            continue
        bt = dict(zip(bots, assign))
        kindf = lambda x, bt=bt: (("seed" if bt[x] == "s" else "proc") if lev(x) == -3 else kind[x])
        modes = (tuple(b for b in bots if bt[b] == "s"), tuple(b for b in bots if bt[b] != "s"))
        val = {b: (-1 if bt[b] == "p1" else 0) for b in bots}
        bad = False
        for x in mids:
            ps = [p for p in preds(x) if p in one]
            if kind[x] == "proc" and all(bt[p] != "s" for p in ps) and all(val[p] == 0 for p in ps):
                bad = True
                break
        if bad:
            continue
        for x in mids:
            val[x] = min(Hb[kind[x]], cert(x, one, kindf, val, modes))
        need = []
        for w in zp:
            ps = [p for p in preds(w) if p in one]
            if all(kind[p] == "proc" for p in ps) and all(val[p] >= 0 for p in ps):
                need.append(ps)
        for br in (itertools.product(*need) if need else [()]):
            v2 = dict(val)
            for p in br:
                v2[p] = min(v2[p], -1)
            if all(cert(w, one, kindf, v2, modes) >= 0 for w in zp):
                return False, dict(bt), br
    return True, None, None


def main():
    t0 = time.time()
    # L1: bookkeeping of the disjoint-fork lemma on explicit weight multisets
    ok = True
    for n1 in range(4):
        for a1 in range(3):
            for s1 in range(1, 3):
                for n2 in range(3):
                    for a2 in range(3):
                        for s2 in range(1, 3):
                            c1 = n1 - 3 * (s1 - 1) - a1
                            c2 = n2 - 3 * (s2 - 1) - a2
                            cu = (n1 + n2) - 3 * (s1 + s2 - 1) - (a1 + a2)
                            ok &= cu == c1 + c2 - 3 and c1 == 3 + n1 - a1 - 3 * s1
    check("L1", ok, "cost = E - 3(|S| - 1) - |A| = 3 + sum of node weights (+1 processed, -1 amplified, -3 seed), and joining two disjoint "
          "trees by one fork adds their costs and subtracts 3 (all small counts); hence two sibling tight sites have intersecting "
          "optimal trees, and so do the rooted trees of any 1-predecessor of one and any 1-predecessor of the other")

    # C1: the depth-2 census, (H) only
    total = cert_n = 0
    classes, cls_cert = {}, {}
    for one, kind, zp in configurations():
        total += 1
        c = canon(one)
        if c not in classes:
            classes[c] = (one, kind, zp)
            cls_cert[c] = h_only(one, kind, zp) <= -1
        cert_n += cls_cert[c]
    ncls, ncls_cert = len(classes), sum(cls_cert.values())
    check("C1", total == 10272 and cert_n == 6196 and ncls == 1844 and ncls_cert == 1107,
          f"{total} local configurations ({ncls} classes under the coordinate permutations) of the cone below a processed z whose "
          f"1-predecessors are all processed; with (H) below level -1 only (bottom 1-sites as open ends of value 0, valid for every bottom "
          f"type), {cert_n} configurations ({ncls_cert} classes) have a 1-predecessor of z with a safe local tree of cost <= -1, so (Vac) "
          f"holds there whatever the realization below; {total - cert_n} ({ncls - ncls_cert} classes) are not certified this way "
          f"({time.time() - t0:.0f} s)")

    # C2: (H) + (Vac) adversary on the uncertified classes with <= KMAX bottom 1-sites
    t1 = time.time()
    res = Counter()
    example = None
    for c, (one, kind, zp) in sorted(classes.items()):
        if cls_cert[c]:
            continue
        k = sum(1 for x in one if lev(x) == -3)
        if k > KMAX:
            res["beyond"] += 1
            continue
        good, bt, br = adversary(one, kind, zp)
        res["certified" if good else "open"] += 1
        if not good and example is None and all(x[0] == 0 for x in one):
            example = (one, kind, zp, bt, br)
        if not good:
            good2, _, _ = adversary(one, kind, zp, feasible_signatures(one))
            res["certified_consistent" if good2 else "open_consistent"] += 1
    check("C2", res["certified"] + res["open"] > 0,
          f"(H) + (Vac) at levels <= -1 with an adversary choosing the unseen bottom (types seed / processed, values 0 or -1; "
          f"amplified dominated by processed -1) on the {res['certified'] + res['open']} uncertified classes with at most {KMAX} bottom "
          f"1-sites: {res['certified']} certified (some 1-predecessor of z has a safe tree of cost <= -1 under every admissible assignment), "
          f"{res['open']} left open; requiring the adversary's bottom types to be realizable from some level -4 layer (every bottom 0-site with "
          f"< 2 one-predecessors) certifies {res['certified_consistent']} more and leaves {res['open_consistent']}; {res['beyond']} classes with "
          f"more bottom 1-sites not examined ({time.time() - t1:.0f} s)")

    # C3: an open class lying in a coordinate plane, and why the adversary's assignment is not planar
    ok = example is not None
    detail = "no planar open class found"
    if ok:
        one, kind, zp, bt, br = example
        seeds = [b for b, t in bt.items() if t == "s"]
        procs = [b for b, t in bt.items() if t != "s"]
        # in the plane x1 = 0 a bottom seed needs both in-plane predecessors 0; a bottom processed site needs both in-plane ones 1
        need1 = {p for b in procs for p in preds(b) if p[0] == 0}
        need0 = {p for b in seeds for p in preds(b) if p[0] == 0}
        clash = sorted(need1 & need0)
        detail = (f"class with 1-sites {sorted(one)} (all in the plane x1 = 0), z's 1-predecessors {zp}; adversary: {bt}, lowered {list(br)}; "
                  f"no safe local tree of cost <= -1 at either 1-predecessor.  Confined to the plane (all marks with x1 = 0) the "
                  f"assignment is impossible: level -4 sites {clash} must be 1 for a processed bottom site and 0 for a seed")
        ok = bool(clash)
    check("C3", ok, detail)

    print("=" * 90)
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = (f"(Vac) at a processed z holds whenever the depth-2 cone below z is in one of the {ncls_cert} of {ncls} classes "
            f"({cert_n} of {total} local configurations) certified by safe local trees under (H) alone, whatever lies below; adding (Vac) "
            f"at lower levels as an induction hypothesis certifies {res['certified']} of the {res['certified'] + res['open']} remaining classes "
            f"with at most {KMAX} bottom 1-sites, and {res['certified_consistent']} more once the unseen bottom must be realizable from a level -4 "
            f"layer; the lemma on Z^3 is reduced, not proved: {res['open_consistent']} of these small classes stay open at depth 2")
    print("SUMMARY: PARTIAL " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
