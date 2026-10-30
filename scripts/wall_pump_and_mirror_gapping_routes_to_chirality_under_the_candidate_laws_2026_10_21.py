#!/usr/bin/env python3
"""Chirality escapes for the CL-2 tick: (a) a fifth coordinate, (b) Floquet 0/pi pumping, (c) mirror gapping via CL-5.
A  rung index as a fifth coordinate: folding keeps W3; the multiresolution rung is locked to momentum; an internal index
   carried in parallel is nearest-neighbour admissible; a synthetic Wilson-Dirac wall built from the tick's own light
   algebra binds one chirality (or one copy) at each end; wall-content anomalies; mirror reflection of the wall.
B  Floquet: index of a product of two reflections; the step-pi/2 tick W_o W_e has none in any site-phase background;
   the 2D overlap gets one only through tr sign(H_W), which needs a non-ultralocal sign function.
C  CL-5: total mode number N is exact; mixed anomalies N-Y^2, N-SU(2)^2 of one family; mirror reflection M = R_odd I.
D  estimates against measurement.  Supplied models, finite diagnostics; no physical identification."""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/WALL_PUMP_AND_MIRROR_GAPPING_ROUTES_TO_CHIRALITY_UNDER_THE_CANDIDATE_LAWS_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from fractions import Fraction as Fr
import numpy as np
from scipy.linalg import expm, schur

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
rng = np.random.default_rng(20261021)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex); I2 = np.eye(2)

# ------------------------------------------------ the CL-2 block: spin-3/2 edge hop W on the 8 corners, Bloch tick
C = np.array(list(itertools.product((0, 1), repeat=3))); cc0 = C - 0.5
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: g = XI[a].conj() @ XI[b]; W[a, b] = -g / abs(g) / np.sqrt(3)
I8 = np.eye(8); S = np.diag([(-1.0) ** int(x.sum()) for x in C])          # s = sublattice (tetrahedron) sign
def Wm(a): return np.cos(a) * W + 1j * np.sin(a) * I8                      # = i exp(-i(pi/2 - a) W)
def U3(Q, mu=0.0, b=0.0):
    D = np.diag(np.exp(1j * C @ Q)); return D @ Wm(mu / 2 - b) @ D.conj().T @ Wm(mu / 2 + b)
def algebra(b):
    h = 1e-6; A = []
    for a in range(3):
        e = np.zeros(3); e[a] = h; A.append(1j * (U3(e, 0, b) - U3(-e, 0, b)) / (2 * h))
    A = [(x + x.conj().T) / 2 for x in A]; c = np.sqrt(np.trace(A[0] @ A[0]).real / 8)
    Bm = -1j * (U3(np.zeros(3), h, b) - U3(np.zeros(3), -h, b)) / (2 * h); Bm = (Bm + Bm.conj().T) / 2
    g5 = -1j * A[0] @ A[1] @ A[2] / c ** 3; return A, c, Bm / np.sqrt(np.trace(Bm @ Bm).real / 8), (g5 + g5.conj().T) / 2
def commutant(gens, n=8):
    M = np.vstack([np.kron(g, np.eye(n)) - np.kron(np.eye(n), g.T) for g in gens]); _, sv, Vh = np.linalg.svd(M)
    sv = np.concatenate([sv, np.zeros(n * n - len(sv))]); return [v.conj().reshape(n, n) for v, x in zip(Vh, sv) if x < 1e-7]
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): rots.append(R)
def axang(R):
    a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(a)), a
def img(R, i): return int(np.argmin(np.sum(abs(cc0 - R @ cc0[i]), 1)))
def Grot(R):
    n_, a = axang(R); Dm = expm(-1j * a * sum(n_[k] * J3[k] for k in range(3))); G = np.zeros((8, 8), complex)
    for i in range(8): k = img(R, i); G[k, i] = XI[k].conj() @ Dm @ XI[i]
    return G
Pi = np.zeros((8, 8))
for i in range(8): Pi[img(-np.eye(3), i), i] = 1
ph = {0: 1.0 + 0j}                                                          # inversion phases: P W P^+ = W
while len(ph) < 8:
    for a in list(ph):
        for b in range(8):
            if b not in ph and abs(W[a, b]) > 0:
                ia, ib = int(np.argmax(Pi[:, a])), int(np.argmax(Pi[:, b])); ph[b] = np.conj(W[ia, ib] / (ph[a] * W[a, b]))
Pinv = Pi @ np.diag([ph[i] for i in range(8)])
def schur_eig(U):
    T, Z = schur(U, output='complex'); return -np.angle(np.diag(T)), Z
def Hsyn(Ls, bp, G4, m0=1.0, r=1.0, d=8):                                 # Wilson-Dirac chain on the internal index
    X = (r * bp + 1j * G4) / 2; H = np.zeros((d * Ls, d * Ls), complex)
    for j in range(Ls - 1):
        H[d * (j + 1):d * (j + 2), d * j:d * (j + 1)] += X; H[d * j:d * (j + 1), d * (j + 1):d * (j + 2)] += X.conj().T
    for j in range(Ls): H[d * j:d * (j + 1), d * j:d * (j + 1)] += (m0 - r) * bp
    return H
def flux(fun, r=0.03, nt=12, nph=24):
    th = np.linspace(0, np.pi, nt + 1); pp = np.linspace(0, 2 * np.pi, nph + 1)[:-1]; V = {}; dims = set()
    for i, t in enumerate(th):
        for k, p in enumerate(pp):
            V[i, k] = fun(r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])); dims.add(V[i, k].shape[1])
    F = 0
    for i in range(nt):
        for k in range(nph):
            a, b2, c2, d2 = V[i, k], V[i + 1, k], V[i + 1, (k + 1) % nph], V[i, (k + 1) % nph]
            F += np.angle(np.linalg.det(a.conj().T @ b2) * np.linalg.det(b2.conj().T @ c2) * np.linalg.det(c2.conj().T @ d2) * np.linalg.det(d2.conj().T @ a))
    return F / (2 * np.pi), dims
def wall_upper(U, Ls, wmax, end, B=None):
    w, V = schur_eig(U); sel = (w > 0) & (w < wmax); Vu = V[:, sel] if B is None else B @ V[:, sel]
    pj = np.zeros(8 * Ls); pj[(8 * end) % (8 * Ls):(8 * end) % (8 * Ls) + 8] = 1
    e, E = np.linalg.eigh(Vu.conj().T @ (pj[:, None] * Vu)); return Vu @ E[:, e > 0.5]

print('== A. rung index as a fifth coordinate')
def w3(Ufun, N):                                                            # spectral-derivative 3D winding
    g = 2 * np.pi * np.arange(N) / N - np.pi; K = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    U0 = Ufun(K); U = U0.reshape(N, N, N, *U0.shape[1:]); kk = np.fft.fftfreq(N, d=1.0 / N)
    def d(ax):
        F = np.fft.fft(U, axis=ax); sh = [1] * 5; sh[ax] = N; F = F * (1j * kk).reshape(sh)
        idx = [slice(None)] * 5; idx[ax] = N // 2; F[tuple(idx)] = 0; return np.fft.ifft(F, axis=ax)
    Ud = U.conj().swapaxes(-1, -2); Ax, Ay, Az = [Ud @ d(a) for a in range(3)]
    return (np.trace(Ax @ (Ay @ Az - Az @ Ay), axis1=-2, axis2=-1).sum() * (2 * np.pi / N) ** 3 / (8 * np.pi ** 2)).real
def qwalk(K, m=-2.0):
    n0 = m + np.cos(K).sum(-1); n_ = np.sin(K); nn = np.sqrt(n0 ** 2 + (n_ ** 2).sum(-1))
    return (n0[:, None, None] * I2 - 1j * (n_[:, 0, None, None] * sx + n_[:, 1, None, None] * sy + n_[:, 2, None, None] * sz)) / nn[:, None, None]
def folded(Q):
    out = np.zeros((len(Q), 16, 16), complex)
    for n_ in C:
        kn = (Q + 2 * np.pi * n_) / 2; F = np.exp(1j * kn @ C.T) / np.sqrt(8)
        out += np.einsum('qr,qs,qab->qrasb', F, F.conj(), qwalk(kn)).reshape(len(Q), 16, 16)
    return out
wa, wf = w3(qwalk, 16), w3(folded, 10); wt = w3(lambda K: np.array([U3(q, 0.1, 1.27) for q in K]), 10)
check('A1 zoom keeps W3: a quasi-local W3=-1 walk folded to the next rung (16 bands) still has W3=-1; finite-depth ticks keep 0', abs(wa + 1) < 1e-4 and abs(wf + 1) < 1e-4 and abs(wt) < 1e-9, f'{wa:+.6f} -> {wf:+.6f}; CL-2 tick {wt:+.1e}')
Nn = 12; x = np.arange(2 ** Nn); err = 0; bound = True; amax = []
for j in (1, 2, 4, 8, 16, 64, 300, 1024, 2047):
    k = 2 * np.pi * j / 2 ** Nn; a = np.exp(1j * k * x) / np.sqrt(2 ** Nn); f = []
    for n_ in range(1, Nn + 1):
        dd = (a[0::2] - a[1::2]) / np.sqrt(2); a = (a[0::2] + a[1::2]) / np.sqrt(2); f.append(np.sum(abs(dd) ** 2))
    f = np.array(f); fp = np.array([np.sin(2.0 ** (n_ - 2) * k) ** 4 / (4.0 ** (n_ - 1) * np.sin(k / 2) ** 2) for n_ in range(1, Nn + 1)])
    err = max(err, abs(f - fp).max(), abs(f.sum() + abs(a[0]) ** 2 - 1)); bound &= all(f[n_ - 1] <= np.pi ** 2 / 4 * 4.0 ** (n_ - 2) * k ** 2 + 1e-15 for n_ in range(1, Nn + 1)); amax.append(float(np.arange(1, Nn + 1) @ f))
check('A2 multiresolution rung is locked to momentum: weight on level n = sin^4(2^(n-2)k)/(4^(n-1)sin^2(k/2)) <= 2.5*4^(n-2)k^2 and moves one level per octave: no rung holds a field down to k=0',
      err < 1e-12 and bound and np.allclose(np.diff(amax[:5]), -1, atol=0.02), f'formula err {err:.0e}; mean level at k=2pi j/4096, j=1,2,4,8,16: ' + ' '.join(f'{v:.3f}' for v in amax[:5]))
dep = []; okn = True
for n_ in (1, 2, 3):
    m = 2 ** n_; target = [y for j in range(m) for y in (j, m + j)]; rk = {lab: i for i, lab in enumerate(target)}; arr = list(range(2 * m)); rounds = []; par = 1
    while [rk[y] for y in arr] != list(range(2 * m)):
        sw = [p for p in range(par, 2 * m - 1, 2) if rk[arr[p]] > rk[arr[p + 1]]]
        for p in sw: arr[p], arr[p + 1] = arr[p + 1], arr[p]
        if sw: rounds.append(sw)
        par ^= 1
    Pm = np.eye(2 * m)
    for sw in rounds:
        T = np.eye(2 * m)
        for p in sw: T[[p, p + 1]] = T[[p + 1, p]]
        Pm = T @ Pm
    mid = np.kron(np.eye(m), sx * 0.6 + sz * 0.8); Odir = np.zeros((2 * m, 2 * m), complex)
    for j in range(m): Odir[np.ix_([j, m + j], [j, m + j])] = sx * 0.6 + sz * 0.8
    okn &= np.abs(Pm.T @ mid @ Pm - Odir).max() < 1e-14; dep.append(2 * len(rounds) + 1)
check('A3 carrying a 2^n-site internal index in parallel to the next cell is a nearest-neighbour swap circuit of depth 2^(n+1)-1 (light cone kept)', okn and dep == [3, 7, 15], f'depths {dep}')
def Wm1(a): return np.cos(a) * sx + 1j * np.sin(a) * I2
def U1(k, b):
    D = np.diag([1, np.exp(1j * k)]); return D @ Wm1(-b) @ D.conj().T @ Wm1(b)
b1 = 1.27; A1 = 1j * (U1(1e-6, b1) - U1(-1e-6, b1)) / 2e-6; A1 = (A1 + A1.conj().T) / 2; c1 = np.sqrt(np.trace(A1 @ A1).real / 2); g51 = A1 / c1
B1 = sx; Ls1 = 8; Ss1 = expm(-1j * 0.6 * Hsyn(Ls1, B1, 1j * B1 @ g51, d=2)); rows = []
for k in (1e-3, 1e-2, 0.1):
    w, V = schur_eig(Ss1 @ np.kron(np.eye(Ls1), U1(k, b1)))
    for i in np.argsort(abs(w))[:2]: rows.append((np.sign(w[i]), w[i] / k / c1, abs(V[0, i]) ** 2 + abs(V[1, i]) ** 2))
near = [r for r in rows if r[2] > .5]; far = [r for r in rows if r[2] <= .5]; zmin = 9.0
for k in np.linspace(1.0, np.pi, 60):
    w, V = schur_eig(Ss1 @ np.kron(np.eye(Ls1), U1(k, b1))); wt = abs(V[0]) ** 2 + abs(V[1]) ** 2
    if (wt > .5).any(): zmin = min(zmin, np.abs(w[wt > .5]).min())
lk = [np.sort(abs(np.linalg.eigvalsh(Hsyn(L_, B1, 1j * B1 @ g51, m0=0.6, d=2))))[0] for L_ in range(6, 12)]
check('A4 1D (step 0.30): each layer is balanced (A = +-c); with the synthetic wall layer 0 holds one right-mover (crossing w=0 only at k=0), the last layer one left-mover, k-independently; leakage x(1-m0) per layer',
      np.allclose(sorted(np.linalg.eigvalsh(A1)), [-c1, c1]) and all(r[0] > 0 and abs(r[1] - 1) < 3e-3 and r[2] > 0.99999 for r in near) and all(r[0] < 0 for r in far)
      and len(near) == 3 and zmin > 0.2 and np.allclose(np.array(lk[1:]) / np.array(lk[:-1]), 0.4, atol=2e-3), f'layer-0 weight >= {min(r[2] for r in near):.6f}, end |w| >= {zmin:.3f} for |k| > 1, ratio {lk[-1] / lk[-2]:.4f}')
res = {}
for bb in (0.0, np.pi / 2 - 0.04):
    A, c, beta, g5 = algebra(bb); cm = commutant(A + [beta])
    res[bb] = (max(abs(A[i] @ A[j] + A[j] @ A[i] - 2 * c * c * (i == j) * I8).max() for i in range(3) for j in range(3)), abs(beta - W).max(),
               max(abs(beta @ x + x @ beta).max() for x in A), abs(g5 @ g5 - I8).max(), len(cm), np.trace(g5).real)
check('A5 light algebra of the tick (steps pi/2 and 0.04): {A_a,A_b}=2c^2, beta = W exactly, g5 = -iA1A2A3/c^3 block-local, traceless; commutant = M_2 (the copy factor)',
      all(r[0] < 1e-8 and r[1] < 1e-9 and r[2] < 1e-8 and r[3] < 1e-8 and r[4] == 4 and abs(r[5]) < 1e-8 for r in res.values()), 'c = 0.5774, 0.0231')
Ls = 5; outs = []
for bb, wmax, tau in ((0.0, 0.2, 0.6), (np.pi / 2 - 0.04, 0.005, 0.02)):
    A, c, beta, g5 = algebra(bb)
    for sgn in (1, -1):
        Xo = 1j * W @ (sgn * 1j * W @ g5); xa = max(abs(Xo @ y - y @ Xo).max() for y in A) + abs(Xo @ W + W @ Xo).max() + abs(Xo + sgn * g5).max()
        xa += max(abs(Grot(R) @ g5 @ Grot(R).conj().T - g5).max() + abs(Grot(R) @ W @ Grot(R).conj().T - W).max() for R in rots)
        Ss = expm(-1j * tau * Hsyn(Ls, W, sgn * 1j * W @ g5)); Uf = lambda q: Ss @ np.kron(np.eye(Ls), U3(q, 0, bb))
        fn, dn = flux(lambda q: wall_upper(Uf(q), Ls, wmax, 0)); ff, df = flux(lambda q: wall_upper(Uf(q), Ls, wmax, -1)); outs.append((round(fn, 3), round(ff, 3), dn, df, xa))
check('A6 wall content: X = i beta\' G4\' (commutes with A_a, anticommutes with beta\') is bound at the ends; X = -g5 puts both copies\' L-Weyl at one end (flux +2) and R at the other, steps pi/2 and 0.04, either orientation; this wall keeps all 24 rotations',
      all(abs(o[0] - t_[0]) < 1e-3 and abs(o[1] - t_[1]) < 1e-3 for o, t_ in zip(outs, [(2, -2), (-2, 2)] * 2)) and all(o[2] == {2} and o[3] == {2} and o[4] < 1e-8 for o in outs), '(near, far) fluxes ' + ' '.join(f'({o[0]:+.3f},{o[1]:+.3f})' for o in outs))
def end_gaps(bb, tau, bp, G4, Ls=4, n=6):
    Ss = expm(-1j * tau * Hsyn(Ls, bp, G4)); worst = 9.0; g = 2 * np.pi * (np.arange(n) + 0.5) / n - np.pi
    pts = [np.pi * v.astype(float) for v in C[1:]] + [np.array(q) for q in itertools.product(g, g, g) if np.linalg.norm(q) > 0.5]
    for Q in pts:
        w, V = schur_eig(Ss @ np.kron(np.eye(Ls), U3(Q, 0, bb))); wt = np.sum(abs(V[:8]) ** 2, 0); bare = np.abs(np.angle(np.linalg.eigvals(U3(Q, 0, bb)))).min()
        if (wt > .3).any(): worst = min(worst, np.abs(w[wt > .3]).min() / bare)
    return worst
dg = {}
for eps_, tau_ in ((0.04, 0.6), (0.04, 0.02), (np.pi / 2, 0.6)):
    A, c, beta, g5 = algebra(np.pi / 2 - eps_); dg[eps_, tau_] = end_gaps(np.pi / 2 - eps_, tau_, W, 1j * W @ g5)
check('A6b the end reproduces the doublers unless tau(2-m0) stays below the tick\'s smallest doubler gap (~1.15 eps, X points)',
      dg[0.04, 0.6] < 0.01 and dg[0.04, 0.02] > 0.7 and dg[np.pi / 2, 0.6] > 0.7, 'min end |w| / bare |w| off K=0: eps .04 tau .6 %.4f (doublers at X, M, R), eps .04 tau .02 %.2f, eps pi/2 tau .6 %.2f' % (dg[0.04, 0.6], dg[0.04, 0.02], dg[np.pi / 2, 0.6]))
A, c, beta, g5 = algebra(0.0); s3 = S @ g5; cm = commutant(A + [beta]); Y = sum(rng.normal() * v for v in cm); Y = Y + Y.conj().T; Y = (Y - s3 @ Y @ s3) / 2; s1 = Y / np.sqrt(np.trace(Y @ Y).real / 8)
s2 = -1j * s3 @ s1; Rodd = [R for R in rots if np.allclose(Grot(R) @ S @ Grot(R).conj().T, -S)][0]; Godd = Grot(Rodd); M = Godd @ Pinv
ma, mb = np.trace(M @ s1 @ M.conj().T @ s1).real / 8, np.trace(M @ s1 @ M.conj().T @ s2).real / 8; ew, ev = np.linalg.eigh(np.array([[ma, mb], [mb, -ma]]))
v1 = ev[:, np.argmax(ew)]; s1 = v1[0] * s1 + v1[1] * s2; s2 = -1j * s3 @ s1
Ssc = expm(-1j * 0.6 * Hsyn(Ls, W @ s1, W @ s2)); Ucw = lambda q: Ssc @ np.kron(np.eye(Ls), U3(q)); Xc = 1j * (W @ s1) @ (W @ s2)
xc = max(abs(Xc @ y - y @ Xc).max() for y in A) + abs(Xc @ W @ s1 + W @ s1 @ Xc).max() + abs(Xc + s3).max()
SS = np.kron(np.eye(Ls), S); qq = rng.uniform(-np.pi, np.pi, 3); fl = {}; dgc = end_gaps(0.0, 0.6, W @ s1, W @ s2)
for sec in (1, -1):
    Pb = np.kron(np.eye(Ls), (I8 + sec * S) / 2); ww, VV = np.linalg.eigh(Pb); Bs = VV[:, ww > .5]
    for end in (0, -1): fl[sec, end] = round(flux(lambda q: wall_upper(Bs.conj().T @ Ucw(q) @ Bs, Ls, 0.2, end, Bs))[0], 3)
check('A7 step pi/2 only: with copy-mixing mass beta\' = W s1 the end binds a whole copy (X = -s3); s is exact and the near end is L on even cells, R on odd (copy +), the far end the mirror',
      xc < 1e-8 and dgc > 0.7 and np.abs(SS @ Ucw(qq) - Ucw(qq) @ SS).max() < 1e-9 and all(abs(fl[k_] - v_) < 1e-3 for k_, v_ in {(1, 0): 1.0, (1, -1): -1.0, (-1, 0): -1.0, (-1, -1): 1.0}.items()), f'sector fluxes (s=+1 near,far; s=-1 near,far) = {fl[1, 0]}, {fl[1, -1]}, {fl[-1, 0]}, {fl[-1, -1]}; doublers gapped ({dgc:.2f})')
JJ = np.kron(np.eye(Ls)[::-1], M); G3 = [Grot(R) for R in rots if abs(np.trace(R)) < 1e-9][0]
symJ = np.abs(JJ @ Ucw(qq) @ JJ.conj().T - Ucw(-(Rodd @ qq))).max()
rot3 = np.degrees(np.arctan2(np.trace(G3 @ s1 @ G3.conj().T @ s2).real / 8, np.trace(G3 @ s1 @ G3.conj().T @ s1).real / 8))
check('A8 the copy wall is exactly symmetric under M.J (M = odd rotation x inversion, J: layer j -> L-1-j), which swaps the ends; C3 turns the copy-mixing mass by 120 deg (rotations survive only at long wavelength)',
      symJ < 1e-9 and abs(abs(rot3) - 120) < 1e-6, f'||MJ U MJ^+ - U(R\'Q)|| {symJ:.1e}, C3 angle {rot3:+.1f}')
reps = {'plain': [(1, 2, 1, 2)], 'Xi': [(1, 2, 1, 1), (-1, 1, 2, 1)]}           # (A(SU4), dim SU2_L, dim SU2_R, copies)
an = {nm: (sum(f[0] * f[1] * f[2] * f[3] for f in fs), sum(4 * f[2] * f[3] for f in fs if f[1] == 2) % 2, sum(4 * f[1] * f[3] for f in fs if f[2] == 2) % 2) for nm, fs in reps.items()}
check('A9 anomalies of the end content: the plain end (X = -g5) on the rung-1 cell (one (4,2)) has SU(4)^3 = 4, not a consistent colour theory; a family end needs X = -g5 Xi, Xi = +1 on (4,2,1), -1 on (4,1,2) (A6 orientations)',
      an['plain'][0] == 4 and an['Xi'] == (0, 0, 0), f'(SU4^3, Witten L, Witten R): plain 2x(4,2)_L {an["plain"]}, Xi (4,2,1)_L+(4b,1,2)_L {an["Xi"]}')

print('== B. Floquet 0/pi pumping')
def rand_refl(n, t):
    d = (n + t) // 2; Q, _ = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))); return Q @ np.diag([1] * d + [-1] * (n - d)) @ Q.conj().T
def ktr(U, R1, sgn):
    w, V = schur_eig(U); sel = np.abs(np.exp(-1j * w) - sgn) < 1e-8
    return (0.0, 0) if not sel.any() else (np.trace(V[:, sel].conj().T @ R1 @ V[:, sel]).real, int(sel.sum()))
okb = True; tab = []
for (n_, t1, t2) in ((40, 6, -2), (40, 0, 4), (41, 3, -5), (40, 0, 0)):
    R1, R2 = rand_refl(n_, t1), rand_refl(n_, t2); (tp, dp), (tm, dm) = ktr(R1 @ R2, R1, 1), ktr(R1 @ R2, R1, -1)
    okb &= abs(tp - (t1 + t2) / 2) < 1e-8 and abs(tm - (t1 - t2) / 2) < 1e-8; tab.append((int(round(tp)), int(round(tm))))
check('B1 for U = R1 R2 (two reflections): tr R1 on U=+1 is (trR1+trR2)/2 and on U=-1 is (trR1-trR2)/2 (exact integers)', okb, f'(traces) -> {tab}')
Lt = 4; sites = np.array(list(itertools.product(range(Lt), repeat=3))); idx = {tuple(s_): i for i, s_ in enumerate(sites)}
def layer(off, th):
    Mx = np.zeros((Lt ** 3, Lt ** 3), complex)
    for b0 in itertools.product(range(0, Lt, 2), repeat=3):
        X = np.array(b0) + off + C; ids = [idx[tuple(v % Lt)] for v in X]; rs = [int((v % 2) @ [4, 2, 1]) for v in X]
        Dp = np.diag(np.exp(1j * th[ids])); Mx[np.ix_(ids, ids)] = Dp @ W[np.ix_(rs, rs)] @ Dp.conj().T
    return Mx
rb = []
for th_e, th_o in ((np.zeros(64), np.zeros(64)), (rng.uniform(0, 2 * np.pi, 64), rng.uniform(0, 2 * np.pi, 64))):
    We, Wo = layer(0, th_e), layer(1, th_o); U = Wo @ We
    rb.append((abs(We @ We - np.eye(64)).max() + abs(Wo @ Wo - np.eye(64)).max(), np.trace(We).real, np.trace(Wo).real, ktr(U, Wo, 1), ktr(U, Wo, -1)))
check('B2 step pi/2 tick U = W_o W_e on a 4^3 torus: W_o U W_o = U^+ (Floquet Ginsparg-Wilson form); with any site-phase links both W stay traceless reflections, so the index at 0 and pi is 0',
      all(r[0] < 1e-12 and abs(r[1]) < 1e-12 and abs(r[2]) < 1e-12 and abs(r[3][0]) < 1e-9 and abs(r[4][0]) < 1e-9 for r in rb) and rb[0][3][1] == 8 and rb[0][4][1] == 8,
      f'free: dims (U=1, U=-1) = ({rb[0][3][1]}, {rb[0][4][1]}), W_o-traces 0; random links: dims ({rb[1][3][1]}, {rb[1][4][1]})')
def overlap(L, Qt, m=-1.0):
    N = L * L; ix = lambda x_, y_: (x_ % L) * L + (y_ % L); D = np.zeros((2 * N, 2 * N), complex)
    for x_ in range(L):
        for y_ in range(L):
            i = ix(x_, y_); D[2 * i:2 * i + 2, 2 * i:2 * i + 2] += (m + 2) * I2
            for mu_, (dx, dy), Ul in ((0, (1, 0), np.exp(-2j * np.pi * Qt * y_ / L ** 2)), (1, (0, 1), np.exp(2j * np.pi * Qt * x_ / L) if y_ == L - 1 else 1.0)):
                j = ix(x_ + dx, y_ + dy); gm = (sx, sy)[mu_]
                D[2 * i:2 * i + 2, 2 * j:2 * j + 2] += 0.5 * (gm - I2) * Ul; D[2 * j:2 * j + 2, 2 * i:2 * i + 2] += 0.5 * (-gm - I2) * np.conj(Ul)
    G5 = np.kron(np.eye(N), sz); Hh = G5 @ D; w, V = np.linalg.eigh((Hh + Hh.conj().T) / 2); sg = V @ np.diag(np.sign(w)) @ V.conj().T
    far = max(np.abs(sg[2 * i:2 * i + 2, 2 * j:2 * j + 2]).max() for i in range(N) for j in range(N)
              if max(min(abs(i // L - j // L), L - abs(i // L - j // L)), min(abs(i % L - j % L), L - abs(i % L - j % L))) >= L // 2)
    return ktr(G5 @ sg, G5, -1)[0], np.trace(sg).real, far
ov = [overlap(8, q) for q in (0, 1, 2)]
check('B3 contrast: the 2D overlap V = g5 sign(H_W) has index -Q = -tr sign(H_W)/2 in flux Q = 0,1,2, because sign(H_W) is not ultralocal (elements ~1e-2 at distance L/2)',
      all(abs(o[0] + q) < 1e-8 and abs(o[1] - 2 * q) < 1e-8 and o[2] > 1e-3 for o, q in zip(ov, (0, 1, 2))), 'index ' + ', '.join(f'{o[0]:+.0f}' for o in ov) + f'; far element {min(o[2] for o in ov):.1e}')

print('== C. CL-5 and mirror gapping')
Lm = 8; aa = np.array([[0, 1], [0, 0]], complex)
def cop(i):
    out = np.array([[1.0 + 0j]])
    for o in [sz] * i + [aa] + [I2] * (Lm - i - 1): out = np.kron(out, o)
    return out
cs = [cop(i) for i in range(Lm)]; Nop = sum(q.conj().T @ q for q in cs)
Dl = np.diag(np.exp(1j * rng.uniform(0, 2 * np.pi, 8))); lam = rng.uniform(.5, 1.5, (8, 8)); lam = (lam + lam.T) / 2
Wl = Dl @ (lam * W) @ Dl.conj().T; Hw = sum(Wl[i, j] * cs[i].conj().T @ cs[j] for i in range(8) for j in range(8))
Kc = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)); Kc = Kc + Kc.conj().T; Jc = sum(Kc[i, j] * cs[i].conj().T @ cs[j] for i in range(8) for j in range(8))
O4 = cs[0] @ cs[1] @ cs[2] @ cs[3]
check('C1 total mode number N is exact under CL-1..CL-5: the tick with site-phase links and edge-length amplitudes, and every current x current response term, commute with N; a four-mode term has [N,O] = -4 O',
      abs(Hw @ Nop - Nop @ Hw).max() < 1e-12 and abs(Jc @ Jc @ Nop - Nop @ Jc @ Jc).max() < 1e-10 and abs(Nop @ O4 - O4 @ Nop + 4 * O4).max() < 1e-12)
def nullsp(rows, n=8):
    _, sv, Vh = np.linalg.svd(np.vstack(rows)); sv = np.concatenate([sv, np.zeros(n * n - len(sv))]); return [v.conj().reshape(n, n) for v, x in zip(Vh, sv) if x < 1e-7]
A, c, beta, g5 = algebra(0.0); anti = [np.kron(y, I8) + np.kron(I8, y.T) for y in A]
masses = nullsp(anti); inv = nullsp(anti + [np.kron(S, I8) - np.kron(I8, S.T)])
check('C2 at step pi/2 the masses ({M,A_a}=0) span 8; the 4 that commute with s (keep SU(2)_even x SU(2)_odd) all anticommute with s3: every symmetric bilinear pairs the family with the mirror',
      len(masses) == 8 and len(inv) == 4 and max(abs(m_ @ s3 + s3 @ m_).max() for m_ in inv) < 1e-8, 'so a free history (CL-5 as written) cannot gap the mirror alone')
fam = [('Q', 1, Fr(1, 6), 2, 3), ('u^c', -1, Fr(-2, 3), 1, 3), ('d^c', -1, Fr(1, 3), 1, 3), ('L', 1, Fr(-1, 2), 2, 1), ('e^c', -1, Fr(1), 1, 1), ('nu^c', -1, Fr(0), 1, 1)]
def anom(fs):
    m = lambda f: f[3] * f[4]
    return {'N-Y2': sum(m(f) * f[1] * f[2] ** 2 for f in fs), 'N-SU2^2': sum(Fr(f[4] * f[1], 2) for f in fs if f[3] == 2), 'N-SU3^2': sum(Fr(f[3] * f[1], 2) for f in fs if f[4] == 3),
            'N3': sum(m(f) * f[1] ** 3 for f in fs), 'N': sum(m(f) * f[1] for f in fs), 'N2Y': sum(m(f) * f[1] ** 2 * f[2] for f in fs), 'Y3': sum(m(f) * f[2] ** 3 for f in fs), 'Y': sum(m(f) * f[2] for f in fs)}
af = anom(fam); am = anom([(n_, -q, -y, d2, d3) for n_, q, y, d2, d3 in fam]); vtx = sum(f[4] * f[1] for f in fam if f[3] == 2)
check('C3 one family (with nu^c): N-Y^2 = -2, N-SU(2)^2 = +2, all else 0; mirror opposite. Exact N forbids gapping the mirror alone; the instanton vertex has dN = 4, so Z_k of N survives iff k | 4',
      af['N-Y2'] == -2 and af['N-SU2^2'] == 2 and all(af[k] == 0 for k in ('N-SU3^2', 'N3', 'N', 'N2Y', 'Y3', 'Y')) and all(am[k] == -af[k] for k in af) and vtx == 4
      and sum(f[3] * f[4] for f in fam) == 16, f'dN per vertex {vtx}; Weyl count 16 = 0 mod 16')
okm = []
for mu, bb in ((0.3, 0.4), (0.0, 0.0), (0.1, 1.53)):
    okm.append(abs(M @ U3(qq, mu, bb) @ M.conj().T - U3(-(Rodd @ qq), mu, bb)).max())
check('C4 exact mirror reflection M = (odd rotation)(inversion) at every step and mass: M s M^+ = s, M g5 M^+ = -g5, M s3 M^+ = -s3, M W M^+ = W: it maps the copy-+ family onto the copy-- mirror on the same cells',
      max(okm) < 1e-12 and np.allclose(M @ S @ M.conj().T, S) and abs(M @ g5 @ M.conj().T + g5).max() < 1e-8 and abs(M @ s3 @ M.conj().T + s3).max() < 1e-8 and abs(M @ W @ M.conj().T - W).max() < 1e-12,
      f'covariance {max(okm):.0e}')

print('== D. against measurement (estimates)')
GeV_s, yr = 6.582e-25, 3.156e7; Lam = 1.22e19 / 3; tau_p = Lam ** 4 / 0.938 ** 5 * GeV_s / yr
gdec = 106.75 + 48 * 2 * 7 / 8; dNeff = 48 * (10.75 / gdec) ** (4 / 3); Lsneed = np.log(0.05e-9 / Lam) / np.log(0.4)
print(f'   proton: a Planck-suppressed dN=4 term gives tau_p ~ Lambda^4/m_p^5 = {tau_p:.0e} yr (Super-K bound 2.4e34 yr); wall leakage adds (p/Lambda)^4 per leg')
print(f'   a massless mirror kept "unobserved" but sphaleron-coupled thermalises (rate ~25 a_W^5 T > H for 1e2-1e12 GeV): dN_eff = {dNeff:.2f} vs N_eff = 2.99 +- 0.17')
print(f'   wall leakage with |1-m0| = 0.4 and Lambda = M_P/3: m_res < 0.05 eV needs L_s >= {int(np.ceil(Lsneed))}; at m0 = r the chain is dimerised and the K=0 end modes are exact for any L_s >= 2')
print('   copy wall (A7) needs step pi/2, where partner pairs at quasi-energy pi are resonant (register: eps < 0.04); the Xi wall (A6/A9) works at eps = 0.04 if tau < ~eps (A6b)')
check('D1 estimates: proton safe, decoupled massless mirror excluded by N_eff, L_s bound finite', tau_p > 2.4e34 and dNeff > 0.6 and 50 < Lsneed < 100, f'{time.monotonic() - T0:.1f} s')
print('theorems: A1 folding, A2 Haar locking, A3 swap depth, A5 algebra, A6 end content, B1 two-reflection index, C1 N exact, C2 bilinears, C3 anomaly sums, C4 M.')
print('cited, not rederived: SK1(C[Z^3]) = 0 (W3 = 0 for non-circuit finite-range QCAs), anomaly matching for on-site symmetries, SMG gapped-phase existence.')
print('supplied: internal index carried in parallel, synthetic mass beta\', m0, r, tau, layer count, Xi, the dN=4 term and its symmetry.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
