"""Does some BKSF vertex ordering make the all-bare-loop +1 assignment consistent (kappa consistent)?
Local search over orderings, using kappa only (labels and hop signs do not change sigma on relations)."""
import sys, random, math
sys.argv = [sys.argv[0], sys.argv[1] if len(sys.argv) > 1 else '3', '0']
exec(open('rev_A2.py').read().split("nconv = int")[0])
random.seed(11)
face_of_edge = [[] for _ in range(nE)]
for i, fe in enumerate(fedges):
    for e in fe: face_of_edge[e].append(i)
rel_of_face = [[] for _ in range(nF)]
for ri, r in enumerate(rels):
    for i in range(nF):
        if (r >> i) & 1: rel_of_face[i].append(ri)
def kappa_face(i, S, label):
    (t, c), fe = faces[i], fedges[i]
    A = (0, 0, 0); eps = 1
    for k, e in enumerate(fe):
        A = pmul(A, S[e]); a, b = c[k], c[(k+1) % len(c)]
        eps *= 1 if label[a] < label[b] else -1
    ph = (len(fe) + std(A)) % 4
    return eps * (1 if ph == 0 else -1)
def Sedge(k, order, rk):
    u, w, _ = elist[k]; z = 0
    for v in (u, w):
        for l in order[v]:
            if rk[v][l] < rk[v][k]: z ^= 1 << l
    return (0, 1 << k, z)
best_overall = None
for trial in range(int(sys.argv[2]) if False else 4):
    order = [random.sample(inc[v], 6) for v in range(nV)]
    label = list(range(nV))
    rk = [{e: r for r, e in enumerate(order[v])} for v in range(nV)]
    S = [Sedge(k, order, rk) for k in range(nE)]
    kap = [kappa_face(i, S, label) for i in range(nF)]
    viol = [math.prod(kap[i] for i in range(nF) if (r >> i) & 1) == -1 for r in rels]
    nv = sum(viol); T = 1.0; best = nv
    for step in range(40000):
        v = random.randrange(nV); a, b = random.sample(range(6), 2)
        e, f = order[v][a], order[v][b]
        order[v][a], order[v][b] = f, e
        rk[v] = {x: r for r, x in enumerate(order[v])}
        touched_e = set(order[v])  # Z strings of edges at v may change
        newS = {k: Sedge(k, order, rk) for k in touched_e}
        oldS = {k: S[k] for k in touched_e}
        for k in touched_e: S[k] = newS[k]
        tf = set(i for k in touched_e for i in face_of_edge[k])
        changed = [i for i in tf if kappa_face(i, S, label) != kap[i]]
        flip = {}
        for i in changed:
            for ri in rel_of_face[i]: flip[ri] = flip.get(ri, 0) ^ 1
        dv = sum((1 - 2 * viol[ri]) for ri, x in flip.items() if x)
        if dv <= 0 or random.random() < math.exp(-dv / T):
            for i in changed: kap[i] = -kap[i]
            for ri, x in flip.items():
                if x: viol[ri] = not viol[ri]
            nv += dv
        else:
            order[v][a], order[v][b] = e, f
            rk[v] = {x: r for r, x in enumerate(order[v])}
            for k in touched_e: S[k] = oldS[k]
        T = max(0.05, T * 0.9998)
        best = min(best, nv)
        if nv == 0: break
    # recheck from scratch
    S2 = [Sedge(k, order, rk) for k in range(nE)]
    kap2, bare2 = loopdata(S2, label)
    sig2 = sigmas(bare2)
    nb = sum(1 for s in sig2 if s == -1)
    print(f"trial {trial}: final violated basis relations {nv} (recomputed from scratch: {nb}); best seen {best}; steps {step+1}")
    if nb == 0:
        print("  FOUND an ordering with the all-bare-+1 assignment consistent; contains -I:", contains_minus_I(bare2))
        import pickle; pickle.dump(order, open(f'ordering_bare_consistent_L{L}.pkl', 'wb'))
        break
