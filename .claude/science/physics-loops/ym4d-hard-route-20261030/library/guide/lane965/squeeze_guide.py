#!/usr/bin/env python3
"""Row 965 (gap-squeeze-opus), Step 6: GUIDE runs G0-G4. Refutes or guides only; proves nothing.
Criteria are written in the note (Step 6) before the run.

M1: lattice free scalar of mass m on B = (Z/b)^3. Per mode 2 cosh eps = 2 + m^2 + sum 4 sin^2(k_i/2).
Vacuum covariance C = (2 sinh eps)^-1, one-step mean map A = e^-eps, cross covariance C A^t.
Gaussian identities (exact in the model): S(t;B) = det(1-A^t)^-1 - 1,
S_j(t) = det(C_QQ)/det(C_QQ - (C A^t)_QQ) - 1, S^V_dia(n) = det(1 - a^T a)^-1 - 1 in the Euclidean frame.
M2: SU(2) one-plaquette box, T = M D M on class functions (see endpoint.py).
"""
import math, sys, resource, time
import numpy as np


def rss_guard(limit_gb=2.0):
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # bytes on macOS
    if peak > limit_gb * 1024**3:
        sys.exit("RSS guard: peak %.2f GB" % (peak / 1024**3))


def modes(b, m):
    k = 2 * np.pi * np.arange(b) / b
    s2 = 4 * np.sin(k / 2) ** 2
    lap = s2[:, None, None] + s2[None, :, None] + s2[None, None, :]
    eps = np.arccosh(1 + (m * m + lap) / 2)
    return eps


def kernel(b, sym):
    # real-space translation-invariant kernel with Fourier symbol sym (b,b,b): K(d) = (1/N) sum_k sym_k cos(k.d)
    return np.real(np.fft.ifftn(sym))


def box_sites(b, side, offset):
    r = np.arange(offset, offset + side) % b
    X, Y, Z = np.meshgrid(r, r, r, indexing="ij")
    return np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1)


def sub_matrix(Kd, b, sites):
    x = sites[:, 0].astype(np.int32); y = sites[:, 1].astype(np.int32); z = sites[:, 2].astype(np.int32)
    idx = (((x[:, None] - x[None, :]) % b) * b + ((y[:, None] - y[None, :]) % b)) * b + ((z[:, None] - z[None, :]) % b)
    return Kd.ravel()[idx]


def schedule(b):
    # sides b (periodic), b-2, ..., 2; centred boxes; one site per face per step
    out = [(b, 0)]
    s = b - 2
    off = 1
    while s >= 2:
        out.append((s, off))
        s -= 2
        off += 1
    return out


def shells(b, m, t):
    eps = modes(b, m)
    S_full = math.exp(-np.sum(np.log1p(-np.exp(-t * eps)))) - 1
    Cd = kernel(b, 1 / (2 * np.sinh(eps)))
    CAd = kernel(b, np.exp(-t * eps) / (2 * np.sinh(eps)))
    Sj = []
    for (side, off) in schedule(b):
        if side == b:
            Sj.append(S_full)
            # code test: the shell formula on the full periodic box
            sites = box_sites(b, b, 0)
            Cq = sub_matrix(Cd, b, sites); CAq = sub_matrix(CAd, b, sites)
            l1 = np.linalg.slogdet(Cq)[1]; l2 = np.linalg.slogdet(Cq - CAq)[1]
            g0 = math.exp(l1 - l2) - 1
            continue
        sites = box_sites(b, side, off)
        Cq = sub_matrix(Cd, b, sites); CAq = sub_matrix(CAd, b, sites)
        l1 = np.linalg.slogdet(Cq)[1]; l2 = np.linalg.slogdet(Cq - CAq)[1]
        Sj.append(math.exp(l1 - l2) - 1)
        rss_guard()
    Sj.append(0.0)
    s = [Sj[k] - Sj[k + 1] for k in range(len(Sj) - 1)]
    return S_full, g0, Sj[:-1], s


def diamond(b, m):
    eps = modes(b, m)
    N = b ** 3
    sites_all = box_sites(b, b, 0)
    A = sub_matrix(kernel(b, np.exp(-eps)), b, sites_all)
    Ch = sub_matrix(kernel(b, (2 * np.sinh(eps)) ** -0.5), b, sites_all)  # C^(1/2)
    sch = schedule(b)[1:]
    Mx = np.eye(N)
    for (side, off) in sch:
        sites = box_sites(b, side, off)
        idx = (sites[:, 0] * b + sites[:, 1]) * b + sites[:, 2]
        Qm, _ = np.linalg.qr(Ch[:, idx])  # orthonormal basis of C^(1/2) R^Q
        Mx = Qm @ (Qm.T @ (A @ Mx))
        rss_guard()
    n = len(sch)
    G = np.eye(N) - Mx.T @ Mx
    Sdia = math.exp(-np.linalg.slogdet(G)[1]) - 1
    S2n = math.exp(-np.sum(np.log1p(-np.exp(-2 * n * eps)))) - 1
    # unit share at time 2n
    Cd = kernel(b, 1 / (2 * np.sinh(eps))); CAd = kernel(b, np.exp(-2 * n * eps) / (2 * np.sinh(eps)))
    side, off = sch[-1]
    sites = box_sites(b, side, off)
    Cq = sub_matrix(Cd, b, sites); CAq = sub_matrix(CAd, b, sites)
    Sn = math.exp(np.linalg.slogdet(Cq)[1] - np.linalg.slogdet(Cq - CAq)[1]) - 1
    return n, Sdia, S2n, Sn


def I(nu, x, kmax=200):
    s = 0.0
    lx = math.log(x / 2)
    for k in range(kmax):
        s += math.exp((2 * k + nu) * lx - math.lgamma(k + 1) - math.lgamma(k + nu + 1))
    return s


def half_plaquette(beta, J2max=24, nq=2000):
    th = (np.arange(nq) + 0.5) * math.pi / nq
    wt = (math.pi / nq) * (2 / math.pi) * np.sin(th) ** 2
    chi = np.array([np.sin((n + 1) * th) / np.sin(th) for n in range(J2max + 1)])
    M = np.exp((beta / 2) * (np.cos(th) - 1))
    D = np.array([(math.exp(-beta) * (2 / beta) * I(n + 1, beta)) ** 4 for n in range(J2max + 1)])
    Mm = (chi * wt * M) @ chi.T
    T = Mm @ np.diag(D) @ Mm
    X = (chi * wt * np.cos(th)) @ chi.T  # multiplication by cos(theta) = (1/2) tr U
    ev, V = np.linalg.eigh(T)
    order = np.argsort(ev)[::-1]
    ev = ev[order]; V = V[:, order]
    r = ev[1:] / ev[0]
    amp = V[:, 1:].T @ (X @ V[:, 0])  # <psi_i, cos(theta) psi_0> in L^2(Haar)
    E1 = -math.log(r[0])
    rows = []
    for a in range(2, 13, 2):
        Xa = math.log1p(np.sum(r ** a))
        La = math.sqrt(np.sum(r ** a * amp ** 2))
        rows.append((a, Xa, La))
    return E1, rows, amp[:3]


def massless_V(b, a):
    eps = modes(b, 0.0)
    e = eps.ravel()[1:]  # drop the zero mode
    CAxx = np.sum(np.exp(-a * e) / (2 * np.sinh(e))) / b ** 3
    V = a * b ** 3 * math.sqrt(2) * CAxx
    Xtrue = -np.sum(np.log1p(-np.exp(-a * e)))
    return V, Xtrue


def massive_V(b, a, m):
    eps = modes(b, m).ravel()
    CAxx = np.sum(np.exp(-a * eps) / (2 * np.sinh(eps))) / b ** 3
    V = a * b ** 3 * math.sqrt(2) * CAxx
    Xtrue = -np.sum(np.log1p(-np.exp(-a * eps)))
    return V, Xtrue


if __name__ == "__main__":
    t0 = time.time()
    print("G1 shells (M1). columns: b r a m ma | S | S_n/S vs 8/b^3 | s_0/S | sum_{k<n} s_k/S | min s_k | G0 shell(B)-S")
    for b in (8, 12, 16):
        for r in (2, 4):
            a = b // r
            for ma in (2.0, 4.0, 6.0):
                m = ma / a
                S, g0, Sj, s = shells(b, m, a)
                Sn = Sj[-1]
                print("  %2d %d %d %.3f %.1f | %.4e | %.3e vs %.3e | %.4f | %.4f | %.1e | %.1e" % (
                    b, r, a, m, ma, S, Sn / S, 8 / b ** 3, s[0] / S, sum(s[:-1]) / S, min(s), g0 - S))
                sys.stdout.flush()
    print("G2 (V) diamond (M1). columns: b m n | S^V_dia(n) | S(2n;B) | ratio | unit share S_n(2n)")
    for b in (8, 12):
        for m in (0.5, 1.0):
            n, Sdia, S2n, Sn = diamond(b, m)
            print("  %2d %.2f %d | %.4e | %.4e | %.4f | %.4e" % (b, m, n, Sdia, S2n, Sdia / S2n, Sn))
            sys.stdout.flush()
    print("G3 Lemma HALF on the one-plaquette box (M2). columns: a | X(a) | L(a) | L/X")
    for beta in (2.3, 2.6):
        E1, rows, amp = half_plaquette(beta)
        print("  beta %.2f  E_1 %.4f  <psi_i, x psi_0> i=1..3: %s" % (beta, E1, ["%.3e" % v for v in amp]))
        for (a, Xa, La) in rows:
            print("   %2d | %.4e | %.4e | %.3e" % (a, Xa, La, La / Xa))
        aa = np.array([row[0] for row in rows if row[0] >= 6]); lx = np.log([row[1] for row in rows if row[0] >= 6]); ll = np.log([row[2] for row in rows if row[0] >= 6])
        print("   fitted rates (a = 6..12): X %.4f  L %.4f  (E_1 %.4f, E_1/2 %.4f)" % (-np.polyfit(aa, lx, 1)[0], -np.polyfit(aa, ll, 1)[0], E1, E1 / 2))
    print("G4 massless scalar (zero mode removed), ratio 4: b a | V(a) = a b^3 sqrt2 (CA^a)_xx | X_true")
    for b in (8, 12, 16, 24, 32):
        V, Xt = massless_V(b, b // 4)
        print("  %2d %d | %.4e | %.4e" % (b, b // 4, V, Xt))
    print("G4' massive scalar m = 0.5, ratio 4 (scope note of 3.4 (e)): b a | V | X_true | V/X")
    for b in (8, 12, 16, 24, 32, 40):
        V, Xt = massive_V(b, b // 4, 0.5)
        print("  %2d %d | %.4e | %.4e | %.3e" % (b, b // 4, V, Xt, V / Xt))
    print("elapsed %.1f s, peak RSS %.2f GB" % (time.time() - t0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024**3))
