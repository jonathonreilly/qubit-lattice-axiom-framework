#!/usr/bin/env python3
"""C10 numeric runner: burn-and-turn (BT) rule vs the C8 metric couplings on the C7 two-qubit walk.

Walk premise (C7 P1-P3) is taken from C8's c8_core.Walk (read-only import); this script builds the
explicit 4x4 matrix U(k) = f + i x.Gamma itself, extracts the hop matrices A_n by an exact 27-point
DFT, and implements the BT rule from its definition (plane_wave_tensors, same formula as the BT
runner). Lattice units a = tau = 1. Pre-registration: ../WORKLOG.md.
"""
from __future__ import annotations
import os, sys, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'C8', 'scripts'))
import c8_core as C8   # noqa: E402  (premise data: parameter points, F, f/h/g symbols)

PASS = FAIL = 0
T0 = time.monotonic()


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


s0 = np.eye(2); s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1.0 + 0j, -1])
GAM = [np.kron(s1, s0), np.kron(s2, s0), np.kron(s3, s1), np.kron(s3, s2), np.kron(s3, s3)]
ALPHA = [-GAM[2 + i] for i in range(3)]
NS = np.array(list(itertools.product((-1, 0, 1), repeat=3)), float)


def plane_wave_tensors(P, dirs, eps):
    """BT rule (verbatim formula of the BT runner): burn, turn tensors and turn action per tick.
    Works for complex weights too (then it is only an algebraic continuation)."""
    P = P / P.sum()
    burn = eps * np.einsum('d,di,dj->ij', P, dirs, dirs)
    turn = np.zeros_like(burn); action = 0.0
    for a in range(len(P)):
        for b in range(len(P)):
            if a != b:
                fl = 2 * eps * P[a] * P[b]; dd = dirs[b] - dirs[a]
                turn = turn - fl * np.outer(dd, dd) / 4; action = action + fl * (dd @ dd) / 4
    return burn, turn, action


class W4:
    def __init__(self, name, theta=0.0, chi=np.pi / 2):
        self.w = C8.Walk(name, theta=theta, chi=chi)
        self.s = self.w.s; self.theta = theta
        g = 2 * np.pi * np.arange(3) / 3
        K = np.array(list(itertools.product(g, g, g)))
        Us = self.U(K)
        # U(k) = sum_n exp(-i k.n) A_n  =>  A_n = (1/27) sum_k exp(+i k.n) U(k)   (exact: degree <= 1 per axis)
        self.A = np.einsum('kn,kij->nij', np.exp(1j * K @ NS.T), Us) / 27

    def U(self, K):
        K = np.atleast_2d(K); u, x = self.w.sym(K)
        f = 1 - u
        return f[:, None, None] * np.eye(4)[None] + 1j * np.einsum('na,aij->nij', x, np.array(GAM))

    def Urec(self, K):
        return np.einsum('kn,nij->kij', np.exp(-1j * np.atleast_2d(K) @ NS.T), self.A)

    def band(self, k):
        """upper band (U eigenvalue exp(-i omega), omega = arccos f in (0, pi)): omega, orthonormal basis (4x2)."""
        u, x, df, dx = self.w.sym(np.atleast_2d(k), deriv=True)
        u, x, df = u[0], x[0], df[0]
        f = 1 - u; om = np.arccos(f); X = np.einsum('a,aij->ij', x, np.array(GAM))
        Pi = (np.eye(4) - X / np.linalg.norm(x)) / 2
        ev, V = np.linalg.eigh(Pi); B = V[:, ev > 0.5]
        v = -df / np.sin(om)                        # group velocity d omega / dk (cos omega = f)
        return om, B, v, x, f


def couplings(W, k):
    om, B, v, x, f = W.band(k)
    g = x[2:]; sx = np.linalg.norm(x); rho = om / sx
    al = np.array([np.real(np.trace(B.conj().T @ A @ B)) / 2 for A in ALPHA])   # band average of <alpha_i>
    sym = lambda a, b: (np.outer(a, b) + np.outer(b, a)) / 2
    T = {'M1': sym(al, rho * g), 'M2': sym(al, g), 'M3': sym(al, W.s * np.sin(k)), 'M4': sym(v, np.sin(k))}
    return om, B, v, x, al, T


def odds(W, k, u):
    om, B, v, x, f = W.band(k)
    PK = np.array([np.linalg.norm(A @ u) ** 2 for A in W.A]).real
    PW = np.exp(1j * om) * np.exp(-1j * NS @ k) * np.array([u.conj() @ A @ u for A in W.A])
    return om, v, PK, PW


def bloch(B, th, ph):
    return B @ np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def main():
    rng = np.random.default_rng(10)
    DIRS = {'100': (1, 0, 0), '110': (1, 1, 0), '111': (1, 1, 1), '123': (1, 2, 3)}
    KS = (0.05, 0.2, 0.5)
    NAMES = ('bstar', 'iso', 'gold')
    # ------------------------------------------------------------------ BT reduction check on BT's own walks
    th1 = 0.05; c1, sn1 = np.cos(th1), np.sin(th1)
    C1 = np.array([[c1, -1j * sn1], [-1j * sn1, c1]])
    th = 0.3
    E6 = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)], float)
    R6 = np.array([[1.0 if np.allclose(a, -b) else 0 for b in E6] for a in E6]); P6 = np.array([[1.0 if abs(a @ b) < 1e-9 else 0 for b in E6] for a in E6])
    C6 = expm(-1j * th * (R6 - P6 + 2 * np.eye(6)))
    errs = []
    for dirs, C, k in ((np.array([[1.0], [-1.0]]), C1, np.array([0.06])), (E6, C6, 0.3 * np.array([1, 1, 0]) / np.sqrt(2))):
        U = np.diag(np.exp(-1j * dirs @ k)) @ C; w, V = np.linalg.eig(U)
        for i in range(len(w)):
            u = V[:, i] / np.linalg.norm(V[:, i]); om = -np.angle(w[i])
            A = [np.exp(0) * np.outer(np.eye(len(dirs))[d], np.eye(len(dirs))[d]) @ C for d in range(len(dirs))]  # A_d = Pi_d C
            PK = np.array([np.linalg.norm(Ad @ u) ** 2 for Ad in A]); PW = np.exp(1j * om) * np.exp(-1j * dirs @ k) * np.array([u.conj() @ Ad @ u for Ad in A])
            errs.append(max(abs(PK - abs(u) ** 2).max(), abs(PW - abs(u) ** 2).max()))
    check('extensions E-K and E-W reduce to the BT Born odds |u_d|^2 on BT\'s 1D and six-direction walks (all bands)',
          max(errs) < 1e-12, f'max dev {max(errs):.1e}')
    # ------------------------------------------------------------------ Step 0: domain test
    for name in NAMES:
        for theta, chi in ((0.0, np.pi / 2), (0.2, 0.0)):
            W = W4(name, theta, chi)
            K = rng.uniform(-np.pi, np.pi, (20, 3))
            rec = abs(W.Urec(K) - W.U(K)).max(); uni = abs(np.einsum('kij,kil->kjl', W.U(K).conj(), W.U(K)) - np.eye(4)).max()
            kraus = abs(np.einsum('nij,nil->jl', W.A.conj(), W.A) - np.eye(4)).max()
            nz = [i for i in range(27) if abs(W.A[i]).max() > 1e-12]
            ov = max(abs(W.A[i] @ W.A[j].conj().T).max() for i in nz for j in nz if i != j)
            ranks = [np.linalg.matrix_rank(W.A[i], 1e-10) for i in nz]
            check(f'[{name}, theta={theta}] hop decomposition exact, unitary, sum A^dag A = 1', max(rec, uni, kraus) < 1e-12,
                  f'rec {rec:.1e}, unitarity {uni:.1e}, Kraus {kraus:.1e}')
            check(f'[{name}, theta={theta}] NOT in the BT domain: {len(nz)} nonzero hops (> dim 4), ranks sum {sum(ranks)} > 4, '
                  f'max |A_n A_m^dag| (n != m) = {ov:.3f} != 0', len(nz) > 4 and ov > 1e-3 and sum(ranks) > 4,
                  'shift-coin form needs <= 4 unit-length hops with orthogonal ranges (ranks sum to 4)')
    # ------------------------------------------------------------------ plane-wave comparisons
    rows = []
    for name in NAMES:
        for theta, chi in ((0.0, np.pi / 2), (0.2, 0.0), (0.2, np.pi / 2)):
            W = W4(name, theta, chi)
            for dn, d in DIRS.items():
                for kk in KS:
                    k = kk * np.array(d, float) / np.linalg.norm(d)
                    om, B, v, x, al, T = couplings(W, k)
                    # checks of the closed forms
                    ag = x[2:] / np.linalg.norm(x)
                    h = 1e-6; vfd = np.array([(W.band(k + h * e)[0] - W.band(k - h * e)[0]) / (2 * h) for e in np.eye(3)])
                    # alpha expectation for every u in band (not just average)
                    devs_al = []; KR = []; WV = []; imW = 0.0; negW = 0.0; negK = 0.0
                    for tb in np.linspace(0, np.pi, 7):
                        for pb in np.linspace(0, 2 * np.pi, 8, endpoint=False):
                            u = bloch(B, tb, pb)
                            devs_al.append(abs(np.array([np.real(u.conj() @ A @ u) for A in ALPHA]) - ag).max())
                            _, _, PK, PW = odds(W, k, u)
                            bK, tK, aK = plane_wave_tensors(PK, NS, om); bW, tW, aW = plane_wave_tensors(PW, NS, om)
                            mK = PK @ NS; mW = PW @ NS
                            KR.append((bK + tK, mK, aK, PK)); WV.append((bW + tW, mW, aW, PW))
                            imW = max(imW, abs(PW.imag).max()); negW = min(negW, PW.real.min()); negK = min(negK, PK.min())
                    rows.append(dict(name=name, theta=theta, chi=chi, d=dn, k=kk, om=om, v=v, vfd=vfd, s=W.s, T=T,
                                     al_dev=max(devs_al), KR=KR, WV=WV, imW=imW, negW=negW, negK=negK))
    # closed-form checks
    check('group velocity -grad f / sin(omega) matches eigenphase finite differences (all points)',
          max(abs(r['v'] - r['vfd']).max() for r in rows) < 1e-7, f"max {max(abs(r['v'] - r['vfd']).max() for r in rows):.1e}")
    check('<alpha_i> = g_i/|x| for EVERY vector in the degenerate upper band (coupling tensors are band-independent)',
          max(r['al_dev'] for r in rows) < 1e-12, f"max {max(r['al_dev'] for r in rows):.1e}")
    # BT algebraic identity under both extensions
    idK = max(abs(T - r['om'] * np.outer(m, m)).max() for r in rows for (T, m, a, P) in r['KR'])
    idW = max(abs(T - r['om'] * np.outer(m, m)).max() for r in rows for (T, m, a, P) in r['WV'])
    check('burns + turns = eps m m (m = mean step) for E-K and E-W odds at every point and band vector', max(idK, idW) < 1e-12,
          f'E-K {idK:.1e}, E-W {idW:.1e}')
    mW = max(abs(m - r['v']).max() for r in rows for (T, m, a, P) in r['WV'])
    check('E-W: mean step = group velocity exactly (every band vector) => T^BT,W = eps v v', mW < 1e-12, f'max {mW:.1e}')
    print('   E-W weights: max |Im w_n| per row group, min Re w_n:')
    for name in NAMES:
        sel = [r for r in rows if r['name'] == name]
        print(f'     {name}: max|Im w| {max(r["imW"] for r in sel):.3e}, min Re w {min(r["negW"] for r in sel):.3e}, '
              f'min E-K P {min(r["negK"] for r in sel):.1e}')
    imax = max(r['imW'] for r in rows); nmin = min(r['negW'] for r in rows)
    check('E-W weights are NOT a front distribution (complex or negative somewhere): BT flows 2 eps w w\'/rho are then not flows',
          imax > 1e-6 or nmin < -1e-6, f'max |Im w| {imax:.3e}, min Re w {nmin:.3e}')
    # E-K: mean step vs group velocity
    print('   E-K: mean step m (range over band) vs v:')
    worstK = 0.0
    for r in rows:
        ms = np.array([m for (T, m, a, P) in r['KR']])
        rel = np.max(np.linalg.norm(ms - r['v'], axis=1)) / np.linalg.norm(r['v'])
        relmin = np.min(np.linalg.norm(ms - r['v'], axis=1)) / np.linalg.norm(r['v'])
        r['K_rel'] = (relmin, rel); worstK = max(worstK, relmin)
        if r['k'] == 0.2 and r['d'] in ('100', '111'):
            print(f"     {r['name']:5s} th={r['theta']} chi={r['chi']:.2f} k||{r['d']} |k|={r['k']}: |v| {np.linalg.norm(r['v']):.4f}, "
                  f"|m| in [{np.linalg.norm(ms, axis=1).min():.4f}, {np.linalg.norm(ms, axis=1).max():.4f}], rel |m-v| in [{relmin:.3f}, {rel:.3f}]")
    check('E-K: mean step differs from the group velocity for every band vector (min rel. dev. > 1% at every point)',
          min(r['K_rel'][0] for r in rows) > 0.01, f"min over points of (min over band) {min(r['K_rel'][0] for r in rows):.3f}")
    # ------------------------------------------------------------------ C-exact: T^BT,W vs couplings
    print('   C-exact: max_ij |T^BT,W - T^X| / max|T^X|  (as given)  and after the continuum constant 1/s^2 (shape):')
    exact = {}
    for X in ('M1', 'M2', 'M3', 'M4'):
        dg = []; ds = []
        for r in rows:
            TB = r['om'] * np.outer(r['v'], r['v']); TX = r['T'][X]
            dg.append(abs(TB - TX).max() / abs(TX).max()); ds.append(abs(TB / r['s'] ** 2 - TX).max() / abs(TX).max())
        exact[X] = (min(dg), max(dg), min(ds), max(ds))
        print(f'     {X}: as given rel dev in [{min(dg):.3e}, {max(dg):.3e}];  shape (BT/s^2) rel dev in [{min(ds):.3e}, {max(ds):.3e}]')
    check('C-exact: no coupling equals T^BT,W on the whole declared momentum set (as given or up to 1/s^2)',
          all(exact[X][1] > 1e-3 and exact[X][3] > 1e-3 for X in exact),
          '; '.join(f'{X} max as-given {exact[X][1]:.2e}, max shape {exact[X][3]:.2e}' for X in exact))
    # massless, k on a lattice axis: f(t,0,0) = (Gphi0).(v + w cos t), D = s^2 sin t, g = s sin t  => T^BT,W = s^2 T^M1 exactly
    ax = [r for r in rows if r['theta'] == 0 and r['d'] == '100']
    dax = max(abs(r['om'] * np.outer(r['v'], r['v']) / r['s'] ** 2 - r['T']['M1']).max() / abs(r['T']['M1']).max() for r in ax)
    check('massless, k on an axis, all three points: T^BT,W = s^2 T^M1 exactly (E3 with x2 = x3 = 0)', dax < 1e-12, f'max rel {dax:.1e}')
    # ------------------------------------------------------------------ E4 cross-check (matrix route vs closed form)
    e4 = 0.0
    for name in NAMES:
        for theta, chi in ((0.0, np.pi / 2), (0.2, 0.0), (0.2, np.pi / 2), (0.3, 1.0)):
            W = W4(name, theta, chi); hh = np.array([np.cos(chi), np.sin(chi)]); cv = hh @ W.w.F[1:]; hW = hh @ W.w.W
            b0, b1, b2 = W.w.b; s = W.s
            beta = -s * (b0 - b1 - 2 * b2) / 3; Cc = -3 * b0 * b1 + 2 * b0 * b2 - 3 * b1 ** 2 + 7 * b1 * b2 + 5 * b2 ** 2
            lam = np.cos(theta) - np.sin(theta) * hW / s ** 2
            E1 = -3 * beta * np.cos(theta) + np.sin(theta) * (cv[2] + cv[3]) - np.sin(theta) * hW * (b1 + b2) / s
            E2 = Cc * np.cos(theta) - np.sin(theta) * cv[3] + np.sin(theta) * hW * b2 / s
            for _ in range(5):
                k = rng.uniform(-1.2, 1.2, 3)
                om, B, v, x, f = W.band(k)
                h = 1e-6; vfd = np.array([(W.band(k + h * e)[0] - W.band(k - h * e)[0]) / (2 * h) for e in np.eye(3)])
                Dm = vfd * np.sin(om); xx = 1 - np.cos(k)
                pred = np.array([lam * s * x[2 + a] + np.sin(k[a]) * (E1 * (xx[(a + 1) % 3] + xx[(a + 2) % 3]) + E2 * xx[(a + 1) % 3] * xx[(a + 2) % 3]) for a in range(3)])
                e4 = max(e4, abs(Dm - pred).max())
    check('E4 closed form D_theta = lam s g + sin k [E1 (x+x) + E2 x x] reproduced by eigenphase finite differences of the explicit 4x4 U',
          e4 < 1e-8, f'max abs dev {e4:.1e} (random k, 3 points x 4 mass settings)')
    # ------------------------------------------------------------------ continuum and O(a^2) scaling (numerical)
    print('   scaling: k = kappa n, theta = kappa mu; D_X = max_ij |T^BT/c - T^X| / max|T^X|, c = s^2 (registered) or lam^2 s^2 (secondary);')
    print('   slope = d log D / d log kappa on kappa in {0.08, 0.04, 0.02, 0.01}')
    scal = {}
    kap = np.array([0.08, 0.04, 0.02, 0.01])
    for name in NAMES:
        for mu, chi in ((0.0, np.pi / 2), (1.0, 0.0), (1.0, np.pi / 2)):
            for dn in ('100', '111', '123'):
                d = np.array(DIRS[dn], float); d /= np.linalg.norm(d)
                D = {X: [] for X in ('M1', 'M2', 'M3', 'M4')}; DL = {X: [] for X in D}; Dg = {X: [] for X in D}
                for kp in kap:
                    W = W4(name, mu * kp, chi); hh = np.array([np.cos(chi), np.sin(chi)])
                    lam = np.cos(mu * kp) - np.sin(mu * kp) * (hh @ W.w.W) / W.s ** 2
                    om, B, v, x, al, T = couplings(W, kp * d)
                    TB = om * np.outer(v, v)
                    for X in D:
                        nrm = abs(T[X]).max()
                        D[X].append(abs(TB / W.s ** 2 - T[X]).max() / nrm); DL[X].append(abs(TB / (lam * W.s) ** 2 - T[X]).max() / nrm)
                        Dg[X].append(abs(TB - T[X]).max() / nrm)
                for X in D:
                    sl = np.polyfit(np.log(kap), np.log(np.array(D[X]) + 1e-300), 1)[0]
                    slL = np.polyfit(np.log(kap), np.log(np.array(DL[X]) + 1e-300), 1)[0]
                    scal[(name, mu, chi, dn, X)] = (D[X][-1], sl, Dg[X][-1], DL[X][-1], slL)
    for name in NAMES:
        for mu, chi in ((0.0, np.pi / 2), (1.0, 0.0), (1.0, np.pi / 2)):
            print(f'     {name:5s} mu={mu} chi={chi:.2f}:')
            for X in ('M1', 'M2', 'M3', 'M4'):
                print('        ' + X + ': ' + '; '.join(f"{dn}: D {scal[(name, mu, chi, dn, X)][0]:.2e} sl {scal[(name, mu, chi, dn, X)][1]:.2f} | lam: D {scal[(name, mu, chi, dn, X)][3]:.2e} sl {scal[(name, mu, chi, dn, X)][4]:.2f}"
                                         for dn in ('100', '111', '123')))
    asgiven = {name: max(scal[(name, 0.0, np.pi / 2, dn, 'M1')][2] for dn in ('100', '111', '123')) for name in NAMES}
    sv = {name: W4(name).s for name in NAMES}
    check('C-cont as given: T^BT,W = s^2 T^X at continuum order (rel dev -> 1 - s^2: b* 0.164, b_iso 1/3; b_gold -> 0)',
          all(abs(asgiven[n] - (1 - sv[n] ** 2)) < 2e-3 for n in ('bstar', 'iso')) and asgiven['gold'] < 1e-3,
          '; '.join(f'{n}: dev {asgiven[n]:.4f} vs 1-s^2 {1 - sv[n] ** 2:.4f}' for n in NAMES))
    m0 = [scal[k][0] for k in scal if k[1] == 0.0 or k[2] == np.pi / 2 or k[0] == 'gold']
    check('C-cont shape: every coupling agrees with T^BT,W/s^2 at continuum order (massless, maximal twist, and b_gold: D -> 0)',
          max(m0) < 1e-3, f'max D at kappa = .01: {max(m0):.2e}')
    off = ('111', '123')
    slM1 = [scal[('bstar', 0.0, np.pi / 2, dn, 'M1')][1] for dn in off] + [scal[('gold', 0.0, np.pi / 2, dn, 'M1')][1] for dn in off]
    check('C-a2 massless, b* and b_gold, off-axis: M1 mismatch is O(a^2) (slope in [1.9, 2.1]; E5c: coefficient 3 beta n1^2(n2^2+n3^2) ...)',
          min(slM1) > 1.9 and max(slM1) < 2.1, f'slopes {min(slM1):.3f}..{max(slM1):.3f}')
    isoM1 = [scal[('iso', 0.0, np.pi / 2, dn, 'M1')] for dn in off]
    check('C-a2 massless, b_iso, off-axis: M1 agrees through O(a^2); first mismatch O(a^4) (slope in [3.8, 4.2])',
          all(3.8 < v[1] < 4.2 for v in isoM1), '; '.join(f'D(.01) {v[0]:.2e} slope {v[1]:.3f}' for v in isoM1))
    sl234 = [scal[(n, 0.0, np.pi / 2, '123', X)][1] for n in NAMES for X in ('M2', 'M3', 'M4')]
    check('C-a2 massless, all three points, generic direction (123): M2, M3, M4 mismatch at O(a^2) (slopes in [1.9, 2.1])',
          min(sl234) > 1.9 and max(sl234) < 2.1, f'slopes {min(sl234):.3f}..{max(sl234):.3f}')
    sl1 = [scal[k][1] for k in scal if k[1] == 1.0 and k[2] == 0.0 and k[0] != 'gold']
    check('massive Wilson-aligned (b*, b_iso), registered constant s^2: every coupling mismatches already at O(a) (slopes in [0.9, 1.1])',
          min(sl1) > 0.9 and max(sl1) < 1.1, f'slopes {min(sl1):.3f}..{max(sl1):.3f}')
    slm2 = [scal[k][1] for k in scal if k[1] == 1.0 and (k[2] == np.pi / 2 or k[0] == 'gold')]
    check('massive maximal twist (and b_gold), registered constant s^2: every coupling mismatches at O(a^2) (slopes in [1.9, 2.1])',
          min(slm2) > 1.9 and max(slm2) < 2.1, f'slopes {min(slm2):.3f}..{max(slm2):.3f}')
    d111 = [scal[('iso', 0.0, np.pi / 2, '111', X)][1] for X in ('M3', 'M4')]
    check('non-generic: at b_iso along (111) M3 and M4 also agree through O(a^2) (slopes ~4); M2 does not (slope 2)',
          all(3.8 < v < 4.2 for v in d111) and 1.9 < scal[('iso', 0.0, np.pi / 2, '111', 'M2')][1] < 2.1, f'M3, M4 slopes {d111[0]:.2f}, {d111[1]:.2f}')
    isoL = [scal[('iso', 1.0, chi, dn, 'M1')][4] for chi in (0.0, np.pi / 2) for dn in off]
    othL = [scal[('iso', 1.0, chi, dn, X)][4] for chi in (0.0, np.pi / 2) for dn in off for X in ('M2', 'M3', 'M4')]
    check('secondary (mass-dependent constant lam^2 s^2, labelled): at b_iso M1 then mismatches only at O(a^3) (Wilson-aligned) or O(a^4) (maximal twist), M2-M4 at O(a^2) or O(a)',
          all(2.8 < v for v in isoL) and max(othL) < 2.1, f'M1 slopes {min(isoL):.2f}..{max(isoL):.2f}; M2-M4 max slope {max(othL):.2f}')
    # ------------------------------------------------------------------ clock
    print('   clock: turn action per tick, E-K [range over band] and E-W (band average), vs m^2/eps = theta^2/omega and the c = s form omega(1 - v^2/s^2)')
    cl = []
    for name in NAMES:
        for theta, chi in ((0.2, 0.0), (0.2, np.pi / 2), (0.05, np.pi / 2)):
            W = W4(name, theta, chi); hW = np.array([np.cos(chi), np.sin(chi)]) @ W.w.W
            for dn in ('100', '111'):
                for kk in (0.0, 0.05, 0.2):
                    d = np.array(DIRS[dn], float) / np.linalg.norm(DIRS[dn]); k = kk * d
                    om, B, v, x, f = W.band(k)
                    aK = []; aW = []; n2K = []; n2W = []
                    for tb in np.linspace(0, np.pi, 7):
                        for pb in np.linspace(0, 2 * np.pi, 8, endpoint=False):
                            u = bloch(B, tb, pb); _, _, PK, PW = odds(W, k, u)
                            aK.append(plane_wave_tensors(PK, NS, om)[2]); aW.append(plane_wave_tensors(PW, NS, om)[2])
                            n2K.append(PK @ np.sum(NS ** 2, 1)); n2W.append(PW @ np.sum(NS ** 2, 1))
                    cl.append(dict(name=name, theta=theta, chi=chi, d=dn, k=kk, aK=(min(aK), max(aK)), aW=np.mean(aW), aWspread=np.ptp(np.real(aW)) + np.ptp(np.imag(aW)),
                                   mg=theta ** 2 / om, rel=om * (1 - v @ v / W.s ** 2), n2K=(min(n2K), max(n2K)), n2W=np.mean(n2W), pred=3 * W.s ** 2 - 3j * hW, s=W.s))
    for c in cl:
        if c['k'] in (0.0, 0.2):
            print(f"     {c['name']:5s} th={c['theta']} chi={c['chi']:.2f} k||{c['d']} |k|={c['k']}: E-K action [{c['aK'][0]:.4f},{c['aK'][1]:.4f}] "
                  f"(<|n|^2> [{c['n2K'][0]:.4f},{c['n2K'][1]:.4f}]), E-W action {np.real(c['aW']):+.4f}{np.imag(c['aW']):+.4f}i, "
                  f"m^2/eps {c['mg']:.4f}, eps(1-v^2/s^2) {c['rel']:.4f}")
    rest = [c for c in cl if c['k'] == 0.0]
    rK = [c['aK'][0] / c['theta'] for c in rest] + [c['aK'][1] / c['theta'] for c in rest]
    check('clock at rest, E-K: action/theta = <|n|^2>_K (band- and theta-independent) is 0.52-0.64, not 1: m^2/eps fails by > 30% at k = 0',
          max(abs(r - 1) for r in rK) < 0.5 and min(abs(r - 1) for r in rK) > 0.3, f'action/(m^2/eps) at rest in [{min(rK):.4f}, {max(rK):.4f}]')
    eW = max(abs(c['n2W'] - c['pred']) for c in rest)
    check('clock at rest, E-W: sum_n |n|^2 w_n = 3 s^2 - 3 i hhat.W (E6), so action = theta (3 s^2 - 3 i hhat.W) != theta unless 3 s^2 = 1 and hhat.W = 0',
          eW < 1e-10 and min(abs(c['aW'] / c['theta'] - 1) for c in rest) > 0.5, f'max dev from E6 {eW:.1e}')
    trend = all(c2['aK'][0] > c1['aK'][1] and np.real(c2['aW']) > np.real(c1['aW']) and c2['mg'] < c1['mg']
                for c1 in rest for c2 in cl if c2['k'] == 0.2 and (c2['name'], c2['theta'], c2['chi'], c2['d']) == (c1['name'], c1['theta'], c1['chi'], c1['d']))
    check('clock trend: from k = 0 to |k| = 0.2 the turn action RISES (both extensions) while m^2/eps falls: no clock even up to a constant', trend)
    aniso = [(c['name'], c['theta'], c['chi'], abs(np.mean(c['aK']) - np.mean(c2['aK'])) / np.mean(c['aK'])) for c in cl for c2 in cl
             if c['k'] == 0.2 and c2['k'] == 0.2 and c['d'] == '100' and c2['d'] == '111' and (c['name'], c['theta'], c['chi']) == (c2['name'], c2['theta'], c2['chi'])]
    print('   clock direction dependence (E-K band-mid action, (100) vs (111), |k| = 0.2): ' + '; '.join(f'{a[0]} th={a[1]} chi={a[2]:.2f}: {a[3]:.2e}' for a in aniso))
    print('per_site: walk family, points, theta, chi are C7 premises; E-K and E-W odds are declared extensions of BT.')
    print('elapsed_seconds', round(time.monotonic() - T0, 1))
    print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')


if __name__ == '__main__':
    main()
