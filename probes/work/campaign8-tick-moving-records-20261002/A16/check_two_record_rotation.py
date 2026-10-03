"""A16 hostile check of A13 (option-A records on A10's plain round): are the READABLE two-record statistics covariant
under a 90-degree turn, allowing any cyclic restart of the round or its reversal?  Exact enumeration, 6^3 torus.
Per layer, each pair with exactly one record moves it to the partner w.p. s = sin^2(theta); two records: nothing."""
import itertools, numpy as np
L = 6; s = np.sin(0.6) ** 2
word = [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]
def partner(x, a, p):
    y = list(x)
    if x[a] % 2 == p: y[a] = (y[a] + 1) % L
    else:             y[a] = (y[a] - 1) % L
    return tuple(y)
def step(dist, a, p):
    out = {}
    for conf, pr in dist.items():
        r1, r2 = conf
        q1, q2 = partner(r1, a, p), partner(r2, a, p)
        if q1 == r2:                      # same pair: nothing happens
            opts = [((r1, r2), 1.0)]
        else:
            o1 = [(r1, 1 - s), (q1, s)]; o2 = [(r2, 1 - s), (q2, s)]
            opts = [((a1, a2), w1 * w2) for a1, w1 in o1 for a2, w2 in o2]
        for c, w in opts:
            key = tuple(sorted(c)); out[key] = out.get(key, 0) + pr * w
    return out
def run(c0, wd):
    d = {tuple(sorted(c0)): 1.0}
    for a, p in wd: d = step(d, a, p)
    return d
def R(x):            # cube-centred C4z: (x,y,z) -> (1-y, x, z)
    return ((1 - x[1]) % L, x[0] % L, x[2])
def tv(d1, d2):
    ks = set(d1) | set(d2); return 0.5 * sum(abs(d1.get(k, 0) - d2.get(k, 0)) for k in ks)
words = {f"restart {k}": word[k:] + word[:k] for k in range(6)}
words.update({f"reversed restart {k}": (word[::-1])[k:] + (word[::-1])[:k] for k in range(6)})
rng = np.random.default_rng(1); worst_best = 0.0
for trial in range(30):
    while True:
        c0 = [tuple(int(v) for v in rng.integers(0, L, 3)) for _ in range(2)]
        if c0[0] != c0[1] and max(abs((c0[0][i]-c0[1][i]+L//2) % L - L//2) for i in range(3)) <= 2: break
    rot_then_run = run([R(c) for c in c0], word)                      # law applied to the turned start
    best = min(tv(rot_then_run, {tuple(sorted((R(a), R(b)))): w for (a, b), w in run(c0, wd).items()})
               for wd in words.values())
    worst_best = max(worst_best, best)
print(f"max over 30 two-record starts of [min over 12 restarts/reversals of TV(turned law, law)] = {worst_best:.4f}")
c0 = [(0,0,0),(1,1,0)]
print("single-record control:", min(tv(run([R((0,0,0)), R((3,3,3))], word),
      {tuple(sorted((R(a), R(b)))): w for (a, b), w in run([(0,0,0),(3,3,3)], wd).items()}) for wd in words.values()))

# Extension: also allow conjugation by every translation t in {0,1}^3 (A10 S7 realizes C4 as T_111 U^T T_111^-1).
def shift(x, t): return tuple((x[i] + t[i]) % L for i in range(3))
trans = list(itertools.product((0, 1), repeat=3))
rng = np.random.default_rng(1); worst_best = 0.0; best_labels = []
for trial in range(30):
    while True:
        c0 = [tuple(int(v) for v in rng.integers(0, L, 3)) for _ in range(2)]
        if c0[0] != c0[1] and max(abs((c0[0][i]-c0[1][i]+L//2) % L - L//2) for i in range(3)) <= 2: break
    target = run([R(c) for c in c0], word)
    best, lab = 9.0, None
    for wname, wd in words.items():
        for t in trans:
            neg = tuple(-v for v in t)
            d = run([shift(c, t) for c in c0], wd)                     # candidate law from translated start
            cand = {tuple(sorted((R(shift(a, neg)), R(shift(b, neg))))): w for (a, b), w in d.items()}
            v = tv(target, cand)
            if v < best: best, lab = v, (wname, t)
    worst_best = max(worst_best, best); best_labels.append(lab)
print(f"with translations too: max over 30 starts of best TV = {worst_best:.4f}; e.g. best candidates {best_labels[:3]}")

# Forward-only (no reversal) restarts, with all 8 translations: is the quarter turn realized WITHOUT time reversal?
rng = np.random.default_rng(1); worst_fwd = 0.0
fwd = {k: v for k, v in words.items() if not k.startswith("reversed")}
for trial in range(30):
    while True:
        c0 = [tuple(int(v) for v in rng.integers(0, L, 3)) for _ in range(2)]
        if c0[0] != c0[1] and max(abs((c0[0][i]-c0[1][i]+L//2) % L - L//2) for i in range(3)) <= 2: break
    target = run([R(c) for c in c0], word)
    best = min(tv(target, {tuple(sorted((R(shift(a, tuple(-v for v in t))), R(shift(b, tuple(-v for v in t)))))): w
                           for (a, b), w in run([shift(c, t) for c in c0], wd).items()})
               for wd in fwd.values() for t in trans)
    worst_fwd = max(worst_fwd, best)
print(f"forward restarts x 8 translations only: max over 30 starts of best TV = {worst_fwd:.4f}")
