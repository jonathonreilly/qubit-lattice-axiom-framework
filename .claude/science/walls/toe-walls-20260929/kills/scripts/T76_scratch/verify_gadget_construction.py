#!/usr/bin/env python3
"""Direct check of the generalised sealed-block lemma: build copies of a gadget window at pitch (side+1), realise every pattern combination,
then complete by random maximal legal growth; verify the final state is frozen, the windows still show the chosen patterns, and all combos are distinct."""
import sys, itertools, random
import gadget_dfs2 as g
from gadget_search import window

def order_for(mask, nb, Aset):
    # forward DFS returning an addition order for mask
    n = len(nb); nbm = [sum(1 << u for u in nb[v]) for v in range(n)]
    seen = {0: None}; stack = [0]
    while stack:
        cur = stack.pop()
        if cur == mask: break
        rem = mask & ~cur
        r = rem
        while r:
            b = r & -r; v = b.bit_length() - 1; r ^= b
            if (cur & nbm[v]).bit_count() in Aset:
                nxt = cur | b
                if nxt not in seen: seen[nxt] = (cur, v); stack.append(nxt)
    order = []; cur = mask
    while seen.get(cur) is not None:
        prev, v = seen[cur]; order.append(v); cur = prev
    return order[::-1]

def run(d, A, shape, L, trials=3, seed=1):
    random.seed(seed)
    Aset = set(A)
    good, lv, unk, cp = g.find(shape, A, cap=200000)
    assert len(good) >= 2, "no gadget"
    pats = good[:2]
    sites, nb, o = window(shape)
    orders = [order_for(p, nb, Aset) for p in pats]
    pitch = [s + 1 for s in shape]
    per_axis = [(L + 1) // p for p in pitch]
    origins = list(itertools.product(*[[i * pitch[k] for i in range(per_axis[k])] for k in range(d)]))
    allsites = list(itertools.product(range(L), repeat=d))
    def nbrs(s):
        for k in range(d):
            for dv in (-1, 1):
                t = list(s); t[k] += dv; t = tuple(t)
                if all(0 <= x < L for x in t): yield t
    ncopy = len(origins)
    results = set(); ok_all = True
    combos = list(itertools.product((0, 1), repeat=ncopy))
    if len(combos) > 64: combos = random.sample(combos, 64)
    for combo in combos:
        rec = set()
        # build all copies first
        for oi, org in enumerate(origins):
            for v in orders[combo[oi]]:
                s = tuple(org[k] + sites[v][k] for k in range(d))
                k_ = sum(1 for t in nbrs(s) if t in rec)
                assert k_ in Aset, "peeling order not legal in box"
                rec.add(s)
        # random maximal growth
        while True:
            cand = [s for s in allsites if s not in rec and sum(1 for t in nbrs(s) if t in rec) in Aset]
            if not cand: break
            rec.add(random.choice(cand))
        frozen = all(s in rec or sum(1 for t in nbrs(s) if t in rec) not in Aset for s in allsites)
        # windows show chosen patterns
        show = True
        for oi, org in enumerate(origins):
            for vi, s0 in enumerate(sites):
                s = tuple(org[k] + s0[k] for k in range(d))
                if ((pats[combo[oi]] >> vi) & 1) != (s in rec): show = False
        ok_all &= frozen and show
        results.add(frozenset(rec))
    print(f"d={d} A={''.join(map(str,A))} window={shape} L={L}: copies={ncopy} combos tested={len(combos)} distinct final frozen states={len(results)} all frozen & windows intact={ok_all}")

run(2, (0, 3), (5, 5), 11)
run(2, (0, 3, 4), (5, 5), 11)
run(2, (0, 1), (3, 4), 11)
run(3, (0, 1, 4), (3, 3, 3), 7)
run(3, (0, 3, 5), (3, 3, 3), 7)
