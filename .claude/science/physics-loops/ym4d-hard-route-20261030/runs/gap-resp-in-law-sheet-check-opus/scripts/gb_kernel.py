"""Guide run for Lemma GB (row 1120 check). Pure Python, no imports beyond math, sys.

Square {0..l}^2, interior {1..l-1}^2, Dirichlet graph Laplacian D - A (D = 4).
For y = (0, j) on F_- and y' = (l, j') on F_+ (non-corner), x(y) = (1, j), x(y') = (l-1, j').
Gaussian sheet: K(y, y') / b = G_D(x(y), x(y')) = P_{x(y)}(walk exits at y').

Method A (spectral): G = U diag(w) U^T with U[j][n] = sqrt(2/l) sin(n pi j / l),
  w_n = sum_m (2/l) sin^2(m pi / l) (-1)^(m+1) / (lam_m + lam_n), lam_k = 2 - 2 cos(k pi / l).
Method B (direct elimination on the full interior system), for small l only.

Prints: l, S1 = sum |G| (sum over y' of P(exit through F_-)), R2 = l^2 sum G^2 (R_c^2 / b^2),
and the minimum over y' in the middle half of F_+ of l * P_{x(y')}(exit through F_-).
"""
import math
import sys


def spectral(l):
    lam = [2.0 - 2.0 * math.cos(k * math.pi / l) for k in range(l)]
    c = [0.0] * l
    for m in range(1, l):
        c[m] = (2.0 / l) * math.sin(m * math.pi / l) ** 2 * (1.0 if m % 2 == 1 else -1.0)
    w = [0.0] * l
    for n in range(1, l):
        s = 0.0
        for m in range(1, l):
            s += c[m] / (lam[m] + lam[n])
        w[n] = s
    U = [[0.0] * l for _ in range(l)]
    for j in range(1, l):
        for n in range(1, l):
            U[j][n] = math.sqrt(2.0 / l) * math.sin(n * math.pi * j / l)
    G = [[0.0] * l for _ in range(l)]
    for j in range(1, l):
        Uj = U[j]
        for jp in range(1, l):
            Ujp = U[jp]
            s = 0.0
            for n in range(1, l):
                s += Uj[n] * w[n] * Ujp[n]
            G[j][jp] = s
    return G


def direct(l):
    # unknowns: interior sites (i, j), 1 <= i, j <= l-1; solve (4I - A) u = e_target for each target column
    idx = {}
    sites = []
    for i in range(1, l):
        for j in range(1, l):
            idx[(i, j)] = len(sites)
            sites.append((i, j))
    N = len(sites)
    M = [[0.0] * N for _ in range(N)]
    for k, (i, j) in enumerate(sites):
        M[k][k] = 4.0
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (i + di, j + dj)
            if q in idx:
                M[k][idx[q]] -= 1.0
    # invert by Gauss-Jordan (small N only)
    A = [row[:] + [1.0 if r == c else 0.0 for c in range(N)] for r, row in enumerate(M)]
    for col in range(N):
        piv = max(range(col, N), key=lambda r: abs(A[r][col]))
        A[col], A[piv] = A[piv], A[col]
        p = A[col][col]
        A[col] = [v / p for v in A[col]]
        for r in range(N):
            if r != col and A[r][col] != 0.0:
                f = A[r][col]
                A[r] = [a - f * b for a, b in zip(A[r], A[col])]
    Ginv = [row[N:] for row in A]
    G = [[0.0] * l for _ in range(l)]
    for j in range(1, l):
        for jp in range(1, l):
            G[j][jp] = Ginv[idx[(1, j)]][idx[(l - 1, jp)]]
    return G


def stats(G, l):
    S1 = 0.0
    S2 = 0.0
    for j in range(1, l):
        for jp in range(1, l):
            S1 += abs(G[j][jp])
            S2 += G[j][jp] ** 2
    lo, hi = l // 4, l - l // 4
    mins = min(l * sum(G[j][jp] for j in range(1, l)) for jp in range(max(1, lo), min(l, hi + 1)))
    neg = min(G[j][jp] for j in range(1, l) for jp in range(1, l))
    return S1, l * l * S2, mins, neg


def main():
    for l in (6, 8):
        Gs = spectral(l)
        Gd = direct(l)
        diff = max(abs(Gs[j][jp] - Gd[j][jp]) for j in range(1, l) for jp in range(1, l))
        print("check l=%d max|spectral-direct|=%.3e" % (l, diff))
    for l in (8, 16, 32, 64, 128, 256):
        G = spectral(l)
        S1, R2, mins, neg = stats(G, l)
        print("l=%4d  sum|K|/b=%.6f  R_c^2/b^2=%.6f  min_mid l*P(exit F_-)=%.6f  min entry=%.3e" % (l, S1, R2, mins, neg))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
