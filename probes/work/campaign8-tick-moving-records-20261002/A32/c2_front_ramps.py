"""
A32 check C2: gated record growth (A28: a site may form only if it has a recorded neighbour
present at the instant of its own tick) under a global tick vs neighbourhood tick phases.

Supplied toy: the record part only (classical). Each gate-open site succeeds with chance F per own tick,
independently of how many recorded neighbours it has (simplest gate). With a global tick, "present
at the instant of the tick" is A28's start-of-tick rule: a record formed on this tick gates only from
the next tick. With site phases phi(x) in [0,1) (units of the period), a neighbour whose tick comes
later in the same period already sees the new record: chains can run along increasing phases.

1D exact renewal formula (derived in the report): front speed v = 1 / (E[w] + 1/F - 1) sites per period,
w = wait (in periods) from a site's tick to its forward neighbour's next tick (w = 1 for equal phases).
"""
import signal, heapq
import numpy as np
signal.alarm(55)
rng = np.random.default_rng(3202)

def front_1d(phi, F, nsteps, rng):
    """Return the time (in periods) at which site nsteps forms, seed at site 0 formed at time phi[0]."""
    t = phi[0]
    for x in range(nsteps):
        p_next = phi[x + 1]
        # next tick of x+1 strictly after t
        m = np.floor(t - p_next) + 1
        t_open = p_next + m
        if t_open <= t + 1e-15:
            t_open += 1.0
        K = rng.geometric(F) - 1          # failures before success
        t = t_open + K
    return t

print("C2a. 1D gated front speed (sites per period): Monte Carlo vs exact renewal formula")
print("  phase field          F       E[w]    v_MC        v_exact     v/v_global(exact)")
nsteps, nrep = 4000, 20
for F in [1.0, 0.5, 0.1, 0.01]:
    for name in ["global", "ramp g=0.1 (up)", "ramp g=0.1 (down)", "iid uniform"]:
        vs = []
        for r in range(nrep):
            if name == "global":
                phi = np.zeros(nsteps + 1); Ew = 1.0
            elif name.startswith("ramp") and "up" in name:
                phi = (0.1 * np.arange(nsteps + 1)) % 1.0; Ew = 0.1
            elif name.startswith("ramp"):
                phi = (-0.1 * np.arange(nsteps + 1)) % 1.0; Ew = 0.9
            else:
                phi = rng.random(nsteps + 1); Ew = 0.5
            t_end = front_1d(phi, F, nsteps, rng)
            vs.append(nsteps / (t_end - phi[0]))
        v_ex = 1.0 / (Ew + 1.0 / F - 1.0)
        print(f"  {name:<20} {F:<7} {Ew:<7} {np.mean(vs):<11.5f} {v_ex:<11.5f} {v_ex / F:.5f}")

def grow_2d(phi, F, T, rng):
    """First-passage gated growth on an LxL grid from the centre; returns formation times (inf if > T)."""
    L = phi.shape[0]
    K = rng.geometric(F, size=phi.shape) - 1
    tform = np.full(phi.shape, np.inf)
    c = L // 2
    tform[c, c] = phi[c, c]
    done = np.zeros(phi.shape, bool)
    pq = [(phi[c, c], c, c)]
    while pq:
        t, x, y = heapq.heappop(pq)
        if done[x, y]:
            continue
        done[x, y] = True
        if t > T:
            break
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            u, v = x + dx, y + dy
            if 0 <= u < L and 0 <= v < L and not done[u, v]:
                p = phi[u, v]
                m = np.floor(t - p) + 1
                t_open = p + m
                if t_open <= t + 1e-15:
                    t_open += 1.0
                tn = t_open + K[u, v]
                if tn < tform[u, v]:
                    tform[u, v] = tn
                    heapq.heappush(pq, (tn, u, v))
    return tform

print("\nC2b. 2D gated growth from one seed: reach after T periods (axis and diagonal), global vs neighbourhood phases")
L = 241
for F, T in [(1.0, 12.0), (0.1, 60.0)]:
    print(f"  F = {F}, T = {T} periods")
    for name in ["global", "iid uniform", "ramp g=0.2 along +x"]:
        reps = 3 if F < 1 else 2
        ax_p, ax_m, dg, area = [], [], [], []
        for r in range(reps):
            if name == "global":
                phi = np.zeros((L, L))
            elif name == "iid uniform":
                phi = rng.random((L, L))
            else:
                phi = (0.2 * np.arange(L)[:, None] * np.ones((1, L))) % 1.0
            tf = grow_2d(phi, F, T, rng)
            c = L // 2
            rec = tf <= T
            row = rec[:, c]
            xs = np.where(row)[0] - c
            ax_p.append(xs.max()); ax_m.append(-xs.min())
            dd = [k for k in range(0, c) if rec[c + k, c + k]]
            dg.append(max(dd) if dd else 0)
            area.append(rec.sum())
        print(f"    {name:<22} reach +x {np.mean(ax_p):6.1f}  -x {np.mean(ax_m):6.1f}  diagonal steps {np.mean(dg):6.1f}  recorded sites {np.mean(area):8.0f}")
print("  (global tick, F=1: reach is exactly T sites per axis, the L1 ball: the strict one-site-per-tick record cone)")

print("\nC2c. 2D small-F trend: recorded area after T periods, i.i.d. phases vs global (same K draws, coupled)")
print("     coupling bound (exact per path): every edge wait is in (0,1] vs exactly 1 for the global tick")
print("  F       T      area_global   area_iid    area ratio   sqrt(ratio)-1   (sqrt(ratio)-1)/F")
L = 241
for F, T in [(0.2, 25.0), (0.1, 50.0), (0.05, 100.0), (0.025, 200.0), (0.0125, 400.0)]:
    ag, ai = [], []
    for r in range(8):
        seed = 1000 + r
        r1 = np.random.default_rng(seed); r2 = np.random.default_rng(seed)
        tg = grow_2d(np.zeros((L, L)), F, T, r1)
        phi = np.random.default_rng(seed + 77).random((L, L))
        ti = grow_2d(phi, F, T, r2)       # same K field (same rng stream), different phases
        ag.append((tg <= T).sum()); ai.append((ti <= T).sum())
    ratio = np.mean(ai) / np.mean(ag)
    print(f"  {F:<7} {T:<6} {np.mean(ag):<13.1f} {np.mean(ai):<11.1f} {ratio:<12.4f} {np.sqrt(ratio)-1:<15.4f} {(np.sqrt(ratio)-1)/F:.3f}")
