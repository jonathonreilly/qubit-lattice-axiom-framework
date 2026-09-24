#!/usr/bin/env python3
"""Referee for corrigendum-PR8149 a1.

Author w-jonathonsmac4f50-jf298 (claude-opus-5). Own orbit count of the star.
"""
import itertools
from collections import Counter, defaultdict
from fractions import Fraction as Fr
from math import factorial

fails = []
AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
IDX = {v: i for i, v in enumerate(AXES)}
OPP = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def kernel(p, q, r):
    p, q, r = Fr(p), Fr(q), Fr(r)
    z = p + q + 4 * r
    return [[(p if a == b else q if b == OPP[a] else r) / z for b in range(6)] for a in range(6)]


def outside():
    leaves = AXES
    out = {}
    for leaf in leaves:
        nbrs = []
        for step in AXES:
            site = tuple(leaf[i] + step[i] for i in range(3))
            if site != (0, 0, 0):
                nbrs.append(site)
        out[leaf] = nbrs
    all_out = sorted({s for nbrs in out.values() for s in nbrs})
    shared = [s for s in all_out if sum(s in out[L] for L in leaves) == 2]
    report(
        "geometry",
        len(all_out) == 18 and len(shared) == 12 and all(len(out[L]) == 5 for L in leaves),
        f"{len(all_out)} outside sites, {len(shared)} corners shared by two leaves; environment space 6^18",
    )
    return out, all_out


def matrices():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = tuple(tuple(signs[i] if j == perm[i] else 0 for j in range(3)) for i in range(3))
            mats.append(M)
    return mats


def apply(M, x):
    return tuple(sum(M[i][j] * x[j] for j in range(3)) for i in range(3))


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def families(all_out):
    six = []
    for M in matrices():
        seen = set()
        a = 0
        while a not in seen:
            seen.add(a)
            a = IDX[apply(M, AXES[a])]
        if len(seen) == 6:
            six.append(M)
    groups = {}
    eye = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for M in six:
        el, cur = [], eye
        for _ in range(6):
            cur = mul(M, cur)
            el.append(cur)
        groups.setdefault(frozenset(el), M)
    fams = []
    orbit_ok = True
    for M in groups.values():
        seen, orbits = set(), []
        for s in all_out:
            if s in seen:
                continue
            orb, t = [], s
            while t not in seen:
                seen.add(t)
                orb.append(t)
                t = apply(M, t)
            orbits.append(orb)
        orbit_ok &= sorted(len(o) for o in orbits) == [6, 6, 6]
        envs = set()
        for choice in itertools.product(range(6), repeat=3):
            env = {}
            good = True
            for oi, orb in enumerate(orbits):
                v = choice[oi]
                for s in orb:
                    if s in env and env[s] != v:
                        good = False
                    env[s] = v
                    v = IDX[apply(M, AXES[v])]
            if good and len(env) == 18:
                envs.add(tuple(env[s] for s in all_out))
        fams.append(envs)
    union = set().union(*fams)
    report(
        "four families",
        len(matrices()) == 48 and len(six) == 8 and len(groups) == 4 and orbit_ok
        and all(len(f) == 216 for f in fams) and len(union) == 840,
        f"{len(six)} six-cycles, {len(groups)} subgroups, family sizes {[len(f) for f in fams]}, union {len(union)}",
    )
    return fams


def phi_constant(env_t, all_out, out, K):
    env = dict(zip(all_out, env_t))
    vals = []
    for a in range(6):
        tot = Fr(1)
        for leaf, nbrs in out.items():
            acc = Fr(0)
            for t in range(6):
                x = K[a][t]
                for s in nbrs:
                    x *= K[env[s]][t]
                acc += x
            tot *= acc
        vals.append(tot)
    return all(v == vals[0] for v in vals)


def factors(rule):
    K = kernel(*rule)
    cls = defaultdict(int)
    for ms in itertools.combinations_with_replacement(range(6), 5):
        vec = []
        for a in range(6):
            acc = Fr(0)
            for s in range(6):
                x = K[a][s]
                for o in ms:
                    x *= K[o][s]
                acc += x
            vec.append(acc)
        ratio = tuple(x / vec[0] for x in vec[1:])
        weight = factorial(5)
        for n in Counter(ms).values():
            weight //= factorial(n)
        cls[ratio] += weight
    const = [r for r in cls if all(x == 1 for x in r)]
    inv = [r for r in cls if tuple(Fr(1) / x for x in r) in cls]
    return len(cls), len(const), len(inv)


def main():
    out, all_out = outside()
    fams = families(all_out)
    if not fails:
        K = kernel(3, 1, 2)
        bad = sum(not phi_constant(e, all_out, out, K) for f in fams for e in f)
        report("phi constant", bad == 0, f"all {sum(len(f) for f in fams)} equivariant environments at (3,1,2) have constant Phi")
    n312, c312, i312 = factors((3, 1, 2))
    n412, c412, i412 = factors((4, 1, 2))
    report(
        "leaf factors",
        n312 == 234 and c312 == 0 and i312 == 0 and n412 == 146 and c412 == 0 and i412 == 8,
        f"(3,1,2): {n312} factors, {c312} constant, {i312} inverse; "
        f"(4,1,2): {n412} factors, {c412} constant, {i412} inverse",
    )
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the centre-first star has 18 outside sites. Exactly four cyclic subgroups "
        "act as 6-cycles on the values; each has 216 equivariant environments and their union is 840. "
        "At (3,1,2) no leaf factor is constant and no two are inverse, so agreement needs at least three leaves."
    )
    print(
        "SUMMARY: confirmed 18 sites, 8 six-cycles, 4 subgroups, 216 each, union 840, "
        "and the leaf-factor counts 234 and 146. The full 6^18 search remains open; 840 is a lower bound."
    )


if __name__ == "__main__":
    main()
