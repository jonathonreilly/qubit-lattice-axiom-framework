"""Translation-invariant vertex orderings only (same local order of the 6 incident edge *directions* at every site):
is there one with the all-bare-+1 assignment consistent?  Exhaustive-ish random search + local search."""
import sys, random, math, itertools
Lr = sys.argv[1] if len(sys.argv) > 1 else '4'
sys.argv = [sys.argv[0], Lr, '0']
exec(open('rev_A2.py').read().split("nconv = int")[0])
random.seed(5)
# local edge "slot" key at a vertex: (pair, other endpoint pair, displacement) -- translation invariant
def slot(v, k):
    u, w, _ = elist[k]; o = w if u == v else u
    sv, pv = V[v]; so, po = V[o]
    d = tuple(((so[i] - sv[i] + 1) % L) - 1 for i in range(3))
    return (tuple(sorted(pv)), tuple(sorted(po)), d)
types = sorted({tuple(sorted(p)) for p in pairs})
slots_of = {}
for v in range(nV):
    t = tuple(sorted(V[v][1]))
    slots_of.setdefault(t, sorted(slot(v, k) for k in inc[v]))
def make_order(perm):  # perm[t] = list of slots in order
    order = []
    for v in range(nV):
        t = tuple(sorted(V[v][1])); m = {slot(v, k): k for k in inc[v]}
        order.append([m[s] for s in perm[t]])
    return order
def nviol(perm):
    S = build(make_order(perm)); kap, bare = loopdata(S, list(range(nV)))
    return sum(1 for s in sigmas(bare) if s == -1), kap
found = None
perm = {t: random.sample(slots_of[t], 6) for t in types}
cur, _ = nviol(perm); best = cur; T = 2.0
for step in range(1500):
    t = random.choice(types); a, b = random.sample(range(6), 2)
    perm[t][a], perm[t][b] = perm[t][b], perm[t][a]
    nv, _ = nviol(perm)
    if nv <= cur or random.random() < math.exp(-(nv - cur) / T):
        cur = nv
    else:
        perm[t][a], perm[t][b] = perm[t][b], perm[t][a]
    T = max(0.05, T * 0.997); best = min(best, cur)
    if cur == 0: found = {k: list(v) for k, v in perm.items()}; break
print(f"L={L} TI-ordering search: steps {step+1}, final {cur}, best {best}")
if found:
    nv, kap = nviol(found)
    S = build(make_order(found)); kap, bare = loopdata(S, list(range(nV)))
    print("  TI ordering with consistent bare assignment found; -I in bare group:", contains_minus_I(bare))
    import pickle; pickle.dump(found, open(f'TI_ordering_L{L}.pkl', 'wb'))
