"""bb5: linearised covariant lifts in d = 2 (lane B session 5).

Criteria: checks/bb5_criteria.md (written before this script). Model only: abelian, one real component, L = 3,
trivial background. Tests (R2) of REVIEW_BFT_B_S4 Part E (C^{1,alpha} stability of iterated commuting refinement pairs,
coarse units) and Lemma CL-blk's mechanism (corner lift + gauge-invariant descent keeps the block-constant extension).
"""
import time
import numpy as np
from scipy.interpolate import CubicSpline

T0 = time.time()
L = 3
T = 6
MMAX = 5
ALPHA = 0.25


def lagrange_weights(p, t):
    nodes = np.arange(-p + 1, p + 1)
    w = np.ones(len(nodes))
    for a, qa in enumerate(nodes):
        for b, qb in enumerate(nodes):
            if a != b:
                w[a] *= (t - qb) / (qa - qb)
    return nodes, w


def s0_matrix(scheme, N):
    """1D refinement: coarse periodic N -> fine 3N; fine 3i+r sits at coarse coordinate i + r/3."""
    S = np.zeros((3 * N, N))
    if scheme == "CS":
        x = np.arange(N + 1, dtype=float)
        xf = np.arange(3 * N) / 3.0
        for i in range(N):
            y = np.zeros(N + 1)
            y[i] = 1.0
            if i == 0:
                y[N] = 1.0
            S[:, i] = CubicSpline(x, y, bc_type="periodic")(xf)
        return S
    p = {"W": 1, "DD4": 2, "DD6": 3, "DD8": 4}[scheme]
    for r in range(3):
        nodes, w = lagrange_weights(p, r / 3.0)
        for i in range(N):
            for q, wq in zip(nodes, w):
                S[3 * i + r, (i + q) % N] += wq
    return S


def diff_matrix(N):
    D = -np.eye(N)
    D[np.arange(N), (np.arange(N) + 1) % N] += 1.0
    return D


def s1_matrix(S0, N):
    """Derived scheme on links: zero-mean part through a periodic potential, mean part uniformly (1/3 per fine link)."""
    P0 = np.eye(N) - np.ones((N, N)) / N
    C = np.tril(np.ones((N, N)), -1)  # p_i = sum_{l<i} d_l
    P = C @ P0
    Df = diff_matrix(3 * N)
    return Df @ S0 @ P + np.ones((3 * N, N)) / (3.0 * N)


def refine_pair(A1, A2, S0, S1):
    return S1 @ A1 @ S0.T, S0 @ A2 @ S1.T


def d0(mu):
    return np.roll(mu, -1, 0) - mu, np.roll(mu, -1, 1) - mu


def curv(A1, A2):
    return A1 + np.roll(A2, -1, 0) - np.roll(A1, -1, 1) - A2


def q_ax(A1, A2):
    N = A1.shape[0] // 3
    q1 = A1[0::3, 0::3] + A1[1::3, 0::3] + A1[2::3, 0::3]
    q2 = A2[0::3, 0::3] + A2[0::3, 1::3] + A2[0::3, 2::3]
    return q1[:N, :N], q2[:N, :N]


def q_ax_T(q1, q2):
    N = q1.shape[0]
    A1 = np.zeros((3 * N, 3 * N))
    A2 = np.zeros((3 * N, 3 * N))
    for r in range(3):
        A1[r::3, 0::3] = q1
        A2[0::3, r::3] = q2
    return A1, A2


def corner(A1, A2):
    N = A1.shape[0]
    F1 = np.zeros((3 * N, 3 * N))
    F2 = np.zeros((3 * N, 3 * N))
    for dl in (-1, 0, 1):
        idx = (3 * np.arange(N) + dl) % (3 * N)
        F1[np.ix_(3 * np.arange(N) + 1, idx)] = A1
        F2[np.ix_(idx, 3 * np.arange(N) + 1)] = A2
    return F1, F2


def corner0(mu):
    R = np.repeat(np.repeat(mu, 3, 0), 3, 1)  # R[f] = mu[f // 3]
    idx = np.arange(1, 3 * mu.shape[0] + 1)  # fine 3I-1, 3I, 3I+1 -> I
    return R.take(idx, axis=0, mode="wrap").take(idx, axis=1, mode="wrap")


def descend(A1, A2, nsteps=18, tau=0.1):
    for _ in range(nsteps):
        F = curv(A1, A2)
        g1 = F - np.roll(F, 1, 1)
        g2 = np.roll(F, 1, 0) - F
        q1, q2 = q_ax(g1, g2)
        c1, c2 = q_ax_T(q1, q2)
        A1 = A1 - tau * (g1 - c1 / 3.0)
        A2 = A2 - tau * (g2 - c2 / 3.0)
    return A1, A2


def proxies(A1, A2, m):
    rho = float(L) ** (-m)
    X = [A1 / rho, A2 / rho]
    P0 = max(np.abs(x).max() for x in X)
    G = [(np.roll(x, -1, ax) - x) / rho for x in X for ax in (0, 1)]
    P1 = max(np.abs(g).max() for g in G)
    P3 = max(np.abs((np.roll(g, -1, ax) - g) / rho).max() for g in G for ax in (0, 1))

    def holder(H):
        best = 0.0
        for t in range(m + 1):
            s = L ** t
            delta = s * rho
            for ax in (0, 1):
                best = max(best, np.abs(np.roll(H, -s, ax) - H).max() / delta ** ALPHA)
        return best

    P2 = max(holder(g) for g in G)
    F = curv(A1, A2) / rho ** 2
    return dict(P0=P0, P1=P1, P2=P2, P3=P3, F0=np.abs(F).max(), F1=holder(F))


def main():
    rng = np.random.default_rng(20261028)
    B1 = rng.standard_normal((T, T))
    B2 = rng.standard_normal((T, T))
    sc = max(np.abs(B1).max(), np.abs(B2).max())
    B1, B2 = B1 / sc, B2 / sc
    rng2 = np.random.default_rng(20261029)
    mu = rng2.standard_normal((T, T))
    g1, g2 = d0(mu)
    scg = max(np.abs(g1).max(), np.abs(g2).max())
    mu = mu / scg
    G1, G2 = d0(mu)

    mats = {}
    res = {}
    ident_ok = True
    worst = {}
    for scheme in ("W", "DD4", "DD6", "DD8", "CS"):
        A1, A2 = B1.copy(), B2.copy()
        M = mu.copy()
        rows = []
        w_comm = w_ev = w_q = 0.0
        for m in range(1, MMAX + 1):
            N = A1.shape[0]
            if (scheme, N) not in mats:
                S0 = s0_matrix(scheme, N)
                mats[(scheme, N)] = (S0, s1_matrix(S0, N))
            S0, S1 = mats[(scheme, N)]
            # identities on this level
            dm1, dm2 = d0(M)
            r1, r2 = refine_pair(dm1, dm2, S0, S1)
            Mf = S0 @ M @ S0.T
            e1, e2 = d0(Mf)
            sM = max(np.abs(dm1).max(), np.abs(dm2).max())
            w_comm = max(w_comm, max(np.abs(r1 - e1).max(), np.abs(r2 - e2).max()) / sM)
            w_ev = max(w_ev, np.abs(Mf[0::3, 0::3] - M).max() / np.abs(M).max())
            A1n, A2n = refine_pair(A1, A2, S0, S1)
            q1, q2 = q_ax(A1n, A2n)
            sA = max(np.abs(A1).max(), np.abs(A2).max())
            w_q = max(w_q, max(np.abs(q1 - A1).max(), np.abs(q2 - A2).max()) / sA)
            A1, A2, M = A1n, A2n, Mf
            rows.append(proxies(A1, A2, m))
        worst[scheme] = (w_comm, w_ev, w_q)
        if max(w_comm, w_ev, w_q) > 1e-11:
            ident_ok = False
        res[scheme] = rows

    # Phi-chain (corner lift + constrained gauge-invariant descent)
    phi = {}
    for label, (b1, b2) in (("I", (B1, B2)), ("II", (G1, G2))):
        A1, A2 = b1.copy(), b2.copy()
        M = mu.copy()
        rows, wq, wg = [], 0.0, 0.0
        for m in range(1, MMAX + 1):
            C1, C2 = corner(A1, A2)
            A1n, A2n = descend(C1, C2)
            q1, q2 = q_ax(A1n, A2n)
            sA = max(np.abs(A1).max(), np.abs(A2).max())
            wq = max(wq, max(np.abs(q1 - A1).max(), np.abs(q2 - A2).max()) / sA)
            A1, A2 = A1n, A2n
            if label == "II":
                M = corner0(M)
                e1, e2 = d0(M)
                sE = max(np.abs(e1).max(), np.abs(e2).max())
                wg = max(wg, max(np.abs(A1 - e1).max(), np.abs(A2 - e2).max()) / sE)
            rows.append(proxies(A1, A2, m))
        phi[label] = (rows, wq, wg)

    # ---- report ----
    def line(rows, key):
        return " ".join("%.3g" % r[key] for r in rows)

    print("bb5 (d=2, L=3, T=6, depths 1..5, alpha=1/4); proxies per depth m=1..5")
    for scheme in res:
        wc, we, wqq = worst[scheme]
        print("[%s] identities: comm %.1e ev %.1e Qax %.1e" % (scheme, wc, we, wqq))
        for key in ("P0", "P1", "P2", "P3", "F0", "F1"):
            print("  %s: %s" % (key, line(res[scheme], key)))
    for label in ("I", "II"):
        rows, wq, wg = phi[label]
        print("[Phi, input %s] Qax constraint %.1e%s" % (label, wq, ("  gauge identity %.1e" % wg) if label == "II" else ""))
        for key in ("P0", "P1", "P2", "P3", "F0", "F1"):
            print("  %s: %s" % (key, line(rows, key)))

    def ratio(rows, key, a, b):
        return rows[b - 1][key] / rows[a - 1][key]

    def bounded(rows):
        return all(0.8 <= ratio(rows, k, 3, 5) <= 1.25 for k in ("P0", "P1", "P2"))

    verdict = {}
    verdict["B5-1"] = ident_ok and phi["I"][1] <= 1e-11 and phi["II"][1] <= 1e-11
    rW = ratio(res["W"], "P1", 2, 5)
    verdict["B5-2"] = rW >= 10
    verdict["B5-3"] = bounded(res["CS"])
    loc = [s for s in ("DD4", "DD6", "DD8") if bounded(res[s])]
    verdict["B5-4"] = len(loc) > 0
    rPhi = ratio(phi["II"][0], "P1", 2, 5)
    verdict["B5-5"] = phi["II"][2] <= 1e-11 and rPhi >= 10
    print("ratios: W P1(5)/P1(2) = %.3g; Phi(II) P1(5)/P1(2) = %.3g" % (rW, rPhi))
    for s in ("CS", "DD4", "DD6", "DD8"):
        print("  %s P(5)/P(3): P0 %.3f P1 %.3f P2 %.3f P3 %.3f" % (
            s, ratio(res[s], "P0", 3, 5), ratio(res[s], "P1", 3, 5), ratio(res[s], "P2", 3, 5), ratio(res[s], "P3", 3, 5)))
    print("  Phi(I) F1(5)/F1(3) = %.3f, F0(5)/F0(3) = %.3f" % (ratio(phi["I"][0], "F1", 3, 5), ratio(phi["I"][0], "F0", 3, 5)))
    print("local schemes passing the B5-3 condition:", loc)
    for k in sorted(verdict):
        print(k, "PASS" if verdict[k] else "FAIL")
    print("VERDICT", "ALL PASS" if all(verdict.values()) else "NOT ALL PASS (%d/%d)" % (sum(verdict.values()), len(verdict)))
    print("[t = %.1f s]" % (time.time() - T0))


if __name__ == "__main__":
    main()
