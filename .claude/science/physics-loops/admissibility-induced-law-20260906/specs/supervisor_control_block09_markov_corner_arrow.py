"""Supervisor control, block 09: the Markov graph of the Z^3 monotone law, the eight corner classes, the arrow.
Exact arithmetic only.  Uses block 08's runner module for the rule, kernels, plane transfer and orbits.
(1) the full conditional gamma^F_x at an interior site depends on the face-diagonal site x+e1-e2: an exact witness;
(2) the eight corner classes: dependency sets of x (6 axial + 6 face-diagonal), which classes share the set; within a
    point-reflection pair, an exact witness configuration where the two conditionals differ;
(3) the 2x2 column: irreversibility TV = sum |pi(w)P(w,v) - pi(v)P(v,w)|/2 exactly at (3,1,2), (5,2,4), (2,2,2);
(4) the eight predecessor structures on the 2x2 column: exact stationary laws and the number of distinct ones.
"""
from fractions import Fraction as F
from itertools import product, permutations
import sys, time
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[5] / "scripts"))
import importlib
run = importlib.import_module("admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_2026_09_15")
M = 6

def cond_full(rule, s_val, axial, triples):
    """Unnormalized full conditional weight of value s at x: prod_axial K(s, v_y) / prod over triples containing x of K_3(s, a, b)."""
    w = F(1)
    for a in axial:
        w *= rule.K[a][s_val]
    for (a, b) in triples:
        w /= rule.K3[(s_val, a, b)]
    return w

def normalized(rule, axial, triples):
    ws = [cond_full(rule, s, axial, triples) for s in range(M)]
    Z = sum(ws)
    return [x / Z for x in ws]

def dep_set(signs):
    """Corner class with sweep signs (s1, s2, s3) in {+1,-1}: predecessors of y are y - s_i e_i.
    x belongs to the triple of y = x + s_i e_i, with co-members x + s_i e_i - s_j e_j (j != i).
    Returns the set of 6 face-diagonal co-member offsets, grouped by i."""
    groups = []
    for i in range(3):
        g = []
        for j in range(3):
            if j == i: continue
            off = [0, 0, 0]; off[i] += signs[i]; off[j] -= signs[j]
            g.append(tuple(off))
        groups.append(tuple(sorted(g)))
    return tuple(sorted(groups))

def main():
    rule = run.Rule((3, 1, 2))
    print("=== (1) dependence of the full conditional on the face-diagonal site x+e1-e2 (class +++; triples {x, x+e1-e2, x+e1-e3}, {x, x+e2-e1, x+e2-e3}, {x, x+e3-e1, x+e3-e2})")
    axial = [0] * 6  # all axial neighbors +x
    # values at the six diagonal sites: d12 = x+e1-e2, d13 = x+e1-e3, d21, d23, d31, d32
    base = dict(d12=0, d13=0, d21=0, d23=0, d31=0, d32=0)
    def triples_of(vals):
        return [(vals['d12'], vals['d13']), (vals['d21'], vals['d23']), (vals['d31'], vals['d32'])]
    c0 = normalized(rule, axial, triples_of(base))
    best = F(0); arg = None
    for v12 in range(M):
        vals = dict(base); vals['d12'] = v12
        c1 = normalized(rule, axial, triples_of(vals))
        d = run.tv(c0, c1)
        if d > best: best, arg = d, v12
    print(f"max TV of gamma_x over changes of v(x+e1-e2) with all else +x: {best} = {run.dec(best)} (at value {run.AXES[arg]})")
    print()
    print("=== (2) the eight corner classes: dependency sets and point-reflection pairs")
    classes = list(product((1, -1), repeat=3))
    sets = {c: dep_set(c) for c in classes}
    flat = {c: frozenset(o for g in sets[c] for o in g) for c in classes}
    for c in classes:
        same_flat = [d for d in classes if flat[d] == flat[c]]
        same_groups = [d for d in classes if sets[d] == sets[c]]
        print(f"class {c}: same dependency set: {same_flat}; same triple grouping: {same_groups}")
    # within the pair (+++) vs (---): witness configuration where the two conditionals differ
    # (+++): triples {x, x+e1-e2, x+e1-e3}, {x, x+e2-e1, x+e2-e3}, {x, x+e3-e1, x+e3-e2}
    # (---): triples {x, x-e1+e2, x-e1+e3}, {x, x-e2+e1, x-e2+e3}, {x, x-e3+e1, x-e3+e2}
    # name the six diagonal sites by offsets: D[(i,j)] = x + e_i - e_j
    def cond_class(rule, D, axial, plus):
        if plus:
            tr = [(D[(0,1)], D[(0,2)]), (D[(1,0)], D[(1,2)]), (D[(2,0)], D[(2,1)])]
        else:
            tr = [(D[(1,0)], D[(2,0)]), (D[(0,1)], D[(2,1)]), (D[(0,2)], D[(1,2)])]
        return normalized(rule, axial, tr)
    keys = [(i, j) for i in range(3) for j in range(3) if i != j]
    best = F(0); arg = None
    for vals in product(range(M), repeat=6):
        D = dict(zip(keys, vals))
        d = run.tv(cond_class(rule, D, axial, True), cond_class(rule, D, axial, False))
        if d > best: best, arg = d, vals
    print(f"max TV between the (+++) and (---) full conditionals over the 6^6 diagonal configurations (axials +x): {best} = {run.dec(best)} at {[run.AXES[v] for v in arg]}")
    print()
    print("=== (3) the 2x2 column: irreversibility of the plane chain")
    states = list(product(range(M), repeat=4))
    for tr in [(3, 1, 2), (5, 2, 4), (2, 2, 2)]:
        t0 = time.time()
        rl = run.Rule(tr)
        st, orbit_of, reps, sizes = run.orbits_2x2()
        n = len(reps)
        Q = [[F(0)] * n for _ in range(n)]
        for o, w in enumerate(reps):
            for v in st:
                Q[o][orbit_of[v]] += run.plane_transfer(rl, w, v)
        pi_orb = run.solve_stationary(Q)
        pi = {s: pi_orb[orbit_of[s]] / sizes[orbit_of[s]] for s in st}
        irr = F(0)
        for w in st:
            pw = pi[w]
            for v in st:
                if v < w: continue
                a = pw * run.plane_transfer(rl, w, v)
                b = pi[v] * run.plane_transfer(rl, v, w)
                irr += abs(a - b)
        irr = irr  # each unordered pair counted once; TV over ordered pairs = sum/2 * 2 = this
        # in-plane reflections: pi(v) vs pi(R2 v) where R2 swaps x2: sites 00<->10, 01<->11
        r2 = sum(abs(pi[v] - pi[(v[2], v[3], v[0], v[1])]) for v in st) / 2
        print(f"{tr}: irreversibility TV(J, J^T) = {irr} ({run.dec(irr) if irr else 0}); TV(pi, pi∘R2) = {r2} ({run.dec(r2) if r2 else 0}); {time.time()-t0:.1f}s")
    print()
    print("=== (4) the eight predecessor structures on the 2x2 column: stationary laws and distinctness (3,1,2)")
    rl = run.Rule((3, 1, 2))
    G = run.group48()
    def transfer_class(signs, w, v):
        # cross-section sites (x2, x3) in {0,1}^2; plane sweep direction s1 (transfer w -> v either way: v records w at the same site);
        # in-plane predecessors: y - s2 e2 and y - s3 e3 when inside the square.
        s2, s3 = signs[1], signs[2]
        K, K2, K3 = rl.K, rl.K2, rl.K3
        idx = {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3}
        pr = F(1)
        for (a, b), k in idx.items():
            rec = [w[k]]
            p2 = (a - s2, b)
            p3 = (a, b - s3)
            if p2 in idx: rec.append(v[idx[p2]])
            if p3 in idx: rec.append(v[idx[p3]])
            pr *= rl.cond(tuple(rec))[v[k]]
        return pr
    laws = {}
    for signs in classes:
        # orbit reduce under the internal group only
        orbit_of, reps = {}, []
        for s in states:
            if s in orbit_of: continue
            o = len(reps); reps.append(s); orbit_of[s] = o
            for g in G:
                orbit_of[tuple(g[x] for x in s)] = o
        sizes = [0] * len(reps)
        for s in states: sizes[orbit_of[s]] += 1
        n = len(reps)
        Q = [[F(0)] * n for _ in range(n)]
        for o, w in enumerate(reps):
            for v in states:
                Q[o][orbit_of[v]] += transfer_class(signs, w, v)
        pi_orb = run.solve_stationary(Q)
        pi = {s: pi_orb[orbit_of[s]] / sizes[orbit_of[s]] for s in states}
        # the sweep direction s1 only reverses the chain: the one-plane law is the same for s1 = +1 and -1 (stationary law of the same P)
        laws[signs] = pi
    distinct = []
    for c in classes:
        if not any(laws[c] == laws[d] for d in distinct):
            distinct.append(c)
    print(f"one-plane stationary laws: {len(classes)} classes -> {len(distinct)} distinct one-plane laws: {distinct}")
    print("(note: s1 = -1 classes share the one-plane law of s1 = +1; the sweep direction is visible only in the two-plane joint law, item 3)")
    for c in classes:
        eq = [d for d in classes if laws[d] == laws[c]]
        print(f"  {c}: equal one-plane law with {eq}")

if __name__ == "__main__":
    main()
