"""
A36 check C2: the record cone when each spot's firing instants are chosen by its recorded neighbours.

Supplied classical toy (gated growth, A28 rule; A32 D7 for comparison):
- one seed record at the origin; an empty site with k >= 1 recorded nearest neighbours is gate-open;
- a shared dial with L fine instants per cycle; a gate-open site fires at the fine instants chosen by
  its recorded-neighbour count k;
- at a firing the site forms a record with a chance; gate and k are evaluated on the records present
  at the START of the fine instant (start-of-instant reading).
Schedules compared (chance per cycle F for every site in every schedule unless stated):
  G      : one shared tick (L = 1; every gate-open site fires once per cycle, chance F);
  UP     : one firing per cycle, at instant k-1 of an L = 2d dial (phase rises with k);
  DOWN   : one firing per cycle, at instant 2d-k (phase falls with k);
  PER    : L = 2 dial; k = 1 sites fire at both instants with chance F/2 each (period halved, chance
           per firing halved: P1), k >= 2 sites fire at instant 0 with chance F;
  PERfix : as PER but chance F at every firing (fixed chance per firing: P1'), so k = 1 sites get
           twice the formation rate.
Checks: (a) F = 1 shapes and reaches (deterministic); (b) the strict bound
'L1 reach <= number of fine instants elapsed' (asserted at every instant); (c) small-F speeds.
"""
import signal, time
import numpy as np
signal.alarm(55)
t0 = time.time()

def nbr_count(rec):
    k = np.zeros(rec.shape, dtype=np.int8)
    for ax in range(rec.ndim):
        for sh in (1, -1):
            k += np.roll(rec, sh, axis=ax)
    return k

def chance(schedule, dim, k, j, F):
    """Chance of forming at fine instant j for a site with k recorded neighbours (array k)."""
    z = np.zeros(k.shape)
    if schedule == 'G':
        z[k >= 1] = F
    elif schedule == 'UP':
        z[k == j + 1] = F
    elif schedule == 'DOWN':
        z[(k == 2 * dim - j) & (k >= 1)] = F
    elif schedule in ('PER', 'PERfix'):
        z[k == 1] = F / 2 if schedule == 'PER' else F
        if j == 0:
            z[k >= 2] = F
    return z

LK = {'G': None, 'UP': None, 'DOWN': None, 'PER': 2, 'PERfix': 2}

def grow(dim, R, schedule, ncyc, F, rng=None, stop_reach=None):
    shape = (2 * R + 1,) * dim
    rec = np.zeros(shape, dtype=np.int8)
    rec[(R,) * dim] = 1
    L = {'G': 1, 'UP': 2 * dim, 'DOWN': 2 * dim, 'PER': 2, 'PERfix': 2}[schedule]
    grids = np.indices(shape) - R
    l1 = np.abs(grids).sum(axis=0)
    linf = np.abs(grids).max(axis=0)
    axis_line = tuple([slice(R, 2 * R + 1)] + [R] * (dim - 1))
    hist = []
    nfine = 0
    for n in range(ncyc):
        for j in range(L):
            k = nbr_count(rec)
            p = chance(schedule, dim, k, j, F) * (rec == 0)
            if F >= 1 and schedule not in ('PER',):
                form = p >= 1
            else:
                form = rng.random(shape) < p
            rec[form] = 1
            nfine += 1
            assert int(l1[rec == 1].max()) <= nfine, "strict cone per fine instant violated"
        rr = rec == 1
        ax = rec[axis_line]
        axis_reach = int(np.max(np.nonzero(ax)[0]))
        hist.append((n + 1, nfine, int(l1[rr].max()), int(linf[rr].max()), axis_reach, int(rr.sum())))
        if stop_reach is not None and int(linf[rr].max()) >= stop_reach:
            break
    return hist

print("C2a. F = 1 (deterministic), seed at the origin. Reaches after n cycles:")
print("     L1 reach (lattice steps), Linf reach, reach along an axis, recorded sites.")
for dim, R, ncyc in ((2, 40, 12), (3, 20, 8)):
    for sch in ('G', 'UP', 'DOWN'):
        h = grow(dim, R, sch, ncyc, 1.0)
        last = h[-1]
        print(f"  {dim}D {sch:<5} {last[0]:>2} cycles = {last[1]:>3} fine instants: L1 {last[2]:>3}, "
              f"Linf {last[3]:>3}, axis {last[4]:>3}, sites {last[5]:>6}")
print(f"  [elapsed {time.time()-t0:.1f}s]")

print("\nC2b. Small F (chance per cycle), 2D, seed at origin; cycles needed to reach Linf distance 30.")
print("     ratio = cycles(G) / cycles(schedule) (> 1 means faster than one shared tick).")
rng = np.random.default_rng(7)
for F, reps in ((0.4, 40), (0.2, 40), (0.1, 30), (0.05, 16)):
    res = {}
    for sch in ('G', 'UP', 'DOWN', 'PER', 'PERfix'):
        cyc = [grow(2, 33, sch, 9000, F, rng=rng, stop_reach=30)[-1][0] for _ in range(reps)]
        res[sch] = (np.mean(cyc), np.std(cyc) / np.sqrt(len(cyc)))
    g, ge = res['G']
    def ratio(s):
        m, e = res[s]
        r = g / m
        return r, r * np.sqrt((ge / g) ** 2 + (e / m) ** 2)
    line = "  ".join(f"{s} {res[s][0]:.1f} ({ratio(s)[0]:.3f}+-{ratio(s)[1]:.3f})" for s in res)
    print(f"  F={F}: {line}")
    print(f"  [elapsed {time.time()-t0:.1f}s]")
