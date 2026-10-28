"""w4b (redesigned sampler, see w4b_criteria.md): influence-column geometry of HW.md session 4 (Lemma FP / LI^U-0). Informational; criteria in w4_criteria.md.

Pure combinatorics on multi-level tori (side ratio L = 3). A level-m cube is a level-(m+1) site.
"""
import itertools
import random
import sys

L = 3


def unit(d, mu, s=1):
    return tuple(s if i == mu else 0 for i in range(d))


def add(x, y, n):
    return tuple((a + b) % n for a, b in zip(x, y))


def down(x):  # level-m site (or cube) -> level-(m+1) site (or cube)
    return tuple(a // L for a in x)


class Tower:
    def __init__(self, d, K, top):
        self.d, self.K = d, K
        # n[m] = side of the level-m site torus; level-m cubes live on the level-(m+1) torus
        self.n = {m: top * L ** (K - m) for m in range(K + 1)}

    def cubes(self, m):  # level-m cubes = level-(m+1) sites, m <= K-1
        return list(itertools.product(range(self.n[m + 1]), repeat=self.d))

    def N1(self, B, m):  # neighbourhood (sup distance <= 1) of a set of level-m cubes
        n = self.n[m + 1]
        out = set()
        for z in B:
            for off in itertools.product((-1, 0, 1), repeat=self.d):
                out.add(add(z, off, n))
        return out

    def proj(self, B):
        return {down(z) for z in B}

    def Sigma(self, B, m):  # level-m set -> level-(m+1) set
        return self.N1(self.proj(B), m + 1)


def random_history(T, rng, density):
    U, Om, A, S = {}, {}, {}, {}
    prev = set()
    for m in range(T.K):
        sig = T.Sigma(prev, m - 1) if m > 0 else set()
        U[m] = set()
        tries = 0
        while len(U[m]) < density and tries < 2000:  # density := n_U cubes per level (w4b); capped tries
            tries += 1
            z = tuple(rng.randrange(T.n[m + 1]) for _ in range(T.d))
            if z not in sig:
                U[m].add(z)
        Om[m] = sig | U[m]
        A[m] = sig | T.N1(U[m], m)
        S[m] = None  # S^(m) = complement of A[m]; tested as 'not in A[m]'
        prev = Om[m]
    return U, Om, A, S


def link_ends(T, ell, m):
    x, nu = ell
    return x, add(x, unit(T.d, nu), T.n[m])


def sdist(u, v, n):  # sup distance on the torus of side n
    return max(min((p - q) % n, (q - p) % n) for p, q in zip(u, v))


def readers(T, ell, m, widen):
    """level-(m+1) links c = (X, mu) that read the level-m link ell."""
    x, y = link_ends(T, ell, m)
    a, b = down(x), down(y)
    n1 = T.n[m + 1]
    out = []
    # candidate X near a
    for off in itertools.product((-2, -1, 0, 1), repeat=T.d):
        X = add(a, off, n1)
        for mu in range(T.d):
            Y = add(X, unit(T.d, mu), n1)
            if widen:
                ok = (min(sdist(a, X, n1), sdist(a, Y, n1)) <= 1) and (min(sdist(b, X, n1), sdist(b, Y, n1)) <= 1)
            else:
                ok = a in (X, Y) and b in (X, Y)
            if ok:
                out.append((X, mu))
    return set(out)


def footprint(T, A0, k, widen):
    F = {k: set(A0)}
    for m in range(k, T.K):
        nxt = set()
        for ell in F[m]:
            nxt |= readers(T, ell, m, widen)
        F[m + 1] = nxt
    return F


def reads(T, F, m, A, U):
    cons, spec, interior = 0, 0, set()
    for ell in F[m]:
        x, y = link_ends(T, ell, m)
        z1, z2 = down(x), down(y)
        if z1 == z2:
            interior.add(z1)
            if z1 not in A[m]:
                cons += 1
        if m + 1 <= T.K - 1 and down(z1) == down(z2) and down(z1) in U.get(m + 1, set()):
            spec += 1
    return cons, spec, interior


def piiter(B, r):
    for _ in range(r):
        B = {down(z) for z in B}
    return B


def run(d, K, top, seed, nhist, nlinks, density):
    rng = random.Random(seed)
    T = Tower(d, K, top)
    res = dict(A_exc=0, A_tested=0, B_exc=0, B_tested=0, C_exc=0, C_tested=0, D_fail=0, D_tested=0)
    for h in range(nhist):
        U, Om, A, S = random_history(T, rng, density)
        for k in range(0, K - 1):
            n = T.n[k]
            # sample links
            relcubes = [z for z in A[k + 1]]  # level-(k+1) cubes in the relaxed set
            for t in range(nlinks):
                if t % 2 == 0:
                    Z = rng.choice(relcubes)  # a level-(k+1) cube; pick a level-k link inside its blocks
                    x = tuple(L * L * Z[i] + rng.randrange(L * L) for i in range(d))
                    x = tuple(a % n for a in x)
                else:
                    x = tuple(rng.randrange(n) for _ in range(d))
                nu = rng.randrange(d)
                ell = (x, nu)
                xs, ys = link_ends(T, ell, k)
                x1, x2 = down(xs), down(ys)  # level-k cubes
                F = footprint(T, [ell], k, widen=False)
                # A: containment
                res['A_tested'] += 1
                for m in range(k + 1, K):
                    _, _, inter = reads(T, F, m, A, U)
                    if not inter <= piiter({x1, x2}, m - k):
                        res['A_exc'] += 1
                    sites = piiter({x1, x2}, m - k - 1)
                    for c in F[m]:
                        e1, e2 = link_ends(T, c, m)
                        if e1 not in sites and e2 not in sites:
                            res['A_exc'] += 1
                p1, p2 = down(x1), down(x2)
                # B: relaxed column
                if p1 in A[k + 1] and p2 in A[k + 1]:
                    res['B_tested'] += 1
                    bad = False
                    for m in range(k + 1, K):
                        cons, spec, _ = reads(T, F, m, A, U)
                        if cons or spec:
                            bad = True
                    if bad:
                        res['B_exc'] += 1
                    # D: widened kernel must break B somewhere
                    if res['D_tested'] < 40:
                        res['D_tested'] += 1
                        Fw = {k: {ell}}
                        for m in range(k, K - 1):
                            nxt = set()
                            for c0 in Fw[m]:
                                nxt |= readers(T, c0, m, True)
                            Fw[m + 1] = nxt
                            cons, spec, _ = reads(T, Fw, m + 1, A, U)
                            if cons or spec:
                                res['D_fail'] += 1
                                break
                # C: constrained column control (interior link of one cube)
                if x1 == x2 and p1 not in A[k + 1]:
                    res['C_tested'] += 1
                    cons, _, _ = reads(T, F, k + 1, A, U)
                    if cons == 0:
                        res['C_exc'] += 1
    return res


def main():
    out = []
    ok = True
    for (d, K, top, seed, nhist, nlinks, density) in [(2, 5, 4, 11, 6, 60, 2), (4, 3, 3, 13, 3, 30, 2)]:
        import time
        t0 = time.time()
        r = run(d, K, top, seed, nhist, nlinks, density)
        r['secs'] = round(time.time() - t0, 1)
        A = r['A_exc'] == 0 and r['A_tested'] > 0
        B = r['B_exc'] == 0 and r['B_tested'] >= 10
        C = r['C_exc'] == 0 and r['C_tested'] >= 10
        D = r['D_fail'] > 0 and r['D_tested'] >= 10
        ok = ok and A and B and C and D
        out.append(f"d={d} K={K} top={top}: {r}")
        out.append(f"  A {'PASS' if A else 'FAIL'}  B {'PASS' if B else 'FAIL'}  C {'PASS' if C else 'FAIL'}  "
                   f"D(neg. control breaks B) {'PASS' if D else 'FAIL'}")
    out.append("OVERALL " + ("PASS" if ok else "FAIL"))
    print("\n".join(out))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
