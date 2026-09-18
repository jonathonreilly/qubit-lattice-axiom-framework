#!/usr/bin/env python3
"""J:falsifier:PR8178 - block 34 (PR #8178), falsifier bullet 2 (C1-C2): "A tiny torus where the covariance recursion and the mode sum
differ, or V_L outside the bracket."  Run on the tori L = 2..48, t <= 64 (C1) and L = 2..20 (C2) - the note: L = 2, 3, 4 with t <= 12 / 8 - exact, with machinery
disjoint from the runner (which iterates Sigma_{t+1} = P Sigma_t P^T + I with rational cosines, possible only for L in {2, 3, 4}).

Objects (the note's declared objects; sigma^2 = 1 per component, an overall scale).  Level plane Z_L^2, predecessors (i,j), (i-1,j),
(i,j-1); P = their average; theta_{t+1} = P theta_t + xi_t from theta_0 = 0.
  C1, process side (real space, integers): N_j(z) = 3^j (P^j)_{0,z} by the recursion N_{j+1}(z) = N_j(z) + N_j(z + e1) + N_j(z + e2)
      on Z_L^2 (paths of the walk); the site variance is v_t = sum_{j<t} sum_z N_j(z)^2 / 9^j and the plane-average variance
      (1/L^4) sum_{j<t} sum_z (column sum of P^j)^2.
  C1, mode side (Laurent coefficients, integers): |phi|^2 = (3 + x + 1/x + y + 1/y + x/y + y/x)/9, so sum_k u_k^j = L^2 * (sum of the
      coefficients c_j(a, b) of (3 + x + 1/x + y + 1/y + x/y + y/x)^j with a = b = 0 mod L)/9^j, and the note's mode formula
      v_t = (1/L^2)[t + sum_{k != 0} (1 - u_k^t)/(1 - u_k)] = (1/L^2) sum_{j<t} sum_k u_k^j becomes an exact rational for every L
      (no cosine is ever evaluated).
  C2 (V_L inside the bracket): V_L = (1/L^2) sum_{k != 0} 1/(1 - u_k) is rational for every L (a Galois-invariant sum); here it is
      computed by an exact real-space linear solve: A = I - P P^T + J (J = projector on constants) has eigenvalues 1 - u_k (k != 0) and 1,
      so V_L = (A^{-1})_{00} - 1/L^2 by translation invariance.  S_L = sum over nonzero n in (-L/2, L/2]^2 of 1/|n|^2 exactly;
      the bracket (3/(4 pi^2)) S_L <= V_L <= (9/16) S_L is decided exactly with rational enclosures of pi.
HIT if any equality fails or V_L leaves the bracket.  Deterministic; fractions only for the exact parts.
"""
import sys
import time
from fractions import Fraction as Fr

L_C1 = list(range(2, 49))          # C1 tori
T_C1 = 64                          # levels t = 1..T_C1
L_C2 = list(range(2, 21))          # C2 tori (exact linear solve of size L^2)
PI_LO, PI_HI = Fr(314159265358979, 10 ** 14), Fr(314159265358980, 10 ** 14)


def path_counts(L, jmax):
    """N_j for j = 0..jmax-1 as dicts over Z_L^2 (Python ints)."""
    N = [[0] * L for _ in range(L)]
    N[0][0] = 1
    out = []
    for _ in range(jmax):
        out.append(N)
        M = [[N[i][j] + N[(i + 1) % L][j] + N[i][(j + 1) % L] for j in range(L)] for i in range(L)]
        N = M
    return out


def laurent_powers(jmax):
    """coefficients of (3 + x + 1/x + y + 1/y + x/y + y/x)^j, j = 0..jmax-1."""
    base = {(0, 0): 3, (1, 0): 1, (-1, 0): 1, (0, 1): 1, (0, -1): 1, (1, -1): 1, (-1, 1): 1}
    cur = {(0, 0): 1}
    out = []
    for _ in range(jmax):
        out.append(cur)
        nxt = {}
        for (a, b), c in cur.items():
            for (da, db), d in base.items():
                key = (a + da, b + db)
                nxt[key] = nxt.get(key, 0) + c * d
        cur = nxt
    return out


def c1():
    print(f"== C1: site variance and plane-average variance, process side (path counts) vs mode formula (Laurent coefficients); "
          f"L = {L_C1[0]}..{L_C1[-1]}, t = 1..{T_C1}")
    lp = laurent_powers(T_C1)
    bad = 0
    n = 0
    for L in L_C1:
        Ns = path_counts(L, T_C1)
        v_proc = Fr(0)
        v_mode = Fr(0)
        pa = Fr(0)
        ok_L = True
        for t in range(1, T_C1 + 1):
            j = t - 1
            Nj = Ns[j]
            sq = sum(Nj[a][b] ** 2 for a in range(L) for b in range(L))
            v_proc += Fr(sq, 9 ** j)
            modesum = sum(c for (a, b), c in lp[j].items() if a % L == 0 and b % L == 0)   # = (9^j/L^2) sum_k u_k^j
            v_mode += Fr(modesum, 9 ** j)                                                    # (1/L^2) sum_k u_k^j
            # plane average: column sums of P^j are sum_x (P^j)_{x,z} = sum_w (P^j)_{0,w} (translation invariance) = 3^j/3^j
            colsum = Fr(sum(Nj[a][b] for a in range(L) for b in range(L)), 3 ** j)
            pa += Fr(L * L, L ** 4) * colsum ** 2                                            # (1/L^4) sum_z (colsum)^2
            n += 1
            if v_proc != v_mode or pa != Fr(t, L * L):
                bad += 1
                ok_L = False
        # the note's closed mode formula at t = T_C1 from the same coefficients: t + sum_{k != 0}(1 - u^t)/(1 - u) = sum_{j<t} sum_k u^j
        print(f"[C1] L={L:2d}: {'equal' if ok_L else 'DIFFER'} at t = 1..{T_C1}; v_{T_C1} = {float(v_proc):.12f} "
              f"(denominator {len(str(v_proc.denominator))} digits); plane-average variance t/L^2 at every t: {ok_L}")
    return n, bad


def solve_exact(A, b):
    """Gauss-Jordan with Fractions; A is a list of lists."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        rowc = [x / pv for x in M[col]]
        M[col] = rowc
        nz = [(j, x) for j, x in enumerate(rowc) if x != 0]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                Mr = M[r]
                for j, x in nz:
                    Mr[j] -= f * x
    return [M[i][n] for i in range(n)]


def c2():
    print(f"== C2: V_L exact by a real-space linear solve; S_L exact; bracket (3/(4 pi^2)) S_L <= V_L <= (9/16) S_L; L = {L_C2[0]}..{L_C2[-1]}")
    bad = 0
    rows = []
    for L in L_C2:
        t0 = time.time()
        n = L * L
        idx = lambda i, j: (i % L) * L + (j % L)
        P = [[Fr(0)] * n for _ in range(n)]
        for i in range(L):
            for j in range(L):
                for (a, b) in ((i, j), (i - 1, j), (i, j - 1)):
                    P[idx(i, j)][idx(a, b)] += Fr(1, 3)
        # P P^T (sparse rows: 3 entries each)
        rowsP = [[(c, x) for c, x in enumerate(P[r]) if x != 0] for r in range(n)]
        PPt = [[Fr(0)] * n for _ in range(n)]
        for r in range(n):
            for s in range(n):
                acc = Fr(0)
                ds = dict(rowsP[s])
                for c, x in rowsP[r]:
                    if c in ds:
                        acc += x * ds[c]
                PPt[r][s] = acc
        A = [[(Fr(1) if r == s else Fr(0)) - PPt[r][s] + Fr(1, n) for s in range(n)] for r in range(n)]
        e0 = [Fr(1) if r == 0 else Fr(0) for r in range(n)]
        g = solve_exact(A, e0)
        V = g[0] - Fr(1, n)
        half = L // 2
        reps = range(-((L - 1) // 2), half + 1)                  # (-L/2, L/2]
        S = sum(Fr(1, a * a + b * b) for a in reps for b in reps if (a, b) != (0, 0))
        lo_ok = V >= Fr(3, 4) / (PI_LO ** 2) * S                    # 3/(4 pi^2) < 3/(4 PI_LO^2): V above the larger value suffices
        hi_ok = V <= Fr(9, 16) * S
        if not (lo_ok and hi_ok):
            bad += 1
        pos = (float(V) / float(S) - 3 / (4 * 3.141592653589793 ** 2)) / (9 / 16 - 3 / (4 * 3.141592653589793 ** 2))
        rows.append((L, V, S))
        print(f"[C2] L={L:2d}: V_L/sigma^2 = {float(V):.12f} (exact, denominator {len(str(V.denominator))} digits), S_L = {float(S):.10f}, "
              f"V_L/S_L = {float(V) / float(S):.6f} in [{3 / (4 * 3.141592653589793 ** 2):.6f}, {9 / 16:.6f}]: {lo_ok and hi_ok} "
              f"(position {pos:.3f} of the bracket; {time.time() - t0:.1f}s)")
    # the tiny tori of the note, cross-checked by the rational-cosine mode sum (a third route) at L = 2, 3, 4, 6
    COS = {2: [1, -1], 3: [1, Fr(-1, 2), Fr(-1, 2)], 4: [1, 0, -1, 0], 6: [1, Fr(1, 2), Fr(-1, 2), -1, Fr(-1, 2), Fr(1, 2)]}
    third = []
    for L, V, S in rows:
        if L in COS:
            c = COS[L]
            s = Fr(0)
            for a in range(L):
                for b in range(L):
                    if (a, b) == (0, 0):
                        continue
                    u = (3 + 2 * Fr(c[a]) + 2 * Fr(c[b]) + 2 * Fr(c[(a - b) % L])) / 9
                    s += 1 / (1 - u)
            third.append((L, s / (L * L) == V))
            if s / (L * L) != V:
                bad += 1
    print(f"[C2] cross-check with the rational-cosine mode sum on L = 2, 3, 4, 6: {third}")
    return len(rows), bad


def main():
    t0 = time.time()
    n1, b1 = c1()
    n2, b2 = c2()
    print(f"[time] {time.time() - t0:.1f}s")
    if b1:
        print(f"HIT: C1 - {b1} of {n1} (L, t) pairs where the process-side site variance or plane-average variance differs from the mode formula")
    if b2:
        print(f"HIT: C2 - {b2} tori where V_L lies outside the bracket or the exact routes disagree")
    print(f"SUMMARY: C1 exact on L = {L_C1[0]}..{L_C1[-1]} x t = 1..{T_C1} ({n1} pairs; path counts vs Laurent coefficients): {n1 - b1} equal, "
          f"{b1} differ; C2 exact V_L (real-space solve) on L = {L_C2[0]}..{L_C2[-1]}: {n2 - b2} inside the bracket [3/(4 pi^2), 9/16] S_L, "
          f"{b2} outside; falsifier {'FIRES' if (b1 or b2) else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
