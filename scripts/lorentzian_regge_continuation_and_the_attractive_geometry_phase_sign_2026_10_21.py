#!/usr/bin/env python3
"""Finite Lorentzian Regge continuation diagnostics on two supplied carriers.
Track square-root branches at 600 phi samples; evaluate endpoint area/angle
DERIVATIVES, Schlaefli residuals and continued quadratic kernels. No absolute
dihedral/deficit branches or full nonlinear real action are constructed.
Two momentum scales yield sampled Richardson ratios against a supplied
Einstein-Hilbert quadratic comparator, not a continuum or alpha->1 theorem.
Causal hinge type comes from its induced metric: negative determinant is
timelike, positive definite is spacelike; tick components do not decide it.
Source/action choices are supplied: P=-S and
S_total=-sigma*kappa*S_L-E integral d tau, E,kappa>0, with the stated metric
reading. S_L here denotes the candidate action whose quadratic kernel is used.
Static response and TT quadratic signs reverse with sigma; gamma is unchanged.
An attractive-gravity comparison selects sigma=-1 only within those choices.
No binary-pulsar decay, light-deflection trajectory or physical law is derived.
G=a^2/(8*pi*kappa) additionally assumes the continuum EH/2 matching condition.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/LORENTZIAN_REGGE_CONTINUATION_AND_THE_ATTRACTIVE_GEOMETRY_PHASE_SIGN_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md',
                     'scripts/scale_ladder_gravity_d4_cone_common_cone_spins_zero_one_two_2026_10_18.py')

import itertools, os, sys, time, signal
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
_T0 = time.monotonic()
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
if not __debug__: raise RuntimeError('Optimized Python is unsupported')

PASS = FAIL = 0
HC = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
T = 3                                   # supplied tick index; HC position 3 is h_tt
PAIRS5 = list(itertools.combinations(range(5), 2))
TRIS5 = list(itertools.combinations(range(5), 3))
B5 = np.vstack([-np.ones(4), np.eye(4)])  # barycentric gradients from the dual basis


def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))


# ---------------------------------------------------------------- carriers (combinatorics as in the repo D4 code)
def kuhn():
    E = np.eye(4, dtype=int); sims = []
    for perm in itertools.permutations(range(4)):
        p = np.zeros(4, int); vs = [(tuple(p), 0)]
        for a in perm: p = p + E[a]; vs.append((tuple(p), 0))
        sims.append(vs)
    return [np.zeros(4)], sims


def d4cone():
    pairs = list(itertools.combinations(range(4), 2))
    OFF = [np.zeros(4), 0.5 * np.ones(4)] + [0.5 * (np.eye(4)[m] + np.eye(4)[n]) for m, n in pairs]
    def asv(p):
        if np.allclose(p, np.round(p)): return (tuple(int(x) for x in np.round(p)), 0)
        q = p - 0.5; return (tuple(int(x) for x in np.round(q)), 1)
    sims = []
    for h, (m, n) in enumerate(pairs):
        r, s = [i for i in range(4) if i not in (m, n)]; c = OFF[2 + h]; E = np.eye(4)
        axes = [0.5 * (E[m] + E[n]), 0.5 * (E[m] - E[n]), 0.5 * (E[r] + E[s]), 0.5 * (E[r] - E[s])]
        for sg in itertools.product([1, -1], repeat=4):
            sims.append([((0, 0, 0, 0), 2 + h)] + [asv(c + a * x) for a, x in zip(sg, axes)])
    return OFF, sims


def kpair(v1, v2):
    (b1, t1), (b2, t2) = v1, v2
    if (t1, b1) > (t2, b2): (b1, t1), (b2, t2) = (b2, t2), (b1, t1)
    return (t1, t2, tuple(np.subtract(b2, b1))), tuple(b1)


def ktri(vs):
    vs = sorted(vs, key=lambda v: (v[1], v[0])); b0 = vs[0][0]
    return tuple((t, tuple(np.subtract(b, b0))) for b, t in vs), tuple(b0)


class Carrier:
    def __init__(self, OFF, sims):
        self.OFF = [np.array(o, float) for o in OFF]; self.sims = sims
        self.ekey = {}
        for s in sims:
            for i, j in PAIRS5: self.ekey.setdefault(kpair(s[i], s[j])[0], len(self.ekey))
        self.E = len(self.ekey); self.V = np.zeros((self.E, 4)); self.O = np.zeros((self.E, 4))
        for (t1, t2, rel), c in self.ekey.items():
            self.V[c] = np.array(rel, float) + self.OFF[t2] - self.OFF[t1]; self.O[c] = self.OFF[t1]
        self.stars, self.hv = {}, {}
        for si, s in enumerate(sims):
            for ti, tri in enumerate(TRIS5):
                key, anc = ktri([s[i] for i in tri]); Tr = -np.array(anc)
                self.stars.setdefault(key, []).append((si, Tr, ti))
                self.hv.setdefault(key, [(tuple(np.add(s[i][0], Tr)), s[i][1]) for i in tri])
        self.hkeys = list(self.stars)
        self.P = np.array([[np.array(v[0], float) + self.OFF[v[1]] for v in s] for s in sims])   # (S,5,4)
        self.HP = np.array([[np.array(v[0], float) + self.OFF[v[1]] for v in self.hv[k]] for k in self.hkeys])

    # ---- geometry at metric g (complex allowed), principal branches; tracking is done by the caller
    def raw(self, g):
        Ed = self.P[:, 1:] - self.P[:, :1]; Gam = np.einsum('sai,ij,sbj->sab', Ed, g, Ed)
        Gi = np.linalg.inv(Gam); W = B5 @ Gi @ B5.T                                  # (S,5,5)
        R2 = np.zeros((len(self.P), 10), complex)
        for ti, tri in enumerate(TRIS5):
            m, n = [i for i in range(5) if i not in tri]
            R2[:, ti] = W[:, m, m] * W[:, n, n] - W[:, m, n] ** 2
        hE = self.HP[:, 1:] - self.HP[:, :1]; Dh = np.linalg.det(np.einsum('hai,ij,hbj->hab', hE, g, hE))
        return Gam, Gi, W, R2, Dh, np.linalg.det(Gam)

    def continue_to(self, alpha, phi_end, n=600):
        """Track nearest square-root branches at n sampled phi values; derivatives are evaluated only at the endpoint."""
        prev = None
        for phi in np.linspace(0, phi_end, n):
            g = np.diag([1, 1, 1, alpha * np.exp(1j * phi)]).astype(complex)
            Gam, Gi, W, R2, Dh, dG = self.raw(g); cur = [np.sqrt(R2), np.sqrt(Dh), np.sqrt(dG)]
            if prev is not None:
                cur = [np.where(abs(c - p) <= abs(-c - p), c, -c) for c, p in zip(cur, prev)]
            prev = cur
        self.g = g; self.Gam, self.Gi, self.W = Gam, Gi, W; self.R, self.sD, self.sdet = prev
        self._coeffs()

    def _coeffs(self):
        S = len(self.P); Gi, W = self.Gi, self.W
        dG = np.zeros((10, 4, 4))                    # dGamma / ds_ij for the 10 local pairs
        for p, (i, j) in enumerate(PAIRS5):
            if i == 0:
                a = j - 1; dG[p, a, :] += .5; dG[p, :, a] += .5
            else:
                dG[p, i - 1, j - 1] -= .5; dG[p, j - 1, i - 1] -= .5
        dW = -np.einsum('ab,sbc,pcd,sde,fe->spaf', B5, Gi, dG, Gi, B5)                  # (S,10,5,5)
        self.dth = np.zeros((S, 10, 10), complex)                                        # [simplex, hinge, pair]
        for ti, tri in enumerate(TRIS5):
            m, n = [i for i in range(5) if i not in tri]
            Wmn, Wmm, Wnn = W[:, m, n], W[:, m, m], W[:, n, n]
            num = dW[:, :, m, n] - 0.5 * Wmn[:, None] * (dW[:, :, m, m] / Wmm[:, None] + dW[:, :, n, n] / Wnn[:, None])
            self.dth[:, ti] = num / self.R[:, ti][:, None]
        # hinge area gradients wrt its three squared lengths (pairs (0,1),(0,2),(1,2))
        hE = self.HP[:, 1:] - self.HP[:, :1]; G2 = np.einsum('hai,ij,hbj->hab', hE, self.g, hE)
        a, b = G2[:, 0, 0], G2[:, 1, 1]; c = a + b - 2 * G2[:, 0, 1]
        dD = np.stack([(b - a + c) / 2, (a - b + c) / 2, (a + b - c) / 2], 1)
        self.dA = dD / (4 * self.sD[:, None]); self.A = 0.5 * self.sD
        self.hinge_tl = np.array([np.real(np.linalg.det(G2[h])) < 0 for h in range(len(G2))])
        self._terms()

    def _terms(self):
        self.terms = []
        for h, key in enumerate(self.hkeys):
            hv = self.hv[key]; at = []
            for n, (i, j) in enumerate([(0, 1), (0, 2), (1, 2)]):
                c, anc = kpair(hv[i], hv[j]); at.append((self.ekey[c], np.array(anc, float), self.dA[h, n]))
            dt = []
            for si, Tr, ti in self.stars[key]:
                vs = [(tuple(np.add(v[0], Tr)), v[1]) for v in self.sims[si]]
                for p, (i, j) in enumerate(PAIRS5):
                    c, anc = kpair(vs[i], vs[j]); dt.append((self.ekey[c], np.array(anc, float), -self.dth[si, ti, p]))
            pk = lambda tl: (np.array([t[0] for t in tl]), np.array([t[1] for t in tl]), np.array([t[2] for t in tl]))
            self.terms.append((pk(at), pk(dt)))

    def schlaefli(self):
        """max_s |sum_h A_h dtheta_h/ds| / max|A dtheta| per simplex (continued branches)."""
        worst = 0.0
        for si, s in enumerate(self.sims):
            acc = np.zeros(10, complex); scale = 0.0
            for ti, tri in enumerate(TRIS5):
                key, anc = ktri([s[i] for i in tri]); h = self.hkeys.index(key)
                acc += self.A[h] * self.dth[si, ti]; scale = max(scale, np.max(abs(self.A[h] * self.dth[si, ti])))
            worst = max(worst, np.max(abs(acc)) / scale)
        return worst

    def M(self, ks):
        """delta s_e = line integral of h along edge e: (K,E,10)."""
        z = ks @ self.V.T; zs = np.where(abs(z) < 1e-14, 1.0, z)
        ph = np.where(abs(z) < 1e-14, 1.0, (np.exp(1j * z) - 1) / (1j * zs)) * np.exp(1j * ks @ self.O.T)
        Wv = np.array([[v[a] * v[b] * (2 if a != b else 1) for a, b in HC] for v in self.V])
        return ph[:, :, None] * Wv[None]

    def K(self, ks, sel=None):
        """Continued Bloch kernel, analytic in the coefficients: K(k) = M(-k)^T Q(k) M(k)."""
        ks = np.atleast_2d(np.asarray(ks, float)); Mp, Mm = self.M(ks), self.M(-ks); out = np.zeros((len(ks), 10, 10), complex)
        for h, (a, d) in enumerate(self.terms):
            if sel is not None and not sel[h]: continue
            rap, rdp = (np.einsum('ke,kej->kj', self._row(t, ks), Mp) for t in (a, d))
            ram, rdm = (np.einsum('ke,kej->kj', self._row(t, -ks), Mm) for t in (a, d))
            out += 0.5 * (ram[:, :, None] * rdp[:, None, :] + rdm[:, :, None] * rap[:, None, :])
        return out

    def _row(self, t, ks):
        idx, anc, w = t; r = np.zeros((len(ks), self.E), complex); ph = np.exp(1j * ks @ anc.T) * w[None]
        for n in range(len(idx)): r[:, idx[n]] += ph[:, n]
        return r


def Fcont(k, g, sq):
    """(1/2)H^T F H = cell average of sqrt(det g) R_2 for h = Re(H e^{ikx}) on flat background g; sq = sqrt(det g)."""
    gi = np.linalg.inv(g); ku = gi @ k; k2 = k @ ku; F = np.zeros((10, 10), complex); I = np.eye(10)
    def mat(Hv):
        Hm = np.zeros((4, 4))
        for j, (a, b) in enumerate(HC): Hm[a, b] = Hm[b, a] = Hv[j]
        return Hm
    for i in range(10):
        for j in range(10):
            A, Bm = mat(I[i]), mat(I[j])
            AB = np.trace(gi @ A @ gi @ Bm); trA, trB = np.trace(gi @ A), np.trace(gi @ Bm)
            F[i, j] = (-0.25 * k2 * AB + 0.5 * (ku @ A) @ gi @ (Bm @ ku) - 0.25 * ((ku @ A @ ku) * trB + trA * (ku @ Bm @ ku))
                       + 0.25 * k2 * trA * trB)
    return sq * F


def geo_angles(P, tri, m, n, g):
    """Real Lorentzian dihedral data at hinge tri of a simplex with real vertex coords P: projected rays u_m,u_n."""
    h = np.array([P[tri[1]] - P[tri[0]], P[tri[2]] - P[tri[0]]]); Gh = h @ g @ h.T; Ghi = np.linalg.inv(Gh)
    def proj(x): x = x - P[tri[0]]; return x - (Ghi @ (h @ g @ x)) @ h
    u, w = proj(P[m]), proj(P[n]); uu, ww, uw = u @ g @ u, w @ g @ w, u @ g @ w
    return uu, ww, uw


def gamma_sign_invariant(res, resp):
    """Gamma is a ratio of responses: numerator and denominator both reverse."""
    return np.allclose([r[1] for r in res], [r[1] for r in resp], rtol=1e-10, atol=1e-10)


def causal_hinge_fixture():
    """Exact scaled Gram for a tick-containing spacelike Kuhn triangle, alpha=3/5."""
    edges = np.array([[1, 0, 0, 1], [1, 1, 0, 1]], dtype=int)
    gram5 = edges @ np.diag([5, 5, 5, -3]) @ edges.T
    determinant25 = gram5[0, 0] * gram5[1, 1] - gram5[0, 1] * gram5[1, 0]
    return bool(np.all(edges[:, 3] != 0) and gram5[0, 0] > 0 and determinant25 > 0 and
                np.array_equal(gram5, np.array([[2, 2], [2, 7]])))


def main():
    check('(0) tick-containing Kuhn triangle has positive definite induced Gram [[.4,.4],[.4,1.4]]: spacelike, not timelike', causal_hinge_fixture())
    rng = np.random.default_rng(11)
    alpha = 0.6                                  # supplied light-cone slope (tick proper duration sqrt(alpha))
    gE = np.diag([1, 1, 1, alpha]).astype(float); gL = np.diag([1, 1, 1, -alpha]).astype(float)
    cars = {'Kuhn cubic': Carrier(*kuhn()), 'coned D4': Carrier(*d4cone())}
    for name, car in cars.items():
        _, _, _, _, Dh, dG = car.raw(gL.astype(complex)); car.continue_to(alpha, np.pi)
        tl = car.hinge_tl
        print(f'{name}: {car.E} edge classes, {len(car.hkeys)} hinge classes ({tl.sum()} timelike, {(~tl).sum()} spacelike); '
              f'min |D_hinge| = {np.min(abs(Dh)):.3f} at alpha = {alpha}')
        sdet = car.sdet / np.sqrt(abs(np.linalg.det(car.Gam)))
        check(f'(1) {name}: 600-point branch tracking: endpoint sqrt(det Gamma) = +i|.| and endpoint Schlaefli residual is small on every simplex',
              np.allclose(sdet, 1j, atol=1e-9) and car.schlaefli() < 1e-9, f'max rel Schlaefli residual {car.schlaefli():.1e}')
        # timelike hinges: A = +i|A|, dtheta real and equal to the derivative of the real rotation angle
        A_tl = car.A[tl]; okA = np.allclose(A_tl.real, 0, atol=1e-12) and np.all(A_tl.imag > 0)
        okS = np.allclose(car.A[~tl].imag, 0, atol=1e-12) and np.all(car.A[~tl].real > 0)
        errs, signs = [], {}
        for si in range(len(car.sims)):
            P = car.P[si]
            for ti, tri in enumerate(TRIS5):
                m, n = [i for i in range(5) if i not in tri]; dx = 1e-5 * rng.standard_normal((5, 4))
                sq = lambda Q: np.array([(Q[j] - Q[i]) @ gL @ (Q[j] - Q[i]) for i, j in PAIRS5])
                pred = car.dth[si, ti] @ (sq(P + dx) - sq(P - dx))          # central difference
                uu0, ww0, uw0 = geo_angles(P - dx, tri, m, n, gL); uu1, ww1, uw1 = geo_angles(P + dx, tri, m, n, gL)
                Ph = P[list(tri)]; hl = np.real(np.linalg.det(np.array([Ph[1] - Ph[0], Ph[2] - Ph[0]]) @ gL @ np.array([Ph[1] - Ph[0], Ph[2] - Ph[0]]).T)) < 0
                if hl:
                    th = lambda uu, ww, uw: np.arccos(uw / np.sqrt(uu * ww))
                    errs.append(abs(pred - (th(uu1, ww1, uw1) - th(uu0, ww0, uw0))) / max(abs(pred), 1e-12))
                else:
                    c0, c1 = uw0 / np.sqrt(abs(uu0 * ww0)), uw1 / np.sqrt(abs(uu1 * ww1))
                    if uu0 * ww0 > 0:   # same causal type: |c| = cosh eta
                        eta = lambda c: np.arccosh(abs(c)); typ = ('both timelike' if uu0 < 0 else 'both spacelike') + (', same cone' if c0 * (1 if uu0 > 0 else -1) > 0 else ', opposite')
                    else:
                        eta = lambda c: np.arcsinh(c); typ = 'mixed (crosses a null ray)'
                    de = eta(c1) - eta(c0)
                    if abs(de) > 1e-9:
                        r = (pred / 1j).real / de; signs.setdefault(typ, set()).add(int(np.sign(r)) if abs(abs(r) - 1) < 1e-3 else 99)
                        if abs((pred / 1j).imag) > 1e-3 * abs(de): signs[typ].add(98)
        check(f'(1) {name}: endpoint timelike-hinge area and sampled angle-derivative comparisons; endpoint spacelike areas are real',
              okA and okS and max(errs) < 1e-6, f'max rel err {max(errs):.1e} over {len(errs)} wedges')
        print(f'    spacelike-hinge wedges: d theta/i = s * d eta, s by wedge type: ' + '; '.join(f'{k}: {sorted(v)}' for k, v in signs.items()))
        check(f'(1) {name}: sampled endpoint spacelike-hinge derivatives dtheta = i s deta have one observed sign per wedge type', all(len(v) == 1 and list(v)[0] in (1, -1) for v in signs.values()))
        car.signs = signs

    # (2) Continued quadratic kernel / i versus supplied EH/2 quadratic comparator, finite samples
    for name, car in cars.items():
        rows = []; imag = 0.0; parts = []
        for trial in range(4):
            kd = rng.standard_normal(4); kd /= np.linalg.norm(kd); H = rng.standard_normal(10); r = []
            for s in (0.04, 0.02):
                KL = car.K(s * kd)[0] / 1j; FL = Fcont(s * kd, gL, 1j * np.sqrt(alpha)) / 1j
                imag = max(imag, abs((H @ KL @ H).imag) / abs(H @ KL @ H)); r.append((H @ KL @ H).real / (H @ FL @ H).real)
            rows.append((4 * r[1] - r[0]) / 3)
            ku = np.linalg.inv(gL) @ (s * kd); parts.append('timelike k' if (s * kd) @ ku < 0 else 'spacelike k')
        check(f'(2) {name}: four seeded quadratic-form Richardson ratios at scales .04/.02 agree with supplied EH/2 comparator within 2e-3; sampled imaginary parts below 1e-9',
              max(abs(np.array(rows) - 1)) < 2e-3 and imag < 1e-9, ', '.join(f'{x:.5f} ({p})' for x, p in zip(rows, parts)) + f'; Im/Re < {imag:.0e}')
    # Finite direction-comparison and flipped-spacelike-part diagnostic
    for name, build in (('Kuhn cubic', kuhn), ('coned D4', d4cone)):
        car = cars[name]; cm = Carrier(*build()); cm.continue_to(alpha, -np.pi)
        kd = rng.standard_normal(4); kd /= np.linalg.norm(kd); kk = 0.03 * kd; H = rng.standard_normal(10)
        Kp, Km = car.K(kk)[0] / 1j, cm.K(kk)[0] / (-1j)
        tl = car.hinge_tl; Kt, Ks = car.K(kk, sel=tl)[0] / 1j, car.K(kk, sel=~tl)[0] / 1j
        FL = (Fcont(kk, gL, 1j * np.sqrt(alpha)) / 1j).real
        flip = (H @ (Kt - Ks) @ H).real / (H @ FL @ H)
        check(f'(2) {name}: at one sampled momentum, opposite continuation directions agree after division by +/-i; flipped spacelike part changes the comparator ratio',
              np.max(abs(Kp - Km)) < 1e-10 * np.max(abs(Kp)) and abs(flip - 1) > 0.1,
              f'max|K(+pi) - K(-pi)| = {np.max(abs(Kp - Km)):.1e}; flipped-boost ratio {flip:.3f}')
    # Euclidean sanity at the same alpha
    carE = Carrier(*kuhn()); carE.continue_to(alpha, 0.0, n=2)
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); H = rng.standard_normal(10)
    rE = [(H @ carE.K(s * kd)[0] @ H).real / (H @ Fcont(s * kd, gE, np.sqrt(alpha)) @ H).real for s in (0.04, 0.02)]
    check('(2) Kuhn cubic, Euclidean diag(1,1,1,alpha): sampled Richardson ratio at .04/.02 agrees with supplied Euclidean comparator within 2e-3', abs((4 * rE[1] - rE[0]) / 3 - 1) < 2e-3, f'{(4 * rE[1] - rE[0]) / 3:.5f}')

    # (3) Supplied source/action convention S_total=-sigma*kappa*S_L-E int dtau, P=-S, E=kappa=1.
    # These choices are not supplied by the axioms or the candidate-law register.
    kappa = 1.0; e = np.zeros(10); e[T] = 1.0
    P3 = lambda kv: np.eye(3) - np.outer(kv, kv) / (kv @ kv)
    for name, car in cars.items():
        out = {}
        for sigma in (-1, +1):
            kgrav = -sigma * kappa
            res = []
            for kd in (np.array([1, 0, 0, 0.]), np.array([1, 1, 0, 0.]) / np.sqrt(2), np.array([1, 1, 1, 0.]) / np.sqrt(3)):
                kk = 0.02 * kd; KL = np.real(car.K(kk)[0] / 1j)
                J = e / np.sqrt(alpha)                     # S_m = -E sqrt(alpha - h_tt) per tick -> linear term (1/2) h_tt E/sqrt(alpha)
                h = -np.linalg.pinv(kgrav * KL, rcond=1e-8, hermitian=True) @ J / 2
                Hm = np.zeros((4, 4))
                for j, (a, b) in enumerate(HC): Hm[a, b] = Hm[b, a] = h[j]
                h00 = Hm[3, 3] / alpha                     # physical time t' = sqrt(alpha) t
                gam = np.trace(P3(kk[:3]) @ Hm[:3, :3]) / (2 * h00)
                res.append((h00 * (kk @ kk), gam))
            # TT wave h_xy, k = (0,0,kz, omega): kinetic sign of S_total = kgrav * S_L
            Ht = np.zeros(10); Ht[4] = 1.0; kz = 0.02
            kin = []
            for om in (0.0, 0.5 * np.sqrt(alpha) * kz, np.sqrt(alpha) * kz, 1.5 * np.sqrt(alpha) * kz):
                kin.append(kgrav * np.real(Ht @ car.K(np.array([0, 0, kz, om]))[0] @ Ht / 1j))
            out[sigma] = (res, kin)
        (res, kin), (resp, kinp) = out[-1], out[+1]
        c = [r[0] for r in res]; gm = [r[1] for r in res]
        check(f'(3) {name}, sigma = -1 (geometry RETARDS the phase by kappa S_L): supplied metric/source reading gives static h_00 k^2 near +E/kappa in three sampled directions (E=kappa=1)',
              max(abs(np.array(c) - 1)) < 3e-3, ', '.join(f'{x:.5f}' for x in c))
        check(f'(3) {name}, sigma = -1: sampled transverse metric ratio gamma = P_ij h_ij / (2 h_00) is near 1; no light trajectory calculated',
              max(abs(np.array(gm) - 1)) < 3e-3, ', '.join(f'{x:.5f}' for x in gm))
        w = np.array(kin)
        check(f'(3) {name}, sigma = -1: four sampled TT quadratic values increase initially with omega and are near zero at omega=sqrt(alpha)k',
              w[1] > w[0] and w[3] > 0 > w[0] and abs(w[2]) < 1e-3 * abs(w[0]), 'S at omega/(sqrt(alpha)k) = 0, .5, 1, 1.5: ' + ', '.join(f'{x:+.3e}' for x in w))
        cp = [r[0] for r in resp]
        check(f'(3) {name}: gamma is invariant under sigma reversal (both response components reverse)',
              gamma_sign_invariant(res, resp), 'sigma -1: ' + ', '.join(f'{r[1]:.5f}' for r in res) + '; sigma +1: ' + ', '.join(f'{r[1]:.5f}' for r in resp))
        print('    sigma +1 static coefficients: ' + ', '.join(f'{x:.5f}' for x in cp) + '; TT values: ' + ', '.join(f'{x:+.3e}' for x in kinp))
        check(f'(3) {name}, sigma = +1 (geometry ADVANCES the phase by kappa S_L): static h_00 < 0 and sampled TT quadratic value at 1.5 sqrt(alpha)k is negative under supplied conventions',
              max(cp) < 0 and kinp[3] < 0, f'h_00 k^2 = {cp[0]:.5f}; S_TT(1.5) = {kinp[3]:+.3e}')

    # (4) static coefficient in position space, coned D4, sigma = -1, kappa = 1
    car = cars['coned D4']; L = 20
    gq = 2 * np.pi * np.fft.fftfreq(L); kx, ky, kz = np.meshgrid(gq, gq, gq, indexing='ij')
    ks = np.stack([kx.ravel(), ky.ravel(), kz.ravel(), np.zeros(kx.size)], 1); hk = np.zeros(len(ks)); hc = np.zeros(len(ks))
    for s0 in range(0, len(ks), 700):
        kk = ks[s0:s0 + 700]; KL = np.real(car.K(kk) / 1j); nz = np.linalg.norm(kk, axis=1) > 1e-12
        sol = np.einsum('kij,j->ki', np.linalg.pinv(KL[nz], rcond=1e-7, hermitian=True), e / np.sqrt(alpha))
        hk[s0:s0 + 700][nz] = -0.5 * sol[:, T] / alpha
        hc[s0:s0 + 700][nz] = 1.0 / np.sum(4 * np.sin(kk[nz, :3] / 2) ** 2, axis=1)
    hx = np.real(np.fft.ifftn(hk.reshape(L, L, L))); gx = np.real(np.fft.ifftn(hc.reshape(L, L, L)))
    x = np.minimum(np.arange(L), L - np.arange(L)); X3 = np.sqrt(x[:, None, None] ** 2 + x[None, :, None] ** 2 + x[None, None, :] ** 2)
    msk = (X3 >= 4) & (X3 <= 8); Am = np.stack([8 * np.pi * gx[msk], np.ones(msk.sum())], 1)
    co, *_ = np.linalg.lstsq(Am, hx[msk], rcond=None); q = np.sqrt(np.mean((hx[msk] - Am @ co) ** 2)) / np.std(hx[msk])
    check(f'(4) coned D4, Lorentzian, sigma = -1: position-space h_00 on a {L}^3 torus fits 8 pi G E G_lat(r) + const over 4 <= r <= 8 with G = 1/(8 pi) = {1 / (8 * np.pi):.5f} within 3%',
          abs(co[0] * 8 * np.pi - 1) < 0.03 and q < 0.05 and co[0] > 0, f'G = {co[0]:.5f}, relative residual {q:.3f}')

    # (5) Three alternative alpha samples only; no null-step limiting theorem
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); H = np.random.default_rng(3).standard_normal(10)
    for name, build in (('Kuhn cubic', kuhn), ('coned D4', d4cone)):
        rows = []
        for al in (1.7, 0.99, 0.999):
            c = Carrier(*build()); c.continue_to(al, np.pi); g = np.diag([1, 1, 1, -al])
            r = [(H @ (c.K(s * kd)[0] / 1j) @ H).real / (H @ (Fcont(s * kd, g, 1j * np.sqrt(al)) / 1j) @ H).real for s in (0.04, 0.02)]
            big = max(np.max(abs(c.dA)), 0.0) * max(np.max(abs(c.dth)), 0.0)
            rows.append((al, (4 * r[1] - r[0]) / 3, np.min(abs(c.A)), big))
        check(f'(5) {name}: finite Richardson ratios at alpha = 1.7, .99, .999 agree within 3e-3; coefficient growth recorded, no alpha->1 conclusion',
              all(abs(x[1] - 1) < 3e-3 for x in rows), '; '.join(f'alpha {a}: ratio {q:.5f}, min|A| {m:.2e}, max|dA||dtheta| {b:.1e}' for a, q, m, b in rows))

    print('supplied: carriers, flat lengths, tick index 3, alpha=.6, branch direction, metric/source reading, P=-S, S_total=-sigma*kappa*S_L-E integral d tau with E,kappa>0; torus, radii and rcond. The declared D4 helper is contextual only and is not executed.')
    print('scope: finite endpoint derivative and quadratic diagnostics only; full real nonlinear action, continuum matching and null limit remain open. Attraction comparison favors sigma=-1 only under supplied source/action choices; gamma does not reverse. G=a^2/(8*pi*kappa) additionally requires continuum EH/2 matching, not proved here.')
    print('elapsed_seconds', round(time.monotonic() - _T0, 1))
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
