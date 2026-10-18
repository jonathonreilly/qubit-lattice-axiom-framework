#!/usr/bin/env python3
"""B18 check 7: dimension of the on-site intertwiner space V HL(k) = w HL(k + pi e) V, all e != 0, w in {1,-1,i,-i};
is it the 3-dim diagonal per-plane family (so the c3 family is complete for on-site V)?"""
from chk_model import *
rng = np.random.default_rng(2); ks = rng.uniform(-np.pi, np.pi, (5, 3)); I = np.eye(12); out = {}
for e in [np.array(t) for t in itertools.product((0, 1), repeat=3) if any(t)]:
    for w in (1, -1, 1j, -1j):
        A = np.vstack([np.kron(RLk(k).T, I) - w * np.kron(I, RLk(k + np.pi * e)) for k in ks]); _, s, Vh = np.linalg.svd(A)
        s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))]); nb = [v.conj().reshape(12, 12, order='F') for v in Vh[s < 1e-9]]
        diag = all(np.allclose(b, np.diag(np.diag(b))) for b in nb)
        out[(tuple(e), w)] = (len(nb), diag)
print(out)
ok = all(v == (3, True) for (e, w), v in out.items() if w in (1, -1)) and all(v[0] == 0 for (e, w), v in out.items() if w in (1j, -1j))
print(f"[{'PASS' if ok else 'FAIL'}] on-site H_link intertwiners: 3-dim and diagonal for every e != 0 and w = +-1; none for w = +-i")
print(f"\nTOTAL: PASS={int(ok)} FAIL={int(not ok)}")
