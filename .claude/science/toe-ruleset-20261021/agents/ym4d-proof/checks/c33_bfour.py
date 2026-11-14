"""c33: toy instance of the B_4 step of RLARGE Theorem R1 (iii) (REVIEW_S16_S17 fix R-3b).

Criteria: checks/c33_criteria.md (written before this script). Usage: python3 c33_bfour.py A|B
"""
import sys, itertools, math
import numpy as np


def neigh_offsets(d):
    return [o for o in itertools.product((-1, 0, 1), repeat=d) if any(o)]


class Torus:
    def __init__(self, d, T):
        self.d, self.T = d, T
        self.offs = neigh_offsets(d)

    def add(self, x, o):
        return tuple((a + b) % self.T for a, b in zip(x, o))

    def star_adj(self, x, y):
        return x != y and all(((a - b) % self.T) in (0, 1, self.T - 1) for a, b in zip(x, y))

    def face_adj(self, x, y):
        diff = [((a - b) % self.T) for a, b in zip(x, y)]
        nz = [v for v in diff if v != 0]
        return len(nz) == 1 and nz[0] in (1, self.T - 1)

    def touch(self, Y1, Y2):
        if Y1 & Y2:
            return True
        return any(self.star_adj(a, b) for a in Y1 for b in Y2)

    def boundary(self, Y):
        out = set()
        for y in Y:
            for o in self.offs:
                z = self.add(y, o)
                if z not in Y:
                    out.add(z)
        return out

    def edges(self, Y):
        L = list(Y)
        return sum(1 for i in range(len(L)) for j in range(i + 1, len(L)) if self.face_adj(L[i], L[j]))

    def fatten(self, Y):
        return frozenset(self.add(y, o) for y in Y for o in itertools.product((0, 1), repeat=self.d))


def activity(tor, Y, D):
    s = sum(D[y] for y in Y) + 0.5 * sum(D[z] ** 2 for z in tor.boundary(Y))
    return (1.0 + 0.2 * tor.edges(Y)) * math.exp(s)


def phiT(tor, tup):
    n = len(tup)
    if n == 1:
        return 1.0
    E = [(i, j) for i in range(n) for j in range(i + 1, n) if tor.touch(tup[i], tup[j])]
    if n == 2:
        return -1.0 if E else 0.0
    if n == 3:
        if len(E) == 3:
            return 2.0
        if len(E) == 2:
            return 1.0
        return 0.0
    raise ValueError


def components(tor, B):
    B = list(B)
    seen, comps = set(), []
    for b in B:
        if b in seen:
            continue
        stack, comp = [b], set([b])
        seen.add(b)
        while stack:
            u = stack.pop()
            for v in B:
                if v not in seen and tor.star_adj(u, v):
                    seen.add(v)
                    comp.add(v)
                    stack.append(v)
        comps.append(frozenset(comp))
    return comps


def connected_sets_upto(tor, sites, nmax):
    level = {frozenset([s]) for s in sites}
    allsets = set(level)
    for _ in range(nmax - 1):
        new = set()
        for Y in level:
            for y in Y:
                for o in tor.offs:
                    z = tor.add(y, o)
                    if z not in Y:
                        new.add(Y | {z})
        level = new
        allsets |= new
    return allsets


def rotate_field(tor, D, R, x):
    """(R.D)(z) = D(x + R^{-1}(z - x)); R = (perm, signs): (Rv)_i = s_i v_{perm[i]}."""
    perm, signs = R
    d, T = tor.d, tor.T
    inv = {}
    out = {}
    for z in D:
        v = [((z[i] - x[i] + T // 2) % T) - T // 2 for i in range(d)]
        # R^{-1} v: R v = w with w_i = s_i v_{perm[i]}  =>  v_{perm[i]} = s_i w_i
        u = [0] * d
        for i in range(d):
            u[perm[i]] = signs[i] * v[i]
        src = tuple((x[i] + u[i]) % T for i in range(d))
        out[z] = D[src]
    return out


def group(d):
    G = []
    for perm in itertools.permutations(range(d)):
        for signs in itertools.product((1, -1), repeat=d):
            G.append((perm, signs))
    return G


def tuple_terms(tor, tuples, D):
    cache = {}
    out = []
    for tup, ph, N, S, X in tuples:
        for Y in tup:
            if Y not in cache:
                cache[Y] = activity(tor, Y, D)
        out.append(ph * math.prod(cache[Y] for Y in tup) / math.factorial(len(tup)))
    return out


def localised(tor, tuples, D, x, Nmax):
    terms = tuple_terms(tor, tuples, D)
    Ft = np.zeros(Nmax + 1)
    Ff = np.zeros(Nmax + 1)
    for (tup, ph, N, S, X), term in zip(tuples, terms):
        if x in S:
            Ft[N] += term / len(S)
        if x in X:
            Ff[N] += term / len(X)
    return Ft, Ff


def localised_all(tuples, terms, Nmax):
    Ft, Ff = {}, {}
    for (tup, ph, N, S, X), term in zip(tuples, terms):
        for y in S:
            Ft.setdefault(y, np.zeros(Nmax + 1))[N] += term / len(S)
        for y in X:
            Ff.setdefault(y, np.zeros(Nmax + 1))[N] += term / len(X)
    return Ft, Ff


def build_tuples(tor, sets, Nmax, filt=None):
    """All tuples with N <= Nmax (n <= 3), with nonzero phi^T; filt(S, X) -> keep."""
    by_size = {}
    for Y in sets:
        by_size.setdefault(len(Y), []).append(Y)
    out = []

    def push(tup):
        ph = phiT(tor, tup)
        if ph == 0.0:
            return
        S = frozenset().union(*tup)
        X = frozenset().union(*[tor.fatten(Y) for Y in tup])
        if filt is None or filt(S, X):
            out.append((tup, ph, sum(len(Y) for Y in tup), S, X))

    for Y in sets:
        if len(Y) <= Nmax:
            push((Y,))
    # n = 2
    for s1 in range(1, Nmax):
        for s2 in range(1, Nmax - s1 + 1):
            for Y1 in by_size.get(s1, []):
                for Y2 in by_size.get(s2, []):
                    if tor.touch(Y1, Y2):
                        push((Y1, Y2))
    # n = 3 (singletons only, N = 3)
    if Nmax >= 3:
        singles = by_size[1]
        for a in singles:
            for b in singles:
                for c in singles:
                    tup = (a, b, c)
                    ph = phiT(tor, tup)
                    if ph != 0.0:
                        push(tup)
    return out


def brute_coeffs(tor, sites, D, Nmax):
    a = [1.0] + [0.0] * Nmax
    for m in range(1, Nmax + 1):
        tot = 0.0
        for B in itertools.combinations(sites, m):
            tot += math.prod(activity(tor, Y, D) for Y in components(tor, B))
        a[m] = tot
    # log of 1 + a1 t + a2 t^2 + a3 t^3
    c = [0.0] * (Nmax + 1)
    c[1] = a[1]
    if Nmax >= 2:
        c[2] = a[2] - a[1] ** 2 / 2
    if Nmax >= 3:
        c[3] = a[3] - a[1] * a[2] + a[1] ** 3 / 3
    return c


def part_A():
    tor = Torus(2, 9)
    sites = list(itertools.product(range(9), repeat=2))
    sets = connected_sets_upto(tor, sites, 3)
    tuples = build_tuples(tor, sets, 3)
    x = (4, 4)
    G = group(2)
    print(f"A: d=2 T=9; connected sets {len(sets)}; tuples (phi^T != 0) {len(tuples)}")
    ok = {k: True for k in ["A1", "A2", "A3", "A4", "A5"]}
    for seed in [0, 1, 2, 3, 4, "const"]:
        if seed == "const":
            D = {s: 0.2 for s in sites}
        else:
            rng = np.random.default_rng(seed)
            D = {s: 0.3 * rng.standard_normal() for s in sites}
        c = brute_coeffs(tor, sites, D, 3)
        # A1
        terms = tuple_terms(tor, tuples, D)
        tot = np.zeros(4)
        for (tup, ph, N, S, X), term in zip(tuples, terms):
            tot[N] += term
        e1 = max(abs(tot[N] - c[N]) / max(1, abs(c[N])) for N in (1, 2, 3))
        ok["A1"] &= e1 <= 1e-10
        # A4: explicit per-x localised values summed over all x
        Fta, Ffa = localised_all(tuples, terms, 3)
        Ftx = sum(Fta.values()); Ffx = sum(Ffa.values())
        e4 = max(max(abs(Ftx[N] - Ffx[N]), abs(Ftx[N] - c[N])) / max(1, abs(c[N])) for N in (1, 2, 3))
        ok["A4"] &= e4 <= 1e-10
        Ft0, Ff0 = localised(tor, tuples, D, x, 3)
        e2 = 0.0; e3 = 0.0
        for R in G:
            DR = rotate_field(tor, D, R, x)
            Ft, Ff = localised(tor, tuples, DR, x, 3)
            for N in (1, 2, 3):
                e2 = max(e2, abs(Ft[N] - Ft0[N]) / max(1, abs(Ft0[N])))
                e3 = max(e3, abs(Ff[N] - Ff0[N]) / max(1, abs(Ff0[N])))
        ok["A2"] &= e2 <= 1e-12
        if seed != "const":
            ok["A3"] &= e3 > 1e-6
        else:
            e5 = max(abs(Ft0[N] - Ff0[N]) / max(1, abs(Ft0[N])) for N in (1, 2, 3))
            e5b = max(abs(Ft0[N] - c[N] / 81) / max(1, abs(Ft0[N])) for N in (1, 2, 3))
            ok["A5"] &= (e5 <= 1e-12) and (e5b <= 1e-12)
            print(f"  const: |F^tup - F^fat| rel {e5:.2e}; |F^tup - c_N/T^2| rel {e5b:.2e}")
        print(f"  seed {seed}: A1 err {e1:.2e}; A4 err {e4:.2e}; A2 max rel change {e2:.2e}; "
              f"fattened max rel change {e3:.2e}; c = {[f'{v:.6f}' for v in c[1:]]}")
    for k, v in ok.items():
        print(f"{k}: {'PASS' if v else 'FAIL'}")
    print("Part A:", "PASS" if all(ok.values()) else "FAIL")


def part_B():
    d, T = 4, 7
    tor = Torus(d, T)
    sites = list(itertools.product(range(T), repeat=d))
    x = (3, 3, 3, 3)
    # sets near x: singletons and *-adjacent pairs within sup-distance 2 of x
    near = [s for s in sites if all(((a - b) % T) in (0, 1, 2, T - 1, T - 2) for a, b in zip(s, x))]
    sets = set(frozenset([s]) for s in near)
    for s in near:
        for o in tor.offs:
            z = tor.add(s, o)
            sets.add(frozenset([s, z]))
    filt = lambda S, X: (x in S) or (x in X)
    tuples = build_tuples(tor, sets, 2, filt)
    G = group(d)
    print(f"B: d=4 T=7; candidate sets {len(sets)}; tuples kept {len(tuples)}; group order {len(G)}")
    ok = {k: True for k in ["B1", "B2", "B3", "B4"]}
    Y = frozenset([tor.add(x, (-1, 0, 0, 0))]); Yp = frozenset([tor.add(x, (1, 0, 0, 0))])
    ok["B3"] = (x in tor.fatten(Y)) and (x not in tor.fatten(Yp))
    print(f"  B3: x in fat({{x-e1}}) = {x in tor.fatten(Y)}; x in fat({{x+e1}}) = {x in tor.fatten(Yp)}")
    for seed in [0, 1, 2, "const"]:
        if seed == "const":
            D = {s: 0.2 for s in sites}
        else:
            rng = np.random.default_rng(seed)
            D = {s: 0.3 * rng.standard_normal() for s in sites}
        Ft0, Ff0 = localised(tor, tuples, D, x, 2)
        if seed == "const":
            e4 = max(abs(Ft0[N] - Ff0[N]) / max(1, abs(Ft0[N])) for N in (1, 2))
            ok["B4"] &= e4 <= 1e-12
            print(f"  const: |F^tup - F^fat| rel {e4:.2e}; F^tup = {Ft0[1:]}")
            continue
        e1 = 0.0; e2 = 0.0
        for R in G:
            DR = rotate_field(tor, D, R, x)
            Ft, Ff = localised(tor, tuples, DR, x, 2)
            for N in (1, 2):
                e1 = max(e1, abs(Ft[N] - Ft0[N]) / max(1, abs(Ft0[N])))
                e2 = max(e2, abs(Ff[N] - Ff0[N]) / max(1, abs(Ff0[N])))
        ok["B1"] &= e1 <= 1e-12
        ok["B2"] &= e2 > 1e-6
        print(f"  seed {seed}: tuple max rel change {e1:.2e}; fattened max rel change {e2:.2e}")
    for k, v in ok.items():
        print(f"{k}: {'PASS' if v else 'FAIL'}")
    print("Part B:", "PASS" if all(ok.values()) else "FAIL")


if __name__ == "__main__":
    {"A": part_A, "B": part_B}[sys.argv[1]]()
