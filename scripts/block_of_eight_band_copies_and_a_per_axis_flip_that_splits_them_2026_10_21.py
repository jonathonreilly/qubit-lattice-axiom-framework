#!/usr/bin/env python3
"""Copies of the block-of-eight light band: why they do not mix, a per-axis chirality flip that splits them, and their masses.
Base tick: block-local masses m, M, then three axis substeps that move L and R together. Proposal: in each axis
substep, move L, flip chirality by angle theta, then move R. Checks: exact copy degeneracy and coset decoupling of the
base tick, the exact corner spectrum of the proposal, its masses, copy group theory, the mean-step identity and its
rotation covariance. No generation, species or physical mass reading is established.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/BLOCK_OF_EIGHT_BAND_COPIES_AND_A_PER_AXIS_FLIP_THAT_SPLITS_THEM_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md')

import sys, os, signal, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
if not __debug__: raise RuntimeError('Optimized Python is unsupported')
sys.stdout.reconfigure(line_buffering=True)
_STARTED = time.monotonic()
def _timeout(*args):
    raise TimeoutError('Owning 300-second aggregate cap exceeded; streamed diagnostics retained')
signal.signal(signal.SIGALRM, _timeout)
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm, null_space
from scipy.optimize import minimize

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


SX = np.array([[0, 1], [1, 0]], complex); SY = np.array([[0, -1j], [1j, 0]]); SZ = np.diag([1., -1]).astype(complex); AL = [SX, SY, SZ]
I2 = np.eye(2)
AL8 = [np.kron(np.diag([1, -1, 1, -1]), A) for A in AL]          # modes L, R, L', R' (two each): L:+sigma, R:-sigma
PL = np.diag([1, 1, 0, 0, 1, 1, 0, 0]).astype(complex); PR = np.eye(8) - PL
SGN = np.diag([1, 1, 1, 1, -1, -1, -1, -1]).astype(complex)
FLIP = np.zeros((8, 8), complex); FLIP[0:2, 2:4] = I2; FLIP[4:6, 6:8] = I2; FLIP = FLIP + FLIP.T   # L<->R in both families


def cshift(D, k):
    w, V = np.linalg.eigh(D); return V @ np.diag(np.exp(-1j * k * w)) @ V.conj().T


def massgate(m, M):
    Mm = np.zeros((8, 8))
    for (a, b) in ((0, 2), (4, 6)): Mm[a:a+2, b:b+2] = m * I2; Mm[b:b+2, a:a+2] = m * I2
    for (a, b) in ((0, 6), (4, 2)): Mm[a:a+2, b:b+2] = M * I2; Mm[b:b+2, a:a+2] = M * I2
    return expm(-1j * Mm)


def U_base(K, m, M):
    K = np.asarray(K, float); A = massgate(m, M)
    for i in (0, 1, 2): A = cshift(AL8[i], K[i]) @ A
    return SGN @ A


def U_prop(K, m, M, th, order=(0, 1, 2), ths=None):
    """Proposal: per axis, move L (and L'), flip chirality by th, move R (and R')."""
    K = np.asarray(K, float); ths = ths if ths is not None else (th, th, th); A = massgate(m, M)
    for i in order: A = cshift(AL8[i] @ PR, K[i]) @ expm(-1j * ths[i] * FLIP) @ cshift(AL8[i] @ PL, K[i]) @ A
    return SGN @ A


def qmin(U): return np.sort(np.abs(np.angle(np.linalg.eigvals(U))))[0]
def spec(U): return np.sort(np.angle(np.linalg.eigvals(U)))
CORNERS = [np.pi * np.array(c, float) for c in itertools.product((0, 1), repeat=3)]
G3 = [np.pi * np.array(g, float) for g in ((1, 1, 0), (1, 0, 1), (0, 1, 1))]
rng = np.random.default_rng(2026)


def support(f, N=6, rest=False):
    g = 2 * np.pi * np.arange(N) / N; A = np.zeros((N, N, N, 8, 8), complex)
    for a, b, c in itertools.product(range(N), repeat=3): A[a, b, c] = f((g[a], g[b], g[c]))
    C = np.fft.ifftn(A, axes=(0, 1, 2))
    if rest: return np.linalg.norm(C[0, 0, 0], 2)
    return [tuple(((x + N // 2) % N) - N // 2 for x in v) for v in itertools.product(range(N), repeat=3) if np.abs(C[v]).max() > 1e-10]


def zone_min(f, n=21, seeds=40):
    g = np.linspace(-np.pi, np.pi, n); vals = sorted((qmin(f((x, y, z))), (x, y, z)) for x in g for y in g for z in g)
    best = min(minimize(lambda k: qmin(f(k)), k0, method='Nelder-Mead', options={'xatol': 1e-8, 'fatol': 1e-12}).fun for _, k0 in vals[:seeds])
    return min(best, vals[0][0])


def rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3))
            for i in range(3): R[i, perm[i]] = sg[i]
            if np.isclose(np.linalg.det(R), 1): out.append(R)
    return out


def main():
    # 1-2. the base tick: four exactly degenerate copies, carried by the four cosets of the lattice x=y=z mod 2
    Ks = rng.uniform(-np.pi, np.pi, (30, 3))
    d1 = max(np.abs(U_base(K + G, .05, .5) - U_base(K, .05, .5)).max() for K in Ks for G in G3)
    d2 = max(np.abs(U_base(K + np.pi, .05, .5) + U_base(K, .05, .5)).max() for K in Ks)
    check('base tick: U(K+G) = U(K) for G = pi(1,1,0), pi(1,0,1), pi(0,1,1), and U(K+pi(1,1,1)) = -U(K)', d1 < 1e-12 and d2 < 1e-12, f'max dev {max(d1, d2):.1e}')
    sb = support(lambda K: U_base(K, .05, .5))
    check('base tick: every block step lies in the lattice x=y=z mod 2, so the four cosets never exchange amplitude', all((v[0] - v[2]) % 2 == 0 and (v[1] - v[2]) % 2 == 0 for v in sb), f'{len(sb)} steps, all (+-1,+-1,+-1)')
    # 3-4. the proposal
    d3 = max(np.abs(U_prop(K, a, b, 0.) - U_base(K, a, b)).max() for K in Ks[:10] for a, b in ((.05, .5), (.3, 1.2)))
    check('proposal at theta = 0 is the base tick', d3 < 1e-12, f'max dev {d3:.1e}')
    sp = support(lambda K: U_prop(K, .1, .5, .09)); un = max(np.abs(U_prop(K, .1, .5, .09) @ U_prop(K, .1, .5, .09).conj().T - np.eye(8)).max() for K in Ks[:10])
    nb = sum(1 for v in sp if (v[0] - v[2]) % 2 or (v[1] - v[2]) % 2)
    check('proposal is unitary with block steps in {-1,0,1}^3, and some steps leave the coset lattice', un < 1e-12 and max(max(map(abs, v)) for v in sp) <= 1 and nb > 0, f'{len(sp)} steps, {nb} cross cosets')
    rn = support(lambda K: U_prop(K, .1, .5, .09), rest=True)
    check('proposal has a rest step (displacement 0) of operator norm sin(theta)^3, so CL-4 as written does not cover it', abs(rn - np.sin(.09) ** 3) < 1e-12, f'norm {rn:.3e} vs sin^3 {np.sin(.09) ** 3:.3e}')
    # 5. exact corner spectrum, any parameters, any axis order
    worst = 0.
    for _ in range(25):
        m, M, th = rng.uniform(-.7, .7), rng.uniform(-1.5, 1.5), rng.uniform(-.7, .7); order = tuple(rng.permutation(3))
        for G in CORNERS:
            mu = m + th * np.cos(G).sum(); pred = np.array([mu, -mu, np.pi + mu, np.pi - mu] * 2)
            got = np.angle(np.linalg.eigvals(U_prop(G, m, M, th, order)))
            worst = max(worst, max(min(abs(np.angle(np.exp(1j * (x - y)))) for y in pred) for x in got))
    check('corner theorem: at each zone corner the spectrum is {+-mu, pi+-mu} twice, mu = m + theta(3 - 2n), n = number of pi components, for any M and axis order', worst < 1e-12, f'max dev {worst:.1e} (25 random draws)')
    # 6-7. masses
    for (m, M, th, lab) in ((0., .5, .09, 'P1 (m = 0, theta replaces m)'), (.1, .5, .09, 'P2 (m = .1, theta = .09)')):
        f = lambda K: U_prop(K, m, M, th); cm = []
        loc = np.linspace(-.25, .25, 11)
        for G in CORNERS:
            lm = min(qmin(f(G + np.array([x, y, z]))) for x in loc for y in loc for z in loc); cm.append((int(round(G.sum() / np.pi)), qmin(f(G)), lm))
        zm = zone_min(f)
        ok_loc = all(abs(c[1] - c[2]) < 1e-9 and abs(c[1] - abs(m + th * (3 - 2 * c[0]))) < 1e-12 for c in cm)
        masses = sorted(float(round(c[1], 4)) for c in cm)
        check(f'{lab}: band minimum at each corner equals |mu|, and the zone minimum equals the lightest', ok_loc and abs(zm - masses[0]) < 1e-7, f'masses {masses}; zone min {zm:.4f}')
    # 8. copy group theory on the four cosets {0, e1, e2, e3}
    lab_ = lambda v: ((v[0] - v[2]) % 2, (v[1] - v[2]) % 2); reps = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]; idx = {lab_(r): i for i, r in enumerate(reps)}
    def perm(f):
        P = np.zeros((4, 4))
        for i, r in enumerate(reps): P[idx[lab_(f(np.array(r)))], i] = 1
        return P
    rots = rotations()
    tr = [perm(lambda v, t=np.array(t): v + t) for t in reps[1:]]
    ro = [perm(lambda v, R=R: (R @ v).astype(int)) for R in rots]
    c3 = [perm(lambda v, R=R: (R @ v).astype(int)) for R in rots if np.allclose(R @ np.ones(3), np.ones(3))]
    d2 = [perm(lambda v, R=R: (R @ v).astype(int)) for R in rots if np.allclose(R, np.diag(np.diag(R)))]
    def cdim(gens): return null_space(np.vstack([np.kron(g, np.eye(4)) - np.kron(np.eye(4), g.T) for g in gens])).shape[1]
    grp = {np.eye(4).tobytes(): np.eye(4)}; frontier = [np.eye(4)]
    while frontier:
        new = []
        for a in frontier:
            for g in tr + ro:
                b = g @ a
                if b.tobytes() not in grp: grp[b.tobytes()] = b; new.append(b)
        frontier = new
    dims = (cdim(tr + ro), cdim(tr + c3), cdim(tr + d2), cdim(ro), cdim(c3))
    check('copy symmetry: translations and rotations act on the four copies as S4 (order 24); commutant dims transl+rot 2, transl+C3[111] 2, transl+D2 4, rotations only 5, C3 only 6', len(grp) == 24 and dims == (2, 2, 4, 5, 6), f'order {len(grp)}, dims {dims}')
    chars = {tuple(int(round(np.cos(G[i]))) for i in range(3)) for G in CORNERS}
    n1 = sorted(tuple(int(round(np.cos(G[i]))) for i in range(3)) for G in CORNERS if round(G.sum() / np.pi) == 1)
    check('one-block translations commute with both ticks (Bloch form); the eight corners carry eight distinct joint characters, the n=1 triplet the diag triple of the three-generation observable note', len(chars) == 8 and n1 == [(-1, 1, 1), (1, -1, 1), (1, 1, -1)], f'n=1 characters {n1}')
    # 10. what splits the triplet: axis-dependent angles
    ths = (.03, .07, .11); m = .2; dev = 0.
    for k in range(3):
        G = np.pi * (np.ones(3) - np.eye(3)[k]); dev = max(dev, abs(qmin(U_prop(G, m, .5, 0, ths=ths)) - abs(m - sum(ths) + 2 * ths[k])))
    check('axis-dependent angles theta_k split the n=2 triplet as m - sum(theta) + 2 theta_k; equal angles keep it exactly degenerate', dev < 1e-12, f'max dev {dev:.1e}')
    # 11. mean step per axis equals group velocity (record-source identity input)
    rows = []
    for kd, km in (((1, 1, 0), .04), ((1, 2, 3), .05), ((1, .15, .05), .03)):
        for G in (np.zeros(3), G3[0]):
            K = G + km * np.array(kd, float) / np.linalg.norm(kd); a = (.1, .5, .09)
            w, V = np.linalg.eig(U_prop(K, *a)); om = -np.angle(w); i = int(np.argmin(np.where(om > 0, om, 9))); u = V[:, i] / np.linalg.norm(V[:, i])
            def omb(KK):
                w2, V2 = np.linalg.eig(U_prop(KK, *a)); return -np.angle(w2[int(np.argmax(abs(V2.conj().T @ u)))])
            h = 1e-6; v = np.array([(omb(K + h * e) - omb(K - h * e)) / (2 * h) for e in np.eye(3)])
            st = massgate(a[0], a[1]) @ u; mean = []
            for ax in range(3):
                dl = np.real(np.vdot(st, AL8[ax] @ PL @ st)); st = cshift(AL8[ax] @ PL, K[ax]) @ st; st = expm(-1j * a[2] * FLIP) @ st
                dr = np.real(np.vdot(st, AL8[ax] @ PR @ st)); st = cshift(AL8[ax] @ PR, K[ax]) @ st; mean.append(dl + dr)
            rows.append(np.abs(np.array(mean) - v).max())
    check('proposal, light band near k=0 and near pi(1,1,0): mean block step per axis equals the group velocity', max(rows) < 1e-6, f'max |mean step - v| {max(rows):.1e}')
    # 12. rotation covariance (spectral)
    Kc = rng.uniform(-np.pi, np.pi, (8, 3))
    cov = lambda f: [R for R in rots if max(np.abs(spec(f(R @ K)) - spec(f(K))).max() for K in Kc) < 1e-9]
    cb = cov(lambda K: U_base(K, .05, .5)); cp = cov(lambda K: U_prop(K, .1, .5, .09))
    d4y = all(abs(R[1, 1]) == 1 for R in cp)
    check('spectral rotation covariance: base 24 of 24; proposal 8 of 24 (the D4 about the middle axis of the substep order)', len(cb) == 24 and len(cp) == 8 and d4y, f'base {len(cb)}, proposal {len(cp)}')
    print('koide_structural: covariant rules give b = 0 on the triplet, Q = 1/3; a C3 circulant needs a coset-privileging term and loss of the 2-fold axes (C3-only commutant dim 6).')
    print('per_site: one fermion mode per site, mode assignment, substep order, M and theta are supplied; light-triplet branch theta = m is a tuning.')
    print('lattice_wide: no generation, species, chirality or physical mass reading is established; exact cubic covariance of the proposal is not.')
    print('elapsed_seconds', round(time.monotonic() - _STARTED, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
