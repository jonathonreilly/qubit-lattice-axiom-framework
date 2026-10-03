"""A37 t2: one record and one excitation on a line (supplied single-excitation toy of the record-tick shape).

Possibilities: one qubit per site, calm vacuum |0> (= +n) with at most one excitation |1>; record content r = |1> (-n).
Record frame: relative sites s = -M..-1, +1..M (record at 0) plus 'no excitation' (index 2M).
Between ticks: compressed Heisenberg J sum sigma.sigma, single-excitation block: hopping 2J between unrecorded
neighbours (never across the record), potential -2J per unrecorded bond at s and -2J(n_r)_z next to the record.
At each tick: step instrument K_d = sqrt(c/2) Map_d sqrt(W_d), W = w_exc on 'excitation at y', w_vac otherwise;
stay K = sqrt(1 - (c/2)(W_+ + W_-)).  Post-step maps (step right; left is the mirror image):
  SW   : y's content -> x                       (swap)
  PL1  : y -> y+1, y+1 -> x                      (capped line push, one return jump of 2)
  PL2  : y -> y+1, y+1 -> y+2, y+2 -> x          (capped line push, return jump of 3)
  Pinf : everything ahead shifts with the record, fresh calm site at x (half-line conveyor)
  PA   : push the excitation train at y up to the first calm site; decohering (two Kraus branches)
  PF   : y's content erased (traced out), fresh calm site at x
Usage: python3 t2_chain_1d.py {exact|mc} {blind|attract|repel}   or   python3 t2_chain_1d.py energy-cone
"""
import sys, signal
import numpy as np
from scipy.linalg import expm
signal.alarm(55)

J, tau, c = 0.25, 0.2, 0.5
M = 60
D = 2 * M + 1
NONE = 2 * M
nz = -1.0                         # (n_r)_z for r = |1> = -n
def idx(s): return s + M if s < 0 else s + M - 1
sites = [s for s in range(-M, M + 1) if s != 0]
H = np.zeros((D, D))
for s in sites:
    nb_unrec = sum(1 for t in (s - 1, s + 1) if t != 0 and -M <= t <= M)
    H[idx(s), idx(s)] = -2 * J * nb_unrec - (2 * J * nz if abs(s) == 1 else 0.0)
    for t in (s - 1, s + 1):
        if t != 0 and -M <= t <= M:
            H[idx(s), idx(t)] = 2 * J
U = expm(-1j * H * tau)
RULES = ["SW", "PL1", "PL2", "Pinf", "PA", "PF"]

def maps_right(rule):
    """List of (src_indices, dst_indices) partial permutations (one per Kraus branch) for a step to the right."""
    def shift(s): return s - 1
    if rule in ("SW", "PL1", "PL2", "Pinf"):
        src, dst = [NONE], [NONE]
        for s in sites:
            if rule == "SW":
                t = -1 if s == 1 else shift(s)
            elif rule == "PL1":
                t = 1 if s == 1 else (-1 if s == 2 else shift(s))
            elif rule == "PL2":
                t = s if s in (1, 2) else (-1 if s == 3 else shift(s))
            else:  # Pinf
                t = s if s >= 1 else shift(s)
            if -M <= t <= M and t != 0:
                src.append(idx(s)); dst.append(idx(t))
        return [(np.array(src), np.array(dst))]
    # PA / PF: branch 0 (no excitation at y): everything but y shifts; branch 1 (excitation at y)
    src0, dst0 = [NONE], [NONE]
    for s in sites:
        if s != 1 and -M <= shift(s) <= M and shift(s) != 0:
            src0.append(idx(s)); dst0.append(idx(shift(s)))
    b1 = (np.array([idx(1)]), np.array([idx(1)])) if rule == "PA" else (np.array([idx(1)]), np.array([NONE]))
    return [(np.array(src0), np.array(dst0)), b1]

order = np.array([0] * D)
for s in sites:
    order[idx(s)] = idx(-s)
order[NONE] = NONE
def maps_for(rule, d):
    mr = maps_right(rule)
    return mr if d == +1 else [(order[a], order[b]) for (a, b) in mr]

def apply_map(m, X):
    """Apply partial permutation m=(src,dst) to columns-of-states X (D x n)."""
    Y = np.zeros_like(X)
    Y[m[1]] = X[m[0]]
    return Y

def weights_vec(w_exc, w_vac, d):
    w = np.full(D, w_vac); w[idx(d)] = w_exc
    return w

def exact_two_steps(rule, w_exc, w_vac, psi0, Tmax=2000, tol=1e-7):
    """Exact joint law of the first two step directions (density-matrix branch classes)."""
    Wp, Wm = weights_vec(w_exc, w_vac, +1), weights_vec(w_exc, w_vac, -1)
    stay = np.sqrt(1 - (c / 2) * (Wp + Wm))
    mp, mm = maps_for(rule, +1), maps_for(rule, -1)
    rho0 = np.outer(psi0, psi0.conj())
    first = {+1: np.zeros((D, D), complex), -1: np.zeros((D, D), complex)}
    P = {(a, b): 0.0 for a in (1, -1) for b in (1, -1)}
    Ud = U.conj().T
    for t in range(Tmax):
        rho0 = U @ rho0 @ Ud
        for d in (1, -1):
            first[d] = U @ first[d] @ Ud
        # second steps out of the one-step classes
        for d1 in (1, -1):
            r = first[d1]
            for d2, Wd in ((1, Wp), (-1, Wm)):
                P[(d1, d2)] += (c / 2) * np.real(np.sum(Wd * np.diag(r)))
            first[d1] = (stay[:, None] * r) * stay[None, :]
        # first steps out of the no-step class
        new = {}
        for d, Wd, ms in ((1, Wp, mp), (-1, Wm, mm)):
            sq = np.sqrt(Wd)
            r = (sq[:, None] * rho0) * sq[None, :] * (c / 2)
            acc = np.zeros((D, D), complex)
            for m in ms:
                acc += _conj_map(m, r)
            new[d] = acc
        rho0 = (stay[:, None] * rho0) * stay[None, :]
        for d in (1, -1):
            first[d] += new[d]
        left = np.real(np.trace(rho0)) + sum(np.real(np.trace(first[d])) for d in (1, -1))
        if left < tol:
            break
    return P, left, t + 1

def _conj_map(m, r):
    """M r M^dagger for a partial permutation M."""
    Y = np.zeros_like(r)
    Y[np.ix_(m[1], m[1])] = r[np.ix_(m[0], m[0])]
    return Y

def basis(s):
    v = np.zeros(D, complex); v[idx(s)] = 1; return v

def mc(rule, w_exc, w_vac, psi0, T, ntraj, seed):
    rs, rb = np.random.default_rng(seed), np.random.default_rng(seed + 1)
    Wp, Wm = weights_vec(w_exc, w_vac, +1), weights_vec(w_exc, w_vac, -1)
    stay = np.sqrt(1 - (c / 2) * (Wp + Wm))
    mp, mm = maps_for(rule, +1), maps_for(rule, -1)
    Psi = np.tile(psi0[:, None], (1, ntraj))
    X = np.zeros(ntraj, int)
    last = np.zeros(ntraj, int); pairsum = np.zeros(ntraj); npairs = np.zeros(ntraj)
    nsteps = np.zeros(ntraj)
    pos_rel = np.array([s for s in sites] + [0])
    exc_abs0 = np.real(np.sum(np.abs(psi0) ** 2 * pos_rel))
    for t in range(T):
        Psi = U @ Psi
        prob2 = np.abs(Psi) ** 2
        pR = (c / 2) * (Wp @ prob2); pL = (c / 2) * (Wm @ prob2)
        u = rs.random(ntraj); ub = rb.random(ntraj)
        goR = u < pR; goL = (u >= pR) & (u < pR + pL); st = ~(goR | goL)
        newPsi = np.empty_like(Psi)
        newPsi[:, st] = stay[:, None] * Psi[:, st]
        for d, go, Wd, ms in ((1, goR, Wp, mp), (-1, goL, Wm, mm)):
            if not go.any():
                continue
            base = np.sqrt(Wd)[:, None] * Psi[:, go]
            if len(ms) == 1:
                newPsi[:, go] = apply_map(ms[0], base)
            else:
                b0, b1 = apply_map(ms[0], base), apply_map(ms[1], base)
                n0, n1 = np.sum(np.abs(b0) ** 2, 0), np.sum(np.abs(b1) ** 2, 0)
                pick1 = ub[go] < n1 / (n0 + n1)
                newPsi[:, go] = np.where(pick1[None, :], b1, b0)
            dvec = np.where(go, d, 0)
            X += dvec
            has = go & (last != 0)
            pairsum[has] += last[has] * d; npairs[has] += 1
            last[go] = d; nsteps[go] += 1
        nrm = np.sqrt(np.sum(np.abs(newPsi) ** 2, 0))
        Psi = newPsi / nrm
    prob2 = np.abs(Psi) ** 2
    ahead = prob2[[idx(s) for s in sites if s > 0]].sum(0)
    behind = prob2[[idx(s) for s in sites if s < 0]].sum(0)
    erased = prob2[NONE]
    rel_mean = (pos_rel @ prob2) / np.maximum(1 - erased, 1e-300)
    exc_disp = np.where(erased < 0.5, X + rel_mean - exc_abs0, np.nan)
    ok = ~np.isnan(exc_disp)
    slope = np.cov(X[ok], exc_disp[ok])[0, 1] / np.var(X[ok]) if ok.sum() > 2 and np.var(X[ok]) > 0 else np.nan
    C1 = pairsum.sum() / max(npairs.sum(), 1)
    return dict(msd=np.mean(X ** 2), meanX=np.mean(X), C1=C1, nsteps=nsteps.mean(), ahead=ahead.mean(),
                behind=behind.mean(), erased=erased.mean(), slope=slope, edge=np.mean(prob2[[idx(-M), idx(M)]].sum(0)))

WEIGHTS = {"blind": (1.0, 1.0), "attract": (1.0, 0.2), "repel": (0.2, 1.0)}
mode = sys.argv[1] if len(sys.argv) > 1 else "energy-cone"
wsel = sys.argv[2] if len(sys.argv) > 2 else "blind"
print(f"J={J} tau={tau} (dose 2J tau={2*J*tau}) c={c} M={M}; record content -n")
if mode == "exact":
    we, wv = WEIGHTS[wsel]
    sym = (basis(1) + basis(-1)) / np.sqrt(2)
    print(f"Exact joint law of the first two step directions, weights {wsel} (w_exc={we}, w_vac={wv})")
    for start_name, psi0 in (("excitation at +1", basis(1)), ("(|+1>+|-1>)/sqrt2", sym)):
        print(f"  start: {start_name}")
        for rule in RULES:
            P, left, n = exact_two_steps(rule, we, wv, psi0)
            tot = sum(P.values())
            ps = (P[(1, 1)] + P[(-1, -1)]) / tot
            print(f"    {rule:5s} RR {P[(1,1)]/tot:.4f} RL {P[(1,-1)]/tot:.4f} LR {P[(-1,1)]/tot:.4f} "
                  f"LL {P[(-1,-1)]/tot:.4f}   p_same {ps:.4f}   (ticks {n}, undecided {left:.1e}, total {tot+left:.6f})")
elif mode == "energy-cone":
    print("Energy <H> change of one step to the right (given it happens), relative to the calm vacuum, units of J:")
    for start_name, psi0 in (("exc at +1", basis(1)), ("exc at +2", basis(2)), ("exc at +3", basis(3)),
                             ("exc at -1", basis(-1)), ("packet k=pi/2 near +5", None), ("no excitation", "none")):
        if psi0 is None:
            v = np.zeros(D, complex)
            for s in range(1, 12):
                v[idx(s)] = np.exp(-((s - 5) / 2.0) ** 2) * np.exp(1j * np.pi / 2 * s)
            psi0 = v / np.linalg.norm(v)
        elif isinstance(psi0, str):
            psi0 = np.zeros(D, complex); psi0[NONE] = 1
        E0 = np.real(psi0.conj() @ H @ psi0)
        line = []
        for rule in RULES:
            Es = 0.0
            for m in maps_for(rule, +1):
                v = apply_map(m, psi0[:, None])[:, 0]
                Es += np.real(v.conj() @ H @ v)          # branches weighted by their norms (sum = 1)
            line.append(f"{rule}:{(Es - E0)/J:+.3f}")
        print(f"  {start_name:22s} " + "  ".join(line))
    Dd = 30
    psi0 = basis(Dd)
    print(f"One tick, excitation {Dd} sites ahead: TV of its absolute position law, step allowed (blind, c={c}) vs no step possible")
    for rule in RULES:
        rho = U @ np.outer(psi0, psi0.conj()) @ U.conj().T
        law_nostep = np.real(np.diag(rho))[:-1]
        absl = {}
        def add(law_rel, shift, w):
            for s, p in zip(sites, law_rel):
                absl[s + shift] = absl.get(s + shift, 0) + w * p
        add(law_nostep, 0, 1 - c)
        for d in (1, -1):
            r = sum(_conj_map(m, rho) for m in maps_for(rule, d))
            add(np.real(np.diag(r))[:-1], d, c / 2)
        ref = {s: p for s, p in zip(sites, law_nostep)}
        keys = set(absl) | set(ref)
        tv = 0.5 * sum(abs(absl.get(k, 0) - ref.get(k, 0)) for k in keys)
        print(f"  {rule:5s} TV = {tv:.6f}")
else:  # mc
    we, wv = WEIGHTS[wsel]
    T, ntraj = 100, 1500
    print(f"Monte Carlo: weights {wsel} (w_exc={we}, w_vac={wv}), {ntraj} trajectories x {T} ticks, excitation starts at +1")
    for rule in RULES:
        r = mc(rule, we, wv, basis(1), T, ntraj, seed=2026)
        print(f"  {rule:5s} steps/traj {r['nsteps']:.2f}  MSD {r['msd']:7.2f}  mean X {r['meanX']:+6.2f}  lag-1 step corr {r['C1']:+.4f}  "
              f"exc ahead {r['ahead']:.3f} behind {r['behind']:.3f} erased {r['erased']:.3f}  carry slope {r['slope']:+.3f}  edge {r['edge']:.1e}")
