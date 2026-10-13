"""R18-1 s4 (written before running). The bU = infinity sector: {0,1} labels with integer G n = 0, in the trivial
coset (span of local moves). MILP (HiGHS): random objectives, require 1 <= sum n <= 6V-1 and n != all-ones pattern
classes; collect distinct solutions; report their structure (which slot types, whether winding: line/plane sums).
Also: (i) every single cube/mu8 flip from a gamma=0 state creates charges (all 2^6 / 2^8 lifts have G delta != 0);
(ii) Z^3 moment lemma: a finitely supported nonnegative integer delta with G delta = 0 is zero (M0 = -D(G delta) = 0)."""
import numpy as np, itertools, sys, time
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csr_matrix, hstack, vstack, identity
from common import *
# (i) lifts
for name, p in [("cube", orbit(CUBE)[0]), ("mu8", orbit(MU8)[0])]:
    ninv = 0
    for sg in itertools.product([1, -1], repeat=len(p)):
        chk = {}
        for ((d, t), s) in zip(p, sg):
            for e, c in G_entries(d, t): chk[e] = chk.get(e, 0) + c*s
        ninv += all(v == 0 for v in chk.values())
    print("(i) %s: %d sign lifts, integer-invariant: %d  -> every %s flip from a gamma=0 state changes gamma" % (name, 2**len(p), ninv, name))
def f2_null(B):
    """basis of {h : B h = 0 mod 2}"""
    B = (B % 2).astype(np.uint8); r, c = B.shape; M = B.copy(); piv = []; row = 0
    for col in range(c):
        pr = None
        for i in range(row, r):
            if M[i, col]: pr = i; break
        if pr is None: continue
        M[[row, pr]] = M[[pr, row]]; nz = np.nonzero(M[:, col])[0]; nz = nz[nz != row]; M[nz] ^= M[row]
        piv.append(col); row += 1
        if row == r: break
    free = [j for j in range(c) if j not in piv]; H = []
    for f in free:
        h = np.zeros(c, dtype=np.int64); h[f] = 1
        for i, pc in enumerate(piv):
            if M[i, f]: h[pc] = 1
        H.append(h)
    return np.array(H)
for L in [3, 4]:
    V = L**3; G = G_matrix(L); B = f2_basis(pattern_vectors(L)); H = f2_null(B)
    assert np.all((B @ H.T) % 2 == 0)
    nS = 6*V; nH = H.shape[0]
    # vars: n (nS bin), u (nH int): G n = 0 ; H n - 2u = 0 ; 1 <= sum n <= nS-1
    A1 = hstack([csr_matrix(G), csr_matrix((G.shape[0], nH))])
    A2 = hstack([csr_matrix(H), csr_matrix(-2*np.eye(nH))])
    A3 = hstack([csr_matrix(np.ones((1, nS))), csr_matrix((1, nH))])
    cons = [LinearConstraint(A1, 0, 0), LinearConstraint(A2, 0, 0), LinearConstraint(A3, 1, nS - 1)]
    lb = np.concatenate([np.zeros(nS), np.zeros(nH)]); ub = np.concatenate([np.ones(nS), np.full(nH, nS)])
    rng = np.random.default_rng(L); sols = {}
    t0 = time.time()
    for trial in range(4):
        c = np.concatenate([rng.normal(size=nS), np.zeros(nH)])
        res = milp(c=c, constraints=cons, integrality=np.ones(nS + nH), bounds=Bounds(lb, ub), options={'time_limit': 25})
        if res.x is None: print("  L=%d trial %d: %s" % (L, trial, res.message)); continue
        n = np.round(res.x[:nS]).astype(int); sols[n.tobytes()] = n
    print("L=%d: trivial-coset gamma=0 configurations found (excluding 0 and all-ones by the sum bound): %d distinct in 4 MILPs (%.0fs)" % (L, len(sols), time.time() - t0))
    for n in list(sols.values())[:4]:
        nt = n.reshape(6, L, L, L); dens = nt.reshape(6, -1).mean(1)
        # winding test: diagonal n_jj constant along j? face n_ij constant in the ij plane?
        const = []
        for t, (i, j) in enumerate(TYPES):
            a = nt[t]
            if i == j: const.append(bool(np.all(a == np.take(a, [0], axis=j))))
            else: const.append(bool(np.all(a == np.take(np.take(a, [0], axis=i), [0], axis=j))))
        print("   sum n = %d ; densities by type %s ; each type of line/plane (winding) form: %s ; G n = 0: %s"
              % (n.sum(), np.round(dens, 3), const, bool(np.all(G @ n == 0))))
