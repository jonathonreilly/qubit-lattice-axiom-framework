#!/usr/bin/env python3
"""Referee check for J:derive:beyond-the-union-bound:a1 (author w-macbookpro90c72-j9773, grok-4.6); referee w-jonathonsmac4f50-j5777.

Independent code: my own two-level automaton and exact enumeration; histories from the NOTE'S OWN block-30 construction
(supervisor_control_block30_core.py read unmodified from PR #8174's branch), not the author's explainer.

Two-level noise on the depth-2 backward cone of x (10 sites, outside = 0): each site independently has U < eps1 (prob eps1), eps1 <= U < eps2
(prob eps2 - eps1) or U >= eps2; a site with >= 2 one-predecessors is 1; with exactly one it is 1 iff U < eps2; with none iff U < eps1.

R1  the census: distinct eta' patterns on the cone and those with eta'_x = 1 (the author: 308 and 234); P(eta'_x = 1) at (1/10, 1/5).
R2  histories: the note's construction on each 1-pattern gives one tree (seeds S, amplified A); cylinders C_h = {U < eps1 on S, U < eps2 on A};
    first-order union S1 = sum_h P(C_h), exact P(union C_h), the order-2 truncation S1 - S2 (a LOWER bound), and Hunter's second-order
    UPPER bound S1 - (max spanning tree of P(C_i n C_j)), which the attempt does not compute.
R3  the 'Chung-Erdos with only the diagonal' number (sum w)^2 / sum w^2: Chung-Erdos is a lower bound on P(union) with the FULL double sum
    in the denominator; the diagonal-only quotient is not a bound (it exceeds 1 here).
"""
from __future__ import annotations

import importlib.util
import itertools
import os
import subprocess
import tempfile
from fractions import Fraction as F

CORE = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block30_core.py"


def load_core():
    br = subprocess.run(["gh", "pr", "view", "8174", "--json", "headRefName", "--jq", ".headRefName"],
                        capture_output=True, text=True, check=True).stdout.strip()
    subprocess.run(["git", "fetch", "origin", br, "--quiet"], check=True)
    src = subprocess.run(["git", "show", f"FETCH_HEAD:{CORE}"], capture_output=True, text=True, check=True).stdout
    d = tempfile.mkdtemp()
    path = os.path.join(d, "b30core.py")
    open(path, "w").write(src)
    spec = importlib.util.spec_from_file_location("b30core", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def preds(z):
    return [tuple(z[i] - (1 if i == j else 0) for i in range(3)) for j in range(3)]


def two_level(sites, cls):
    """cls[z] in {0: U >= eps2, 1: eps1 <= U < eps2, 2: U < eps1}."""
    eta = {}
    for z in sorted(sites, key=sum):
        n1 = sum(eta.get(p, 0) for p in preds(z))
        eta[z] = 1 if (n1 >= 2 or (n1 == 1 and cls[z] >= 1) or (n1 == 0 and cls[z] == 2)) else 0
    return eta


def main():
    core = load_core()
    x = (0, 0, 0)
    sites = sorted(core.cone(x, 2), key=sum)
    assert len(sites) == 10
    e1, e2 = F(1, 10), F(1, 5)
    pcls = {0: 1 - e2, 1: e2 - e1, 2: e1}
    patterns = {}
    P_x = F(0)
    configs = []
    for cl in itertools.product((0, 1, 2), repeat=len(sites)):
        cls = dict(zip(sites, cl))
        eta = two_level(sites, cls)
        w = F(1)
        for z in sites:
            w *= pcls[cls[z]]
        key = tuple(eta[z] for z in sites)
        patterns[key] = patterns.get(key, F(0)) + w
        if eta[x]:
            P_x += w
        configs.append((cl, w))
    n_pat = len(patterns)
    n_pat_x = sum(1 for k in patterns if k[sites.index(x)] == 1)
    print(f"R1 depth-2 cone: {n_pat} distinct eta' patterns, {n_pat_x} with eta'_x = 1; P(eta'_x = 1) at (1/10, 1/5) = {P_x} = {float(P_x):.6f}")

    # histories from the note's construction
    hist = set()
    for key in patterns:
        eta = dict(zip(sites, key))
        if not eta[x]:
            continue
        zeta = {z: 1 for z in sites if eta[z] and sum(eta.get(p, 0) for p in preds(z)) < 2}
        eta2 = core.run_automaton(sites, zeta)
        assert all(eta2.get(z, 0) == eta[z] for z in sites)
        ex = core.Explainer(eta2, zeta)
        nodes, edges, S, A, refs, bad = ex.explain(x)
        assert core.check_tree(nodes, edges, x, ex)
        hist.add((frozenset(S), frozenset(A), frozenset((frozenset(e), k) for e, k in edges.items())))
    cyl = {}
    for S, A, _ in hist:
        cyl[(S, A)] = cyl.get((S, A), 0) + 1
    print(f"R2 the note's construction: {len(hist)} distinct trees over the {n_pat_x} one-patterns; {len(cyl)} distinct cylinders (S, A); "
          f"trees sharing a cylinder with another: {sum(c for c in cyl.values() if c > 1)}")
    H = [(S, A) for S, A, _ in hist]

    def p_cyl(S, A):
        return e1 ** len(S) * e2 ** len(A - S)

    S1 = sum(p_cyl(S, A) for S, A in H)
    inter = {}
    for i, j in itertools.combinations(range(len(H)), 2):
        Si, Ai = H[i]
        Sj, Aj = H[j]
        Su = Si | Sj
        Au = (Ai | Aj) - Su
        inter[(i, j)] = e1 ** len(Su) * e2 ** len(Au)
    S2 = sum(inter.values())
    # exact union probability by enumeration of the site classes
    idx = {z: k for k, z in enumerate(sites)}
    Pu = F(0)
    for cl, w in configs:
        if any(all(cl[idx[z]] == 2 for z in S) and all(cl[idx[z]] >= 1 for z in A) for S, A in H):
            Pu += w
    # Hunter: maximum spanning tree (Kruskal) on the pairwise intersections
    par = list(range(len(H)))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    tree_sum = F(0)
    for (i, j), v in sorted(inter.items(), key=lambda kv: kv[1], reverse=True):
        a, b = find(i), find(j)
        if a != b:
            par[a] = b
            tree_sum += v
    hunter = S1 - tree_sum
    print(f"   first-order union S1 = {float(S1):.6f}; exact P(union C_h) = {float(Pu):.6f}; order-2 truncation S1 - S2 = {float(S1 - S2):.6f} "
          f"(lower bound: {S1 - S2 <= Pu}); Hunter second-order UPPER bound = {float(hunter):.6f} (valid: {hunter >= Pu}; "
          f"{float(hunter / S1):.3f} of S1); P(eta'_x = 1) = {float(P_x):.6f} <= P(union) {P_x <= Pu}")
    w = [p_cyl(S, A) for S, A in H]
    ce_diag = sum(w) ** 2 / sum(v * v for v in w)
    ce_full = sum(w) ** 2 / (sum(v * v for v in w) + 2 * S2)
    print(f"R3 (sum w)^2 / sum w^2 (diagonal only) = {float(ce_diag):.5f} (not a bound; exceeds 1); the Chung-Erdos LOWER bound with the full "
          f"double sum = {float(ce_full):.6f} <= P(union) {ce_full <= Pu}")

    ok_census = n_pat == 308 and n_pat_x == 234 and abs(float(P_x) - 0.19208) < 5e-5
    if ok_census and hunter < S1 and hunter >= Pu:
        print(f"SUMMARY: fails at step 4 - the no-go for inclusion-exclusion on the CYLINDERS is asserted, not proved: steps 1-3 (disjoint A_h, "
              f"IE on them vacuous, order-2 truncation a lower bound) hold and the census re-derives (308 patterns, 234 ones, P = "
              f"{float(P_x):.5f}), but the union bound sums over cylinders, and a valid second-order UPPER bound on them exists (Hunter): on the "
              f"depth-2 cone it gives {float(hunter):.5f} against the first-order {float(S1):.5f} (exact union {float(Pu):.5f}), so second-order "
              f"IE on cylinders does cut the count here; whether it moves the 4/27 radius is not decided by the attempt's argument (a constant "
              f"at one (eps1, eps2) and the claim that the radius 'is independent of those overlaps'); the Chung-Erdos check uses the "
              f"diagonal-only quotient {float(ce_diag):.3f}, not a bound, and Chung-Erdos is a lower bound in any case; the attempt's order-2 "
              f"truncation 0.139484 treats a site that is a seed in one cylinder and amplified in another as making the cylinders disjoint "
              f"(U < eps1 satisfies both), so its overlap sum is too small: with the intersections computed correctly the truncation is "
              f"{float(S1 - S2):.6f} on the note's {len(hist)} trees (the attempt's own explainer gave 96 keys and S1 = 0.32658)")
    else:
        print(f"SUMMARY: fails - census {n_pat}/{n_pat_x}/{float(P_x)}, hunter {float(hunter)}, S1 {float(S1)}, union {float(Pu)}")


if __name__ == "__main__":
    main()
