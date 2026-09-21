"""Block 49 control core (floating point; not the runner; identical to block 44's seeded simulator): the inertial clause, both menus.
usage: supervisor_control_block49_inertial.py six|sphere side density gamma   (standing density waves against the product-closure speed)
(S) streaming: a record tries to step along its content (six axes: to x + e_d with probability 1 per attempt; sphere: to x + e_k with probability
    max(0, s.e_k)/sqrt(3)); an empty target is entered; an occupied target exchanges contents with the record.
(C) scattering: a bond picked at random (gamma * 3 L^3 picks per tick) whose two ends are occupied re-draws the two contents uniformly on their
    momentum class (six axes: an opposite pair becomes a uniformly random opposite pair, other pairs exchange with probability 1/2;
    sphere: P/2 +- r w with w uniform on the circle orthogonal to P).
Number and momentum are conserved by every event and the uniform measure is stationary (exact: the block's runner and refuter)."""
import sys, time
import numpy as np
from numba import njit

EK = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], np.int64)
INV3 = 1.0 / np.sqrt(3.0)

@njit(cache=True)
def seed_compiled(seed):
    np.random.seed(seed)                      # the compiled code has its own generator; numpy's seed does not reach it


@njit(cache=True)
def rand_unit():
    while True:
        a = np.random.normal(); b = np.random.normal(); c = np.random.normal(); n = np.sqrt(a * a + b * b + c * c)
        if n > 1e-9: return a / n, b / n, c / n

@njit(cache=True)
def scatter_pair(a, b, c, a2, b2, c2):
    px = a + a2; py = b + b2; pz = c + c2; p2 = px * px + py * py + pz * pz
    r = np.sqrt(max(0.0, 1.0 - 0.25 * p2)); wx, wy, wz = rand_unit()
    if p2 > 1e-12:
        dot = (wx * px + wy * py + wz * pz) / p2; wx -= dot * px; wy -= dot * py; wz -= dot * pz
        n = np.sqrt(wx * wx + wy * wy + wz * wz)
        if n < 1e-9: return a, b, c, a2, b2, c2
        wx /= n; wy /= n; wz /= n
    return 0.5 * px + r * wx, 0.5 * py + r * wy, 0.5 * pz + r * wz, 0.5 * px - r * wx, 0.5 * py - r * wy, 0.5 * pz - r * wz

@njit(cache=True)
def tick_s(occ, sx, sy, sz, solid, force, L, periodic, gamma, absorb):
    n_att = L * L * L
    for _ in range(n_att):
        x = np.random.randint(0, L); y = np.random.randint(0, L); z = np.random.randint(0, L)
        if not occ[x, y, z]: continue
        a = sx[x, y, z]; b = sy[x, y, z]; c = sz[x, y, z]
        u = np.random.random(); k = -1; acc = 0.0
        for kk in range(6):
            p = (a * EK[kk, 0] + b * EK[kk, 1] + c * EK[kk, 2]) * INV3
            if p > 0:
                acc += p
                if u < acc: k = kk; break
        if k < 0: continue
        tx = x + EK[k, 0]; ty = y + EK[k, 1]; tz = z + EK[k, 2]
        if periodic: tx %= L; ty %= L; tz %= L
        elif tx < 0 or tx >= L or ty < 0 or ty >= L or tz < 0 or tz >= L:
            occ[x, y, z] = False; continue
        bid = solid[tx, ty, tz]
        if bid > 0:
            if absorb:
                occ[x, y, z] = False; force[bid, 0] += a; force[bid, 1] += b; force[bid, 2] += c; force[0, bid] += 1.0
            else:
                sn = a * EK[k, 0] + b * EK[k, 1] + c * EK[k, 2]
                sx[x, y, z] = a - 2 * sn * EK[k, 0]; sy[x, y, z] = b - 2 * sn * EK[k, 1]; sz[x, y, z] = c - 2 * sn * EK[k, 2]
                force[bid, 0] += 2 * sn * EK[k, 0]; force[bid, 1] += 2 * sn * EK[k, 1]; force[bid, 2] += 2 * sn * EK[k, 2]
        elif not occ[tx, ty, tz]:
            occ[tx, ty, tz] = True; sx[tx, ty, tz] = a; sy[tx, ty, tz] = b; sz[tx, ty, tz] = c; occ[x, y, z] = False
        else:
            sx[x, y, z] = sx[tx, ty, tz]; sy[x, y, z] = sy[tx, ty, tz]; sz[x, y, z] = sz[tx, ty, tz]
            sx[tx, ty, tz] = a; sy[tx, ty, tz] = b; sz[tx, ty, tz] = c
    for _ in range(int(gamma * 3 * n_att)):
        x = np.random.randint(0, L); y = np.random.randint(0, L); z = np.random.randint(0, L); k = 2 * np.random.randint(0, 3)
        tx = x + EK[k, 0]; ty = y + EK[k, 1]; tz = z + EK[k, 2]
        if periodic: tx %= L; ty %= L; tz %= L
        elif tx >= L or ty >= L or tz >= L: continue
        if occ[x, y, z] and occ[tx, ty, tz]:
            a, b, c, a2, b2, c2 = scatter_pair(sx[x, y, z], sy[x, y, z], sz[x, y, z], sx[tx, ty, tz], sy[tx, ty, tz], sz[tx, ty, tz])
            sx[x, y, z] = a; sy[x, y, z] = b; sz[x, y, z] = c; sx[tx, ty, tz] = a2; sy[tx, ty, tz] = b2; sz[tx, ty, tz] = c2

@njit(cache=True)
def tick6(dirn, L, gamma):
    n_att = L * L * L
    for _ in range(n_att):
        x = np.random.randint(0, L); y = np.random.randint(0, L); z = np.random.randint(0, L); d = dirn[x, y, z]
        if d < 0: continue
        tx = (x + EK[d, 0]) % L; ty = (y + EK[d, 1]) % L; tz = (z + EK[d, 2]) % L; d2 = dirn[tx, ty, tz]
        dirn[tx, ty, tz] = d; dirn[x, y, z] = d2                     # move (d2 = -1) or exchange
    for _ in range(int(gamma * 3 * n_att)):
        x = np.random.randint(0, L); y = np.random.randint(0, L); z = np.random.randint(0, L); k = 2 * np.random.randint(0, 3)
        tx = (x + EK[k, 0]) % L; ty = (y + EK[k, 1]) % L; tz = (z + EK[k, 2]) % L
        d = dirn[x, y, z]; d2 = dirn[tx, ty, tz]
        if d < 0 or d2 < 0: continue
        if d2 == (d ^ 1):
            e = np.random.randint(0, 6); dirn[x, y, z] = e; dirn[tx, ty, tz] = e ^ 1
        elif np.random.random() < 0.5:
            dirn[x, y, z] = d2; dirn[tx, ty, tz] = d

def gas_s(L, rho, rng, profile=None):
    occ = rng.random((L, L, L)) < (rho if profile is None else profile)
    v = rng.normal(size=(L, L, L, 3)); v /= np.linalg.norm(v, axis=-1, keepdims=True)
    return occ, v[..., 0].copy(), v[..., 1].copy(), v[..., 2].copy()

def sound(menu, L, rho0, gamma, modes, T, runs, seed=1, eps=0.2):
    rng = np.random.default_rng(seed); seed_compiled(seed); xs = np.arange(L); out = {}
    solid = np.zeros((L, L, L), np.int8); force = np.zeros((3, 3))
    for mode in modes:
        k = 2 * np.pi * mode / L; amps = np.zeros(T + 1)
        for _ in range(runs):
            prof = rho0 * (1 + eps * np.cos(k * xs))[:, None, None] * np.ones((L, L, L))
            if menu == "six":
                dirn = np.full((L, L, L), -1, np.int8); o = rng.random((L, L, L)) < prof; dirn[o] = rng.integers(0, 6, o.sum())
            else: occ, sx, sy, sz = gas_s(L, rho0, rng, prof)
            for t in range(T + 1):
                dens = ((dirn >= 0) if menu == "six" else occ).sum(axis=(1, 2)) / L ** 2
                amps[t] += 2 * np.mean(dens * np.cos(k * xs)) / (rho0 * eps) / runs
                if menu == "six": tick6(dirn, L, gamma)
                else: tick_s(occ, sx, sy, sz, solid, force, L, True, gamma, False)
        out[mode] = amps
    return out

def fit_damped(amps, k):
    """least squares for A exp(-g t) cos(w t): grid over (g, w)"""
    t = np.arange(len(amps)); best = None
    for w in np.linspace(0.2 * k, 1.2 * k, 201):
        for g in np.linspace(0.0, 0.08, 81):
            model = np.exp(-g * t) * np.cos(w * t); A = (model @ amps) / (model @ model); err = ((amps - A * model) ** 2).sum()
            if best is None or err < best[0]: best = (err, w, g, A)
    _, w, g, A = best
    return np.sqrt(w * w + g * g) / k, w / k, g

if __name__ == "__main__":
    menu, L, rho0, gamma = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
    pred = np.sqrt((1 - rho0) / 3) if menu == "six" else np.sqrt(1 - rho0) / 3
    t0 = time.time(); res = sound(menu, L, rho0, gamma, (1, 2), 300, 4)
    for mode, amps in res.items():
        k = 2 * np.pi * mode / L; c, c_raw, g = fit_damped(amps, k)
        print(f"{menu} menu, side {L}, density {rho0}, gamma {gamma}, mode {mode}: fitted speed sqrt(w^2 + g^2)/k = {c:.3f} (w/k = {c_raw:.3f}, damping {g:.4f} per tick); product-closure prediction {pred:.3f};  amplitude every 30 ticks: " + " ".join(f"{amps[t]:+.2f}" for t in range(0, 301, 30)))
    print(f"   {time.time() - t0:.0f} s")
