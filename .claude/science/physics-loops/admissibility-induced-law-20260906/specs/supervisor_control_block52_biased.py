"""Block 52 control core (floating point; not the runner): the BIASED-WALK streaming clause, sphere menu.
A record of content s hops to x + e with probability (1 + s.e)/6 for each of the six lattice directions e (mean displacement s/3, second moment
delta/3 whatever the content); an empty target is entered, an occupied target exchanges contents, a solid target captures; bonds re-draw their
pair of contents on the momentum class at rate gamma, as in block 44."""
import numpy as np
from numba import njit
from supervisor_control_block52_inertial import EK, INV3, scatter_pair, rand_unit, seed_compiled, gas_s

@njit(cache=True)
def tick_b(occ, sx, sy, sz, solid, force, L, periodic, gamma, absorb):
    n_att = L * L * L
    for _ in range(n_att):
        x = np.random.randint(0, L); y = np.random.randint(0, L); z = np.random.randint(0, L)
        if not occ[x, y, z]: continue
        a = sx[x, y, z]; b = sy[x, y, z]; c = sz[x, y, z]
        u = np.random.random(); k = 5; acc = 0.0
        for kk in range(6):                                  # symmetric walk biased by the content: direction kk with probability (1 + s.e_kk)/6
            acc += (1.0 + a * EK[kk, 0] + b * EK[kk, 1] + c * EK[kk, 2]) / 6.0
            if u < acc: k = kk; break
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

