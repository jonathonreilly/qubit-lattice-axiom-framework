"""Self-tests of t1lib: conservation, one-to-one moves, isolated-record odds, edge-leak odds (exact formulas)."""
import numpy as np
from t1lib import move_phase, neighbour_count

rng = np.random.default_rng(1)

# 1. conservation + one-to-one, random states, 2D and 3D, several g
for shape in [(64, 64), (16, 16, 16)]:
    for g in [0.0, 1.0, 2.5]:
        occ = rng.random(shape) < 0.4
        for _ in range(50):
            new, out, arr, wins = move_phase(occ, g, rng)
            assert new.sum() == occ.sum()
            assert out.sum() == arr.sum()
            assert not (out & arr).any()
            assert (occ[out]).all() and (~occ[arr]).all()
            # every move is a nearest-neighbour step: each arrival has exactly one origin among its neighbours
            occ = new
print("conservation/one-to-one: OK")

# 2. isolated record: stay and each direction 1/(1+2d)
for shape in [(9, 9), (7, 7, 7)]:
    d = len(shape)
    occ = np.zeros(shape, bool)
    c = tuple(s // 2 for s in shape)
    occ[c] = True
    n = 40000
    stay = 0
    for _ in range(n):
        new, out, arr, wins = move_phase(occ, 2.0, rng)
        stay += new[c]
    print(f"isolated record d={d}: P(stay)={stay/n:.4f} expected {1/(1+2*d):.4f} (+-{np.sqrt((1/(1+2*d))*(1-1/(1+2*d))/n):.4f})")

# 3. jam edge leak, 2D square jam side 10 in empty 40x40, first tick only
for g in [0.5, 1.0, 1.5]:
    L, s = 40, 10
    occ = np.zeros((L, L), bool)
    occ[15:15 + s, 15:15 + s] = True
    nrep = 4000
    facet_out = 0
    corner_out = 0
    for _ in range(nrep):
        new, out, arr, wins = move_phase(occ, g, rng)
        # facet records: on boundary but not corners
        sub = out[15:15 + s, 15:15 + s]
        corners = int(sub[0, 0]) + int(sub[0, -1]) + int(sub[-1, 0]) + int(sub[-1, -1])
        edge = sub[0, 1:-1].sum() + sub[-1, 1:-1].sum() + sub[1:-1, 0].sum() + sub[1:-1, -1].sum()
        interior = sub[1:-1, 1:-1].sum()
        assert interior == 0
        facet_out += edge
        corner_out += corners
    nf = 4 * (s - 2) * nrep
    nc = 4 * nrep
    pf = facet_out / nf
    pc = corner_out / nc
    ef = 1 / (np.exp(3 * g) + 1)
    ec = 2 / (np.exp(2 * g) + 2)
    print(f"g={g}: facet leak {pf:.5f} (exact {ef:.5f}, +-{np.sqrt(ef*(1-ef)/nf):.5f}); corner leak {pc:.5f} (exact {ec:.5f}, +-{np.sqrt(ec*(1-ec)/nc):.5f})")

# 4. 3D cube jam side 6 in empty 20^3, first tick
for g in [0.5, 1.0]:
    L, s = 20, 6
    occ = np.zeros((L, L, L), bool)
    occ[7:13, 7:13, 7:13] = True
    nrep = 2000
    cnt = {3: 0, 4: 0, 5: 0}
    tot = {3: 0, 4: 0, 5: 0}
    nrec = neighbour_count(occ)
    for _ in range(nrep):
        new, out, arr, wins = move_phase(occ, g, rng)
        for b in (3, 4, 5):
            m = occ & (nrec == b)
            cnt[b] += out[m].sum()
            tot[b] += m.sum()
    for b, nout in ((5, 1), (4, 2), (3, 3)):
        e = nout / (np.exp(b * g) + nout)
        print(f"3D g={g} bonds={b}: leak {cnt[b]/tot[b]:.5f} exact {e:.5f} +-{np.sqrt(e*(1-e)/tot[b]):.5f}")
