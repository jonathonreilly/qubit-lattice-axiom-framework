import sys, numpy as np
sys.argv = ['x', sys.argv[1] if len(sys.argv) > 1 else '8']
exec(open('massive_bdg.py').read().split('RM = 2 if L == 8 else 3')[0])
for d in [(1,1,1), (3,1,1)]:
    val = all_invariants(d)[0]
    Delta = np.zeros((N, N))
    for (i, j), x in val.items(): Delta[i, j] = x; Delta[j, i] = -x
    print("class", d, " pairs:", len(val))
    for lam in [0.0, 0.01, 0.02, 0.05, 0.1]:
        H = np.block([[hm, lam * Delta], [-lam * Delta, -hm]])
        E = np.linalg.eigvalsh(H)
        pos = np.sort(E[E > 0])[:8]
        print(f"  lam={lam:5.2f} lowest positive BdG levels: {np.round(pos,4)}")
