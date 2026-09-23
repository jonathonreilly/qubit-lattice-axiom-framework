#!/usr/bin/env python3
"""Supervisor control for block 95 (floating point and simulation; evidence, not proof).

Records on a 3D torus, one per site at a time; a tick rate at every site slaved to the records by block 53's law,
log w_z = 6 log(kappa) sum_(records r) G(z - r), G the zero-mean inverse of the lattice Laplacian; a record hops to an empty
neighbour at the rate w_x^a w_y^(1 - a) / 6 (a = 1: timed by the site it leaves; a = 1/2: by the bond; a = 0: by the site it enters).
Continuous-time simulation by the direct method; averages weight each visited state by its expected holding time.

W1: the kernel's far field: G(r) - G(r') against (1/r - 1/r')/(4 pi) along an axis and a body diagonal (64^3 torus).
W2: two records on 10^3, log(kappa) = -1: the law of their separation against the exact law of T2, exp(6 log(kappa)(1 - 2a) G(d)),
    for the three timings (total variation), the contact probability, and (a = 1) the mean displacement of a record per unit time
    as a function of the separation (T3: zero away from contact, -w/6 at contact).
W3: 96 records on 16^3 (density 3/128), timed by the site they leave, log(kappa) = -g, 20 million events: clustering against g; the structure factor
    at the smallest wave vector against the mean-field value (1 - rho)/(1 - 6 g rho (1 - rho)/E(k)) (a comparator), which fails
    at g = E(k_min)/(6 rho (1 - rho)); and an energy-entropy count for the collapse into one ball of 96 records.
W4: along the run at g = 0.8 (the two seeds of W3): the number of free records (six empty neighbours), the elapsed coordinate time,
    the total rate and the range of log w, every two million events.
"""
import math
import sys
import time

import numpy as np
from numba import njit


def zero_mean_kernel(L):
    k = 2 * np.pi * np.fft.fftfreq(L)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    E = 6 - 2 * (np.cos(kx) + np.cos(ky) + np.cos(kz))
    E[0, 0, 0] = 1.0
    inv = 1.0 / E
    inv[0, 0, 0] = 0.0
    return np.real(np.fft.ifftn(inv))


# ---------------------------------------------------------------------------------------------------- W2: two records
@njit(cache=True)
def two_records(G, L, lam, a, steps, seed, hist, disp, dispw):
    np.random.seed(seed)
    p = np.zeros((2, 3), dtype=np.int64)
    p[1, 0] = L // 2
    p[1, 1] = L // 2
    p[1, 2] = L // 2
    dirs = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
    rates = np.zeros((2, 6))
    burn = steps // 10
    for t in range(steps):
        # field at a site: 6 lam sum_j G(z - p_j)
        tot = 0.0
        for i in range(2):
            fx = 6 * lam * (G[0, 0, 0] + G[(p[i, 0] - p[1 - i, 0]) % L, (p[i, 1] - p[1 - i, 1]) % L, (p[i, 2] - p[1 - i, 2]) % L])
            for e in range(6):
                y0 = (p[i, 0] + dirs[e, 0]) % L
                y1 = (p[i, 1] + dirs[e, 1]) % L
                y2 = (p[i, 2] + dirs[e, 2]) % L
                if y0 == p[1 - i, 0] and y1 == p[1 - i, 1] and y2 == p[1 - i, 2]:
                    rates[i, e] = 0.0
                    continue
                fy = 6 * lam * (G[(y0 - p[0, 0]) % L, (y1 - p[0, 1]) % L, (y2 - p[0, 2]) % L]
                                + G[(y0 - p[1, 0]) % L, (y1 - p[1, 1]) % L, (y2 - p[1, 2]) % L])
                rates[i, e] = math.exp(a * fx + (1 - a) * fy) / 6
                tot += rates[i, e]
        h = 1.0 / tot
        if t >= burn:
            d0 = (p[1, 0] - p[0, 0]) % L
            d1 = (p[1, 1] - p[0, 1]) % L
            d2 = (p[1, 2] - p[0, 2]) % L
            hist[d0, d1, d2] += h
            # mean displacement per unit time of record 0 along the separation's x axis component (sign-folded)
            vx = 0.0
            for e in range(6):
                vx += rates[0, e] * dirs[e, 0]
            s = 1.0 if d0 <= L // 2 else -1.0
            disp[d0, d1, d2] += h * vx * s
            dispw[d0, d1, d2] += h
        u = np.random.random() * tot
        acc = 0.0
        chosen_i = 0
        chosen_e = 0
        found = False
        for i in range(2):
            for e in range(6):
                acc += rates[i, e]
                if acc >= u and not found:
                    chosen_i = i
                    chosen_e = e
                    found = True
        if not found:
            chosen_i = 1
            chosen_e = 5
            while rates[chosen_i, chosen_e] == 0.0:
                chosen_e -= 1
        for c in range(3):
            p[chosen_i, c] = (p[chosen_i, c] + dirs[chosen_e, c]) % L


# ---------------------------------------------------------------------------------------------------- W3: many records
@njit(cache=True)
def many_records(G, L, lam, n, steps, seed, every):
    np.random.seed(seed)
    V = L * L * L
    occ = -np.ones(V, dtype=np.int64)
    pos = np.zeros((n, 3), dtype=np.int64)
    i = 0
    while i < n:
        s = np.random.randint(V)
        if occ[s] < 0:
            occ[s] = i
            pos[i, 0] = s // (L * L)
            pos[i, 1] = (s // L) % L
            pos[i, 2] = s % L
            i += 1
    dirs = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
    logw = np.zeros(n)
    for i in range(n):
        acc = 0.0
        for j in range(n):
            acc += G[(pos[i, 0] - pos[j, 0]) % L, (pos[i, 1] - pos[j, 1]) % L, (pos[i, 2] - pos[j, 2]) % L]
        logw[i] = 6 * lam * acc
    empt = np.zeros(n, dtype=np.int64)
    R = np.zeros(n)
    burn = steps // 5
    sw = 0.0
    s_contact = 0.0
    s_sk = 0.0
    s_big = 0.0
    kmin = 2 * math.pi / L
    parent = np.zeros(n, dtype=np.int64)
    for t in range(steps):
        tot = 0.0
        for i in range(n):
            c = 0
            for e in range(6):
                s = ((pos[i, 0] + dirs[e, 0]) % L) * L * L + ((pos[i, 1] + dirs[e, 1]) % L) * L + (pos[i, 2] + dirs[e, 2]) % L
                if occ[s] < 0:
                    c += 1
            empt[i] = c
            R[i] = math.exp(logw[i]) * c / 6
            tot += R[i]
        if t >= burn and t % every == 0:
            h = 1.0 / tot
            sw += h
            con = 0
            for i in range(n):
                if empt[i] < 6:
                    con += 1
            s_contact += h * con / n
            sk = 0.0
            for ax in range(3):
                re = 0.0
                im = 0.0
                for i in range(n):
                    re += math.cos(kmin * pos[i, ax])
                    im += math.sin(kmin * pos[i, ax])
                sk += (re * re + im * im) / n
            s_sk += h * sk / 3
            # largest cluster (nearest-neighbour contact), union-find
            for i in range(n):
                parent[i] = i
            for i in range(n):
                for e in range(0, 6, 2):
                    s = ((pos[i, 0] + dirs[e, 0]) % L) * L * L + ((pos[i, 1] + dirs[e, 1]) % L) * L + (pos[i, 2] + dirs[e, 2]) % L
                    j = occ[s]
                    if j >= 0:
                        ri = i
                        while parent[ri] != ri:
                            ri = parent[ri]
                        rj = j
                        while parent[rj] != rj:
                            rj = parent[rj]
                        if ri != rj:
                            parent[ri] = rj
            big = 0
            for i in range(n):
                ri = i
                while parent[ri] != ri:
                    ri = parent[ri]
                parent[i] = ri
            for i in range(n):
                c = 0
                for j in range(n):
                    if parent[j] == i:
                        c += 1
                if c > big:
                    big = c
            s_big += h * big / n
        u = np.random.random() * tot
        acc = 0.0
        k = n - 1
        for i in range(n):
            acc += R[i]
            if acc >= u:
                k = i
                break
        while R[k] == 0.0:
            k -= 1
        # a uniformly chosen empty neighbour
        m = np.random.randint(empt[k])
        for e in range(6):
            s = ((pos[k, 0] + dirs[e, 0]) % L) * L * L + ((pos[k, 1] + dirs[e, 1]) % L) * L + (pos[k, 2] + dirs[e, 2]) % L
            if occ[s] < 0:
                if m == 0:
                    old = pos[k, 0] * L * L + pos[k, 1] * L + pos[k, 2]
                    x0, x1, x2 = pos[k, 0], pos[k, 1], pos[k, 2]
                    occ[old] = -1
                    occ[s] = k
                    pos[k, 0] = (pos[k, 0] + dirs[e, 0]) % L
                    pos[k, 1] = (pos[k, 1] + dirs[e, 1]) % L
                    pos[k, 2] = (pos[k, 2] + dirs[e, 2]) % L
                    for j in range(n):
                        if j == k:
                            continue
                        logw[j] += 6 * lam * (G[(pos[j, 0] - pos[k, 0]) % L, (pos[j, 1] - pos[k, 1]) % L, (pos[j, 2] - pos[k, 2]) % L]
                                              - G[(pos[j, 0] - x0) % L, (pos[j, 1] - x1) % L, (pos[j, 2] - x2) % L])
                    acc2 = 0.0
                    for j in range(n):
                        acc2 += G[(pos[k, 0] - pos[j, 0]) % L, (pos[k, 1] - pos[j, 1]) % L, (pos[k, 2] - pos[j, 2]) % L]
                    logw[k] = 6 * lam * acc2
                    break
                m -= 1
    return s_contact / sw, s_sk / sw, s_big / sw


# ---------------------------------------------------------------------------------------------------- W4: the condensed state along the run
@njit(cache=True)
def trace_condensation(G, L, lam, n, steps, seed, every, out):
    np.random.seed(seed)
    V = L*L*L
    occ = -np.ones(V, dtype=np.int64); pos = np.zeros((n,3), dtype=np.int64)
    i = 0
    while i < n:
        s = np.random.randint(V)
        if occ[s] < 0:
            occ[s] = i; pos[i,0] = s//(L*L); pos[i,1] = (s//L)%L; pos[i,2] = s%L; i += 1
    dirs = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
    logw = np.zeros(n)
    for i in range(n):
        acc = 0.0
        for j in range(n):
            acc += G[(pos[i,0]-pos[j,0])%L,(pos[i,1]-pos[j,1])%L,(pos[i,2]-pos[j,2])%L]
        logw[i] = 6*lam*acc
    empt = np.zeros(n, dtype=np.int64); R = np.zeros(n)
    tcoord = 0.0
    row = 0
    for t in range(steps):
        tot = 0.0
        for i in range(n):
            c = 0
            for e in range(6):
                s = ((pos[i,0]+dirs[e,0])%L)*L*L + ((pos[i,1]+dirs[e,1])%L)*L + (pos[i,2]+dirs[e,2])%L
                if occ[s] < 0:
                    c += 1
            empt[i] = c; R[i] = math.exp(logw[i])*c/6; tot += R[i]
        tcoord += 1.0/tot
        if t % every == 0:
            free = 0
            for i in range(n):
                if empt[i] == 6:
                    free += 1
            out[row,0] = t; out[row,1] = tcoord; out[row,2] = free; out[row,3] = tot
            mn = 1e300; mx = -1e300
            for i in range(n):
                if logw[i] < mn: mn = logw[i]
                if logw[i] > mx: mx = logw[i]
            out[row,4] = mn; out[row,5] = mx
            row += 1
        u = np.random.random()*tot; acc = 0.0; k = n-1
        for i in range(n):
            acc += R[i]
            if acc >= u:
                k = i; break
        while R[k] == 0.0:
            k -= 1
        m = np.random.randint(empt[k])
        for e in range(6):
            s = ((pos[k,0]+dirs[e,0])%L)*L*L + ((pos[k,1]+dirs[e,1])%L)*L + (pos[k,2]+dirs[e,2])%L
            if occ[s] < 0:
                if m == 0:
                    old = pos[k,0]*L*L + pos[k,1]*L + pos[k,2]
                    x0, x1, x2 = pos[k,0], pos[k,1], pos[k,2]
                    occ[old] = -1; occ[s] = k
                    pos[k,0] = (pos[k,0]+dirs[e,0])%L; pos[k,1] = (pos[k,1]+dirs[e,1])%L; pos[k,2] = (pos[k,2]+dirs[e,2])%L
                    for j in range(n):
                        if j == k: continue
                        logw[j] += 6*lam*(G[(pos[j,0]-pos[k,0])%L,(pos[j,1]-pos[k,1])%L,(pos[j,2]-pos[k,2])%L] - G[(pos[j,0]-x0)%L,(pos[j,1]-x1)%L,(pos[j,2]-x2)%L])
                    acc2 = 0.0
                    for j in range(n):
                        acc2 += G[(pos[k,0]-pos[j,0])%L,(pos[k,1]-pos[j,1])%L,(pos[k,2]-pos[j,2])%L]
                    logw[k] = 6*lam*acc2
                    break
                m -= 1
    return row



def main():
    t0 = time.time()
    scale = 100 if "--quick" in sys.argv else 1
    print("W1: far field of the zero-mean kernel on 64^3, torus background r^2/(6V) removed (expected slope 1/(4 pi) = %.5f)" % (1 / (4 * math.pi)))
    G64 = zero_mean_kernel(64)
    V64 = 64 ** 3
    for name, pts in (("axis", [(r, 0, 0) for r in (4, 6, 8, 12, 16)]), ("body diagonal", [(r, r, r) for r in (2, 3, 4, 6, 8)])):
        rs = [math.sqrt(sum(c * c for c in q)) for q in pts]
        gs = [G64[q] - rs[i] ** 2 / (6 * V64) for i, q in enumerate(pts)]
        slopes = ["%.5f" % ((gs[i] - gs[i + 1]) / (1 / rs[i] - 1 / rs[i + 1])) for i in range(len(pts) - 1)]
        print("  %-13s slopes of G against 1/r between successive points %s: %s" % (name, [round(r, 2) for r in rs], ", ".join(slopes)))

    L = 10
    G = zero_mean_kernel(L)
    lam = -1.0
    offs = [(i, j, k) for i in range(L) for j in range(L) for k in range(L) if (i, j, k) != (0, 0, 0)]
    contact = [(1, 0, 0), (L - 1, 0, 0), (0, 1, 0), (0, L - 1, 0), (0, 0, 1), (0, 0, L - 1)]
    print("W2: two records on 10^3, log(kappa) = -1; separation law against exp(6 log(kappa)(1 - 2a) G(d))")
    exact = {}
    for a in (1.0, 0.5, 0.0):
        e = np.array([math.exp(6 * lam * (1 - 2 * a) * G[o]) for o in offs])
        exact[a] = e / e.sum()
    print("  distances between the exact laws: TV(leave, bond) = %.4f, TV(enter, bond) = %.4f, TV(leave, enter) = %.4f"
          % (0.5 * np.abs(exact[1.0] - exact[0.5]).sum(), 0.5 * np.abs(exact[0.0] - exact[0.5]).sum(), 0.5 * np.abs(exact[1.0] - exact[0.0]).sum()))
    for a, name in ((1.0, "site it leaves (a = 1)"), (0.5, "bond (a = 1/2)"), (0.0, "site it enters (a = 0)")):
        hist = np.zeros((L, L, L))
        disp = np.zeros((L, L, L))
        dispw = np.zeros((L, L, L))
        two_records(G, L, lam, a, 40_000_000 // scale, 7, hist, disp, dispw)
        emp = np.array([hist[o] for o in offs])
        emp /= emp.sum()
        ex = np.array([math.exp(6 * lam * (1 - 2 * a) * G[o]) for o in offs])
        ex /= ex.sum()
        tv = 0.5 * np.abs(emp - ex).sum()
        ci = [offs.index(c) for c in contact]
        print("  timed by the %-22s TV(empirical, exact) = %.4f; P(contact) empirical %.4f, exact %.4f, uniform %.4f"
              % (name, tv, emp[ci].sum(), ex[ci].sum(), 6 / len(offs)))
        if a == 1.0:
            rows = []
            for d in ((1, 0, 0), (2, 0, 0), (3, 0, 0), (5, 0, 0), (2, 1, 0), (3, 2, 1)):
                v = disp[d] / dispw[d]
                wd = math.exp(6 * lam * (G[0, 0, 0] + G[d]))
                rows.append("%s: %+.4f (w/6 = %.4f)" % (d, v, wd / 6))
            print("    mean x-displacement per unit time of the record at the origin, sign towards the other record: " + "; ".join(rows))
    print("W3: 96 records on 16^3 (rho = 3/128), timed by the site they leave, log(kappa) = -g; 20 million events from a random start, two seeds")
    L = 16
    G = zero_mean_kernel(L)
    n = 96
    rho = n / L ** 3
    Emin = 2 - 2 * math.cos(2 * math.pi / L)
    print("  mean-field comparator: uniform gas unstable above g = E(k_min)/(6 rho (1 - rho)) = %.3f" % (Emin / (6 * rho * (1 - rho))))
    pts = sorted(((i, j, k) for i in range(-8, 8) for j in range(-8, 8) for k in range(-8, 8)), key=lambda q: (q[0] ** 2 + q[1] ** 2 + q[2] ** 2, q))[:n]
    spair = sum(G[tuple((pts[u][c] - pts[v][c]) % L for c in range(3))] for u in range(n) for v in range(u + 1, n))
    logc = math.lgamma(L ** 3 + 1) - math.lgamma(n + 1) - math.lgamma(L ** 3 - n + 1)
    print("  energy-entropy count: a ball of %d records has sum_pairs G = %.2f; log C(%d, %d) - log V = %.1f; collapse into the ball pays from g = %.3f"
          % (n, spair, L ** 3, n, logc - math.log(L ** 3), (logc - math.log(L ** 3)) / (6 * spair)))
    for g in (0.0, 0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0):
        vals = []
        for seed in (11, 12):
            vals.append(many_records(G, L, -g, n, 20_000_000 // scale, seed, 50))
        vals = np.array(vals)
        mf = (1 - rho) / (1 - 6 * g * rho * (1 - rho) / Emin) if 6 * g * rho * (1 - rho) < Emin else float("nan")
        print("  g = %.1f: records touching another %.3f / %.3f; largest cluster share %.3f / %.3f; S(k_min) %.2f / %.2f (mean field %.2f; nan = beyond its threshold)"
              % (g, vals[0, 0], vals[1, 0], vals[0, 2], vals[1, 2], vals[0, 1], vals[1, 1], mf))
        sys.stdout.flush()
    print("W4: along the run at g = 0.8, every two million events (seeds 11 and 12, as in W3)")
    for seed in (11, 12):
        steps = 20_000_000 // scale
        every = max(1, 2_000_000 // scale)
        out = np.zeros((steps // every + 1, 6))
        r = trace_condensation(G, L, -0.8, n, steps, seed, every, out)
        print("  seed %d" % seed)
        for row in out[:r]:
            print("    event %9d  coordinate time %.3e  free records %3d  total rate %.3e  log w from %.1f to %.1f" % tuple(row))
    print("elapsed %.0f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
