#!/usr/bin/env python3
"""A gradient-type adversarial search of the field inequality (5.5), Text 5. The obligation asks for one: the hill climbs so far moved links one at a time or in hand-made groups.

Ratio := |W(dP) - 1| / ( L^-2 ||f||_{l^1(rough)} + ||f||_{l^2(not rough)} ), on the hull of one coarse plaquette, with the map of hard-core--independent_field_ineq.py, final rule, L = 3.
Search: simultaneous perturbation (Spall), all 4 x |hull region| links at once. At each step a random sign pattern Delta on the su(2) components of every link gives
    g_l = (Ratio(+ delta Delta) - Ratio(- delta Delta)) / (2 delta) Delta_l,   and the field moves by exp(i a g_l / |g|_max), a fixed step in the worst link, accepted only if Ratio does not fall by more than 2 percent.
Starts: the sheet of Ratio 1, small noise, a smooth constant flux, and Haar noise at a few strengths. The map is piecewise smooth, so a gradient is only an estimate, which is why this is a stochastic estimate and not differentiation.

Pre-registered criteria, written before the first run.
    PASS-SPSA: best Ratio at most the bound 12 (log L)^(1/2) = 12.58 at L = 3, the only thing the theorem's constant has to beat in the check file. Report the best Ratio from each start.
    ABOVE-ONE: if any best Ratio exceeds 1.05, report it: it would be the first field above the sheet, and it says C_OS >= that, not that the theorem fails.
    FAIL-SPSA: a Ratio above the bound. Then C_OS has to be read again, and Theorem 5.5 with it.
This can fail to find anything, and that does not prove the inequality. L = 3 only, one coarse plaquette, about 1300 links.

Design change before any result: a first version moved all links at once. From the sheet no move was accepted in 800 iterations, because sqrt(sum f^2) has a kink at f = 0 on the many flat plaquettes, so a generic small move on all links raises the denominator at first order. It told nothing, and I stopped it. Now each step moves a random 5 percent of the links, and a move is accepted if Ratio does not fall.

Run under the numeric lock, nice, RSS checked against 2 GB.
"""
import importlib.util
import math
import pathlib
import random
import sys
import time

HERE = pathlib.Path(__file__)
spec = importlib.util.spec_from_file_location("field_ineq", HERE.with_name("hard-core--independent_field_ineq.py"))
fi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fi)

L = 3
DIM = fi.DIM


def exp_su2(v):
    t = math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
    if t < 1e-14:
        return fi.ONE
    s = math.sin(t) / t
    return (math.cos(t), v[0] * s, v[1] * s, v[2] * s)


def links():
    o = (L - 1) // 2
    out = []
    for a in range(-o, L + o + 1):
        for b in range(-o, L + o + 1):
            for c in range(-o, o + 1):
                for d in range(-o, o + 1):
                    for mu in range(DIM):
                        out.append(((a, b, c, d), mu))
    return out


def run_start(name, base, init, rng, iters, delta, step):
    ls = links()
    field = dict(init)
    cur = fi.ratio_of(fi.overlay(base, field), L)[0]
    best = cur
    t0 = time.time()
    accepted = 0
    print(f"  start {name}: Ratio {cur:.4f}, links {len(ls)}", flush=True)
    for it in range(iters):
        chosen = rng.sample(ls, max(1, len(ls) // 20))
        signs = {l: (rng.choice((-1, 1)), rng.choice((-1, 1)), rng.choice((-1, 1))) for l in chosen}
        plus = dict(field)
        minus = dict(field)
        for l in chosen:
            c = field.get(l, base(l[0], l[1]))
            sg = signs[l]
            plus[l] = fi.qmul(exp_su2((delta * sg[0], delta * sg[1], delta * sg[2])), c)
            minus[l] = fi.qmul(exp_su2((-delta * sg[0], -delta * sg[1], -delta * sg[2])), c)
        rp = fi.ratio_of(fi.overlay(base, plus), L)[0]
        rm = fi.ratio_of(fi.overlay(base, minus), L)[0]
        slope = (rp - rm) / (2 * delta)
        if slope == 0.0:
            continue
        new = dict(field)
        sgn = 1 if slope > 0 else -1
        for l in chosen:
            c = field.get(l, base(l[0], l[1]))
            sg = signs[l]
            a = step * sgn
            new[l] = fi.qmul(exp_su2((a * sg[0], a * sg[1], a * sg[2])), c)
        rn = fi.ratio_of(fi.overlay(base, new), L)[0]
        if rn >= cur:
            field = new
            cur = rn
            accepted += 1
            best = max(best, cur)
        if it % 200 == 0:
            print(f"    {name} it={it} cur={cur:.4f} best={best:.4f} accepted={accepted} t={time.time() - t0:.0f}", flush=True)
        fi.check_rss()
    print(f"  end {name}: best Ratio {best:.4f}", flush=True)
    return best


def main():
    iters = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    rng = random.Random(20261031)
    bests = {}
    flat = lambda s, mu: fi.ONE
    sheet = (lambda q: (lambda s, mu: q if (mu == 0 and s[0] == 1 and s[1] >= 2) else fi.ONE))(fi.rot(1.0))
    bests["sheet"] = run_start("sheet", sheet, {}, rng, iters, 0.002, 0.002)
    # smooth constant flux in the (0, 1) plane: U_(s, 1) = exp(i f s_0 sigma_1), small enough to be regular
    smooth = lambda s, mu: fi.rot(0.02 * s[0]) if mu == 1 else fi.ONE
    bests["smooth"] = run_start("smooth", smooth, {}, rng, iters, 0.002, 0.002)
    noise = {}
    for l in links():
        g = [rng.gauss(0, 0.05) for _ in range(3)]
        noise[l] = exp_su2(g)
    bests["noise"] = run_start("noise", flat, noise, rng, iters, 0.002, 0.002)
    big = {}
    for l in links():
        g = [rng.gauss(0, 0.5) for _ in range(3)]
        big[l] = exp_su2(g)
    bests["rough"] = run_start("rough", flat, big, rng, iters, 0.01, 0.01)
    bound = 12 * math.sqrt(math.log(L))
    top = max(bests.values())
    print(f"best by start: { {k: round(v, 4) for k, v in bests.items()} }, bound {bound:.2f}")
    if top > 1.05:
        print(f"ABOVE-ONE: {top:.4f}")
    print("PASS-SPSA" if top <= bound else "FAIL-SPSA")


if __name__ == "__main__":
    main()
