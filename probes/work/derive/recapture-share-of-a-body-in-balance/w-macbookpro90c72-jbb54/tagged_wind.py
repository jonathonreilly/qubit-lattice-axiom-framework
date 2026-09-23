"""Executed diagnostic for ATTEMPT.md (floating point, INFO only; not run by check.py).
A tagged copy of block 49's uniform-wind balanced control (supervisor_control_block49_wind.py with --pinned --balanced, and
without --balanced for the capture-only body): same tick (tick_s of probes/lib/inertial.py), same emission (emit() of the
balanced control), same seeds (1000 + sd), plus tags: on each CONTENT a weight w (1 at emission; both contents of a scattered
pair get the mean of their weights; w travels with the content through moves and exchanges) and a flag 'never scattered';
on each PARTICLE a flag 'emitted by the body' (it stays with the record on exchange). Reported over all captures: the push per
capture (captured minus emitted momentum over u times captures, as the control), the unscattered own-content share, the
own-content weight share s_w, the own-particle share, the mean x-content of the other captures, of own particles, of emissions.
usage: tagged_wind.py seeds R fill gammas [ticks]   (L = 32, rho = 0.3, b = 0.3 as the control; ticks = 40 by default)
"""
import sys, time
import numpy as np
from numba import njit
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'lib'))
from inertial import EK, INV3, scatter_pair, seed_compiled
@njit(cache=False)
def tick_t(occ, sx, sy, sz, tw, tu, tp, solid, acc, L, gamma):
    n_att = L * L * L
    for _ in range(n_att):
        x = np.random.randint(0, L); y = np.random.randint(0, L); z = np.random.randint(0, L)
        if not occ[x, y, z]: continue
        a = sx[x, y, z]; b = sy[x, y, z]; c = sz[x, y, z]
        u = np.random.random(); k = -1; s = 0.0
        for kk in range(6):
            pr = (a * EK[kk, 0] + b * EK[kk, 1] + c * EK[kk, 2]) * INV3
            if pr > 0:
                s += pr
                if u < s: k = kk; break
        if k < 0: continue
        tx = (x + EK[k, 0]) % L; ty = (y + EK[k, 1]) % L; tz = (z + EK[k, 2]) % L
        if solid[tx, ty, tz] > 0:
            occ[x, y, z] = False
            acc[0] += 1.0; acc[1] += a; acc[2] += tw[x, y, z]; acc[3] += tu[x, y, z]; acc[4] += tp[x, y, z]
            acc[5] += a * tu[x, y, z]; acc[6] += a * tp[x, y, z]
            tw[x, y, z] = 0.0; tu[x, y, z] = 0; tp[x, y, z] = 0
        elif not occ[tx, ty, tz]:
            occ[tx, ty, tz] = True; sx[tx, ty, tz] = a; sy[tx, ty, tz] = b; sz[tx, ty, tz] = c; occ[x, y, z] = False
            tw[tx, ty, tz] = tw[x, y, z]; tu[tx, ty, tz] = tu[x, y, z]; tp[tx, ty, tz] = tp[x, y, z]
            tw[x, y, z] = 0.0; tu[x, y, z] = 0; tp[x, y, z] = 0
        else:
            sx[x, y, z] = sx[tx, ty, tz]; sy[x, y, z] = sy[tx, ty, tz]; sz[x, y, z] = sz[tx, ty, tz]
            sx[tx, ty, tz] = a; sy[tx, ty, tz] = b; sz[tx, ty, tz] = c
            w0 = tw[x, y, z]; u0 = tu[x, y, z]
            tw[x, y, z] = tw[tx, ty, tz]; tu[x, y, z] = tu[tx, ty, tz]; tw[tx, ty, tz] = w0; tu[tx, ty, tz] = u0
    for _ in range(int(gamma * 3 * n_att)):
        x = np.random.randint(0, L); y = np.random.randint(0, L); z = np.random.randint(0, L); k = 2 * np.random.randint(0, 3)
        tx = (x + EK[k, 0]) % L; ty = (y + EK[k, 1]) % L; tz = (z + EK[k, 2]) % L
        if occ[x, y, z] and occ[tx, ty, tz]:
            a, b, c, a2, b2, c2 = scatter_pair(sx[x, y, z], sy[x, y, z], sz[x, y, z], sx[tx, ty, tz], sy[tx, ty, tz], sz[tx, ty, tz])
            sx[x, y, z] = a; sy[x, y, z] = b; sz[x, y, z] = c; sx[tx, ty, tz] = a2; sy[tx, ty, tz] = b2; sz[tx, ty, tz] = c2
            wm = 0.5 * (tw[x, y, z] + tw[tx, ty, tz]); tw[x, y, z] = wm; tw[tx, ty, tz] = wm; tu[x, y, z] = 0; tu[tx, ty, tz] = 0
@njit(cache=False)
def emit_t(occ, sx, sy, sz, tw, tu, tp, solid, sites, store, em, L):
    left = store
    for _ in range(store):
        i = np.random.randint(0, sites.shape[0]); k = np.random.randint(0, 6)
        tx = (sites[i, 0] + EK[k, 0]) % L; ty = (sites[i, 1] + EK[k, 1]) % L; tz = (sites[i, 2] + EK[k, 2]) % L
        if solid[tx, ty, tz] != 0 or occ[tx, ty, tz]: continue
        u = np.random.random(); cn = np.sqrt(u); st = np.sqrt(1.0 - u); ph = 2.0 * np.pi * np.random.random()
        a = k // 2; sgn = 1.0 if k % 2 == 0 else -1.0
        v = np.zeros(3); v[a] = sgn * cn; v[(a + 1) % 3] = st * np.cos(ph); v[(a + 2) % 3] = st * np.sin(ph)
        occ[tx, ty, tz] = True; sx[tx, ty, tz] = v[0]; sy[tx, ty, tz] = v[1]; sz[tx, ty, tz] = v[2]
        tw[tx, ty, tz] = 1.0; tu[tx, ty, tz] = 1; tp[tx, ty, tz] = 1
        em[0] += 1.0; em[1] += v[0]; left -= 1
    return left
def offsets(radius, fill, rng):
    out = []
    for dx in range(-radius, radius + 1):
        for dy in range(-radius, radius + 1):
            for dz in range(-radius, radius + 1):
                if dx * dx + dy * dy + dz * dz <= radius * radius and rng.random() < fill: out.append((dx, dy, dz))
    return np.array(out, np.int64)
def tilted_gas(L, rho, b, rng):
    occ = rng.random((L, L, L)) < rho
    U = rng.random((L, L, L)); mu = np.log(np.exp(-b) + U * (np.exp(b) - np.exp(-b))) / b
    phi = 2 * np.pi * rng.random((L, L, L)); r = np.sqrt(np.maximum(0.0, 1 - mu * mu))
    return occ, mu.copy(), (r * np.cos(phi)).copy(), (r * np.sin(phi)).copy()
def run(L, rho0, gamma, bt, ticks, seeds, R, fill, balanced, offset=0):
    u = 1 / np.tanh(bt) - 1 / bt
    tot = np.zeros(7); emt = np.zeros(2); P = 0.0; fracs = []; ratio_num = []; ratio_den = []
    for sd in range(seeds):
        rng = np.random.default_rng(1000 + offset + sd); seed_compiled(1000 + offset + sd)
        offs = offsets(R, fill, rng)
        while len(offs) < 3: offs = offsets(R, fill, rng)
        occ, sx, sy, sz = tilted_gas(L, rho0, bt, rng); solid = np.zeros((L, L, L), np.int8)
        s = (np.array([L // 2] * 3)[None, :] + offs) % L; solid[s[:, 0], s[:, 1], s[:, 2]] = 1; occ[solid > 0] = False
        tw = np.zeros((L, L, L)); tu = np.zeros((L, L, L), np.int8); tp = np.zeros((L, L, L), np.int8)
        acc = np.zeros(7); em = np.zeros(2); store = 0; M0 = float(len(offs))
        for t in range(ticks):
            before = acc[0]
            tick_t(occ, sx, sy, sz, tw, tu, tp, solid, acc, L, gamma)
            if balanced:
                store += int(round(acc[0] - before)); store = emit_t(occ, sx, sy, sz, tw, tu, tp, solid, s.astype(np.int64), store, em, L)
        Pn = acc[1] - em[1]; M = M0 + acc[0]
        ratio_num.append(Pn / M); ratio_den.append(acc[0] / M)
        tot += acc; emt += em
    push = np.mean(ratio_num) / (u * np.mean(ratio_den))
    C = tot[0]
    return dict(push=push, captures_per_seed=C / seeds, share_unscattered_content=tot[3] / C, share_content_weight=tot[2] / C,
                share_particle=tot[4] / C, px_untagged=(tot[1] - tot[5]) / max(1, C - tot[3]) / u, px_own_particle=tot[6] / max(1, tot[4]) / u,
                emitted_px=emt[1] / max(1, emt[0]) / u)
if __name__ == "__main__":
    L, rho0, bt, seeds = 32, 0.3, 0.3, int(sys.argv[1])
    ticks = int(sys.argv[5]) if len(sys.argv) > 5 else 40
    R, fill = int(sys.argv[2]), float(sys.argv[3])
    for g in map(float, sys.argv[4].split(',')):
        for bal in (True, False):
            t0 = time.time(); r = run(L, rho0, g, bt, ticks, seeds, R, fill, bal)
            print(f"R={R} fill={fill} gamma={g} {'balanced' if bal else 'capture '}: " + ", ".join(f"{k} {v:.4f}" for k, v in r.items()) + f" ({time.time()-t0:.0f} s)", flush=True)
