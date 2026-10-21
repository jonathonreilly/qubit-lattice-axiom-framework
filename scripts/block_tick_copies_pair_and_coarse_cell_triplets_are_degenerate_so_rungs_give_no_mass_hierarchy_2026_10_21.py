#!/usr/bin/env python3
"""Generations as a zoom phenomenon? Tests of rule-level copy and rung mechanisms against measured masses and mixing.

(A) The supplied spin-3/2 Margolus tick (one fermion mode per site): copies at one-block rung and in a coarse cell
    of 2^3 blocks (fine corners {0,pi}^3 folded to coarse K = 0).
(B) Exact copy-symmetry algebra for three copies: S3, C3, C3 with a real structure.
(C) Rung ladders: rung-independent rules, block-size suppression laws, a universal two-parameter rung map.
(D) Mixing implied by a shared copy symmetry.
Measured inputs are PDG/NuFIT central values (quoted below).  Supplied model, finite diagnostic; no physical
identification.  A PASS line states a true mathematical or numerical fact; several facts are failures of a
candidate mechanism against measurement, stated as such.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, sys, signal, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
def nrm(X): return np.abs(X).max()

# ---------------- measured inputs (MeV) ----------------
me, mmu, mtau, dtau = 0.51099895, 105.6583755, 1776.86, 0.12
mu_, mc_, mt_ = 2.16, 1270.0, 172690.0          # u(2 GeV), c(m_c), t (direct)
md_, ms_, mb_ = 4.67, 93.4, 4180.0              # d, s (2 GeV), b(m_b)
Vus = 0.22500; dVus = 0.00067; s13sq = 0.0220; s12sq = 0.307
def Q(m): m = np.array(m, float); return m.sum() / np.sqrt(m).sum() ** 2

# ---------------- (A) supplied Margolus tick (same construction as the covariant-tick runner) ----------------
C = np.array(list(itertools.product((0, 1), repeat=3))); c = C - 0.5
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): rots.append(R)
def img(R, i): return int(np.argmin(np.sum(abs(c - R @ c[i]), 1)))
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def axang(R):
    a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(a)), a
J3 = Jm(1.5)
xi = []
for i in range(8):
    n = (2 * C[i] - 1.0) / np.sqrt(3); w, v = np.linalg.eigh(sum(n[k] * J3[k] for k in range(3))); xi.append(v[:, -1])
def Lrot(R):
    n, a = axang(R); Dm = expm(-1j * a * sum(n[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = img(R, i); L[k, i] = xi[k].conj() @ Dm @ xi[i]
    return L
Ls = [Lrot(R) for R in rots]
Gm = np.array([[xi[a].conj() @ xi[b] for b in range(8)] for a in range(8)])
Wa = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1:
            ax = int(np.argmax(abs(C[a] - C[b]))); Wa[ax][a, b] = -Gm[a, b] / abs(Gm[a, b]) / np.sqrt(3)
W3 = sum(Wa); I8 = np.eye(8)
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def Wm(mu): return np.cos(mu / 2) * W3 + 1j * np.sin(mu / 2) * I8
def Utick(K, Vs):                       # half-steps alternate even (V) and odd (D^dag V D) partitions
    u = I8.astype(complex); d = Dg(K)
    for t, V in enumerate(Vs): u = (d.conj().T @ V @ d if t % 2 else V) @ u
    return u
def levels(u): return np.sort(np.mod(np.angle(np.linalg.eigvals(u)), 2 * np.pi))
def mults(lv, tol=1e-8):
    out, i = [], 0
    while i < len(lv):
        j = i
        while j + 1 < len(lv) and lv[j + 1] - lv[i] < tol: j += 1
        out.append(j - i + 1); i = j + 1
    if len(out) > 1 and (lv[0] + 2 * np.pi - lv[-1]) < tol: out[0] += out.pop()
    return out
def comm(Ms):
    A = np.vstack([np.kron(M, I8) - np.kron(I8, M.T) for M in Ms])
    _, s, Vh = np.linalg.svd(A); nd = int(np.sum(s < 1e-9)); return [v.reshape(8, 8) for v in Vh[len(s) - nd:].conj()]
rng = np.random.default_rng(7)

print('== A. supplied Margolus tick: copies at one block and in a coarse cell of 2^3 blocks')
Bs = comm(Ls)
Hb = []
for b in Bs:
    for h in ((b + b.conj().T) / 2, (b - b.conj().T) / 2j):
        if nrm(h) > 1e-9: Hb.append(h)
check('commutant of the 24 spin-3/2 corner actions has dim 4 (covariant block unitaries exp(i sum x_j H_j))', len(Bs) == 4, f'dim {len(Bs)}')
corners = [np.pi * np.array(k) for k in itertools.product((0, 1), repeat=3)]
ncnt = [int(round(k.sum() / np.pi)) for k in corners]
okm, okorb, allm = True, True, set()
for trial in range(30):
    nst = 2 * int(rng.integers(1, 5))
    Vs = [expm(1j * sum(rng.normal() * h for h in Hb)) for _ in range(nst)]
    lv = [levels(Utick(K, Vs)) for K in corners]
    for n in range(4):
        grp = [lv[i] for i in range(8) if ncnt[i] == n]
        okorb &= max(np.abs(g - grp[0]).max() for g in grp) < 1e-8
    for x in (lv[0], lv[7]):
        m = mults(x); allm |= set(m); okm &= all(q % 4 == 0 for q in m)
check('30 random covariant multi-step ticks: K = 0 and K = pi(1,1,1) levels have multiplicity 4k (copies come in pairs)',
      okm, f'multiplicities seen {sorted(allm)}')
check('coarse cell of 2^3 blocks: fine corners fold to coarse K = 0 in rotation orbits of sizes 1,3,3,1 (n = # of pi),'
      ' and corners in one orbit have identical spectra (each triplet is exactly degenerate)', okorb,
      f'orbit sizes {[ncnt.count(n) for n in range(4)]}')
# supplied mass tick W(mu): cos w = cos^2(mu/2) S - sin^2(mu/2), S = mean cos K
mu0 = 0.1; dev = 0
for K in corners:
    S = np.cos(K).mean(); w = np.arccos(np.cos(mu0 / 2) ** 2 * S - np.sin(mu0 / 2) ** 2)
    lv = levels(Utick(K, [Wm(mu0), Wm(mu0)])); dev = max(dev, min(np.abs(np.abs(np.angle(np.exp(1j * lv))) - w).max(), 9))
w_orb = [np.arccos(np.cos(mu0 / 2) ** 2 * (3 - 2 * n) / 3 - np.sin(mu0 / 2) ** 2) for n in range(4)]
check('W(mu) tick: coarse-cell levels |w_n| = arccos(cos^2(mu/2)(3-2n)/3 - sin^2(mu/2)); mu = 0.1 gives',
      dev < 1e-10, 'w_n = ' + ', '.join(f'{x:.4f}' for x in w_orb) + f'  (dev {dev:.1e})')
# zoom does not move the light mass: two fine ticks = one coarse tick, coarse momentum 2k
def light(K, mu): return np.min(np.abs(np.angle(np.linalg.eigvals(Utick(K, [Wm(mu), Wm(mu)])))))
k = 0.02; mc = np.sqrt((2 * light(np.array([k, 0, 0]), mu0)) ** 2 - (2 * k) ** 2 * (np.cos(mu0 / 2) ** 2) / 3)
check('one zoom step (2 fine ticks per coarse tick, K_c = 2K_f): coarse gap = 2 x fine gap, so the physical mass is'
      ' rung-invariant; zooming makes no new light copy', abs(mc - 2 * mu0) < 2e-4, f'coarse gap {mc:.5f} vs 2mu {2*mu0}')
# Wilson-type family cos w = A S - B: cos w_n is affine in n, so cos w0 - 2 cos w1 + cos w2 = 0
r1, r2 = mmu / me, mtau / mmu
x = np.linspace(1e-6, np.pi / r2, 200001)
f = np.cos(x / r1) - 2 * np.cos(x) + np.cos(r2 * x)
check('family cos w = A S - B (Margolus with any even/odd masses): one copy per orbit n = 0,1,2 cannot carry the lepton'
      ' ratios, since cos w0 - 2cos w1 + cos w2 = 0 has no root with w1/w0 = 206.77, w2/w1 = 16.817 (w2 <= pi)',
      f.max() < 0, f'f < 0 on (0, pi/16.817], f ~ -140 w1^2 near 0; small-w law w_n^2 affine in n gives w2/w1 -> sqrt2 = 1.414')

print('== B. three copies: what a copy symmetry allows')
P = np.roll(np.eye(3), 1, 0); T = np.eye(3)[[0, 2, 1]]; J = np.ones((3, 3))
def comm3(Ms):
    A = np.vstack([np.kron(M, np.eye(3)) - np.kron(np.eye(3), M.T) for M in Ms])
    s = np.linalg.svd(A, compute_uv=False); return int(np.sum(s < 1e-9))
check('S3 (perm rep = A1 + E): commutant dim 2 = span{1, J}, spectrum {a+2d, a-d, a-d}: at most 2 distinct masses',
      comm3([P, T]) == 2)
sq = np.sqrt([me, mmu, mtau]); a = sq.mean(); z = (sq * np.exp(-2j * np.pi * np.arange(3) / 3)).sum() / 3
rec = a + 2 * abs(z) * np.cos(np.angle(z) + 2 * np.pi * np.arange(3) / 3)
check('C3 only: commutant dim 3 (circulants a + bP + b*P^2); (a, |b|, phase) reproduce ANY three masses: 3 parameters'
      ' for 3 data, 0 predictions', comm3([P]) == 3 and np.allclose(np.sort(rec), np.sort(sq), rtol=1e-12),
      f'leptons: |b|/a = {abs(z)/a:.6f}, phase = {np.angle(z)%(2*np.pi/3):.6f} rad mod 2pi/3')
deg = [np.sort(1 + 2 * 0.4 * np.cos(ph + 2 * np.pi * np.arange(3) / 3)) for ph in (0, np.pi / 3, np.pi)]
check('C3 with a real structure (b real, i.e. an axis reflection or antiunitary symmetry) forces a degenerate pair;'
      ' three distinct masses need a complex phase off multiples of pi/3', all(np.isclose(d[0], d[1]) or np.isclose(d[1], d[2]) for d in deg))
Qs = [Q((1 + 2 * 0.5 * np.cos(ph + 2 * np.pi * np.arange(3) / 3)) ** 2) for ph in np.linspace(0, 2, 7)]
check('Koide Q = 1/3 + (2/3)|b|^2/a^2 on the sqrt-mass circulant, independent of the phase', np.allclose(Qs, 1 / 3 + 2 / 3 * 0.25))
Ql = Q([me, mmu, mtau]); dQ = abs(Q([me, mmu, mtau + dtau]) - Ql)
print(f'   measured Q: leptons {Ql:.6f} +- {dQ:.6f} (2/3 at {abs(Ql-2/3)/dQ:.1f} sigma); up {Q([mu_, mc_, mt_]):.4f}; down {Q([md_, ms_, mb_]):.4f}')
check('measured Koide Q: leptons within 1 sigma of 2/3, quarks not (so no species-blind Q = 2/3 mechanism)',
      abs(Ql - 2 / 3) < dQ and abs(Q([mu_, mc_, mt_]) - 2 / 3) > 0.1 and abs(Q([md_, ms_, mb_]) - 2 / 3) > 0.05)

print('== C. rung ladders')
rr = r1 / r2
check('rung-independent rule => m_(n+1)/m_n constant; measured lepton ratios 206.77 and 16.817 differ by x12.30',
      rr > 12 and rr < 12.4, f'ratio of ratios {rr:.4f}')
s = (5 + np.sqrt(21)) / 2
check('a geometric ladder obeys Koide only for sqrt-ratio s with s^2 - 5s + 1 = 0: mass ratio (23+5sqrt21)/2 per rung,'
      ' i.e. 1 : 22.96 : 527 vs measured 1 : 206.8 : 3477', np.isclose(Q([1, s**2, s**4]), 2 / 3),
      f'ratio {s**2:.4f}')
lr = lambda m: np.log(m[1] / m[0]) / np.log(m[2] / m[1])
Lz = {'leptons': lr([me, mmu, mtau]), 'up': lr([mu_, mc_, mt_]), 'down': lr([md_, ms_, mb_])}
check('suppression m_n ~ exp(-c L_n), L_n = 2^n: predicts ln(m2/m1)/ln(m3/m2) = 2 (8 for L = 8^n); measured differ'
      ' and differ by species', all(abs(v - 2) > 0.1 for v in Lz.values()),
      ', '.join(f'{k} {v:.4f}' for k, v in Lz.items()) + f'; c fitted to mu/e predicts tau/mu {np.sqrt(r1):.2f} vs {r2:.3f}')
lm = np.log([me, mmu, mtau]); cc = (lm[2] - lm[1]) / (lm[1] - lm[0]); Ls_ = (lm[1] - cc * lm[0]) / (1 - cc)
flow = lambda m: np.exp(Ls_ + cc * (np.log(m) - Ls_))
pred = {'c from u': (flow(mu_), mc_), 't from c': (flow(mc_), mt_), 's from d': (flow(md_), ms_), 'b from s': (flow(ms_), mb_)}
check('universal 2-parameter rung map ln m -> L* + c(ln m - L*) fitted to leptons (c = %.4f, m* = %.1f GeV) mispredicts'
      ' every quark step by more than x2' % (cc, np.exp(Ls_) / 1e3), all(max(p / o, o / p) > 2 for p, o in pred.values()),
      '; '.join(f'{k} {p/o:.2f}x' for k, (p, o) in pred.items()))

print('== D. mixing from a shared copy symmetry')
F = np.exp(2j * np.pi * np.outer(range(3), range(3)) / 3) / np.sqrt(3)
Mu_ = F @ np.diag([1, 5, 9]) @ F.conj().T; Md_ = F @ np.diag([2, 3, 7]) @ F.conj().T
Uu = np.linalg.eigh(Mu_)[1]; Ud = np.linalg.eigh(Md_)[1]; V = np.abs(Uu.conj().T @ Ud)
check('up and down both circulant in one copy basis: CKM is a permutation matrix, |V_us| = 0 vs measured 0.22500 +- 0.00067',
      np.allclose(np.sort(V.ravel()), [0] * 6 + [1] * 3, atol=1e-10), f'{Vus/dVus:.0f} sigma')
Up = np.abs(F) ** 2
check('circulant charged leptons with diagonal neutrinos: |U|^2 = 1/3 everywhere, sin^2 th13 = 1/3, sin^2 th12 = 1/2'
      ' vs measured 0.0220 and 0.307', np.allclose(Up, 1 / 3))

print('== E. reference: Brannen form, r and delta supplied (not produced by any tick here)')
A_ = np.sqrt(me) + np.sqrt(mmu); B_ = me + mmu
d0 = 2 / 9; sqb = 1 + np.sqrt(2) * np.cos(d0 + 2 * np.pi * np.arange(3) / 3); mb = np.sort(sqb ** 2)
print(f'   r = 1/2, delta = 2/9: mu/e {mb[1]/mb[0]:.3f} (meas {r1:.3f}), tau/mu {mb[2]/mb[1]:.4f} (meas {r2:.4f});'
      f' Koide (Q = 2/3) m_tau from e, mu: {(2*A_+np.sqrt(6*A_**2-3*B_))**2:.2f} MeV (meas {mtau} +- {dtau})')
check('Brannen (r = 1/2, delta = 2/9) reproduces both lepton ratios within 0.1%, with two supplied constants for two ratios',
      abs(mb[1] / mb[0] / r1 - 1) < 1e-3 and abs(mb[2] / mb[1] / r2 - 1) < 1e-3)
print('supplied: tick, j = 3/2 action, partitions, masses; measured PDG/NuFIT values; rung-to-copy assignments.')
print('not established: any tick-level mechanism giving three non-degenerate light copies, Koide r, delta, or mixing.')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
