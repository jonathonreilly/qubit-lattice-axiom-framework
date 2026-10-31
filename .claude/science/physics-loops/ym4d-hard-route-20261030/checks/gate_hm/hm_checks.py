#!/usr/bin/env python3
"""Hostile checks for Theorem Z at 3b7fd4e57. Criteria are in theorem-z-3b7fd4e57.md, written first.

N1: 2D U(1) counterexample shape for the class path lemma (item (r)).
N2: Dirichlet face constant C_bd, 2D U(1), one level, flat parents, whole-block band.
N3: comb configuration against Step 2 of Theorem Z.
N4: arithmetic of Step 6: hops available against hops the surface count needs.
"""
import math
import sys
from collections import deque

import numpy as np
from scipy.optimize import linprog


def n1(T=0.05):
    N = int(math.ceil(math.sqrt(2 * math.pi / T)))
    theta = 2 * math.pi / N ** 2
    # Links on an N x N patch: A_x(x, y) = 0, A_y(x, y) = theta * x for x < N, in a gauge with
    # bottom, left trivial. Plaquette angle theta everywhere. The right edge has A_y = theta N per
    # link, i.e. holonomy 2 pi over N links only after a gauge transformation by exp(i 2 pi y / N),
    # which is trivial at y = 0 and y = N, so all boundary links are made trivial.
    Ax = np.zeros((N, N + 1))
    Ay = np.zeros((N + 1, N))
    for x in range(N + 1):
        for y in range(N):
            Ay[x, y] = theta * x
    # gauge transform on x = N column and interior so that right column links vanish:
    # chi(x, y) = -theta * y * x, which gives A_y -> 0 at no x except via A_x -> -theta y.
    chi = np.array([[-theta * x * y for y in range(N + 1)] for x in range(N + 1)])
    Ax2 = np.zeros_like(Ax)
    Ay2 = np.zeros_like(Ay)
    for x in range(N):
        for y in range(N + 1):
            Ax2[x, y] = Ax[x, y] + chi[x + 1, y] - chi[x, y]
    for x in range(N + 1):
        for y in range(N):
            Ay2[x, y] = Ay[x, y] + chi[x, y + 1] - chi[x, y]
    # After chi the top row has A_x = -theta N per link, holonomy -2 pi. A gauge transformation of
    # the top row of sites alone, chi2(x, N) = theta N x, makes those links trivial; it equals
    # 2 pi = identity at x = N, so the corners stay fixed and the compact field is unchanged there.
    for x in range(N):
        Ax2[x, N] += theta * N
    for x in range(N + 1):
        Ay2[x, N - 1] += theta * N * x
    wrap = lambda a: (a + math.pi) % (2 * math.pi) - math.pi
    bnd = [wrap(Ax2[x, 0]) for x in range(N)] + [wrap(Ax2[x, N]) for x in range(N)]
    bnd += [wrap(Ay2[0, y]) for y in range(N)] + [wrap(Ay2[N, y]) for y in range(N)]
    plaq = np.zeros((N, N))
    for x in range(N):
        for y in range(N):
            plaq[x, y] = wrap(Ax2[x, y] + Ay2[x + 1, y] - Ax2[x, y + 1] - Ay2[x, y])
    ok = (np.abs(bnd).max() < 1e-12 and np.abs(plaq).max() <= T + 1e-12
          and abs(plaq.sum() - 2 * math.pi) < 1e-9)
    print(f"N1 N={N} max_boundary_link={np.abs(bnd).max():.2e} max_plaq={np.abs(plaq).max():.5f} "
          f"T={T} sum_angles/2pi={plaq.sum() / (2 * math.pi):.6f} -> {'PASS' if ok else 'FAIL'}")
    return ok


def build(L, Nc, wb):
    N = L * Nc
    idx = lambda x, y, m: 2 * ((x % N) * N + (y % N)) + m
    nl = 2 * N * N

    def plaq(x, y):
        v = np.zeros(nl)
        v[idx(x, y, 0)] += 1
        v[idx(x + 1, y, 1)] += 1
        v[idx(x, y + 1, 0)] -= 1
        v[idx(x, y, 1)] -= 1
        return v

    D = np.array([plaq(x, y) for x in range(N) for y in range(N)])

    def path(a, b):
        """Axis path a -> b, first coordinate first, shortest displacement inside a block."""
        v = np.zeros(nl)
        x, y = a
        dx, dy = b[0] - a[0], b[1] - a[1]
        s = 1 if dx >= 0 else -1
        for _ in range(abs(dx)):
            if s > 0:
                v[idx(x, y, 0)] += 1
            else:
                v[idx(x - 1, y, 0)] -= 1
            x += s
        s = 1 if dy >= 0 else -1
        for _ in range(abs(dy)):
            if s > 0:
                v[idx(x, y, 1)] += 1
            else:
                v[idx(x, y - 1, 1)] -= 1
            y += s
        return v

    h = (L - 1) // 2
    rows = []
    for cx in range(Nc):
        for cy in range(Nc):
            c = (L * cx + h, L * cy + h)
            for m in (0, 1):
                e = (L, 0) if m == 0 else (0, L)
                row = np.zeros(nl)
                for ox in range(-h, h + 1):
                    for oy in range(-h, h + 1):
                        x = (c[0] + ox, c[1] + oy)
                        row += path(c, x)
                        px, py = x
                        for t in range(L):
                            row[idx(px, py, m)] += 1
                            if m == 0:
                                px += 1
                            else:
                                py += 1
                        cp = (c[0] + e[0], c[1] + e[1])
                        xp = (x[0] + e[0], x[1] + e[1])
                        row -= path(cp, xp)
                rows.append(row / L ** 2)
    Q = np.array(rows)
    band_w = wb * L
    in_band = lambda x: (x % N) < band_w
    frozen = np.zeros(nl, bool)
    for x in range(N):
        for y in range(N):
            if in_band(x) and in_band(x + 1):
                frozen[idx(x, y, 0)] = True
            if in_band(x):
                frozen[idx(x, y, 1)] = True
    pb = np.array([in_band(x) and in_band(x + 1) for x in range(N) for y in range(N)])
    px = np.array([x for x in range(N) for y in range(N)])
    py = np.array([y for x in range(N) for y in range(N)])
    return N, D, Q, frozen, pb, px, py, band_w


def n2(L, Nc, wb=2):
    N, D, Q, frozen, pb, px, py, bw = build(L, Nc, wb)
    F = ~frozen
    Df, Db = D[:, F], D[:, frozen]
    Qf, Qb = Q[:, F], Q[:, frozen]
    mixed = np.abs(Qf).sum(axis=1) > 1e-14
    Qm_f, Qm_b = Qf[mixed], Qb[mixed]
    Qff = Qb[~mixed]
    nf = Df.shape[1]
    K = np.block([[Df.T @ Df, Qm_f.T], [Qm_f, np.zeros((Qm_f.shape[0], Qm_f.shape[0]))]])
    rhs = np.vstack([-Df.T @ Db, -Qm_b])
    Kp = np.linalg.pinv(K, rcond=1e-10)
    X = (Kp @ rhs)[:nf]
    G = Df @ X + Db  # angle of every plaquette as a linear function of the band data
    res = np.abs(Qm_f @ X + Qm_b).max()
    print(f"N2 L={L} Nc={Nc} band={bw} links={D.shape[1]} free={nf} mixed_rows={mixed.sum()} "
          f"frozen_only_rows={(~mixed).sum()} constraint_residual={res:.1e}")
    Dband = Db[pb]
    A_ub = np.vstack([Dband, -Dband])
    b_ub = np.ones(A_ub.shape[0])
    best = {}
    # Free plaquettes in columns next to the band, over one block of rows on each side.
    for side, cols in (("right", range(bw - 1, bw + 2 * L)), ("left", range(N - 2 * L - 1, N))):
        for x in cols:
            for y in range(L):
                k = x * N + y
                if pb[k]:
                    continue
                res_lp = linprog(-G[k], A_ub=A_ub, b_ub=b_ub,
                                 A_eq=Qff if Qff.shape[0] else None,
                                 b_eq=np.zeros(Qff.shape[0]) if Qff.shape[0] else None,
                                 bounds=[(-1e3, 1e3)] * Db.shape[1], method="highs")
                if res_lp.status != 0:
                    print("  LP status", res_lp.status, "at", x, y)
                    continue
                dist = (x - (bw - 1)) if side == "right" else (N - 1 - x)
                val = -res_lp.fun
                if val > best.get((side, dist), (-1,))[0]:
                    best[(side, dist)] = (val, x, y)
    for key in sorted(best):
        print(f"  side={key[0]} columns_from_band={key[1]} C={best[key][0]:.4f} at plaquette {best[key][1:]}")
    Cbd = max(v[0] for v in best.values())
    print(f"N2 L={L} C_bd={Cbd:.4f} -> {'above 1' if Cbd > 1 else 'at most 1'}; "
          f"{'at least 2' if Cbd >= 2 else 'below 2'}")
    return Cbd, res


def n3(L=5, W=40, rS=1):
    t = 2 * W // L + 2 * rS  # thickness per line 19 of the note, read in level-1 cells
    R = t  # a closed layer of thickness t fits between rough cells only at spacing above t
    M = 10 * t  # tangential cells, periodic
    tip = W // 2
    rough = np.zeros((W, M), bool)
    for th in range(0, M, t - 1):
        rough[:tip, th] = True
    # (a) no chain at range R crosses annulus_1: BFS over rough cells from r = 0.
    seen = np.zeros_like(rough)
    q = deque()
    for th in range(M):
        if rough[0, th]:
            seen[0, th] = True
            q.append((0, th))
    while q:
        r, th = q.popleft()
        for dr in range(-R, R + 1):
            for dth in range(-R, R + 1):
                r2, th2 = r + dr, (th + dth) % M
                if 0 <= r2 < W and rough[r2, th2] and not seen[r2, th2]:
                    seen[r2, th2] = True
                    q.append((r2, th2))
    crossed = seen[W - 1].any()
    reach = np.where(seen.any(axis=1))[0].max()
    # (b) allowed centres for a closed layer of thickness t at level 1: radial positions g with a
    # block [g, g + t) free of rough cells, tangentially wide t; a closed layer must wind around th.
    ok = np.zeros((W, M), bool)
    for g in range(0, W - t + 1):
        for th in range(M):
            cols = [(th + i) % M for i in range(t)]
            ok[g, th] = not rough[g:g + t][:, cols].any()
    gmin_closed = None
    for g0 in range(0, W - t + 1):
        # winding path through ok cells with inner radius at least g0: BFS across th, unwrapped
        start = [(g, 0) for g in range(g0, W - t + 1) if ok[g, 0]]
        found = False
        seen2 = set(start)
        q = deque(start)
        while q and not found:
            g, u = q.popleft()
            if u == M:
                found = True
                break
            for dg in (-1, 0, 1):
                g2 = g + dg
                if g0 <= g2 <= W - t and ok[g2, (u + 1) % M] and (g2, u + 1) not in seen2:
                    seen2.add((g2, u + 1))
                    q.append((g2, u + 1))
        if found and gmin_closed is None:
            gmin_closed = g0
    # A closed layer exists with inner radius >= gmin_closed only if the smallest g with a winding
    # path needs g >= tip. Report the smallest inner radius any cell of a winding layer can take.
    all_g = None
    for g0 in range(W - t, -1, -1):
        start = [(g, 0) for g in range(g0, W - t + 1) if ok[g, 0]]
        seen2 = set(start)
        q = deque(start)
        found = False
        while q:
            g, u = q.popleft()
            if u == M:
                found = True
                break
            for dg in (-1, 0, 1):
                g2 = g + dg
                if g0 <= g2 <= W - t and ok[g2, (u + 1) % M] and (g2, u + 1) not in seen2:
                    seen2.add((g2, u + 1))
                    q.append((g2, u + 1))
        if found:
            all_g = g0
        else:
            break
    # (c) nested level-0 layer: annulus_0 is r0 in [0, W), and the layer must lie in the shadow of a
    # level-1 layer at clearance L * rS: r0 >= L * (g + rS).
    level0_room = None if all_g is None else W - L * (all_g + rS)
    family = level0_room is not None and level0_room >= t
    ok_all = (not crossed) and (not family) and all_g is not None
    print(f"N3 L={L} W={W} t={t} R={R} tip={tip}: chain_crosses_annulus_1={crossed} (reach {reach}); "
          f"smallest_inner_radius_of_a_closed_level1_layer={all_g}; "
          f"level0_room_in_annulus_0={level0_room} (needs {t}); family_exists={family} "
          f"-> {'PASS' if ok_all else 'FAIL'}")
    return ok_all


def n4():
    # Constants as generous as the note allows: c = (1/16)/C_T with C_T = 32, a_* = 1.
    c = 1 / (16 * 32)
    print("N4 L  T^2  hops_available(<=L/2)  hops_needed=3 log L/(c c0 T^2)  ratio  m0/x_l")
    for L in (17, 101, 1001):
        T2 = 1 / L ** 4
        c0 = (11 * 4 / (12 * math.pi ** 2)) * math.log(L)
        H_avail = L / 2
        H_need = 3 * math.log(L) / (c * c0 * T2)
        # With H_avail hops, the count L^(3 m) exp(-c (x_l + c0 m) T2 H) exceeds 1 once m > m0.
        slope = 3 * math.log(L) - c * c0 * T2 * H_avail
        m0_per_x = c * T2 * H_avail / slope
        print(f"   {L:5d} {T2:.2e} {H_avail:8.1f} {H_need:.3e} {H_need / H_avail:.3e} {m0_per_x:.3e}")


if __name__ == "__main__":
    which = sys.argv[1:] or ["n1", "n3", "n4", "n2"]
    if "n1" in which:
        n1()
    if "n3" in which:
        n3()
    if "n4" in which:
        n4()
    if "n2" in which:
        n2(3, 5)
        n2(5, 4)
