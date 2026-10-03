"""E20: the triangle family for general mixing angle phi at the reading record B.
A chooses theta0 = phi/2 or theta1 = phi/2 + pi/4, then splits; B applies R(phi).
Predicted minimal TV of B's two-tick history law = sin(phi) + cos(phi) - 1 (0 < phi < pi/2).
"""
import numpy as np
from mtlp import Model, history_lp, block_unitary, line_adj, rot
nA, nB, T = 3, 2, 2
psi = np.zeros((nA, nB), complex); psi[1, 0] = psi[2, 1] = 1 / np.sqrt(2)
for phi in (np.pi / 12, np.pi / 6, np.pi / 4, np.pi / 3, 5 * np.pi / 12):
    th = [phi / 2, phi / 2 + np.pi / 4]
    UA = [[block_unitary(nA, [[1, 2]], [rot(t)]) for t in th], [block_unitary(nA, [[0, 1]], [rot(np.pi / 2)])]]
    UB = [[np.eye(nB, dtype=complex)], [rot(phi)]]
    m = Model(psi.reshape(-1), UA, UB, [line_adj(nA)] * T, [line_adj(nB)] * T)
    lp, idx = history_lp(m, ns=True, caus=False)
    r = lp.solve(soft={'NSB': 1.0, 'BORN': 1e4}, method='highs-ds')
    print(f"phi={phi/np.pi:.4f}pi: LP min TV = {r.slack_by_tag['NSB']/2:.6f};  sin+cos-1 = {np.sin(phi)+np.cos(phi)-1:.6f}")
