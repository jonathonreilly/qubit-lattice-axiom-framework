"""moving_gas.py p q r scale rho L sweeps seed [mode]

Records that MOVE on the periodic cubic lattice (Z/L)^3, L divisible by 4.  A site is empty or carries one record whose content is one of
the six axes; content is carried.  Pair weight of two neighbouring records: W(a, b) = c * omega(a, b), omega = p, q, r for equal, opposite,
orthogonal axes; a bond with an empty end weighs 1.  `scale` is c, or the word `neutral` for c = 6/(p + q + 4r) (an empty neighbour then
weighs what a record of uniformly random content weighs on average).  MOTION: a bond with exactly one occupied end is visited; the record
chooses between its two positions in proportion to the pair weights it would have there (detailed balance with the static law on the
occupied set, contents fixed).  One sweep visits every bond once, in 48 sublattice passes whose bonds do not interact.
Start: records placed uniformly at random at density rho with uniformly random contents.
Output: a table over time and a SUMMARY line: nbrs = mean number of recorded neighbours per record (6 rho if placed at random);
aligned = fraction of record-record bonds with equal contents (1/6 at random); accept = fraction of proposed moves accepted;
S = density structure factor at the smallest wavevector (order 1 if uniform, order N if clumped)."""
import numpy as np, sys, time
p, q, r = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]); scale_arg = sys.argv[4]; rho = float(sys.argv[5]); L = int(sys.argv[6]); sweeps = int(sys.argv[7]); seed = int(sys.argv[8])
mode = sys.argv[9] if len(sys.argv) > 9 else "parallel"
c = 6.0 / (p + q + 4 * r) if scale_arg == "neutral" else float(scale_arg)
rng = np.random.default_rng(seed); N = L ** 3
LW = np.zeros((6, 7))                      # log pair weight of content a (row) with neighbour content b (col); column 6 = empty neighbour
for a in range(6):
    for b in range(6): LW[a, b] = np.log(c * (p if a == b else q if a == (b ^ 1) else r))
state = np.full((L, L, L), 6, dtype=np.int64); occ = rng.random((L, L, L)) < rho; state[occ] = rng.integers(0, 6, occ.sum())
def shifted(arr, d, s): return np.roll(arr, -s, axis=d)          # value at x + s e_d
def measure(state):
    occ = state < 6; n = occ.sum(); nb = 0.0; al = 0.0; bonds = 0
    for d in range(3):
        o2 = shifted(state, d, 1); both = occ & (o2 < 6); bonds += both.sum(); al += (both & (state == o2)).sum()
    nbrs = 2.0 * bonds / max(n, 1); aligned = al / max(bonds, 1)
    f = np.fft.fftn(occ - occ.mean()); S = np.mean([abs(f[1, 0, 0]) ** 2, abs(f[0, 1, 0]) ** 2, abs(f[0, 0, 1]) ** 2]) / N
    return nbrs, aligned, S
def logw_at(state, content, d, side):
    """log weight content would have at x (side 0) or at x + e_d (side 1), the other end of the bond excluded; arrays indexed by x"""
    tot = np.zeros(state.shape)
    for dd in range(3):
        for s in (1, -1):
            if dd == d and ((side == 0 and s == 1) or (side == 1 and s == -1)): continue      # the bond's other end
            nbr = shifted(state, dd, s) if side == 0 else shifted(shifted(state, d, 1), dd, s)
            tot += LW[np.minimum(content, 5), nbr]
    return tot
idx = np.indices((L, L, L)); prop = acc = 0
def sweep_parallel():
    global state, prop, acc
    passes = [(d, o, t1, t2) for d in range(3) for o in range(4) for t1 in range(2) for t2 in range(2)]
    rng.shuffle(passes)
    for d, o, t1, t2 in passes:
        tr = [a for a in range(3) if a != d]
        sel = (idx[d] % 4 == o) & (idx[tr[0]] % 2 == t1) & (idx[tr[1]] % 2 == t2)
        other = shifted(state, d, 1); ox, oy = state < 6, other < 6
        fwd = sel & ox & ~oy; bwd = sel & ~ox & oy                     # record at x moves to x+e_d, or record at x+e_d moves to x
        content = np.where(fwd, state, np.where(bwd, other, 0))
        lw0 = logw_at(state, content, d, 0); lw1 = logw_at(state, content, d, 1)
        pm = np.where(fwd, 1.0 / (1.0 + np.exp(lw0 - lw1)), np.where(bwd, 1.0 / (1.0 + np.exp(lw1 - lw0)), 0.0))
        go = (rng.random((L, L, L)) < pm) & (fwd | bwd)
        prop += int((fwd | bwd).sum()); acc += int(go.sum())
        new_x = np.where(go & fwd, 6, np.where(go & bwd, other, state)); new_y = np.where(go & fwd, state, np.where(go & bwd, 6, other))
        state = np.where(sel, new_x, state)
        state = np.where(shifted(sel, d, -1), shifted(new_y, d, -1), state)
def sweep_sequential():
    global prop, acc
    for _ in range(3 * N):
        x = tuple(rng.integers(0, L, 3)); d = int(rng.integers(0, 3)); y = list(x); y[d] = (y[d] + 1) % L; y = tuple(y)
        a, b = state[x], state[y]
        if (a < 6) == (b < 6): continue
        src, dst = (x, y) if a < 6 else (y, x); cont = state[src]; prop += 1
        def lw(site, excl):
            t = 0.0
            for dd in range(3):
                for s in (1, -1):
                    z = list(site); z[dd] = (z[dd] + s) % L; z = tuple(z)
                    if z != excl: t += LW[cont, state[z]]
            return t
        if rng.random() < 1.0 / (1.0 + np.exp(lw(src, dst) - lw(dst, src))): state[dst] = cont; state[src] = 6; acc += 1
step = sweep_parallel if mode == "parallel" else sweep_sequential
t0 = time.time(); marks = sorted(set(int(round(v)) for v in np.geomspace(1, sweeps, 12))); tail = []
print(f"weights ({p},{q},{r}) scale c={c:.4f} ({scale_arg}) rho={rho} L={L} sweeps={sweeps} seed={seed} mode={mode}; random baseline: nbrs={6*rho:.3f} aligned=0.1667")
print("sweep  nbrs  aligned  accept  S")
for t in range(1, sweeps + 1):
    prop = acc = 0; step()
    if t in marks or t > 0.75 * sweeps:
        m = measure(state)
        if t in marks: print(f"{t:6d} {m[0]:.3f} {m[1]:.3f} {acc/max(prop,1):.3f} {m[2]:.2f}", flush=True)
        if t > 0.75 * sweeps: tail.append(m + (acc / max(prop, 1),))
tm = np.mean(tail, axis=0)
print(f"SUMMARY: p={p} q={q} r={r} c={c:.4f} rho={rho} L={L} nbrs={tm[0]:.3f} nbrs_over_random={tm[0]/(6*rho):.3f} aligned={tm[1]:.3f} S={tm[2]:.2f} accept={tm[3]:.3f} records={int((state<6).sum())} seconds={time.time()-t0:.0f}")
