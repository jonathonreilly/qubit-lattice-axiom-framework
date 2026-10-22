#!/usr/bin/env python3
"""octree-field: what the gauged octree ladder (octree-16 rules: SM 16 in parallel on every rung, exchange W(1+g5)/2, coarse
links by fine-path transport) does in a background magnetic field (supplied models, finite diagnostics, exact power counting;
estimates against measurement; no physical identification is established).
 A  exact: coarse holonomy = enclosed flux (any local covariant transport), coarse modes carry the fine charge, per-rung scaling
 B  field-induced compensating modes (massless ladder): count, velocity = <2^j> x light speed, hybridisation with rung 0
 C  coarse-rung bulk magnetic response (ladder gapped by a species mass on every rung): sign, size, growth 2^j, rung locality
 D  against measurement (estimates): magnetostatics and light speed, PVLAS, IXPE magnetars, Penning-trap g-2, energy loss"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/FINE_RATE_OCTREE_LADDER_CHARGED_COARSE_SEA_MAGNETIC_RESPONSE_DOUBLES_PER_RUNG_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from fractions import Fraction as Fr
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm, eigh, eigvalsh
from scipy.sparse.csgraph import connected_components

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
OM = np.exp(2j * np.pi / 3); I8 = np.eye(8)
C = np.array(list(itertools.product((0, 1), repeat=3))); cc0 = C - 0.5
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        Rm = np.zeros((3, 3))
        for i in range(3): Rm[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(Rm), 1): rots.append(Rm)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def axang(Rm):
    a = np.arccos(np.clip((np.trace(Rm) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((Rm + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([Rm[2, 1] - Rm[1, 2], Rm[0, 2] - Rm[2, 0], Rm[1, 0] - Rm[0, 1]]) / (2 * np.sin(a)), a
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: g = XI[a].conj() @ XI[b]; W[a, b] = -g / abs(g) / np.sqrt(3)
def Lrot(Rm):
    n_, a = axang(Rm); Dm = expm(-1j * a * sum(n_[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = int(np.argmin(np.sum(abs(cc0 - Rm @ cc0[i]), 1))); L[k, i] = XI[k].conj() @ Dm @ XI[i]
    return L
def ex(th): return np.cos(th) * I8 + 1j * np.sin(th) * W
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def logH(U):
    w, V = np.linalg.eig(U); H = (V * (-np.angle(w))) @ np.linalg.inv(V); return (H + H.conj().T) / 2
class Tick:   # CL-1 tick: even cube exp(-i st W), odd cube exp(+i st W); copy mass F = exp(i M P1 W / 2) on both sides
    def __init__(s, st):
        s.st, s.Ve, s.Vo = st, ex(-st), ex(st); h = 1e-5; al = []
        U0 = lambda K: Dg(K) @ ex(st) @ Dg(K).conj().T @ ex(-st)
        for a in range(3):
            e = np.zeros(3); e[a] = h; A = (logH(U0(e)) - logH(U0(-e))) / (2 * h); al.append((A + A.conj().T) / 2)
        s.v = np.sqrt(np.trace(al[0] @ al[0]).real / 8); s.al = [A / s.v for A in al]
        g5 = 1j * s.al[0] @ s.al[1] @ s.al[2]; s.g5 = (g5 + g5.conj().T) / 2
        iC3 = [i for i, Rm in enumerate(rots) if np.isclose(np.trace(Rm), 0) and np.allclose(axang(Rm)[0], np.ones(3) / np.sqrt(3))][0]
        Sig = [-1j * s.al[1] @ s.al[2], -1j * s.al[2] @ s.al[0], -1j * s.al[0] @ s.al[1]]; L3 = Lrot(rots[iC3]); s.Sig = Sig
        Mr = np.array([[np.trace(L3 @ s.al[a] @ L3.conj().T @ s.al[b]).real / 8 for b in range(3)] for a in range(3)]); nax, ang = axang(np.round(Mr).T)
        best = min((max(np.abs(Sx @ s.al[q] @ Sx.conj().T - L3 @ s.al[q] @ L3.conj().T).max() for q in range(3)), k, Sx) for k, Sx in
                   enumerate(expm(-1j * sgn * ang / 2 * sum(nax[k_] * Sig[k_] for k_ in range(3))) for sgn in (1, -1)))
        wr, Vr = np.linalg.eig(best[2].conj().T @ L3); Vl = Vr[:, np.abs(wr - OM) < 1e-5]; P1 = Vl @ np.linalg.pinv(Vl)
        s.P1 = (P1 + P1.conj().T) / 2; s.Fc = {}
    def U(s, K, M=0.0):
        X = Dg(K) @ s.Vo @ Dg(K).conj().T @ s.Ve
        if M:
            F = s.Fc.setdefault(M, expm(1j * M * s.P1 @ W / 2)); X = F @ X @ F
        return X
    def H(s, K, M=0.0): return logH(s.U(K, M)) / s.st
def expmh(H, t):   # exp(-i t H) for Hermitian H
    w, V = np.linalg.eigh((H + H.conj().T) / 2); return (V * np.exp(-1j * t * w)) @ V.conj().T
def lidx(L, x):
    x = np.mod(x, L); return int((x[0] * L[1] + x[1]) * L[2] + x[2])
def coarse_links(A, L):
    Lc = tuple(l // 2 for l in L); Ac = []
    for mu in range(3):
        a = np.zeros(Lc)
        for p in itertools.product(*[range(l) for l in Lc]):
            x = 2 * np.array(p); y = x.copy(); y[mu] += 1; a[p] = A[mu][tuple(np.mod(x, L))] + A[mu][tuple(np.mod(y, L))]
        Ac.append(a)
    return Ac, Lc
def path_phase(A, L, x0, x1):   # transporter x0 -> x1 along x, then y, then z (direct displacement)
    ph = 0.0; x = np.array(x0, int).copy()
    for mu in range(3):
        dd = int(x1[mu] - x0[mu])
        for _ in range(abs(dd)):
            if dd > 0: ph += A[mu][tuple(np.mod(x, L))]; x[mu] += 1
            else: x[mu] -= 1; ph -= A[mu][tuple(np.mod(x, L))]
    return ph
def cube_blocks(A, L, par):
    out = []
    for n in itertools.product(*[range(l // 2) for l in L]):
        o = 2 * np.array(n) + par; xs = [o + cp for cp in C]; ids = [lidx(L, x) for x in xs]
        lab = [int(np.argmin(np.abs(C - np.mod(x, 2)).sum(1))) for x in xs]; Wg = np.zeros((8, 8), complex)
        for i in range(8):
            for k in range(8):
                if np.abs(C[i] - C[k]).sum() == 1: Wg[i, k] = W[lab[i], lab[k]] * np.exp(1j * path_phase(A, L, xs[k], xs[i]))
        out.append((ids, lab, xs, Wg))
    return out
def copy_block(A, L, xs, lab, P1W):
    B = np.zeros((8, 8), complex)
    for i in range(8):
        for k in range(i, 8):
            if abs(P1W[lab[i], lab[k]]) > 1e-14:
                B[i, k] = P1W[lab[i], lab[k]] * np.exp(1j * path_phase(A, L, xs[k], xs[i]))
                if k != i: B[k, i] = np.conj(B[i, k])
    return B
def h5_blocks(A, L, Xm):   # coarse site P sits at fine position 2P; coarse cube n <-> its 8 children, corner b <-> corner a via X[a,b]/sqrt8
    Lc = tuple(l // 2 for l in L); out = []
    for n in itertools.product(*[range(l // 2) for l in Lc]):
        n = np.array(n); fids, fpos, flab, cids, cpos = [], [], [], [], []
        for c in C:
            for ia, a in enumerate(C): x = 2 * (2 * n + c) + a; fids.append(lidx(L, x)); fpos.append(x); flab.append(ia)
        for b in C: P = 2 * n + b; cids.append(lidx(Lc, P)); cpos.append(2 * P)
        B = np.zeros((72, 72), complex)
        for i in range(64):
            for k in range(8):
                v = Xm[flab[i], k] / np.sqrt(8)
                if abs(v) > 1e-15: B[i, 64 + k] = v * np.exp(1j * path_phase(A, L, cpos[k], fpos[i])); B[64 + k, i] = np.conj(B[i, 64 + k])
        out.append((fids, cids, B))
    return out
def ladder_parts(tk, A0, L0, R, Xm, M, dense=False, mu=0.0):
    As, Ls = [A0], [tuple(L0)]
    for j in range(R):
        Ac, Lc = coarse_links(As[-1], Ls[-1]); As.append(Ac); Ls.append(Lc)
    Ns = [int(np.prod(l)) for l in Ls]; off = np.concatenate([[0], np.cumsum(Ns)]).astype(int); Nt = int(off[-1]); P1W = tk.P1 @ W; P1W = (P1W + P1W.conj().T) / 2
    ve, vo, ff = [], [], []
    for j in range(R + 1):
        for (ids, lab, xs, Wg) in cube_blocks(As[j], Ls[j], 0):
            g = [off[j] + i for i in ids]; ve.append((g, expm(-1j * (tk.st - mu / 2) * Wg))); ff.append((g, expm(1j * M * copy_block(As[j], Ls[j], xs, lab, P1W) / 2)))
        for (ids, lab, xs, Wg) in cube_blocks(As[j], Ls[j], 1): vo.append(([off[j] + i for i in ids], expm(1j * (tk.st + mu / 2) * Wg)))
    r_, c_, v_ = [], [], []
    for j in range(R):
        for (fids, cids, B) in h5_blocks(As[j], Ls[j], Xm):
            ids = np.array([off[j] + f for f in fids] + [off[j + 1] + c for c in cids]); ii, jj = np.meshgrid(ids, ids, indexing='ij'); m = np.abs(B) > 0
            r_.append(ii[m]); c_.append(jj[m]); v_.append(B[m])
    e5 = []
    if R:
        H5 = sp.csr_matrix((np.concatenate(v_), (np.concatenate(r_), np.concatenate(c_))), shape=(Nt, Nt))
        nc, lab = connected_components(H5 != 0, directed=False)
        for k in range(nc):   # exact exp(-i tau H5) by connected components (one per top-rung cube)
            ids = np.where(lab == k)[0]
            if len(ids) > 1: e5.append((list(ids), expmh(H5[ids][:, ids].toarray(), 0.5 * tk.st)))
    def blk(blocks):
        if not blocks: return sp.identity(Nt, dtype=complex, format='csr')
        r, c, v = [], [], []
        for ids, B in blocks:
            ii, jj = np.meshgrid(ids, ids, indexing='ij'); r.append(ii.ravel()); c.append(jj.ravel()); v.append(B.ravel())
        Mx = sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(Nt, Nt)); Dm = sp.lil_matrix((Nt, Nt), dtype=complex)
        cov = np.zeros(Nt, bool); cov[np.concatenate([np.array(i) for i, _ in blocks])] = True
        for i in np.where(~cov)[0]: Dm[i, i] = 1.0
        return (Mx + Dm.tocsr()).tocsr()
    T = (blk(ff) @ (blk(vo) @ (blk(ve) @ blk(ff)))).tocsr(); rung = np.concatenate([np.full(Ns[j], j) for j in range(R + 1)])
    if not dense: return (blk(e5) @ T).tocsr(), rung
    Ud = np.zeros((Nt, Nt), complex); done = np.zeros(Nt, bool)
    for ids, B in e5: Ud[ids, :] = B @ T[ids, :].toarray(); done[ids] = True
    for i in np.where(~done)[0]: Ud[i, :] = T[i, :].toarray()
    return Ud, rung
def landau(L, F, theta):   # F flux quanta through every xy layer (Landau gauge), holonomy theta along z
    Lx, Ly, Lz = L; A = [np.zeros(L), np.zeros(L), np.full(L, theta / Lz)]
    for x in range(Lx):
        for y in range(Ly):
            A[0][x, y, :] = -2 * np.pi * F * y / (Lx * Ly)
            if y == Ly - 1: A[1][x, y, :] = 2 * np.pi * F * x / Lx
    return A
def sinpart(U, nb=128):   # in place: lower triangle of (U - U^+)/2i (= sin of the quasi-energies), returned as a Fortran view
    N = len(U)
    for r0 in range(0, N, nb):
        r1 = min(N, r0 + nb); U[r0:r1, :r1] = (U[r0:r1, :r1] - U[:r1, r0:r1].conj().T) * (-0.5j)
    return U.T                                                                 # F-ordered; its upper triangle = conj of K's lower

tk = Tick(0.04); MC = tk.st; KAP = 0.5; g5 = tk.g5; Pp = (I8 + g5) / 2; XL = W @ Pp; VS = 2 * np.sin(tk.st) / np.sqrt(3)  # light speed, sites/tick
def lan(L, F, phx=0.0, thz=0.0):
    A = landau(L, F, thz); A[0] = A[0] + phx / L[0]; return A
def wrap(x): return (x + np.pi) % (2 * np.pi) - np.pi
# ============================================================ A
print('== A. exact: coarse links, charges, per-rung scaling')
L = (16, 16, 8); F = 3; A0 = lan(L, F, 0.0, 0.7); rng = np.random.default_rng(1); chi = rng.uniform(-np.pi, np.pi, L)
Ag = [A0[m] + np.roll(chi, -1, axis=m) - chi for m in range(3)]; err = 0.0
for AA in (A0, Ag):
    As, Ls = [AA], [L]
    for j in range(2): Ac, Lc = coarse_links(As[-1], Ls[-1]); As.append(Ac); Ls.append(Lc)
    for j in (1, 2):
        Ax, Ay, Az = As[j]; pxy = Ax + np.roll(Ay, -1, 0) - np.roll(Ax, -1, 1) - Ay; pxz = Ax + np.roll(Az, -1, 0) - np.roll(Ax, -1, 2) - Az
        err = max(err, np.abs(wrap(pxy - 4 ** j * 2 * np.pi * F / 256)).max(), np.abs(wrap(pxz)).max())
check('A1 THEOREM coarse holonomy = enclosed flux: rung-j plaquette phase = 4^j x fine plaquette flux, gauge invariant (Stokes; any local '
      'covariant transport gives the same up to O(dF))', err < 1e-12, f'rungs 1, 2, random gauge: max error {err:.0e}')
Ud, rung = ladder_parts(tk, [np.zeros((8, 8, 4))] * 3, (8, 8, 4), 1, XL, MC, dense=True)
nc, _ = connected_components(sp.csr_matrix(np.abs(Ud) > 1e-12), directed=False)
check('A2 THEOREM the ladder graph is connected, so a U(1) commuting with it gives coarse modes the fine charge: coarse rungs are charged '
      '(neutral coarse modes would make the light charge leak through H5)', nc == 1, f'components {nc} of {len(Ud)} modes')
pc = [(Fr(16) ** j / Fr(8) ** j, Fr(4) ** j / Fr(8) ** j, Fr(256) ** j / Fr(8) ** j) for j in range(6)]
check('A3 THEOREM power counting at the fine rate (energy per rung-j cell in ticks, cell volume 8^j): B^2 per volume x 2^j, E^2 x 2^-j, '
      'B^4 x 32^j; so d(1/mu)_j = 8 pi alpha q^2 (c_b/v) 2^j and d(eps)_j ~ 2^-j', all(p == (Fr(2) ** j, Fr(1, 2 ** j), Fr(32) ** j) for j, p in enumerate(pc)),
      'exact for j = 0..5')
# ============================================================ B
print("== B. field-induced compensating modes (mu = 0, X' = W(1+g5)/2; slopes in units v/Lz)")
def lev(L, R, F, th, Wt):
    Ud, rung = ladder_parts(tk, landau(L, F, th), L, R, XL, MC, dense=True); KT = sinpart(Ud); del Ud
    w, V = eigh(KT, lower=False, subset_by_value=(-np.sin(Wt), np.sin(Wt)), driver='evr', overwrite_a=True, check_finite=False)
    return -np.arcsin(np.clip(w, -1, 1)), np.array([np.sum(np.abs(V[rung == j]) ** 2, 0) for j in range(R + 1)]), V
def modes(L, R, F, Wt=0.014):
    a, b = lev(L, R, F, 0.3, Wt), lev(L, R, F, 0.5, Wt); ov = np.abs(a[2].conj().T @ b[2]) ** 2; s0, sc = [], []
    for i in range(len(a[0])):
        k = int(np.argmax(ov[i]))
        if ov[i, k] < 0.5: continue
        s = (b[0][k] - a[0][i]) / 0.2 / (tk.v / L[2]); wj = b[1][:, k]
        if s > 1.5 and wj[0] > 0.9: s0.append(s)
        elif s < -2.5: sc.append((s, float(np.sum(wj * 2.0 ** np.arange(R + 1)))))
    g = np.sort(np.abs(lev(L, R, F, 0.0, Wt)[0]))[:2 * abs(F)]
    return s0, sc, 2 * np.mean(g)
res = {F: modes((16, 16, 4), 1, F) for F in (1, 2, 3)}
rat = [-np.mean([s for s, _ in r[1]]) / np.mean(r[0]) for r in res.values()]; avg = [np.mean([e for _, e in r[1]]) for r in res.values()]
check('B1 R = 1, 16x16x4: flux F gives |F| rung-0 lowest-Landau-level branches and |F| compensating branches of opposite slope on rung 1; '
      'compensating velocity / light velocity = <2^j> within 10%', all(len(r[0]) == F and len(r[1]) == F for F, r in res.items())
      and all(abs(x / y - 1) < 0.1 for x, y in zip(rat, avg)), 'F=1,2,3: ratio ' + ', '.join(f'{x:.2f}' for x in rat) + '; <2^j> ' + ', '.join(f'{y:.2f}' for y in avg)
      + f'; rung-0 slope {np.mean(res[1][0]):.2f}')
r2 = {L: modes(L, 2, 1) for L in ((8, 8, 8), (16, 8, 8))}
rr = {L: (-min(s for s, _ in r[1]) / np.mean(r[0]), [e for s, e in r[1] if s == min(x for x, _ in r[1])][0]) for L, r in r2.items()}
check('B2 R = 2: the compensating branch moves at <2^j> times the light speed (middle rung 8^3, top rung 16x8x8) within 10%: velocity '
      '2^j* c on the landing rung j*', all(abs(x / y - 1) < 0.1 for x, y in rr.values()) and rr[(16, 8, 8)][0] > rr[(8, 8, 8)][0],
      '; '.join(f'{L}: {x:.2f} vs {y:.2f}' for L, (x, y) in rr.items()))
hyb = [r[2] for r in res.values()]
check('B3 DIAGNOSTIC hybridisation of rung-0 and compensating branches (avoided crossing at k_z = 0, one rung apart): small, sublinear in F',
      max(hyb) < 2e-3 and hyb[0] < hyb[2], 'gap F=1,2,3: ' + ', '.join(f'{h:.1e}' for h in hyb) + ' rad/tick (bulk gap 1.6e-2)')
# ============================================================ C
print('== C. coarse-rung bulk magnetic response (species mass mu on every rung gaps the ladder; energy = sum of sea quasi-energies)')
def Esea(L, R, F, mu, nkx, nkz, by_rung=False):
    tot = np.zeros(R + 1); gap = np.inf
    for kx in range(nkx):
        for kz in range(nkz):
            Ud, rung = ladder_parts(tk, lan(L, F, 2 * np.pi * kx / nkx, 2 * np.pi * kz / nkz), L, R, XL, MC, dense=True, mu=mu)
            KT = sinpart(Ud); del Ud
            if by_rung:
                w, V = eigh(KT, lower=False, overwrite_a=True, check_finite=False); om = -np.arcsin(np.clip(w, -1, 1)); o = om < 0
                P = np.abs(V[:, o]) ** 2; tot += np.array([np.sum(P[rung == j] @ om[o]) for j in range(R + 1)])
            else:
                w = eigvalsh(KT, lower=False, overwrite_a=True, check_finite=False); om = -np.arcsin(np.clip(w, -1, 1)); tot[0] += np.sum(om[om < 0])
            gap = min(gap, np.abs(om).min())
    return tot / (nkx * nkz), gap
mu = tk.st; L = (8, 32, 4); N = np.prod(L); P0 = lambda F: 2 * np.pi * F / (L[0] * L[1]); cc = {}
for R in (0, 1):
    e0, g0 = Esea(L, R, 0, mu, 4, 2, R == 1); cc[R] = [((Esea(L, R, F, mu, 4, 2, R == 1)[0] - e0) / N / P0(F) ** 2) for F in (1, 2)]; cc[R, 'g'] = g0
c0, c1 = cc[0][0][0], cc[1][0]; A1 = c1.sum() - 2 * c0; cb = (A1 + c1[0]) / 2
quad = [cc[R][1].sum() / cc[R][0].sum() for R in (0, 1)]
check('C1 DIAGNOSTIC 32x32x8-equivalent tori (Bloch twists): gapped (min |w| >= 0.7 mu), quadratic in flux (c(F=2)/c(F=1) = 1 +- 0.1), '
      'field costs energy (diamagnetic) on every rung', min(cc[0, 'g'], cc[1, 'g']) > 0.7 * mu and all(abs(q - 1) < 0.1 for q in quad)
      and c0 > 0 and (c1 > 0).all(), f'gap/mu {cc[0, "g"]/mu:.2f}, {cc[1, "g"]/mu:.2f}; c(2)/c(1) {quad[0]:.3f}, {quad[1]:.3f}')
check('C2 DIAGNOSTIC per-site coefficients dE = c Phi^2 (Phi = plaquette flux, rad/tick): single rung c0; R = 1 total and by rung; '
      'bulk rung c_b = (c1 - 2c0 + c_rung0)/2 > 0 in its own units', cb > 3e-4 and c1.sum() > 3 * c0,
      f'c0 {c0:.2e}; c1 {c1.sum():.2e} = {c1[0]:.2e} (rung 0) + {c1[1]:.2e} (rung 1); c_b {cb:.2e}')
Lf, Lc = (8, 16, 8), (4, 8, 4); d = {}
for nm, LL, R in (('0c', Lc, 0), ('1c', Lc, 1), ('1', Lf, 1), ('2', Lf, 2)):
    d[nm] = Esea(LL, R, 1, mu, 1, 1)[0].sum() - Esea(LL, R, 0, mu, 1, 1)[0].sum()
A_1, A_2 = d['1'] - d['0c'], d['2'] - d['1c']
check('C3 DIAGNOSTIC rung locality of the self-similar recursion E_R(Phi) = E_(R-1)(4 Phi on the coarse lattice) + A(Phi): A independent '
      'of R, so the coefficient grows as 2^R (c0 + A)', abs(A_2 / A_1 - 1) < 0.02, f'A(R=1) {A_1:.4e}, A(R=2) {A_2:.4e} (F = 1, plain tori)')
# ============================================================ D
print('== D. against measurement (estimates; a = sqrt(8 pi) l_P = 8.10e-35 m site spacing, light speed = rung-0 speed)')
alpha = 1 / 137.036; a = np.sqrt(8 * np.pi) * 1.616255e-35; lB = lambda B: 25.6556e-9 / np.sqrt(B); SQ2, SQ3 = 16 / 3, 4.0  # sum q^2, |q|^3 per family
jst = lambda B: int(np.floor(np.log((np.pi / 4) / (a / lB(B)) ** 2) / np.log(4)))       # landing rung: coarsest with plaquette flux <= pi/4
KB = 8 * np.pi * alpha * SQ2 * cb / VS                                                     # d(1/mu) per unit 2^j, summed over the family
dmu = lambda lam: KB * 2.0 ** (np.floor(np.log2(lam / a)) + 1)                             # rungs whose cells the field resolves
mix = sum(np.log10(4.0 ** (i - jst(1.0)) * (np.pi / 4) / (6 * KAP)) for i in range(1, jst(1.0) + 1))
print(f'   compensating modes: rung j*(B) = {jst(1.0)} (1 T), {jst(5.4)} (5.4 T), {jst(1e10)} (1e10 T, magnetar), {jst(1e15)} (1e15 T, heavy ions); '
      f'1D chiral branch along B, velocity 2^j* c = {2.0**jst(1.0):.1e} c at 1 T; next Landau level ~ E_a = 2.4e18 GeV; '
      f'rung-0 overlap amplitude ~ 10^{mix:.0f} (octree-unify D1 law); net charge inflow 0 (sum q^3), conductance along B ~ sum |q|^3 != 0')
lC = 3.8616e-13; d_C, d_um, d_lab = dmu(lC), dmu(1e-6), dmu(0.1)
print(f'   bulk stiffness: K = 8 pi alpha (16/3) c_b / v = {KB:.3f}; d(1/mu) = {d_C:.1e} (electron Compton length), {d_um:.1e} (1 um), '
      f'{d_lab:.1e} (0.1 m); electric d(eps) converges (sum 2^-j)')
cg = np.sqrt(1 + d_um)
print(f'   light: photon/matter speed at 1 um = {cg:.1e} (bound |dc/c| < 3e-19, photon decay at 1.4 PeV); static vs atomic 1/mu ratio '
      f'{d_lab/d_C:.1e} (current balances vs alpha agree to ~1e-6; Weber-Kohlrausch/Rosa-Dorsey ratio of units = c)')
dn_nl = 0.5 * KB * 2.0 ** jst(2.5); dn_cm = alpha / (6 * np.pi) * SQ3 * (0.02 * 1e-3 / lB(2.5) ** 2) / 2.0 ** jst(2.5) / 2
print(f'   PVLAS 2.5 T: nonlinear rung-j* anisotropy dn ~ {dn_nl:.1e}; compensating-branch polarisability (2 cm field line, 1 mm beam) '
      f'dn ~ {dn_cm:.1e}; measured (12 +- 17)e-23, QED 2.5e-23')
d_mag = KB * 2.0 ** jst(1e10); qed_mag = alpha / (3 * np.pi) * np.log(1e10 / 4.414e9)
print(f'   IXPE magnetars (1e10 T): coarse anisotropy ~ {d_mag:.1e} vs QED vacuum term {qed_mag:.1e} (polarisation 12-80% fits QED mode physics)')
print(f'   Penning g-2 (5.4 T): loop photons at k ~ m_e see d(1/mu) ~ {d_C:.0e}, an O(1) change of a_e = alpha/2pi vs agreement to 1e-10; '
      f'compensating mixing 10^{mix:.0f}: no direct shift')
lab = 1.97327e-7 / (alpha * SQ3 * (1 / lB(1.0) ** 2) * 1.97327e-7 ** 2 / 1.17 / 2.0 ** jst(1.0))
print(f'   energy loss: photon -> compensating pair absorption length ~ {lab:.0e} m at 1 T, 1.17 eV; thermal weight c/v = {2.0**-jst(1.0):.0e}: sterile')
check('D1 estimates: bulk stiffness exceeds the light-speed bound by > 1e30, the static/atomic ratio by > 1e10, PVLAS by > 1e40; '
      'compensating branches are sterile in mixing and emission but their polarisability exceeds PVLAS (geometry-dependent)',
      cg - 1 > 1e30 * 3e-19 and d_lab / d_C > 1e10 and dn_nl > 1e40 * 3e-22 and mix < -1000 and lab > 1e15 and dn_cm > 3e-22,
      f'{time.monotonic() - T0:.1f} s')
print('supplied: octree sites, fine rate, X\', kap = 0.5, M = st = 0.04, the species mass mu = st used to gap the ladder in C, tori and '
      'twists, axis-ordered transport, the sea as vacuum, a = sqrt(8 pi) l_P, landing threshold pi/4, PVLAS geometry.')
print('cited: octree-16 C1/C2 counts, octree-unify D1 law, induced-action velocity rescaling, measured values.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
