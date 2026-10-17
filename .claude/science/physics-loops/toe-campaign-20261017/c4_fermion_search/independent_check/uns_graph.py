"""Claim (3): orbit commutation graph for the unsoldered C4z/C3-fixed class (vectorized, chunked)."""
import sys, pickle, time, numpy as np
sys.path.insert(0, '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4')
from sitecore import *
W = '/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/indep_C4/'
t0 = time.time()
orbs = pickle.load(open(W + 'orbs_unsoldered_C4z_C3.pkl', 'rb'))
idS = (0,)*7
orbs = [(S, d) for S, d, ok in orbs if S != idS]
N = len(orbs); print('orbits', N)
members = [T for S, d in orbs for T in d]; morb = np.array([u for u, (S, d) in enumerate(orbs) for T in d])
M = len(members); print('strings', M)
reps = np.array([S for S, d in orbs], np.uint64); mem = np.array(members, np.uint64)
swap = lambda c: ((c & np.uint64(7)) << np.uint64(3)) | (c >> np.uint64(3))
NC = np.zeros((N, N), bool)
for start in range(0, N, 400):
    R = reps[start:start+400]; acc = np.zeros((len(R), M), bool)
    for t, pr in OVL.items():
        a = np.zeros(len(R), np.uint64); b = np.zeros(M, np.uint64)
        for k, (i, j) in enumerate(pr):
            a |= R[:, i] << np.uint64(6*k); b |= swap(mem[:, j]) << np.uint64(6*k)
        acc |= (np.bitwise_count(a[:, None] & b[None, :]) & 1).astype(bool)
    # orbit aggregation
    for u in range(len(R)):
        NC[start + u, np.unique(morb[acc[u]])] = True
print('built %.1fs' % (time.time() - t0))
assert (NC == NC.T).all()
assert not NC.diagonal().any()
# spot check against scalar code
import random; random.seed(3)
for _ in range(3000):
    u, v = random.randrange(N), random.randrange(N)
    sc = all(comm_translates(orbs[u][0], T) for T in orbs[v][1])
    assert sc == (not NC[u, v])
A = ~NC; np.fill_diagonal(A, False)
print('edges', int(A.sum()) // 2, 'density %.4f' % (A.sum() / N / (N - 1)), 'degree min/max', A.sum(1).min(), A.sum(1).max())
np.save(W + 'uns_adj.npy', A); pickle.dump(orbs, open(W + 'uns_orbs.pkl', 'wb'))
print('time %.1fs' % (time.time() - t0))
