#!/usr/bin/env python3
"""Checks for J:derive:the-two-place-test-with-the-walk-as-test-body:a2
(worker w-macbookpro9927a-j096b).  See ATTEMPT.md for the statements.

EXACT (fractions): block 116's held box of side 9 and its field
g = (1 - A)^{-1} delta_S with zero wall values; its exact residual; block 116
T4(c)'s witness numbers.

FLOATING POINT (labelled, controlled): block 54's walk as the test body,
i dchi/dt = phi H phi chi with phi = 1 - k E_B g, at first order in k.  Each
walk number is produced two independent ways, and the checks assert that they
agree:
  - the Duhamel derivative from an augmented linear system (expm_multiply);
  - an eigendecomposition (box 9) or a symmetric finite difference in k (box 61).
The run is single-threaded.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import itertools
import time
from fractions import Fraction as F

import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import cg, expm_multiply

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")


# ------------------------------------------------------------------ exact box 9


def exact_field(n, src):
    """g = (1-A)^{-1} delta_src inside a box of odd side n (coords -h..h), zero on the wall layer."""
    h = (n - 1) // 2
    m = h - 1
    sites = list(itertools.product(range(-m, m + 1), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    rows = []
    for s in sites:
        r = {idx[s]: F(1)}
        for a in range(3):
            for sg in (1, -1):
                t = list(s); t[a] += sg; t = tuple(t)
                if t in idx:
                    r[idx[t]] = r.get(idx[t], 0) - F(1, 6)
        rows.append(r)
    A0 = [dict(r) for r in rows]
    b = [F(1) if s == src else F(0) for s in sites]
    for c in range(N):          # symmetric positive definite band: no pivoting
        piv, rc, bc = rows[c][c], rows[c], b[c]
        for rr in range(c + 1, N):
            if c not in rows[rr]:
                continue
            f = rows[rr][c] / piv
            del rows[rr][c]
            for j, v in rc.items():
                if j > c:
                    rows[rr][j] = rows[rr].get(j, 0) - f * v
            b[rr] -= f * bc
    x = [F(0)] * N
    for c in range(N - 1, -1, -1):
        acc = b[c]
        for j, v in rows[c].items():
            if j > c:
                acc -= v * x[j]
        x[c] = acc / rows[c][c]
    exact = all(sum(v * x[j] for j, v in A0[i].items()) == (1 if sites[i] == src else 0)
                for i in range(N))
    return {s: x[idx[s]] for s in sites}, exact


gL9, ex9 = exact_field(9, (0, -2, 0))


def g9(S, s):  # S in 'LR'; R is the mirror y -> -y
    t = s if S == 'L' else (s[0], -s[1], s[2])
    return gL9.get(t, F(0))


def kappa116(S):
    return sum((g9(S, (x, 0, 0)) - g9(S, (x, -2, 0))) / 2 for x in range(-3, 4))


kL, kR = kappa116('L'), kappa116('R')
ok116 = (ex9 and abs(kL - F(-967409, 10 ** 6)) < F(1, 10 ** 6) and abs(kR - F(201858, 10 ** 6)) < F(1, 10 ** 6)
         and abs((kL + kR) / 2 - F(-382775, 10 ** 6)) < F(1, 10 ** 6)
         and abs(kL / 3 + 2 * kR / 3 - F(-187897, 10 ** 6)) < F(1, 10 ** 6))
check("X1", ok116, f"box 9, exact rational (1-A)g = delta_L solved and its residual verified exactly; block 116 "
      f"T4(c) reproduced: kappa(g_L) = {float(kL):.9f}, kappa(g_R) = {float(kR):.9f}, "
      f"means {float((kL + kR) / 2):.9f} (p_L=1/2), {float(kL / 3 + 2 * kR / 3):.9f} (p_L=1/3); its mean kick "
      f"vanishes at p_L = {float(kR / (kR - kL)):.4f}")

# ------------------------------------------------------------------ the walk (floating point)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def walk_H(n):
    """block 54's walk H = sum_a sigma_a D_a, D_a = (i/2)(T_a - T_a^dag), (T_a psi)(x) = psi(x - e_a),
    on the full box of side n, hops leaving the box dropped."""
    I = sps.identity(n, format='csr')
    S1 = sps.diags([np.ones(n - 1)], [-1], shape=(n, n), format='csr')
    H = None
    for a in range(3):
        mats = [I, I, I]; mats[a] = S1
        T = sps.kron(sps.kron(mats[0], mats[1]), mats[2], format='csr')
        term = sps.kron(0.5j * (T - T.getH()), sps.csr_matrix(SIG[a]), format='csr')
        H = term if H is None else H + term
    return H.tocsr()


def float_field(n, S):
    h = (n - 1) // 2
    m = h - 1
    ni = 2 * m + 1
    L1 = sps.diags([np.ones(ni - 1), np.ones(ni - 1)], [-1, 1], shape=(ni, ni))
    Ii = sps.identity(ni)
    As = (sps.kron(sps.kron(L1, Ii), Ii) + sps.kron(sps.kron(Ii, L1), Ii) + sps.kron(sps.kron(Ii, Ii), L1))
    Mf = (sps.identity(ni ** 3) - As / 6).tocsr()
    b = np.zeros(ni ** 3)
    b[((S[0] + m) * ni + (S[1] + m)) * ni + (S[2] + m)] = 1.0
    x, _ = cg(Mf, b, rtol=1e-14, atol=0, maxiter=50000)
    res = float(np.linalg.norm(Mf @ x - b))
    full = np.zeros((n, n, n))
    full[1:-1, 1:-1, 1:-1] = x.reshape(ni, ni, ni)
    return full, res


def packet(n, s, xc):
    """positive-band packet: amplitude exp(-s^2|k-k0|^2) P_+(k) u0 on a 64^3 torus, k0 = (pi/4,0,0),
    u0 = (1,1)/sqrt2, centred at xc, restricted to the box."""
    M = 64
    kk = 2 * np.pi * np.fft.fftfreq(M)
    KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing='ij')
    k0 = np.pi / 4
    pd = lambda a, b: (a - b + np.pi) % (2 * np.pi) - np.pi
    A = np.exp(-s * s * (pd(KX, k0) ** 2 + KY ** 2 + KZ ** 2))
    hx, hy, hz = np.sin(KX), np.sin(KY), np.sin(KZ)
    eps = np.sqrt(hx ** 2 + hy ** 2 + hz ** 2) + 1e-300
    u = np.array([1, 1]) / np.sqrt(2)
    c0 = A * (u[0] + (hz * u[0] + (hx - 1j * hy) * u[1]) / eps) / 2
    c1 = A * (u[1] + ((hx + 1j * hy) * u[0] - hz * u[1]) / eps) / 2
    p0 = np.fft.fftshift(np.fft.ifftn(c0)); p1 = np.fft.fftshift(np.fft.ifftn(c1))
    h = (n - 1) // 2
    co = np.arange(-h, h + 1)
    chi = np.zeros((n, n, n, 2), complex)
    gi = co - xc[0] + M // 2; gj = co - xc[1] + M // 2; gk = co - xc[2] + M // 2
    ok = lambda g: (g >= 0) & (g < M)
    I, J, K = np.meshgrid(np.where(ok(gi))[0], np.where(ok(gj))[0], np.where(ok(gk))[0], indexing='ij')
    ph = np.exp(1j * k0 * xc[0])
    chi[I, J, K, 0] = p0[gi[I], gj[J], gk[K]] * ph
    chi[I, J, K, 1] = p1[gi[I], gj[J], gk[K]] * ph
    v = chi.reshape(-1)
    return v / np.linalg.norm(v)


def coords(n):
    h = (n - 1) // 2
    co = np.arange(-h, h + 1)
    Xg, Yg, Zg = np.meshgrid(co, co, co, indexing='ij')
    return [np.repeat(G.reshape(-1).astype(float), 2) for G in (Xg, Yg, Zg)]


def Vop(H, g):
    P = sps.diags(np.repeat(g.reshape(-1), 2))
    return -(P @ H + H @ P)      # phi H phi = H - kE_B (gH + Hg) + O(k^2)


def aug(H, V, chi0, tf):
    z = expm_multiply(-1j * tf * sps.bmat([[H, None], [V, H]], format='csr'),
                      np.concatenate([chi0, np.zeros_like(chi0)]))
    return z[:len(chi0)], z[len(chi0):]


def ex(v, O, w=None):
    return float(np.real(np.vdot(v, O * (v if w is None else w))))


# W1: Hermitian and the symbol, on box 9
H9 = walk_H(9)
X9, Y9, Z9 = coords(9)
kt = np.array([0.3, -0.7, 1.1])
pw = np.exp(1j * (kt[0] * X9 + kt[1] * Y9 + kt[2] * Z9)) * np.tile([0.6, 0.8j], 9 ** 3)
hk = sum(np.sin(kt[a]) * SIG[a] for a in range(3))
Hpw = (H9 @ pw).reshape(-1, 2)
inner = [i for i in range(9 ** 3) if max(abs(X9[2 * i]), abs(Y9[2 * i]), abs(Z9[2 * i])) < 4]
sym_err = max(np.abs(Hpw[i] - hk @ pw.reshape(-1, 2)[i]).max() for i in inner)
check("W1", abs(H9 - H9.getH()).max() == 0 and sym_err < 1e-13,
      f"walk on the box: H = H^dag exactly; on a plane wave at interior sites H acts as sum sin k_a sigma_a "
      f"(max error {sym_err:.1e})")

# W2: block 116's own box: no clean passage
g9L = np.zeros((9, 9, 9)); g9R = np.zeros((9, 9, 9))
for s in itertools.product(range(-3, 4), repeat=3):
    g9L[s[0] + 4, s[1] + 4, s[2] + 4] = float(g9('L', s)); g9R[s[0] + 4, s[1] + 4, s[2] + 4] = float(g9('R', s))
c9 = packet(9, 1.0, (-3, -1, 0))
tf9 = 6 / np.cos(np.pi / 4)
E, U = np.linalg.eigh(H9.toarray())
cc = U.conj().T @ c9
Ea, Eb = E[:, None], E[None, :]
with np.errstate(divide='ignore', invalid='ignore'):
    fac = (np.exp(-1j * Ea * tf9) - np.exp(-1j * Eb * tf9)) / (Ea - Eb)
fac = np.where(np.abs(Ea - Eb) < 1e-10, -1j * tf9 * np.exp(-1j * Eb * tf9), fac)
out9 = {}
for S, g in (('L', g9L), ('R', g9R)):
    V = Vop(H9, g)
    ch, et = aug(H9, V, c9, tf9)
    d_aug = 2 * ex(ch, Y9, et)
    eta_e = U @ (((U.conj().T @ V.toarray() @ U) * fac) @ cc)
    chi_e = U @ (np.exp(-1j * E * tf9) * cc)
    out9[S] = (d_aug, 2 * ex(chi_e, Y9, eta_e))
mY9 = ex(ch, Y9); sY9 = np.sqrt(ex(ch, Y9 * Y9) - mY9 ** 2); mX9 = ex(ch, X9)
check("W2", all(abs(a - b) < 1e-10 for a, b in out9.values()) and sY9 > 2 and mX9 < 1.5,
      f"box 9 (block 116's box), packet s=1 from (-3,-1,0), t_f = 6/cos(pi/4): first-order dY per k E_B "
      f"L {out9['L'][0]:.6f}, R {out9['R'][0]:.6f} (augmented = eigendecomposition to 1e-10); at t_f <X> = "
      f"{mX9:.2f}, sigma_Y = {sY9:.2f} of half-width 4: the walk fills the box, no clean passage")


# W3, W4: large held boxes, clean passage


def run_box(n, fd):
    h = (n - 1) // 2
    H = walk_H(n)
    X, Y, Z = coords(n)
    gL, rL = float_field(n, (0, -2, 0))
    gR, rR = float_field(n, (0, 2, 0))
    chi0 = packet(n, 2.5, (-10, -1, 0))
    tf = 20 / np.cos(np.pi / 4)
    out = {'res': max(rL, rR)}
    for S, g in (('L', gL), ('R', gR)):
        V = Vop(H, g)
        ch, et = aug(H, V, chi0, tf)
        out[S] = 2 * ex(ch, Y, et)
        out['dX' + S] = 2 * ex(ch, X, et)
        out['rho' + S] = (2 * np.real(np.conj(ch) * et)).reshape(n, n, n, 2).sum(axis=(0, 2, 3))
        if fd:
            e = 1e-6
            zp = expm_multiply(-1j * tf * (H + e * V), chi0)
            zm = expm_multiply(-1j * tf * (H - e * V), chi0)
            out['fd' + S] = (ex(zp, Y) - ex(zm, Y)) / (2 * e)
    Vm = Vop(H, gL / 3 + 2 * gR / 3)
    chm, etm = aug(H, Vm, chi0, tf)
    out['lin'] = 2 * ex(chm, Y, etm) - (out['L'] / 3 + 2 * out['R'] / 3)
    out['P0'] = (np.abs(ch) ** 2).reshape(n, n, n, 2).sum(axis=(0, 2, 3))
    out['mY'] = ex(ch, Y); out['sY'] = np.sqrt(ex(ch, Y * Y) - out['mY'] ** 2); out['mX'] = ex(ch, X)
    w = (np.abs(ch) ** 2).reshape(n, n, n, 2).sum(axis=3)
    co = np.arange(-h, h + 1)
    near = (np.abs(co) >= h - 3)
    out['wall'] = float(w[near, :, :].sum() + w[:, near, :].sum() + w[:, :, near].sum())
    out['kap116'] = (sum((gL[h + x, h, h] - gL[h + x, h - 2, h]) / 2 for x in range(-3, 4)),
                     sum((gR[h + x, h, h] - gR[h + x, h - 2, h]) / 2 for x in range(-3, 4)))
    return out


b61 = run_box(61, True)
okW3 = (b61['res'] < 1e-12 and b61['wall'] < 1e-3
        and all(abs(b61['fd' + S] - b61[S]) < 1e-7 * max(1, abs(b61[S])) for S in 'LR')
        and abs(b61['lin']) < 1e-10 and 7 < b61['mX'] < 9)
check("W3", okW3, f"held box 61, packet s=2.5 from (-10,-1,0), k0=(pi/4,0,0), t_f = 20/cos(pi/4): first-order dY "
      f"per k E_B: L {b61['L']:.6f}, R {b61['R']:.6f} (augmented = finite difference to 1e-7); "
      f"dX (delay) L {b61['dXL']:.3f}, R {b61['dXR']:.3f}; <X> = {b61['mX']:.2f}, sigma_Y = {b61['sY']:.3f}, "
      f"weight within 3 of a wall {b61['wall']:.1e}; field CG residual {b61['res']:.0e}; linear in the field")
b41 = run_box(41, False)
rel = max(abs(b41[S] / b61[S] - 1) for S in 'LR')
check("W4", rel < 0.05 and b41['wall'] > 10 * b61['wall'],
      f"same packet in held box 41: L {b41['L']:.6f}, R {b41['R']:.6f} ({100 * rel:.1f}% from box 61; "
      f"weight near walls {b41['wall']:.3f}). Block 116's gradient kappa in box 61: "
      f"{b61['kap116'][0]:.4f}, {b61['kap116'][1]:.4f}; the walk's kick is a different functional")

# R1: exit record with weight |chi|^2 at t_f; distributions of the recorded y
P0, rL, rR = b61['P0'], b61['rhoL'], b61['rhoR']
msk = P0 > 1e-12
JLL = float((rL[msk] ** 2 / P0[msk]).sum())
JRR = float((rR[msk] ** 2 / P0[msk]).sum())
JLR = float((rL[msk] * rR[msk] / P0[msk]).sum())
det = JLL * JRR - JLR ** 2
yy = np.arange(-30, 31)
okM = (abs(P0.sum() - 1) < 1e-12 and abs(rL.sum()) < 1e-12 and abs(rR.sum()) < 1e-12
       and abs((yy * rL).sum() - b61['L']) < 1e-10 and abs((yy * rR).sum() - b61['R']) < 1e-10)
pstar = b61['R'] / (b61['R'] - b61['L'])


def Jpair(a, b):  # a, b coefficient pairs (cL, cR) of rho = cL rho_L + cR rho_R
    d = (a[0] - b[0], a[1] - b[1])
    return d[0] ** 2 * JLL + 2 * d[0] * d[1] * JLR + d[1] ** 2 * JRR


eps_err = 0.01
lines = []
for pl in (F(1, 2), F(1, 3)):
    p = float(pl)
    H4 = {'L': (1, 0), 'R': (0, 1), 'mean': (p, 1 - p), '0': (0, 0)}
    worst = min(Jpair(H4[a], H4[b]) for a, b in itertools.combinations(H4, 2))
    j0m = Jpair(H4['0'], H4['mean'])
    lines.append(f"p_L={pl}: J(0,mean)={j0m:.4f} -> N (k E_B)^2 in [{4 * np.log(1 / (4 * eps_err * (1 - eps_err))) / j0m:.0f}, "
                 f"{8 * np.log(1 / (2 * eps_err)) / j0m:.0f}]; hardest pair J={worst:.4f}")
kE = 1e-3
PL, PR = np.clip(P0 + kE * rL, 0, None), np.clip(P0 + kE * rR, 0, None)
BC = float(np.sqrt(PL * PR).sum())
okR1 = okM and det > 0 and JLL > 0 and abs(-np.log(BC) / (kE ** 2 * (JLL + JRR - 2 * JLR) / 8) - 1) < 1e-2
check("R1", okR1, f"rule R1 (one record at t_f, weights |chi|^2): recorded y ~ P0 + k E_B rho_v; sum y rho_v = dY_v; "
      f"Gram [[{JLL:.4f},{JLR:.4f}],[{JLR:.4f},{JRR:.4f}]] of the rho's against 1/P0 has det {det:.4f} > 0, so all "
      f"six pairs of readings separate at every p_L; the mean kick alone is blind at p_L* = {pstar:.4f}; "
      f"Bhattacharyya -ln BC = (k E_B)^2 J/8 (checked at k E_B = 1e-3)")
dm = 0.5 * b61['L'] + 0.5 * b61['R']
lines.append(f"sample mean only, 0 vs mean at p_L=1/2: N (k E_B)^2 = (2 z sigma_Y/|mean kick|)^2 = "
             f"{(2 * 2.326 * b61['sY'] / abs(dm)) ** 2:.0f} at z = 2.326")
for ln in lines:
    print("    " + ln)
mY, mX = b61['mY'], b61['mX']
mY_marg = min(abs(mY - (np.floor(mY) + 0.5)), abs(mY - (np.ceil(mY) - 0.5)))
mX_marg = min(abs(mX - (np.floor(mX) + 0.5)), abs(mX - (np.ceil(mX) - 0.5)))
kmax = min(mY_marg / max(abs(b61['L']), abs(b61['R'])), mX_marg / max(abs(b61['dXL']), abs(b61['dXR'])))
check("R2", 0.1 < kmax < 0.3,
      f"rule R2 (one record at the site nearest the mean position): the recorded site is ({round(mX)},{round(mY)},0) "
      f"for all four fields whenever k E_B < {kmax:.3f}; margins {mX_marg:.3f} (x), {mY_marg:.3f} (y)")

npass = sum(ok for _, ok in RES)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass}  ({time.time() - T0:.0f} s)")
if npass == len(RES):
    print(f"SUMMARY: PARTIAL block 116's two-place test with block 54's walk as test body (phi H phi, first order "
          f"in k, controlled floating point, two methods each): held box 61 gives dY_L = {b61['L']:.4f}, "
          f"dY_R = {b61['R']:.4f} per k E_B (mean and 0 by linearity) against sigma_Y = {b61['sY']:.2f}; an exit "
          f"record weighted by |chi|^2 separates all four readings at every p_L in N ~ (13-31)/(J (k E_B)^2) passages; "
          f"the mean alone is blind at p_L* = {pstar:.3f}; block 116's box 9 has no clean passage.")
    print(f"HIT: block 54's walk as test body (i dchi/dt = phi H phi chi, first order in k) in a held box of side 61 "
          f"(packet s = 2.5, k0 = (pi/4,0,0), from x = -10, read at t = 20 sqrt2) takes transverse kicks "
          f"{b61['L']:.4f} (L), {b61['R']:.4f} (R), p_L dY_L + p_R dY_R (amplitude sourcing) and 0 (records only) per "
          f"k E_B, with spread {b61['sY']:.2f}; one exit record with weights |chi|^2 separates every pair at every p_L "
          f"after N ~ (13-31)/(J (k E_B)^2) passages (J(0,mean) = {Jpair((0, 0), (0.5, 0.5)):.3f} at p_L = 1/2); the "
          f"sample mean is blind at p_L* = {pstar:.3f}; a record at the centre site separates nothing for "
          f"k E_B < {kmax:.2f}.")
else:
    print("SUMMARY: ROUTE FAILS AT a failed check above")
