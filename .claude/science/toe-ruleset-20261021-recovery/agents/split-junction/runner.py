#!/usr/bin/env python3
"""An exactly Lambda-conserving split: refraction junction + half-step corner map (supplied models; finite diagnostics;
no physical identification).
 A  rule-U cubic-frustum Regge FRW (edge l, central tick T, kappa = 1 per rung cell) through k^3 splits:
    scheduled split (split slice fixed, its edge varied) vs triggered split (split edge = threshold, the 4-volume of the
    split tick shared between parent and children at the stationary point); kick, matter loss, vacuum change, 4 splits
 B  split mode maps on the supplied cube tick (no copy mass; K_f = K_c/2 + pi m): energy no-go, corner map, half-step
    frame corner map, sign-projected (heat-free) map, sea heating, range; record 4-volume vs step algebra
 C  redshift under the edge reading through growth and a split
 D  estimates against measurement
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from math import comb
import numpy as np
from scipy.linalg import schur
from scipy.optimize import brentq
np.seterr(all='ignore')
T0 = time.monotonic(); PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ---------------- A. frustum carrier (rule U), several k^3 splits ----------------
def Af(u): return np.arcsin(u * u / (1 - u * u)) / np.sqrt(1 - 2 * u * u)
def gf(u): return np.sqrt(1 - 2 * u * u) * np.arcsin(u * u / (1 - u * u))
def fv(a, b): return (a + b) * (a * a + b * b) / 4
def fL(u): return -24 * u * np.arctanh(u) + 12 * gf(u)            # per-cell Lagrangian / l, u = ldot/2
def fLp(u, h=1e-6): return (fL(u + h) - fL(u - h)) / (2 * h)
class Carrier:
    """per original cell; slice values in rung units of the slab's own cell edge; a split slice stores the child edge"""
    def __init__(s, Cd, L0, c, k=2, nsplit=1, nafter=40, loss=0.0, rv=(0.0, 0.0)):
        s.k, s.Cd, s.loss, s.rv = k, Cd, loss, rv; ls, Ts, mesh = [1.0], [], []; u = np.sqrt((Cd + L0) / 3) / 2; m = 0; s.splits = []
        while True:
            l = ls[-1]; T = c * l / (2 * u); E = Cd / k ** (3 * m)
            uu = brentq(lambda x: E + L0 * fv(l, l + 2 * x * T) - 6 * (2 * l + 2 * x * T) * Af(x), 1e-300, (1 - 1e-15) / np.sqrt(2), xtol=1e-300, rtol=1e-15)
            if l + 2 * uu * T >= k and m < nsplit:
                Tk = brentq(lambda T_: E + L0 * fv(l, k) - 6 * (l + k) * Af((k - l) / (2 * T_)), (k - l) / np.sqrt(2) * 1.0000001, 1e6)
                ls.append(1.0); Ts.append(Tk); mesh.append(m); s.splits.append(len(ls) - 1); m += 1; u = (k - l) / (2 * Tk) / k; continue
            ls.append(l + 2 * uu * T); Ts.append(T); mesh.append(m); u = uu
            if m == nsplit and len(ls) - s.splits[-1] > nafter: break
        s.lr, s.mesh = np.array(ls), np.array(mesh); s.M = len(Ts); s.w = k ** (3.0 * s.mesh); s.sp = set(s.splits)
        s.V = np.array([Ts[n] * fv(*s.edges(n, s.lr)) for n in range(s.M)])
    def edges(s, n, lv): return lv[n], (s.k * lv[n + 1] if n + 1 in s.sp else lv[n + 1])
    def E(s, n): return s.Cd / s.w[n] * (1 - s.loss if s.mesh[n] > 0 else 1.0)
    def u(s, n, lv, V): a, b = s.edges(n, lv); return (b - a) * fv(a, b) / (2 * V[n])
    def slab(s, n, lv, V):
        a, b = s.edges(n, lv); T = V[n] / fv(a, b); uu = (b - a) / (2 * T)
        return s.w[n] * (6 * (a + b) * T * gf(uu) - s.E(n) * T - s.rv[min(s.mesh[n], 1)] * V[n])
    def cpm(s, j, lv):
        if j == 0: return 6 * lv[0] ** 2, 0.0
        if j in s.sp: A = s.w[j - 1] * 6 * (s.k * lv[j]) ** 2; return s.k * A, A
        A = s.w[j] * 6 * lv[j] ** 2; return A, A
    def local(s, j, lv, V):
        cp, cm = s.cpm(j, lv); out = s.slab(j - 1, lv, V) + s.slab(j, lv, V) + cp * np.arctanh(s.u(j, lv, V)) - cm * np.arctanh(s.u(j - 1, lv, V))
        out += s.cpm(j - 1, lv)[0] * np.arctanh(s.u(j - 1, lv, V))
        return out - (s.cpm(j + 1, lv)[1] * np.arctanh(s.u(j, lv, V)) if j + 1 <= s.M - 1 else 0.0)
    def eq(s, j, lv, V):
        h = 1e-7 * lv[j]; p, q = lv.copy(), lv.copy(); p[j] += h; q[j] -= h; return (s.local(j, p, V) - s.local(j, q, V)) / (2 * h)
    def Lam(s, n, lv, V): a, b = s.edges(n, lv); return (6 * (a + b) * Af(s.u(n, lv, V)) - s.E(n)) / fv(a, b)
    def root(s, f, ref, wd):
        for _ in range(60):
            if f(ref - wd) * f(ref + wd) < 0: break
            wd *= 1.5
        return brentq(f, ref - wd, ref + wd, xtol=1e-15, rtol=1e-14)
    def grow(s, j): return (s.k * s.lr[j + 1] - s.lr[j]) / s.k if j + 1 in s.sp else abs(s.lr[j + 1] - s.lr[j])
    def run(s, rule):
        lv = s.lr.copy(); V = s.V.copy(); j = 1; s.dSdd = 0.0
        while j < s.M - 1:
            if rule == 'trig' and j + 1 in s.sp:
                sj = j + 1; Vt = s.w[sj - 1] * V[sj - 1] + s.w[sj] * V[sj]
                def setd(d, V=V, sj=sj, Vt=Vt):
                    V2 = V.copy(); V2[sj - 1] = s.V[sj - 1] + d; V2[sj] = (Vt - s.w[sj - 1] * V2[sj - 1]) / s.w[sj]; return V2
                d = s.root(lambda d: s.eq(j, lv, setd(d)), 0.0, 0.05 * s.V[sj - 1]); V = setd(d)
                tgt = s.Lam(sj - 1, lv, V) - s.rv[0] + s.rv[1]          # stationarity in the partition (vacuum included)
                lv[sj + 1] = s.root(lambda lp: s.Lam(sj, np.concatenate([lv[:sj + 1], [lp], lv[sj + 2:]]), V) - tgt, s.lr[sj + 1], 0.3 * s.grow(sj))
                def part(W):   # every term of the phase that depends on the partition
                    out = s.slab(sj - 1, lv, W) + s.slab(sj, lv, W) + s.cpm(sj - 1, lv)[0] * np.arctanh(s.u(sj - 1, lv, W))
                    cp, cm = s.cpm(sj, lv); out += cp * np.arctanh(s.u(sj, lv, W)) - cm * np.arctanh(s.u(sj - 1, lv, W))
                    return out - s.cpm(sj + 1, lv)[1] * np.arctanh(s.u(sj, lv, W))
                e = 1e-5 * s.V[sj - 1]; s.dSdd = (part(setd(d + e)) - part(setd(d - e))) / (2 * e) / (s.w[sj - 1] * abs(tgt)); j = sj + 1; continue
            lv[j + 1] = s.root(lambda lp: s.eq(j, np.concatenate([lv[:j + 1], [lp], lv[j + 2:]]), V), s.lr[j + 1], 0.3 * s.grow(j) + 1e-12); j += 1
        Lm = np.array([s.Lam(n, lv, V) for n in range(s.M - 1)]); Lb = 0.5 * (Lm[1:] + Lm[:-1])
        H = np.array([2 * s.u(n, lv, V) / (0.5 * sum(s.edges(n, lv))) for n in range(s.M - 1)])
        seg = [0] + s.splits + [s.M - 2]; Ls = [Lb[seg[i] + 3:seg[i + 1] - 3].mean() for i in range(len(seg) - 1)]
        return Ls, H

print('== A. rule-U frustum Regge FRW through k^3 splits (dust + constant L0 = 0.005; kappa = 1)')
us = np.array([0.01, 0.1, 0.3, 0.6]); idn = np.abs((us * fLp(us) - fL(us)) / (-12 * Af(us)) - 1).max()
check('THEOREM: per-cell Lagrangian l f(u) - E, f = -24u artanh u + 12 sqrt(1-2u^2) asin(u^2/(1-u^2)), has energy function '
      'u f\' - f = -12 A(u); so the rule-U constant is Lambda = 12 A(u)/l^2 - rho (4-volume-translation charge)', idn < 1e-8, f'max rel dev {idn:.0e}')
kick, cont = {}, {}
for k in (2, 3, 4):
    for c in (0.004, 0.002):
        R = Carrier(0.05, 0.005, c, k); La, _ = R.run('sched'); Lt, _ = R.run('trig'); kick[(k, c)] = La[1] - La[0]; cont[(k, c)] = (Lt[1] - Lt[0], R.dSdd)
    rho = 0.05 / k ** 3 + 0.005; uc = brentq(lambda x: Af(x) - rho * k * k / 12, 1e-9, 0.7); uf = brentq(lambda x: k * fLp(x) - fLp(uc), 1e-9, uc)
    kick[k] = (12 * (k * k * Af(uf) - Af(uc)) / k ** 2, rho * rho * (k * k - 1) / 18)
rat = [kick[(k, 0.002)] / kick[k][0] for k in (2, 3, 4)]; lead = [kick[(k, 0.002)] / kick[k][1] for k in (2, 3, 4)]
check('THEOREM + check: a scheduled split kicks Lambda by 12[k^2 A(u_f) - A(u_c)]/L^2 with f\'(u_c) = k f\'(u_f) (momentum '
      'continuity) = (rho^2/3)[1/rho*(L) - 1/rho*(L/k)] at leading order; step-independent; telescopes, so no schedule avoids it',
      max(abs(r - 1) for r in rat) < 5e-4 and max(abs(x - 1) for x in lead) < 5e-3 and all(abs(kick[(k, 0.004)] / kick[(k, 0.002)] - 1) < 1e-3 for k in (2, 3, 4)),
      'discrete/continuum ' + ', '.join(f'{r:.5f}' for r in rat) + '; /leading ' + ', '.join(f'{x:.4f}' for x in lead) + ' (k = 2, 3, 4)')
rc = [abs(cont[(k, c)][0]) / kick[(k, c)] for k in (2, 3, 4) for c in (0.004, 0.002)]
check('THEOREM (refraction) + check: a split triggered at threshold edge, its moment free (the split tick\'s 4-volume shared '
      'at the stationary point), keeps Lambda continuous: residual is bulk drift only, falling with the step',
      max(rc) < 1e-3 and all(abs(cont[(k, 0.002)][0]) < abs(cont[(k, 0.004)][0]) for k in (2, 3, 4)) and max(abs(cont[(k, c)][1]) for k in (2, 3, 4) for c in (0.004, 0.002)) < 1e-5,
      'shift/kick ' + ', '.join(f'{x:.0e}' for x in rc) + '; dS/d(partition) <= ' + f'{max(abs(cont[(k, c)][1]) for k in (2, 3, 4) for c in (0.004, 0.002)):.0e}')
mat = []
for loss, rv in ((0.01, (0.0, 0.0)), (0.0, (50.0, 50.0)), (0.0, (50.0, 50.001))):
    R = Carrier(0.05, 0.005, 0.002, 2, loss=loss, rv=rv); La, _ = R.run('sched'); Lt, _ = R.run('trig'); mat.append((La[1] - La[0], Lt[1] - Lt[0]))
kk = kick[(2, 0.002)]; lost = 0.01 * 0.05 / 8
check('matter lost at the split: scheduled -> Lambda gains kick + lost density; triggered -> nothing (H absorbs it)',
      abs(mat[0][0] / (kk + lost) - 1) < 1e-4 and abs(mat[0][1]) < 1e-3 * lost, f'scheduled {mat[0][0] / (kk + lost):.5f} x (kick+lost); triggered {mat[0][1]:+.0e}')
check('vacuum density: both blind to a common rho_v = 1e4 Lambda0; a jump d rho_v enters the triggered junction 1:1, so '
      'CL-3\'s vacuum-phase subtraction (rho_v = 0 on both edge sets) is what makes it exact', abs(mat[1][0] / kk - 1) < 1e-4 and abs(mat[1][1]) < 1e-3 * kk and abs(mat[2][1] / 1e-3 - 1) < 1e-4,
      f'common: {mat[1][0] / kk:.5f} kick, {mat[1][1]:+.0e}; jump 1e-3: triggered shift {mat[2][1]:.5e}')
ms = {}
for rule in ('sched', 'trig'):
    R = Carrier(1e-6, 0.005, 0.002, 2, nsplit=4, nafter=60); Ls, H = R.run(rule)
    lnH = [np.log(H[a + 2:b - 2]).mean() for a, b in zip(R.splits[:-1], R.splits[1:])]
    ms[rule] = (np.diff(Ls) / 0.005, np.diff(lnH).mean(), np.mean([np.log(H[sp] / H[sp - 1]) for sp in R.splits]))
u2 = 0.005 * 4 / 12
check('4 splits, Lambda-dominated: scheduled raises Lambda by Lambda/rho* every split and drifts H up (blue); triggered '
      'keeps Lambda and has no mean drift; ln H steps (3/4)u^2 at a triggered split (u^2 scheduled)',
      np.all(abs(ms['sched'][0] / (0.005 / 6) - 1) < 0.02) and np.abs(ms['trig'][0]).max() < 1e-5 and abs(ms['trig'][1]) < 1e-5
      and abs(ms['trig'][2] / (0.75 * u2) - 1) < 0.02 and abs(ms['sched'][2] / u2 - 1) < 0.02,
      f"dLambda/L0 per split {ms['sched'][0].mean():.2e} vs {ms['trig'][0].mean():+.0e}; mean dlnH/split {ms['sched'][1]:+.1e} vs {ms['trig'][1]:+.0e}; "
      f"step {ms['trig'][2] / u2:.3f} vs {ms['sched'][2] / u2:.3f} u^2")

print('== B. split mode maps on the supplied cube tick (2^3 cubes; light states |w| < 0.3)')
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = (2 * CORN - 1).astype(float); OPP = 7 - np.arange(8)
def coherent(j, nv):
    th, ph, d = np.arccos(np.clip(nv[2], -1, 1)), np.arctan2(nv[1], nv[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, q)) * np.cos(th / 2) ** (d - q) * np.sin(th / 2) ** q * np.exp(1j * (q - j) * ph) for q in range(d + 1)])
XI = [coherent(1.5, v / np.sqrt(3)) for v in NV]; W0 = np.zeros((8, 8), complex)
for a_, b_ in itertools.product(range(8), repeat=2):
    if abs(CORN[a_] - CORN[b_]).sum() == 1: g_ = XI[a_].conj() @ XI[b_]; W0[a_, b_] = -g_ / abs(g_) / np.sqrt(3)
def Wa(x): return np.cos(x) * W0 + 1j * np.sin(x) * np.eye(8)
def half(psi, Wm, odd):
    X, Y, Z = psi.shape; p = np.roll(psi, -1, (0, 1, 2)) if odd else psi
    q = p.reshape(X // 2, 2, Y // 2, 2, Z // 2, 2).transpose(0, 2, 4, 1, 3, 5).reshape(-1, 8) @ (Wm[np.ix_(OPP, OPP)] if odd else Wm).T
    p = q.reshape(X // 2, Y // 2, Z // 2, 2, 2, 2).transpose(0, 3, 1, 4, 2, 5).reshape(X, Y, Z)
    return np.roll(p, 1, (0, 1, 2)) if odd else p
def blocks(eps, mu, L=8):
    b = np.pi / 2 - eps; We, Wo = Wa(mu / 2 + b), Wa(mu / 2 - b); N = L ** 3; E = np.eye(N).reshape(N, L, L, L)
    Ue, Uo = [np.stack([half(e, Wm, od).ravel() for e in E], 1) for Wm, od in ((We, 0), (Wo, 1))]; U = Uo @ Ue
    s_ = lambda v: np.ravel_multi_index(tuple(np.asarray(v) % L), (L, L, L)); n0 = np.array([1, 1, 1])
    return {R: np.array([[U[s_(2 * (n0 + R) + CORN[a]), s_(2 * n0 + CORN[c])] for c in range(8)] for a in range(8)]) for R in itertools.product((-1, 0, 1), repeat=3)}
def eigK(BL, K):
    T, Z = schur(sum(M * np.exp(-1j * (np.asarray(K, float) @ np.array(R, float))) for R, M in BL.items()), output='complex'); return -np.angle(np.diag(T)), Z
def Fh(eps, mu): a = 0.5 * (eps - mu / 2); return np.cos(a) * np.eye(8) - 1j * np.sin(a) * W0     # half of the even-cube step
def smap(BLc, BLf, K, kind, fr=None):
    Vs = [(np.asarray(K) / 2 + np.pi * m, np.prod((1 + np.exp(-1j * (np.asarray(K) / 2 + np.pi * m))) / 2) * np.eye(8)) for m in CORN]
    if kind == 'frame': Vs = [(Kf, fr[1].conj().T @ V @ fr[0]) for Kf, V in Vs]
    if kind != 'sign': return Vs, None
    omc, Zc = eigK(BLc, K); PF = [eigK(BLf, Kf) for Kf, _ in Vs]; out = np.zeros((64, 8), complex); svm = 1.0
    for sg in (1, -1):
        B = Zc[:, np.sign(omc) == sg]; X = np.vstack([PF[i][1][:, np.sign(PF[i][0]) == sg] @ (PF[i][1][:, np.sign(PF[i][0]) == sg].conj().T @ (V @ B)) for i, (_, V) in enumerate(Vs)])
        U_, sv, Vh = np.linalg.svd(X, full_matrices=False); out += (U_ @ Vh) @ B.conj().T; svm = min(svm, sv.min())
    return [(Vs[i][0], out[8 * i:8 * i + 8]) for i in range(8)], svm
def stats(BLc, BLf, K, Vs, tr=1.0):
    omc, Qc = eigK(BLc, K); fine = [eigK(BLf, Kf) for Kf, _ in Vs]; out = []
    for j in np.where(abs(omc) < 0.3)[0]:
        f_ = e_ = 0.0
        for (omf, Qf), (_, V) in zip(fine, Vs):
            p = np.abs(Qf.conj().T @ (V @ Qc[:, j])) ** 2; f_ += p[np.sign(omf) != np.sign(omc[j])].sum(); e_ += (p * omf).sum()
        out.append((f_, e_ / tr / omc[j]))
    return np.array(out)
dirs = [np.array([1, 0, 0.]), np.array([1, 1, 1.]) / np.sqrt(3), np.array([1, 2, 3.]) / np.sqrt(14)]
e0 = 0.371; s0 = np.sin(e0); BL0 = blocks(e0, 0.0); dev = 0.0; mism = []
for d in dirs:
    for kq in (0.05, 0.2):
        wc, wf = eigK(BL0, kq * d)[0], eigK(BL0, kq * d / 2)[0]; wcp, wfp = wc[wc > 0].min(), wf[wf > 0].min()
        dev = max(dev, abs(wcp - np.arccos(np.cos(e0) ** 2 + s0 * s0 * np.cos(kq * d).mean())))
        mism.append(((2 * wfp / wcp - 1) / kq ** 2, 0.75 * ((d ** 4).sum() / 24 - s0 * s0 / 72)))
check('THEOREM (no-go): massless light band cos w = cos^2 eps + sin^2 eps <cos K_i> exactly; a band-following split at fixed '
      'step raises each mode\'s energy by (3/4)[sum K_i^4/(24K^2) - sin^2(eps) K^2/72] > 0 in every direction; compensating it needs '
      'opposite-sign components, so no covariant split keeps both band and energy of every excitation', dev < 1e-12 and max(abs(a / b - 1) for a, b in mism) < 3e-3 and min(b for a, b in mism) > 0,
      'dE/E/K^2 ' + ', '.join(f'{a:.5f}' for a, b in mism[1::2]) + ' (axis, diagonal, (1,2,3); eps .371)')
cases = {'step x1 (2^4)': (e0, e0, 0.0, 0.0, 0.5), 'step x2 (2^3, fixed tick)': (np.arcsin(np.sin(0.3) / 2), 0.3, 0.0, 0.0, 1.0),
         'step x16 (2^3, fixed record 4-volume)': (np.arcsin(np.sin(0.3) / 16), 0.3, 0.0, 0.0, 8.0), 'x16 with mu 0.01 -> 0.08': (np.arcsin(np.sin(0.3) / 16), 0.3, 0.01, 0.08, 8.0)}
res = {}
for lab, (ec, ef, mc, mf, tr) in cases.items():
    BLc, BLf = blocks(ec, mc), blocks(ef, mf)
    for kind in ('corner', 'frame'):
        r = {}
        for kq in (0.02, 0.1):
            st = np.vstack([stats(BLc, BLf, kq * d, smap(BLc, BLf, kq * d, kind, (Fh(ec, mc), Fh(ef, mf)))[0], tr) for d in dirs]); r[kq] = (st[:, 0].mean(), st[:, 1].mean())
        res[(lab, kind)] = (r[0.02][0] / 0.02 ** 2, r[0.1][0] / 0.1 ** 2, r[0.02][1], ef)
fl = lambda lab, kind: res[(lab, kind)]
check('corner map: flips 0.04 K^2 at a kept step, but any step change flips ~eps_f^2 of every light mode (all K)',
      fl('step x1 (2^4)', 'corner')[0] < 0.06 and fl('step x2 (2^3, fixed tick)', 'corner')[0] > 5 and fl('step x16 (2^3, fixed record 4-volume)', 'corner')[0] > 20,
      '; '.join(f"{lab.split(' (')[0]}: flip/K^2 {fl(lab, 'corner')[0]:.3f} (K .02), {fl(lab, 'corner')[1]:.3f} (K .1)" for lab in list(cases)[:3]))
Pp = lambda BL, K: (lambda om, Z: Z[:, om > 0] @ Z[:, om > 0].conj().T)(*eigK(BL, K))
B1_, B2_ = blocks(0.15, 0.0), blocks(0.3, 0.0); P1_, P2_ = Pp(B1_, 0.004 * dirs[2]), Pp(B2_, 0.004 * dirs[2]); F1_, F2_ = Fh(0.15, 0.0), Fh(0.3, 0.0)
pdif = (np.linalg.norm(P1_ - P2_), np.linalg.norm(F1_ @ P1_ @ F1_.conj().T - F2_ @ P2_ @ F2_.conj().T))
fr_ok = all(0.03 < fl(lab, 'frame')[0] < 0.08 and 0.03 < fl(lab, 'frame')[1] < 0.08 and abs(fl(lab, 'frame')[2] - 1) < 1e-4 for lab in cases)
check('split at the midpoint of an even half-tick (half the step read from the parent\'s edges, half from the children\'s): '
      'flips stay 0.04-0.05 K^2 for every step change and the photon energy is continuous; the ticks need not be halved',
      fr_ok and pdif[1] < 1e-4 and pdif[0] > 0.1, '; '.join(f"{lab.split(' (')[0]}: {fl(lab, 'frame')[0]:.3f} K^2, E_f/E_c {fl(lab, 'frame')[2]:.5f}" for lab in cases)
      + f'. Why: light-band projector at K=.004, eps .15 vs .3: tick-boundary frame {pdif[0]:.2f}, midpoint frame {pdif[1]:.0e} (~K)')
g6 = (np.arange(6) + 0.5) / 6 * 2 * np.pi - np.pi; sea = {}
for lab, (ec, ef, mc, mf) in (('2^4', (0.3, 0.3, 0.4, 0.2)), ('x16', (np.arcsin(np.sin(0.3) / 16), 0.3, 0.05, 0.4))):
    BLc, BLf = blocks(ec, mc), blocks(ef, mf)
    for kind in ('frame', 'sign'):
        tot = n_ = 0.0; svm = 1.0
        for Kc in itertools.product(g6, repeat=3):
            Vs, sv = smap(BLc, BLf, np.array(Kc), kind, (Fh(ec, mc), Fh(ef, mf))); svm = min(svm, sv) if sv is not None else svm
            omc, Qc = eigK(BLc, np.array(Kc)); fine = [eigK(BLf, Kf) for Kf, _ in Vs]
            for j in np.where(omc < 0)[0]:
                n_ += 1; tot += sum((np.abs(Qf.conj().T @ (V @ Qc[:, j])) ** 2)[omf > 0].sum() for (omf, Qf), (_, V) in zip(fine, Vs))
        sea[(lab, kind)] = (tot / n_, svm)
check('THEOREM + check: a split that maps the half-filled sea to the sea isometrically must keep each band sign; the polar part '
      'of the corner map\'s sign blocks does (heating 0), the local maps heat ~20% of the sea per split',
      all(sea[(l, 'sign')][0] < 1e-25 and sea[(l, 'frame')][0] > 0.1 and sea[(l, 'sign')][1] > 0.5 for l in ('2^4', 'x16')),
      ', '.join(f"{l}: local {sea[(l, 'frame')][0]:.3f}, sign {sea[(l, 'sign')][0]:.0e} (min sv {sea[(l, 'sign')][1]:.2f})" for l in ('2^4', 'x16')))
Nc = 12; Nf = 2 * Nc; tail = {}
Rg = np.stack(np.meshgrid(*[np.arange(Nf)] * 3, indexing='ij'), -1); Rg = np.where(Rg > Nf // 2, Rg - Nf, Rg); dch = np.abs(Rg - 0.5).max(-1)
for mu in (0.6, 0.15, 0.0):
    BLc, BLf = blocks(0.371, mu), blocks(0.371, mu / 2); psi = np.zeros((Nf, Nf, Nf, 8, 8), complex); ks = 2 * np.pi * (np.arange(Nc) + 0.5) / Nc
    for ix, iy, iz in itertools.product(range(Nc), repeat=3):
        for (Kf, V), m in zip(smap(BLc, BLf, np.array([ks[ix], ks[iy], ks[iz]]), 'sign')[0], CORN): psi[tuple((np.array([ix, iy, iz]) + Nc * m) % Nf)] = V
    nrm = np.sqrt((np.abs(np.fft.ifftn(psi, axes=(0, 1, 2))) ** 2).sum(axis=(3, 4))); tail[mu] = (nrm[np.isclose(dch, 8.5)].max() / nrm.max(), (nrm[dch < 1] ** 2).sum() / (nrm ** 2).sum())
check('range of the heat-free map: its tails lengthen as the light mass falls (analytic sign blocks: range ~ 1/gap, i.e. the '
      'Compton length of the lightest sea species; slowest at mu = 0)', tail[0.6][0] < tail[0.15][0] < tail[0.0][0] and tail[0.0][0] > 30 * tail[0.6][0],
      'tail at 8.5 fine cubes: ' + ', '.join(f'mu {m}: {tail[m][0]:.0e}' for m in tail) + f'; weight on the 8 children {tail[0.0][1]:.3f} (mu 0)')
kj = [(k, j) for k in (1, 2, 3, 4) for j in (1 / 64, 1 / 27, 1 / 8, 1 / 2, 1, 2) if abs(k ** 3 * j - 1) < 1e-12 and abs(j / k - 1) < 1e-12]
check('THEOREM (algebra): a split by k in space and 1/j in tick keeps the record 4-volume iff k^3 j = 1 and the step iff j = k; '
      'both only for k = 1. At fixed record 4-volume a 2^3 split lengthens the tick 8-fold and sin(eps) x16, eps ~ l^-4 between splits', kj == [(1, 1)], f'solutions {kj}')

print('== C. redshift under the edge reading (fixed record 4-volume: tau ~ l^-3, sin eps = sqrt3 tau/l, mu = m tau)')
def wlight(K, s): return np.arccos(1 - s * s * (1 - np.cos(K).mean()))
Kv = 0.05 * dirs[2]; sfin = 0.04; r_ = []
for l in (1.0, 1.25, 1.6, 2.0):
    s = sfin / 16 * 2 ** 4 / l ** 4; r_.append(wlight(Kv, s) / (1.0 / l ** 3) * l)        # (omega/mu) * l, m tau0 = 1
rc_ = wlight(Kv, sfin / 16) / (1 / 8.0); rf_ = wlight(Kv / 2, sfin) / 1.0
check('edges growing at fixed record 4-volume: photon/atom phase ratio ~ 1/l (1+z = edge ratio) although eps falls 16-fold; '
      'across the half-step split it is continuous (C x B), so splits are invisible and the redshift is the edge growth',
      np.ptp(r_) / np.mean(r_) < 1e-3 and abs(rf_ / rc_ - 1) < 1e-3 and abs(fl('step x16 (2^3, fixed record 4-volume)', 'frame')[2] - 1) < 1e-4,
      f'(omega/mu) l spread {np.ptp(r_) / np.mean(r_):.0e} over l 1..2; at the split {rf_ / rc_:.6f} (band), map {fl("step x16 (2^3, fixed record 4-volume)", "frame")[2]:.6f}')

print('== D. against measurement (estimates; a = sqrt(8 pi) l_P, cube = 2a, unit map of the earlier probes)')
MP, T0K = 1.22089e19, 2.348e-13; a_s = np.sqrt(8 * np.pi) / MP; Hinf = 1e13
jump = 0.75 * (Hinf * 2 * a_s) ** 2          # u_c = H L/2, L = 2 cube edges = 4a
check('triggered split during inflation (H = 1e13 GeV): ln H steps by ~3(H a)^2, a log-periodic feature ~1e-10 in the '
      'spectrum, against the 1.2% per split decline n_s needs; the split neither supplies nor spoils the drift',
      jump < 1e-8, f'step {jump:.0e} per split vs needed -1.22e-02 per split (eps_H = 0.0176)')
cfl = fl('step x1 (2^4)', 'frame')[0]; Tmax = np.sqrt(30 * 2.7 * T0K / (cfl * (4 / 3) * 36 * a_s))   # K = 6aT, m_p = 1/a, sum 4/3
check('IF zone-edge partners are stable Planck-mass relics: 0.04 K^2 creation per particle per split bounds the hottest split '
      'epoch; the heat-free sign map or a sharper local map relaxes it', 1e3 < Tmax < 1e5, f'T_max ~ {Tmax:.0e} GeV for partner density <~ 1% of dark matter')
print('  Lambda: triggered splits add exactly 0 (scheduled: sum rho_s^2/rho*, needs first split below ~1 TeV); its size is the')
print('  first-slab datum + any non-split matter loss. n_s: needs a decaying component with eps_H = 0.0176; no law gives one.')
print('supplied: frustum carrier, central tick, dust/-E T, kappa = 1, reference slicing, threshold 2 rung units, the')
print('  partition clause, cube tick without copy mass at the listed (eps, mu), corner map family, half-step frame (chosen by')
print('  test), sign projection, unit map, H_inf, relic stability, measured numbers.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
