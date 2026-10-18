import sys, time, pickle, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
t0 = time.time(); OFF, S = RG.d4cone(); C = RG.Complex(OFF, S)
print("D4 cone:", len(S), "simplices,", C.E, "edges,", len(C.terms), "hinges,", len(C.types), "vertex types", f"{time.time()-t0:.1f}s")
vol = sum(np.sqrt(np.linalg.det((lambda E: E @ E.T)(np.array([C.pos(v) for v in s])[1:] - C.pos(s[0]))))/24 for s in S)
print("total simplex volume per cell:", vol)
pickle.dump(C, open('d4.pkl', 'wb'))
rng = np.random.default_rng(0)
for kk in [0.4*rng.standard_normal(4), np.array([0.7, 0, 0, 0]), np.array([1.2, -0.6, 0.3, 0.9])]:
    Q = C.Q(kk); s = np.sort(np.linalg.svd(Q, compute_uv=False)); s /= s[-1]
    lg = np.log10(np.maximum(s, 1e-300)); i = int(np.argmax(np.diff(lg)[:60]))
    G = C.gauge(kk)
    print(f"k={np.round(kk,2)}: nullity {i+1} (gap {s[i]:.0e} -> {s[i+1]:.0e}); gauge rank {np.linalg.matrix_rank(G, tol=1e-9)}; |QG|/|Q| {np.abs(Q@G).max()/np.abs(Q).max():.0e}")
