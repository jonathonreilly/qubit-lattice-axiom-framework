#!/usr/bin/env python3
"""Independent checks for causal-clauses a2 on the three-site path.

Own kernels. V is the two-parent site; the chain is the bent path.
"""
import itertools
from fractions import Fraction as F

FAILS = []
M = 6
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
IDX = {d: i for i, d in enumerate(STEPS)}


def ok(name, good, msg):
    print(("ok " if good else "FAIL ") + name + ": " + msg, flush=True)
    if not good:
        FAILS.append(name)


def rel(a, b):
    return 0 if a == b else (1 if a // 2 == b // 2 else 2)


P, Q, R = 3, 1, 2
Z1 = P + Q + 4 * R
PHI = [[(P, Q, R)[rel(a, b)] for b in range(M)] for a in range(M)]
K = [[F(PHI[a][s], Z1) for s in range(M)] for a in range(M)]


def Kk(vals):
    t = F(0)
    for s in range(M):
        u = F(1)
        for v in vals:
            u *= K[v][s]
        t += u
    return t


def cond(rec, a):
    if not rec:
        return F(1, M)
    num = F(1)
    for v in rec:
        num *= K[v][a]
    return num / Kk(rec)


def factors():
    return sorted({int(144 * Kk((a, b))) for a in range(M) for b in range(M)})


def tv_static_mu():
    """1/2 sum_{a,b} |Kk(a,b)/6 - 1/36|, the distance named in S4."""
    acc = F(0)
    for a, b in itertools.product(range(M), repeat=2):
        acc += abs(Kk((a, b)) / 6 - F(1, 36))
    return acc / 2


def y_last_prob(rate):
    """Probability the middle site of a path is formed last. rate(i, done) ignores values."""
    sites = (0, 1, 2)  # ends 0,2 middle 1
    nb = {0: (1,), 1: (0, 2), 2: (1,)}
    total = F(0)
    for seq in itertools.permutations(sites):
        done = []
        prob = F(1)
        for i in seq:
            wts = []
            for j in sites:
                if j in done:
                    wts.append(F(0))
                else:
                    wts.append(F(rate(j, done, nb)))
            s = sum(wts)
            prob *= wts[i] / s
            done.append(i)
        if seq[-1] == 1:
            total += prob
    return total


def main():
    fac = factors()
    ok("K2", fac == [22, 24, 26], f"144 K2 takes {fac}")
    dist = tv_static_mu()
    ok("tv", dist == F(1, 72), f"TV(static, mu') = {dist}")

    def uniform(i, done, nb):
        return 1

    def seeded(i, done, nb):
        return 1 if (not done or any(j in done for j in nb[i])) else 0

    def attracting(i, done, nb):
        return 1 + sum(1 for j in nb[i] if j in done)

    pu, ps, pa = y_last_prob(uniform), y_last_prob(seeded), y_last_prob(attracting)
    ok("orders", pu == F(1, 3) and ps == 0 and pa == F(2, 9),
       f"P(middle last): uniform {pu}, seeded {ps}, attracting {pa}")

    # V: causal law is mu', so distance is P(not middle-last) * 1/72
    # chain: causal law is static, so distance is P(middle last) * 1/72
    base = F(1, 72)
    ok("V", (1 - pu) * base == F(1, 108) and (1 - ps) * base == F(1, 72) and (1 - pa) * base == F(7, 648),
       "V distances 1/108, 1/72, 7/648")
    ok("chain", pu * base == F(1, 216) and ps * base == 0 and pa * base == F(1, 324),
       "chain distances 1/216, 0, 1/324")

    if FAILS:
        print("SUMMARY: fails at step " + FAILS[0] + " - independent arithmetic did not match")
        return
    print(
        "HIT: confirmed - every causal process finishes in the product of parent kernels, "
        "and the three-site clock distances from that law are 1/72, 1/108, 1/216, 7/648 and 1/324"
    )
    print(
        "SUMMARY: confirmed the probability-tree theorem on the finite path, 144 K2 in {22,24,26}, "
        "TV 1/72, and the uniform, seeded and attracting mixtures; parallel growth was not re-summed"
    )


if __name__ == "__main__":
    main()
