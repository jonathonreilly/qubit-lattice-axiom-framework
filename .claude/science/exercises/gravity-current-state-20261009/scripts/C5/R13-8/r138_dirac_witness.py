"""R13-8 script D: Dirac-sea variant of the one-loop TT witness.
Naive Dirac h(k) = sum_i alpha_i sin k_i + beta m (4 components, all 8 tastes), filled sea.
Metric vertex (Hermitian, O_h-covariant): M_ij(k1,k2) = 1/4[alpha_i (sin k1_j + sin k2_j) + (i<->j)],
psi^dag_{k+q} M psi_k. Lindhard form, pair (interband) terms only; no seagull (q-independent contact)."""
import numpy as np, os
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "r138_onshell_loop.py")).read()
head, tail = src.split("# ---------------- one-loop witness ----------------")
exec(head.split("dirs = [v / np.linalg.norm(v)")[0])
NG = int(os.environ.get("NG", "24"))
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
Z2 = np.zeros((2, 2)); I2c = np.eye(2)
alpha = [np.block([[Z2, s], [s, Z2]]) for s in (sx, sy, sz)]
beta = np.block([[I2c, Z2], [Z2, -I2c]])
def hk(K, m):
    H = m * beta[None] + sum(np.sin(K[:, i])[:, None, None] * alpha[i][None] for i in range(3))
    e = np.sqrt(m * m + (np.sin(K) ** 2).sum(-1))
    return H, e
def scalar_loop_tt(m, w, q, Ngrid=NG):
    ks = 2 * np.pi * (np.arange(Ngrid) + 0.5) / Ngrid
    K = np.stack(np.meshgrid(ks, ks, ks, indexing="ij"), -1).reshape(-1, 3)
    K2 = K + q[None, :]
    H1, e1 = hk(K, m); H2, e2 = hk(K2, m)
    I4 = np.eye(4)[None]
    Pm1 = 0.5 * (I4 - H1 / e1[:, None, None]); Pp2 = 0.5 * (I4 + H2 / e2[:, None, None])
    Pp1 = 0.5 * (I4 + H1 / e1[:, None, None]); Pm2 = 0.5 * (I4 - H2 / e2[:, None, None])
    S = np.sin(K) + np.sin(K2)
    qn = q / np.linalg.norm(q); E = tt_basis(qn); pols = []
    for a in range(2):
        Hh = np.zeros((4, 4))
        for A, (x, y) in enumerate(SYM):
            Hh[x, y] = E[A, a]; Hh[y, x] = E[A, a]
        P = Hh[1:, 1:]
        # M_a = sum_ij P_ij M_ij = 1/2 sum_ij P_ij alpha_i S_j  (P symmetric)
        Ma = 0.5 * sum(P[i, j] * S[:, j][:, None, None] * alpha[i][None] for i in range(3) for j in range(3))
        pols.append(Ma)
    Mab = np.zeros((2, 2))
    for a in range(2):
        for b in range(2):
            # psi^dag_{k+q} M psi_k : M maps k -> k+q
            t1 = np.einsum("nij,njk,nkl,nli->n", Pp2, pols[a], Pm1, pols[b].conj().transpose(0, 2, 1))
            t2 = np.einsum("nij,njk,nkl,nli->n", Pm2, pols[a], Pp1, pols[b].conj().transpose(0, 2, 1))
            # sea (-) at k -> (+) at k+q : 1/(w - (e1+e2)); (+) at k <- (-) at k+q : -1/(w + e1 + e2)
            val = t1 / (w - (e1 + e2)) - t2 / (w + (e1 + e2))
            Mab[a, b] = val.real.mean()
    return 0.5 * (Mab + Mab.T), E
tail2 = tail.replace('mons2, N2, F2 = res["O_h x T"]', 'mons2, N2 = invariant_forms(G_C_PT, 2)').replace("def scalar_loop_tt(", "def scalar_loop_tt_nn(").replace("np.array2string(sA, precision=3)", "np.array2string(sA, formatter={'float_kind': lambda v: f'{v:.3e}'})")
print(f"[Dirac witness] naive Dirac (8 tastes), Ngrid={NG}")
exec(tail2, globals())
