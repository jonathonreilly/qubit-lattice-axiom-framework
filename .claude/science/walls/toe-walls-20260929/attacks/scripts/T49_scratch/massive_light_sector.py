"""With the staggered Dirac mass m (H = h + m * diag(eps_v)), the 8 light modes sit at +-m.
Does a covariant charge-2 pairing split / shift them at first order?  (BdG, lowest levels.)"""
import sys, numpy as np
src = open('verify_and_bdg.py').read().split('print("\\n== step 2')[0].replace('print(', '(lambda *a, **k: None)(')
sys.argv = ['x', '12']
exec(src)
exec(open('verify_and_bdg.py').read().split('print("\\n== step 2: build invariant Delta for the class of d=(3,1,0), verify invariance ==")')[1].split('nodes, val, ok = build_invariant')[0])
h = np.zeros((N, N))
for (i, j), e in hop.items(): h[i, j] = e
eps = np.array([(-1) ** (sum(coords(i))) for i in range(N)], dtype=float)
m = 0.3
hm = h + m * np.diag(eps)
w0 = np.linalg.eigvalsh(hm)
print("unperturbed lowest |E|:", np.round(np.sort(np.abs(w0))[:16], 4))
for d in [(3, 1, 0), (4, 2, -1), (3, 2, -1)]:
    nodes, val, ok = build_invariant(d, -1)
    Delta = np.zeros((N, N))
    for (i, j), x in val.items():
        Delta[i, j] = x; Delta[j, i] = -x
    out = []
    for lam in [0.0, 0.02, 0.05, 0.1]:
        H = np.block([[hm, lam * Delta], [-lam * Delta, -hm]])
        a = np.sort(np.abs(np.linalg.eigvalsh(H)))
        out.append(np.round(a[:16:2], 5))
    print(f"d={d}: lowest |E| (every other) at lam=0,0.02,0.05,0.1:")
    for lam, o in zip([0.0, 0.02, 0.05, 0.1], out): print("   lam", lam, o)
