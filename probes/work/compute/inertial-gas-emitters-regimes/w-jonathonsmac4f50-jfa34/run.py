#!/usr/bin/env python3
"""Emitting bodies across regimes in block 44's sphere-menu inertial gas (floating point throughout), independent run 1 of 2.

As landed on main (block 44, PR #8550):
- T1-T5 are exact for the supplied clause, including T4: no mean force on a reflecting body in the uniform state.
- The forces between bodies are 'HISTORICAL AUTHOR OBSERVATIONS, NOT FRESH EVIDENCE', and no force law is claimed.
- The author's emitting pair (Q = 5, reflecting, side 96, gamma = 1): -0.209, -0.061, -0.004 (+- 0.02) per tick
  at separations 12, 20, 32 (pushed apart).
Simulator: probes/lib/inertial_bodies.py and probes/lib/inertial.py, used unchanged.
- body(); emit(), which places Q records per tick on empty surface sites with outward random directions and books the recoil;
  tick_s(..., absorb=False), so the bodies reflect; reservoir().
- The same per-tick order as the lib's main: emit for each body, then tick_s, then reservoir.
- 2000 warm-up ticks, density 0.3, radius 3, side 96 (the author's side; the task gives none).
- Force per tick along the joining axis, positive towards the other body.
Added here, without changing the dynamics:
- a single emitting body at the same position as the pair's first body (its control), subtracted;
- a wall-clock budget, with jobs run in priority order on a process pool (gamma = 1 first, then 0.1, then 4);
- every job reports the ticks it actually measured.
Errors: standard errors over blocks of 500 measured ticks.
Grid (the task's): Q = 2, 5, 10; separations 12, 20, 32; gamma = 0.1, 1, 4.
References printed, not claimed:
- the ideal-fluid source pair Q1 Q2 / (4 pi rho r^2), the attraction named in the task;
- a product-state estimate of the mean free path, drift speed / re-draw rate = (1/sqrt3) / (6 gamma rho),
  from the mean step s/sqrt3 and one re-draw per occupied bond per unit gamma.
No HIT is printed: the task states two rival expectations (kinetic repulsion, ideal-fluid attraction) and asks which holds where.
"""
import os, sys, time, math
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", "lib")))
BUDGET_S = 5.5 * 3600
RHO0, RADIUS, WARM, BLOCK, LSIDE = 0.3, 3, 2000, 500, 96
TEST = os.environ.get("EMIT_TEST") == "1"      # development only: small box, short runs
if TEST: WARM, BLOCK, BUDGET_S, LSIDE = 50, 50, 1200, 72

def out(s): print(s, flush=True)

def job(spec):
    tag, g, q, sep, single, T, seed, deadline = spec
    if TEST: T = 200
    import inertial_bodies as ib
    from inertial import tick_s, gas_s, seed_compiled
    L = LSIDE; t0 = time.time()
    rng = np.random.default_rng(seed); seed_compiled(seed)
    solid = np.zeros((L, L, L), np.int8); c = L // 2
    c1, c2 = (c - sep // 2, c, c), (c - sep // 2 + sep, c, c)
    s1, d1 = ib.body(L, c1, RADIUS, solid, 1)
    s2, d2 = (s1, d1) if single else ib.body(L, c2, RADIUS, solid, 2)
    occ, sx, sy, sz = gas_s(L, RHO0, rng); occ[solid > 0] = False
    idx = np.indices((L, L, L)); edge = np.zeros((L, L, L), bool)
    for a in range(3): edge |= (idx[a] < 2) | (idx[a] >= L - 2)
    bsites = np.argwhere(edge).astype(np.int64)
    force = np.zeros((3, 3)); qw, qf = int(q), q - int(q)
    def tick():
        ib.emit(occ, sx, sy, sz, s1, d1, qw, qf, force, 1)
        if not single: ib.emit(occ, sx, sy, sz, s2, d2, qw, qf, force, 2)
        tick_s(occ, sx, sy, sz, solid, force, L, False, g, False); ib.reservoir(occ, sx, sy, sz, bsites, RHO0)
    for t in range(WARM):
        tick()
        if t % 100 == 0 and time.time() > deadline: return dict(spec=spec[:7], ran=0, note="budget reached during warm-up")
    force[:] = 0; blocks = []; last = np.zeros(2); measured = 0
    while measured < T:
        tick(); measured += 1
        if measured % BLOCK == 0:
            cur = np.array([force[1, 0], force[2, 0]]); blocks.append((cur - last) / BLOCK); last = cur
            if time.time() > deadline: break
    return dict(spec=spec[:7], ran=len(blocks) * BLOCK, blocks=np.array(blocks), secs=time.time() - t0,
                density=float(occ[(solid == 0) & ~edge].mean()))

def se(x): return x.std(ddof=1) / math.sqrt(len(x)) if len(x) > 1 else float("nan")

def main():
    t_start = time.time(); deadline = t_start + BUDGET_S
    import inertial_bodies  # compile the numba cache once before the pool starts
    specs = []
    seed = 1000
    for g, T in ((1.0, 4000), (0.1, 4000), (4.0, 3000)):
        for q in (5, 10, 2):
            for sep in (12, 20, 32):
                seed += 1; specs.append(("g%.1f" % g, g, q, sep, False, T, seed, deadline))
                seed += 1; specs.append(("g%.1f" % g, g, q, sep, True, T, seed, deadline))
    out("N grid: Q = 2, 5, 10; separations 12, 20, 32; gamma = 0.1, 1, 4; each point a pair and its single-body control (%d jobs), side %d, "
        "density %.1f, radius %d; %d warm-up ticks; 4000 measured ticks (3000 at gamma = 4); one seed per job; 6 processes; wall budget %.1f h"
        % (len(specs), LSIDE, RHO0, RADIUS, WARM, BUDGET_S / 3600))
    from multiprocessing import get_context
    with get_context("spawn").Pool(6) as pool:
        results = pool.map(job, specs, chunksize=1)
    out("N wall time %.2f h" % ((time.time() - t_start) / 3600))
    return results

def report(results):
    R = {}
    for r in results:
        tag, g, q, sep, single, T, seed = r["spec"]
        R[(g, q, sep, single)] = r
        if not r["ran"]:
            out("N gamma=%.1f Q=%d sep=%d %s: NOT RUN (%s)" % (g, q, sep, "single" if single else "pair", r["note"])); continue
        b = r["blocks"]; f = b[:, 0] if single else 0.5 * (b[:, 0] - b[:, 1])
        r["f"], r["fe"] = f.mean(), se(f)
        out("N gamma=%.1f Q=%d sep=%d %s: %d measured ticks (of %d asked), force towards the other body %+.4f +- %.4f per tick, "
            "mean free-site density %.3f (%.0f s)" % (g, q, sep, "single" if single else "pair", r["ran"], T, r["f"], r["fe"], r["density"], r["secs"]))
    out("")
    signs = {}
    for g in (0.1, 1.0, 4.0):
        mfp = (1 / math.sqrt(3)) / (6 * g * RHO0)
        out("N gamma = %.1f: product-state mean free path estimate %.2f sites" % (g, mfp))
        for q in (2, 5, 10):
            for sep in (12, 20, 32):
                p, s = R.get((g, q, sep, False)), R.get((g, q, sep, True))
                if not p or not s or not p.get("ran") or not s.get("ran"):
                    out("    Q=%2d sep=%d: not resolved (a job was cut by the budget)" % (q, sep)); continue
                F = p["f"] - s["f"]; E = math.hypot(p["fe"], s["fe"])
                ideal = q * q / (4 * math.pi * p["density"] * sep ** 2)
                sg = "repel" if F < -2 * E else ("attract" if F > 2 * E else "unresolved")
                signs[(g, q, sep)] = (sg, F, E)
                out("    Q=%2d sep=%d: net force %+.4f +- %.4f (%s); F r^2/Q^2 = %+.3f +- %.3f; ideal-fluid attraction Q^2/(4 pi rho r^2) = %.4f; "
                    "single control %+.4f +- %.4f" % (q, sep, F, E, sg, F * sep ** 2 / q ** 2, E * sep ** 2 / q ** 2, ideal, s["f"], s["fe"]))
    return signs

if __name__ == "__main__":
    results = main()
    signs = report(results)
    out("")
    parts = []
    for g in (0.1, 1.0, 4.0):
        v = [signs[k] for k in signs if k[0] == g]
        parts.append("gamma %.1f: %d repel, %d attract, %d unresolved of %d" % (g, sum(x[0] == "repel" for x in v), sum(x[0] == "attract" for x in v),
                                                                             sum(x[0] == "unresolved" for x in v), len(v)))
    out("SUMMARY: emitting pairs in block 44's sphere-menu gas (side %d, rho 0.3; 2-sigma signs of the net force, pair minus single control): %s"
        % (LSIDE, "; ".join(parts)))
