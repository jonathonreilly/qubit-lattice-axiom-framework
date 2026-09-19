#!/usr/bin/env python3
"""Probe: KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.

Literal checks of the note's proof steps, beyond the runner's sizes, with
machinery disjoint from the runner (the runner uses sympy case analysis at
degree 1, the top coefficient only at degree 2, an abstract trace for D1-D4,
and a 12-point float sweep for D6d):

 S1  Monomial lemma (B1-B4), full statement, by EXHAUSTIVE enumeration: every
     Laurent polynomial sum_{|n|<=r} a_n z^n with coefficients in (1/D)Z[i]
     that is unimodular on the circle (exact integer lag identities
     sum_n a_{n+m} conj(a_n) = D^2 delta_{m0}) is a monomial.
     Sizes: D = 5 at r = 1, 2, 3, 4; D = 25 at r = 1; D = 10 at r = 2.
 S2  Band theorem (D1-D4) on every member of an exact family of P3 radius-1
     two-band unitaries U(z) = z^{-1} W (Q1 + P1 z)(Q2 + P2 z), W in SU(2) with
     entries in (1/5)Z[i], P1, P2 rank-one projectors from (1/5)Z[i]^2 unit
     vectors.  Exact integer checks: paraunitarity, det U = 1, trace real,
     |beta| + 2|gamma| <= 2, winding cell (beta, |gamma|) = (0, 1) and its
     structure.  Band winding and max |v| computed per trace class by numeric
     branch tracking through touchings over two Brillouin loops (not by the
     note's surjectivity argument).
 S3  D6d dichotomy on an exact rational (beta, g) grid (denominator 60):
     exact bound sup v^2 <= S^2, S = |beta|/2 + g, and the touching limit
     v^2 -> g on S = 1; numeric cross-check on a dense momentum grid.
 S4  Part C: distance-2 amplitude of exp(i x cos k) from exact rational
     Fourier coefficients of cos^m k; Bessel zeros of the distance-2 amplitude
     and the beyond-radius-1 weight there (mpmath).
 S5  E2 witness S_+ C(0.6): branch velocity range by direct eigenvalue
     tracking of the 2x2 matrix, against the note's [0.087, 0.913].

Prints SUMMARY: lines; prints HIT: only when a checked statement of the note
fails literally.
"""
from fractions import Fraction
import math
import sys
import time

import numpy as np
import mpmath as mp

HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


# ---------------------------------------------------------------------------
# S1  monomial lemma, exhaustive over (1/D)Z[i]
# ---------------------------------------------------------------------------
def gaussian_points(D):
    return np.array([(x, y) for x in range(-D, D + 1) for y in range(-D, D + 1)
                     if x * x + y * y <= D * D], dtype=np.int64)


def enumerate_unimodular(r, D):
    """All a in Z[i]^{2r+1} (index n = -r..r) with
    R(m) := sum_{n=-r}^{r-m} a_{n+m} conj(a_n) = D^2 delta_{m0}, m = 0..2r.
    Breadth-first over outside-in levels (a_j, a_{-j}), j = r..1, then a_0.
    At level j the lag m = r + j is fully determined and must vanish; the
    running norm must stay <= D^2.  Every pruning test is an exact necessary
    condition, so the enumeration is complete over the grid."""
    P = gaussian_points(D)
    G = len(P)
    nrm = P[:, 0] ** 2 + P[:, 1] ** 2
    L = 2 * r + 1
    D2 = D * D
    ii, jj = np.meshgrid(np.arange(G), np.arange(G), indexing="ij")
    ii = ii.ravel()
    jj = jj.ravel()
    ok = nrm[ii] + nrm[jj] <= D2
    pi_, pj_ = ii[ok], jj[ok]
    pn = nrm[pi_] + nrm[pj_]
    order = np.argsort(pn, kind="stable")
    pi_, pj_, pn = pi_[order], pj_[order], pn[order]

    def lag(REs, IMs, m):
        rr = np.zeros(REs.shape[0], np.int64)
        ri = np.zeros(REs.shape[0], np.int64)
        for n in range(-r, r - m + 1):
            ar, ai = REs[:, n + m + r], IMs[:, n + m + r]
            br, bi = REs[:, n + r], IMs[:, n + r]
            rr += ar * br + ai * bi
            ri += ai * br - ar * bi
        return rr, ri

    RE = np.zeros((1, L), np.int64)
    IM = np.zeros((1, L), np.int64)
    NR = np.zeros(1, np.int64)
    nodes = 0
    for j in range(r, 0, -1):
        m_new = r + j
        outR, outI, outN = [], [], []
        for s in range(len(NR)):
            budget = D2 - NR[s]
            cnt = int(np.searchsorted(pn, budget, side="right"))
            if cnt == 0:
                continue
            tR = np.repeat(RE[s:s + 1], cnt, axis=0)
            tI = np.repeat(IM[s:s + 1], cnt, axis=0)
            tR[:, j + r] = P[pi_[:cnt], 0]
            tI[:, j + r] = P[pi_[:cnt], 1]
            tR[:, -j + r] = P[pj_[:cnt], 0]
            tI[:, -j + r] = P[pj_[:cnt], 1]
            nodes += cnt
            rr, ri = lag(tR, tI, m_new)
            keep = (rr == 0) & (ri == 0)
            if keep.any():
                outR.append(tR[keep])
                outI.append(tI[keep])
                outN.append(NR[s] + pn[:cnt][keep])
        if not outN:
            return [], nodes
        RE = np.concatenate(outR)
        IM = np.concatenate(outI)
        NR = np.concatenate(outN)
    # level 0: a_0 must complete the norm exactly; then all lags 1..r vanish
    sols = []
    for s in range(len(NR)):
        need = D2 - NR[s]
        cand = np.nonzero(nrm == need)[0]
        if len(cand) == 0:
            continue
        tR = np.repeat(RE[s:s + 1], len(cand), axis=0)
        tI = np.repeat(IM[s:s + 1], len(cand), axis=0)
        tR[:, r] = P[cand, 0]
        tI[:, r] = P[cand, 1]
        nodes += len(cand)
        keep = np.ones(len(cand), bool)
        for m in range(1, r + 1):
            rr, ri = lag(tR, tI, m)
            keep &= (rr == 0) & (ri == 0)
        # independent re-check of the full identity, lag 0 included
        for row in np.nonzero(keep)[0]:
            a = [complex(int(tR[row, t]), int(tI[row, t])) for t in range(L)]
            full = all(sum(a[n + m] * a[n].conjugate() for n in range(L - m)) == (D2 if m == 0 else 0)
                       for m in range(0, 2 * r + 1))
            if not full:
                raise RuntimeError("enumeration bookkeeping error")
            sols.append(tuple((int(tR[row, t]), int(tI[row, t])) for t in range(L)))
    return sols, nodes


def run_S1():
    print("=" * 78)
    print("S1  monomial lemma (B1-B4): exhaustive enumeration over (1/D)Z[i]")
    unit_count = {}
    all_ok = True
    rows = []
    for (r, D) in ((1, 5), (2, 5), (3, 5), (4, 5), (1, 25), (2, 10)):
        t0 = time.time()
        sols, nodes = enumerate_unimodular(r, D)
        dt = time.time() - t0
        nunit = sum(1 for x in range(-D, D + 1) for y in range(-D, D + 1) if x * x + y * y == D * D)
        unit_count[D] = nunit
        nonmono = [s for s in sols if sum(1 for (x, y) in s if (x, y) != (0, 0)) != 1]
        expected = (2 * r + 1) * nunit
        ok = (not nonmono) and len(sols) == expected
        all_ok &= ok
        rows.append((r, D, len(sols), expected, len(nonmono), nodes, dt))
        print(f"  r={r} D={D:2d}: unimodular found = {len(sols):4d} (expected monomials "
              f"(2r+1)*{nunit} = {expected}), non-monomial = {len(nonmono)}, "
              f"search nodes = {nodes}, {dt:.1f}s")
        if nonmono:
            hit(f"monomial lemma: non-monomial unimodular Laurent polynomial of degree <= {r} "
                f"over (1/{D})Z[i]: {nonmono[0]}")
    summary("S1 monomial lemma exhaustive: " + "; ".join(
        f"r={r},D={D}: {n} unimodular, all monomial={nm == 0}, count==(2r+1)*units: {n == e}"
        for (r, D, n, e, nm, _, _) in rows))
    return all_ok


# ---------------------------------------------------------------------------
# S2  exact P3 radius-1 two-band family
# ---------------------------------------------------------------------------
def cmul(A, B):
    Ar, Ai = A
    Br, Bi = B
    return (Ar @ Br - Ai @ Bi, Ar @ Bi + Ai @ Br)


def cadd(A, B):
    return (A[0] + B[0], A[1] + B[1])


def cadj(A):
    return (np.swapaxes(A[0], -1, -2), -np.swapaxes(A[1], -1, -2))


def ctr(A):
    return (A[0][..., 0, 0] + A[0][..., 1, 1], A[1][..., 0, 0] + A[1][..., 1, 1])


def unit_vectors(D):
    out = []
    rng = range(-D, D + 1)
    for x1 in rng:
        for y1 in rng:
            for x2 in rng:
                for y2 in rng:
                    if x1 * x1 + y1 * y1 + x2 * x2 + y2 * y2 == D * D:
                        out.append((x1, y1, x2, y2))
    return out


def track_bands(T0, T1r, T1i, S, K=2048, loops=2, k0=0.1234567):
    """Scaled integer trace class: tr(k) = (T0 + 2 Re((T1r + i T1i) e^{ik}))/S,
    det = 1.  Follow one eigenvalue branch e^{i theta(k)} continuously (linear
    prediction picks the analytic continuation through touchings) for `loops`
    Brillouin loops.  sin(omega) is evaluated cancellation-free from
    (1 - tr/2)(1 + tr/2) = (a + 2g sin^2(kap/2)) (b + 2g cos^2(kap/2)),
    a = 1 - beta/2 - g, b = 1 + beta/2 - g, with a, b from exact integers.
    Returns (degree over the loops, max |v|, min |v|)."""
    N = len(T0)
    t0s = [int(t) for t in T0]
    g2s = [int(x) ** 2 + int(y) ** 2 for x, y in zip(T1r, T1i)]
    beta = np.array(t0s, dtype=float) / S
    g = np.sqrt(np.array(g2s, dtype=float)) / S
    phi = np.arctan2(np.asarray(T1i, dtype=float), np.asarray(T1r, dtype=float))

    def gap(sign):
        # 1 + sign*beta/2 - g = ((2S + sign T0)^2 - 4 g2) / (2S ((2S + sign T0) + 2 sqrt g2)),
        # numerator an exact integer (>= 0 by the D2 bound)
        out = np.zeros(N)
        for i in range(N):
            u = 2 * S + sign * t0s[i]
            den = 2 * S * (u + 2 * math.sqrt(g2s[i]))
            out[i] = (u * u - 4 * g2s[i]) / den if den > 0 else 0.0
        return out
    a = gap(-1)
    b = gap(+1)
    dk = 2 * np.pi / K
    theta = np.zeros(N)
    prev = None
    vmax = np.zeros(N)
    vmin = np.full(N, np.inf)
    start = None
    for s in range(loops * K + 1):
        kv = k0 + s * dk
        kap = kv + phi
        cw = beta / 2 + g * np.cos(kap)
        sw = np.sqrt(np.maximum(a + 2 * g * np.sin(kap / 2) ** 2, 0) *
                     np.maximum(b + 2 * g * np.cos(kap / 2) ** 2, 0))
        om = np.arctan2(sw, cw)
        if s == 0:
            theta = om.copy()
            start = theta.copy()
            prev = theta.copy()
            continue
        pred = theta + (theta - prev) if s > 1 else theta
        best = None
        for cand in (om, -om):
            d = np.angle(np.exp(1j * (cand - pred)))
            best = d if best is None else np.where(np.abs(d) < np.abs(best), d, best)
        new = pred + best
        v = np.abs(new - theta) / dk
        vmax = np.maximum(vmax, v)
        vmin = np.minimum(vmin, v)
        prev, theta = theta, new
    deg = (theta - start) / (2 * np.pi)
    return deg, vmax, vmin


def run_S2():
    print("=" * 78)
    print("S2  exact P3 radius-1 two-band family z^-1 W (Q1 + P1 z)(Q2 + P2 z)")
    D = 5
    vecs = unit_vectors(D)
    # SU(2): W = [[a, -conj b], [b, conj a]] / 5
    Wr = np.array([[[a1, -b1], [b1, a1]] for (a1, a2, b1, b2) in vecs], np.int64)
    Wi = np.array([[[a2, b2], [b2, -a2]] for (a1, a2, b1, b2) in vecs], np.int64)
    # projectors M = u u^dagger (scaled by 25), deduplicated
    projs = {}
    for (x1, y1, x2, y2) in vecs:
        u = (complex(x1, y1), complex(x2, y2))
        M = tuple((int((u[i] * u[j].conjugate()).real), int((u[i] * u[j].conjugate()).imag))
                  for i in range(2) for j in range(2))
        projs[M] = True
    plist = list(projs)
    Mr = np.array([[[p[0][0], p[1][0]], [p[2][0], p[3][0]]] for p in plist], np.int64)
    Mi = np.array([[[p[0][1], p[1][1]], [p[2][1], p[3][1]]] for p in plist], np.int64)
    nW, nP = len(Wr), len(Mr)
    I25 = 25 * np.eye(2, dtype=np.int64)
    Qr, Qi = I25[None] - Mr, -Mi
    S = 3125
    S2 = S * S
    M1 = (Mr[:, None], Mi[:, None])
    M2 = (Mr[None, :], Mi[None, :])
    Q1 = (Qr[:, None], Qi[:, None])
    Q2 = (Qr[None, :], Qi[None, :])
    P1P2 = cmul(M1, M2)
    P1Q2_Q1P2 = cadd(cmul(M1, Q2), cmul(Q1, M2))
    Q1Q2 = cmul(Q1, Q2)
    n_inst = 0
    bad_unit = bad_det = bad_real = bad_bound = 0
    n_cell = 0
    bad_cell_struct = 0
    classes = {}
    eyeS2 = S2 * np.eye(2, dtype=np.int64)
    for w in range(nW):
        W = (Wr[w], Wi[w])
        A1 = cmul(W, P1P2)
        A0 = cmul(W, P1Q2_Q1P2)
        Am = cmul(W, Q1Q2)
        n_inst += nP * nP
        # paraunitarity, both sides, all lags
        m0 = cadd(cadd(cmul(Am, cadj(Am)), cmul(A0, cadj(A0))), cmul(A1, cadj(A1)))
        m1 = cadd(cmul(A1, cadj(A0)), cmul(A0, cadj(Am)))
        m2 = cmul(A1, cadj(Am))
        n0 = cadd(cadd(cmul(cadj(Am), Am), cmul(cadj(A0), A0)), cmul(cadj(A1), A1))
        n1 = cadd(cmul(cadj(Am), A0), cmul(cadj(A0), A1))
        n2 = cmul(cadj(Am), A1)
        uok = ((m0[0] == eyeS2).all(axis=(-1, -2)) & (m0[1] == 0).all(axis=(-1, -2)) &
               (n0[0] == eyeS2).all(axis=(-1, -2)) & (n0[1] == 0).all(axis=(-1, -2)))
        for X in (m1, m2, n1, n2):
            uok &= (X[0] == 0).all(axis=(-1, -2)) & (X[1] == 0).all(axis=(-1, -2))
        bad_unit += int((~uok).sum())
        # det U(z) as a Laurent polynomial (coefficients z^-2..z^2), scaled by S^2
        coef = [Am, A0, A1]

        def ent(i, j):
            return [(c[0][..., i, j], c[1][..., i, j]) for c in coef]
        u00, u01, u10, u11 = ent(0, 0), ent(0, 1), ent(1, 0), ent(1, 1)
        dok = np.ones((nP, nP), bool)
        for deg in range(5):
            re = np.zeros((nP, nP), np.int64)
            im = np.zeros((nP, nP), np.int64)
            for p in range(3):
                q = deg - p
                if 0 <= q < 3:
                    re += u00[p][0] * u11[q][0] - u00[p][1] * u11[q][1]
                    im += u00[p][0] * u11[q][1] + u00[p][1] * u11[q][0]
                    re -= u01[p][0] * u10[q][0] - u01[p][1] * u10[q][1]
                    im -= u01[p][0] * u10[q][1] + u01[p][1] * u10[q][0]
            dok &= (re == (S2 if deg == 2 else 0)) & (im == 0)
        bad_det += int((~dok).sum())
        # trace coefficients
        Tm = ctr(Am)
        T0 = ctr(A0)
        T1 = ctr(A1)
        rok = (T0[1] == 0) & (Tm[0] == T1[0]) & (Tm[1] == -T1[1])
        bad_real += int((~rok).sum())
        absT0 = np.abs(T0[0])
        g2 = T1[0] ** 2 + T1[1] ** 2
        bok = (absT0 <= 2 * S) & (4 * g2 <= (2 * S - absT0) ** 2)
        bad_bound += int((~bok).sum())
        cell = (T0[0] == 0) & (g2 == S2)
        n_cell += int(cell.sum())
        if cell.any():
            idx = np.nonzero(cell)
            a0r, a0i = A0[0][idx], A0[1][idx]
            a1 = (A1[0][idx], A1[1][idx])
            am = (Am[0][idx], Am[1][idx])
            t1 = (T1[0][idx][:, None, None], T1[1][idx][:, None, None])
            tm = (Tm[0][idx][:, None, None], Tm[1][idx][:, None, None])
            sq1 = cmul(a1, a1)
            sqm = cmul(am, am)
            t1a1 = (t1[0] * a1[0] - t1[1] * a1[1], t1[0] * a1[1] + t1[1] * a1[0])
            tmam = (tm[0] * am[0] - tm[1] * am[1], tm[0] * am[1] + tm[1] * am[0])
            x1 = cmul(a1, am)
            x2 = cmul(am, a1)
            okc = ((a0r == 0).all(axis=(-1, -2)) & (a0i == 0).all(axis=(-1, -2)) &
                   (sq1[0] == t1a1[0]).all(axis=(-1, -2)) &
                   (sq1[1] == t1a1[1]).all(axis=(-1, -2)) &
                   (sqm[0] == tmam[0]).all(axis=(-1, -2)) & (sqm[1] == tmam[1]).all(axis=(-1, -2)) &
                   (x1[0] == 0).all(axis=(-1, -2)) & (x1[1] == 0).all(axis=(-1, -2)) &
                   (x2[0] == 0).all(axis=(-1, -2)) & (x2[1] == 0).all(axis=(-1, -2)))
            bad_cell_struct += int((~okc).sum())
        keys = np.stack([T0[0].ravel(), T1[0].ravel(), T1[1].ravel()], axis=1)
        for kk in np.unique(keys, axis=0):
            classes[tuple(int(v) for v in kk)] = True
    print(f"  W in SU(2) over (1/5)Z[i]: {nW}; rank-one projectors: {nP}; instances: {n_inst}")
    print(f"  exact failures: paraunitarity {bad_unit}, det=1 {bad_det}, real trace {bad_real}, "
          f"D2 bound {bad_bound}; winding-cell instances {n_cell}, cell-structure failures {bad_cell_struct}")
    if bad_unit or bad_det or bad_real:
        raise RuntimeError("construction error: family member not P3 radius-1 unitary")
    if bad_bound:
        hit(f"D2: {bad_bound} P3 radius-1 unitaries with |beta| + 2|gamma| > 2")
    if bad_cell_struct:
        hit(f"D3: {bad_cell_struct} winding-cell instances whose coefficients are not c P, 0, conj(c)(1-P)")
    # branch tracking per trace class
    keys = np.array(sorted(classes), dtype=np.int64)
    t0 = time.time()
    deg, vmax, vmin = track_bands(keys[:, 0], keys[:, 1], keys[:, 2], S)
    dt = time.time() - t0
    g2 = keys[:, 1] ** 2 + keys[:, 2] ** 2
    absb = np.abs(keys[:, 0])
    is_cell = (keys[:, 0] == 0) & (g2 == S2)
    on_bdry = (4 * g2 == (2 * S - absb) ** 2) & ~is_cell
    interior = ~is_cell & ~on_bdry
    degr = np.round(deg)
    deg_int = np.abs(deg - degr) < 1e-6
    n_cls = len(keys)
    print(f"  distinct trace classes (beta, gamma): {n_cls}; cell {int(is_cell.sum())}, "
          f"touching boundary |beta|+2g=2 off the cell {int(on_bdry.sum())}, interior {int(interior.sum())}; "
          f"tracking {dt:.1f}s")
    wind = deg_int & (degr != 0)
    bad_wind_off = int((wind & ~is_cell).sum())
    bad_deg_int = int((~deg_int).sum())
    cell_deg = sorted(set(int(x) for x in degr[is_cell]))
    cell_v = (float(vmax[is_cell].max()), float(vmin[is_cell].min())) if is_cell.any() else (None, None)
    off_vmax = float(vmax[~is_cell].max())
    bd_g = np.sqrt(g2[on_bdry]) / S
    bd_vmax = vmax[on_bdry]
    int_S = (absb[interior] / 2 + np.sqrt(g2[interior])) / S
    print(f"  two-loop branch degree: cell classes {cell_deg}; off-cell classes with nonzero degree {bad_wind_off}; "
          f"non-integer degrees {bad_deg_int}")
    print(f"  cell |v| range [{cell_v[1]:.12f}, {cell_v[0]:.12f}]; max |v| off the cell {off_vmax:.6f}")
    if on_bdry.any():
        print(f"  touching-boundary classes: max g = {bd_g.max():.6f} (sqrt = {np.sqrt(bd_g.max()):.6f}); "
              f"max |tracked v - sqrt(g)| = {np.max(np.abs(bd_vmax - np.sqrt(bd_g))):.2e}")
    print(f"  interior classes: max S = |beta|/2 + g = {int_S.max():.6f} (bound sup v^2 <= S^2)")
    # tracked velocities against the per-class bounds (interior: S^2; touching boundary: g)
    pos_i = int_S > 0
    pos_b = bd_g > 0
    ratio_int = float(np.max(vmax[interior][pos_i] ** 2 / int_S[pos_i] ** 2)) if pos_i.any() else 0.0
    ratio_bd = float(np.max(vmax[on_bdry][pos_b] ** 2 / bd_g[pos_b])) if pos_b.any() else 0.0
    ratio_bd_min = float(np.min(vmax[on_bdry][pos_b] ** 2 / bd_g[pos_b])) if pos_b.any() else 0.0
    print(f"  tracked max v^2 / bound: interior (S^2) max {ratio_int:.6f}; touching boundary (g) "
          f"in [{ratio_bd_min:.7f}, {ratio_bd:.7f}]")
    if max(ratio_int, ratio_bd) > 1 + 1e-6:
        hit(f"D6d: tracked velocity exceeds the per-class bound (ratio {max(ratio_int, ratio_bd):.7f})")
    if bad_wind_off:
        hit(f"D2: {bad_wind_off} P3 radius-1 trace classes off (beta,|gamma|)=(0,1) carry a winding band")
    if is_cell.any() and (cell_deg != [-2, 2] and cell_deg != [2] and cell_deg != [-2]):
        hit(f"D3: winding-cell two-loop degrees {cell_deg} (expected +-2)")
    if is_cell.any() and (abs(cell_v[0] - 1) > 1e-9 or abs(cell_v[1] - 1) > 1e-9):
        hit(f"D4: winding-cell band velocity not identically 1: range {cell_v}")
    if off_vmax >= 1 - 1e-9:
        hit(f"D6d: an off-cell P3 class has max |v| = {off_vmax}")
    # spot check: char-poly roots against direct eigenvalues of the matrices
    rng = np.random.default_rng(20260919)
    dev = 0.0
    kk = np.linspace(0, 2 * np.pi, 64, endpoint=False)
    for _ in range(300):
        w = rng.integers(nW)
        p1, p2 = rng.integers(nP), rng.integers(nP)
        W = (Wr[w] + 1j * Wi[w]) / 5
        P1 = (Mr[p1] + 1j * Mi[p1]) / 25
        P2 = (Mr[p2] + 1j * Mi[p2]) / 25
        I2 = np.eye(2)
        for kv in kk:
            z = np.exp(1j * kv)
            U = W @ (I2 - P1 + P1 * z) @ (I2 - P2 + P2 * z) / z
            ev = np.linalg.eigvals(U)
            tr = np.trace(U)
            rts = np.roots([1, -tr, np.linalg.det(U)])
            dev = max(dev, max(min(abs(e - r) for r in rts) for e in ev))
    print(f"  direct eigenvalues vs characteristic-polynomial roots (300 instances x 64 k): max dev {dev:.1e}")
    summary(f"S2 exact P3 radius-1 family: {n_inst} instances ({nW} W x {nP}^2 projector pairs), "
            f"paraunitary/det=1/real-trace exact: all; D2 bound violations {bad_bound}; "
            f"winding-cell instances {n_cell} (all of the form diag-shift c z P + conj(c) z^-1 (1-P): "
            f"{bad_cell_struct == 0}); {n_cls} trace classes tracked: winding only in the cell "
            f"({int(is_cell.sum())} classes, two-loop degree {cell_deg}, |v|=1 to "
            f"{max(abs(cell_v[0] - 1), abs(cell_v[1] - 1)):.1e}); max |v| off the cell {off_vmax:.6f}")
    return True


# ---------------------------------------------------------------------------
# S3  D6d on an exact rational grid
# ---------------------------------------------------------------------------
def run_S3():
    print("=" * 78)
    print("S3  D6d dichotomy on the exact rational (beta, g) grid, denominator 60")
    q = 60
    n_pts = n_int = n_bd = 0
    worst_int = Fraction(0)
    worst_bd = Fraction(0)
    bad = 0
    num_dev = 0.0
    kap = np.linspace(-np.pi, np.pi, 200001)
    for p in range(-2 * q, 2 * q + 1):
        for s in range(0, q + 1):
            if abs(p) + 2 * s > 2 * q:
                continue
            beta = Fraction(p, q)
            g = Fraction(s, q)
            if beta == 0 and g == 1:
                continue
            n_pts += 1
            Sx = abs(beta) / 2 + g
            if Sx < 1:
                n_int += 1
                worst_int = max(worst_int, Sx * Sx)   # exact: sup v^2 <= S^2 < 1
                sup_bound = Sx * Sx
            else:
                n_bd += 1                              # S = 1, beta != 0: sup v^2 = g (touching limit)
                worst_bd = max(worst_bd, g)
                sup_bound = g
                if g >= 1:
                    bad += 1
            if (p % 12 == 0 and s % 6 == 0) or Sx == 1:
                # v^2 = g^2 sin^2 kap / ((a + 2g sin^2(kap/2)) (b + 2g cos^2(kap/2))),
                # a = 1 - beta/2 - g, b = 1 + beta/2 - g exact rationals (no cancellation)
                gf = float(g)
                af = float(1 - beta / 2 - g)
                bf = float(1 + beta / 2 - g)
                den = (af + 2 * gf * np.sin(kap / 2) ** 2) * (bf + 2 * gf * np.cos(kap / 2) ** 2)
                num = gf * gf * np.sin(kap) ** 2
                m = den > 0
                v2 = np.max(num[m] / den[m]) if m.any() else 0.0
                num_dev = max(num_dev, v2 - float(sup_bound))
    print(f"  grid points (beta,g) != (0,1) with |beta| + 2g <= 2: {n_pts}; interior {n_int}, "
          f"touching boundary {n_bd}")
    print(f"  exact: interior max S^2 = {worst_int} = {float(worst_int):.6f} < 1; boundary max g = {worst_bd} "
          f"= {float(worst_bd):.6f} < 1; failures {bad}")
    print(f"  numeric sup v^2 minus exact bound on sampled points: max {num_dev:.2e} (<= 0 up to grid error)")
    if bad or num_dev > 1e-6:
        hit(f"D6d: grid point off (0,1) with sup |v| >= 1 (exact failures {bad}, numeric excess {num_dev})")
    summary(f"S3 D6d exact rational grid (den 60): {n_pts} points off (0,1): interior {n_int} with "
            f"sup v^2 <= S^2 <= {float(worst_int):.6f}, touching boundary {n_bd} with sup v^2 = g <= "
            f"{float(worst_bd):.6f}; numeric excess over bound {num_dev:.1e}")
    return True


# ---------------------------------------------------------------------------
# S4  Part C: distance-2 amplitude of the Hamiltonian tick
# ---------------------------------------------------------------------------
def run_S4():
    print("=" * 78)
    print("S4  Part C: Fourier amplitudes of exp(i x cos k), x = a*kappa")
    # A_2(x) = sum_m (i x)^m / m! * [coefficient of e^{2ik} in cos^m k]
    #        = sum_{m even >= 2} i^m x^m / m! * C(m, (m-2)/2) / 2^m   (exact rationals)
    coeffs = {}
    for m in range(2, 13, 2):
        c = Fraction((-1) ** (m // 2) * math.comb(m, (m - 2) // 2), 2 ** m * math.factorial(m))
        coeffs[m] = c
    print("  A_2 series coefficients (x^m):", ", ".join(f"x^{m}: {coeffs[m]}" for m in sorted(coeffs)))
    if coeffs[2] != Fraction(-1, 8):
        hit(f"C1: distance-2 coefficient of x^2 is {coeffs[2]}, not -1/8")
    # cross-check against -J_2(x) (mpmath) at x = 0.3
    mp.mp.dps = 40
    x = mp.mpf("0.3")
    ser = sum(mp.mpf(c.numerator) / c.denominator * x ** m for m, c in coeffs.items())
    print(f"  series at x=0.3: {mp.nstr(ser, 20)};  -J_2(0.3) = {mp.nstr(-mp.besselj(2, x), 20)}")
    # zeros of the distance-2 amplitude and the beyond-radius-1 weight there
    rows = []
    for n in range(1, 4):
        z2 = mp.besseljzero(2, n)
        leak = 1 - mp.besselj(0, z2) ** 2 - 2 * mp.besselj(1, z2) ** 2
        rows.append((z2, mp.besselj(3, z2), leak))
        print(f"  zero {n} of A_2: x = {mp.nstr(z2, 12)}; |A_3| = {mp.nstr(abs(mp.besselj(3, z2)), 8)}; "
              f"weight beyond radius 1 = {mp.nstr(leak, 8)}")
    # weight beyond radius 1: sum_{|n|>=2} J_n(x)^2 = 1 - J_0^2 - 2 J_1^2  (~ x^4/32 as x -> 0)
    def leak(xv):
        xv = mp.mpf(xv)
        return 1 - mp.besselj(0, xv) ** 2 - 2 * mp.besselj(1, xv) ** 2
    small = [(xv, float(leak(xv) / (mp.mpf(xv) ** 4 / 32))) for xv in ("0.001", "0.01", "0.1")]
    print("  small x: weight / (x^4/32) = " + ", ".join(f"{r:.6f} at x={xv}" for xv, r in small))
    xs = np.linspace(0.5, 40, 2000)
    minleak = min(float(leak(xv)) for xv in xs)
    print(f"  min over x in [0.5, 40] (2000 samples) of the weight beyond radius 1: {minleak:.4f}")
    if not (minleak > 0 and all(r > 0 for _, r in small)):
        hit("C: a nonzero hopping sample gives a radius-1 Hamiltonian tick")
    summary(f"S4 Part C: A_2 = -x^2/8 + x^4/96 - x^6/3072 + ... exact (= -J_2(x)); A_2 vanishes at "
            f"x = {mp.nstr(rows[0][0], 10)}, {mp.nstr(rows[1][0], 10)}, {mp.nstr(rows[2][0], 10)} where "
            f"|A_3| = {mp.nstr(abs(rows[0][1]), 6)}, {mp.nstr(abs(rows[1][1]), 6)}, {mp.nstr(abs(rows[2][1]), 6)} "
            f"(weight beyond radius 1 there {mp.nstr(rows[0][2], 6)}, {mp.nstr(rows[1][2], 6)}, "
            f"{mp.nstr(rows[2][2], 6)}); min sampled weight beyond radius 1 on [0.5,40] = {minleak:.4f}, "
            f"small-x weight/(x^4/32) = {small[0][1]:.6f} at x=0.001")
    return True


# ---------------------------------------------------------------------------
# S5  E2 witness velocity range
# ---------------------------------------------------------------------------
def run_S5():
    print("=" * 78)
    print("S5  E2 witness U(k) = S_+ C(theta): branch velocities by direct eigen-tracking")
    out = []
    for th in (0.6, 0.3, 1.0):
        C = np.array([[np.cos(th), 1j * np.sin(th)], [1j * np.sin(th), np.cos(th)]])
        K = 20000
        ks = -np.pi + 2 * np.pi * np.arange(2 * K + 1) / K + 1e-3
        theta_prev = None
        theta = None
        vmin, vmax = np.inf, 0.0
        start = None
        for s, kv in enumerate(ks):
            U = np.diag([np.exp(1j * kv), 1.0]) @ C
            ev = np.linalg.eigvals(U)
            ph = np.angle(ev)
            if s == 0:
                theta = ph[0]
                start = theta
                continue
            pred = theta + (theta - theta_prev) if theta_prev is not None else theta
            d = np.angle(np.exp(1j * (ph - pred)))
            new = pred + d[np.argmin(np.abs(d))]
            v = abs(new - theta) / (ks[1] - ks[0])
            vmin, vmax = min(vmin, v), max(vmax, v)
            theta_prev, theta = theta, new
        deg2 = (theta - start) / (2 * np.pi)
        exact = ((1 - math.cos(th)) / 2, (1 + math.cos(th)) / 2)
        out.append((th, vmin, vmax, exact, deg2))
        print(f"  theta={th}: tracked |v| in [{vmin:.6f}, {vmax:.6f}]; (1 -+ cos theta)/2 = "
              f"[{exact[0]:.6f}, {exact[1]:.6f}]; two-loop degree {deg2:.6f}")
    th, vmin, vmax, exact, deg2 = out[0]
    lab = (0.087, 0.913)
    if abs(exact[0] - lab[0]) > 5e-4 or abs(exact[1] - lab[1]) > 5e-4 or \
            abs(vmin - exact[0]) > 1e-4 or abs(vmax - exact[1]) > 1e-4:
        hit(f"E2: velocity range at theta=0.6 is [{vmin:.6f}, {vmax:.6f}] vs note [0.087, 0.913]")
    summary(f"S5 E2 S_+C(0.6): tracked branch |v| range [{vmin:.6f}, {vmax:.6f}] = [(1-cos0.6)/2, "
            f"(1+cos0.6)/2] = [{exact[0]:.7f}, {exact[1]:.7f}] (note [0.087, 0.913]); two-loop degree "
            f"{deg2:.4f}; theta=0.3 -> [{out[1][1]:.4f}, {out[1][2]:.4f}], theta=1.0 -> "
            f"[{out[2][1]:.4f}, {out[2][2]:.4f}]")
    return True


def main():
    t0 = time.time()
    run_S1()
    run_S2()
    run_S3()
    run_S4()
    run_S5()
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
