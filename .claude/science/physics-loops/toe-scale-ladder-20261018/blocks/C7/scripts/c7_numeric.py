#!/usr/bin/env python3
"""C7 numerical part. This is a different implementation path from c7_exact.py. It builds
explicit 4x4 matrices, applies the mass as M U0 M with matrix exponentials, takes
matrix logarithms by eigendecomposition and powers by repeated multiplication.

Everything here is numerical evidence and is labelled so. The expected constants
(s, |W| = s sqrt(1-s^2), the TRIM cosines, alpha, beta) come from the analytic
formulas in NOTE.md. They are not tuned here. Only C3 (the remainder
constant) is measured; it is reported and not asserted.
"""
from __future__ import annotations

import itertools
import sys

import numpy as np
from scipy.linalg import expm, schur
import mpmath as mp

PASS = FAIL = 0


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS [numerical] {name}")
    else:
        FAIL += 1
        print(f"FAIL [numerical] {name}")


I2 = np.eye(2); t1 = np.array([[0, 1], [1, 0]], complex); t2 = np.array([[0, -1j], [1j, 0]]); t3 = np.diag([1.0, -1.0]).astype(complex)
TAU = [np.kron(t1, I2), np.kron(t2, I2)]
TS = [np.kron(t3, x) for x in (t1, t2, t3)]
ALPHA = [-x for x in TS]


def Gmat(b0, b1, b2):
    return np.array([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
                     [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
                     [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
                     [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])


def phi(k):
    c = np.cos(k)
    return np.array([1.0, c.sum(), c[0]*c[1] + c[0]*c[2] + c[1]*c[2], c.prod()])


def gvec(b, k):
    c, s = np.cos(k), np.sin(k)
    return np.array([s[i]*(b[0] + b[1]*(c[(i+1) % 3] + c[(i+2) % 3]) + b[2]*c[(i+1) % 3]*c[(i+2) % 3]) for i in range(3)])


phi0 = np.array([1.0, 3, 3, 1]); wv = np.array([0.0, 1, 2, 1])


class Walk:
    def __init__(self, b, name):
        self.b = np.array(b, float); self.name = name
        G = Gmat(*self.b)
        ev, V = np.linalg.eigh(G)
        keep = ev > 1e-13
        F = (V[:, keep]*np.sqrt(ev[keep])).T
        if F.shape[0] < 3:
            F = np.vstack([F, np.zeros((3 - F.shape[0], 4))])
        e = F @ phi0
        Q = np.linalg.qr(np.column_stack([e, np.eye(3)]))[0][:, :3]
        if Q[:, 0] @ e < 0:
            Q[:, 0] *= -1
        F = Q.T @ F
        W = F[1:] @ wv
        if np.linalg.norm(W) > 1e-12:          # rotate the h-plane so that W lies on h1
            ang = np.arctan2(W[1], W[0])
            R = np.array([[np.cos(ang), np.sin(ang)], [-np.sin(ang), np.cos(ang)]])
            F[1:] = R @ F[1:]
        self.F = F
        self.Wvec = F[1:] @ wv
        self.s = self.b[0] + 2*self.b[1] + self.b[2]

    def U0(self, k):
        f, h1, h2 = self.F @ phi(k)
        g = gvec(self.b, k)
        return f*np.eye(4) + 1j*(h1*TAU[0] + h2*TAU[1] + sum(g[i]*TS[i] for i in range(3)))

    def U(self, k, th, chi):
        Mm = expm(0.5j*th*(np.cos(chi)*TAU[0] + np.sin(chi)*TAU[1]))
        return Mm @ self.U0(k) @ Mm


def logH(Um, a):
    """(i/a) Log U, principal branch, via complex Schur form (diagonal for normal U)."""
    T, Z = schur(Um, output='complex')
    lam = np.diag(T)
    return (1j/a) * (Z @ np.diag(np.log(lam/np.abs(lam))) @ Z.conj().T)


def HD(p, m, s, chi):
    beta = -(np.cos(chi)*TAU[0] + np.sin(chi)*TAU[1])
    return s*sum(p[i]*ALPHA[i] for i in range(3)) + m*beta


def opn(A):
    return np.linalg.norm(A, 2)


# ---------------------------------------------------------------- parameter points
co = [259200000000, -453744000000, 12644840000, 1185396800, -39225499]
ustar = min(r.real for r in np.roots(co) if abs(r.imag) < 1e-12 and r.real > 0)
r5, r6, r15 = np.sqrt(5), np.sqrt(6), np.sqrt(15)
walks = [Walk((11/30, np.sqrt(ustar), 3/20), 'bstar'),
         Walk(((r6 + 2*r15)/27, (5*r6 - 2*r15)/27, (2*r15 - 2*r6)/27), 'iso'),
         Walk(((9*r5 - 5)/38, (5*r5 - 7)/19, (71 - 29*r5)/38), 'gold')]
TRIM = [np.array(K)*np.pi for K in itertools.product((0, 1), repeat=3)]
rng = np.random.default_rng(7)

for Wk in walks:
    print(f"--- {Wk.name}: b = {Wk.b}, s = {Wk.s:.10f}, |W| = {np.linalg.norm(Wk.Wvec):.10f}")
    check(f'{Wk.name}: |W| = s sqrt(1-s^2)', abs(np.linalg.norm(Wk.Wvec) - abs(Wk.s)*np.sqrt(max(0, 1 - Wk.s**2))) < 1e-7)
    Ks = rng.uniform(-np.pi, np.pi, (300, 3))
    err = max(opn(Wk.U(k, 0.2, 0.7) @ Wk.U(k, 0.2, 0.7).conj().T - np.eye(4)) for k in Ks)
    check(f'{Wk.name}: massive member M U0 M unitary (theta=0.2, chi=0.7), max err {err:.1e}', err < 1e-12)
    # covariance under the cubic C4 about z: k -> R k, W = 1 (x) exp(-i pi sigma3/4)
    Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); Dz = np.kron(I2, expm(-0.25j*np.pi*t3))
    cov = max(opn(Wk.U(Rz @ k, 0.2, 0.7) - Dz @ Wk.U(k, 0.2, 0.7) @ Dz.conj().T) for k in Ks[:50])
    check(f'{Wk.name}: massive member is cubic covariant (C4z), err {cov:.1e}', cov < 1e-12)

    # quasienergy table at TRIMs, massless and massive
    for th, chi in ((0.0, 0.0), (0.1, 0.0), (0.1, np.pi/2)):
        qe = [np.max(np.abs(np.angle(np.linalg.eigvals(Wk.U(K, th, chi))))) for K in TRIM]
        print(f"   theta={th}, chi={chi:.3f}: TRIM quasienergies |omega| = {np.round(qe, 6)}")
    th = 0.1
    q0 = [np.max(np.abs(np.angle(np.linalg.eigvals(Wk.U(K, 0, 0))))) for K in TRIM]
    ok = True
    for chi in np.linspace(0, np.pi, 7):
        qt = [np.max(np.abs(np.angle(np.linalg.eigvals(Wk.U(K, th, chi))))) for K in TRIM]
        ok &= all(abs(x - y) <= th + 1e-12 for x, y in zip(qt, q0))
    check(f'{Wk.name}: |omega_K(theta) - theta_K| <= theta at all TRIMs (theta=0.1, 7 twist angles)', ok)
    if Wk.name == 'gold':
        dX = max(abs(np.max(np.abs(np.angle(np.linalg.eigvals(Wk.U(np.array([np.pi, 0, 0]), th, chi))))) - (np.pi - th))
                 for th in (0.05, 0.1, 0.3) for chi in (0, 1.0, np.pi/2))
        check(f'gold: massive axis doubler sits at quasienergy pi - theta exactly (U(X) = -U(0)), err {dX:.1e}', dX < 1e-10)

    # vertex-lemma bound and the global minimum at the TRIMs (sampled sanity check; the lemma itself is exact)
    for th, chi in ((0.0, 0.0), (0.1, 0.0), (0.1, np.pi/2)):
        fK = [np.real(np.trace(Wk.U(K, th, chi)))/4 for K in TRIM]
        cth = min((np.cos(th) - fK[i])/(2*np.count_nonzero(TRIM[i])) for i in range(1, 8))
        Kr = rng.uniform(-np.pi, np.pi, (4000, 3))
        lhs = np.array([1 - np.real(np.trace(Wk.U(k, th, chi)))/4 for k in Kr])
        rhs = (1 - np.cos(th)) + cth*np.array([np.sum(1 - np.cos(k)) for k in Kr])
        check(f'{Wk.name}: theta={th}, chi={chi:.2f}: 1 - cos omega >= (1 - cos theta) + c_theta sum(1 - cos k_a), c_theta = {cth:.4f} (4000 random k)',
              np.all(lhs >= rhs - 1e-12) and cth > 0)
        fpi = 1 + np.array([np.real(np.trace(Wk.U(k, th, chi)))/4 for k in Kr])
        print(f"   min over samples of 1 + cos omega = {fpi.min():.4e}; min over TRIMs = {min(1 + x for x in fK):.4e}")
        check(f'{Wk.name}: theta={th}, chi={chi:.2f}: sampled min of 1 + cos omega >= its TRIM minimum',
              fpi.min() >= min(1 + x for x in fK) - 1e-12)

# ---------------------------------------------------------------- fiber Hamiltonian and convergence
m, t, Pmax = 1.0, 1.0, 2.0
dirs = rng.normal(size=(40, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
psamp = [r*d for d in dirs for r in (0.5, 1.0, 2.0)]
alist = [0.04, 0.02, 0.01, 0.005]
for Wk in walks:
    for chi in (0.0, np.pi/2):
        Wt = Wk.Wvec[0]*TAU[0] + Wk.Wvec[1]*TAU[1]
        C3 = []
        errs, errsV = [], []
        for a in alist:
            r3, e1, e2 = 0.0, 0.0, 0.0
            n = int(round(t/a))
            for p in psamp:
                Um = Wk.U(a*p, m*a, chi)
                Ha = logH(Um, a)
                Hd = HD(p, m, Wk.s, chi)
                lead = Hd + 0.5*a*(p @ p)*Wt
                r3 = max(r3, opn(Ha - lead)/(a**2*(np.linalg.norm(p) + m)**3))
                Un = np.linalg.matrix_power(Um, n)
                E = expm(-1j*t*Hd)
                e1 = max(e1, opn(Un - E))
                # momentum-dependent chiral rotation (maximal twist only removes the O(a) term)
                eps_ = 0.5*a*(p @ p)*np.linalg.norm(Wk.Wvec)
                beta = -(np.cos(chi)*TAU[0] + np.sin(chi)*TAU[1])
                Gp = -(np.cos(chi + np.pi/2)*TAU[0] + np.sin(chi + np.pi/2)*TAU[1])  # perp flavour direction
                sgn = np.sign(np.real(np.trace(Wt @ Gp))) or 1.0
                ph = np.arctan(eps_/m)
                Vr = np.cos(ph/2)*np.eye(4) + sgn*np.sin(ph/2)*beta @ Gp
                e2 = max(e2, opn(Vr @ Un @ Vr.conj().T - E))
            C3.append(r3); errs.append(e1); errsV.append(e2)
        sl = np.polyfit(np.log(alist), np.log(errs), 1)[0]
        slV = np.polyfit(np.log(alist), np.log(errsV), 1)[0]
        print(f"   {Wk.name} chi={chi:.3f}: max_p ||U^n - e^(-itH_D)|| = {np.array(errs)} slope {sl:.3f}; "
              f"with p-dependent chiral rotation: {np.array(errsV)} slope {slV:.3f}; C3 estimates {np.round(C3, 4)}")
        check(f'{Wk.name} chi={chi:.2f}: remainder ||H_a - H_D - (a/2)p^2 W.tau|| / (a^2(|p|+m)^3) stays bounded as a -> 0 (max {max(C3):.3f})',
              max(C3) < 5 and C3[-1] <= 1.2*C3[0] + 1e-3)
        bound = [alist[i]*0 + t*(0.5*alist[i]*np.linalg.norm(Wk.Wvec)*Pmax**2 + max(C3)*alist[i]**2*(Pmax + m)**3) for i in range(len(alist))]
        check(f'{Wk.name} chi={chi:.2f}: error <= t(|W| a P^2/2 + C3 a^2 (P+m)^3) (t multiple of a, floor term zero)',
              all(e <= bb*1.0001 + 1e-12 for e, bb in zip(errs, bound)))
        if Wk.name == 'gold':
            check(f'gold chi={chi:.2f}: |W| = 0, convergence is O(a^2) (slope {sl:.2f})', sl > 1.8)
        elif chi == 0.0:
            check(f'{Wk.name} chi=0 (Wilson-aligned mass): convergence is O(a) (slope {sl:.2f}) and the chiral rotation does not help (slope {slV:.2f})',
                  0.85 < sl < 1.2 and slV < 1.3)
        else:
            check(f'{Wk.name} chi=pi/2 (maximal twist): constant identification O(a) (slope {sl:.2f}); p-dependent chiral rotation V_a(p) gives O(a^2) (slope {slV:.2f})',
                  0.85 < sl < 1.2 and slV > 1.8)

# floor term: t not a multiple of a
Wk = walks[0]
a = 0.01; tt = 1.0 + 0.6*a; n = int(np.floor(tt/a))
p = np.array([0.3, 0.2, 0.1])
fe = opn(np.linalg.matrix_power(Wk.U(a*p, m*a, 0.0), n) - expm(-1j*tt*HD(p, m, Wk.s, 0.0)))
print(f"   floor-term example: a={a}, t={tt}: error {fe:.4e} vs a*E = {a*np.sqrt(m**2 + Wk.s**2*p@p):.4e}")
check('floor term: with t/a non-integer the error includes (t - na) E <= a E (example within bound)',
      fe <= a*np.sqrt(m**2 + Wk.s**2*p @ p)*0.61 + t*(0.5*a*np.linalg.norm(Wk.Wvec)*(p @ p) + 3*a**2) + 1e-12)

# ---------------------------------------------------------------- dispersion coefficients (numerical fits)
print('--- massive dispersion: E_a^2 a^2 = omega^2 fitted in eps for (k, theta) = eps (n, mu)')
for Wk in walks:
    b0, b1, b2 = Wk.b; s = Wk.s
    alpha = s*(s**3 + 3*b0 - 6*b1 - 9*b2)/12; beta = -s*(b0 - b1 - 2*b2)/3
    Wn = np.linalg.norm(Wk.Wvec)
    for chi in (0.0, np.pi/2, 1.0):
        ok = True
        for nd in (np.array([1.0, 0, 0]), np.array([1.0, 1, 0])/np.sqrt(2), np.array([1.0, 1, 1])/np.sqrt(3), np.array([0.3, -0.5, 0.81])):
            mu = 0.7
            nd = nd/np.linalg.norm(nd)
            pred = lambda e: (mu**2 + s**2)*e**2 - mu*Wn*np.cos(chi)*e**3 + (alpha + beta*np.sum(nd**4) - s**2*mu**2/3)*e**4
            # exact omega from the matrix, mpmath-free: residual should scale as e^5
            res = []
            for e in (0.02, 0.01):
                om = np.max(np.abs(np.angle(np.linalg.eigvals(Wk.U(e*nd, e*mu, chi)))))
                res.append(abs(om**2 - pred(e)))
            slope = np.log(res[0]/res[1])/np.log(2)
            ok &= slope > 4.5
        check(f'{Wk.name} chi={chi:.2f}: omega^2 = theta^2 + s^2 k^2 - theta |W| cos(chi) k^2 + alpha|k|^4 + beta sum k^4 - (s^2/3) theta^2 k^2 + O(eps^5) along 4 directions', ok)

# ---------------------------------------------------------------- parent sextic coefficient (b_iso, axis direction)
mp.mp.dps = 60
s6, s15 = mp.sqrt(6), mp.sqrt(15)
bi = [(s6 + 2*s15)/27, (5*s6 - 2*s15)/27, (2*s15 - 2*s6)/27]


def Gmp(b0, b1, b2):
    return mp.matrix([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
                      [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
                      [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
                      [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])


Gi = Gmp(*bi); av = Gi*mp.matrix([1, 3, 3, 1])


def om2(kv):
    cc = [mp.cos(x) for x in kv]
    ph = [1, sum(cc), cc[0]*cc[1] + cc[0]*cc[2] + cc[1]*cc[2], cc[0]*cc[1]*cc[2]]
    f = sum(av[i]*ph[i] for i in range(4))
    return mp.acos(f)**2


for nd, label in (((1, 0, 0), 'axis'), ((1, 1, 1), 'diag')):
    nd = [mp.mpf(x)/mp.sqrt(sum(y*y for y in nd)) for x in nd]
    N4 = sum(x**4 for x in nd); P222 = nd[0]**2*nd[1]**2*nd[2]**2
    kk = mp.mpf('1e-6')
    c6 = (om2([kk*x for x in nd]) - mp.mpf(2)/3*kk**2 + kk**4/54)/kk**6
    z = mp.sqrt(10)/9 - mp.mpf(16)/45
    parent = mp.mpf(1)/243 - N4/540 + z*P222
    corrected = mp.mpf(1)/1215 - N4/540 + z*P222
    print(f"   b_iso sextic coefficient along {label}: measured {mp.nstr(c6, 12)}, parent formula {mp.nstr(parent, 12)}, "
          f"with |k|^6 coefficient 1/1215 {mp.nstr(corrected, 12)}")
    check(f'b_iso {label}: the omega^2 sextic coefficient matches |k|^6 coefficient 1/1215 (not the parent 1/243)',
          abs(c6 - corrected) < 1e-6 and abs(c6 - parent) > 1e-4)

# ---------------------------------------------------------------- Poincare defects
print('--- Poincare defects on |p| <= 2, m = 1')
for Wk in walks:
    for chi in (0.0, np.pi/2):
        d1s, d0s, drs = [], [], []
        for a in (0.02, 0.01, 0.005):
            d1 = d0 = dr = 0.0
            hstep = 1e-4
            for p in psamp[:60]:
                Hp = lambda q: logH(Wk.U(a*q, m*a, chi), a)
                E2 = lambda q: np.real(np.trace(Hp(q) @ Hp(q)))/4
                dE2 = np.array([(E2(p + hstep*np.eye(3)[j]) - E2(p - hstep*np.eye(3)[j]))/(2*hstep) for j in range(3)])
                d1 = max(d1, np.linalg.norm(0.5*dE2 - Wk.s**2*p))
                dH = [(Hp(p + hstep*np.eye(3)[j]) - Hp(p - hstep*np.eye(3)[j]))/(2*hstep) for j in range(3)]
                comm = dH[0] @ dH[1] - dH[1] @ dH[0]
                commD = Wk.s**2*(ALPHA[0] @ ALPHA[1] - ALPHA[1] @ ALPHA[0])
                d0 = max(d0, opn(comm - commD)/4)
                # continuous rotation by 0.3 rad about z: H_a(Rp) vs D H_a(p) D^dagger
                ang = 0.3
                Rm = np.array([[np.cos(ang), -np.sin(ang), 0], [np.sin(ang), np.cos(ang), 0], [0, 0, 1]])
                Dm = np.kron(I2, expm(-0.5j*ang*t3))
                dr = max(dr, opn(Hp(Rm @ p) - Dm @ Hp(p) @ Dm.conj().T))
            d1s.append(d1); d0s.append(d0); drs.append(dr)
        sl = lambda v: np.polyfit(np.log([0.02, 0.01, 0.005]), np.log(np.maximum(v, 1e-300)), 1)[0]
        print(f"   {Wk.name} chi={chi:.2f}: |1/2 grad E_a^2 - s^2 p| {np.array(d1s)} (slope {sl(d1s):.2f}); "
              f"(1/4)||[d1H,d2H] - continuum|| {np.array(d0s)} (slope {sl(d0s):.2f}); rotation defect {np.array(drs)} (slope {sl(drs):.2f})")
        if Wk.name != 'gold':
            exp1 = 2.0 if chi == np.pi/2 else 1.0
            check(f'{Wk.name} chi={chi:.2f}: [K,H] defect scales as a^{exp1:.0f} (slope {sl(d1s):.2f}); [K1,K2] spin-part defect O(a) (slope {sl(d0s):.2f}); continuous-rotation defect O(a^2) (slope {sl(drs):.2f})',
                  abs(sl(d1s) - exp1) < 0.25 and abs(sl(d0s) - 1) < 0.25 and abs(sl(drs) - 2) < 0.25)
        else:
            check(f'gold chi={chi:.2f}: all three defects O(a^2) (slopes {sl(d1s):.2f}, {sl(d0s):.2f}, {sl(drs):.2f})',
                  min(sl(d1s), sl(d0s), sl(drs)) > 1.75)

# ---------------------------------------------------------------- Gaussian doubler overlap (1D factor)
from scipy.special import erfc
print('--- Gaussian packet: lattice-momentum weight at |k_a| >= pi/2 (1D factor), FFT vs erfc')
for Sa in (1.0, 1.5, 2.0):
    N = 4096
    x = np.arange(N) - N//2
    psi = np.exp(-x**2/(4*Sa**2)); psi /= np.linalg.norm(psi)
    pk = np.abs(np.fft.fft(psi))**2; pk /= pk.sum()
    kk = 2*np.pi*np.fft.fftfreq(N)
    w = pk[np.abs(kk) >= np.pi/2].sum()
    pred = erfc(np.pi/2*np.sqrt(2)*Sa)
    print(f"   Sigma/a = {Sa}: weight {w:.3e}, erfc(kappa sqrt2 Sigma/a) = {pred:.3e}")
    check(f'Sigma/a={Sa}: doubler-region weight equals the Gaussian tail erfc(pi Sigma/(sqrt2 a)) to 5%',
          abs(w - pred) <= 0.05*pred + 1e-300)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
