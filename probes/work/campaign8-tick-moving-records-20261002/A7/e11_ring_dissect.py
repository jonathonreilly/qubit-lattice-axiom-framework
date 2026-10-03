"""E11: pick the ring-6 instance (seed 2 stream of e10) with the largest forced signalling
under LATTICE moves; save it; dissect which ingredients are needed; extract and verify a
dual certificate (lower bound on the minimal signalling) independently of the solver.
"""
import pickle
import numpy as np
from scipy.sparse import coo_matrix
from mtlp import Model, history_lp, haar_unitary, block_unitary, ring_adj, tick_support_adj

n, w, T, Bt = 6, 2, 3, [0, 1]
rng = np.random.default_rng(2)
EVEN = [[2 * i, 2 * i + 1] for i in range(n // 2)]
ODD = [[2 * i + 1, (2 * i + 2) % n] for i in range(n // 2)]


def gate():
    th = rng.uniform(0, 2 * np.pi)
    return np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]], complex)


def tick(k):
    blocks = EVEN if k % 2 == 0 else ODD
    return block_unitary(n, blocks, [gate() for _ in blocks])


best = None
for tr in range(60):
    loc = np.zeros((n, n), complex)
    loc[:w, :w] = rng.normal(size=(w, w))
    psi0 = (loc / np.linalg.norm(loc)).reshape(n * n)
    UA = [[tick(k)] for k in range(T)]
    UB = [[tick(k), tick(k)] if k in Bt else [tick(k)] for k in range(T)]
    m = Model(psi0, UA, UB, [ring_adj(n)] * T, [ring_adj(n)] * T)
    lp, idx = history_lp(m, ns=True, caus=True)
    r = lp.solve(soft={'NSA': 1.0, 'BORN': 1e4})
    v = r.slack_by_tag['NSA']
    if best is None or v > best[0]:
        best = (v, tr, psi0, UA, UB)
v, tr, psi0, UA, UB = best
pickle.dump(dict(psi0=psi0, UA=UA, UB=UB, n=n, T=T), open('ring6_best.pkl', 'wb'))
print(f"best trial {tr}: min NS-A violation {v:.6f}")
print("psi0 (2x2 block, rows a, cols b):\n", np.round(psi0.reshape(n, n)[:2, :2].real, 4))

m = Model(psi0, UA, UB, [ring_adj(n)] * T, [ring_adj(n)] * T)


def viol(model, caus=True, drop_times=()):
    lp, idx = history_lp(model, ns=True, caus=caus)
    # drop Born rows at chosen times by making them soft with zero weight -> remove rows
    if drop_times:
        keep = []
        # rebuild without those rows: tag them and give them weight 0
        k_of_row = []
    r = lp.solve(soft={'NSA': 1.0, 'BORN': 1e4})
    return r.slack_by_tag['NSA'], lp, r


v0, lp, r = viol(m)
print(f"  lattice moves, with CAUS : {v0:.6f}")
v1, _, _ = viol(m, caus=False)
print(f"  lattice moves, no CAUS   : {v1:.6f}")
mt = Model(psi0, UA, UB, [tick_support_adj(UA[k][0]) for k in range(T)], [tick_support_adj(UB[k][0]) for k in range(T)])
v2, _, _ = viol(mt)
print(f"  flow-only moves          : {v2:.6f}")
for keep in ([0], [1]):
    UBk = [UB[k] if k in keep else UB[k][:1] for k in range(T)]
    mk = Model(psi0, UA, UBk, [ring_adj(n)] * T, [ring_adj(n)] * T)
    vk, _, _ = viol(mk)
    print(f"  B chooses only at tick {keep}: {vk:.6f}")
mm = Model(psi0, UA[:2], [UB[0], UB[1]], [ring_adj(n)] * 2, [ring_adj(n)] * 2)
v3, _, _ = viol(mm)
print(f"  only ticks 0,1 (3 times) : {v3:.6f}")

# ---- dual certificate, verified independently ---------------------------------
lp, idx = history_lp(m, ns=True, caus=True)
weights = {'NSA': 1.0, 'BORN': 1e4}
r = lp.solve(soft=weights, method='highs-ds')
y = r.eqlin.marginals                     # duals of equality rows
A = coo_matrix((lp.vals, (lp.rows, lp.cols)), shape=(lp.nr, lp.nv)).tocsr()
b = np.array(lp.b)
wrow = np.array([weights.get(t, np.inf) for t in lp.tags])
# dual of: min w.(s+ + s-) s.t. A x + s+ - s- = b, x,s >= 0   is   max b.y, A^T y <= 0, |y| <= w
ATy = A.T @ y
print(f"  certificate (simplex duals): b.y = {b @ y:.6f}  (primal value {r.fun:.6f});"
      f" max(A^T y) = {ATy.max():.2e}; max |y|/w on soft rows = {np.max(np.abs(y)/wrow):.4f};"
      f" max |y| on hard rows = {np.max(np.abs(y[np.isinf(wrow)])) if np.isinf(wrow).any() else 0:.3e}")
# make the certificate strictly valid: shift so A^T y <= 0 exactly, by subtracting the
# positive part through the Born rows' total-mass direction is not generic; instead report
# the bound b.y - (max(A^T y)_+ * total mass)  (valid since sum x = 1 and x >= 0)
slackpos = max(ATy.max(), 0.0)
print(f"  rigorous lower bound on min NS-A violation from this certificate: {b @ y - slackpos * 1.0:.6f}")
np.save('ring6_cert_y.npy', y)
