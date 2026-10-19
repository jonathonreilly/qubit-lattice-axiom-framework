#!/usr/bin/env python3
"""Candidate law CL-2 evidence: a record's qubit leaves the flow, and the network stays short that site's share.

Finite checks of stated toy rules on the cubic grid (2D slice for M1, 1D line for M6), supplied-model framing:
  M1 a wave packet (gamma = 1 weights) bends toward records that lower the pace and away from records that raise it;
  M2 the far field depends only on the total drain (single site, 3x3x3 block, 6-site star agree), the near field on its shape;
  M3 under a lean-away (chessboard) pace rule two records on opposite-colour sites cancel at long range; under averaging they add;
  M4 subtract-with-floor: sparse records give additive mass, a dense cluster freezes a region (pace 0) larger than itself;
     scale (multiplicative) drains never freeze and are not additive at the same strength;
  M5 the group delay of a packet through a pace well tends to the same value for every long wavelength (equivalence),
     with a lattice-scale excess growing as the wavelength approaches the spacing;
  M6 a pure hole (influence detours) has no far-field effect; a perfect absorber pulls but its mass per record falls
     as records are added (shielding); a fixed share per record is additive;
  M7 a record holding the pace it had when it formed has no effect;
  M8 timing: a one-time removal at formation leaves no lasting far field; a record permanently short one share
     settles to a steady 1/r value; an absorber settles too;
  M9 removed sites slow influence crossing a crowded slab, roughly in proportion to the removed fraction.
Supplied models only; no physical identification.
Companion: docs/CANDIDATE_LAW_CL2_A_RECORDS_QUBIT_LEAVES_THE_FLOW_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500

import sys
import numpy as np
import scipy.sparse.linalg as spl

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


def L3(u): return np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) + np.roll(u, 1, 2) + np.roll(u, -1, 2)


def main():
    # ---------------- M1 bending direction (2D slice)
    Lx, Ly = 400, 240; x = np.arange(Lx) - 100; y = np.arange(Ly) - Ly / 2; X, Y = np.meshgrid(x, y, indexing='ij')
    def run(phi_amp, dt=0.4, T=500):
        R = np.sqrt((X - 120) ** 2 + Y ** 2); Phi = phi_amp * np.exp(-R ** 2 / (2 * 25.0 ** 2)); m = (1 + Phi) ** -4.0
        env = np.exp(-((X + 40) ** 2) / (2 * 12.0 ** 2) - (Y - 40.0) ** 2 / (2 * 12.0 ** 2)); kx = 0.6
        u = env * np.cos(kx * X); v = kx * env * np.sin(kx * X)
        for _ in range(int(T / dt)):
            lap = np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) - 4 * u; v += dt * lap / m; u += dt * v
        E = u ** 2; mk = X > 200; return (E[mk] * Y[mk]).sum() / E[mk].sum()
    b0, bl, br = run(0.0), run(-0.05), run(+0.05)
    check("M1 a packet bends toward records that lower the pace and away from records that raise it",
          (bl - b0) < -3 and (br - b0) > 3, f"extra sideways shift: lower {bl - b0:+.2f}, raise {br - b0:+.2f} sites (negative = toward)")
    # ---------------- M2 far field depends only on the total drain
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
    check("M2 far field fixed by the total drain: single site, 3x3x3 block and 6-site star agree at r = 16; they differ close in (r = 3)",
          np.ptp(f16) < 1e-4 * abs(f16[0]) * 10 and np.ptp(f3) > 1e-3, f"r=16: {', '.join(f'{v:.5f}' for v in f16)}; r=3: {', '.join(f'{v:.5f}' for v in f3)}")
    # ---------------- M3 chessboard sign under lean-away
    Xs, Ys, Zs = np.meshgrid(*[np.arange(L)] * 3, indexing='ij'); stag = (-1.0) ** (Xs + Ys + Zs)
    def pair(pos, sign, chess):
        s = np.zeros((L,) * 3)
        for p in pos: s[p] = 1.0
        z = resp(s, sign); return far(z * stag if chess else z, 12)
    one = far(resp(s1, -1) * stag, 12)
    same, opp = pair([(0, 0, 0), (1, 1, 0)], -1, True), pair([(0, 0, 0), (1, 0, 0)], -1, True)
    av_opp = pair([(0, 0, 0), (1, 0, 0)], 1, False)
    check("M3 lean-away pace rule: two records on same-colour sites add, on opposite-colour sites cancel at long range; under averaging they add",
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
        x_, _ = spl.gmres(spl.LinearOperator((nf, nf), matvec=op), rhs, rtol=1e-11, restart=100, maxiter=3000)
        p = val.copy(); p[free] = x_; return p
    def subtract_floor(rec, q):
        fr = np.zeros_like(rec)
        for _ in range(60):
            p = solve(rec & ~fr, q, 'subtract', fr); new = fr | (p < 0)
            if (new == fr).all(): return p, fr
            fr = new
        return p, fr
    def mass(p): return (1 - p[c + 22, c, c]) / (1 / 22 - 1 / c)
    q = 0.2; sparse = (Xg % 4 == 0) & (Yg % 4 == 0) & (Zg % 4 == 0)
    per = []
    for rad in (4.5, 8.5):
        rec = (Rg <= rad) & sparse; p, fr = subtract_floor(rec, q); per.append((mass(p) / rec.sum(), int(fr.sum())))
    dense = Rg <= 3.2; pd, frd = subtract_floor(dense, q); r_fr = (3 * frd.sum() / (4 * np.pi)) ** (1 / 3)
    ps_s = [mass(solve((Rg <= rad) & sparse, q, 'scale')) / ((Rg <= rad) & sparse).sum() for rad in (4.5, 8.5)]
    ps_d = solve(dense, q, 'scale')
    check("M4 subtract-with-floor: sparse records additive (no freezing); a dense cluster freezes a region larger than itself. Scale drains: no freezing, not additive",
          abs(per[0][0] - per[1][0]) < 0.02 * per[0][0] and per[0][1] == per[1][1] == 0 and r_fr > 2 * 3.2 and ps_d.min() > 0 and ps_s[1] < 0.9 * ps_s[0],
          f"subtract per record {per[0][0]:.4f}, {per[1][0]:.4f}; dense radius 3.2 -> frozen radius {r_fr:.1f}; scale per record {ps_s[0]:.4f}, {ps_s[1]:.4f}, min pace {ps_d.min():.3f}")
    # ---------------- M5 equivalence: group delay vs wavelength
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
    check("M5 group delay through a pace well: within 6% of the long-wavelength value at wavelengths 42 and 21 sites; a lattice-scale excess (> 30%) at wavelength 6",
          abs(ratios[0] - 1) < 0.06 and abs(ratios[1] - 1) < 0.08 and ratios[2] > 1.3, f"delay / (2 int |Phi|) = {', '.join(f'{r:.3f}' for r in ratios)} at wavelengths 41.9, 20.9, 6.3")


    # ---------------- M6 hole vs absorber vs fixed share (41^3 grid)
    Lh = 41; ch = Lh // 2
    Xh, Yh, Zh = np.meshgrid(*[np.arange(Lh) - ch] * 3, indexing='ij'); Rh = np.sqrt(Xh ** 2 + Yh ** 2 + Zh ** 2)
    bh = np.zeros((Lh,) * 3, bool); bh[[0, -1], :, :] = bh[:, [0, -1], :] = bh[:, :, [0, -1]] = True
    shf = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    def rl(u, s_): return np.roll(np.roll(np.roll(u, s_[0], 0), s_[1], 1), s_[2], 2)
    def lin(op, rhs, n_):
        x_, _ = spl.gmres(spl.LinearOperator((n_, n_), matvec=op), rhs, rtol=1e-11, restart=100, maxiter=3000); return x_
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
    check("M6 pure hole: no far-field effect; perfect absorbers shield (mass per record falls); a fixed share per record is additive",
          dev < 1e-8 and abs33 < 0.7 * abs1 and abs(sh33 - sh1) < 0.02 * sh1,
          f"pure-hole max deviation {dev:.0e}; absorber per record {abs1:.3f} (1) -> {abs33:.3f} ({n33}); fixed share per record {sh1:.5f} -> {sh33:.5f}")
    # ---------------- M7 hold the formation-time pace
    rng_ = np.random.default_rng(4); sites = list(zip(*np.nonzero(Rh <= 2.2))); fixed = bh.copy(); val = np.where(bh, 1.0, 0.0)
    p = dirichlet(fixed, val)
    for j in rng_.permutation(len(sites))[:12]:
        s_ = sites[j]; val[s_] = p[s_]; fixed[s_] = True; p = dirichlet(fixed, val)
    check("M7 records that hold the pace they had when they formed have no effect", abs(mh(p)) < 1e-8, f"far-field mass after 12 records {mh(p):+.1e}")
    # ---------------- M8 timing
    Lt = 80; ct = Lt // 2
    def L3t(u): return np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) + np.roll(u, 1, 2) + np.roll(u, -1, 2) - 6 * u
    res = {}
    for rule in ('once', 'steady', 'absorber'):
        d0 = np.zeros((Lt,) * 3); d1 = d0.copy(); vals = []
        for step in range(1, 70 + 1):
            src_ = np.zeros((Lt,) * 3)
            if rule == 'steady': src_[ct, ct, ct] = 0.3
            if rule == 'once' and step == 1: src_[ct, ct, ct] = 0.3 * 40
            d2 = 2 * d1 - d0 + 0.25 * (L3t(d1) + src_); d0, d1 = d1, d2
            if rule == 'absorber': d1[ct, ct, ct] = 1.0
            if step in (56, 60, 64, 68): vals.append(10 * d1[ct + 10, ct, ct])
        res[rule] = vals
    st = np.mean(res['steady'])
    check("M8 timing: a record permanently short one share settles to a steady 1/r value; an absorber settles too; a one-time removal does not settle",
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
    check("M9 removed sites slow influence crossing a crowded slab, about in proportion to the removed fraction",
          0.8 < delays[0] / 0.05 < 1.8 and 0.8 < delays[1] / 0.1 < 1.8, f"fractional slowing {delays[0]:.3f} at 5%, {delays[1]:.3f} at 10%")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
