"""s2: lane F session 2 checks (criteria: checks/s2_criteria.md, written before this script).
Numerical sanity checks only; not proofs."""
import itertools
import math
import os

import numpy as np
from scipy.linalg import expm

RES = []


def rec(name, ok, msg):
    ok = bool(ok)
    RES.append((name, ok))
    print(f"{name}: {'PASS' if ok else 'FAIL'}  {msg}")


# ---------------- A: Lemma LOC-s on a d = 1 ring ----------------
def part_a():
    Ls, p, mu = 24, 1.3, 0.45
    dist = lambda a, b: min((a - b) % Ls, (b - a) % Ls)
    Cm = np.array([[0.7 * math.exp(-0.9 * dist(b, y)) for y in range(Ls)] for b in range(Ls)])
    X = [0, 1]
    dX = [min(dist(y, x) for x in X) for y in range(Ls)]
    B = [y for y in range(Ls) if dX[y] <= 2]
    rest = sorted([y for y in range(Ls) if y not in B], key=lambda y: (dX[y], y))
    F = rest[:12]
    nF = len(F)
    lam = np.zeros(Ls)
    for y in B:
        lam[y] = 1.0
    for y in F:
        lam[y] = 1.0 + math.exp(mu * dX[y])
    R = [p * sum(abs(Cm[b, y]) * lam[y] for y in B + F) for b in (0, 1)]
    h = math.exp(R[0]) + R[0] * R[1] ** 2
    H = lambda A: math.exp(A[0]) + A[0] * A[1] ** 2
    rng = np.random.default_rng(2)
    w = np.array([math.exp(-mu * dX[y]) for y in F])
    a1 = 0.0
    maxratio_bound = 0.0
    nonvac = 0.0
    nonvac3 = 0.0
    a2 = 0.0
    samples = []
    for smp in range(20):
        Z = np.zeros(Ls)
        for y in B + F:
            Z[y] = rng.uniform(-p, p)
        samples.append(Z.copy())
        g = np.empty(2 ** nF)
        for mask in range(2 ** nF):
            Zt = np.zeros(Ls)
            for y in B:
                Zt[y] = Z[y]
            for i in range(nF):
                if mask >> i & 1:
                    Zt[F[i]] = Z[F[i]]
            A = Cm[:2] @ Zt
            g[mask] = H(A)
        f = g.copy()
        for i in range(nF):
            bit = 1 << i
            for mask in range(2 ** nF):
                if mask & bit:
                    f[mask] -= f[mask ^ bit]
        full = g[2 ** nF - 1]
        a1 = max(a1, abs(f.sum() - full) / max(1.0, abs(full)))
        for mask in range(2 ** nF):
            prod = 1.0
            k = 0
            for i in range(nF):
                if mask >> i & 1:
                    prod *= w[i]
                    k += 1
            r = abs(f[mask]) / (h * prod)
            maxratio_bound = max(maxratio_bound, r)
            if mask:
                nonvac = max(nonvac, r)
            if k >= 3:
                nonvac3 = max(nonvac3, r)
        # A2
        for _ in range(10):
            mask = int(rng.integers(1, 2 ** nF))
            S = [i for i in range(nF) if mask >> i & 1]

            def piece(Zv):
                tot = 0.0
                for r_ in range(len(S) + 1):
                    for T in itertools.combinations(S, r_):
                        Zt = np.zeros(Ls)
                        for y in B:
                            Zt[y] = Zv[y]
                        for i in T:
                            Zt[F[i]] = Zv[F[i]]
                        tot += (-1) ** (len(S) - len(T)) * H(Cm[:2] @ Zt)
                return tot
            v1 = piece(Z)
            Z2 = Z.copy()
            for i in range(nF):
                if i not in S:
                    Z2[F[i]] = rng.uniform(-p, p)
            v2 = piece(Z2)
            a2 = max(a2, abs(v1 - v2) / max(1.0, np.abs(f).max()))
    rec("A1", a1 <= 1e-11, f"max rel |sum_S F_S - Phi| = {a1:.2e}  (|B| = {len(B)}, |F| = {nF})")
    rec("A2", a2 <= 1e-12, f"max change of F_S under re-draw off B u S = {a2:.2e}")
    rec("A3", maxratio_bound <= 1.0, f"max |F_S|/(h prod e^-mu delta) = {maxratio_bound:.3e}  (h = {h:.3e})")
    rec("A4", nonvac >= 1e-4 and nonvac3 >= 1e-8, f"max ratio S!=0: {nonvac:.3e}; |S|>=3: {nonvac3:.3e}")


# ---------------- B: Lemma HULL geometry in d = 4 ----------------
def part_b():
    Tc, M = 7, 2
    rng = np.random.default_rng(5)
    offs = [o for o in itertools.product((-1, 0, 1), repeat=4) if any(o)]
    linf = lambda a, b: max(min((a[i] - b[i]) % Tc, (b[i] - a[i]) % Tc) for i in range(4))
    allc = list(itertools.product(range(Tc), repeat=4))
    b1 = b2 = b3 = True
    worst_b2 = -1e9
    min_gap = 1e9
    for trial in range(200):
        c0 = tuple(int(v) for v in rng.integers(0, Tc, 4))
        X = {c0}
        for _ in range(int(rng.integers(0, 3))):
            base = list(X)[int(rng.integers(0, len(X)))]
            o = offs[int(rng.integers(0, len(offs)))]
            X.add(tuple((base[i] + o[i]) % Tc for i in range(4)))
        Xp = {c for c in allc if min(linf(c, x) for x in X) <= 1}
        Y = set(Xp)
        nS = int(rng.integers(1, 5))
        S = []
        while len(S) < nS:
            y = tuple(int(v) for v in rng.integers(0, Tc * M, 4))
            q = tuple(v // M for v in y)
            if q not in Xp:
                S.append(y)
        added_len = 0.0
        bound = 0.0
        for y in S:
            q = tuple(v // M for v in y)
            dl = sorted((linf(q, c), c) for c in Xp)
            n = dl[0][0]
            ctar = dl[0][1]
            D = [((ctar[i] - q[i] + 3) % Tc) - 3 for i in range(4)]
            assert max(abs(v) for v in D) == n
            # cubes met by the segment q + tD, t in [0, 1] (lift coordinates)
            rngs = [range(min(0, D[i]) - 1, max(0, D[i]) + 2) for i in range(4)]
            for k in itertools.product(*rngs):
                lo, hi = 0.0, 1.0
                okk = True
                for i in range(4):
                    if D[i] == 0:
                        if abs(-k[i]) > 0.5 + 1e-12:
                            okk = False
                            break
                    else:
                        t1 = (k[i] - 0.5) / D[i]
                        t2 = (k[i] + 0.5) / D[i]
                        a, b = min(t1, t2), max(t1, t2)
                        lo, hi = max(lo, a), min(hi, b)
                if okk and lo <= hi + 1e-12:
                    Y.add(tuple((q[i] + k[i]) % Tc for i in range(4)))
            added_len += math.sqrt(sum(v * v for v in D)) + 1.0
            bound += 2 * n + 1
            # B3
            delta = min(max(min((y[i] - z[i]) % (Tc * M), (z[i] - y[i]) % (Tc * M)) for i in range(4))
                        for x in X for z in itertools.product(*[range(x[i] * M, x[i] * M + M) for i in range(4)]))
            min_gap = min(min_gap, delta - M * n)
            if not (delta > M * n and n >= 1):
                b3 = False
            if q not in Y:
                b1 = False
        # connectivity
        Yl = list(Y)
        seen = {Yl[0]}
        stack = [Yl[0]]
        while stack:
            c = stack.pop()
            for o in offs:
                nb = tuple((c[i] + o[i]) % Tc for i in range(4))
                if nb in Y and nb not in seen:
                    seen.add(nb)
                    stack.append(nb)
        if len(seen) != len(Y):
            b1 = False
        worst_b2 = max(worst_b2, added_len - bound)
        if added_len > bound + 1e-12:
            b2 = False
    rec("B1", b1, "Y *-connected and contains every q(y), 200 trials")
    rec("B2", b2, f"max (added tree length - sum(2n+1)) = {worst_b2:.3f}")
    rec("B3", b3, f"min (delta - M n) = {min_gap}")


# ---------------- C: constants ----------------
def part_c():
    k0 = 16 * math.log(12800)
    kc = 3 * k0 + 4
    kp = kc + 16 * math.log(2)
    w8 = sum((2 * n + 1) ** 4 * math.exp(-8 * n) for n in range(1, 200))
    rec("C1", w8 <= 0.03, f"kappa_0 = {k0:.4f}, kappa_c = {kc:.4f}, kappa' = {kp:.4f}, w_8 = {w8:.5f}, "
        f"273 kappa' + 1296 w_8 = {273 * kp + 1296 * w8:.1f}")
    mu = 4.83e-11
    # least integer M with mu M >= 3 kappa' + 4 log M + 8 (monotone for M large)
    M = (3 * kp + 8) / mu
    for _ in range(100):
        M = (3 * kp + 4 * math.log(M) + 8) / mu
    Mi = math.ceil(M)
    while mu * (Mi - 1) >= 3 * kp + 4 * math.log(Mi - 1) + 8:
        Mi -= 1
    while mu * Mi < 3 * kp + 4 * math.log(Mi) + 8:
        Mi += 1
    logs = [4 * math.log(Mi) + kp + 4 * math.log(2 * n + 1) - (mu * Mi - 2 * kp) * n for n in range(1, 50)]
    mx = max(logs)
    W = math.exp(mx) * sum(math.exp(l - mx) for l in logs)
    rec("C2", W <= w8 and Mi < 2.646e15, f"M_min = {Mi:.4e}, W(M_min) = {W:.4e}, mu M_min = {mu * Mi:.2f}")


# ---------------- D: Lemma SF-J' coverage ----------------
def haar_su(N, rng):
    Zc = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / math.sqrt(2)
    Q, Rr = np.linalg.qr(Zc)
    d = np.diag(Rr)
    Q = Q * (d / abs(d))
    det = np.linalg.det(Q)
    return Q / det ** (1.0 / N)


def part_d():
    rng = np.random.default_rng(3)
    fr = {}
    d3 = True
    worst_rec = 0.0
    for N, ns in ((2, 10000), (3, 40000), (4, 40000), (5, 10000)):
        good = 0
        for it in range(ns):
            U = haar_su(N, rng)
            ev, W = np.linalg.eig(U)
            ph = np.angle(ev)  # (-pi, pi]
            if abs(ph.sum()) < 1e-8 and np.min(np.abs(ev + 1)) > 1e-12:
                good += 1
            # windows
            phi = np.sort(np.mod(ph, 2 * math.pi))
            K = phi.sum() / (2 * math.pi)
            if abs(K - round(K)) > 1e-8:
                d3 = False
            K = int(round(K))
            count = 0
            sol = None
            for j in range(N):
                for m in range(-N - 2, N + 3):
                    if K + j + N * m == 0:
                        count += 1
                        sol = (j, m)
            if count != 1:
                d3 = False
            if it < 500:
                j, m = sol
                th = np.concatenate([phi[j:], phi[:j] + 2 * math.pi]) + 2 * math.pi * m
                # match th to eigenvectors: th values are representatives of sorted phi
                order = np.argsort(np.mod(ph, 2 * math.pi))
                thv = np.empty(N)
                srt = np.concatenate([phi[j:], phi[:j] + 2 * math.pi]) + 2 * math.pi * m
                idx_sorted = np.concatenate([order[j:], order[:j]])
                for a, idx in enumerate(idx_sorted):
                    thv[idx] = srt[a]
                A = W @ np.diag(1j * thv) @ np.linalg.inv(W)
                err = np.abs(expm(A) - U).max()
                spread = thv.max() - thv.min()
                worst_rec = max(worst_rec, err, abs(np.trace(A)))
                if not (spread < 2 * math.pi):
                    d3 = False
        fr[N] = good / ns
    rec("D1", 0.96 <= fr[3] <= 0.99, f"SU(3) fraction in exp(D_3) = {fr[3]:.4f}  (SU(2) {fr[2]:.4f})")
    rec("D2", 0.93 <= fr[4] <= 0.965, f"SU(4) fraction in exp(D_4) = {fr[4]:.4f}  (SU(5) {fr[5]:.4f}, informational)")
    rec("D3", d3 and worst_rec < 1e-10, f"exactly one spread<2pi traceless log in every sample; reconstruction err {worst_rec:.1e}")


# ---------------- E: Lemma BS ----------------
def rand_su(N, rng, scale):
    Hm = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    A = (Hm - Hm.conj().T) / 2
    A -= np.trace(A) / N * np.eye(N)
    return A * scale / np.linalg.norm(A, 2)


def part_e():
    rng = np.random.default_rng(7)
    s = 0.01
    e1 = True
    worst = -1e9
    cnt = 0
    for N in (2, 3):
        done = 0
        while done < 5000:
            Us = [expm(rand_su(N, rng, rng.uniform(0, 0.06))) for _ in range(4)]
            Up = Us[0] @ Us[1] @ Us[2].conj().T @ Us[3].conj().T
            a = np.linalg.norm(np.eye(N) - Up, 2)
            if a > 0.2:
                continue
            Zs = [expm(rand_su(N, rng, rng.uniform(0, s))) for _ in range(4)]
            V = [Us[i] @ Zs[i] for i in range(4)]
            Vp = V[0] @ V[1] @ V[2].conj().T @ V[3].conj().T
            b = np.linalg.norm(np.eye(N) - Vp, 2)
            worst = max(worst, b - a - 4 * (math.exp(s) - 1))
            if b > a + 4 * (math.exp(s) - 1) + 1e-14:
                e1 = False
            done += 1
            cnt += 1
    rec("E1", e1, f"max (||1-U'_p|| - ||1-U_p|| - 4(e^s-1)) = {worst:.3e} over {cnt} samples")
    rec("E2", 4 * (math.exp(0.01) - 1) <= 4.05 * 0.01, f"4(e^0.01-1) = {4 * (math.exp(0.01) - 1):.6f} vs 0.0405")


if __name__ == "__main__":
    print("s2 (lane F session 2); OMP threads:", os.environ.get("OMP_NUM_THREADS"))
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    ok = all(r[1] for r in RES)
    print("OVERALL:", "PASS" if ok else "FAIL", f"({sum(r[1] for r in RES)}/{len(RES)})")
