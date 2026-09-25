#!/usr/bin/env python3
"""Records forming at empty sites under block 95's clock field, and hopping: does the lattice fill from the voids and jam?
Worked computation, run 2 of 2.  Floating point (numba kinetic Monte Carlo; exact event selection, no time step).

As landed on main, block 95 (#8860): torus field u_z = 6 lambda sum_{r in C} G(z - r), G the mean-zero inverse of Delta = 6I - Adj
(Delta G = delta_0 - 1/V), lambda = log kappa; hops at a = 1 with W = 1 run at w_x/12 there (heat-bath h = 1/2); formation is not in its
scope.  This task supplies: formation at every empty site at rate z w_x, hops of a record at w_x/6 to each empty neighbour (the landed
w_x/12 is the same process with z doubled), log kappa = -g.  16^3 torus from empty; z = 1e-3, 1e-4; g = 0.5, 1.
Measured against time: record count, largest cluster share (6-neighbour clusters), and for formation events the fraction within graph
distance 2 of the largest cluster, against the fraction of EMPTY sites within that distance at the same moment (enrichment < 1 means
formation avoids the cluster).
"""
import sys, time
import numpy as np
from numba import njit

L = 16; V = L ** 3
def green():
    k = 2 * np.pi * np.arange(L) / L
    E = 6 - 2 * (np.cos(k)[:, None, None] + np.cos(k)[None, :, None] + np.cos(k)[None, None, :])
    E[0, 0, 0] = np.inf
    return np.real(np.fft.ifftn(1.0 / E)).ravel()          # mean-zero, Delta G = delta_0 - 1/V
G = green()
coords = np.array([(x, y, z) for x in range(L) for y in range(L) for z in range(L)], np.int64)
def sid(x, y, z): return ((x % L) * L + (y % L)) * L + (z % L)
NB = np.array([[sid(x + dx, y + dy, z + dz) for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))] for x, y, z in coords], np.int64)
DISP = np.zeros((V, V), np.int64) if False else None
def disp_index(i, j):
    a = coords[i]; b = coords[j]; d = (a - b) % L; return (d[0] * L + d[1]) * L + d[2]
# displacement table as arrays for numba: dsite[i, j] would be V^2 = 16.7M int64 (134 MB); instead compute on the fly from coordinates
CX, CY, CZ = coords[:, 0].copy(), coords[:, 1].copy(), coords[:, 2].copy()

@njit(cache=True)
def run(seed, zrate, g, maxev, CX, CY, CZ, NB, G, marks):
    np.random.seed(seed)
    V = CX.shape[0]; L = 16
    occ = np.zeros(V, np.bool_)
    w = np.ones(V)                                  # w = exp(u), u = -6 g sum G(z - r); starts at 1 (no records)
    EG = np.exp(-6.0 * g * G)                       # multiplicative factor for adding a record at displacement d
    nrec = 0; t = 0.0
    out_t = np.zeros(marks.shape[0]); out_n = np.zeros(marks.shape[0], np.int64); out_lc = np.zeros(marks.shape[0])
    out_fr = np.zeros(marks.shape[0]); out_null = np.zeros(marks.shape[0]); mk = 0
    lab = np.zeros(V, np.int64); near = np.zeros(V, np.bool_); stack = np.zeros(V, np.int64); dist = np.zeros(V, np.int64)
    nf_win = 0; nf_near = 0; null_acc = 0.0; nform = 0; ev = 0; lcshare = 0.0
    def_dummy = 0
    while ev < maxev and nrec < V and mk < marks.shape[0]:
        # rates
        R = 0.0
        for x in range(V):
            if occ[x]:
                ne = 0
                for k in range(6):
                    if not occ[NB[x, k]]: ne += 1
                R += w[x] * ne / 6.0
            else:
                R += zrate * w[x]
        t += -np.log(np.random.random()) / R
        u = np.random.random() * R; acc = 0.0; chosen = -1; kind = 0
        for x in range(V):
            if occ[x]:
                for k in range(6):
                    y = NB[x, k]
                    if not occ[y]:
                        acc += w[x] / 6.0
                        if acc >= u:
                            chosen = x; kind = k + 1; break
                if chosen >= 0: break
            else:
                acc += zrate * w[x]
                if acc >= u:
                    chosen = x; kind = 0; break
        if chosen < 0: chosen = V - 1; kind = 0
        ev += 1
        if kind == 0:
            if occ[chosen]: continue
            # every 32 formations refresh the largest cluster and its distance-2 neighbourhood
            if nform % 32 == 0:
                for i in range(V): lab[i] = -1
                best = -1; bestsize = 0; cur = 0
                for s0 in range(V):
                    if occ[s0] and lab[s0] < 0:
                        sp = 0; stack[sp] = s0; sp += 1; lab[s0] = cur; size = 0
                        while sp > 0:
                            sp -= 1; a = stack[sp]; size += 1
                            for k in range(6):
                                b = NB[a, k]
                                if occ[b] and lab[b] < 0:
                                    lab[b] = cur; stack[sp] = b; sp += 1
                        if size > bestsize: bestsize = size; best = cur
                        cur += 1
                for i in range(V):
                    near[i] = False; dist[i] = 99
                if best >= 0:
                    sp = 0
                    for i in range(V):
                        if lab[i] == best: dist[i] = 0; stack[sp] = i; sp += 1
                    head = 0
                    while head < sp:
                        a = stack[head]; head += 1
                        if dist[a] >= 2: continue
                        for k in range(6):
                            b = NB[a, k]
                            if dist[b] > dist[a] + 1:
                                dist[b] = dist[a] + 1; stack[sp] = b; sp += 1
                    for i in range(V): near[i] = dist[i] <= 2
                lcshare = bestsize / max(nrec, 1)
            # null: fraction of empty sites within distance 2 at this moment
            ne_all = 0; ne_near = 0
            for i in range(V):
                if not occ[i]:
                    ne_all += 1
                    if near[i]: ne_near += 1
            null_acc += ne_near / max(ne_all, 1)
            nf_win += 1
            if near[chosen]: nf_near += 1
            occ[chosen] = True; nrec += 1; nform += 1
            cx, cy, cz = CX[chosen], CY[chosen], CZ[chosen]
            for i in range(V):
                d = (((CX[i] - cx) % L) * L + ((CY[i] - cy) % L)) * L + ((CZ[i] - cz) % L)
                w[i] *= EG[d]
            if nrec >= marks[mk]:
                out_t[mk] = t; out_n[mk] = nrec; out_lc[mk] = lcshare
                out_fr[mk] = nf_near / max(nf_win, 1); out_null[mk] = null_acc / max(nf_win, 1)
                nf_win = 0; nf_near = 0; null_acc = 0.0; mk += 1
        else:
            x = chosen; y = NB[x, kind - 1]
            occ[x] = False; occ[y] = True
            ax, ay, az = CX[x], CY[x], CZ[x]; bx, by, bz = CX[y], CY[y], CZ[y]
            for i in range(V):
                d1 = (((CX[i] - ax) % L) * L + ((CY[i] - ay) % L)) * L + ((CZ[i] - az) % L)
                d2 = (((CX[i] - bx) % L) * L + ((CY[i] - by) % L)) * L + ((CZ[i] - bz) % L)
                w[i] *= EG[d2] / EG[d1]
    return out_t[:mk], out_n[:mk], out_lc[:mk], out_fr[:mk], out_null[:mk], nrec, ev, t

marks = np.array([int(V * f) for f in (0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 1.0)], np.int64)
print("N 16^3 torus from empty; formation z w_x, hops w_x/6 per empty neighbour, log kappa = -g; checkpoints at filling fractions %s" % (list(np.round(marks / V, 2)),), flush=True)
MAXEV = int(sys.argv[1]) if len(sys.argv) > 1 else 60_000_000
summary = []; hits = []
for g in (0.5, 1.0):
    for zr in (1e-3, 1e-4):
        t0 = time.time()
        ts, ns, lc, fr, nul, nrec, ev, tf = run(7, zr, g, MAXEV, CX, CY, CZ, NB, G, marks)
        rows = ["%.2f: t=%.3g lc=%.2f near=%.2f/null %.2f" % (n / V, tt, l, f, nn) for tt, n, l, f, nn in zip(ts, ns, lc, fr, nul)]
        jam = nrec == V
        print("N g=%.1f z=%.0e: %s | final count %d/%d (%s), %d events, %.0f s" % (g, zr, " | ".join(rows), nrec, V, "jammed" if jam else "NOT jammed within the event cap", ev, time.time() - t0), flush=True)
        # enrichment only where it is informative: checkpoints whose null fraction is below 0.9 (before the one cluster is everywhere)
        enrich = [f / nn for f, nn in zip(fr, nul) if 0.02 <= nn < 0.9]
        mean_en = float(np.mean(enrich)) if enrich else float('nan')
        summary.append((g, zr, jam, mean_en, float(max(lc)) if len(lc) else 0.0, nrec))
        if enrich and mean_en > 1.0: hits.append("g=%.1f z=%.0e: formation enriched near the largest cluster (mean %.2f)" % (g, zr, mean_en))
        if not jam and ev < MAXEV: hits.append("g=%.1f z=%.0e: count saturated at %d < %d" % (g, zr, nrec, V))
print()
print("SUMMARY: formation under the clock field on 16^3: " + "; ".join("g=%.1f z=%.0e %s, enrichment of formation within distance 2 of the largest cluster (null < 0.9) %.2f, largest cluster share up to %.2f"
      % (g, zr, ("jams" if j else "not jammed within cap (%d/4096)" % n), e, m) for g, zr, j, e, m, n in summary))
if hits:
    print("HIT: " + "; ".join(hits))
