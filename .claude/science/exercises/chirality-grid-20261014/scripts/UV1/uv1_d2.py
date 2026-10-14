"""UV-1 Stage B (PREREG §3-5): open-time Lt = 12, depth-2 kernel (buffer slice 1 + mirror integrated) vs depth-1 kernel
of the SAME witnesses.  All (arm, beta_g) from one determinant pass per (level, op).
usage: python3 uv1_d2.py POOL.npz sel IDX(comma)        (B-sel: K2c configs moved one slice deeper)
       python3 uv1_d2.py POOL.npz rand SEED K           (B-rand: random W-matched-at-slice-2 configs)"""
import numpy as np, sys, time
from uv1_lib import *
from k2c_lib import max_bulk
from k2b_lib import admissible
from lat2d import rand_half

pool, mode = sys.argv[1], sys.argv[2]; t00 = time.time()
d = np.load(pool); T = d['ux'].shape[1]; G = Geom(2, T, False, -1); Lx = 2
if mode == 'sel':
    idx = [int(i) for i in sys.argv[3].split(',')]
    U1 = [{'x': d['ux'][i], 't': d['ut'][i]} for i in idx]                              # depth-1 witnesses (as in K2c)
else:
    rng = np.random.default_rng(int(sys.argv[3])); kk = int(sys.argv[4]); U1 = []
    while len(U1) < kk:
        u = rand_half(rng, G, 0.25, DB); u = {'x': u['x'] - 0.5 * u['x'][0].sum(), 't': u['t']}
        U1.append(u)
k = len(U1)
UD = [{'x': u['x'][:T-1].copy(), 't': u['t'][:T-2].copy()} for u in U1]                # same witnesses, one slice deeper
print(f"# UV-1 Stage B open Lt={G.Lt} mode={mode} {sys.argv[3:]} k={k}; depth-2 = slices 1..{T-1} of each witness placed on 2..{T}", flush=True)
print(f"# W-match at depth-2 slice: max|W2| {max(abs(wrap(u['x'][0].sum())) for u in UD):.1e}; max bulk |plaq| depth1 {max(max_bulk(G, u) for u in U1):.4f}", flush=True)

lev = {'lo': 2, 'hi': 3, 'third': 4}
NODES = {}
for L_, n in lev.items():
    NODES[L_] = nested_nodes_d2(n); print(f"# nodes level {L_} (n={n}): {len(NODES[L_][2])} per entry; sum base w {NODES[L_][2].sum():.6f}", flush=True)
# exact volume check: sum of base weights = volume of {q in [-d,d]^4, d0 : |d0|<d, |Phi_eff - d0| < d} (computed at all levels)
nhi = len(NODES['hi'][2]) * k * (k + 1) // 2
print(f"# hi-level determinant evaluations per op: {nhi:.2e} (cap 4e6)", flush=True)
if nhi > 4e6: raise SystemExit('cost cap exceeded: reduce k')

FsC, BsC = G.crossing_mats(); FsX, BsX = buffer_xlink_mats(G)

# ---- V-B0: bookkeeping check against the direct builder and explicit plaquettes (one random node, two pairs) ----
Q, d0, w = NODES['lo']; rr = np.random.default_rng(5)
for (a, b) in [(0, 1), (1, 0)]:
    i = int(rr.integers(len(w)))
    ua = deep_to_ext(UD[a], Q[i, 0:2]); ub = deep_to_ext(UD[b], Q[i, 2:4])
    A = ub['x'][0] - ua['x'][0]; Phi = wrap(A.sum()); phis = np.array([0.0, d0[i] - A[0]])
    Dd = G.full_D(ua, ub, phis)
    ua0 = deep_to_ext(UD[a], np.zeros(Lx)); ub0 = deep_to_ext(UD[b], np.zeros(Lx))
    e0 = np.exp(1j * np.concatenate([ua0['x'][0], ub0['x'][0]]))
    Dfix = G.D0(ua0, ub0) - np.einsum('j,jab->ab', e0, FsX) - np.einsum('j,jab->ab', np.conj(e0), BsX)
    th = np.concatenate([ua['x'][0], ub['x'][0], phis])[None]
    Dn = D_links(Dfix, np.concatenate([FsX, FsC]), np.concatenate([BsX, BsC]), th)[0]
    pl = explicit_plaquettes(G, ua, ub, phis)
    Qa, da, wa = Q[i:i+1], d0[i:i+1], w[i:i+1]
    vl, _, _ = entry_d2(G, UD[a], UD[b], (Qa, da, wa), 'O', FsC, BsC, FsX, BsX)
    ld, _ = point_logs(G, Dd[None], 'O')
    print(f"# V-B0 lib-path check: log det via entry_d2 (beta=0 tri, weight-stripped) vs direct: {abs((vl[('hard', 0.0)] - np.log(wa[0] + 0j)) - ld[0]):.1e}", flush=True)
    print(f"# V-B0 pair {(a, b)} node {i}: |D_nodes - D_direct| {np.abs(Dn - Dd).max():.1e}; buffer plaq (+) {[round(pl[(x, 1)] - Q[i, x], 14) for x in range(2)]}, "
          f"(-) {[round(pl[(x, -1)] + Q[i, 2 + x], 14) for x in range(2)]} [mirror gap (-1|0) plaquette = -q-, reflection orientation]; crossing {pl[(0, 0)] - d0[i]:.1e}, {wrap(pl[(1, 0)] - (Phi - d0[i])):.1e}", flush=True)

rs = np.random.default_rng(99); pairs = set()
while len(pairs) < min(6, k * (k - 1) // 2):
    a_ = int(rs.integers(k)); b_ = int(rs.integers(k))
    if a_ != b_: pairs.add((min(a_, b_), max(a_, b_)))
pairs = sorted(pairs); sub = sorted(set(pairs) | {(i, i) for p in pairs for i in p})
allpairs = [(a, b) for a in range(k) for b in range(a, k)]


def logmats_d2(L_, op, which):
    L = {key: np.full((k, k), -np.inf + 0j) for key in ARMS}; gm = np.inf
    for (a, b) in which:
        if op == 'PG':
            Q_, d_, w_ = NODES[L_]; Phi = Q_[:, 2:4].sum(1) - Q_[:, 0:2].sum(1)
            vals = entry_logs_all(np.zeros(len(w_), complex), w_, np.concatenate([Q_, d_[:, None], (Phi - d_)[:, None]], 1)); g = np.inf
        else:
            vals, g, _ = entry_d2(G, UD[a], UD[b], NODES[L_], op, FsC, BsC, FsX, BsX, chunk=64)
        gm = min(gm, g)
        for key in ARMS:
            L[key][a, b] = vals[key]
            if a != b: L[key][b, a] = np.conj(vals[key])
            else: L[key][a, a] = vals[key].real
    return L, gm


def logmats_d1(n, op):
    L = {key: np.full((k, k), -np.inf + 0j) for key in ARMS}; gm = np.inf
    for (a, b) in allpairs:
        vals, g = entry_d1(G, U1[a], U1[b], n, None, op, FsC, BsC); gm = min(gm, g)
        for key in ARMS:
            L[key][a, b] = vals[key]
            if a != b: L[key][b, a] = np.conj(vals[key])
            else: L[key][a, a] = vals[key].real
    return L, gm


ref = {}
for op in ('O', 'W'):
    Llo, _ = logmats_d1(8, op); Lhi, g = logmats_d1(12, op)
    for key in ARMS:
        Zlo, Zhi = normalized(Llo[key]), normalized(Lhi[key]); a, b, _ = lam(Zhi); E = k * np.abs(Zhi - Zlo).max() + 1e-13
        ref[(op, key)] = (a, b, E)
    print(f"[depth-1 reference {op} done, min|H| {g:.3f}, {time.time()-t00:.0f}s]", flush=True)

res = {}
for op in ('O', 'W', 'PG'):
    t1 = time.time()
    Llo, glo = logmats_d2('lo', op, allpairs); print(f"[{op} lo done {time.time()-t1:.0f}s]", flush=True)
    Lhi, ghi = logmats_d2('hi', op, allpairs); print(f"[{op} hi done {time.time()-t1:.0f}s]", flush=True)
    L3, g3 = logmats_d2('third', op, sub); print(f"[{op} third done {time.time()-t1:.0f}s; min|H| lo {glo:.3f} hi {ghi:.3f} third {g3:.3f}]", flush=True)
    for key in ARMS:
        Zlo = normalized(Llo[key]); Zhi = normalized(Lhi[key]); d3 = L3[key].diagonal().real
        q = np.abs(Zhi - Zlo).max()
        q3 = max(abs(np.exp(L3[key][a, b] - 0.5 * (d3[a] + d3[b])) - Zhi[a, b]) for (a, b) in pairs)
        E = k * max(q, q3) + 1e-13; a, b, ev = lam(Zhi); res[(op, key)] = (a, b, E)
        print(f"FINAL depth2 {op:2s} arm={key[0]:4s} beta={key[1]:3.0f}: lam_min {a:+.4e} min/max {a/b:+.4e} q {q:.1e} q3 {q3:.1e} E {E:.1e} -> {'NEG(conv)' if a < -10*E else 'PSD-within-10E'} | lowest {np.array2string(ev[:3], precision=3)} max {b:.3f}", flush=True)
    print(flush=True)

print("SUMMARY Stage B (depth-1 reference O | depth-2 O | ratio of min/max | label | controls depth 2):")
for key in ARMS:
    a1, b1, E1 = ref[('O', key)]; a2, b2, E2 = res[('O', key)]
    aw, _, Ew = res[('W', key)]; ap, _, Ep = res[('PG', key)]
    if a2 < -10 * E2: lab = 'PROXY-NEG(2)'
    elif a1 < -10 * E1 and 10 * E2 <= 0.1 * abs(a1): lab = 'PROXY-PSD-at-power(2)'
    else: lab = 'PROXY-UNRESOLVED(2)' if a1 < -10 * E1 else 'no reference'
    print(f"  {key[0]:4s} beta={key[1]:3.0f}: d1 {a1:+.3e} ({a1/b1:+.2e}, E {E1:.0e}) | d2 {a2:+.3e} ({a2/b2:+.2e}, E {E2:.1e}) | rho {(a2/b2)/(a1/b1):+.2e} | {lab}"
          f" | W {aw:+.1e} {'NEG!' if aw < -10*Ew else 'psd'} PG {ap:+.1e} {'NEG!' if ap < -10*Ep else 'psd'}  (d1 W {ref[('W', key)][0]:+.1e})")
print(f"done [{time.time()-t00:.0f}s]", flush=True)
