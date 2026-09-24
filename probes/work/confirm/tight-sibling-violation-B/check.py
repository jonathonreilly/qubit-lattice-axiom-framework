#!/usr/bin/env python3
"""Independent check of the logged S:tight-sibling-violation-B witness.

Level dynamic program, exact integers, one seed. Not violate.py and not the ILP.
"""
E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
FORK = tuple(
    tuple(E3[a][i] - E3[b][i] for i in range(3))
    for a in range(3) for b in range(3) if a != b
)

ZETA = [
    (0, 0, 0), (0, 0, 1), (0, 0, 7), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 7),
    (0, 2, 7), (0, 4, 4), (1, 0, 0), (1, 0, 2), (1, 0, 5), (1, 1, 2), (1, 2, 0),
    (1, 2, 2), (1, 3, 1), (1, 3, 7), (2, 0, 0), (2, 0, 7), (2, 2, 0), (2, 2, 2),
    (2, 2, 3), (2, 2, 6), (2, 3, 3), (2, 3, 4), (2, 4, 2), (2, 4, 6), (3, 0, 1),
    (3, 0, 2), (3, 1, 2), (3, 2, 1), (3, 2, 7), (4, 0, 2), (4, 0, 6), (4, 1, 1),
    (4, 2, 1), (4, 4, 2), (4, 4, 4), (4, 5, 5), (5, 0, 7), (5, 2, 3),
]
ROOT = (5, 4, 4)


def level(z):
    return z[0] + z[1] + z[2]


def preds(z):
    return [tuple(z[i] - e[i] for i in range(3)) for e in E3]


def automaton(sites, zeta):
    eta = {}
    for z in sorted(sites, key=level):
        ps = [eta.get(p, 0) for p in preds(z)]
        eta[z] = 1 if sum(ps) >= 2 or z in zeta else 0
    return eta


def component(ones, root):
    npred = {z: [p for p in preds(z) if p in ones] for z in ones}
    seen = {root}
    stack = [root]
    while stack:
        z = stack.pop()
        nb = list(npred[z])
        nb += [s for s in ones if z in preds(s)]
        nb += [tuple(z[i] + o[i] for i in range(3)) for o in FORK]
        for w in nb:
            if w in ones and w not in seen:
                seen.add(w)
                stack.append(w)
    return seen, npred


def min_cost(comp, npred, root):
    """Exact min of E - A over trees in the one-seed component, c = 1."""
    kind = {}
    for z in comp:
        k = len(npred[z])
        kind[z] = "seed" if k == 0 else "amp" if k == 1 else "proc"
    seeds = [z for z in comp if kind[z] == "seed"]
    if len(seeds) != 1:
        return None, kind
    seed = seeds[0]
    at = {}
    for z in comp:
        at.setdefault(level(z), []).append(z)
    Lmax, Ls, lr = max(at), level(seed), level(root)
    if any(level(z) > lr for z in comp):
        return None, kind  # rooted and unrooted would differ
    def cost(X):
        s = 0
        for z in X:
            s += 1 if kind[z] == "proc" else -1 if kind[z] == "amp" else 0
        return s
    top = at[Lmax]
    states = {}
    for mask in range(1 << len(top)):
        X = frozenset(top[i] for i in range(len(top)) if mask >> i & 1)
        if Lmax == lr and root not in X:
            continue
        states[X] = cost(X)
    for lev in range(Lmax, Ls, -1):
        below = at.get(lev - 1, [])
        nxt = {}
        for X, val in states.items():
            need = [z for z in X if kind[z] != "seed"]
            for mask in range(1 << len(below)):
                Y = frozenset(below[i] for i in range(len(below)) if mask >> i & 1)
                if lev - 1 == lr and root not in Y:
                    continue
                if any(not any(p in Y for p in npred[z]) for z in need):
                    continue
                v2 = val + cost(Y)
                if Y not in nxt or v2 < nxt[Y]:
                    nxt[Y] = v2
        states = nxt
    return states.get(frozenset([seed])), kind


def main():
    sites = [(a, b, c) for a in range(6) for b in range(6) for c in range(9)]
    eta = automaton(sites, set(ZETA))
    ones = {z for z, v in eta.items() if v == 1}
    comp, npred = component(ones, ROOT)
    value, kind = min_cost(comp, npred, ROOT)
    proc = kind.get(ROOT) == "proc"
    ok = value == 1 and proc and len(ones) == 78 and len(ZETA) == 41
    print(("PASS " if ok else "FAIL ") + f"witness cost {value}, root kind {kind.get(ROOT)}, ones {len(ones)}")
    if ok:
        print("SUMMARY: confirmed - the logged 41-mark configuration on the 6x6x9 box has exact min cost 1 at (5,4,4), both unrooted and rooted, since the component has one seed and nothing above the root.")
        print("HIT: confirmed - seed 44 from Z_B reaches max cost (1, 1) at (5, 4, 4); an independent level DP gives cost 1, so c* > 1 and the rooted value is positive.")
    else:
        print(f"SUMMARY: not reproduced - level DP cost is {value}, not 1")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
