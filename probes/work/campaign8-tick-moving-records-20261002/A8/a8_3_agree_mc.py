"""A8 check 3: neighbourhood-set capture (toy).  Does an irreversible net sink emerge from agreement odds,
and is the depletion (clock) field then the Green potential of the measured capture current (Gauss/Poisson)?

Supplied toy (nothing adopted), 31^3 box, global ticks, move dynamics of lane G's g3:
  * free records (carriers) carry a content c in {0..k-1}; the reservoir layer is reset every tick to
    occupancy u_inf with contents drawn with equal odds (Q4);
  * each tick a carrier attempts one hop (prob 1/2, uniform direction); target must be empty and unrecorded
    (one record per site; held records impenetrable); contention: one winner, equal odds; no swaps;
  * STOP RULE (Q7-style menu): a free record with >= 1 held neighbour whose held neighbours ALL carry its own
    content has the menu {stay}: it becomes held.  Held records never move, contents never change, so the
    condition once met stays met: capture is irreversible from permanence, no sink is imposed.  The lump grows.
  * reading 'carried'  : content travels with the record.
    reading 'reformed' : each arrival is a fresh formation (R1-like): content redrawn with equal odds.
Seed lump: 3^3 cube, all content 0.
Per block (geometry = held set at block start):
  (i)  MC capture flux J_b vs mean-field prediction (absorbing contacts: q=1 for species 0 if 'carried',
       q=1/k per arrival for all species if 'reformed');
  (ii) Poisson/Gauss check: deficit D = u_sp - u solves (deg_f - Adj_f) D = 12 j_MC on the free graph,
       D = 0 on the reservoir, with j_MC the MEASURED capture distribution.  Compare radial bins.
Usage: python a8_3_agree_mc.py reading k u_inf T_burn n_blocks block_len seed
"""
import os
for kk in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[kk] = "1"
import sys
import time
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import cg

t0 = time.time()
READING = sys.argv[1] if len(sys.argv) > 1 else "carried"
KC = int(sys.argv[2]) if len(sys.argv) > 2 else 4
U_INF = float(sys.argv[3]) if len(sys.argv) > 3 else 0.004
T_BURN = int(sys.argv[4]) if len(sys.argv) > 4 else 3000
NB = int(sys.argv[5]) if len(sys.argv) > 5 else 8
BL = int(sys.argv[6]) if len(sys.argv) > 6 else 4000
SEED = int(sys.argv[7]) if len(sys.argv) > 7 else 20261002
rng = np.random.default_rng(SEED)

L, C = 31, 15
N = L ** 3
I, J, K = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
FI, FJ, FK = I.ravel(), J.ravel(), K.ravel()
res = ((I == 0) | (I == L - 1) | (J == 0) | (J == L - 1) | (K == 0) | (K == L - 1)).ravel()
res_idx = np.flatnonzero(res)
interior = ~res
DI = np.array([1, -1, 0, 0, 0, 0]); DJ = np.array([0, 0, 1, -1, 0, 0]); DK = np.array([0, 0, 0, 0, 1, -1])
OFF = DI * L * L + DJ * L + DK
idx = np.arange(N).reshape(L, L, L)
rows, cols = [], []
for d in range(3):
    a = [slice(None)] * 3; b = [slice(None)] * 3
    a[d] = slice(0, L - 1); b[d] = slice(1, L)
    p = idx[tuple(a)].ravel(); q = idx[tuple(b)].ravel()
    rows += [p, q]; cols += [q, p]
rows = np.concatenate(rows); cols = np.concatenate(cols)
ADJ = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(N, N))
rr = np.sqrt((FI - C) ** 2 + (FJ - C) ** 2 + (FK - C) ** 2)


def step(occ, cont, blocked, periodic):
    p = np.flatnonzero(occ)
    p = p[rng.random(len(p)) < 0.5]
    d = rng.integers(0, 6, size=len(p))
    ti = FI[p] + DI[d]; tj = FJ[p] + DJ[d]; tk = FK[p] + DK[d]
    if periodic:
        ti %= L; tj %= L; tk %= L
    else:
        inb = (ti >= 0) & (ti < L) & (tj >= 0) & (tj < L) & (tk >= 0) & (tk < L)
        p, ti, tj, tk = p[inb], ti[inb], tj[inb], tk[inb]
    t = (ti * L + tj) * L + tk
    ok = ~(occ[t] | blocked[t])
    p, t = p[ok], t[ok]
    perm = rng.permutation(len(t))
    p, t = p[perm], t[perm]
    _, first = np.unique(t, return_index=True)
    p, t = p[first], t[first]
    c = cont[p].copy()
    occ[p] = False
    occ[t] = True
    cont[t] = rng.integers(0, KC, size=len(t)).astype(np.int8) if READING == "reformed" else c
    return p, t


from scipy import ndimage


def reach(held):
    """free sites face-connected to the reservoir layer (sealed pockets excluded)."""
    lab, n = ndimage.label((~held).reshape(L, L, L))
    keep = np.unique(lab.ravel()[res_idx]); keep = keep[keep > 0]
    return np.isin(lab.ravel(), keep)


def free_graph(held):
    free = ~held
    adjf = ADJ.multiply(free[None, :]).tocsr()
    deg = np.asarray(adjf.sum(1)).ravel()
    return free, adjf, deg


def poisson_deficit(held, src):
    """(deg_f - Adj_f) D = src on free interior sites, D = 0 on reservoir."""
    free, adjf, deg = free_graph(held)
    ui = np.flatnonzero(free & interior & reach(held))
    Mm = sp.diags(deg[ui]) - adjf[ui][:, ui]
    x, info = cg(Mm.tocsr(), src[ui], rtol=1e-10, maxiter=50000)
    D = np.zeros(N); D[ui] = x
    return D


def predicted_J(held, hcont):
    """mean-field capture flux for the current geometry (dilute limit)."""
    free, adjf, deg = free_graph(held)
    hn = np.zeros((N, 6), dtype=bool)
    hc = np.full((N, 6), -1, dtype=np.int16)
    ii = np.flatnonzero(interior)
    nb = ii[:, None] + OFF[None, :]
    hn[ii] = held[nb]; hc[ii] = np.where(held[nb], hcont[nb], -1)
    nh = hn.sum(1)
    if READING == "carried":
        S = free & interior & (nh >= 1) & ((hc == 0) | ~hn).all(1)
        q, u_res = 1.0, U_INF / KC
    else:
        first = np.where(hn, hc, 99).min(1)
        S = free & interior & (nh >= 1) & ((hc == first[:, None]) | ~hn).all(1)
        q, u_res = 1.0 / KC, U_INF
    unk = free & interior
    if q >= 1.0:
        unk = unk & ~S
    ui = np.flatnonzero(unk)
    diag = deg[ui] / np.where(S[ui], 1.0 - min(q, 0.999999), 1.0)
    Mm = sp.diags(diag) - adjf[ui][:, ui]
    fixed = np.where(res, u_res, 0.0)
    x, info = cg(Mm.tocsr(), adjf[ui] @ fixed, rtol=1e-10, maxiter=50000)
    u = fixed.copy(); u[ui] = x
    inflow = adjf @ u
    return (q * inflow[S]).sum() / 12.0


# ---- homogeneous reference r_inf ----
occ = np.zeros(N, dtype=bool)
occ[rng.choice(N, size=int(round(U_INF * N)), replace=False)] = True
cont = np.zeros(N, dtype=np.int8)
ev = 0; TH = 6000
for it in range(TH):
    p, t = step(occ, cont, np.zeros(N, dtype=bool), True)
    if it >= 500:
        ev += 2 * len(p)
r_inf = ev / ((TH - 500) * N)

# ---- lump run ----
held = np.zeros(N, dtype=bool)
hcont = np.full(N, -1, dtype=np.int8)
for i in range(C - 1, C + 2):
    for j in range(C - 1, C + 2):
        for k in range(C - 1, C + 2):
            held[idx[i, j, k]] = True; hcont[idx[i, j, k]] = 0
N0 = int(held.sum())
occ = (rng.random(N) < U_INF) & ~held
cont = rng.integers(0, KC, size=N).astype(np.int8)
held_start = []; hcont_start = []
ev_b = np.zeros((NB, N), dtype=np.int64)
oc_b = np.zeros((NB, N), dtype=np.int64)
oc0_b = np.zeros((NB, N), dtype=np.int64)
capsite_b = np.zeros((NB, N), dtype=np.int64)
released = 0
for it in range(T_BURN + NB * BL):
    if it >= T_BURN and (it - T_BURN) % BL == 0:
        held_start.append(held.copy()); hcont_start.append(hcont.copy())
    p, t = step(occ, cont, held, False)
    f = np.flatnonzero(occ & interior)
    nb = f[:, None] + OFF[None, :]
    hn = held[nb]
    nh = hn.sum(1)
    agree = (hcont[nb] == cont[f][:, None]) & hn
    s = f[(nh >= 1) & (agree.sum(1) == nh)]
    if READING == 'nostop':
        s = s[:0]
    if len(s):
        held[s] = True; hcont[s] = cont[s]; occ[s] = False
    occ[res_idx] = rng.random(len(res_idx)) < U_INF
    cont[res_idx] = rng.integers(0, KC, size=len(res_idx)).astype(np.int8)
    if it >= T_BURN:
        b = (it - T_BURN) // BL
        ev_b[b] += np.bincount(p, minlength=N) + np.bincount(t, minlength=N)
        oc_b[b] += occ
        oc0_b[b] += occ & (cont == 0)
        if len(s):
            capsite_b[b] += np.bincount(s, minlength=N)

print(f"reading={READING} k={KC} u_inf={U_INF} seed={SEED} r_inf={r_inf:.6f} (12*kappa*u(1-u)={U_INF*(1-U_INF):.6f}) "
      f"[{time.time()-t0:.1f} s]")
sizes = [int(h.sum()) for h in held_start] + [int(held.sum())]
print("lump size at block starts (+end): " + " ".join(map(str, sizes)))
hp = np.flatnonzero(held)
pk = occ & ~reach(held)
print(f"carriers sealed in pockets at end: {int(pk.sum())} (species 0: {int((pk & (cont == 0)).sum())})")
print(f"final lump N={len(hp)}, max radius {rr[hp].max():.2f}, contents {np.bincount(hcont[hp].astype(int), minlength=KC).tolist()}")
J_mc = capsite_b.sum(1) / BL
J_pr = np.array([predicted_J(h, hc) for h, hc in zip(held_start, hcont_start)])
J_pr_end = np.array([predicted_J(h, hc) for h, hc in zip(held_start[1:] + [held], hcont_start[1:] + [hcont])])
print("block  J_MC     J_pred(start)  J_pred(end)   J_MC/mean(pred)")
for b in range(NB):
    print(f"{b:4d}  {J_mc[b]:.5f}   {J_pr[b]:.5f}       {J_pr_end[b]:.5f}      {J_mc[b]/(0.5*(J_pr[b]+J_pr_end[b])):.3f}")

# Poisson / Gauss check with the measured capture distribution
u_sp = U_INF / KC if READING == "carried" else U_INF
occ_sp_b = oc0_b if READING == "carried" else oc_b
bins = [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5]
mc_def = np.zeros((NB, len(bins))); po_def = np.zeros((NB, len(bins))); clk_def = np.zeros((NB, len(bins)))
oth_def = np.zeros((NB, len(bins)))
for b in range(NB):
    D = poisson_deficit(held_start[b], 12.0 * capsite_b[b] / BL)
    hend = held_start[b + 1] if b + 1 < NB else held
    REACH_END = reach(hend)
    for i, lo in enumerate(bins):
        m = interior & ~hend & REACH_END & (rr >= lo) & (rr < lo + 1)
        mc_def[b, i] = 1 - occ_sp_b[b, m].mean() / BL / u_sp
        po_def[b, i] = D[m].mean() / u_sp
        clk_def[b, i] = 1 - ev_b[b, m].mean() / BL / r_inf
        oth_def[b, i] = 1 - (oc_b[b, m] - oc0_b[b, m]).mean() / BL / (U_INF * (KC - 1) / KC)
print("\n  r  | species deficit: MC (s.e.)   Poisson(j_MC)  ratio | clock deficit (all) | other-species deficit")
for i, lo in enumerate(bins):
    mm, se = mc_def[:, i].mean(), mc_def[:, i].std(ddof=1) / np.sqrt(NB)
    pp = po_def[:, i].mean()
    print(f"{lo+0.5:4.1f} |        {mm:+.4f} ({se:.4f})   {pp:+.4f}      {mm/pp:.3f} |  {clk_def[:, i].mean():+.4f}           |  {oth_def[:, i].mean():+.4f}")
print(f"elapsed {time.time()-t0:.1f} s")
sel = slice(1, 10)   # r = 4 .. 12
fac = u_sp / U_INF
print(f"SUMMARY {READING} seed={SEED} N_end={int(held.sum())} J_MC/J_pred={J_mc.sum()/(0.5*(J_pr+J_pr_end)).sum():.4f} "
      f"captures={int(capsite_b.sum())} species_def_ratio={mc_def[:, sel].sum()/po_def[:, sel].sum():.4f} "
      f"clock_def_ratio={clk_def[:, sel].sum()/(fac*po_def[:, sel]).sum():.4f} others_def_mean={oth_def[:, sel].mean():+.4f}")
