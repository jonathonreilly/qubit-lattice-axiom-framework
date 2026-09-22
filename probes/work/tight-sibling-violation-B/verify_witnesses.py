"""Verification of the S:tight-sibling-violation-B hits of 2026-09-21 (seeds 44 and 161, 6x6x9, loop worker w-jonathonsmac4f50-4).
Rebuilds each witness from the zeta printed in its log with an automaton re-implemented from the rule, then
  (1) levdp.exact_min (solver-free level-by-level connectivity DP written from the family's definition) at the hit site,
      unrooted and rooted, at c = 1, 16/15, 10/9, and the search's score (max over processed 1-sites at level >= 3);
  (2) the campaign's MinTree/rooted/cstar (probes/lib, HiGHS) at the hit site, and family.verify_tree on MinTree's tree;
  (3) a cross-check of levdp against MinTree/rooted (and brute_min when <= 14 one-sites) on random 3x3x5 configurations and on
      1-3 mark perturbations of the witnesses.
usage: python3 probes/work/tight-sibling-violation-B/verify_witnesses.py [n_random] [n_perturb]   (from a checkout root)"""
import os, sys, ast, random, time
from fractions import Fraction as Fr
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "probes", "lib"))
from levdp import exact_min, lev
from mintree import MinTree, run_automaton
from rooted import rooted
import family as m
E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
LOGS = {44: "w-jonathonsmac4f50-4__1324f61c__20260921T205558Z", 161: "w-jonathonsmac4f50-4__19379286__20260921T202536Z"}
BOX, X = (6, 6, 9), (5, 4, 4)
SITES = [(a, b, c) for a in range(BOX[0]) for b in range(BOX[1]) for c in range(BOX[2])]


def automaton(sites, zeta):
    eta = {}
    for z in sorted(sites, key=lev):
        k = sum(eta.get(tuple(z[i] - E3[j][i] for i in range(3)), 0) for j in range(3))
        eta[z] = 1 if (k >= 2 or z in zeta) else 0
    return eta


def witness(seed):
    txt = open(os.path.join(ROOT, "logs", "probes", "S:tight-sibling-violation-B", LOGS[seed] + ".txt")).read()
    line = [l for l in txt.splitlines() if "max cost = " in l and "zeta=" in l][-1]
    return line, ast.literal_eval(line.split("zeta=")[1])


def main():
    n_rand = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    n_pert = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    t0 = time.time()
    witnesses = {}
    for seed in LOGS:
        line, zl = witness(seed)
        eta = automaton(SITES, set(map(tuple, zl)))
        assert eta == run_automaton(SITES, {tuple(z): 1 for z in zl}), "automaton re-implementation differs from probes/lib"
        ones = [z for z, v in eta.items() if v]
        p1 = {z: [p for p in (tuple(z[i] - E3[j][i] for i in range(3)) for j in range(3)) if eta.get(p, 0)] for z in ones}
        procs = [z for z in ones if len(p1[z]) >= 2 and lev(z) >= 3]
        assert X in procs
        dp = {c: tuple(str(v) for v in (exact_min(eta, X, c=c), exact_min(eta, X, c=c, rooted=True))) for c in (Fr(1), Fr(16, 15), Fr(10, 9))}
        score = {z: (exact_min(eta, z), exact_min(eta, z, rooted=True)) for z in procs}
        mx = max(score.values()); arg = sorted(z for z, v in score.items() if v == mx)
        r = MinTree(eta, X).solve(1.0)
        ok_tree = m.verify_tree(eta, X, r["nodes"], r["arrows"], r["forks"])
        cs, ctree, _ = MinTree(eta, X).cstar()
        mt = (r["E"] - 3 * (r["S"] - 1) - r["A"], rooted(eta, X)[0])
        witnesses[seed] = (eta, zl)
        print(f"seed {seed}: log line: {line.split('; ones?')[0]}")
        print(f"seed {seed}: {len(zl)} marks -> {len(ones)} one-sites; x = {X} processed at level {lev(X)}")
        print(f"seed {seed}: levdp (unrooted, rooted) at x: c=1 {dp[Fr(1)]}, c=16/15 {dp[Fr(16, 15)]}, c=10/9 {dp[Fr(10, 9)]}")
        print(f"seed {seed}: levdp max over {len(procs)} processed sites at level >= 3: {mx} at {arg}")
        print(f"seed {seed}: MinTree (unrooted, rooted) at x, c=1: {mt}; tree (E,A,S,F) = {(r['E'], r['A'], r['S'], r['F'])}, "
              f"{len(r['nodes'])} nodes, verify_tree {ok_tree}; cstar(x) = {cs} by tree (E,A,S,F) = {(ctree['E'], ctree['A'], ctree['S'], ctree['F'])}")
        assert dp[Fr(1)] == tuple(str(v) for v in mt) and ok_tree and dp[Fr(1)][0] == str(r["E"] - 3 * (r["S"] - 1) - r["A"])
        assert cs == Fr(16, 15) and dp[cs][0] == "0" and Fr(dp[Fr(1)][0]) > 0
    same = {z for z, v in witnesses[44][0].items() if v} == {z for z, v in witnesses[161][0].items() if v}
    print(f"the two witnesses have {'the same' if same else 'different'} one-site sets")
    # cross-checks
    random.seed(20260922)
    agree = dis = brute = 0
    for trial in range(n_rand + n_pert):
        if trial < n_rand:
            sites = [(a, b, c) for a in range(3) for b in range(3) for c in range(5)]
            zeta = {z: 1 for z in sites if random.random() < 0.3}
        else:
            sites = SITES
            zeta = {tuple(z): 1 for z in witnesses[random.choice(list(LOGS))][1]}
            for _ in range(random.choice((1, 2, 3))):
                z = random.choice(sites)
                if z in zeta: del zeta[z]
                else: zeta[z] = 1
        eta = run_automaton(sites, zeta)
        ones = [z for z, v in eta.items() if v]
        if not ones: continue
        _, npred, kind = m.kinds(eta)
        cand = [z for z in ones if kind[z] == "proc" and lev(z) >= 3] or ones
        x = random.choice(cand)
        r = MinTree(eta, x).solve(1.0)
        ref = (None if r is None else r["E"] - 3 * (r["S"] - 1) - r["A"], rooted(eta, x)[0])
        mine = (exact_min(eta, x), exact_min(eta, x, rooted=True))
        ok = ref == mine
        if len(ones) <= 14:
            brute += 1; ok = ok and m.brute_min(eta, x, 1) == mine[0]
        agree += ok; dis += (not ok)
        if not ok: print("HIT: levdp disagrees with the campaign solver at", x, ref, mine, sorted(zeta))
    print(f"cross-check: {agree} agree, {dis} disagree ({n_rand} random 3x3x5, {n_pert} witness perturbations; brute_min on {brute}); {time.time() - t0:.0f}s")
    print(f"SUMMARY: both witnesses verified: (unrooted, rooted) min cost (1, 1) at {X} on 6x6x9 by the solver-free DP and by MinTree; "
          f"the site's family constant is 16/15; levdp agrees with the campaign solver on {agree} of {agree + dis} cross-check configurations")


if __name__ == "__main__":
    main()
