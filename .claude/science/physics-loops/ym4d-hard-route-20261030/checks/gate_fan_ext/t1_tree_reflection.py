#!/usr/bin/env python3
"""T1: tree cover (Section 3) and discrete reflection (Section 4). See CRITERIA.md."""
import itertools, random, resource, sys

K, M_, D = 80, 328, 4
NU = 1 + (K + 2) ** D


def guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 2e9:
        sys.exit("RSS above 2 GB")


# ---- Section 3: split a cube of the tiling (3.1) -------------------------
def walls(b, coord, m):
    """offset of the walls perpendicular to coord (1..4), given m_(coord+1..4)."""
    off = 0
    for j in range(coord + 1, 5):
        off += m[j] * b // 2 ** (j - coord)
    return off


def tree(b, lo, hi, m, coord):
    """lo, hi: closed cube, real walls at integer points; returns nested tree."""
    while coord >= 1:
        off = walls(b, coord, m)
        k = (lo[coord] - off) // b
        w = off + (k + 1) * b  # first wall above lo
        inside = lo[coord] < w <= hi[coord]
        if inside:
            l, h = dict(lo), dict(hi)
            h[coord], l[coord] = w, w
            ml, mu = dict(m), dict(m)
            ml[coord], mu[coord] = k, k + 1
            return (coord, tree(b, lo, h, ml, coord - 1), tree(b, l, hi, mu, coord - 1))
        m = dict(m)
        m[coord] = k
        coord -= 1
    return "o"


def nodes(t):
    return [] if t == "o" else [t[0]] + nodes(t[1]) + nodes(t[2])


def check_cover(trials=200000):
    b = 8 * 64
    r = b // 64
    worst = 0
    seen = set()
    for _ in range(trials):
        lo, hi, m = {}, {}, {}
        for j in range(1, 5):
            c = random.randrange(-8 * b, 8 * b)
            lo[j], hi[j] = c - r, c + r
        t = tree(b, lo, hi, m, 4)
        n = nodes(t)
        assert len(n) == len(set(n)) and len(n) <= 4, (t, lo, hi)
        worst = max(worst, len(n))
        seen.add(t)
    print("cover: max nodes", worst, "distinct shapes seen", len(seen))
    return seen


# ---- Section 4 ------------------------------------------------------------
def all_trees(coords):
    """every tree on a subset of coords, decreasing along paths, distinct overall."""
    out = ["o"]
    coords = sorted(coords, reverse=True)
    for i, c in enumerate(coords):
        rest = coords[i + 1 :]
        for r in range(len(rest) + 1):
            for L in itertools.combinations(rest, r):
                R = [x for x in rest if x not in L]
                for a in all_trees(list(L)):
                    for bb in all_trees(R):
                        out.append((c, a, bb))
    return out


def leaves(t, path=()):
    if t == "o":
        return [path]
    return leaves(t[1], path + ((t[0], -1),)) + leaves(t[2], path + ((t[0], 1),))


def score(leaf, z):
    s = 0.0
    for c, side in leaf:
        s -= max(z[c], 0.0) if side < 0 else max(-z[c], 0.0)
    return s


def inv_T(t, q, lv, z):
    """(4.1): z_v = max upper - max lower, by leaf index ranges."""
    if t == "o":
        return
    nl = len(leaves(t[1]))
    lo = lv[: nl]
    up = lv[nl:]
    z[t[0]] = max(q[i] for i in up) - max(q[i] for i in lo)
    inv_T(t[1], q, lo, z)
    inv_T(t[2], q, up, z)


def R_map(t, ls, S, z):
    q = [score(l, z) for l in ls]
    F = max(q[i] for i in S) - max(q[i] for i in range(len(ls)) if i not in S)
    q2 = [q[i] - 2 * F if i in S else q[i] for i in range(len(ls))]
    z2 = dict(z)
    inv_T(t, q2, list(range(len(ls))), z2)
    return z2, F


def selected(ls, z):
    q = [score(l, z) for l in ls]
    m = max(q)
    return [i for i, v in enumerate(q) if v == m], q


def round_to_leaf(ls, S, zr):
    q = [score(l, zr) for l in ls]
    best = max(q[i] for i in S)
    i = min(i for i in S if q[i] == best)
    con = dict(ls[i])
    out = {}
    for c, v in zr.items():
        # lattice coordinates are half odd; 2v integer
        import math

        fl = math.floor(v) + 0.5  # nearest half odd
        if c in con:
            if con[c] > 0 and fl < 0:
                fl = 0.5
            if con[c] < 0 and fl > 0:
                fl = -0.5
        out[c] = fl
    assert all(abs(out[c] - zr[c]) <= 0.5 + 1e-12 for c in zr)
    return out, i


def leaf_of(ls, z):
    return next(i for i, l in enumerate(ls) if all((z[c] > 0) == (s > 0) for c, s in l))


def lca_path_ok(t, ls, S, p, q):
    """Section 4 path: every site before the crossing in p's leaf, after it in q's."""
    i, j = leaf_of(ls, p), leaf_of(ls, q)
    if i == j:
        return True
    a, b = dict(ls[i]), dict(ls[j])
    v = next(c for c in a if c in b and a[c] != b[c])
    # stage 1: coordinates constrained only by q's path, at their q values
    x = dict(p)
    for c in q:
        if c in b and c not in a:
            x[c] = q[c]
    if leaf_of(ls, x) != i:
        return False
    y = dict(x)
    y[v] = q[v]
    if leaf_of(ls, y) != j:
        return False
    return i in S and j in S


def check_reflection(samples=4000):
    coords = [1, 2, 3, 4]
    ts = [t for t in all_trees(coords) if t != "o"]
    worst_lip, worst_l1, patterns = 0.0, 0.0, 0
    worst_mult = 0
    for t in ts:
        ls = leaves(t)
        ac = sorted(set(nodes(t)))
        n = len(ls)
        for mask in range(1, 2 ** n - 1):
            S = {i for i in range(n) if mask >> i & 1}
            patterns += 1
            images = {}
            for _ in range(samples):
                z = {c: random.randrange(-40, 40) + 0.5 for c in ac}
                sel, q = selected(ls, z)
                assert len(sel) == 1
                # exact-selected-leaf check
                assert leaf_of(ls, z) == sel[0]
                c0 = random.choice(ac)
                z1 = dict(z)
                z1[c0] += 1
                zs = [z, z1]
                imgs = []
                for w in zs:
                    Rw, F = R_map(t, ls, S, w)
                    RR, F2 = R_map(t, ls, S, Rw)
                    assert all(abs(RR[c] - w[c]) < 1e-9 for c in ac), "involution"
                    assert abs(F2 + F) < 1e-9
                    if leaf_of(ls, w) in S:
                        imgs.append((Rw, dict(w)))
                    else:
                        pi, _ = round_to_leaf(ls, S, Rw)
                        assert leaf_of(ls, pi) in S, "pi in Omega"
                        images.setdefault(tuple(sorted(pi.items())), set()).add(tuple(sorted(w.items())))
                        imgs.append((Rw, pi))
                lip = max(abs(imgs[0][0][c] - imgs[1][0][c]) for c in ac)
                l1 = sum(abs(imgs[0][1][c] - imgs[1][1][c]) for c in ac)
                worst_lip = max(worst_lip, lip)
                worst_l1 = max(worst_l1, l1)
                assert lca_path_ok(t, ls, S, imgs[0][1], imgs[1][1]), "path"
            if images:
                worst_mult = max(worst_mult, max(len(v) for v in images.values()))
        guard()
    print("patterns", patterns, "trees", len(ts))
    print("worst neighbour Lipschitz of R", worst_lip, "(bound 80)")
    print("worst neighbour image l1", worst_l1, "(bound 328)")
    print("worst sampled preimage count", worst_mult, "(bound", NU, ")")
    assert worst_lip <= K and worst_l1 <= M_


if __name__ == "__main__":
    random.seed(20261102)
    check_cover()
    check_reflection(samples=int(sys.argv[1]) if len(sys.argv) > 1 else 1000)
    print("T1 PASS")
