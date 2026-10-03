#!/usr/bin/env python3
"""A15 tasks 1 (2D) and 4: phase walls in the A11 4-sub-step swap cycle (full transfers), supplied 2D toy.

A11 cycle: A sites (x+y even). At effective sub-step j a site's partner is x + d_j (A site) or x - d_j (B site),
d = (+x, +y, -x, -y). Full transfers: one cycle is a permutation of site contents.
Rigid local clocks: site x uses j = t + phi(x) (mod 4) at global sub-step t.  Rules:
  H  a pair acts iff both sites name each other
  K  candidate pairs = named by >= 1 site; candidates sharing a site with another candidate are skipped
Measured per cycle: whether any content crosses between regions; the one-cycle current through horizontal cuts,
column by column, near each wall (positive = toward +y), and orbit structure around an island.
Self-timed local clocks (handshake-wait): counters advance only when a pair fires; check deadlock / healing."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np

D = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def partner(x, y, j, L):
    dx, dy = D[j % 4]
    if (x + y) % 2 == 0:
        return ((x + dx) % L, (y + dy) % L)
    return ((x - dx) % L, (y - dy) % L)

def substep_pairs(L, jfield, rule):
    sel = {}
    for x in range(L):
        for y in range(L):
            sel[(x, y)] = partner(x, y, jfield[x, y], L)
    mutual, onesided = set(), set()
    for a, b in sel.items():
        e = tuple(sorted((a, b)))
        if sel[b] == a:
            mutual.add(e)
        else:
            onesided.add(e)
    if rule == 'H':
        return mutual
    cand = mutual | onesided
    cnt = {}
    for a, b in cand:
        cnt[a] = cnt.get(a, 0) + 1
        cnt[b] = cnt.get(b, 0) + 1
    return {e for e in cand if cnt[e[0]] == 1 and cnt[e[1]] == 1}

def cycle_perm(L, phi, rule, t0=0):
    """item (start site) -> site after one cycle (4 sub-steps), with unwrapped displacement."""
    where = {(x, y): (x, y) for x in range(L) for y in range(L)}      # site -> item
    disp = {(x, y): (0, 0) for x in range(L) for y in range(L)}       # item -> unwrapped displacement
    for t in range(t0, t0 + 4):
        pairs = substep_pairs(L, (t + phi) % 4, rule)
        new = dict(where)
        for a, b in pairs:
            ia, ib = where[a], where[b]
            new[a], new[b] = ib, ia
            # unwrapped step vector from a to b
            vx = ((b[0] - a[0] + L // 2) % L) - L // 2
            vy = ((b[1] - a[1] + L // 2) % L) - L // 2
            disp[ia] = (disp[ia][0] + vx, disp[ia][1] + vy)
            disp[ib] = (disp[ib][0] - vx, disp[ib][1] - vy)
        where = new
    final = {item: site for site, item in where.items()}
    return final, disp

def column_current(L, disp, yc):
    """net number of items whose one-cycle chord crosses the line y = yc + 1/2 upward, per start column."""
    cur = np.zeros(L, int)
    for (x, y), (dx, dy) in disp.items():
        if dy == 0:
            continue
        # count crossings of lines y = yc + 1/2 + m L by the vertical chord from y to y + dy
        lo, hi = (y, y + dy) if dy > 0 else (y + dy, y)
        n = 0
        for m in range(-2, 3):
            if lo <= yc + m * L < hi:
                n += 1
        cur[x] += n if dy > 0 else -n
    return cur

def strip_test(L, x0, x1, k, rule):
    phi = np.zeros((L, L), int)
    phi[x0:x1, :] = k
    final, disp = cycle_perm(L, phi, rule)
    inR = lambda s: x0 <= s[0] < x1
    cross = sum(1 for item, site in final.items() if inR(item) != inR(site))
    moved = sum(1 for item, site in final.items() if item != site)
    curs = np.array([column_current(L, disp, yc) for yc in range(L)])   # per cut row, per column
    mean_cur = curs.mean(axis=0)
    return cross, moved, mean_cur, curs

def island_test(L, s, k, rule):
    phi = np.zeros((L, L), int)
    c0 = L // 2 - s // 2
    phi[c0:c0 + s, c0:c0 + s] = k
    final, disp = cycle_perm(L, phi, rule)
    inI = lambda p: c0 <= p[0] < c0 + s and c0 <= p[1] < c0 + s
    cross = sum(1 for item, site in final.items() if inI(item) != inI(site))
    moved = [it for it, st in final.items() if it != st]
    # orbits and winding about the island centre
    cen = (c0 + (s - 1) / 2, c0 + (s - 1) / 2)
    seen, orbs = set(), []
    for it in moved:
        if it in seen:
            continue
        orb, cur = [], it
        while cur not in seen:
            seen.add(cur); orb.append(cur); cur = final[cur]
        wsum = 0.0
        for p in orb:
            q = final[p]
            a0 = np.arctan2(p[1] - cen[1], p[0] - cen[0]); a1 = np.arctan2(q[1] - cen[1], q[0] - cen[0])
            wsum += (a1 - a0 + np.pi) % (2 * np.pi) - np.pi
        orbs.append((len(orb), 'in' if inI(orb[0]) else 'out', round(wsum / (2 * np.pi), 6)))
    return cross, len(moved), sorted(orbs)

if __name__ == '__main__':
    L = 16
    print("== rigid clocks: vertical strip x in [4,12) at offset k, torus L=16; walls at x=3|4 and x=11|12 ==")
    for rule in ('H', 'K'):
        for k in (0, 1, 2, 3):
            cross, moved, mc, curs = strip_test(L, 4, 12, k, rule)
            print(" rule %s k=%d: items crossing between regions per cycle = %d; moved items = %d" % (rule, k, cross, moved))
            print("    mean current per column (cols 0..15): " + " ".join("%+.2f" % v for v in mc))
            w1 = mc[1:7].sum(); w2 = mc[9:15].sum()
            print("    summed over window around wall1 (cols 1-6): %+.3f, wall2 (cols 9-14): %+.3f; L-side/R-side wall1: %+.3f / %+.3f"
                  % (w1, w2, mc[1:4].sum(), mc[4:7].sum()))
    print("== rigid clocks: square island of offset k inside offset 0, torus L=24 ==")
    for rule in ('H', 'K'):
        for s in (2, 4, 6):
            for k in (1, 2, 3):
                cross, nmoved, orbs = island_test(24, s, k, rule)
                print(" rule %s s=%d k=%d: crossing=%d moved=%d orbits (length, side, winding)=%s" % (rule, s, k, cross, nmoved, orbs))
