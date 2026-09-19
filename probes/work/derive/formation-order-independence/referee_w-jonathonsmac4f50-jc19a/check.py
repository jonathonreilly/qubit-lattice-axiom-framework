#!/usr/bin/env python3
"""Referee check for J:derive:formation-order-independence:a2 (author w-macbookpro90c72-je352, grok-4.6).

Independent code (exact Fractions, full joint laws). A record formed along an order conditions on what is recorded:
  directed   -- only on its already-formed parents (the attempt's V: sources never see C; C without both parents
                uses the empty kernel);
  undirected -- on its already-formed graph neighbours (the attempt's two-site E1; the campaign's Z^3 sweeps).

S1  step 1: random DAGs, random kernels, every linear extension gives one law.
S2  steps 2-3: the attempt's V (sources Bern(1/2), P(C=1|a,b) = (2a+b+1)/7, empty kernel 1/2): ABC = BAC;
    P(1,0,1) = 3/28 legal, 1/8 C-first; which of the six orders agree; how many put C before BOTH parents.
S3  the 'smallest' claim: the two-site edge a -> b in the directed reading its V uses, with its own one-parent kernel
    (p = 3/4 equal, q = 1/4) and with the V's kernel at b = 0; and in the undirected reading of its E1 with a
    non-symmetric one-parent kernel.
S4  step 4 on the 2x2x2 cube (parents x - e_i): the (1,1,1) corner order is a linear extension of x -> {x - e_j}
    and, read undirected, gives the DAG law; the other seven corner orders are not and give other laws.
"""
from __future__ import annotations

import itertools
import random
from fractions import Fraction as F


def law(nodes, order, menu, kern, cond):
    out = {}
    for vals in itertools.product(menu, repeat=len(nodes)):
        s = dict(zip(nodes, vals))
        w, formed = F(1), set()
        for v in order:
            c = cond(v, formed)
            w *= kern(v, s[v], tuple((y, s[y]) for y in sorted(c, key=str)))
            formed.add(v)
        if w:
            out[vals] = w
    assert sum(out.values()) == 1
    return out


def tv(p, q):
    return sum(abs(p.get(k, F(0)) - q.get(k, F(0))) for k in set(p) | set(q)) / 2


def lin_ext(nodes, parents):
    return [o for o in itertools.permutations(nodes)
            if all(o.index(p) < o.index(v) for v in nodes for p in parents[v])]


def s1(seed=11, trials=30):
    rng = random.Random(seed)
    ok, n_ext = True, 0
    for _ in range(trials):
        n = rng.randint(3, 5)
        nodes = list(range(n))
        parents = {v: [u for u in range(v) if rng.random() < 0.6] for v in nodes}
        table = {}

        def kern(v, x, a, table=table):
            key = (v, a)
            if key not in table:
                w = [F(rng.randint(1, 9)) for _ in (0, 1)]
                table[key] = [w[0] / sum(w), w[1] / sum(w)]
            return table[key][x]

        cond = lambda v, formed, parents=parents: [p for p in parents[v] if p in formed]
        exts = lin_ext(nodes, parents)
        n_ext += len(exts)
        laws = [law(nodes, e, (0, 1), kern, cond) for e in exts]
        ok &= all(L == laws[0] for L in laws)
    return ok, n_ext


def v_kernel(v, x, a):
    if v in ("A", "B"):
        return F(1, 2)
    d = dict(a)
    if "A" in d and "B" in d:
        p1 = F(2 * d["A"] + d["B"] + 1, 7)
    else:
        p1 = F(1, 2)  # the attempt's convention: C without both parents uses the empty kernel
    return p1 if x == 1 else 1 - p1


def s2():
    nodes = ["A", "B", "C"]
    parents = {"A": [], "B": [], "C": ["A", "B"]}
    cond = lambda v, formed: [p for p in parents[v] if p in formed]
    laws = {o: law(nodes, o, (0, 1), v_kernel, cond) for o in itertools.permutations(nodes)}
    legal = laws[("A", "B", "C")]
    agree = sorted("".join(o) for o, L in laws.items() if L == legal)
    c_before_both = sorted("".join(o) for o in laws if o.index("C") < o.index("A") and o.index("C") < o.index("B"))
    c_between = sorted("".join(o) for o in laws if o not in [tuple(x) for x in agree] and "".join(o) not in c_before_both)
    return legal[(1, 0, 1)], laws[("C", "A", "B")][(1, 0, 1)], agree, c_before_both, c_between


def s3():
    nodes = ["a", "b"]
    parents = {"a": [], "b": ["a"]}
    cond_d = lambda v, formed: [p for p in parents[v] if p in formed]

    def k_ising(v, x, a):  # the attempt's E0 kernel: empty 1/2; one parent p = 3/4 if equal, q = 1/4
        d = dict(a)
        if not d:
            return F(1, 2)
        (_, y), = d.items()
        return F(3, 4) if x == y else F(1, 4)

    def k_v0(v, x, a):  # the V's kernel with B = 0: P(1|a) = (2a+1)/7; empty 1/2
        d = dict(a)
        p1 = F(2 * d["a"] + 1, 7) if (v == "b" and d) else F(1, 2)
        return p1 if x == 1 else 1 - p1

    t_ising = tv(law(nodes, ("a", "b"), (0, 1), k_ising, cond_d), law(nodes, ("b", "a"), (0, 1), k_ising, cond_d))
    t_v0 = tv(law(nodes, ("a", "b"), (0, 1), k_v0, cond_d), law(nodes, ("b", "a"), (0, 1), k_v0, cond_d))
    # undirected reading (the attempt's E1): the later site conditions on the earlier one
    nb = {"a": ["b"], "b": ["a"]}
    cond_u = lambda v, formed: [y for y in nb[v] if y in formed]
    t_und_sym = tv(law(nodes, ("a", "b"), (0, 1), k_ising, cond_u), law(nodes, ("b", "a"), (0, 1), k_ising, cond_u))

    def k_nonsym(v, x, a):  # one-parent kernel not symmetric as a joint: P(1|1) = 3/4, P(1|0) = 1/2; empty 1/2
        d = dict(a)
        if not d:
            return F(1, 2)
        (_, y), = d.items()
        p1 = F(3, 4) if y == 1 else F(1, 2)
        return p1 if x == 1 else 1 - p1

    t_und_ns = tv(law(nodes, ("a", "b"), (0, 1), k_nonsym, cond_u), law(nodes, ("b", "a"), (0, 1), k_nonsym, cond_u))
    return t_ising, t_v0, t_und_sym, t_und_ns


def s4():
    sites = list(itertools.product((0, 1), repeat=3))
    parents = {x: [tuple(x[j] - (j == i) for j in range(3)) for i in range(3) if x[i] == 1] for x in sites}
    nbrs = {x: [y for y in sites if sum(abs(a - b) for a, b in zip(x, y)) == 1] for x in sites}
    W = {(0, 0): F(2), (1, 1): F(2), (0, 1): F(1), (1, 0): F(1)}

    def kern(v, x, a):
        def w(t):
            out = F(1)
            for _, sy in a:
                out *= W[(t, sy)]
            return out
        return w(x) / (w(0) + w(1))

    cond_d = lambda v, formed: [p for p in parents[v] if p in formed]
    cond_u = lambda v, formed: [y for y in nbrs[v] if y in formed]
    dag = law(sites, lin_ext(sites, parents)[0], (0, 1), kern, cond_d)
    rows = []
    for sig in itertools.product((1, -1), repeat=3):
        order = sorted(sites, key=lambda x: sum(s * c for s, c in zip(sig, x)))
        is_ext = all(order.index(p) < order.index(v) for v in sites for p in parents[v])
        L = law(sites, order, (0, 1), kern, cond_u)
        rows.append((sig, is_ext, L == dag))
    return rows


def main():
    ok1, n_ext = s1()
    print(f"S1 step 1: 30 random DAGs (3-5 sites), {n_ext} linear extensions, random kernels: one law per DAG {ok1}")
    p_legal, p_cfirst, agree, before_both, between = s2()
    print(f"S2 V: P(1,0,1) legal {p_legal}, C-first {p_cfirst}; orders with the legal law {agree}; C before both parents "
          f"{before_both}; C between its parents {between}")
    t_ising, t_v0, t_und_sym, t_und_ns = s3()
    print(f"S3 two-site edge a -> b formed b-first: directed reading (the V's) TV {t_ising} with the attempt's E0 kernel "
          f"(p=3/4, q=1/4), TV {t_v0} with the V's kernel at B=0; undirected reading (its E1) TV {t_und_sym} for the symmetric "
          f"kernel and {t_und_ns} for a non-symmetric one-parent kernel")
    rows = s4()
    for sig, is_ext, same in rows:
        print(f"S4 cube corner order {sig}: linear extension of x -> {{x - e_j}} {is_ext}; undirected law = DAG law {same}")

    ok_v = p_legal == F(3, 28) and p_cfirst == F(1, 8) and agree == ["ABC", "BAC"]
    corner111 = [r for r in rows if r[0] == (1, 1, 1)][0]
    others_differ = all((not ext) and (not same) for sig, ext, same in rows if sig != (1, 1, 1))
    if ok1 and ok_v and t_ising > 0 and t_v0 > 0:
        print(f"SUMMARY: fails at step 3 - the V is not the smallest violating example: in the reading its V uses (sources never "
              f"see C, C without both parents uses the empty kernel) the two-site edge formed child-first already changes the law, "
              f"TV {t_ising} with the attempt's own E0 kernel and TV {t_v0} with the V's kernel at B=0 (its E1 switched to the "
              f"undirected reading, TV {t_und_sym} there for a symmetric kernel, {t_und_ns} for a non-symmetric one); step 3's "
              f"'four that place C before both predecessors' is {len(before_both)} ({', '.join(before_both)}), the other two "
              f"({', '.join(between)}) place C between them; step 4's 'a monotone corner order is not a linear extension of "
              f"x -> {{x-e_j}}' fails for the (1,1,1) corner (linear extension {corner111[1]}, its undirected law = the DAG law "
              f"{corner111[2]}; the other seven corners differ {others_differ}); step 1 holds ({n_ext} extensions, one law per DAG), "
              f"the V numbers 3/28 and 1/8 hold; blocks 14/15 not addressed")
    else:
        print(f"SUMMARY: fails - step 1 {ok1}, V {ok_v}, two-site {t_ising}/{t_v0}")


if __name__ == "__main__":
    main()
