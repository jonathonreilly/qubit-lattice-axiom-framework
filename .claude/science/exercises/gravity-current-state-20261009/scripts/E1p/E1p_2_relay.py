"""E1' (b) compounding: two-stage massless relay, exact on a shared Poisson sprinkling (rho = 1).
Source ball B0 (radius s, at rest, X1 = -(D1+D0)), relay ball B1 (radius s, X1 = -D1), observer x = origin.
phi1(w) = sum_{y in B0, y <. w} 1  for w in B1;   phi2(x) = sum_{w in B1, w <. x} phi1(w)   (a/rho factors dropped).
Dependence region (EXACT, up to the SMAX shell truncation):
  R_x  = x's past shell toward B1 (as in E1p_1);
  Slab = {u = t - X1 in [u_lo, 0], X1 in [-(D0+D1+s+m), -D1+s+m], perp < s+m}  contains every I(y,w), y in B0, w in B1
         relevant (u is monotone along causal curves pointing along +X1: u_y <= u_z <= u_w).
Union sampled at density 1: R_x fully + Slab minus R_x.
Compare relative variance with the 'no-compounding' law  Var/mean^2 = F1/N1 + F0/(N1 N0)  (single-stage F's from E1p_1).
"""
import sys, time, json
import numpy as np
from numba import njit, prange
from math import pi, sqrt
from E1p_1_massless_needle import region_table, sample_region, TAU2, TAU

M = TAU  # margin


def in_Rx(P, D, s):
    sig = P[:, 0]**2 - (P[:, 1:]**2).sum(1)
    perp = np.sqrt(P[:, 2]**2 + P[:, 3]**2)
    return (P[:, 0] < 0) & (sig > 0) & (sig < TAU2) & (perp < s + TAU) & (P[:, 1] > -(D + s + TAU)) & (P[:, 1] < TAU)


@njit(parallel=True, cache=True)
def links_into(P, tgt, cand_lists_ptr, cand_lists, order_u, u_sorted):
    """For each target w (index tgt[q]) and its candidate past points y (cand list), decide y <. w:
    no z with y < z < w. z must have u_y <= u_z <= u_w (u = t - X1); scan that u-window."""
    nq = tgt.shape[0]
    out = np.zeros(cand_lists.shape[0], np.int8)
    for q in prange(nq):
        w = tgt[q]
        tw, xw, yw, zw = P[w, 0], P[w, 1], P[w, 2], P[w, 3]
        uw = tw - xw
        for c in range(cand_lists_ptr[q], cand_lists_ptr[q + 1]):
            y = cand_lists[c]
            ty, xy, yy, zy = P[y, 0], P[y, 1], P[y, 2], P[y, 3]
            uy = ty - xy
            lo = np.searchsorted(u_sorted, uy)
            hi = np.searchsorted(u_sorted, uw)
            linked = 1
            for p in range(lo, hi + 1):
                if p >= order_u.shape[0]:
                    break
                z = order_u[p]
                if z == y or z == w:
                    continue
                dt1 = P[z, 0] - ty
                if dt1 <= 0:
                    continue
                dx = P[z, 1] - xy; dy = P[z, 2] - yy; dz = P[z, 3] - zy
                if dt1 * dt1 <= dx * dx + dy * dy + dz * dz:
                    continue
                dt2 = tw - P[z, 0]
                if dt2 <= 0:
                    continue
                dx = xw - P[z, 1]; dy = yw - P[z, 2]; dz = zw - P[z, 3]
                if dt2 * dt2 > dx * dx + dy * dy + dz * dz:
                    linked = 0
                    break
            out[c] = linked
    return out


def run(s, D0, D1, nreal, seed):
    rng = np.random.default_rng(seed)
    tab = region_table(D1, s)
    R = s + M
    u_lo = -(1.3 * (s * s + TAU2) / (2 * (D1 - s)) + 1.3 * ((2 * s)**2 + TAU2) / (2 * (D0 - 2 * s)) + 0.5)
    X_lo = -(D0 + D1 + s + M); X_hi = -D1 + s + M
    Vslab = (0 - u_lo) * (X_hi - X_lo) * pi * R * R
    out = np.zeros(nreal); n1 = np.zeros(nreal); m0 = []
    t0 = time.time()
    for it in range(nreal):
        Px = sample_region(D1, s, rng, tab)
        Ns = rng.poisson(Vslab)
        u = rng.uniform(u_lo, 0, Ns); X1 = rng.uniform(X_lo, X_hi, Ns)
        rr = R * np.sqrt(rng.uniform(0, 1, Ns)); ph = rng.uniform(0, 2 * pi, Ns)
        Ps = np.column_stack([u + X1, X1, rr * np.cos(ph), rr * np.sin(ph)])
        Ps = Ps[~in_Rx(Ps, D1, s)]
        P = np.vstack([Px, Ps])
        # stage 2: x's links into B1 (blockers in R_x; use all points with smaller sigma)
        sig = P[:, 0]**2 - (P[:, 1:]**2).sum(1)
        d1 = np.sqrt((P[:, 1] + D1)**2 + P[:, 2]**2 + P[:, 3]**2)
        inB1 = (d1 < s) & (P[:, 0] < 0) & (sig > 0) & (sig < TAU2)
        cand1 = np.where(inB1)[0]
        # brute: blockers z with sigma_z < sigma_w, z > w  (z < x automatic for sig>0,t<0)
        ok = (P[:, 0] < 0) & (sig > 0)
        Pok = P[ok]; idx_ok = np.where(ok)[0]; sig_ok = sig[ok]
        order = np.argsort(sig_ok)
        from E1p_1_massless_needle import links_to_origin
        loc = np.searchsorted(idx_ok, cand1)
        lk1 = links_to_origin(Pok, order, loc).astype(bool)
        W = cand1[lk1]
        n1[it] = len(W)
        # stage 1: each linked w's links into B0
        d0 = np.sqrt((P[:, 1] + D0 + D1)**2 + P[:, 2]**2 + P[:, 3]**2)
        B0 = np.where(d0 < s)[0]
        ptr = [0]; cl = []
        for w in W:
            dtv = P[w, 0] - P[B0, 0]
            dd2 = ((P[w, 1:] - P[B0, 1:])**2).sum(1)
            sg = dtv * dtv - dd2
            c = B0[(dtv > 0) & (sg > 0) & (sg < TAU2)]
            cl.extend(c.tolist()); ptr.append(len(cl))
        uu = P[:, 0] - P[:, 1]
        ou = np.argsort(uu); us = uu[ou]
        if len(W) > 0 and len(cl) > 0:
            lk0 = links_into(P, W.astype(np.int64), np.array(ptr, np.int64), np.array(cl, np.int64), ou, us)
            per_w = np.add.reduceat(lk0.astype(np.int64), np.array(ptr[:-1])) if len(cl) else np.zeros(len(W))
            # reduceat on empty segments returns the element at the index; fix empties
            per_w = np.array([lk0[ptr[i]:ptr[i + 1]].sum() for i in range(len(W))])
        else:
            per_w = np.zeros(len(W))
        m0.extend(per_w.tolist())
        out[it] = per_w.sum()
        if it % max(1, nreal // 5) == 0:
            print(f"  it {it}: |P|={len(P)} N1={len(W)} phi={out[it]:.0f} t={time.time()-t0:.1f}s", flush=True)
    return out, n1, np.array(m0)


if __name__ == "__main__":
    s, D0, D1, n, seed = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    phi, n1, m0 = run(s, D0, D1, n, seed)
    N1 = n1.mean(); F1 = n1.var(ddof=1) / N1
    N0 = m0.mean(); F0 = m0.var(ddof=1) / N0
    pred = F1 / N1 + F0 / (N1 * N0)
    rel = phi.var(ddof=1) / phi.mean()**2
    print(f"s={s} D0={D0} D1={D1} n={n}: <N1>={N1:.3f} F1={F1:.3f} <M0>={N0:.3f} F0={F0:.3f} <phi>={phi.mean():.3f} (N1*M0={N1*N0:.3f})")
    print(f"   relative variance of phi: {rel:.4f};  no-compounding law F1/N1 + F0/(N1 N0) = {pred:.4f};  last stage alone F1/N1 = {F1/N1:.4f}")
    np.savez(f"../out/relay_s{s}_D0{D0}_D1{D1}.npz", phi=phi, n1=n1, m0=m0)
