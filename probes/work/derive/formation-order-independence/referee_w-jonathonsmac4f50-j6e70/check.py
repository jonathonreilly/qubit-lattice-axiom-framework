#!/usr/bin/env python3
"""Referee check for J:derive:formation-order-independence:a3 (author w-macbookpro90c72-j08d0, grok-4.6).

Independent code (exact Fractions, full joint laws); nothing is imported from the author's script.

A record formed in an order conditions on what is already recorded:
  directed reading   -- on its already-formed PARENTS (the attempt's reading: its V's sources ignore the
                        child; its D1 forms the parent 'empty' after the child);
  undirected reading -- on its already-formed graph NEIGHBOURS (the campaign's Z^3 sweeps, blocks 05/08/09).

R1  step 1: random DAGs, random non-symmetric kernels, every linear extension -> one joint law; some
    non-extension changes it (directed reading).
R2  step 2: the V numbers (P(C=1) 1/2 vs 1/3, TV 5/24) with the attempt's kernels, recomputed.
R3  the 'smallest' claim: one site has no violating order; the two-site edge formed child-first changes
    the law in the attempt's own reading (its kernels: TV 1/6, its own D1; the rule-consistent six-axis
    kernel at (3,1,2): TV 1/12); only the undirected six-axis reading leaves the edge order-free.
R4  Z^3 on the 2x2x2 cube (parents x - e_i), binary product kernel W = [[2,1],[1,2]]: 48 linear
    extensions -> one law; the (1,1,1) sweep read undirected = that law; the other seven monotone sweep
    directions read undirected give other laws; a reversed (anti-causal) order read directed differs.
"""
from __future__ import annotations

import itertools
import random
from fractions import Fraction as F

# --------------------------------------------------------------------------------------- machinery


def linear_extensions(nodes, parents):
    out = []
    for perm in itertools.permutations(nodes):
        pos = {v: i for i, v in enumerate(perm)}
        if all(pos[p] < pos[v] for v in nodes for p in parents[v]):
            out.append(perm)
    return out


def joint_law(nodes, order, menu, kern, cond_set):
    """exact law of the records formed along `order`; cond_set(v, formed) = the formed sites v conditions on;
    kern(v, s, assignment) with assignment a tuple of (site, value) pairs sorted by site."""
    law = {}
    for vals in itertools.product(menu, repeat=len(nodes)):
        s = dict(zip(nodes, vals))
        pr = F(1)
        formed = set()
        for v in order:
            cs = sorted(cond_set(v, formed))
            pr *= kern(v, s[v], tuple((y, s[y]) for y in cs))
            if pr == 0:
                break
            formed.add(v)
        if pr:
            law[vals] = pr
    assert sum(law.values()) == 1
    return law


def tv(p, q):
    return sum(abs(p.get(k, F(0)) - q.get(k, F(0))) for k in set(p) | set(q)) / 2


def product_kernel(W, menu):
    """the campaign's rule: K(s | recorded values) proportional to prod W(s, s_y); uniform with nothing recorded."""
    def kern(v, s, assignment):
        def w(t):
            out = F(1)
            for _, sy in assignment:
                out *= W[(t, sy)]
            return out
        return w(s) / sum(w(t) for t in menu)
    return kern


# --------------------------------------------------------------------------------------- R1


def r1(seed=1729, trials=40):
    rng = random.Random(seed)
    n_dags = n_ext = changed = 0
    ok = True
    for _ in range(trials):
        n = rng.randint(3, 6)
        nodes = list(range(n))
        parents = {v: [u for u in range(v) if rng.random() < 0.5] for v in nodes}
        if not any(parents.values()):
            parents[n - 1] = [0]
        menu = (0, 1, 2) if n <= 4 else (0, 1)
        table = {}

        def kern(v, s, assignment, table=table, menu=menu):
            key = (v, assignment)
            if key not in table:
                ws = [F(rng.randint(1, 9)) for _ in menu]
                table[key] = {t: w / sum(ws) for t, w in zip(menu, ws)}
            return table[key][s]

        def cond_directed(v, formed, parents=parents):
            return [p for p in parents[v] if p in formed]

        exts = linear_extensions(nodes, parents)
        laws = [joint_law(nodes, e, menu, kern, cond_directed) for e in exts]
        ok = ok and all(L == laws[0] for L in laws)
        # a non-extension: some v before one of its parents
        non = next(p for p in itertools.permutations(nodes) if p not in set(exts))
        changed += joint_law(nodes, non, menu, kern, cond_directed) != laws[0]
        n_dags += 1
        n_ext += len(exts)
    return ok, n_dags, n_ext, changed


# --------------------------------------------------------------------------------------- R2 / R3 with the attempt's kernels


def attempt_kernels():
    # the attempt's: sources Bern(1/2); K(1|x) = (1+x)/3; K(1|x,y) = (1+x+y)/4; K(1|empty) = 1/3
    def kern(v, s, assignment):
        if v in ("A", "B", "x"):
            return F(1, 2)
        xs = [val for _, val in assignment]
        if not xs:
            p1 = F(1, 3)
        elif len(xs) == 1:
            p1 = F(1 + xs[0], 3)
        else:
            p1 = F(1 + sum(xs), 4)
        return p1 if s == 1 else 1 - p1
    return kern


def r2():
    nodes = ["A", "B", "C"]
    parents = {"A": [], "B": [], "C": ["A", "B"]}
    kern = attempt_kernels()
    cond = lambda v, formed: [p for p in parents[v] if p in formed]
    topo = [joint_law(nodes, e, (0, 1), kern, cond) for e in linear_extensions(nodes, parents)]
    first = joint_law(nodes, ("C", "A", "B"), (0, 1), kern, cond)
    pc = lambda L: sum(p for k, p in L.items() if k[2] == 1)
    return len(topo), all(L == topo[0] for L in topo), pc(topo[0]), pc(first), tv(topo[0], first)


def r3():
    # two-site edge x -> y, child first, the attempt's own reading and kernels (its D1)
    nodes = ["x", "y"]
    parents = {"x": [], "y": ["x"]}
    kern = attempt_kernels()
    cond = lambda v, formed: [p for p in parents[v] if p in formed]
    t_att = tv(joint_law(nodes, ("x", "y"), (0, 1), kern, cond), joint_law(nodes, ("y", "x"), (0, 1), kern, cond))
    # the rule-consistent six-axis product kernel at (p,q,r) = (3,1,2)
    menu = ("+1", "-1", "+2", "-2", "+3", "-3")
    p, q, r = 3, 1, 2
    W = {(a, b): F(p) if a == b else (F(q) if a[1] == b[1] else F(r)) for a in menu for b in menu}
    k6 = product_kernel(W, menu)
    t_dir = tv(joint_law(nodes, ("x", "y"), menu, k6, cond), joint_law(nodes, ("y", "x"), menu, k6, cond))
    nbr = {"x": ["y"], "y": ["x"]}
    cond_u = lambda v, formed: [y for y in nbr[v] if y in formed]
    t_und = tv(joint_law(nodes, ("x", "y"), menu, k6, cond_u), joint_law(nodes, ("y", "x"), menu, k6, cond_u))
    # three-site path a - b - c (the V read undirected), six-axis: ends-first vs middle-first
    n3 = ["a", "b", "c"]
    nb3 = {"a": ["b"], "b": ["a", "c"], "c": ["b"]}
    cu3 = lambda v, formed: [y for y in nb3[v] if y in formed]
    L_mid = joint_law(n3, ("b", "a", "c"), menu, k6, cu3)
    L_end = joint_law(n3, ("a", "c", "b"), menu, k6, cu3)
    return t_att, t_dir, t_und, tv(L_mid, L_end)


# --------------------------------------------------------------------------------------- R4: the 2x2x2 cube


def r4():
    sites = [tuple(c) for c in itertools.product((0, 1), repeat=3)]
    parents = {x: [tuple(x[j] - (1 if j == i else 0) for j in range(3)) for i in range(3) if x[i] == 1] for x in sites}
    nbrs = {x: [y for y in sites if sum(abs(a - b) for a, b in zip(x, y)) == 1] for x in sites}
    menu = (0, 1)
    W = {(0, 0): F(2), (1, 1): F(2), (0, 1): F(1), (1, 0): F(1)}
    kern = product_kernel(W, menu)
    cond_d = lambda v, formed: [p for p in parents[v] if p in formed]
    cond_u = lambda v, formed: [y for y in nbrs[v] if y in formed]
    exts = linear_extensions(sites, parents)
    laws = [joint_law(sites, e, menu, kern, cond_d) for e in exts]
    one_law = all(L == laws[0] for L in laws)
    dag_law = laws[0]
    sweep_laws = {}
    for sig in itertools.product((1, -1), repeat=3):
        order = sorted(sites, key=lambda x: sum(s * c for s, c in zip(sig, x)))
        sweep_laws[sig] = joint_law(sites, order, menu, kern, cond_u)
    same_as_dag = [sig for sig, L in sweep_laws.items() if L == dag_law]
    distinct = len({tuple(sorted(L.items())) for L in sweep_laws.values()})
    min_tv_other = min(tv(L, dag_law) for sig, L in sweep_laws.items() if sig != (1, 1, 1))
    rev = list(reversed(exts[0]))
    tv_rev = tv(joint_law(sites, rev, menu, kern, cond_d), dag_law)
    return len(exts), one_law, same_as_dag, distinct, min_tv_other, tv_rev


def main():
    ok1, n_dags, n_ext, changed = r1()
    print(f"R1 step 1: {n_dags} random DAGs (3-6 sites), {n_ext} linear extensions, random non-symmetric kernels: "
          f"one joint law per DAG {ok1}; a non-extension changes the law on {changed}/{n_dags}")
    n_topo, same, pc_t, pc_f, tv_v = r2()
    print(f"R2 step 2: V with the attempt's kernels: {n_topo} topological orders agree {same}; P(C=1) {pc_t} topological, "
          f"{pc_f} child-first; full-joint TV {tv_v}")
    t_att, t_dir, t_und, t_path = r3()
    print(f"R3 smallest: one site has one order; the two-site edge formed child-first: TV {t_att} (the attempt's kernels and "
          f"reading, = its own D1), TV {t_dir} (six-axis product kernel at (3,1,2), directed reading), TV {t_und} "
          f"(six-axis, undirected reading); three-site path undirected, middle-first vs ends-first TV {t_path}")
    n_ext4, one4, same4, distinct4, min_tv4, tv_rev4 = r4()
    print(f"R4 Z^3 2x2x2 cube, binary W=[[2,1],[1,2]]: {n_ext4} linear extensions give one law {one4}; monotone sweeps read "
          f"undirected equal to it: {same4}; distinct sweep laws {distinct4}/8, min TV of the other seven to the DAG law "
          f"{min_tv4}; reversed order read directed TV {tv_rev4}")

    step1 = ok1 and changed == n_dags
    step2 = same and pc_t == F(1, 2) and pc_f == F(1, 3) and tv_v == F(5, 24)
    two_site = t_att == F(1, 6) and t_dir > 0
    z3 = n_ext4 == 48 and one4 and same4 == [(1, 1, 1)] and min_tv4 > 0 and tv_rev4 > 0
    print(f"verdicts: step 1 holds {step1}; step 2 arithmetic holds {step2}; two-site violation exists in the attempt's reading "
          f"{two_site}; Z^3 comparison holds {z3}")
    if step1 and step2 and z3 and not two_site:
        print("HIT: confirmed - product of kernels along every linear extension; the 3-site V is the smallest violation")
        print("SUMMARY: confirmed")
    elif step1 and step2 and two_site:
        print(f"SUMMARY: fails at step 2 - the 3-site V is not the smallest violating example: in the attempt's own reading "
              f"(a record formed before a parent conditions on the parents already formed) the two-site edge formed "
              f"child-first changes the law, TV {t_att} with the attempt's kernels (its own D1) and TV {t_dir} with the "
              f"six-axis product kernel at (3,1,2); the V is smallest only in the undirected six-axis reading (edge TV "
              f"{t_und}, path TV {t_path}); step 1 (one law over {n_ext} linear extensions of {n_dags} random DAGs) and the "
              f"Z^3 comparison (48 extensions of the cube, one law; seven other sweeps differ) hold; blocks 14/15 not addressed")
    else:
        print(f"SUMMARY: fails - step 1 {step1}, step 2 {step2}, Z^3 {z3}; see the lines above")


if __name__ == "__main__":
    main()
