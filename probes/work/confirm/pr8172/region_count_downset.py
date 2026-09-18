#!/usr/bin/env python3
"""J:confirm:J-attack-PR8172 - independent test of the finder's executed-number HIT on block 28 (PR #8172): the T2 proof's executed
parenthetical "the exact |U(I)| on 120 random islands is at most 4.05(D + 1)^3" against the runner's "on 120 random islands (largest
ratio 6671/1728)" and the exact spec's "on 200 random islands ... worst |U|/(D+1)^3 = 4.043".

Different machinery from the runner, the spec and the finder (who compared the printed numbers only):
  * both island sets are regenerated exactly from their generators (the runner's random.seed(28) stream, first 120 of 300 islands; the
    spec's random.seed(4) stream after its 300 eroder islands, 200 islands), read from the PR head;
  * |U(I)| is counted by a different algorithm: the forward cone F_{D+1}(I) is enumerated explicitly (each island site plus every
    composition of D + 1 into three non-negative parts) and its down-set is built level by level through the predecessor map
    y -> y - e_j down to level 1 (the runner and the spec test tau(max(i, y)) <= D + 1 over a bounding box); the two are compared on
    all 120 runner islands;
  * ratios are exact rationals; a hill-climb over islands in the generator's box records how large |U|/(D + 1)^3 gets beyond the
    random samples (context for the sample statement; the proved bound is 18);
  * found while recounting: the two counts differ on some islands, so the proof's box (y_j <= 2D + 1, from x_j <= D + 1 + i_j <= 2D + 1)
    is tested directly: the second inequality needs i_j <= D, and islands with a coordinate maximum above D are counted both ways; the
    box y_j <= D + 1 + M_j (which follows from x >= i and tau(x) = D + 1 alone) is checked as the replacement: at level s it holds
    C(4D + 5 - s, 2) sites, so |U| <= (D + 1)(4D + 4)(4D + 3)/2 = 8(D + 1)^3 - 2(D + 1)^2.
Prints "HIT: confirmed - ..." when this test reaches the finder's conclusion, and says what it does not reproduce.
"""
import random
import re
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BRANCH = "physics-loop/admissibility-induced-law-block28-map-of-memory-four-laws-located-healing-influence-20260916"
HEAD = "c8ae4a4622c1aa924ff6c9b3452021022f20746d"
NOTE = ("docs/ADMISSIBILITY_RULE_MAP_OF_MEMORY_WHERE_EACH_OF_THE_FOUR_LAWS_KEEPS_ITS_PLANE_LOCATED_AGAINST_THE_PROVED_REGIONS_WITH_THE_"
        "HEALING_AND_INFLUENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-16.md")
RUNNER = "scripts/admissibility_rule_map_of_memory_four_laws_transitions_located_against_proved_regions_healing_and_influence_bounds_2026_09_16.py"
CACHE = "logs/runner-cache/admissibility_rule_map_of_memory_four_laws_transitions_located_against_proved_regions_healing_and_influence_bounds_2026_09_16.txt"
SPEC = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block28_exact"


def show(path):
    r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", BRANCH], cwd=ROOT, check=True)
        r = subprocess.run(["git", "show", f"{HEAD}:{path}"], cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout


def u_downset(ones):
    I = [(a, b, -a - b) for a, b in ones]
    D = sum(max(i[j] for i in I) for j in range(3))
    level = set()
    for i in I:
        for d1 in range(D + 2):
            for d2 in range(D + 2 - d1):
                level.add((i[0] + d1, i[1] + d2, i[2] + D + 1 - d1 - d2))
    total = 0
    for s in range(D + 1, 0, -1):
        total += len(level)
        if s > 1:
            level = {(y[0] - 1, y[1], y[2]) for y in level} | {(y[0], y[1] - 1, y[2]) for y in level} | {(y[0], y[1], y[2] - 1) for y in level}
    return total, D


def u_join(ones):
    I = [(a, b, -a - b) for a, b in ones]
    D = sum(max(i[j] for i in I) for j in range(3))
    B = 2 * D + 1
    cnt = 0
    for y1 in range(-3 * B - 3, B + 1):
        for y2 in range(-3 * B - 3, B + 1):
            for s in range(1, D + 2):
                y = (y1, y2, s - y1 - y2)
                if y[2] <= B and any(sum(max(i[j], y[j]) for j in range(3)) <= D + 1 for i in I):
                    cnt += 1
    return cnt, D


def main():
    t0 = time.time()
    note = show(NOTE)
    runner = show(RUNNER)
    cache = show(CACHE)
    spec_py = show(SPEC + ".py")
    spec_out = show(SPEC + ".out.txt")
    stated_n, stated_r = re.search(r"the exact `\|U\(I\)\|` on `(\d+)` random islands is at most `([0-9.]+)\(D \+ 1\)³`", note).groups()
    stated_n, stated_r = int(stated_n), Fraction(stated_r)
    cache_n, cache_p, cache_q = map(int, re.search(r"on (\d+) random islands \(largest ratio (\d+)/(\d+)\)", cache).groups())
    spec_n, spec_r = re.search(r"on (\d+) random islands: True; worst \|U\|/\(D\+1\)\^3 = ([0-9.]+)", spec_out).groups()
    assert "random.seed(28)" in runner and "for ones in islands[:120]:" in runner and "n = random.randint(1, 10)" in runner
    assert "random.seed(4)" in spec_py and "n = random.randint(1, 12)" in spec_py and "for trial in range(200):" in spec_py
    # the runner's islands
    rnd = random.Random(28)
    run_isl = []
    for _ in range(300):
        n = rnd.randint(1, 10)
        run_isl.append({(rnd.randint(-4, 4), rnd.randint(-4, 4)) for _ in range(n)})
    run_isl = run_isl[:120]
    # the spec's islands: 300 eroder islands first, then 200 for the region count
    rnd = random.Random(4)
    for _ in range(300):
        n = rnd.randint(1, 12)
        _ = {(rnd.randint(-4, 4), rnd.randint(-4, 4)) for _ in range(n)}
    spec_isl = []
    for _ in range(200):
        n = rnd.randint(1, 10)
        spec_isl.append({(rnd.randint(-4, 4), rnd.randint(-4, 4)) for _ in range(n)})
    res_run = [u_downset(o) for o in run_isl]
    res_spec = [u_downset(o) for o in spec_isl]
    join_run = [u_join(o) for o in run_isl]
    diff = [(o, a, b) for o, a, b in zip(run_isl, res_run, join_run) if a != b]
    agree = not diff

    def maxima(o):
        I = [(x, y, -x - y) for x, y in o]
        M = [max(i[j] for i in I) for j in range(3)]
        return M, sum(M)

    over = [o for o in run_isl if max(maxima(o)[0]) > maxima(o)[1]]
    diff_is_over = {frozenset(o) for o, _, _ in diff} == {frozenset(o) for o in over}
    all_under = all(b[0] < a[0] for _, a, b in diff)
    ex = max(diff, key=lambda t: t[1][0] - t[2][0])
    one = [({(1, 0)}, (1, 0, -1)), ({(-1, -1)}, (-1, -1, 2))]
    one_rows = [(t, u_downset(o), u_join(o)) for o, t in one]
    x_bad = (2, 0, -1)                                   # i + e_1 for i = (1, 0, -1), a level-1 site of F_1
    step_fails = sum(x_bad) == 1 and all(x_bad[j] >= (1, 0, -1)[j] for j in range(3)) and x_bad[0] > 2 * 0 + 1
    newbox = all(c <= (d + 1) * (4 * d + 4) * (4 * d + 3) // 2 for c, d in res_run + res_spec)
    r_run = max(Fraction(c, (d + 1) ** 3) for c, d in res_run)
    r_spec = max(Fraction(c, (d + 1) ** 3) for c, d in res_spec)
    bound18 = all(c <= 18 * (d + 1) ** 3 for c, d in res_run + res_spec)
    d_run = max(d for _, d in res_run)
    print(f"[inputs] at {HEAD[:10]}: note '{stated_n} random islands ... at most {stated_r}(D+1)^3'; runner cache '{cache_n} islands, largest "
          f"{cache_p}/{cache_q}'; spec '{spec_n} islands, worst {spec_r}'")
    print(f"[box] the join-test count (the runner's and the spec's, box y_j <= 2D + 1) equals the down-set count on all 120 runner islands: "
          f"{agree}; islands where they differ: {len(diff)}, the join count smaller on every one: {all_under}; they are exactly the islands with "
          f"a coordinate maximum above D: {diff_is_over}; largest gap {ex[1][0]} (down-set) vs {ex[2][0]} (join) at D = {ex[1][1]}, maxima "
          f"{maxima(ex[0])[0]}; one-site islands: " + "; ".join(f"{t}: down-set |U| = {a[0]}, join {b[0]}" for t, a, b in one_rows)
          + f"; the proof's step x_j <= D + 1 + i_j <= 2D + 1 at i = (1, 0, -1), D = 0: x = {x_bad} lies in F_1 with x_1 = 2 > 2D + 1 = 1: "
          f"{step_fails}; every recount (runner, spec) within the box y_j <= D + 1 + M_j bound (D+1)(4D+4)(4D+3)/2: {newbox}")
    print(f"[recount] runner's 120 islands (seed 28): largest |U|/(D+1)^3 = "
          f"{r_run} = {float(r_run):.6f} (cache {cache_p}/{cache_q}: {r_run == Fraction(cache_p, cache_q)}), D up to {d_run}; spec's 200 islands "
          f"(seed 4): largest {r_spec} = {float(r_spec):.6f} (spec prints {spec_r}); all within 18 (D+1)^3: {bound18}  ({time.time() - t0:.0f}s)")
    holds_run = r_run <= stated_r
    holds_spec = r_spec <= stated_r
    ceil2 = Fraction(-(-r_spec.numerator * 100 // r_spec.denominator), 100)
    print(f"[sentence] 'at most {stated_r}' holds on the runner's {stated_n} islands: {holds_run} (largest {float(r_run):.4f}); on the spec's 200: "
          f"{holds_spec}; {stated_r} = the spec's 200-island largest rounded up to two decimals ({ceil2}): {ceil2 == stated_r}; the runner's own "
          f"largest rounded up would be {Fraction(-(-r_run.numerator * 100 // r_run.denominator), 100)}")
    # hill-climb for context
    rng = random.Random(8172)
    best, best_isl = Fraction(0), None
    box = 4
    deadline = time.time() + 45
    while time.time() < deadline:
        cur = {(rng.randint(-box, box), rng.randint(-box, box)) for _ in range(rng.randint(1, 10))}
        c, d = u_downset(cur)
        val = Fraction(c, (d + 1) ** 3)
        for _ in range(60):
            cand = set(cur)
            mv = rng.random()
            if mv < 0.4 and len(cand) > 1:
                cand.remove(rng.choice(sorted(cand)))
            elif mv < 0.7:
                cand.add((rng.randint(-box, box), rng.randint(-box, box)))
            else:
                p = rng.choice(sorted(cand))
                cand.remove(p)
                cand.add((max(-box, min(box, p[0] + rng.choice((-1, 0, 1)))), max(-box, min(box, p[1] + rng.choice((-1, 0, 1))))))
            c2, d2 = u_downset(cand)
            v2 = Fraction(c2, (d2 + 1) ** 3)
            if v2 >= val:
                cur, val = cand, v2
        if val > best:
            best, best_isl = val, sorted(cur)
    bc, bd = u_downset(best_isl)
    newbox = newbox and bc <= (bd + 1) * (4 * bd + 4) * (4 * bd + 3) // 2
    print(f"[climb] 45 s of hill-climbing over islands in the generators' box [-4, 4]^2: largest |U|/(D+1)^3 = {best} = {float(best):.4f} at D = {bd} "
          f"(|U| = {bc}), island {best_isl}; the proved constant is 18")
    hits = []
    if r_run == Fraction(cache_p, cache_q) and r_run != stated_r and abs(r_spec - stated_r) < Fraction(1, 100):
        hits.append(f"the note's executed bound '{stated_r}(D+1)^3 on {stated_n} random islands' is the spec's 200-island largest ratio {float(r_spec):.4f} "
                    f"rounded up, not the runner's {stated_n}-island largest {r_run} = {float(r_run):.4f} (both island sets regenerated and recounted "
                    f"by the down-set); the bound itself holds on both sets")
    for h in hits:
        print("HIT: confirmed - " + h)
    new = []
    if step_fails and diff:
        new.append(f"T2's count bounds every site of U(I) by y_j <= 2D + 1 through x_j <= D + 1 + i_j <= 2D + 1, whose second step needs i_j <= D and "
                   f"fails when a coordinate maximum exceeds D (i = (1, 0, -1): D = 0 and x = (2, 0, -1) in F_1 has x_1 = 2 > 1); the runner's C2 "
                   f"count uses that box and undercounts |U| on {len(diff)} of its 120 islands (true {ex[1][0]} vs {ex[2][0]} at D = {ex[1][1]}; "
                   f"3 vs {one_rows[1][2][0]} for the one-site island (-1, -1, 2)); the stated 18(D+1)^3 survives: the box y_j <= D + 1 + M_j gives "
                   f"|U| <= (D+1)(4D+4)(4D+3)/2 <= 8(D+1)^3, met by every recount: {newbox}")
    for h in new:
        print("HIT: new - " + h)
    print(f"SUMMARY: {'confirmed as an attribution slip, not a false bound' if hits else 'not reproduced'} - runner's 120 islands largest "
          f"{float(r_run):.4f}, spec's 200 islands largest {float(r_spec):.4f}, stated 'at most {stated_r} on {stated_n} islands' (true on both sets: "
          f"{holds_run and holds_spec}); the finder's test compared an upper bound as an equality, so the bound's truth is not in question; "
          f"{'new: the proof box y_j <= 2D + 1 fails for islands with a coordinate maximum above D and the runner undercounts |U| on ' + str(len(diff)) + ' of 120 islands (the largest ratios are unaffected); the bound survives via y_j <= D + 1 + M_j, |U| <= 8(D+1)^3; ' if new else ''}"
          f"the hill-climb reaches {float(best):.3f} (D = {bd})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
