#!/usr/bin/env python3
"""Finite supplied scalar rules: neutralized Green identities, floor complementarity,
static Dirichlet comparisons, pre-wrap packet diagnostics and exact torus means.
No universal dynamics classification or physical records-to-gravity bridge.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = ('docs/CANDIDATE_LAWS.md', 'docs/CANDIDATE_LAW_CL2_A_RECORDS_QUBIT_LEAVES_THE_FLOW_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/audit/AXIOM_MINIMALITY_POLICY.md', 'docs/audit/data/axiom_premise_nodes.json', 'archive/record_flow_review_2026_10_18/MANIFEST.json')

import sys, os, signal, time
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['VECLIB_MAXIMUM_THREADS']='1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
_STARTED=time.monotonic()
def _timeout(*args):
    raise TimeoutError('Owning 1500-second aggregate cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM,_timeout)
signal.setitimer(signal.ITIMER_REAL,AUDIT_TIMEOUT_SEC-2)
import numpy as np
import scipy.sparse.linalg as spl

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def certified_solve(op,rhs,n,label):
    operator=spl.LinearOperator((n,n),matvec=op,dtype=float)
    x,info=spl.gmres(operator,rhs,rtol=2e-13,atol=0.0,restart=100,maxiter=3000)
    residual=float(np.linalg.norm(op(x)-rhs)/max(1.0,np.linalg.norm(rhs)))
    check(label+' linear solve',info==0 and np.all(np.isfinite(x)) and residual<2e-11,f'info={info} normalized_residual={residual:.3e}')
    if info!=0 or not np.all(np.isfinite(x)) or residual>=2e-11:raise RuntimeError('Uncertified linear solve')
    return x


def L3(u): return np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) + np.roll(u, 1, 2) + np.roll(u, -1, 2)


def main():
    # ---------------- M1 bending direction (2D slice)
    Lx, Ly = 400, 240; x = np.arange(Lx) - 100; y = np.arange(Ly) - Ly / 2; X, Y = np.meshgrid(x, y, indexing='ij')
    def run(phi_amp, dt=0.4, T=260):
        R = np.sqrt((X - 120) ** 2 + Y ** 2); Phi = phi_amp * np.exp(-R ** 2 / (2 * 25.0 ** 2)); m = (1 + Phi) ** -4.0
        env = np.exp(-((X + 40) ** 2) / (2 * 12.0 ** 2) - (Y - 40.0) ** 2 / (2 * 12.0 ** 2)); kx = 0.6
        u = env * np.cos(kx * X); v = kx * env * np.sin(kx * X)
        boundary_weight=0.0
        edge=(X < -90)|(X>289)|(Y < -110)|(Y>109)
        for _ in range(int(T / dt)):
            lap = np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) - 4 * u; v += dt * lap / m; u += dt * v
            power=u*u; boundary_weight=max(boundary_weight,float(power[edge].sum()/power.sum()))
        E=u*u; mk=(X>140)&(X<280)
        fraction=float(E[mk].sum()/E.sum()); peak=float(x[np.argmax(E.sum(axis=1))])
        check('packet pre-wrap detection '+str(phi_amp),fraction>.5 and boundary_weight<.05 and 140<peak<280,f'T={T} detected_u2_fraction={fraction:.6g} peak_x={peak} max_boundary_u2_fraction={boundary_weight:.6g}')
        return float((E[mk]*Y[mk]).sum()/E[mk].sum())
    b0, bl, br = run(0.0), run(-0.05), run(+0.05)
    check("finite pre-wrap scalar packet centroid direction",
          (bl - b0) < 0 and (br - b0) > 0, f"extra sideways shift: lower {bl - b0:+.2f}, raise {br - b0:+.2f} sites (negative = toward)")
    # ---------------- finite neutralized source proxies
    L = 96; k = 2 * np.pi * np.fft.fftfreq(L); KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij'); avg = (np.cos(KX) + np.cos(KY) + np.cos(KZ)) / 3
    def resp(src, sign):
        den = 1 - sign * avg
        with np.errstate(divide='ignore'): G = np.where(np.abs(den) < 1e-12, 0.0, 1.0 / den)
        return np.real(np.fft.ifftn(G * np.fft.fftn(src)))
    def far(d, r): return d[r, 0, 0] - d[L // 2, 0, 0]
    s1 = np.zeros((L,) * 3); s1[0, 0, 0] = 1.0
    s27 = np.zeros((L,) * 3); s27[np.ix_([-1, 0, 1], [-1, 0, 1], [-1, 0, 1])] = 1 / 27
    s6 = np.zeros((L,) * 3)
    for dx in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)): s6[dx] = 1 / 6
    d = [resp(s, 1) for s in (s1, s27, s6)]
    f16 = [far(z, 16) for z in d]; f3 = [far(z, 3) for z in d]
    check("finite neutralized source proxies at r16 and r3",
          np.ptp(f16) < 1e-4 * abs(f16[0]) * 10 and np.ptp(f3) > 1e-3, f"r=16: {', '.join(f'{v:.5f}' for v in f16)}; r=3: {', '.join(f'{v:.5f}' for v in f3)}")
    # ---------------- M3 chessboard sign under lean-away
    Xs, Ys, Zs = np.meshgrid(*[np.arange(L)] * 3, indexing='ij'); stag = (-1.0) ** (Xs + Ys + Zs)
    arbitrary=np.random.default_rng(9826).normal(size=(L,)*3)
    plus=resp(arbitrary,1); minus=resp(arbitrary,-1)
    ordinary=plus-L3(plus)/6-(arbitrary-arbitrary.mean())
    staggered=minus+L3(minus)/6-(arbitrary-stag*np.mean(stag*arbitrary))
    check('arbitrary-source torus neutralization and conjugacy',max(np.max(abs(ordinary)),np.max(abs(staggered)),np.max(abs(minus-stag*resp(stag*arbitrary,1))))<1e-10)
    check('torus gauge constraints',abs(plus.mean())<1e-12 and abs(np.mean(stag*minus))<1e-12)
    def pair(pos, sign, chess):
        s = np.zeros((L,) * 3)
        for p in pos: s[p] = 1.0
        z = resp(s, sign); return far(z * stag if chess else z, 12)
    one = far(resp(s1, -1) * stag, 12)
    same, opp = pair([(0, 0, 0), (1, 1, 0)], -1, True), pair([(0, 0, 0), (1, 0, 0)], -1, True)
    av_opp = pair([(0, 0, 0), (1, 0, 0)], 1, False)
    check("finite staggered and ordinary source proxy comparisons",
          abs(same - 2 * one) < 0.15 * abs(one) and abs(opp) < 0.2 * abs(one) and av_opp > 1.8 * far(resp(s1, 1), 12),
          f"one record {one:+.5f}; same colour {same:+.5f}; opposite colour {opp:+.5f}; averaging, opposite colour {av_opp:+.5f}")
    # ---------------- M4 subtract with floor vs scale
    Lg = 61; c = Lg // 2
    Xg, Yg, Zg = np.meshgrid(*[np.arange(Lg) - c] * 3, indexing='ij'); Rg = np.sqrt(Xg ** 2 + Yg ** 2 + Zg ** 2)
    bd = np.zeros((Lg,) * 3, bool); bd[[0, -1], :, :] = bd[:, [0, -1], :] = bd[:, :, [0, -1]] = True
    def solve(rec, q, mode, frozen=None):
        fixed = bd if frozen is None else (bd | frozen); val = np.where(bd, 1.0, 0.0); free = ~fixed; nf = int(free.sum())
        def op(v):
            u = np.zeros((Lg,) * 3); u[free] = v; nb = L3(u)
            return (6 * u - (np.where(rec, (1 - q) * nb, nb) if mode == 'scale' else nb))[free]
        nbg = L3(val); rhs = (np.where(rec, (1 - q) * nbg, nbg) if mode == 'scale' else nbg - 6 * q * rec)[free]
        x_=certified_solve(op,rhs,nf,'floor/scale '+mode)
        p = val.copy(); p[free] = x_; return p
    def subtract_floor(rec, q):
        # Primal-dual active set, permitting release; p>=0, w=(I-A)p+q rec>=0, p*w=0.
        fr=np.zeros_like(rec)
        for iteration in range(200):
            p=solve(rec,q,'subtract',fr)
            w=p-L3(p)/6+q*rec
            residual=float(np.max(abs(p[~bd]-np.maximum(L3(p)[~bd]/6-q*rec[~bd],0))))
            new=(p-w<=0)&~bd
            if np.array_equal(new,fr) and residual<1e-9:
                complementarity=float(max(np.max(np.maximum(-p[~bd],0)),np.max(np.maximum(-w[~bd],0)),np.max(abs(p[~bd]*w[~bd]))))
                check('floor complementarity',complementarity<1e-8,f'iterations={iteration+1} fixed_point={residual:.3e} complementarity={complementarity:.3e} active={fr.sum()}')
                return p,fr
            fr=new
        raise RuntimeError('Floor active set did not certify a fixed point in 200 iterations')
    def mass(p): return (1 - p[c + 22, c, c]) / (1 / 22 - 1 / c)
    q = 0.2; sparse = (Xg % 4 == 0) & (Yg % 4 == 0) & (Zg % 4 == 0)
    per = []
    for rad in (4.5, 8.5):
        rec = (Rg <= rad) & sparse; p, fr = subtract_floor(rec, q); per.append((mass(p) / rec.sum(), int(fr.sum())))
    dense = Rg <= 3.2; pd, frd = subtract_floor(dense, q); r_fr = (3 * frd.sum() / (4 * np.pi)) ** (1 / 3)
    ps_s = [mass(solve((Rg <= rad) & sparse, q, 'scale')) / ((Rg <= rad) & sparse).sum() for rad in (4.5, 8.5)]
    ps_d = solve(dense, q, 'scale')
    exterior=~dense&~bd
    check('floor source support and positive exterior',not np.any(frd&~dense) and np.min(pd[exterior])>0 and np.min(ps_d)>0,
          f'sparse proxy/count={per}; dense active={frd.sum()} active_volume_radius={r_fr:.6g}; scale proxies={ps_s}; scale_min={ps_d.min():.6g}')
    # ---------------- chosen scalar packet delay vs wavelength
    L1 = 20000; x1 = np.arange(L1) - L1 / 2; Phi = -0.02 * np.exp(-x1 ** 2 / (2 * 150.0 ** 2)); mw = (1 + Phi) ** -4.0; pred = 2 * np.sum(np.abs(Phi))
    def signal(mm, kc, w, dt=0.4):
        u = np.exp(-(x1 + 1500) ** 2 / (2 * w ** 2)) * np.cos(kc * x1)
        K = 2 * np.pi * np.fft.fftfreq(L1); U = np.fft.fft(u); W = 2 * np.abs(np.sin(K / 2)); U[K < 0] = 0
        u = 2 * np.real(np.fft.ifft(U)); v = 2 * np.real(np.fft.ifft(-1j * W * U))
        det = int(L1 / 2 + 1500); t = 0.0; sig = []
        while t < 3000 + 8 * w + 800:
            lap = np.roll(u, 1) + np.roll(u, -1) - 2 * u; v += dt * lap / mm; u += dt * v; t += dt; sig.append(u[det])
        s_ = np.array(sig) ** 2; tt = np.arange(len(s_)) * dt; return (s_ * tt).sum() / s_.sum()
    ratios = []
    for kc, w in ((0.15, 120.0), (0.3, 80.0), (1.0, 60.0)):
        ratios.append((signal(mw, kc, w) - signal(np.ones(L1), kc, w)) / pred)
    check("finite scalar delay: 6% and 8% continuum comparisons; short wavelength excess",
          abs(ratios[0] - 1) < 0.06 and abs(ratios[1] - 1) < 0.08 and ratios[2] > 1.3, f"delay / (2 int |Phi|) = {', '.join(f'{r:.3f}' for r in ratios)} at wavelengths 41.9, 20.9, 6.3")


    # ---------------- M6 hole vs absorber vs fixed share (41^3 grid)
    Lh = 41; ch = Lh // 2
    Xh, Yh, Zh = np.meshgrid(*[np.arange(Lh) - ch] * 3, indexing='ij'); Rh = np.sqrt(Xh ** 2 + Yh ** 2 + Zh ** 2)
    bh = np.zeros((Lh,) * 3, bool); bh[[0, -1], :, :] = bh[:, [0, -1], :] = bh[:, :, [0, -1]] = True
    shf = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    def rl(u, s_): return np.roll(np.roll(np.roll(u, s_[0], 0), s_[1], 1), s_[2], 2)
    def lin(op, rhs, n_):
        return certified_solve(op,rhs,n_,'Dirichlet graph')
    def pure(rec):
        live = ~rec; free = live & ~bh; nf = int(free.sum()); nl = sum(rl(live.astype(float), s_) for s_ in shf); val = np.where(bh, 1.0, 0.0)
        def op(v):
            u = np.zeros((Lh,) * 3); u[free] = v; return (nl * u - sum(rl(u * live, s_) for s_ in shf))[free]
        p = val.copy(); p[free] = lin(op, sum(rl(val * live, s_) for s_ in shf)[free], nf); return p
    def dirichlet(fixed, val):
        free = ~fixed; nf = int(free.sum())
        def op(v):
            u = np.zeros((Lh,) * 3); u[free] = v; return (6 * u - L3(u))[free]
        g = np.where(fixed, val, 0.0); p = g.copy(); p[free] = lin(op, L3(g)[free], nf); return p
    def share(rec, q_):
        free = ~bh; nf = int(free.sum()); val = np.where(bh, 1.0, 0.0)
        def op(v):
            u = np.zeros((Lh,) * 3); u[free] = v; return (6 * u - L3(u))[free]
        p = val.copy(); p[free] = lin(op, L3(val)[free] - 6 * q_ * rec[free], nf); return p
    def mh(p): return (1 - p[ch + 14, ch, ch]) / (1 / 14 - 1 / ch)
    sp4 = (Xh % 4 == 0) & (Yh % 4 == 0) & (Zh % 4 == 0)
    ph = pure(Rh <= 3.2); dev = np.nanmax(np.abs(np.where(Rh <= 3.2, np.nan, ph) - 1))
    abs1 = mh(dirichlet(bh | (Rh <= 0.5), np.where(bh, 1.0, 0.0))); recs = (Rh <= 8.5) & sp4; n33 = int(recs.sum())
    abs33 = mh(dirichlet(bh | recs, np.where(bh, 1.0, 0.0))) / n33
    sh1 = mh(share(Rh <= 0.5, 0.01)); sh33 = mh(share(recs, 0.01)) / n33
    check("finite uniform-boundary hole and position-dependent source proxies",
          dev < 1e-8 and abs33 < 0.7 * abs1 and abs(sh33 - sh1) < 0.02 * sh1,
          f"pure-hole max deviation {dev:.0e}; absorber per record {abs1:.3f} (1) -> {abs33:.3f} ({n33}); fixed share per record {sh1:.5f} -> {sh33:.5f}")
    # ---------------- pin the current static equilibrium
    rng_ = np.random.default_rng(4); sites = list(zip(*np.nonzero(Rh <= 2.2))); fixed = bh.copy(); val = np.where(bh, 1.0, 0.0)
    p = dirichlet(fixed, val)
    for j in rng_.permutation(len(sites))[:12]:
        s_ = sites[j]; val[s_] = p[s_]; fixed[s_] = True; p = dirichlet(fixed, val)
    check("pinning vertices to their existing static equilibrium values", abs(mh(p)) < 1e-8, f"far-field mass after 12 records {mh(p):+.1e}")
    # ---------------- M8 timing
    Lt = 80; ct = Lt // 2
    def L3t(u): return np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) + np.roll(u, 1, 2) + np.roll(u, -1, 2) - 6 * u
    res = {}
    for rule in ('once', 'steady', 'absorber'):
        d0 = np.zeros((Lt,) * 3); d1 = d0.copy(); vals = []; mean_error=0.0; m0=m1=0.0
        for step in range(1, 70 + 1):
            src_ = np.zeros((Lt,) * 3)
            if rule == 'steady': src_[ct, ct, ct] = 0.3
            if rule == 'once' and step == 1: src_[ct, ct, ct] = 0.3 * 40
            d2 = 2 * d1 - d0 + 0.25 * (L3t(d1) + src_); d0, d1 = d1, d2
            injection=0.0
            if rule == 'absorber':
                injection=(1.0-d1[ct,ct,ct])/Lt**3
                d1[ct,ct,ct]=1.0
            expected=2*m1-m0+.25*src_.mean()+injection
            mean_error=max(mean_error,abs(float(d1.mean())-expected));m0,m1=m1,float(d1.mean())
            if rule=='steady':mean_error=max(mean_error,abs(m1-.075*step*(step+1)/(2*Lt**3)))
            if rule=='once':mean_error=max(mean_error,abs(m1-3*step/Lt**3))
            if step in (56, 60, 64, 68): vals.append(10 * d1[ct + 10, ct, ct])
        res[rule] = vals
        check('exact torus mean '+rule,mean_error<1e-12,f'mean_at_70={m1:.12g} recurrence_error={mean_error:.3e}; no stationarity inferred')
    st = np.mean(res['steady'])
    check("finite r10 trace variation over ticks56-68 only",
          np.ptp(res['steady']) < 0.25 * abs(st) and np.ptp(res['absorber']) < 0.25 * abs(np.mean(res['absorber'])) and np.ptp(res['once']) > 1.0 * abs(st),
          f"r*d late values: steady {', '.join(f'{v:+.3f}' for v in res['steady'])}; absorber {', '.join(f'{v:+.3f}' for v in res['absorber'])}; once {', '.join(f'{v:+.3f}' for v in res['once'])}")
    # ---------------- M9 crowded removed sites slow influence
    rng2 = np.random.default_rng(2); Lx2, Ly2 = 600, 48; sh2 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def crossing(f, dt=0.5):
        live = np.ones((Lx2, Ly2), bool); slab = np.zeros((Lx2, Ly2), bool); slab[250:350, :] = True
        live[slab & (rng2.random((Lx2, Ly2)) < f)] = False; xx = np.arange(Lx2)[:, None] * np.ones((1, Ly2))
        u = np.exp(-(xx - 150) ** 2 / 450.0) * live; v = (xx - 150) / 225.0 * np.exp(-(xx - 150) ** 2 / 450.0) * live
        nlive = sum(np.roll(np.roll(live, a, 0), b, 1) for a, b in sh2); t = 0.0; sig = []
        while t < 420:
            lap = sum(np.roll(np.roll(u, a, 0), b, 1) * np.roll(np.roll(live, a, 0), b, 1) for a, b in sh2) - u * nlive
            v += dt * lap * live; u += dt * v; u *= live; t += dt; sig.append(u[420].mean())
        s_ = np.array(sig) ** 2; tt = np.arange(len(s_)) * dt; return (s_ * tt).sum() / s_.sum()
    t0c = crossing(0.0); delays = [(crossing(f) - t0c) / 100 for f in (0.05, 0.1)]
    check("two seeded slab excess crossing-time diagnostics",
          0.8 < delays[0] / 0.05 < 1.8 and 0.8 < delays[1] / 0.1 < 1.8, f"excess crossing time / 100 sites: {delays[0]:.6g} at 5%, {delays[1]:.6g} at 10%; not fractional speed")

    print('per_element: full floor complementarity and normalized linear residuals are checked before finite proxy comparisons.')
    print('per_site: equal drain and scalar wave weights are supplied choices, not consequences of the local qubit algebra.')
    print('per_mode: zero and checkerboard torus projections are explicit; packet diagnostics use chosen amplitude weights.')
    print('per_block: finite geometries, source supports, seeds and detection windows are printed or fixed in the bound source.')
    print('lattice_wide: no universal dynamics, stationary torus field, physical gravity or empirical readout conclusion is established.')
    print('elapsed_seconds',time.monotonic()-_STARTED)
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
