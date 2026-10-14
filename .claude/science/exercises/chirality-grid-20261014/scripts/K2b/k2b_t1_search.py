"""K2b-T1 (PREREG.md): greedy search for the most negative direction of the gauge-invariant overlap RP kernel.
usage: python3 k2b_t1_search.py MODE GEOM T K SEED START
  MODE  search | screen        GEOM open | torus        START random | clustered
open: Lx=2 antiperiodic x, GL n = 16/32.  torus: Lx=2 periodic x, antiperiodic t, n = 4/6, nw = 4/6."""
import numpy as np, sys, time
from lat2d import Geom, rand_half
from k2b_lib import *

mode, gname, T, K, seed, start = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
OP = sys.argv[7] if len(sys.argv) > 7 else 'O'   # target fermion measure: O (Neuberger, default) or SH (Shamir overlap)
delta = 0.6; s0 = 0.25
if gname == 'open':
    G = Geom(2, T, False, -1); qlo, qhi = (16, None), (32, None)
else:
    G = Geom(2, T, True, 1); qlo, qhi = (4, 4), (6, 6)
rng = np.random.default_rng(seed); t00 = time.time()
print(f"# K2b-T1 {mode} op={OP} {gname} Lx={G.Lx} Lt={G.Lt} K={K} seed={seed} start={start} delta={delta} quad lo={qlo} hi={qhi}", flush=True)


def clustered(k):
    base = rand_half(rng, G, s0, delta); U = [base]
    while len(U) < k:
        v = perturb(rng, G, base, 0.05, delta)
        if v is not None: U.append(v)
    return U


k0 = K if mode == 'screen' else 8
if start.endswith('.npz'):   # V5: resume from a saved pool
    _d = np.load(start); U0 = [{'x': _d['ux'][i], 't': _d['ut'][i]} for i in range(len(_d['ux']))]
else:
    U0 = clustered(k0) if start == 'clustered' else [rand_half(rng, G, s0, delta) for _ in range(k0)]
P = Pool(G, delta, qlo[0], qlo[1], OP); PW = Pool(G, delta, qlo[0], qlo[1], 'W')
for u in U0:
    logs, g = P.row(u); P.add(u, logs, g)
    if mode == 'gsearch': lw, _ = PW.row(u); PW.add(u, lw, np.inf)
a, b, _ = lam(normalized(P.L))
print(f"start k={len(P.U)}: lam_min {a:+.3e} min/max {a/b:+.3e} min|H_W| {P.gmin:.3f} [{time.time()-t00:.0f}s]", flush=True)

if mode in ('search', 'gsearch'):
    step = 0
    while len(P.U) < K:
        step += 1; cands = []
        for _ in range(3): cands.append(('rand', rand_half(rng, G, s0, delta)))
        for sig in (0.02, 0.05, 0.1):
            v = perturb(rng, G, P.U[rng.integers(len(P.U))], sig, delta)
            if v is not None: cands.append((f'pert{sig}', v))
        for _ in range(2): cands.append(('hol', holonomy_shift(rng, P.U[rng.integers(len(P.U))])))
        best = None
        for (tag, u) in cands:
            logs, g = P.row(u); Zb = normalized(P.bordered(logs)); a, b, _ = lam(Zb)
            if mode == 'gsearch':
                lw, _ = PW.row(u); obj = gen_ratio(Zb, normalized(PW.bordered(lw)), 1e-6)
            else:
                lw = None; obj = a
            if best is None or obj < best[0]: best = (obj, a, b, tag, u, logs, g, lw)
        P.add(best[4], best[5], best[6])
        if mode == 'gsearch': PW.add(best[4], best[7], np.inf)
        print(f"step {step}: k={len(P.U)} added {best[3]:8s} objective {best[0]:+.3e} lam_min {best[1]:+.3e} min/max {best[1]/best[2]:+.3e} min|H_W| {P.gmin:.3f} [{time.time()-t00:.0f}s]", flush=True)

# final verification: overlap hi quadrature, Wilson lo and hi, on the same pool
U = P.U; k = len(U)
np.savez(f"pool_{mode}_{gname}_Lt{G.Lt}_seed{seed}" + ("" if OP == "O" else "_" + OP) + ".npz", ux=np.array([u['x'] for u in U]), ut=np.array([u['t'] for u in U]))
Zo_lo = normalized(P.L)
import os
NSUB = int(os.environ.get('K2B_QSUB', '0'))   # V4: if > 0 and lo-quadrature lam_min > 1e-6, q is estimated on NSUB random entries
if NSUB > 0 and lam(Zo_lo)[0] > 1e-6:
    Zw_lo = normalized(PW.L) if mode == 'gsearch' else full_kernel(G, U, delta, qlo[0], qlo[1], 'W')[0]
    Fs_, Bs_ = G.crossing_mats(); rs = np.random.default_rng(99); pairs = set()
    while len(pairs) < NSUB:
        a_ = int(rs.integers(k)); b_ = int(rs.integers(k)); pairs.add((min(a_, b_), max(a_, b_)))
    pairs |= {(i, i) for i in range(k)}
    Lo_ = np.full((k, k), np.nan + 0j); Lw_ = np.full((k, k), np.nan + 0j); go = np.inf
    for (a_, b_) in sorted(pairs):
        v_, g_ = entry_log(G, U[a_], U[b_], delta, qhi[0], qhi[1], OP, Fs_, Bs_); Lo_[a_, b_] = v_; go = min(go, g_)
        Lw_[a_, b_], _ = entry_log(G, U[a_], U[b_], delta, qhi[0], qhi[1], 'W', Fs_, Bs_)
    def nsub(Lh, Zl):
        d_ = Lh.diagonal().real; out = 0.0
        for (a_, b_) in pairs:
            z_ = np.exp(Lh[a_, b_] - 0.5 * (d_[a_] + d_[b_])) if np.isfinite(Lh[a_, b_].real) else 0
            out = max(out, abs(z_ - Zl[a_, b_]))
        return out
    qo = nsub(Lo_, Zo_lo); qw = nsub(Lw_, Zw_lo); Zo_hi = Zo_lo; Zw_hi = Zw_lo
    print(f"   (V4: q estimated on {len(pairs)} entries incl. diagonal; eigenvalues below are LOW-quadrature)")
else:
    Zo_hi, go = full_kernel(G, U, delta, qhi[0], qhi[1], OP)
    Zw_lo, _ = full_kernel(G, U, delta, qlo[0], qlo[1], 'W')
    Zw_hi, _ = full_kernel(G, U, delta, qhi[0], qhi[1], 'W')
    qo = np.abs(Zo_hi - Zo_lo).max(); qw = np.abs(Zw_hi - Zw_lo).max()
Eo = k * qo + 1e-13; Ew = k * qw + 1e-13
ao, bo, evo = lam(Zo_hi); aw, bw, evw = lam(Zw_hi)
gmin = min(P.gmin, go)
clean = qo < 1e-6 and qw < 1e-6 and gmin > 0.1
cert = ao < -10 * Eo; wpsd = aw > -10 * Ew
print(f"FINAL k={k}: OVERLAP lam_min {ao:+.4e} min/max {ao/bo:+.4e} q {qo:.1e} E {Eo:.1e} | WILSON lam_min {aw:+.4e} min/max {aw/bw:+.4e} q {qw:.1e} E {Ew:.1e}"
      f" | min|H_W| {gmin:.3f} | clean {clean} | certified-negative {cert} | Wilson PSD {wpsd} | K2-line(min/max<-1e-6) {ao/bo < -1e-6}", flush=True)
print(f"   overlap eigenvalues: {np.array2string(evo[:6], precision=3)} ... max {evo[-1]:.3f}")
print(f"   Wilson  eigenvalues: {np.array2string(evw[:6], precision=3)} ... max {evw[-1]:.3f}")
try:
    print(f"   diagnostic gen-ratio min (overlap vs Wilson, Wilson range > 1e-8): {gen_ratio(Zo_hi, Zw_hi):+.3e}")
except Exception as ex:
    print("   gen-ratio failed", ex)
v = np.linalg.eigh(Zo_hi)[1][:, 0]
print(f"   most-negative-direction weights |v_a|: {np.array2string(np.abs(v), precision=2)}")
print(f"done [{time.time()-t00:.0f}s]", flush=True)
