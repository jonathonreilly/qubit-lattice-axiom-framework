"""bb7c: weighted residuals of the S_1-chain under symmetric / asymmetric S4'-type root maps (lane B session 7), d = 2.

Criteria: checks/bb7c_criteria.md (written before this script). Abelian, L = 3, ternary DD8 pair (bb5 conventions: fine site
3i + r sits at coarse coordinate i + r/3; roots at fine sites 3I). Arrays A1[x, y] = link (x, y) -> (x + 1, y), A2 = (x, y) -> (x, y + 1).
"""
import time

import numpy as np

T0 = time.time()
rng = np.random.default_rng(7373)
L = 3
T = 6
KMAX = 5


def lagrange_weights(p, t):
    nodes = np.arange(-p + 1, p + 1)
    w = np.ones(len(nodes))
    for a, qa in enumerate(nodes):
        for b, qb in enumerate(nodes):
            if a != b:
                w[a] *= (t - qb) / (qa - qb)
    return nodes, w


def s0_matrix(N, p=4):
    S = np.zeros((3 * N, N))
    for r in range(3):
        nodes, w = lagrange_weights(p, r / 3.0)
        for i in range(N):
            for q, wq in zip(nodes, w):
                S[3 * i + r, (i + q) % N] += wq
    return S


def s1_matrix(S0, N):
    """Derived scheme on links (bb5): zero-mean part through a periodic potential, mean part uniformly."""
    P0 = np.eye(N) - np.ones((N, N)) / N
    C = np.tril(np.ones((N, N)), -1)
    P = C @ P0
    Df = -np.eye(3 * N)
    Df[np.arange(3 * N), (np.arange(3 * N) + 1) % (3 * N)] += 1.0
    return Df @ S0 @ P + np.ones((3 * N, N)) / (3.0 * N)


def refine(A1, A2):
    N = A1.shape[0]
    S0 = s0_matrix(N)
    S1 = s1_matrix(S0, N)
    return S1 @ A1 @ S0.T, S0 @ A2 @ S1.T


def qmap(A1, A2, ys):
    """Average over transverse offsets y in ys of the contour root -> root + y e_perp -> straight 3-leg -> back to the root."""
    N = A1.shape[0] // 3
    q1 = np.zeros((N, N))
    q2 = np.zeros((N, N))
    for y in ys:
        # x-links: from (3I, 3J) up by y along e2, 3 steps along e1 at row 3J + y, down from (3I + 3, 3J + y) to (3I + 3, 3J)
        leg = sum(np.roll(A1, -r, axis=0) for r in range(3))          # leg[x, y'] = sum_r A1[x + r, y']
        vert = np.zeros_like(A1)                                       # vert[x, y0] = integral along e2 from y0 to y0 + y
        if y > 0:
            vert = sum(np.roll(A2, -m, axis=1) for m in range(y))
        elif y < 0:
            vert = -sum(np.roll(A2, -m, axis=1) for m in range(y, 0))
        val = vert + np.roll(leg, -y, axis=1) - np.roll(vert, -3, axis=0)
        q1 += val[0::3, 0::3][:N, :N]
        # y-links: mirror (swap roles of the axes)
        leg2 = sum(np.roll(A2, -r, axis=1) for r in range(3))
        hor = np.zeros_like(A1)
        if y > 0:
            hor = sum(np.roll(A1, -m, axis=0) for m in range(y))
        elif y < 0:
            hor = -sum(np.roll(A1, -m, axis=0) for m in range(y, 0))
        val2 = hor + np.roll(leg2, -y, axis=0) - np.roll(hor, -3, axis=1)
        q2 += val2[0::3, 0::3][:N, :N]
    return q1 / len(ys), q2 / len(ys)


QS = {"ax": [0], "sym": [-1, 0, 1], "asym": [0, 1]}
out = []
# C0 structure
N = 8
lam = rng.standard_normal((3 * N, 3 * N))
d1 = np.roll(lam, -1, 0) - lam
d2 = np.roll(lam, -1, 1) - lam
ev = lam[0::3, 0::3]
e1 = np.roll(ev, -1, 0) - ev
e2 = np.roll(ev, -1, 1) - ev
c0 = max(max(np.abs(qmap(d1, d2, ys)[0] - e1).max(), np.abs(qmap(d1, d2, ys)[1] - e2).max()) for ys in QS.values())
c0 /= np.abs(lam).max()

# chain
Bk = (rng.standard_normal((T, T)), rng.standard_normal((T, T)))
chain = [Bk]
for _ in range(KMAX):
    chain.append(refine(*chain[-1]))
# chain[m] is the level k - m field when the depth is k (top = chain[0])
qax_dev = 0.0
for m in range(1, KMAX + 1):
    q1, q2 = qmap(*chain[m], QS["ax"])
    qax_dev = max(qax_dev, np.abs(q1 - chain[m - 1][0]).max(), np.abs(q2 - chain[m - 1][1]).max())
qax_dev /= max(np.abs(Bk[0]).max(), np.abs(Bk[1]).max())
C0 = c0 <= 1e-12 and qax_dev <= 1e-10
out.append(f"C0 root covariance max|Q d lam - d ev lam|/max|lam| = {c0:.1e}; max|Q_ax B_j - B_(j+1)|/max|B_k| = {qax_dev:.1e}: "
           f"{'PASS' if C0 else 'FAIL'}")

# C1 Lemma Gamma0 on a patch (linear field, constant curvature H = 1); evaluate at the patch centre link
P = 30
zz = np.indices((P, P)).astype(float)
Bl1 = -zz[1] / 2.0          # A1(x, y) at the link (x, y)->(x+1, y): -H y / 2
Bl2 = zz[0] / 2.0           # A2(x, y): H x / 2
# rolled sums near the centre do not see the wrap-around for offsets <= 4
qa = qmap(Bl1, Bl2, QS["ax"])
qs_ = qmap(Bl1, Bl2, QS["sym"])
qa2 = qmap(Bl1, Bl2, QS["asym"])
ic = P // 6  # coarse index well inside the patch
g_sym = max(abs(qs_[0][ic, ic] - qa[0][ic, ic]), abs(qs_[1][ic, ic] - qa[1][ic, ic]))
g_asym = max(abs(qa2[0][ic, ic] - qa[0][ic, ic]), abs(qa2[1][ic, ic] - qa[1][ic, ic]))
C1 = g_sym <= 1e-12 and g_asym >= 0.1
out.append(f"C1 Lemma Gamma0 (constant curvature 1): |(Q_sym - Q_ax)B| = {g_sym:.1e}; control |(Q_asym - Q_ax)B| = {g_asym:.3f}: "
           f"{'PASS' if C1 else 'FAIL'}")


def weighted(k, ys, theta):
    """W_theta(k, j) for j = 0..k-1, using the depth-k chain chain[0..k] (level j = chain[k - j])."""
    W = []
    for j in range(k):
        Bj = chain[k - j]
        Bj1 = chain[k - j - 1]
        q1, q2 = qmap(*Bj, ys)
        r = max(np.abs(q1 - Bj1[0]).max(), np.abs(q2 - Bj1[1]).max())
        W.append(L ** (theta * (k - j)) * L ** (2 * (k - 1 - j)) * r)
    return np.array(W)


Ws = {(nm, th): weighted(KMAX, QS[nm], th) for nm in ("sym", "asym") for th in (0.0, 0.5, 1.0)}
C2 = Ws[("sym", 0.5)][0] / Ws[("sym", 0.5)][4] <= 0.5
C3 = Ws[("sym", 1.0)].max() <= 2 * Ws[("sym", 1.0)][4]
C4 = Ws[("asym", 0.5)][0] / Ws[("asym", 0.5)][4] >= 2
out.append(f"C2 symmetric, theta = 1/2: W(5,0)/W(5,4) = {Ws[('sym', 0.5)][0] / Ws[('sym', 0.5)][4]:.4f} (<= 0.5): {'PASS' if C2 else 'FAIL'}")
out.append(f"C3 symmetric, theta = 1: max_j W/W(5,4) = {Ws[('sym', 1.0)].max() / Ws[('sym', 1.0)][4]:.4f} (<= 2): {'PASS' if C3 else 'FAIL'}")
out.append(f"C4 control asymmetric, theta = 1/2: W(5,0)/W(5,4) = {Ws[('asym', 0.5)][0] / Ws[('asym', 0.5)][4]:.4f} (>= 2): "
           f"{'PASS' if C4 else 'FAIL'}")
out.append("C5 informational profiles W_theta(5, j), j = 0..4 (finest first):")
for (nm, th), W in Ws.items():
    out.append(f"  {nm:4s} theta = {th:.1f}: " + ", ".join(f"{x:.4f}" for x in W))
mx = [weighted(k, QS["sym"], 0.5).max() for k in range(1, KMAX + 1)]
out.append("  symmetric max_j W_1/2(k, j), k = 1..5: " + ", ".join(f"{x:.4f}" for x in mx))
allp = C0 and C1 and C2 and C3 and C4
out.append(f"VERDICT: {'ALL PASS' if allp else 'NOT ALL PASS'} (C0-C4)")
out.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(out))
