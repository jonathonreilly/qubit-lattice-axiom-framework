"""Lane G check 3: Monte Carlo of a supplied I1-I3-type move process (toy).

Global ticks (I1). Each free record, each tick: with prob 1/2 it attempts one hop to a
uniformly chosen neighbour (I2: at most one grid space per tick; isotropic odds in the void).
Target must be empty at tick start (one record per site). If several records want the same
site, one wins with equal odds (I3 contention). No swaps. No formation in the void.
Lump B (3^3, held records) is impenetrable; a free record that lands on the contact shell S
is captured (joins the lump; removed from the free gas so the lump shape stays fixed).
Reservoir: every tick the outer layer is reset to independent occupancy u_inf (stands in for
the far gas of the infinite grid).

Clock: per-site count of move events (departures + arrivals) per tick.
Prediction (dilute, mean equation u_{t+1} = u_t + (1/12) Delta u_t + O(u^2)):
    u(x)/u_inf = 1 - h(x) = 1 + Phi(x),  r(x)/r_inf = 1 + Phi(x) + O(u_inf * Phi),
    capture flux J = u_inf * Cap_box(S) / 12 (Gauss: monopole = net capture current).
h(x) from check 2 (h_box.npy, same geometry).
"""
import os
for k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[k] = "1"
import sys
import time
import numpy as np

t0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
L, C = 31, 15
N = L ** 3
U_INF = float(sys.argv[4]) if len(sys.argv) > 4 else 0.04
T_BURN = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
T_MEAS = int(sys.argv[2]) if len(sys.argv) > 2 else 40000
T_HOM = int(sys.argv[3]) if len(sys.argv) > 3 else 6000
rng = np.random.default_rng(777)

I, J, K = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
FI, FJ, FK = I.ravel(), J.ravel(), K.ravel()
res = ((I == 0) | (I == L - 1) | (J == 0) | (J == L - 1) | (K == 0) | (K == L - 1)).ravel()
lump3 = (abs(I - C) <= 1) & (abs(J - C) <= 1) & (abs(K - C) <= 1)
dil = lump3.copy()
for d in range(3):
    for s in (1, -1):
        dil |= np.roll(lump3, s, axis=d)
lump = lump3.ravel(); shell = (dil & ~lump3).ravel()
res_idx = np.flatnonzero(res); shell_idx = np.flatnonzero(shell)
DI = np.array([1, -1, 0, 0, 0, 0]); DJ = np.array([0, 0, 1, -1, 0, 0]); DK = np.array([0, 0, 0, 0, 1, -1])


def step(occ, blocked, periodic):
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
    occ[p] = False
    occ[t] = True
    return p, t


# ---- homogeneous reference (periodic, no lump): r_inf ----
occ = np.zeros(N, dtype=bool)
occ[rng.choice(N, size=int(round(U_INF * N)), replace=False)] = True
noblock = np.zeros(N, dtype=bool)
ev_h = 0
for it in range(T_HOM):
    p, t = step(occ, noblock, True)
    if it >= 500:
        ev_h += 2 * len(p)
dens_h = occ.mean()
r_inf = ev_h / ((T_HOM - 500) * N)
print(f"homogeneous: final density {dens_h:.4f}, r_inf = {r_inf:.6f} events/site/tick "
      f"(dilute estimate u_inf = {U_INF})   [{time.time()-t0:.1f} s]")

# ---- lump + reservoir ----
occ = rng.random(N) < U_INF
occ[lump] = False; occ[shell] = False
NB = 8
BL = T_MEAS // NB
ev_b = np.zeros((NB, N), dtype=np.int64)
oc_b = np.zeros((NB, N), dtype=np.int64)
cap_b = np.zeros(NB, dtype=np.int64)
for it in range(T_BURN + NB * BL):
    p, t = step(occ, lump, False)
    cap_now = int(occ[shell_idx].sum())
    occ[shell_idx] = False
    occ[res_idx] = rng.random(len(res_idx)) < U_INF
    if it >= T_BURN:
        b = (it - T_BURN) // BL
        ev_b[b] += np.bincount(p, minlength=N) + np.bincount(t, minlength=N)
        oc_b[b] += occ
        cap_b[b] += cap_now
T_MEAS = NB * BL
events = ev_b.sum(0); occsum = oc_b.sum(0); captured = int(cap_b.sum())
print(f"lump run done [{time.time()-t0:.1f} s]")

h = np.load(os.path.join(HERE, "h_box.npy")).ravel()
lap = np.zeros(N)
H3 = h.reshape(L, L, L)
L3 = -6 * H3
for d in range(3):
    L3 += np.roll(H3, 1, axis=d) + np.roll(H3, -1, axis=d)
capbox = float((-L3).ravel()[shell].sum())
J_pred = U_INF * capbox / 12.0
J_mc = captured / T_MEAS
J_blocks = cap_b / BL
print(f"capture flux: MC {J_mc:.5f} +/- {J_blocks.std(ddof=1)/np.sqrt(NB):.5f} (block s.e.) per tick; "
      f"Gauss prediction u_inf*Cap_box/12 = {J_pred:.5f}  (ratio {J_mc/J_pred:.4f})")

bulk = ~(res | lump | shell)
rr = np.sqrt((FI - C) ** 2 + (FJ - C) ** 2 + (FK - C) ** 2)
r_site = events / T_MEAS
u_site = occsum / T_MEAS
print("\n r-bin  sites | u/u_inf (s.e.)   1-h   | r/r_inf (s.e.)   LE-pred | r/r_inf-(1-h)  r/r_inf-LE")
for lo in np.arange(2.5, 13.5, 1.0):
    m = bulk & (rr >= lo) & (rr < lo + 1)
    if m.sum() == 0:
        continue
    one_m_h = (1 - h[m]).mean()
    le = ((1 - h[m]) * (1 - U_INF * (1 - h[m])) / (1 - U_INF)).mean()
    ub = oc_b[:, m].mean(1) / BL / U_INF
    rb = ev_b[:, m].mean(1) / BL / r_inf
    ru, rc = ub.mean(), rb.mean()
    su, sc = ub.std(ddof=1) / np.sqrt(NB), rb.std(ddof=1) / np.sqrt(NB)
    print(f"{lo+0.5:5.1f}  {m.sum():5d} | {ru:.4f} ({su:.4f})  {one_m_h:.4f} | {rc:.4f} ({sc:.4f})   {le:.4f} |"
          f"   {rc-one_m_h:+.4f}       {rc-le:+.4f}")

# statistical error estimate: split measurement into 4 blocks is not stored; use site-level spread
m = bulk & (rr >= 6.5) & (rr < 7.5)
print(f"\nper-site event-rate spread in r~7 bin: sd/mean = {r_site[m].std()/r_site[m].mean():.3f} "
      f"over {m.sum()} sites (bin-mean standard error ~ {r_site[m].std()/r_site[m].mean()/np.sqrt(m.sum()):.4f} if independent)")
print(f"elapsed {time.time()-t0:.1f} s")
