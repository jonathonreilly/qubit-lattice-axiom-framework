"""A16: two option-A records on A10's plain round (6^3 torus, exact enumeration).  For each parity translation t in {0,1}^3,
is 'law applied to the t-shifted start' equal to (shifted back) some forward restart or reversed restart of the round?"""
import itertools, numpy as np
exec(open("check_two_record_rotation.py").read().split("rng = np.random.default_rng(1); worst_best")[0])
def shift(x, t): return tuple((x[i] + t[i]) % L for i in range(3))
rng = np.random.default_rng(7); starts = []
while len(starts) < 30:
    c0 = [tuple(int(v) for v in rng.integers(0, L, 3)) for _ in range(2)]
    if c0[0] != c0[1] and max(abs((c0[0][i]-c0[1][i]+L//2) % L - L//2) for i in range(3)) <= 2: starts.append(c0)
for t in itertools.product((0, 1), repeat=3):
    neg = tuple(-v for v in t); worst = {"fwd": 0.0, "rev": 0.0}
    for c0 in starts:
        tgt = {tuple(sorted((shift(a, neg), shift(b, neg)))): w for (a, b), w in run([shift(c, t) for c in c0], word).items()}
        for kind in ("fwd", "rev"):
            best = min(tv(tgt, run(c0, wd)) for k, wd in words.items() if k.startswith("reversed") == (kind == "rev"))
            worst[kind] = max(worst[kind], best)
    print(f"translation {t}: worst best-TV forward {worst['fwd']:.4f}   reversed {worst['rev']:.4f}")
