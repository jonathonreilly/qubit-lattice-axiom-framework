"""C5 s3: W3 of strictly finite-range walks (Laurent polynomial unitaries).

Theorem K (NOTE.md) predicts W3 = 0 for every one of them. Two computational paths per instance:
 (a) exact-grid certificate: integrand is a trig polynomial of degree <= 6r per axis (Lemma Q; its
     Fourier support is checked directly on two instances), so the N >= 6r+1 grid sum IS the integral;
     |sum| < 1e-9 then forces the integer W3 to be 0;
 (b) for SU(2)-valued walks: signed preimage count of random regular values (Newton from a seed grid),
     a path that does not integrate the form at all; calibrated on the analytic control V_2 (W3 = -1).
"""
import itertools
import sys
import numpy as np
from w3lib import (Checker, PAULI, lp_mul, lp_const, lp_cond_shift, lp_range, lp_eval_grid, w3_from_fields,
                   w3_laurent, unitarity_error, haar, rand_projector)

ck = Checker()
rng = np.random.default_rng(20261018)
VEC = [v for v in itertools.product((-1, 0, 1), repeat=3) if any(v)]

def rand_shift_coin(d, L, rng, su2=False):
    C0 = haar(d, rng)
    if su2:
        C0 = C0 / np.sqrt(np.linalg.det(C0))
    A = lp_const(C0)
    for _ in range(L):
        a = VEC[rng.integers(len(VEC))]
        if su2:   # e^{i (k.a) n.sigma} = P e^{ik.a} + (1-P) e^{-ik.a}
            Pm = rand_projector(2, 1, rng)
            S = {tuple(a): Pm.astype(complex), tuple(-x for x in a): (np.eye(2) - Pm).astype(complex)}
        else:
            S = lp_cond_shift(rand_projector(d, rng.integers(1, d), rng), a)
        C = haar(d, rng)
        if su2:
            C = C / np.sqrt(np.linalg.det(C))
        A = lp_mul(lp_mul(A, S), lp_const(C))
    return A

def det_monomial(A, N=7):
    U, _ = lp_eval_grid(A, N)
    k = 2 * np.pi * np.arange(N) / N
    dets = np.linalg.det(U)
    # fit det = c exp(i m.k): FFT and find single nonzero coefficient
    Fh = np.fft.fftn(dets) / N ** 3
    idx = np.unravel_index(np.argmax(np.abs(Fh)), Fh.shape)
    m = tuple(int(i) if i <= N // 2 else int(i) - N for i in idx)
    return m, abs(abs(Fh[idx]) - 1)

walks = []
for t in range(4):
    walks.append((f'n=2 shift-coin product L=4 #{t}', rand_shift_coin(2, 4, rng)))
for t in range(3):
    walks.append((f'n=2 SU(2) symmetric-shift product L=3 #{t}', rand_shift_coin(2, 3, rng, su2=True)))
for t in range(3):
    walks.append((f'n=3 shift-coin product L=4 #{t}', rand_shift_coin(3, 4, rng)))
for t in range(4):
    walks.append((f'n=4 shift-coin product L=5 #{t}', rand_shift_coin(4, 5, rng)))

# Clifford-type non-shift-coin presentation: x = (cos th * q, sin th * (cos k.n, sin k.n)) in S^5
s = PAULI
G5 = [np.kron(s[1], s[0]), np.kron(s[2], s[0]), np.kron(s[3], s[1]), np.kron(s[3], s[2]), np.kron(s[3], s[3])]
def clifford_from_quaternion(qA, th, nvec):
    # qA: SU(2) Laurent walk = f + i g.sigma ; components as Laurent dicts of scalars
    out = {}
    for n, M in qA.items():
        f = (M[0, 0] + M[1, 1]) / 2
        g = [np.trace(M @ s[a + 1]) / 2j for a in range(3)]
        out[n] = out.get(n, 0) + np.cos(th) * (f * np.eye(4) + 1j * sum(g[a] * G5[2 + a] for a in range(3)))
    nv = tuple(nvec); mv = tuple(-x for x in nvec)
    # sin th (cos(k.n) i Gamma_1 + sin(k.n) i Gamma_2)
    out[nv] = out.get(nv, 0) + np.sin(th) * 1j * (G5[0] / 2 + G5[1] / 2j)
    out[mv] = out.get(mv, 0) + np.sin(th) * 1j * (G5[0] / 2 - G5[1] / 2j)
    return out
for t in range(2):
    q = rand_shift_coin(2, 3, rng, su2=True)
    walks.append((f'n=4 Clifford map S^5 with quaternion part #{t}', clifford_from_quaternion(q, 0.7 + 0.3 * t, (1, 1, 0))))

# covariant one-qubit walks from the cubic-freeze note
def qshift(a):
    e = [0, 0, 0]; e[a] = 1
    P = (np.eye(2) + s[a + 1]) / 2
    return {tuple(e): P.astype(complex), tuple(-x for x in e): (np.eye(2) - P).astype(complex)}
D2 = lp_mul(lp_mul(qshift(0), qshift(1)), qshift(2))
nb = np.ones(3) / np.sqrt(3)
Pb = (np.eye(2) + sum(nb[a] * s[a + 1] for a in range(3))) / 2
D3 = {(1, 1, 1): Pb.astype(complex), (-1, -1, -1): (np.eye(2) - Pb).astype(complex)}
D4 = qshift(2)
walks += [('D2-covariant product walk q_x q_y q_z (Weyl cone at 0)', D2),
          ('D3-covariant body-diagonal shift', D3), ('D4-covariant axial shift', D4)]

print(f'{"walk":58s} {"n":>2s} {"r":>2s} {"N":>3s} {"unit.err":>9s} {"det monomial":>14s} {"W3 (grid)":>22s}')
allzero = True
for name, A in walks:
    d = next(iter(A.values())).shape[0]
    r = lp_range(A)
    ue = unitarity_error(A)
    m, me = det_monomial(A, N=4 * r + 3)
    w, N = w3_laurent(A)
    w2, N2 = w3_laurent(A, N=6 * r + 5)
    print(f'{name:58s} {d:2d} {r:2d} {N:3d} {ue:9.1e} {str(m):>14s} {w.real:+.2e}{w.imag:+.1e}i  (N={N2}: {abs(w2):.1e})')
    ok = ue < 1e-10 and me < 1e-10 and abs(w) < 1e-9 and abs(w2) < 1e-9
    allzero &= ok
    ck.check(f'{name}: unitary, det is a unit monomial, exact-grid W3 = 0', ok)

# ---- Lemma Q check: Fourier support of the integrand has degree <= 6r per axis ----
def integrand_fourier_degree(A, N):
    U, dU = lp_eval_grid(A, N)
    Ui = np.conj(np.swapaxes(U, -1, -2))
    Aa = [Ui @ x for x in dU]
    t = np.trace(Aa[0] @ Aa[1] @ Aa[2], axis1=-2, axis2=-1) - np.trace(Aa[0] @ Aa[2] @ Aa[1], axis1=-2, axis2=-1)
    Fh = np.fft.fftn(t) / N ** 3
    freqs = np.fft.fftfreq(N, 1 / N).astype(int)
    big = np.argwhere(np.abs(Fh) > 1e-12 * np.abs(Fh).max())
    return max(max(abs(freqs[i]) for i in b) for b in big)
for name, A in [walks[0], walks[-3]]:
    r = lp_range(A)
    deg = integrand_fourier_degree(A, 12 * r + 4)
    ck.check(f'Lemma Q on "{name}": integrand Fourier degree {deg} <= 6r = {6 * r} (sampled on N = {12 * r + 4} grid)', deg <= 6 * r)

# ---- path (b): signed preimage counting for SU(2)-valued maps ----
def su2_parts(func):
    def fg(k):
        U, dU = func(k)
        f = np.real(np.trace(U)) / 2
        g = np.array([np.real(np.trace(U @ s[a + 1]) / 2j) for a in range(3)])
        Dg = np.array([[np.real(np.trace(dU[b] @ s[a + 1]) / 2j) for b in range(3)] for a in range(3)])
        return f, g, Dg
    return fg

def laurent_point(A):
    def func(k):
        U = sum(M * np.exp(1j * np.dot(n, k)) for n, M in A.items())
        dU = [sum(1j * n[b] * M * np.exp(1j * np.dot(n, k)) for n, M in A.items()) for b in range(3)]
        return U, dU
    return func

def V2_point(k):
    M = 2.0
    f = M - np.cos(k).sum(); g = np.sin(k)
    W = f * s[0] + 1j * sum(g[a] * s[a + 1] for a in range(3)); nr = np.sqrt(f * f + g @ g)
    dU = []
    for b in range(3):
        dW = np.sin(k[b]) * s[0] + 1j * np.cos(k[b]) * s[b + 1]
        dn = (f * np.sin(k[b]) + g[b] * np.cos(k[b])) / nr
        dU.append(dW / nr - W * dn / nr ** 2)
    return W / nr, dU

def preimage_degree(fg, y, seeds=14):
    grid = 2 * np.pi * (np.arange(seeds) + 0.5) / seeds
    sols = []
    for k0 in itertools.product(grid, grid, grid):
        k = np.array(k0)
        for _ in range(40):
            f, g, Dg = fg(k)
            res = g - y[1:]
            if np.abs(res).max() < 1e-13:
                break
            try:
                k = k - np.linalg.solve(Dg, res)
            except np.linalg.LinAlgError:
                break
        f, g, Dg = fg(k)
        if np.abs(g - y[1:]).max() < 1e-11 and np.sign(f) == np.sign(y[0]):
            kk = np.mod(k, 2 * np.pi)
            if not any(np.abs(np.angle(np.exp(1j * (kk - q)))).max() < 1e-7 for q, _ in sols):
                sols.append((kk, np.sign(f) * np.sign(np.linalg.det(Dg))))
    return sols

ys = []
for _ in range(3):
    v = rng.normal(size=4); ys.append(v / np.linalg.norm(v))
cal = [sum(e for _, e in preimage_degree(su2_parts(V2_point), y)) for y in ys]
print('control V_2: signed preimage sums for 3 random regular values:', cal)
ck.check('path (b) calibration: V_2 gives the same nonzero signed count for 3 random regular values', len(set(cal)) == 1 and cal[0] != 0)
eps = -1 / cal[0]   # orientation constant so that eps * count = W3 = -1 for V_2
su2_list = [(n, A) for n, A in walks if 'SU(2)' in n or 'D2' in n]
for name, A in su2_list:
    counts = []
    npre = []
    for y in ys:
        sol = preimage_degree(su2_parts(laurent_point(A)), y)
        counts.append(eps * sum(e for _, e in sol)); npre.append(len(sol))
    print(f'{name}: preimage counts {npre}, signed degrees {counts}')
    ck.check(f'path (b) {name}: signed preimage degree 0 for 3 random values (preimages found: {npre})', all(abs(c) < 1e-12 for c in counts))
ck.check('all finite-range walks in the battery have W3 = 0', allzero)
sys.exit(ck.total())
