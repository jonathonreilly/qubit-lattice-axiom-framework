"""A FREE capturing body in the sphere-menu inertial gas.
Body clause (supplied): a body is a rigid set of N capturing sites with a mass M (the records it holds) and a momentum P (the sum of their contents);
once per tick it steps along e_k with probability max(0, (P/M).e_k)/sqrt 3 (the streaming rule of a record whose content is the body's mean content);
records found on the sites it enters are captured; a captured record adds one to M and its content to P.
usage: inertial_free_body.py wind L rho0 gamma b ticks seeds R fill      (periodic box, gas with content law ~ exp(b s_x); dilution law p = u (M - M0)/M)
       inertial_free_body.py fall L rho0 gamma sep warm ticks seeds R1 f1 R2 f2   (open box with a reservoir; body 1 fixed, body 2 released after the warm-up)"""
import sys, time
import numpy as np
from inertial import tick_s, gas_s, seed_compiled, EK
from inertial_porous_bodies import reservoir

C = 1.0 / np.sqrt(3.0)
PINNED = "--pinned" in sys.argv
OFFSET = int(sys.argv[sys.argv.index("--offset") + 1]) if "--offset" in sys.argv else 0

def offsets(radius, fill, rng):
    out = []
    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):
            for dz in range(-radius, radius + 1):
                if dx * dx + dy * dy + dz * dz <= radius * radius and rng.random() < fill: out.append((dx, dy, dz))
    return np.array(out, np.int64)

def place(solid, centre, offs, bid, L, periodic):
    s = centre[None, :] + offs
    if periodic: s %= L
    solid[s[:, 0], s[:, 1], s[:, 2]] = bid
    return s

def body_step(state, solid, occ, sx, sy, sz, offs, bid, L, periodic, rng):
    """One move attempt of the free body; returns the step taken (0 if none)."""
    centre, P, M = state["centre"], state["P"], state["M"]
    p = P / M; probs = np.maximum(0.0, EK @ p) * C; u = rng.random(); acc = 0.0; k = -1
    for kk in range(6):
        acc += probs[kk]
        if u < acc: k = kk; break
    if k < 0: return 0
    old = centre[None, :] + offs
    if periodic: old %= L
    solid[old[:, 0], old[:, 1], old[:, 2]] = 0
    centre += EK[k]
    new = place(solid, centre, offs, bid, L, periodic)
    hit = occ[new[:, 0], new[:, 1], new[:, 2]]
    if hit.any():
        h = new[hit]
        state["P"] = P + np.array([sx[h[:, 0], h[:, 1], h[:, 2]].sum(), sy[h[:, 0], h[:, 1], h[:, 2]].sum(), sz[h[:, 0], h[:, 1], h[:, 2]].sum()])
        state["M"] = M + hit.sum(); state["swept"] += hit.sum()
        occ[h[:, 0], h[:, 1], h[:, 2]] = False
    return 1

def tilted_gas(L, rho, b, rng):
    occ = rng.random((L, L, L)) < rho
    U = rng.random((L, L, L)); mu = np.log(np.exp(-b) + U * (np.exp(b) - np.exp(-b))) / b
    phi = 2 * np.pi * rng.random((L, L, L)); r = np.sqrt(np.maximum(0.0, 1 - mu * mu))
    return occ, mu.copy(), (r * np.cos(phi)).copy(), (r * np.sin(phi)).copy()

def wind(L, rho0, gamma, b, ticks, seeds, R, fill):
    u = 1 / np.tanh(b) - 1 / b
    pt = np.zeros((seeds, ticks, 3)); fr = np.zeros((seeds, ticks)); X = np.zeros((seeds, ticks)); sw = np.zeros(seeds); n_sites = []
    for sd in range(seeds):
        rng = np.random.default_rng(1000 + sd); seed_compiled(1000 + sd)
        offs = offsets(R, fill, rng)
        while len(offs) < 3: offs = offsets(R, fill, rng)
        n_sites.append(len(offs))
        occ, sx, sy, sz = tilted_gas(L, rho0, b, rng); solid = np.zeros((L, L, L), np.int8)
        state = {"centre": np.array([L // 2] * 3, np.int64), "P": np.zeros(3), "M": float(len(offs)), "swept": 0}
        s = place(solid, state["centre"], offs, 1, L, True); occ[s[:, 0], s[:, 1], s[:, 2]] = False
        force = np.zeros((3, 3)); M0 = state["M"]; x0 = 0
        for t in range(ticks):
            force[:] = 0
            tick_s(occ, sx, sy, sz, solid, force, L, True, gamma, True)
            state["P"] = state["P"] + force[1]; state["M"] += force[0, 1]
            x_before = state["centre"][0]
            if not PINNED: body_step(state, solid, occ, sx, sy, sz, offs, 1, L, True, rng)
            x0 += state["centre"][0] - x_before
            pt[sd, t] = state["P"] / state["M"]; fr[sd, t] = (state["M"] - M0) / state["M"]; X[sd, t] = x0
        sw[sd] = state["swept"] / max(1.0, state["M"] - M0)
    print(f"WIND L={L} rho={rho0} gamma={gamma} b={b} (u = {u:.4f}) seeds={seeds} sites/body={np.mean(n_sites):.1f}; swept share of captures {sw.mean():.3f}")
    print(" tick  captured-fraction   p_x/u (measured)   p_x/u over captured fraction    p_y/u    p_z/u    X/(c u sum frac)")
    e = lambda v: v.std(ddof=1) / np.sqrt(len(v))
    for t in sorted(set([max(1, ticks // 16), ticks // 8, ticks // 4, ticks // 2, 3 * ticks // 4, ticks - 1])):
        ratio = pt[:, t, 0].mean() / (u * fr[:, t].mean()); pred_x = C * u * fr[:, : t + 1].mean(axis=0).sum()
        print(f" {t + 1:4d}   {fr[:, t].mean():.3f}               {pt[:, t, 0].mean() / u:+.3f}+-{e(pt[:, t, 0]) / u:.3f}       {ratio:+.3f}+-{e(pt[:, t, 0]) / (u * fr[:, t].mean()):.3f}                 {pt[:, t, 1].mean() / u:+.3f}   {pt[:, t, 2].mean() / u:+.3f}   {X[:, t].mean() / pred_x:+.3f}+-{e(X[:, t]) / pred_x:.3f}")

def fall(L, rho0, gamma, sep, warm, ticks, seeds, R1, f1, R2, f2):
    drift = np.zeros((seeds, ticks)); pr = np.zeros((seeds, ticks)); fr = np.zeros((seeds, ticks)); Q1s = []; n1s = []; n2s = []
    for sd in range(seeds):
        rng = np.random.default_rng(5000 + OFFSET + sd); seed_compiled(5000 + OFFSET + sd)
        o1 = offsets(R1, f1, rng); o2 = offsets(R2, f2, rng)
        while len(o2) < 3: o2 = offsets(R2, f2, rng)
        n1s.append(len(o1)); n2s.append(len(o2))
        solid = np.zeros((L, L, L), np.int8); c = L // 2
        c1 = np.array([c - sep // 2, c, c], np.int64); state = {"centre": np.array([c - sep // 2 + sep, c, c], np.int64), "P": np.zeros(3), "M": float(len(o2)), "swept": 0}
        place(solid, c1, o1, 1, L, False); place(solid, state["centre"], o2, 2, L, False)
        occ, sx, sy, sz = gas_s(L, rho0, rng); occ[solid > 0] = False
        idx = np.indices((L, L, L)); edge = np.zeros((L, L, L), bool)
        for a in range(3): edge |= (idx[a] < 2) | (idx[a] >= L - 2)
        bsites = np.argwhere(edge).astype(np.int64); force = np.zeros((3, 3)); q1 = 0.0
        for t in range(warm):
            force[:] = 0; tick_s(occ, sx, sy, sz, solid, force, L, False, gamma, True); reservoir(occ, sx, sy, sz, bsites, rho0)
            if t >= warm // 2: q1 += force[0, 1]
        Q1s.append(q1 / (warm - warm // 2)); M0 = state["M"]; x_start = state["centre"][0]
        for t in range(ticks):
            force[:] = 0; tick_s(occ, sx, sy, sz, solid, force, L, False, gamma, True); reservoir(occ, sx, sy, sz, bsites, rho0)
            state["P"] = state["P"] + force[2]; state["M"] += force[0, 2]
            if 4 < state["centre"][0] - c1[0] - R1 - R2:                       # stop stepping when the balls touch
                body_step(state, solid, occ, sx, sy, sz, o2, 2, L, False, rng)
            drift[sd, t] = x_start - state["centre"][0]; pr[sd, t] = -state["P"][0] / state["M"]; fr[sd, t] = (state["M"] - M0) / state["M"]
    Q1 = np.mean(Q1s); e = lambda v: v.std(ddof=1) / np.sqrt(len(v))
    if "--save" in sys.argv: np.savez(sys.argv[sys.argv.index("--save") + 1], drift=drift, pr=pr, fr=fr, Q1s=np.array(Q1s), n1s=np.array(n1s), n2s=np.array(n2s))
    print(f"FALL L={L} rho={rho0} gamma={gamma} sep={sep} warm={warm} seeds={seeds}; body 1 fixed: sites {np.mean(n1s):.1f}, Q1 = {Q1:.2f}; body 2 free: sites {np.mean(n2s):.1f}")
    print(" tick   drift towards body 1 (sites)   -p_x (towards body 1)   captured fraction   quasi-static prediction of the drift")
    pred = np.zeros(ticks); r = float(sep); acc = 0.0; frm = fr.mean(axis=0)
    for t in range(ticks):
        uw = np.sqrt(3) * Q1 / (4 * np.pi * r * r * rho0 * (1 - rho0)); acc += C * uw * frm[t]; r = max(sep - acc, R1 + R2 + 4.0); pred[t] = acc
    for t in sorted(set([ticks // 16, ticks // 8, ticks // 4, ticks // 2, 3 * ticks // 4, ticks - 1])):
        print(f" {t + 1:4d}   {drift[:, t].mean():+.2f}+-{e(drift[:, t]):.2f}                  {pr[:, t].mean():+.4f}+-{e(pr[:, t]):.4f}          {frm[t]:.3f}               {pred[t]:+.2f}")

if __name__ == "__main__":
    t0 = time.time(); a = sys.argv
    if a[1] == "wind": wind(int(a[2]), float(a[3]), float(a[4]), float(a[5]), int(a[6]), int(a[7]), int(a[8]), float(a[9]))
    else: fall(int(a[2]), float(a[3]), float(a[4]), int(a[5]), int(a[6]), int(a[7]), int(a[8]), int(a[9]), float(a[10]), int(a[11]), float(a[12]))
    print(f"({time.time() - t0:.0f} s)")
