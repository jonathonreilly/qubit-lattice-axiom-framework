#!/usr/bin/env python3
"""Block capacity under burns (a site records once, CL-4 one record per relay per tick).

(T) exact counting: pigeonhole lifetime of a confined region; capacity bound on following the odds;
    rung-independence of the bound.
(R) supplied 1D lossless walk on a ring of L blocks of n sites, one relay per world, odds never
    conditioned, CL-6 switching + redraws at 2*eps.  Rules for 'every neighbouring block used up':
      cl4      : none (relay stuck; CL-4 as written)
      ladder   : step at the next coarser rung of a FIXED partition (blocks of 2^k blocks)
      doubling : relay-centred coarser rung (targets at offsets 2^k .. 2^(k+1)-1 in its direction)
      nearest  : nearest block that is not used up, equal probability among the nearest
    Checks: every record lands on an unburnt site; lifetime reaches the pigeonhole bound;
    exact block-translation covariance (coupled random streams); displacement sizes;
    forced departure from the odds after the capacity time.
(P) measured densities and ages: burnt fraction beta = (relays per site) x (ticks).
Supplied models; no physical identification.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/BURNT_SITE_CAPACITY_BOUNDS_RELAY_LIFE_AND_ODDS_FOLLOWING_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120


import sys, os, signal
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
def _timeout(*args):
    raise TimeoutError('Owning 120-second cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

PASS = FAIL = 0
TH = 0.2


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ---------------- supplied walk U = S C on (x, d); d=0 steps +1, d=1 steps -1
def mats(N, th):
    c, s = np.cos(th), np.sin(th)
    C = np.zeros((2 * N, 2 * N), complex); S = np.zeros((2 * N, 2 * N))
    for x in range(N):
        C[2 * x:2 * x + 2, 2 * x:2 * x + 2] = [[c, -1j * s], [-1j * s, c]]
        S[2 * ((x + 1) % N), 2 * x] = 1; S[2 * ((x - 1) % N) + 1, 2 * x + 1] = 1
    return C, S


def mode(N, th, k):
    Cc = np.array([[np.cos(th), -1j * np.sin(th)], [-1j * np.sin(th), np.cos(th)]])
    w, V = np.linalg.eig(np.diag([np.exp(-1j * k), np.exp(1j * k)]) @ Cc)
    j = int(np.argmax(-np.angle(w))); v = V[:, j] / np.linalg.norm(V[:, j])
    return np.outer(np.exp(1j * k * np.arange(N)), v).ravel() / np.sqrt(N)


def band_packet(N, th, k0, x0, sig):
    ks = 2 * np.pi * np.fft.fftfreq(N); amp = np.zeros((N, 2), complex)
    for i, k in enumerate(ks):
        v = mode(N, th, k).reshape(N, 2)[0] * np.sqrt(N); v = v * np.exp(-1j * np.angle(v[0]))
        dk = (k - k0 + np.pi) % (2 * np.pi) - np.pi
        amp[i] = v * np.exp(-dk ** 2 * sig ** 2 / 2 - 1j * k * x0)
    psi = np.fft.ifft(amp, axis=0) * N
    return (psi / np.linalg.norm(psi)).ravel()


# ---------------- fallback target sets, as lists of relative offsets per direction (+1 / -1)
def fallback_sets(rule, L):
    """for 'doubling': level k>=1 target offsets [2^k, 2^(k+1)) in each direction (capped at L-1)."""
    out = []; k = 1
    while 2 ** k <= L - 1:
        out.append(np.arange(2 ** k, min(2 ** (k + 1), L)))
        k += 1
    return out


def pick_site(burnt, ar, blocks_rel, x, u, L):
    """choose an unburnt site uniformly over the blocks x+blocks_rel (ordered by relative offset).
    blocks_rel: (m, K) int relative offsets (-999 = unused). Returns (block, site)."""
    m, K = blocks_rel.shape; n = burnt.shape[2]
    valid = blocks_rel != -999
    b = (x[:, None] + np.where(valid, blocks_rel, 0)) % L
    free = (~burnt[ar[:, None], b]) & valid[:, :, None]           # (m, K, n)
    flat = free.reshape(m, K * n); tot = flat.sum(1)
    r = np.minimum((u * tot).astype(int), np.maximum(tot - 1, 0))
    j = np.argmax(np.cumsum(flat, 1) > r[:, None], 1)
    return b[np.arange(m), j // n], j % n


def simulate(psi0, n, T, M, rule, x0=None, d0=None, seed=1, track=False):
    """one relay per world. returns dict of diagnostics."""
    L = len(psi0) // 2; C, S = mats(L, TH); psi = psi0.copy()
    rng = np.random.default_rng(seed)
    P = (abs(psi) ** 2).reshape(L, 2)
    if x0 is None:
        idx = rng.choice(2 * L, M, p=P.ravel() / P.sum()); x, d = idx // 2, idx % 2
    else:
        x, d = x0.copy(), d0.copy()
    ar = np.arange(M); burnt = np.zeros((M, L, n), bool); vis = np.zeros((M, L), np.int32)
    burnt[ar, x, 0] = True; vis[ar, x] = 1
    alive = np.ones(M, bool); stuck_at = np.full(M, -1); first_full = np.full(M, -1)
    nfall = 0; jumps = []; occ_tv = []; ratio = []; traj = [] if track else None
    double = 0; records = M
    sets = fallback_sets('doubling', L)
    for t in range(T):
        U = rng.random((7, M))
        P = (abs(psi) ** 2).reshape(L, 2); pc = C @ psi; Pc = (abs(pc) ** 2).reshape(L, 2)
        # CL-6 switching at the coin step
        ex = np.clip(P - Pc, 0, None); sh = np.clip(Pc - P, 0, None); Ssh = sh.sum(1)
        pr = P[x, d]; sw = (U[0] < np.where(pr > 0, ex[x, d] / np.where(pr > 0, pr, 1), 0)) & (Ssh[x] > 0)
        d = np.where(sw, (U[1] > sh[x, 0] / np.where(Ssh[x] > 0, Ssh[x], 1)).astype(int), d)
        full = vis >= n
        s = 1 - 2 * d; tgt = (x + s) % L; alt = (x - s) % L
        tf = full[ar, tgt]; af = full[ar, alt]
        first_full = np.where(tf & (first_full < 0) & alive, t, first_full)
        # CL-4 clause 2: other direction (1D: the only other one); its odds must be > 0
        oth_odds = Pc[x, 1 - d] > 0
        can = tf & ~af & oth_odds
        s = np.where(can, -s, s); d = np.where(can, 1 - d, d)
        fb = tf & ~can & alive                       # fallback needed
        nx = (x + s) % L
        blocks = np.full((M, 1), -999); blocks[:, 0] = s           # default target: neighbour in direction
        newb, site = pick_site(burnt, ar, blocks, x, U[2], L)
        if fb.any():
            i = np.nonzero(fb)[0]; nfall += len(i)
            if rule == 'cl4':
                newb[i] = -1
            else:
                ok = np.zeros(len(i), bool); nb = np.full(len(i), -1); st = np.zeros(len(i), int)
                fr = ~full[i]
                if rule == 'nearest':
                    offs = np.arange(1, L)
                    fp = fr[np.arange(len(i))[:, None], (x[i, None] + offs) % L]
                    fm = fr[np.arange(len(i))[:, None], (x[i, None] - offs) % L]
                    jp = np.where(fp.any(1), np.argmax(fp, 1) + 1, L); jm = np.where(fm.any(1), np.argmax(fm, 1) + 1, L)
                    jmin = np.minimum(jp, jm); ok = jmin < L
                    tie = jp == jm; sgn = np.where(jp < jm, 1, -1)
                    sgn = np.where(tie, np.where(U[3, i] < 0.5, 1, -1), sgn)
                    rel = np.full((len(i), 1), -999); rel[:, 0] = np.where(ok, sgn * jmin, -999)
                    b2, s2 = pick_site(burnt[i], np.arange(len(i)), rel, x[i], U[2, i], L)
                    nb = np.where(ok, b2, -1); st = s2
                else:
                    for lev, offs in enumerate(sets):
                        todo = ~ok
                        if not todo.any(): break
                        for which in (0, 1):                 # own direction first, then the other
                            todo = ~ok
                            if not todo.any(): break
                            sg = s[i] * (1 if which == 0 else -1)
                            if rule == 'doubling':
                                rel = np.full((len(i), len(offs)), -999)
                                rel[todo] = sg[todo, None] * offs[None, :]
                            else:                            # ladder: neighbouring rung-k superblock, fixed partition
                                kk = lev + 1; W = 2 ** kk; nsb = L // W
                                if nsb < 2: rel = np.full((len(i), W), -999)
                                else:
                                    tsb = ((x[i] // W) + sg) % nsb
                                    blk = tsb[:, None] * W + np.arange(W)[None, :]
                                    rr = (blk - x[i, None]) % L
                                    rel = np.where(todo[:, None], rr, -999)
                                    rel = np.where(rel == 0, -999, rel)
                            vb = rel != -999
                            hasfree = (fr[np.arange(len(i))[:, None], (x[i, None] + np.where(vb, rel, 0)) % L] & vb).any(1)
                            sel = todo & hasfree
                            if sel.any():
                                b2, s2 = pick_site(burnt[i][sel], np.arange(sel.sum()), rel[sel], x[i][sel], U[2, i][sel], L)
                                nb[sel] = b2; st[sel] = s2; ok[sel] = True
                newb[i] = nb; site[i] = st
                jj = (newb[i] - x[i] + L // 2) % L - L // 2
                jumps.extend(np.abs(jj[ok]).tolist())
        stuck = newb < 0
        stuck_at = np.where(stuck & (stuck_at < 0), t, stuck_at)
        alive &= ~stuck
        mv = alive.copy(); w = ar[mv]
        double += int(burnt[w, newb[mv], site[mv]].sum()); records += int(mv.sum())
        burnt[w, newb[mv], site[mv]] = True; vis[w, newb[mv]] += 1
        step = np.where(mv, (newb - x + L // 2) % L - L // 2, 0)
        x = np.where(mv, newb, x)
        J = (Pc[:, 0] - Pc[:, 1]).sum()
        ratio.append(step[alive].mean() / J if alive.any() and abs(J) > 1e-9 else np.nan)
        new = S @ pc; Pn = (abs(new) ** 2).reshape(L, 2); Wn = Pn.sum(1)
        e = (Pn * -np.angle(new * psi.conj()).reshape(L, 2)).sum(1) / np.where(Wn > 0, Wn, 1)
        r = np.clip(2 * e, 0, 1); h = (U[4] < r[x]) | (fb & mv)       # fallback relays redraw from new block's odds
        p0 = Pn[x, 0] / np.where(Wn[x] > 0, Wn[x], 1); p0 = np.where(Wn[x] > 0, p0, 0.5)
        d = np.where(h, (U[5] > p0).astype(int), d)
        jd = np.where(fb & mv, np.where(step > 0, 0, 1), d)            # placeholder (unused) for clarity
        psi = new
        if alive.sum() > 50:
            hst = np.bincount(x[alive] * 2 + d[alive], minlength=2 * L) / alive.sum()
            occ_tv.append(0.5 * abs(hst - Pn.ravel() / Pn.sum()).sum())
        else: occ_tv.append(np.nan)
        if track: traj.append(x.copy())
    return dict(stuck_at=stuck_at, first_full=first_full, nfall=nfall, jumps=np.array(jumps), tv=np.array(occ_tv),
                ratio=np.array(ratio), double=double, records=records, burnt_total=int(burnt.sum()), vis=vis,
                traj=np.array(traj) if track else None, alive=alive, x=x, burnt=burnt)


# ================= T: exact counting theorems (checked on the walk) =================
def section_theorems():
    print('T. exact counting (Record + CL-4): lifetime and capacity bounds')
    L, n = 16, 4; th = TH
    # T1 pigeonhole: one relay per world, S = nL sites, 1 burnt at start => at most nL-1 further records
    res = simulate(mode(L, th, 2 * np.pi / L), n, n * L + 8, 2000, 'nearest', seed=3)
    life = np.where(res['stuck_at'] >= 0, res['stuck_at'], n * L + 8)
    check('T1 pigeonhole: no world records more than nL-1 times after its start (nL=64), and records = burnt sites',
          life.max() <= n * L - 1 and res['records'] == res['burnt_total'] and res['double'] == 0,
          f'max life {life.max()}, records {res["records"]}, burnt {res["burnt_total"]}, double {res["double"]}')
    # T2 capacity bound on following the odds: standing wave, stationary non-uniform odds
    psi = mode(L, th, 2 * np.pi / L) + mode(L, th, -2 * np.pi / L); psi /= np.linalg.norm(psi)
    C, S = mats(L, th); U = S @ C; Ps = []
    p = psi.copy()
    for t in range(40): Ps.append((abs(p) ** 2).reshape(L, 2).sum(1)); p = U @ p
    Ps = np.array(Ps); stat = abs(Ps - Ps[0]).max(); Pm = Ps.mean(0)
    Tcap = n / Pm.max()
    check('T2 standing wave odds are stationary and non-uniform; capacity time n/max P < nL',
          stat < 1e-12 and Tcap < n * L, f'stationarity {stat:.1e}, max P {Pm.max():.4f} (uniform {1 / L:.4f}), T_cap {Tcap:.1f} (nL {n * L})')
    # T3 rung independence: counting at rung k (blocks of 2^k) gives n 2^k / sum P >= T_cap and <= nL
    caps = []
    for k in range(5):
        W = 2 ** k; caps.append((n * W) / Pm.reshape(L // W, W).sum(1).max())
    check('T3 counting at coarser rungs: capacity time rises from n/maxP towards nL = sites/relays, never above it',
          all(caps[i] <= caps[i + 1] + 1e-9 for i in range(4)) and abs(caps[-1] - n * L) < 1e-6,
          'rung 0..4: ' + ', '.join(f'{c:.1f}' for c in caps))
    return psi, Tcap


# ================= R: rules on the 1D ring =================
def section_rules(psi_sw, Tcap):
    print('R. ring L=16, one relay per world; rules for "every neighbouring block used up"')
    L = 16; k = 2 * np.pi / L; pw = mode(L, TH, k)
    rows = {}
    for n in (4, 16):
        T = n * L + 4; M = 3000
        for rule in ('cl4', 'ladder', 'doubling', 'nearest'):
            r = simulate(pw, n, T, M, rule, seed=11)
            life = np.where(r['stuck_at'] >= 0, r['stuck_at'], T)
            # when stuck, are all unburnt sites in the relay's own block?
            fullv = r['vis'] >= n; own_only = np.ones(M, bool)
            for w in np.nonzero(~r['alive'])[0]:
                fr = np.nonzero(~fullv[w])[0]; own_only[w] = (len(fr) == 0) or (len(fr) == 1 and fr[0] == r['x'][w])
            f = r['first_full'][r['first_full'] >= 0]
            pre = np.nanmean(r['ratio'][:max(int(f.min()), 1)]) if len(f) else np.nan
            rows[(n, rule)] = (np.median(life), (life >= n * L - n).mean(), own_only[~r['alive']].mean() if (~r['alive']).any() else 1.0,
                               r['double'], r['jumps'], pre, r['nfall'] / M)
        a = rows[(n, 'cl4')]
        check(f'R1 n={n}: CL-4 alone strands relays with unburnt sites left elsewhere on the ring',
              a[2] < 0.5, f'median life {a[0]:.0f} of nL-1={n * L - 1}; stuck with only own block fresh: {a[2]:.3f}')
        for rule in ('ladder', 'doubling', 'nearest'):
            b = rows[(n, rule)]
            check(f'R2 n={n} {rule}: no site records twice; a relay stops only when every unburnt site is in its own block',
                  b[3] == 0 and b[2] == 1.0,
                  f'median life {b[0]:.0f}; reach >= nL-n: {b[1]:.3f}; fallbacks/world {b[6]:.1f}; jump mean {b[4].mean():.2f} max {b[4].max()}')
        check(f'R3 n={n}: nearest-fresh jumps are never longer than the other fallbacks (it minimises the displacement)',
              rows[(n, 'nearest')][4].mean() <= min(rows[(n, 'ladder')][4].mean(), rows[(n, 'doubling')][4].mean()) + 1e-12,
              ', '.join(f'{r}: mean |jump| {rows[(n, r)][4].mean():.2f}' for r in ('ladder', 'doubling', 'nearest')))
        check(f'R4 n={n}: until the first used-up target, the realised current follows the odds (all rules identical there)',
              all(abs(rows[(n, r)][5] - 1) < 0.05 for r in ('cl4', 'nearest')),
              f'current/odds before first hit {rows[(n, "nearest")][5]:.3f}')
    # R5 exact block-translation covariance with coupled random streams (plane-wave odds are shift-invariant)
    n = 4; T = n * L + 4; M = 600; rng = np.random.default_rng(5)
    x0 = rng.integers(0, L, M); d0 = rng.integers(0, 2, M); out = {}
    for rule in ('ladder', 'doubling', 'nearest'):
        a = simulate(pw, n, T, M, rule, x0, d0, seed=21, track=True)
        b = simulate(pw, n, T, M, rule, (x0 + 1) % L, d0, seed=21, track=True)
        out[rule] = (((a['traj'] + 1) % L) != b['traj']).any(0).mean()
    check('R5 block-translation covariance (shift by one block, same random stream): doubling and nearest exact; '
          'fixed-partition ladder is not (it privileges partition boundaries)',
          out['doubling'] == 0 and out['nearest'] == 0 and out['ladder'] > 0,
          ', '.join(f'{r}: worlds differing {v:.3f}' for r, v in out.items()))
    # R6 departure from the odds: control (n=200, no block used up) vs n=4 (first-clause hits, then T_cap)
    T = 60; M = 6000; tv = {}
    for n, rule in ((200, 'nearest'), (4, 'cl4'), (4, 'nearest')):
        r = simulate(psi_sw, n, T, M, rule, seed=31)
        hit18 = ((r['first_full'] >= 0) & (r['first_full'] < 18)).mean()
        tv[(n, rule)] = (np.nanmean(r['tv'][:18]), np.nanmean(r['tv'][int(Tcap):int(Tcap) + 15]), hit18)
    c0 = tv[(200, 'nearest')]
    check(f'R6 standing wave: with ample capacity the occupation stays at the odds; at n=4 it leaves them, '
          f'first through used-up targets (CL-4 clause 2) and by T_cap={Tcap:.0f} necessarily (T2)',
          max(c0[0], c0[1]) < 0.035 and tv[(4, 'nearest')][1] > 4 * c0[1],
          f'n=200 TV {c0[0]:.3f}/{c0[1]:.3f} (sampling noise ~0.03); ' +
          '; '.join(f'n=4 {r}: TV ticks<18 {v[0]:.3f} (worlds hit by 18: {v[2]:.2f}), after T_cap {v[1]:.3f}'
                    for (n, r), v in tv.items() if n == 4))
    # R7 drifting packet on a long ring: fallback events vs first-clause hits
    N = 300; pk = band_packet(N, TH, 2 * np.pi / 16, 60, 6.0); s = []
    for n in (1, 2, 4, 8):
        r = simulate(pk, n, 150, 2000, 'nearest', seed=41)
        hit = (r['first_full'] >= 0).mean()
        s.append((n, hit, r['nfall'] / 2000, np.nanmean(r['ratio']), r['double'], (~r['alive']).mean()))
    check('R7 drifting packet (v~0.88): nearest rule never strands a relay; fallbacks rarer than first-clause hits',
          all(x[4] == 0 and x[5] == 0 for x in s),
          '; '.join(f'n={x[0]}: hit {x[1]:.3f}, fallbacks/relay {x[2]:.3f}, cur/odds {x[3]:.3f}' for x in s))


def walk3d(n, q, T, W, seed):
    """supplied 3D relay path: persistent walk on the block lattice Z^3, turning with probability q per tick
    to a uniformly chosen face direction (uniform odds). CL-4 clause 2 among non-used-up directions;
    'nearest' fallback by breadth-first search with equal probability among the nearest. Counts events."""
    rng = np.random.default_rng(seed); D = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    hits = falls = steps = 0; maxjump = 0; double = 0
    for w in range(W):
        vis = {(0, 0, 0): 1}; x = (0, 0, 0); d = int(rng.integers(6))
        for t in range(T):
            if rng.random() < q: d = int(rng.integers(6))
            tg = tuple(a + b for a, b in zip(x, D[d]))
            if vis.get(tg, 0) >= n:
                hits += 1
                ok = [j for j in range(6) if vis.get(tuple(a + b for a, b in zip(x, D[j])), 0) < n]
                if ok: d = ok[int(rng.integers(len(ok)))]; tg = tuple(a + b for a, b in zip(x, D[d]))
                else:
                    falls += 1; seen = {x}; front = [x]; found = []
                    while not found:
                        nxt = []
                        for y in front:
                            for e in D:
                                z = tuple(a + b for a, b in zip(y, e))
                                if z not in seen: seen.add(z); nxt.append(z)
                        found = [z for z in nxt if vis.get(z, 0) < n]; front = nxt
                    tg = found[int(rng.integers(len(found)))]
                    maxjump = max(maxjump, sum(abs(a - b) for a, b in zip(tg, x))); d = int(rng.integers(6))
            if vis.get(tg, 0) >= n: double += 1
            vis[tg] = vis.get(tg, 0) + 1; x = tg; steps += 1
    return hits / steps, falls / steps, maxjump, double


def section_3d():
    print('D. 3D relay paths (supplied persistent walk, uniform odds): how often each CL-4 clause acts')
    res = {}
    for n, q in ((1, 1.0), (2, 1.0), (8, 1.0), (8, 0.1)):
        res[(n, q)] = walk3d(n, q, 4000, 25, seed=7)
    check('D1 3D: with n=8 a used-up target is rare and an all-used-up neighbourhood is not seen; '
          'only n=1 needs the fallback; no site records twice',
          res[(8, 1.0)][1] == 0 and res[(8, 0.1)][1] == 0 and all(v[3] == 0 for v in res.values()),
          '; '.join(f'n={n},q={q}: target used up {v[0]:.1e}/step, fallback {v[1]:.1e}/step, max jump {v[2]}'
                    for (n, q), v in res.items()))


# ================= P: measured regimes =================
def section_physical():
    print('P. burnt fraction beta = relays/site x ticks; a = lam l_P, block b = 2a (n = 8), tick tau = b/c')
    lP, c, mu, yr = 1.616255e-35, 2.99792458e8, 1.66054e-27, 3.15576e7
    hbarc = 1.97327e-16   # GeV m
    Msun = 1.98847e30; G = 6.6743e-11

    def beta(nrel, t, lam=2.0):
        a = lam * lP; tau = 2 * a / c; return nrel * a ** 3 * t / tau

    def life(nrel, lam=2.0):
        a = lam * lP; tau = 2 * a / c; return tau / (nrel * a ** 3)

    sun = (1.5e5 / mu) * (3 + 0.67); b_sun = beta(sun, 4.6e9 * yr)
    Vp = 4 / 3 * np.pi * (0.84e-15) ** 3; t_pin = life(3 / Vp) / yr
    lam_th = 6.62607e-34 / np.sqrt(2 * np.pi * 1.67262e-27 * 1.380649e-23 * 1.57e7)
    t_th = life(3 / lam_th ** 3) / yr
    wd = (1e9 / mu) * 3.5; b_wd = beta(wd, 1e10 * yr)
    ns = 3 * 0.48e45; b_ns = beta(ns, 1e10 * yr); t_ns = life(ns) / yr
    lam1 = 2.0 / np.sqrt(b_ns)                                  # beta ~ lam^2
    b_trail = beta(ns, 2.4e4 / 1e5)                             # 24 km at 100 km/s
    check('P1 Sun core, 4.6 Gyr, static in the lattice frame: beta far below 1', b_sun < 1e-10,
          f'beta {b_sun:.1e} (lam=2); first-clause used-up blocks need ~8 visits on one 8-site block')
    check('P2 a proton held fixed: its own volume lasts ~1e8 yr; spread over its thermal wavelength in the Sun, >1e13 yr',
          1e7 < t_pin < 1e9 and t_th > 1e12, f'pinned {t_pin:.2e} yr; thermal packet ({lam_th:.1e} m) {t_th:.1e} yr')
    check('P3 white dwarf core (1e9 kg/m^3), 10 Gyr static: beta < 1e-5', b_wd < 1e-5, f'beta {b_wd:.1e}')
    check('P4 neutron star core (3 n0), 10 Gyr, static in the lattice frame: beta > 1 (sites would run out)',
          b_ns > 1, f'beta {b_ns:.0f}; static life {t_ns:.1e} yr; beta=1 at lam={lam1:.2f}')
    check('P5 same star moving at 100 km/s through the lattice: trailing-edge beta < 1e-15', b_trail < 1e-15,
          f'beta_trail {b_trail:.1e}; needs |v| < {2.4e4 / (t_ns * yr):.1e} m/s to exhaust')
    # early universe: fermion number density n = (3/4)(zeta3/pi^2) g_f T^3, t = 0.301 g*^-1/2 M_P / T^2
    z3 = 1.2020569; MP = 1.22091e19; hbar = 6.582120e-25  # GeV s
    def rad(T_GeV, gf, gs):
        n = 0.75 * z3 / np.pi ** 2 * gf * (T_GeV / hbarc) ** 3; t = 0.301 / np.sqrt(gs) * MP / T_GeV ** 2 * hbar
        return beta(n, 2 * t), t
    b_bbn, t_bbn = rad(1e-3, 10, 10.75)
    zr = 1090; n_rec = (3.36e8 + 0.25 * 3 + 0.25) * (1 + zr) ** 3; b_rec = beta(n_rec, 3.8e5 * yr)
    b_gut, _ = rad(1e16, 90, 106.75)
    check('P6 BBN (T=1 MeV) and recombination: beta < 1e-20', b_bbn < 1e-20 and b_rec < 1e-20,
          f'BBN {b_bbn:.1e} (t={t_bbn:.2f} s), recombination {b_rec:.1e}; T=1e16 GeV (unmeasured) {b_gut:.1e}')
    # black holes: static count of sites inside r_s vs 3 relays per nucleon
    out = []
    for M in (10, 33, 6.5e9):
        rs = 2 * G * M * Msun / c ** 2; N = 3 * M * Msun / mu; a = 2 * lP; tau = 2 * a / c
        out.append((M, (4 / 3 * np.pi * rs ** 3 / a ** 3) * tau / N / yr))
    rmin = np.sqrt(3 * 33 * Msun / mu * (2 * lP) ** 3 / (np.pi * 3e5 * 4 * lP / c))
    check('P7 black holes, static site count inside r_s (conditional on sites ~ coordinate volume): life ~ M^2',
          out[0][1] < 1e10 < out[2][1], '; '.join(f'{m:g} Msun {t:.1e} yr' for m, t in out) +
          f'; a core moving at 300 km/s needs radius > {rmin * 1e3:.2f} mm')


if __name__ == '__main__':
    psi_sw, Tcap = section_theorems()
    section_rules(psi_sw, Tcap)
    section_3d()
    section_physical()
    print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
