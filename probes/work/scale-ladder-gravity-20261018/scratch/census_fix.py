import sys, itertools, time, pickle, numpy as np
sys.path.insert(0, '.')
import canon_tri as CT, regge_generic as RG
B4 = []
for p in itertools.permutations(range(4)):
    for s in itertools.product([1, -1], repeat=4):
        M = np.zeros((4, 4))
        for i in range(4): M[p[i], i] = s[i]
        B4.append(M)
def sym_ok(C):
    def canon(P):
        P2 = np.array(sorted(tuple(np.round(840*p).astype(int)) for p in P)); sh = np.floor_divide(P2.min(axis=0), 840)*840
        return tuple(map(tuple, P2 - sh))
    base = {canon([C.pos(v) for v in s]) for s in C.simp}
    return all(canon([g @ C.pos(v) for v in s]) in base for g in B4[::7] for s in C.simp)
def ortho(C, s):
    P = np.array([C.pos(v) for v in s])
    for perm in itertools.permutations(range(5)):
        st = [P[perm[i+1]] - P[perm[i]] for i in range(4)]
        if all(abs(st[i] @ st[j]) < 1e-9 for i in range(4) for j in range(i+1, 4)): return True
    return False
results = {}
for r in range(1, 3):
    for which in [w for w in itertools.combinations([1, 2, 3, 4], r) if w in [(2,), (1, 2)]]:
        t0 = time.time()
        try:
            OFF, base, vol, ncell, sizes = CT.build(which)
            C = RG.Complex(OFF, base)
            ng = 4*len(C.types)
            q = np.array([0.31, -0.22, 0.17, 0.4]); s = np.sort(np.linalg.svd(C.Q(q), compute_uv=False)); s /= s[-1]
            nul = int((s < 1e-8).sum()); grk = np.linalg.matrix_rank(C.gauge(q), tol=1e-9)
            kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); ev = []
            for x in (0.02, 0.01):
                Q = C.Q(x*kd); w = np.linalg.eigvalsh(0.5*(Q + Q.conj().T)); ev.append(np.sort(np.abs(w)))
            soft = int(sum(1 for i in range(nul, min(nul + 40, C.E)) if abs(ev[0][i]/ev[1][i] - 4) < 0.1 and ev[1][i] < 1e-2))
            no = sum(ortho(C, sm) for sm in C.simp)
            res = dict(simplices=len(base), types=len(C.types), edges=C.E, vol=vol, cells=sorted(set(sizes)), nullity=nul, gauge=grk,
                       hidden=nul - grk, massless=soft, partners=soft - 6, orthoschemes=no, sym=sym_ok(C))
            results[which] = res
            pickle.dump(C, open(f"canon_{''.join(map(str, which)) or '0'}.pkl", 'wb'))
            print(f"orbits {which!s:14s}: {res['simplices']:4d} simp, {res['types']:2d} types, {res['edges']:4d} edges, vol {vol:.3f}, cells {res['cells']}, B4 {res['sym']}, orthoschemes {no}; nullity {nul} vs gauge {grk} -> hidden {nul-grk}; massless non-gauge {soft} -> partners {soft-6}  [{time.time()-t0:.0f}s]", flush=True)
        except Exception as e:
            print(f"orbits {which}: FAILED {type(e).__name__}: {e}", flush=True)
pickle.dump(results, open('census_results_fix.pkl', 'wb'))
