"""h3: Lemma H-geo (i)-(iv) and Lemma H-nest (iii) of HIST.md §7. Criteria: checks/h3_criteria.md (written first)."""
import itertools, resource, time
import numpy as np

T0 = time.time()
NB = [d for d in itertools.product((-1, 0, 1), repeat=4) if any(d)]


def proj(A, L):
    return {tuple(c // L for c in z) for z in A}


def nbhd(A, r):
    offs = list(itertools.product(range(-r, r + 1), repeat=4))
    return {tuple(z[k] + o[k] for k in range(4)) for z in A for o in offs}


def Sig(A, L):
    return nbhd(proj(A, L), 1)


def grow(rng, n, start):
    D = {start}
    lst = [start]
    while len(D) < n:
        z = lst[rng.integers(len(lst))]
        d = NB[rng.integers(len(NB))]
        y = tuple(z[k] + d[k] for k in range(4))
        if y not in D:
            D.add(y)
            lst.append(y)
    return D


def line(n, steps, start):
    z = list(start)
    D = {tuple(z)}
    i = 0
    while len(D) < n:
        s = steps[i % len(steps)]
        z = [z[k] + s[k] for k in range(4)]
        D.add(tuple(z))
        i += 1
    return D


ok = dict(G1=True, G2=True, G3=True, G4=True, N1=True)
mx2 = mx3 = 0.0
pers = {}
for L in (3, 5):
    rng = np.random.default_rng(7 + L)
    sets = []
    for n in (1, 2, 5, 10, 30, 100, 300):
        for t in range(60 // 7 + 1):
            sets.append(grow(rng, n, tuple(int(v) for v in rng.integers(-50, 50, 4))))
    for n in (10, 50, 200):
        for off in (0, L ** 3 - 1):
            st = (off,) * 4
            sets.append(line(n, [(1, 0, 0, 0)], st))
            sets.append(line(n, [(1, 1, 1, 1)], st))
            sets.append(line(n, [(1, 1, 0, 0)], st))
            sets.append(line(n, [(1, 0, 0, 0), (1, 1, 1, 1)], st))
    for D in sets:
        n = len(D)
        sh = set(D)
        pm = set(D)
        tot = n
        if not tot <= 38417 * n:
            ok['G4'] = False
        for m in range(1, 7):
            sh = Sig(sh, L)
            pm = proj(pm, L)
            if not sh <= nbhd(pm, 3):
                ok['G1'] = False
            b2 = min(n, 16 + 32 * (n - 1) * L ** (-m))
            mx2 = max(mx2, len(pm) / (16 + 32 * (n - 1) * L ** (-m)))
            if len(pm) > b2 + 1e-9:
                ok['G2'] = False
            b3 = 2401 * (16 + 32 * (n - 1) * L ** (-m))
            mx3 = max(mx3, len(sh) / b3)
            if len(sh) > b3:
                ok['G3'] = False
            tot += len(sh)
            if tot > 38417 * n + 38416 * m:
                ok['G4'] = False
            if n == 1:
                pers[(L, m)] = max(pers.get((L, m), 0), len(sh))
    print(f"L={L}: {len(sets)} sets checked")

# N1: columns property of random histories (L = 3, levels 0..4)
L = 3
rng = np.random.default_rng(11)
for h in range(20):
    Om = []  # Om[k] = Omega^c_k
    prev = set()
    for k in range(5):
        base = Sig(prev, L) if k > 0 else set()
        new = set()
        for _ in range(rng.integers(0, 4)):
            cand = grow(rng, int(rng.integers(1, 40)), tuple(int(v) for v in rng.integers(-60 // (L ** k) - 3, 60 // (L ** k) + 3, 4)))
            if not (cand & base):
                new |= cand
        cur = base | new
        Om.append(cur)
        prev = cur
    window = [tuple(int(v) for v in rng.integers(-70, 70, 4)) for _ in range(3000)]
    for D in Om[0]:
        window.append(D)
    for x in window:
        flags = []
        z = x
        for m in range(5):
            flags.append(z not in Om[m])
            z = tuple(c // L for c in z)
        # initial interval: once False, stays False
        seen_false = False
        for fl in flags:
            if not fl:
                seen_false = True
            elif seen_false:
                ok['N1'] = False

print(f"G2 max ratio |pi^m|/(16+32(n-1)L^-m) = {mx2:.4f}; G3 max ratio = {mx3:.4f}")
print(f"persistent size |sh_m| for n = 1: {pers}")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
print({k: ('PASS' if v else 'FAIL') for k, v in ok.items()})
print(f"h3: {'PASS' if all(ok.values()) else 'FAIL'}  t {time.time() - T0:.1f}s  peak RSS {rss:.0f} MB")
