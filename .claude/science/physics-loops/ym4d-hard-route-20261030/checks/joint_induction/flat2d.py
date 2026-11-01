#!/usr/bin/env python3
"""Two-step test of the flat commuting current on a d = 2 torus, and of nested walls.

Registered before the first run (2026-11-01, mac-mini-worker, item joint-induction).

Model. d = 2, abelian, fine plaquette angles theta on Z_N^2, L = 3, s_l = 3^l. The
level-l flux of a coarse plaquette is the tent-weighted sum of Text 3.1 of the mapped
file, t(a) = s - |a - (s - 1)|, 0 <= a <= 2 s - 2, so T_l theta(Y) = sum t(a) t(b) theta / s^2.
H_l := range T_l^*, P_j := 1 - projector on H_(j+1), so P_j = Pi_0 + ... + Pi_j.
d = 2 has no Bianchi identity and only finitely many levels, so this is a model.

Part B (current). Phi[w, P] of toy_formula.py, f_j := Phi[w, P_j] - Phi[w, P_(j-1)], for w the
plaquette weight of a level-(j+1) block, theta = T^* G^-1 psi, psi a coarse flux.
 B1 PASS if |sum over all blocks of f_j| <= 1e-9 sum |f_j| (the current is a current).
 B2 PASS if the fitted decay of |f_j(psi_1) - f_j(psi_2)|, psi_1 = psi_2 on Q_n about the block,
    is at least 0.5 per coarse cell, at j = 0, 1 (compare rho_f >= 2 kappa of RC-rates).
 B3 PASS if R(n) := |f(pi_n^* psi) - f(pi_(n-1)^* psi)| / (E_n exp(-0.5 n)) stays below
    20 R_max(n <= 2), where E_n is the energy of psi on Q_n: the K1 form with kappa = 0.5.
 B4 PASS if f_j(lambda psi) = lambda^2 f_j(psi) to 1e-9: no term linear or constant.
Controls: C-B1 at w = 1 must give |f| <= 1e-9 sum over blocks |f|; C-B2 with psi_2 = psi_1 must
give 0.

Part A (nest). Strip in x, period N_y in y. Constraints: every level-n plaquette (W fixed), and
on nested layers about an inner and an outer sheet the level-l plaquettes for l < n, each layer
a union of whole level-(l+1) blocks, inside the shadow of the next at clearance r level-(l+1)
blocks. Rows normalised to unit l^2 norm. G := C C^T. lam := smallest non-zero eigenvalue,
K(l, l') := block of pinv(G) between inner level-l rows and outer level-l' rows.
 A1 PASS if lam at depth n stays >= (1/2) lam at depth 2, n = 2, 3, 4, at clearance 2: no
    depth-growing coercivity loss, by inf-sup.
 A2 PASS if for every (l, l') the fitted rate of ||K(l, l')|| in D is >= 0.7 per coarse cell at
    each depth: no slower channel.
 A3 PASS if at fixed D the largest sqrt(#rows_l #rows_l') ||K(l, l')|| / sqrt(rows_top^2) at
    depth n stays <= 3 times its value at depth 2: amplitude uniform in depth, with the count of
    fine data included, which is what (MD*) asks of worst data.
Failures are kept. A run can refute; it discharges nothing. Stops itself above 2 GB RSS.

Amended before Part A ran, criteria A1 to A3 unchanged: the first geometry (each layer inside the
last, clearance 2) gives about 44000 finest rows at depth 4, too large for a dense solve under the
2 GB limit, so no such run was made. Each level-l layer now has half-width 3 s_(l+1) about its
sheet, clearance 2 level-(l+2) blocks, and period Ny = s_n. Depths 2 and 3 are also reported at
Ny = 3 s_n, which carries non-zero coarse momentum along the wall; depth 4 is not.
"""
import resource
import sys
import time

import numpy as np
import scipy.sparse as sp

RSS_LIMIT = 2 * 1024 ** 3


def guard():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_LIMIT:
        sys.exit("RSS guard: above 2 GB, stopping")


# ---------------------------------------------------------------- Part B
class Level:
    """Projector on H_l on the torus Z_N^2, by FFT, for s = 3^l."""

    def __init__(self, N, s):
        self.N, self.s = N, s
        t = np.zeros(N)
        for a in range(2 * s - 1):
            t[a] = (s - abs(a - (s - 1))) / s
        self.h = np.outer(t, t)
        self.Fh = np.fft.fft2(self.h)
        M = N // s
        self.M = M
        delta = np.zeros((M, M))
        delta[0, 0] = 1.0
        g = self.T(self.Tt(delta))
        self.Gh = np.fft.fft2(g)

    def T(self, th):
        c = np.fft.ifft2(np.fft.fft2(th) * np.conj(self.Fh)).real
        return c[:: self.s, :: self.s]

    def Tt(self, psi):
        u = np.zeros((self.N, self.N))
        u[:: self.s, :: self.s] = psi
        return np.fft.ifft2(np.fft.fft2(u) * self.Fh).real

    def Ginv(self, psi):
        return np.fft.ifft2(np.fft.fft2(psi) / self.Gh).real

    def B(self, th):
        return self.Tt(self.Ginv(self.T(th)))

    def lift(self, psi):
        return self.Tt(self.Ginv(psi))

    def rows(self):
        """B e_p for p in one block: array (s, s, N, N)."""
        s, N = self.s, self.N
        out = np.zeros((s, s, N, N))
        for a in range(s):
            for b in range(s):
                e = np.zeros((N, N))
                e[a, b] = 1.0
                out[a, b] = self.B(e)
        return out


class Proj:
    """P = 1 - B for the level l; carries diag and Hadamard-square action."""

    def __init__(self, lev):
        self.lev = lev
        self.s, self.N = lev.s, lev.N
        self.rowsB = lev.rows()
        s, N = self.s, self.N
        dB = np.array([[self.rowsB[a, b, a, b] for b in range(s)] for a in range(s)])
        self.dB = np.tile(dB, (N // s, N // s))
        self.Fsq = np.fft.fft2(self.rowsB ** 2, axes=(2, 3))

    def apply(self, v):
        return v - self.lev.B(v)

    def diag(self):
        return 1.0 - self.dB

    def hadamard(self, v):
        """(P o P) v, entrywise square of the kernel."""
        s, N = self.s, self.N
        Fv = np.fft.fft2(v)
        out = np.zeros((N, N))
        for a in range(s):
            for b in range(s):
                c = np.fft.ifft2(Fv * np.conj(self.Fsq[a, b])).real
                # c[Y] = sum_r B(a + 0, r - Y... )^2 v(r): row at p = (a, b) + s Y
                out[a:: s, b:: s] = c[:: s, :: s]
        return (1.0 - 2.0 * self.dB) * v + out


def phi(w, theta, P):
    d = P.diag()
    a = 0.5 * np.sum(w * theta * P.apply(theta * d))
    b = 0.25 * np.sum(w * P.hadamard(theta ** 2))
    c = 0.25 * np.sum(w * theta ** 2 * d)
    return a + b - c


def block_weight(N, s, Y=(0, 0)):
    """w_p := number of corners of plaquette p in the block / 4."""
    site = np.zeros((N, N))
    x0, y0 = Y[0] * s, Y[1] * s
    site[np.ix_((x0 + np.arange(s)) % N, (y0 + np.arange(s)) % N)] = 1.0
    w = (site + np.roll(site, -1, 0) + np.roll(site, -1, 1) + np.roll(np.roll(site, -1, 0), -1, 1)) / 4.0
    return w


def fj(w, theta, Pj, Pm):
    v = phi(w, theta, Pj)
    if Pm is not None:
        v -= phi(w, theta, Pm)
    return v


def pullback(psi, n):
    """pi_n^* on coarse plaquette fluxes, centred on cell 0, on Z_M^2."""
    M = psi.shape[0]
    assert 4 * n < M
    # site map phi on the circle, sites -M/2..M/2, coordinates relative to the centre
    def phi_site(i):
        i = ((i + M // 2) % M) - M // 2
        if abs(i) <= n:
            return i
        # the return arc runs across the antipode in the last 2 n steps
        half = M / 2.0
        d = half - abs(i)
        if d >= n:
            return n if i > 0 else -n
        val = (d / n) * n if False else None
        return None

    # build by the explicit arc: order sites 0..M-1 around the circle from -n
    ph = np.zeros(M, dtype=int)
    ms = M // 2
    for k in range(M):
        i = k if k <= ms else k - M
        a = abs(i)
        if a <= n:
            ph[k] = i
        elif a <= ms - n:
            ph[k] = n if i > 0 else -n
        else:
            # distance from the antipode
            rem = ms - a
            ph[k] = (rem if i > 0 else -rem)
    out = np.zeros_like(psi)
    for a in range(M):
        pa, qa = ph[a], ph[(a + 1) % M]
        if pa == qa:
            continue
        ca, sa = (pa, 1) if qa == pa + 1 else (qa, -1)
        for b in range(M):
            pb, qb = ph[b], ph[(b + 1) % M]
            if pb == qb:
                continue
            cb, sb = (pb, 1) if qb == pb + 1 else (qb, -1)
            out[a, b] = sa * sb * psi[ca % M, cb % M]
    return out


def part_b():
    N = 243
    rng = np.random.default_rng(2026)
    levels = {l: Level(N, 3 ** l) for l in (1, 2)}
    print("levels ready", flush=True)
    t0 = time.time()
    P0 = Proj(levels[1])
    P1 = Proj(levels[2])
    guard()
    print("projectors ready", round(time.time() - t0, 1), "s", flush=True)
    results = {}
    for j, (Pj, Pm, lev) in {0: (P0, None, levels[1]), 1: (P1, P0, levels[2])}.items():
        s, M = lev.s, lev.M
        w0 = block_weight(N, s)
        # B1
        psi = rng.normal(size=(M, M))
        th = lev.lift(psi)
        res = np.max(np.abs(Pj.apply(th)))
        vals = []
        for Y in [(a, b) for a in range(M) for b in range(M)]:
            vals.append(fj(block_weight(N, s, Y), th, Pj, Pm))
            if len(vals) >= M * M:
                break
        vals = np.array(vals)
        b1 = abs(vals.sum()) / np.abs(vals).sum()
        tot = abs(fj(np.ones((N, N)), th, Pj, Pm)) / np.abs(vals).sum()
        # B4
        f1 = fj(w0, th, Pj, Pm)
        f2 = fj(w0, 2.5 * th, Pj, Pm)
        b4 = abs(f2 - 2.5 ** 2 * f1) / abs(f2)
        print(f"j={j}: P theta resid {res:.2e}; B1 {b1:.2e}; C-B1 {tot:.2e}; B4 {b4:.2e}; "
              f"rms f {np.sqrt(np.mean(vals ** 2)):.4e}", flush=True)
        # B2
        rs = list(range(1, min(M // 2 - 1, 11)))
        means = []
        for n in rs:
            acc = []
            for trial in range(6):
                p1 = rng.normal(size=(M, M))
                p2 = rng.normal(size=(M, M))
                idx = np.minimum(np.arange(M), M - np.arange(M))
                mask = (idx[:, None] <= n) & (idx[None, :] <= n)
                p2 = np.where(mask, p1, p2)
                d = fj(w0, lev.lift(p1), Pj, Pm) - fj(w0, lev.lift(p2), Pj, Pm)
                acc.append(abs(d))
            means.append(float(np.mean(acc)))
            guard()
        means = np.array(means)
        slope = -np.polyfit(np.array(rs)[1:], np.log(means[1:]), 1)[0]
        print(f"j={j}: far difference n={rs} mean |d|={np.array2string(means, precision=3)}; "
              f"rate {slope:.3f}", flush=True)
        # control C-B2
        cb2 = fj(w0, lev.lift(psi), Pj, Pm) - fj(w0, lev.lift(psi.copy()), Pj, Pm)
        # B3, K1 form with pullback about the block's own centre
        kappa = 0.5
        Rs = []
        nmax = (M - 1) // 4
        for trial in range(4):
            p = rng.normal(size=(M, M))
            prev = None
            for n in range(0, nmax + 1):
                pb = pullback(p, n)
                fn = fj(w0, lev.lift(pb), Pj, Pm)
                idx = np.minimum(np.arange(M), M - np.arange(M))
                mask = (idx[:, None] <= n) & (idx[None, :] <= n)
                En = np.sum(p[mask] ** 2)
                if prev is not None:
                    Rs.append((n, abs(fn - prev) / (En * np.exp(-kappa * n))))
                prev = fn
        byn = {}
        for n, r in Rs:
            byn[n] = max(byn.get(n, 0.0), r)
        print(f"j={j}: K1 ratio by n {[(n, round(v, 5)) for n, v in sorted(byn.items())]}", flush=True)
        results[j] = dict(b1=b1, b2=slope, b4=b4, tot=tot, byn=byn, cb2=abs(cb2))
        guard()
    # two steps: the transported block response is Phi[P_1] - Phi[P_-1] on theta in H_3
    lev3 = Level(N, 27)
    M = lev3.M
    psi = rng.normal(size=(M, M))
    th = lev3.lift(psi)
    w = block_weight(N, 27)
    f0 = fj(w, th, P0, None)
    f1 = fj(w, th, P1, P0)
    print(f"two steps on H_3: level-0 piece {f0:+.4e}, level-1 piece {f1:+.4e}, sum {f0 + f1:+.4e}, "
          f"Phi[P_1] {phi(w, th, P1):+.4e}", flush=True)
    B1 = all(r["b1"] <= 1e-9 for r in results.values())
    B2 = all(r["b2"] >= 0.5 for r in results.values())
    B3 = True
    for r in results.values():
        small = max(v for n, v in r["byn"].items() if n <= 2)
        B3 = B3 and all(v <= 20 * small for v in r["byn"].values())
    B4 = all(r["b4"] <= 1e-9 for r in results.values())
    print("B1", "PASS" if B1 else "FAIL", "B2", "PASS" if B2 else "FAIL",
          "B3", "PASS" if B3 else "FAIL", "B4", "PASS" if B4 else "FAIL", flush=True)
    print("controls: C-B1", max(r["tot"] for r in results.values()), "C-B2",
          max(r["cb2"] for r in results.values()), flush=True)


# ---------------------------------------------------------------- Part A
def tent_row(sx, sy_period, y_index, x_node, s, Nx, Ny):
    """Sparse unit row of the level s plaquette with corner block (x_node, y_index)."""
    a = np.arange(2 * s - 1)
    t = (s - np.abs(a - (s - 1))) / s
    xs = (x_node * s + a) % Nx
    ys = (y_index * s + a) % Ny
    I = np.repeat(xs, a.size)
    J = np.tile(ys, a.size)
    V = np.outer(t, t).ravel()
    return I * Ny + J, V


def build(n, D, thick, L=3, ybl=1):
    """Rows for depth n. Layer of level l: half-width thick * s_(l+1) about the sheet, whole
    level-(l+1) blocks, so the clearance to the next layer is 2 thick / 3 level-(l+2) blocks.
    Returns csr C and dict of label -> row indices."""
    sn = L ** n
    Ny = sn * ybl
    half = thick * sn
    margin = 2 * sn
    centre_I = margin + half + 2 * sn
    centre_I = int(np.ceil(centre_I / sn)) * sn
    centre_O = centre_I + 2 * half + D * sn
    Nx = centre_O + half + 2 * sn + margin
    Nx = int(np.ceil(Nx / sn)) * sn
    labels = {}
    rows_i, rows_j, rows_v = [], [], []
    k = 0

    def add(idx, val, tag):
        nonlocal k
        val = val / np.linalg.norm(val)
        rows_i.append(np.full(idx.size, k))
        rows_j.append(idx)
        rows_v.append(val)
        labels.setdefault(tag, []).append(k)
        k += 1

    for X in range(Nx // sn):
        for Y in range(ybl):
            idx, val = tent_row(None, None, Y, X, sn, Nx, Ny)
            add(idx, val, ("W", n))
    for side, c in (("I", centre_I), ("O", centre_O)):
        for l in range(n):
            s = L ** l
            s1 = L ** (l + 1)
            lo, hi = c - thick * s1, c + thick * s1
            for X in range(lo // s, hi // s - 1):
                for Y in range(Ny // s):
                    idx, val = tent_row(None, None, Y, X, s, Nx, Ny)
                    add(idx, val, (side, l))
    C = sp.csr_matrix((np.concatenate(rows_v), (np.concatenate(rows_i), np.concatenate(rows_j))),
                      shape=(k, Nx * Ny))
    return C, labels, Nx, Ny


def analyse(n, D, thick, ybl=1):
    C, labels, Nx, Ny = build(n, D, thick, ybl=ybl)
    G = (C @ C.T).toarray()
    guard()
    ev, U = np.linalg.eigh(G)
    tol = 1e-10
    keep = ev > tol
    lam = ev[keep].min()
    nullity = int((~keep).sum())
    Gi = (U[:, keep] / ev[keep]) @ U[:, keep].T
    K = {}
    counts = {}
    for l in range(n):
        for lp in range(n):
            ri = labels[("I", l)]
            ro = labels[("O", lp)]
            K[(l, lp)] = np.linalg.norm(Gi[np.ix_(ri, ro)], 2)
            counts[l] = len(ri)
    guard()
    return lam, nullity, K, counts, G.shape[0], Nx, Ny


def part_a():
    thick = 3
    Ds = [2, 4, 6, 8]
    table = {}
    for n, D in [(2, 2), (2, 4), (3, 2), (3, 4)]:
        lam, nullity, K, counts, size, Nx, Ny = analyse(n, D, thick, ybl=3)
        print(f"extra ybl=3: n={n} D={D}: rows {size} fine {Nx}x{Ny} lam {lam:.5f} null {nullity} "
              f"K(top,top) {K[(n - 1, n - 1)]:.3e}", flush=True)
        guard()
    for n in (2, 3, 4):
        for D in Ds:
            t0 = time.time()
            lam, nullity, K, counts, size, Nx, Ny = analyse(n, D, thick, ybl=1)
            table[(n, D)] = (lam, K, counts)
            print(f"n={n} D={D}: rows {size} fine {Nx}x{Ny} lam {lam:.5f} null {nullity} "
                  f"K(top,top) {K[(n - 1, n - 1)]:.3e} t={time.time() - t0:.0f}s", flush=True)
            guard()
    A1 = all(table[(n, Ds[0])][0] >= 0.5 * table[(2, Ds[0])][0] for n in (2, 3, 4))
    A2 = True
    rates = {}
    for n in (2, 3, 4):
        for key in table[(n, Ds[0])][1]:
            ys = [table[(n, D)][1][key] for D in Ds]
            if min(ys) < 1e-13:
                continue  # below rounding; a faster channel than the fit can see
            r = -np.polyfit(Ds, np.log(ys), 1)[0]
            rates[(n,) + key] = r
            A2 = A2 and r >= 0.7
    print("rates (n, l, lp):", {k: round(v, 3) for k, v in rates.items()}, flush=True)
    amp = {}
    D0 = Ds[1]
    for n in (2, 3, 4):
        lam, K, counts = table[(n, D0)]
        top = counts[n - 1]
        amp[n] = max(np.sqrt(counts[l] * counts[lp]) * K[(l, lp)] / top for (l, lp) in K)
    A3 = all(amp[n] <= 3 * amp[2] for n in amp)
    print("amplitude by depth", {k: float(f"{v:.4e}") for k, v in amp.items()}, flush=True)
    print("A1", "PASS" if A1 else "FAIL", "A2", "PASS" if A2 else "FAIL", "A3", "PASS" if A3 else "FAIL", flush=True)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "ab"
    if "b" in which:
        part_b()
    if "a" in which:
        part_a()
    print("peak RSS bytes", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
