"""E18: the triangle no-go stated with the choice at A and the signal in B's history, on lines.
A: sites (-1, 0, 1) -> indices (0, 1, 2); B: sites (0, 1) -> indices (0, 1).
psi_0 = (|0>_A|0>_B + |1>_A|1>_B)/sqrt2
tick 0: A applies R(theta) on its bond {0,1}, theta in {pi/8, 3pi/8} (A's choice); B idle.
tick 1: A moves its site-0 possibility to site -1 (R(pi/2) on the pair (-1, 0)); B applies R(pi/4).
Checks: min TV over all one-site rules with Born odds of B's two-tick history law across A's
choices (expect sqrt2 - 1), with dual certificate; Markov-L feasibility at each tick;
and the control without A's split (expect 0).
"""
import numpy as np
from scipy.sparse import coo_matrix
from mtlp import Model, history_lp, markov_local_lp, block_unitary, line_adj, rot
nA, nB, T = 3, 2, 2
psi = np.zeros((nA, nB), complex); psi[1, 0] = psi[2, 1] = 1 / np.sqrt(2)
psi0 = psi.reshape(-1)
th = [np.pi / 8, 3 * np.pi / 8]
for label, split in (('A splits its branches at tick 1', True), ('control: A idle at tick 1', False)):
    UA = [[block_unitary(nA, [[1, 2]], [rot(t)]) for t in th],
          [block_unitary(nA, [[0, 1]], [rot(np.pi / 2)]) if split else np.eye(nA, dtype=complex)]]
    UB = [[np.eye(nB, dtype=complex)], [rot(np.pi / 4)]]
    m = Model(psi0, UA, UB, [line_adj(nA)] * T, [line_adj(nB)] * T)
    lp, idx = history_lp(m, ns=True, caus=False)
    w = {'NSB': 1.0, 'BORN': 1e4}
    r = lp.solve(soft=w, method='highs-ds')
    y = r.eqlin.marginals
    A = coo_matrix((lp.vals, (lp.rows, lp.cols)), shape=(lp.nr, lp.nv)).tocsr()
    b = np.array(lp.b)
    ml = [markov_local_lp(m, k, method='highs-ds')[0].status == 0 for k in range(T)]
    print(f"{label:34s}: min sum|mu_B diff| = {r.slack_by_tag['NSB']:.6f} (TV {r.slack_by_tag['NSB']/2:.6f}; "
          f"sqrt2-1 = {np.sqrt(2)-1:.6f}); certificate b.y = {b @ y:.6f}, max A^T y = {(A.T @ y).max():.1e}; "
          f"Markov-L feasible per tick: {ml}")
    for i, t in enumerate(th):
        P1 = m.born(((i, 0),)); P2 = m.born(((i, 0), (0, 0)))
        idxA = {0: 0, 1: 1, 2: 1} if split else {1: 0, 2: 1}   # A's branch label at time 2
        if split:
            e2 = P2[0, 1] + P2[2, 0]       # b2 != branch(a2): (a=-1 i.e. branch 0, b=1) or (a=1, b=0)
        else:
            e2 = P2[1, 1] + P2[2, 0]
        d1 = P1[1, 1] + P1[2, 0]
        print(f"     theta={t/np.pi:.3f}pi: P(b1 != a1) = {d1:.6f};  P(b2 != branch(a2)) = {e2:.6f}")
