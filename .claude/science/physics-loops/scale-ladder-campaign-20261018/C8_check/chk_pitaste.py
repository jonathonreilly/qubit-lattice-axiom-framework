"""C8 check (c) supplement: which E-words keep a spectral Pi taste?  Own code (mymodel)."""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chk_class23.py')).read()
exec(src[:src.index("# ================= (b) class 2")])
rng = np.random.default_rng(8803)
def reduce_E(w):
    """count E letters after cancelling adjacent E+E- / merging E E -> R-type (cyclic not applied)"""
    return sum(1 for t in w if isinstance(t, str) and t[0] == 'E')
def hygienic(w):
    n = len(w)
    for i in range(n):
        a, b = w[i], w[(i + 1) % n]
        if isinstance(a, str) and isinstance(b, str) and ((a[0] == 'E' and (b[0] == 'E' or b == 'R')) or (b[0] == 'E' and a == 'R')): return False
        if not isinstance(a, str) and not isinstance(b, str): return False
    return True
cnt = collections.Counter(); exs = collections.defaultdict(list)
tries = 0
while sum(cnt.values()) < 300 and tries < 20000:
    tries += 1
    n = int(rng.integers(3, 7)); toks = [str(rng.choice(['S', 'Si', 'S2', 'R', 'Rt', 'E+', 'E-', 'o'])) for _ in range(n)]
    if not any(t[0] == 'E' for t in toks) or nS(toks) == 0: continue
    w = [rand_onsite_unitary(rng) if t == 'o' else t for t in toks]
    if not hygienic(w): continue
    ks = rng.uniform(-np.pi, np.pi, (3, 3))
    kp = all(specdist(W(w, k + PI), W(w, k)) < 1e-7 for k in ks); km = all(specdist(W(w, k + PI), -W(w, k)) < 1e-7 for k in ks)
    nEp = toks.count('E+'); nEm = toks.count('E-')
    key = ('keep' if (kp or km) else 'broken', 'E+/E- balanced' if nEp == nEm else 'unbalanced', 'with on-site slot' if 'o' in toks else 'no slot')
    cnt[key] += 1
    if len(exs[key]) < 3: exs[key].append(tuple(toks))
print("hygienic E-words with random symmetric on-site unitaries (n_S != 0):", dict(cnt))
for k_, v in exs.items(): print("  ", k_, v)
# exact mechanism for balanced words: W(k+Pi) = (-1)^{n_R} W'(k), W' = E+<->E-.  E.g. E+ X E- Y : is spec(E- X E+ Y) = spec(E+ X E- Y)?
