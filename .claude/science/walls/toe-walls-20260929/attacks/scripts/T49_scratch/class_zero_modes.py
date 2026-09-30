"""For each covariant pairing class found by pairing_census (L=12, |d_i|<=5), build the
invariant Delta, form the BdG matrix, and report (i) number of exact zero modes
(unperturbed: 16 = 8 particle zero modes doubled), (ii) the smallest nonzero |E| relative
to the unperturbed one.  A Majorana mass on the KS zero modes shows up as fewer zero modes."""
import sys, numpy as np
src = open('verify_and_bdg.py').read().split('print("\\n== step 2')[0]
src = src.replace('print(', '(lambda *a, **k: None)(')
sys.argv = ['x', '12']
exec(src)
exec(open('verify_and_bdg.py').read().split('print("\\n== step 2: build invariant Delta for the class of d=(3,1,0), verify invariance ==")')[1].split('nodes, val, ok = build_invariant')[0])
classes_to_test = [(3,1,0),(3,2,-1),(4,2,-1),(4,3,-1),(5,1,0),(4,3,-2),(5,2,-1),(5,3,0),(5,3,-1),(5,3,-2),(5,4,-1),(5,4,-2),(5,4,-3)]
h = np.zeros((N, N))
for (i, j), e in hop.items(): h[i, j] = e
for d in classes_to_test:
    nodes, val, ok = build_invariant(d, -1)
    Delta = np.zeros((N, N))
    for (i, j), x in val.items():
        Delta[i, j] = x; Delta[j, i] = -x
    row = []
    for lam in [0.05, 0.2]:
        H = np.block([[h, lam * Delta], [-lam * Delta, -h]])
        a = np.sort(np.abs(np.linalg.eigvalsh(H)))
        row.append((int(np.sum(a < 1e-8)), round(float(a[a >= 1e-8][0]), 4)))
    par = sum(d) % 2
    print(f"d={d} |d|^2={sum(x*x for x in d)} sublattice parity(sum d)={'odd' if par else 'even'} consistent={ok} n_pairs={len(val)}; (zero modes, first nonzero |E|) at lam=0.05,0.2: {row}", flush=True)
